# How I Met Claude Code
## Book Material — Source Notes & Chapter Outlines

**Author: Yann Debray**
*Compiled from ~3 months of conversations (December 2025 – February 2026)*

---

## TRANSCRIBED INTRODUCTION (Handwritten)

**How I Met Claude Code**

As I was about to respond to a friend who had asked if there was a GPT to look up flight prices to Boston, it got me to reflect on the journey of AI for the past few years.

GPTs were a thing, and then Claude Code arrived.

This is the story of how I met Claude. But mainly Claude Code.

It was December of 2025. For some reason, this is when the world started to pay attention to Claude Code, and what was happening with coding agents.

The company I worked for (the MathWorks, developers of MATLAB) was starting a pilot to assess the potential for non-developers first. A few product managers were given access, with the responsibility to report back on their usage in the first quarter of 2026. I was one of the lucky ones.

---

## CHAPTER 1: BEFORE CLAUDE CODE (BCC) — THE CHATGPT ERA

### The Vibe Coding Origin Story

**Key scene: The Kitchen Demo (August 2025)**

Late August 2025. My in-laws were visiting, shortly after GPT-5's release. My father-in-law and I were in the kitchen late at night.

> **Me**: "What website or web app would you like to develop?"
> **Father-in-law**: *looks around, points at a recipe book*
> **Me**: "Ok, let's build a website with French recipes."

Single prompt. Single session. Domain purchased on Cloudflare that same night. recettesdezoe.com was born.

**The Surprise Discovery (December 2025):**
Four months later — zero edits, zero marketing, zero SEO work — I checked my Cloudflare dashboard: **1,300+ visitors in the past month.** Pure organic traffic.

*Lessons:*
- Vibe coding can produce genuinely useful, discoverable products
- The "demo that becomes real" pattern is more powerful than planned projects
- Domain purchases at 10pm sometimes pay off

### Other Pre-Claude Projects

**GhostRunners.app** — Summer 2025. I wanted to beat my cycling performance but lacked real-time analytics comparing my current ride to previous efforts. Built with MATLAB Mobile, MATLAB Online, Python (Garmin FIT SDK). Recorded YouTube videos about it.

**OpenAI Codex** — Early VSCode integration for vibe-coded HTML/JS apps, later evolved into cloud agent for hands-off data analysis.

**OpenAI Canvas** — Used once. For single-page web apps, you defaulted to the Claude app (mobile or desktop).

### "GenAI Tools for Modern Tech Marketers" (September 2025)

*Source: Claude Code Book Draft.md — Week 2*

Before the Claude pilot even began, I gave a presentation to the broader product marketing department at the end of September 2025 with my colleague Jacob — called "GenAI Tools for Modern Tech Marketers."

The focus was on **Microsoft Copilot** capabilities, as those were more widely available in the organisation. It covered three personas and use cases:
- **Product Manager** — strategic and analytical work
- **Developer** — code assistance
- **Outbound Marketer** — content and campaign support

Two Microsoft 365 Copilot tools stood out for product managers:
1. **The Researcher** — deep research capability (similar to what ChatGPT and Perplexity introduced in early 2025)
2. **The Analyst** — data analysis integrated in the Microsoft 365 environment, with access to Excel files. I used it to analyze product usage sliced across different dimensions.

*This pre-dates the Claude pilot by two months and establishes the "before" baseline — what AI tools looked like before Claude Code changed the game.*

---

## CHAPTER 2: DECEMBER 2025 — FIRST CONTACT

### Claude Desktop: The Stepping Stone

*Source: Claude Code Book Draft.md — Week 1*

Before diving into Claude Code, I started with **Claude Desktop**. The Desktop app is a very approachable interface for those who come from chat apps like ChatGPT. The first question you ask yourself is: What kind of project can I tackle with Claude?

