---
title: "Sharing Knowledge — The Agentic AI Roadshow"
status: source-notes
last_editor: claude
notes: "Detailed notes on presentations to outbound marketing (week 2), industry marketing (week 3), and educator programs (week 6), plus the Marketing Book Club on Co-Intelligence"
---

# Sharing Knowledge — The Agentic AI Roadshow

## Overview

Between January and February 2026, Yann delivered a series of internal presentations to different marketing groups at MathWorks, sharing learnings from his Claude Code pilot. The presentations evolved over time — each iteration reflected additional weeks of experience, new use cases, and deeper insights. What started as a "show and tell" became something closer to an internal evangelism campaign, tailored to each audience.

### Timeline

| Week (2026) | Audience | Deck | Claude Code Week |
|---|---|---|---|
| Week 2 (Jan 15) | Outbound Marketing | "Agentic Best Practices" | Week 6 |
| Week 3 | Industry Marketing | "Agentic — Industry Marketing" | Week 7 |
| Week 6 | Educator Programs | "Agentic Learnings — Edu Marketing" | Week 10 |
| (same period) | Marketing Book Club | Co-Intelligence discussion | ~Week 8-10 |

All three presentations evolved from an earlier deck, "GenAI Tools for Modern Tech Marketers," co-created with Jacob George in September 2025 — originally focused on Microsoft Copilot capabilities.

---

## Presentation 1: Outbound Marketing (Week 2, Jan 15)

**Co-presenters:** Eric and Yann
**Subtitle:** "Agentic Learnings" — "Learnings after 2–3 weeks of Claude Code"

### Structure

The deck organized agentic use cases into three categories, establishing a taxonomy that would carry through all subsequent presentations:

1. **Agentic MVP (App Building Workflow)** — "MVP for Minimal Viable Product or Minimal Viable Prototype?" The ambiguity was intentional — vibe coding blurs the line between prototype and product (recettesdezoe.com being the prime example).

2. **Agentic Digital Marketing (Blogging Workflow)** — Automating the boring steps to concentrate on ideation and code writing. The workflow diagram showed how Claude handles formatting, structuring, and first-pass drafts while the human focuses on ideas and technical content.

3. **Agentic Market Intelligence** — Three sub-workflows:
   - **Deep research post-processing** — Example: PIDO (Process Integration and Design Optimization) market analysis. A single prompt produced a comprehensive analysis: "$200-220M USD market in 2024, growing at 10-12% CAGR." Strategic implications for MathWorks included.
   - **Conference reporting** — Replacing NotebookLM with a slide deck generation tool for conference report-outs.
   - **MATLAB Community insights** — Analyzing MATLAB Answers for product intelligence. Specific requests from colleagues: "Can you tell me what users say about the live editor?" (Rohan), "Can you tell me if a feature like live editor is useful and loved?" (Johanna).

