---
description: "Prismic is a headless content management system. Manage custom types, shared slices, documents and media assets."
hidden: true
---

# Prismic

<img src="../../.gitbook/assets/connectors/lg/prismic.png" alt="Prismic logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [prismic.io](https://prismic.io) |
| **Authentication** | Repository name and access token |
| **Slug** | `prismic` |

## Setup

Your customers enter their repository name and access token for Prismic when they connect. Nothing else needs setting up.

## Use it

Add Prismic from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.prismic.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Custom Type</td><td><code>createCustomType</code></td><td>Create a new custom type (page type) in the Prismic repository.</td></tr><tr><td>Create Document</td><td><code>createDocument</code></td><td>Create a new document (page) in the Prismic repository via the Migration API. The page is created as a draft in the Migration Release. Returns the created document with its id.</td></tr><tr><td>Create Shared Slice</td><td><code>createSlice</code></td><td>Create a new shared slice in the Prismic repository.</td></tr><tr><td>Delete Asset</td><td><code>deleteAsset</code></td><td>Delete an asset from the Prismic media library via the Asset API. Deleting assets used on published pages will break those files.</td></tr><tr><td>Delete Custom Type</td><td><code>deleteCustomType</code></td><td>Delete a custom type by its API ID from the Prismic repository.</td></tr><tr><td>Delete Shared Slice</td><td><code>deleteSlice</code></td><td>Delete a shared slice by its API ID from the Prismic repository.</td></tr><tr><td>Get Custom Type</td><td><code>getCustomType</code></td><td>Retrieve a single custom type by its API ID from the Prismic Custom Types API.</td></tr><tr><td>Get Repository</td><td><code>getRepository</code></td><td>Get the Prismic repository metadata from the Content API v2: available refs (master and releases), document types, languages, tags and query forms.</td></tr><tr><td>Get Shared Slice</td><td><code>getSlice</code></td><td>Retrieve a single shared slice by its API ID from the Prismic Custom Types API.</td></tr><tr><td>List Assets</td><td><code>listAssets</code></td><td>List assets from the Prismic media library via the Asset API, with optional filtering and pagination.</td></tr></tbody></table>

<details>

<summary>View 9 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Custom Types</td><td><code>listCustomTypes</code></td><td>List all custom types (page types) in the Prismic repository via the Custom Types API.</td></tr><tr><td>List Shared Slices</td><td><code>listSlices</code></td><td>List all shared slices in the Prismic repository via the Custom Types API.</td></tr><tr><td>List Tags</td><td><code>listTags</code></td><td>List all tags used across documents in the Prismic repository via the Content API.</td></tr><tr><td>Search Documents</td><td><code>searchDocuments</code></td><td>Query published documents from the Prismic Content API v2. Requires a ref (from Get Repository). Use q predicates to filter, e.g. [[at(document.type,"page")]].</td></tr><tr><td>Update Asset</td><td><code>updateAsset</code></td><td>Update the metadata (notes, credits, alt) of an existing asset in the Prismic media library via the Asset API.</td></tr><tr><td>Update Custom Type</td><td><code>updateCustomType</code></td><td>Update an existing custom type model in the Prismic repository.</td></tr><tr><td>Update Document</td><td><code>updateDocument</code></td><td>Update an existing document (page) in the Prismic repository via the Migration API. type, lang and alternate_language_id cannot be modified. Omitting tags deletes existing tags.</td></tr><tr><td>Update Shared Slice</td><td><code>updateSlice</code></td><td>Update an existing shared slice in the Prismic repository.</td></tr><tr><td>Upload Asset</td><td><code>uploadAsset</code></td><td>Upload a new asset to the Prismic media library via the Asset API. Sends the file as multipart/form-data with optional metadata. Requires a file reference input.</td></tr></tbody></table>

</details>

## Events

Prismic has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
