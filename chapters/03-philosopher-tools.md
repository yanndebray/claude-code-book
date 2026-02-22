---
title: "Chapter 3: The Philosopher Tools"
status: draft-v1
last_editor: claude
notes: "Covers Week 2 — the shift from thinking partner to building partner, CLI tools named after philosophers, the reading list that fed the naming, and the creative momentum that followed"
---

# Chapter 3: The Philosopher Tools

The philosopher tools were about to arrive. That's how I closed the last chapter, and I meant it literally.

Week 2 brought a shift I hadn't anticipated. Claude wasn't just a thinking partner anymore — it was a building partner. The strategic memos and blog drafts from Week 1 had been intellectually rewarding, but they were still fundamentally about *writing*. Now I found myself doing something different: building software. Real, distributable, reusable software. And the tools that emerged came with names I didn't expect.

## From Skills to Tools

The key insight of Week 2 was deceptively simple: **density — less is more.** Build tools, not just skills.

Let me explain. In Week 1, Claude had helped me create "skills" — structured prompts that captured my writing voice, my presentation style, my analytical frameworks. They were useful, but they were also fragile. A skill lives in a conversation. You invoke it, it shapes the output, and then it vanishes when the session ends. It's a one-shot thing — powerful in the moment, but not reusable in any systematic way.

A CLI tool is different. A CLI tool is a piece of software that lives on your machine, that agents can call deterministically, that follows a workflow you've defined and tested. It doesn't depend on the quality of your prompt or the mood of the conversation. It just runs.

This distinction — between a prompt that works once and a tool that works every time — turned out to be the difference between playing with AI and actually building with it. And once I understood that, the tools started coming fast.

## The Army of Philosophers

If you are like me, you probably name your projects something boring and descriptive — `slide-generator`, `media-converter`, `search-tool`. Functional. Forgettable. I'd done this my whole career.

But something about building with Claude changed the naming instinct. Maybe it was the late-night energy. Maybe it was the reading I'd been doing all year. Maybe it was the feeling that these tools deserved names that carried meaning beyond their function. Whatever the reason, I started naming my tools after philosophers.

And once I started, I couldn't stop.

**montaigne.cc** was the first. A media processing toolkit for presentation localization — transcription, translation, audio and video processing, all powered by Google Gemini AI. Montaigne's *Essais* are the original explorations — a mind wandering across languages, cultures, and ideas, interpreting everything it encounters through the lens of personal experience. The tool does the same thing, in its own way. It takes content in one language and interprets it into another. It listens to audio and renders it as text. It crosses boundaries between media the way Montaigne crossed boundaries between disciplines.

**nietzsche.cc** came next. A presentation generator — a CLI where the `power` command generates slide decks. "The will to present." I know, I know. But hear me out. Nietzsche's Übermensch is about self-overcoming, about transcending the tedious and mundane to reach something higher. If you've ever spent three hours manually formatting a PowerPoint deck when the ideas were already clear in your head, you understand the appeal. The tool was my Übermensch moment — a way to transcend the drudgery and focus on what mattered: the ideas themselves.

There's another Nietzschean concept that fits even better: eternal recurrence. The idea that you should live as though you'd have to repeat every action for eternity. In automation, this is exactly what you want — a workflow so clean, so reliable, that running it again and again produces consistent results. Create, iterate, reuse. Eternal recurrence, but for slide decks.

**ricoeur.cc** was the one I was most proud of conceptually. A CLI search tool for conversation history — a way to dig through past dialogues and extract meaning from them. Paul Ricoeur's hermeneutic circle is the idea that you understand the parts through the whole, and the whole through the parts. Part, whole, part, whole — an endless loop of interpretation and reinterpretation. That's exactly what searching through conversation history feels like. You find a fragment, it reframes your understanding of the entire exchange, and that new understanding sends you looking for different fragments. The tool and the philosophy were almost uncomfortably aligned.

I even asked Claude to evaluate the naming. The feedback was characteristically direct: ricoeur.cc edged ahead on conceptual coherence — the mapping between the tool's purpose and the philosopher's theme was the tightest. But nietzsche.cc was more polished in UX, more immediately usable. Claude recommended building a shared landing page to tell the story of why these tools existed as a family. Not just a collection of utilities, but a suite with a philosophical backbone.

An army of philosophers. That's what I started calling them.

## Why Philosophers?

The naming wasn't random. It grew out of a reading list that had been building all year — a personal arc through books that, looking back, were preparing me for exactly this moment.

It started with Kafka's *The Trial*. The individual against the system, navigating opaque bureaucracies that operate by rules no one fully understands. If you've ever tried to introduce AI tooling into a large organization, you know this story intimately. The committees, the approval processes, the security reviews — Kafka wrote the manual on corporate AI adoption before AI existed.

Then Camus's *The Stranger*. Absurdism. The idea that life doesn't owe you meaning, so you'd better create your own. There's something deeply Camusian about vibe coding — this acceptance that the process is absurd, that you're building software by describing it in plain language to a machine, and that the appropriate response is not to demand it make sense but to embrace the creative freedom it offers.

Nietzsche's *Thus Spoke Zarathustra* was the big one. Will to power, self-overcoming, the three metamorphoses. More on that in a moment.

Plato's *Apology* — Socrates on trial, defending the examined life. Intellectual humility as a practice. The idea that wisdom begins with knowing what you don't know. Every time I typed "I'm not an expert in Finance!" into a blog post, I was channeling Socrates without realizing it.

