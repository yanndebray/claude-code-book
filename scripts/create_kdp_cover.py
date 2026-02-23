#!/usr/bin/env python3
"""Generate an Amazon KDP-compliant paperback cover (back + spine + front).

Usage:
    python scripts/create_kdp_cover.py [--pages 120]

Produces a single PDF at 300 DPI with 0.125" bleed on all sides.
Trim size: 6" x 9" (standard trade paperback).
"""

import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
DPI = 300
TRIM_W = 6.0       # inches — front/back cover width
TRIM_H = 9.0       # inches — cover height
BLEED = 0.125       # inches — required bleed on each edge
SAFE_MARGIN = 0.25  # inches — keep important text inside this from trim edge

FONT_DIR = Path("C:/Windows/Fonts")
FONT_TITLE = FONT_DIR / "georgiab.ttf"   # Georgia Bold
FONT_BODY = FONT_DIR / "georgia.ttf"     # Georgia Regular
FONT_BODY_ITALIC = FONT_DIR / "georgiai.ttf"

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (100, 100, 100)
LIGHT_GRAY = (200, 200, 200)


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


def create_cover(page_count: int, output_path: Path, front_cover_path: Path):
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

    # Create canvas
    cover = Image.new("RGB", (pw, ph), WHITE)
    draw = ImageDraw.Draw(cover)

    # Key x-coordinates (in pixels)
    bleed_px = inches(BLEED)
    back_left = bleed_px                           # back cover trim left
    back_right = bleed_px + inches(TRIM_W)         # back cover trim right
    spine_left = back_right                         # spine left edge
    spine_right = spine_left + inches(spine_w)      # spine right edge
    front_left = spine_right                        # front cover trim left
    front_right = front_left + inches(TRIM_W)       # front cover trim right

    # -----------------------------------------------------------------------
    # FRONT COVER — paste original cover.jpg
    # -----------------------------------------------------------------------
    front = Image.open(front_cover_path).convert("RGB")
    # Resize to exactly the front panel + bleed on right/top/bottom
    front_panel_w = inches(TRIM_W + BLEED)
    front_panel_h = ph
    front_resized = front.resize((front_panel_w, front_panel_h), Image.LANCZOS)
    cover.paste(front_resized, (spine_right, 0))

    # -----------------------------------------------------------------------
    # SPINE — title + author, rotated
    # -----------------------------------------------------------------------
    spine_px = inches(spine_w)
    if spine_px > 0 and page_count >= 79:
        # Determine font size that fits the spine width (height when rotated)
        spine_font_size = max(7, min(14, int(spine_w * DPI * 0.55)))
        try:
            spine_font = ImageFont.truetype(str(FONT_TITLE), spine_font_size)
        except OSError:
            spine_font = ImageFont.load_default()

        spine_text = "HOW I MET CLAUDE CODE — Yann Debray"

        # Create a temporary image for the rotated spine text
        # Text runs bottom-to-top on the spine (standard for English books)
        bbox = draw.textbbox((0, 0), spine_text, font=spine_font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]

        spine_img = Image.new("RGB", (text_w + 20, text_h + 10), WHITE)
        spine_draw = ImageDraw.Draw(spine_img)
        spine_draw.text((10, 5), spine_text, fill=BLACK, font=spine_font)

        # Rotate 90° CCW (text reads top-to-bottom when book spine faces you)
        spine_rotated = spine_img.rotate(90, expand=True)

        # Center on spine area
        sx = spine_left + (spine_px - spine_rotated.width) // 2
        sy = (ph - spine_rotated.height) // 2
        cover.paste(spine_rotated, (sx, sy))

    # Draw thin spine fold lines (guides — will be at trim edges)
    draw.line([(spine_left, 0), (spine_left, ph)], fill=LIGHT_GRAY, width=1)
    draw.line([(spine_right, 0), (spine_right, ph)], fill=LIGHT_GRAY, width=1)

    # -----------------------------------------------------------------------
    # BACK COVER — description text
    # -----------------------------------------------------------------------
    safe = inches(SAFE_MARGIN)
    text_left = bleed_px + safe
    text_right = back_right - safe
    text_width = text_right - text_left
    y = bleed_px + safe

    # Subtitle / tagline
    try:
        tagline_font = ImageFont.truetype(str(FONT_BODY_ITALIC), 24)
        desc_font = ImageFont.truetype(str(FONT_BODY), 18)
        quote_font = ImageFont.truetype(str(FONT_BODY_ITALIC), 16)
        heading_font = ImageFont.truetype(str(FONT_TITLE), 28)
    except OSError:
        tagline_font = desc_font = quote_font = heading_font = ImageFont.load_default()

    # Title on back
    draw.text((text_left, y), "How I Met Claude Code", fill=BLACK, font=heading_font)
    y += 50

    # Tagline
    draw.text((text_left, y), "A Memoir of Human-AI Collaboration", fill=GRAY, font=tagline_font)
    y += 60

    # Description paragraphs
    description = [
        "In December 2025, Yann Debray — a product manager with more curiosity than coding skill — was given access to a pilot program for Claude Code. What was meant to be a three-month evaluation turned into a book.",
        "",
        "From the author of Programming GPTs, How I Met Claude Code is not a technical manual. It is the honest, personal story of what happens when an AI stops being a tool you pick up and put down, and starts becoming a thinking partner that builds alongside you.",
        "",
        "Over the course of three months, Yann found himself vibe coding websites at midnight, conducting competitive intelligence that would have taken weeks in a matter of hours, publishing CLI tools named after Nietzsche and Montaigne to PyPI, launching a sports analytics YouTube channel across five different sports, and presenting to increasingly bewildered colleagues about a transformation he was living in real time.",
        "",
        "The book traces a journey through five modes of collaboration — strategic thinking partner, creative collaborator, research engine, writing partner, and builder — and asks the question that most AI books avoid: When intelligence becomes cheap, what is distinctly human?",
        "",
        "Part memoir, part field guide, part philosophical inquiry — for anyone who suspects that the relationship between humans and AI is changing faster than the conversation about it.",
    ]

    for para in description:
        if para == "":
            y += 12
            continue
        lines = wrap_text(draw, para, desc_font, text_width)
        for line in lines:
            draw.text((text_left, y), line, fill=BLACK, font=desc_font)
            y += 26
        y += 8

    # Closing quote
    y += 20
    quote = '"There\'s BC — Before ChatGPT. There\'s BCC — Before Claude Code. And now there\'s whatever comes next."'
    quote_lines = wrap_text(draw, quote, quote_font, text_width - 40)
    for line in quote_lines:
        draw.text((text_left + 20, y), line, fill=GRAY, font=quote_font)
        y += 24

    # Barcode area placeholder (bottom-right of back cover)
    barcode_w = inches(2.0)
    barcode_h = inches(1.2)
    barcode_x = back_right - safe - barcode_w
    barcode_y = ph - bleed_px - safe - barcode_h
    draw.rectangle(
        [barcode_x, barcode_y, barcode_x + barcode_w, barcode_y + barcode_h],
        outline=LIGHT_GRAY,
        width=2,
    )
    barcode_font = ImageFont.truetype(str(FONT_BODY), 14) if FONT_BODY.exists() else ImageFont.load_default()
    draw.text(
        (barcode_x + 10, barcode_y + barcode_h // 2 - 10),
        "ISBN BARCODE AREA",
        fill=LIGHT_GRAY,
        font=barcode_font,
    )

    # -----------------------------------------------------------------------
    # Save as PDF at 300 DPI
    # -----------------------------------------------------------------------
    cover.save(str(output_path), "PDF", resolution=DPI)
    print(f"\nSaved: {output_path} ({output_path.stat().st_size / 1024:.0f} KB)")


def main():
    parser = argparse.ArgumentParser(description="Generate KDP paperback cover")
    parser.add_argument("--pages", type=int, default=120,
                        help="Interior page count (default: 120)")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    front_cover = repo / "cover.jpg"
    output = repo / "cover-kdp-paperback.pdf"

    if not front_cover.exists():
        print(f"Error: {front_cover} not found")
        return

    create_cover(args.pages, output, front_cover)


if __name__ == "__main__":
    main()
