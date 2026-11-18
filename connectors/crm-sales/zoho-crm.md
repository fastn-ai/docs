---
description: "Zoho CRM is a cloud-based CRM platform."
hidden: true
---

# Zoho CRM

<img src="../../.gitbook/assets/connectors/lg/zoho-crm.png" alt="Zoho CRM logo">

Zoho CRM is a cloud-based CRM platform. Manage leads, contacts, accounts, deals, tasks, events, calls, and notes via the Zoho CRM REST API v8.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [zoho.com](https://zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `zohoCrm` |

## Use it

Add Zoho CRM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoCrm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Account</td><td><code>createAccount</code></td><td>Create an Account record. Account_Name is required; all other fields optional and omitted from the request when not supplied.</td></tr><tr><td>Create Contact</td><td><code>createContact</code></td><td>Create a Contact record. Last_Name is required; all other fields optional and omitted when not supplied.</td></tr><tr><td>Create Deal</td><td><code>createDeal</code></td><td>Create a Deal record. Deal_Name and Stage are required; all other fields optional and omitted when not supplied.</td></tr><tr><td>Create Lead</td><td><code>createLead</code></td><td>Create a Lead record. Last_Name and Company are required; all other fields optional and omitted when not supplied.</td></tr><tr><td>Create Note</td><td><code>createNote</code></td><td>Create a Note record. Pass a 'record' object (Note_Title, Note_Content, Parent_Id, se_module). To attach to a record set Parent_Id + se_module (Leads/Accounts/Contacts/Deals).</td></tr><tr><td>Create Task</td><td><code>createTask</code></td><td>Create a Task record. Subject is required; all other fields optional and omitted when not supplied.</td></tr><tr><td>Delete Account</td><td><code>deleteAccount</code></td><td>Delete an Account by ID.</td></tr><tr><td>Delete Contact</td><td><code>deleteContact</code></td><td>Delete a Contact by ID.</td></tr><tr><td>Delete Deal</td><td><code>deleteDeal</code></td><td>Delete a Deal by ID.</td></tr><tr><td>Delete Lead</td><td><code>deleteLead</code></td><td>Delete a Lead by ID.</td></tr></tbody></table>

<details>

<summary>View 18 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Note</td><td><code>deleteNote</code></td><td>Delete a Note by ID.</td></tr><tr><td>Delete Task</td><td><code>deleteTask</code></td><td>Delete a Task by ID.</td></tr><tr><td>Get Record</td><td><code>getRecord</code></td><td>Retrieve a single record by id from any Zoho CRM module, such as Leads, Contacts, Accounts, Deals, Tasks or Notes.</td></tr><tr><td>Get Users</td><td><code>getUsers</code></td><td>List org users. Pass type = AllUsers, ActiveUsers, DeactiveUsers, etc.</td></tr><tr><td>List Accounts</td><td><code>listAccounts</code></td><td>List Account records with pagination.</td></tr><tr><td>List Contacts</td><td><code>listContacts</code></td><td>List Contact records with pagination.</td></tr><tr><td>List Deals</td><td><code>listDeals</code></td><td>List Deal records with pagination.</td></tr><tr><td>List Leads</td><td><code>listLeads</code></td><td>List Lead records. Returns a page of records with pagination info.</td></tr><tr><td>List Modules</td><td><code>listModules</code></td><td>List all modules available in the Zoho CRM org (metadata).</td></tr><tr><td>List Notes</td><td><code>listNotes</code></td><td>List Note records with pagination.</td></tr><tr><td>List Tasks</td><td><code>listTasks</code></td><td>List Task records with pagination.</td></tr><tr><td>Search Records</td><td><code>searchRecords</code></td><td>Search records in a Zoho CRM module by criteria, email address, phone number or a free-text word. Exactly one of criteria, email, phone or word must be supplied.</td></tr><tr><td>Update Account</td><td><code>updateAccount</code></td><td>Update an Account by ID. Only the fields you supply are sent, so this is a partial update.</td></tr><tr><td>Update Contact</td><td><code>updateContact</code></td><td>Update a Contact by ID. Only the fields you supply are sent, so this is a partial update.</td></tr><tr><td>Update Deal</td><td><code>updateDeal</code></td><td>Update a Deal by ID. Only the fields you supply are sent, so this is a partial update.</td></tr><tr><td>Update Lead</td><td><code>updateLead</code></td><td>Update a Lead by ID. Only the fields you supply are sent, so this is a partial update.</td></tr><tr><td>Update Note</td><td><code>updateNote</code></td><td>Update a Note by ID. Only the fields you supply are sent, so this is a partial update.</td></tr><tr><td>Update Task</td><td><code>updateTask</code></td><td>Update a Task by ID. Only the fields you supply are sent, so this is a partial update.</td></tr></tbody></table>

</details>
