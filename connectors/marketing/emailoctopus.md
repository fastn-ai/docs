---
description: "EmailOctopus is an email marketing and newsletter sending platform."
hidden: true
---

# EmailOctopus

<img src="../../.gitbook/assets/connectors/lg/emailoctopus.png" alt="EmailOctopus logo">

EmailOctopus is an email marketing and newsletter sending platform. This connector covers the EmailOctopus v2 REST API: list and contact management (including custom fields), campaign retrieval and reporting, and automation triggering.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [emailoctopus.com](https://emailoctopus.com) |
| **Authentication** | Bearer token |
| **Slug** | `emailoctopus` |

## Use it

Add EmailOctopus from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.emailoctopus.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Update Contacts</td><td><code>batchUpdateContacts</code></td><td>Updates up to 500 existing contacts on a list in a single call. Each item must include the contact's id; email_address, fields, tags and status are optional and update the targeted contact. Returns per-item success and error results.</td></tr><tr><td>Create Contact</td><td><code>createContact</code></td><td>Adds a new contact to a list, optionally with custom field values, tags, and a subscription status.</td></tr><tr><td>Create Field</td><td><code>createField</code></td><td>Creates a new custom contact field on a list. Use type text, number, or date for simple fields, or choice_single/choice_multiple with a set of choices for dropdown-style fields.</td></tr><tr><td>Create List</td><td><code>createList</code></td><td>Creates a new contact list (audience) in the EmailOctopus account.</td></tr><tr><td>Create or Update Contact</td><td><code>upsertContact</code></td><td>Creates a contact on a list if one does not already exist for the given email address, or updates it if it does (upsert).</td></tr><tr><td>Create Tag</td><td><code>createTag</code></td><td>Creates a new contact tag on a list. Returns a conflict error if a tag with the same name already exists on that list.</td></tr><tr><td>Delete Contact</td><td><code>deleteContact</code></td><td>Permanently deletes a contact from a list.</td></tr><tr><td>Delete Field</td><td><code>deleteField</code></td><td>Permanently deletes a custom contact field from a list.</td></tr><tr><td>Delete List</td><td><code>deleteList</code></td><td>Permanently deletes a contact list and all of its contacts.</td></tr><tr><td>Delete Tag</td><td><code>deleteTag</code></td><td>Permanently deletes a contact tag from a list, removing it from every contact that carries it.</td></tr></tbody></table>

<details>

<summary>View 15 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Campaign</td><td><code>getCampaign</code></td><td>Retrieves a single email campaign by its ID.</td></tr><tr><td>Get Campaign Contact Reports</td><td><code>getCampaignContactReports</code></td><td>Retrieves the list of contacts matching a specific engagement status (e.g. opened, clicked, bounced) for a campaign, paginated.</td></tr><tr><td>Get Campaign Links Report</td><td><code>getCampaignLinksReport</code></td><td>Retrieves the click counts for each link contained in a campaign's content.</td></tr><tr><td>Get Campaign Summary Report</td><td><code>getCampaignSummaryReport</code></td><td>Retrieves aggregate engagement statistics (sent, opened, clicked, bounced, complained, unsubscribed) for a campaign.</td></tr><tr><td>Get Contact</td><td><code>getContact</code></td><td>Retrieves a single contact from a list by its ID (a UUID, or the MD5 hash of the contact's lowercased email address).</td></tr><tr><td>Get List</td><td><code>getList</code></td><td>Retrieves a single contact list by its ID.</td></tr><tr><td>List Campaigns</td><td><code>listCampaigns</code></td><td>Retrieves all email campaigns in the account, paginated.</td></tr><tr><td>List Contacts</td><td><code>listContacts</code></td><td>Retrieves the contacts belonging to a list, with optional filtering by tag, status, and creation/update date ranges.</td></tr><tr><td>List Lists</td><td><code>listLists</code></td><td>Retrieves all contact lists (audiences) in the EmailOctopus account, paginated.</td></tr><tr><td>List Tags</td><td><code>listTags</code></td><td>Retrieves all contact tags defined on a list, paginated.</td></tr><tr><td>Start Automation For Contact</td><td><code>startAutomation</code></td><td>Queues a contact to start a specific automation (drip sequence) built in the EmailOctopus dashboard.</td></tr><tr><td>Update Contact</td><td><code>updateContact</code></td><td>Updates an existing contact's email address, custom fields, tags, or subscription status.</td></tr><tr><td>Update Field</td><td><code>updateField</code></td><td>Updates an existing custom contact field's label, tag, type, or fallback value.</td></tr><tr><td>Update List</td><td><code>updateList</code></td><td>Updates the name of an existing contact list.</td></tr><tr><td>Update Tag</td><td><code>updateTag</code></td><td>Renames an existing contact tag on a list. The rename applies to every contact currently carrying the tag.</td></tr></tbody></table>

</details>
