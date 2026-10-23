# AI Summarization Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Languages](https://img.shields.io/badge/languages-Arabic%20%7C%20French%20%7C%20English-2ea44f.svg)](#language-support)

A model-agnostic instruction skill for faithful educational summarization of text and text extracted from images. It is designed to help AI assistants summarize without inventing facts, losing key ideas, or changing the source's meaning.

> **Important:** Publishing this skill does not automatically train or configure every AI model. Compatible systems can load `SKILL.md`; other systems can use the universal prompt adapter.

## Start here

- **[SKILL.md](SKILL.md)** — canonical instructions for AI assistants.
- [Universal prompt adapter](prompts/universal-prompt.md) — for systems that cannot load skill files directly.
- [Formal rules and quality gates](specifications/summarization-rules.md)
- [Basic example](examples/basic-example.md)
- [Multilingual examples](examples/multilingual-examples.md)
- [Evaluation checklist](tests/evaluation-checklist.md)
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

1. Open [SKILL.md](SKILL.md) and provide it to your AI system as its instructions or skill file.
2. If the system does not support skill files, copy the instructions from [the universal prompt adapter](prompts/universal-prompt.md).
3. Supply the source text or a clear image of it.
4. Review the output against the [evaluation checklist](tests/evaluation-checklist.md).

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
