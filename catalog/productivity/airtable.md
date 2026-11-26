---
description: "Airtable is a spreadsheet-style database. Create, update and delete records, manage tables and fields, and add record comments."
hidden: true
---

# Airtable

<img src="../../.gitbook/assets/connectors/lg/airtable.png" alt="Airtable logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [airtable.com](https://airtable.com) |
| **Authentication** | Access token, OAuth 2.0 |
| **Slug** | `airtable` |

## Setup

Your customers sign in to Airtable through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Airtable from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.airtable.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Field</td><td><code>createField</code></td><td>Create a new field in a table. Requires schema.bases:write scope.</td></tr><tr><td>Create Record Comment</td><td><code>createComment</code></td><td>Create a comment on a record. Requires data.recordComments:write scope. Use parentCommentId to reply in a thread.</td></tr><tr><td>Create Records</td><td><code>createRecords</code></td><td>Create one or more records (up to 10). Pass an array of {fields} objects in 'records'.</td></tr><tr><td>Create Table</td><td><code>createTable</code></td><td>Create a new table in a base. Requires schema.bases:write scope.</td></tr><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Register a webhook on a base. Returns id and macSecretBase64 (save the secret to verify payloads). Requires webhook:manage scope.</td></tr><tr><td>Delete Record Comment</td><td><code>deleteComment</code></td><td>Delete a record comment. Requires data.recordComments:write scope; only the comment author can delete it.</td></tr><tr><td>Delete Records</td><td><code>deleteRecords</code></td><td>Delete one or more records (up to 10). Pass record IDs in 'records'.</td></tr><tr><td>Delete Single Record</td><td><code>deleteSingleRecord</code></td><td>Delete a single record by ID.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Delete a webhook from a base.</td></tr><tr><td>Get Base Schema</td><td><code>getBaseSchema</code></td><td>Get the schema (tables, fields, views) of a base.</td></tr></tbody></table>

<details>

<summary>View 16 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Record</td><td><code>getRecord</code></td><td>Retrieve a single record by ID.</td></tr><tr><td>List Bases</td><td><code>listBases</code></td><td>List all bases the token can access. Supports pagination via offset.</td></tr><tr><td>List Record Comments</td><td><code>listComments</code></td><td>List comments on a record. Requires data.recordComments:read scope. Supports pageSize (max 100) and offset pagination.</td></tr><tr><td>List Records</td><td><code>listRecords</code></td><td>List records in a table. Supports filtering, sorting, pagination, field selection, and views.</td></tr><tr><td>List Webhook Payloads</td><td><code>listWebhookPayloads</code></td><td>Retrieve change payloads for a webhook since a cursor.</td></tr><tr><td>List Webhooks</td><td><code>listWebhooks</code></td><td>List webhooks registered on a base.</td></tr><tr><td>Refresh Webhook</td><td><code>refreshWebhook</code></td><td>Extend a webhook's expiration time.</td></tr><tr><td>Toggle Webhook Notifications</td><td><code>toggleWebhookNotifications</code></td><td>Enable or disable ping notifications for a webhook.</td></tr><tr><td>Update Field</td><td><code>updateField</code></td><td>Update a field's name and/or description. Requires schema.bases:write scope.</td></tr><tr><td>Update Record Comment</td><td><code>updateComment</code></td><td>Update the text of an existing record comment. Requires data.recordComments:write scope; only the comment author can update it.</td></tr><tr><td>Update Records (PATCH)</td><td><code>updateRecordsPatch</code></td><td>Partial update of one or more records (up to 10). Only specified cell values are updated; others are left unchanged.</td></tr><tr><td>Update Records (PUT)</td><td><code>updateRecordsPut</code></td><td>Destructive update of one or more records (up to 10). Any fields not included are cleared.</td></tr><tr><td>Update Single Record</td><td><code>updateSingleRecord</code></td><td>Partial update of a single record by ID.</td></tr><tr><td>Update Table</td><td><code>updateTable</code></td><td>Update a table's name and/or description. Requires schema.bases:write scope.</td></tr><tr><td>Upsert Records (Bulk)</td><td><code>upsertRecords</code></td><td>Bulk create-or-update (upsert). with performUpsert.fieldsToMergeOn. Records matching on the merge fields are updated; others are created.</td></tr><tr><td>Who Am I</td><td><code>whoami</code></td><td>Get the current user's ID, email, and granted OAuth scopes for the authenticated token. No scopes required; email requires user.email:read; scopes array only present for OAuth tokens.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Field Created</td><td><code>tableFields.add</code></td><td>A field/column was added (dataTypes=tableFields, changeType=add).</td></tr><tr><td>Field Deleted</td><td><code>tableFields.remove</code></td><td>A field/column was removed (dataTypes=tableFields, changeType=remove).</td></tr><tr><td>Field Updated</td><td><code>tableFields.update</code></td><td>A field definition changed (dataTypes=tableFields, changeType=update).</td></tr><tr><td>Record Created</td><td><code>tableData.add</code></td><td>A record was added to a table (dataTypes=tableData, changeType=add).</td></tr><tr><td>Record Deleted</td><td><code>tableData.remove</code></td><td>A record was removed from a table (dataTypes=tableData, changeType=remove).</td></tr><tr><td>Record Updated</td><td><code>tableData.update</code></td><td>A record's cell values changed (dataTypes=tableData, changeType=update).</td></tr><tr><td>Table Created</td><td><code>tableMetadata.add</code></td><td>A table was added to the base (dataTypes=tableMetadata, changeType=add).</td></tr><tr><td>Table Deleted</td><td><code>tableMetadata.remove</code></td><td>A table was removed from the base (dataTypes=tableMetadata, changeType=remove).</td></tr><tr><td>Table Updated</td><td><code>tableMetadata.update</code></td><td>A table's metadata (name/description) changed (dataTypes=tableMetadata, changeType=update).</td></tr></tbody></table>
