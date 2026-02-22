---
title: "Chapter 4: The Competitive Intelligence Machine"
status: draft-v1
last_editor: claude
notes: "Covers how Claude became a research partner for competitive intelligence — the pattern, the examples (PIDO, neuroscience toolboxes, MATLAB community), and what this meant for the PM role"
---

# Chapter 4: The Competitive Intelligence Machine

The philosopher tools had given me a taste of building. But building wasn't the only thing that happened in those early weeks. Alongside the CLI tools and the PyPI packages, a completely different body of work was taking shape — one that had nothing to do with code and everything to do with thinking.

Claude was becoming my research partner. And the research was getting serious.

## The Pattern

If you are like me — a product manager at a technology company — you've spent a meaningful fraction of your career doing competitive intelligence. Reading analyst reports. Scanning press releases. Sitting in meetings where someone presents a slide that says "Market Size: $X Billion" and everyone nods as if the number is more than an educated guess.

The traditional workflow is slow and fragmented. You gather information from a dozen sources, synthesize it in your head, write it up in a memo, circulate it for feedback, revise, and eventually arrive at something useful — weeks after you started. By then, the market has moved.

With Claude, a new pattern emerged. It was simple, repeatable, and remarkably effective:

1. **I bring the question.** A company, a technology, a market segment. Something I need to understand deeply for strategic planning.
2. **Claude researches broadly.** Not just surface-level facts — deep dives into market dynamics, competitive positioning, technology trends, customer segments.
3. **Together, we extract implications.** This is the part that matters. Not "what is the market size?" but "what does this mean for us? Where are the opportunities? Where are the threats?"

This wasn't just fact-gathering. It was thinking partnership applied to strategy. And the volume of what we produced shocked me.

## The PIDO Deep Dive

The first major competitive intelligence effort was about a market I'd been tracking: Process Integration and Design Optimization — PIDO, for those who live in the engineering software world.

In a traditional workflow, building a comprehensive market analysis of PIDO would take me the better part of a week. I'd need to identify the key players, understand their positioning, map the competitive landscape, estimate market sizes from fragmented data sources, and connect it all to MathWorks' strategic positioning.

With Claude, I typed a single prompt. What came back was a comprehensive analysis: a $200–220M USD market in 2024, growing at 10–12% CAGR. But the numbers were the easy part. What made it valuable was the strategic layer — the implications for MathWorks' positioning, the gaps in our current approach, the segments where we were strong and the ones where we were vulnerable.

I sat with the output for a while, cross-checking claims, testing the logic. Some of the analysis I'd adjust. Some of the market estimates I'd refine with internal data Claude didn't have access to. But the foundation was solid. The synthesis was genuinely useful. And it had taken an hour instead of a week.

This is the part that most people misunderstand about AI-assisted research. They imagine you press a button and receive a report. That's not how it works — or at least, that's not how it works well. What actually happens is a dialogue. I'd push back on Claude's framing. Claude would defend it or adjust. I'd bring internal context — things I knew about our product roadmap, our customer conversations, our engineering investments — that Claude couldn't access. Claude would integrate that context and sharpen the analysis.

The output was neither mine nor Claude's. It was ours.

## The Neuroscience Toolbox Analysis

The second example was more technical and, in some ways, more revealing. Industry marketing needed a competitive analysis of the neuroscience research tools ecosystem — specifically, how MATLAB-based tools compared to the rising Python alternatives.

Claude dove into the landscape: FieldTrip, EEGLAB, MNE-Python, and the constellation of smaller tools orbiting them. The research surfaced something I hadn't fully appreciated. EEGLAB was leading in academic citations at 21,700+. But MNE-Python was showing the fastest growth trajectory — 3,200 GitHub stars, 416 contributors, and the kind of community momentum that's hard to reverse.

The strategic insight was pointed: a clear bifurcation was emerging between MATLAB-based tools (historically dominant, deeply embedded in research workflows) and Python-based alternatives (rapidly growing, zero licensing costs, open-source community energy). This wasn't just a technical comparison. It was a strategic signal about where the neuroscience research community was heading.

This is the kind of analysis that, delivered in a deck to industry marketing, changes how people think about their market. And it emerged from a conversation, not a consulting engagement.

## MATLAB Community Intelligence

The third stream of research was the most internally focused. Colleagues had started coming to me with requests.

"Can you tell me what users say about the Live Editor?" — that was Rohan.

"Can you tell me if a feature like Live Editor is useful and loved?" — that was Johanna.

These weren't idle questions. They were the kind of product intelligence that normally requires weeks of manual analysis — combing through MATLAB Answers, reading forum threads, categorizing sentiment, identifying patterns. The kind of work that everyone agrees is important and nobody has time to do.

