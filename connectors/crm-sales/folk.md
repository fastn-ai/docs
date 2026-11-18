---
description: "Folk CRM REST API v1 — manage people, companies, groups, deals (custom objects), notes, reminders, interactions, users, and webhooks."
hidden: true
---

# Folk

Folk CRM REST API v1 — manage people, companies, groups, deals (custom objects), notes, reminders, interactions, users, and webhooks. Base https://api.folk.app.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [folk.app](https://folk.app) |
| **Authentication** | Bearer token |
| **Actions** | 57 |
| **Events** | 0 |
| **Slug** | `folk` |

## Use it

Add Folk from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.folk.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Group Member | `addGroupMember` | Add a workspace user to a folk group with a given role. Relevant for private groups, where membership is explicit. |
| Create Company | `createCompany` | Create a company. Name is required and unique across the workspace (existing returned if duplicate). |
| Create Deal | `createDeal` | Create a deal (custom object) within a group. name required. |
| Create Group | `createGroup` | Create a new group in the folk workspace. A default All people table view is created for the group automatically. Note that folk exposes no endpoint to delete a group, so a group created here can only be removed from the folk web app. |
| Create Group Custom Field | `createGroupCustomField` | Create a custom field on a folk group for a given entity type. Supply options only for singleSelect and multipleSelect fields. Note that folk exposes no endpoint to delete a group custom field, so a field created here can only be removed from the folk web app. |
| Create Interaction | `createInteraction` | Log an interaction on a person or company. entity, dateTime, title, content, type all required. |
| Create Note | `createNote` | Create a note linked to a person, company, or deal. entity.id, visibility, content required. |
| Create Person | `createPerson` | Create a person. All fields optional; provide at least one name field. |
| Create Reminder | `createReminder` | Create a reminder on a person/company/deal. entity, name, recurrenceRule, visibility required; assignedUsers required for public reminders. |
| Create Task | `createTask` | Create a new task in the folk workspace and attach it to a person, company or deal. Tasks replace the deprecated reminders endpoints. |
| Create Webhook | `createWebhook` | Create a webhook that listens to folk workspace events. The target URL must be publicly reachable over HTTP or HTTPS. Verified on 2026-09-12 that folk answers this endpoint with HTTP 500 "Failed to create webhook." on the ops@fastn.ai workspace for every event combination and target URL, reproduced identically with a direct request outside fastn; the wiring is correct and the failure is server-side at folk. |
| Delete Company | `deleteCompany` | Delete a company by ID. |
| Delete Deal | `deleteDeal` | Delete a deal (custom object) by ID within a group. |
| Delete Interaction | `deleteInteraction` | Delete a logged folk interaction. Imported interactions cannot be deleted. This folk endpoint is in open beta. |
| Delete Note | `deleteNote` | Delete a note by ID. |
| Delete Person | `deletePerson` | Delete a person by ID. |
| Delete Reminder | `deleteReminder` | Delete a reminder by ID. |
| Delete Task | `deleteTask` | Permanently delete a task from the folk workspace by its identifier. |
| Delete Webhook | `deleteWebhook` | Delete a webhook by ID. |
| Get Company | `getCompany` | Retrieve a single company by ID (com_...). |
| Get Current User | `getCurrentUser` | Get the user associated with the API key. |
| Get Deal | `getDeal` | Retrieve a single deal (custom object) by ID within a group. |
| Get Group Custom Field | `getGroupCustomField` | Retrieve the full definition of one custom field on a folk group, including its select options. |
| Get Interaction | `getInteraction` | Retrieve a single past or upcoming interaction in folk. The full email or calendar body is included when privacy rules allow it. This folk endpoint is in open beta. |
| Get Note | `getNote` | Retrieve a single note by ID. |
| Get Person | `getPerson` | Retrieve a single person by ID (per_...). |
| Get Reminder | `getReminder` | Retrieve a single reminder by ID (rmd_...). |
| Get Task | `getTask` | Retrieve a single task from the folk workspace by its identifier. |
| Get User | `getUser` | Retrieve a single user by ID (usr_...). |
| Get Webhook | `getWebhook` | Retrieve a single webhook by ID (wbk_...). |
| List Companies | `listCompanies` | List companies in the workspace. Paginated. |
| List Deals | `listDeals` | List deals (custom objects) within a group. objectType is the deal custom object name from List group custom fields. |
| List Group Custom Fields | `listGroupCustomFields` | List custom fields defined on a group for a given entity type (person, company, or custom object name). |
| List Group Members | `listGroupMembers` | List the workspace users who are members of a folk group. For a public group every workspace user is a member. |
| List Groups | `listGroups` | List groups in the workspace. Paginated. |
| List Notes | `listNotes` | List notes. Optionally filter by entity via entity.id. |
| List Past Interactions | `listPastInteractions` | List the past interactions linked to a person, company or object in folk. This folk endpoint is in open beta and its response shape may change. |
| List People | `listPeople` | List people in the workspace. Paginated via cursor/nextLink. |
| List Reminders | `listReminders` | List reminders. Paginated. |
| List Tasks | `listTasks` | Retrieve a paginated list of tasks in the folk workspace, optionally restricted to the tasks assigned to the current user. Tasks replace the deprecated reminders endpoints. |
| List Upcoming Interactions | `listUpcomingInteractions` | List the upcoming interactions linked to a person, company or object in folk. This folk endpoint is in open beta and its response shape may change. |
| List Users | `listUsers` | List workspace users. Paginated. |
| List Webhooks | `listWebhooks` | List webhooks. Paginated. |
| Mark Task As Done | `markTaskAsDone` | Mark an existing folk task as done, recording the completion timestamp. |
| Mark Task As To Do | `markTaskAsTodo` | Reopen a completed folk task by marking it as to do, clearing its completion timestamp. |
| Remove Group Member | `removeGroupMember` | Remove a workspace user from a folk group. |
| Update Company | `updateCompany` | Update a company by ID. List fields replace existing values. |
| Update Deal | `updateDeal` | Update a deal (custom object) by ID within a group. List fields replace existing values. |
| Update Group | `updateGroup` | Update a folk group's name and/or visibility. Only the fields supplied are changed. |
| Update Group Custom Field | `updateGroupCustomField` | Rename a folk group custom field, change its numeric formatting, or add and remove select options. Removing an option deletes all data stored against it. |
| Update Group Member | `updateGroupMember` | Change the role a workspace user holds in a folk group. |
| Update Interaction | `updateInteraction` | Partially update a logged folk interaction's title, content, date-time or activity type. Imported interactions cannot be updated. This folk endpoint is in open beta. |
| Update Note | `updateNote` | Update a note by ID (content and/or visibility). |
| Update Person | `updatePerson` | Update a person by ID. List fields replace existing values. |
| Update Reminder | `updateReminder` | Update a reminder by ID. |
| Update Task | `updateTask` | Update an existing task in the folk workspace. Only the fields supplied are changed; omit a field to leave it untouched. |
| Update Webhook | `updateWebhook` | Update a webhook by ID (name, targetUrl, subscribedEvents, status). |
