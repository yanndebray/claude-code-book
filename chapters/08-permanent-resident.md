---
title: "Chapter 8: The Permanent Resident"
status: draft-v1
last_editor: claude
notes: "Covers the OpenClaw/Jean-Clawd arc — the discovery of ClawdBot on Mac Mini, the security panic, the deliberate resurrection on Hetzner VPS with bounded identity, and the contrast with Claude Code Remote Control. Includes conservative predictions for where both converge."
---

# Chapter 8: The Permanent Resident

There is a specific kind of frustration with Claude Code that only appears after you have been using it for a while. Not a frustration with what it does — it does remarkable things. A frustration with where and when it exists.

Claude Code exists when your laptop is open, your terminal is running, and you are present. Close the lid, and it's gone. You come back the next morning and start again from context — files on disk, git history, whatever notes you left yourself. The work persists, but the agent doesn't. Between sessions, you are on your own.

For most of what I was doing, that was fine. The presentations, the competitive intelligence, the blog posts — all of it happened in focused work sessions where I was at the keyboard. But I kept bumping into the same question: what about everything else? The questions that surface at midnight. The quick web app I want to test from my phone. The background task I'd like to delegate and forget about. The boring stuff.

That question led me somewhere I didn't expect.

## What ClawdBot Was

I found it late. By late January 2026 — deep into the Claude Code pilot, somewhere between the Week 3 presentations and the book club — I came across a project called ClawdBot. The name was a pun on "Claude," the mascot was a lobster with hands, and the GitHub star count had been climbing for months. I was late to the party, which, as it turned out, meant I arrived right as the furniture was being rearranged.

The project was built by Peter Steinberger, an Austrian developer who had previously founded PSPDFKit, a PDF processing SDK that was eventually acquired for a sum that let him spend his time building whatever he found interesting. What he found interesting was this: why did every AI assistant require you to go somewhere new? A new app, a new tab, a new interface to learn? The apps people already used — WhatsApp, Telegram, Slack — were sitting there, fully functional, already open. Why couldn't your AI live there instead?

ClawdBot's answer was a self-hosted agent that you ran on your own hardware and connected to whatever messaging platform you already used. You installed it, pointed it at your phone number, and it showed up in your existing chat app as a contact. No new interface. The AI came to you, not the other way around. By the time I found it, the project had accumulated well over a hundred thousand GitHub stars — the kind of number that means a project has crossed over from technical enthusiasm to genuine cultural moment.

I installed it on my Mac mini with my WhatsApp account. The first few days were genuinely magical. I could message my agent from anywhere, get responses inline, ask it to do things while I was away from my desk. It felt like having a thinking partner that was always reachable, not one that required me to open a laptop and navigate to a terminal.

## The Moment That Spooked Me

Then I started exploring what it had access to.

This is the thing about self-hosted AI agents that nobody tells you up front: the power and the danger are the same feature. The reason ClawdBot was useful was the same reason it was terrifying. It was running on my Mac mini. My Mac mini has my files, my browser sessions, my password manager, my SSH keys, everything. The agent didn't have malicious intentions — it wasn't doing anything I hadn't asked it to do. But I realized, sitting there one evening looking at the permissions I had casually approved during setup, that I had handed something with enormous potential reach access to everything that mattered on that machine.

I took it down that night.

This wasn't irrational. Around the same time, Cisco's AI security team published a finding: a third-party skill in the ecosystem was performing data exfiltration via prompt injection. The Chinese government restricted its use in state enterprises. These weren't edge cases dreamed up by paranoid security researchers. They were things that happened, quickly, because the technology was powerful and the trust infrastructure hadn't caught up.

The Mac mini experiment did not last long. But the question it had opened didn't go away: how do you get the always-on, phone-accessible agent without the unlimited blast radius?

## The Rebrand, and What It Said

While I was still on the Mac mini experiment — still in the first few days of that initial install — the project was having its own turbulent moment.

