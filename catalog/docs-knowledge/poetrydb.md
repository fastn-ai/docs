---
description: "PoetryDB is a free collection of classic English poems. Find poems by author, title, line text or line count, or get random ones."
hidden: true
---

# PoetryDB

<img src="../../.gitbook/assets/connectors/lg/poetrydb.png" alt="PoetryDB logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [poetrydb.org](https://poetrydb.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `poetrydb` |

## Setup

PoetryDB needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect PoetryDB from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **PoetryDB**.
2. Select **Connect** on the PoetryDB card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. PoetryDB needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use PoetryDB's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Poems</td><td><code>getPoems</code></td><td>Get the first N poems fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>Get Poems by Author</td><td><code>getPoemsByAuthor</code></td><td>Get poems whose author matches the name or part of it fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>Get Poems by Line Count</td><td><code>getPoemsByLineCount</code></td><td>Get poems with exactly the given number of lines fields}). Section headings count, empty lines do not. Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>Get Poems by Title</td><td><code>getPoemsByTitle</code></td><td>Get poems whose title matches the text or part of it fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>Get Random Poems</td><td><code>getRandomPoems</code></td><td>Get N random poems fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>List Authors</td><td><code>listAuthors</code></td><td>List the names of all authors in PoetryDB Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>List Titles</td><td><code>listTitles</code></td><td>List the titles of all poems in PoetryDB Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>Search Poem Lines</td><td><code>searchPoemLines</code></td><td>Get poems containing the given text in any of their lines fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>Search Poems (Combined)</td><td><code>searchPoems</code></td><td>Search with several input fields at once fields}). With one term per field the fields are combined with AND (e.g. fields author,linecount and terms Shakespeare;14); with a single term over several of author/title/lines it is an OR. Each term may end in:abs or:word. poemcount or random can be added as a field to cap results. Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr></tbody></table>