4. **Agentic Learnings** — Practical Claude Code tips:
   - `/init` — Project initialization
   - `/context` — Context management
   - `/commands` — Custom commands
   - Commands vs. Skills distinction (referencing Issue #8 on yanndebray/nietzsche)
   - Encoding gotchas: `'charmap' codec can't encode character` errors

5. **Bonus: MATLAB Central MCP Server** — A custom MCP server for querying MATLAB Central programmatically (internal GitLab: `ydebray/matlab-central-mcp-server`).

### Key Insight

This was the most **workflow-oriented** of the three decks. It was aimed at marketers who needed to see concrete "before and after" comparisons of their daily work — blogging, competitive analysis, community monitoring.

---

## Presentation 2: Industry Marketing (Week 3)

**Presenter:** Yann Debray
**Subtitle:** "Agentic AI — The next wave of GenAI" — "Learnings after 4 weeks of Claude Code"

### Evolution from Week 2

The deck expanded significantly, adding two weeks of additional experience. New sections included:

1. **Agentic Development** — New category not present in the outbound deck. Focused on "Porting a Python package to MATLAB" — a technical use case showing Claude Code as a development tool, not just a marketing productivity tool.

2. **Deep Research → Presentation pipeline** — New example: neuroscience community toolbox analysis (FieldTrip, EEGLAB, MNE-Python). The deep research revealed: "EEGLAB leading citations at 21,700+ and MNE-Python showing fastest growth with 3,200 GitHub stars and 416 contributors. A clear bifurcation is emerging between MATLAB-based tools (historically dominant) and Python-based alternatives (rapidly growing, zero licensing costs)." This kind of competitive intelligence was directly actionable for industry marketing.

3. **Presentation → Video pipeline** — A new step in the content chain: going from slide deck to narrated video.

4. **Advanced Learnings** — A more detailed learnings section with a weekly progression:
   - Week 1: "Density" — build tools, not skills
   - Week 2: Claude Code running Codex and Gemini (agents calling agents)
   - Week 3: TUI (Terminal User Interface)
   - Week 4: ?

5. **Bonus: Local Agents** — Running AI locally, plus a new section on **"Agents calling Agents"**:
   - Gemini CLI headless mode (`geminicli.com/docs/cli/headless/`)
   - OpenAI Codex CLI (`developers.openai.com/codex/cli/reference#codex-exec`)
   - Claude subcontracting to GitHub Copilot
   - `/github:AssignCodingAgent` (MCP) to implement issues

### Key Insight

This deck was more **technically ambitious** than the outbound version. It introduced the "agentic development" category and the "agents calling agents" concept — Claude orchestrating other coding agents (Codex, Gemini, Copilot). The audience of industry marketers needed to understand the competitive landscape, so the deep research examples were chosen for their strategic relevance to MathWorks market segments.

---

## Presentation 3: Educator Programs (Week 6)

**Presenter:** Yann Debray
**Subtitle:** "Agentic AI — For Edu workflows" — "Learnings after 6 weeks of Claude Code"

### Structure (Tailored for Education)

The deck was restructured entirely for the educator audience:

1. **From GenAI to Agentic AI** — Introductory framing for an audience that may be less familiar with the distinction.

2. **Resources** — Both internal (sessions by Maria Elena and Akhil) and external (Yann's MATLAB AI blog post published the day before: "Automate the Documentation of Your MATLAB Analysis with Agentic AI").

3. **Use Cases** (education-specific):
   - **Teaching Forums** — Creating educational content for a linear algebra workshop (University of Oklahoma). This was the central demo.
   - **Community Toolboxes** — Planned for next session.
   - **Conference Report-Out** — Planned for next session.

4. **Agentic Development** — Brief section showing `yanndebray/zoetrope` project.

5. **Agentic Learnings** — Same practical tips section.

6. **Bonus: Local Agents** — Carried over from industry marketing deck.

### Key Insight

This was the most **audience-adapted** of the three decks. The use cases were reframed entirely around educator workflows — teaching content creation, forum support, community toolbox analysis. The generic "blogging workflow" and "market intelligence" sections from earlier decks were replaced with education-specific equivalents.

---

## The Educator Programs Meeting (VTT Transcript)

**Duration:** ~58 minutes
**Participants:** Stefano, Jeff, Maria Elena, Will, Nandini, Ascension (remote)

### The Live Demo That Wasn't Planned

The most memorable moment came when Ascension challenged Yann: "What is the agentic part about this?" She wasn't convinced this was different from regular generative AI. Yann's response was to open Claude Code live and unrehearsed:

- Typed `claude` in the terminal
- Prompted: "Look at the linear algebra folder/example and now do the same for Fourier analysis"
- Claude Code autonomously explored the folder, read existing MATLAB live scripts, learned the format, and generated new Fourier analysis content
- It used 3-4 tools, wrote both code and documentation

Yann's commentary during the demo: *"It's a spectacle. Like this just now. It turns into a performance. This thing is insane."* And the practical advice: *"Always read the code."*

### The Teaching Forum Pipeline

The full demonstrated workflow:
1. MATLAB script on PCA (Principal Component Analysis, Fisher Iris dataset)
2. Claude Code generates the code and content
3. Export to Word/markdown
4. Feed into NotebookLM for slide deck generation
5. AI-generated voiceover for narrated video
6. Total pipeline time: **under 30 minutes**

Caveat from Yann: *"People don't like [the AI-generated voice]. So that's the part that you should probably get rid of, but the rest is actually quite interesting."*

### The "Skills" Concept — The Matrix Analogy

Yann used the Matrix analogy to explain skills: *"I don't know if some of you saw the movie The Matrix... 'I know Kung Fu,' right? Like he plugs himself into the skill and then he knows."* Teaching Claude how to write MATLAB live scripts through structured documentation.

### Audience Reactions

**From skepticism to pragmatism** — Started skeptical ("Not yet, Yann. But I'm sure you will [impress me].") but came around, seeing the potential for scaling educational content production on GitHub and File Exchange.

**On cost:** *"With great powers come great consumptions."* — Yann, on the $200/month subscription and its daily limits. His practical note: *"I have a 5-hour window where I start in the morning and then until 2... at some point I'm eating 100% and then I cannot work anymore."*

### Outcome

Yann proposed creating a new **Gen AI Tiger Team** specifically for the Educator Programs group. The team agreed and discussed scheduling follow-up sessions for the remaining use cases.

---

## The Marketing Book Club: Co-Intelligence by Ethan Mollick

**Duration:** ~50 minutes
**Co-leaders:** Yann Debray, Kyle Hakes, Jacob George
**Session:** Week 1 — Introduction and Chapter 1

### Setup

Yann co-organized a marketing book club around Mollick's "Co-Intelligence." The choice was deliberate — the book explores practical frameworks for human-AI collaboration, directly connecting to Yann's lived experience with Claude Code. He re-listened to the audiobook and found it "still very relevant" despite being written before the agentic AI wave.

### Key Themes Discussed

**"Sleepless Nights"** — Mollick's concept of the first visceral encounter with AI. Participants shared their own moments. Kyle Hakes had perhaps the most striking: someone replicated six months of his market analysis work with a deep research prompt in 30 minutes — "70% of the way there." His reaction: *"I was like, well, I'm out of a job."*

**The "Alien Mind" Metaphor** — Mollick frames AI as fundamentally non-human intelligence. Yann connected this to his experience: AI doesn't think like us, but that's what makes it a powerful thinking partner.

**Sycophancy** — Yann demonstrated ChatGPT's memory feature describing him in flattering terms ("deep technical"), sparking a humorous discussion about AI telling users what they want to hear. This contrasted sharply with his experience of Claude pushing back on his strategic memo.

**"Productive Anthropomorphism"** — Yann introduced "Jean Claude," his personal AI agent on Telegram with a French accent. He coined the term to describe how giving AI personas and names makes collaboration more effective and intuitive rather than being a cognitive trap.

**The Identity Question** — One of the most substantive exchanges:

> *Yann: "When AI starts writing good code, what is the part of your identity that you feel is threatened, if any?"*
> *David Barnes: "I really like that articulation. About somewhat of the identity. It's not something I've thought about before."*

Yann's framing: *"If intelligence is just so cheap, so accessible, so scalable, what is me?... It's not necessarily insecurity, it's evolution."*

**The Eras** — Yann described his personal timeline as having three eras, borrowing from Taylor Swift: the OpenAI days, "Google is so back," and "Claude Code — it's the new era." He added: *"There's BC — Before ChatGPT. Now there's also BCC — Before Claude Code."*

### Yann's Demos During the Book Club

- **Claude** as preparation partner: "Based on all of our conversations, help me prepare for a book club on Co-Intelligence"
- **Jean Claude** on Telegram — personal agent with French accent
- **MATLAB MCP Core Server** with OpenAI Codex desktop app — MATLAB running headless while an agent controls it
- **NotebookLM** for conference note → slide deck pipeline
- Philosopher-named tools: Nietzsche (slides), Montaigne (videos), Schopenhauer (documents), Merleau-Ponty (video analysis)

### The "AND" Conclusion

Yann's closing message: *"If you can think of it as an AND — if we can do for humans AND for AI, then maybe we have something here."* MathWorks should serve both humans and AI agents, not treat it as zero-sum.

---

## Cross-Cutting Themes (Potential Chapter Material)

### 1. The Presentation Evolved with the Presenter

Each deck iteration reflected genuine learning, not just additional slides. Week 2 was workflow-focused for marketers. Week 3 added technical depth (agents calling agents) for industry marketing. Week 6 was rebuilt from scratch for educators. The presentations were artifacts of Yann's own evolving understanding.

### 2. Tailoring the Message

The same core learnings were repackaged for each audience:
- **Outbound marketing** → blogging workflows, community monitoring, competitive analysis
- **Industry marketing** → deep research for market segments, technical development, agent orchestration
- **Educators** → teaching content creation, forum support, MATLAB live script generation
- **Book club** → philosophical framing, identity questions, strategic implications

### 3. The Live Demo as Persuasion

Across both the educator meeting and the book club, live demos were the turning point. Ascension went from skeptical to excited after seeing Claude Code work in real time. The book club came alive when Yann showed MATLAB being controlled by an agent. The demos were unrehearsed — *"I didn't prepare this"* — which made them more convincing.

### 4. Resistance and Honest Concerns

Every session surfaced genuine strategic tensions:
- **Desktop vs. cloud** (Jeff Alderson, Sam Marshalik) — agentic tools require desktop MATLAB, but MathWorks pushes cloud
- **Identity threat** (book club) — "What is me if intelligence is cheap?"
- **Cost** (Ascension) — "$200/month... with great powers come great consumptions"
- **Governance** — "Very gray area" around what AI-generated content can be used for
- **The business model** — "This is a controversial topic that puts pressure on our very business model"

### 5. The Evangelist Pattern

Yann wasn't just sharing learnings — he was building a movement:
- Proposed a **Gen AI Tiger Team** for Educator Programs
- Co-led a **Marketing Book Club** on human-AI collaboration
- Created **onboarding materials** for other MathWorkers
- Shared **internal tools** (MATLAB Central MCP server, skills repos)
- Documented everything with **weekly iterations** of the slide deck

### 6. Signature Quotes

- *"It's a spectacle. This thing is insane."* — on live Claude Code demos
- *"Always read the code."* — practical best practice
- *"With great powers come great consumptions."* — on token limits
- *"I have a 5-hour window... at some point I'm eating 100% and then I cannot work anymore. I need to go and chat with colleagues."* — on daily usage limits
- *"The question you need to ask yourself now is not what it can do, but what it cannot do."*
- *"We need to surf on the wave, because otherwise we're gonna get crushed."*
- *"Don't shoot the messenger. I'm just sharing what's currently out there in the market."*
- *"BC — Before ChatGPT. Now there's also BCC — Before Claude Code."*
- *"If we can do for humans AND for AI, then maybe we have something here."*