The type of tasks I tackled with Claude Desktop was more around strategy and competitive analysis than coding related (at first). I created a presentation on the impact of agentic AI on the market of scientific and technical computing — something that most companies must be asking themselves now.

**The technology adoption chasm:** I developed a diagram describing the chasm between early adopters of agentic AI (evaluating solutions like Claude) and the majority still associating AI with chatbots like ChatGPT. This strategic framing became a recurring lens.

### The MathWorks Pilot

The company started a pilot for Claude Code — assessing potential for non-developers first. Product managers were given access, with responsibility to report back in Q1 2026. I was one of the lucky ones.

### Conference Report-Outs as Early Use Cases

*Source: Claude Code Book Draft.md — Week 1*

We went to the **JupyterCon conference** in San Diego with my colleague Rohan in early November. We had already delivered an internal presentation to report on what was happening in open-source scientific computing and notebooks. But the whole process took us a long time, and I wondered: could some parts of it be automated? How much so, and how qualitative would the result be?

I designed a workflow with three scenarios between note-taking and proper reporting in presentation form. Another conference was coming up — **PyData**, happening locally in Boston for the first time (usually PyData US takes place in NYC) — so I replicated this workflow to test it on a new set of data.

### The Blogging Workflow

*Source: Claude Code Book Draft.md — Week 1*

The core insight applied to blog writing: **automate the boring steps to concentrate on ideation and code writing.** This became a visual workflow diagram and a recurring principle throughout the collaboration.

### The Strategic Awakening

My very first substantive conversation with Claude was about strategy. I shared a memo I'd written to the Director of Product Marketing. I won't share the full memo here, but the core thesis was about the strategic tension between being best-in-class at coding agents vs. being best-in-class at building tools that coding agents call.

**Claude's role:** Fact-checking market claims (confirmed Cursor crossed $1B ARR, Claude Code reached $1B run-rate within 6 months), stress-testing arguments, identifying gaps. The feedback was direct — praised the strategic logic but called out the need for concrete examples, better risk coverage, and clearer success metrics.

*This set the tone for everything that followed: Claude as thinking partner, not just tool.*

### The Blog Posts Begin

Within the first week, I started drafting blog posts for the MATLAB AI Blog I'd taken over on September 1st. Posts about:
- MATLAB MCP Core Server 
- Connecting to Hardware (like Data and Image Acquisition devices)
- Deploying a Quant Agent
- Antigravity + MATLAB (wicked good)
- Giving Local AI Agents the ability to use MATLAB with MCP
- Building an Optimization Agent
- Automating the Documentation of MATLAB Analysis
- AI-assisted Model-Based Design

Claude analyzed my published writing style and created a "skill" — a structured guide capturing my voice:

**My signature patterns:**
- Opening hooks: "If you are like me, you are probably familiar with this situation."
- Colleague references: "my dear colleague [Name]"
- Honest limitations: "I'm not an expert in Finance!"
- Closings: "Happy hacking, and let me know what you build! 👋🏻"
- Structure: Problem → Demo → Walkthrough → Resources

---

## CHAPTER 3: THE PHILOSOPHER TOOLS

### A Suite of Developer Tools Named After Philosophers

I built a family of developer tools, each named after a philosopher whose ideas connect to the tool's purpose:

**nietzsche.cc** — Presentation generator (CLI). The `power` command generates slide decks. Connection: "The will to present" / Übermensch idea of transcending tedious manual work. Eternal recurrence fits automation and reusable templates.

**montaigne.cc** — Media processing toolkit for presentation localization. Transcription, translation, audio/video processing using Google Gemini AI. Connection: Montaigne's *Essais* as exploration and interpretation of diverse perspectives.

**ricoeur.cc** — CLI search tool for conversation history. The "part → whole → part → whole" hermeneutic circle motif. Connection: Ricoeur's philosophy of interpretation and understanding context.

