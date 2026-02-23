#!/usr/bin/env python3
"""Generate an Amazon KDP-compliant paperback cover (back + spine + front).

Usage:
    python scripts/create_kdp_cover.py [--pages 64]

Reads back cover text from:  cover/back-cover-text.md
Reads front cover image from: cover/cover.jpg
Outputs PDF + preview to:     cover/

See cover/KDP-COVER-RULES.md for full spec reference.
"""

import argparse
import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
DPI = 300
TRIM_W = 6.0       # inches — front/back cover width
TRIM_H = 9.0       # inches — cover height
BLEED = 0.125       # inches — required bleed on each edge
SAFE_MARGIN = 0.375 # inches — keep important text inside this from trim edge

FONT_DIR = Path("C:/Windows/Fonts")
FONT_TITLE = FONT_DIR / "georgiab.ttf"   # Georgia Bold
FONT_BODY = FONT_DIR / "georgia.ttf"     # Georgia Regular
FONT_BODY_ITALIC = FONT_DIR / "georgiai.ttf"

WHITE = (255, 255, 255)
OFF_WHITE = (230, 230, 230)
SOFT_WHITE = (200, 200, 200)
BG_DARK = (20, 20, 20)
BLACK = (30, 30, 30)
DARK_GRAY = (60, 60, 60)


def inches(val):
    """Convert inches to pixels at target DPI."""
    return round(val * DPI)


def spine_width_inches(page_count: int) -> float:
    """KDP spine width for B&W interior on white paper."""
    return page_count * 0.002252


