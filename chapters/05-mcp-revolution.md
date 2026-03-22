---
title: "Chapter 5: The MCP Revolution"
status: draft-v1
last_editor: claude
notes: "Covers the Model Context Protocol — the MATLAB MCP Core Server, the 'USB-C for AI' metaphor, MCP server experiments, the onboarding campaign, commands vs. skills, and agents calling agents"
---

# Chapter 5: The MCP Revolution

Everything I'd built so far — the philosopher tools, the competitive intelligence reports, the blog posts, the strategic memos — had one thing in common. They were separate. Each tool lived in its own world. Each workflow started from scratch. The blog posts didn't know about the CLI tools. The research didn't feed back into the presentations. The competitive intelligence existed in documents, not in systems.

What I needed was infrastructure. A way to connect all of these pieces so that agents could use them together, not just one at a time. That infrastructure had a name, and it was about to become the central theme of everything I did.

The Model Context Protocol. MCP.

## USB-C for AI

If you are like me, you remember the era of proprietary chargers. Every device had its own connector — a different shape, a different voltage, a different cable cluttering your desk drawer. Then USB-C arrived and suddenly everything plugged into everything. One standard. Universal compatibility. The end of cable chaos.

MCP is USB-C for AI.

That's the metaphor that stuck. Not because I coined it — it was already circulating in the developer community — but because it captured exactly what was happening. Before MCP, connecting an AI agent to an external tool meant building a custom integration for every combination. Claude needs to use MATLAB? Build a bespoke bridge. Copilot needs to access your database? Write another one. Every agent-tool pair required its own plumbing.

MCP changed the equation. It defined a standard protocol — a universal connector — that any AI agent could use to talk to any tool. Build one MCP server for your tool, and suddenly every MCP-compatible agent can use it. Claude Code, GitHub Copilot, Cursor, Windsurf — all of them, through the same interface.

For someone working at MathWorks, this wasn't an abstract standard. It was a strategic imperative.

## The MATLAB MCP Core Server

The MATLAB MCP Core Server became the centerpiece of my work. I wrote about it, created tutorials for it, built onboarding materials around it, and positioned it as the bridge between MATLAB and the agentic AI ecosystem.

The server itself was elegant in its simplicity. Five tools:

1. **`detect_matlab_toolboxes`** — Reports which toolboxes are installed. Simple, but essential. An agent needs to know what capabilities are available before it can plan how to solve a problem.
2. **`check_matlab_code`** — Runs MATLAB's built-in `checkcode` function for style and correctness analysis. The agent can lint your code before running it.
3. **`evaluate_matlab_code`** — Executes a string of MATLAB code and returns the results. This is the core — the ability for an agent to actually *use* MATLAB, not just talk about it.
4. **`run_matlab_file`** — Executes a `.m` script file and returns the output. Where `evaluate_matlab_code` runs a snippet, this runs a full file.
5. **`run_matlab_test_file`** — Executes a MATLAB unit test file and returns comprehensive test results. The agent can not only write code but verify it.

Five tools. That's it. But those five tools turned MATLAB from a standalone application into something that any AI agent could call programmatically. The strategic implications were enormous.

I remember the moment it clicked for me — watching Claude Code call `evaluate_matlab_code`, run a computation, inspect the output, decide it needed to adjust a parameter, and call it again. No human in the loop. The agent was *using* MATLAB the way a developer would. Not generating MATLAB code and hoping you'd copy-paste it (the ChatGPT pattern), but actually running it, reading the results, and iterating.

This is the difference between AI that generates code and AI that uses tools. MCP made the latter possible.

## The Integration Play

Here's the positioning insight that emerged, and it was one of the most important strategic ideas I contributed during the pilot:

> This is an **integration play**, not putting agentic front and center. MATLAB "integrates" with coding agents like Claude Code and GitHub Copilot. We're showing MATLAB users that they're not left behind.

The temptation for any established software company watching the agentic AI wave is to panic and try to build their own AI agent from scratch. "We need our own copilot! Our own agentic platform!" That's the instinct, and it's usually wrong.

The smarter play — the one I kept advocating — was integration. MATLAB doesn't need to be an AI agent. MATLAB needs to be the tool that AI agents reach for when they need to do serious computation. The MCP server was the bridge that made this possible.

I developed this into a pocket guide strategy aimed at two audiences:

**Primary audience:** MATLAB users evaluating coding agents. The people asking, "Does MATLAB work with these new coding agents I keep hearing about?" These are the users who've seen colleagues using Copilot or Claude Code and are wondering if they're being left behind. The answer: no. MATLAB works with all of them, through MCP.

**Secondary audience:** MATLAB users who already use GitHub Copilot and want to extend it. They've got the coding agent — now they want it to actually run MATLAB, not just generate MATLAB code. The MCP server closes that gap.

> "If you can think of it as an AND — if we can do for humans AND for AI, then maybe we have something here."

That became my closing line in more than one presentation. MathWorks serving both humans and AI agents. Not zero-sum. An AND.

## The MCP Server Experiments

The MATLAB MCP Core Server was just the beginning. Once you understand the MCP pattern, you start seeing servers everywhere.

**ThingSpeak** — IoT data access via MCP. ThingSpeak is MathWorks' platform for IoT data storage and analysis. Wrapping it in an MCP server meant that any AI agent could query IoT sensor data, analyze trends, and trigger actions — all through the same standard protocol.

**Google Spreadsheet** — Private data access. This one actually got deployed. My colleague and I built an MCP server that let agents read from and write to Google Sheets — a bridge between the structured world of spreadsheets and the conversational world of AI agents. It sounds mundane, but think about how many business workflows live in spreadsheets. Giving agents access to that data, through a standard interface, unlocked an enormous amount of practical utility.

