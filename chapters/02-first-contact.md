---
title: "Chapter 2: December 2025 — First Contact"
status: draft-v1
last_editor: claude
notes: "Covers the MathWorks pilot, strategic conversations, blogging workflow, and the moment Claude became more than a chatbot"
---

# Chapter 2: December 2025 — First Contact

The email arrived sometime in early December. MathWorks was running a pilot program — Claude Code for non-developers. A handful of product managers would get access, with one responsibility: report back on what they found in Q1 2026. I was one of the lucky early testers.

But I didn't start with Claude Code. That would have been too big a leap for someone coming from the ChatGPT world. Instead, I started where most people would: Claude Desktop.

The Desktop app is a very approachable interface for those who come from chat apps like ChatGPT. Same text box, same conversational flow, same satisfying rhythm of typing a question and watching an answer materialize. The first question I asked myself was simple: *What kind of project can I tackle with Claude?*

The answer surprised me. Because it wasn't code.

## The Strategic Awakening

My very first substantive conversation with Claude wasn't about building something — it was about *thinking* about something.

I had been drafting a memo to our Director of Product Marketing. The core thesis was about a strategic tension I'd been mulling over for weeks: the difference between being best-in-class at coding agents and being best-in-class at building tools that coding agents call. For a company like MathWorks, this wasn't an abstract distinction — it was the question that would shape our positioning in the age of agentic AI.

I won't share the full memo here, but I can tell you what happened when I brought it to Claude. I expected what I'd gotten from ChatGPT — a polished summary, maybe some rephrased bullet points, the kind of agreeable helpfulness that makes you feel good but doesn't make you think harder.

Instead, Claude fact-checked my market claims. It confirmed that Cursor had crossed $1B ARR, that Claude Code had reached a $1B run-rate within six months of its launch. Then it stress-tested my arguments — praised the strategic logic but called out gaps. Where were the concrete examples? What about the risks I'd glossed over? The success metrics were too vague. The feedback was direct, specific, and genuinely useful.

I sat with that for a moment. This wasn't what I was used to from AI conversations. ChatGPT would have told me my memo was great and offered to make it longer. Claude told me where it was weak and how to make it stronger.

> *This set the tone for everything that followed: Claude as thinking partner, not just tool.*

I went back and rewrote sections of the memo. The final version was meaningfully better — not because Claude wrote it for me, but because Claude pushed back on the parts that needed pushing. It was the kind of feedback you'd hope to get from a sharp colleague, delivered without ego or politics.

That experience stayed with me. Sitting with a sharper memo on one side of the conversation, I found myself thinking not just about the argument I'd improved, but about what the interaction itself *meant*. I had just been pushed to think harder — by a machine. Not nudged toward an answer, not flattered into confidence. Actually challenged. I wondered how many other people were having this moment, and how many still weren't.

I was also creating a presentation on the impact of agentic AI on the market of scientific and technical computing — something that most companies must have been asking themselves at that point. One diagram I developed described the chasm between the early adopters of agentic AI, evaluating solutions like Claude, and the majority still associating AI with chatbots like ChatGPT. That chasm was real, and I was watching myself cross it in real time.

## The Blog Posts Begin

Within the first week, the strategic conversations spilled over into something more tangible. I had taken over the MATLAB AI Blog on September 1st, and now, with Claude as a collaborator, I found myself drafting posts at a pace I hadn't thought possible.

The list grew quickly:

- MATLAB MCP Core Server — the foundational post about connecting MATLAB to the agentic ecosystem
- Connecting to Hardware — data acquisition and image acquisition devices via MCP
- Deploying a Quant Agent — financial analysis with MATLAB as the computational backbone
- Antigravity + MATLAB — a playful post that turned out to be wicked good
- Giving Local AI Agents the Ability to Use MATLAB with MCP
- Building an Optimization Agent
- Automating the Documentation of MATLAB Analysis

A series of posts in the pipeline within the first week. This wasn't because I suddenly became a faster writer. The content was still mine — the ideas, the technical depth, the perspective on where MATLAB fit in the agentic AI landscape. What changed was the workflow.

Claude handled the boring parts. The formatting, the structuring, the initial research and benchmarking, the first-pass drafts of sections where I knew what I wanted to say but didn't want to stare at a blank page. This freed me to concentrate on the two things that actually mattered: **ideation and code.** The thinking and the building. Everything else was scaffolding, and Claude was excellent at scaffolding.

## Claude Analyzes My Voice

Then something happened that I hadn't expected.

I asked Claude to study my published writing — the blog posts, the technical articles, the presentation scripts — and tell me what patterns it found. I wanted to know if my writing had a recognizable voice, and if so, whether Claude could capture it.

What came back was a plain text file. A `.md` file, formatted like any other Markdown document, that Claude called a "skill." Not code. Not a configuration. Just structured prose describing how I write — and instructions for how to apply it.

