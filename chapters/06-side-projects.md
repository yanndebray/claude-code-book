---
title: "Chapter 6: The Side Projects That Kept Growing"
status: draft-v1
last_editor: claude
notes: "Covers the transformation of side projects from one-shot demos to evolving portfolio — recettesdezoe.com business validation, sports analytics YouTube channel, music recommendation deep dive"
---

# Chapter 6: The Side Projects That Kept Growing

If you are like me, you probably have a graveyard of side projects. Half-finished repos, abandoned domain names, ideas that burned bright for an evening and cooled by morning. The normal lifecycle of a side project is: excitement, prototype, neglect, guilt, quiet deletion. Maybe you keep them around in a private GitHub folder as monuments to good intentions. I certainly did.

Something different happened this time.

It was early January, a few weeks into the new year. I was in the terminal one evening, working on something for the recipe site — I don't even remember what, probably a content pipeline — when I realized I had three different projects open in three different tabs, and all of them were *active*. Not in the "I should really get back to that" sense. Active as in: I'd made progress on each one in the past week, and each one had a clear next step waiting for me. I stopped typing and tried to remember the last time that had happened with a side project. I couldn't.

Over the previous chapters, I'd built an infrastructure I hadn't planned. The philosopher tools gave me reusable CLIs and a workflow for turning ideas into distributable software. The competitive intelligence work with Claude taught me how to research markets rigorously instead of guessing. The MCP revolution connected my tools to each other and to external services in ways that multiplied what a single person could do. None of this had been designed as a system. It was more like — each piece created the conditions for the next piece to exist.

And then the side projects stopped being "side." They started growing on their own.

Not all of them. Not into businesses. But the pattern was unmistakable: projects that would normally have died after one session were instead evolving, branching, connecting to each other. The graveyard wasn't filling up anymore. Things were staying alive.

This chapter is about three of those projects — a recipe website that almost became a business, a YouTube channel that became a laboratory, and a music recommendation app that became a philosophical statement. Each one started as an island. Each one turned into something I didn't expect.

## recettesdezoe.com — From Demo to Business?

You already know the origin story from Chapter 1. Late-night kitchen session, father-in-law watching over my shoulder, a recipe website conjured from a single ChatGPT prompt, domain purchased at 2am. Then the surprise: 1,300 organic visitors four months later, with zero marketing, zero updates, zero effort.

What you don't know is what happened next.

The traffic numbers broke something in my mental model, I said that already. But breaking a mental model is one thing. Deciding what to build on the rubble is another. Because once I had evidence that people were actually visiting this site — cooking from it, maybe — I had to ask a question I hadn't planned on asking: *Is this a product?*

I did what any self-respecting product manager would do with an existential question about a 2am side project. I reached for a framework.

### The Mom Test

Rob Fitzpatrick's *The Mom Test* is the gold standard for product validation. The core idea is deceptively simple: stop asking people if your idea is good (they'll lie to be polite) and start asking about their actual behavior. Don't say "Would you use a recipe website?" Say "Tell me about the last time you looked for a recipe online. What happened?"

I couldn't interview the 1,300 visitors — I didn't know who they were. But I could do the next best thing: study the market they were already choosing from.

### The Competitive Landscape

This is where the Chapter 4 pattern kicked in. I'd spent weeks training Claude to be a competitive intelligence partner — structured research, market sizing, strategic analysis. Now I turned that same lens on the French recipe market. And the landscape was sobering.

**Marmiton** — the absolute behemoth. 10 million monthly visitors, user-generated content, a brand so embedded in French cooking culture that "je vais regarder sur Marmiton" is practically a reflex. **750g** (owned by Webedia) — professional content, video-forward, with the media infrastructure to dominate on search and social. **Cuisine AZ** — another giant, part of the same media group as 750g, covering every conceivable recipe with industrial-scale content production.

Then there was recettesdezoe.com. A site built in a kitchen. By a product manager. At 2am.

The analysis was honest, and Claude didn't sugarcoat it: the French recipe market was a red ocean. The incumbents had decades of SEO authority, millions of indexed pages, and content pipelines that no solo operator could match on volume. The 1,300 visitors were real — probably finding the site through long-tail keywords that the giants hadn't bothered to optimize for. But scaling against Marmiton was like opening a corner bakery and hoping to outcompete an industrial bread factory.

