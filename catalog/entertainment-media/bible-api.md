---
description: "Bible API serves verses in public-domain translations. Look up passages, chapters and random verses, and list books and translations."
hidden: true
---

# Bible API

<img src="../../.gitbook/assets/connectors/lg/bible-api.png" alt="Bible API logo">

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [bible-api.com](https://bible-api.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `bibleApi` |

## Setup

Bible API needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Bible API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bibleApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Chapter</td><td><code>getChapter</code></td><td>Get every verse of one chapter of a book in a translation Docs: https://bible-api.com/</td></tr><tr><td>Get Passage</td><td><code>getPassage</code></td><td>Get a verse or passage from a free-form reference as a user would type it, e.g. john 3:16, jn 3:16 or matt 25:31-33,46 Default translation is the World English Bible. Docs: https://bible-api.com/</td></tr><tr><td>Get Random Verse</td><td><code>getRandomVerse</code></td><td>Get one random verse from the whole Bible in a translation Docs: https://bible-api.com/</td></tr><tr><td>Get Random Verse from Books</td><td><code>getRandomVerseFromBooks</code></td><td>Get one random verse from chosen books, or from the Old or New Testament Docs: https://bible-api.com/</td></tr><tr><td>List Books</td><td><code>listBooks</code></td><td>List the books in a translation Docs: https://bible-api.com/</td></tr><tr><td>List Chapters</td><td><code>listChapters</code></td><td>List the chapters of one book in a translation Docs: https://bible-api.com/</td></tr><tr><td>List Translations</td><td><code>listTranslations</code></td><td>List every Bible translation the service offers, with language and license Docs: https://bible-api.com/</td></tr></tbody></table>

## Events

Bible API has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
