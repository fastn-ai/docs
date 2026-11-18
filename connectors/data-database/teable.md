---
description: "Teable is an open-source, Airtable-style no-code database (spaces > bases > tables > fields > records > views)."
hidden: true
---

# Teable

<img src="../../.gitbook/assets/connectors/lg/teable.png" alt="Teable logo">

Teable is an open-source, Airtable-style no-code database (spaces &gt; bases &gt; tables &gt; fields &gt; records &gt; views). This connector wraps the Teable Cloud REST API at https://app.teable.ai/api for base, table, field, record, view, aggregation, comment and trash operations.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [teable.ai](https://teable.ai) |
| **Authentication** | API key |
| **Slug** | `teable` |

## Use it

Add Teable from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.teable.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Field Type | `convertField` | Change a field's type in place, converting the existing cell values. Destructive when the new type cannot represent the old values. Returns the converted field definition. |
| Create Base | `createBase` | Create a new base inside a Teable space. Returns {id, name, icon, spaceId}. Requires the base\|create scope. |
| Create Field | `createField` | Add a field (column) to a table. type is one of singleLineText, longText, user, attachment, checkbox, multipleSelect, singleSelect, date, number, rating, formula, rollup, link, createdTime, lastModifiedTime, createdBy, lastModifiedBy, autoNumber, button. Pass type-specific settings in options. Returns the created field with its generated id. |
| Create Record Comment | `createRecordComment` | Post a plain-text comment on a record. The text is wrapped in Teable's rich-content shape [{"type":"p","children":[{"type":"span","value":text}]}]. Returns 201 with an empty body; list the comments to confirm. |
| Create Records | `createRecords` | Insert one or more rows into a table. records is an array of {fields:{...}} where the keys follow fieldKeyType (field name by default). Set typecast true to let Teable coerce loosely-typed values. Returns {records:[...]} with the generated record ids. |
| Create Space | `createSpace` | Create a new Teable space. Returns {id, name}. NOTE: a space-restricted personal access token can create a space but cannot then read, update or delete it - use an unrestricted token if you need to manage the new space. |
| Create Table | `createTable` | Create a table in a base. Pass fields as an array of {name, type} objects (type is one of singleLineText, longText, user, attachment, checkbox, multipleSelect, singleSelect, date, number, rating, formula, rollup, link, createdTime, lastModifiedTime, createdBy, lastModifiedBy, autoNumber, button) and optionally seed records as an array of {fields:{...}}. Returns the created table with its generated fields, views and records. |
| Create View | `createView` | Add a view to a table. type is grid, calendar, kanban, form, gallery or plugin. Returns the created view with its generated id. |
| Delete Base | `deleteBase` | Move a base to the space trash. Its tables and records go with it; it can be restored from the trash until it is permanently deleted. Returns 200 with an empty body. |
| Delete Field | `deleteField` | Remove a field (column) and all of its cell values from a table. Returns 200 with an empty body; list the fields again to confirm it is gone. |

<details>

<summary>See 53 more actions</summary>