**Claude's design feedback:** ricoeur.cc edges ahead on conceptual coherence (tool purpose ↔ philosopher theme), while nietzsche.cc is more polished in UX. Recommended a shared landing page to tell the story of why these tools exist as a family.

### The Deeper Connection: Philosophy Meets Code

My 2025 reading list wasn't random — it formed a deliberate arc:

| Book | Author | Resonance |
|------|--------|-----------|
| *The Trial* | Kafka | Individual vs. system — relevant to navigating corporate AI adoption |
| *The Stranger* | Camus | Absurdism, authentic living — the ethos behind vibe coding |
| *Thus Spoke Zarathustra* | Nietzsche | Will to power, self-overcoming — naming your tools after this |
| *Apology* | Plato/Socrates | Examined life, intellectual humility |
| *The Schopenhauer Cure* | Irvin Yalom | Philosophy as therapy, bridging thought and practice |
| *Nexus* | Harari | AI as new chapter in human story |
| *Co-Intelligence* | Mollick | Practical frameworks for human-AI collaboration |

**My synthesis:**
> "The existentialists ask 'how should I live authentically?' while Mollick and Harari ask 'how should we live with AI?' These questions are not separate. The tools we build shape the lives we lead."

I even created a full voiceover script for a Zarathustra presentation — 15 slides covering the prophet's descent, the Übermensch, the three metamorphoses (Camel → Lion → Child), the Last Man, Will to Power, Eternal Recurrence. Estimated runtime: 12-15 minutes.

The philosopher rap battle app concept emerged naturally — an educational, gamified web app where philosophers debate each other. Nietzsche vs. Schopenhauer as the flagship matchup.

---

## CHAPTER 4: THE COMPETITIVE INTELLIGENCE MACHINE

### How Claude Became My Research Partner

A massive body of work emerged: comprehensive competitive intelligence reports spanning multiple software markets.

**The Pattern:** I'd bring Claude a company or technology, Claude would research extensively, and together we'd extract strategic implications for MathWorks' positioning. This wasn't just fact-gathering — it was thinking partnership.

---

## CHAPTER 5: THE MCP REVOLUTION

### "USB-C for AI"

The MATLAB MCP Core Server became a central theme. I wrote about it, created tutorials for it, built onboarding materials around it, and positioned it as the bridge between MATLAB and the agentic AI ecosystem.

**The MCP Core Server provides 5 tools:**
1. `detect_matlab_toolboxes` — Reports installed toolboxes
2. `check_matlab_code` — Runs checkcode for style/correctness
3. `evaluate_matlab_code` — Executes MATLAB code
4. `start_matlab` / `quit_matlab` — Session management

**Key positioning insight I developed:**
> This is an **integration play**, not putting agentic front and center. MATLAB "integrates" with coding agents like Claude Code and GitHub Copilot. We're showing MATLAB users that they're not left behind.

**The Pocket Guide Strategy:** I developed a strategic document for a pocket guide aimed at two audiences:
1. *Primary:* MATLAB users evaluating coding agents ("Does MATLAB work with these new coding agents I keep hearing about?")
2. *Secondary:* MATLAB users who already use GitHub Copilot and want to extend it to run MATLAB code

**Claude Code Onboarding for MathWorkers:** I created a complete onboarding package — installation guide, CLAUDE.md files, slash commands, MCP server setup, Git workflows, tips & best practices. Complete with a Claude Code 101 presentation.

### The MCP Server Design Experiments

I designed MCP servers for:
- **ThingSpeak** (IoT data access via MCP)
- **Google Spreadsheet** (private data access — actually deployed)
- **MATLAB Remote Service** (for remote execution in the cloud or on a local server)

### Agentic Learnings: Tips & Tricks with Claude Code

*Source: Claude Code Book Draft.md — "Agentic learnings" section*

Key Claude Code features I documented for onboarding:

- **`/init`** — Bootstrap a project with CLAUDE.md and initial configuration
- **`/context`** — Load context into a session
- **`/commands`** — Custom slash commands for repeatable workflows

