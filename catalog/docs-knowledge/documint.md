---
description: "Documint turns data into PDFs from designed templates. Create documents and manage templates, folders and assets."
hidden: true
---

# Documint

<img src="../../.gitbook/assets/connectors/lg/documint.png" alt="Documint logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [documint.me](https://documint.me) |
| **Authentication** | API key |
| **Slug** | `documint` |

## Setup

Your customers enter their API key for Documint when they connect. Nothing else needs setting up.

## Use it

Add Documint from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.documint.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Document</td><td><code>createDocument</code></td><td>Merges your data into a Documint template and renders a document, returning a signed download URL for the generated PDF. Shape the merge data to the template's own field schema, which Get Template returns as fieldSchema. Set Preview to true to render a non-billable test document (the response comes back with isTest true and isLive false); leave it off to produce a live document.</td></tr><tr><td>Create Template</td><td><code>createTemplate</code></td><td>Creates a new, empty Documint template and returns it with its id. The template body and stylesheet cannot be supplied through the API - Documint refuses editor fields for API keys - so design the layout afterwards in the Documint template editor.</td></tr><tr><td>Delete Asset</td><td><code>deleteAsset</code></td><td>Permanently deletes an uploaded Documint asset. Templates that reference the asset will lose the image.</td></tr><tr><td>Delete Folder</td><td><code>deleteFolder</code></td><td>Permanently deletes a Documint template folder.</td></tr><tr><td>Delete Template</td><td><code>deleteTemplate</code></td><td>Permanently deletes a Documint template. This cannot be undone - to move a template to the trash reversibly instead, set Is Trashed on Update Template.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Returns the Documint account the API key belongs to, including the company profile and postal address shown on generated documents.</td></tr><tr><td>Get Asset</td><td><code>getAsset</code></td><td>Retrieves a single uploaded Documint asset by its id, including the URL a template can reference.</td></tr><tr><td>Get Document</td><td><code>getDocument</code></td><td>Retrieves a single rendered Documint document by its id, including a freshly signed download URL for the file. Documint ignores the select parameter on this endpoint and always returns the full record, so no field picker is offered here.</td></tr><tr><td>Get Folder</td><td><code>getFolder</code></td><td>Retrieves a single Documint template folder by its id.</td></tr><tr><td>Get Subscription</td><td><code>getSubscription</code></td><td>Returns the Documint plan and billing state for the account - plan name, billing period, trial status and the current billing period end - so a workflow can check entitlement before rendering documents.</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Template</td><td><code>getTemplate</code></td><td>Retrieves a single Documint template by its id, including its HTML, CSS, page options, field schema, test data and editor component tree.</td></tr><tr><td>List Assets</td><td><code>listAssets</code></td><td>Lists the images and other files uploaded to the Documint account for use inside templates.</td></tr><tr><td>List Documents</td><td><code>listDocuments</code></td><td>Lists the documents Documint has rendered for the account, newest first by default. Optionally filter by the template they came from, by live or test renders, or by expiry, and choose which fields come back.</td></tr><tr><td>List Folders</td><td><code>listFolders</code></td><td>Lists the folders used to organise templates in the Documint account, with pagination metadata.</td></tr><tr><td>List Templates</td><td><code>listTemplates</code></td><td>Lists the document templates in the Documint account, with pagination metadata. Optionally filter by exact name, folder, type, trashed state or debug state, choose which fields come back and sort the results.</td></tr><tr><td>Update Account</td><td><code>updateAccount</code></td><td>Updates the Documint account's company profile and postal address. Supply the whole company object - Documint replaces it with what you send.</td></tr><tr><td>Update Folder</td><td><code>updateFolder</code></td><td>Renames a Documint template folder. Returns the updated folder.</td></tr><tr><td>Update Template</td><td><code>updateTemplate</code></td><td>Updates a Documint template's metadata - name, folder, page options, header and footer HTML, test data, debug mode and trashed state. Only the fields you supply change. Documint rejects the editor-managed fields html and css for API keys with HTTP 403, and it silently ignores isActive, isStarred and tags for API keys, so none of those are exposed here.</td></tr></tbody></table>

</details>

## Events

Documint has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
