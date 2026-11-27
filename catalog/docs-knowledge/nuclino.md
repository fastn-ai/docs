---
description: "Nuclino is a team wiki for knowledge and projects. Manage workspaces, items, collections and fields."
hidden: true
---

# Nuclino

<img src="../../.gitbook/assets/connectors/lg/nuclino.png" alt="Nuclino logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [nuclino.com](https://nuclino.com) |
| **Authentication** | Access token |
| **Slug** | `nuclino` |

## Setup

Your customers enter their access token for Nuclino when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Nuclino from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Nuclino**.
2. Select **Connect** on the Nuclino card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Nuclino's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Collection</td><td><code>createCollection</code></td><td>Creates a new collection (folder). Provide either workspaceId (to create at the workspace root) or parentId (to nest inside another collection).</td></tr><tr><td>Create Field</td><td><code>createField</code></td><td>Creates a new custom field in a workspace. Field values are then set per item via Create/Update Item.</td></tr><tr><td>Create Item</td><td><code>createItem</code></td><td>Creates a new item (document/page). Provide either workspaceId (to create at the workspace root) or parentId (to create inside a collection). Content is Markdown.</td></tr><tr><td>Delete Field</td><td><code>deleteField</code></td><td>Deletes a custom field and removes its values from every item in the workspace.</td></tr><tr><td>Delete Item or Collection</td><td><code>deleteItem</code></td><td>Moves an item or collection to the workspace trash. Returns the deleted item's ID.</td></tr><tr><td>Get File</td><td><code>getFile</code></td><td>Retrieves file metadata and a temporary signed download URL (valid for 10 minutes).</td></tr><tr><td>Get Item or Collection</td><td><code>getItem</code></td><td>Retrieves a single item or collection by its ID, including full Markdown content.</td></tr><tr><td>Get Team</td><td><code>getTeam</code></td><td>Retrieves a single team by its ID.</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Retrieves a single user by their ID.</td></tr><tr><td>Get Workspace</td><td><code>getWorkspace</code></td><td>Retrieves a single workspace by its ID, including its custom fields and top-level child item IDs.</td></tr></tbody></table>

<details>

<summary>View 5 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Items and Collections</td><td><code>listItems</code></td><td>Lists items (documents/pages) and collections (folders). Filter by either a team or a workspace (mutually exclusive). Content is not included in list results; use Get Item for full content.</td></tr><tr><td>List Teams</td><td><code>listTeams</code></td><td>Lists all teams the API key has access to. Supports cursor pagination via the 'after' parameter.</td></tr><tr><td>List Workspaces</td><td><code>listWorkspaces</code></td><td>Lists workspaces, optionally filtered by team. Supports cursor pagination via 'after'.</td></tr><tr><td>Update Field</td><td><code>updateField</code></td><td>Updates a custom field definition. Destructive type changes may delete existing values across all items.</td></tr><tr><td>Update Item or Collection</td><td><code>updateItem</code></td><td>Updates an existing item or collection. Provide at least one of title, content, or fields. Set a value to null to clear it.</td></tr></tbody></table>

</details>

