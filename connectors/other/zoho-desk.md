---
description: "Zoho Desk is Zoho's context-aware customer support / helpdesk ticketing platform."
hidden: true
---

# Zoho Desk

<img src="../../.gitbook/assets/connectors/lg/zoho-desk.png" alt="Zoho Desk logo">

Zoho Desk is Zoho's context-aware customer support / helpdesk ticketing platform. This connector provides access to Desk's REST API v1: tickets, threads/comments, contacts, accounts, agents, departments, teams, tasks, calls, custom views, business hours, holiday lists, and webhooks (notifications).

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [zoho.com](https://zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zohoDesk` |

## Use it

Add Zoho Desk from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoDesk.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Ticket Comment | `addTicketComment` | Adds an internal (public or private) comment to a ticket. |
| Create Account | `createAccount` | Creates a new customer account (company). |
| Create Business Hours | `createBusinessHours` | Creates a new business hours schedule. |
| Create Contact | `createContact` | Creates a new customer contact. |
| Create Department | `createDepartment` | Creates a new helpdesk department. |
| Create Holiday List | `createHolidayList` | Creates a new holiday list. |
| Create Product | `createProduct` | Creates a new product. |
| Create Team | `createTeam` | Creates a new agent team. |
| Create Ticket | `createTicket` | Creates a new support ticket. |
| Create Ticket Task | `createTicketTask` | Creates a new task on a ticket. |

<details>

<summary>See 64 more actions</summary>

* **Create Webhook** `createWebhook`: Creates a new outbound webhook that fires on a ticket/module event.
* **Delete Account** `deleteAccount`: Deletes a customer account.
* **Delete Business Hours** `deleteBusinessHours`: Deletes a business hours schedule.
* **Delete Call** `deleteCall`: Deletes a logged call. KNOWN DEFECT, NOT YET FIXED (2026-09-03): Zoho rejects the current body with 422 {"errorCode":"UNPROCESSABLE_ENTITY","message":"An extra parameter 'ids' is found"}. Every working sibling moveToTrash in this connector uses a module-prefixed key (tickets {"ticketIds":[...]} -&gt; 204, contacts {"contactIds":[...]}, accounts {"accountIds":[...]}), so the correct key is almost certainly {"callIds":["&lt;callId&gt;"]}. NOT APPLIED because it cannot be proven: CALLS are license-blocked on the portal available for testing (FREE_2019), so no call can be created and no corrected request can be re-executed to a 2xx. Apply and verify on a portal with the Calls module enabled.
* **Delete Contact** `deleteContact`: Deletes a contact.
* **Delete Product** `deleteProduct`: Deletes a product.
* **Delete Task** `deleteTask`: Deletes a task. KNOWN DEFECT, NOT YET FIXED (2026-09-03): Zoho rejects the current body with 422 {"errorCode":"UNPROCESSABLE_ENTITY","message":"An extra parameter 'activityIds' is found"}. Every working sibling moveToTrash in this connector uses a module-prefixed key (tickets {"ticketIds":[...]} -&gt; 204, contacts {"contactIds":[...]}, accounts {"accountIds":[...]}), so the correct key is almost certainly {"taskIds":["&lt;taskId&gt;"]}. NOT APPLIED because it cannot be proven: TASKS are license-blocked on the portal available for testing (FREE_2019), so no task can be created and no corrected request can be re-executed to a 2xx. Apply and verify on a portal with the Tasks module enabled.
* **Delete Team** `deleteTeam`: Deletes an agent team. KNOWN DEFECT, NOT YET FIXED (2026-09-03): DELETE https://desk.zoho.com/api/v1/teams/{teamId} returns 405 {"errorCode":"METHOD_NOT_ALLOWED","message":"This HTTP method is not allowed on this URL."} - Zoho does not expose team deletion as a DELETE on the team resource. Third-party integration references map Zoho Desk's documented "Delete team" operation (https://desk.zoho.com/DeskAPIDocument#Teams#Teams_Deleteteam) to the sub-path /teams/{teamId}/delete, matching Zoho's usual action-sub-path convention (see moveToTrash elsewhere in this connector). NOT APPLIED because it cannot be proven: TEAMS are license-blocked on the portal available for testing - Create Team and Update Team both return 403 LICENSE_ACCESS_LIMITED - so no team can be created and no corrected request can be re-executed to a 2xx. Confirm the exact verb and path against the live Zoho Desk API document, then apply and verify on a licensed portal.
* **Delete Ticket** `deleteTicket`: Moves a ticket to trash (deletes it).
* **Delete Ticket Attachment** `deleteTicketAttachment`: Deletes a file attachment from a ticket.
* **Delete Ticket Comment** `deleteTicketComment`: Deletes a comment from a ticket.
* **Delete Webhook** `deleteWebhook`: Deletes an outbound webhook.
* **Get Account** `getAccount`: Gets a single customer account by id.
* **Get Agent** `getAgent`: Gets a single agent by id.
* **Get Business Hours** `getBusinessHours`: Gets a single business hours schedule by id.
* **Get Call** `getCall`: Gets a single logged call by id.
* **Get Contact** `getContact`: Gets a single contact by id.
* **Get Custom View** `getCustomView`: Gets a single custom view's definition by id.
* **Get Department** `getDepartment`: Gets a single department by id.
* **Get Holiday List** `getHolidayList`: Gets a single holiday list by id.
* **Get Organization** `getOrganization`: Gets details of a specific Zoho Desk organization (portal) by id.
* **Get Product** `getProduct`: Gets a single product by id.
* **Get Task** `getTask`: Gets a single task by id.
* **Get Team** `getTeam`: Gets a single agent team by id.
* **Get Ticket** `getTicket`: Gets details of a single ticket by id.
* **Get Ticket Count** `getTicketCount`: Gets the count of tickets matching an optional view/status filter.
* **Get Ticket History** `getTicketHistory`: Gets the audit history/activity feed of a ticket (field changes, status changes, etc).
* **Get Ticket Thread** `getTicketThread`: Gets the full content of a single ticket thread (email conversation entry).
* **Get Webhook** `getWebhook`: Gets a single configured webhook by id.
* **Invite Agent** `inviteAgent`: Invites a new agent to the helpdesk portal.
* **List Accounts** `listAccounts`: Lists customer accounts (companies).
* **List Agents** `listAgents`: Lists support agents in the portal.
* **List Business Hours** `listBusinessHours`: Lists configured business hours schedules used for SLA calculations.
* **List Calls** `listCalls`: Lists logged phone calls.
* **List Contacts** `listContacts`: Lists customer contacts.
* **List Custom Views** `listCustomViews`: Lists custom ticket views/filters defined in the module.
* **List Departments** `listDepartments`: Lists helpdesk departments.
* **List Holiday Lists** `listHolidayLists`: Lists configured holiday lists used for SLA / business hours calculations.
* **List Organizations** `listOrganizations`: Lists the Zoho Desk organizations (portals) the authenticated user has access to. Use this first to obtain the orgId required by every other action.
* **List Products** `listProducts`: Lists products/service offerings tickets can be associated with.
* **List Roles** `listRoles`: Lists agent roles available in the portal (used as roleId when inviting/updating agents).
* **List Teams** `listTeams`: Lists agent teams.
* **List Ticket Attachments** `listTicketAttachments`: Lists files attached to a ticket.
* **List Ticket Comments** `listTicketComments`: Lists internal comments on a ticket.
* **List Ticket Tasks** `listTicketTasks`: Lists tasks associated with a ticket.
* **List Ticket Threads** `listTicketThreads`: Lists the email/conversation threads of a ticket.
* **List Tickets** `listTickets`: Lists tickets in the helpdesk, with optional filters (status, department, view, sort).
* **List Tickets by Custom View** `listTicketsByCustomView`: Lists tickets matching a saved custom view/filter.
* **List Webhooks** `listWebhooks`: Lists configured outbound webhooks (Setup &gt; Automation &gt; Webhooks).
* **Log Call** `createCall`: Logs a new phone call.
* **Search Contacts** `searchContacts`: Searches contacts by name, email, or phone.
* **Search Tickets** `searchTickets`: Searches tickets by subject, email, phone, or ticket number.
* **Send Reply on Ticket** `sendTicketReply`: Sends an email reply on a ticket, creating a new outbound thread.
* **Update Account** `updateAccount`: Updates fields on an existing account.
* **Update Agent** `updateAgent`: Updates fields on an existing agent (e.g. role, associated departments, status).
* **Update Call** `updateCall`: Updates fields on an existing logged call.
* **Update Contact** `updateContact`: Updates fields on an existing contact.
* **Update Department** `updateDepartment`: Updates fields on an existing department.
* **Update Product** `updateProduct`: Updates fields on an existing product.
* **Update Task** `updateTask`: Updates fields on an existing task.
* **Update Team** `updateTeam`: Updates an existing agent team.
* **Update Ticket** `updateTicket`: Updates fields on an existing ticket (status, priority, subject, assignee, etc).
* **Update Ticket Comment** `updateTicketComment`: Updates the content of an existing ticket comment.
* **Update Webhook** `updateWebhook`: Updates an existing outbound webhook.

</details>
