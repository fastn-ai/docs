---
description: "Nuclino is a unified workspace for team knowledge, docs, and projects."
hidden: true
---

# Nuclino

<img src="../../.gitbook/assets/connectors/lg/nuclino.png" alt="Nuclino logo">

Nuclino is a unified workspace for team knowledge, docs, and projects. This connector wraps the Nuclino REST API v0 to manage teams, workspaces, items and collections (pages/notes), custom fields, files, and users.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [nuclino.com](https://nuclino.com) |
| **Authentication** | Bearer token |
| **Slug** | `nuclino` |

## Use it

Add Nuclino from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nuclino.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Collection | `createCollection` | Creates a new collection (folder). Provide either workspaceId (to create at the workspace root) or parentId (to nest inside another collection). |
| Create Field | `createField` | Creates a new custom field in a workspace. Field values are then set per item via Create/Update Item. |
| Create Item | `createItem` | Creates a new item (document/page). Provide either workspaceId (to create at the workspace root) or parentId (to create inside a collection). Content is Markdown. |
| Delete Field | `deleteField` | Deletes a custom field and removes its values from every item in the workspace. |
| Delete Item or Collection | `deleteItem` | Moves an item or collection to the workspace trash. Returns the deleted item's ID. |
| Get File | `getFile` | Retrieves file metadata and a temporary signed download URL (valid for 10 minutes). |
| Get Item or Collection | `getItem` | Retrieves a single item or collection by its ID, including full Markdown content. |
| Get Team | `getTeam` | Retrieves a single team by its ID. |
| Get User | `getUser` | Retrieves a single user by their ID. |
| Get Workspace | `getWorkspace` | Retrieves a single workspace by its ID, including its custom fields and top-level child item IDs. |

<details>

<summary>See 5 more actions</summary>

* **List Items and Collections** `listItems`: Lists items (documents/pages) and collections (folders). Filter by either a team or a workspace (mutually exclusive). Content is not included in list results; use Get Item for full content.
* **List Teams** `listTeams`: Lists all teams the API key has access to. Supports cursor pagination via the 'after' parameter.
* **List Workspaces** `listWorkspaces`: Lists workspaces, optionally filtered by team. Supports cursor pagination via 'after'.
* **Update Field** `updateField`: Updates a custom field definition. Destructive type changes may delete existing values across all items.
* **Update Item or Collection** `updateItem`: Updates an existing item or collection. Provide at least one of title, content, or fields. Set a value to null to clear it.

</details>
