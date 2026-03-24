---
title: "Chapter 7: Writing the Future — Sharing Knowledge"
status: draft-v1
last_editor: claude
notes: "Covers the internal evangelism campaign — three presentations to different marketing groups, the live demo that changed minds, the blog post feedback loop, the Marketing Book Club on Co-Intelligence, and the transition from user to advocate"
---

# Chapter 7: Writing the Future — Sharing Knowledge

By mid-January 2026, I had been using Claude Code for about six weeks. I'd built tools, sharpened strategies, drafted blog posts at a pace that surprised even me, and spent more late nights in the terminal than I probably should have. But now I faced a challenge that no amount of agentic wizardry could automate: explaining what I'd found to colleagues who hadn't experienced it.

The pilot had a simple requirement — report back on your usage in Q1. What started as a reporting obligation became something I hadn't anticipated: an internal evangelism campaign.

You might know the feeling if you are passionate about tech. You discover something that changes how you work, and suddenly you can't stop talking about it. The problem is that enthusiasm without structure is just noise. I needed to show, not tell. And I needed to tailor the message to audiences who cared about very different things.

## The Presentation That Kept Evolving

The story of these presentations actually begins with that September 2025 deck Jacob and I built together (remember chapter 1) — "GenAI Tools for Modern Tech Marketers." Solid. Useful. Conventional.

By January, that deck had been transformed beyond recognition. Most of the original slides were gone. In their place was something called "Agentic Learnings" — and over the next six weeks, I would rewrite it every week, each time for a different audience. Each version wasn't just a reshuffled slide order. Each one reflected genuine learning, additional weeks of experience, and a deeper understanding of what mattered to the people in the room.

### Outbound Marketing — The Workflow Version

The first presentation landed on January 15th, Week 2 of the new year. I presented to the outbound marketing team, together with Eric, the head of product management for MATLAB. The subtitle said it plainly: "Learnings after a few weeks of Claude Code."

I organized everything into three categories that would carry through all subsequent presentations:

**Agentic MVP** — building apps and prototypes. I posed the question the audience was probably thinking: "MVP for Minimal Viable Product or Minimal Viable Prototype?" The ambiguity was intentional. This wasn't just Vibe coding web sites anymore. It was architecture work, guiding a senior developer (Claude).

**Agentic Digital Marketing** — automating the boring steps of the blogging workflow so you can concentrate on ideation and code writing. I showed the workflow diagram: Claude handles formatting, structuring, and first-pass drafts. The human focuses on ideas and technical content.

**Agentic Market Intelligence** — this was the one that made people lean forward. I showed the PIDO example: Process Integration and Design Optimization market analysis from a single prompt. The output? A comprehensive analysis: "$200M USD market in 2024, growing at 10% CAGR," with strategic implications included. One prompt. What used to take a week of research distilled into minutes.

The outbound team needed concrete before-and-after comparisons of their daily work — blogging, competitive analysis, community monitoring. So that's what I gave them. This was the most workflow-oriented of the three decks.

### Industry Marketing — The Technically Ambitious Version

A week later, same core material, completely different emphasis. The industry marketing team needed to understand the competitive landscape — that was their job, after all. So I added depth.

A new category appeared that hadn't existed in the outbound deck. **Agentic Development** showed Claude Code porting a Python package to MATLAB — a technical use case proving this wasn't just a marketing productivity tool. 

Then came the research examples — and this is where the deck hit differently for this audience. The neuroscience toolbox analysis I'd run with Claude (covered in Chapter 4) wasn't just an interesting output anymore. In this room, it was a mirror. These were the people responsible for deciding where MathWorks should invest in academic disciplines. Showing them that a bifurcation was already underway between MATLAB-based tools and Python alternatives wasn't a demonstration of what AI could do. It was a strategic conversation starter about their own market. The same analysis that had felt like a research experiment when I ran it became something closer to a briefing when I presented it to people with skin in the game.

The weekly learnings section had evolved too. By Week 3, the slides carried three layers of accumulating insight — from Agentic 101 through tool-building to multi-agent orchestration. The audience could see the learning curve accelerating in real time.

### Educator Programs — The One Built from Scratch

By Week 6, I didn't just update the deck. I rebuilt it entirely.

