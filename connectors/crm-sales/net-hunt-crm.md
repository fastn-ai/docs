---
description: "NetHunt CRM is a CRM that runs inside Gmail and organises data into folders (Contacts, Companies, Deals, Tasks and custom folders)."
---

# NetHunt CRM

NetHunt CRM is a CRM that runs inside Gmail and organises data into folders (Contacts, Companies, Deals, Tasks and custom folders). This connector covers the full NetHunt public REST API v2: list, get, create and update folders; add and update folder fields; create, get, update and delete records; list recently updated records for incremental sync; full-text search and structured filtering with sorting and cursor pagination; read a record's activity timeline and timeline item content; and log comments and calls on a record. Authentication uses a NetHunt API token. NetHunt does not offer outgoing webhooks through its API, so changes are detected by polling the List Updated Records action.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [nethunt.com](https://nethunt.com) |
| **Authentication** | Bearer token |
| **Actions** | 17 |
| **Events** | 0 |
| **Slug** | `netHuntCrm` |

## Use it

Add NetHunt CRM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.netHuntCrm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Folder Field | `addFolderField` | Adds a new field to a NetHunt folder. NetHunt's API has no endpoint to delete a field, so an added field can only be removed from the NetHunt interface. Returns the full updated folder including all fields. |
| Add Record Comment | `addRecordComment` | Adds a comment to a NetHunt record's timeline and returns it as a comment timeline event. To mention a workspace member, write their email right after an @ at the start of a word (for example @jane.doe@acme.com followed by a space); mentioned members are notified. |
| Create Folder | `createFolder` | Creates a new folder in the NetHunt workspace, optionally with an initial set of fields. NetHunt's API has no endpoint to delete a folder, so a created folder can only be removed from the NetHunt interface. Returns the created folder. |
| Create Record | `createRecord` | Creates a record (for example a contact, company or deal) in a NetHunt folder. Field values are passed as a map keyed by field ID, or by field label when Field Keys is 'label'; use Get Folder to discover the folder's fields. Returns the created record. |
| Delete Record | `deleteRecord` | Moves a record in a NetHunt folder to the trash, where it can still be recovered from the NetHunt interface. Returns no content on success. |
| Filter Records | `filterRecords` | Queries records in a NetHunt folder with an optional structured filter, optional sort and cursor pagination, returning up to Limit matches plus the total match count on the first page. Filter keys are field IDs (or labels) and special fields name, created, updated and active_tasks_count; values are bare values for equality or operator objects such as {"_gte": 100}, {"_in": "acme"} or {"_exists": true}, combinable with _and and _or groups. Omit Filter to page through all records. |
| Get Folder | `getFolder` | Retrieves a single NetHunt folder by ID, including its full field schema (field IDs, names, types, value types, presets and options). Use the field IDs returned here as keys when creating, updating or filtering records. |
| Get Record | `getRecord` | Retrieves a single record from a NetHunt folder by ID, with field values keyed by field ID or, when Field Keys is 'label', by field label. |
| Get Timeline Item Content | `getTimelineItemContent` | Retrieves the full content of one timeline item on a NetHunt record: message bodies, participants and attachments for email and campaign-email items, or the transcript for messenger chats. Other event types return an empty messages list because they are already complete in the timeline. |
| List Folders | `listFolders` | Lists all folders (such as Contacts, Companies, Deals, Tasks and custom folders) accessible to the authenticated NetHunt user. Field definitions are not included; use Get Folder to read a folder's full field schema. |
| List Record Timeline | `listRecordTimeline` | Lists the activity timeline of a NetHunt record, newest first: emails, campaign emails, calls, comments, chats, calendar events, files and record created/updated changes. Supports filtering by event type and time range, and cursor pagination via Next Cursor. Note: NetHunt currently returns an upstream error when Event Types is exactly 'call'; to read logged calls, omit Event Types and select events whose type is 'call'. |
| List Updated Records | `listUpdatedRecords` | Lists records in a NetHunt folder that were created or updated since a point in time, oldest first. Designed for incremental polling and sync: pass the returned Next Since token back in Since to read the rest of the window. Without Since, the last 24 hours are returned. |
| Log Record Call | `logRecordCall` | Logs a call that happened outside NetHunt on a record's timeline, with notes, time and duration, and returns it as a call timeline event. Calls made through NetHunt telephony integrations appear automatically and do not need to be logged. |
| Search Records | `searchRecords` | Runs a full-text search across record field values in a NetHunt folder and returns up to Limit relevance-ranked records. There is no pagination; use Filter Records for structured queries with sorting and cursor pagination. |
| Update Folder | `updateFolder` | Updates the name and/or description of a NetHunt folder. Only the properties you pass are changed. Returns the updated folder. |
| Update Folder Field | `updateFolderField` | Updates the name, description, required flag, presets, group or non-structural options of a field in a NetHunt folder. The field type cannot be changed, and protected fields (the built-in Name field and role-bound Tasks fields) cannot be updated. Returns the full updated folder. |
| Update Record | `updateRecord` | Partially updates a record in a NetHunt folder: only the keys present in Fields change, a null value clears a field, and omitted fields are left untouched. The record name cannot be changed and read-only fields are rejected. Returns the updated record. |
