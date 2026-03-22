---
title: "Chapter 1: Before Claude Code (BCC) — The ChatGPT Era"
status: draft-v2
last_editor: claude
notes: "Added MathWorks/pilot framing to opening; fixed broken kitchen transition; inserted Copilot/Jacob enterprise section (Sep 2025); expanded friction texture throughout"
---

# Chapter 1: Before Claude Code (BCC) — The ChatGPT Era

By mid-2025, you were probably deep in the ChatGPT era — like me — and didn't even realize a seismic shift was coming.

Everyone I knew was experimenting. Product managers were tip-toeing with the technology, prototyping with AI services or locally with Ollama. Marketing teams were generating content drafts. Developers were starting to evaluate copilots and some were happy enough about the productivity gain it was providing. It's in mid-2025 that the term "vibe coding" entered the vocabulary — this idea that you could describe what you wanted in plain language and watch an AI conjure it into existence. It felt like magic, and like most magic, we didn't fully understand the trick.

I was spending all the free hours I had on AI. I had my ChatGPT subscription, my collection of apps connecting to the OpenAI web services, and a growing sense that something fundamental was changing about how software would be built. But in practice, working with AI meant a lot of friction. You'd generate something useful, copy it into another tool, realize the context was lost, paste it back, re-explain what you were trying to do. Every session started fresh. Every project lived in its own bubble. The AI had no memory of you, no awareness of what you'd built together before. It was capable and frustrating in equal measure — like working with a brilliant colleague who had amnesia.

That was about to change. But the first crack in that model didn't come from Claude — it came on Valentine's Day, 2025, from an unlikely source.

## The First Agent

On February 14th, 2025 — Valentine's Day, of all days — Perplexity launched Deep Research. I remember the date because it felt like a gift, though not the kind you'd expect.

Up until then, AI was something you talked *to*. You asked a question, it answered. You wrote a prompt, it generated text. The mental model was a very smart search box, or a very patient assistant who never got tired of your follow-up questions. The loop was always: me type, AI respond, me copy, me paste, me think.

Deep Research broke that loop. You gave it a question — a real, meaty one — and it went away. It searched. It read. It synthesized across dozens of sources. It came back with something that looked less like a chatbot response and more like a document a junior analyst might produce after a week of work. The first time I used it for a competitive analysis at MathWorks, I had that specific feeling that something had shifted: I hadn't helped it do research. It had done research, and showed me the results.

A colleague of mine had a reaction that stayed with me — watching someone replicate months of his market analysis work with a single deep research prompt in under thirty minutes. I'll come back to that story in Chapter 4, when we get into the competitive intelligence work in more *depth*. But the seed of it was here, in early 2025, the first time a research task felt genuinely delegatable.

Still, there was a ceiling. Deep Research was powerful for synthesis, but it remained a one-shot interaction. You asked, it answered. There was no memory between sessions, no ongoing project, no sense of working *with* something over time. The AI was a very capable contractor you hired for a single job and never saw again. Next week, when the follow-up question came, you'd have to re-hire, re-brief, and re-explain everything from scratch — hoping the output would be consistent with what came before.

I didn't know yet what continuity would feel like. But I was about to get a taste of something closer to it.

## The Vibe Coding Origin Story

Late August 2025. My in-laws were visiting, shortly after GPT-5's release. My father-in-law and I were in the kitchen late at night — the kind of hour where ambitious ideas feel perfectly reasonable.

> **Me**: "What website or web app would you like to develop?"
> **Father-in-law**: *looks around the kitchen, spots a recipe book*
> **Me**: "Ok, let's build a website with French recipes."

Single prompt. Single session. I opened ChatGPT, described what I wanted — a clean, browsable website of French recipes — and watched it generate the HTML, CSS, and JavaScript. The whole thing took maybe an hour, most of which was us discussing which recipes to feature and laughing about the absurdity of what we were doing.

That same night, sometime around 2am, I purchased the domain on Cloudflare. recettesdezoe.com was born — named after my daughter Zoé. We deployed it right there, my father-in-law watching over my shoulder as the site went live.

It was a demo. A party trick. A thing I'd built to show what was possible.

Or so I thought.

## The Surprise Discovery

Four months later — December 2025 — I was poking around my Cloudflare dashboard for an unrelated reason when something caught my eye. The analytics for recettesdezoe.com showed **1,300+ visitors in the past month.**

