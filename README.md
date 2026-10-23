# AI Summarization Skill

A model-agnostic skill for faithful educational summarization of plain text and text extracted from images.

## Start here

- **[SKILL.md](SKILL.md)** — complete instructions for an AI model to follow.
- [Formal summarization rules](specifications/summarization-rules.md)
- [Universal prompt adapter](prompts/universal-prompt.md) — for models that cannot load skill files directly.
- [Basic example](examples/basic-example.md)

## Core principle

Rewrite the source in new wording while preserving its essential meaning and original order. Aim for approximately **25–33%** of the original word count, but never sacrifice an essential idea just to meet a length target.

## Workflow

1. Read and understand the complete source.
2. Identify ambiguous vocabulary using context only.
3. Extract keywords and all essential ideas in source order.
4. Verify those ideas against the full source.
5. Rewrite independently in clear language.
6. Remove non-essential details, examples, repetition, and extended explanations.
7. Check fidelity, order, grammar, coherence, and approximate length.

## Non-negotiable rules

- Do not invent information or import outside knowledge into the summary.
- Do not add opinions, criticism, impressions, or unsupported conclusions.
- Do not omit essential ideas to make the summary shorter.
- Do not imitate the author's wording unnecessarily.
- Do not guess unreadable text in images; request a clearer image when needed.

## Language support

Designed for multilingual use, including Arabic, French, and English. Follow the same fidelity rules in every language.

## License

MIT. See [LICENSE](LICENSE).
