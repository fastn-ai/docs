---
description: "GoDial is a telecalling CRM and auto dialer."
hidden: true
---

# GoDial

<img src="../../.gitbook/assets/connectors/godial.png" alt="GoDial logo" width="64">

GoDial is a telecalling CRM and auto dialer. This connector wraps the GoDial CRM External API (v2) to manage teams, accounts (members), calling lists, contacts, dispositions, tasks and call logs.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [godial.cc](https://godial.cc) |
| **Authentication** | Credentials you enter |
| **Slug** | `godial` |

## Use it

Add GoDial from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.godial.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Assign List To Account | `assignList` | Assigns a GoDial calling list to an account (member) so the member can call its contacts. |
| Create Account | `createAccount` | Creates a new account (member) in your GoDial company with login credentials, a role and team memberships. |
| Create Contact | `createContact` | Adds a new contact to a GoDial calling list, optionally assigning it to an agent directly or by round robin. Custom fields are stored only when a field with that name is defined in your GoDial company. |
| Create List | `createList` | Creates a new calling list inside a GoDial team. |
| Create Task | `createTask` | Creates a new GoDial task assigned to an account (member), optionally linked to a contact and with a reminder. |
| Create Team | `createTeam` | Creates a new team in your GoDial company. |
| Delete Account | `deleteAccount` | Deletes an account (member) from your GoDial company by its ID. Returns the number of records removed. |
| Delete Contact | `deleteContact` | Deletes a GoDial contact by its ID. Returns the number of records removed. |
| Delete Contact By Phone | `deleteContactByPhone` | Deletes a GoDial contact matched by its phone number within a specific calling list. |
| Delete List | `deleteList` | Deletes a calling list from your GoDial company by its ID. Returns the number of records removed. |

<details>

<summary>See 21 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Task | `deleteTask` | Deletes a GoDial task by its ID. Returns the number of records removed. |
| Delete Team | `deleteTeam` | Deletes a team from your GoDial company by its ID. Returns the number of records removed. |
| Detach List From Account | `detachList` | Removes a GoDial calling list assignment from an account (member). |
| Dispose Contact | `disposeContact` | Records a call, SMS or email disposition for a GoDial contact, optionally scheduling a callback. The disposition must be an uppercase value configured in your GoDial company. |
| Get Account | `getAccount` | Retrieves a single GoDial account (member) by its ID, including its assigned lists and teams. GoDial returns an error with the message "Account is not valid" when no account matches the ID. |
| Get Contact | `getContact` | Retrieves a single GoDial contact by its ID. GoDial returns HTTP 204 with an empty body when no contact matches the ID. |
| Get List | `getList` | Retrieves a single GoDial calling list by its ID. GoDial returns HTTP 204 with an empty body when no list matches the ID. |
| Get Task | `getTask` | Retrieves a single GoDial task by its ID. GoDial returns HTTP 204 with an empty body when no task matches the ID. |
| Get Team | `getTeam` | Retrieves a single GoDial team by its ID. GoDial returns an error with the message "Team is not valid" when no team matches the ID. |
| List Accounts | `listAccounts` | Lists all accounts (members) in your GoDial company, including their role, team memberships and permissions. |
| List Call Logs | `listCallLogs` | Lists GoDial call logs filtered by lists, agents, dispositions and a date range. GoDial requires all four filters; use ["allLists"] and ["All Dispos"] to include everything. |
| List Contacts In List | `listContacts` | Lists all contacts that belong to a GoDial calling list. |
| List Lists | `listLists` | Lists all calling lists in your GoDial company. Lists hold contacts and are assigned to accounts. |
| List Tasks | `listTasks` | Lists all tasks in your GoDial company. |
| List Teams | `listTeams` | Lists all teams in your GoDial company. Every account belongs to at least one team. |
| Move Contact To List | `changeContactList` | Moves a GoDial contact from its current calling list to another list. |
| Update Account | `updateAccount` | Updates an existing GoDial account (member). GoDial requires the name, email, role and team IDs on every update, and any access flag you omit is reset to false; username and password cannot be changed through this action. |
| Update Contact | `updateContact` | Updates an existing GoDial contact. Only the fields you pass are changed. |
| Update List | `updateList` | Updates the name, description or team of an existing GoDial calling list. Only the fields you pass are changed. |
| Update Task | `updateTask` | Updates a GoDial task, for example renaming it or marking it done. The task name is required on every update. Setting done to true completes the task; GoDial does not reopen a completed task when done is false. |
| Update Team | `updateTeam` | Updates the name or description of an existing GoDial team. Only the fields you pass are changed. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| After Call | `afterCall` | Fires after a call is completed in GoDial. GoDial has no webhook registration API (its External API token is rejected on every non-external route with "Api Manager is only able to access external apis"), so a GoDial manager must register the fastn webhook URL manually: GoDial dashboard &gt; Integrations &gt; Web Hook &gt; enable the webhook, paste the fastn webhook URL into Target URL, optionally turn on Custom Headers and add a header key and value, switch on the After Call event, then click Save. GoDial allows one webhook URL per company and does not publish a payload schema or an event-type field, so the payload below is the recommended field set, not a vendor contract; if both After Call and Contact Update are enabled on the same URL, route on the payload content in your workflow. |
| Contact Update | `contactUpdate` | Fires after a contact is updated in GoDial. GoDial has no webhook registration API, so a GoDial manager must register the fastn webhook URL manually: GoDial dashboard &gt; Integrations &gt; Web Hook &gt; enable the webhook, paste the fastn webhook URL into Target URL, optionally turn on Custom Headers and add a header key and value, switch on the Contact Update event, then click Save. GoDial allows one webhook URL per company and does not publish a payload schema or an event-type field, so the payload below is the recommended field set (mirroring the contact object returned by the External API), not a vendor contract. |
