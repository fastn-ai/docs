---
description: "Gamma Generate API — programmatically generate presentations, documents, webpages, and social posts from text or templates, manage themes/folders, and…"
hidden: true
---

# Gamma API

<img src="../../.gitbook/assets/connectors/gamma-api.jpg" alt="Gamma API logo" width="64">

Gamma Generate API — programmatically generate presentations, documents, webpages, and social posts from text or templates, manage themes/folders, and archive/delete gammas. Auth via X-API-KEY header.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [gamma.app](https://gamma.app) |
| **Authentication** | API key |
| **Slug** | `gammaApi` |

## Use it

Add Gamma API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gammaApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Gamma | `archiveGamma` | Archive a Gamma, removing it from the active workspace. Requires the gammaId returned by a completed generation. |
| Create Generation | `createGeneration` | Start an asynchronous generation from text. Gamma determines the layout from your input. Returns a generationId to poll with Get Generation. |
| Create Generation From Template | `createGenerationFromTemplate` | Adapt an existing Gamma as a template (Remix). Provide gammaId of the template and a prompt describing changes. Returns a generationId to poll. |
| Delete Gamma | `deleteGamma` | Permanently delete a Gamma. Requires workspace admin role. Requires the gammaId returned by a completed generation. |
| Get Generation | `getGeneration` | Poll a generation by id until status is completed or failed. Returns gammaUrl, exportUrl, gammaId and credits when completed. |
| List Folders | `listFolders` | List folders in the workspace. Use returned ids as folderIds in generation requests. Cursor-paginated. |
| List Themes | `listThemes` | List themes available in the workspace (standard + custom). Use returned ids as themeId in generation requests. Cursor-paginated. |
