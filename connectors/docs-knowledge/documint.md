---
description: "Documint turns structured data into pixel-perfect PDFs from templates you design in its drag-and-drop editor."
hidden: true
---

# Documint

<img src="../../.gitbook/assets/connectors/documint.png" alt="Documint logo" width="64">

Documint turns structured data into pixel-perfect PDFs from templates you design in its drag-and-drop editor. This connector covers the Documint public API: template management, merging data into a template to render a document, the rendered-document store, folders, uploaded assets, and the account and subscription records.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [documint.me](https://documint.me) |
| **Authentication** | Credentials you enter |
| **Slug** | `documint` |

## Use it

Add Documint from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.documint.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Document | `createDocument` | Merges your data into a Documint template and renders a document, returning a signed download URL for the generated PDF. Shape the merge data to the template's own field schema, which Get Template returns as fieldSchema. Set Preview to true to render a non-billable test document (the response comes back with isTest true and isLive false); leave it off to produce a live document. |
| Create Template | `createTemplate` | Creates a new, empty Documint template and returns it with its id. The template body and stylesheet cannot be supplied through the API - Documint refuses editor fields for API keys - so design the layout afterwards in the Documint template editor. |
| Delete Asset | `deleteAsset` | Permanently deletes an uploaded Documint asset. Templates that reference the asset will lose the image. |
| Delete Folder | `deleteFolder` | Permanently deletes a Documint template folder. |
| Delete Template | `deleteTemplate` | Permanently deletes a Documint template. This cannot be undone - to move a template to the trash reversibly instead, set Is Trashed on Update Template. |
| Get Account | `getAccount` | Returns the Documint account the API key belongs to, including the company profile and postal address shown on generated documents. |
| Get Asset | `getAsset` | Retrieves a single uploaded Documint asset by its id, including the URL a template can reference. |
| Get Document | `getDocument` | Retrieves a single rendered Documint document by its id, including a freshly signed download URL for the file. Documint ignores the select parameter on this endpoint and always returns the full record, so no field picker is offered here. |
| Get Folder | `getFolder` | Retrieves a single Documint template folder by its id. |
| Get Subscription | `getSubscription` | Returns the Documint plan and billing state for the account - plan name, billing period, trial status and the current billing period end - so a workflow can check entitlement before rendering documents. |

<details>

<summary>See 8 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Template | `getTemplate` | Retrieves a single Documint template by its id, including its HTML, CSS, page options, field schema, test data and editor component tree. |
| List Assets | `listAssets` | Lists the images and other files uploaded to the Documint account for use inside templates. |
| List Documents | `listDocuments` | Lists the documents Documint has rendered for the account, newest first by default. Optionally filter by the template they came from, by live or test renders, or by expiry, and choose which fields come back. |
| List Folders | `listFolders` | Lists the folders used to organise templates in the Documint account, with pagination metadata. |
| List Templates | `listTemplates` | Lists the document templates in the Documint account, with pagination metadata. Optionally filter by exact name, folder, type, trashed state or debug state, choose which fields come back and sort the results. |
| Update Account | `updateAccount` | Updates the Documint account's company profile and postal address. Supply the whole company object - Documint replaces it with what you send. |
| Update Folder | `updateFolder` | Renames a Documint template folder. Returns the updated folder. |
| Update Template | `updateTemplate` | Updates a Documint template's metadata - name, folder, page options, header and footer HTML, test data, debug mode and trashed state. Only the fields you supply change. Documint rejects the editor-managed fields html and css for API keys with HTTP 403, and it silently ignores isActive, isStarred and tags for API keys, so none of those are exposed here. |

</details>
