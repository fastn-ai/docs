---
description: "bible-api.com is a free JSON API for Bible verses and passages in 16 public-domain translations."
---

# Bible API

bible-api.com is a free JSON API for Bible verses and passages in 16 public-domain translations. Look up passages by reference, list translations, books and chapters, read a full chapter, and get random verses. No API key needed (rate limit 15 requests per 30 seconds).

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [bible-api.com](https://bible-api.com) |
| **Authentication** | No authentication |
| **Actions** | 7 |
| **Events** | 0 |
| **Slug** | `bibleApi` |

## Use it

Add Bible API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bibleApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Chapter | `getChapter` | Get every verse of one chapter of a book in a translation (GET /data/{translation}/{book}/{chapter}). Docs: https://bible-api.com/ |
| Get Passage | `getPassage` | Get a verse or passage from a free-form reference as a user would type it, e.g. john 3:16, jn 3:16 or matt 25:31-33,46 (GET /{reference}). Default translation is the World English Bible. Docs: https://bible-api.com/ |
| Get Random Verse | `getRandomVerse` | Get one random verse from the whole Bible in a translation (GET /data/{translation}/random). Docs: https://bible-api.com/ |
| Get Random Verse from Books | `getRandomVerseFromBooks` | Get one random verse from chosen books, or from the Old or New Testament (GET /data/{translation}/random/{books}). Docs: https://bible-api.com/ |
| List Books | `listBooks` | List the books in a translation (GET /data/{translation}). Docs: https://bible-api.com/ |
| List Chapters | `listChapters` | List the chapters of one book in a translation (GET /data/{translation}/{book}). Docs: https://bible-api.com/ |
| List Translations | `listTranslations` | List every Bible translation the service offers, with language and license (GET /data). Docs: https://bible-api.com/ |
