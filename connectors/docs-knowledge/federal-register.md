---
description: "The Federal Register API (U.S."
hidden: true
---

# Federal Register

<img src="../../.gitbook/assets/connectors/lg/federal-register.png" alt="Federal Register logo">

The Federal Register API (U.S. Office of the Federal Register) gives free access to every Federal Register document published since 1994 and to documents on public inspection: search with rich filters, get documents and facet counts, issue tables of contents, agencies, images and suggested searches. No API key needed.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [federalregister.gov](https://federalregister.gov) |
| **Authentication** | No authentication |
| **Slug** | `federalRegister` |

## Use it

Add Federal Register from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.federalRegister.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Agency | `getAgency` | Fetch a particular agency's details. (GET /agencies/{slug}). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| Get Document | `getDocument` | Fetch a single Federal Register document. (GET /documents/{document_number}.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| Get Document Facet Counts | `getDocumentFacets` | Fetch counts of matching Federal Register Documents grouped by a facet. (GET /documents/facets/{facet}). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| Get Image Variants | `getImageVariants` | Fetch the available image variants and their metadata for a single image identifier. (GET /images/{identifier}). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| Get Issue Table of Contents | `getIssueTableOfContents` | Fetch document table of contents based on the print edition. (GET /issues/{publication_date}.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| Get Multiple Documents | `getDocuments` | Fetch multiple Federal Register documents. (GET /documents/{document_numbers}.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| Get Multiple Public Inspection Documents | `getPublicInspectionDocuments` | Fetch multiple public inspection documents. (GET /public-inspection-documents/{document_numbers}.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| Get Public Inspection Document | `getPublicInspectionDocument` | Fetch a single public inspection document. (GET /public-inspection-documents/{document_number}.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| Get Suggested Search | `getSuggestedSearch` | Fetch a particular suggested search. (GET /suggested_searches/{slug}). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| List Agencies | `listAgencies` | Fetch all agency details. (GET /agencies). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| List Current Public Inspection Documents | `listCurrentPublicInspectionDocuments` | Fetch all the public inspection documents that are currently on public inspection. (GET /public-inspection-documents/current.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| List Suggested Searches | `listSuggestedSearches` | Fetch all suggested searches or limit by FederalRegister.gov section. (GET /suggested_searches). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| Search Documents | `searchDocuments` | Search all Federal Register documents published since 1994. (GET /documents.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
| Search Public Inspection Documents | `searchPublicInspectionDocuments` | Search all the public inspection documents that are currently on public inspection; use the document search to find documents that have been published. (GET /public-inspection-documents.{format}). Docs: https://www.federalregister.gov/developers/documentation/api/v1 |
