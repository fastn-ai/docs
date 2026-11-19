---
description: "PoetryDB is a free API with thousands of classic English poems."
hidden: true
---

# PoetryDB

PoetryDB is a free API with thousands of classic English poems. List authors and titles, and find poems by author, title, line text or line count, get random poems, or combine fields in one search, choosing which fields come back. No API key needed.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [poetrydb.org](https://poetrydb.org) |
| **Authentication** | No authentication |
| **Slug** | `poetrydb` |

## Use it

Add PoetryDB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.poetrydb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Poems</td><td><code>getPoems</code></td><td>Get the first N poems (GET /poemcount/{count}/{output fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>Get Poems by Author</td><td><code>getPoemsByAuthor</code></td><td>Get poems whose author matches the name or part of it (GET /author/{author}/{output fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>Get Poems by Line Count</td><td><code>getPoemsByLineCount</code></td><td>Get poems with exactly the given number of lines (GET /linecount/{count}/{output fields}). Section headings count, empty lines do not. Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>Get Poems by Title</td><td><code>getPoemsByTitle</code></td><td>Get poems whose title matches the text or part of it (GET /title/{title}/{output fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>Get Random Poems</td><td><code>getRandomPoems</code></td><td>Get N random poems (GET /random/{count}/{output fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>List Authors</td><td><code>listAuthors</code></td><td>List the names of all authors in PoetryDB (GET /author). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>List Titles</td><td><code>listTitles</code></td><td>List the titles of all poems in PoetryDB (GET /title). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>Search Poem Lines</td><td><code>searchPoemLines</code></td><td>Get poems containing the given text in any of their lines (GET /lines/{text}/{output fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr><tr><td>Search Poems (Combined)</td><td><code>searchPoems</code></td><td>Search with several input fields at once (GET /{fields}/{terms}/{output fields}). With one term per field the fields are combined with AND (e.g. fields author,linecount and terms Shakespeare;14); with a single term over several of author/title/lines it is an OR. Each term may end in :abs or :word. poemcount or random can be added as a field to cap results. Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference</td></tr></tbody></table>
