---
description: "noCRM.io lead management and sales CRM."
hidden: true
---

# noCRM.io

<img src="../../.gitbook/assets/connectors/lg/nocrmio.png" alt="noCRM.io logo">

noCRM.io lead management and sales CRM. Manage leads, prospecting lists and prospects, pipelines and steps, users, teams, client folders, categories, tags, custom fields, activities, comments, attachments, and webhooks via the noCRM.io API v2.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [nocrm.io](https://nocrm.io) |
| **Authentication** | API key |
| **Slug** | `nocrmio` |

## Use it

Add noCRM.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nocrmio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Webhook | `activateWebhook` | Enable a webhook. |
| Add Prospecting List Comment | `addProspectingListComment` | Add a comment to a prospecting list. |
| Add Prospects | `addProspects` | Add one or more prospects to a prospecting list. |
| Add Team User | `addTeamUser` | Add a user to a team. |
| Assign Lead | `assignLead` | Assign a lead to a user. |
| Assign Prospecting List | `assignProspectingList` | Assign a prospecting list to a user. |
| Bulk Delete Leads | `bulkDeleteLeads` | Delete multiple leads by id array. |
| Convert Prospect To Lead | `convertProspectToLead` | Convert a prospect into a lead. |
| Create Category | `createCategory` | Create a tag category. |
| Create Client Folder | `createClient` | Create a client folder. |

<details>

<summary>See 54 more actions</summary>

* **Create Custom Field** `createField`: Create a custom field.
* **Create Lead** `createLead`: Create a new lead. title and description are required.
* **Create Lead Comment** `createLeadComment`: Add a comment to a lead.
* **Create Predefined Tag** `createPredefinedTag`: Create a predefined tag within a category.
* **Create Prospecting List** `createProspectingList`: Create a prospecting list.
* **Create Team** `createTeam`: Create a team.
* **Create User** `createUser`: Create a new user in the account.
* **Create Webhook** `createWebhook`: Create a webhook subscription for one or more events.
* **Delete Client Folder** `deleteClient`: Delete a client folder.
* **Delete Lead** `deleteLead`: Delete a single lead by id.
* **Delete Lead Attachment** `deleteLeadAttachment`: Delete an attachment from a lead.
* **Delete Lead Comment** `deleteLeadComment`: Delete a comment from a lead.
* **Delete Prospect** `deleteProspect`: Delete a prospect from a prospecting list.
* **Delete Team** `deleteTeam`: Delete a team.
* **Disable User** `disableUser`: Disable a user account.
* **Disable Webhook** `disableWebhook`: Disable a webhook.
* **Duplicate Lead** `duplicateLead`: Duplicate an existing lead.
* **Get Client Folder** `getClient`: Retrieve a client folder by id.
* **Get Lead** `getLead`: Retrieve a lead by id.
* **Get Lead Attachment** `getLeadAttachment`: Retrieve a single lead attachment's details.
* **Get Lead Business Card** `getLeadBusinessCard`: Retrieve the business card (contact) info of a lead.
* **Get Prospecting List** `getProspectingList`: Retrieve a prospecting list (with prospects).
* **Get Step** `getStep`: Retrieve a single pipeline step by id or name.
* **Get Team** `getTeam`: Retrieve a team by id.
* **Get User** `getUser`: Retrieve a user by id.
* **Get Webhook Event** `getWebhookEvent`: Retrieve details of a webhook event type.
* **List Activities** `listActivities`: List activity types.
* **List Called Prospects** `listCalledProspects`: List prospects that have been called.
* **List Categories** `listCategories`: List tag categories, optionally including their tags.
* **List Client Folders** `listClients`: List client folders.
* **List Custom Fields** `listFields`: List custom fields (lead or client).
* **List Lead Action Histories** `listLeadActionHistories`: List the action history of a lead.
* **List Lead Attachments** `listLeadAttachments`: List attachments on a lead.
* **List Lead Comments** `listLeadComments`: List comments on a lead.
* **List Lead Duplicates** `listLeadDuplicates`: List potential duplicate leads for a lead.
* **List Leads** `listLeads`: List leads with optional filters (status, step, user, tags, dates, pagination).
* **List Pipelines** `listPipelines`: List all pipelines.
* **List Predefined Tags** `listPredefinedTags`: List all predefined tags.
* **List Prospecting Lists** `listProspectingLists`: List prospecting lists.
* **List Steps** `listSteps`: List all pipeline steps.
* **List Teams** `listTeams`: List all teams.
* **List Unassigned Leads** `listUnassignedLeads`: List leads not assigned to any user.
* **List Users** `listUsers`: List account users.
* **List Webhook Events** `listWebhookEvents`: List available webhook event types.
* **List Webhooks** `listWebhooks`: List configured webhooks.
* **Ping** `ping`: Verify API authentication. Returns account/user info for the API key.
* **Remove Team User** `removeTeamUser`: Remove a user from a team.
* **Send User Activation** `sendUserActivation`: Send (or resend) the activation email to a user so they can set up their account.
* **Update Client Folder** `updateClient`: Update a client folder.
* **Update Lead** `updateLead`: Update a lead. Send only the fields to change (partial update).
* **Update Lead Comment** `updateLeadComment`: Update a comment on a lead.
* **Update Prospect** `updateProspect`: Update a prospect in a prospecting list.
* **Update Prospect Fields** `updateProspectFields`: Update the custom fields of a prospect.
* **Update Team** `updateTeam`: Update a team.

</details>
