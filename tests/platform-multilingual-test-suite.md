# Multilingual Platform Evaluation Suite

Use these cases to evaluate the summarization instructions in Gemini, Claude, and ChatGPT. Paste one case at a time. The test set checks source fidelity, ordering, language consistency, and resistance to invented facts.

**Important:** The user reported that they tested the instructions on the target platforms and that the tests succeeded. The table below records this as **User-confirmed pass**; it does not assign numerical scores that were not provided.

## Scoring rubric (10 points)

- **Fidelity and no invention (0–3):** all claims are supported by the source.
- **Essential idea coverage (0–3):** all required ideas are present.
- **Original order (0–1):** ideas remain in source order.
- **Independent, clear wording (0–1):** meaning is preserved without copying sentences mechanically.
- **Language and format (0–1):** correct language and appropriate readability.
- **Length discipline (0–1):** reasonably concise; does not sacrifice fidelity for length.

**Pass:** 8/10 or higher, with no zero for fidelity or idea coverage. If the source is too short for a meaningful length ratio, do not penalize that alone.

## Case AR-01 — Arabic factual passage

### Source
تحتاج النباتات إلى الماء والضوء والهواء كي تنمو. تمتص الجذور الماء والأملاح المعدنية من التربة، بينما تصنع الأوراق الغذاء باستخدام ضوء الشمس. وقد يؤدي نقص الماء مدة طويلة إلى ذبول النبات، لكن كمية الماء المناسبة تختلف باختلاف نوع النبات والظروف المحيطة به.

### Required ideas
1. Plants need water, light, and air to grow.
2. Roots absorb water and mineral salts from soil.
3. Leaves make food using sunlight.
4. Long-term water shortage may cause wilting.
5. Appropriate water quantity varies by plant type and surrounding conditions.

### Reference summary
تحتاج النباتات إلى الماء والضوء والهواء للنمو؛ فالجذور تمتص الماء والأملاح المعدنية من التربة، وتصنع الأوراق الغذاء باستخدام ضوء الشمس. وقد يسبب نقص الماء طويلًا ذبول النبات، وتختلف الكمية المناسبة من الماء حسب نوع النبات والظروف المحيطة.

### Red flags
- Claiming all plants need the same amount of water.
- Adding fertilizer, photosynthesis details, or other facts not stated in the source.
- Omitting the final qualification about differing water needs.

## Case FR-01 — French explanatory passage

### Source
Le recyclage permet de transformer certains déchets en nouvelles matières ou en nouveaux objets. Il peut réduire la quantité de déchets envoyés aux décharges et limiter l'utilisation de matières premières. Cependant, tous les déchets ne sont pas recyclables, et le tri doit respecter les consignes locales.

### Required ideas
1. Recycling transforms some waste into new materials or objects.
2. It can reduce waste sent to landfills.
3. It can limit the use of raw materials.
4. Not all waste is recyclable.
5. Sorting must follow local instructions.

### Reference summary
Le recyclage transforme certains déchets en nouvelles matières ou en objets. Il peut diminuer les déchets envoyés aux décharges et limiter l'emploi de matières premières. Toutefois, tous les déchets ne sont pas recyclables et le tri doit suivre les consignes locales.

### Red flags
- Saying all waste can be recycled.
- Claiming recycling eliminates pollution or landfills.
- Dropping the local sorting instructions.

## Case EN-01 — English process passage

### Source
A school library introduced a digital borrowing system in September. Students can search the catalogue online and reserve available books. They still need to show their school card when collecting a book. During the first month, the library reported shorter queues, but it did not publish figures about the total number of loans.

### Required ideas
1. A school library introduced a digital borrowing system in September.
2. Students can search the catalogue online and reserve available books.
3. Students must still show their school card at collection.
4. The library reported shorter queues during the first month.
5. It did not publish total-loan figures.

### Reference summary
In September, a school library introduced a digital borrowing system that lets students search the catalogue online and reserve available books. They must still show their school card when collecting a book. The library reported shorter queues during the first month but published no figures for total loans.

### Red flags
- Inventing numbers about loans or queue reduction.
- Saying books are delivered to students.
- Omitting the missing-data limitation.

## Results log

The user reported successful testing of the instructions on the target platforms. Because no numerical scores were provided, this log records the outcome without inventing scores.

| Platform | AR-01 | FR-01 | EN-01 | Notes |
|---|---|---|---|---|
| Gemini | User-confirmed pass | User-confirmed pass | User-confirmed pass | Tested successfully by user |
| Claude | User-confirmed pass | User-confirmed pass | User-confirmed pass | Tested successfully by user |
| ChatGPT | User-confirmed pass | User-confirmed pass | User-confirmed pass | Tested successfully by user |

## Fixing failures

- If fidelity or coverage scores below 2/3, strengthen the instruction to verify the idea list against the source before writing.
- If ideas are reordered, explicitly require the original order and compare each idea to the source sequence.
- If outside facts appear, state that only source-supported claims are permitted.
- If the summary is too long, remove repetition and secondary detail, not essential ideas.
- If the summary is too short, prioritize coverage over the 25–33% target.
