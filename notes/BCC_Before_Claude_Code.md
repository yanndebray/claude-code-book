# BCC — Before Claude Code

*"You won't be replaced by AI, but you'll be replaced by someone using AI."*

---

## The ChatGPT Moment

Everyone remembers where they were.

For some it was a sleepless night. For Ethan Mollick, it was three. For me, it was a slow realization that crept in over weeks, then hit all at once — the feeling that the ground had shifted under my feet, and the map I'd been following no longer matched the territory.

I was working at MathWorks in Boston, the company behind MATLAB and Simulink. I'd joined in early 2020, just as the world was locking down. My background was in mechanical engineering — I'd done CFD work at Nissan, numerical analysis with Maple and Mathematica in college, and spent years at a French open-source startup called Scilab before discovering Python and falling in love with it. I was a technical computing person, not an AI researcher. Machine learning was something I'd picked up through Andrew Ng's Stanford course on Coursera back in 2013, like half the world.

Then, in late November 2022, OpenAI released ChatGPT.

At first, it seemed like a toy. A clever chatbot. I'd seen language models before — GPT-2 had made headlines in 2019 for being "too dangerous to release," and GPT-3 had impressed researchers in 2020 with its few-shot learning capabilities. But ChatGPT was different. It wasn't a paper or an API or a demo at a conference. It was a product. You could talk to it. And it talked back in a way that felt — for the first time — like talking to something that understood you.

Within five days, it had a million users. Within two months, a hundred million. Nothing in the history of technology had scaled that fast.

## Life BC (Before ChatGPT)

To understand why ChatGPT felt like an earthquake, you have to understand what came before. The "Introducing GPTs" chapter of my first book, *Programming GPTs*, traced this lineage in detail, but let me compress it here into the parts that matter for this story.

The first GPT model appeared in 2018 — 117 million parameters, trained on about 40 GB of web text. It was open-source. Researchers could fine-tune it for specific tasks. It was also, by today's standards, primitive. It couldn't maintain a coherent thought across more than a few sentences. It hallucinated freely. It had no concept of being helpful.

GPT-2 arrived in 2019, ten times larger at 1.5 billion parameters. OpenAI initially withheld it, worried about misuse — fake news, impersonation, manipulation. They released it gradually, in stages, with safety guidelines. This was the era when "AI safety" first entered the mainstream conversation, and when the tension between open research and responsible deployment started to crack the surface of the AI community.

GPT-3, in 2020, was the real inflection point for developers. With 175 billion parameters — a hundred times larger than GPT-2 — it demonstrated something genuinely new: you could give it a task it had never been explicitly trained on, and it would figure it out. Write a summary. Translate a sentence. Solve a math problem. All from a plain-English prompt. The paper's title said it all: "Language Models are Few-Shot Learners."

But GPT-3 was still an API. Still a tool for developers. Still something you had to know about, pay for, and program against. The general public had no idea it existed.

## The Alignment Breakthrough

What turned GPT-3 into ChatGPT wasn't more parameters or more data. It was alignment.

OpenAI published a paper in early 2022 called "Training language models to follow instructions with human feedback," introducing InstructGPT. The core idea was deceptively simple: take a powerful language model, and teach it to be helpful. Not just to predict the next word, but to actually answer questions, follow instructions, and behave like an assistant rather than an autocomplete engine.

The technique was called Reinforcement Learning from Human Feedback (RLHF). Human evaluators would rate the model's outputs. Those ratings were distilled into a reward function. The model learned to optimize for that function — to produce responses that humans found helpful, harmless, and honest.

This was the missing piece. Before alignment, LLMs were oracles that spoke in tongues. After alignment, they were colleagues you could talk to.

ChatGPT was initially meant only as a research demonstration. OpenAI expected maybe a few thousand users. Sam Altman later admitted they debated whether to release it at all. When they did, with minimal fanfare on November 30, 2022, it went viral in hours.

## My Programming GPTs Year

