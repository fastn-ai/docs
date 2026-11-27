---
description: "Gamma creates presentations, documents and web pages with AI. Generate content from text or templates, and list folders and themes."
hidden: true
---

# Gamma API

<img src="../../.gitbook/assets/connectors/lg/gamma-api.png" alt="Gamma API logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [gamma.app](https://gamma.app) |
| **Authentication** | API key |
| **Slug** | `gammaApi` |

## Setup

Your customers enter their API key for Gamma API when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Gamma API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Gamma API**.
2. Select **Connect** on the Gamma API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Gamma API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Archive Gamma</td><td><code>archiveGamma</code></td><td>Archive a Gamma, removing it from the active workspace. Requires the gammaId returned by a completed generation.</td></tr><tr><td>Create Generation</td><td><code>createGeneration</code></td><td>Start an asynchronous generation from text. Gamma determines the layout from your input. Returns a generationId to poll with Get Generation.</td></tr><tr><td>Create Generation From Template</td><td><code>createGenerationFromTemplate</code></td><td>Adapt an existing Gamma as a template (Remix). Provide gammaId of the template and a prompt describing changes. Returns a generationId to poll.</td></tr><tr><td>Delete Gamma</td><td><code>deleteGamma</code></td><td>Permanently delete a Gamma. Requires workspace admin role. Requires the gammaId returned by a completed generation.</td></tr><tr><td>Get Generation</td><td><code>getGeneration</code></td><td>Poll a generation by id until status is completed or failed. Returns gammaUrl, exportUrl, gammaId and credits when completed.</td></tr><tr><td>List Folders</td><td><code>listFolders</code></td><td>List folders in the workspace. Use returned ids as folderIds in generation requests. Cursor-paginated.</td></tr><tr><td>List Themes</td><td><code>listThemes</code></td><td>List themes available in the workspace (standard + custom). Use returned ids as themeId in generation requests. Cursor-paginated.</td></tr></tbody></table>