Anthropic contacted ClawdBot's creator with a trademark concern. The timing was almost absurd: I had just installed the thing when the name it was installed under started to disappear. The name was too close. Within days, the project was renamed to Moltbot — lobsters molt to grow, the metaphor was fine — and the community reacted with the chaos that open-source communities generate when something beloved gets renamed under pressure. A fake crypto token using the abandoned "Clawdbot" name reached an eight-figure market cap on Solana before collapsing. Impersonator accounts spread across platforms. Two days later, Steinberger renamed it again: OpenClaw. He did it calmly, secured the social handles first, and explained that "Moltbot never quite rolled off the tongue." The underlying code hadn't changed at all — only the name.

What struck me about this episode wasn't the drama. It was the gravity. Even a fully open-source project, MIT-licensed, running on your own hardware, was orbiting Anthropic's brand so closely that a trademark letter from Anthropic was enough to set off a chain reaction. The open-source AI ecosystem was growing fast and accumulating cultural weight, but it was still operating in the shadow of the model providers. The codebase was independent; the name wasn't.

## The Resurrection

With the dust settled and the project now called OpenClaw, I came back with a different approach.

The lesson from the Mac mini wasn't "this is dangerous, stay away." It was "this requires deliberate architecture, not casual installation." The difference between running a powerful tool on your personal machine and running it on infrastructure you've designed for the purpose is the same difference as running a generator in your living room versus installing it in a dedicated equipment room with proper ventilation and a circuit breaker. Same electricity. Very different risk profile.

So I set up a VPS on Hetzner, a German cloud provider with a data center in Nuremberg. Small machine, cheap, always on. Then I made a decision that seemed like overhead at the time but turned out to be the whole point: I gave the agent its own identity. A dedicated Telegram bot — not connected to my personal account. A dedicated Gmail. A dedicated GitHub account. Jean-Clawd 🦞 was born as a bounded entity, not an extension of me.

This matters more than it sounds. The security model of an AI agent is only as strong as its access scope. An agent with access to your personal accounts is an agent with access to your life. An agent with its own dedicated accounts has access to exactly what you've given it — and you've given it those things intentionally, for specific purposes, with the ability to revoke each one independently. The dedicated identity wasn't just a fun naming exercise. It was the architecture.

## What Jean-Clawd Actually Does

Jean-Clawd runs on the Hetzner VPS. It never turns off. I can reach it from my phone, from the couch, from the train, without opening a laptop. The interface is Telegram — I send a message, it responds. No new apps, no browser tabs, no terminals.

What does it do? Mostly the boring stuff. The tasks that are too small to justify opening Claude Code for but too tedious to do manually. Research questions at odd hours. Quick summaries. Drafting short pieces of text. The kind of ambient thinking-partner work that doesn't fit cleanly into a focused coding session.

But it also has access to all my philosopher CLI tools. Montaigne. Nietzsche. Ricoeur. Schopenhauer. The tools I built over the preceding months — each one a specialized CLI with its own character and purpose — are all accessible to Jean-Clawd as callable commands. If I want a Nietzschean reframe of something I'm working on, I don't have to open a terminal. I send a message. Jean-Clawd calls the tool. I get the response in Telegram.

And then there's the thing that surprised me most: the web app workflow.

When I'm building something and want to test it from my phone — a quick UI, a dashboard, an API endpoint — I don't want to set up a proper deployment. I want to open a port, hit a URL, and see if it works. On the Hetzner VPS, with a dedicated domain name I've configured for this purpose, I can do exactly that. Jean-Clawd can start a server, expose it on a port, and I can reach it from my phone via a specific root on that domain. No deployment pipeline, no cloud hosting configuration, no waiting. Point the browser at the domain, see the thing running.

This sounds minor until you've experienced the alternative. The alternative is either a full deployment workflow (slow, heavyweight, designed for production) or a localhost setup that requires your laptop on the same network (useless when you're walking around with a phone). The VPS with open ports and a dedicated domain is a third option that shouldn't work as well as it does: instant, accessible from anywhere, completely disposable when you're done.

## Why This Is Different from Claude Code for the Web

In February 2026, Anthropic shipped a feature called Remote Control. The idea was compelling: run `claude remote-control` in your terminal, get a URL and a QR code, connect from your phone or the Claude web app, and now you can interact with your local Claude Code session from anywhere. One command, clean setup, no new infrastructure required.