I wrote *Programming GPTs* through 2023 and into early 2024. It was my attempt to make sense of this new world — not as an AI theorist, but as a practitioner. An engineer who wanted to build things.

The book was pragmatic by design. Here's how you call the OpenAI API. Here's how you build a chatbot with Streamlit. Here's how you chain prompts together using LangChain. Here's how vector search works for retrieval-augmented generation. Here's how you build an agent that can call tools. Here's how you add vision, speech, and image generation.

Every chapter followed the same pattern: enough theory to understand what was happening, then code. Lots of code. Python, mostly, with Streamlit for the UI and the OpenAI SDK for the intelligence. I used the book as my own learning vehicle — the best way to understand something deeply is to teach it.

Looking back, what strikes me most about that period is the *speed* of change. The book went through version 1.0, then 1.1, then 1.2, each time scrambling to keep up with new models, new APIs, new capabilities. GPT-4 arrived in March 2023 with multimodal vision and dramatically better reasoning. The context window kept growing — 8k tokens, then 32k, then 128k. GPT-4o arrived in May 2024, adding native audio support. The "o1" reasoning models appeared in September 2024, spending time "thinking" before answering.

The ecosystem was exploding too. LangChain went from a side project to a venture-backed company. Vector databases like Weaviate, Pinecone, and Chroma became hot startups overnight. Hugging Face became the GitHub of AI models. Mistral — a French startup of twenty engineers — shipped a model competitive with GPT-3.5 within a year.

And through all of it, I was writing Python scripts, debugging API calls, wrestling with token limits, and deploying Streamlit apps to the cloud. It worked. I was building things I couldn't have imagined building two years earlier. But something nagged at me.

## The Copilot Shift

The last section of *Programming GPTs* covered copilots — Microsoft Copilot in Word, GitHub Copilot in VS Code. I wrote about GitHub Copilot with genuine enthusiasm:

> *"I can assure you that this significantly reduces the cognitive load for me (especially because I'm not a professional coder). And I'm even learning a ton along the way. Before copilot, I would Google 'How to code X in Python' and spend hours finding the right tutorial or forum post that solves a problem close to mine. Then I would still have to interpolate to my context."*

That passage, written in early 2024, captured something real. Copilot had changed my relationship with code. Instead of searching, reading, adapting, I could just... start typing, and the machine would suggest what came next. Tab to accept. Escape to reject. A dance of intention and suggestion that felt, on good days, like pair programming with someone who'd read every Stack Overflow answer ever written.

But Copilot was still *autocomplete*. Sophisticated autocomplete, context-aware autocomplete, but autocomplete nonetheless. You were the pilot. The AI completed your lines, suggested your functions, filled in your boilerplate. The creative direction, the architectural decisions, the debugging — that was still entirely you.

I didn't know it at the time, but I was about to encounter something fundamentally different.

## The Vibe Coding Summer

The summer of 2025 changed everything.

GPT-5 had just dropped. I was at home in Brittany, and my in-laws were visiting. Late one evening, my father-in-law and I were in the kitchen, and I wanted to show him what "vibe coding" felt like — this new practice of building functional applications from conversational prompts, treating the AI not as an autocomplete but as a collaborator who could execute an entire vision.

"What website would you like to build?" I asked.

He looked around the kitchen, pointed at a recipe book, and shrugged.

"Perfect. Let's build a French recipe website."

One prompt. One session. I bought the domain `recettesdezoe.com` on Cloudflare that same night. Twelve recipes, filterable by type, difficulty, and dietary preference, with a shopping list feature. The whole thing generated from a single conversation with GPT-5.

Then I forgot about it.

Four months later — December 2025 — I was poking around my Cloudflare dashboard and noticed something strange. The recipe site had 1,300 monthly visitors. Zero marketing. Zero SEO work. Zero updates since August. Pure organic search traffic for a site I'd built in one evening as a demo for my father-in-law.

