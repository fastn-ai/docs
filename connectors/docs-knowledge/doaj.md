---
description: "DOAJ indexes peer-reviewed open access journals. Search and get journals and articles."
hidden: true
---

# DOAJ (Directory of Open Access Journals)

<img src="../../.gitbook/assets/connectors/lg/doaj.png" alt="DOAJ (Directory of Open Access Journals) logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [doaj.org](https://doaj.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `doaj` |

## Setup

DOAJ (Directory of Open Access Journals) needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add DOAJ (Directory of Open Access Journals) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.doaj.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Article</td><td><code>getArticle</code></td><td>Get one article's DOAJ record by its DOAJ id Docs: https://doaj.org/api/v4/docs</td></tr><tr><td>Get Journal</td><td><code>getJournal</code></td><td>Get one journal's DOAJ record by its DOAJ id Docs: https://doaj.org/api/v4/docs</td></tr><tr><td>Search Articles</td><td><code>searchArticles</code></td><td>Search DOAJ article metadata (title, abstract, authors, DOI, journal, keywords, links) with a query string, paging and sort Docs: https://doaj.org/api/v4/docs</td></tr><tr><td>Search Journals</td><td><code>searchJournals</code></td><td>Search DOAJ-indexed open access journals (title, ISSN, publisher, licence, APCs, subjects, editorial policy) with a query string, paging and sort Docs: https://doaj.org/api/v4/docs</td></tr></tbody></table>

## Events

DOAJ (Directory of Open Access Journals) has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
