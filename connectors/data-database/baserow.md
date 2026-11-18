---
description: "Baserow is an open-source no-code database platform (an Airtable alternative)."
hidden: true
---

# Baserow

<img src="../../.gitbook/assets/connectors/lg/baserow.png" alt="Baserow logo">

Baserow is an open-source no-code database platform (an Airtable alternative). This connector manages rows, fields, and tables through Baserow's database-token-authenticated REST API: list, get, create, update, delete, move, and batch rows; list and create fields; discover tables accessible to the token; and validate the token or a row's password field.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [baserow.io](https://baserow.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `baserow` |

## Use it

Add Baserow from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.baserow.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Authenticate Password Field | `authenticatePasswordField` | Checks whether a supplied password matches the value stored in a row's password-type field, without ever exposing the stored password. Use this to build custom login/authentication flows against a Baserow table that has a "password" field. |
| Batch Create Rows | `batchCreateRows` | Creates up to 200 rows in a single request. Each item in the items array is a field name -&gt; value object for one new row (call List Fields first to see this table's exact field names, types, and select-option ids). |
| Batch Delete Rows | `batchDeleteRows` | Permanently deletes up to 200 rows from a Baserow table in a single request. |
| Batch Update Rows | `batchUpdateRows` | Updates up to 200 existing rows in a single request. Each item must include the row's id plus the field name -&gt; value pairs to change on that row; fields omitted on an item are left untouched. |
| Check Database Token | `checkToken` | Verifies that the configured database token is valid. Returns a simple confirmation; a 401 means the token is invalid or has been revoked. Useful as a lightweight connectivity/health check. |
| Create Field | `createField` | Creates a new field (column) on a Baserow table. Set "type" to the field type (e.g. text, number, boolean, single_select, link_row) and supply only the type-specific properties relevant to that type; irrelevant properties are ignored. Note: updating or deleting an existing field requires a Baserow user (JWT) session and is not available through this database-token connection - only field creation and listing are token-authenticated. |
| Create Field (User Session) | `createFieldWithSession` | Creates a new field (column) on a Baserow table, authenticated with a JWT user session rather than a database token. Use this instead of Create Field when the database token is rejected with ERROR_NO_PERMISSION_TO_TABLE (Baserow's object-permission layer denies field mutation to some tokens even when the token's own create/update/delete toggles are all enabled) - a real user session carries the user's own workspace membership permissions instead. Set "type" to the field type and supply only the type-specific properties relevant to that type. |
| Create Row | `createRow` | Creates a new row in a Baserow table. Pass the table id plus one top-level input property per field you want to set (field name as key, recommended - call List Fields first to see exact field names, types, and select-option ids for this table). Fields you omit keep their default value. |
| Create Table | `createTable` | Creates a new table inside a Baserow database, optionally seeded with initial row data. If "data" is omitted, Baserow creates the table with its own example data. Requires the JWT (user session) auth method - table creation is not available through a database token. |
| Create Table Webhook | `createTableWebhook` | Creates a webhook subscription on a Baserow table: Baserow will POST (or another configured method) to your URL whenever the selected events occur (rows created/updated/deleted, field created/updated/deleted, view created/updated/deleted, view rows entered). Requires the JWT (user session) auth method - the webhook subscription API does not accept a database token. |
| Create View | `createView` | Creates a new view on a Baserow table. Set "type" to grid, gallery, form, kanban, calendar, or timeline; each type accepts its own additional settings beyond the common fields listed here (e.g. a grid view's row_height_size, a kanban view's single_select_field) - pass any such type-specific setting as an extra top-level property and Baserow will apply it (undocumented-here properties are accepted directly, per Baserow's per-type view schemas). Requires the JWT (user session) auth method. |
| Delete Field | `deleteField` | Permanently deletes a field (column) and all of its data from a Baserow table. Requires the JWT (user session) auth method. |
| Delete Row | `deleteRow` | Permanently deletes a single row from a Baserow table. |
| Delete Table | `deleteTable` | Permanently deletes a Baserow table and all of its fields and rows. Requires the JWT (user session) auth method. |
| Delete Table Webhook | `deleteTableWebhook` | Permanently deletes a table webhook subscription. Requires the JWT (user session) auth method. |
| Delete View | `deleteView` | Permanently deletes a Baserow view (grid, gallery, form, kanban, calendar, or timeline). Requires the JWT (user session) auth method. |
| Get Field | `getField` | Fetches a single field (column) definition by its id, including its type and full type-specific configuration. Requires the JWT (user session) auth method - Baserow only allows List Fields and Create Field over a database token, not a single-field GET. |
| Get Row | `getRow` | Fetches a single row from a Baserow table by its row id. |
| Get Table | `getTable` | Fetches a single Baserow table by its id, including its name, order, parent database id, and data-sync configuration if any. Requires the JWT (user session) auth method. |
| Get Table Webhook | `getTableWebhook` | Fetches a single table webhook by its id, including its recent call history. Requires the JWT (user session) auth method. |
| Get View | `getView` | Fetches a single Baserow view by its id. The shape of the response depends on the view's type (grid/gallery/form/kanban/calendar/timeline), each with its own type-specific settings alongside the common name/order/filters/sortings fields. Requires the JWT (user session) auth method. |
| List Accessible Tables | `listTables` | Lists every table the current database token can access, across all databases the token is scoped to, including each table's id, name, and parent database id. Use this to discover the tableId values needed by the row and field actions. |
| List Fields | `listFields` | Lists every field (column) defined on a Baserow table, including each field's id, name, type, and type-specific configuration (e.g. select options, number formatting). Use this before Create Row / Update Row / Create Field to discover exact field names, types, and valid select-option ids. Note: Baserow returns a raw JSON array of field objects (the outputContract's \"items\" wrapper is a schema-representation convention, not part of the real response body). |
| List Grid View Rows | `listGridViewRows` | Lists the rows of a table through one of its grid views, applying that view's own saved filters/sorts plus any ad-hoc filters, search, or ordering passed here. Use the "filters" JSON parameter for ad-hoc field filters (Baserow's per-field "filter__{field}__{condition}" query-parameter form is not exposed here since the field to filter on is only known at call time). Requires the JWT (user session) auth method - grid view row listing needs a view id, which requires JWT to discover via List Views. Note: unlike List Rows, this endpoint does not support user_field_names - rows are always returned keyed by field_&lt;id&gt;; call List Fields to map ids to names. |
| List Row Names | `listRowNames` | Looks up the display name (primary field value) of specific rows across one or more tables, without fetching every field. Useful for resolving link-row references to human-readable labels. |
| List Rows | `listRows` | Lists the rows of a Baserow table, with optional pagination, search, filtering, sorting, and field selection. Returns a paginated envelope with the total row count and the matching rows. |
| List Table Webhooks | `listTableWebhooks` | Lists all webhooks configured on a Baserow table. Requires the JWT (user session) auth method - Baserow's webhook subscription API does not accept a database token. Baserow returns a bare JSON array (the outputContract's "items" wrapper is a schema-representation convention, not part of the real response body). |
| List Tables In Database | `listTablesInDatabase` | Lists every table that belongs to a specific Baserow database (application), including each table's id, name, and order. Requires the JWT (user session) auth method. For a token-scoped view across every database the token can see, use List Accessible Tables instead. |
| List Views | `listViews` | Lists every view (grid, gallery, form, kanban, calendar, or timeline) defined on a Baserow table. Requires the JWT (user session) auth method. Baserow returns a bare JSON array (the outputContract's "items" wrapper is a schema-representation convention, not part of the real response body). |
| Move Row | `moveRow` | Moves a row to a new position in a Baserow table, either to before a given row or to the end of the table. |
| Test Table Webhook | `testTableWebhook` | Sends a real, immediate test call for a given event type to a URL, without creating a saved webhook. Returns a copy of the request that was sent, the response received, and whether the URL was reachable - use this to validate an endpoint before saving it with Create Table Webhook. Requires the JWT (user session) auth method. |
| Update Field | `updateField` | Updates an existing field (column) on a Baserow table - rename it, change its type, or change its type-specific configuration (e.g. select options, number formatting). Set "type" to change the field's type and supply only the type-specific properties relevant to that type; omitted properties are left unchanged. Requires the JWT (user session) auth method. |
| Update Row | `updateRow` | Updates one or more field values on an existing row in a Baserow table. Only the fields you pass are changed; every other field on the row is left untouched. Pass the table id and row id plus one top-level input property per field to update (field name as key, recommended - call List Fields first to see exact field names, types, and select-option ids for this table). |
| Update Table | `updateTable` | Renames an existing Baserow table. Requires the JWT (user session) auth method. |
| Update Table Webhook | `updateTableWebhook` | Updates an existing table webhook. Only the fields you pass are changed. Use "active":false to pause a webhook without deleting it (Baserow also auto-deactivates a webhook after repeated delivery failures). Requires the JWT (user session) auth method. |
| Update View | `updateView` | Updates an existing Baserow view. Only the fields you pass are changed. Accepts the same common settings as Create View plus any type-specific extra property for that view's own type (grid/gallery/form/kanban/calendar/timeline). Requires the JWT (user session) auth method. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Field Created | `field.created` | A field was created in the table. |
| Field Deleted | `field.deleted` | A field was deleted from the table. |
| Field Updated | `field.updated` | A field in the table was updated. |
| Rows Created | `rows.created` | One or more rows were created in the table. |
| Rows Deleted | `rows.deleted` | One or more rows were deleted from the table. |
| Rows Entered View | `view.rows_entered` | One or more rows entered a filtered view. |
| Rows Updated | `rows.updated` | One or more rows were updated in the table. |
| View Created | `view.created` | A view was created on the table. |
| View Deleted | `view.deleted` | A view was deleted from the table. |
| View Updated | `view.updated` | A view on the table was updated. |
