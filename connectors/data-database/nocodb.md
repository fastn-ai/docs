---
description: "NocoDB is an open-source no-code database and Airtable alternative."
hidden: true
---

# NocoDB

<img src="../../.gitbook/assets/connectors/lg/nocodb.png" alt="NocoDB logo">

NocoDB is an open-source no-code database and Airtable alternative. Manage workspaces, bases, tables, columns, views, records, links, filters, sorts, shared views, comments, and webhooks via the NocoDB v2 REST API.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Authentication** | Credentials you enter |
| **Slug** | `nocodb` |

## Use it

Add NocoDB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nocodb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Base User | `addBaseUser` | Invite a user to a base by email with a specific role. |
| Add Column To View | `createViewColumn` | Add a table column to a view. |
| Add Comment | `addComment` | Add a comment to a record. |
| Count Comments | `countComments` | Count the comments on one or more records. |
| Count Table Records | `countRecords` | Count the number of records in a table, optionally filtered. |
| Create Base | `createBase` | Create a new base (project) inside a workspace. |
| Create Base API Token | `createBaseApiToken` | Create a new API token scoped to a base. |
| Create Column | `createColumn` | Add a new column (field) to a table. |
| Create Form View | `createFormView` | Create a form view on a table for data entry. |
| Create Gallery View | `createGalleryView` | Create a gallery view on a table. |
| Create Grid View | `createGridView` | Create a grid (spreadsheet) view on a table. |
| Create Kanban View | `createKanbanView` | Create a kanban view on a table, grouped by a single-select column. |
| Create Shared Base | `createSharedBase` | Enable public sharing of a base and return its shared link UUID. |
| Create Shared View | `createSharedView` | Enable public sharing of a view and return its shared UUID. |
| Create Table | `createTable` | Create a new table in a base with an initial set of columns. |
| Create Table Records | `createRecords` | Create one or more records in a table. Pass a single JSON object for one record or a JSON array of objects for bulk insert. |
| Create Table Webhook | `createTableHook` | Create a webhook on a table that fires on record events and calls a URL. |
| Create View Filter | `createViewFilter` | Add a filter condition to a view. |
| Create View Sort | `createViewSort` | Add a sort rule to a view. |
| Create Webhook Filter | `createHookFilter` | Add a filter condition that gates when a webhook fires. |
| Create Workspace | `createWorkspace` | Create a new workspace (NocoDB Cloud). |
| Delete Base | `deleteBase` | Permanently delete a base and all of its tables and data. |
| Delete Base API Token | `deleteBaseApiToken` | Revoke an API token from a base. |
| Delete Column | `deleteColumn` | Permanently delete a column from a table. |
| Delete Comment | `deleteComment` | Delete a comment from a record. |
| Delete Filter | `deleteFilter` | Delete a filter from a view. |
| Delete Shared Base | `deleteSharedBase` | Disable public sharing for a base. |
| Delete Shared View | `deleteSharedView` | Disable public sharing for a view. |
| Delete Sort | `deleteSort` | Delete a sort rule from a view. |
| Delete Table | `deleteTable` | Permanently delete a table and all of its records. |
| Delete Table Records | `deleteRecords` | Delete one or more records. Pass a JSON object or array of objects; each must include the primary key field (e.g. Id). |
| Delete Table Webhook | `deleteTableHook` | Delete a webhook from a table. |
| Delete View | `deleteView` | Delete a view from a table. |
| Delete Workspace | `deleteWorkspace` | Permanently delete a workspace and all of its bases (NocoDB Cloud). |
| Duplicate Base | `duplicateBase` | Duplicate a base, optionally excluding its data, views, or hooks. Runs asynchronously and returns a job. |
| Duplicate Table | `duplicateTable` | Duplicate a table within a base, optionally excluding data, views, or hooks. Runs asynchronously. |
| Get App Info | `getAppInfo` | Retrieve NocoDB instance/application information and feature flags. |
| Get Base | `getBase` | Retrieve a base's schema and metadata by ID. |
| Get Base Info | `getBaseInfo` | Retrieve extended information about a base. |
| Get Column | `getColumn` | Retrieve a single column's metadata by ID. |
| Get Current User | `getUserInfo` | Get information about the authenticated user. |
| Get Filter | `getFilter` | Retrieve a single filter's configuration. |
| Get Form View | `getFormView` | Retrieve a form view's configuration. |
| Get Gallery View | `getGalleryView` | Retrieve a gallery view's configuration. |
| Get Kanban View | `getKanbanView` | Retrieve a kanban view's configuration. |
| Get Sample Webhook Payload | `getSampleHookPayload` | Retrieve a sample webhook payload for an event/operation combination. |
| Get Shared Base | `getSharedBase` | Get the shared-base link configuration for a base. |
| Get Sort | `getSort` | Retrieve a single sort rule's configuration. |
| Get Source | `getSource` | Retrieve the schema and configuration of a single data source. |
| Get Table | `getTable` | Retrieve a table's metadata and columns by ID. |
| Get Workspace | `getWorkspace` | Retrieve a single workspace by its ID (NocoDB Cloud). |
| Hide All Columns In View | `hideAllColumnsInView` | Hide every column in a view. |
| Invite Workspace User | `inviteWorkspaceUser` | Invite a user to a workspace by email with a given role (NocoDB Cloud). |
| Link Records | `linkRecords` | Link one or more records to a record through a link field. Pass a JSON object or array identifying the records by primary key. |
| List Base API Tokens | `listBaseApiTokens` | List the API tokens created within a base. |
| List Base Users | `listBaseUsers` | List all users who have access to a base. |
| List Bases | `listBases` | List all bases within a workspace (NocoDB Cloud). |
| List Comments | `listComments` | List comments on a record. |
| List Filter Group Children | `getFilterGroupChildren` | List the child filters of a filter group. |
| List Grid View Columns | `listGridViewColumns` | List the columns of a grid view including width settings. |
| List Linked Records | `listLinkedRecords` | List records linked to a given record through a link field. |
| List Shared Views | `listSharedViews` | List the shared (public) views for a table. |
| List Sources | `listSources` | List the data sources connected to a base. |
| List Table Records | `listRecords` | List records in a table with optional field selection, filtering, sorting, and pagination. |
| List Table Webhooks | `listTableHooks` | List all webhooks (hooks) configured on a table. |
| List Tables | `listTables` | List all tables within a base. |
| List View Columns | `listViewColumns` | List the columns configured on a view with their visibility and order. |
| List View Filters | `listViewFilters` | List the filters applied to a view. |
| List View Sorts | `listViewSorts` | List the sort rules applied to a view. |
| List Views | `listViews` | List all views defined on a table. |
| List Webhook Filters | `listHookFilters` | List the filter conditions attached to a webhook. |
| List Webhook Logs | `listHookLogs` | List delivery logs for a webhook. |
| List Workspace Users | `listWorkspaceUsers` | List all members of a workspace (NocoDB Cloud). |
| List Workspaces | `listWorkspaces` | List all workspaces the authenticated NocoDB user can access (NocoDB Cloud). |
| Read Table Record | `getRecord` | Read a single record by its ID. |
| Remove Base User | `deleteBaseUser` | Revoke a user's access to a base. |
| Remove Workspace User | `deleteWorkspaceUser` | Remove a member from a workspace (NocoDB Cloud). |
| Reorder Table | `reorderTable` | Change a table's display order within its base. |
| Set Display Value Column | `setPrimaryColumn` | Set a column as the table's display (primary value) column. |
| Show All Columns In View | `showAllColumnsInView` | Make every column visible in a view. |
| Test Table Webhook | `testTableHook` | Send a test payload through a webhook configuration without saving it. |
| Unlink Records | `unlinkRecords` | Remove links between records through a link field. Pass a JSON object or array identifying the records by primary key. |
| Update Base | `updateBase` | Update a base's title, order, or metadata. |
| Update Base User | `updateBaseUser` | Change a base user's role. |
| Update Column | `updateColumn` | Update a column's title, type, or options. |
| Update Comment | `updateComment` | Edit an existing comment. |
| Update Filter | `updateFilter` | Update a filter's operator, value, or logic. |
| Update Form View | `updateFormView` | Update form-view settings such as heading, subheading, and success message. |
| Update Form View Column | `updateFormViewColumn` | Update a form-view field's label, help text, or requirement. |
| Update Gallery View | `updateGalleryView` | Update gallery-view settings such as the cover image column. |
| Update Grid View | `updateGridView` | Update grid-view-specific settings such as row height. |
| Update Grid View Column | `updateGridViewColumn` | Update a grid-view column's width or visibility. |
| Update Kanban View | `updateKanbanView` | Update kanban-view settings such as the grouping column or cover image. |
| Update Shared Base | `updateSharedBase` | Update the role granted by a base's shared link. |
| Update Shared View | `updateSharedView` | Update a shared view's password or metadata. |
| Update Sort | `updateSort` | Update a sort rule's column or direction. |
| Update Table | `updateTable` | Update a table's title or physical name. |
| Update Table Records | `updateRecords` | Update one or more records. Pass a JSON object or array of objects; each must include the primary key field (e.g. Id). |
| Update Table Webhook | `updateTableHook` | Update a table webhook. NocoDB replaces the whole hook, so title, event, operation, notification, and version must all be provided. |
| Update User Profile | `updateUserProfile` | Update the authenticated user's display name. |
| Update View | `updateView` | Update a view's title, lock type, ordering, or metadata. |
| Update View Column | `updateViewColumn` | Update a column's visibility or order within a view. |
| Update Workspace | `updateWorkspace` | Update a workspace's title or metadata (NocoDB Cloud). |
| Update Workspace User | `updateWorkspaceUser` | Change a workspace member's role (NocoDB Cloud). |
| Upload Attachment By URL | `uploadAttachmentByUrl` | Upload one or more attachments to NocoDB storage from public URLs. |
