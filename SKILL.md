---
name: ai-summarization-skill
description: School-style precision summarization from text or images in Arabic, French, English, and other languages. Produce a real rewritten summary from the source, not an idea list. Preserve essential ideas, order, meaning, text type, tense, pronouns, and coherence while targeting approximately 25–33% of the source length.
license: MIT
metadata:
  author: saadguennezr10-debug
  version: "1.5.0"
---

# Precision School Text Summarization Skill

## Strict activation

**Start PH** is the mandatory direct-user activation keyword. The request must begin with the exact case-sensitive phrase `Start PH`. Do not activate when the phrase appears only in the middle or end, uses different capitalization, or is paraphrased.

For a web application, the application may activate the engine programmatically by sending `Start PH` followed by the OCR-extracted source text. The marker is never part of the source or final summary.

## Mission

The task is **real school-style summarization**, not extraction of ideas alone.

The final product must be a shorter, coherent text rewritten in new wording while preserving the source's meaning, all essential ideas, their original order, and the original text type. Keywords and essential ideas are internal planning stages; they are never a substitute for the final summary.

Definition:

> Rewrite the source in your own wording, preserving its content and essential ideas and reducing it to approximately one quarter to one third of its original word count.

## Image-to-summary workflow

When the source is an image:

1. Inspect the complete image carefully.
2. Extract the readable source text accurately, including punctuation and paragraph structure when possible.
3. Do not guess unreadable words. If an important part cannot be read reliably, identify the unclear part and request a clearer image when necessary.
4. Do not summarize before the complete readable source has been understood.
5. Run the full school summarization pipeline below.

## Phase 1 — Understand

Internally determine:
- general topic;
- general idea;
- essential ideas;
- relationships between ideas;
- sequence of events or arguments when present;
- text type/pattern;
- difficult vocabulary.

Explain ambiguous vocabulary only from the source context. Do not add encyclopedic or outside information.

## Phase 2 — Keywords

Internally extract only the keywords needed to reconstruct the essential content, such as people, places, events, causes, results, concepts, positions, main actions, and important terms.

Keywords are a tool, not the final answer.

## Phase 3 — Essential ideas

Extract every essential idea in the exact order of the source.

Remove only secondary details, unnecessary examples, long explanations, repetition, and non-essential descriptive wording.

An essential idea is the meaning that must survive in the summary. Do not copy source sentences merely to represent an idea.

## Phase 4 — Verify

Re-read/compare the source against the internal ideas and verify:
1. the topic is correct;
2. every essential idea is present;
3. no secondary detail has been promoted incorrectly;
4. no meaning has changed;
5. the order is preserved;
6. no information appears that is absent from the source.

Correct any failure before writing the summary.

## Phase 5 — Rewrite

Set aside the source wording. Reconstruct the summary from the verified ideas only.

Requirements:
- use clear, natural, correct language;
- genuinely change sentence structure and wording;
- preserve necessary technical terms and proper names;
- preserve tense and pronoun relationships;
- preserve the source's text type and style of discourse;
- preserve the order of ideas;
- connect ideas coherently;
- do not turn a coherent paragraph into bullets unless requested;
- do not add an invented introduction or conclusion.

## Phase 6 — Length control

Count source words and target approximately 25–33% of the original.

Examples:
- 120 words → about 30–40 words;
- 150 words → about 38–50 words;
- 180 words → about 45–60 words;
- 240 words → about 60–80 words;
- 300 words → about 75–100 words.

The range is a target, not a license to delete essential meaning. If reaching 25% would remove an essential idea, preserve the idea and move toward the upper end or slightly beyond the range when necessary.

## Phase 7 — Final quality control

Before displaying the final result, internally check:

### Understanding
- topic and general meaning are correct;
- the summary reflects real understanding rather than sentence deletion.

### Coverage and order
- every essential idea is represented;
- no essential idea was removed;
- the original order is preserved.

### Fidelity
- every factual claim comes from the source;
- no external information, examples, causes, consequences, interpretations, or conclusions were added.

### Rewrite
- wording is independently constructed;
- the author's sentences and structure were not merely shortened.

### Style and language
- source text type is preserved;
- tense and pronouns remain correct;
- the result is coherent, cohesive, grammatical, and correctly punctuated.

### Length
- summary is approximately 25–33% where feasible.

If any required criterion fails, rewrite the summary before returning it.

## Absolute prohibitions

Never:
- stop after keywords or idea bullets when a summary is requested;
- copy the author's sentences unnecessarily;
- delete an essential idea merely to hit a word count;
- add facts from memory, web search, or general knowledge;
- add examples not in the source;
- add unstated causes or consequences;
- add personal opinion, criticism, praise, judgment, impression, or evaluation;
- change the order of essential ideas;
- change the text type without a request;
- guess unreadable image text.

## Output contract

When the user asks for the full school analysis, return in this order:

### 1. Understanding
- General topic
- Text type/pattern
- General idea

### 2. Ambiguous vocabulary
List only words that genuinely need contextual explanation. If none: `No ambiguous vocabulary needs explanation.`

### 3. Keywords
List the most important keywords only.

### 4. Essential ideas
List the essential ideas in source order. Explicitly treat this section as **analysis only**, not the final summary.

### 5. Length calculation
Show approximate original word count, target range, and final summary word count.

### 6. Final summary
Write the actual rewritten summary as a coherent text, preserving content, essential ideas, order, text type, tense, pronouns, coherence, and language quality.

### 7. Final review
Confirm that no outside information was added, no essential idea was removed, the wording is rewritten, the length target is respected as far as feasible, order and text type are preserved, and language/grammar/punctuation are correct.

If the user asks for **summary only**, return only the final summary. If the application requests structured data, it may expose the analysis fields separately, but the final summary must always be generated.

## Multilingual behavior

Apply the same methodology to Arabic, French, English, and other languages. Detect the source language automatically unless another output language is explicitly requested. Keep the output in the source language by default. For Arabic, support RTL, appropriate Arabic punctuation, precise terminology, correct tense, and correct pronoun relationships.

## Priority order

When constraints conflict, prioritize:
1. fidelity to the source;
2. preservation of every essential idea;
3. original order and text type;
4. genuine rewriting and coherence;
5. target length.
