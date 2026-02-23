# Amazon KDP Paperback Cover Rules

Reference: https://kdp.amazon.com/en_US/help/topic/G201953020

## Trim Size

- **6" x 9"** (standard trade paperback)

## File Format

- Single **PDF** combining back cover + spine + front cover
- Max file size: 650 MB (aim for < 40 MB)

## Resolution & Color

- Minimum **300 DPI**
- **CMYK** recommended for print (RGB accepted — KDP converts internally)
- Avoid spot colors, multiple color spaces

## Bleed

- **0.125" (3.2 mm)** added to top, bottom, and outside edges
- All background images/colors must extend into the bleed area

## Spine Width

Calculated from page count and paper type:

| Paper             | Formula                       |
|-------------------|-------------------------------|
| B&W, white paper  | `page_count × 0.002252"`      |
| B&W, cream paper  | `page_count × 0.0025"`        |
| Premium color     | `page_count × 0.002347"`      |
| Standard color    | `page_count × 0.002252"`      |

### Examples (B&W white paper)

| Pages | Spine Width | Spine Text? |
|-------|-------------|-------------|
| 64    | 0.144"      | No          |
| 79    | 0.178"      | Minimum allowed by KDP |
| 100   | 0.225"      | Barely readable |
| 130   | 0.293"      | Marginally usable |
| 150   | 0.338"      | Comfortable |
| 200   | 0.450"      | Good        |
| 250   | 0.563"      | Generous    |

### Spine Text Rules

- **Minimum 79 pages** required to have any text on the spine
- Spine text must have **at least 0.0625" (1.6 mm)** margin on each side
- Below ~130 pages, the usable width after margins is so narrow that text is effectively illegible
- **Recommendation:** omit spine text below 130 pages

## Safe Margins (Text & Important Content)

- Front/back cover text: **minimum 0.125"** inside trim lines (we use 0.375" for comfort)
- Font size: minimum **7 point** (at 300 DPI: `7 × 300/72 ≈ 29px` in Pillow)
- Spine text: minimum **0.0625"** margin on each side

## Full Cover Dimensions Formula

```
Total width  = bleed + back_cover + spine + front_cover + bleed
             = 0.125 + 6.0 + spine_width + 6.0 + 0.125

Total height = bleed + trim_height + bleed
             = 0.125 + 9.0 + 0.125
             = 9.25"
```

At 300 DPI for 64 pages (spine = 0.144"):
- Width: `12.394" × 300 = 3718 px`
- Height: `9.25" × 300 = 2775 px`

## Font Size Reference (Pillow at 300 DPI)

Pillow's `ImageFont.truetype(path, size)` uses pixel sizes. To convert print points to pixels:

```
pixels = points × 300 / 72
```

| Print Size | Pillow px |
|------------|-----------|
| 7 pt       | 29 px     |
| 9 pt       | 38 px     |
| 10 pt      | 42 px     |
| 11 pt      | 46 px     |
| 12 pt      | 50 px     |
| 14 pt      | 58 px     |

Our back cover uses ~11-12pt body text (46-48px) to match the Kindle Cover Creator output style.

## Pre-Publication Checklist

- [ ] Flatten transparencies
- [ ] Embed all fonts
- [ ] Remove crop marks
- [ ] Ensure 300 DPI minimum throughout
- [ ] No file security / password protection
- [ ] ISBN barcode area left clear (bottom-right of back cover) — KDP places its own

## Current Book

- **Page count:** 64 (from formatted .docx/.pdf)
- **Spine width:** 0.144" (no spine text)
- **Script:** `scripts/create_kdp_cover.py --pages 64`
