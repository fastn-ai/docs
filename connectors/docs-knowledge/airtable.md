---
description: "Airtable connector — manage bases, tables, fields, records and webhooks via the Airtable Web API (https://api.airtable.com/v0)."
hidden: true
---

# Airtable

<img src="../../.gitbook/assets/connectors/lg/airtable.png" alt="Airtable logo">

Airtable connector — manage bases, tables, fields, records and webhooks via the Airtable Web API (https://api.airtable.com/v0). Connect with OAuth 2.0 (authorization code + PKCE), or with a Personal Access Token (Bearer).

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [airtable.com](https://airtable.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Slug** | `airtable` |

## Use it

Add Airtable from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.airtable.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Field | `createField` | Create a new field in a table. POST /meta/bases/{baseId}/tables/{tableId}/fields. Requires schema.bases:write scope. |
| Create Record Comment | `createComment` | Create a comment on a record. POST /{baseId}/{tableIdOrName}/{recordId}/comments. Requires data.recordComments:write scope. Use parentCommentId to reply in a thread. |
| Create Records | `createRecords` | Create one or more records (up to 10). POST /{baseId}/{tableIdOrName}. Pass an array of {fields} objects in 'records'. |
| Create Table | `createTable` | Create a new table in a base. POST /meta/bases/{baseId}/tables. Requires schema.bases:write scope. |
| Create Webhook | `createWebhook` | Register a webhook on a base. POST /bases/{baseId}/webhooks. Returns id and macSecretBase64 (save the secret to verify payloads). Requires webhook:manage scope. |
| Delete Record Comment | `deleteComment` | Delete a record comment. DELETE /{baseId}/{tableIdOrName}/{recordId}/comments/{rowCommentId}. Requires data.recordComments:write scope; only the comment author can delete it. |
| Delete Records | `deleteRecords` | Delete one or more records (up to 10). DELETE /{baseId}/{tableIdOrName}?records[]=recId. Pass record IDs in 'records'. |
| Delete Single Record | `deleteSingleRecord` | Delete a single record by ID. DELETE /{baseId}/{tableIdOrName}/{recordId}. |
| Delete Webhook | `deleteWebhook` | Delete a webhook from a base. DELETE /bases/{baseId}/webhooks/{webhookId}. |
| Get Base Schema | `getBaseSchema` | Get the schema (tables, fields, views) of a base. GET /meta/bases/{baseId}/tables. |

<details>

<summary>See 16 more actions</summary>

* **Get Record** `getRecord`: Retrieve a single record by ID. GET /{baseId}/{tableIdOrName}/{recordId}.
* **List Bases** `listBases`: List all bases the token can access. GET /meta/bases. Supports pagination via offset.
* **List Record Comments** `listComments`: List comments on a record. GET /{baseId}/{tableIdOrName}/{recordId}/comments. Requires data.recordComments:read scope. Supports pageSize (max 100) and offset pagination.
* **List Records** `listRecords`: List records in a table. GET /{baseId}/{tableIdOrName}. Supports filtering, sorting, pagination, field selection, and views.
* **List Webhook Payloads** `listWebhookPayloads`: Retrieve change payloads for a webhook since a cursor. GET /bases/{baseId}/webhooks/{webhookId}/payloads.
* **List Webhooks** `listWebhooks`: List webhooks registered on a base. GET /bases/{baseId}/webhooks.
* **Refresh Webhook** `refreshWebhook`: Extend a webhook's expiration time. POST /bases/{baseId}/webhooks/{webhookId}/refresh.
* **Toggle Webhook Notifications** `toggleWebhookNotifications`: Enable or disable ping notifications for a webhook. POST /bases/{baseId}/webhooks/{webhookId}/enableNotifications.
* **Update Field** `updateField`: Update a field's name and/or description. PATCH /meta/bases/{baseId}/tables/{tableId}/fields/{fieldId}. Requires schema.bases:write scope.
* **Update Record Comment** `updateComment`: Update the text of an existing record comment. PATCH /{baseId}/{tableIdOrName}/{recordId}/comments/{rowCommentId}. Requires data.recordComments:write scope; only the comment author can update it.
* **Update Records (PATCH)** `updateRecordsPatch`: Partial update of one or more records (up to 10). PATCH /{baseId}/{tableIdOrName}. Only specified cell values are updated; others are left unchanged.
* **Update Records (PUT)** `updateRecordsPut`: Destructive update of one or more records (up to 10). PUT /{baseId}/{tableIdOrName}. Any fields not included are cleared.
* **Update Single Record** `updateSingleRecord`: Partial update of a single record by ID. PATCH /{baseId}/{tableIdOrName}/{recordId}.
* **Update Table** `updateTable`: Update a table's name and/or description. PATCH /meta/bases/{baseId}/tables/{tableId}. Requires schema.bases:write scope.
* **Upsert Records (Bulk)** `upsertRecords`: Bulk create-or-update (upsert). PATCH /{baseId}/{tableIdOrName} with performUpsert.fieldsToMergeOn. Records matching on the merge fields are updated; others are created.
* **Who Am I** `whoami`: Get the current user's ID, email, and granted OAuth scopes for the authenticated token. GET /meta/whoami. No scopes required; email requires user.email:read; scopes array only present for OAuth tokens.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Field Created | `tableFields.add` | A field/column was added (dataTypes=tableFields, changeType=add). |
| Field Deleted | `tableFields.remove` | A field/column was removed (dataTypes=tableFields, changeType=remove). |
| Field Updated | `tableFields.update` | A field definition changed (dataTypes=tableFields, changeType=update). |
| Record Created | `tableData.add` | A record was added to a table (dataTypes=tableData, changeType=add). |
| Record Deleted | `tableData.remove` | A record was removed from a table (dataTypes=tableData, changeType=remove). |
| Record Updated | `tableData.update` | A record's cell values changed (dataTypes=tableData, changeType=update). |
| Table Created | `tableMetadata.add` | A table was added to the base (dataTypes=tableMetadata, changeType=add). |
| Table Deleted | `tableMetadata.remove` | A table was removed from the base (dataTypes=tableMetadata, changeType=remove). |
| Table Updated | `tableMetadata.update` | A table's metadata (name/description) changed (dataTypes=tableMetadata, changeType=update). |