Claude changed the equation. By analyzing MATLAB community data — forum posts, questions, answers, the whole corpus of user-generated content — we could extract product intelligence at a pace that made it practical. Not perfect. Not a replacement for proper user research. But a first pass that was fast enough to be useful and comprehensive enough to be informative.

The fact that colleagues were bringing me their questions told me something important. The competitive intelligence work wasn't just useful to me — it was becoming useful to the people around me. The research partner I'd found in Claude was turning into something closer to a research service.

## What Claude Brought, What I Brought

Here's the honest accounting of who contributed what.

**Claude brought breadth.** The ability to survey a landscape quickly, to pull together information from diverse sources, to identify patterns across large bodies of data. When I asked about the PIDO market, Claude could synthesize information from analyst reports, company announcements, technology trends, and market dynamics — the kind of breadth that would take me days to assemble manually.

**I brought judgment.** The ability to say "that market estimate feels high" or "you're missing the political dimension of this competitive dynamic" or "that's technically correct but strategically irrelevant." I knew which of our products competed where. I knew which customer segments we were winning and which we were losing. I knew the internal politics — which initiatives had executive sponsorship and which were struggling for resources.

**Together, we produced synthesis.** Neither of us could have done it alone. Claude without my judgment would produce technically accurate but strategically naive reports. My judgment without Claude's breadth would produce insightful but narrow analyses that took too long to assemble.

This is the pattern that Ethan Mollick describes in *Co-Intelligence* — the idea that human-AI collaboration isn't about automation but about augmentation. You don't replace the human. You amplify them. And you don't use AI as a search engine. You use it as a thinking partner.

## The Sleepless Nights

There's a moment that Mollick writes about — the first time AI does something that makes you lie awake at night. Not in fear, exactly, but in a disorienting sense that the ground has shifted.

My colleague Kyle Hakes had his moment during the marketing book club I organized around *Co-Intelligence*. He told the group that someone had replicated six months of his market analysis work with a single deep research prompt — in thirty minutes. "70% of the way there," he said. His reaction: "I was like, well, I'm out of a job."

He was joking. Mostly. But the feeling was real. When you've spent years developing expertise in market analysis and competitive intelligence, and then you watch an AI produce something that's 70% as good in 0.1% of the time, the natural response is existential unease.

I felt it too. The competitive intelligence work I was doing with Claude wasn't just faster than my old workflow — it was a different thing entirely. The old workflow was labor-intensive and slow, which meant I was selective about what I researched. I only deep-dived into markets that justified the time investment. With Claude, the marginal cost of research dropped close to zero. I could explore markets I'd never have bothered with before, just because the friction was gone.

This changes the job. Not eliminates it — changes it. The product manager who spends 80% of their time gathering information and 20% thinking about it now spends 20% gathering and 80% thinking. The bottleneck shifts from research to judgment. And judgment, it turns out, is the part that's hard to automate.

## The Quality Question

I want to be honest about something. Not everything Claude produced was gold.

Some market estimates were off — based on outdated data or extrapolations that didn't account for recent disruptions. Some competitive analyses missed nuances that only someone embedded in the industry would catch. Some strategic recommendations were plausible but generic — the kind of thing any competent consultant would suggest.

The 70% number Kyle mentioned is about right. On a first pass, Claude gets you 70% of the way to a solid competitive intelligence report. The remaining 30% — the part that requires insider knowledge, strategic nuance, and the kind of judgment that comes from years of sitting in customer meetings — that's still you.

But here's the thing: 70% in thirty minutes versus 100% in two weeks is not a close comparison. The first pass gives you a foundation to build on, a framework to critique, a starting point that's dramatically better than a blank page. And the iteration from 70% to 95% — adding your judgment, your context, your strategic perspective — takes hours, not weeks.

The competitive intelligence machine wasn't perfect. But it was fast, it was comprehensive, and it freed me to do the part of my job that actually requires a human: deciding what the information means.

## What This Changed

By the end of those early weeks, I had produced competitive intelligence reports covering markets I'd never have had time to analyze before. Each one followed the same pattern — Claude's breadth plus my judgment, iterated through conversation until we arrived at something genuinely useful.

But the bigger change was subtler. My relationship to information itself had shifted. I'd gone from being a person who carefully selected which questions to research (because research was expensive in time) to a person who could research anything, anytime, and focus my energy on the higher-order question: *So what?*

The "so what" is where product managers earn their keep. And Claude had cleared the path to get there faster.

The competitive intelligence work was happening alongside the philosopher tools, alongside the blog posts, alongside the strategic memos. All of it feeding into a growing body of work that would need a unifying infrastructure. That infrastructure had a name — the Model Context Protocol — and it was about to change everything. But that's the next chapter.
