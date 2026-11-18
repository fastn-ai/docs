---
description: "Mixmax sales engagement platform — sequences, recipients, contacts, contact groups, snippets, meetings/summaries, file requests, and more via the Mixmax REST…"
hidden: true
---

# Mixmax

<img src="../../.gitbook/assets/connectors/mixmax.png" alt="Mixmax logo" width="64">

Mixmax sales engagement platform — sequences, recipients, contacts, contact groups, snippets, meetings/summaries, file requests, and more via the Mixmax REST API v1.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [mixmax.com](https://mixmax.com) |
| **Authentication** | API key |
| **Slug** | `mixmax` |

## Use it

Add Mixmax from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mixmax.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contact Group Member | `addContactGroupMember` | Add a contact to a contact group (POST /contactgroups/:id/contacts). Provide email or contactId; supports bulk via contacts array. |
| Add Sequence Recipients | `addSequenceRecipients` | Add one or more recipients to a sequence (POST /sequences/:id/recipients). Provide a recipients array of {email, variables, scheduledAt}. |
| Create Contact | `createContact` | Create a contact (POST /contacts). email is unique; a duplicate email merges. Returns 204 no content. |
| Create Contact Group | `createContactGroup` | Create a contact group (POST /contactgroups). Provide a name; optionally contacts. |
| Create Contact Note | `createContactNote` | Add a note to a contact (POST /contacts/:id/notes). Provide text. |
| Create Rule | `createRule` | Create a Mixmax automation rule record (POST /rules). Provide a name. |
| Create Snippet Tag | `createSnippetTag` | Create a snippet tag (POST /snippettags). Provide a name. |
| Delete Contact | `deleteContact` | Delete a contact (DELETE /contacts/:id). |
| Delete Contact Group | `deleteContactGroup` | Delete a contact group (DELETE /contactgroups/:id). |
| Delete Contact Note | `deleteContactNote` | Delete a contact note (DELETE /contacts/:id/notes/:noteId). Only the creator can delete. |

<details>

<summary>See 33 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Rule | `deleteRule` | Delete an automation rule (DELETE /rules/:id). Returns 204. |
| Delete Snippet Tag | `deleteSnippetTag` | Delete a snippet tag (DELETE /snippettags/:id). Returns 204. |
| Get Contact | `getContact` | Retrieve a contact by _id (GET /contacts/:id). |
| Get Contact Group | `getContactGroup` | Retrieve a specific contact group (GET /contactgroups/:id). |
| Get Current User | `getCurrentUser` | Retrieve the authenticated Mixmax user (GET /users/me). Returns the user's _id. |
| Get Live Feed | `getLiveFeed` | Get your Mixmax activity/insights live feed with engagement stats (GET /livefeed). |
| Get Meeting Transcript | `getMeetingTranscript` | Retrieve the full transcript for a meeting by its summary id (GET /meetings/transcripts/:id). |
| Get Meeting Type | `getMeetingType` | Retrieve a single availability / scheduling link type by id (GET /meetingtypes/:id). |
| Get Message | `getMessage` | Retrieve a single tracked message by its id (GET /messages/:id). |
| Get Rule | `getRule` | Retrieve a single automation rule by id (GET /rules/:id). |
| Get Snippet | `getSnippet` | Retrieve a single snippet by id (GET /snippets/:id). |
| Get Snippet Tag | `getSnippetTag` | Retrieve a single snippet tag by id (GET /snippettags/:id). |
| List Contact Group Members | `listContactGroupMembers` | Return membership for a contact group (GET /contactgroups/:id/contacts). |
| List Contact Groups | `listContactGroups` | List contact groups you can access (GET /contactgroups). |
| List Contact Notes | `listContactNotes` | List notes for a contact (GET /contacts/:id/notes). Pass expand=userId to include owner name/email. |
| List Contacts | `listContacts` | List your Mixmax contacts (GET /contacts). Cursor paginated. |
| List File Requests | `listFileRequests` | List file requests you have sent (GET /filerequests). |
| List Meeting Types | `listMeetingTypes` | List your availability / scheduling link types (GET /meetingtypes). Cursor paginated. |
| List Messages | `listMessages` | List tracked messages you have sent with Mixmax (GET /messages). Cursor paginated via next/previous. |
| List Rules | `listRules` | List your Mixmax automation rules (GET /rules). |
| List Sequence Recipients | `listSequenceRecipients` | List activated recipients of a sequence (GET /sequences/:id/recipients). Offset paginated; returns an array. |
| List Sequences | `listSequences` | List sequences you have access to (GET /sequences). Filter by name/folder; pass expand=stages for stage detail. |
| List Snippet Tags | `listSnippetTags` | List snippet tags (GET /snippettags). Cursor paginated. |
| List Snippets | `listSnippets` | List your saved snippets/templates (GET /snippets). Cursor paginated. |
| List Teams | `listTeams` | List teams you belong to (GET /teams). |
| Query Contacts | `queryContacts` | Search contacts across Mixmax, Google directory, and Salesforce (GET /contacts/query). |
| Remove Contact Group Member | `removeContactGroupMember` | Remove a contact from a contact group (DELETE /contactgroups/:id/contacts/:contactId). |
| Search Meeting Summaries | `searchMeetingSummaries` | Search meeting (Copilot) summaries (GET /meetings/summaries/search). Requires the mixmaxApi feature. |
| Update Contact | `updateContact` | Update a contact (PATCH /contacts/:id). Returns 200 with empty body. |
| Update Contact Group | `updateContactGroup` | Edit a contact group (PATCH /contactgroups/:id). |
| Update Contact Note | `updateContactNote` | Edit a contact note (PATCH /contacts/:id/notes/:noteId). Only the creator can edit. |
| Update Rule | `updateRule` | Update an automation rule (PATCH /rules/:id). Provide fields to change (e.g. name). |
| Update Snippet Tag | `updateSnippetTag` | Rename a snippet tag (PATCH /snippettags/:id). |

</details>