The insight wasn't "give up." It was "compete differently." The big players wrote recipes like food blogs — SEO-optimized, template-driven, drowning in ads and pop-ups. recettesdezoe.com had something they didn't: a voice.

### The Voice Test

This was the moment where Chapter 2's voice analysis came back in a new form. Remember the blogging workflow I'd developed with Claude — the careful attention to preserving an authentic writing voice, the resistance to letting AI flatten everything into generic corporate prose? The same principle applied here, but the domain was entirely different.

I defined a quality test for any recipe the site would publish:

> "Could this have been written by someone sharing their grandmother's recipe over coffee? If it sounds like a food blog template or a restaurant menu, it's wrong."

That was the moat. Not SEO. Not scale. Voice. The feeling that a real person had cooked this dish, tasted it, adjusted the seasoning, and wanted to tell you about it the way they'd tell a friend.

### Content Scaling with Zoé

If voice was the moat, I still needed a way to produce content without spending every evening writing recipes by hand. This is where the Chapter 3 pattern kicked in again: build tools, not just skills.

I designed a CLI tool for recipe generation. I called it "Zoé" — the same name as my daughter, the same name that was already in the domain. If the philosopher tools got names that carried conceptual meaning, this one carried something more personal: a family name, a familial tradition. Where montaigne.cc and nietzsche.cc encoded philosophical values, Zoé encoded the domestic warmth that the whole project was supposed to embody.

The tool was built with the Copilot SDK and followed a structured workflow: research a recipe category, generate drafts that matched the established voice, validate against the Voice Test, and produce Markdown files ready for the site. Claude was the engine, but the CLI was the guardrail — deterministic, repeatable, consistent. A skill would have drifted with every conversation. A tool kept the voice stable.

Did recettesdezoe.com become a business? No. Not yet, maybe not ever. But it stopped being a demo. It had a competitive analysis, a content strategy, a voice standard, and a production tool named after my daughter. The 2am party trick had become something I could pick up, work on for an evening, put down, and come back to a week later without starting from zero.

That's what "kept growing" means. Not exponential growth. Not viral success. Just — alive.

## The YouTube Channel That Became a Lab

@yannspeaksai started as a way to document my projects. Record what I'm building, explain the process, put it out there. The kind of thing a lot of technical people do — part portfolio, part accountability mechanism, part excuse to learn video editing.

Seven videos in 2025. Five different sports. Five completely different technology stacks. And without planning it, the channel became less of a content outlet and more of a laboratory — each video an experiment in a different domain, with the only constant being Claude as a collaborator.

### Tennis — Predicting the French Open

The first sports video was about prediction. I built an ELO rating system enhanced with machine learning to forecast French Open match outcomes. The model achieved 75% accuracy, which sounds impressive until you realize that tennis prediction is a well-studied problem and the best models in the literature hover around the same range. The point wasn't to beat the state of the art. The point was that a product manager with no background in sports statistics could build a credible prediction system in a few evenings.

The stack was MATLAB for the analysis and Python for the data pipeline. Claude handled the integration between the two — something that would have taken me days of Stack Overflow diving in the Before Claude Code era.

### NBA — Dashboards and Automation

The basketball project pushed into web development territory. Season ranking animations, a React dashboard showing team statistics, and — the part I was proudest of — a full GitHub Actions CI/CD pipeline that automatically updated the data and rebuilt the visualizations.

This was the "build tools, not skills" philosophy applied to content creation. I didn't just make a dashboard. I built a system that kept the dashboard alive. Every new game night triggered an automatic update. The infrastructure outlasted the session that created it.

### NFL — From Toolbox to Clutch Factor

The American football work was actually two projects built back-to-back, each in a single day, both vibe-coded with OpenAI Codex.

