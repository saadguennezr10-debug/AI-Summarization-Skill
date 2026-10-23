# Platform Setup Guide: Gemini, Claude, and ChatGPT

This project is a reusable AI summarization instruction set, not a browser extension. There is no single installer that automatically adds it to every AI service. Use the platform-specific method below. Interface labels and plan availability may change, so consult the linked official help pages if a menu differs.

## 1. Google Gemini — create a Gem

The most reusable option in Gemini is a custom Gem with the summarization instructions.

1. Download the repository ZIP from GitHub using **Code → Download ZIP**, then extract it.
2. Open [Gemini](https://gemini.google.com/).
3. Open **Gems** in the sidebar, then choose **New Gem**.
4. Name it **AI Summarization Skill**.
5. Open [the universal prompt](prompts/universal-prompt.md) and copy its full contents into the Gem's **Instructions** field.
6. If the interface offers **Knowledge → Add files**, optionally upload `ai-summarization-skill/SKILL.md` as reference material. Instructions should remain in the Instructions field.
7. Save the Gem and test it with a short passage. Check that it preserves all essential ideas and does not add outside facts.

Official guide: [Use Gems in Gemini Apps](https://support.google.com/gemini/answer/15146780?hl=en).

**Upcoming interface change:** Google's current help page says Gems on personal Google accounts are scheduled to transition to Skills starting in November 2026, but says the transition for users under 18 will happen later. Google's Skills feature currently has an 18+ eligibility requirement. Use only the features available for your account and follow Google's current official guide; do not try to bypass eligibility rules. The copy-and-paste prompt remains a fallback where allowed.

## 2. Anthropic Claude — use a Project or paste the instructions

### Option A: Claude Project (when available)

1. Open [Claude](https://claude.ai/).
2. Create a new Project, if Projects are available for your account.
3. Open the [Claude-optimized Project instructions](prompts/claude-project-instructions.md) and copy the section titled **Project instructions to paste**. If you prefer, use the [universal prompt](prompts/universal-prompt.md).
4. Paste the instructions into the Project Instructions field and save.
5. Optionally add `ai-summarization-skill/SKILL.md` to the Project knowledge, if file uploads are available.
6. Start a chat inside that Project and test it with a short passage.

Projects are currently plan-dependent; if you do not see Projects, use Option B.

### Option B: use it in a normal chat

1. Open [the universal prompt](prompts/universal-prompt.md).
2. Copy its full contents and paste them into a new Claude chat.
3. Below the instructions, add the text or readable image you want summarized.

Official guides: [Create and manage Projects](https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects) and [supported document uploads](https://support.anthropic.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai).

## 3. OpenAI ChatGPT — use a Project, Custom Instructions, or a chat

### Option A: ChatGPT Project (if available)

1. Open [ChatGPT](https://chatgpt.com/).
2. Create a Project if that option is available in your account.
3. Open [the universal prompt](prompts/universal-prompt.md), copy its complete contents, and paste it into the Project Instructions field.
4. If useful, upload `ai-summarization-skill/SKILL.md` as a reference file.
5. Start a chat in that Project and test the summarization process.

### Option B: Custom Instructions (if available)

1. Open ChatGPT settings and look for **Personalization / Custom Instructions**.
2. Paste the contents of [the universal prompt](prompts/universal-prompt.md) into the relevant instruction field, if it fits the field's limits.
3. Save the changes and test the instructions with a short passage.

### Option C: use it for one conversation

1. Open [the universal prompt](prompts/universal-prompt.md).
2. Copy the complete instructions into a ChatGPT conversation.
3. Add the source text or a clear image and ask for a faithful summary.

Custom GPT creation and some personalization features can depend on the current plan, workspace, and account settings. The methods above do not require you to create or publish a GPT.

Official guides: [ChatGPT capabilities](https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview) and [file uploads](https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt).

## Recommended instruction file

For the simplest cross-platform setup, use **[`prompts/universal-prompt.md`](prompts/universal-prompt.md)**. It is designed to be copied into instruction fields or chats. The full [`SKILL.md`](ai-summarization-skill/SKILL.md) is also available for clients that support the Agent Skills format.

## Multilingual evaluation

Use the [multilingual platform test suite](tests/platform-multilingual-test-suite.md) to evaluate Arabic, French, and English. It includes required ideas, failure indicators, and a results log. The results are marked “Not run” until each live service is tested manually.

## Test after setup

Try a short school passage and check that the assistant:

- identifies the topic and keywords;
- lists essential ideas in the original order;
- does not add outside facts, opinions, or invented details;
- does not guess unclear words in images;
- prioritizes fidelity over the 25–33% target length.

## Troubleshooting

- **No Projects, Gems, or custom instructions option:** use the copy-and-paste method in a normal chat.
- **The assistant misses key ideas:** remind it that accuracy and coverage matter more than the target length.
- **The image is blurry:** upload a clearer image or paste the text; do not ask the assistant to guess.
- **I expected a browser extension:** this repository is not a Chrome or Edge extension.
- **The interface looks different:** follow the service's current official help page linked above. Features and account eligibility can change.

## Privacy note

Only upload source material you are allowed to share. Review each provider's data and privacy settings before uploading private or sensitive documents.
