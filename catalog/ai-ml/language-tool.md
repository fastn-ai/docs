---
description: "LanguageTool checks grammar, spelling and style. Check text, list supported languages and manage your personal dictionary."
hidden: true
---

# LanguageTool

<img src="../../.gitbook/assets/connectors/lg/language-tool.png" alt="LanguageTool logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [languagetool.org](https://languagetool.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `languageTool` |

## Setup

LanguageTool needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect LanguageTool from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **LanguageTool**.
2. Select **Connect** on the LanguageTool card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. LanguageTool needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use LanguageTool's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Dictionary Word</td><td><code>addDictionaryWord</code></td><td>Add a word to one of a user's personal LanguageTool dictionaries so it is no longer flagged as a spelling error. Requires a LanguageTool Premium account (username + API key) - not available on the free public tier used by this connector's default setup. Personal dictionaries are capped at 500 words.</td></tr><tr><td>Check Text</td><td><code>checkText</code></td><td>Check a piece of text for grammar, spelling, and style issues using LanguageTool's free public checker. Returns detected language, and an array of matches with the issue message, offset/length in the text, suggested replacements, and the rule/category that triggered.</td></tr><tr><td>Delete Dictionary Word</td><td><code>deleteDictionaryWord</code></td><td>Remove a word from one of a user's personal LanguageTool dictionaries. Requires a LanguageTool Premium account (username + API key) - not available on the free public tier used by this connector's default setup.</td></tr><tr><td>Get Supported Languages</td><td><code>getSupportedLanguages</code></td><td>List all languages and language variants supported by LanguageTool for text checking, each with a display name, short code, and long code.</td></tr><tr><td>List Dictionary Words</td><td><code>listDictionaryWords</code></td><td>List the words stored in a user's personal LanguageTool dictionaries. Requires a LanguageTool Premium account (username + API key) - not available on the free public tier used by this connector's default setup.</td></tr></tbody></table>

