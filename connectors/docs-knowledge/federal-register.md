---
description: "The Federal Register API (U.S."
hidden: true
---

# Federal Register

<img src="../../.gitbook/assets/connectors/lg/federal-register.png" alt="Federal Register logo">

Office of the Federal Register) gives free access to every Federal Register document published since 1994 and to documents on public inspection: search with rich filters, get documents and facet counts, issue tables of contents, agencies, images and suggested searches. No API key needed.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [federalregister.gov](https://federalregister.gov) |
| **Authentication** | No authentication |
| **Slug** | `federalRegister` |

## Use it

Add Federal Register from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.federalRegister.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Agency</td><td><code>getAgency</code></td><td>Fetch a particular agency's details. (GET /agencies/{slug}). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Document</td><td><code>getDocument</code></td><td>Fetch a single Federal Register document. (GET /documents/{document_number}.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Document Facet Counts</td><td><code>getDocumentFacets</code></td><td>Fetch counts of matching Federal Register Documents grouped by a facet. (GET /documents/facets/{facet}). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Image Variants</td><td><code>getImageVariants</code></td><td>Fetch the available image variants and their metadata for a single image identifier. (GET /images/{identifier}). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Issue Table of Contents</td><td><code>getIssueTableOfContents</code></td><td>Fetch document table of contents based on the print edition. (GET /issues/{publication_date}.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Multiple Documents</td><td><code>getDocuments</code></td><td>Fetch multiple Federal Register documents. (GET /documents/{document_numbers}.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Multiple Public Inspection Documents</td><td><code>getPublicInspectionDocuments</code></td><td>Fetch multiple public inspection documents. (GET /public-inspection-documents/{document_numbers}.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Public Inspection Document</td><td><code>getPublicInspectionDocument</code></td><td>Fetch a single public inspection document. (GET /public-inspection-documents/{document_number}.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Suggested Search</td><td><code>getSuggestedSearch</code></td><td>Fetch a particular suggested search. (GET /suggested_searches/{slug}). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>List Agencies</td><td><code>listAgencies</code></td><td>Fetch all agency details. (GET /agencies). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Current Public Inspection Documents</td><td><code>listCurrentPublicInspectionDocuments</code></td><td>Fetch all the public inspection documents that are currently on public inspection. (GET /public-inspection-documents/current.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>List Suggested Searches</td><td><code>listSuggestedSearches</code></td><td>Fetch all suggested searches or limit by FederalRegister.gov section. (GET /suggested_searches). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Search Documents</td><td><code>searchDocuments</code></td><td>Search all Federal Register documents published since 1994. (GET /documents.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Search Public Inspection Documents</td><td><code>searchPublicInspectionDocuments</code></td><td>Search all the public inspection documents that are currently on public inspection; use the document search to find documents that have been published. (GET /public-inspection-documents.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr></tbody></table>

</details>