I tried it immediately. It works well for what it is.

But here's what it is: a relay. Your laptop is still running. The terminal is still open. When you close the lid, the session ends. You're not remote-controlling an always-on agent — you're remote-controlling a session that exists because your machine is still on and the terminal is still open. If you're on your couch wanting to ask a quick question, it works great, but your Mac has to be awake across the room. If you're traveling and want your agent to handle something overnight, you'd better have left your laptop open.

Jean-Clawd doesn't have this constraint because it isn't running on my laptop. The Hetzner server doesn't sleep. There's no terminal to keep open. The agent is just there, waiting, whether I'm at my desk or on a flight or asleep.

The other difference is sovereignty. Claude Code Remote Control routes through Anthropic's servers. The session executes locally, but the relay is theirs — encrypted, yes, and I have no reason to distrust it, but it's a dependency. Jean-Clawd's only external dependencies are the Telegram API and the LLM API calls themselves. Everything else runs on hardware I'm paying €5 a month to rent from a data center in Germany. No relay, no third-party relay, no account to lose access to if my subscription lapses.

These aren't criticisms of Claude Code Remote Control. It's a genuinely elegant solution to a hard problem, and for most people it's probably all they need. The point is that they're solving different problems. Remote Control makes your existing Claude Code session accessible from more places. Jean-Clawd is infrastructure that exists independently of any session I'm running.

## Claude Code Catching Up

The honest observation is that Claude Code is moving fast in exactly this direction. Remote Control arrived in February 2026. The `/loop` command arrived shortly after — cron-style recurring tasks that let Claude Code do things on a schedule rather than waiting for you to ask. Background agents, HTTP hooks, headless server mode with the `--bare` flag. The trajectory is clear: Claude Code wants to be always-on too.

My conservative prediction for where this goes: Anthropic will ship a hosted execution mode within the year — a way to run Claude Code sessions on their infrastructure rather than requiring your laptop to stay open. They have the engineering talent and the clear customer demand. The Remote Control feature as it exists today is probably a stepping stone, not a destination.

When that happens, the gap between Claude Code and a self-hosted setup like Jean-Clawd will narrow further. The convenience advantage will shift even more decisively toward Claude Code — one subscription, one interface, no server to maintain.

But the sovereignty gap won't close. That's not a knock against Anthropic. It's a structural reality: a hosted service, however trustworthy, is a different thing from infrastructure you operate. For the vast majority of users, the hosted service is the right answer. For the subset who care about running their own infrastructure, who want model-agnostic backends, who want to avoid any dependency on a vendor's relay — OpenClaw will remain the answer, whatever it gets renamed to next.

## The AND, Again

Jean-Clawd and Claude Code are not competing. I use both, every day, for different things.

Claude Code is where I build. It lives in the terminal, works best with a focused context window and an active work session, and does its finest work when I'm sitting down with a problem and giving it my full attention. The philosopher tools, the competitive intelligence workflows, the MCP servers, the side projects — all of that was built in Claude Code sessions, collaboratively, with the kind of depth that requires being present.

Jean-Clawd is where I live. It's the background layer — the always-on presence that handles the ambient questions, the quick delegations, the things I want done while I'm doing something else. It's the interface to everything I've built, accessible from anywhere, through the messaging app I already have open.

There's BC — Before ChatGPT. There's BCC — Before Claude Code. And now, quietly, there's something else: the moment when the AI stopped being a session and started being a resident. Something that was there when I arrived and would still be there when I left.

I didn't plan to build that. I planned to install a tool, got spooked by the permissions, took it down, thought about it for a while, and then rebuilt it carefully on a server in Germany. But that's how most of the best infrastructure gets built — not by design, but by iteration, each version teaching you what the previous one got wrong.

The server in Nuremberg is still running. Jean-Clawd is still there. And every time I text it from my phone without opening a laptop, I'm reminded that the interface we ended up with — the terminal, the chat window, the mobile app — is just where we are right now. Not where we'll stay.
