---
description: "Stackby is a no-code database and spreadsheet work platform."
hidden: true
---

# Stackby

<img src="../../.gitbook/assets/connectors/lg/stackby.png" alt="Stackby logo">

Stackby is a no-code database and spreadsheet work platform. This connector manages stacks (databases), tables, columns, views, and rows - list, retrieve, create, update, and delete records - plus file uploads, via the Stackby Web API v1.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [stackby.com](https://stackby.com) |
| **Authentication** | API key |
| **Slug** | `stackby` |

## Use it

Add Stackby from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.stackby.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Column | `createColumn` | Create a new column (field) on a table. The column type is supplied in the path (e.g. shortText, number, date, link). |
| Create Rows | `createRows` | Create one or more rows in a table. Each record supplies a field map keyed by column name. |
| Create Stack | `createStack` | Create a new stack (database) in the workspace configured on the connection. The workspace identifier comes from the connection's Workspace ID credential. |
| Create Table | `createTable` | Create a new table in a stack. |
| Delete Column | `deleteColumn` | Delete a column (field) from a table. |
| Delete Row | `deleteRow` | Delete a single row from a table by its row ID. |
| Delete Stack | `deleteStack` | Delete a stack (database) from a workspace. |
| Delete Table | `deleteTable` | Delete a table from a stack. |
| List Columns | `listColumns` | List all columns (fields) defined on a table, including each column's type. |
| List New Rows in View | `listNewRowsInView` | List rows in a specific view flagged as new. Useful for polling a view for recently added records. |
| List Rows | `listRows` | List rows from a table in a stack. Supports optional row limit, view scoping, and latest-first ordering. |
| List Stacks | `listStacks` | List all stacks (databases) in the workspace configured on the connection. The workspace identifier comes from the connection's Workspace ID credential, so no input is required. |
| List Tables | `listTables` | List all tables in a stack. |
| List Views | `listViews` | List all views defined on a table. |
| Retrieve Row | `retrieveRow` | Retrieve a single row from a table by its row ID. |
| Update Rows | `updateRows` | Update one or more existing rows in a table. Each record supplies its row ID and the field values to change. |
| Upload File | `uploadFile` | Upload a file to Stackby and receive a hosted URL that can be stored in a file/attachment column. |
