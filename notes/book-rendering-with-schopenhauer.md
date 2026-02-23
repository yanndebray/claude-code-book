# Rendering the Book with Schopenhauer

How we used [Schopenhauer](https://schopenhauer.cc) (`will` CLI) to render the chapter Markdown files into a single `.docx` book.

## Pipeline Overview

```
chapters/*.md  →  concatenate  →  book.md  →  Schopenhauer (Pandoc)  →  book.docx
                                                    ↑
                                          reference doc (template)
```

1. **Source**: 9 Markdown chapter files (`00-introduction.md` through `08-sharing-knowledge.md`) in `chapters/`.
2. **Assembly**: Chapters concatenated into a single `book.md` with YAML frontmatter and `\newpage` page breaks between chapters. Per-chapter frontmatter is stripped.
3. **Template**: `Programming GPTs - Book - chap1.docx` used as a Pandoc reference document — Pandoc inherits its style definitions (fonts, colors, spacing, heading styles).
4. **Rendering**: `will render book.md -o book.docx -t <reference-doc>` calls Pandoc under the hood.

## Assembling Chapters

The combined `book.md` has this structure:

```markdown
---
title: "Programming with Claude Code"
author: "Yann Debray"
---

# Introduction
...chapter 00 content (frontmatter stripped)...

\newpage

# What is Claude Code?
...chapter 01 content...

\newpage

...
```

Key points:
- YAML frontmatter from individual chapters is stripped (only the top-level frontmatter is kept).
- `\newpage` between chapters produces page breaks in the docx output.

## Using a Reference Document as Template

Pandoc's `--reference-doc` option tells it to copy all style definitions from an existing `.docx`. This controls fonts, sizes, colors, heading styles, margins, etc.

```bash
will render book.md -o book.docx -t "Programming GPTs - Book - chap1.docx"
```

The `-t` flag maps to Pandoc's `--reference-doc`.

## Fixing Font Size (10pt vs 12pt)

### Problem

The generated `.docx` had 12pt body text instead of the expected 10pt, even though the reference document appeared to use 10pt.

### Root Cause

Pandoc uses multiple styles for body text — not just "Normal":

| Style             | Paragraphs | Purpose                          |
|-------------------|------------|----------------------------------|
| **Body Text**     | ~280       | Most body paragraphs             |
| **First Paragraph** | ~93      | First paragraph after a heading  |
| **Normal**        | ~48        | Fallback / metadata paragraphs   |

Inspecting the reference doc with python-docx revealed:

```python
from docx import Document
doc = Document("reference.docx")
for name in ['Normal', 'Body Text', 'First Paragraph']:
    style = doc.styles[name]
    size = style.font.size  # in EMU (1pt = 12700 EMU)
    print(f"{name}: {size / 12700 if size else 'None'}pt")
```

Output:
```
Normal: 10.0pt
Body Text: 12.0pt        ← explicit 12pt, overrides Normal
First Paragraph: None     ← inherits from Body Text → 12pt
```

The "Normal" style was 10pt, but **"Body Text" had an explicit 12pt** that overrode it. Since Pandoc maps most body content to "Body Text", the output was 12pt.

### Fix

Patch all three styles in the reference doc:

```python
from docx import Document
from docx.shared import Pt

doc = Document("reference.docx")
for style_name in ['Normal', 'Body Text', 'First Paragraph']:
    doc.styles[style_name].font.size = Pt(10)
doc.save("reference-patched.docx")
```

Then re-render:

```bash
will render book.md -o book.docx -t reference-patched.docx
```

### Lesson

When using a `.docx` as a Pandoc reference document, check **all** body text styles — not just "Normal". Pandoc's style mapping:

- **Normal** → fallback base style
- **Body Text** → most paragraph content
- **First Paragraph** → first paragraph after headings
- **Compact** → tight lists

All of these need consistent font settings for uniform output.

## Commands Reference

```bash
# Render single chapter
will render chapters/00-introduction.md -o outputs/ch00.docx -t template.docx

# Render assembled book
will render book.md -o book.docx -t template.docx

# Render to HTML
will render book.md -o book.html -f html

# Render with variable substitution
will render book.md -o book.docx -V year=2025 -V edition="First"
```
