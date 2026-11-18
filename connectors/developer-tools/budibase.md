---
description: "Budibase low-code platform public API (v1)."
hidden: true
---

# Budibase

<img src="../../.gitbook/assets/connectors/budibase.jpg" alt="Budibase logo" width="64">

Budibase low-code platform public API (v1). Covers workspaces and applications including publish, unpublish, import and export, tables and their schemas, rows with create, update, delete, retrieve and search, views and view row search, data-source queries, users, role assignment and unassignment, and tenant metrics. Authenticates with a Budibase user API key sent in the x-budibase-api-key header; app-scoped calls also take the target app or workspace ID in the x-budibase-app-id header.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [budibase.com](https://budibase.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `budibase` |

## Use it

Add Budibase from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.budibase.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Assign Role | `assignRole` | Assign a role to a list of users. Grant a per-app role, global builder access or global admin access. Budibase Cloud rejects this endpoint with "Unable to assign roles - license required" unless the account holds a licence that includes role management. |
| Create Application | `createApplication` | Create an application. Budibase marks this endpoint deprecated in favour of the equivalent workspace endpoint; it still works on current Budibase versions. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Create Row | `createRow` | Create a row. Creates a row within the specified table. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Create Table | `createTable` | Create a table. Create a table, this could be internal or external. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Create User | `createUser` | Create a user. |
| Create View | `createView` | Create a view. Create a view, this can be against an internal or external table. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Create Workspace | `createWorkspace` | Create a workspace. |
| Delete Application | `deleteApplication` | Delete an application. Budibase marks this endpoint deprecated in favour of the equivalent workspace endpoint; it still works on current Budibase versions. Returns the deleted record on success. |
| Delete Row | `deleteRow` | Delete a row. Deletes a row within the specified table. Requires the target app or workspace ID, sent as the x-budibase-app-id header. Returns the deleted record on success. |
| Delete Table | `deleteTable` | Delete a table. Delete a table, this could be internal or external. Requires the target app or workspace ID, sent as the x-budibase-app-id header. Returns the deleted record on success. |

<details>

<summary>See 34 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete User | `deleteUser` | Delete a user. Returns the deleted record on success. |
| Delete View | `deleteView` | Delete a view. Delete a view, this can be against an internal or external table. Requires the target app or workspace ID, sent as the x-budibase-app-id header. Returns the deleted record on success. |
| Delete Workspace | `deleteWorkspace` | Delete a workspace. Returns the deleted record on success. |
| Execute Query | `executeQuery` | Execute a data-source query that has been defined in the Budibase builder, passing any bindings the query declares. Requires the target app or workspace ID, sent as the x-budibase-app-id header. Queries cannot be created through the public API, so the query must already exist in the workspace. |
| Export Application | `exportApplication` | Export an application. Budibase responds with a gzip tarball of the app database and object store, optionally encrypted with the supplied password, so the response is a binary archive rather than JSON. Budibase marks this endpoint deprecated in favour of the equivalent workspace endpoint; it still works on current Budibase versions. |
| Export Workspace | `exportWorkspace` | Export a workspace. Budibase responds with a gzip tarball of the workspace database and object store, optionally encrypted with the supplied password, so the response is a binary archive rather than JSON. |
| Get Application | `getApplication` | Retrieve an application. Budibase marks this endpoint deprecated in favour of the equivalent workspace endpoint; it still works on current Budibase versions. |
| Get Row | `getRow` | Retrieve a row. This gets a single row, it will be enriched with the full related rows, rather than the squashed "primaryDisplay" format returned by the search endpoint. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Get Table | `getTable` | Retrieve a table. Lookup a table, this could be internal or external. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Get Tenant Metrics | `getTenantMetrics` | Retrieve Budibase tenant metrics. The endpoint responds with Prometheus exposition text rather than JSON, so the whole response body is the metrics document and it carries no JSON keys. |
| Get User | `getUser` | Retrieve a user. |
| Get View | `getView` | Retrieve a view. Lookup a view, this could be internal or external. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Get Workspace | `getWorkspace` | Retrieve a workspace. |
| Import Application | `importApplication` | Import a previously exported archive into an existing application. Budibase accepts this body only as multipart/form-data carrying the export file, so the archive must be uploaded as a file; the request returns 204 with an empty body on success. Budibase marks this endpoint deprecated in favour of the equivalent workspace endpoint. |
| Import Workspace | `importWorkspace` | Import a previously exported archive into an existing workspace. Budibase accepts this body only as multipart/form-data carrying the export file, so the archive must be uploaded as a file; the request returns 204 with an empty body on success. |
| Publish Application | `publishApplication` | Publish an application. Budibase marks this endpoint deprecated in favour of the equivalent workspace endpoint; it still works on current Budibase versions. |
| Publish Workspace | `publishWorkspace` | Publish a workspace. |
| Search Applications | `searchApplications` | Search for applications. Based on application properties (currently only name) search for applications. Budibase marks this endpoint deprecated in favour of the equivalent workspace endpoint; it still works on current Budibase versions. |
| Search Queries | `searchQueries` | Search for queries. Based on query properties (currently only name) search for queries. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Search Rows | `searchRows` | Search for rows. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Search Tables | `searchTables` | Search for tables. Based on table properties (currently only name) search for tables. This could be an internal or an external table. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Search Users | `searchUsers` | Search for users. Based on user properties (currently only name) search for users. |
| Search View Rows | `searchViewRows` | Search for rows in a view. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Search Views | `searchViews` | Search for views. Based on view properties (currently only name) search for views. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Search Workspaces | `searchWorkspaces` | Search for workspaces. Based on workspace properties (currently only name) search for workspaces. |
| Unassign Role | `unassignRole` | Un-assign a role from a list of users. Removes a per-app role, global builder access or global admin access. Budibase Cloud rejects this endpoint with "Unable to un-assign roles - license required" unless the account holds a licence that includes role management. |
| Unpublish Application | `unpublishApplication` | Unpublish an application. Budibase marks this endpoint deprecated in favour of the equivalent workspace endpoint; it still works on current Budibase versions. |
| Unpublish Workspace | `unpublishWorkspace` | Unpublish a workspace. |
| Update Application | `updateApplication` | Update an application. Budibase marks this endpoint deprecated in favour of the equivalent workspace endpoint; it still works on current Budibase versions. |
| Update Row | `updateRow` | Update a row. Updates a row within the specified table. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Update Table | `updateTable` | Update a table. Update a table, this could be internal or external. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Update User | `updateUser` | Update a user. |
| Update View | `updateView` | Update a view. Update a view, this can be against an internal or external table. Requires the target app or workspace ID, sent as the x-budibase-app-id header. |
| Update Workspace | `updateWorkspace` | Update a workspace. |

</details>
