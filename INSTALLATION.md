# Installation and Usage

This repository packages a reusable summarization skill. It does not install itself into an AI product or change a model's training.

## Option 1 — Use as a standard Agent Skill

1. Download or clone this repository.
2. Put the skill folder in a skills directory supported by your AI client.
3. Keep the `SKILL.md` file at the root of the skill folder. The folder should be named `ai-summarization-skill` to match the skill metadata.
4. Restart or refresh the client if its documentation says that is required.
5. Ask the AI to summarize a short passage and check the result against [the evaluation checklist](tests/evaluation-checklist.md).

The exact discovery directory and installation steps depend on the client. Consult the client's current official documentation; do not assume every product automatically discovers repository folders.

## Option 2 — Use with a system that does not load skill folders

1. Open [the universal prompt](prompts/universal-prompt.md).
2. Copy its full instructions into the system's instruction/custom-prompt field, or provide them as context for the task.
3. Paste the source text or upload a readable image.
4. Review the result using the evaluation checklist.

## Option 3 — Use manually for a single task

Open [SKILL.md](SKILL.md), provide its instructions to your AI assistant, then submit the source text or image.

## Compatibility notes

- The skill uses plain Markdown instructions and requires no scripts or external packages.
- A compatible client must actually load or be given these instructions for them to affect behavior.
- Image text extraction depends on the AI client's vision/OCR capabilities. If it cannot read an image reliably, provide the extracted text or a clearer image.
- The 25–33% length target is approximate. Fidelity and coverage of essential ideas take priority.
- Do not upload confidential or personal source material to an AI service unless you are allowed to share it and understand that service's data practices.

## Official format reference

This repository uses the open Agent Skills directory concept. Read the [Agent Skills specification](https://agentskills.io/specification) and your AI client's official documentation for current requirements.