The first was the **NFL Analytics Toolbox** — a MATLAB-first interface to NFL statistics. The idea was to bridge MATLAB and the open-source `nfl_data_py` Python library, so you could pull weekly player stats, play-by-play data, and team rosters directly into MATLAB tables. I built high-level functions like `showTeamDashboard("KC", 2023)` that generated four-tile figures with yardage breakdowns, projected vs. actual wins, roster profiles, and top performer summaries. The whole thing was packaged as a proper MATLAB toolbox — with an `Open in MATLAB Online` badge, unit tests, and a setup script that auto-provisioned a Python virtual environment via `uv`. The first commit message tells the story: *"vibe coding v0 with Codex."*

A week later, I built the second project: the **TV Clutch Factor**. This one was pure Python into a web dashboard. The pipeline downloaded 25 seasons of NFL play-by-play data, filtered to clutch situations — score differential within 7.5 points in the final minutes of the fourth quarter or overtime — and computed an original metric that combined traditional passer rating with volume weighting. Which quarterbacks performed best when the game was on the line? Aaron Rodgers, Matthew Stafford, and Drew Brees topped the leaderboard. The results fed into an interactive HTML dashboard with a broadcast-style dark theme, sortable columns, and gold/silver/bronze podium styling, served directly from GitHub Pages.

Two projects, two days total. One MATLAB, one Python-to-web. Neither would have existed if the cost of building them had been measured in weeks instead of evenings.

### Cycling — The Ghost That Kept Running

And then there was cycling. GhostRunners.app from Chapter 1 — the ride comparison tool built with MATLAB Mobile data capture. The clearest example of "kept growing" in the entire portfolio.

In the pre-Claude era, GhostRunners was a functional but rough prototype. MATLAB Mobile captured the data, MATLAB Online crunched the analysis, Python handled the Garmin FIT file parsing. It worked. I recorded YouTube videos about it. And then it sat there.

With Claude, I came back to it. The MCP server connected MATLAB to the broader workflow. The CLI patterns from the philosopher tools gave me a structure for the user interface. The CI/CD learnings from the NBA project meant I could automate the data pipeline. Each previous project had deposited a capability that GhostRunners could now draw on.

The ghost was still running. But now it was running faster.

### Soccer — The Premier League Dashboard

The soccer project was the most MATLAB-native of all the sports experiments. Not a data pipeline feeding a web dashboard, not a Python/MATLAB hybrid — a pure MATLAB programmatic UI built as a single class file.

The idea started with a screenshot. I'd seen a Premier League standings dashboard somewhere — clean layout, color-coded zones, position-by-matchday chart — and thought: *I bet I can build that in MATLAB.* Not App Designer, not a MATLAB App with a `.mlapp` file that's impossible to diff or version-control. A programmatic `uifigure` with `uigridlayout`, written as a single `.m` class file. The kind of code that plays nicely with Git, that Claude can read and modify, that you can share with a link.

Two days. That's how long it took to go from an empty file to a polished dashboard with five iterations documented in screenshots — v0.1 through v0.5, each one closer to the target layout. The final version had a full standings table color-coded by Champions League spots (blue), Europa League (orange), and relegation zone (red). Click a team and the side panel showed their badge (fetched live from TheSportsDB API), their card counts, and a ten-match form guide rendered as colored blocks. A position-by-matchday chart tracked all twenty teams across the season, highlighting your selection in bold blue against gray background lines.

The part that surprised me was the test suite. I'd built `matlab.unittest` test cases with tagged categories — unit tests for the API name mappings, integration tests for the full badge-fetching workflow, performance tests verifying that cached lookups stayed under 10 milliseconds. This was a side project with better test coverage than some production code I'd seen. The pattern of building things *properly* — tests, documentation, clean architecture — had become a habit, not an overhead.

And the `Open in MATLAB Online` button in the README? That was a small detail that connected the project to my day job. Anyone could click that badge and run the dashboard in their browser, no installation required. A product manager dogfooding his own product, building the kind of showcase he'd want other users to create.

### The Pattern

Here's what the YouTube channel taught me: **the marginal cost of exploration had dropped to near zero.**

Each video required learning a new domain — tennis statistics, NBA data APIs, NFL play-by-play formats, cycling biomechanics. In the old world, the domain learning alone would have consumed weeks. With Claude as a research and implementation partner, I could go from "I know nothing about ELO ratings" to "here's a working prediction system" in an evening or two.

