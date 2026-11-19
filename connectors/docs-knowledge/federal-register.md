---
description: "The Federal Register publishes US government rules and notices. Search and get documents, agencies and public inspection items."
hidden: true
---

# Federal Register

<img src="../../.gitbook/assets/connectors/lg/federal-register.png" alt="Federal Register logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [federalregister.gov](https://federalregister.gov) |
| **Authentication** | No sign-in needed |
| **Slug** | `federalRegister` |

## Setup

Federal Register needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Federal Register from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.federalRegister.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Agency</td><td><code>getAgency</code></td><td>Fetch a particular agency's details. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Document</td><td><code>getDocument</code></td><td>Fetch a single Federal Register document. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Document Facet Counts</td><td><code>getDocumentFacets</code></td><td>Fetch counts of matching Federal Register Documents grouped by a facet. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Image Variants</td><td><code>getImageVariants</code></td><td>Fetch the available image variants and their metadata for a single image identifier. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Issue Table of Contents</td><td><code>getIssueTableOfContents</code></td><td>Fetch document table of contents based on the print edition. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Multiple Documents</td><td><code>getDocuments</code></td><td>Fetch multiple Federal Register documents. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Multiple Public Inspection Documents</td><td><code>getPublicInspectionDocuments</code></td><td>Fetch multiple public inspection documents. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Public Inspection Document</td><td><code>getPublicInspectionDocument</code></td><td>Fetch a single public inspection document. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Get Suggested Search</td><td><code>getSuggestedSearch</code></td><td>Fetch a particular suggested search. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>List Agencies</td><td><code>listAgencies</code></td><td>Fetch all agency details. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Current Public Inspection Documents</td><td><code>listCurrentPublicInspectionDocuments</code></td><td>Fetch all the public inspection documents that are currently on public inspection. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>List Suggested Searches</td><td><code>listSuggestedSearches</code></td><td>Fetch all suggested searches or limit by FederalRegister.gov section. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Search Documents</td><td><code>searchDocuments</code></td><td>Search all Federal Register documents published since 1994. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr><tr><td>Search Public Inspection Documents</td><td><code>searchPublicInspectionDocuments</code></td><td>Search all the public inspection documents that are currently on public inspection; use the document search to find documents that have been published. Docs: https://www.federalregister.gov/developers/documentation/api/v1</td></tr></tbody></table>

</details>

## Events

Federal Register has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
