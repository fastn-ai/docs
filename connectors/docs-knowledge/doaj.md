---
description: "DOAJ (Directory of Open Access Journals) is a community-curated index of peer-reviewed open access journals and their articles."
hidden: true
---

# DOAJ (Directory of Open Access Journals)

<img src="../../.gitbook/assets/connectors/lg/doaj.png" alt="DOAJ (Directory of Open Access Journals) logo">

Its free public API (v4) searches articles and journals with Elasticsearch query strings and gets single article and journal records. No API key needed for search and read.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [doaj.org](https://doaj.org) |
| **Authentication** | No authentication |
| **Slug** | `doaj` |

## Use it

Add DOAJ (Directory of Open Access Journals) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.doaj.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Article</td><td><code>getArticle</code></td><td>Get one article's DOAJ record by its DOAJ id (GET /api/v4/articles/{article_id}). Docs: https://doaj.org/api/v4/docs</td></tr><tr><td>Get Journal</td><td><code>getJournal</code></td><td>Get one journal's DOAJ record by its DOAJ id (GET /api/v4/journals/{journal_id}). Docs: https://doaj.org/api/v4/docs</td></tr><tr><td>Search Articles</td><td><code>searchArticles</code></td><td>Search DOAJ article metadata (title, abstract, authors, DOI, journal, keywords, links) with a query string, paging and sort (GET /api/v4/search/articles/{search_query}). Docs: https://doaj.org/api/v4/docs</td></tr><tr><td>Search Journals</td><td><code>searchJournals</code></td><td>Search DOAJ-indexed open access journals (title, ISSN, publisher, licence, APCs, subjects, editorial policy) with a query string, paging and sort (GET /api/v4/search/journals/{search_query}). Docs: https://doaj.org/api/v4/docs</td></tr></tbody></table>
