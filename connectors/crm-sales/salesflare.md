---
description: "Salesflare CRM — accounts, contacts, opportunities, tasks, meetings, calls, notes, tags, custom fields, pipelines, stages, users, groups, workflows (email…"
---

# Salesflare

Salesflare CRM — accounts, contacts, opportunities, tasks, meetings, calls, notes, tags, custom fields, pipelines, stages, users, groups, workflows (email campaigns), and settings. REST API at api.salesflare.com, Bearer token auth.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [salesflare.com](https://salesflare.com) |
| **Authentication** | Bearer token |
| **Actions** | 71 |
| **Events** | 0 |
| **Slug** | `salesflare` |

## Use it

Add Salesflare from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.salesflare.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Account | `createAccount` | Create an account (company). Set update_if_exists=true to upsert by domain. |
| Create Call | `createCall` | Create a logged call. Body is an array; this creates one call. date and participants are required. |
| Create Contact | `createContact` | Create a contact (person). Body is an array; this action creates one contact from email + name. Use Update Contact for the full field set (phone, address, tags, etc.). |
| Create Custom Field | `createCustomField` | Create a custom field on an item class. type (data-type id) and name are required. |
| Create Meeting | `createMeeting` | Create a meeting. Body is an array; this creates one meeting. date and participants are required. |
| Create Message | `createMessage` | Create an internal note/message on an account. account and body are required. |
| Create Message Feedback | `createMessageFeedback` | Add feedback to an internal note (POST /messages/{id}/feedback). feedback is required. |
| Create Message Feedback Alt | `createMessageFeedbackAlt` | Add feedback to an internal note (singular POST /message/{id}/feedback route). feedback is required. |
| Create Opportunity | `createOpportunity` | Create an opportunity (deal). account is required. |
| Create Tag | `createTag` | Create a tag. name is required. |
| Create Task | `createTask` | Create a task. Body is an array; this creates one task. description is required. |
| Create Workflow | `createWorkflow` | Create an email workflow (campaign). name is required. |
| Delete Account | `deleteAccount` | Delete an account by id. |
| Delete Contact | `deleteContact` | Delete a contact by id. |
| Delete Custom Field | `deleteCustomField` | Delete a custom field by item class and id. |
| Delete Meeting | `deleteMeeting` | Delete a meeting by id. |
| Delete Message | `deleteMessage` | Delete an internal note/message by id. |
| Delete Opportunity | `deleteOpportunity` | Delete an opportunity by id. |
| Delete Tag | `deleteTag` | Delete a tag by id. |
| Delete Task | `deleteTask` | Delete a task by id. |
| Get Account | `getAccount` | Get full details of a single account by id. |
| Get Account Feed | `getAccountFeed` | Get the activity feed (interactions) of an account. |
| Get AI Settings | `getAiSettings` | Get the team/user AI settings. |
| Get Campaign Merge Fields | `getCampaignMergefields` | Get the available merge fields for workflow/campaign email templates. |
| Get Contact | `getContact` | Get full details of a single contact by id. |
| Get Custom Field | `getCustomField` | Get custom field details by item class and id. |
| Get Group | `getGroup` | Get a group's details by id. |
| Get Me | `getMe` | Get the current authenticated user and team details. Use to validate the connection. |
| Get Meeting | `getMeeting` | Get meeting details by id. |
| Get Opportunity | `getOpportunity` | Get full details of a single opportunity by id. |
| Get Stage | `getStage` | Get a pipeline stage's details by id. |
| Get Tag | `getTag` | Get tag details by id. |
| Get Tag Usage | `getTagUsage` | Get a tag's usage in workflows, saved filters and reports. |
| Get User | `getUser` | Get a user's details by id. |
| Get Workflow | `getWorkflow` | Get an email workflow's details by id. |
| Link Account Contact | `linkAccountContact` | Attach a contact to an account (POST variant). Body is an array of {id,_dirty}. |
| Link Account User | `linkAccountUser` | Assign a user to an account (POST variant). Body is an array of {id,_dirty}. |
| List Account Messages | `listAccountMessages` | List messages/notes on an account. |
| List Accounts | `listAccounts` | List/search accounts (companies). Supports filtering by name, size, hotness, creation date and free-text search. |
| List Contacts | `listContacts` | List/search contacts (people). |
| List Currencies | `listCurrencies` | List supported currencies. |
| List Custom Field Options | `listCustomFieldOptions` | List the options of a dropdown-type custom field. |
| List Custom Field Types | `listCustomFieldTypes` | List the available custom field data types. |
| List Custom Fields | `listCustomFields` | List custom fields for an item class (account, contact, opportunity). |
| List Email Data Sources | `listEmailDatasources` | List the current user's connected email data sources. |
| List Filter Fields | `listFilterFields` | List the filter fields available for an entity (account, contact, opportunity). |
| List Groups | `listGroups` | List user groups/teams. |
| List My Contacts | `listMyContacts` | List contacts owned by the current authenticated user. |
| List Opportunities | `listOpportunities` | List/search opportunities (deals). |
| List Persons | `listPersons` | List persons (contacts + users combined lightweight search). |
| List Pipelines | `listPipelines` | List sales pipelines. |
| List Stages | `listStages` | List pipeline stages. |
| List Tags | `listTags` | List/search tags. |
| List Tasks | `listTasks` | List/search tasks (to-dos). |
| List Users | `listUsers` | List team users. |
| List Workflows | `listWorkflows` | List email workflows (campaigns). |
| Update Account | `updateAccount` | Update fields on an existing account. Only provided fields are sent. |
| Update Account Contacts | `updateAccountContacts` | Attach/update a contact on an account (PUT variant). Body is an array of {id,_dirty}. |
| Update Account Users | `updateAccountUsers` | Assign/update users on an account (PUT variant). Body is an array of {id,_dirty}. |
| Update AI Settings | `updateAiSettings` | Update the team/user AI settings. |
| Update Call | `updateCall` | Update a call's minutes/notes. calendar_id, external_id and notes are required by the API. |
| Update Contact | `updateContact` | Update fields on an existing contact. Only provided fields are sent. |
| Update Custom Field | `updateCustomField` | Update a custom field. id (in body) is required by the API. |
| Update Email Data Source | `updateEmailDatasource` | Update an email data source's signature and sending limits. |
| Update Meeting | `updateMeeting` | Update a meeting's minutes/notes. calendar_id, external_id and notes are required by the API. |
| Update Message | `updateMessage` | Update an internal note/message. account and body are required. |
| Update Opportunity | `updateOpportunity` | Update fields on an existing opportunity. Only provided fields are sent. |
| Update Tag | `updateTag` | Rename a tag. name is required. |
| Update Task | `updateTask` | Update a task (description, reminder, assignees, completion). Only provided fields are sent. |
| Update Workflow | `updateWorkflow` | Update an email workflow. name is required by the API. |
| Update Workflow Audience | `updateWorkflowAudience` | Re-enter or exit an entity (record) from a workflow's audience. |