* **Delete Multiple Records** `deleteRecords`: Delete up to five rows of a table in one call. Teable expects the qs array form recordIds[0..n]; the fastn engine comma-joins an array-typed query parameter, so each id is passed in its own numbered slot. Returns {records:[...]} listing the rows that were deleted - an empty array means nothing matched.
* **Delete Record** `deleteRecord`: Delete one row from a table by record id. Returns 200 with an empty body; read the record back (it 404s) or re-list to confirm.
* **Delete Record Comment** `deleteRecordComment`: Delete one comment from a record's thread by comment id. Returns 200 with an empty body; list the comments to confirm.
* **Delete Space** `deleteSpace`: Move a Teable space to the trash. Destructive: every base, table and record inside the space goes with it. Returns 200 with an empty body on success.
* **Delete Table** `deleteTable`: Move a table to the base trash. Its records go with it and can be restored until permanently deleted. Returns 200 with an empty body.
* **Delete View** `deleteView`: Delete a view from a table. The underlying records are not affected. Returns 200 with an empty body; re-list the views to confirm.
* **Disable View Share Link** `disableViewShare`: Turn off public sharing for a view, invalidating its share URL. Returns 200 with an empty body; read the view back and check that shareId and shareMeta are gone.
* **Duplicate Base** `duplicateBase`: Copy an existing base into a space, optionally including its records. Returns the new base {id, name, spaceId}.
* **Duplicate Field** `duplicateField`: Copy a field, including its cell values, into a new column of the same table. Returns the new field definition.
* **Duplicate Record** `duplicateRecord`: Copy one row and insert the copy before or after an anchor row in a given view. Returns the new record.
* **Duplicate Table** `duplicateTable`: Copy a table inside the same base, with or without its records. Returns the new table id.
* **Duplicate View** `duplicateView`: Copy a view, including its filter, sort, grouping and column settings, into a new view of the same table. Returns the new view. Note: Teable currently ignores the supplied name and auto-names the copy after the source view (e.g. "My view 2"); rename it afterwards with Rename View if you need an exact name.
* **Enable View Share Link** `enableViewShare`: Turn on public sharing for a view and return {shareId}. WARNING: the resulting URL https://app.teable.ai/share/{shareId}/view exposes the view's records to anyone who has the link, with no authentication. Disable it with Disable View Share Link when finished.
* **Get Base** `getBase`: Fetch one Teable base by id. Returns {id, name, icon, spaceId, createdBy, role, collaboratorType}.
* **Get Field** `getField`: Fetch one field of a table by id. Returns {id, name, dbFieldName, type, cellValueType, dbFieldType, options, isPrimary}.
* **Get Field Aggregation** `getFieldAggregation`: Run one aggregate function over one field of a table and return {aggregations:[{fieldId, total:{value, aggFunc}}]}. aggFunc is a Teable statistic such as count, empty, filled, unique, max, min, sum or average.
* **Get Record** `getRecord`: Fetch one row by record id. Returns {id, fields, name, autoNumber, createdTime, lastModifiedTime}.
* **Get Record Comment Count** `getRecordCommentCount`: Return {count} - how many comments a record has. Cheaper than listing the thread when you only need a badge number.
* **Get Record History** `getRecordHistory`: Return the cell-change history of a single record. Returns {historyList:[{fieldId, before, after, createdBy, createdTime}], userMap:{...}}.
* **Get Record Status** `getRecordStatus`: Report whether a record still exists and whether it is visible in a given view. Returns {isDeleted, isVisible}.
* **Get Space** `getSpace`: Fetch a single Teable space by its id. Returns {id, name, avatar, role}.
* **Get Table** `getTable`: Fetch one table of a base, including its id, name, dbTableName, defaultViewId, description and icon.
* **Get Table Default View Id** `getTableDefaultViewId`: Return {id} holding the id of the table's default (first) view. Useful before calling any view-scoped record query.
* **Get Table Permissions** `getTablePermission`: Return the caller's effective permission matrix for a table, grouped as {table, view, record, field, automation}, each a map of permission key to boolean.
* **Get Table Row Count** `getTableRowCount`: Return {rowCount} for a table, optionally narrowed by a view or a JSON filter. Cheaper than paging through List Records when you only need the total.
* **Get Table Search Count** `getTableSearchCount`: Count how many cells of a table match a full-text search term. Returns {count}. Use it to size a search before fetching rows.
* **Get View** `getView`: Fetch one view by id, including its type, filter, sort, group, options, columnMeta and share settings.
* **Get View Group Points** `getViewGroupPoints`: Return the group headers and per-group row counts a grid view would render for a grouping. groupBy is a JSON array of {fieldId, order}. Returns an array mixing group rows (type 0) and count rows (type 1).
* **List All Accessible Bases** `listAllBases`: List every base the token can access across all spaces. Returns an array of base objects with id, name, spaceId, icon, role and createdUser.
* **List Bases In Space** `listSpaceBases`: List the bases that belong to one Teable space. Returns an array of base objects with id, name, spaceId, order, icon and role.
* **List Fields** `listFields`: List the fields (columns) of a table. Returns an array of field objects with id, name, dbFieldName, type, cellValueType, isPrimary and options.
* **List Record Comments** `listRecordComments`: List the comment thread on one record. Returns {comments:[{id, content, createdBy, createdTime, reaction}], nextCursor}.
* **List Record Field Collaborators** `listRecordFieldCollaborators`: List the users referenced by a user-type field across the table's records, for building a person picker. fieldId must point at a field of type user. Returns an array of {userId, userName, email, avatar}.
* **List Records** `listRecords`: Query the rows of a table with paging, view scoping, field projection and a JSON filter. Returns {records:[{id, fields, name, autoNumber, createdTime}]}. The filter string uses Teable's filter DSL, e.g. {"conjunction":"and","filterSet":[{"fieldId":"fldXXX","operator":"is","value":"Ada"}]}.
* **List Spaces** `listSpaces`: List every Teable space the access token can reach. Returns an array of {id, name, avatar, role}. A space-restricted personal access token only lists the spaces it was scoped to.
* **List Table Record History** `listTableRecordHistory`: Return the cell-change history for a whole table. Returns {historyList:[...], userMap:{...}}; historyList is empty when nothing has been edited yet.
* **List Tables** `listTables`: List the tables in a Teable base. Returns an array of table objects with id, name, dbTableName, defaultViewId, order, icon and description.
* **List Views** `listViews`: List the views of a table. Returns an array of view objects with id, name, type (grid, kanban, form, gallery, calendar, plugin), order, filter, sort, group and columnMeta.
* **Permanently Delete Base** `permanentDeleteBase`: Irreversibly destroy a base and everything inside it, bypassing the trash. There is no undo. Returns 200 with an empty body.
* **Permanently Delete Table** `permanentDeleteTable`: Irreversibly destroy a table and all of its records, bypassing the trash. There is no undo. Returns 200 with an empty body.
* **Rename Table** `updateTableName`: Change a table's display name. Returns 200 with an empty body; read the table back to confirm.
* **Rename View** `updateViewName`: Change a view's display name. Returns 200 with an empty body; read the view back to confirm.
* **Set View Filter** `updateViewFilter`: Replace the filter of a view. filter is the Teable filter object, e.g. {"conjunction":"and","filterSet":[{"fieldId":"fldXXX","operator":"is","value":"Ada"}]}. Returns 200 with an empty body; read the view back to confirm.
* **Set View Grouping** `updateViewGroup`: Replace the grouping of a view. The live API takes {"group":[{fieldId, order}]} - the published swagger shows a bare array, which the server rejects. This action sends exactly one grouping level per call. Returns 200 with an empty body; read the view back to confirm.
* **Set View Sort** `updateViewSort`: Replace the sort order of a view. sortObjs is an array of {fieldId, order} where order is asc or desc. The live API wraps these in a `sort` object; the published swagger omits that wrapper and a flat body is rejected 400. Returns 200 with an empty body; read the view back to confirm.
* **Update Base** `updateBase`: Rename a base and/or change its emoji icon. Returns the updated base {id, name, icon, spaceId}.
* **Update Field** `updateField`: Rename a field and/or change its description. Does not change the field type - use Convert Field Type for that. Returns 200 with an empty body; read the field back to confirm.
* **Update Multiple Records** `updateRecords`: Update many rows in one call. records is an array of {id, fields:{...}}. Returns the array of updated records.
* **Update Record** `updateRecord`: Update the cell values of one row. fields is a map of field name (or id, per fieldKeyType) to the new value; omitted fields keep their current value. Returns the updated record.
* **Update Space Name** `updateSpace`: Rename an existing Teable space. Returns the updated {id, name}.
* **Update Table Description** `updateTableDescription`: Set the description text shown under a table. Returns 200 with an empty body; read the table back to confirm.
* **Update Table Icon** `updateTableIcon`: Set the emoji icon shown next to a table in the sidebar. Returns 200 with an empty body; read the table back to confirm.
* **Update View Description** `updateViewDescription`: Set the description text of a view. Returns 200 with an empty body; read the view back to confirm.

</details>