The educator audience cared about teaching content creation, forum support, and MATLAB live script generation. The generic "blogging workflow" and "market intelligence" sections from earlier decks? Gone. Replaced with education-specific use cases: creating content for a linear algebra workshop at the University of Oklahoma, analyzing community toolboxes for academic adoption, generating teaching materials that could scale.

This was the most audience-adapted version. And it was the one where something unexpected happened.

## The Learning Curve in Four Weeks

Each version of the deck included a "weekly learnings" section — a running log of what I'd discovered since the last presentation. What started as a simple bullet list became, without my planning it, a narrative of transformation. Four weeks, four stages.

**Week 1: Agentic 101.** Start with Claude Desktop. Get a taste of the agentic capabilities — the ability to read and write directly on the file system. Discover a few concepts: skills, tools, the Model Context Protocol. See how this applies to coding. Begin with Python, then connect to MATLAB via the MCP Core Server. This was the foundation — understanding that an AI agent isn't just a chatbot with delusions of grandeur, but a system that can use tools autonomously. When I presented this to the outbound team, it was already two weeks old. But for most people in the room, it was new. That gap — between where I was and where my audience was — would widen with every passing week.

**Week 2: Density — less is more.** Focus on just the necessary context. Filter and condense the information you need. The crucial insight: build tools, not just skills. CLI tools can be used by your agents and follow deterministic behavior — a workflow for slide deck creation, information extraction from YouTube videos. This is when the army of philosophers was born: Montaigne, Nietzsche, Schopenhauer. Claude generating GitHub Issues to manage requirements. Tests validated automatically through GitHub Actions. When a test failed, ask the GitHub MCP server to retrieve the trace — no more copy-pasting error logs. `uv` is life. Python for CLI is fire. Publish to PyPI — let the game begin. If Week 1 was about learning what agents could do, Week 2 was about building things that agents could use. The shift from consumer to creator.

**Week 3: Agents calling agents.** Beyond "agents calling tools" — the MCP thesis — a more advanced pattern emerged: Claude orchestrating Codex and Gemini CLI. Deep research workflows inspired by NetworkChuck — sending multiple agents down different research paths and synthesizing the results. This wasn't just tool use anymore. This was orchestration. The conductor stepping up from the orchestra pit. When I showed this slide to the industry marketing team, I could see the moment it clicked for some of them — and the moment it overwhelmed others. The gap between "I use ChatGPT for emails" and "I orchestrate multiple AI agents in parallel" was wider than anyone had expected.

**Week 4: The terminal is my happy place.** Building CLIs for Claude and for myself. TUIs — terminal user interfaces, yes, very nerdy. Even SSH apps that could be accessed remotely. The terminal had become home. Not the IDE, not the browser, not the chat window — the terminal. For a non-developer who started this journey in a ChatGPT text box three months earlier, landing in the terminal and feeling comfortable there was perhaps the most telling sign that something fundamental had shifted.

The progression told a story I hadn't planned but couldn't deny:

| Week | Theme | Identity |
|------|-------|----------|
| 1 | Agentic 101 | Consumer |
| 2 | Density — less is more | Creator |
| 3 | Agents calling agents | Conductor |
| 4 | The terminal is my happy place | Native |

Each stage wasn't just a skill upgrade — it was an identity shift. And each presentation caught me at a different point on that curve, which is why no two versions of the deck told the same story. The audience mattered, yes. But so did where I was on the journey. The person who presented Agentic 101 in Week 2 was not the same person who rebuilt the entire deck for educators in Week 6. The tool had changed me, and the presentations were the evidence.

## The Live Demo That Changed Minds

The educator meeting had about seven people — Stefano, Jeff, Maria Elena, Will, Nandini, and Ascension joining remotely. I had just walked through the PCA-to-video pipeline: MATLAB script, Claude Code generating content, export to Word, feed into NotebookLM for slides, AI-generated voiceover. Total pipeline time: under 30 minutes. I added the honest caveat: "People don't like the AI-generated voice. So that's the part you should probably get rid of. But the rest is actually quite interesting."

Then Ascension asked the question that mattered: "What is the agentic part about this?"

She wasn't being difficult. She was being precise. She wasn't convinced this was different from regular generative AI — from the ChatGPT-era copy-paste workflows we'd all been doing. And she was right to push. If I couldn't explain the distinction clearly, the whole presentation was just a show.