```markdown
---
name: yann-blog-voice
description: Write in Yann Debray's established blogging style for MathWorks technical posts
---

## Voice & Tone
Conversational but technically grounded. Acknowledge what you don't know.
Make the reader feel like a peer discovering something alongside you.

## Signature patterns
- **Opening hooks**: "If you are like me, you are probably familiar with..."
- **Colleague references**: "my dear colleague [Name]"
- **Honest limitations**: "I'm not an expert in Finance!"
- **Closings**: "Happy hacking, and let me know what you build! 👋🏻"
- **Structure**: Problem → Demo → Walkthrough → Resources
```

I read through it with a strange mix of recognition and surprise. These were patterns I'd developed over years of writing, and I'd never consciously catalogued them. Claude had done it in a single conversation.

More importantly, it *worked*. When I asked Claude to draft sections using this skill, the output sounded like me. Not a generic approximation of a tech blogger, but specifically like me — my rhythms, my tendency to acknowledge what I don't know, my habit of opening with a shared experience. It was the difference between a cover band playing the notes and actually capturing the feel.

The writing voice skill was just the first one. I quickly saw that the format could capture almost any repeatable workflow. Converting conference notes into an internal presentation. Turning a YouTube transcript into a structured blog post. Taking a MATLAB analysis and automatically generating its live script documentation — something I later wrote about in detail on the [MathWorks blog](https://blogs.mathworks.com/deep-learning/2026/02/09/automate-the-documentation-of-your-matlab-analysis-with-agentic-ai/). Each of these was a transformation: input of one type, output of another, with the skill defining the rules of conversion.

The more ambitious examples came later: a skill for embedded AI workflows, walking Claude through the steps of taking a machine learning or deep learning algorithm and targeting it to a chip. The kind of pipeline that normally lives in an engineer's head — implicit, tribal, undocumented. A skill made it explicit.

But I want to be honest about the limitation. Skills are non-deterministic. They're just text. Claude reads them and interprets them, and that interpretation can vary. Two runs of the same skill won't produce identical results. This isn't a bug — it's the nature of language models — but it's a real constraint if you need reproducibility.

What made people love them anyway was the simplicity. No code to write. No system to configure. Just a Markdown file that says: *here's how this works, here's what good looks like, do it this way.* My colleagues started gravitating toward skills almost immediately. They recognized them as something they'd always needed but never had a format for: a way to capture their own know-how and make it portable.

"I can write down how I do competitive analysis," one colleague told me. "And then Claude can do it the same way."

That's the idea. Skills as institutional memory. Skills as the interface between human expertise and AI execution.

There's a more dramatic way to put it — involving The Matrix and Keanu Reeves downloading kung fu in seconds — but that story belongs to Chapter 7, when we actually watched it happen live.

This was when I started to understand that what was happening went beyond productivity. A tool that makes you faster is useful. A tool that learns your voice and helps you sound more like yourself — that's something else entirely.

## Something Was Shifting

By the end of that first week with Claude, I had:

- Sharpened a strategic memo through genuine intellectual sparring
- Drafted the foundations for several blog posts
- Had my writing voice analyzed and codified in a way I could actually use

But the numbers don't capture what was really changing. It was the *quality* of the interaction. Each conversation with Claude built on the ones before it. There was continuity — a shared context that grew with every exchange. When I mentioned the "agent calling toolboxes" strategy, Claude knew what I meant. When I referenced the blog voice, Claude could apply it. When I circled back to an idea from two days ago, I didn't have to re-explain everything from scratch.

The conversations had something I'd never experienced with an AI before: **honest feedback.** Claude didn't just agree with me. It pushed back. It identified weaknesses. It suggested alternatives I hadn't considered. And it did all of this without the social dynamics that make human feedback complicated — no ego, no office politics, no tiptoeing around seniority.

What had started as a productivity experiment — can this tool help me write blog posts faster? — was becoming something I didn't have a name for yet. It wasn't a chatbot. It wasn't an assistant. It was starting to feel like a colleague who happened to be available at 10pm and never needed coffee.

I didn't know where this was headed. But I knew that the one-shot, disposable AI interactions of the ChatGPT era were behind me. Whatever came next would be built on continuity, shared context, and the kind of thinking partnership I was only beginning to understand.

Looking back, I'd later distill this first week into a slide I called "Agentic 101" — the foundation layer. Claude Desktop as the gateway drug. Python first, then MATLAB. It was the simplest of the four weekly lessons I'd eventually present to colleagues, but it was also the most important. Everything that followed — the philosopher tools, the agent orchestration, the terminal becoming home — grew from this first week of unlearning what I thought AI could do.

The philosopher tools were about to arrive. But that's the next chapter.
