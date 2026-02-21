---
title: "Writing Workflow Best Practices"
created: 2026-02-21
status: reference
---

# Writing Workflow Best Practices: Markdown + AI Peer Writers

## Core Principle

**Markdown is the source of truth.** All drafting, outlining, and AI collaboration happens in `.md` files under version control. Word and Google Docs are export targets for human collaboration and publishing — edits always flow back into markdown.

## Folder Structure

```
book/
├── chapters/
│   ├── 01-introduction.md
│   ├── 02-chapter-name.md
│   └── ...
├── outlines/
│   └── book-outline.md
├── notes/
│   └── (this file lives here)
├── exports/
│   └── (generated .docx files)
└── README.md
```

## Conversion Paths

### Markdown → Word (.docx)

Use Pandoc:

```bash
pandoc chapters/01-introduction.md -o exports/01-introduction.docx
```

For consistent styling, use a reference template:

```bash
pandoc chapters/01-introduction.md --reference-doc=templates/reference.docx -o exports/01-introduction.docx
```

### Markdown → Google Docs

1. Convert to `.docx` via Pandoc
2. Upload to Google Drive (auto-converts to Google Docs)

### Google Docs → Markdown

Use the "Docs to Markdown" Google Docs add-on, then review the diff in Git before merging changes back.

## AI Peer Writer Best Practices

1. **One chapter = one file.** Easier to hand sections to different AI tools and merge cleanly.

2. **Use front matter for metadata** at the top of every chapter:

    ```yaml
    ---
    title: "Chapter 2: The Agent Layer"
    status: draft-v2
    last_editor: claude
    notes: "Needs stronger opening, examples from automotive"
    ---
    ```

3. **Maintain a `style-guide.md`.** Paste it into every AI session to keep voice and tone consistent across tools.

4. **Structured prompts with context.** When asking an AI to draft or revise, provide: the outline, previous chapter summary, and style notes.

5. **Version everything with Git.** Commit after every meaningful AI-assisted edit. Use descriptive messages:
    - `"Claude: expanded section on MCP architecture"`
    - `"GPT: rewrote opening anecdote"`
    - `"Manual: incorporated editor feedback from Google Docs"`

## When to Use What

| Format       | Use Case                                                  |
|--------------|-----------------------------------------------------------|
| Markdown     | Drafting, outlining, brainstorming, AI collaboration      |
| Word (.docx) | Formal submissions, track changes, publisher deliverables |
| Google Docs  | Real-time collaboration with human co-authors/editors     |

## Tools

- **Pandoc** — format conversion (pandoc.org)
- **Git/GitHub** — version control and collaboration log
- **Docs to Markdown** — Google Docs add-on for round-tripping
- **Claude / ChatGPT / Gemini** — AI peer writers (all markdown-native)
