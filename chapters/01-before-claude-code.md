---
title: "Chapter 1: Before Claude Code (BCC) — The ChatGPT Era"
status: draft-v1
last_editor: claude
notes: "Covers the pre-Claude AI landscape, vibe coding origin story, and projects that set the stage"
---

# Chapter 1: Before Claude Code (BCC) — The ChatGPT Era

If you are like me, you were probably deep in the ChatGPT era by mid-2025 and didn't even realize a seismic shift was coming.

Everyone I knew was experimenting. Product managers were tip-toeing with the technology, prototyping with AI services or locally with Ollama. Marketing teams were generating content drafts. Developers were starting to evaluate copilots and some were happy enough about the productivity gain it was providing. It's in mid-2025 that the term "vibe coding" entered the vocabulary — this idea that you could describe what you wanted in plain language and watch an AI conjure it into existence. It felt like magic, and like most magic, we didn't fully understand the trick.

I was spending all the free hours I had on AI. I had my ChatGPT subscription, my collection of apps connecting to the OpenAI web services, and a growing sense that something fundamental was changing about how software would be built. But everything I did with AI in those years prior to Claude and agentic involved a lot of copy-pasting, trial and error, and manual integration.

That was about to change. But first, let me tell you about the night I built a website in my kitchen.

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

This broke something in my mental model. I had always assumed that building a useful product required sustained effort — iteration, marketing, user research, the whole product management playbook I'd internalized over years at MathWorks. But here was a website I'd built in a kitchen at 2am with an AI, and it was generating more organic traffic than projects I'd spent months planning.

The lessons hit me one at a time over the following days:

- **Vibe coding can produce genuinely useful, discoverable products.** Not just demos — real things that real people find and use.
- **The "demo that becomes real" pattern is more powerful than planned projects.** When you remove the friction of building, you can test ideas at the speed of conversation.
- **Domain purchases at 2am sometimes pay off.** I'm not saying it's a strategy. But I'm not saying it isn't.

## Other Pre-Claude Projects

recettesdezoe.com wasn't my only experiment in the pre-Claude era. That summer and fall, I'd been building a small portfolio of AI-assisted projects, each one pushing a little further into what was possible.

**GhostRunners.app** was probably the most ambitious. I'm a cycling enthusiast, and I wanted something that didn't exist: real-time analytics that could compare my current ride to previous efforts on the same route — essentially racing against my own ghost, like in a video game. I built it using MATLAB Mobile for data capture, MATLAB Online for the analysis, and Python with the Garmin FIT SDK for parsing the ride files. I even recorded YouTube videos documenting the process on my channel @yannspeaksai. It wasn't pretty code, but it worked, and it scratched an itch no existing app could reach.

**OpenAI Codex** came next — first as a VSCode integration where I could vibe-code small HTML and JavaScript apps, and later as a cloud-based agent that could run data analysis hands-off. The progression was revealing: from AI helping me write code, to AI writing code while I watched, to AI writing and running code while I did something else entirely.

**OpenAI Canvas** I tried once and largely abandoned. For single-page web apps, I found myself defaulting to the Claude app — either on mobile or desktop. Even before Claude Code entered the picture, something about Claude's approach to conversation was pulling me in.

## The Pattern I Couldn't See Yet

Looking back, these projects trace an arc I couldn't see at the time. Each one was a single interaction — a prompt, a session, an output. I'd build something, feel the rush of creation, and move on. There was no continuity between sessions, no shared context, no sense that the AI remembered or built upon what we'd done before.

Every conversation started from zero. Every project was an island.

I didn't know it yet, but I was about to discover what happens when AI stops being a tool you pick up and put down, and starts becoming something closer to a collaborator who remembers where you left off.

December 2025 was coming, and with it, an invitation to a pilot program that would change how I thought about all of this.
