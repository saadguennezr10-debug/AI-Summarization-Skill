---
name: precision-text-summarization
version: 1.0.0
language: multilingual
input: image-or-text
purpose: faithful educational summarization
---

# Precision Text Summarization Skill

## Definition

Rewrite the source in new wording while preserving its essential content, meaning, structure, and order, aiming for approximately one quarter to one third of the original size.

This is not sentence deletion, mechanical compression, paraphrase-by-sentence, commentary, or free-form interpretation.

## Required pipeline

### Phase 1 — Read and understand
Read the entire source before drafting. Determine the topic, central idea, essential ideas, relationships between ideas, text type/pattern, and difficult or ambiguous vocabulary.

Interpret ambiguous vocabulary only from the source context. Never invent an uncertain word.

### Phase 2 — Keywords
Extract keywords that help reconstruct the essential ideas.

### Phase 3 — Essential ideas
Extract every essential idea in the exact order in which it appears. Preserve essential ideas; compress or remove secondary details, non-essential examples, repetition, and extended explanations.

### Phase 4 — Verification
Compare the extracted ideas against the complete source. Check that no essential idea is missing, no meaning changed, no idea was invented, and the original order remains intact.

### Phase 5 — Rewrite
Set aside the source wording and reconstruct the summary from the verified ideas. Preserve technical terms and proper names when necessary, but avoid copying the author's sentence structure. Write clearly, naturally, and faithfully.

### Phase 6 — Length control
Aim for 25–33% of the source word count. This is a target, not permission to delete essential meaning. If strict compression would remove a core idea, prioritize fidelity.

### Phase 7 — Quality control
Verify that:
- every essential idea is represented and the order is preserved;
- the source meaning and text type/pattern are preserved;
- no outside information, opinions, or unsupported conclusions were added;
- wording is independently constructed;
- non-essential details and repetition were removed;
- tense and pronoun relationships remain correct;
- the result is coherent, cohesive, correctly punctuated, and grammatically clear;
- the length is approximately 25–33%, where feasible.

Revise before responding if a mandatory check fails.

## Forbidden behaviors

Do not add facts from memory, the web, or general knowledge; add unstated causes, consequences, examples, or conclusions; provide criticism, praise, opinions, or reactions; omit a core idea to reach a shorter length; unnecessarily imitate the author's structure; reorder essential ideas; or fabricate unreadable text from an image.

## Image input protocol

1. Inspect the complete image.
2. Recover the readable text.
3. Identify uncertain portions and do not guess them.
4. Apply the full summarization pipeline.
5. If the image prevents reliable understanding, ask for a clearer image.

## Default output protocol

Unless the user requests another format, provide:
1. Topic
2. Keywords
3. Essential ideas in order
4. Approximate source and target word counts
5. Final summary
6. Final quality check

For a coherent paragraph source, the final summary should normally be a coherent paragraph too.

## Multilingual behavior

Apply the same principles to Arabic, French, English, and other languages. For Arabic, support right-to-left text, preserve precise terminology, use appropriate punctuation, and maintain tense and pronoun relationships.

## Priority rule

When constraints conflict, prioritize:
1. factual fidelity;
2. preservation of essential ideas;
3. original order and text type;
4. clear, independently written wording;
5. target length.

Never sacrifice an essential idea merely to satisfy a word-count target.
