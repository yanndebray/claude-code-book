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
├── chapters/
│   └── 01-introduction.md ← Drafted chapters (numbered, one file per chapter)
└── notes/
    ├── how-i-met-claude-code-material.md    ← Source material & chapter outlines
    └── writing-workflow-best-practices.md   ← Writing methodology reference
```

**No build system, no dependencies, no tests.** This is a pure Markdown writing project under Git version control.

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
5. The MCP Revolution
6. The Side Projects That Kept Growing
7. Writing the Future — "The Age of AI Agents"
8. The Hackathon Moment
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

## Key Context for AI Assistants

- The source material in `notes/how-i-met-claude-code-material.md` is the comprehensive outline. Chapters in `chapters/` are the polished drafts derived from it.
- The book is narrative and personal, not a technical manual. Maintain warmth, anecdotes, and the author's reflections.
- Central thesis: Claude Code represents a shift from AI-as-tool to AI-as-thinking-partner.
- The book covers real projects: recettesdezoe.com, nietzsche.cc, montaigne.cc, ricoeur.cc, GhostRunners.app, MATLAB MCP Core Server, sports analytics YouTube channel (@yannspeaksai).
- The author works at MathWorks — MATLAB and MCP integration are recurring themes.
- Do not over-edit the author's natural voice. When expanding outlines into prose, match the tone of `chapters/01-introduction.md` and the documented style patterns above.