def wrap_text(draw, text, font, max_width):
    """Word-wrap text to fit within max_width pixels. Returns list of lines."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_justified_line(draw, x, y, words, font, max_width, fill):
    """Draw a single line of text with words spaced to fill max_width."""
    if len(words) == 1:
        draw.text((x, y), words[0], fill=fill, font=font)
        return

    # Measure total word width
    word_widths = []
    for w in words:
        bbox = draw.textbbox((0, 0), w, font=font)
        word_widths.append(bbox[2] - bbox[0])
    total_word_w = sum(word_widths)
    total_space = max_width - total_word_w
    gap = total_space / (len(words) - 1)

    cx = x
    for i, w in enumerate(words):
        draw.text((cx, y), w, fill=fill, font=font)
        cx += word_widths[i] + gap


def draw_justified_text(draw, x, y, text, font, max_width, fill, line_height):
    """Word-wrap and draw fully justified text. Last line of each paragraph
    is left-aligned. Returns the y position after the last line."""
    lines = wrap_text(draw, text, font, max_width)
    for i, line in enumerate(lines):
        words = line.split()
        is_last_line = (i == len(lines) - 1)
        if is_last_line or len(words) <= 1:
            # Left-align the last line
            draw.text((x, y), line, fill=fill, font=font)
        else:
            draw_justified_line(draw, x, y, words, font, max_width, fill)
        y += line_height
    return y


# ---------------------------------------------------------------------------
# Parse back-cover-text.md
# ---------------------------------------------------------------------------
def parse_back_cover_text(md_path: Path) -> dict:
    """Parse cover/back-cover-text.md into sections.

    Expected format:
        ## Tagline
        <paragraph>

        ## Description
        <paragraph 1>

        <paragraph 2>
        ...

        ## Quote
        <single paragraph>

    Returns dict with keys: tagline, description (list of paragraphs), quote.
    """
    text = md_path.read_text(encoding="utf-8")

    sections = {}
    current_section = None
    current_lines = []

    for line in text.splitlines():
        # Match ## headings
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            if current_section:
                sections[current_section] = "\n".join(current_lines).strip()
            current_section = m.group(1).strip().lower()
            current_lines = []
        elif current_section:
            current_lines.append(line)

    if current_section:
        sections[current_section] = "\n".join(current_lines).strip()

    # Split description into paragraphs (double newline separated)
    desc_raw = sections.get("description", "")
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", desc_raw) if p.strip()]

    return {
        "tagline": sections.get("tagline", ""),
        "description": paragraphs,
        "quote": sections.get("quote", "").strip('""\u201c\u201d'),
    }


# ---------------------------------------------------------------------------
# Cover generation
# ---------------------------------------------------------------------------
def create_cover(page_count: int, output_path: Path, front_cover_path: Path,
                 back_text_path: Path):
    spine_w = spine_width_inches(page_count)

    # Full cover dimensions with bleed
    total_w = BLEED + TRIM_W + spine_w + TRIM_W + BLEED
    total_h = BLEED + TRIM_H + BLEED

    pw = inches(total_w)
    ph = inches(total_h)

    print(f"Page count:     {page_count}")
    print(f"Spine width:    {spine_w:.4f}\" ({inches(spine_w)}px)")
    print(f"Total cover:    {total_w:.4f}\" x {total_h:.4f}\"")
    print(f"Pixel size:     {pw} x {ph} @ {DPI} DPI")
    print(f"Back text from: {back_text_path}")

    # Read back cover text
    back = parse_back_cover_text(back_text_path)

    # Create canvas — dark background (covers back + spine)
    cover = Image.new("RGB", (pw, ph), BG_DARK)
    draw = ImageDraw.Draw(cover)

    # Key x-coordinates (in pixels)
    bleed_px = inches(BLEED)
    back_right = bleed_px + inches(TRIM_W)
    spine_left = back_right
    spine_px = inches(spine_w)
    spine_right = spine_left + spine_px
    safe = inches(SAFE_MARGIN)

    # -----------------------------------------------------------------------
    # FRONT COVER — paste original cover.jpg
    # -----------------------------------------------------------------------
    front = Image.open(front_cover_path).convert("RGB")
    front_panel_w = inches(TRIM_W + BLEED)
    front_panel_h = ph
    front_resized = front.resize((front_panel_w, front_panel_h), Image.LANCZOS)
    cover.paste(front_resized, (spine_right, 0))

    # -----------------------------------------------------------------------
    # SPINE — dark background, no text (too narrow below ~130 pages)
    # -----------------------------------------------------------------------
    # See cover/KDP-COVER-RULES.md for spine text thresholds.

    # -----------------------------------------------------------------------
    # BACK COVER — dark background, white text, crab emoji
    # -----------------------------------------------------------------------
    # Load fonts — sizes in pixels, calibrated for 300 DPI print
    # Target ~11-12pt print = 46-50px at 300 DPI  (px = pt * 300/72)
    try:
        tagline_font = ImageFont.truetype(str(FONT_BODY_ITALIC), 48)
        desc_font = ImageFont.truetype(str(FONT_BODY), 46)
        quote_font = ImageFont.truetype(str(FONT_BODY_ITALIC), 42)
        barcode_font = ImageFont.truetype(str(FONT_BODY), 18)
    except OSError:
        tagline_font = desc_font = quote_font = barcode_font = \
            ImageFont.load_default()

    text_left = bleed_px + safe
    text_right = back_right - safe
    text_width = text_right - text_left

    # -- Emoji + tagline block (top of back cover) --
    emoji_size = inches(1.5)
    thumb_margin = inches(0.25)
    thumb_x = text_left
    thumb_y = bleed_px + safe

    # Render crab emoji
    try:
        emoji_font = ImageFont.truetype("C:/Windows/Fonts/seguiemj.ttf",
                                        emoji_size - 40)
    except OSError:
        emoji_font = ImageFont.load_default()
    draw.text((thumb_x, thumb_y), "\U0001F980",
              font=emoji_font, embedded_color=True)

    # Tagline next to emoji
    tagline_x = thumb_x + emoji_size + thumb_margin
    tagline_width = text_right - tagline_x
    ty = draw_justified_text(draw, tagline_x, thumb_y, back["tagline"],
                             tagline_font, tagline_width, OFF_WHITE, 62)

    # -- Main description paragraphs --
    y = max(ty, thumb_y + emoji_size) + inches(0.35)

    for para in back["description"]:
        y = draw_justified_text(draw, text_left, y, para,
                                desc_font, text_width, OFF_WHITE, 58)
        y += 24  # paragraph gap

    # -- Closing quote --
    y += inches(0.2)
    quote_text = f"\u201c{back['quote']}\u201d"
    y = draw_justified_text(draw, text_left + 20, y, quote_text,
                            quote_font, text_width - 40, SOFT_WHITE, 54)

    # -- Barcode area placeholder (bottom-right of back cover) --
    barcode_w = inches(2.0)
    barcode_h = inches(1.2)
    barcode_x = back_right - safe - barcode_w
    barcode_y = ph - bleed_px - safe - barcode_h
    draw.rectangle(
        [barcode_x, barcode_y, barcode_x + barcode_w, barcode_y + barcode_h],
        fill=(40, 40, 40),
        outline=DARK_GRAY,
        width=2,
    )
    draw.text(
        (barcode_x + 10, barcode_y + barcode_h // 2 - 10),
        "ISBN BARCODE AREA",
        fill=DARK_GRAY,
        font=barcode_font,
    )

    # -----------------------------------------------------------------------
    # Save as PDF and JPEG preview
    # -----------------------------------------------------------------------
    cover.save(str(output_path), "PDF", resolution=DPI)
    print(f"\nSaved: {output_path} ({output_path.stat().st_size / 1024:.0f} KB)")

    preview_path = output_path.with_name("cover-kdp-preview.jpg")
    preview = cover.resize((pw // 2, ph // 2), Image.LANCZOS)
    preview.save(str(preview_path), "JPEG", quality=90)
    print(f"Preview: {preview_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate KDP paperback cover")
    parser.add_argument("--pages", type=int, default=64,
                        help="Interior page count (default: 64)")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    front_cover = repo / "cover" / "cover.jpg"
    back_text = repo / "cover" / "back-cover-text.md"
    output = repo / "cover" / "cover-kdp-paperback.pdf"

    for f in (front_cover, back_text):
        if not f.exists():
            print(f"Error: {f} not found")
            return

    create_cover(args.pages, output, front_cover, back_text)


if __name__ == "__main__":
    main()