**Commands vs. Skills:**

| Aspect | Commands | Skills |
|--------|----------|--------|
| Invocation | Manual: /command | Automatic: Claude decides |
| Structure | Single .md file | Directory with SKILL.md |
| Location | .claude/commands/ | .claude/skills/ |
| Discovery | User must type command | Claude matches description |
| Supporting files | Not supported | Load on demand |
| Best for | Quick templates | Complex workflows |

### Advanced Maneuvers: Agents Calling Agents

Beyond "agents calling tools" (the MCP thesis), a more advanced pattern emerged: **agents calling agents** — orchestrating multiple AI agents in sequence or parallel. This escalation from tool-use to agent-orchestration represents another step in the agentic AI evolution.

*See also: [Add examples for slides with a table · Issue #8 · yanndebray/nietzsche](https://github.com/yanndebray/nietzsche/issues/8)*

---

## CHAPTER 6: THE SIDE PROJECTS THAT KEPT GROWING

### recettesdezoe.com — From Demo to Business?

The recipe site story evolved through multiple conversations:

1. **Origin** — Kitchen demo with father-in-law
2. **Discovery** — 1,300+ organic visitors
3. **Strategy** — I applied Rob Fitzpatrick's "Mom Test" methodology to validate whether to invest further
4. **Competitive analysis** — French recipe landscape (Marmiton, 750g, Cuisine AZ)
5. **Content scaling** — I designed a CLI tool ("Zoé") using Copilot SDK to generate recipes while preserving the authentic voice

**The Voice Test** I defined for recipe generation:
> "Could this have been written by someone sharing their grandmother's recipe over coffee? If it sounds like a food blog template or a restaurant menu, it's wrong."

### Sports Analytics YouTube Channel (@yannspeaksai)

7 videos published in 2025:
- **Tennis** — French Open prediction (ELO + ML, 75% accuracy)
- **NBA** — Season ranking animations, dashboard with React/GitHub Actions
- **NFL** — Two projects: (1) MATLAB NFL Analytics Toolbox wrapping nfl_data_py (github.com/slevin48/NFL-toolbox), vibe-coded with Codex; (2) TV Clutch Factor metric + interactive dashboard (github.com/slevin48/NFL-analysis), 25 seasons of clutch QB analysis
- **Cycling** — Beat Your Ghost ride comparison, MATLAB Mobile data capture
- **Soccer** — Premier League dashboard, programmatic MATLAB UI (uifigure), TheSportsDB API integration, built in 2 days (github.com/yanndebray/premier-league-matlab)
- **Music** — KNN recommendation system using Spotify audio features

### The Music Recommendation Deep Dive

A full architecture designed for a personal music management app:
- Spotify API integration for audio features (energy, acousticness, etc.)
- "Gain back control over the algorithm"
- Multiple form factors explored: web app, CLI, desktop, hybrid
- Different use cases: local music management, personal Spotify Wrapped, mood-based playlist generation

---

## CHAPTER 7: WRITING THE FUTURE — "THE AGE OF AI AGENTS"

### The Academic Paper

I drafted comprehensive essays on agentic AI covering:
- MCP infrastructure and the "USB-C for AI" metaphor
- RAG-augmented workflows for engineering
- Hybrid human-agent collaboration

### The Blog Post Feedback Loop

One of the most revealing conversations: a colleague gave me feedback on a blog post draft about automating documentation with the MCP Core Server. They said:

> "Based on the first paragraph, it sounded like you were going to show me how to take an existing script/analysis and get that ready for GitHub. But the workflow below starts from scratch and delegates the analysis to the LLM as well. I actually really liked the idea that you were going with in the first paragraph — do we have like an initial version of the script that we can start from? That way it's still the human doing the 'interesting' parts, and then you're using the AI to do the 'tedious' parts?"

This feedback crystallized a key theme of the book: **the human does the interesting parts, AI handles the tedious parts.** Not AI replacing humans, but AI as amplifier.

---

## CHAPTER 8: WHAT THIS RELATIONSHIP ACTUALLY IS

### The Nature of Human-AI Collaboration

Over 3 months, the conversations reveal a pattern:

**Claude as strategic thinking partner** — Not just answering questions, but challenging assumptions, fact-checking claims, identifying gaps in arguments. The "agent calling toolboxes" strategy was sharpened through dialogue.

**Claude as creative collaborator** — The philosopher-themed tools, the voiceover scripts, the rap battle concept, the recipe site strategy — these emerged from iterative conversation, not one-shot prompts.

**Claude as research engine** — The competitive intelligence work was genuinely collaborative. I brought context and strategic judgment; Claude brought breadth of research and synthesis.

**Claude as writing partner** — My blog voice was analyzed, codified into a "skill," and then used to draft posts that authentically sounded like me.

**Claude as builder** — Presentations, documents, web apps, architecture designs, onboarding materials — actual artifacts produced together.

### What Makes This Different From GPTs

Your intro captures it: "GPTs were a thing, and then Claude Code came arrived."

The difference isn't just capability — it's the nature of the interaction. GPTs were tools you used. Claude became something closer to a colleague. The conversations have:
- **Continuity** — Each builds on the last
- **Shared context** — Claude knows my projects, my style, my strategic thesis
- **Honest feedback** — Claude pushes back, identifies weaknesses, suggests alternatives
- **Mutual shaping** — My ideas shape Claude's outputs; Claude's responses shape my thinking

---

## APPENDIX: KEY LINKS & REFERENCES

### My Projects
- recettesdezoe.com — French recipe website
- ghostrunners.app — Cycling analytics
- nietzsche.cc — Presentation generator
- montaigne.cc — Media processing toolkit
- ricoeur.cc — Conversation search tool
- github.com/yanndebray/cycling — Cycling data repo
- github.com/slevin48/spreadsheet-MCP — Google Sheets MCP server

### YouTube (@yannspeaksai)
- Cycling data with MATLAB Mobile: youtu.be/maZ26FN_cqQ
- Beat Your Ghost ride comparison: youtu.be/Q_1XZrtrnWA
- First Codex development: youtu.be/3X6K-END624
- Codex cloud agent data analysis: youtu.be/zhpPdpjdbRM

### MathWorks Blog Posts
- MATLAB MCP Core Server release (Nov 3, 2025)
- MATLAB MCP Client on GitHub (Dec 10, 2025)
- MCP Servers for Quant Agent (Nov 10, 2025)
- Connecting to Hardware with MCP (Dec 17, 2025)
- Building an Optimization Agent with MCP (Jan 15, 2026)
- Automating Documentation with MCP (Feb 5, 2026)

## APPENDIX: THE HACKATHON PROJECTS

### Claude Recommends What To Build

When I asked Claude what to build for a Claude Code hackathon, based on everything we'd discussed, the top recommendations were:

1. **MCP-Orchestrated Slide Deck Generator** — Combining nietzsche.cc with Claude Code. "Agents calling tools" thesis in action.
2. **Philosopher Rap Battle Web App** — My existing concept, built live using Claude Code as a vibe coding demo.
3. **Voiceover Annotation Tool (montaigne.cc MVP)** — Minimal web app for reviewing AI-generated voiceovers. Play video, press a key to drop a timestamped note, export annotations as JSON or SRT. Why it fits: I already did the competitive research (Frame.io gaps, etc.), it scratches my own itch (Zarathustra voiceover workflow), it's lightweight enough for a hackathon, and could evolve into a real tool for my YouTube content production.

The twist for #2: *Build the entire thing live using Claude Code as a demonstration of vibe coding itself.*


---

*"The tools we build shape the lives we lead."*
