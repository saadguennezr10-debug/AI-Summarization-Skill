# AI Summarization Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Languages](https://img.shields.io/badge/languages-Arabic%20%7C%20French%20%7C%20English-2ea44f.svg)](#language-support)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-blue.svg)](https://agentskills.io/specification)

A model-agnostic instruction skill for faithful educational summarization of text and text extracted from images. It is designed to help AI assistants summarize without inventing facts, losing key ideas, or changing the source's meaning.

> **Important:** Publishing this skill does not automatically train or configure every AI model. A compatible client must load the skill, or you must provide its instructions manually.

## Start here

- **[Installable skill package](ai-summarization-skill/SKILL.md)** — standard Agent Skill folder with matching metadata and directory name.
- [Root copy of the instructions](SKILL.md) — convenient project reference.
- [Platform setup guide](PLATFORM_GUIDE.md) — step-by-step setup for Gemini, Claude, and ChatGPT.
- [Installation and usage guide](INSTALLATION.md) — download from GitHub, install where supported, or use custom instructions.
- [دليل التنزيل والتركيب بالعربية](README_AR.md)
- [Arabic project overview](README_AR.md)
- [Changelog](CHANGELOG.md)
- [Universal prompt adapter](prompts/universal-prompt.md) — for systems that cannot load skill folders directly.
- [Formal rules and quality gates](specifications/summarization-rules.md)
- [Basic example](examples/basic-example.md)
- [Multilingual examples](examples/multilingual-examples.md)
- [Evaluation checklist](tests/evaluation-checklist.md)
- [Evaluation cases](tests/evaluation-cases.md)
- [Validation script](scripts/validate_skill.py) — dependency-free metadata and structure checks.
- [Contributing guide](CONTRIBUTING.md)
- [MIT License](LICENSE)

## Core principle

Rewrite the source in new wording while preserving its essential meaning and original order. Aim for approximately **25–33%** of the source word count, but never sacrifice an essential idea just to meet a length target.

## Workflow

1. Read and understand the complete source.
2. Identify ambiguous vocabulary using context only.
3. Extract keywords and all essential ideas in source order.
4. Verify those ideas against the complete source.
5. Rewrite independently in clear language.
6. Remove non-essential details, examples, repetition, and extended explanations.
7. Check fidelity, order, grammar, coherence, and approximate length.

## Non-negotiable rules

- Do not add outside information to the summary.
- Do not add opinions, criticism, impressions, or unsupported conclusions.
- Do not omit essential ideas to make the summary shorter.
- Do not imitate the author's wording unnecessarily.
- Do not reorder the essential ideas.
- Do not guess unreadable text in images; request a clearer image when needed.
- If the compression target conflicts with fidelity, fidelity wins.

## Quick use

1. Read the [installation guide](INSTALLATION.md) for options. For Arabic step-by-step instructions, see [README_AR.md](README_AR.md).
2. Provide [SKILL.md](SKILL.md) to your AI system as its skill file or instructions.
3. If the system does not support skill files, copy [the universal prompt adapter](prompts/universal-prompt.md).
4. Supply the source text or a clear image of it.
5. Review the output against the [evaluation checklist](tests/evaluation-checklist.md) and [evaluation cases](tests/evaluation-cases.md).

## Default output format

Unless a user requests a different format, return:
1. Topic
2. Keywords
3. Essential ideas in source order
4. Approximate source and target word counts
5. Final summary
6. Final quality check

## Language support

Designed for multilingual use, including **Arabic, French, and English**. The same fidelity rules apply in every language. For Arabic, preserve right-to-left text and appropriate punctuation.

## Contributing

Bug reports, examples, translations, and improvements are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
