---
description: "The Erskine May API gives open access to Erskine May, the authoritative guide to UK parliamentary practice: list parts and chapters, read sections and page…"
hidden: true
---

# Erskine May API

<img src="../../.gitbook/assets/connectors/erskine-may-api.png" alt="Erskine May API logo" width="64">

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

| Action | Slug | What it does |
| --- | --- | --- |
| Browse Index Terms | `browseIndexTerms` | Returns a list of index terms by start letter. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/IndexTerm/browse) |
| Get Adjacent Section | `getSectionStep` | Get the overview of the section that is a number of steps before (negative) or after (positive) a given section, to page through the book (GET /api/Section/{sectionId},{step}). Docs: https://erskinemay-api.parliament.uk/index.html |
| Get Chapter | `getChapter` | Returns a single chapter overview by chapter number. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Chapter/{chapterNumber}) |
| Get Index Term | `getIndexTerm` | Returns an index term by id. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/IndexTerm/{indexTermId}) |
| Get Part | `getPart` | Returns a part by part number. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Part/{partNumber}) |
| Get Section | `getSection` | Returns a section by section id. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Section/{sectionId}) |
| Get Section by Paragraph Reference | `getSectionByParagraphReference` | Returns a section overview by reference. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Search/Paragraph/{reference}) |
| List Parts | `listParts` | Returns a list of all parts. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Part) |
| Search Index Terms | `searchIndexTerms` | Returns a list of index terms which contain the search term. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Search/IndexTermSearchResults/{searchTerm}) |
| Search Paragraphs | `searchParagraphs` | Returns a list of paragraphs which contain the search term. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Search/ParagraphSearchResults/{searchTerm}) |

<details>

<summary>See 1 more action</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Search Sections | `searchSections` | Returns a list of sections which contain the search term. Docs: https://erskinemay-api.parliament.uk/index.html (OpenAPI /swagger/v1/swagger.json) (GET /api/Search/SectionSearchResults/{searchTerm}) |

</details>
