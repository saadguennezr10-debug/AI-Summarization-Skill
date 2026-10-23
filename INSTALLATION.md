# Installation and Usage

This repository packages a reusable summarization skill. It does not install itself into an AI product or change a model's training.

## Option 1 — Use as an Agent Skill

The ready-to-use package is in `ai-summarization-skill/`. Its folder name matches the `name` field in `SKILL.md`, as required by common Agent Skills implementations.

1. Download or clone this repository.
2. Copy the entire `ai-summarization-skill` folder into a skills directory supported by your AI client.
3. Follow that client's current official instructions for enabling or discovering local skills.
4. Ask the AI to summarize a short passage and check the result against [the evaluation checklist](tests/evaluation-checklist.md).

The exact discovery directory and installation steps depend on the client. Do not assume every product automatically discovers repository folders.

## Option 2 — Use with a system that does not load skill folders

1. Open [the universal prompt](prompts/universal-prompt.md).
2. Copy its full instructions into the system's instruction/custom-prompt field, or provide them as context for the task.
3. Paste the source text or upload a readable image.
4. Review the result using the evaluation checklist.

## Option 3 — Use manually for a single task

Open [the distributable SKILL.md](ai-summarization-skill/SKILL.md), provide its instructions to your AI assistant, then submit the source text or image.

## Validate the package

Python 3 is required only if you want to run the repository's lightweight validator locally; the skill itself has no runtime dependencies.

```bash
python scripts/validate_skill.py
```

The validator checks the frontmatter's required fields, name format and directory match, description limits, Markdown heading, and file length. GitHub Actions also runs this check on relevant pushes and pull requests. This is a structural sanity check, not proof that every AI platform will load the skill or that every summary will be correct.

## Compatibility and privacy notes

- The skill uses plain Markdown instructions and requires no scripts or external packages during normal use.
- A compatible client must actually load or be given these instructions for them to affect behavior.
- Image text extraction depends on the AI client's vision/OCR capabilities. If it cannot read an image reliably, provide the extracted text or a clearer image.
- The 25–33% length target is approximate. Fidelity and coverage of essential ideas take priority.
- Do not upload confidential or personal source material to an AI service unless you are allowed to share it and understand that service's data practices.

## Official format reference

Read the [Agent Skills specification](https://agentskills.io/specification) and your AI client's official documentation for current requirements.
