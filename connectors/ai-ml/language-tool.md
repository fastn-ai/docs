---
description: "Grammar, spelling, and style checker API by LanguageTool."
---

# LanguageTool

Grammar, spelling, and style checker API by LanguageTool. Uses the free, public, anonymous API tier at api.languagetool.org - no signup or API key required for text checking and language listing. Personal-dictionary endpoints (list/add/delete words) require a separate Premium account with username + API key and are not usable on this free tier.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [languagetool.org](https://languagetool.org) |
| **Authentication** | No authentication |
| **Actions** | 5 |
| **Events** | 0 |
| **Slug** | `languageTool` |

## Use it

Add LanguageTool from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.languageTool.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Dictionary Word | `addDictionaryWord` | Add a word to one of a user's personal LanguageTool dictionaries so it is no longer flagged as a spelling error. Requires a LanguageTool Premium account (username + API key) - not available on the free public tier used by this connector's default setup. Personal dictionaries are capped at 500 words. |
| Check Text | `checkText` | Check a piece of text for grammar, spelling, and style issues using LanguageTool's free public checker. Returns detected language, and an array of matches with the issue message, offset/length in the text, suggested replacements, and the rule/category that triggered. |
| Delete Dictionary Word | `deleteDictionaryWord` | Remove a word from one of a user's personal LanguageTool dictionaries. Requires a LanguageTool Premium account (username + API key) - not available on the free public tier used by this connector's default setup. |
| Get Supported Languages | `getSupportedLanguages` | List all languages and language variants supported by LanguageTool for text checking, each with a display name, short code, and long code. |
| List Dictionary Words | `listDictionaryWords` | List the words stored in a user's personal LanguageTool dictionaries. Requires a LanguageTool Premium account (username + API key) - not available on the free public tier used by this connector's default setup. |
