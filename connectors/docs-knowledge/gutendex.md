---
description: "Gutendex is a free, keyless JSON API for Project Gutenberg ebook metadata: search 70,000+ public-domain books by title, author, topic, language, author…"
hidden: true
---

# Gutendex

Gutendex is a free, keyless JSON API for Project Gutenberg ebook metadata: search 70,000+ public-domain books by title, author, topic, language, author lifetime and copyright status, and get each book's authors, subjects, bookshelves, summaries and download links.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [gutendex.com](https://gutendex.com) |
| **Authentication** | No authentication |
| **Actions** | 2 |
| **Events** | 0 |
| **Slug** | `gutendex` |

## Use it

Add Gutendex from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gutendex.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Book | `getBook` | Returns one book by Project Gutenberg id: title, authors, translators, subjects, bookshelves, summaries, languages, copyright, download count and format download links. Docs: https://gutendex.com/ |
| List Books | `listBooks` | Searches and lists Project Gutenberg books (32 per page, most popular first by default) with filters for words in title/author, topic, languages, author lifetime, copyright status, ids and MIME type. Docs: https://gutendex.com/ |
