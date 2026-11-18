---
description: "The Erskine May API gives open access to Erskine May, the authoritative guide to UK parliamentary practice: list parts and chapters, read sections and page…"
hidden: true
---

# Erskine May API

<img src="../../.gitbook/assets/connectors/lg/erskine-may-api.png" alt="Erskine May API logo">

The Erskine May API gives open access to Erskine May, the authoritative guide to UK parliamentary practice: list parts and chapters, read sections and page between them, look up a paragraph reference, browse and search the index, and full-text search paragraphs and sections. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [parliament.uk](https://parliament.uk) |
| **Authentication** | No authentication |
| **Slug** | `erskineMayApi` |

## Use it

Add Erskine May API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.erskineMayApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Browse Index Terms</td><td><code>browseIndexTerms</code></td><td>Returns a list of index terms by start letter. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/IndexTerm/browse)</td></tr><tr><td>Get Adjacent Section</td><td><code>getSectionStep</code></td><td>Get the overview of the section that is a number of steps before (negative) or after (positive) a given section, to page through the book (GET /api/Section/{sectionId},{step}). Docs: https://erskinemay-api.parliament.uk/index.html</td></tr><tr><td>Get Chapter</td><td><code>getChapter</code></td><td>Returns a single chapter overview by chapter number. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Chapter/{chapterNumber})</td></tr><tr><td>Get Index Term</td><td><code>getIndexTerm</code></td><td>Returns an index term by id. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/IndexTerm/{indexTermId})</td></tr><tr><td>Get Part</td><td><code>getPart</code></td><td>Returns a part by part number. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Part/{partNumber})</td></tr><tr><td>Get Section</td><td><code>getSection</code></td><td>Returns a section by section id. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Section/{sectionId})</td></tr><tr><td>Get Section by Paragraph Reference</td><td><code>getSectionByParagraphReference</code></td><td>Returns a section overview by reference. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Search/Paragraph/{reference})</td></tr><tr><td>List Parts</td><td><code>listParts</code></td><td>Returns a list of all parts. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Part)</td></tr><tr><td>Search Index Terms</td><td><code>searchIndexTerms</code></td><td>Returns a list of index terms which contain the search term. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Search/IndexTermSearchResults/{searchTerm})</td></tr><tr><td>Search Paragraphs</td><td><code>searchParagraphs</code></td><td>Returns a list of paragraphs which contain the search term. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Search/ParagraphSearchResults/{searchTerm})</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Sections</td><td><code>searchSections</code></td><td>Returns a list of sections which contain the search term. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Search/SectionSearchResults/{searchTerm})</td></tr></tbody></table>

</details>