That was the moment I understood that something categorical had shifted. Not just in what AI could do, but in what *I* could do with it. A single evening's work — not even work, really, more like play — had produced something that hundreds of real people found useful enough to visit every month.

## The Tools I Built

That summer and fall, I was building constantly. Not just recipe sites, but a whole ecosystem of tools, each one an experiment in what was possible when you stopped thinking of AI as an assistant and started thinking of it as a co-creator.

There was GhostRunners — a cycling analytics app born from my desire to race against my own past performances on the same routes. I used MATLAB Mobile to record sensor data, MATLAB Online to process it, Python for Garmin integration, and Streamlit for the web interface. Two YouTube videos came out of it, and the code lives on GitHub.

There were the sports analytics projects — predicting tennis match outcomes with 76% accuracy, building NBA and NFL prediction models, creating a music recommendation engine using k-nearest neighbors on Spotify's audio features. Each one was a vehicle for learning machine learning concepts, but also for testing the limits of AI-assisted development.

And then there were the philosopher-named tools. Nietzsche.cc for presentations — a slide deck generator that competed with platforms like Gamma. Montaigne.cc for media processing. Ricoeur.cc for conversation search. Each named after a thinker whose ideas resonated with the tool's purpose, because naming things matters, and because the existentialists were asking the same question I was grappling with: how should we live authentically in a world that's fundamentally changed?

## The Limits of the ChatGPT Paradigm

For all this productivity, I was running into walls.

The workflow always looked the same: I'd describe what I wanted in ChatGPT or Claude, get code back in the chat window, copy it into my editor, run it, hit an error, paste the error back into the chat, get a fix, paste it back, run again. A continuous loop of copy-paste-run-debug-paste-back. It worked, but it was friction. Real friction. The kind that slows you down just enough to break flow state.

And the AI had no idea what my project actually looked like. Every conversation started from zero. I'd have to explain my file structure, my dependencies, my conventions, every single time. The context window was generous — 128k tokens, 200k tokens — but I was wasting most of it on orientation rather than creation.

Worse, the AI couldn't *do* anything. It could generate code, but it couldn't run it. It could suggest file changes, but it couldn't make them. It could propose terminal commands, but it couldn't execute them. It was like having a brilliant collaborator who could only communicate through handwritten notes passed under a locked door.

I was spending more and more time being a human clipboard — a relay station between the AI's intelligence and my project's reality.

This is what I now think of as the "ChatGPT paradigm" of AI-assisted development. The model is smart, the output is useful, but the interface is a bottleneck. You're the one who has to bridge the gap between what the AI knows and what your codebase needs. And that bridge is made of copy-paste.

## Looking for Something More

By late 2025, the landscape of AI coding tools was shifting fast. Cursor had crossed $100M in annual recurring revenue. GitHub Copilot was everywhere. OpenAI's Codex had evolved from a VS Code extension to a cloud-based agent. Anthropic had launched something called Claude Code — a command-line tool that lived in your terminal and could read, write, and execute code directly in your project.

At MathWorks, I was developing a thesis I called "agents calling toolboxes" — the idea that the future wasn't about AI replacing MATLAB, but about AI agents orchestrating MATLAB's specialized toolboxes as callable assets. MCP — the Model Context Protocol — was emerging as the standard for this kind of tool integration, and I'd built one of the first MCP servers for MATLAB.

I was thinking about all of this through the lens of Ethan Mollick's *Co-Intelligence*, which I was preparing to discuss in a book club. Mollick's central argument was that AI isn't just a tool — it's a new kind of intelligence that requires new modes of collaboration. Not delegation, not supervision, but genuine co-creation.

Everything was converging. The technical capabilities were there. The conceptual frameworks were there. What was missing was the right interface — the right way to work *with* AI rather than *through* AI.

And then I installed Claude Code.

---

*What happened next — how a terminal-based AI agent transformed not just my workflow but my understanding of what human-AI collaboration could look like — is the subject of the rest of this book.*
