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

## Connect in Fastn

Your customers connect Gutendex from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Gutendex**.
2. Select **Connect** on the Gutendex card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Gutendex needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Gutendex's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Book</td><td><code>getBook</code></td><td>Returns one book by Project Gutenberg id: title, authors, translators, subjects, bookshelves, summaries, languages, copyright, download count and format download links. Docs: https://gutendex.com/</td></tr><tr><td>List Books</td><td><code>listBooks</code></td><td>Searches and lists Project Gutenberg books (32 per page, most popular first by default) with filters for words in title/author, topic, languages, author lifetime, copyright status, ids and MIME type. Docs: https://gutendex.com/</td></tr></tbody></table>

