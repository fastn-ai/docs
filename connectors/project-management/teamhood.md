---
description: "Teamhood public API v1 — work management: items (tasks/issues/projects), item types and fields, comments, attachments, time logs, resource allocations,…"
hidden: true
---

# Teamhood

<img src="../../.gitbook/assets/connectors/lg/teamhood.png" alt="Teamhood logo">

Teamhood public API v1 — work management: items (tasks/issues/projects), item types and fields, comments, attachments, time logs, resource allocations, availability and capacity profiles, teams, users, roles and the item changelog.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [teamhood.com](https://teamhood.com) |
| **Authentication** | API key |
| **Slug** | `teamhood` |

## Use it

Add Teamhood from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.teamhood.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Allocation | `createAllocation` | Create a resource allocation for a user or team. 'distribution' must be { segments: [{ fromDay, toDay, hoursPerDay }], totalHours? } with at least one segment — fromDay/toDay are zero-based day offsets. IMPORTANT: a 'reserved' allocation carries its own startDate/endDate; a 'shaped' allocation does NOT — it reads the linked item's dates, and sending startDate/endDate with kind=shaped is rejected 422 "A shaped allocation carries no dates of its own; it reads the item's." Returns 201. |
| Create Availability Entry | `createAvailability` | Create an availability entry overriding a principal's working hours for a date range (hoursPerDay, e.g. 0 for leave or 4 for a part-time week). Returns 201 with the created entry. |
| Create Capacity Profile | `createCapacityProfile` | Create a capacity profile setting a principal's standard weekly hours from an effective date. IMPORTANT: weeklyHours keys must be Luxon weekday numbers as strings, "1" (Monday) to "7" (Sunday) — day names are rejected with a 422. Returns 201. |
| Create Comment | `createComment` | Post a comment on an item, optionally as a reply to another comment and with attachments already uploaded. Supply contentText (Teamhood converts it to rich text) or an explicit contentRichText document. Returns 201. |
| Create Custom Field | `createField` | Create a custom field and attach it to one or more item types. 'type' is the field data type (text, number, date, select, people, boolean, formula, rollup, autoincrement, trackedTime...). 'config' carries type-specific settings such as select options, multiple, defaultValue or formula. Returns 201. |
| Create Item | `createItem` | Create a Teamhood item (task, issue, project...). 'type' is the item type key and is required. 'fields' is a free-form map of field key to value (e.g. status, assignees, start, finish, estimate). Returns 201 with the created item. |
| Create Item Type | `createItemType` | Create a new item type (a work-item class such as 'epic' or 'bug') with its key, colour, permitted child types and default open/container view modes. Returns 201. |
| Create Team | `createTeam` | Create a team, optionally nested under an existing team via parentId, with a display colour. Returns 201 with the created team. |
| Deactivate User | `deactivateUser` | Deactivate an account user by id, freeing their seat. WARNING: this removes a person's access. Deactivating the account owner, or the only remaining administrator, can lock the whole account out with no API route back. Never point it at the identity your API key authenticates as. Returns 204 No Content. |
| Delete Allocation | `deleteAllocation` | Delete a resource allocation by id. Returns 204 No Content. |
| Delete Attachment | `deleteAttachment` | Delete an attachment and its stored file by id. Returns 204 No Content. |
| Delete Availability Entry | `deleteAvailability` | Delete an availability entry by id, restoring the principal's default working hours for that range. Returns 204 No Content. |
| Delete Capacity Profile | `deleteCapacityProfile` | Delete a capacity profile by id. Returns 204 No Content. |
| Delete Comment | `deleteComment` | Delete a comment by id, along with its replies. Returns 204 No Content. |
| Delete Custom Field | `deleteField` | Delete a field definition by id. Set orphanValues=true to keep already-stored values on items instead of removing them. Returns 204 No Content. |
| Delete Item | `deleteItem` | Permanently delete a Teamhood item by id. Child items and the item's comments, attachments and time logs go with it. Returns 204 No Content. |
| Delete Item Type | `deleteItemType` | Delete an item type by id. Set deleteItems=true to also delete every item of that type — leave it false to fail safe when items still exist. Returns 204 No Content. |
| Delete Team | `deleteTeam` | Delete a team by id. Members are not deleted, but lose this team membership and any team-level allocations. Returns 204 No Content. |
| Delete Time Log | `deleteTimeLog` | Delete a time-log entry by id, removing its hours from the item's tracked time. Returns 204 No Content. |
| Download Attachment Content | `downloadAttachmentContent` | Download the raw bytes of an attachment by id. The response is application/octet-stream, so text files come back as text and binary files are not usefully representable in JSON. |
| Get Allocation | `getAllocation` | Fetch one resource allocation by id, including its principal, item, date range and hour distribution. |
| Get Attachment | `getAttachment` | Fetch one attachment's metadata by id: file name, MIME type, size in bytes, isImage flag, owning item and author. |
| Get Availability Entry | `getAvailability` | Fetch one availability entry by id, with its principal, date range and hours per day. |
| Get Capacity Profile | `getCapacityProfile` | Fetch one capacity profile by id, with its principal, effective-from date and weekly hours map. |
| Get Comment | `getComment` | Fetch one comment by id, with its text, rich text, author, completion state and attachment ids. |
| Get Custom Field | `getField` | Fetch one field definition by id, with its key, title, data type, applicable item types and configuration. |
| Get Item | `getItem` | Fetch a single Teamhood item by its id, including its type, description, watchers, dependencies and field values. |
| Get Item Type | `getItemType` | Fetch one item type by its id (not its key), with its key, name, colour, child-type rules and view modes. |
| Get Team | `getTeam` | Fetch one team by id (name, parentId, colour, createdAt). |
| Get Time Log | `getTimeLog` | Fetch one time-log entry by id, with its item, field, date, duration and description. |
| Get User | `getUser` | Fetch one account user by id (id, name, email). |
| Invite User To Account | `inviteUser` | Invite a person to the Teamhood account by email, with a role and optional team memberships. WARNING: this SENDS A REAL INVITATION EMAIL to the address supplied and consumes a seat — only call it for an address you control. The 201 response also contains the raw invite token, which grants account access: treat the response as a secret and do not log it. Use List Pending Invites / Revoke Pending Invite to manage the result. |
| List Allocations | `listAllocations` | List resource allocations (planned work assigned to a person or team over a date range), filterable by principalId, itemId, kind (shaped/reserved), firmness (firm/tentative) and a from/to window. Cursor-paginated. |
| List Attachments | `listAttachments` | List attachment metadata for exactly one of an item or a comment. Supply itemId OR commentId, not both and not neither — Teamhood answers 422 "Provide exactly one of itemId or commentId." otherwise. |
| List Availability Entries | `listAvailability` | List availability entries (per-principal overrides of working hours for a date range, e.g. part-time weeks or leave), filterable by principalId and a from/to window. Cursor-paginated. |
| List Capacity Profiles | `listCapacityProfiles` | List capacity profiles — each principal's standard weekly working hours from an effective date onward. Filterable by principalId and a from/to window. Cursor-paginated. |
| List Comments | `listComments` | List all comments on one item, including replies (parentCommentId), completion state and attachment ids. itemId is required. |
| List Custom Fields | `listFields` | List every field defined in the account (built-in and custom): id, key, title, data type, which item types it applies to, readOnly flag and per-type configuration such as select options. |
| List Fields For Item Type | `listTypeFields` | List the field descriptors available on one item type, keyed by type key (e.g. 'issue'). Each descriptor gives the field key, title, data type, readOnly flag and select options — use it to learn what keys the 'fields' map of Create Item / Update Item accepts. |
| List Item Changelog | `listItemChangelog` | List the audit/changelog entries for one item: who changed what and when, with the event type, source and payload. Use 'since' plus the returned nextCursor to poll for new activity — this is the only change-feed Teamhood's public API offers. |
| List Item Types | `listItemTypes` | List the account's item types (project, task, issue and any custom ones): id, key, name, colour, which child types they support and their default open/view modes. The 'key' is what Create Item's 'type' expects. |
| List Items | `listItems` | List and filter Teamhood items (tasks, issues, projects). Supports filtering by type key, explicit ids, parentId, title, watchers, created/updated windows, ordering, and cursor pagination. Returns { items: [...], nextCursor }. |
| List Pending Invites | `listPendingInvites` | List invitations that have been sent but not yet accepted: email, role, teams, creation and expiry time. |
| List Roles | `listRoles` | List the account's roles (id, name, isSystemRole). The role id is what the Invite User action needs. |
| List Teams | `listTeams` | List the account's teams (id, name, parentId for nested teams, colour, createdAt). A team id can also be used as a principalId for allocations and capacity. |
| List Time Logs | `listTimeLogs` | List the time logged against one item. itemId is required; fieldId narrows it to a single trackedTime field. Returns an array of entries with date, durationSeconds, description and author. |
| List Users | `listUsers` | List the active users of the Teamhood account (id, name, email). The user id is the principalId used by allocations, availability and capacity. |
| Log Time On Item | `logTime` | Log time against an item's trackedTime field. fieldId must be a field of type 'trackedTime' (see List Fields). The date may not be in the future — Teamhood answers 422 "Time cannot be logged against a future date." Returns 201 with the created entry. |
| Rename Attachment | `renameAttachment` | Rename an attachment. Only the displayed fileName changes; the stored file is untouched. Returns 200 with the updated metadata. |
| Replace Attachment File | `replaceAttachmentContent` | Replace the stored file of an existing attachment, keeping its id (multipart/form-data). TEXT content only — fileContent is sent verbatim, so raw binary formats cannot be expressed. Returns 200 with the refreshed attachment metadata. |
| Revoke Pending Invite | `revokePendingInvite` | Revoke an invitation that has not yet been accepted, by its invite id from List Pending Invites. The invite link stops working. Returns 204 No Content. |
| Update Allocation | `updateAllocation` | Partially update a resource allocation: firmness, start/end dates, hour distribution or label. The principal and item of an allocation cannot be changed. |
| Update Availability Entry | `updateAvailability` | Partially update an availability entry: start date, end date, hours per day or label. |
| Update Capacity Profile | `updateCapacityProfile` | Partially update a capacity profile's effective-from date or weekly hours. weeklyHours keys must be "1".."7" (Monday..Sunday). |
| Update Comment | `updateComment` | Edit a comment's text or rich text, change its attachment ids, or mark it complete/incomplete with isCompleted. |
| Update Custom Field | `updateField` | Partially update a field definition: title, data type, colour, ordering rank, key, the item types it applies to, or its type-specific config. |
| Update Item | `updateItem` | Partially update a Teamhood item: title, description, parent, watchers, dependencies, or any field values. Only the supplied keys change. |
| Update Item Type | `updateItemType` | Partially update an item type: name, key, colour, ordering rank, permitted child types or default open/container view modes. |
| Update Team | `updateTeam` | Partially update a team's name, parent team or colour. |
| Update Time Log | `updateTimeLog` | Partially update a time-log entry's date, duration in seconds or description. |
| Upload Attachment To Item | `uploadAttachment` | Upload a TEXT file as an attachment on an item (multipart/form-data). fileContent is sent verbatim as the file body, so this carries text formats (txt, csv, json, md, svg, ASCII PPM) only — raw binary such as PNG, ZIP or docx cannot be expressed here. Returns 201 with the attachment metadata. |
