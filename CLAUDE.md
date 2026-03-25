# CLAUDE.md

## Project Overview

This is a personal memoir/book titled **"How I Met Claude Code"** by Yann Debray. It documents the author's journey discovering and working with Claude Code over ~3 months (December 2025 – February 2026). The author is a product manager at MathWorks (developers of MATLAB) who participated in an internal pilot program to assess Claude Code for non-developers.

The book explores human-AI collaboration through narrative, covering strategic thinking, creative projects, technical work, competitive research, and software development.

## Repository Structure

```
claude-code-book/
├── CLAUDE.md              ← This file
├── README.md              ← Project title and one-liner
├── LICENSE                ← MIT License (2026, Yann Debray)
├── .gitignore             ← Ignores archives/
├── chapters/
│   └── 01-introduction.md ← Drafted chapters (numbered, one file per chapter)
├── notes/
│   ├── how-i-met-claude-code-material.md    ← Source material & chapter outlines
│   ├── writing-workflow-best-practices.md   ← Writing methodology reference
│   ├── Claude Code Book Draft.md            ← Google Docs export (contains base64 images — see Preprocessing section)
│   └── resources.md                         ← Google Docs → Markdown conversion tools
└── scripts/
    └── strip_base64_images.py               ← Strips base64 images from Google Docs exports
```

**No build system, no dependencies, no tests.** This is a pure Markdown writing project under Git version control (Python 3 used only for preprocessing scripts).

## Writing Conventions

### File Naming
- **Chapters:** Numbered prefix + kebab-case name: `01-introduction.md`, `02-chapter-name.md`
- **Notes:** Descriptive kebab-case: `how-i-met-claude-code-material.md`

### Markdown Format
- **Markdown is the source of truth.** Word and Google Docs are export targets only.
- One chapter = one `.md` file (enables clean AI collaboration and diffing).
- Use YAML front matter for metadata when applicable:
  ```yaml
  ---
  title: "Chapter Title"
  status: draft-v1
  last_editor: claude
  notes: "Any relevant context"
  ---
  ```
- Use blockquotes (`>`) for key insights and dialogue.
- Use Markdown tables for structured data.

### Author's Writing Style
The author has a documented voice with these signature patterns:
- **Opening hooks:** "If you are like me, you are probably familiar with..."
- **Colleague references:** "my dear colleague [Name]"
- **Honest limitations:** "I'm not an expert in Finance!"
- **Closings:** "Happy hacking, and let me know what you build! 👋🏻"
- **Structure:** Problem → Demo → Walkthrough → Resources

When drafting or expanding chapters, preserve this voice. Do not flatten it into generic technical writing.

### Book Structure (9 Chapters + Appendix)
1. Before Claude Code (BCC) — The ChatGPT Era
2. December 2025 — First Contact
3. The Philosopher Tools
4. The Competitive Intelligence Machine
5. The MCP Standardization
6. The Side Projects That Kept Growing
7. Writing the Future — Sharing Knowledge
8. The Permanent Resident — Jean-Clawd & OpenClaw
9. What This Relationship Actually Is
- Appendix: Key Links & References

The detailed outlines for all chapters live in `notes/how-i-met-claude-code-material.md`.

## Git Workflow

### Commit Messages
Use descriptive messages that indicate who made the edit and what changed:
- `"Claude: expanded section on MCP architecture"`
- `"Manual: incorporated editor feedback from Google Docs"`
- `"Add introductory chapter and source notes"`

### Branching
- Primary remote branch: `main`
- Development happens on feature branches

## Tools & Conversion

- **Pandoc** — Markdown ↔ Word conversion: `pandoc chapters/01-introduction.md -o exports/01-introduction.docx`
- **Git/GitHub** — Version control
- **Google Docs + "Docs to Markdown" add-on** — For human collaboration round-trips

## Preprocessing Google Docs Exports

Files exported from Google Docs (via "Docs to Markdown") often contain **base64-encoded images** inlined at the bottom of the `.md` file. These can make a single file over 1 MB, which exceeds Claude's file-read limits and wastes context.

**Before reading or working with a Google Docs export, strip the embedded images using Python:**

```bash
python3 scripts/strip_base64_images.py notes/my-export.md
```

This produces a cleaned file at `notes/my-export.stripped.md` with image references replaced by descriptive placeholders.

**The script (`scripts/strip_base64_images.py`):**

```python
#!/usr/bin/env python3
"""Strip base64-encoded images from Markdown files exported by Google Docs.

Replaces [imageN]: <data:image/...> references with readable placeholders
and keeps all other content intact. Writes to <original>.stripped.md.
"""
import re
import sys
from pathlib import Path

def strip_base64_images(filepath: Path) -> Path:
    text = filepath.read_text(encoding="utf-8")

    # Replace inline base64 image references: [imageN]: <data:image/png;base64,...>
    text = re.sub(
        r'^\[image(\d+)\]:\s*<data:image/[^>]+>',
        r'[image\1]: <!-- base64 image removed for AI processing -->',
        text,
        flags=re.MULTILINE,
    )

    # Replace any remaining inline base64 data URIs in image tags
    text = re.sub(
        r'!\[([^\]]*)\]\(data:image/[^)]+\)',
        r'![\1](<!-- base64 image removed -->)',
        text,
    )

    out = filepath.with_suffix(".stripped.md")
    out.write_text(text, encoding="utf-8")
    print(f"Stripped: {filepath} -> {out} ({filepath.stat().st_size:,} -> {out.stat().st_size:,} bytes)")
    return out

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 strip_base64_images.py <file.md> [file2.md ...]")
        sys.exit(1)
    for arg in sys.argv[1:]:
        strip_base64_images(Path(arg))
```

**Convention:** Always read the `.stripped.md` version when one exists. The original export is kept for reference but should not be read directly by Claude.

## Key Context for AI Assistants

- The source material in `notes/how-i-met-claude-code-material.md` is the comprehensive outline. Chapters in `chapters/` are the polished drafts derived from it.
- The book is narrative and personal, not a technical manual. Maintain warmth, anecdotes, and the author's reflections.
- Central thesis: Claude Code represents a shift from AI-as-tool to AI-as-thinking-partner.
- The book covers real projects: recettesdezoe.com, nietzsche.cc, montaigne.cc, ricoeur.cc, GhostRunners.app, MATLAB MCP Core Server, sports analytics YouTube channel (@yannspeaksai).
- The author works at MathWorks — MATLAB and MCP integration are recurring themes.
- Do not over-edit the author's natural voice. When expanding outlines into prose, match the tone of `chapters/01-introduction.md` and the documented style patterns above.
