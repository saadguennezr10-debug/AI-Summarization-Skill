# Formal Specification

## Inputs
- Plain text
- One or more images containing text

## Output
A faithful, compressed reconstruction of the source.

## Compression target
`0.25 <= summary_words / source_words <= 0.33`

Approximate compliance is acceptable when strict compliance would damage fidelity.

## Invariants
1. Every essential source idea is represented.
2. No unsupported information appears in the summary.
3. Essential ideas retain their source order.
4. The summary remains semantically faithful.
5. Wording is independently constructed.
6. The source text's mode/pattern is preserved where practical.
7. Tense and pronoun relationships are preserved.
8. Examples and secondary explanations may be removed when non-essential.
9. Personal evaluation is prohibited.
10. Unreadable image text is never fabricated.

## Quality gates
A summary is accepted only if all mandatory invariants pass. Fidelity takes precedence over the compression target.
