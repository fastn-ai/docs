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

## Connect in Fastn

Your customers connect DOAJ (Directory of Open Access Journals) from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **DOAJ (Directory of Open Access Journals)**.
2. Select **Connect** on the DOAJ (Directory of Open Access Journals) card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. DOAJ (Directory of Open Access Journals) needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use DOAJ (Directory of Open Access Journals)'s actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Article</td><td><code>getArticle</code></td><td>Get one article's DOAJ record by its DOAJ id Docs: https://doaj.org/api/v4/docs</td></tr><tr><td>Get Journal</td><td><code>getJournal</code></td><td>Get one journal's DOAJ record by its DOAJ id Docs: https://doaj.org/api/v4/docs</td></tr><tr><td>Search Articles</td><td><code>searchArticles</code></td><td>Search DOAJ article metadata (title, abstract, authors, DOI, journal, keywords, links) with a query string, paging and sort Docs: https://doaj.org/api/v4/docs</td></tr><tr><td>Search Journals</td><td><code>searchJournals</code></td><td>Search DOAJ-indexed open access journals (title, ISSN, publisher, licence, APCs, subjects, editorial policy) with a query string, paging and sort Docs: https://doaj.org/api/v4/docs</td></tr></tbody></table>

