---
description: "Gutendex lists Project Gutenberg's public-domain ebooks. Search books by title, author, topic or language and get book details."
hidden: true
---

# Gutendex

<img src="../../.gitbook/assets/connectors/lg/gutendex.png" alt="Gutendex logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [gutendex.com](https://gutendex.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `gutendex` |

## Setup

Gutendex needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Gutendex from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gutendex.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Book</td><td><code>getBook</code></td><td>Returns one book by Project Gutenberg id: title, authors, translators, subjects, bookshelves, summaries, languages, copyright, download count and format download links. Docs: https://gutendex.com/</td></tr><tr><td>List Books</td><td><code>listBooks</code></td><td>Searches and lists Project Gutenberg books (32 per page, most popular first by default) with filters for words in title/author, topic, languages, author lifetime, copyright status, ids and MIME type. Docs: https://gutendex.com/</td></tr></tbody></table>

## Events

Gutendex has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