Five sports. Five stacks. One year. The channel wasn't just documenting what I built. It was proving, video by video, that the barrier to entry for any technical domain had collapsed. Not to zero — you still needed taste, judgment, and the willingness to learn. But the activation energy had dropped from "this will take months, is it worth it?" to "let's find out this weekend."

## Gaining Back Control Over the Algorithm

The music project started with an itch.

If you use Spotify — and statistically, you probably do — you've experienced this: the algorithm decides what you like. It feeds you recommendations based on your listening history, and over time, your taste and the algorithm's model of your taste begin to converge. You listen to what it suggests, which reinforces its model, which narrows its suggestions, which narrows what you listen to. The feedback loop is invisible and relentless.

I didn't hate Spotify's recommendations. Some of them were genuinely good. But I resented the passivity of it. My music taste was becoming a mirror of an algorithm's assumptions about me, and I wanted to break out of that loop.

### The Architecture

The idea was simple in concept, ambitious in scope: build a personal music recommendation system using Spotify's own audio features — energy, acousticness, danceability, valence, tempo — but with *my* logic instead of *their* algorithm.

The core engine was a K-nearest neighbors (KNN) model. Take a song I loved, find the songs in my library that were most similar across those audio features, and surface the ones I'd forgotten about or never noticed. Not discovery of new music (Spotify already does that well) but rediscovery of music I already owned and had lost in the algorithmic shuffle.

Claude helped me design the system architecture and integrate the Spotify API. The data pipeline pulled my listening history and audio features for every track. The KNN model ran locally — no cloud dependency, no algorithm I didn't control. The recommendations were mine, based on rules I could see and modify.

### Form Factors

This is where the project got interesting. Once the recommendation engine existed, the question became: how do you interact with it?

I explored four different form factors, each one a different answer to that question:

**Web app** — the obvious first choice. A clean interface where you pick a seed song and see recommendations. Good for exploration, but it required a browser and a server.

**CLI tool** — because by this point, everything I built had a CLI. Type a song name, get recommendations in the terminal. Fast, scriptable, composable with other tools. The philosopher tool ethos applied to music.

**Desktop app** — for a more visual experience. Album art, audio previews, the kind of rich interface that a terminal can't provide.

**Hybrid** — the most ambitious version. A CLI that could launch a lightweight web interface when you wanted the visual experience, but stayed in the terminal when you wanted speed. The best of both worlds, if you could stomach the complexity.

Each form factor taught me something different about interface design. But the lesson that stuck was this: having the recommendation engine as a separate, well-defined module meant I could experiment with interfaces freely. The tool-first approach from Chapter 3 — building the engine before the interface — paid dividends I hadn't anticipated.

### Use Cases That Multiplied

The recommendation engine was the seed, but the use cases kept branching:

**Local music management** — I had years of downloaded music scattered across hard drives. The same audio feature analysis that powered recommendations could also organize, tag, and deduplicate my local collection.

**Personal Spotify Wrapped** — Spotify's annual summary is fun but superficial. With raw access to my listening data and audio features, I could build something deeper: trends in my taste over time, the acoustic signature of my moods, the genres I gravitated to during specific seasons.

**Mood-based playlists** — Instead of Spotify's generic "Chill" or "Focus" categories, playlists generated from my own definition of what those moods sounded like, calibrated to my library, my features, my thresholds.

### The Philosophical Resonance

Here's where the project connected back to something deeper.

In Chapter 3, the existentialist synthesis emerged: *"The existentialists ask 'how should I live authentically?' while Mollick and Harari ask 'how should we live with AI?' These questions are not separate."* The philosopher tools were answers to philosophical questions encoded in code.

The music project was the same impulse, just in a different domain. Building your own recommendation algorithm is an act of self-determination. It says: I refuse to let a platform decide what I like. I'll examine my own taste, build my own model of it, and use that model to rediscover what I've been missing. Socrates meets Spotify. The examined playlist is worth listening to.

> "Gaining back control over the algorithm isn't about rejecting technology. It's about choosing which technology reflects who you are instead of who a platform thinks you should be."

This wasn't just a music project. It was the book's thesis — AI as amplifier of human intention — applied to the most personal domain I could think of: what sounds fill your house on a Sunday morning.