So I did something I hadn't planned. I opened Claude Code. Live. Unrehearsed.

I typed `claude` in the terminal and prompted: "Look at the linear algebra folder and the existing examples. Now do the same for Fourier analysis."

What happened next was the kind of thing you can't fake. Claude Code autonomously explored the folder structure, read the existing MATLAB live scripts, learned the format and conventions from the examples, and generated new Fourier analysis content — code, documentation, everything. It used three or four tools on its own, making decisions about what to read, what to generate, and how to structure the output.

I used the Matrix analogy to explain what we'd just seen: "I don't know if some of you saw the movie The Matrix... 'I know Kung Fu,' right? Like he plugs himself into the skill and then he knows." Teaching Claude how to write MATLAB live scripts through structured documentation — that was the agentic part. Not just generating text, but autonomously learning and applying a format.

> "It's a spectacle. Like this just now. It turns into a performance. This thing is insane."

And the practical advice I gave right after: "Always read the code."

Ascension's arc during that meeting was the most rewarding part. She started skeptical — "Not yet, Yann. But I'm sure you will impress me." She ended engaged, seeing the potential for scaling educational content production on GitHub and File Exchange. The live demo did what slides never could.

## The Blog Post Feedback Loop

Around the same time, a parallel conversation was shaping how I thought about all of this.

A colleague had given me feedback on a blog post draft — the one about automating documentation with the MCP Core Server. Their response cut right to the core:

> "Based on the first paragraph, it sounded like you were going to show me how to take an existing script/analysis and get that ready for GitHub. But the workflow below starts from scratch and delegates the analysis to the LLM as well. I actually really liked the idea that you were going with in the first paragraph — do we have like an initial version of the script that we can start from? That way it's still the human doing the 'interesting' parts, and then you're using the AI to do the 'tedious' parts?"

I read that three times. It crystallized something I'd been circling around in every presentation, every demo, every late-night terminal session: **the human does the interesting parts, AI handles the tedious parts.** Not AI replacing humans. AI as amplifier.

This wasn't a new idea — but hearing it reflected back from a colleague who had independently arrived at the same framing made it feel like a thesis, not just a hunch. It connected the presentations back to the book's central question: what is this relationship, actually?

## The Book Club — Co-Intelligence as Mirror

If the presentations were about showing what Claude Code could do, the Marketing Book Club was about wrestling with what it all meant.

Kyle, Jacob, and I co-organized the club around Ethan Mollick's "Co-Intelligence." The choice was deliberate — Mollick's book explores practical frameworks for human-AI collaboration, and I'd re-listened to the audiobook recently. It was still remarkably relevant, even though it had been written before the agentic AI wave arrived.

The first session — Introduction and Chapter 1 — went places I didn't expect.

Mollick opens with the concept of "Sleepless Nights" — that first visceral encounter with AI that keeps you up. The participants shared their own moments. Kyle had perhaps the most striking one: someone had replicated six months of his market analysis work with a single deep research prompt in thirty minutes. "70% of the way there," he said. His reaction was immediate: "I was like, well, I'm out of a job."

Six months of work. Thirty minutes. Seventy percent. Those numbers tell a story that no slide deck can.

The discussion spiraled into territory that felt more like philosophy than a marketing meeting. Mollick's "Alien Mind" metaphor — AI as fundamentally non-human intelligence — resonated with what I'd been experiencing. AI doesn't think like us, but that's exactly what makes it a powerful thinking partner. If it thought like us, it would have the same blind spots.

I showed them ChatGPT's memory feature, which described me in absurdly flattering terms — "deep technical," endlessly praiseworthy. The room laughed. This was sycophancy in action, the AI telling you what you want to hear. I contrasted it with my experience of Claude pushing back on my strategic memo in the first week. The difference mattered.

Then I introduced Jean Claude — my personal AI agent on Telegram, complete with a French accent. I called the concept "productive anthropomorphism." Giving AI a persona and a name isn't a cognitive trap — it makes collaboration more intuitive, more natural. You don't anthropomorphize your spreadsheet, but maybe you should anthropomorphize your thinking partner.

The most substantive exchange came when I posed a question I'd been sitting with for weeks:

