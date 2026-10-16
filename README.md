# Tiny Harness
## Why?
I've been somewhat of an AI hater/skeptic for a while. We're at the point where it's impact is undeniable. So far I've been keeping my AI usage to a minimum as I'm still very fresh as a developer (2+ years of work experience) so I feel like I'm at a stage where relying on AI to write code for me will be a huge boost to my productivity but also a huge disservice to my learning.

The past few months I've started to look into all the crazy stuff people have been doing with AI. It's not just hype anymore, this thing is extremely powerful. In one hand models have gotten considerably better, but I think the major upgrade we've had is the harness. People have figured out the most insane workflows using AI, this drew my attention, there's a skill to this.

As I was studying people's workflows I realised that the central piece that allows for all of that is the harness, and I was completely out of the loop in how this thing works and what you could do with it.

The more I looked into it, the harness capabilities, the more fascinated I got, the more I wanted to learn about it. But this has already gone so far that I was feeling a little bit lost. I decided to take it super slow to really understand the fundamentals of what a model does and what a harness does. Best way that came to mind was to implement my own tiny harness.

I don't intend this to be any more than a learning project, I don't want to build a product that'll replace Pi/Opencode or whatever. I am doing this really just so I can better understand these concepts.

Ironically, I am not using AI except for helping me search documentation and occasional questions. All code will be hand crafted by me so excuse me if it looks like trash. I'd rather have lower quality code that I created than better code that not only didn't create but have no idea how it works.

## What I've got so far
- Harness with a basic loop that that saves and sends the whole conversation on each request
- Ability to switch between models
- Extremely basic tool call to read files
- Tool to list directories, doesn't allow listing outside the project, can't list recursively for now

## TODO
- Find a proper architecture so the project can grow in complexity without becoming spaghetti in only two commits
- Safeguards for the read tool
- Write tool (I'm thinking of just using some library to generate diffs and implement changes instead of reinventing the wheel here)
- A "delegate" tool call or whatever people call that, so that an agent can start another session without polluting the main session's context
- Allow different agents to use different models (e.g. main agent uses a general purpose model can call "delegate" to the coding agent, coding agent uses a model that is best at coding)

## Would also be nice
- "search" tool
- Compact context
- Plan mode
- Skills

## Docs / Useful links
[Ollama's Qwen3.8:27b](https://ollama.com/library/qwen3.8:27b)
[Tool Calling in Ollama](https://docs.ollama.com/capabilities/tool-calling#python)
[Project Layout Reference](https://realpython.com/ref/best-practices/project-layout/)
[Chat API](https://docs.ollama.com/api/chat)
