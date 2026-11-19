---
description: "Connect Crossref to your product with fastn."
hidden: true
---

# Crossref

<img src="../../.gitbook/assets/connectors/lg/crossref.png" alt="Crossref logo">

Crossref REST API: free, keyless access to metadata for 150M+ scholarly works registered with DOIs - search and filter works, look up a DOI, and browse members (publishers), funders, journals, DOI prefixes, work types and licenses. Add a mailto address to use the faster 'polite' pool.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [crossref.org](https://crossref.org) |
| **Authentication** | No authentication |
| **Slug** | `crossref` |

## Use it

Add Crossref from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.crossref.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Funder</td><td><code>getFunder</code></td><td>Returns a funder (and its sub-organizations) by its Funder Registry id. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Get Journal</td><td><code>getJournal</code></td><td>Returns a journal by ISSN: title, publisher, ISSNs, subjects, DOI counts and coverage. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Get Member</td><td><code>getMember</code></td><td>Returns a member's metadata: name, prefixes, location, deposit counts and coverage statistics. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Get Prefix</td><td><code>getPrefix</code></td><td>Returns the owner (member) of a DOI prefix. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Get Work</td><td><code>getWork</code></td><td>Returns the full metadata of one work by DOI (title, authors, dates, journal, references count, funders, licenses, links). Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Get Work Registration Agency</td><td><code>getWorkAgency</code></td><td>Returns the DOI registration agency (Crossref, DataCite, mEDRA...) of a DOI. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Get Work Type</td><td><code>getType</code></td><td>Returns one work type by id. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Funder Works</td><td><code>listFunderWorks</code></td><td>Searches and filters the works funded by a funder. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Funders</td><td><code>listFunders</code></td><td>Searches the Open Funder Registry; filter by location. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Journal Works</td><td><code>listJournalWorks</code></td><td>Searches and filters the works published in a journal. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Journals</td><td><code>listJournals</code></td><td>Searches journals by title. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Licenses</td><td><code>listLicenses</code></td><td>Returns the license URLs used by works, with work counts. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Member Works</td><td><code>listMemberWorks</code></td><td>Searches and filters the works deposited by a member. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Members</td><td><code>listMembers</code></td><td>Searches Crossref members (organisations that register content, mostly publishers). Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Prefix Works</td><td><code>listPrefixWorks</code></td><td>Searches and filters the works registered under a DOI prefix. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Work Types</td><td><code>listTypes</code></td><td>Returns the valid work types (journal-article, book-chapter, posted-content, dataset...). Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>List Works by Type</td><td><code>listTypeWorks</code></td><td>Searches and filters the works of one type. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr><tr><td>Search Works</td><td><code>listWorks</code></td><td>Searches and filters all registered works (journal articles, books, chapters, conference papers, datasets, preprints...), with field queries, filters, sorting, facets and paging. Docs: https://api.crossref.org/swagger-ui/index.html</td></tr></tbody></table>

</details>
