---
description: "Crossref REST API: free, keyless access to metadata for 150M+ scholarly works registered with DOIs - search and filter works, look up a DOI, and browse…"
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

| Action | Slug | What it does |
| --- | --- | --- |
| Get Funder | `getFunder` | Returns a funder (and its sub-organizations) by its Funder Registry id. Docs: https://api.crossref.org/swagger-ui/index.html |
| Get Journal | `getJournal` | Returns a journal by ISSN: title, publisher, ISSNs, subjects, DOI counts and coverage. Docs: https://api.crossref.org/swagger-ui/index.html |
| Get Member | `getMember` | Returns a member's metadata: name, prefixes, location, deposit counts and coverage statistics. Docs: https://api.crossref.org/swagger-ui/index.html |
| Get Prefix | `getPrefix` | Returns the owner (member) of a DOI prefix. Docs: https://api.crossref.org/swagger-ui/index.html |
| Get Work | `getWork` | Returns the full metadata of one work by DOI (title, authors, dates, journal, references count, funders, licenses, links). Docs: https://api.crossref.org/swagger-ui/index.html |
| Get Work Registration Agency | `getWorkAgency` | Returns the DOI registration agency (Crossref, DataCite, mEDRA...) of a DOI. Docs: https://api.crossref.org/swagger-ui/index.html |
| Get Work Type | `getType` | Returns one work type by id. Docs: https://api.crossref.org/swagger-ui/index.html |
| List Funder Works | `listFunderWorks` | Searches and filters the works funded by a funder. Docs: https://api.crossref.org/swagger-ui/index.html |
| List Funders | `listFunders` | Searches the Open Funder Registry; filter by location. Docs: https://api.crossref.org/swagger-ui/index.html |
| List Journal Works | `listJournalWorks` | Searches and filters the works published in a journal. Docs: https://api.crossref.org/swagger-ui/index.html |
| List Journals | `listJournals` | Searches journals by title. Docs: https://api.crossref.org/swagger-ui/index.html |
| List Licenses | `listLicenses` | Returns the license URLs used by works, with work counts. Docs: https://api.crossref.org/swagger-ui/index.html |
| List Member Works | `listMemberWorks` | Searches and filters the works deposited by a member. Docs: https://api.crossref.org/swagger-ui/index.html |
| List Members | `listMembers` | Searches Crossref members (organisations that register content, mostly publishers). Docs: https://api.crossref.org/swagger-ui/index.html |
| List Prefix Works | `listPrefixWorks` | Searches and filters the works registered under a DOI prefix. Docs: https://api.crossref.org/swagger-ui/index.html |
| List Work Types | `listTypes` | Returns the valid work types (journal-article, book-chapter, posted-content, dataset...). Docs: https://api.crossref.org/swagger-ui/index.html |
| List Works by Type | `listTypeWorks` | Searches and filters the works of one type. Docs: https://api.crossref.org/swagger-ui/index.html |
| Search Works | `listWorks` | Searches and filters all registered works (journal articles, books, chapters, conference papers, datasets, preprints...), with field queries, filters, sorting, facets and paging. Docs: https://api.crossref.org/swagger-ui/index.html |
