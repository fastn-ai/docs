---
description: "Close CRM connector."
hidden: true
---

# Close

<img src="../../.gitbook/assets/connectors/lg/close.png" alt="Close logo">

Close CRM connector. Full REST coverage of the Close API (https://api.close.com/api/v1): leads, contacts, opportunities, activities (calls/emails/notes/sms/meetings/custom), tasks, comments, users, organizations, memberships, roles, groups, pipelines, lead/opportunity statuses, custom fields, custom objects, smart views, email/SMS templates, sequences, reporting, bulk actions, exports, webhooks and events. Covers both Close and Close.io (same product). Auth: HTTP Basic with the API key as username and an empty password.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [close.com](https://close.com) |
| **Authentication** | Basic auth |
| **Slug** | `close` |

## Use it

Add Close from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.close.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activity Report | `getActivityReport` | Run an activity report (overview or comparison) over a time range. |
| Add Group Member | `addGroupMember` | Add a user to a group. |
| Bulk Update Memberships | `bulkUpdateMemberships` | Bulk-update memberships: pass the membership ids in _params.id__in and the settings to apply (e.g. role_id) at top level. Returns the number updated. |
| Bulk Update Tasks | `bulkUpdateTasks` | Bulk-update tasks matching a filter (query params) with the supplied body fields. |
| Create Activity Custom Field | `createActivityCustomField` | Create an activity custom field definition. Requires the custom_activity_type_id it belongs to. |
| Create Comment | `createComment` | Create an internal comment (optionally starting a thread on an activity). |
| Create Contact | `createContact` | Create a contact on a lead. |
| Create Contact Custom Field | `createContactCustomField` | Create a contact custom field definition. |
| Create Custom Activity | `createCustomActivity` | Create a custom activity of a given type on a lead. Set custom field values with top-level custom.&lt;field_id&gt; keys. |
| Create Custom Activity Type | `createCustomActivityType` | Create a custom activity type. |
| Create Custom Object | `createCustomObject` | Create a custom object instance. |
| Create Custom Object Type | `createCustomObjectType` | Create a custom object type. Add its fields afterwards with the custom object custom field actions. |
| Create Delete Bulk Action | `createBulkDelete` | Bulk-delete leads matching a query. Use with care. |
| Create Edit Bulk Action | `createBulkEdit` | Bulk-edit leads matching a query (e.g. set status). |
| Create Email | `createEmail` | Create an email activity (draft/log/send). |
| Create Email Bulk Action | `createBulkEmail` | Send a bulk email to contacts matching a query. |
| Create Email Template | `createEmailTemplate` | Create an email template. |
| Create Group | `createGroup` | Create a user group. Groups start empty; add users with Add Group Member. |
| Create Integration Link | `createIntegrationLink` | Create an integration link shown on leads/contacts. |
| Create Lead | `createLead` | Create a new lead. Optionally include nested contacts, addresses and custom fields. |
| Create Lead Custom Field | `createLeadCustomField` | Create a lead custom field definition. |
| Create Lead Export | `createLeadExport` | Start a lead export job (optionally for leads matching a search query). The file link is available from Get Export when done. |
| Create Lead Status | `createLeadStatus` | Create a lead status. |
| Create Membership | `createMembership` | Invite/create a membership (add a user to the organization). |
| Create Note | `createNote` | Create a note activity on a lead. |
| Create Opportunity | `createOpportunity` | Create an opportunity on a lead. |
| Create Opportunity Custom Field | `createOpportunityCustomField` | Create an opportunity custom field definition. |
| Create Opportunity Export | `createOpportunityExport` | Start an opportunity export job, optionally filtered with the same filters as List Opportunities. The file link is available from Get Export when done. |
| Create Opportunity Status | `createOpportunityStatus` | Create an opportunity status within a pipeline. |
| Create Outcome | `createOutcome` | Create a call/meeting outcome. |
| Create Pipeline | `createPipeline` | Create an opportunity pipeline. |
| Create Role | `createRole` | Create a custom role with a permissions map. |
| Create Sequence | `createSequence` | Create a sequence. |
| Create Sequence Subscription | `createSequenceSubscription` | Subscribe a contact to a sequence. Requires a connected sending email account. |
| Create Sequence Subscription Bulk Action | `createBulkSequenceSubscription` | Bulk-subscribe contacts matching a query to a sequence. |
| Create Shared Custom Field | `createSharedCustomField` | Create a shared custom field definition. |
| Create Smart View | `createSmartView` | Create a smart view (saved search). |
| Create SMS | `createSms` | Create an SMS activity (draft/log/send). |
| Create SMS Template | `createSmsTemplate` | Create an SMS template. |
| Create Task | `createTask` | Create a lead task. |
| Create Webhook | `createWebhook` | Create a webhook subscription. events is a list of {object_type, action} filters. |
| Custom Report | `getCustomReport` | Explorer / custom report producing graphable metric data. |
| Delete Activity Custom Field | `deleteActivityCustomField` | Delete an activity custom field definition by id. |
| Delete Call | `deleteCall` | Delete a call activity by id. |
| Delete Comment | `deleteComment` | Delete a comment by id. |
| Delete Contact | `deleteContact` | Delete a contact by id. |
| Delete Contact Custom Field | `deleteContactCustomField` | Delete a contact custom field definition by id. |
| Delete Custom Activity | `deleteCustomActivity` | Delete a custom-activity instance by id. |
| Delete Custom Activity Type | `deleteCustomActivityType` | Delete a custom activity type by id. |
| Delete Custom Object | `deleteCustomObject` | Delete a custom object instance by id. |
| Delete Custom Object Type | `deleteCustomObjectType` | Delete a custom object type by id. |
| Delete Email | `deleteEmail` | Delete an email activity by id. |
| Delete Email Template | `deleteEmailTemplate` | Delete an email template by id. |
| Delete Group | `deleteGroup` | Delete a group by id. |
| Delete Integration Link | `deleteIntegrationLink` | Delete an integration link by id. |
| Delete Lead | `deleteLead` | Delete a lead by id. |
| Delete Lead Custom Field | `deleteLeadCustomField` | Delete a lead custom field definition by id. |
| Delete Lead Status | `deleteLeadStatus` | Delete a lead status by id. |
| Delete Meeting | `deleteMeeting` | Delete a meeting activity by id. |
| Delete Membership | `deleteMembership` | Remove a membership from the organization. |
| Delete Note | `deleteNote` | Delete a note activity by id. |
| Delete Opportunity | `deleteOpportunity` | Delete an opportunity by id. |
| Delete Opportunity Custom Field | `deleteOpportunityCustomField` | Delete an opportunity custom field definition by id. |
| Delete Opportunity Status | `deleteOpportunityStatus` | Delete an opportunity status by id. |
| Delete Outcome | `deleteOutcome` | Delete a call/meeting outcome by id. |
| Delete Pipeline | `deletePipeline` | Delete an opportunity pipeline by id. |
| Delete Role | `deleteRole` | Delete a custom role by id. |
| Delete Sequence | `deleteSequence` | Delete a sequence by id. |
| Delete Sequence Subscription | `deleteSequenceSubscription` | Pause/delete a sequence subscription by id. |
| Delete Shared Custom Field | `deleteSharedCustomField` | Delete a shared custom field definition by id. |
| Delete Smart View | `deleteSmartView` | Delete a smart view (saved search) by id. |
| Delete SMS | `deleteSms` | Delete an SMS activity by id. |
| Delete SMS Template | `deleteSmsTemplate` | Delete an SMS template by id. |
| Delete Task | `deleteTask` | Delete a task by id. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription by id. |
| Funnel Stages Report | `getFunnelStagesReport` | Opportunity funnel stages report for a pipeline. |
| Funnel Totals Report | `getFunnelTotalsReport` | Opportunity funnel totals report for a pipeline. |
| Get Activity Custom Field | `getActivityCustomField` | Retrieve an activity custom field definition by id. |
| Get Call | `getCall` | Retrieve a call activity by id. |
| Get Comment | `getComment` | Retrieve a comment by id. |
| Get Comment Thread | `getCommentThread` | Retrieve a comment thread by id. |
| Get Connected Account | `getConnectedAccount` | Retrieve a connected account by id. |
| Get Contact | `getContact` | Retrieve a contact by id. |
| Get Contact Custom Field | `getContactCustomField` | Retrieve a contact custom field definition by id. |
| Get Custom Activity | `getCustomActivity` | Retrieve a custom-activity instance by id. |
| Get Custom Activity Type | `getCustomActivityType` | Retrieve a custom activity type by id. |
| Get Custom Field Schema | `getCustomFieldSchema` | Get the ordered custom field schema for an object type (lead/contact/opportunity/etc.). |
| Get Custom Object | `getCustomObject` | Retrieve a custom object instance by id. |
| Get Custom Object Type | `getCustomObjectType` | Retrieve a custom object type by id. |
| Get Delete Bulk Action | `getBulkDelete` | Retrieve a bulk delete action by id. |
| Get Edit Bulk Action | `getBulkEdit` | Retrieve a bulk edit action by id. |
| Get Email | `getEmail` | Retrieve an email activity by id. |
| Get Email Bulk Action | `getBulkEmail` | Retrieve a bulk email action by id. |
| Get Email Template | `getEmailTemplate` | Retrieve an email template by id. |
| Get Event | `getEvent` | Retrieve an event by id. |
| Get Export | `getExport` | Retrieve an export job by id (status + download URL when ready). |
| Get Form | `getForm` | Retrieve a form by id. |
| Get Group | `getGroup` | Retrieve a group by id. |
| Get Integration Link | `getIntegrationLink` | Retrieve an integration link by id. |
| Get Lead | `getLead` | Retrieve a single lead by id. |
| Get Lead Custom Field | `getLeadCustomField` | Retrieve a lead custom field definition by id. |
| Get Lead Status | `getLeadStatus` | Retrieve a lead status by id. |
| Get Me | `getMe` | Get the current authenticated user, including memberships and organizations. |
| Get Meeting | `getMeeting` | Retrieve a meeting activity by id. |
| Get Membership Pinned Views | `getMembershipPinnedViews` | Get the pinned smart views for a membership. |
| Get Note | `getNote` | Retrieve a note activity by id. |
| Get Opportunity | `getOpportunity` | Retrieve an opportunity by id. |
| Get Opportunity Custom Field | `getOpportunityCustomField` | Retrieve an opportunity custom field definition by id. |
| Get Opportunity Status | `getOpportunityStatus` | Retrieve an opportunity status by id. |
| Get Organization | `getOrganization` | Retrieve an organization by id. |
| Get Outcome | `getOutcome` | Retrieve an outcome by id. |
| Get Phone Number | `getPhoneNumber` | Retrieve a phone number by id. |
| Get Pipeline | `getPipeline` | Retrieve a pipeline by id. |
| Get Role | `getRole` | Retrieve a role by id. |
| Get Sequence | `getSequence` | Retrieve a sequence by id. |
| Get Sequence Subscription | `getSequenceSubscription` | Retrieve a sequence subscription by id. |
| Get Sequence Subscription Bulk Action | `getBulkSequenceSubscription` | Retrieve a bulk sequence-subscription action by id. |
| Get Shared Custom Field | `getSharedCustomField` | Retrieve a shared custom field definition by id. |
| Get Smart View | `getSmartView` | Retrieve a smart view by id. |
| Get SMS | `getSms` | Retrieve an SMS activity by id. |
| Get SMS Template | `getSmsTemplate` | Retrieve an SMS template by id. |
| Get Task | `getTask` | Retrieve a task by id. |
| Get User | `getUser` | Retrieve a user by id. |
| Get Webhook | `getWebhook` | Retrieve a webhook subscription by id. |
| List Activities | `listActivities` | List all activities of any type, optionally filtered by lead. |
| List Activity Custom Fields | `listActivityCustomFields` | List custom field definitions for custom activities. |
| List Activity Metrics | `listActivityMetrics` | List the available metric keys for activity reports. |
| List Calls | `listCalls` | List call activities. |
| List Comment Threads | `listCommentThreads` | List comment threads. |
| List Comments | `listComments` | List internal comments on a thread. |
| List Connected Accounts | `listConnectedAccounts` | List connected email/calendar accounts. |
| List Contact Custom Fields | `listContactCustomFields` | List custom field definitions for contacts. |
| List Contacts | `listContacts` | List contacts, optionally filtered by lead. |
| List Custom Activities | `listCustomActivities` | List custom-activity instances. |
| List Custom Activity Types | `listCustomActivityTypes` | List custom activity type definitions. |
| List Custom Object Types | `listCustomObjectTypes` | List custom object type definitions. |
| List Custom Objects | `listCustomObjects` | List custom object instances of a given type. |
| List Custom Report Fields | `listCustomReportFields` | List fields usable in custom/explorer reports. |
| List Delete Bulk Actions | `listBulkDeletes` | List bulk delete actions. |
| List Edit Bulk Actions | `listBulkEdits` | List bulk edit actions. |
| List Email Bulk Actions | `listBulkEmails` | List bulk email actions. |
| List Email Templates | `listEmailTemplates` | List email templates. |
| List Emails | `listEmails` | List email activities. |
| List Events | `listEvents` | List events from the event log (last 30 days). |
| List Exports | `listExports` | List export jobs. |
| List Forms | `listForms` | List forms. |
| List Groups | `listGroups` | List user groups. |
| List Integration Links | `listIntegrationLinks` | List integration links. |
| List Lead Custom Fields | `listLeadCustomFields` | List custom field definitions for leads. |
| List Lead Statuses | `listLeadStatuses` | List lead statuses. |
| List Leads | `listLeads` | List/search leads. Supports Close search query and field selection. |
| List Meetings | `listMeetings` | List meeting activities. |
| List Notes | `listNotes` | List note activities. |
| List Opportunities | `listOpportunities` | List opportunities, optionally filtered by lead. |
| List Opportunity Custom Fields | `listOpportunityCustomFields` | List custom field definitions for opportunities. |
| List Opportunity Statuses | `listOpportunityStatuses` | List opportunity statuses. |
| List Outcomes | `listOutcomes` | List activity outcomes. |
| List Phone Numbers | `listPhoneNumbers` | List phone numbers in the organization. |
| List Pipelines | `listPipelines` | List opportunity pipelines. |
| List Roles | `listRoles` | List organization roles. |
| List Sequence Subscription Bulk Actions | `listBulkSequenceSubscriptions` | List bulk sequence-subscription actions. |
| List Sequence Subscriptions | `listSequenceSubscriptions` | List sequence subscriptions. |
| List Sequences | `listSequences` | List email/SMS sequences. |
| List Shared Custom Fields | `listSharedCustomFields` | List shared custom field definitions. |
| List Smart Views | `listSmartViews` | List smart views (saved searches). |
| List SMS | `listSms` | List SMS activities. |
| List SMS Templates | `listSmsTemplates` | List SMS templates. |
| List Tasks | `listTasks` | List tasks, optionally filtered by lead and completion. |
| List User Availabilities | `listUserAvailabilities` | List availability/presence for users in the organization. |
| List Users | `listUsers` | List users in the organization. |
| List Webhooks | `listWebhooks` | List webhook subscriptions. |
| Log Call | `createCall` | Log a call activity on a lead. |
| Merge Leads | `mergeLeads` | Merge a source lead into a destination lead. |
| Remove Group Member | `removeGroupMember` | Remove a user from a group. |
| Render Email Template | `renderEmailTemplate` | Render an email template against a lead/contact to preview merged content. |
| Search Meetings | `searchMeetings` | Search meetings across the organization. |
| Sent Emails Report | `getSentEmailsReport` | Report of sent-email stats for the organization. |
| Update Activity Custom Field | `updateActivityCustomField` | Update an activity custom field definition. |
| Update Call | `updateCall` | Update a call activity (e.g. add note/outcome). |
| Update Comment | `updateComment` | Update a comment body. |
| Update Contact | `updateContact` | Update a contact. |
| Update Contact Custom Field | `updateContactCustomField` | Update a contact custom field definition. |
| Update Custom Activity | `updateCustomActivity` | Update a custom activity: change status or set/clear custom field values with top-level custom.&lt;field_id&gt; keys. |
| Update Custom Activity Type | `updateCustomActivityType` | Update a custom activity type. |
| Update Custom Field Schema | `updateCustomFieldSchema` | Update (reorder) the custom field schema for an object type. |
| Update Custom Object | `updateCustomObject` | Update a custom object instance. |
| Update Custom Object Type | `updateCustomObjectType` | Update a custom object type. |
| Update Email | `updateEmail` | Update an email activity (e.g. a draft). |
| Update Email Template | `updateEmailTemplate` | Update an email template. |
| Update Group | `updateGroup` | Update a group name. |
| Update Integration Link | `updateIntegrationLink` | Update an integration link. |
| Update Lead | `updateLead` | Update fields on an existing lead. |
| Update Lead Custom Field | `updateLeadCustomField` | Update a lead custom field definition. |
| Update Lead Status | `updateLeadStatus` | Update a lead status label. |
| Update Meeting | `updateMeeting` | Update a meeting activity (note/outcome). |
| Update Membership | `updateMembership` | Update a membership (e.g. change role). |
| Update Membership Pinned Views | `updateMembershipPinnedViews` | Update the pinned smart views for a membership. |
| Update Note | `updateNote` | Update a note activity. |
| Update Opportunity | `updateOpportunity` | Update an opportunity. |
| Update Opportunity Custom Field | `updateOpportunityCustomField` | Update an opportunity custom field definition. |
| Update Opportunity Status | `updateOpportunityStatus` | Update an opportunity status. |
| Update Organization | `updateOrganization` | Update an organization (e.g. name). |
| Update Outcome | `updateOutcome` | Update an outcome. Only the fields sent are changed. |
| Update Pipeline | `updatePipeline` | Update a pipeline. |
| Update Role | `updateRole` | Update a role's name or permissions. |
| Update Sequence | `updateSequence` | Update a sequence. |
| Update Sequence Subscription | `updateSequenceSubscription` | Update a sequence subscription (e.g. pause/resume). |
| Update Shared Custom Field | `updateSharedCustomField` | Update a shared custom field definition. |
| Update Smart View | `updateSmartView` | Update a smart view. |
| Update SMS | `updateSms` | Update an SMS activity (e.g. a draft). |
| Update SMS Template | `updateSmsTemplate` | Update an SMS template. |
| Update Task | `updateTask` | Update a task (e.g. mark complete). |
| Update Webhook | `updateWebhook` | Update a webhook subscription (e.g. pause/resume or change events). |
