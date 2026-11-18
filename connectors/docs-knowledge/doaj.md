---
description: "DOAJ (Directory of Open Access Journals) is a community-curated index of peer-reviewed open access journals and their articles."
---

# DOAJ (Directory of Open Access Journals)

DOAJ (Directory of Open Access Journals) is a community-curated index of peer-reviewed open access journals and their articles. Its free public API (v4) searches articles and journals with Elasticsearch query strings and gets single article and journal records. No API key needed for search and read.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [doaj.org](https://doaj.org) |
| **Authentication** | No authentication |
| **Actions** | 4 |
| **Events** | 0 |
| **Slug** | `doaj` |

## Use it

Add DOAJ (Directory of Open Access Journals) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.doaj.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Article | `getArticle` | Get one article's DOAJ record by its DOAJ id (GET /api/v4/articles/{article_id}). Docs: https://doaj.org/api/v4/docs |
| Get Journal | `getJournal` | Get one journal's DOAJ record by its DOAJ id (GET /api/v4/journals/{journal_id}). Docs: https://doaj.org/api/v4/docs |
| Search Articles | `searchArticles` | Search DOAJ article metadata (title, abstract, authors, DOI, journal, keywords, links) with a query string, paging and sort (GET /api/v4/search/articles/{search_query}). Docs: https://doaj.org/api/v4/docs |
| Search Journals | `searchJournals` | Search DOAJ-indexed open access journals (title, ISSN, publisher, licence, APCs, subjects, editorial policy) with a query string, paging and sort (GET /api/v4/search/journals/{search_query}). Docs: https://doaj.org/api/v4/docs |