Irvin Yalom's *The Schopenhauer Cure* bridged philosophy and practice — the idea that thinking about the world and doing something in the world aren't separate activities. Philosophy as therapy. Code as philosophy.

Then the modern voices: Harari's *Nexus*, framing AI as the next chapter in the human information story. Mollick's *Co-Intelligence*, providing the practical frameworks for working alongside AI systems.

> "The existentialists ask 'how should I live authentically?' while Mollick and Harari ask 'how should we live with AI?' These questions are not separate. The tools we build shape the lives we lead."

That synthesis emerged during a late-night conversation with Claude, and it became the philosophical thesis underneath everything I was building. The tools weren't just utilities. They were answers — my answers — to questions that philosophers had been asking for centuries.

## The Zarathustra Project

The philosopher tools and the reading list converged most dramatically in the Zarathustra project. I built a full voiceover script for a fifteen-slide presentation on *Thus Spoke Zarathustra*, and I built it using nietzsche.cc itself. The tool and its namesake, working together.

The presentation traced the arc of Nietzsche's masterwork: the prophet Zarathustra descending from his mountain after ten years of solitude. The Übermensch — not a superhero, but a concept of human self-overcoming. The three metamorphoses: the Camel who bears the weight of tradition, the Lion who rebels and creates freedom, the Child who plays and creates new values. The Last Man — Nietzsche's warning about a humanity so comfortable it stops striving. The Will to Power as creative drive, not domination. Eternal Recurrence as the ultimate test of how you choose to live.

Twelve to fifteen minutes of narrated content, generated from a tool I'd built with an AI, about a philosopher whose ideas had inspired the tool's name. If Nietzsche had known about recursion, he would have appreciated the structure.

## The Philosopher Rap Battle

And then — because creative momentum has a logic of its own — the rap battle happened.

Once you've named your tools after philosophers and built a presentation about Zarathustra, the next step is obviously an educational web app where philosophers debate each other in rap format. Obviously.

The concept was simple: pick two philosophers, set them against each other on a topic, and let the arguments fly — but in verse. Nietzsche vs. Schopenhauer was the flagship matchup. Master and student. Pessimism vs. affirmation. "The world is suffering" vs. "Embrace it all and will it again."

It was playful. It was absurd. It was exactly the kind of project that happens when you're building with a collaborator who doesn't get tired, doesn't judge your ideas, and responds to "What if we made philosophers rap-battle each other?" with genuine creative energy rather than a raised eyebrow.

This is something I didn't expect about building with Claude: the creative compound effect. Each project made the next one easier to imagine. The philosopher naming led to the reading list connections, which led to the Zarathustra presentation, which led to the rap battle. One idea feeding the next, accelerating, branching. Not because Claude was generating ideas autonomously, but because having a tireless collaborator meant I never had to stop and wonder "Is this too weird? Is this worth the time?" The answer was always: let's find out.

## The Developer Workflow

Behind the philosophical naming and the creative experiments, Week 2 was also when I became a real developer. Or at least, a closer approximation of one.

Python for CLI is fire. I'd known Python before, but building command-line tools with it — using `fire` for argument parsing, structuring projects as proper packages — felt different. These weren't scripts. They were software.

`uv` is life. The Python package manager that made everything faster — environment creation, dependency resolution, the whole toolchain. Once you've used `uv`, going back to `pip` feels like going back to dial-up.

Publishing to PyPI was the moment it felt real. My tools weren't just local scripts anymore. Anyone could `pip install` them. They existed in the world, with version numbers and documentation and download counts. Let the game begin.

GitHub Issues became my requirements management system. Instead of keeping a mental list of features to add, I'd have Claude generate issues — structured, labeled, prioritized. Then I'd work through them methodically. Requirements in, code out, tests validating, CI/CD deploying.

Speaking of tests: automated testing via GitHub Actions meant that every push was validated. And when a test failed, I could ask the GitHub MCP server to retrieve the trace. No more copy-pasting error logs from one window to another. The feedback loop tightened until it was nearly instantaneous.

I even recorded a YouTube demo — the whole workflow from concept to published package, captured on my @yannspeaksai channel. Because if you build an army of philosophers and don't document it, did it really happen?

## Tools as Self-Portraits

Here's what I think Chapter 3 is really about.

Naming your tools after philosophers isn't vanity — it's a way of encoding your values into the things you build. Every developer names their projects. Most names are functional, forgettable, interchangeable. But when you name a tool after Ricoeur, you're making a claim about what the tool means, not just what it does. You're saying: this search tool embodies a philosophy of interpretation. This presentation generator carries a vision of self-overcoming. This media toolkit is an act of translation in the deepest sense.

The philosopher tools were the first sign that my collaboration with Claude was producing something more personal than productivity gains. The blog posts from Week 1 were useful. The strategic memos were valuable. But the tools — the tools were self-portraits in code. They reflected not just what I could build, but how I thought about the world.

Week 2 had taught me that the line between philosophy and programming was thinner than I'd imagined. The existentialists and the engineers were asking the same question: *What should I build, and why does it matter?*

What I didn't know yet was that these weekly discoveries — the density principle, the philosopher army, the shift from skills to tools — would become the backbone of an internal evangelism campaign. Slides I'd present to three different audiences over the next six weeks, each time with a deeper understanding of what "build tools, not skills" really meant. But that story belongs to a later chapter.

I didn't have a complete answer yet. But I had an army of philosophers, a PyPI account, and a growing suspicion that the most interesting work was still ahead.

The competitive intelligence reports were about to begin. Claude was about to become my research partner. But that's the next chapter.