> "When AI starts writing good code, what is the part of your identity that you feel is threatened, if any?"

David Barnes paused. "I really like that articulation. About somewhat of the identity. It's not something I've thought about before."

I tried to frame it honestly: "If intelligence is just so cheap, so accessible, so scalable, what is me?... It's not necessarily insecurity, it's evolution."

I described my personal timeline as having three eras — the OpenAI days, "Google is so back," and now Claude Code. "There's BC — Before ChatGPT. Now there's also BCC — Before Claude Code."

The session ended with a message I'd been building toward across all the presentations and conversations: "If you can think of it as an AND — if we can do for humans AND for AI, then maybe we have something here." MathWorks should serve both humans and AI agents. Not zero-sum. AND.

## Resistance and Real Concerns

I'd be painting a dishonest picture if I suggested everyone walked out of these sessions converted. They didn't. And the pushback wasn't ignorance — it was legitimate concern.

Jeff raised the desktop-versus-cloud tension that ran through the company like a fault line. Agentic tools needed desktop software installed to be most effective, but the education market was demanding a cloud-first experience. That wasn't a problem I could demo my way out of.

The cost conversation came up in every session. "With great powers come great consumptions," I'd say, and it always got a knowing laugh. The $200-a-month subscription with daily limits was real. I was honest about it: "I have a 5-hour window where I start in the morning and then until 2... at some point I'm eating 100% and then I cannot work anymore. I need to go and chat with colleagues."

The governance gray areas were real too. What could AI-generated content be used for internally? Externally? Where was the line? "Very gray area" was the consensus, and nobody had a satisfying answer.

And then there was the elephant in the room that I tried to address head-on: "This is a controversial topic that puts pressure on our very business model." If AI could write MATLAB code, what happened to the value proposition of MATLAB itself? I didn't pretend to have the answer. But I did tell the room: "Don't shoot the messenger. I'm just sharing what's currently out there in the market."

These concerns weren't obstacles to adoption. They were evidence that the conversations mattered. Easy ideas don't generate pushback. Only ideas that challenge the status quo do.

The governance question, in particular, hung over every session like a fog that nobody could quite disperse. What could AI-generated content be used for internally? What about externally? If Claude drafted a competitive analysis, could it go into a customer-facing presentation? If it generated MATLAB code examples, who owned the intellectual property? "Very gray area" was the consensus, and nobody — not in marketing, not in legal, not anywhere I could find — had a satisfying answer yet. The honest response was that we were all figuring it out together, in real time, and pretending otherwise would have been the worst kind of evangelism.

> "The question you need to ask yourself now is not what it can do, but what it cannot do."

## From User to Advocate

Looking back at those six weeks, the trajectory surprises me. I walked into the pilot as someone who'd been asked to evaluate a tool. I walked out as something closer to an internal organizer.

At the end of the educator meeting, after Ascension's skepticism had turned to engagement and the team had seen Claude Code work in real time, I proposed creating a new Gen AI Tiger Team specifically for Educator Programs. Not a vague "let's keep talking about this" — a concrete team with scheduled sessions, a backlog of use cases to explore, and a commitment to document what worked and what didn't. The room said yes. We discussed follow-up sessions for the remaining use cases: community toolboxes, conference report-outs, and more.

That proposal was one piece of a larger pattern. I was also co-leading the Marketing Book Club on human-AI collaboration, creating onboarding materials for other MathWorkers, and sharing internal tools — the MATLAB Central MCP server, the skills repos, the philosopher-named tool chain.

The presentations evolved because I evolved. Week 2 was about workflows. Week 3 was about technical possibilities. Week 6 was about meeting people where they were. The book club was about grappling with what it all meant for who we are and what we do.

What started as "report back on your usage" became something more: an argument that we needed to surf on the wave, because otherwise we were going to get crushed.

But here's the thing I didn't expect. The most valuable part of having a thinking partnership wasn't what it did for me — it was what it taught me to share. Every demo, every slide, every uncomfortable question from a skeptical colleague pushed me to understand the technology more deeply, articulate its implications more clearly, and confront its limitations more honestly.

The evangelist doesn't just spread the word. The evangelist refines it.

And I was about to refine it further — in the most intense way possible. The hackathon was coming.
