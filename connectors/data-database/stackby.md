---
description: "Stackby is a no-code database and spreadsheet work platform."
hidden: true
---

# Stackby

<img src="../../.gitbook/assets/connectors/lg/stackby.png" alt="Stackby logo">

This connector manages stacks (databases), tables, columns, views, and rows - list, retrieve, create, update, and delete records - plus file uploads, via the Stackby Web API v1.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [stackby.com](https://stackby.com) |
| **Authentication** | API key |
| **Slug** | `stackby` |

## Use it

Add Stackby from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.stackby.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Column</td><td><code>createColumn</code></td><td>Create a new column (field) on a table. The column type is supplied in the path (e.g. shortText, number, date, link).</td></tr><tr><td>Create Rows</td><td><code>createRows</code></td><td>Create one or more rows in a table. Each record supplies a field map keyed by column name.</td></tr><tr><td>Create Stack</td><td><code>createStack</code></td><td>Create a new stack (database) in the workspace configured on the connection. The workspace identifier comes from the connection's Workspace ID credential.</td></tr><tr><td>Create Table</td><td><code>createTable</code></td><td>Create a new table in a stack.</td></tr><tr><td>Delete Column</td><td><code>deleteColumn</code></td><td>Delete a column (field) from a table.</td></tr><tr><td>Delete Row</td><td><code>deleteRow</code></td><td>Delete a single row from a table by its row ID.</td></tr><tr><td>Delete Stack</td><td><code>deleteStack</code></td><td>Delete a stack (database) from a workspace.</td></tr><tr><td>Delete Table</td><td><code>deleteTable</code></td><td>Delete a table from a stack.</td></tr><tr><td>List Columns</td><td><code>listColumns</code></td><td>List all columns (fields) defined on a table, including each column's type.</td></tr><tr><td>List New Rows in View</td><td><code>listNewRowsInView</code></td><td>List rows in a specific view flagged as new. Useful for polling a view for recently added records.</td></tr></tbody></table>

<details>

<summary>View 7 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Rows</td><td><code>listRows</code></td><td>List rows from a table in a stack. Supports optional row limit, view scoping, and latest-first ordering.</td></tr><tr><td>List Stacks</td><td><code>listStacks</code></td><td>List all stacks (databases) in the workspace configured on the connection. The workspace identifier comes from the connection's Workspace ID credential, so no input is required.</td></tr><tr><td>List Tables</td><td><code>listTables</code></td><td>List all tables in a stack.</td></tr><tr><td>List Views</td><td><code>listViews</code></td><td>List all views defined on a table.</td></tr><tr><td>Retrieve Row</td><td><code>retrieveRow</code></td><td>Retrieve a single row from a table by its row ID.</td></tr><tr><td>Update Rows</td><td><code>updateRows</code></td><td>Update one or more existing rows in a table. Each record supplies its row ID and the field values to change.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Upload a file to Stackby and receive a hosted URL that can be stored in a file/attachment column.</td></tr></tbody></table>

</details>