**MATLAB Remote Service** — For remote execution in the cloud or on a local server. This was the ambitious one. Instead of requiring a local MATLAB installation, the remote server let agents call MATLAB running somewhere else — in the cloud, on a compute cluster, on a colleague's machine. The MCP server abstracted away the location, so the agent didn't care whether MATLAB was local or remote.

Each server was a small project, but together they painted a picture: MCP wasn't just a way to connect one tool to one agent. It was the foundation for an ecosystem. Every server you build multiplies the capabilities of every agent that connects to it.

## The Blog Post Machine

The blog posts I'd started drafting in Week 1 had a recurring character: MCP. Almost every post I published on the MATLAB AI Blog connected back to the protocol:

- **MATLAB MCP Core Server** — the foundational post, announcing the server and explaining the architecture
- **Connecting to Hardware** — data acquisition and image acquisition devices via MCP. The physical world, accessible to agents
- **Deploying a Quant Agent** — financial analysis with MATLAB as the computational backbone, connected through MCP
- **Giving Local AI Agents the Ability to Use MATLAB** — the on-ramp for users running local models
- **Building an Optimization Agent** — engineering optimization workflows, orchestrated through MCP
- **Automating the Documentation of MATLAB Analysis** — the full pipeline from analysis to documentation, with MCP as the connective tissue

Six posts, all variations on the same theme: MATLAB + MCP = MATLAB in the agentic era. The blog posts weren't just content marketing. They were proof of concept. Each one demonstrated a different use case, a different audience, a different reason why the MCP integration mattered.

## The Onboarding Campaign

As I went deeper into the MCP ecosystem, I realized something: the technology was only half the challenge. The other half was getting people to use it.

So I built an onboarding package. A complete Claude Code 101 for MathWorkers: installation guide, CLAUDE.md files for common project types, slash commands for repeatable workflows, MCP server setup instructions, Git workflow best practices, tips and tricks I'd accumulated over weeks of daily use.

This is where the Claude Code features I'd been exploring became teachable material:

**`/init`** — Bootstrap a project with CLAUDE.md and initial configuration. The command that turns a blank directory into a project that Claude understands. I showed colleagues how one command could set up the context, conventions, and instructions that would make every subsequent conversation more productive.

**`/context`** — Load context into a session. The ability to bring Claude up to speed on a project without re-explaining everything from scratch. For someone who'd experienced the "every session starts from zero" frustration of the ChatGPT era, this was transformative.

**`/commands`** — Custom slash commands for repeatable workflows. The bridge between "I do this manually every time" and "I type one command and it happens." I built commands for blog post drafting, for presentation generation, for competitive intelligence — all the workflows I'd been doing manually, now formalized and shareable.

The distinction between commands and skills became one of my favorite things to explain:

| Aspect | Commands | Skills |
|--------|----------|--------|
| Invocation | Manual: /command | Automatic: Claude decides |
| Structure | Single .md file | Directory with SKILL.md |
| Location | .claude/commands/ | .claude/skills/ |
| Discovery | User must type command | Claude matches description |
| Best for | Quick templates | Complex workflows |

Commands are things you ask for. Skills are things Claude recognizes it needs. The difference is subtle but profound — it's the difference between a tool you pick up and a capability that activates itself when the situation calls for it.

## Agents Calling Agents

And then things got weird. In a good way.

The MCP thesis was "agents calling tools" — an AI agent reaching out to external capabilities through a standard protocol. But somewhere around Week 3, a more advanced pattern emerged: **agents calling agents.**

Not just Claude using MATLAB. Claude orchestrating Codex and Gemini CLI. Multiple AI agents, working in parallel, each assigned a different piece of a larger task. Claude as the conductor, the other agents as the orchestra.

The inspiration came from NetworkChuck — the idea of sending multiple agents down different research paths and synthesizing the results. Deep research, but parallelized. Instead of Claude doing everything itself, it could delegate: "You go research the market size. You go analyze the technical architecture. You go find the competitive landscape." Then it would synthesize the results into something more comprehensive than any single agent could produce.

Gemini CLI's headless mode made this practical. OpenAI's Codex CLI offered another execution path. Even GitHub Copilot could be subcontracted through the `/github:AssignCodingAgent` MCP command — Claude assigning implementation work to Copilot through GitHub Issues.

This escalation from tool-use to agent-orchestration felt like watching a gear shift. The MCP server gave agents hands. Agents calling agents gave them a team. The metaphor wasn't a single worker with better tools anymore — it was a manager coordinating a team of specialists, each with their own strengths.

I showed this slide to the industry marketing team during my Week 3 presentation. I could see the moment it clicked for some of them — and the moment it overwhelmed others. The gap between "I use ChatGPT for emails" and "I orchestrate multiple AI agents in parallel" was wider than anyone had expected.

## What MCP Actually Changed

Here's what I think the MCP revolution is really about.

Before MCP, every AI integration was a one-off. You'd connect one agent to one tool, and the integration was fragile, proprietary, and hard to maintain. The cost of connecting anything to anything was high, so people connected very little.

After MCP, connection became cheap. Build one server, and every agent can use it. Build one client, and every server is accessible. The network effects kick in: every new server makes every agent more capable, and every new agent makes every server more valuable.

For MathWorks, this meant MATLAB could join the agentic ecosystem without rebuilding itself. The MCP server was the bridge — lightweight, standards-based, and infinitely extensible. For me personally, it meant the philosopher tools, the competitive intelligence workflows, the blog post pipelines, and the MATLAB integrations could all talk to each other through the same protocol.

The infrastructure I'd been looking for — the thing that would connect all the separate pieces of work into a coherent system — had been there all along, waiting for me to understand it.

And understanding it changed everything that came after. The side projects were about to get ambitious. But that's the next chapter.
