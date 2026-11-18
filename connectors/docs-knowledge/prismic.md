---
description: "Prismic headless CMS connector."
hidden: true
---

# Prismic

<img src="../../.gitbook/assets/connectors/prismic.png" alt="Prismic logo" width="64">

Prismic headless CMS connector. Manages custom types and shared slices (Custom Types API), creates and updates documents (Migration API), manages media library assets (Asset API), and reads published content and repository refs (Content API v2).

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [prismic.io](https://prismic.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `prismic` |

## Use it

Add Prismic from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.prismic.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Custom Type | `createCustomType` | Create a new custom type (page type) in the Prismic repository. Returns 201 on success, 409 if the ID already exists. |
| Create Document | `createDocument` | Create a new document (page) in the Prismic repository via the Migration API. The page is created as a draft in the Migration Release. Returns the created document with its id. |
| Create Shared Slice | `createSlice` | Create a new shared slice in the Prismic repository. Returns 201 on success, 409 if the ID already exists. |
| Delete Asset | `deleteAsset` | Delete an asset from the Prismic media library via the Asset API. Deleting assets used on published pages will break those files. |
| Delete Custom Type | `deleteCustomType` | Delete a custom type by its API ID from the Prismic repository. Returns 204 on success. |
| Delete Shared Slice | `deleteSlice` | Delete a shared slice by its API ID from the Prismic repository. Returns 204 on success. |
| Get Custom Type | `getCustomType` | Retrieve a single custom type by its API ID from the Prismic Custom Types API. |
| Get Repository | `getRepository` | Get the Prismic repository metadata from the Content API v2: available refs (master and releases), document types, languages, tags and query forms. |
| Get Shared Slice | `getSlice` | Retrieve a single shared slice by its API ID from the Prismic Custom Types API. |
| List Assets | `listAssets` | List assets from the Prismic media library via the Asset API, with optional filtering and pagination. |

<details>

<summary>See 9 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Custom Types | `listCustomTypes` | List all custom types (page types) in the Prismic repository via the Custom Types API. |
| List Shared Slices | `listSlices` | List all shared slices in the Prismic repository via the Custom Types API. |
| List Tags | `listTags` | List all tags used across documents in the Prismic repository via the Content API. |
| Search Documents | `searchDocuments` | Query published documents from the Prismic Content API v2. Requires a ref (from Get Repository). Use q predicates to filter, e.g. [[at(document.type,"page")]]. |
| Update Asset | `updateAsset` | Update the metadata (notes, credits, alt) of an existing asset in the Prismic media library via the Asset API. |
| Update Custom Type | `updateCustomType` | Update an existing custom type model in the Prismic repository. Returns 204 on success, 422 if the ID does not exist. |
| Update Document | `updateDocument` | Update an existing document (page) in the Prismic repository via the Migration API. type, lang and alternate_language_id cannot be modified. Omitting tags deletes existing tags. |
| Update Shared Slice | `updateSlice` | Update an existing shared slice in the Prismic repository. Returns 204 on success, 422 if the ID does not exist. |
| Upload Asset | `uploadAsset` | Upload a new asset to the Prismic media library via the Asset API. Sends the file as multipart/form-data with optional metadata. Requires a file reference input. |

</details>
