---
description: "PoetryDB is a free API with thousands of classic English poems."
---

# PoetryDB

PoetryDB is a free API with thousands of classic English poems. List authors and titles, and find poems by author, title, line text or line count, get random poems, or combine fields in one search, choosing which fields come back. No API key needed.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [poetrydb.org](https://poetrydb.org) |
| **Authentication** | No authentication |
| **Actions** | 9 |
| **Events** | 0 |
| **Slug** | `poetrydb` |

## Use it

Add PoetryDB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.poetrydb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Poems | `getPoems` | Get the first N poems (GET /poemcount/{count}/{output fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference |
| Get Poems by Author | `getPoemsByAuthor` | Get poems whose author matches the name or part of it (GET /author/{author}/{output fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference |
| Get Poems by Line Count | `getPoemsByLineCount` | Get poems with exactly the given number of lines (GET /linecount/{count}/{output fields}). Section headings count, empty lines do not. Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference |
| Get Poems by Title | `getPoemsByTitle` | Get poems whose title matches the text or part of it (GET /title/{title}/{output fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference |
| Get Random Poems | `getRandomPoems` | Get N random poems (GET /random/{count}/{output fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference |
| List Authors | `listAuthors` | List the names of all authors in PoetryDB (GET /author). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference |
| List Titles | `listTitles` | List the titles of all poems in PoetryDB (GET /title). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference |
| Search Poem Lines | `searchPoemLines` | Get poems containing the given text in any of their lines (GET /lines/{text}/{output fields}). Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference |
| Search Poems (Combined) | `searchPoems` | Search with several input fields at once (GET /{fields}/{terms}/{output fields}). With one term per field the fields are combined with AND (e.g. fields author,linecount and terms Shakespeare;14); with a single term over several of author/title/lines it is an OR. Each term may end in :abs or :word. poemcount or random can be added as a field to cap results. Errors come back as HTTP 200 with a body like {"status":404,"reason":"Not found"}. Docs: https://github.com/thundercomb/poetrydb#api-reference |
