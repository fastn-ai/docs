---
description: "EmailOctopus is an email marketing and newsletter sending platform."
---

# EmailOctopus

EmailOctopus is an email marketing and newsletter sending platform. This connector covers the EmailOctopus v2 REST API: list and contact management (including custom fields), campaign retrieval and reporting, and automation triggering.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [emailoctopus.com](https://emailoctopus.com) |
| **Authentication** | Bearer token |
| **Actions** | 25 |
| **Events** | 0 |
| **Slug** | `emailoctopus` |

## Use it

Add EmailOctopus from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.emailoctopus.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Update Contacts | `batchUpdateContacts` | Updates up to 500 existing contacts on a list in a single call. Each item must include the contact's id; email_address, fields, tags and status are optional and update the targeted contact. Returns per-item success and error results. |
| Create Contact | `createContact` | Adds a new contact to a list, optionally with custom field values, tags, and a subscription status. |
| Create Field | `createField` | Creates a new custom contact field on a list. Use type text, number, or date for simple fields, or choice_single/choice_multiple with a set of choices for dropdown-style fields. |
| Create List | `createList` | Creates a new contact list (audience) in the EmailOctopus account. |
| Create or Update Contact | `upsertContact` | Creates a contact on a list if one does not already exist for the given email address, or updates it if it does (upsert). |
| Create Tag | `createTag` | Creates a new contact tag on a list. Returns a conflict error if a tag with the same name already exists on that list. |
| Delete Contact | `deleteContact` | Permanently deletes a contact from a list. |
| Delete Field | `deleteField` | Permanently deletes a custom contact field from a list. |
| Delete List | `deleteList` | Permanently deletes a contact list and all of its contacts. |
| Delete Tag | `deleteTag` | Permanently deletes a contact tag from a list, removing it from every contact that carries it. |
| Get Campaign | `getCampaign` | Retrieves a single email campaign by its ID. |
| Get Campaign Contact Reports | `getCampaignContactReports` | Retrieves the list of contacts matching a specific engagement status (e.g. opened, clicked, bounced) for a campaign, paginated. |
| Get Campaign Links Report | `getCampaignLinksReport` | Retrieves the click counts for each link contained in a campaign's content. |
| Get Campaign Summary Report | `getCampaignSummaryReport` | Retrieves aggregate engagement statistics (sent, opened, clicked, bounced, complained, unsubscribed) for a campaign. |
| Get Contact | `getContact` | Retrieves a single contact from a list by its ID (a UUID, or the MD5 hash of the contact's lowercased email address). |
| Get List | `getList` | Retrieves a single contact list by its ID. |
| List Campaigns | `listCampaigns` | Retrieves all email campaigns in the account, paginated. |
| List Contacts | `listContacts` | Retrieves the contacts belonging to a list, with optional filtering by tag, status, and creation/update date ranges. |
| List Lists | `listLists` | Retrieves all contact lists (audiences) in the EmailOctopus account, paginated. |
| List Tags | `listTags` | Retrieves all contact tags defined on a list, paginated. |
| Start Automation For Contact | `startAutomation` | Queues a contact to start a specific automation (drip sequence) built in the EmailOctopus dashboard. |
| Update Contact | `updateContact` | Updates an existing contact's email address, custom fields, tags, or subscription status. |
| Update Field | `updateField` | Updates an existing custom contact field's label, tag, type, or fallback value. |
| Update List | `updateList` | Updates the name of an existing contact list. |
| Update Tag | `updateTag` | Renames an existing contact tag on a list. The rename applies to every contact currently carrying the tag. |