I stared at the number. Zero edits since launch. Zero marketing. Zero SEO work. Zero social media promotion. Nothing. I had literally forgotten the site existed for weeks at a time, and over a thousand people had found it, visited it, and presumably cooked something from it.

This broke something in my mental model. I had always assumed that building a useful product required sustained effort — iteration, marketing, user research, the whole product management playbook I'd internalized over years in my job. But here was a website I'd built in a kitchen at 10pm with AI, and it was generating more organic traffic than projects I'd spent months planning.

The lessons hit me one at a time over the following days:

- **Vibe coding can produce genuinely useful, discoverable products.** Not just demos — real things that real people find and use.
- **The "demo that becomes real" pattern is more powerful than planned projects.** When you remove the friction of building, you can test ideas at the speed of conversation.
- **Domain purchases at 10pm sometimes pay off.** I'm not saying it's a strategy. But I'm not saying it isn't.

## What AI Looked Like at Work

In September 2025, a month after the kitchen demo, I gave a presentation to the broader product marketing department at MathWorks with my colleague Jacob. We called it "GenAI Tools for Modern Tech Marketers." The focus was on Microsoft Copilot — the AI tools most widely available inside the organization — and we structured it around three personas: the product manager, the developer, and the outbound marketer.

For product managers, two tools stood out. The first was the Researcher — Microsoft's version of the deep research capability that ChatGPT and Perplexity had introduced earlier that year. You could ask it to analyze a market, summarize a competitive landscape, synthesize a body of documentation, and it would produce something genuinely useful. The second was the Analyst — a data analysis tool integrated directly into the Microsoft 365 environment, with access to your Excel files. I used it to slice product usage data across dimensions that would have taken me hours to do manually.

The audience was receptive. Some people in the room had their own "sleepless night" moment during the session — a first encounter with AI that hit differently than they expected. We had built something that felt like real progress.

And it was. But preparing that presentation also clarified something I hadn't fully articulated before: every one of these tools operated in isolation. The Researcher didn't know what the Analyst had found. Neither of them knew what project you were working on, what decisions you were trying to make, or what you'd already tried. You stitched the outputs together manually, in your own head, across a dozen open tabs. The AI was useful in each individual moment and absent everywhere in between.

That was the state of the art in the enterprise in late 2025. It felt like progress — until you started wondering what it would feel like if the AI actually stuck around.

## Other Pre-Claude Projects

recettesdezoe.com wasn't my only experiment in the pre-Claude era. That summer and fall, I'd been building a small portfolio of AI-assisted projects, each one pushing a little further into what was possible.

**GhostRunners.app** was probably the most ambitious. I was getting back on my bicycle, and I wanted to get better at it: so i looked at analytics that could compare my current ride to previous efforts on the same route — essentially racing against my own ghost, like in a video game. I built it using MATLAB Mobile for data capture, MATLAB Online for the analysis, and Python with the Garmin FIT SDK for parsing the ride files. I even recorded YouTube videos documenting the process on my channel @yannspeaksai. It wasn't pretty code, but it worked, and it scratched an itch and motivated me to exercise more.

**OpenAI Codex** came next — first as a VSCode integration where I could vibe-code small HTML and JavaScript apps, and later as a cloud-based agent that could run data analysis hands-off. The progression was revealing: from AI helping me write code, to AI writing code while I watched, to AI writing and running code while I did something else entirely.

**OpenAI Canvas** I tried once and largely abandoned. For single-page web apps, I found myself defaulting to the Claude app — either on mobile or desktop. Even before Claude Code entered the picture, something about Claude's approach to Artifacts was pulling me in.

## The Pattern I Couldn't See Yet

Looking back, these projects trace an arc I couldn't see at the time. Each one was a single interaction — a prompt, a session, an output. I'd build something, feel the rush of creation, and move on. There was no continuity between sessions, no shared context, no sense that the AI remembered or built upon what we'd done before. I remember coming back to GhostRunners two weeks after building it, wanting to add a feature, and spending the first twenty minutes just re-explaining what the project was, what the data structure looked like, and what I'd already tried. The AI was helpful — but it was meeting me for the first time, again.

Every conversation started from zero. Every project was an island.

I didn't know it yet, but I was about to discover what happens when AI stops being a tool you pick up and put down, and starts becoming something closer to a collaborator who remembers where you left off.

December 2025 was coming, and with it, an invitation to a pilot program that would change how I thought about all of this.
