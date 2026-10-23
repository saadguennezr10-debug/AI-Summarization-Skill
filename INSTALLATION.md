# Installation and Usage

This project is an AI instruction skill, **not a browser extension**. It does not install itself into an AI product or change a model's training. The installation method depends on the AI client.

## Download from GitHub

### Download the whole project (recommended)

1. Open the [project page](https://github.com/saadguennezr10-debug/AI-Summarization-Skill).
2. Click the green **Code** button.
3. Choose **Download ZIP**.
4. When the download finishes, extract the ZIP archive.
5. Open the extracted folder and locate `ai-summarization-skill/SKILL.md`.

You can also [open the skill file directly](ai-summarization-skill/SKILL.md) if you only need its instructions.

## Method 1 — Install in an Agent Skills-compatible client

1. Read the AI client's official documentation and look for **Skills**, **Agent Skills**, or **local skills**.
2. Find the exact skills directory supported by that client.
3. Copy the entire `ai-summarization-skill` folder into that directory.
4. Enable the skill or reload the client if its documentation requires it.
5. Test it on a short text and review the result using the [evaluation checklist](tests/evaluation-checklist.md).

**Important:** There is no single installation path shared by all AI apps. Do not copy the folder to an arbitrary location if your client does not document local skill support.

## Method 2 — Use it with custom instructions

If your AI client does not support skill folders:

1. Open [the universal prompt adapter](prompts/universal-prompt.md).
2. Copy the complete instructions.
3. Paste them into the client's custom instructions or project instructions field, if available.
4. If no persistent instruction field is available, send the instructions along with your summarization request.
5. Paste your source text or upload a readable image.

You may also open [the skill file](ai-summarization-skill/SKILL.md) and copy its instructions instead.

## Method 3 — Use for one task

Open [the skill file](ai-summarization-skill/SKILL.md), copy the instructions into your AI conversation, and then provide the source text or image.

## Troubleshooting

- **I cannot find a Skills setting:** use Method 2; do not assume your app supports Agent Skills.
- **The AI ignores the instructions:** check that the full instructions were included and that the platform accepts custom instructions.
- **Text in an image is unclear:** upload a sharper image or paste the text; the skill must not guess unreadable words.
- **The summary is too short:** remind the AI that preserving all essential ideas matters more than meeting the 25–33% target.
- **I expected a browser add-on:** this repository is not a Chrome/Edge extension and cannot be installed from the browser's extensions page.

## Validate the package

Python 3 is required only if you want to run the repository's lightweight validator locally; the skill itself has no runtime dependencies.

```bash
python scripts/validate_skill.py
```

This checks basic metadata and structure. It does not prove compatibility with every AI platform or guarantee the quality of every summary.

## Privacy and compatibility

- The skill uses plain Markdown instructions and requires no runtime packages during normal use.
- The AI client must load or receive the instructions for them to affect behavior.
- Image text extraction depends on the AI client's vision/OCR capabilities.
- Do not upload confidential or personal source material unless you are allowed to share it and understand the service's data practices.

See the [Agent Skills specification](https://agentskills.io/specification) and your AI client's official documentation for platform-specific requirements.
