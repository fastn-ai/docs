---
description: "Crossref holds metadata for scholarly works with DOIs. Look up and search works, journals, funders and members."
hidden: true
---

# Crossref

<img src="../../.gitbook/assets/connectors/lg/crossref.png" alt="Crossref logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [crossref.org](https://crossref.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `crossref` |

## Setup

Crossref needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Crossref from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Crossref**.
2. Select **Connect** on the Crossref card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Crossref needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Crossref's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Funder</td><td><code>getFunder</code></td><td>Returns a funder (and its sub-organizations) by its Funder Registry id. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Get Journal</td><td><code>getJournal</code></td><td>Returns a journal by ISSN: title, publisher, ISSNs, subjects, DOI counts and coverage. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Get Member</td><td><code>getMember</code></td><td>Returns a member's metadata: name, prefixes, location, deposit counts and coverage statistics. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Get Prefix</td><td><code>getPrefix</code></td><td>Returns the owner (member) of a DOI prefix. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Get Work</td><td><code>getWork</code></td><td>Returns the full metadata of one work by DOI (title, authors, dates, journal, references count, funders, licenses, links). Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Get Work Registration Agency</td><td><code>getWorkAgency</code></td><td>Returns the DOI registration agency (Crossref, DataCite, mEDRA...) of a DOI. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Get Work Type</td><td><code>getType</code></td><td>Returns one work type by id. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Funder Works</td><td><code>listFunderWorks</code></td><td>Searches and filters the works funded by a funder. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Funders</td><td><code>listFunders</code></td><td>Searches the Open Funder Registry; filter by location. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Journal Works</td><td><code>listJournalWorks</code></td><td>Searches and filters the works published in a journal. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Journals</td><td><code>listJournals</code></td><td>Searches journals by title. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Licenses</td><td><code>listLicenses</code></td><td>Returns the license URLs used by works, with work counts. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Member Works</td><td><code>listMemberWorks</code></td><td>Searches and filters the works deposited by a member. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Members</td><td><code>listMembers</code></td><td>Searches Crossref members (organisations that register content, mostly publishers). Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Prefix Works</td><td><code>listPrefixWorks</code></td><td>Searches and filters the works registered under a DOI prefix. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Work Types</td><td><code>listTypes</code></td><td>Returns the valid work types (journal-article, book-chapter, posted-content, dataset...). Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Works by Type</td><td><code>listTypeWorks</code></td><td>Searches and filters the works of one type. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Search Works</td><td><code>listWorks</code></td><td>Searches and filters all registered works (journal articles, books, chapters, conference papers, datasets, preprints...), with field queries, filters, sorting, facets and paging. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr></tbody></table>

</details>

