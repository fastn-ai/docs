---
description: "Attio CRM API v2 (base https://api.attio.com/v2)."
---

# Attio

Attio CRM API v2 (base https://api.attio.com/v2). Manage objects and attributes, records (query/create/assert/get/update/delete + attribute values), lists and list entries, workspace members, notes, tasks, comments and threads, and webhooks. Auth: Bearer API access token. Responses wrap payloads in a 'data' envelope.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [attio.com](https://attio.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Actions** | 91 |
| **Events** | 34 |
| **Slug** | `attio` |

## Use it

Add Attio from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.attio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Unsubscribed Emails | `addUnsubscribedEmails` | Add email addresses to the sequence unsubscribe list; active sequence runs for them are exited (POST /v2/sequences/unsubscribed_emails). Max 1000 per call. Requires sequence_unsubscribe:read-write. |
| Assert List Entry | `assertListEntry` | Upsert a list entry by its parent record (create if absent, update if present). Maps to PUT /v2/lists/{list}/entries. Required scope: list_entry:read-write, list_configuration:read. |
| Assert Record | `assertRecord` | Create or update a record matched on a unique attribute (PUT /v2/objects/{object}/records). |
| Create Activity | `createActivity` | Create a custom activity type (POST /v2/activities). The schema it extends is fixed after creation. Alpha endpoint. Requires activity_configuration:read-write. |
| Create Activity Record | `createActivityRecord` | Create an activity record, e.g. one phone call (POST /v2/activities/{activity}/records). Alpha endpoint. Requires activity_record:read-write. |
| Create Attribute | `createAttribute` | Creates a new attribute on an object or a list. Attributes cannot be deleted through the API; archive them with Update Attribute instead. |
| Create Call Recording | `createCallRecording` | Attach a call recording (video URL and/or transcript) to a meeting (POST /v2/meetings/{meeting_id}/call_recordings). Rate limited to 1 request per second. Always supply a transcript. Beta. Requires call_recording:read-write. |
| Create Comment | `createComment` | Creates a comment. Supply either a thread ID to reply to an existing thread, or a record or list entry to open a new thread on it. |
| Create File Entry | `createFileEntry` | Create a native folder, or a connected file/folder entry from Dropbox, Box, Google Drive or OneDrive, on a record (POST /v2/files). Body is NOT wrapped in data. Beta. Requires file:read-write. |
| Create List | `createList` | Creates a new list. A list must be given either full workspace access or at least one workspace member with full access. Lists cannot be deleted through the API. |
| Create List Entry | `createListEntry` | Adds a record to a list as a new list entry. Fails on conflicts with unique entry attributes; multiple entries for the same parent record are allowed. |
| Create Meeting | `createMeeting` | Create a meeting with participants and linked records (POST /v2/meetings). Beta. Requires meeting:read-write. |
| Create Note | `createNote` | Creates a note on a record. The note body is supplied as plaintext or markdown and is attached to the parent record. |
| Create Object | `createObject` | Create a new custom object in the workspace. Maps to POST /v2/objects. Required scope: object_configuration:read-write. |
| Create Record | `createRecord` | Create a record (POST /v2/objects/{object}/records). |
| Create Select Option | `createSelectOption` | Add a select option to a select attribute on an object or list (POST /v2/{target}/{identifier}/attributes/{attribute}/options). |
| Create Status | `createStatus` | Add a status to a status attribute on an object or list (POST /v2/{target}/{identifier}/attributes/{attribute}/statuses). |
| Create Task | `createTask` | Create a task (POST /v2/tasks). |
| Create Webhook | `createWebhook` | Create a webhook with event subscriptions (POST /v2/webhooks). Used by the webhook config. |
| Delete Activity | `deleteActivity` | Delete an activity type and all of its records (DELETE /v2/activities/{activity}). Irreversible. Alpha endpoint. |
| Delete Activity Record | `deleteActivityRecord` | Delete one activity record (DELETE /v2/activities/{activity}/records/{record_id}). Alpha endpoint. |
| Delete Call Recording | `deleteCallRecording` | Delete a call recording and all associated data (DELETE /v2/meetings/{meeting_id}/call_recordings/{call_recording_id}). Returns 204. Beta. |
| Delete Comment | `deleteComment` | Delete a comment (DELETE /v2/comments/{commentId}). |
| Delete File | `deleteFile` | Delete a file or folder; deleting a folder deletes all descendants (DELETE /v2/files/{file_id}). Beta. Requires file:read-write. |
| Delete List Entry | `deleteListEntry` | Remove a record from a list (DELETE /v2/lists/{list}/entries/{entryId}). |
| Delete Note | `deleteNote` | Delete a note (DELETE /v2/notes/{noteId}). |
| Delete Object | `deleteObject` | Delete a custom object and all of its records (DELETE /v2/objects/{object}). System objects (people, companies, users, deals, workspaces) cannot be deleted. Irreversible. |
| Delete Record | `deleteRecord` | Delete a record (DELETE /v2/objects/{object}/records/{recordId}). |
| Delete Task | `deleteTask` | Delete a task (DELETE /v2/tasks/{taskId}). |
| Delete Webhook | `deleteWebhook` | Delete a webhook (DELETE /v2/webhooks/{webhookId}). |
| Get Activity | `getActivity` | Get one activity type by activity_id or slug (GET /v2/activities/{activity}). Alpha endpoint. |
| Get Activity Record | `getActivityRecord` | Get one activity record by record_id (GET /v2/activities/{activity}/records/{record_id}). Alpha endpoint. |
| Get Attribute | `getAttribute` | Retrieve a single attribute on an object or list. Maps to GET /v2/{target}/{identifier}/attributes/{attribute}. Required scope: object_configuration:read (objects) or list_configuration:read (lists). |
| Get Call Recording | `getCallRecording` | Get a call recording including its transcript and a short-lived video URL (GET /v2/meetings/{meeting_id}/call_recordings/{call_recording_id}). Beta. |
| Get Call Transcript | `getCallTranscript` | Deprecated by Attio: get a call recording's transcript segments (GET /v2/meetings/{meeting_id}/call_recordings/{call_recording_id}/transcript). Prefer Get Call Recording, which includes the transcript. |
| Get Comment | `getComment` | Get a comment by id (GET /v2/comments/{commentId}). |
| Get File | `getFile` | Get one file, folder or connected entry by ID (GET /v2/files/{file_id}). Beta. Requires file:read. |
| Get List | `getList` | Get a list by id or slug (GET /v2/lists/{list}). |
| Get List Entry | `getListEntry` | Get a list entry by id (GET /v2/lists/{list}/entries/{entryId}). |
| Get Meeting | `getMeeting` | Get one meeting by ID (GET /v2/meetings/{meeting_id}). Beta. Requires meeting:read. |
| Get Note | `getNote` | Get a note by id (GET /v2/notes/{noteId}). |
| Get Object | `getObject` | Get an object by id or api_slug (GET /v2/objects/{object}). |
| Get Record | `getRecord` | Get a record by id (GET /v2/objects/{object}/records/{recordId}). |
| Get Task | `getTask` | Get a task by id (GET /v2/tasks/{taskId}). |
| Get Thread | `getThread` | Retrieve a single comment thread by ID, including all its comments. Maps to GET /v2/threads/{thread_id}. Required scope: comment:read. |
| Get Webhook | `getWebhook` | Gets a single webhook and its event subscriptions by ID. |
| Get Workspace Member | `getWorkspaceMember` | Get a workspace member by id (GET /v2/workspace_members/{memberId}). |
| Identify Self | `identifySelf` | Identify the current access token: returns active status, granted scopes, workspace identity, and the authorizing member. Maps to GET /v2/self. Required scope: none (token introspection). |
| List Activities | `listActivities` | List system-defined and custom activity types in the workspace (GET /v2/activities). Alpha endpoint. Requires activity_configuration:read. |
| List Attributes | `listAttributes` | List attributes on an object or a list (GET /v2/{target}/{identifier}/attributes). Returned in UI sort order. |
| List Call Recordings | `listCallRecordings` | List call recordings for a meeting (GET /v2/meetings/{meeting_id}/call_recordings). Beta. Requires call_recording:read. |
| List Emails | `listEmails` | List email metadata from connected mailboxes; content is never returned (GET /v2/emails). At least one of linked_object+linked_record_ids, participants, or domain is required. Beta. Requires email:read. |
| List Files | `listFiles` | List native files, connected files and folders on a record (GET /v2/files). Beta. Requires file:read. |
| List List Entry Attribute Values | `listListEntryAttributeValues` | List all values (optionally historic) for one attribute on a list entry (GET /v2/lists/{list}/entries/{entry_id}/attributes/{attribute}/values). |
| List List Views | `listListViews` | Lists the saved views defined for a list, ordered by view ID. |
| List Lists | `listLists` | List all lists (GET /v2/lists). |
| List Meetings | `listMeetings` | List meetings in the workspace, optionally filtered by linked record, participants or time window (GET /v2/meetings). Beta. Requires meeting:read. |
| List Notes | `listNotes` | List notes (GET /v2/notes). |
| List Object Views | `listObjectViews` | Lists the saved views defined for an object, ordered by view ID. |
| List Objects | `listObjects` | List all objects in the workspace (GET /v2/objects). |
| List Record Attribute Values | `listRecordAttributeValues` | List the historic and current values of a single attribute on a record. Maps to GET /v2/objects/{object}/records/{record_id}/attributes/{attribute}/values. Required scope: record_permission:read, object_configuration:read. |
| List Record Entries | `listRecordEntries` | Lists every list entry, across all lists, whose parent is the given record. Returns entry metadata only; use Get List Entry for values. |
| List Select Options | `listSelectOptions` | Lists the select options available on a select attribute of an object or list. |
| List Statuses | `listStatuses` | Lists the statuses available on a status attribute of an object or list. |
| List Tasks | `listTasks` | List tasks (GET /v2/tasks). |
| List Threads | `listThreads` | List comment threads, optionally filtered to a specific record (record_id + object) or list entry (entry_id + list). Maps to GET /v2/threads. Required scope: comment:read. |
| List Webhooks | `listWebhooks` | List webhooks (GET /v2/webhooks). |
| List Workspace Members | `listWorkspaceMembers` | List workspace members (GET /v2/workspace_members). |
| Merge Records | `mergeRecords` | Merges two records of the same object. Where both hold a value for an attribute, the primary record's value wins. The secondary record is consumed by the merge, so this cannot be undone. |
| Overwrite Activity Record | `overwriteActivityRecord` | Update an activity record, overwriting multiselect values (PUT /v2/activities/{activity}/records/{record_id}). Alpha endpoint. |
| Overwrite List Entry | `overwriteListEntry` | Update a list entry, overwriting multiselect values with the supplied ones (PUT /v2/lists/{list}/entries/{entry_id}). Use Update List Entry to append multiselect values instead. |
| Overwrite Record | `overwriteRecord` | Updates a record by ID, overwriting multiselect attribute values with the supplied values. Use Update Record to append multiselect values instead. |
| Query Activity Records | `queryActivityRecords` | List activity records with optional filter and sort (POST /v2/activities/{activity}/records/query). Alpha endpoint. Requires activity_record:read. |
| Query List Entries | `queryListEntries` | Query entries in a list (POST /v2/lists/{list}/entries/query). |
| Query Records | `queryRecords` | Query records of an object with filters and sorts (POST /v2/objects/{object}/records/query). |
| Query SQL | `querySql` | Query records and lists with SQL (POST /v2/sql). Enterprise plan only. Beta. Requires record_permission:read and object_configuration:read. |
| Search Records | `searchRecords` | Fuzzy-searches records across one or more objects, matching names, domains, email addresses, phone numbers and social handles. |
| Update Activity | `updateActivity` | Rename an activity type (PATCH /v2/activities/{activity}). extends cannot be changed. Alpha endpoint. |
| Update Activity Record | `updateActivityRecord` | Update an activity record, appending multiselect values (PATCH /v2/activities/{activity}/records/{record_id}). Use Overwrite Activity Record to replace multiselect values. Alpha endpoint. |
| Update Attribute | `updateAttribute` | Updates a single attribute on an object or list. Only the fields supplied inside Data are changed. |
| Update List | `updateList` | Updates a list's name, API slug or access permissions. Only the fields supplied inside Data are changed. A list must keep either full workspace access or at least one member with full access. |
| Update List Entry | `updateListEntry` | Update list-specific attribute values on an entry (PATCH /v2/lists/{list}/entries/{entryId}). |
| Update Note | `updateNote` | Updates an existing note's title or content. Only the fields supplied inside Data are changed; supplying content replaces the whole note body. |
| Update Object | `updateObject` | Updates a custom object's API slug, singular noun or plural noun. Only the fields supplied inside Data are changed. |
| Update Record | `updateRecord` | Update a record, appending multiselect values (PATCH /v2/objects/{object}/records/{recordId}). |
| Update Select Option | `updateSelectOption` | Rename or archive a select option (PATCH /v2/{target}/{identifier}/attributes/{attribute}/options/{option}). Options cannot be deleted, only archived. |
| Update Status | `updateStatus` | Rename, archive or reconfigure a status on a status attribute (PATCH /v2/{target}/{identifier}/attributes/{attribute}/statuses/{status}). |
| Update Task | `updateTask` | Updates an existing task's deadline, completion state, linked records or assignees. Only the fields supplied inside Data are changed; task content cannot be edited. |
| Update Webhook | `updateWebhook` | Update a webhook's target URL and/or subscriptions (PATCH /v2/webhooks/{webhook_id}). Each target URL + event type + filter combination must be unique in the workspace (409 otherwise). |
| Write List Entry Attribute Values | `writeListEntryAttributeValues` | Replace the entire value history of one attribute on a list entry (PUT /v2/lists/{list}/entries/{entry_id}/attributes/{attribute}/values). Every existing value is destroyed. Meant for migrating historic data. |
| Write Record Attribute Values | `writeRecordAttributeValues` | Replace the entire value history of one attribute on a record (PUT /v2/objects/{object}/records/{record_id}/attributes/{attribute}/values). Every existing value is destroyed and the supplied values with active_from/active_until are written. Meant for migrating historic data. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Activity Attribute Created | `activity-attribute.created` | An attribute was added to an activity type. |
| Activity Attribute Updated | `activity-attribute.updated` | An activity attribute definition changed. |
| Activity Created | `activity.created` | A custom activity type was created. |
| Activity Deleted | `activity.deleted` | A custom activity type was deleted. |
| Activity Record Created | `activity-record.created` | An activity record was created. |
| Activity Record Deleted | `activity-record.deleted` | An activity record was deleted. |
| Activity Updated | `activity.updated` | A custom activity type changed. |
| Call Recording Created | `call-recording.created` | A call recording was added to a meeting. |
| Comment Created | `comment.created` | A comment was created. |
| Comment Deleted | `comment.deleted` | A comment was deleted. |
| Comment Resolved | `comment.resolved` | A comment thread was resolved. |
| Comment Unresolved | `comment.unresolved` | A comment thread was reopened. |
| List Attribute Created | `list-attribute.created` | An attribute was added to a list. |
| List Attribute Updated | `list-attribute.updated` | A list attribute definition changed. |
| List Created | `list.created` | A list was created. |
| List Deleted | `list.deleted` | A list was deleted. |
| List Entry Created | `list-entry.created` | A record was added to a list. |
| List Entry Deleted | `list-entry.deleted` | A record was removed from a list. |
| List Entry Updated | `list-entry.updated` | A list entry attribute value changed. |
| List Updated | `list.updated` | A list's settings changed. |
| Note Content Updated | `note-content.updated` | A note's body changed. |
| Note Created | `note.created` | A note was created. |
| Note Deleted | `note.deleted` | A note was deleted. |
| Note Updated | `note.updated` | A note's title or metadata changed. |
| Object Attribute Created | `object-attribute.created` | An attribute was added to an object. |
| Object Attribute Updated | `object-attribute.updated` | An object attribute definition changed. |
| Record Created | `record.created` | A record was created. |
| Record Deleted | `record.deleted` | A record was deleted. |
| Record Merged | `record.merged` | Two records were merged; id names the surviving record. |
| Record Updated | `record.updated` | A record attribute value changed. |
| Task Created | `task.created` | A task was created. |
| Task Deleted | `task.deleted` | A task was deleted. |
| Task Updated | `task.updated` | A task changed. |
| Workspace Member Created | `workspace-member.created` | A member joined the workspace. |
