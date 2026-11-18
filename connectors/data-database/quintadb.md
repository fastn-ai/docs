---
description: "QuintaDB online database and form builder."
hidden: true
---

# QuintaDB

<img src="../../.gitbook/assets/connectors/quintadb.png" alt="QuintaDB logo" width="64">

QuintaDB online database and form builder. Manage databases (apps), forms (tables), fields (columns), records, reports, file attachments, bulk updates and record search through the QuintaDB REST API.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [quintadb.com](https://quintadb.com) |
| **Authentication** | API key |
| **Slug** | `quintadb` |

## Use it

Add QuintaDB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.quintadb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Database | `createDatabase` | Create a new QuintaDB database (app). A database cannot exist without at least one form, so a first form name is required too. Returns the new database id and the new form id. |
| Create Field | `createField` | Add a field (column) to a QuintaDB form. Returns the new field including the id that is used as the key in record value maps. |
| Create Form | `createForm` | Create a new form (table) inside an existing QuintaDB database. Returns the new form with its id. |
| Create Record | `createRecord` | Create a record in a QuintaDB form. The values object must contain entity_id (the form id) plus one key per field id. Optionally pass your own 22-character URL-safe base64 id inside values to control the record id - required when a file was uploaded for the record beforehand. |
| Create Webhook | `createWebhook` | Register an outbound webhook on a QuintaDB form so record events are POSTed to your URL. QuintaDB exposes webhook management only through its MCP endpoint (https://quintadb.com/mcp), not through the documented REST API, so this action wraps that JSON-RPC call with the same REST API key. The webhook fires when an action rule on the form runs. |
| Delete All Records | `deleteAllRecords` | Permanently delete EVERY record in a QuintaDB form, or only those in a saved report when view is supplied. This cannot be undone. Returns {"success":"Done"}; confirm with List Records. |
| Delete Database | `deleteDatabase` | Permanently delete a QuintaDB database (app) together with all of its forms, fields and records. This cannot be undone. Returns the remaining databases in the account. |
| Delete Field | `deleteField` | Permanently delete a QuintaDB field (column) and the data stored in it for every record. This cannot be undone. Returns the fields that remain on the form. |
| Delete Form | `deleteForm` | Permanently delete a QuintaDB form (table) and every record in it. This cannot be undone. Returns the forms that remain in the database. |
| Delete Multiple Records | `deleteMultipleRecords` | Permanently delete a chosen list of QuintaDB records. Pass the ids as json_dtype_ids (a JSON array string) or dtype_ids (an array). This cannot be undone. Returns {"success":"Records successfully deleted"}; confirm with List Records. |

<details>

<summary>See 29 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Record | `deleteRecord` | Permanently delete a single QuintaDB record by its id. This cannot be undone. Returns {"result":"Successfully deleted"}. |
| Delete Webhook | `deleteWebhook` | Remove an outbound webhook from a QuintaDB database by its id. Served by QuintaDB's MCP endpoint (https://quintadb.com/mcp) because webhook management is absent from the documented REST API. Confirm with List Webhooks that the entry is gone. |
| Get Column Total | `getColumnTotal` | Sum a numeric QuintaDB field across all records of a form, or across a saved report when view is supplied. Returns {"total": number}. |
| Get Database | `getDatabase` | Fetch a single QuintaDB database (app) by its id. Returns the database name, timestamps and counts of records, forms and fields. Note: QuintaDB answers HTTP 200 with an error field ("App with such id not found") when the id does not exist, so check the body rather than the status code. |
| Get Database By Name | `getDatabaseByName` | Look up a QuintaDB database (app) by its exact name instead of its id. Returns HTTP 200 with an error field when no database carries that name. |
| Get Field | `getField` | Fetch a single QuintaDB field (column) by its id. The vendor returns the single field under the plural key "fields". |
| Get Field By Name | `getFieldByName` | Look up a QuintaDB field (column) by database name, form name and field name instead of by ids. KNOWN VENDOR BUG: as of 2026-09 this documented endpoint always answers HTTP 200 with {"error":"Field not found"} even for a field that exists and is returned by List Fields. Use List Fields or Get Field instead until QuintaDB fixes it. |
| Get Form | `getForm` | Fetch a single QuintaDB form (table) by its id. Returns HTTP 200 with an error field when the form id does not exist. |
| Get Form By Name | `getFormByName` | Look up a QuintaDB form (table) by the database name and form name instead of by ids. Returns HTTP 200 with an error field when no matching form exists. |
| Get Record | `getRecord` | Fetch a single QuintaDB record by its id. Values are keyed by field id; set name_value to 1 to also receive them keyed by field name. |
| Get Relationship Record ID | `getRelationshipRecordId` | Return the numeric rel_id of a QuintaDB relationship field. QuintaDB answers with a BARE INTEGER body (e.g. 128011), not a JSON object, so the value arrives as the whole response rather than under a key; a field that is not a configured relationship returns a bare null. Use the rel_id when linking records: pass values.rel = {"&lt;rel_id&gt;": "&lt;target record id&gt;"} (or an array of ids for many-to-many) to Create Record or Update Record. |
| List Databases | `listDatabases` | List all QuintaDB databases (apps) in the authenticated account. Results are paginated 20 per page. Returns each database id, name, timestamps and counts of records, forms and fields. |
| List Fields | `listFields` | List every field (column) of a QuintaDB form. Returns each field's id, name, description, type, default value, position and display size. Field ids are the keys used in record value maps. |
| List Forms | `listForms` | List every form (table) inside a QuintaDB database. Returns each form's id, name, description, notification address, sort settings, page size and record count. |
| List Records | `listRecords` | List the records of a QuintaDB form, optionally restricted to a saved report (view). Values are keyed by field id; set name_value to 1 to also receive them keyed by field name. fetch_all with per_page returns more than one page at once on paid plans (FREE 200, STANDARD 500, PROFESSIONAL 1000, ENTERPRISE 2000 rows). |
| List Reports | `listReports` | List the saved reports (views) defined on a QuintaDB form. A report id can be passed as the view parameter to List Records, Search Records, Get Column Total, Update All Records and Delete All Records. |
| List Webhooks | `listWebhooks` | List the outbound webhooks registered on a QuintaDB database, optionally filtered to one form. Served by QuintaDB's MCP endpoint (https://quintadb.com/mcp) because webhook management is absent from the documented REST API. Returns id, url, method, entity_id and action_rule_id per webhook. |
| Remove File From Record | `removeFileFromRecord` | Delete one uploaded file from a QuintaDB file or image field on a record. Returns {"error":"File removed"} - despite the key name that is the success response. Confirm with Get Record that the field is now null. |
| Run Action On Multiple Records | `runActionOnMultipleRecords` | Trigger a QuintaDB action column for a list of records at once, or for every record of the table or report when run_by_all_table_or_report is true. Returns {"success":"Done"}. Be aware the configured action may send a real message to every record it runs against. |
| Run Action On Record | `runActionOnRecord` | Trigger a QuintaDB action column for one record. The action column is a field of type "action" whose behaviour (email, SMS, webhook, record change) is configured in the QuintaDB form designer. Returns {"success":"Done"}. Be aware the configured action may send a real message. |
| Search Records | `searchRecords` | Search the records of a QuintaDB form with field-level criteria. The search value is an array of arrays of {a: field id (or -ALL- for every column), b: value, o: operator}; clauses in the same inner array are ANDed, separate inner arrays are ORed. Operators include is, is_not, is_empty, is_not_empty, starts_with, ends_with, like, contains, not_contains, the numeric comparisons less_than/greater_than/less_than_or_equal_to/greater_than_or_equal_to and the date ranges today, last_7_days, this_month and similar. Maximum 200 rows. |
| Update All Records | `updateAllRecords` | Set one field to the same value on EVERY record of a QuintaDB form, or of a saved report when view is supplied. This rewrites data in bulk and cannot be undone. Returns {"success":"Done"}; confirm with List Records. |
| Update Cell Value | `updateCellValue` | Write a single cell: set one field of one QuintaDB record to a new value. Returns the stored value as {"new_value": ...}. |
| Update Database | `updateDatabase` | Rename an existing QuintaDB database (app). Returns the updated database record. |
| Update Field | `updateField` | Change a QuintaDB field's name, description, default value, position or display dimensions. The vendor silently ignores the "visible" flag and the field type cannot be changed after creation, so neither is exposed here. |
| Update Form | `updateForm` | Rename a QuintaDB form (table) and set its description. QuintaDB's update-form endpoint accepts only name and desc; per_page, allow_delete, asc, sort_by and post_action are silently ignored by the vendor and are therefore not exposed here. |
| Update Multiple Records | `updateMultipleRecords` | Set one field to the same value across a chosen list of QuintaDB records. Pass the record ids as json_dtype_ids (a JSON-encoded array string) or dtype_ids (an array). Returns {"success":"Done"}; confirm the change with List Records. |
| Update Record | `updateRecord` | Update the values of a single QuintaDB record. Only the field ids present in the values object are changed; omitted fields keep their current value. |
| Upload File To Record | `uploadFileToRecord` | Attach a text file to a QuintaDB file or image field. QuintaDB stores the upload against a record id that must be supplied up front, so the order is: generate a 22-character URL-safe base64 record id, call this action with it, then call Create Record (or Update Record) passing the same id inside values and the file name as the value of the file field. Only text content can be sent; binary uploads are not supported by the fastn HTTP engine. Returns {"error":"Uploaded"} - despite the key name that is the success response. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Record Created | `on_create` | Fires when a record is added to the watched QuintaDB form and an action rule with on_create is configured on that form. QuintaDB webhooks are form-scoped and carry no event-type discriminator, so create and update deliveries are distinguished only by which action rule fired; configure exactly one rule per trigger. payloadSchema below is MODELLED from QuintaDB's record representation, not captured from a live delivery. |
| Record Updated | `on_update` | Fires when a record in the watched QuintaDB form is changed and an action rule with on_update is configured on that form. QuintaDB webhooks are form-scoped and carry no event-type discriminator, so create and update deliveries are distinguished only by which action rule fired; configure exactly one rule per trigger. payloadSchema below is MODELLED from QuintaDB's record representation, not captured from a live delivery. |
