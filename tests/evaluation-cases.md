# Evaluation Cases

Use these cases to test whether the skill produces a real rewritten summary, not only an analysis or idea list. The expected results describe required facts and order, not one exact wording.

## Case 1 — Arabic cause and effect

**Source**

تحتاج النباتات إلى الماء والضوء لكي تنمو. فعندما يقل الماء، تذبل الأوراق وقد يتوقف النمو. أما الضوء فيساعد النبات على صنع غذائه. لذلك يجب توفير الماء والضوء بقدر مناسب.

**A passing summary must**
- be a coherent rewritten summary, not only keywords or bullet-point ideas;
- mention the need for both water and light;
- keep the source's order: general needs, effect of water shortage, role of light, conclusion;
- avoid adding plant-care facts not in the source.

## Case 2 — French historical explanation

**Source**

Au XIXe siècle, plusieurs villes se développent rapidement. L'arrivée de nouvelles usines attire des travailleurs depuis les campagnes. La population urbaine augmente, mais les logements et les services ne suivent pas toujours ce rythme.

**A passing summary must**
- be written as an actual concise French summary;
- retain the period and rapid urban growth;
- preserve the link between factories and workers moving from rural areas;
- mention that housing and services do not always keep pace;
- not invent a specific country, statistic, or political cause.

## Case 3 — English process

**Source**

A seed absorbs water and begins to germinate. A small root emerges first and anchors the seedling. Then the shoot grows upward toward the light. The young plant continues growing when it receives suitable water, light, and nutrients.

**A passing summary must**
- be a coherent rewritten paragraph, not an outline;
- preserve the sequence: water absorption, root, shoot, continued growth;
- retain the conditions for continued growth;
- not add stages or scientific details absent from the source.

## Case 4 — Length target versus completeness

**Task**

Summarize a source with five distinct essential ideas in a very short paragraph.

**A passing response must**
- keep all five essential ideas;
- produce a real rewritten summary;
- be concise where possible;
- explain briefly if the requested length would otherwise force omission, rather than silently dropping a core idea.

## Case 5 — Unreadable image text

**Task**

An uploaded page contains a sentence whose key noun is too blurred to read.

**A passing response must**
- identify that the relevant text is unclear;
- ask for a clearer image or typed text;
- never guess the noun or build a summary around an unsupported guess.

## Case 6 — Outside knowledge temptation

**Task**

The source describes one cause of an event but says nothing about its consequences.

**A passing response must**
- summarize only the cause and other ideas actually present;
- not add consequences from general knowledge;
- keep the original order of essential ideas.

## Case 7 — Regression: ideas are not the final answer

**Source**

تحتاج النباتات إلى الماء والضوء والهواء كي تنمو. تمتص الجذور الماء والأملاح المعدنية من التربة، بينما تصنع الأوراق الغذاء باستخدام ضوء الشمس. وقد يؤدي نقص الماء مدة طويلة إلى ذبول النبات، لكن كمية الماء المناسبة تختلف باختلاف نوع النبات والظروف المحيطة به.

**A passing response must**
- contain an actual rewritten summary in Arabic;
- combine the essential ideas into coherent sentences;
- preserve their original order;
- be substantially shorter than the source;
- NOT stop after listing keywords or main ideas;
- NOT expose the internal idea extraction unless analysis was requested.

**Example of a passing form**

`تحتاج النباتات إلى الماء والضوء والهواء للنمو؛ فالجذور تمتص الماء والأملاح المعدنية من التربة، وتصنع الأوراق الغذاء باستخدام ضوء الشمس. وقد يسبب نقص الماء طويلًا ذبول النبات، وتختلف الكمية المناسبة حسب نوع النبات والظروف المحيطة.`

The wording may differ; the required behavior is a coherent rewritten summary.

## Case 8 — Strict activation

**Valid activation**

`Start PH` followed by source text must activate the skill.

**Invalid activation**

`start ph`, `START PH`, `Please Start PH`, and requests containing `Start PH` only in the middle or end must not activate the skill.

## Suggested scoring

Score each dimension from 0 to 2:
- **Fidelity:** 0 = meaning changed; 1 = minor distortion; 2 = faithful.
- **Coverage:** 0 = several core ideas missing; 1 = one core idea missing; 2 = all core ideas retained.
- **Order:** 0 = materially reordered; 1 = minor order issue; 2 = source order preserved.
- **Grounding:** 0 = unsupported additions; 1 = questionable addition; 2 = no unsupported additions.
- **Summary output:** 0 = only ideas/outline; 1 = partial or awkward summary; 2 = complete coherent rewritten summary.

Maximum: 10 points per case. A suggested release gate is at least 8/10 per case, with **no zero in fidelity, coverage, grounding, or summary output**. This is a manual evaluation rubric, not an automated benchmark.
