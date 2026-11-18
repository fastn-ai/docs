---
description: "Notion REST API connector for managing pages, databases, blocks, users, comments, and search across a Notion workspace."
hidden: true
---

# Notion

<img src="../../.gitbook/assets/connectors/lg/notion.png" alt="Notion logo">

Notion REST API connector for managing pages, databases, blocks, users, comments, and search across a Notion workspace.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [notion.so](https://notion.so) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `notion` |

## Use it

Add Notion from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.notion.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Append Block Children | `appendBlockChildren` | Append new child blocks to a Notion page or block |
| Append Block Children (Raw) | `appendBlockChildrenRaw` | Append fully-formed Notion block objects to a page or block. Unlike appendBlockChildren, which wraps a single plain-text string in one paragraph, this accepts the raw children array so callers can send headings, bulleted_list_items, dividers and mixed rich_text. Pass children exactly as the Notion API expects, e.g. [{object:"block",type:"heading_3",heading_3:{rich_text:[{type:"text",text:{content:"Title"}}]}}]. Max 100 blocks per call. Returns the list of created block objects. |
| Complete File Upload | `completeFileUpload` | Finalize a multi_part file upload after all parts have been sent (POST file_uploads/{file_upload_id}/complete). No request body. Only used for multi_part mode; single_part and external_url uploads do not need this call. Returns the file_upload object with status 'uploaded'. |
| Create Comment | `createComment` | Create a comment on a Notion page |
| Create Data Source | `createDataSource` | Add an additional data source to an existing Notion database. A standard table view is automatically created alongside the new data source. |
| Create Database | `createDatabase` | LEGACY - create a new database in Notion as a child of a page, with a single title column named "Name". Deliberately pinned to Notion-Version 2022-06-28. Verified live: this same request body is still ACCEPTED on 2026-03-11 (HTTP 200), but the response body there omits the properties (column schema) object that this action's outputContract declares and instead returns a data_sources[] array, so the version is held back to keep the documented response correct. On current API versions a database is a container of data sources: after creating one, add or inspect its schema with createDataSource / retrieveDataSource / updateDataSource, and add rows with createPageRaw using a data_source_id parent. |
| Create Database Row (Plain Text) | `createDatabaseRowPlainText` | Create a row (page) in a Notion database from flat plain-text inputs. The title goes into the database's title column (titleProperty, e.g. "Name"); the plain-text description becomes one paragraph in the page body. status and priority are optional objects sent under statusProperty / priorityProperty ({status:{name}} / {select:{name}}). Unset optional fields are omitted. Returns the created page. |
| Create File Upload | `createFileUpload` | Start a file upload (POST file_uploads). Returns a file_upload object (status 'pending') whose upload_url is then used by sendFileUpload to transmit bytes. mode defaults to single_part; for files &gt;20MB use multi_part with filename + number_of_parts; for external_url provide an HTTPS external_url. Required body fields depend on mode; this action templates only the always-safe defaults (mode). Pass filename/content_type/number_of_parts/external_url via input as needed. |
| Create Page | `createPage` | Create a new page in Notion as a child of another PAGE. Note: parentId is always sent as parent.page_id, so this action only supports page parents, not database parents. To create a row in a database use createPageRaw with a parent of {"data_source_id":"&lt;id&gt;"} (Notion 2025-09-03 and later) — a database parent is no longer addressed by database_id on current API versions. |
| Create Page (Raw) | `createPageRaw` | Create a Notion page from a fully-formed request body. Unlike createPage (page parents only), this sends parent/properties/children verbatim and supports every parent type: {"page_id":"..."} for a child page, {"data_source_id":"..."} for a row in a data source (preferred on Notion 2025-09-03+), and {"database_id":"..."} which is still accepted and auto-resolves to that database's data source when it has only one. For a database or data source parent the title key MUST match that data source's real title column (resolve it with retrieveDataSource and pick the property whose type is "title") - a hardcoded "title" key returns validation_error. children accepts up to 100 fully-formed Notion block objects. Runs on Notion-Version 2026-03-11; all three parent forms verified live. Returns the created page object. |
| Delete Block | `deleteBlock` | Archive (delete) a Notion block |
| Get Block | `getBlock` | Retrieve a single block from Notion by its ID |
| Get Block Children | `getBlockChildren` | Retrieve all child blocks of a Notion block or page |
| Get Bot User | `getBotUser` | Retrieve the bot user associated with the current OAuth token |
| Get Comment | `getComment` | Retrieve a single Notion comment by its comment_id (GET comments/{comment_id}). Pinned to Notion-Version 2026-03-11, consistent with the rest of the connector. Verified live on both 2022-06-28 and 2026-03-11: the endpoint is available on BOTH, so the earlier "requires 2026-03-11 or later" note in this description was incorrect. Returns the comment object with rich_text, parent, discussion_id. |
| Get Database | `getDatabase` | Retrieve a Notion database by its ID. LEGACY - deliberately pinned to Notion-Version 2022-06-28. Verified live: on 2026-03-11 this endpoint still returns 200 but its body changes shape - it returns a data_sources[] array and OMITS the properties (column schema) object this action's outputContract declares. It is therefore kept on 2022-06-28 so the documented response stays correct. For the column schema on current API versions use retrieveDataSource with a data_source_id; list a database's data sources by reading data_sources[] from a 2026-03-11 call. Known limitation: on 2022-06-28 a database with MULTIPLE data sources returns "Databases with multiple data sources are not supported in this API version" - use retrieveDataSource for those. |
| Get File Upload | `getFileUpload` | Retrieve a single file_upload object by its id (GET file_uploads/{file_upload_id}). Use to poll upload status. Returns the file_upload object. |
| Get Page | `getPage` | Retrieve a Notion page by its ID |
| Get Page Property | `getPageProperty` | Retrieve a specific property of a Notion page |
| Get User | `getUser` | Retrieve a specific Notion user by their ID |
| List Comments | `listComments` | Retrieve all comments on a Notion page or block |
| List Data Source Templates | `listDataSourceTemplates` | Retrieves details of all page templates available for a given data source. Results are paginated up to 100 per page. |
| List File Uploads | `listFileUploads` | List file_upload objects for the workspace (GET file_uploads). Supports filtering by status and cursor pagination. Returns a paginated list envelope with results[]. Query params (status, start_cursor, page_size) are auto-appended on GET from the inputContract. |
| List Users | `listUsers` | List all users in a Notion workspace |
| Query Data Source | `queryDataSource` | Gets a paginated list of pages (rows) contained in a data source, filtered and sorted according to the provided conditions. Supports up to 10,000 results per query. |
| Query Database | `queryDatabase` | LEGACY - query a Notion database and return matching pages. This endpoint (POST /v1/databases/{id}/query) was REMOVED in Notion API version 2025-09-03; verified live that it returns HTTP 400 invalid_request_url on 2026-03-11. It is therefore deliberately pinned to Notion-Version 2022-06-28, which still works. REPLACEMENT: use queryDataSource (POST /v1/data_sources/{data_source_id}/query), which runs on 2026-03-11 and also supports filter, sorts and filter_properties. Get a data_source_id from getDatabase's data_sources[] or from a relation property. Known limitation of this legacy action: a database with MULTIPLE data sources returns "Databases with multiple data sources are not supported in this API version" - those must use queryDataSource. |
| Query Database Rows (Paged) | `queryDatabaseRows` | List rows (pages) of a Notion database, newest first, with cursor pagination: POST /v1/databases/{databaseId}/query. Only page_size and start_cursor are sent in the body, so extra inputs never leak into the request. Returns results plus next_cursor / has_more. |
| Retrieve Data Source | `retrieveDataSource` | Retrieves a data source object — including its properties schema (columns) — for a provided data source ID. Use this to inspect the structure of a data source before querying its rows. |
| Search | `search` | Search all pages and databases in a Notion workspace by title. Deliberately pinned to Notion-Version 2022-06-28. Verified live: on 2026-03-11 an unfiltered search still returns 200, but this action's documented filter.value "database" is REJECTED with HTTP 400 validation_error ("should be `page` or `data_source`"), and the response envelope changes from type "page_or_database" to "page_or_data_source". Keeping 2022-06-28 preserves both the filter input and the documented response for existing callers. To search data sources on a current API version, a new action using filter.value "data_source" would be needed. |
| Send File Upload | `sendFileUpload` | Transmit file bytes for a pending file upload (POST file_uploads/{file_upload_id}/send). Uses multipart/form-data with a 'file' part (raw binary, provided via the fastn FileRef input field 'file') and, for multi_part uploads, an optional 'part_number' (1-1000). EXECUTOR LIMITATION: the fastn executor's multipart/form-data + FileRef support may not transmit binary bodies correctly; if execution fails on the multipart body (not on auth/routing), classify as BLOCKED (executor multipart limitation) rather than fail. Returns the updated file_upload object. |
| Update Block | `updateBlock` | Update the content of a Notion block |
| Update Data Source | `updateDataSource` | Updates a Notion data source object — its properties schema, title, icon, trash status, or parent database. Returns the updated data source object. |
| Update Database | `updateDatabase` | LEGACY - rename a Notion database. Deliberately pinned to Notion-Version 2022-06-28. Verified live: this title-only PATCH is still ACCEPTED on 2026-03-11 (HTTP 200), but the response there omits the properties (column schema) object this action's outputContract declares, so the version is held back to keep the documented response correct. Note the body template sends only the title, so the "archived" input is currently ignored (archiving is not actually applied). To change a database's COLUMN SCHEMA on current API versions use updateDataSource, whose properties map edits the data source that owns the columns; a database itself no longer carries a schema. |
| Update Database Row (Plain Text) | `updateDatabaseRowPlainText` | Partially update a Notion database row (page) by pageId. titleValue, status and priority are optional objects written under titleProperty / statusProperty / priorityProperty ({title:[{text:{content}}]} / {status:{name}} / {select:{name}}); unset ones are omitted and keep their value. Returns the updated page. |
| Update Database Row Title | `updateDatabaseRowTitle` | Set the title of a Notion database row (page) from plain text. titleProperty is the database's title column (usually Name), title is the new text. Returns the updated page. To set several columns or rich values, use Update Database Row (Plain Text). |
| Update Page | `updatePage` | Update a Notion page's properties or archive it. Deliberately pinned to Notion-Version 2022-06-28. Verified live: on 2026-03-11 this action's REQUIRED "archived" input is rejected with HTTP 400 validation_error ("body.archived should be not present") because Notion renamed that field to "in_trash" on newer versions. Keeping 2022-06-28 preserves the existing input contract. Moving this action forward would require accepting in_trash instead, which is a breaking input change and so needs a new action version rather than an edit. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Comment Created | `comment.created` | A comment was created on a page or block. |
| Comment Deleted | `comment.deleted` | A comment was deleted. |
| Comment Updated | `comment.updated` | A comment was edited. |
| Database Content Updated | `database.content_updated` | Rows/content within a database were updated. |
| Database Created | `database.created` | A database was created. |
| Database Deleted | `database.deleted` | A database was moved to trash (deleted). |
| Database Moved | `database.moved` | A database was moved to a different parent. |
| Database Schema Updated | `database.schema_updated` | The property schema of a database was changed. |
| Database Undeleted | `database.undeleted` | A database was restored from trash. |
| Page Content Updated | `page.content_updated` | The block content of a page was updated. |
| Page Created | `page.created` | A page was created in the workspace. |
| Page Deleted | `page.deleted` | A page was moved to trash (deleted). |
| Page Locked | `page.locked` | A page was locked. |
| Page Moved | `page.moved` | A page was moved to a different parent. |
| Page Properties Updated | `page.properties_updated` | One or more properties of a page were updated. |
| Page Undeleted | `page.undeleted` | A page was restored from trash. |
| Page Unlocked | `page.unlocked` | A page was unlocked. |