## The Portfolio Effect

Let me step back and look at what had happened.

In Chapter 1, I described a pattern: *"Every conversation started from zero. Every project was an island."* recettesdezoe.com was a single-session creation. GhostRunners was a rough prototype that worked but couldn't grow. The YouTube channel was a series of disconnected experiments. Each project lived in its own bubble, with no shared infrastructure, no common patterns, no way for one to feed into another.

By the time I'd reached the projects in this chapter, that had changed entirely. The projects weren't islands anymore — they were nodes in a network.

recettesdezoe.com drew on the competitive intelligence patterns from Chapter 4 for its market analysis, on the voice preservation techniques from Chapter 2 for its content standard, and on the "build tools, not skills" philosophy from Chapter 3 for the Zoé CLI. The YouTube sports projects cross-pollinated: CI/CD from the NBA project fed into GhostRunners, MATLAB toolbox patterns from the NFL project informed the cycling analysis, and every project deposited knowledge that the next one could draw on. The music recommendation app used the same CLI architecture as the philosopher tools, the same research methodology as the competitive analysis, and connected back to the existentialist themes that ran through the whole journey.

The infrastructure chapters — the philosopher tools, the competitive intelligence machine, the MCP revolution — hadn't just produced outputs. They had produced a *way of working*. A set of patterns and capabilities that made every subsequent project cheaper, faster, and more connected than it would have been in isolation.

This is the portfolio effect. Not a planned portfolio — I never sat down and said "I'm going to build an interconnected network of side projects." It emerged from the compounding of tools, patterns, and knowledge across dozens of conversations with Claude. Each project made the next one possible. Each tool reduced the cost of the next tool. Each experiment deposited a capability that future experiments could inherit.

I want to be honest about the limits. Most of these projects are still side projects. recettesdezoe.com isn't generating revenue. The YouTube channel has a modest audience. The music app is something I use personally. None of this is a startup success story.

But that's precisely the point. The transformation wasn't about commercial outcomes — it was about the *cost of exploration*. When it takes weeks to build something, you have to be strategic about what you build. You plan, you evaluate, you calculate the expected return on investment. When it takes an evening, you can afford to follow curiosity wherever it leads.

> "When exploration becomes cheap, you stop asking 'is this worth my time?' and start asking 'what am I curious about?'"

That shift — from strategic allocation of scarce building capacity to abundant, curiosity-driven exploration — is, I think, the most underappreciated consequence of working with an AI collaborator. The projects themselves matter less than the fact that they exist at all. Each one is evidence that the barrier between "I wonder if..." and "let's find out" has been nearly erased.

## What the Side Projects Taught Me

The side projects taught me something that the work projects couldn't.

At MathWorks, the value of Claude was measurable — faster blog posts, sharper competitive analyses, better presentations. The ROI story was clear and presentable. But the side projects operated outside the logic of ROI. Nobody asked me to build a recipe website or a music recommendation engine. Nobody was tracking the output. The only metric was whether I wanted to keep going.

And I kept going. That was the data point that mattered.

Because when you strip away the professional context — the reporting obligations, the pilot program requirements, the need to justify your tools budget — what you're left with is the raw question: *Do I want to spend my evenings doing this?* And the answer, project after project, evening after evening, was yes.

There's a specific kind of knowledge that comes from building things nobody asked you to build. Work projects teach you what's possible. Side projects teach you what's *exciting*. And when the time came to explain this journey to colleagues — to stand in front of a room and make the case that something fundamental had changed — I needed both kinds of knowledge. The work projects gave me the evidence: productivity gains, workflow improvements, measurable outputs. But the side projects gave me the conviction. The ability to say, with genuine enthusiasm and not just professional obligation, that this technology had changed how I spent my free time. That I *chose* to be in the terminal at 11pm on a Tuesday, not because anyone was watching, but because the next experiment was calling.

That conviction was about to matter more than I expected. Over the following weeks, I'd present to three different teams at MathWorks, each time refining the message, each time drawing on both the professional evidence and the personal story. The internal evangelism campaign was about to begin — and with it, a new challenge: translating a felt experience into something that could change other people's minds.

But that's the next chapter.
