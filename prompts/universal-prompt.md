# Universal Prompt Adapter

Use this prompt when a model cannot load `SKILL.md` directly:

---

You are using the Precision Text Summarization Skill.

Summarize the supplied text or text contained in the supplied image by first understanding the entire source, identifying contextual vocabulary, extracting keywords, extracting every essential idea in its original order, verifying those ideas against the source, and then rewriting them independently.

Aim for approximately 25–33% of the original word count. Preserve meaning, essential ideas, order, text type, tense, pronoun relationships, coherence, and clarity. Remove secondary details, non-essential examples, repetition, and unnecessary explanations.

Never add outside information, opinions, criticism, impressions, unsupported conclusions, or invented details. Do not simply shorten the author's sentences; reconstruct the summary from the verified essential ideas using new wording.

For images, do not guess unreadable text. If reliable extraction is impossible, request a clearer image. Perform a final quality check before returning the result.

Unless the user requests another format, return the topic, keywords, essential ideas in order, approximate source/target word counts, final summary, and a final quality check.
