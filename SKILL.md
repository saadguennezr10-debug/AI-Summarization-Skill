---
name: ai-summarization-skill
description: Summarize educational text or readable text from images faithfully in Arabic, French, English, and other languages. Produce an actual rewritten summary, not only an idea list. Preserve every essential idea and the original order, avoid outside facts, and prioritize accuracy over a target length.
license: MIT
metadata:
  author: saadguennezr10-debug
  version: "1.4.0"
---

# Precision Text Summarization Skill

## Strict activation mode

**Start PH** is the mandatory activation keyword for direct user activation.

### Activation rule

The skill MUST remain inactive unless the user's request begins with the exact keyword **Start PH** (case-sensitive), followed by optional whitespace, punctuation, or the source/request to summarize.

- **Starts with `Start PH`** → activate the full summarization workflow.
- **Does not start with `Start PH`** → do not apply this skill.
- Do not treat `Start PH` appearing in the middle or end of a request as activation.
- Do not infer, paraphrase, translate, or replace the activation keyword.
- The keyword is a trigger only and is not part of the source text.

### Application integration rule

A host application may activate this skill programmatically. When integrating this skill into a web application, the application MUST explicitly invoke the summarization engine as if the request begins with `Start PH`, then pass the OCR-extracted source text after the activation marker. The application must not expose the activation marker as part of the source or final summary.

Recommended internal call format:

`Start PH\nSOURCE_TEXT`

The application may perform OCR, language detection, word counting, and UI rendering outside the skill. The skill is responsible for faithful summarization and final quality control.

## Core objective

The output MUST be a real summary: a newly written, coherent text that is shorter than the source while preserving its essential meaning, ideas, order, and text type.

**Critical rule:** extracting keywords or listing main ideas is an internal analysis step, NOT the final answer. Never stop after producing keywords or idea bullets when a summary has been requested.

The final summary should normally be a coherent paragraph when the source is a coherent paragraph, or preserve the source's appropriate structure when another text type requires it.

## Required pipeline

### Phase 1 — Read and understand

Read the entire source before drafting. Determine the topic, central idea, essential ideas, relationships between ideas, text type/pattern, and difficult or ambiguous vocabulary. Interpret ambiguity only from source context and never invent uncertain content.

### Phase 2 — Internal analysis

Internally extract keywords and every essential idea in exact source order. This analysis is a planning tool for reconstruction and must not replace the final summary.

### Phase 3 — Verify coverage

Compare the internal idea list against the complete source. Confirm that every essential idea is covered, no meaning has changed, no idea was invented, and the original order is preserved.

### Phase 4 — Rewrite the summary

Hide/set aside the original wording and reconstruct a shorter text from the verified ideas. Use independently written sentences and preserve necessary technical terms, proper names, tense, pronouns, relationships, and text type.

### Phase 5 — Length control

Calculate the source word count and target approximately 25–33% of the original. This is a target, not permission to remove essential meaning. If reaching 25% would delete an essential idea, prioritize fidelity and coverage.

### Phase 6 — Final quality control

Before returning the result, internally verify:
- all essential ideas are present;
- ideas remain in original order;
- every factual claim is supported by the source;
- no external facts, opinions, criticism, praise, examples, causes, consequences, or conclusions were added;
- wording is genuinely rewritten rather than copied;
- secondary detail and repetition were reduced;
- tense, pronouns, coherence, cohesion, punctuation, and grammar are correct;
- the length is approximately 25–33% where feasible.

If any mandatory check fails, revise the summary before returning it.

## Final output contract

### Default behavior

Return the **actual final summary first**. Do not return only keywords or main ideas.

A compact default result may include:
1. `SUMMARY` — the completed rewritten summary.
2. `WORD COUNT` — original and summary counts.
3. `REDUCTION` — approximate percentage.
4. `QUALITY` — pass/fail status of the internal checks.

Do NOT expose the internal keyword list or essential-idea list unless the user explicitly asks for analysis.

### Optional analysis

If the host application or user requests `Show analysis`, provide the summary plus:
- keywords;
- essential ideas in original order;
- detected text type;
- ambiguous vocabulary explained only from context;
- word counts and reduction;
- quality-control results.

Even in analysis mode, the final summary MUST be present.

### Summary-only requests

If the user asks for only the summary, output only the final summary and nothing else.

## Forbidden behaviors

Do not stop at keywords, main ideas, notes, or an outline when summarization is requested. Do not add facts from memory, the web, or general knowledge; add unstated causes, consequences, examples, or conclusions; provide criticism, praise, opinions, or reactions; omit a core idea to reach a shorter length; copy source sentences unnecessarily; reorder essential ideas; change the text type without request; or fabricate unreadable text from an image.

## Image input protocol

1. Inspect the complete image.
2. Recover the readable text with OCR or available visual reading.
3. Identify uncertain portions and do not guess them.
4. Pass the recovered source text through the full summarization pipeline.
5. If the image prevents reliable understanding, request a clearer image instead of inventing text.

## Multilingual behavior

Apply the same principles to Arabic, French, English, and other languages. Detect the source language automatically unless the user specifies another output language. Keep the summary in the source language by default. For Arabic, support RTL text, precise terminology, appropriate punctuation, and correct tense/pronoun relationships.

## Priority rule

When constraints conflict, prioritize:
1. factual fidelity;
2. preservation of every essential idea;
3. original order and text type;
4. clear, independently written wording;
5. target length.

Never sacrifice an essential idea merely to satisfy a word-count target.
