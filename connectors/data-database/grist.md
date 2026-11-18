---
description: "Grist is a modern relational spreadsheet."
hidden: true
---

# Grist

<img src="../../.gitbook/assets/connectors/lg/grist.png" alt="Grist logo">

Grist is a modern relational spreadsheet. Manage organizations, workspaces, documents, tables, columns, records, attachments, webhooks, and run SQL queries via the Grist REST API.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [getgrist.com](https://getgrist.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `grist` |

## Use it

Add Grist from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.grist.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add or Update Columns | `upsertColumns` | Add or update columns in a single call. Existing columns (matched by id) are updated; new ones are created. Use noadd/noupdate/replaceall to control behavior. |
| Add or Update Records | `upsertRecords` | Add or update records using a require match. For each record, require specifies the lookup values; if a match exists it is updated with fields, otherwise a new record is created. |
| Add Records | `addRecords` | Add one or more records to a table. Each record is an object with a fields map of column ids to values. |
| Add Table Data | `addTableData` | Add rows to a table in columnar format. Pass data as a JSON object string mapping column ids to arrays of values. |
| Copy Document | `copyDoc` | Copy a document into a workspace, optionally as a template (structure only). |
| Create Columns | `createColumns` | Add columns to a table. Each column has an id and a fields object (type, label, formula, widgetOptions, etc.). |
| Create Document | `createDocument` | Create a document directly, specifying its target workspace. Optionally copy from a source document. Returns the new document id. |
| Create Document in Workspace | `createDoc` | Create a new empty document inside a workspace. Returns the new document id. |
| Create Tables | `createTables` | Add one or more tables to a document. Each table has an id and an array of column definitions. |
| Create Webhooks | `createWebhooks` | Create one or more webhooks for a document. Each webhook's fields require a url, tableId, and eventTypes (add/update). |
| Create Workspace | `createWorkspace` | Create a new empty workspace within an organization. Returns the new workspace id. |
| Delete Column | `deleteColumn` | Delete a single column from a table. |
| Delete Document | `deleteDoc` | Permanently delete a document and all of its data. |
| Delete Records | `deleteRecords` | Delete records from a table by their numeric ids. Pass rowIds as a JSON array string, e.g. [1,2,3]. |
| Delete Table Data | `deleteTableData` | Delete rows from a table by their numeric ids. Pass rowIds as a JSON array string, e.g. [1,2,3]. |
| Delete Webhook | `deleteWebhook` | Remove a webhook from a document. |
| Delete Workspace | `deleteWorkspace` | Permanently delete a workspace and all documents inside it. |
| Download Attachment | `downloadAttachment` | Download the binary contents of a single attachment by its id. |
| Download Document (SQLite) | `downloadDocSqlite` | Download the full document as a Grist SQLite (.grist) file. |
| Download Table as CSV | `downloadTableCsv` | Download a single table from a document as a CSV file. |
| Download Table Schema | `downloadTableSchema` | Download the frictionless Table Schema (JSON) describing a table's structure. |
| Empty Webhook Queue | `emptyWebhookQueue` | Clear a document's queue of undelivered webhook payloads. |
| Force Reload Document | `forceReloadDoc` | Force the document engine to reload the document, disconnecting active clients. Useful to recover a stuck document. |
| Get Attachment Metadata | `getAttachment` | Get metadata (file name, size, upload time) for a single attachment by its id. |
| Get Current User | `getCurrentUser` | Retrieve the profile of the authenticated user (id, name, email). |
| Get Document | `getDoc` | Retrieve a document's metadata (name, workspace, pinned state, access). |
| Get Organization | `getOrg` | Retrieve details of a single organization (team) by its numeric id or subdomain. |
| Get Organization Usage | `getOrgUsage` | Get a usage summary for an organization (document, row, and attachment counts). |
| Get Table Data | `getTableData` | Fetch table data in columnar format (a map of column id to an array of values) with optional filter, sort, and limit. |
| Get Template | `getTemplate` | Retrieve details of a single Grist template document by its id. |
| Get Workspace | `getWorkspace` | Retrieve a workspace's metadata and the documents it contains. |
| List Attachments | `listAttachments` | List metadata for all attachments in a document, with optional filter, sort, and limit. |
| List Columns | `listColumns` | List the columns of a table, including their types and options. Set hidden to true to include system columns. |
| List Custom Widgets | `listWidgets` | List the custom widgets available in the Grist widget repository. |
| List Document Access | `listDocAccess` | List the users who have access to a document and their roles. |
| List Document Snapshots | `listDocSnapshots` | List saved snapshots (historical versions) of a document. |
| List Document States | `listDocStates` | List the recent action states (edit history) of a document. |
| List Organization Access | `listOrgAccess` | List the users who have access to an organization and their roles. |
| List Organizations | `listOrgs` | List all organizations (teams) the authenticated user has access to. |
| List Records | `listRecords` | Fetch records from a table with optional filtering, sorting, and limit. filter is a JSON object string mapping column names to arrays of allowed values. |
| List Tables | `listTables` | List all tables in a document. Set expand to 'column' to include column metadata. |
| List Templates | `listTemplates` | List the available Grist document templates in the template organization. |
| List Webhooks | `listWebhooks` | List all webhooks configured for a document. |
| List Workspace Access | `listWorkspaceAccess` | List the users who have access to a workspace and their roles. |
| List Workspaces | `listOrgWorkspaces` | List all workspaces (and the documents inside them) within an organization. |
| Modify Columns | `modifyColumns` | Modify existing columns of a table. Each entry has a column id and a fields object with the properties to change (including colId to rename). |
| Modify Document | `modifyDoc` | Update a document's metadata such as its name or pinned state. Does not change its contents. |
| Modify Document Access | `modifyDocAccess` | Grant, change, or revoke user access to a document. Provide a delta with a users map (email to role or null) and optional maxInheritedRole. |
| Modify Organization | `modifyOrg` | Rename an organization. Only owners may modify an org; personal orgs cannot be renamed. |
| Modify Organization Access | `modifyOrgAccess` | Grant, change, or revoke user access to an organization. Provide a delta object mapping emails to roles (owners/editors/viewers/members) or null to remove. |
| Modify Tables | `modifyTables` | Modify tables of a document, e.g. rename a table or toggle on-demand loading. Provide table id and fields to change. |
| Modify Webhook | `modifyWebhook` | Modify an existing webhook's fields (url, name, memo, enabled, eventTypes, tableId, isReadyColumn). Only provided fields are changed. |
| Modify Workspace | `modifyWorkspace` | Rename a workspace. |
| Modify Workspace Access | `modifyWorkspaceAccess` | Grant, change, or revoke user access to a workspace. Provide a delta with a users map (email to role or null) and optional maxInheritedRole. |
| Move Document | `moveDoc` | Move a document to another workspace. |
| Pin Document | `pinDoc` | Pin a document so it appears in the pinned section of its organization. |
| Remove Workspace to Trash | `removeWorkspace` | Move a workspace to the trash (soft delete). It can be restored within 30 days. |
| Restore Workspace | `unremoveWorkspace` | Restore a workspace previously moved to the trash. |
| Run SQL Query | `runSqlQuery` | Run a read-only (SELECT) SQL query against a document and return the matching records. |
| Run SQL Query with Parameters | `runSqlQueryParams` | Run a parameterized read-only SQL query against a document. Use ? placeholders in sql and supply values in args. |
| Unpin Document | `unpinDoc` | Unpin a document. |
| Update Records | `updateRecords` | Update existing records in a table. Each record must include its numeric id and a fields map of the columns to change. |
| Update Table Data | `updateTableData` | Update rows in a table in columnar format. The data must include an id array plus arrays for each column to change. |
| Upload Attachments | `uploadAttachments` | Upload one or more files as attachments to a document. Returns the ids of the created attachments. |
