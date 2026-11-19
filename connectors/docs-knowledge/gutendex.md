---
description: "Connect Gutendex to your product with fastn."
hidden: true
---

# Gutendex

Gutendex is a free, keyless JSON API for Project Gutenberg ebook metadata: search 70,000+ public-domain books by title, author, topic, language, author lifetime and copyright status, and get each book's authors, subjects, bookshelves, summaries and download links.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [gutendex.com](https://gutendex.com) |
| **Authentication** | No authentication |
| **Slug** | `gutendex` |

## Use it

Add Gutendex from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gutendex.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Book</td><td><code>getBook</code></td><td>Returns one book by Project Gutenberg id: title, authors, translators, subjects, bookshelves, summaries, languages, copyright, download count and format download links. Docs: https://gutendex.com/</td></tr><tr><td>List Books</td><td><code>listBooks</code></td><td>Searches and lists Project Gutenberg books (32 per page, most popular first by default) with filters for words in title/author, topic, languages, author lifetime, copyright status, ids and MIME type. Docs: https://gutendex.com/</td></tr></tbody></table>
