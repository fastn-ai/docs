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

| Action | Slug | What it does |
| --- | --- | --- |
| Create Account | `createAccount` | Create an Account record. Account_Name is required; all other fields optional and omitted from the request when not supplied. |
| Create Contact | `createContact` | Create a Contact record. Last_Name is required; all other fields optional and omitted when not supplied. |
| Create Deal | `createDeal` | Create a Deal record. Deal_Name and Stage are required; all other fields optional and omitted when not supplied. |
| Create Lead | `createLead` | Create a Lead record. Last_Name and Company are required; all other fields optional and omitted when not supplied. |
| Create Note | `createNote` | Create a Note record. Pass a 'record' object (Note_Title, Note_Content, Parent_Id, se_module). To attach to a record set Parent_Id + se_module (Leads/Accounts/Contacts/Deals). |
| Create Task | `createTask` | Create a Task record. Subject is required; all other fields optional and omitted when not supplied. |
| Delete Account | `deleteAccount` | Delete an Account by ID. |
| Delete Contact | `deleteContact` | Delete a Contact by ID. |
| Delete Deal | `deleteDeal` | Delete a Deal by ID. |
| Delete Lead | `deleteLead` | Delete a Lead by ID. |

<details>

<summary>See 18 more actions</summary>

* **Delete Note** `deleteNote`: Delete a Note by ID.
* **Delete Task** `deleteTask`: Delete a Task by ID.
* **Get Record** `getRecord`: Retrieve a single record by id from any Zoho CRM module, such as Leads, Contacts, Accounts, Deals, Tasks or Notes.
* **Get Users** `getUsers`: List org users. Pass type = AllUsers, ActiveUsers, DeactiveUsers, etc.
* **List Accounts** `listAccounts`: List Account records with pagination.
* **List Contacts** `listContacts`: List Contact records with pagination.
* **List Deals** `listDeals`: List Deal records with pagination.
* **List Leads** `listLeads`: List Lead records. Returns a page of records with pagination info.
* **List Modules** `listModules`: List all modules available in the Zoho CRM org (metadata).
* **List Notes** `listNotes`: List Note records with pagination.
* **List Tasks** `listTasks`: List Task records with pagination.
* **Search Records** `searchRecords`: Search records in a Zoho CRM module by criteria, email address, phone number or a free-text word. Exactly one of criteria, email, phone or word must be supplied.
* **Update Account** `updateAccount`: Update an Account by ID. Only the fields you supply are sent, so this is a partial update.
* **Update Contact** `updateContact`: Update a Contact by ID. Only the fields you supply are sent, so this is a partial update.
* **Update Deal** `updateDeal`: Update a Deal by ID. Only the fields you supply are sent, so this is a partial update.
* **Update Lead** `updateLead`: Update a Lead by ID. Only the fields you supply are sent, so this is a partial update.
* **Update Note** `updateNote`: Update a Note by ID. Only the fields you supply are sent, so this is a partial update.
* **Update Task** `updateTask`: Update a Task by ID. Only the fields you supply are sent, so this is a partial update.

</details>
