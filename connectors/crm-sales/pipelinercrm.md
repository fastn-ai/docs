---
description: "Coevera (formerly Pipeliner CRM), a sales CRM by Pipelinersales Inc."
hidden: true
---

# Pipeliner CRM (Coevera)

<img src="../../.gitbook/assets/connectors/lg/pipelinercrm.png" alt="Pipeliner CRM (Coevera) logo">

Coevera (formerly Pipeliner CRM), a sales CRM by Pipelinersales Inc. This connector provides full REST API access to accounts, contacts, leads, opportunities, pipelines, activities (tasks, calls, appointments), products, quotes, custom fields and custom entities, documents, notes, emails, tags, targets, projects, approvals, webhooks, and organization/reference data.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [coevera.com](https://coevera.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `pipelinercrm` |

## Use it

Add Pipeliner CRM (Coevera) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pipelinercrm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| AccountRelations.create | `createAccountRelation` | AccountRelations.create. Creates new AccountRelation |
| Accounts.batch_create_or_update | `batchUpsertAccounts` | Accounts.batch_create_or_update. Create or update an batch of Accounts |
| Accounts.batch_delete | `batchDeleteAccounts` | Accounts.batch_delete. Removes Accounts with given list of ids |
| Accounts.batch_restore | `batchRestoreAccounts` | Accounts.batch_restore. Restores Accounts with given list of ids |
| Accounts.merge | `mergeAccounts` | Accounts.merge. Merger multiple Accounts into master record. |
| AccountSocialRelations.batch_create_or_update | `batchUpsertAccountSocialRelations` | AccountSocialRelations.batch_create_or_update. Create or update an batch of AccountSocialRelations |
| AccountSocialRelations.batch_delete | `batchDeleteAccountSocialRelations` | AccountSocialRelations.batch_delete. Removes AccountSocialRelations with given list of ids |
| AccountSocialRelations.batch_restore | `batchRestoreAccountSocialRelations` | AccountSocialRelations.batch_restore. Restores AccountSocialRelations with given list of ids |
| AccountSocialRelations.create | `createAccountSocialRelation` | AccountSocialRelations.create. Creates new AccountSocialRelation |
| AccountSocialRelations.delete | `deleteAccountSocialRelation` | AccountSocialRelations.delete. Removes AccountSocialRelation with given id |
| AccountSocialRelations.update | `updateAccountSocialRelation` | AccountSocialRelations.update. Modifies AccountSocialRelation or AccountSocialRelations with given id(s) |
| AccountTypes.batch_create_or_update | `batchUpsertAccountTypes` | AccountTypes.batch_create_or_update. Create or update an batch of AccountTypes |
| AccountTypes.batch_delete | `batchDeleteAccountTypes` | AccountTypes.batch_delete. Removes AccountTypes with given list of ids |
| AccountTypes.batch_restore | `batchRestoreAccountTypes` | AccountTypes.batch_restore. Restores AccountTypes with given list of ids |
| AccountTypes.create | `createAccountType` | AccountTypes.create. Creates new AccountType |
| AccountTypes.delete | `deleteAccountType` | AccountTypes.delete. Removes AccountType with given id |
| AccountTypes.get | `getAccountType` | AccountTypes.get. Returns AccountType with given id |
| AccountTypes.list | `listAccountTypes` | AccountTypes.list. Returns all defined AccountTypes |
| AccountTypes.update | `updateAccountType` | AccountTypes.update. Modifies AccountType or AccountTypes with given id(s) |
| ActivityComments.batch_create_or_update | `batchUpsertActivityComments` | ActivityComments.batch_create_or_update. Create or update an batch of ActivityComments |
| ActivityComments.batch_delete | `batchDeleteActivityComments` | ActivityComments.batch_delete. Removes ActivityComments with given list of ids |
| ActivityComments.batch_restore | `batchRestoreActivityComments` | ActivityComments.batch_restore. Restores ActivityComments with given list of ids |
| ActivityComments.create | `createActivityComment` | ActivityComments.create. Creates new ActivityComment |
| ActivityComments.delete | `deleteActivityComment` | ActivityComments.delete. Removes ActivityComment with given id |
| ActivityComments.get | `getActivityComment` | ActivityComments.get. Returns ActivityComment with given id |
| ActivityComments.list | `listActivityComments` | ActivityComments.list. Returns all defined ActivityComments |
| ActivityComments.update | `updateActivityComment` | ActivityComments.update. Modifies ActivityComment or ActivityComments with given id(s) |
| ActivityDataExRelations.get | `getActivityDataExRelation` | ActivityDataExRelations.get. Returns ActivityDataExRelation with given id |
| ActivityDataExRelations.list | `listActivityDataExRelations` | ActivityDataExRelations.list. Returns all defined ActivityDataExRelations |
| ActivityKPIs.batch_create_or_update | `batchUpsertActivityKPIs` | ActivityKPIs.batch_create_or_update. Create or update an batch of ActivityKPIs |
| ActivityKPIs.batch_delete | `batchDeleteActivityKPIs` | ActivityKPIs.batch_delete. Removes ActivityKPIs with given list of ids |
| ActivityKPIs.batch_restore | `batchRestoreActivityKPIs` | ActivityKPIs.batch_restore. Restores ActivityKPIs with given list of ids |
| ActivityKPIs.create | `createActivityKPI` | ActivityKPIs.create. Creates new ActivityKPI |
| ActivityKPIs.delete | `deleteActivityKPI` | ActivityKPIs.delete. Removes ActivityKPI with given id |
| ActivityKPIs.get | `getActivityKPI` | ActivityKPIs.get. Returns ActivityKPI with given id |
| ActivityKPIs.list | `listActivityKPIs` | ActivityKPIs.list. Returns all defined ActivityKPIs |
| ActivityKPIs.update | `updateActivityKPI` | ActivityKPIs.update. Modifies ActivityKPI or ActivityKPIs with given id(s) |
| ActivityRelations.batch_create_or_update | `batchUpsertActivityRelations` | ActivityRelations.batch_create_or_update. Create or update an batch of ActivityRelations |
| ActivityRelations.batch_delete | `batchDeleteActivityRelations` | ActivityRelations.batch_delete. Removes ActivityRelations with given list of ids |
| ActivityRelations.batch_restore | `batchRestoreActivityRelations` | ActivityRelations.batch_restore. Restores ActivityRelations with given list of ids |
| ActivityRelations.create | `createActivityRelation` | ActivityRelations.create. Creates new ActivityRelation |
| ActivityRelations.delete | `deleteActivityRelation` | ActivityRelations.delete. Removes ActivityRelation with given id |
| ActivityRelations.get | `getActivityRelation` | ActivityRelations.get. Returns ActivityRelation with given id |
| ActivityRelations.list | `listActivityRelations` | ActivityRelations.list. Returns all defined ActivityRelations |
| ActivityRelations.update | `updateActivityRelation` | ActivityRelations.update. Modifies ActivityRelation or ActivityRelations with given id(s) |
| AllowedAccountTypes.batch_create_or_update | `batchUpsertAllowedAccountTypes` | AllowedAccountTypes.batch_create_or_update. Create or update an batch of AllowedAccountTypes |
| AllowedAccountTypes.batch_delete | `batchDeleteAllowedAccountTypes` | AllowedAccountTypes.batch_delete. Removes AllowedAccountTypes with given list of ids |
| AllowedAccountTypes.batch_restore | `batchRestoreAllowedAccountTypes` | AllowedAccountTypes.batch_restore. Restores AllowedAccountTypes with given list of ids |
| AllowedAccountTypes.create | `createAllowedAccountType` | AllowedAccountTypes.create. Creates new AllowedAccountType |
| AllowedAccountTypes.delete | `deleteAllowedAccountType` | AllowedAccountTypes.delete. Removes AllowedAccountType with given id |
| AllowedAccountTypes.get | `getAllowedAccountType` | AllowedAccountTypes.get. Returns AllowedAccountType with given id |
| AllowedAccountTypes.list | `listAllowedAccountTypes` | AllowedAccountTypes.list. Returns all defined AllowedAccountTypes |
| AllowedAccountTypes.update | `updateAllowedAccountType` | AllowedAccountTypes.update. Modifies AllowedAccountType or AllowedAccountTypes with given id(s) |
| AllowedAppointmentTypes.batch_create_or_update | `batchUpsertAllowedAppointmentTypes` | AllowedAppointmentTypes.batch_create_or_update. Create or update an batch of AllowedAppointmentTypes |
| AllowedAppointmentTypes.batch_delete | `batchDeleteAllowedAppointmentTypes` | AllowedAppointmentTypes.batch_delete. Removes AllowedAppointmentTypes with given list of ids |
| AllowedAppointmentTypes.batch_restore | `batchRestoreAllowedAppointmentTypes` | AllowedAppointmentTypes.batch_restore. Restores AllowedAppointmentTypes with given list of ids |
| AllowedAppointmentTypes.create | `createAllowedAppointmentType` | AllowedAppointmentTypes.create. Creates new AllowedAppointmentType |
| AllowedAppointmentTypes.delete | `deleteAllowedAppointmentType` | AllowedAppointmentTypes.delete. Removes AllowedAppointmentType with given id |
| AllowedAppointmentTypes.get | `getAllowedAppointmentType` | AllowedAppointmentTypes.get. Returns AllowedAppointmentType with given id |
| AllowedAppointmentTypes.list | `listAllowedAppointmentTypes` | AllowedAppointmentTypes.list. Returns all defined AllowedAppointmentTypes |
| AllowedAppointmentTypes.update | `updateAllowedAppointmentType` | AllowedAppointmentTypes.update. Modifies AllowedAppointmentType or AllowedAppointmentTypes with given id(s) |
| AllowedCompanyEmails.batch_create_or_update | `batchUpsertAllowedCompanyEmails` | AllowedCompanyEmails.batch_create_or_update. Create or update an batch of AllowedCompanyEmails |
| AllowedCompanyEmails.batch_delete | `batchDeleteAllowedCompanyEmails` | AllowedCompanyEmails.batch_delete. Removes AllowedCompanyEmails with given list of ids |
| AllowedCompanyEmails.batch_restore | `batchRestoreAllowedCompanyEmails` | AllowedCompanyEmails.batch_restore. Restores AllowedCompanyEmails with given list of ids |
| AllowedCompanyEmails.create | `createAllowedCompanyEmail` | AllowedCompanyEmails.create. Creates new AllowedCompanyEmail |
| AllowedCompanyEmails.delete | `deleteAllowedCompanyEmail` | AllowedCompanyEmails.delete. Removes AllowedCompanyEmail with given id |
| AllowedCompanyEmails.get | `getAllowedCompanyEmail` | AllowedCompanyEmails.get. Returns AllowedCompanyEmail with given id |
| AllowedCompanyEmails.list | `listAllowedCompanyEmails` | AllowedCompanyEmails.list. Returns all defined AllowedCompanyEmails |
| AllowedCompanyEmails.update | `updateAllowedCompanyEmail` | AllowedCompanyEmails.update. Modifies AllowedCompanyEmail or AllowedCompanyEmails with given id(s) |
| AllowedCompanyPhones.batch_create_or_update | `batchUpsertAllowedCompanyPhones` | AllowedCompanyPhones.batch_create_or_update. Create or update an batch of AllowedCompanyPhones |
| AllowedCompanyPhones.batch_delete | `batchDeleteAllowedCompanyPhones` | AllowedCompanyPhones.batch_delete. Removes AllowedCompanyPhones with given list of ids |
| AllowedCompanyPhones.batch_restore | `batchRestoreAllowedCompanyPhones` | AllowedCompanyPhones.batch_restore. Restores AllowedCompanyPhones with given list of ids |
| AllowedCompanyPhones.create | `createAllowedCompanyPhone` | AllowedCompanyPhones.create. Creates new AllowedCompanyPhone |
| AllowedCompanyPhones.delete | `deleteAllowedCompanyPhone` | AllowedCompanyPhones.delete. Removes AllowedCompanyPhone with given id |
| AllowedCompanyPhones.get | `getAllowedCompanyPhone` | AllowedCompanyPhones.get. Returns AllowedCompanyPhone with given id |
| AllowedCompanyPhones.list | `listAllowedCompanyPhones` | AllowedCompanyPhones.list. Returns all defined AllowedCompanyPhones |
| AllowedCompanyPhones.update | `updateAllowedCompanyPhone` | AllowedCompanyPhones.update. Modifies AllowedCompanyPhone or AllowedCompanyPhones with given id(s) |
| AllowedContactTypes.batch_create_or_update | `batchUpsertAllowedContactTypes` | AllowedContactTypes.batch_create_or_update. Create or update an batch of AllowedContactTypes |
| AllowedContactTypes.batch_delete | `batchDeleteAllowedContactTypes` | AllowedContactTypes.batch_delete. Removes AllowedContactTypes with given list of ids |
| AllowedContactTypes.batch_restore | `batchRestoreAllowedContactTypes` | AllowedContactTypes.batch_restore. Restores AllowedContactTypes with given list of ids |
| AllowedContactTypes.create | `createAllowedContactType` | AllowedContactTypes.create. Creates new AllowedContactType |
| AllowedContactTypes.delete | `deleteAllowedContactType` | AllowedContactTypes.delete. Removes AllowedContactType with given id |
| AllowedContactTypes.get | `getAllowedContactType` | AllowedContactTypes.get. Returns AllowedContactType with given id |
| AllowedContactTypes.list | `listAllowedContactTypes` | AllowedContactTypes.list. Returns all defined AllowedContactTypes |
| AllowedContactTypes.update | `updateAllowedContactType` | AllowedContactTypes.update. Modifies AllowedContactType or AllowedContactTypes with given id(s) |
| AllowedLeadTypes.batch_create_or_update | `batchUpsertAllowedLeadTypes` | AllowedLeadTypes.batch_create_or_update. Create or update an batch of AllowedLeadTypes |
| AllowedLeadTypes.batch_delete | `batchDeleteAllowedLeadTypes` | AllowedLeadTypes.batch_delete. Removes AllowedLeadTypes with given list of ids |
| AllowedLeadTypes.batch_restore | `batchRestoreAllowedLeadTypes` | AllowedLeadTypes.batch_restore. Restores AllowedLeadTypes with given list of ids |
| AllowedLeadTypes.create | `createAllowedLeadType` | AllowedLeadTypes.create. Creates new AllowedLeadType |
| AllowedLeadTypes.delete | `deleteAllowedLeadType` | AllowedLeadTypes.delete. Removes AllowedLeadType with given id |
| AllowedLeadTypes.get | `getAllowedLeadType` | AllowedLeadTypes.get. Returns AllowedLeadType with given id |
| AllowedLeadTypes.list | `listAllowedLeadTypes` | AllowedLeadTypes.list. Returns all defined AllowedLeadTypes |
| AllowedLeadTypes.update | `updateAllowedLeadType` | AllowedLeadTypes.update. Modifies AllowedLeadType or AllowedLeadTypes with given id(s) |
| AllowedPipelines.batch_create_or_update | `batchUpsertAllowedPipelines` | AllowedPipelines.batch_create_or_update. Create or update an batch of AllowedPipelines |
| AllowedPipelines.batch_delete | `batchDeleteAllowedPipelines` | AllowedPipelines.batch_delete. Removes AllowedPipelines with given list of ids |
| AllowedPipelines.batch_restore | `batchRestoreAllowedPipelines` | AllowedPipelines.batch_restore. Restores AllowedPipelines with given list of ids |
| AllowedPipelines.create | `createAllowedPipeline` | AllowedPipelines.create. Creates new AllowedPipeline |
| AllowedPipelines.delete | `deleteAllowedPipeline` | AllowedPipelines.delete. Removes AllowedPipeline with given id |
| AllowedPipelines.get | `getAllowedPipeline` | AllowedPipelines.get. Returns AllowedPipeline with given id |
| AllowedPipelines.list | `listAllowedPipelines` | AllowedPipelines.list. Returns all defined AllowedPipelines |
| AllowedPipelines.update | `updateAllowedPipeline` | AllowedPipelines.update. Modifies AllowedPipeline or AllowedPipelines with given id(s) |
| AllowedQuoteTypes.batch_create_or_update | `batchUpsertAllowedQuoteTypes` | AllowedQuoteTypes.batch_create_or_update. Create or update an batch of AllowedQuoteTypes |
| AllowedQuoteTypes.batch_delete | `batchDeleteAllowedQuoteTypes` | AllowedQuoteTypes.batch_delete. Removes AllowedQuoteTypes with given list of ids |
| AllowedQuoteTypes.batch_restore | `batchRestoreAllowedQuoteTypes` | AllowedQuoteTypes.batch_restore. Restores AllowedQuoteTypes with given list of ids |
| AllowedQuoteTypes.create | `createAllowedQuoteType` | AllowedQuoteTypes.create. Creates new AllowedQuoteType |
| AllowedQuoteTypes.delete | `deleteAllowedQuoteType` | AllowedQuoteTypes.delete. Removes AllowedQuoteType with given id |
| AllowedQuoteTypes.get | `getAllowedQuoteType` | AllowedQuoteTypes.get. Returns AllowedQuoteType with given id |
| AllowedQuoteTypes.list | `listAllowedQuoteTypes` | AllowedQuoteTypes.list. Returns all defined AllowedQuoteTypes |
| AllowedQuoteTypes.update | `updateAllowedQuoteType` | AllowedQuoteTypes.update. Modifies AllowedQuoteType or AllowedQuoteTypes with given id(s) |
| AllowedTaskTypes.batch_create_or_update | `batchUpsertAllowedTaskTypes` | AllowedTaskTypes.batch_create_or_update. Create or update an batch of AllowedTaskTypes |
| AllowedTaskTypes.batch_delete | `batchDeleteAllowedTaskTypes` | AllowedTaskTypes.batch_delete. Removes AllowedTaskTypes with given list of ids |
| AllowedTaskTypes.batch_restore | `batchRestoreAllowedTaskTypes` | AllowedTaskTypes.batch_restore. Restores AllowedTaskTypes with given list of ids |
| AllowedTaskTypes.create | `createAllowedTaskType` | AllowedTaskTypes.create. Creates new AllowedTaskType |
| AllowedTaskTypes.delete | `deleteAllowedTaskType` | AllowedTaskTypes.delete. Removes AllowedTaskType with given id |
| AllowedTaskTypes.get | `getAllowedTaskType` | AllowedTaskTypes.get. Returns AllowedTaskType with given id |
| AllowedTaskTypes.list | `listAllowedTaskTypes` | AllowedTaskTypes.list. Returns all defined AllowedTaskTypes |
| AllowedTaskTypes.update | `updateAllowedTaskType` | AllowedTaskTypes.update. Modifies AllowedTaskType or AllowedTaskTypes with given id(s) |
| ApiAccesses.get | `getApiAccess` | ApiAccesses.get. Returns ApiAccess with given id |
| ApiAccesses.list | `listApiAccesses` | ApiAccesses.list. Returns all defined ApiAccesses |
| AppointmentClientInviteesRelations.batch_create_or_update | `batchUpsertAppointmentClientInviteesRelations` | AppointmentClientInviteesRelations.batch_create_or_update. Create or update an batch of AppointmentClientInviteesRelations |
| AppointmentClientInviteesRelations.batch_delete | `batchDeleteAppointmentClientInviteesRelations` | AppointmentClientInviteesRelations.batch_delete. Removes AppointmentClientInviteesRelations with given list of ids |
| AppointmentClientInviteesRelations.batch_restore | `batchRestoreAppointmentClientInviteesRelations` | AppointmentClientInviteesRelations.batch_restore. Restores AppointmentClientInviteesRelations with given list of ids |
| AppointmentClientInviteesRelations.create | `createAppointmentClientInviteesRelation` | AppointmentClientInviteesRelations.create. Creates new AppointmentClientInviteesRelation |
| AppointmentClientInviteesRelations.delete | `deleteAppointmentClientInviteesRelation` | AppointmentClientInviteesRelations.delete. Removes AppointmentClientInviteesRelation with given id |
| AppointmentClientInviteesRelations.get | `getAppointmentClientInviteesRelation` | AppointmentClientInviteesRelations.get. Returns AppointmentClientInviteesRelation with given id |
| AppointmentClientInviteesRelations.list | `listAppointmentClientInviteesRelations` | AppointmentClientInviteesRelations.list. Returns all defined AppointmentClientInviteesRelations |
| AppointmentClientInviteesRelations.update | `updateAppointmentClientInviteesRelation` | AppointmentClientInviteesRelations.update. Modifies AppointmentClientInviteesRelation or AppointmentClientInviteesRelations with given id(s) |
| AppointmentContactInviteesRelations.batch_create_or_update | `batchUpsertAppointmentContactInviteesRelations` | AppointmentContactInviteesRelations.batch_create_or_update. Create or update an batch of AppointmentContactInviteesRelations |
| AppointmentContactInviteesRelations.batch_delete | `batchDeleteAppointmentContactInviteesRelations` | AppointmentContactInviteesRelations.batch_delete. Removes AppointmentContactInviteesRelations with given list of ids |
| AppointmentContactInviteesRelations.batch_restore | `batchRestoreAppointmentContactInviteesRelations` | AppointmentContactInviteesRelations.batch_restore. Restores AppointmentContactInviteesRelations with given list of ids |
| AppointmentContactInviteesRelations.create | `createAppointmentContactInviteesRelation` | AppointmentContactInviteesRelations.create. Creates new AppointmentContactInviteesRelation |
| AppointmentContactInviteesRelations.delete | `deleteAppointmentContactInviteesRelation` | AppointmentContactInviteesRelations.delete. Removes AppointmentContactInviteesRelation with given id |
| AppointmentContactInviteesRelations.get | `getAppointmentContactInviteesRelation` | AppointmentContactInviteesRelations.get. Returns AppointmentContactInviteesRelation with given id |
| AppointmentContactInviteesRelations.list | `listAppointmentContactInviteesRelations` | AppointmentContactInviteesRelations.list. Returns all defined AppointmentContactInviteesRelations |
| AppointmentContactInviteesRelations.update | `updateAppointmentContactInviteesRelation` | AppointmentContactInviteesRelations.update. Modifies AppointmentContactInviteesRelation or AppointmentContactInviteesRelations with given id(s) |
| AppointmentReminders.batch_create_or_update | `batchUpsertAppointmentReminders` | AppointmentReminders.batch_create_or_update. Create or update an batch of AppointmentReminders |
| AppointmentReminders.batch_delete | `batchDeleteAppointmentReminders` | AppointmentReminders.batch_delete. Removes AppointmentReminders with given list of ids |
| AppointmentReminders.batch_restore | `batchRestoreAppointmentReminders` | AppointmentReminders.batch_restore. Restores AppointmentReminders with given list of ids |
| AppointmentReminders.create | `createAppointmentReminder` | AppointmentReminders.create. Creates new AppointmentReminder |
| AppointmentReminders.delete | `deleteAppointmentReminder` | AppointmentReminders.delete. Removes AppointmentReminder with given id |
| AppointmentReminders.get | `getAppointmentReminder` | AppointmentReminders.get. Returns AppointmentReminder with given id |
| AppointmentReminders.list | `listAppointmentReminders` | AppointmentReminders.list. Returns all defined AppointmentReminders |
| AppointmentReminders.update | `updateAppointmentReminder` | AppointmentReminders.update. Modifies AppointmentReminder or AppointmentReminders with given id(s) |
| Appointments.batch_create_or_update | `batchUpsertAppointments` | Appointments.batch_create_or_update. Create or update an batch of Appointments |
| Appointments.batch_delete | `batchDeleteAppointments` | Appointments.batch_delete. Removes Appointments with given list of ids |
| Appointments.batch_restore | `batchRestoreAppointments` | Appointments.batch_restore. Restores Appointments with given list of ids |
| Appointments.create | `createAppointment` | Appointments.create. Creates new Appointment |
| Appointments.delete | `deleteAppointment` | Appointments.delete. Removes Appointment with given id |
| Appointments.get | `getAppointment` | Appointments.get. Returns Appointment with given id |
| Appointments.list | `listAppointments` | Appointments.list. Returns all defined Appointments |
| Appointments.update | `updateAppointment` | Appointments.update. Modifies Appointment or Appointments with given id(s) |
| AppointmentSchedules.batch_create_or_update | `batchUpsertAppointmentSchedules` | AppointmentSchedules.batch_create_or_update. Create or update an batch of AppointmentSchedules |
| AppointmentSchedules.batch_delete | `batchDeleteAppointmentSchedules` | AppointmentSchedules.batch_delete. Removes AppointmentSchedules with given list of ids |
| AppointmentSchedules.batch_restore | `batchRestoreAppointmentSchedules` | AppointmentSchedules.batch_restore. Restores AppointmentSchedules with given list of ids |
| AppointmentSchedules.create | `createAppointmentSchedule` | AppointmentSchedules.create. Creates new AppointmentSchedule |
| AppointmentSchedules.delete | `deleteAppointmentSchedule` | AppointmentSchedules.delete. Removes AppointmentSchedule with given id |
| AppointmentSchedules.get | `getAppointmentSchedule` | AppointmentSchedules.get. Returns AppointmentSchedule with given id |
| AppointmentSchedules.list | `listAppointmentSchedules` | AppointmentSchedules.list. Returns all defined AppointmentSchedules |
| AppointmentSchedules.update | `updateAppointmentSchedule` | AppointmentSchedules.update. Modifies AppointmentSchedule or AppointmentSchedules with given id(s) |
| AppointmentTypes.batch_create_or_update | `batchUpsertAppointmentTypes` | AppointmentTypes.batch_create_or_update. Create or update an batch of AppointmentTypes |
| AppointmentTypes.batch_delete | `batchDeleteAppointmentTypes` | AppointmentTypes.batch_delete. Removes AppointmentTypes with given list of ids |
| AppointmentTypes.batch_restore | `batchRestoreAppointmentTypes` | AppointmentTypes.batch_restore. Restores AppointmentTypes with given list of ids |
| AppointmentTypes.create | `createAppointmentType` | AppointmentTypes.create. Creates new AppointmentType |
| AppointmentTypes.delete | `deleteAppointmentType` | AppointmentTypes.delete. Removes AppointmentType with given id |
| AppointmentTypes.get | `getAppointmentType` | AppointmentTypes.get. Returns AppointmentType with given id |
| AppointmentTypes.list | `listAppointmentTypes` | AppointmentTypes.list. Returns all defined AppointmentTypes |
| AppointmentTypes.update | `updateAppointmentType` | AppointmentTypes.update. Modifies AppointmentType or AppointmentTypes with given id(s) |
| ApprovalApprovers.batch_create_or_update | `batchUpsertApprovalApprovers` | ApprovalApprovers.batch_create_or_update. Create or update an batch of ApprovalApprovers |
| ApprovalApprovers.batch_delete | `batchDeleteApprovalApprovers` | ApprovalApprovers.batch_delete. Removes ApprovalApprovers with given list of ids |
| ApprovalApprovers.batch_restore | `batchRestoreApprovalApprovers` | ApprovalApprovers.batch_restore. Restores ApprovalApprovers with given list of ids |
| ApprovalApprovers.create | `createApprovalApprover` | ApprovalApprovers.create. Creates new ApprovalApprover |
| ApprovalApprovers.delete | `deleteApprovalApprover` | ApprovalApprovers.delete. Removes ApprovalApprover with given id |
| ApprovalApprovers.get | `getApprovalApprover` | ApprovalApprovers.get. Returns ApprovalApprover with given id |
| ApprovalApprovers.list | `listApprovalApprovers` | ApprovalApprovers.list. Returns all defined ApprovalApprovers |
| ApprovalApprovers.update | `updateApprovalApprover` | ApprovalApprovers.update. Modifies ApprovalApprover or ApprovalApprovers with given id(s) |
| ApprovalProcessActivityLogLines.batch_create_or_update | `batchUpsertApprovalProcessActivityLogLines` | ApprovalProcessActivityLogLines.batch_create_or_update. Create or update an batch of ApprovalProcessActivityLogLines |
| ApprovalProcessActivityLogLines.batch_delete | `batchDeleteApprovalProcessActivityLogLines` | ApprovalProcessActivityLogLines.batch_delete. Removes ApprovalProcessActivityLogLines with given list of ids |
| ApprovalProcessActivityLogLines.batch_restore | `batchRestoreApprovalProcessActivityLogLines` | ApprovalProcessActivityLogLines.batch_restore. Restores ApprovalProcessActivityLogLines with given list of ids |
| ApprovalProcessActivityLogLines.create | `createApprovalProcessActivityLogLine` | ApprovalProcessActivityLogLines.create. Creates new ApprovalProcessActivityLogLine |
| ApprovalProcessActivityLogLines.delete | `deleteApprovalProcessActivityLogLine` | ApprovalProcessActivityLogLines.delete. Removes ApprovalProcessActivityLogLine with given id |
| ApprovalProcessActivityLogLines.get | `getApprovalProcessActivityLogLine` | ApprovalProcessActivityLogLines.get. Returns ApprovalProcessActivityLogLine with given id |
| ApprovalProcessActivityLogLines.list | `listApprovalProcessActivityLogLines` | ApprovalProcessActivityLogLines.list. Returns all defined ApprovalProcessActivityLogLines |
| ApprovalProcessActivityLogLines.update | `updateApprovalProcessActivityLogLine` | ApprovalProcessActivityLogLines.update. Modifies ApprovalProcessActivityLogLine or ApprovalProcessActivityLogLines with given id(s) |
| ApprovalProcesses.batch_create_or_update | `batchUpsertApprovalProcesses` | ApprovalProcesses.batch_create_or_update. Create or update an batch of ApprovalProcesses |
| ApprovalProcesses.batch_delete | `batchDeleteApprovalProcesses` | ApprovalProcesses.batch_delete. Removes ApprovalProcesses with given list of ids |
| ApprovalProcesses.batch_restore | `batchRestoreApprovalProcesses` | ApprovalProcesses.batch_restore. Restores ApprovalProcesses with given list of ids |
| ApprovalProcesses.create | `createApprovalProcess` | ApprovalProcesses.create. Creates new ApprovalProcess |
| ApprovalProcesses.delete | `deleteApprovalProcess` | ApprovalProcesses.delete. Removes ApprovalProcess with given id |
| ApprovalProcesses.get | `getApprovalProcess` | ApprovalProcesses.get. Returns ApprovalProcess with given id |
| ApprovalProcesses.list | `listApprovalProcesses` | ApprovalProcesses.list. Returns all defined ApprovalProcesses |
| ApprovalProcesses.update | `updateApprovalProcess` | ApprovalProcesses.update. Modifies ApprovalProcess or ApprovalProcesses with given id(s) |
| Approvals.batch_create_or_update | `batchUpsertApprovals` | Approvals.batch_create_or_update. Create or update an batch of Approvals |
| Approvals.batch_delete | `batchDeleteApprovals` | Approvals.batch_delete. Removes Approvals with given list of ids |
| Approvals.batch_restore | `batchRestoreApprovals` | Approvals.batch_restore. Restores Approvals with given list of ids |
| Approvals.create | `createApproval` | Approvals.create. Creates new Approval |
| Approvals.delete | `deleteApproval` | Approvals.delete. Removes Approval with given id |
| Approvals.get | `getApproval` | Approvals.get. Returns Approval with given id |
| Approvals.list | `listApprovals` | Approvals.list. Returns all defined Approvals |
| Approvals.update | `updateApproval` | Approvals.update. Modifies Approval or Approvals with given id(s) |
| Batch Create Or Update Account KPIs | `batchUpsertAccountKPIs` | Create or update a batch of Account KPIs records in one call. Body must be a JSON array string (engine limitation for top-level array bodies). |
| Batch Create Or Update Account Product Pricings | `batchUpsertAccountProductPricings` | Create or update a batch of Account Product Pricings records in one call. Body must be a JSON array string (engine limitation for top-level array bodies). |
| Batch Create Or Update Account Relation Labels | `batchUpsertAccountRelationLabels` | Create or update a batch of Account Relation Labels records in one call. Body must be a JSON array string (engine limitation for top-level array bodies). |
| Batch Create Or Update Account Relation Types | `batchUpsertAccountRelationTypes` | Create or update a batch of Account Relation Types records in one call. Body must be a JSON array string (engine limitation for top-level array bodies). |
| Batch Create Or Update Account Relations | `batchUpsertAccountRelations` | Create or update a batch of Account Relations records in one call. Body must be a JSON array string (engine limitation for top-level array bodies). |
| Batch Create Or Update Account Roles | `batchUpsertAccountRoles` | Create or update a batch of Account Roles records in one call. Body must be a JSON array string (engine limitation for top-level array bodies). |
| Batch Create Or Update Account Sharing Client Relations | `batchUpsertAccountSharingClientRelations` | Create or update a batch of Account Sharing Client Relations records in one call. Body must be a JSON array string (engine limitation for top-level array bodies). |
| Batch Create Or Update Account Sharing Sales Unit Relations | `batchUpsertAccountSharingSalesUnitRelations` | Create or update a batch of Account Sharing Sales Unit Relations records in one call. Body must be a JSON array string (engine limitation for top-level array bodies). |
| Batch Delete Account KPIs | `batchDeleteAccountKPIs` | Delete a batch of Account KPIs records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Delete Account Product Pricings | `batchDeleteAccountProductPricings` | Delete a batch of Account Product Pricings records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Delete Account Relation Labels | `batchDeleteAccountRelationLabels` | Delete a batch of Account Relation Labels records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Delete Account Relation Types | `batchDeleteAccountRelationTypes` | Delete a batch of Account Relation Types records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Delete Account Relations | `batchDeleteAccountRelations` | Delete a batch of Account Relations records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Delete Account Roles | `batchDeleteAccountRoles` | Delete a batch of Account Roles records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Delete Account Sharing Client Relations | `batchDeleteAccountSharingClientRelations` | Delete a batch of Account Sharing Client Relations records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Delete Account Sharing Sales Unit Relations | `batchDeleteAccountSharingSalesUnitRelations` | Delete a batch of Account Sharing Sales Unit Relations records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Restore Account KPIs | `batchRestoreAccountKPIs` | Restore a batch of soft-deleted Account KPIs records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Restore Account Product Pricings | `batchRestoreAccountProductPricings` | Restore a batch of soft-deleted Account Product Pricings records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Restore Account Relation Labels | `batchRestoreAccountRelationLabels` | Restore a batch of soft-deleted Account Relation Labels records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Restore Account Relation Types | `batchRestoreAccountRelationTypes` | Restore a batch of soft-deleted Account Relation Types records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Restore Account Relations | `batchRestoreAccountRelations` | Restore a batch of soft-deleted Account Relations records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Restore Account Roles | `batchRestoreAccountRoles` | Restore a batch of soft-deleted Account Roles records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Restore Account Sharing Client Relations | `batchRestoreAccountSharingClientRelations` | Restore a batch of soft-deleted Account Sharing Client Relations records by ID in one call. Body must be a JSON array string of IDs. |
| Batch Restore Account Sharing Sales Unit Relations | `batchRestoreAccountSharingSalesUnitRelations` | Restore a batch of soft-deleted Account Sharing Sales Unit Relations records by ID in one call. Body must be a JSON array string of IDs. |
| Calls.batch_create_or_update | `batchUpsertCalls` | Calls.batch_create_or_update. Create or update an batch of Calls |
| Calls.batch_delete | `batchDeleteCalls` | Calls.batch_delete. Removes Calls with given list of ids |
| Calls.batch_restore | `batchRestoreCalls` | Calls.batch_restore. Restores Calls with given list of ids |
| Calls.create | `createCall` | Calls.create. Creates new Call |
| Calls.delete | `deleteCall` | Calls.delete. Removes Call with given id |
| Calls.get | `getCall` | Calls.get. Returns Call with given id |
| Calls.list | `listCalls` | Calls.list. Returns all defined Calls |
| Calls.update | `updateCall` | Calls.update. Modifies Call or Calls with given id(s) |
| ChatConversations.batch_create_or_update | `batchUpsertChatConversations` | ChatConversations.batch_create_or_update. Create or update an batch of ChatConversations |
| ChatConversations.batch_delete | `batchDeleteChatConversations` | ChatConversations.batch_delete. Removes ChatConversations with given list of ids |
| ChatConversations.batch_restore | `batchRestoreChatConversations` | ChatConversations.batch_restore. Restores ChatConversations with given list of ids |
| ChatConversations.create | `createChatConversation` | ChatConversations.create. Creates new ChatConversation |
| ChatConversations.delete | `deleteChatConversation` | ChatConversations.delete. Removes ChatConversation with given id |
| ChatConversations.get | `getChatConversation` | ChatConversations.get. Returns ChatConversation with given id |
| ChatConversations.list | `listChatConversations` | ChatConversations.list. Returns all defined ChatConversations |
| ChatConversations.update | `updateChatConversation` | ChatConversations.update. Modifies ChatConversation or ChatConversations with given id(s) |
| ClientExcludedOppties.batch_create_or_update | `batchUpsertClientExcludedOppties` | ClientExcludedOppties.batch_create_or_update. Create or update an batch of ClientExcludedOppties |
| ClientExcludedOppties.batch_delete | `batchDeleteClientExcludedOppties` | ClientExcludedOppties.batch_delete. Removes ClientExcludedOppties with given list of ids |
| ClientExcludedOppties.batch_restore | `batchRestoreClientExcludedOppties` | ClientExcludedOppties.batch_restore. Restores ClientExcludedOppties with given list of ids |
| ClientExcludedOppties.create | `createClientExcludedOppty` | ClientExcludedOppties.create. Creates new ClientExcludedOppty |
| ClientExcludedOppties.delete | `deleteClientExcludedOppty` | ClientExcludedOppties.delete. Removes ClientExcludedOppty with given id |
| ClientExcludedOppties.get | `getClientExcludedOppty` | ClientExcludedOppties.get. Returns ClientExcludedOppty with given id |
| ClientExcludedOppties.list | `listClientExcludedOppties` | ClientExcludedOppties.list. Returns all defined ClientExcludedOppties |
| ClientExcludedOppties.update | `updateClientExcludedOppty` | ClientExcludedOppties.update. Modifies ClientExcludedOppty or ClientExcludedOppties with given id(s) |
| ClientFavorites.batch_create_or_update | `batchUpsertClientFavorites` | ClientFavorites.batch_create_or_update. Create or update an batch of ClientFavorites |
| ClientFavorites.batch_delete | `batchDeleteClientFavorites` | ClientFavorites.batch_delete. Removes ClientFavorites with given list of ids |
| ClientFavorites.batch_restore | `batchRestoreClientFavorites` | ClientFavorites.batch_restore. Restores ClientFavorites with given list of ids |
| ClientFavorites.create | `createClientFavorite` | ClientFavorites.create. Creates new ClientFavorite |
| ClientFavorites.delete | `deleteClientFavorite` | ClientFavorites.delete. Removes ClientFavorite with given id |
| ClientFavorites.get | `getClientFavorite` | ClientFavorites.get. Returns ClientFavorite with given id |
| ClientFavorites.list | `listClientFavorites` | ClientFavorites.list. Returns all defined ClientFavorites |
| ClientFavorites.update | `updateClientFavorite` | ClientFavorites.update. Modifies ClientFavorite or ClientFavorites with given id(s) |
| Clients.batch_create_or_update | `batchUpsertClients` | Clients.batch_create_or_update. Create or update an batch of Clients |
| Clients.batch_delete | `batchDeleteClients` | Clients.batch_delete. Removes Clients with given list of ids |
| Clients.batch_restore | `batchRestoreClients` | Clients.batch_restore. Restores Clients with given list of ids |
| Clients.create | `createClient` | Clients.create. Creates new Client |
| Clients.delete | `deleteClient` | Clients.delete. Removes Client with given id |
| Clients.get | `getClient` | Clients.get. Returns Client with given id |
| Clients.list | `listClients` | Clients.list. Returns all defined Clients |
| Clients.update | `updateClient` | Clients.update. Modifies Client or Clients with given id(s) |
| ClientSettings.get | `getClientSetting` | ClientSettings.get. Returns ClientSetting with given id |
| ClientSettings.list | `listClientSettings` | ClientSettings.list. Returns all defined ClientSettings |
| ClientStoryReads.batch_create_or_update | `batchUpsertClientStoryReads` | ClientStoryReads.batch_create_or_update. Create or update an batch of ClientStoryReads |
| ClientStoryReads.batch_delete | `batchDeleteClientStoryReads` | ClientStoryReads.batch_delete. Removes ClientStoryReads with given list of ids |
| ClientStoryReads.batch_restore | `batchRestoreClientStoryReads` | ClientStoryReads.batch_restore. Restores ClientStoryReads with given list of ids |
| ClientStoryReads.create | `createClientStoryRead` | ClientStoryReads.create. Creates new ClientStoryRead |
| ClientStoryReads.delete | `deleteClientStoryRead` | ClientStoryReads.delete. Removes ClientStoryRead with given id |
| ClientStoryReads.get | `getClientStoryRead` | ClientStoryReads.get. Returns ClientStoryRead with given id |
| ClientStoryReads.list | `listClientStoryReads` | ClientStoryReads.list. Returns all defined ClientStoryReads |
| ClientStoryReads.update | `updateClientStoryRead` | ClientStoryReads.update. Modifies ClientStoryRead or ClientStoryReads with given id(s) |
| CloudObjectFolders.batch_create_or_update | `batchUpsertCloudObjectFolders` | CloudObjectFolders.batch_create_or_update. Create or update an batch of CloudObjectFolders |
| CloudObjectFolders.batch_delete | `batchDeleteCloudObjectFolders` | CloudObjectFolders.batch_delete. Removes CloudObjectFolders with given list of ids |
| CloudObjectFolders.batch_restore | `batchRestoreCloudObjectFolders` | CloudObjectFolders.batch_restore. Restores CloudObjectFolders with given list of ids |
| CloudObjectFolders.create | `createCloudObjectFolder` | CloudObjectFolders.create. Creates new CloudObjectFolder |
| CloudObjectFolders.delete | `deleteCloudObjectFolder` | CloudObjectFolders.delete. Removes CloudObjectFolder with given id |
| CloudObjectFolders.get | `getCloudObjectFolder` | CloudObjectFolders.get. Returns CloudObjectFolder with given id |
| CloudObjectFolders.list | `listCloudObjectFolders` | CloudObjectFolders.list. Returns all defined CloudObjectFolders |
| CloudObjectFolders.update | `updateCloudObjectFolder` | CloudObjectFolders.update. Modifies CloudObjectFolder or CloudObjectFolders with given id(s) |
| CloudObjectRelations.batch_create_or_update | `batchUpsertCloudObjectRelations` | CloudObjectRelations.batch_create_or_update. Create or update an batch of CloudObjectRelations |
| CloudObjectRelations.batch_delete | `batchDeleteCloudObjectRelations` | CloudObjectRelations.batch_delete. Removes CloudObjectRelations with given list of ids |
| CloudObjectRelations.batch_restore | `batchRestoreCloudObjectRelations` | CloudObjectRelations.batch_restore. Restores CloudObjectRelations with given list of ids |
| CloudObjectRelations.create | `createCloudObjectRelation` | CloudObjectRelations.create. Creates new CloudObjectRelation |
| CloudObjectRelations.delete | `deleteCloudObjectRelation` | CloudObjectRelations.delete. Removes CloudObjectRelation with given id |
| CloudObjectRelations.get | `getCloudObjectRelation` | CloudObjectRelations.get. Returns CloudObjectRelation with given id |
| CloudObjectRelations.list | `listCloudObjectRelations` | CloudObjectRelations.list. Returns all defined CloudObjectRelations |
| CloudObjectRelations.update | `updateCloudObjectRelation` | CloudObjectRelations.update. Modifies CloudObjectRelation or CloudObjectRelations with given id(s) |
| CloudObjects.batch_create_or_update | `batchUpsertCloudObjects` | CloudObjects.batch_create_or_update. Create or update an batch of CloudObjects |
| CloudObjects.batch_delete | `batchDeleteCloudObjects` | CloudObjects.batch_delete. Removes CloudObjects with given list of ids |
| CloudObjects.batch_restore | `batchRestoreCloudObjects` | CloudObjects.batch_restore. Restores CloudObjects with given list of ids |
| CloudObjects.create | `createCloudObject` | CloudObjects.create. Creates new CloudObject |
| CloudObjects.delete | `deleteCloudObject` | CloudObjects.delete. Removes CloudObject with given id |
| CloudObjects.get | `getCloudObject` | CloudObjects.get. Returns CloudObject with given id |
| CloudObjects.list | `listCloudObjects` | CloudObjects.list. Returns all defined CloudObjects |
| CloudObjects.update | `updateCloudObject` | CloudObjects.update. Modifies CloudObject or CloudObjects with given id(s) |
| CloudObjectStepRelations.batch_create_or_update | `batchUpsertCloudObjectStepRelations` | CloudObjectStepRelations.batch_create_or_update. Create or update an batch of CloudObjectStepRelations |
| CloudObjectStepRelations.batch_delete | `batchDeleteCloudObjectStepRelations` | CloudObjectStepRelations.batch_delete. Removes CloudObjectStepRelations with given list of ids |
| CloudObjectStepRelations.batch_restore | `batchRestoreCloudObjectStepRelations` | CloudObjectStepRelations.batch_restore. Restores CloudObjectStepRelations with given list of ids |
| CloudObjectStepRelations.create | `createCloudObjectStepRelation` | CloudObjectStepRelations.create. Creates new CloudObjectStepRelation |
| CloudObjectStepRelations.delete | `deleteCloudObjectStepRelation` | CloudObjectStepRelations.delete. Removes CloudObjectStepRelation with given id |
| CloudObjectStepRelations.get | `getCloudObjectStepRelation` | CloudObjectStepRelations.get. Returns CloudObjectStepRelation with given id |
| CloudObjectStepRelations.list | `listCloudObjectStepRelations` | CloudObjectStepRelations.list. Returns all defined CloudObjectStepRelations |
| CloudObjectStepRelations.update | `updateCloudObjectStepRelation` | CloudObjectStepRelations.update. Modifies CloudObjectStepRelation or CloudObjectStepRelations with given id(s) |
| CloudObjectTemplates.batch_create_or_update | `batchUpsertCloudObjectTemplates` | CloudObjectTemplates.batch_create_or_update. Create or update an batch of CloudObjectTemplates |
| CloudObjectTemplates.batch_delete | `batchDeleteCloudObjectTemplates` | CloudObjectTemplates.batch_delete. Removes CloudObjectTemplates with given list of ids |
| CloudObjectTemplates.batch_restore | `batchRestoreCloudObjectTemplates` | CloudObjectTemplates.batch_restore. Restores CloudObjectTemplates with given list of ids |
| CloudObjectTemplates.create | `createCloudObjectTemplate` | CloudObjectTemplates.create. Creates new CloudObjectTemplate |
| CloudObjectTemplates.delete | `deleteCloudObjectTemplate` | CloudObjectTemplates.delete. Removes CloudObjectTemplate with given id |
| CloudObjectTemplates.get | `getCloudObjectTemplate` | CloudObjectTemplates.get. Returns CloudObjectTemplate with given id |
| CloudObjectTemplates.list | `listCloudObjectTemplates` | CloudObjectTemplates.list. Returns all defined CloudObjectTemplates |
| CloudObjectTemplates.update | `updateCloudObjectTemplate` | CloudObjectTemplates.update. Modifies CloudObjectTemplate or CloudObjectTemplates with given id(s) |
| CompanyEmails.get | `getCompanyEmail` | CompanyEmails.get. Returns CompanyEmail with given id |
| CompanyEmails.list | `listCompanyEmails` | CompanyEmails.list. Returns all defined CompanyEmails |
| ContactAccountAccountRoleRelations.batch_create_or_update | `batchUpsertContactAccountAccountRoleRelations` | ContactAccountAccountRoleRelations.batch_create_or_update. Create or update an batch of ContactAccountAccountRoleRelations |
| ContactAccountAccountRoleRelations.batch_delete | `batchDeleteContactAccountAccountRoleRelations` | ContactAccountAccountRoleRelations.batch_delete. Removes ContactAccountAccountRoleRelations with given list of ids |
| ContactAccountAccountRoleRelations.batch_restore | `batchRestoreContactAccountAccountRoleRelations` | ContactAccountAccountRoleRelations.batch_restore. Restores ContactAccountAccountRoleRelations with given list of ids |
| ContactAccountAccountRoleRelations.create | `createContactAccountAccountRoleRelation` | ContactAccountAccountRoleRelations.create. Creates new ContactAccountAccountRoleRelation |
| ContactAccountAccountRoleRelations.delete | `deleteContactAccountAccountRoleRelation` | ContactAccountAccountRoleRelations.delete. Removes ContactAccountAccountRoleRelation with given id |
| ContactAccountAccountRoleRelations.get | `getContactAccountAccountRoleRelation` | ContactAccountAccountRoleRelations.get. Returns ContactAccountAccountRoleRelation with given id |
| ContactAccountAccountRoleRelations.list | `listContactAccountAccountRoleRelations` | ContactAccountAccountRoleRelations.list. Returns all defined ContactAccountAccountRoleRelations |
| ContactAccountAccountRoleRelations.update | `updateContactAccountAccountRoleRelation` | ContactAccountAccountRoleRelations.update. Modifies ContactAccountAccountRoleRelation or ContactAccountAccountRoleRelations with given id(s) |
| ContactAccountRelations.batch_create_or_update | `batchUpsertContactAccountRelations` | ContactAccountRelations.batch_create_or_update. Create or update an batch of ContactAccountRelations |
| ContactAccountRelations.batch_delete | `batchDeleteContactAccountRelations` | ContactAccountRelations.batch_delete. Removes ContactAccountRelations with given list of ids |
| ContactAccountRelations.batch_restore | `batchRestoreContactAccountRelations` | ContactAccountRelations.batch_restore. Restores ContactAccountRelations with given list of ids |
| ContactAccountRelations.create | `createContactAccountRelation` | ContactAccountRelations.create. Creates new ContactAccountRelation |
| ContactAccountRelations.delete | `deleteContactAccountRelation` | ContactAccountRelations.delete. Removes ContactAccountRelation with given id |
| ContactAccountRelations.get | `getContactAccountRelation` | ContactAccountRelations.get. Returns ContactAccountRelation with given id |
| ContactAccountRelations.list | `listContactAccountRelations` | ContactAccountRelations.list. Returns all defined ContactAccountRelations |
| ContactAccountRelations.update | `updateContactAccountRelation` | ContactAccountRelations.update. Modifies ContactAccountRelation or ContactAccountRelations with given id(s) |
| ContactDataExRelations.get | `getContactDataExRelation` | ContactDataExRelations.get. Returns ContactDataExRelation with given id |
| ContactDataExRelations.list | `listContactDataExRelations` | ContactDataExRelations.list. Returns all defined ContactDataExRelations |
| ContactKPIs.batch_create_or_update | `batchUpsertContactKPIs` | ContactKPIs.batch_create_or_update. Create or update an batch of ContactKPIs |
| ContactKPIs.batch_delete | `batchDeleteContactKPIs` | ContactKPIs.batch_delete. Removes ContactKPIs with given list of ids |
| ContactKPIs.batch_restore | `batchRestoreContactKPIs` | ContactKPIs.batch_restore. Restores ContactKPIs with given list of ids |
| ContactKPIs.create | `createContactKPI` | ContactKPIs.create. Creates new ContactKPI |
| ContactKPIs.delete | `deleteContactKPI` | ContactKPIs.delete. Removes ContactKPI with given id |
| ContactKPIs.get | `getContactKPI` | ContactKPIs.get. Returns ContactKPI with given id |
| ContactKPIs.list | `listContactKPIs` | ContactKPIs.list. Returns all defined ContactKPIs |
| ContactKPIs.update | `updateContactKPI` | ContactKPIs.update. Modifies ContactKPI or ContactKPIs with given id(s) |
| ContactRelationLabels.batch_create_or_update | `batchUpsertContactRelationLabels` | ContactRelationLabels.batch_create_or_update. Create or update an batch of ContactRelationLabels |
| ContactRelationLabels.batch_delete | `batchDeleteContactRelationLabels` | ContactRelationLabels.batch_delete. Removes ContactRelationLabels with given list of ids |
| ContactRelationLabels.batch_restore | `batchRestoreContactRelationLabels` | ContactRelationLabels.batch_restore. Restores ContactRelationLabels with given list of ids |
| ContactRelationLabels.create | `createContactRelationLabel` | ContactRelationLabels.create. Creates new ContactRelationLabel |
| ContactRelationLabels.delete | `deleteContactRelationLabel` | ContactRelationLabels.delete. Removes ContactRelationLabel with given id |
| ContactRelationLabels.get | `getContactRelationLabel` | ContactRelationLabels.get. Returns ContactRelationLabel with given id |
| ContactRelationLabels.list | `listContactRelationLabels` | ContactRelationLabels.list. Returns all defined ContactRelationLabels |
| ContactRelationLabels.update | `updateContactRelationLabel` | ContactRelationLabels.update. Modifies ContactRelationLabel or ContactRelationLabels with given id(s) |
| ContactRelations.batch_create_or_update | `batchUpsertContactRelations` | ContactRelations.batch_create_or_update. Create or update an batch of ContactRelations |
| ContactRelations.batch_delete | `batchDeleteContactRelations` | ContactRelations.batch_delete. Removes ContactRelations with given list of ids |
| ContactRelations.batch_restore | `batchRestoreContactRelations` | ContactRelations.batch_restore. Restores ContactRelations with given list of ids |
| ContactRelations.create | `createContactRelation` | ContactRelations.create. Creates new ContactRelation |
| ContactRelations.delete | `deleteContactRelation` | ContactRelations.delete. Removes ContactRelation with given id |
| ContactRelations.get | `getContactRelation` | ContactRelations.get. Returns ContactRelation with given id |
| ContactRelations.list | `listContactRelations` | ContactRelations.list. Returns all defined ContactRelations |
| ContactRelations.update | `updateContactRelation` | ContactRelations.update. Modifies ContactRelation or ContactRelations with given id(s) |
| ContactRelationTypes.batch_create_or_update | `batchUpsertContactRelationTypes` | ContactRelationTypes.batch_create_or_update. Create or update an batch of ContactRelationTypes |
| ContactRelationTypes.batch_delete | `batchDeleteContactRelationTypes` | ContactRelationTypes.batch_delete. Removes ContactRelationTypes with given list of ids |
| ContactRelationTypes.batch_restore | `batchRestoreContactRelationTypes` | ContactRelationTypes.batch_restore. Restores ContactRelationTypes with given list of ids |
| ContactRelationTypes.create | `createContactRelationType` | ContactRelationTypes.create. Creates new ContactRelationType |
| ContactRelationTypes.delete | `deleteContactRelationType` | ContactRelationTypes.delete. Removes ContactRelationType with given id |
| ContactRelationTypes.get | `getContactRelationType` | ContactRelationTypes.get. Returns ContactRelationType with given id |
| ContactRelationTypes.list | `listContactRelationTypes` | ContactRelationTypes.list. Returns all defined ContactRelationTypes |
| ContactRelationTypes.update | `updateContactRelationType` | ContactRelationTypes.update. Modifies ContactRelationType or ContactRelationTypes with given id(s) |
| Contacts.batch_create_or_update | `batchUpsertContacts` | Contacts.batch_create_or_update. Create or update an batch of Contacts |
| Contacts.batch_delete | `batchDeleteContacts` | Contacts.batch_delete. Removes Contacts with given list of ids |
| Contacts.batch_restore | `batchRestoreContacts` | Contacts.batch_restore. Restores Contacts with given list of ids |
| Contacts.merge | `mergeContacts` | Contacts.merge. Merger multiple Contacts into master record. |
| ContactSharingClientRelations.batch_create_or_update | `batchUpsertContactSharingClientRelations` | ContactSharingClientRelations.batch_create_or_update. Create or update an batch of ContactSharingClientRelations |
| ContactSharingClientRelations.batch_delete | `batchDeleteContactSharingClientRelations` | ContactSharingClientRelations.batch_delete. Removes ContactSharingClientRelations with given list of ids |
| ContactSharingClientRelations.batch_restore | `batchRestoreContactSharingClientRelations` | ContactSharingClientRelations.batch_restore. Restores ContactSharingClientRelations with given list of ids |
| ContactSharingClientRelations.create | `createContactSharingClientRelation` | ContactSharingClientRelations.create. Creates new ContactSharingClientRelation |
| ContactSharingClientRelations.delete | `deleteContactSharingClientRelation` | ContactSharingClientRelations.delete. Removes ContactSharingClientRelation with given id |
| ContactSharingClientRelations.get | `getContactSharingClientRelation` | ContactSharingClientRelations.get. Returns ContactSharingClientRelation with given id |
| ContactSharingClientRelations.list | `listContactSharingClientRelations` | ContactSharingClientRelations.list. Returns all defined ContactSharingClientRelations |
| ContactSharingClientRelations.update | `updateContactSharingClientRelation` | ContactSharingClientRelations.update. Modifies ContactSharingClientRelation or ContactSharingClientRelations with given id(s) |
| ContactSharingSalesUnitRelations.batch_create_or_update | `batchUpsertContactSharingSalesUnitRelations` | ContactSharingSalesUnitRelations.batch_create_or_update. Create or update an batch of ContactSharingSalesUnitRelations |
| ContactSharingSalesUnitRelations.batch_delete | `batchDeleteContactSharingSalesUnitRelations` | ContactSharingSalesUnitRelations.batch_delete. Removes ContactSharingSalesUnitRelations with given list of ids |
| ContactSharingSalesUnitRelations.batch_restore | `batchRestoreContactSharingSalesUnitRelations` | ContactSharingSalesUnitRelations.batch_restore. Restores ContactSharingSalesUnitRelations with given list of ids |
| ContactSharingSalesUnitRelations.create | `createContactSharingSalesUnitRelation` | ContactSharingSalesUnitRelations.create. Creates new ContactSharingSalesUnitRelation |
| ContactSharingSalesUnitRelations.delete | `deleteContactSharingSalesUnitRelation` | ContactSharingSalesUnitRelations.delete. Removes ContactSharingSalesUnitRelation with given id |
| ContactSharingSalesUnitRelations.get | `getContactSharingSalesUnitRelation` | ContactSharingSalesUnitRelations.get. Returns ContactSharingSalesUnitRelation with given id |
| ContactSharingSalesUnitRelations.list | `listContactSharingSalesUnitRelations` | ContactSharingSalesUnitRelations.list. Returns all defined ContactSharingSalesUnitRelations |
| ContactSharingSalesUnitRelations.update | `updateContactSharingSalesUnitRelation` | ContactSharingSalesUnitRelations.update. Modifies ContactSharingSalesUnitRelation or ContactSharingSalesUnitRelations with given id(s) |
| ContactSocialRelations.batch_create_or_update | `batchUpsertContactSocialRelations` | ContactSocialRelations.batch_create_or_update. Create or update an batch of ContactSocialRelations |
| ContactSocialRelations.batch_delete | `batchDeleteContactSocialRelations` | ContactSocialRelations.batch_delete. Removes ContactSocialRelations with given list of ids |
| ContactSocialRelations.batch_restore | `batchRestoreContactSocialRelations` | ContactSocialRelations.batch_restore. Restores ContactSocialRelations with given list of ids |
| ContactSocialRelations.create | `createContactSocialRelation` | ContactSocialRelations.create. Creates new ContactSocialRelation |
| ContactSocialRelations.delete | `deleteContactSocialRelation` | ContactSocialRelations.delete. Removes ContactSocialRelation with given id |
| ContactSocialRelations.get | `getContactSocialRelation` | ContactSocialRelations.get. Returns ContactSocialRelation with given id |
| ContactSocialRelations.list | `listContactSocialRelations` | ContactSocialRelations.list. Returns all defined ContactSocialRelations |
| ContactSocialRelations.update | `updateContactSocialRelation` | ContactSocialRelations.update. Modifies ContactSocialRelation or ContactSocialRelations with given id(s) |
| ContactTypes.batch_create_or_update | `batchUpsertContactTypes` | ContactTypes.batch_create_or_update. Create or update an batch of ContactTypes |
| ContactTypes.batch_delete | `batchDeleteContactTypes` | ContactTypes.batch_delete. Removes ContactTypes with given list of ids |
| ContactTypes.batch_restore | `batchRestoreContactTypes` | ContactTypes.batch_restore. Restores ContactTypes with given list of ids |
| ContactTypes.create | `createContactType` | ContactTypes.create. Creates new ContactType |
| ContactTypes.delete | `deleteContactType` | ContactTypes.delete. Removes ContactType with given id |
| ContactTypes.get | `getContactType` | ContactTypes.get. Returns ContactType with given id |
| ContactTypes.list | `listContactTypes` | ContactTypes.list. Returns all defined ContactTypes |
| ContactTypes.update | `updateContactType` | ContactTypes.update. Modifies ContactType or ContactTypes with given id(s) |
| CountryCrms.batch_create_or_update | `batchUpsertCountryCrms` | CountryCrms.batch_create_or_update. Create or update an batch of CountryCrms |
| CountryCrms.batch_delete | `batchDeleteCountryCrms` | CountryCrms.batch_delete. Removes CountryCrms with given list of ids |
| CountryCrms.batch_restore | `batchRestoreCountryCrms` | CountryCrms.batch_restore. Restores CountryCrms with given list of ids |
| CountryCrms.create | `createCountryCrm` | CountryCrms.create. Creates new CountryCrm |
| CountryCrms.delete | `deleteCountryCrm` | CountryCrms.delete. Removes CountryCrm with given id |
| CountryCrms.get | `getCountryCrm` | CountryCrms.get. Returns CountryCrm with given id |
| CountryCrms.list | `listCountryCrms` | CountryCrms.list. Returns all defined CountryCrms |
| CountryCrms.update | `updateCountryCrm` | CountryCrms.update. Modifies CountryCrm or CountryCrms with given id(s) |
| Create Account | `createAccount` | Accounts.create. Creates new Account |
| Create Account KPI | `createAccountKPI` | AccountKPIs.create. Creates new AccountKPI |
| Create Account Product Pricing | `createAccountProductPricing` | AccountProductPricings.create. Creates new AccountProductPricing |
| Create Account Relation Label | `createAccountRelationLabel` | AccountRelationLabels.create. Creates new AccountRelationLabel |
| Create Account Relation Type | `createAccountRelationType` | AccountRelationTypes.create. Creates new AccountRelationType |
| Create Account Role | `createAccountRole` | AccountRoles.create. Creates new AccountRole |
| Create Account Sharing Client Relation | `createAccountSharingClientRelation` | AccountSharingClientRelations.create. Creates new AccountSharingClientRelation |
| Create Account Sharing Sales Unit Relation | `createAccountSharingSalesUnitRelation` | AccountSharingSalesUnitRelations.create. Creates new AccountSharingSalesUnitRelation |
| Create Contact | `createContact` | Contacts.create. Creates new Contact |
| Create Custom Field | `createField` | Fields.create. Creates new Field |
| Create Lead | `createLead` | Leads.create. Creates new Lead |
| Create Opportunity | `createOpportunity` | Opportunities.create. Creates new Opportunity |
| Create Pipeline | `createPipeline` | Pipelines.create. Creates new Pipeline |
| Create Product | `createProduct` | Products.create. Creates new Product |
| Create Quote | `createQuote` | Quotes.create. Creates new Quote |
| Create Task | `createTask` | Tasks.create. Creates new Task |
| Create Webhook | `createWebhook` | Webhooks.create. Creates new Webhook |
| Currencies.batch_create_or_update | `batchUpsertCurrencies` | Currencies.batch_create_or_update. Create or update an batch of Currencies |
| Currencies.batch_delete | `batchDeleteCurrencies` | Currencies.batch_delete. Removes Currencies with given list of ids |
| Currencies.batch_restore | `batchRestoreCurrencies` | Currencies.batch_restore. Restores Currencies with given list of ids |
| Currencies.create | `createCurrency` | Currencies.create. Creates new Currency |
| Currencies.delete | `deleteCurrency` | Currencies.delete. Removes Currency with given id |
| Currencies.get | `getCurrency` | Currencies.get. Returns Currency with given id |
| Currencies.list | `listCurrencies` | Currencies.list. Returns all defined Currencies |
| Currencies.update | `updateCurrency` | Currencies.update. Modifies Currency or Currencies with given id(s) |
| CurrencyExchangeRates.batch_create_or_update | `batchUpsertCurrencyExchangeRates` | CurrencyExchangeRates.batch_create_or_update. Create or update an batch of CurrencyExchangeRates |
| CurrencyExchangeRates.batch_delete | `batchDeleteCurrencyExchangeRates` | CurrencyExchangeRates.batch_delete. Removes CurrencyExchangeRates with given list of ids |
| CurrencyExchangeRates.batch_restore | `batchRestoreCurrencyExchangeRates` | CurrencyExchangeRates.batch_restore. Restores CurrencyExchangeRates with given list of ids |
| CurrencyExchangeRates.create | `createCurrencyExchangeRate` | CurrencyExchangeRates.create. Creates new CurrencyExchangeRate |
| CurrencyExchangeRates.delete | `deleteCurrencyExchangeRate` | CurrencyExchangeRates.delete. Removes CurrencyExchangeRate with given id |
| CurrencyExchangeRates.get | `getCurrencyExchangeRate` | CurrencyExchangeRates.get. Returns CurrencyExchangeRate with given id |
| CurrencyExchangeRates.list | `listCurrencyExchangeRates` | CurrencyExchangeRates.list. Returns all defined CurrencyExchangeRates |
| CurrencyExchangeRates.update | `updateCurrencyExchangeRate` | CurrencyExchangeRates.update. Modifies CurrencyExchangeRate or CurrencyExchangeRates with given id(s) |
| CurrencyExchangeRatesLists.batch_create_or_update | `batchUpsertCurrencyExchangeRatesLists` | CurrencyExchangeRatesLists.batch_create_or_update. Create or update an batch of CurrencyExchangeRatesLists |
| CurrencyExchangeRatesLists.batch_delete | `batchDeleteCurrencyExchangeRatesLists` | CurrencyExchangeRatesLists.batch_delete. Removes CurrencyExchangeRatesLists with given list of ids |
| CurrencyExchangeRatesLists.batch_restore | `batchRestoreCurrencyExchangeRatesLists` | CurrencyExchangeRatesLists.batch_restore. Restores CurrencyExchangeRatesLists with given list of ids |
| CurrencyExchangeRatesLists.create | `createCurrencyExchangeRatesList` | CurrencyExchangeRatesLists.create. Creates new CurrencyExchangeRatesList |
| CurrencyExchangeRatesLists.delete | `deleteCurrencyExchangeRatesList` | CurrencyExchangeRatesLists.delete. Removes CurrencyExchangeRatesList with given id |
| CurrencyExchangeRatesLists.get | `getCurrencyExchangeRatesList` | CurrencyExchangeRatesLists.get. Returns CurrencyExchangeRatesList with given id |
| CurrencyExchangeRatesLists.list | `listCurrencyExchangeRatesLists` | CurrencyExchangeRatesLists.list. Returns all defined CurrencyExchangeRatesLists |
| CurrencyExchangeRatesLists.update | `updateCurrencyExchangeRatesList` | CurrencyExchangeRatesLists.update. Modifies CurrencyExchangeRatesList or CurrencyExchangeRatesLists with given id(s) |
| CustomEntities.batch_create_or_update | `batchUpsertCustomEntityRecord` | CustomEntities.batch_create_or_update. Create or update an batch of {custom_entity_api_name} |
| CustomEntities.batch_delete | `batchDeleteCustomEntityRecord` | CustomEntities.batch_delete. Removes {custom_entity_api_name} with given list of ids |
| CustomEntities.batch_restore | `batchRestoreCustomEntityRecord` | CustomEntities.batch_restore. Restores {custom_entity_api_name} with given list of ids |
| CustomEntities.create | `createCustomEntityRecord` | CustomEntities.create. Creates new CustomEntity |
| CustomEntities.delete | `deleteCustomEntityRecord` | CustomEntities.delete. Removes CustomEntity with given id |
| CustomEntities.get | `getCustomEntityRecord` | CustomEntities.get. Returns CustomEntity with given id |
| CustomEntities.list | `listCustomEntityRecord` | CustomEntities.list. Returns all defined {custom_entity_api_name} |
| CustomEntities.update | `updateCustomEntityRecord` | CustomEntities.update. Modifies CustomEntity or {custom_entity_api_name} with given id(s) |
| CustomEntityTypes.batch_create_or_update | `batchUpsertCustomEntityTypeRecord` | CustomEntityTypes.batch_create_or_update. Create or update an batch of {custom_entity_type_api_name} |
| CustomEntityTypes.batch_delete | `batchDeleteCustomEntityTypeRecord` | CustomEntityTypes.batch_delete. Removes {custom_entity_type_api_name} with given list of ids |
| CustomEntityTypes.batch_restore | `batchRestoreCustomEntityTypeRecord` | CustomEntityTypes.batch_restore. Restores {custom_entity_type_api_name} with given list of ids |
| CustomEntityTypes.create | `createCustomEntityTypeRecord` | CustomEntityTypes.create. Creates new CustomEntityType |
| CustomEntityTypes.delete | `deleteCustomEntityTypeRecord` | CustomEntityTypes.delete. Removes CustomEntityType with given id |
| CustomEntityTypes.get | `getCustomEntityTypeRecord` | CustomEntityTypes.get. Returns CustomEntityType with given id |
| CustomEntityTypes.list | `listCustomEntityTypeRecord` | CustomEntityTypes.list. Returns all defined {custom_entity_type_api_name} |
| CustomEntityTypes.update | `updateCustomEntityTypeRecord` | CustomEntityTypes.update. Modifies CustomEntityType or {custom_entity_type_api_name} with given id(s) |
| Data.batch_create_or_update | `batchUpsertData` | Data.batch_create_or_update. Create or update an batch of Data |
| Data.batch_delete | `batchDeleteData` | Data.batch_delete. Removes Data with given list of ids |
| Data.batch_restore | `batchRestoreData` | Data.batch_restore. Restores Data with given list of ids |
| Data.create | `createData` | Data.create. Creates new Data |
| Data.delete | `deleteData` | Data.delete. Removes Data with given id |
| Data.get | `getData` | Data.get. Returns Data with given id |
| Data.list | `listData` | Data.list. Returns all defined Data |
| Data.update | `updateData` | Data.update. Modifies Data or Data with given id(s) |
| Delete Account | `deleteAccount` | Accounts.delete. Removes Account with given id |
| Delete Account KPI | `deleteAccountKPI` | AccountKPIs.delete. Removes AccountKPI with given id |
| Delete Account Product Pricing | `deleteAccountProductPricing` | AccountProductPricings.delete. Removes AccountProductPricing with given id |
| Delete Account Relation | `deleteAccountRelation` | AccountRelations.delete. Removes AccountRelation with given id |
| Delete Account Relation Label | `deleteAccountRelationLabel` | AccountRelationLabels.delete. Removes AccountRelationLabel with given id |
| Delete Account Relation Type | `deleteAccountRelationType` | AccountRelationTypes.delete. Removes AccountRelationType with given id |
| Delete Account Role | `deleteAccountRole` | AccountRoles.delete. Removes AccountRole with given id |
| Delete Account Sharing Client Relation | `deleteAccountSharingClientRelation` | AccountSharingClientRelations.delete. Removes AccountSharingClientRelation with given id |
| Delete Account Sharing Sales Unit Relation | `deleteAccountSharingSalesUnitRelation` | AccountSharingSalesUnitRelations.delete. Removes AccountSharingSalesUnitRelation with given id |
| Delete Contact | `deleteContact` | Contacts.delete. Removes Contact with given id |
| Delete Custom Field | `deleteField` | Fields.delete. Removes Field with given id |
| Delete Lead | `deleteLead` | Leads.delete. Removes Lead with given id |
| Delete Opportunity | `deleteOpportunity` | Opportunities.delete. Removes Opportunity with given id |
| Delete Pipeline | `deletePipeline` | Pipelines.delete. Removes Pipeline with given id |
| Delete Product | `deleteProduct` | Products.delete. Removes Product with given id |
| Delete Quote | `deleteQuote` | Quotes.delete. Removes Quote with given id |
| Delete Task | `deleteTask` | Tasks.delete. Removes Task with given id |
| Delete Webhook | `deleteWebhook` | Webhooks.delete. Removes Webhook with given id |
| EmailContentSharingClientRelations.batch_create_or_update | `batchUpsertEmailContentSharingClientRelations` | EmailContentSharingClientRelations.batch_create_or_update. Create or update an batch of EmailContentSharingClientRelations |
| EmailContentSharingClientRelations.batch_delete | `batchDeleteEmailContentSharingClientRelations` | EmailContentSharingClientRelations.batch_delete. Removes EmailContentSharingClientRelations with given list of ids |
| EmailContentSharingClientRelations.batch_restore | `batchRestoreEmailContentSharingClientRelations` | EmailContentSharingClientRelations.batch_restore. Restores EmailContentSharingClientRelations with given list of ids |
| EmailContentSharingClientRelations.create | `createEmailContentSharingClientRelation` | EmailContentSharingClientRelations.create. Creates new EmailContentSharingClientRelation |
| EmailContentSharingClientRelations.delete | `deleteEmailContentSharingClientRelation` | EmailContentSharingClientRelations.delete. Removes EmailContentSharingClientRelation with given id |
| EmailContentSharingClientRelations.get | `getEmailContentSharingClientRelation` | EmailContentSharingClientRelations.get. Returns EmailContentSharingClientRelation with given id |
| EmailContentSharingClientRelations.list | `listEmailContentSharingClientRelations` | EmailContentSharingClientRelations.list. Returns all defined EmailContentSharingClientRelations |
| EmailContentSharingClientRelations.update | `updateEmailContentSharingClientRelation` | EmailContentSharingClientRelations.update. Modifies EmailContentSharingClientRelation or EmailContentSharingClientRelations with given id(s) |
| EmailContentSharingSalesUnitRelations.batch_create_or_update | `batchUpsertEmailContentSharingSalesUnitRelations` | EmailContentSharingSalesUnitRelations.batch_create_or_update. Create or update an batch of EmailContentSharingSalesUnitRelations |
| EmailContentSharingSalesUnitRelations.batch_delete | `batchDeleteEmailContentSharingSalesUnitRelations` | EmailContentSharingSalesUnitRelations.batch_delete. Removes EmailContentSharingSalesUnitRelations with given list of ids |
| EmailContentSharingSalesUnitRelations.batch_restore | `batchRestoreEmailContentSharingSalesUnitRelations` | EmailContentSharingSalesUnitRelations.batch_restore. Restores EmailContentSharingSalesUnitRelations with given list of ids |
| EmailContentSharingSalesUnitRelations.create | `createEmailContentSharingSalesUnitRelation` | EmailContentSharingSalesUnitRelations.create. Creates new EmailContentSharingSalesUnitRelation |
| EmailContentSharingSalesUnitRelations.delete | `deleteEmailContentSharingSalesUnitRelation` | EmailContentSharingSalesUnitRelations.delete. Removes EmailContentSharingSalesUnitRelation with given id |
| EmailContentSharingSalesUnitRelations.get | `getEmailContentSharingSalesUnitRelation` | EmailContentSharingSalesUnitRelations.get. Returns EmailContentSharingSalesUnitRelation with given id |
| EmailContentSharingSalesUnitRelations.list | `listEmailContentSharingSalesUnitRelations` | EmailContentSharingSalesUnitRelations.list. Returns all defined EmailContentSharingSalesUnitRelations |
| EmailContentSharingSalesUnitRelations.update | `updateEmailContentSharingSalesUnitRelation` | EmailContentSharingSalesUnitRelations.update. Modifies EmailContentSharingSalesUnitRelation or EmailContentSharingSalesUnitRelations with given id(s) |
| EmailEvents.batch_create_or_update | `batchUpsertEmailEvents` | EmailEvents.batch_create_or_update. Create or update an batch of EmailEvents |
| EmailEvents.batch_delete | `batchDeleteEmailEvents` | EmailEvents.batch_delete. Removes EmailEvents with given list of ids |
| EmailEvents.batch_restore | `batchRestoreEmailEvents` | EmailEvents.batch_restore. Restores EmailEvents with given list of ids |
| EmailEvents.create | `createEmailEvent` | EmailEvents.create. Creates new EmailEvent |
| EmailEvents.delete | `deleteEmailEvent` | EmailEvents.delete. Removes EmailEvent with given id |
| EmailEvents.get | `getEmailEvent` | EmailEvents.get. Returns EmailEvent with given id |
| EmailEvents.list | `listEmailEvents` | EmailEvents.list. Returns all defined EmailEvents |
| EmailEvents.update | `updateEmailEvent` | EmailEvents.update. Modifies EmailEvent or EmailEvents with given id(s) |
| EmailLabelRelations.batch_create_or_update | `batchUpsertEmailLabelRelations` | EmailLabelRelations.batch_create_or_update. Create or update an batch of EmailLabelRelations |
| EmailLabelRelations.batch_delete | `batchDeleteEmailLabelRelations` | EmailLabelRelations.batch_delete. Removes EmailLabelRelations with given list of ids |
| EmailLabelRelations.batch_restore | `batchRestoreEmailLabelRelations` | EmailLabelRelations.batch_restore. Restores EmailLabelRelations with given list of ids |
| EmailLabelRelations.create | `createEmailLabelRelation` | EmailLabelRelations.create. Creates new EmailLabelRelation |
| EmailLabelRelations.delete | `deleteEmailLabelRelation` | EmailLabelRelations.delete. Removes EmailLabelRelation with given id |
| EmailLabelRelations.get | `getEmailLabelRelation` | EmailLabelRelations.get. Returns EmailLabelRelation with given id |
| EmailLabelRelations.list | `listEmailLabelRelations` | EmailLabelRelations.list. Returns all defined EmailLabelRelations |
| EmailLabelRelations.update | `updateEmailLabelRelation` | EmailLabelRelations.update. Modifies EmailLabelRelation or EmailLabelRelations with given id(s) |
| EmailLabels.batch_create_or_update | `batchUpsertEmailLabels` | EmailLabels.batch_create_or_update. Create or update an batch of EmailLabels |
| EmailLabels.batch_delete | `batchDeleteEmailLabels` | EmailLabels.batch_delete. Removes EmailLabels with given list of ids |
| EmailLabels.batch_restore | `batchRestoreEmailLabels` | EmailLabels.batch_restore. Restores EmailLabels with given list of ids |
| EmailLabels.create | `createEmailLabel` | EmailLabels.create. Creates new EmailLabel |
| EmailLabels.delete | `deleteEmailLabel` | EmailLabels.delete. Removes EmailLabel with given id |
| EmailLabels.get | `getEmailLabel` | EmailLabels.get. Returns EmailLabel with given id |
| EmailLabels.list | `listEmailLabels` | EmailLabels.list. Returns all defined EmailLabels |
| EmailLabels.update | `updateEmailLabel` | EmailLabels.update. Modifies EmailLabel or EmailLabels with given id(s) |
| EmailMailboxRelations.batch_create_or_update | `batchUpsertEmailMailboxRelations` | EmailMailboxRelations.batch_create_or_update. Create or update an batch of EmailMailboxRelations |
| EmailMailboxRelations.batch_delete | `batchDeleteEmailMailboxRelations` | EmailMailboxRelations.batch_delete. Removes EmailMailboxRelations with given list of ids |
| EmailMailboxRelations.batch_restore | `batchRestoreEmailMailboxRelations` | EmailMailboxRelations.batch_restore. Restores EmailMailboxRelations with given list of ids |
| EmailMailboxRelations.create | `createEmailMailboxRelation` | EmailMailboxRelations.create. Creates new EmailMailboxRelation |
| EmailMailboxRelations.delete | `deleteEmailMailboxRelation` | EmailMailboxRelations.delete. Removes EmailMailboxRelation with given id |
| EmailMailboxRelations.get | `getEmailMailboxRelation` | EmailMailboxRelations.get. Returns EmailMailboxRelation with given id |
| EmailMailboxRelations.list | `listEmailMailboxRelations` | EmailMailboxRelations.list. Returns all defined EmailMailboxRelations |
| EmailMailboxRelations.update | `updateEmailMailboxRelation` | EmailMailboxRelations.update. Modifies EmailMailboxRelation or EmailMailboxRelations with given id(s) |
| Emails.batch_create_or_update | `batchUpsertEmails` | Emails.batch_create_or_update. Create or update an batch of Emails |
| Emails.batch_delete | `batchDeleteEmails` | Emails.batch_delete. Removes Emails with given list of ids |
| Emails.batch_restore | `batchRestoreEmails` | Emails.batch_restore. Restores Emails with given list of ids |
| Emails.create | `createEmail` | Emails.create. Creates new Email |
| Emails.delete | `deleteEmail` | Emails.delete. Removes Email with given id |
| Emails.get | `getEmail` | Emails.get. Returns Email with given id |
| Emails.list | `listEmails` | Emails.list. Returns all defined Emails |
| Emails.update | `updateEmail` | Emails.update. Modifies Email or Emails with given id(s) |
| EmailSequenceActivityLogLines.batch_create_or_update | `batchUpsertEmailSequenceActivityLogLines` | EmailSequenceActivityLogLines.batch_create_or_update. Create or update an batch of EmailSequenceActivityLogLines |
| EmailSequenceActivityLogLines.batch_delete | `batchDeleteEmailSequenceActivityLogLines` | EmailSequenceActivityLogLines.batch_delete. Removes EmailSequenceActivityLogLines with given list of ids |
| EmailSequenceActivityLogLines.batch_restore | `batchRestoreEmailSequenceActivityLogLines` | EmailSequenceActivityLogLines.batch_restore. Restores EmailSequenceActivityLogLines with given list of ids |
| EmailSequenceActivityLogLines.create | `createEmailSequenceActivityLogLine` | EmailSequenceActivityLogLines.create. Creates new EmailSequenceActivityLogLine |
| EmailSequenceActivityLogLines.delete | `deleteEmailSequenceActivityLogLine` | EmailSequenceActivityLogLines.delete. Removes EmailSequenceActivityLogLine with given id |
| EmailSequenceActivityLogLines.get | `getEmailSequenceActivityLogLine` | EmailSequenceActivityLogLines.get. Returns EmailSequenceActivityLogLine with given id |
| EmailSequenceActivityLogLines.list | `listEmailSequenceActivityLogLines` | EmailSequenceActivityLogLines.list. Returns all defined EmailSequenceActivityLogLines |
| EmailSequenceActivityLogLines.update | `updateEmailSequenceActivityLogLine` | EmailSequenceActivityLogLines.update. Modifies EmailSequenceActivityLogLine or EmailSequenceActivityLogLines with given id(s) |
| EmailSequenceActivityLogs.batch_create_or_update | `batchUpsertEmailSequenceActivityLogs` | EmailSequenceActivityLogs.batch_create_or_update. Create or update an batch of EmailSequenceActivityLogs |
| EmailSequenceActivityLogs.batch_delete | `batchDeleteEmailSequenceActivityLogs` | EmailSequenceActivityLogs.batch_delete. Removes EmailSequenceActivityLogs with given list of ids |
| EmailSequenceActivityLogs.batch_restore | `batchRestoreEmailSequenceActivityLogs` | EmailSequenceActivityLogs.batch_restore. Restores EmailSequenceActivityLogs with given list of ids |
| EmailSequenceActivityLogs.create | `createEmailSequenceActivityLog` | EmailSequenceActivityLogs.create. Creates new EmailSequenceActivityLog |
| EmailSequenceActivityLogs.delete | `deleteEmailSequenceActivityLog` | EmailSequenceActivityLogs.delete. Removes EmailSequenceActivityLog with given id |
| EmailSequenceActivityLogs.get | `getEmailSequenceActivityLog` | EmailSequenceActivityLogs.get. Returns EmailSequenceActivityLog with given id |
| EmailSequenceActivityLogs.list | `listEmailSequenceActivityLogs` | EmailSequenceActivityLogs.list. Returns all defined EmailSequenceActivityLogs |
| EmailSequenceActivityLogs.update | `updateEmailSequenceActivityLog` | EmailSequenceActivityLogs.update. Modifies EmailSequenceActivityLog or EmailSequenceActivityLogs with given id(s) |
| EmailSequenceEnrolleds.batch_create_or_update | `batchUpsertEmailSequenceEnrolleds` | EmailSequenceEnrolleds.batch_create_or_update. Create or update an batch of EmailSequenceEnrolleds |
| EmailSequenceEnrolleds.batch_delete | `batchDeleteEmailSequenceEnrolleds` | EmailSequenceEnrolleds.batch_delete. Removes EmailSequenceEnrolleds with given list of ids |
| EmailSequenceEnrolleds.batch_restore | `batchRestoreEmailSequenceEnrolleds` | EmailSequenceEnrolleds.batch_restore. Restores EmailSequenceEnrolleds with given list of ids |
| EmailSequenceEnrolleds.create | `createEmailSequenceEnrolled` | EmailSequenceEnrolleds.create. Creates new EmailSequenceEnrolled |
| EmailSequenceEnrolleds.delete | `deleteEmailSequenceEnrolled` | EmailSequenceEnrolleds.delete. Removes EmailSequenceEnrolled with given id |
| EmailSequenceEnrolleds.get | `getEmailSequenceEnrolled` | EmailSequenceEnrolleds.get. Returns EmailSequenceEnrolled with given id |
| EmailSequenceEnrolleds.list | `listEmailSequenceEnrolleds` | EmailSequenceEnrolleds.list. Returns all defined EmailSequenceEnrolleds |
| EmailSequenceEnrolleds.update | `updateEmailSequenceEnrolled` | EmailSequenceEnrolleds.update. Modifies EmailSequenceEnrolled or EmailSequenceEnrolleds with given id(s) |
| EmailSequences.batch_create_or_update | `batchUpsertEmailSequences` | EmailSequences.batch_create_or_update. Create or update an batch of EmailSequences |
| EmailSequences.batch_delete | `batchDeleteEmailSequences` | EmailSequences.batch_delete. Removes EmailSequences with given list of ids |
| EmailSequences.batch_restore | `batchRestoreEmailSequences` | EmailSequences.batch_restore. Restores EmailSequences with given list of ids |
| EmailSequences.create | `createEmailSequence` | EmailSequences.create. Creates new EmailSequence |
| EmailSequences.delete | `deleteEmailSequence` | EmailSequences.delete. Removes EmailSequence with given id |
| EmailSequences.get | `getEmailSequence` | EmailSequences.get. Returns EmailSequence with given id |
| EmailSequences.list | `listEmailSequences` | EmailSequences.list. Returns all defined EmailSequences |
| EmailSequences.update | `updateEmailSequence` | EmailSequences.update. Modifies EmailSequence or EmailSequences with given id(s) |
| EmailTemplateFolders.batch_create_or_update | `batchUpsertEmailTemplateFolders` | EmailTemplateFolders.batch_create_or_update. Create or update an batch of EmailTemplateFolders |
| EmailTemplateFolders.batch_delete | `batchDeleteEmailTemplateFolders` | EmailTemplateFolders.batch_delete. Removes EmailTemplateFolders with given list of ids |
| EmailTemplateFolders.batch_restore | `batchRestoreEmailTemplateFolders` | EmailTemplateFolders.batch_restore. Restores EmailTemplateFolders with given list of ids |
| EmailTemplateFolders.create | `createEmailTemplateFolder` | EmailTemplateFolders.create. Creates new EmailTemplateFolder |
| EmailTemplateFolders.delete | `deleteEmailTemplateFolder` | EmailTemplateFolders.delete. Removes EmailTemplateFolder with given id |
| EmailTemplateFolders.get | `getEmailTemplateFolder` | EmailTemplateFolders.get. Returns EmailTemplateFolder with given id |
| EmailTemplateFolders.list | `listEmailTemplateFolders` | EmailTemplateFolders.list. Returns all defined EmailTemplateFolders |
| EmailTemplateFolders.update | `updateEmailTemplateFolder` | EmailTemplateFolders.update. Modifies EmailTemplateFolder or EmailTemplateFolders with given id(s) |
| EmailTemplates.batch_create_or_update | `batchUpsertEmailTemplates` | EmailTemplates.batch_create_or_update. Create or update an batch of EmailTemplates |
| EmailTemplates.batch_delete | `batchDeleteEmailTemplates` | EmailTemplates.batch_delete. Removes EmailTemplates with given list of ids |
| EmailTemplates.batch_restore | `batchRestoreEmailTemplates` | EmailTemplates.batch_restore. Restores EmailTemplates with given list of ids |
| EmailTemplates.create | `createEmailTemplate` | EmailTemplates.create. Creates new EmailTemplate |
| EmailTemplates.delete | `deleteEmailTemplate` | EmailTemplates.delete. Removes EmailTemplate with given id |
| EmailTemplates.get | `getEmailTemplate` | EmailTemplates.get. Returns EmailTemplate with given id |
| EmailTemplates.list | `listEmailTemplates` | EmailTemplates.list. Returns all defined EmailTemplates |
| EmailTemplates.update | `updateEmailTemplate` | EmailTemplates.update. Modifies EmailTemplate or EmailTemplates with given id(s) |
| EmailTemplateSharingClientRelations.batch_create_or_update | `batchUpsertEmailTemplateSharingClientRelations` | EmailTemplateSharingClientRelations.batch_create_or_update. Create or update an batch of EmailTemplateSharingClientRelations |
| EmailTemplateSharingClientRelations.batch_delete | `batchDeleteEmailTemplateSharingClientRelations` | EmailTemplateSharingClientRelations.batch_delete. Removes EmailTemplateSharingClientRelations with given list of ids |
| EmailTemplateSharingClientRelations.batch_restore | `batchRestoreEmailTemplateSharingClientRelations` | EmailTemplateSharingClientRelations.batch_restore. Restores EmailTemplateSharingClientRelations with given list of ids |
| EmailTemplateSharingClientRelations.create | `createEmailTemplateSharingClientRelation` | EmailTemplateSharingClientRelations.create. Creates new EmailTemplateSharingClientRelation |
| EmailTemplateSharingClientRelations.delete | `deleteEmailTemplateSharingClientRelation` | EmailTemplateSharingClientRelations.delete. Removes EmailTemplateSharingClientRelation with given id |
| EmailTemplateSharingClientRelations.get | `getEmailTemplateSharingClientRelation` | EmailTemplateSharingClientRelations.get. Returns EmailTemplateSharingClientRelation with given id |
| EmailTemplateSharingClientRelations.list | `listEmailTemplateSharingClientRelations` | EmailTemplateSharingClientRelations.list. Returns all defined EmailTemplateSharingClientRelations |
| EmailTemplateSharingClientRelations.update | `updateEmailTemplateSharingClientRelation` | EmailTemplateSharingClientRelations.update. Modifies EmailTemplateSharingClientRelation or EmailTemplateSharingClientRelations with given id(s) |
| EmailTemplateSharingSalesUnitRelations.batch_create_or_update | `batchUpsertEmailTemplateSharingSalesUnitRelations` | EmailTemplateSharingSalesUnitRelations.batch_create_or_update. Create or update an batch of EmailTemplateSharingSalesUnitRelations |
| EmailTemplateSharingSalesUnitRelations.batch_delete | `batchDeleteEmailTemplateSharingSalesUnitRelations` | EmailTemplateSharingSalesUnitRelations.batch_delete. Removes EmailTemplateSharingSalesUnitRelations with given list of ids |
| EmailTemplateSharingSalesUnitRelations.batch_restore | `batchRestoreEmailTemplateSharingSalesUnitRelations` | EmailTemplateSharingSalesUnitRelations.batch_restore. Restores EmailTemplateSharingSalesUnitRelations with given list of ids |
| EmailTemplateSharingSalesUnitRelations.create | `createEmailTemplateSharingSalesUnitRelation` | EmailTemplateSharingSalesUnitRelations.create. Creates new EmailTemplateSharingSalesUnitRelation |
| EmailTemplateSharingSalesUnitRelations.delete | `deleteEmailTemplateSharingSalesUnitRelation` | EmailTemplateSharingSalesUnitRelations.delete. Removes EmailTemplateSharingSalesUnitRelation with given id |
| EmailTemplateSharingSalesUnitRelations.get | `getEmailTemplateSharingSalesUnitRelation` | EmailTemplateSharingSalesUnitRelations.get. Returns EmailTemplateSharingSalesUnitRelation with given id |
| EmailTemplateSharingSalesUnitRelations.list | `listEmailTemplateSharingSalesUnitRelations` | EmailTemplateSharingSalesUnitRelations.list. Returns all defined EmailTemplateSharingSalesUnitRelations |
| EmailTemplateSharingSalesUnitRelations.update | `updateEmailTemplateSharingSalesUnitRelation` | EmailTemplateSharingSalesUnitRelations.update. Modifies EmailTemplateSharingSalesUnitRelation or EmailTemplateSharingSalesUnitRelations with given id(s) |
| EmailThreadMailboxClientReadStates.batch_create_or_update | `batchUpsertEmailThreadMailboxClientReadStates` | EmailThreadMailboxClientReadStates.batch_create_or_update. Create or update an batch of EmailThreadMailboxClientReadStates |
| EmailThreadMailboxClientReadStates.batch_delete | `batchDeleteEmailThreadMailboxClientReadStates` | EmailThreadMailboxClientReadStates.batch_delete. Removes EmailThreadMailboxClientReadStates with given list of ids |
| EmailThreadMailboxClientReadStates.batch_restore | `batchRestoreEmailThreadMailboxClientReadStates` | EmailThreadMailboxClientReadStates.batch_restore. Restores EmailThreadMailboxClientReadStates with given list of ids |
| EmailThreadMailboxClientReadStates.create | `createEmailThreadMailboxClientReadState` | EmailThreadMailboxClientReadStates.create. Creates new EmailThreadMailboxClientReadState |
| EmailThreadMailboxClientReadStates.delete | `deleteEmailThreadMailboxClientReadState` | EmailThreadMailboxClientReadStates.delete. Removes EmailThreadMailboxClientReadState with given id |
| EmailThreadMailboxClientReadStates.get | `getEmailThreadMailboxClientReadState` | EmailThreadMailboxClientReadStates.get. Returns EmailThreadMailboxClientReadState with given id |
| EmailThreadMailboxClientReadStates.list | `listEmailThreadMailboxClientReadStates` | EmailThreadMailboxClientReadStates.list. Returns all defined EmailThreadMailboxClientReadStates |
| EmailThreadMailboxClientReadStates.update | `updateEmailThreadMailboxClientReadState` | EmailThreadMailboxClientReadStates.update. Modifies EmailThreadMailboxClientReadState or EmailThreadMailboxClientReadStates with given id(s) |
| Entities.get | `getEntity` | Entities.get. Returns Entity with given id |
| Entities.list | `listEntities` | Entities.list. Returns all defined Entities |
| EntityFitnesses.batch_create_or_update | `batchUpsertEntityFitnesses` | EntityFitnesses.batch_create_or_update. Create or update an batch of EntityFitnesses |
| EntityFitnesses.batch_delete | `batchDeleteEntityFitnesses` | EntityFitnesses.batch_delete. Removes EntityFitnesses with given list of ids |
| EntityFitnesses.batch_restore | `batchRestoreEntityFitnesses` | EntityFitnesses.batch_restore. Restores EntityFitnesses with given list of ids |
| EntityFitnesses.create | `createEntityFitness` | EntityFitnesses.create. Creates new EntityFitness |
| EntityFitnesses.delete | `deleteEntityFitness` | EntityFitnesses.delete. Removes EntityFitness with given id |
| EntityFitnesses.get | `getEntityFitness` | EntityFitnesses.get. Returns EntityFitness with given id |
| EntityFitnesses.list | `listEntityFitnesses` | EntityFitnesses.list. Returns all defined EntityFitnesses |
| EntityFitnesses.update | `updateEntityFitness` | EntityFitnesses.update. Modifies EntityFitness or EntityFitnesses with given id(s) |
| EntityFitnessIndicators.batch_create_or_update | `batchUpsertEntityFitnessIndicators` | EntityFitnessIndicators.batch_create_or_update. Create or update an batch of EntityFitnessIndicators |
| EntityFitnessIndicators.batch_delete | `batchDeleteEntityFitnessIndicators` | EntityFitnessIndicators.batch_delete. Removes EntityFitnessIndicators with given list of ids |
| EntityFitnessIndicators.batch_restore | `batchRestoreEntityFitnessIndicators` | EntityFitnessIndicators.batch_restore. Restores EntityFitnessIndicators with given list of ids |
| EntityFitnessIndicators.create | `createEntityFitnessIndicator` | EntityFitnessIndicators.create. Creates new EntityFitnessIndicator |
| EntityFitnessIndicators.delete | `deleteEntityFitnessIndicator` | EntityFitnessIndicators.delete. Removes EntityFitnessIndicator with given id |
| EntityFitnessIndicators.get | `getEntityFitnessIndicator` | EntityFitnessIndicators.get. Returns EntityFitnessIndicator with given id |
| EntityFitnessIndicators.list | `listEntityFitnessIndicators` | EntityFitnessIndicators.list. Returns all defined EntityFitnessIndicators |
| EntityFitnessIndicators.update | `updateEntityFitnessIndicator` | EntityFitnessIndicators.update. Modifies EntityFitnessIndicator or EntityFitnessIndicators with given id(s) |
| EntityHealths.batch_create_or_update | `batchUpsertEntityHealths` | EntityHealths.batch_create_or_update. Create or update an batch of EntityHealths |
| EntityHealths.batch_delete | `batchDeleteEntityHealths` | EntityHealths.batch_delete. Removes EntityHealths with given list of ids |
| EntityHealths.batch_restore | `batchRestoreEntityHealths` | EntityHealths.batch_restore. Restores EntityHealths with given list of ids |
| EntityHealths.create | `createEntityHealth` | EntityHealths.create. Creates new EntityHealth |
| EntityHealths.delete | `deleteEntityHealth` | EntityHealths.delete. Removes EntityHealth with given id |
| EntityHealths.get | `getEntityHealth` | EntityHealths.get. Returns EntityHealth with given id |
| EntityHealths.list | `listEntityHealths` | EntityHealths.list. Returns all defined EntityHealths |
| EntityHealths.update | `updateEntityHealth` | EntityHealths.update. Modifies EntityHealth or EntityHealths with given id(s) |
| EntityScorings.batch_create_or_update | `batchUpsertEntityScorings` | EntityScorings.batch_create_or_update. Create or update an batch of EntityScorings |
| EntityScorings.batch_delete | `batchDeleteEntityScorings` | EntityScorings.batch_delete. Removes EntityScorings with given list of ids |
| EntityScorings.batch_restore | `batchRestoreEntityScorings` | EntityScorings.batch_restore. Restores EntityScorings with given list of ids |
| EntityScorings.create | `createEntityScoring` | EntityScorings.create. Creates new EntityScoring |
| EntityScorings.delete | `deleteEntityScoring` | EntityScorings.delete. Removes EntityScoring with given id |
| EntityScorings.get | `getEntityScoring` | EntityScorings.get. Returns EntityScoring with given id |
| EntityScorings.list | `listEntityScorings` | EntityScorings.list. Returns all defined EntityScorings |
| EntityScorings.update | `updateEntityScoring` | EntityScorings.update. Modifies EntityScoring or EntityScorings with given id(s) |
| EntitySettingses.batch_create_or_update | `batchUpsertEntitySettingses` | EntitySettingses.batch_create_or_update. Create or update an batch of EntitySettingses |
| EntitySettingses.batch_delete | `batchDeleteEntitySettingses` | EntitySettingses.batch_delete. Removes EntitySettingses with given list of ids |
| EntitySettingses.batch_restore | `batchRestoreEntitySettingses` | EntitySettingses.batch_restore. Restores EntitySettingses with given list of ids |
| EntitySettingses.create | `createEntitySettingse` | EntitySettingses.create. Creates new EntitySettings |
| EntitySettingses.delete | `deleteEntitySettingse` | EntitySettingses.delete. Removes EntitySettings with given id |
| EntitySettingses.get | `getEntitySettingse` | EntitySettingses.get. Returns EntitySettings with given id |
| EntitySettingses.list | `listEntitySettingses` | EntitySettingses.list. Returns all defined EntitySettingses |
| EntitySettingses.update | `updateEntitySettingse` | EntitySettingses.update. Modifies EntitySettings or EntitySettingses with given id(s) |
| FieldMappings.batch_create_or_update | `batchUpsertFieldMappings` | FieldMappings.batch_create_or_update. Create or update an batch of FieldMappings |
| FieldMappings.batch_delete | `batchDeleteFieldMappings` | FieldMappings.batch_delete. Removes FieldMappings with given list of ids |
| FieldMappings.batch_restore | `batchRestoreFieldMappings` | FieldMappings.batch_restore. Restores FieldMappings with given list of ids |
| FieldMappings.create | `createFieldMapping` | FieldMappings.create. Creates new FieldMapping |
| FieldMappings.delete | `deleteFieldMapping` | FieldMappings.delete. Removes FieldMapping with given id |
| FieldMappings.get | `getFieldMapping` | FieldMappings.get. Returns FieldMapping with given id |
| FieldMappings.list | `listFieldMappings` | FieldMappings.list. Returns all defined FieldMappings |
| FieldMappings.update | `updateFieldMapping` | FieldMappings.update. Modifies FieldMapping or FieldMappings with given id(s) |
| FieldPermissions.batch_create_or_update | `batchUpsertFieldPermissions` | FieldPermissions.batch_create_or_update. Create or update an batch of FieldPermissions |
| FieldPermissions.batch_delete | `batchDeleteFieldPermissions` | FieldPermissions.batch_delete. Removes FieldPermissions with given list of ids |
| FieldPermissions.batch_restore | `batchRestoreFieldPermissions` | FieldPermissions.batch_restore. Restores FieldPermissions with given list of ids |
| FieldPermissions.create | `createFieldPermission` | FieldPermissions.create. Creates new FieldPermission |
| FieldPermissions.delete | `deleteFieldPermission` | FieldPermissions.delete. Removes FieldPermission with given id |
| FieldPermissions.get | `getFieldPermission` | FieldPermissions.get. Returns FieldPermission with given id |
| FieldPermissions.list | `listFieldPermissions` | FieldPermissions.list. Returns all defined FieldPermissions |
| FieldPermissions.update | `updateFieldPermission` | FieldPermissions.update. Modifies FieldPermission or FieldPermissions with given id(s) |
| Fields.batch_restore | `batchRestoreFields` | Fields.batch_restore. Restores Fields with given list of ids |
| FieldSequences.get | `getFieldSequence` | FieldSequences.get. Returns FieldSequence with given id |
| FieldSequences.list | `listFieldSequences` | FieldSequences.list. Returns all defined FieldSequences |
| Forecasts.batch_create_or_update | `batchUpsertForecasts` | Forecasts.batch_create_or_update. Create or update an batch of Forecasts |
| Forecasts.batch_delete | `batchDeleteForecasts` | Forecasts.batch_delete. Removes Forecasts with given list of ids |
| Forecasts.batch_restore | `batchRestoreForecasts` | Forecasts.batch_restore. Restores Forecasts with given list of ids |
| Forecasts.create | `createForecast` | Forecasts.create. Creates new Forecast |
| Forecasts.delete | `deleteForecast` | Forecasts.delete. Removes Forecast with given id |
| Forecasts.get | `getForecast` | Forecasts.get. Returns Forecast with given id |
| Forecasts.list | `listForecasts` | Forecasts.list. Returns all defined Forecasts |
| Forecasts.update | `updateForecast` | Forecasts.update. Modifies Forecast or Forecasts with given id(s) |
| FormViews.batch_create_or_update | `batchUpsertFormViews` | FormViews.batch_create_or_update. Create or update an batch of FormViews |
| FormViews.batch_delete | `batchDeleteFormViews` | FormViews.batch_delete. Removes FormViews with given list of ids |
| FormViews.batch_restore | `batchRestoreFormViews` | FormViews.batch_restore. Restores FormViews with given list of ids |
| FormViews.create | `createFormView` | FormViews.create. Creates new FormView |
| FormViews.delete | `deleteFormView` | FormViews.delete. Removes FormView with given id |
| FormViews.get | `getFormView` | FormViews.get. Returns FormView with given id |
| FormViews.list | `listFormViews` | FormViews.list. Returns all defined FormViews |
| FormViews.update | `updateFormView` | FormViews.update. Modifies FormView or FormViews with given id(s) |
| FormViewSharingClientRelations.batch_create_or_update | `batchUpsertFormViewSharingClientRelations` | FormViewSharingClientRelations.batch_create_or_update. Create or update an batch of FormViewSharingClientRelations |
| FormViewSharingClientRelations.batch_delete | `batchDeleteFormViewSharingClientRelations` | FormViewSharingClientRelations.batch_delete. Removes FormViewSharingClientRelations with given list of ids |
| FormViewSharingClientRelations.batch_restore | `batchRestoreFormViewSharingClientRelations` | FormViewSharingClientRelations.batch_restore. Restores FormViewSharingClientRelations with given list of ids |
| FormViewSharingClientRelations.create | `createFormViewSharingClientRelation` | FormViewSharingClientRelations.create. Creates new FormViewSharingClientRelation |
| FormViewSharingClientRelations.delete | `deleteFormViewSharingClientRelation` | FormViewSharingClientRelations.delete. Removes FormViewSharingClientRelation with given id |
| FormViewSharingClientRelations.get | `getFormViewSharingClientRelation` | FormViewSharingClientRelations.get. Returns FormViewSharingClientRelation with given id |
| FormViewSharingClientRelations.list | `listFormViewSharingClientRelations` | FormViewSharingClientRelations.list. Returns all defined FormViewSharingClientRelations |
| FormViewSharingClientRelations.update | `updateFormViewSharingClientRelation` | FormViewSharingClientRelations.update. Modifies FormViewSharingClientRelation or FormViewSharingClientRelations with given id(s) |
| FormViewSharingSalesUnitRelations.batch_create_or_update | `batchUpsertFormViewSharingSalesUnitRelations` | FormViewSharingSalesUnitRelations.batch_create_or_update. Create or update an batch of FormViewSharingSalesUnitRelations |
| FormViewSharingSalesUnitRelations.batch_delete | `batchDeleteFormViewSharingSalesUnitRelations` | FormViewSharingSalesUnitRelations.batch_delete. Removes FormViewSharingSalesUnitRelations with given list of ids |
| FormViewSharingSalesUnitRelations.batch_restore | `batchRestoreFormViewSharingSalesUnitRelations` | FormViewSharingSalesUnitRelations.batch_restore. Restores FormViewSharingSalesUnitRelations with given list of ids |
| FormViewSharingSalesUnitRelations.create | `createFormViewSharingSalesUnitRelation` | FormViewSharingSalesUnitRelations.create. Creates new FormViewSharingSalesUnitRelation |
| FormViewSharingSalesUnitRelations.delete | `deleteFormViewSharingSalesUnitRelation` | FormViewSharingSalesUnitRelations.delete. Removes FormViewSharingSalesUnitRelation with given id |
| FormViewSharingSalesUnitRelations.get | `getFormViewSharingSalesUnitRelation` | FormViewSharingSalesUnitRelations.get. Returns FormViewSharingSalesUnitRelation with given id |
| FormViewSharingSalesUnitRelations.list | `listFormViewSharingSalesUnitRelations` | FormViewSharingSalesUnitRelations.list. Returns all defined FormViewSharingSalesUnitRelations |
| FormViewSharingSalesUnitRelations.update | `updateFormViewSharingSalesUnitRelation` | FormViewSharingSalesUnitRelations.update. Modifies FormViewSharingSalesUnitRelation or FormViewSharingSalesUnitRelations with given id(s) |
| Get Account | `getAccount` | Accounts.get. Returns Account with given id |
| Get Account Data Ex Relation | `getAccountDataExRelation` | AccountDataExRelations.get. Returns AccountDataExRelation with given id |
| Get Account KPI | `getAccountKPI` | AccountKPIs.get. Returns AccountKPI with given id |
| Get Account Product Pricing | `getAccountProductPricing` | AccountProductPricings.get. Returns AccountProductPricing with given id |
| Get Account Relation | `getAccountRelation` | AccountRelations.get. Returns AccountRelation with given id |
| Get Account Relation Label | `getAccountRelationLabel` | AccountRelationLabels.get. Returns AccountRelationLabel with given id |
| Get Account Relation Type | `getAccountRelationType` | AccountRelationTypes.get. Returns AccountRelationType with given id |
| Get Account Role | `getAccountRole` | AccountRoles.get. Returns AccountRole with given id |
| Get Account Sharing Client Relation | `getAccountSharingClientRelation` | AccountSharingClientRelations.get. Returns AccountSharingClientRelation with given id |
| Get Account Sharing Sales Unit Relation | `getAccountSharingSalesUnitRelation` | AccountSharingSalesUnitRelations.get. Returns AccountSharingSalesUnitRelation with given id |
| Get Account Social Relation | `getAccountSocialRelation` | AccountSocialRelations.get. Returns AccountSocialRelation with given id |
| Get Activity | `getActivity` | Activities.get. Returns Activity with given id |
| Get Contact | `getContact` | Contacts.get. Returns Contact with given id |
| Get Custom Field | `getField` | Fields.get. Returns Field with given id |
| Get Lead | `getLead` | Leads.get. Returns Lead with given id |
| Get Lead/Opportunity | `getLeadOppty` | LeadOppties.get. Returns LeadOppty with given id |
| Get Opportunity | `getOpportunity` | Opportunities.get. Returns Opportunity with given id |
| Get Pipeline | `getPipeline` | Pipelines.get. Returns Pipeline with given id |
| Get Product | `getProduct` | Products.get. Returns Product with given id |
| Get Quote | `getQuote` | Quotes.get. Returns Quote with given id |
| Get Task | `getTask` | Tasks.get. Returns Task with given id |
| Get Webhook | `getWebhook` | Webhooks.get. Returns Webhook with given id |
| GhostContactAccountAccountRoleRelations.batch_create_or_update | `batchUpsertGhostContactAccountAccountRoleRelations` | GhostContactAccountAccountRoleRelations.batch_create_or_update. Create or update an batch of GhostContactAccountAccountRoleRelations |
| GhostContactAccountAccountRoleRelations.batch_delete | `batchDeleteGhostContactAccountAccountRoleRelations` | GhostContactAccountAccountRoleRelations.batch_delete. Removes GhostContactAccountAccountRoleRelations with given list of ids |
| GhostContactAccountAccountRoleRelations.batch_restore | `batchRestoreGhostContactAccountAccountRoleRelations` | GhostContactAccountAccountRoleRelations.batch_restore. Restores GhostContactAccountAccountRoleRelations with given list of ids |
| GhostContactAccountAccountRoleRelations.create | `createGhostContactAccountAccountRoleRelation` | GhostContactAccountAccountRoleRelations.create. Creates new GhostContactAccountAccountRoleRelation |
| GhostContactAccountAccountRoleRelations.delete | `deleteGhostContactAccountAccountRoleRelation` | GhostContactAccountAccountRoleRelations.delete. Removes GhostContactAccountAccountRoleRelation with given id |
| GhostContactAccountAccountRoleRelations.get | `getGhostContactAccountAccountRoleRelation` | GhostContactAccountAccountRoleRelations.get. Returns GhostContactAccountAccountRoleRelation with given id |
| GhostContactAccountAccountRoleRelations.list | `listGhostContactAccountAccountRoleRelations` | GhostContactAccountAccountRoleRelations.list. Returns all defined GhostContactAccountAccountRoleRelations |
| GhostContactAccountAccountRoleRelations.update | `updateGhostContactAccountAccountRoleRelation` | GhostContactAccountAccountRoleRelations.update. Modifies GhostContactAccountAccountRoleRelation or GhostContactAccountAccountRoleRelations with given id(s) |
| GhostContactAccountRelations.batch_create_or_update | `batchUpsertGhostContactAccountRelations` | GhostContactAccountRelations.batch_create_or_update. Create or update an batch of GhostContactAccountRelations |
| GhostContactAccountRelations.batch_delete | `batchDeleteGhostContactAccountRelations` | GhostContactAccountRelations.batch_delete. Removes GhostContactAccountRelations with given list of ids |
| GhostContactAccountRelations.batch_restore | `batchRestoreGhostContactAccountRelations` | GhostContactAccountRelations.batch_restore. Restores GhostContactAccountRelations with given list of ids |
| GhostContactAccountRelations.create | `createGhostContactAccountRelation` | GhostContactAccountRelations.create. Creates new GhostContactAccountRelation |
| GhostContactAccountRelations.delete | `deleteGhostContactAccountRelation` | GhostContactAccountRelations.delete. Removes GhostContactAccountRelation with given id |
| GhostContactAccountRelations.get | `getGhostContactAccountRelation` | GhostContactAccountRelations.get. Returns GhostContactAccountRelation with given id |
| GhostContactAccountRelations.list | `listGhostContactAccountRelations` | GhostContactAccountRelations.list. Returns all defined GhostContactAccountRelations |
| GhostContactAccountRelations.update | `updateGhostContactAccountRelation` | GhostContactAccountRelations.update. Modifies GhostContactAccountRelation or GhostContactAccountRelations with given id(s) |
| GhostContacts.batch_create_or_update | `batchUpsertGhostContacts` | GhostContacts.batch_create_or_update. Create or update an batch of GhostContacts |
| GhostContacts.batch_delete | `batchDeleteGhostContacts` | GhostContacts.batch_delete. Removes GhostContacts with given list of ids |
| GhostContacts.batch_restore | `batchRestoreGhostContacts` | GhostContacts.batch_restore. Restores GhostContacts with given list of ids |
| GhostContacts.create | `createGhostContact` | GhostContacts.create. Creates new GhostContact |
| GhostContacts.delete | `deleteGhostContact` | GhostContacts.delete. Removes GhostContact with given id |
| GhostContacts.get | `getGhostContact` | GhostContacts.get. Returns GhostContact with given id |
| GhostContacts.list | `listGhostContacts` | GhostContacts.list. Returns all defined GhostContacts |
| GhostContacts.update | `updateGhostContact` | GhostContacts.update. Modifies GhostContact or GhostContacts with given id(s) |
| GhostLeadOpptyContactRelations.batch_create_or_update | `batchUpsertGhostLeadOpptyContactRelations` | GhostLeadOpptyContactRelations.batch_create_or_update. Create or update an batch of GhostLeadOpptyContactRelations |
| GhostLeadOpptyContactRelations.batch_delete | `batchDeleteGhostLeadOpptyContactRelations` | GhostLeadOpptyContactRelations.batch_delete. Removes GhostLeadOpptyContactRelations with given list of ids |
| GhostLeadOpptyContactRelations.batch_restore | `batchRestoreGhostLeadOpptyContactRelations` | GhostLeadOpptyContactRelations.batch_restore. Restores GhostLeadOpptyContactRelations with given list of ids |
| GhostLeadOpptyContactRelations.create | `createGhostLeadOpptyContactRelation` | GhostLeadOpptyContactRelations.create. Creates new GhostLeadOpptyContactRelation |
| GhostLeadOpptyContactRelations.delete | `deleteGhostLeadOpptyContactRelation` | GhostLeadOpptyContactRelations.delete. Removes GhostLeadOpptyContactRelation with given id |
| GhostLeadOpptyContactRelations.get | `getGhostLeadOpptyContactRelation` | GhostLeadOpptyContactRelations.get. Returns GhostLeadOpptyContactRelation with given id |
| GhostLeadOpptyContactRelations.list | `listGhostLeadOpptyContactRelations` | GhostLeadOpptyContactRelations.list. Returns all defined GhostLeadOpptyContactRelations |
| GhostLeadOpptyContactRelations.update | `updateGhostLeadOpptyContactRelation` | GhostLeadOpptyContactRelations.update. Modifies GhostLeadOpptyContactRelation or GhostLeadOpptyContactRelations with given id(s) |
| GhostLeadOpptyContactSalesRoleRelations.batch_create_or_update | `batchUpsertGhostLeadOpptyContactSalesRoleRelations` | GhostLeadOpptyContactSalesRoleRelations.batch_create_or_update. Create or update an batch of GhostLeadOpptyContactSalesRoleRelations |
| GhostLeadOpptyContactSalesRoleRelations.batch_delete | `batchDeleteGhostLeadOpptyContactSalesRoleRelations` | GhostLeadOpptyContactSalesRoleRelations.batch_delete. Removes GhostLeadOpptyContactSalesRoleRelations with given list of ids |
| GhostLeadOpptyContactSalesRoleRelations.batch_restore | `batchRestoreGhostLeadOpptyContactSalesRoleRelations` | GhostLeadOpptyContactSalesRoleRelations.batch_restore. Restores GhostLeadOpptyContactSalesRoleRelations with given list of ids |
| GhostLeadOpptyContactSalesRoleRelations.create | `createGhostLeadOpptyContactSalesRoleRelation` | GhostLeadOpptyContactSalesRoleRelations.create. Creates new GhostLeadOpptyContactSalesRoleRelation |
| GhostLeadOpptyContactSalesRoleRelations.delete | `deleteGhostLeadOpptyContactSalesRoleRelation` | GhostLeadOpptyContactSalesRoleRelations.delete. Removes GhostLeadOpptyContactSalesRoleRelation with given id |
| GhostLeadOpptyContactSalesRoleRelations.get | `getGhostLeadOpptyContactSalesRoleRelation` | GhostLeadOpptyContactSalesRoleRelations.get. Returns GhostLeadOpptyContactSalesRoleRelation with given id |
| GhostLeadOpptyContactSalesRoleRelations.list | `listGhostLeadOpptyContactSalesRoleRelations` | GhostLeadOpptyContactSalesRoleRelations.list. Returns all defined GhostLeadOpptyContactSalesRoleRelations |
| GhostLeadOpptyContactSalesRoleRelations.update | `updateGhostLeadOpptyContactSalesRoleRelation` | GhostLeadOpptyContactSalesRoleRelations.update. Modifies GhostLeadOpptyContactSalesRoleRelation or GhostLeadOpptyContactSalesRoleRelations with given id(s) |
| ImportMappingMasks.batch_create_or_update | `batchUpsertImportMappingMasks` | ImportMappingMasks.batch_create_or_update. Create or update an batch of ImportMappingMasks |
| ImportMappingMasks.batch_delete | `batchDeleteImportMappingMasks` | ImportMappingMasks.batch_delete. Removes ImportMappingMasks with given list of ids |
| ImportMappingMasks.batch_restore | `batchRestoreImportMappingMasks` | ImportMappingMasks.batch_restore. Restores ImportMappingMasks with given list of ids |
| ImportMappingMasks.create | `createImportMappingMask` | ImportMappingMasks.create. Creates new ImportMappingMask |
| ImportMappingMasks.delete | `deleteImportMappingMask` | ImportMappingMasks.delete. Removes ImportMappingMask with given id |
| ImportMappingMasks.get | `getImportMappingMask` | ImportMappingMasks.get. Returns ImportMappingMask with given id |
| ImportMappingMasks.list | `listImportMappingMasks` | ImportMappingMasks.list. Returns all defined ImportMappingMasks |
| ImportMappingMasks.update | `updateImportMappingMask` | ImportMappingMasks.update. Modifies ImportMappingMask or ImportMappingMasks with given id(s) |
| InterfacePreviews.batch_create_or_update | `batchUpsertInterfacePreviews` | InterfacePreviews.batch_create_or_update. Create or update an batch of InterfacePreviews |
| InterfacePreviews.batch_delete | `batchDeleteInterfacePreviews` | InterfacePreviews.batch_delete. Removes InterfacePreviews with given list of ids |
| InterfacePreviews.batch_restore | `batchRestoreInterfacePreviews` | InterfacePreviews.batch_restore. Restores InterfacePreviews with given list of ids |
| InterfacePreviews.create | `createInterfacePreview` | InterfacePreviews.create. Creates new InterfacePreview |
| InterfacePreviews.delete | `deleteInterfacePreview` | InterfacePreviews.delete. Removes InterfacePreview with given id |
| InterfacePreviews.get | `getInterfacePreview` | InterfacePreviews.get. Returns InterfacePreview with given id |
| InterfacePreviews.list | `listInterfacePreviews` | InterfacePreviews.list. Returns all defined InterfacePreviews |
| InterfacePreviews.update | `updateInterfacePreview` | InterfacePreviews.update. Modifies InterfacePreview or InterfacePreviews with given id(s) |
| LeadOpptyAccountRelations.batch_create_or_update | `batchUpsertLeadOpptyAccountRelations` | LeadOpptyAccountRelations.batch_create_or_update. Create or update an batch of LeadOpptyAccountRelations |
| LeadOpptyAccountRelations.batch_delete | `batchDeleteLeadOpptyAccountRelations` | LeadOpptyAccountRelations.batch_delete. Removes LeadOpptyAccountRelations with given list of ids |
| LeadOpptyAccountRelations.batch_restore | `batchRestoreLeadOpptyAccountRelations` | LeadOpptyAccountRelations.batch_restore. Restores LeadOpptyAccountRelations with given list of ids |
| LeadOpptyAccountRelations.create | `createLeadOpptyAccountRelation` | LeadOpptyAccountRelations.create. Creates new LeadOpptyAccountRelation |
| LeadOpptyAccountRelations.delete | `deleteLeadOpptyAccountRelation` | LeadOpptyAccountRelations.delete. Removes LeadOpptyAccountRelation with given id |
| LeadOpptyAccountRelations.get | `getLeadOpptyAccountRelation` | LeadOpptyAccountRelations.get. Returns LeadOpptyAccountRelation with given id |
| LeadOpptyAccountRelations.list | `listLeadOpptyAccountRelations` | LeadOpptyAccountRelations.list. Returns all defined LeadOpptyAccountRelations |
| LeadOpptyAccountRelations.update | `updateLeadOpptyAccountRelation` | LeadOpptyAccountRelations.update. Modifies LeadOpptyAccountRelation or LeadOpptyAccountRelations with given id(s) |
| LeadOpptyContactGroupRelations.batch_create_or_update | `batchUpsertLeadOpptyContactGroupRelations` | LeadOpptyContactGroupRelations.batch_create_or_update. Create or update an batch of LeadOpptyContactGroupRelations |
| LeadOpptyContactGroupRelations.batch_delete | `batchDeleteLeadOpptyContactGroupRelations` | LeadOpptyContactGroupRelations.batch_delete. Removes LeadOpptyContactGroupRelations with given list of ids |
| LeadOpptyContactGroupRelations.batch_restore | `batchRestoreLeadOpptyContactGroupRelations` | LeadOpptyContactGroupRelations.batch_restore. Restores LeadOpptyContactGroupRelations with given list of ids |
| LeadOpptyContactGroupRelations.create | `createLeadOpptyContactGroupRelation` | LeadOpptyContactGroupRelations.create. Creates new LeadOpptyContactGroupRelation |
| LeadOpptyContactGroupRelations.delete | `deleteLeadOpptyContactGroupRelation` | LeadOpptyContactGroupRelations.delete. Removes LeadOpptyContactGroupRelation with given id |
| LeadOpptyContactGroupRelations.get | `getLeadOpptyContactGroupRelation` | LeadOpptyContactGroupRelations.get. Returns LeadOpptyContactGroupRelation with given id |
| LeadOpptyContactGroupRelations.list | `listLeadOpptyContactGroupRelations` | LeadOpptyContactGroupRelations.list. Returns all defined LeadOpptyContactGroupRelations |
| LeadOpptyContactGroupRelations.update | `updateLeadOpptyContactGroupRelation` | LeadOpptyContactGroupRelations.update. Modifies LeadOpptyContactGroupRelation or LeadOpptyContactGroupRelations with given id(s) |
| LeadOpptyContactRelations.batch_create_or_update | `batchUpsertLeadOpptyContactRelations` | LeadOpptyContactRelations.batch_create_or_update. Create or update an batch of LeadOpptyContactRelations |
| LeadOpptyContactRelations.batch_delete | `batchDeleteLeadOpptyContactRelations` | LeadOpptyContactRelations.batch_delete. Removes LeadOpptyContactRelations with given list of ids |
| LeadOpptyContactRelations.batch_restore | `batchRestoreLeadOpptyContactRelations` | LeadOpptyContactRelations.batch_restore. Restores LeadOpptyContactRelations with given list of ids |
| LeadOpptyContactRelations.create | `createLeadOpptyContactRelation` | LeadOpptyContactRelations.create. Creates new LeadOpptyContactRelation |
| LeadOpptyContactRelations.delete | `deleteLeadOpptyContactRelation` | LeadOpptyContactRelations.delete. Removes LeadOpptyContactRelation with given id |
| LeadOpptyContactRelations.get | `getLeadOpptyContactRelation` | LeadOpptyContactRelations.get. Returns LeadOpptyContactRelation with given id |
| LeadOpptyContactRelations.list | `listLeadOpptyContactRelations` | LeadOpptyContactRelations.list. Returns all defined LeadOpptyContactRelations |
| LeadOpptyContactRelations.update | `updateLeadOpptyContactRelation` | LeadOpptyContactRelations.update. Modifies LeadOpptyContactRelation or LeadOpptyContactRelations with given id(s) |
| LeadOpptyContactSalesRoleRelations.batch_create_or_update | `batchUpsertLeadOpptyContactSalesRoleRelations` | LeadOpptyContactSalesRoleRelations.batch_create_or_update. Create or update an batch of LeadOpptyContactSalesRoleRelations |
| LeadOpptyContactSalesRoleRelations.batch_delete | `batchDeleteLeadOpptyContactSalesRoleRelations` | LeadOpptyContactSalesRoleRelations.batch_delete. Removes LeadOpptyContactSalesRoleRelations with given list of ids |
| LeadOpptyContactSalesRoleRelations.batch_restore | `batchRestoreLeadOpptyContactSalesRoleRelations` | LeadOpptyContactSalesRoleRelations.batch_restore. Restores LeadOpptyContactSalesRoleRelations with given list of ids |
| LeadOpptyContactSalesRoleRelations.create | `createLeadOpptyContactSalesRoleRelation` | LeadOpptyContactSalesRoleRelations.create. Creates new LeadOpptyContactSalesRoleRelation |
| LeadOpptyContactSalesRoleRelations.delete | `deleteLeadOpptyContactSalesRoleRelation` | LeadOpptyContactSalesRoleRelations.delete. Removes LeadOpptyContactSalesRoleRelation with given id |
| LeadOpptyContactSalesRoleRelations.get | `getLeadOpptyContactSalesRoleRelation` | LeadOpptyContactSalesRoleRelations.get. Returns LeadOpptyContactSalesRoleRelation with given id |
| LeadOpptyContactSalesRoleRelations.list | `listLeadOpptyContactSalesRoleRelations` | LeadOpptyContactSalesRoleRelations.list. Returns all defined LeadOpptyContactSalesRoleRelations |
| LeadOpptyContactSalesRoleRelations.update | `updateLeadOpptyContactSalesRoleRelation` | LeadOpptyContactSalesRoleRelations.update. Modifies LeadOpptyContactSalesRoleRelation or LeadOpptyContactSalesRoleRelations with given id(s) |
| LeadOpptyDataExRelations.get | `getLeadOpptyDataExRelation` | LeadOpptyDataExRelations.get. Returns LeadOpptyDataExRelation with given id |
| LeadOpptyDataExRelations.list | `listLeadOpptyDataExRelations` | LeadOpptyDataExRelations.list. Returns all defined LeadOpptyDataExRelations |
| LeadOpptyKPIs.batch_create_or_update | `batchUpsertLeadOpptyKPIs` | LeadOpptyKPIs.batch_create_or_update. Create or update an batch of LeadOpptyKPIs |
| LeadOpptyKPIs.batch_delete | `batchDeleteLeadOpptyKPIs` | LeadOpptyKPIs.batch_delete. Removes LeadOpptyKPIs with given list of ids |
| LeadOpptyKPIs.batch_restore | `batchRestoreLeadOpptyKPIs` | LeadOpptyKPIs.batch_restore. Restores LeadOpptyKPIs with given list of ids |
| LeadOpptyKPIs.create | `createLeadOpptyKPI` | LeadOpptyKPIs.create. Creates new LeadOpptyKPI |
| LeadOpptyKPIs.delete | `deleteLeadOpptyKPI` | LeadOpptyKPIs.delete. Removes LeadOpptyKPI with given id |
| LeadOpptyKPIs.get | `getLeadOpptyKPI` | LeadOpptyKPIs.get. Returns LeadOpptyKPI with given id |
| LeadOpptyKPIs.list | `listLeadOpptyKPIs` | LeadOpptyKPIs.list. Returns all defined LeadOpptyKPIs |
| LeadOpptyKPIs.update | `updateLeadOpptyKPI` | LeadOpptyKPIs.update. Modifies LeadOpptyKPI or LeadOpptyKPIs with given id(s) |
| LeadOpptySharingClientRelations.batch_create_or_update | `batchUpsertLeadOpptySharingClientRelations` | LeadOpptySharingClientRelations.batch_create_or_update. Create or update an batch of LeadOpptySharingClientRelations |
| LeadOpptySharingClientRelations.batch_delete | `batchDeleteLeadOpptySharingClientRelations` | LeadOpptySharingClientRelations.batch_delete. Removes LeadOpptySharingClientRelations with given list of ids |
| LeadOpptySharingClientRelations.batch_restore | `batchRestoreLeadOpptySharingClientRelations` | LeadOpptySharingClientRelations.batch_restore. Restores LeadOpptySharingClientRelations with given list of ids |
| LeadOpptySharingClientRelations.create | `createLeadOpptySharingClientRelation` | LeadOpptySharingClientRelations.create. Creates new LeadOpptySharingClientRelation |
| LeadOpptySharingClientRelations.delete | `deleteLeadOpptySharingClientRelation` | LeadOpptySharingClientRelations.delete. Removes LeadOpptySharingClientRelation with given id |
| LeadOpptySharingClientRelations.get | `getLeadOpptySharingClientRelation` | LeadOpptySharingClientRelations.get. Returns LeadOpptySharingClientRelation with given id |
| LeadOpptySharingClientRelations.list | `listLeadOpptySharingClientRelations` | LeadOpptySharingClientRelations.list. Returns all defined LeadOpptySharingClientRelations |
| LeadOpptySharingClientRelations.update | `updateLeadOpptySharingClientRelation` | LeadOpptySharingClientRelations.update. Modifies LeadOpptySharingClientRelation or LeadOpptySharingClientRelations with given id(s) |
| LeadOpptySharingSalesUnitRelations.batch_create_or_update | `batchUpsertLeadOpptySharingSalesUnitRelations` | LeadOpptySharingSalesUnitRelations.batch_create_or_update. Create or update an batch of LeadOpptySharingSalesUnitRelations |
| LeadOpptySharingSalesUnitRelations.batch_delete | `batchDeleteLeadOpptySharingSalesUnitRelations` | LeadOpptySharingSalesUnitRelations.batch_delete. Removes LeadOpptySharingSalesUnitRelations with given list of ids |
| LeadOpptySharingSalesUnitRelations.batch_restore | `batchRestoreLeadOpptySharingSalesUnitRelations` | LeadOpptySharingSalesUnitRelations.batch_restore. Restores LeadOpptySharingSalesUnitRelations with given list of ids |
| LeadOpptySharingSalesUnitRelations.create | `createLeadOpptySharingSalesUnitRelation` | LeadOpptySharingSalesUnitRelations.create. Creates new LeadOpptySharingSalesUnitRelation |
| LeadOpptySharingSalesUnitRelations.delete | `deleteLeadOpptySharingSalesUnitRelation` | LeadOpptySharingSalesUnitRelations.delete. Removes LeadOpptySharingSalesUnitRelation with given id |
| LeadOpptySharingSalesUnitRelations.get | `getLeadOpptySharingSalesUnitRelation` | LeadOpptySharingSalesUnitRelations.get. Returns LeadOpptySharingSalesUnitRelation with given id |
| LeadOpptySharingSalesUnitRelations.list | `listLeadOpptySharingSalesUnitRelations` | LeadOpptySharingSalesUnitRelations.list. Returns all defined LeadOpptySharingSalesUnitRelations |
| LeadOpptySharingSalesUnitRelations.update | `updateLeadOpptySharingSalesUnitRelation` | LeadOpptySharingSalesUnitRelations.update. Modifies LeadOpptySharingSalesUnitRelation or LeadOpptySharingSalesUnitRelations with given id(s) |
| LeadOpptyStepCheckListRelations.batch_create_or_update | `batchUpsertLeadOpptyStepCheckListRelations` | LeadOpptyStepCheckListRelations.batch_create_or_update. Create or update an batch of LeadOpptyStepCheckListRelations |
| LeadOpptyStepCheckListRelations.batch_delete | `batchDeleteLeadOpptyStepCheckListRelations` | LeadOpptyStepCheckListRelations.batch_delete. Removes LeadOpptyStepCheckListRelations with given list of ids |
| LeadOpptyStepCheckListRelations.batch_restore | `batchRestoreLeadOpptyStepCheckListRelations` | LeadOpptyStepCheckListRelations.batch_restore. Restores LeadOpptyStepCheckListRelations with given list of ids |
| LeadOpptyStepCheckListRelations.create | `createLeadOpptyStepCheckListRelation` | LeadOpptyStepCheckListRelations.create. Creates new LeadOpptyStepCheckListRelation |
| LeadOpptyStepCheckListRelations.delete | `deleteLeadOpptyStepCheckListRelation` | LeadOpptyStepCheckListRelations.delete. Removes LeadOpptyStepCheckListRelation with given id |
| LeadOpptyStepCheckListRelations.get | `getLeadOpptyStepCheckListRelation` | LeadOpptyStepCheckListRelations.get. Returns LeadOpptyStepCheckListRelation with given id |
| LeadOpptyStepCheckListRelations.list | `listLeadOpptyStepCheckListRelations` | LeadOpptyStepCheckListRelations.list. Returns all defined LeadOpptyStepCheckListRelations |
| LeadOpptyStepCheckListRelations.update | `updateLeadOpptyStepCheckListRelation` | LeadOpptyStepCheckListRelations.update. Modifies LeadOpptyStepCheckListRelation or LeadOpptyStepCheckListRelations with given id(s) |
| LeadProcesses.batch_create_or_update | `batchUpsertLeadProcesses` | LeadProcesses.batch_create_or_update. Create or update an batch of LeadProcesses |
| LeadProcesses.batch_delete | `batchDeleteLeadProcesses` | LeadProcesses.batch_delete. Removes LeadProcesses with given list of ids |
| LeadProcesses.batch_restore | `batchRestoreLeadProcesses` | LeadProcesses.batch_restore. Restores LeadProcesses with given list of ids |
| LeadProcesses.create | `createLeadProcess` | LeadProcesses.create. Creates new LeadProcess |
| LeadProcesses.delete | `deleteLeadProcess` | LeadProcesses.delete. Removes LeadProcess with given id |
| LeadProcesses.get | `getLeadProcess` | LeadProcesses.get. Returns LeadProcess with given id |
| LeadProcesses.list | `listLeadProcesses` | LeadProcesses.list. Returns all defined LeadProcesses |
| LeadProcesses.update | `updateLeadProcess` | LeadProcesses.update. Modifies LeadProcess or LeadProcesses with given id(s) |
| Leads.batch_create_or_update | `batchUpsertLeads` | Leads.batch_create_or_update. Create or update an batch of Leads |
| Leads.batch_delete | `batchDeleteLeads` | Leads.batch_delete. Removes Leads with given list of ids |
| Leads.batch_restore | `batchRestoreLeads` | Leads.batch_restore. Restores Leads with given list of ids |
| LeadTypes.batch_create_or_update | `batchUpsertLeadTypes` | LeadTypes.batch_create_or_update. Create or update an batch of LeadTypes |
| LeadTypes.batch_delete | `batchDeleteLeadTypes` | LeadTypes.batch_delete. Removes LeadTypes with given list of ids |
| LeadTypes.batch_restore | `batchRestoreLeadTypes` | LeadTypes.batch_restore. Restores LeadTypes with given list of ids |
| LeadTypes.create | `createLeadType` | LeadTypes.create. Creates new LeadType |
| LeadTypes.delete | `deleteLeadType` | LeadTypes.delete. Removes LeadType with given id |
| LeadTypes.get | `getLeadType` | LeadTypes.get. Returns LeadType with given id |
| LeadTypes.list | `listLeadTypes` | LeadTypes.list. Returns all defined LeadTypes |
| LeadTypes.update | `updateLeadType` | LeadTypes.update. Modifies LeadType or LeadTypes with given id(s) |
| List Account Data Ex Relations | `listAccountDataExRelations` | AccountDataExRelations.list. Returns all defined AccountDataExRelations |
| List Account KPIs | `listAccountKPIs` | AccountKPIs.list. Returns all defined AccountKPIs |
| List Account Product Pricings | `listAccountProductPricings` | AccountProductPricings.list. Returns all defined AccountProductPricings |
| List Account Relation Labels | `listAccountRelationLabels` | AccountRelationLabels.list. Returns all defined AccountRelationLabels |
| List Account Relation Types | `listAccountRelationTypes` | AccountRelationTypes.list. Returns all defined AccountRelationTypes |
| List Account Relations | `listAccountRelations` | AccountRelations.list. Returns all defined AccountRelations |
| List Account Roles | `listAccountRoles` | AccountRoles.list. Returns all defined AccountRoles |
| List Account Sharing Client Relations | `listAccountSharingClientRelations` | AccountSharingClientRelations.list. Returns all defined AccountSharingClientRelations |
| List Account Sharing Sales Unit Relations | `listAccountSharingSalesUnitRelations` | AccountSharingSalesUnitRelations.list. Returns all defined AccountSharingSalesUnitRelations |
| List Account Social Relations | `listAccountSocialRelations` | AccountSocialRelations.list. Returns all defined AccountSocialRelations |
| List Accounts | `listAccounts` | Accounts.list. Returns all defined Accounts |
| List Activities | `listActivities` | Activities.list. Returns all defined Activities |
| List Contacts | `listContacts` | Contacts.list. Returns all defined Contacts |
| List Custom Fields | `listFields` | Fields.list. Returns all defined Fields |
| List Lead/Opportunities | `listLeadOppties` | LeadOppties.list. Returns all defined LeadOppties |
| List Leads | `listLeads` | Leads.list. Returns all defined Leads |
| List Opportunities | `listOpportunities` | Opportunities.list. Returns all defined Opportunities |
| List Pipelines | `listPipelines` | Pipelines.list. Returns all defined Pipelines |
| List Products | `listProducts` | Products.list. Returns all defined Products |
| List Quotes | `listQuotes` | Quotes.list. Returns all defined Quotes |
| List Tasks | `listTasks` | Tasks.list. Returns all defined Tasks |
| List Webhooks | `listWebhooks` | Webhooks.list. Returns all defined Webhooks |
| MasterRights.batch_create_or_update | `batchUpsertMasterRights` | MasterRights.batch_create_or_update. Create or update an batch of MasterRights |
| MasterRights.batch_delete | `batchDeleteMasterRights` | MasterRights.batch_delete. Removes MasterRights with given list of ids |
| MasterRights.batch_restore | `batchRestoreMasterRights` | MasterRights.batch_restore. Restores MasterRights with given list of ids |
| MasterRights.create | `createMasterRight` | MasterRights.create. Creates new MasterRight |
| MasterRights.delete | `deleteMasterRight` | MasterRights.delete. Removes MasterRight with given id |
| MasterRights.get | `getMasterRight` | MasterRights.get. Returns MasterRight with given id |
| MasterRights.list | `listMasterRights` | MasterRights.list. Returns all defined MasterRights |
| MasterRights.update | `updateMasterRight` | MasterRights.update. Modifies MasterRight or MasterRights with given id(s) |
| Medias.batch_create_or_update | `batchUpsertMedias` | Medias.batch_create_or_update. Create or update an batch of Medias |
| Medias.batch_delete | `batchDeleteMedias` | Medias.batch_delete. Removes Medias with given list of ids |
| Medias.batch_restore | `batchRestoreMedias` | Medias.batch_restore. Restores Medias with given list of ids |
| Medias.create | `createMedia` | Medias.create. Creates new Media |
| Medias.delete | `deleteMedia` | Medias.delete. Removes Media with given id |
| Medias.get | `getMedia` | Medias.get. Returns Media with given id |
| Medias.list | `listMedias` | Medias.list. Returns all defined Medias |
| Medias.update | `updateMedia` | Medias.update. Modifies Media or Medias with given id(s) |
| MemoComments.batch_create_or_update | `batchUpsertMemoComments` | MemoComments.batch_create_or_update. Create or update an batch of MemoComments |
| MemoComments.batch_delete | `batchDeleteMemoComments` | MemoComments.batch_delete. Removes MemoComments with given list of ids |
| MemoComments.batch_restore | `batchRestoreMemoComments` | MemoComments.batch_restore. Restores MemoComments with given list of ids |
| MemoComments.create | `createMemoComment` | MemoComments.create. Creates new MemoComment |
| MemoComments.delete | `deleteMemoComment` | MemoComments.delete. Removes MemoComment with given id |
| MemoComments.get | `getMemoComment` | MemoComments.get. Returns MemoComment with given id |
| MemoComments.list | `listMemoComments` | MemoComments.list. Returns all defined MemoComments |
| MemoComments.update | `updateMemoComment` | MemoComments.update. Modifies MemoComment or MemoComments with given id(s) |
| Memos.batch_create_or_update | `batchUpsertMemos` | Memos.batch_create_or_update. Create or update an batch of Memos |
| Memos.batch_delete | `batchDeleteMemos` | Memos.batch_delete. Removes Memos with given list of ids |
| Memos.batch_restore | `batchRestoreMemos` | Memos.batch_restore. Restores Memos with given list of ids |
| Memos.create | `createMemo` | Memos.create. Creates new Memo |
| Memos.delete | `deleteMemo` | Memos.delete. Removes Memo with given id |
| Memos.get | `getMemo` | Memos.get. Returns Memo with given id |
| Memos.list | `listMemos` | Memos.list. Returns all defined Memos |
| Memos.update | `updateMemo` | Memos.update. Modifies Memo or Memos with given id(s) |
| MessageRelations.batch_create_or_update | `batchUpsertMessageRelations` | MessageRelations.batch_create_or_update. Create or update an batch of MessageRelations |
| MessageRelations.batch_delete | `batchDeleteMessageRelations` | MessageRelations.batch_delete. Removes MessageRelations with given list of ids |
| MessageRelations.batch_restore | `batchRestoreMessageRelations` | MessageRelations.batch_restore. Restores MessageRelations with given list of ids |
| MessageRelations.create | `createMessageRelation` | MessageRelations.create. Creates new MessageRelation |
| MessageRelations.delete | `deleteMessageRelation` | MessageRelations.delete. Removes MessageRelation with given id |
| MessageRelations.get | `getMessageRelation` | MessageRelations.get. Returns MessageRelation with given id |
| MessageRelations.list | `listMessageRelations` | MessageRelations.list. Returns all defined MessageRelations |
| MessageRelations.update | `updateMessageRelation` | MessageRelations.update. Modifies MessageRelation or MessageRelations with given id(s) |
| MessageSharingClientRelations.batch_create_or_update | `batchUpsertMessageSharingClientRelations` | MessageSharingClientRelations.batch_create_or_update. Create or update an batch of MessageSharingClientRelations |
| MessageSharingClientRelations.batch_delete | `batchDeleteMessageSharingClientRelations` | MessageSharingClientRelations.batch_delete. Removes MessageSharingClientRelations with given list of ids |
| MessageSharingClientRelations.batch_restore | `batchRestoreMessageSharingClientRelations` | MessageSharingClientRelations.batch_restore. Restores MessageSharingClientRelations with given list of ids |
| MessageSharingClientRelations.create | `createMessageSharingClientRelation` | MessageSharingClientRelations.create. Creates new MessageSharingClientRelation |
| MessageSharingClientRelations.delete | `deleteMessageSharingClientRelation` | MessageSharingClientRelations.delete. Removes MessageSharingClientRelation with given id |
| MessageSharingClientRelations.get | `getMessageSharingClientRelation` | MessageSharingClientRelations.get. Returns MessageSharingClientRelation with given id |
| MessageSharingClientRelations.list | `listMessageSharingClientRelations` | MessageSharingClientRelations.list. Returns all defined MessageSharingClientRelations |
| MessageSharingClientRelations.update | `updateMessageSharingClientRelation` | MessageSharingClientRelations.update. Modifies MessageSharingClientRelation or MessageSharingClientRelations with given id(s) |
| MessageSharingSalesUnitRelations.batch_create_or_update | `batchUpsertMessageSharingSalesUnitRelations` | MessageSharingSalesUnitRelations.batch_create_or_update. Create or update an batch of MessageSharingSalesUnitRelations |
| MessageSharingSalesUnitRelations.batch_delete | `batchDeleteMessageSharingSalesUnitRelations` | MessageSharingSalesUnitRelations.batch_delete. Removes MessageSharingSalesUnitRelations with given list of ids |
| MessageSharingSalesUnitRelations.batch_restore | `batchRestoreMessageSharingSalesUnitRelations` | MessageSharingSalesUnitRelations.batch_restore. Restores MessageSharingSalesUnitRelations with given list of ids |
| MessageSharingSalesUnitRelations.create | `createMessageSharingSalesUnitRelation` | MessageSharingSalesUnitRelations.create. Creates new MessageSharingSalesUnitRelation |
| MessageSharingSalesUnitRelations.delete | `deleteMessageSharingSalesUnitRelation` | MessageSharingSalesUnitRelations.delete. Removes MessageSharingSalesUnitRelation with given id |
| MessageSharingSalesUnitRelations.get | `getMessageSharingSalesUnitRelation` | MessageSharingSalesUnitRelations.get. Returns MessageSharingSalesUnitRelation with given id |
| MessageSharingSalesUnitRelations.list | `listMessageSharingSalesUnitRelations` | MessageSharingSalesUnitRelations.list. Returns all defined MessageSharingSalesUnitRelations |
| MessageSharingSalesUnitRelations.update | `updateMessageSharingSalesUnitRelation` | MessageSharingSalesUnitRelations.update. Modifies MessageSharingSalesUnitRelation or MessageSharingSalesUnitRelations with given id(s) |
| Notes.batch_create_or_update | `batchUpsertNotes` | Notes.batch_create_or_update. Create or update an batch of Notes |
| Notes.batch_delete | `batchDeleteNotes` | Notes.batch_delete. Removes Notes with given list of ids |
| Notes.batch_restore | `batchRestoreNotes` | Notes.batch_restore. Restores Notes with given list of ids |
| Notes.create | `createNote` | Notes.create. Creates new Note |
| Notes.delete | `deleteNote` | Notes.delete. Removes Note with given id |
| Notes.get | `getNote` | Notes.get. Returns Note with given id |
| Notes.list | `listNotes` | Notes.list. Returns all defined Notes |
| Notes.update | `updateNote` | Notes.update. Modifies Note or Notes with given id(s) |
| OnlineFormActivityLogLines.batch_create_or_update | `batchUpsertOnlineFormActivityLogLines` | OnlineFormActivityLogLines.batch_create_or_update. Create or update an batch of OnlineFormActivityLogLines |
| OnlineFormActivityLogLines.batch_delete | `batchDeleteOnlineFormActivityLogLines` | OnlineFormActivityLogLines.batch_delete. Removes OnlineFormActivityLogLines with given list of ids |
| OnlineFormActivityLogLines.batch_restore | `batchRestoreOnlineFormActivityLogLines` | OnlineFormActivityLogLines.batch_restore. Restores OnlineFormActivityLogLines with given list of ids |
| OnlineFormActivityLogLines.create | `createOnlineFormActivityLogLine` | OnlineFormActivityLogLines.create. Creates new OnlineFormActivityLogLine |
| OnlineFormActivityLogLines.delete | `deleteOnlineFormActivityLogLine` | OnlineFormActivityLogLines.delete. Removes OnlineFormActivityLogLine with given id |
| OnlineFormActivityLogLines.get | `getOnlineFormActivityLogLine` | OnlineFormActivityLogLines.get. Returns OnlineFormActivityLogLine with given id |
| OnlineFormActivityLogLines.list | `listOnlineFormActivityLogLines` | OnlineFormActivityLogLines.list. Returns all defined OnlineFormActivityLogLines |
| OnlineFormActivityLogLines.update | `updateOnlineFormActivityLogLine` | OnlineFormActivityLogLines.update. Modifies OnlineFormActivityLogLine or OnlineFormActivityLogLines with given id(s) |
| OnlineFormDataExRelations.batch_create_or_update | `batchUpsertOnlineFormDataExRelations` | OnlineFormDataExRelations.batch_create_or_update. Create or update an batch of OnlineFormDataExRelations |
| OnlineFormDataExRelations.batch_delete | `batchDeleteOnlineFormDataExRelations` | OnlineFormDataExRelations.batch_delete. Removes OnlineFormDataExRelations with given list of ids |
| OnlineFormDataExRelations.batch_restore | `batchRestoreOnlineFormDataExRelations` | OnlineFormDataExRelations.batch_restore. Restores OnlineFormDataExRelations with given list of ids |
| OnlineFormDataExRelations.create | `createOnlineFormDataExRelation` | OnlineFormDataExRelations.create. Creates new OnlineFormDataExRelation |
| OnlineFormDataExRelations.delete | `deleteOnlineFormDataExRelation` | OnlineFormDataExRelations.delete. Removes OnlineFormDataExRelation with given id |
| OnlineFormDataExRelations.get | `getOnlineFormDataExRelation` | OnlineFormDataExRelations.get. Returns OnlineFormDataExRelation with given id |
| OnlineFormDataExRelations.list | `listOnlineFormDataExRelations` | OnlineFormDataExRelations.list. Returns all defined OnlineFormDataExRelations |
| OnlineFormDataExRelations.update | `updateOnlineFormDataExRelation` | OnlineFormDataExRelations.update. Modifies OnlineFormDataExRelation or OnlineFormDataExRelations with given id(s) |
| OnlineFormRelations.batch_create_or_update | `batchUpsertOnlineFormRelations` | OnlineFormRelations.batch_create_or_update. Create or update an batch of OnlineFormRelations |
| OnlineFormRelations.batch_delete | `batchDeleteOnlineFormRelations` | OnlineFormRelations.batch_delete. Removes OnlineFormRelations with given list of ids |
| OnlineFormRelations.batch_restore | `batchRestoreOnlineFormRelations` | OnlineFormRelations.batch_restore. Restores OnlineFormRelations with given list of ids |
| OnlineFormRelations.create | `createOnlineFormRelation` | OnlineFormRelations.create. Creates new OnlineFormRelation |
| OnlineFormRelations.delete | `deleteOnlineFormRelation` | OnlineFormRelations.delete. Removes OnlineFormRelation with given id |
| OnlineFormRelations.get | `getOnlineFormRelation` | OnlineFormRelations.get. Returns OnlineFormRelation with given id |
| OnlineFormRelations.list | `listOnlineFormRelations` | OnlineFormRelations.list. Returns all defined OnlineFormRelations |
| OnlineFormRelations.update | `updateOnlineFormRelation` | OnlineFormRelations.update. Modifies OnlineFormRelation or OnlineFormRelations with given id(s) |
| OnlineForms.batch_create_or_update | `batchUpsertOnlineForms` | OnlineForms.batch_create_or_update. Create or update an batch of OnlineForms |
| OnlineForms.batch_delete | `batchDeleteOnlineForms` | OnlineForms.batch_delete. Removes OnlineForms with given list of ids |
| OnlineForms.batch_restore | `batchRestoreOnlineForms` | OnlineForms.batch_restore. Restores OnlineForms with given list of ids |
| OnlineForms.create | `createOnlineForm` | OnlineForms.create. Creates new OnlineForm |
| OnlineForms.delete | `deleteOnlineForm` | OnlineForms.delete. Removes OnlineForm with given id |
| OnlineForms.get | `getOnlineForm` | OnlineForms.get. Returns OnlineForm with given id |
| OnlineForms.list | `listOnlineForms` | OnlineForms.list. Returns all defined OnlineForms |
| OnlineForms.update | `updateOnlineForm` | OnlineForms.update. Modifies OnlineForm or OnlineForms with given id(s) |
| OnlineFormStyles.batch_create_or_update | `batchUpsertOnlineFormStyles` | OnlineFormStyles.batch_create_or_update. Create or update an batch of OnlineFormStyles |
| OnlineFormStyles.batch_delete | `batchDeleteOnlineFormStyles` | OnlineFormStyles.batch_delete. Removes OnlineFormStyles with given list of ids |
| OnlineFormStyles.batch_restore | `batchRestoreOnlineFormStyles` | OnlineFormStyles.batch_restore. Restores OnlineFormStyles with given list of ids |
| OnlineFormStyles.create | `createOnlineFormStyle` | OnlineFormStyles.create. Creates new OnlineFormStyle |
| OnlineFormStyles.delete | `deleteOnlineFormStyle` | OnlineFormStyles.delete. Removes OnlineFormStyle with given id |
| OnlineFormStyles.get | `getOnlineFormStyle` | OnlineFormStyles.get. Returns OnlineFormStyle with given id |
| OnlineFormStyles.list | `listOnlineFormStyles` | OnlineFormStyles.list. Returns all defined OnlineFormStyles |
| OnlineFormStyles.update | `updateOnlineFormStyle` | OnlineFormStyles.update. Modifies OnlineFormStyle or OnlineFormStyles with given id(s) |
| OnlineFormTypeEmailRelations.batch_create_or_update | `batchUpsertOnlineFormTypeEmailRelations` | OnlineFormTypeEmailRelations.batch_create_or_update. Create or update an batch of OnlineFormTypeEmailRelations |
| OnlineFormTypeEmailRelations.batch_delete | `batchDeleteOnlineFormTypeEmailRelations` | OnlineFormTypeEmailRelations.batch_delete. Removes OnlineFormTypeEmailRelations with given list of ids |
| OnlineFormTypeEmailRelations.batch_restore | `batchRestoreOnlineFormTypeEmailRelations` | OnlineFormTypeEmailRelations.batch_restore. Restores OnlineFormTypeEmailRelations with given list of ids |
| OnlineFormTypeEmailRelations.create | `createOnlineFormTypeEmailRelation` | OnlineFormTypeEmailRelations.create. Creates new OnlineFormTypeEmailRelation |
| OnlineFormTypeEmailRelations.delete | `deleteOnlineFormTypeEmailRelation` | OnlineFormTypeEmailRelations.delete. Removes OnlineFormTypeEmailRelation with given id |
| OnlineFormTypeEmailRelations.get | `getOnlineFormTypeEmailRelation` | OnlineFormTypeEmailRelations.get. Returns OnlineFormTypeEmailRelation with given id |
| OnlineFormTypeEmailRelations.list | `listOnlineFormTypeEmailRelations` | OnlineFormTypeEmailRelations.list. Returns all defined OnlineFormTypeEmailRelations |
| OnlineFormTypeEmailRelations.update | `updateOnlineFormTypeEmailRelation` | OnlineFormTypeEmailRelations.update. Modifies OnlineFormTypeEmailRelation or OnlineFormTypeEmailRelations with given id(s) |
| OnlineFormTypes.batch_create_or_update | `batchUpsertOnlineFormTypes` | OnlineFormTypes.batch_create_or_update. Create or update an batch of OnlineFormTypes |
| OnlineFormTypes.batch_delete | `batchDeleteOnlineFormTypes` | OnlineFormTypes.batch_delete. Removes OnlineFormTypes with given list of ids |
| OnlineFormTypes.batch_restore | `batchRestoreOnlineFormTypes` | OnlineFormTypes.batch_restore. Restores OnlineFormTypes with given list of ids |
| OnlineFormTypes.create | `createOnlineFormType` | OnlineFormTypes.create. Creates new OnlineFormType |
| OnlineFormTypes.delete | `deleteOnlineFormType` | OnlineFormTypes.delete. Removes OnlineFormType with given id |
| OnlineFormTypes.get | `getOnlineFormType` | OnlineFormTypes.get. Returns OnlineFormType with given id |
| OnlineFormTypes.list | `listOnlineFormTypes` | OnlineFormTypes.list. Returns all defined OnlineFormTypes |
| OnlineFormTypes.update | `updateOnlineFormType` | OnlineFormTypes.update. Modifies OnlineFormType or OnlineFormTypes with given id(s) |
| Opportunities.batch_create_or_update | `batchUpsertOpportunities` | Opportunities.batch_create_or_update. Create or update an batch of Opportunities |
| Opportunities.batch_delete | `batchDeleteOpportunities` | Opportunities.batch_delete. Removes Opportunities with given list of ids |
| Opportunities.batch_restore | `batchRestoreOpportunities` | Opportunities.batch_restore. Restores Opportunities with given list of ids |
| OpportunityTypes.batch_create_or_update | `batchUpsertOpportunityTypes` | OpportunityTypes.batch_create_or_update. Create or update an batch of OpportunityTypes |
| OpportunityTypes.batch_delete | `batchDeleteOpportunityTypes` | OpportunityTypes.batch_delete. Removes OpportunityTypes with given list of ids |
| OpportunityTypes.batch_restore | `batchRestoreOpportunityTypes` | OpportunityTypes.batch_restore. Restores OpportunityTypes with given list of ids |
| OpportunityTypes.create | `createOpportunityType` | OpportunityTypes.create. Creates new OpportunityType |
| OpportunityTypes.delete | `deleteOpportunityType` | OpportunityTypes.delete. Removes OpportunityType with given id |
| OpportunityTypes.get | `getOpportunityType` | OpportunityTypes.get. Returns OpportunityType with given id |
| OpportunityTypes.list | `listOpportunityTypes` | OpportunityTypes.list. Returns all defined OpportunityTypes |
| OpportunityTypes.update | `updateOpportunityType` | OpportunityTypes.update. Modifies OpportunityType or OpportunityTypes with given id(s) |
| OpptyProductRelationDataExRelations.batch_create_or_update | `batchUpsertOpptyProductRelationDataExRelations` | OpptyProductRelationDataExRelations.batch_create_or_update. Create or update an batch of OpptyProductRelationDataExRelations |
| OpptyProductRelationDataExRelations.batch_delete | `batchDeleteOpptyProductRelationDataExRelations` | OpptyProductRelationDataExRelations.batch_delete. Removes OpptyProductRelationDataExRelations with given list of ids |
| OpptyProductRelationDataExRelations.batch_restore | `batchRestoreOpptyProductRelationDataExRelations` | OpptyProductRelationDataExRelations.batch_restore. Restores OpptyProductRelationDataExRelations with given list of ids |
| OpptyProductRelationDataExRelations.create | `createOpptyProductRelationDataExRelation` | OpptyProductRelationDataExRelations.create. Creates new OpptyProductRelationDataExRelation |
| OpptyProductRelationDataExRelations.delete | `deleteOpptyProductRelationDataExRelation` | OpptyProductRelationDataExRelations.delete. Removes OpptyProductRelationDataExRelation with given id |
| OpptyProductRelationDataExRelations.get | `getOpptyProductRelationDataExRelation` | OpptyProductRelationDataExRelations.get. Returns OpptyProductRelationDataExRelation with given id |
| OpptyProductRelationDataExRelations.list | `listOpptyProductRelationDataExRelations` | OpptyProductRelationDataExRelations.list. Returns all defined OpptyProductRelationDataExRelations |
| OpptyProductRelationDataExRelations.update | `updateOpptyProductRelationDataExRelation` | OpptyProductRelationDataExRelations.update. Modifies OpptyProductRelationDataExRelation or OpptyProductRelationDataExRelations with given id(s) |
| OpptyProductRelationRevenueSchedulePeriods.batch_create_or_update | `batchUpsertOpptyProductRelationRevenueSchedulePeriods` | OpptyProductRelationRevenueSchedulePeriods.batch_create_or_update. Create or update an batch of OpptyProductRelationRevenueSchedulePeriods |
| OpptyProductRelationRevenueSchedulePeriods.batch_delete | `batchDeleteOpptyProductRelationRevenueSchedulePeriods` | OpptyProductRelationRevenueSchedulePeriods.batch_delete. Removes OpptyProductRelationRevenueSchedulePeriods with given list of ids |
| OpptyProductRelationRevenueSchedulePeriods.batch_restore | `batchRestoreOpptyProductRelationRevenueSchedulePeriods` | OpptyProductRelationRevenueSchedulePeriods.batch_restore. Restores OpptyProductRelationRevenueSchedulePeriods with given list of ids |
| OpptyProductRelationRevenueSchedulePeriods.create | `createOpptyProductRelationRevenueSchedulePeriod` | OpptyProductRelationRevenueSchedulePeriods.create. Creates new OpptyProductRelationRevenueSchedulePeriod |
| OpptyProductRelationRevenueSchedulePeriods.delete | `deleteOpptyProductRelationRevenueSchedulePeriod` | OpptyProductRelationRevenueSchedulePeriods.delete. Removes OpptyProductRelationRevenueSchedulePeriod with given id |
| OpptyProductRelationRevenueSchedulePeriods.get | `getOpptyProductRelationRevenueSchedulePeriod` | OpptyProductRelationRevenueSchedulePeriods.get. Returns OpptyProductRelationRevenueSchedulePeriod with given id |
| OpptyProductRelationRevenueSchedulePeriods.list | `listOpptyProductRelationRevenueSchedulePeriods` | OpptyProductRelationRevenueSchedulePeriods.list. Returns all defined OpptyProductRelationRevenueSchedulePeriods |
| OpptyProductRelationRevenueSchedulePeriods.update | `updateOpptyProductRelationRevenueSchedulePeriod` | OpptyProductRelationRevenueSchedulePeriods.update. Modifies OpptyProductRelationRevenueSchedulePeriod or OpptyProductRelationRevenueSchedulePeriods with given id(s) |
| OpptyProductRelationRevenueSchedules.batch_create_or_update | `batchUpsertOpptyProductRelationRevenueSchedules` | OpptyProductRelationRevenueSchedules.batch_create_or_update. Create or update an batch of OpptyProductRelationRevenueSchedules |
| OpptyProductRelationRevenueSchedules.batch_delete | `batchDeleteOpptyProductRelationRevenueSchedules` | OpptyProductRelationRevenueSchedules.batch_delete. Removes OpptyProductRelationRevenueSchedules with given list of ids |
| OpptyProductRelationRevenueSchedules.batch_restore | `batchRestoreOpptyProductRelationRevenueSchedules` | OpptyProductRelationRevenueSchedules.batch_restore. Restores OpptyProductRelationRevenueSchedules with given list of ids |
| OpptyProductRelationRevenueSchedules.create | `createOpptyProductRelationRevenueSchedule` | OpptyProductRelationRevenueSchedules.create. Creates new OpptyProductRelationRevenueSchedule |
| OpptyProductRelationRevenueSchedules.delete | `deleteOpptyProductRelationRevenueSchedule` | OpptyProductRelationRevenueSchedules.delete. Removes OpptyProductRelationRevenueSchedule with given id |
| OpptyProductRelationRevenueSchedules.get | `getOpptyProductRelationRevenueSchedule` | OpptyProductRelationRevenueSchedules.get. Returns OpptyProductRelationRevenueSchedule with given id |
| OpptyProductRelationRevenueSchedules.list | `listOpptyProductRelationRevenueSchedules` | OpptyProductRelationRevenueSchedules.list. Returns all defined OpptyProductRelationRevenueSchedules |
| OpptyProductRelationRevenueSchedules.update | `updateOpptyProductRelationRevenueSchedule` | OpptyProductRelationRevenueSchedules.update. Modifies OpptyProductRelationRevenueSchedule or OpptyProductRelationRevenueSchedules with given id(s) |
| OpptyProductRelations.batch_create_or_update | `batchUpsertOpptyProductRelations` | OpptyProductRelations.batch_create_or_update. Create or update an batch of OpptyProductRelations |
| OpptyProductRelations.batch_delete | `batchDeleteOpptyProductRelations` | OpptyProductRelations.batch_delete. Removes OpptyProductRelations with given list of ids |
| OpptyProductRelations.batch_restore | `batchRestoreOpptyProductRelations` | OpptyProductRelations.batch_restore. Restores OpptyProductRelations with given list of ids |
| OpptyProductRelations.create | `createOpptyProductRelation` | OpptyProductRelations.create. Creates new OpptyProductRelation |
| OpptyProductRelations.delete | `deleteOpptyProductRelation` | OpptyProductRelations.delete. Removes OpptyProductRelation with given id |
| OpptyProductRelations.get | `getOpptyProductRelation` | OpptyProductRelations.get. Returns OpptyProductRelation with given id |
| OpptyProductRelations.list | `listOpptyProductRelations` | OpptyProductRelations.list. Returns all defined OpptyProductRelations |
| OpptyProductRelations.update | `updateOpptyProductRelation` | OpptyProductRelations.update. Modifies OpptyProductRelation or OpptyProductRelations with given id(s) |
| OpptyProductRelationTypes.batch_create_or_update | `batchUpsertOpptyProductRelationTypes` | OpptyProductRelationTypes.batch_create_or_update. Create or update an batch of OpptyProductRelationTypes |
| OpptyProductRelationTypes.batch_delete | `batchDeleteOpptyProductRelationTypes` | OpptyProductRelationTypes.batch_delete. Removes OpptyProductRelationTypes with given list of ids |
| OpptyProductRelationTypes.batch_restore | `batchRestoreOpptyProductRelationTypes` | OpptyProductRelationTypes.batch_restore. Restores OpptyProductRelationTypes with given list of ids |
| OpptyProductRelationTypes.create | `createOpptyProductRelationType` | OpptyProductRelationTypes.create. Creates new OpptyProductRelationType |
| OpptyProductRelationTypes.delete | `deleteOpptyProductRelationType` | OpptyProductRelationTypes.delete. Removes OpptyProductRelationType with given id |
| OpptyProductRelationTypes.get | `getOpptyProductRelationType` | OpptyProductRelationTypes.get. Returns OpptyProductRelationType with given id |
| OpptyProductRelationTypes.list | `listOpptyProductRelationTypes` | OpptyProductRelationTypes.list. Returns all defined OpptyProductRelationTypes |
| OpptyProductRelationTypes.update | `updateOpptyProductRelationType` | OpptyProductRelationTypes.update. Modifies OpptyProductRelationType or OpptyProductRelationTypes with given id(s) |
| OpptyRecurrences.batch_create_or_update | `batchUpsertOpptyRecurrences` | OpptyRecurrences.batch_create_or_update. Create or update an batch of OpptyRecurrences |
| OpptyRecurrences.batch_delete | `batchDeleteOpptyRecurrences` | OpptyRecurrences.batch_delete. Removes OpptyRecurrences with given list of ids |
| OpptyRecurrences.batch_restore | `batchRestoreOpptyRecurrences` | OpptyRecurrences.batch_restore. Restores OpptyRecurrences with given list of ids |
| OpptyRecurrences.create | `createOpptyRecurrence` | OpptyRecurrences.create. Creates new OpptyRecurrence |
| OpptyRecurrences.delete | `deleteOpptyRecurrence` | OpptyRecurrences.delete. Removes OpptyRecurrence with given id |
| OpptyRecurrences.get | `getOpptyRecurrence` | OpptyRecurrences.get. Returns OpptyRecurrence with given id |
| OpptyRecurrences.list | `listOpptyRecurrences` | OpptyRecurrences.list. Returns all defined OpptyRecurrences |
| OpptyRecurrences.update | `updateOpptyRecurrence` | OpptyRecurrences.update. Modifies OpptyRecurrence or OpptyRecurrences with given id(s) |
| OpptyRevenueSchedulePeriods.batch_create_or_update | `batchUpsertOpptyRevenueSchedulePeriods` | OpptyRevenueSchedulePeriods.batch_create_or_update. Create or update an batch of OpptyRevenueSchedulePeriods |
| OpptyRevenueSchedulePeriods.batch_delete | `batchDeleteOpptyRevenueSchedulePeriods` | OpptyRevenueSchedulePeriods.batch_delete. Removes OpptyRevenueSchedulePeriods with given list of ids |
| OpptyRevenueSchedulePeriods.batch_restore | `batchRestoreOpptyRevenueSchedulePeriods` | OpptyRevenueSchedulePeriods.batch_restore. Restores OpptyRevenueSchedulePeriods with given list of ids |
| OpptyRevenueSchedulePeriods.create | `createOpptyRevenueSchedulePeriod` | OpptyRevenueSchedulePeriods.create. Creates new OpptyRevenueSchedulePeriod |
| OpptyRevenueSchedulePeriods.delete | `deleteOpptyRevenueSchedulePeriod` | OpptyRevenueSchedulePeriods.delete. Removes OpptyRevenueSchedulePeriod with given id |
| OpptyRevenueSchedulePeriods.get | `getOpptyRevenueSchedulePeriod` | OpptyRevenueSchedulePeriods.get. Returns OpptyRevenueSchedulePeriod with given id |
| OpptyRevenueSchedulePeriods.list | `listOpptyRevenueSchedulePeriods` | OpptyRevenueSchedulePeriods.list. Returns all defined OpptyRevenueSchedulePeriods |
| OpptyRevenueSchedulePeriods.update | `updateOpptyRevenueSchedulePeriod` | OpptyRevenueSchedulePeriods.update. Modifies OpptyRevenueSchedulePeriod or OpptyRevenueSchedulePeriods with given id(s) |
| OpptyRevenueSchedules.batch_create_or_update | `batchUpsertOpptyRevenueSchedules` | OpptyRevenueSchedules.batch_create_or_update. Create or update an batch of OpptyRevenueSchedules |
| OpptyRevenueSchedules.batch_delete | `batchDeleteOpptyRevenueSchedules` | OpptyRevenueSchedules.batch_delete. Removes OpptyRevenueSchedules with given list of ids |
| OpptyRevenueSchedules.batch_restore | `batchRestoreOpptyRevenueSchedules` | OpptyRevenueSchedules.batch_restore. Restores OpptyRevenueSchedules with given list of ids |
| OpptyRevenueSchedules.create | `createOpptyRevenueSchedule` | OpptyRevenueSchedules.create. Creates new OpptyRevenueSchedule |
| OpptyRevenueSchedules.delete | `deleteOpptyRevenueSchedule` | OpptyRevenueSchedules.delete. Removes OpptyRevenueSchedule with given id |
| OpptyRevenueSchedules.get | `getOpptyRevenueSchedule` | OpptyRevenueSchedules.get. Returns OpptyRevenueSchedule with given id |
| OpptyRevenueSchedules.list | `listOpptyRevenueSchedules` | OpptyRevenueSchedules.list. Returns all defined OpptyRevenueSchedules |
| OpptyRevenueSchedules.update | `updateOpptyRevenueSchedule` | OpptyRevenueSchedules.update. Modifies OpptyRevenueSchedule or OpptyRevenueSchedules with given id(s) |
| ParentAccountRelationTypes.batch_create_or_update | `batchUpsertParentAccountRelationTypes` | ParentAccountRelationTypes.batch_create_or_update. Create or update an batch of ParentAccountRelationTypes |
| ParentAccountRelationTypes.batch_delete | `batchDeleteParentAccountRelationTypes` | ParentAccountRelationTypes.batch_delete. Removes ParentAccountRelationTypes with given list of ids |
| ParentAccountRelationTypes.batch_restore | `batchRestoreParentAccountRelationTypes` | ParentAccountRelationTypes.batch_restore. Restores ParentAccountRelationTypes with given list of ids |
| ParentAccountRelationTypes.create | `createParentAccountRelationType` | ParentAccountRelationTypes.create. Creates new ParentAccountRelationType |
| ParentAccountRelationTypes.delete | `deleteParentAccountRelationType` | ParentAccountRelationTypes.delete. Removes ParentAccountRelationType with given id |
| ParentAccountRelationTypes.get | `getParentAccountRelationType` | ParentAccountRelationTypes.get. Returns ParentAccountRelationType with given id |
| ParentAccountRelationTypes.list | `listParentAccountRelationTypes` | ParentAccountRelationTypes.list. Returns all defined ParentAccountRelationTypes |
| ParentAccountRelationTypes.update | `updateParentAccountRelationType` | ParentAccountRelationTypes.update. Modifies ParentAccountRelationType or ParentAccountRelationTypes with given id(s) |
| Phones.batch_create_or_update | `batchUpsertPhones` | Phones.batch_create_or_update. Create or update an batch of Phones |
| Phones.batch_delete | `batchDeletePhones` | Phones.batch_delete. Removes Phones with given list of ids |
| Phones.batch_restore | `batchRestorePhones` | Phones.batch_restore. Restores Phones with given list of ids |
| Phones.create | `createPhone` | Phones.create. Creates new Phone |
| Phones.delete | `deletePhone` | Phones.delete. Removes Phone with given id |
| Phones.get | `getPhone` | Phones.get. Returns Phone with given id |
| Phones.list | `listPhones` | Phones.list. Returns all defined Phones |
| Phones.update | `updatePhone` | Phones.update. Modifies Phone or Phones with given id(s) |
| Pipelines.batch_create_or_update | `batchUpsertPipelines` | Pipelines.batch_create_or_update. Create or update an batch of Pipelines |
| Pipelines.batch_delete | `batchDeletePipelines` | Pipelines.batch_delete. Removes Pipelines with given list of ids |
| Pipelines.batch_restore | `batchRestorePipelines` | Pipelines.batch_restore. Restores Pipelines with given list of ids |
| ProcessActivityLogLines.batch_create_or_update | `batchUpsertProcessActivityLogLines` | ProcessActivityLogLines.batch_create_or_update. Create or update an batch of ProcessActivityLogLines |
| ProcessActivityLogLines.batch_delete | `batchDeleteProcessActivityLogLines` | ProcessActivityLogLines.batch_delete. Removes ProcessActivityLogLines with given list of ids |
| ProcessActivityLogLines.batch_restore | `batchRestoreProcessActivityLogLines` | ProcessActivityLogLines.batch_restore. Restores ProcessActivityLogLines with given list of ids |
| ProcessActivityLogLines.create | `createProcessActivityLogLine` | ProcessActivityLogLines.create. Creates new ProcessActivityLogLine |
| ProcessActivityLogLines.delete | `deleteProcessActivityLogLine` | ProcessActivityLogLines.delete. Removes ProcessActivityLogLine with given id |
| ProcessActivityLogLines.get | `getProcessActivityLogLine` | ProcessActivityLogLines.get. Returns ProcessActivityLogLine with given id |
| ProcessActivityLogLines.list | `listProcessActivityLogLines` | ProcessActivityLogLines.list. Returns all defined ProcessActivityLogLines |
| ProcessActivityLogLines.update | `updateProcessActivityLogLine` | ProcessActivityLogLines.update. Modifies ProcessActivityLogLine or ProcessActivityLogLines with given id(s) |
| ProcessActivityLogs.batch_create_or_update | `batchUpsertProcessActivityLogs` | ProcessActivityLogs.batch_create_or_update. Create or update an batch of ProcessActivityLogs |
| ProcessActivityLogs.batch_delete | `batchDeleteProcessActivityLogs` | ProcessActivityLogs.batch_delete. Removes ProcessActivityLogs with given list of ids |
| ProcessActivityLogs.batch_restore | `batchRestoreProcessActivityLogs` | ProcessActivityLogs.batch_restore. Restores ProcessActivityLogs with given list of ids |
| ProcessActivityLogs.create | `createProcessActivityLog` | ProcessActivityLogs.create. Creates new ProcessActivityLog |
| ProcessActivityLogs.delete | `deleteProcessActivityLog` | ProcessActivityLogs.delete. Removes ProcessActivityLog with given id |
| ProcessActivityLogs.get | `getProcessActivityLog` | ProcessActivityLogs.get. Returns ProcessActivityLog with given id |
| ProcessActivityLogs.list | `listProcessActivityLogs` | ProcessActivityLogs.list. Returns all defined ProcessActivityLogs |
| ProcessActivityLogs.update | `updateProcessActivityLog` | ProcessActivityLogs.update. Modifies ProcessActivityLog or ProcessActivityLogs with given id(s) |
| Processes.batch_create_or_update | `batchUpsertProcesses` | Processes.batch_create_or_update. Create or update an batch of Processes |
| Processes.batch_delete | `batchDeleteProcesses` | Processes.batch_delete. Removes Processes with given list of ids |
| Processes.batch_restore | `batchRestoreProcesses` | Processes.batch_restore. Restores Processes with given list of ids |
| Processes.create | `createProcess` | Processes.create. Creates new Process |
| Processes.delete | `deleteProcess` | Processes.delete. Removes Process with given id |
| Processes.get | `getProcess` | Processes.get. Returns Process with given id |
| Processes.list | `listProcesses` | Processes.list. Returns all defined Processes |
| Processes.update | `updateProcess` | Processes.update. Modifies Process or Processes with given id(s) |
| ProcessTemplates.batch_create_or_update | `batchUpsertProcessTemplates` | ProcessTemplates.batch_create_or_update. Create or update an batch of ProcessTemplates |
| ProcessTemplates.batch_delete | `batchDeleteProcessTemplates` | ProcessTemplates.batch_delete. Removes ProcessTemplates with given list of ids |
| ProcessTemplates.batch_restore | `batchRestoreProcessTemplates` | ProcessTemplates.batch_restore. Restores ProcessTemplates with given list of ids |
| ProcessTemplates.create | `createProcessTemplate` | ProcessTemplates.create. Creates new ProcessTemplate |
| ProcessTemplates.delete | `deleteProcessTemplate` | ProcessTemplates.delete. Removes ProcessTemplate with given id |
| ProcessTemplates.get | `getProcessTemplate` | ProcessTemplates.get. Returns ProcessTemplate with given id |
| ProcessTemplates.list | `listProcessTemplates` | ProcessTemplates.list. Returns all defined ProcessTemplates |
| ProcessTemplates.update | `updateProcessTemplate` | ProcessTemplates.update. Modifies ProcessTemplate or ProcessTemplates with given id(s) |
| ProductCategories.batch_create_or_update | `batchUpsertProductCategories` | ProductCategories.batch_create_or_update. Create or update an batch of ProductCategories |
| ProductCategories.batch_delete | `batchDeleteProductCategories` | ProductCategories.batch_delete. Removes ProductCategories with given list of ids |
| ProductCategories.batch_restore | `batchRestoreProductCategories` | ProductCategories.batch_restore. Restores ProductCategories with given list of ids |
| ProductCategories.create | `createProductCategory` | ProductCategories.create. Creates new ProductCategory |
| ProductCategories.delete | `deleteProductCategory` | ProductCategories.delete. Removes ProductCategory with given id |
| ProductCategories.get | `getProductCategory` | ProductCategories.get. Returns ProductCategory with given id |
| ProductCategories.list | `listProductCategories` | ProductCategories.list. Returns all defined ProductCategories |
| ProductCategories.update | `updateProductCategory` | ProductCategories.update. Modifies ProductCategory or ProductCategories with given id(s) |
| ProductDataExRelations.get | `getProductDataExRelation` | ProductDataExRelations.get. Returns ProductDataExRelation with given id |
| ProductDataExRelations.list | `listProductDataExRelations` | ProductDataExRelations.list. Returns all defined ProductDataExRelations |
| ProductPipelineRelations.batch_create_or_update | `batchUpsertProductPipelineRelations` | ProductPipelineRelations.batch_create_or_update. Create or update an batch of ProductPipelineRelations |
| ProductPipelineRelations.batch_delete | `batchDeleteProductPipelineRelations` | ProductPipelineRelations.batch_delete. Removes ProductPipelineRelations with given list of ids |
| ProductPipelineRelations.batch_restore | `batchRestoreProductPipelineRelations` | ProductPipelineRelations.batch_restore. Restores ProductPipelineRelations with given list of ids |
| ProductPipelineRelations.create | `createProductPipelineRelation` | ProductPipelineRelations.create. Creates new ProductPipelineRelation |
| ProductPipelineRelations.delete | `deleteProductPipelineRelation` | ProductPipelineRelations.delete. Removes ProductPipelineRelation with given id |
| ProductPipelineRelations.get | `getProductPipelineRelation` | ProductPipelineRelations.get. Returns ProductPipelineRelation with given id |
| ProductPipelineRelations.list | `listProductPipelineRelations` | ProductPipelineRelations.list. Returns all defined ProductPipelineRelations |
| ProductPipelineRelations.update | `updateProductPipelineRelation` | ProductPipelineRelations.update. Modifies ProductPipelineRelation or ProductPipelineRelations with given id(s) |
| ProductPriceListPrices.batch_create_or_update | `batchUpsertProductPriceListPrices` | ProductPriceListPrices.batch_create_or_update. Create or update an batch of ProductPriceListPrices |
| ProductPriceListPrices.batch_delete | `batchDeleteProductPriceListPrices` | ProductPriceListPrices.batch_delete. Removes ProductPriceListPrices with given list of ids |
| ProductPriceListPrices.batch_restore | `batchRestoreProductPriceListPrices` | ProductPriceListPrices.batch_restore. Restores ProductPriceListPrices with given list of ids |
| ProductPriceListPrices.create | `createProductPriceListPrice` | ProductPriceListPrices.create. Creates new ProductPriceListPrice |
| ProductPriceListPrices.delete | `deleteProductPriceListPrice` | ProductPriceListPrices.delete. Removes ProductPriceListPrice with given id |
| ProductPriceListPrices.get | `getProductPriceListPrice` | ProductPriceListPrices.get. Returns ProductPriceListPrice with given id |
| ProductPriceListPrices.list | `listProductPriceListPrices` | ProductPriceListPrices.list. Returns all defined ProductPriceListPrices |
| ProductPriceListPrices.update | `updateProductPriceListPrice` | ProductPriceListPrices.update. Modifies ProductPriceListPrice or ProductPriceListPrices with given id(s) |
| ProductPriceLists.batch_create_or_update | `batchUpsertProductPriceLists` | ProductPriceLists.batch_create_or_update. Create or update an batch of ProductPriceLists |
| ProductPriceLists.batch_delete | `batchDeleteProductPriceLists` | ProductPriceLists.batch_delete. Removes ProductPriceLists with given list of ids |
| ProductPriceLists.batch_restore | `batchRestoreProductPriceLists` | ProductPriceLists.batch_restore. Restores ProductPriceLists with given list of ids |
| ProductPriceLists.create | `createProductPriceList` | ProductPriceLists.create. Creates new ProductPriceList |
| ProductPriceLists.delete | `deleteProductPriceList` | ProductPriceLists.delete. Removes ProductPriceList with given id |
| ProductPriceLists.get | `getProductPriceList` | ProductPriceLists.get. Returns ProductPriceList with given id |
| ProductPriceLists.list | `listProductPriceLists` | ProductPriceLists.list. Returns all defined ProductPriceLists |
| ProductPriceLists.update | `updateProductPriceList` | ProductPriceLists.update. Modifies ProductPriceList or ProductPriceLists with given id(s) |
| Products.batch_create_or_update | `batchUpsertProducts` | Products.batch_create_or_update. Create or update an batch of Products |
| Products.batch_delete | `batchDeleteProducts` | Products.batch_delete. Removes Products with given list of ids |
| Products.batch_restore | `batchRestoreProducts` | Products.batch_restore. Restores Products with given list of ids |
| ProductTypes.batch_create_or_update | `batchUpsertProductTypes` | ProductTypes.batch_create_or_update. Create or update an batch of ProductTypes |
| ProductTypes.batch_delete | `batchDeleteProductTypes` | ProductTypes.batch_delete. Removes ProductTypes with given list of ids |
| ProductTypes.batch_restore | `batchRestoreProductTypes` | ProductTypes.batch_restore. Restores ProductTypes with given list of ids |
| ProductTypes.create | `createProductType` | ProductTypes.create. Creates new ProductType |
| ProductTypes.delete | `deleteProductType` | ProductTypes.delete. Removes ProductType with given id |
| ProductTypes.get | `getProductType` | ProductTypes.get. Returns ProductType with given id |
| ProductTypes.list | `listProductTypes` | ProductTypes.list. Returns all defined ProductTypes |
| ProductTypes.update | `updateProductType` | ProductTypes.update. Modifies ProductType or ProductTypes with given id(s) |
| ProfileRelations.batch_create_or_update | `batchUpsertProfileRelations` | ProfileRelations.batch_create_or_update. Create or update an batch of ProfileRelations |
| ProfileRelations.batch_delete | `batchDeleteProfileRelations` | ProfileRelations.batch_delete. Removes ProfileRelations with given list of ids |
| ProfileRelations.batch_restore | `batchRestoreProfileRelations` | ProfileRelations.batch_restore. Restores ProfileRelations with given list of ids |
| ProfileRelations.create | `createProfileRelation` | ProfileRelations.create. Creates new ProfileRelation |
| ProfileRelations.delete | `deleteProfileRelation` | ProfileRelations.delete. Removes ProfileRelation with given id |
| ProfileRelations.get | `getProfileRelation` | ProfileRelations.get. Returns ProfileRelation with given id |
| ProfileRelations.list | `listProfileRelations` | ProfileRelations.list. Returns all defined ProfileRelations |
| ProfileRelations.update | `updateProfileRelation` | ProfileRelations.update. Modifies ProfileRelation or ProfileRelations with given id(s) |
| Profiles.get | `getProfile` | Profiles.get. Returns Profile with given id |
| Profiles.list | `listProfiles` | Profiles.list. Returns all defined Profiles |
| ProfileSharingClientRelations.get | `getProfileSharingClientRelation` | ProfileSharingClientRelations.get. Returns ProfileSharingClientRelation with given id |
| ProfileSharingClientRelations.list | `listProfileSharingClientRelations` | ProfileSharingClientRelations.list. Returns all defined ProfileSharingClientRelations |
| ProfileSharingSalesUnitRelations.get | `getProfileSharingSalesUnitRelation` | ProfileSharingSalesUnitRelations.get. Returns ProfileSharingSalesUnitRelation with given id |
| ProfileSharingSalesUnitRelations.list | `listProfileSharingSalesUnitRelations` | ProfileSharingSalesUnitRelations.list. Returns all defined ProfileSharingSalesUnitRelations |
| ProjectContactRelations.batch_create_or_update | `batchUpsertProjectContactRelations` | ProjectContactRelations.batch_create_or_update. Create or update an batch of ProjectContactRelations |
| ProjectContactRelations.batch_delete | `batchDeleteProjectContactRelations` | ProjectContactRelations.batch_delete. Removes ProjectContactRelations with given list of ids |
| ProjectContactRelations.batch_restore | `batchRestoreProjectContactRelations` | ProjectContactRelations.batch_restore. Restores ProjectContactRelations with given list of ids |
| ProjectContactRelations.create | `createProjectContactRelation` | ProjectContactRelations.create. Creates new ProjectContactRelation |
| ProjectContactRelations.delete | `deleteProjectContactRelation` | ProjectContactRelations.delete. Removes ProjectContactRelation with given id |
| ProjectContactRelations.get | `getProjectContactRelation` | ProjectContactRelations.get. Returns ProjectContactRelation with given id |
| ProjectContactRelations.list | `listProjectContactRelations` | ProjectContactRelations.list. Returns all defined ProjectContactRelations |
| ProjectContactRelations.update | `updateProjectContactRelation` | ProjectContactRelations.update. Modifies ProjectContactRelation or ProjectContactRelations with given id(s) |
| ProjectDataExRelations.get | `getProjectDataExRelation` | ProjectDataExRelations.get. Returns ProjectDataExRelation with given id |
| ProjectDataExRelations.list | `listProjectDataExRelations` | ProjectDataExRelations.list. Returns all defined ProjectDataExRelations |
| ProjectKPIs.batch_create_or_update | `batchUpsertProjectKPIs` | ProjectKPIs.batch_create_or_update. Create or update an batch of ProjectKPIs |
| ProjectKPIs.batch_delete | `batchDeleteProjectKPIs` | ProjectKPIs.batch_delete. Removes ProjectKPIs with given list of ids |
| ProjectKPIs.batch_restore | `batchRestoreProjectKPIs` | ProjectKPIs.batch_restore. Restores ProjectKPIs with given list of ids |
| ProjectKPIs.create | `createProjectKPI` | ProjectKPIs.create. Creates new ProjectKPI |
| ProjectKPIs.delete | `deleteProjectKPI` | ProjectKPIs.delete. Removes ProjectKPI with given id |
| ProjectKPIs.get | `getProjectKPI` | ProjectKPIs.get. Returns ProjectKPI with given id |
| ProjectKPIs.list | `listProjectKPIs` | ProjectKPIs.list. Returns all defined ProjectKPIs |
| ProjectKPIs.update | `updateProjectKPI` | ProjectKPIs.update. Modifies ProjectKPI or ProjectKPIs with given id(s) |
| ProjectObjectives.batch_create_or_update | `batchUpsertProjectObjectives` | ProjectObjectives.batch_create_or_update. Create or update an batch of ProjectObjectives |
| ProjectObjectives.batch_delete | `batchDeleteProjectObjectives` | ProjectObjectives.batch_delete. Removes ProjectObjectives with given list of ids |
| ProjectObjectives.batch_restore | `batchRestoreProjectObjectives` | ProjectObjectives.batch_restore. Restores ProjectObjectives with given list of ids |
| ProjectObjectives.create | `createProjectObjective` | ProjectObjectives.create. Creates new ProjectObjective |
| ProjectObjectives.delete | `deleteProjectObjective` | ProjectObjectives.delete. Removes ProjectObjective with given id |
| ProjectObjectives.get | `getProjectObjective` | ProjectObjectives.get. Returns ProjectObjective with given id |
| ProjectObjectives.list | `listProjectObjectives` | ProjectObjectives.list. Returns all defined ProjectObjectives |
| ProjectObjectives.update | `updateProjectObjective` | ProjectObjectives.update. Modifies ProjectObjective or ProjectObjectives with given id(s) |
| Projects.batch_create_or_update | `batchUpsertProjects` | Projects.batch_create_or_update. Create or update an batch of Projects |
| Projects.batch_delete | `batchDeleteProjects` | Projects.batch_delete. Removes Projects with given list of ids |
| Projects.batch_restore | `batchRestoreProjects` | Projects.batch_restore. Restores Projects with given list of ids |
| Projects.create | `createProject` | Projects.create. Creates new Project |
| Projects.delete | `deleteProject` | Projects.delete. Removes Project with given id |
| Projects.get | `getProject` | Projects.get. Returns Project with given id |
| Projects.list | `listProjects` | Projects.list. Returns all defined Projects |
| Projects.update | `updateProject` | Projects.update. Modifies Project or Projects with given id(s) |
| ProjectSharingClientRelations.batch_create_or_update | `batchUpsertProjectSharingClientRelations` | ProjectSharingClientRelations.batch_create_or_update. Create or update an batch of ProjectSharingClientRelations |
| ProjectSharingClientRelations.batch_delete | `batchDeleteProjectSharingClientRelations` | ProjectSharingClientRelations.batch_delete. Removes ProjectSharingClientRelations with given list of ids |
| ProjectSharingClientRelations.batch_restore | `batchRestoreProjectSharingClientRelations` | ProjectSharingClientRelations.batch_restore. Restores ProjectSharingClientRelations with given list of ids |
| ProjectSharingClientRelations.create | `createProjectSharingClientRelation` | ProjectSharingClientRelations.create. Creates new ProjectSharingClientRelation |
| ProjectSharingClientRelations.delete | `deleteProjectSharingClientRelation` | ProjectSharingClientRelations.delete. Removes ProjectSharingClientRelation with given id |
| ProjectSharingClientRelations.get | `getProjectSharingClientRelation` | ProjectSharingClientRelations.get. Returns ProjectSharingClientRelation with given id |
| ProjectSharingClientRelations.list | `listProjectSharingClientRelations` | ProjectSharingClientRelations.list. Returns all defined ProjectSharingClientRelations |
| ProjectSharingClientRelations.update | `updateProjectSharingClientRelation` | ProjectSharingClientRelations.update. Modifies ProjectSharingClientRelation or ProjectSharingClientRelations with given id(s) |
| ProjectSharingSalesUnitRelations.batch_create_or_update | `batchUpsertProjectSharingSalesUnitRelations` | ProjectSharingSalesUnitRelations.batch_create_or_update. Create or update an batch of ProjectSharingSalesUnitRelations |
| ProjectSharingSalesUnitRelations.batch_delete | `batchDeleteProjectSharingSalesUnitRelations` | ProjectSharingSalesUnitRelations.batch_delete. Removes ProjectSharingSalesUnitRelations with given list of ids |
| ProjectSharingSalesUnitRelations.batch_restore | `batchRestoreProjectSharingSalesUnitRelations` | ProjectSharingSalesUnitRelations.batch_restore. Restores ProjectSharingSalesUnitRelations with given list of ids |
| ProjectSharingSalesUnitRelations.create | `createProjectSharingSalesUnitRelation` | ProjectSharingSalesUnitRelations.create. Creates new ProjectSharingSalesUnitRelation |
| ProjectSharingSalesUnitRelations.delete | `deleteProjectSharingSalesUnitRelation` | ProjectSharingSalesUnitRelations.delete. Removes ProjectSharingSalesUnitRelation with given id |
| ProjectSharingSalesUnitRelations.get | `getProjectSharingSalesUnitRelation` | ProjectSharingSalesUnitRelations.get. Returns ProjectSharingSalesUnitRelation with given id |
| ProjectSharingSalesUnitRelations.list | `listProjectSharingSalesUnitRelations` | ProjectSharingSalesUnitRelations.list. Returns all defined ProjectSharingSalesUnitRelations |
| ProjectSharingSalesUnitRelations.update | `updateProjectSharingSalesUnitRelation` | ProjectSharingSalesUnitRelations.update. Modifies ProjectSharingSalesUnitRelation or ProjectSharingSalesUnitRelations with given id(s) |
| ProjectTypes.batch_create_or_update | `batchUpsertProjectTypes` | ProjectTypes.batch_create_or_update. Create or update an batch of ProjectTypes |
| ProjectTypes.batch_delete | `batchDeleteProjectTypes` | ProjectTypes.batch_delete. Removes ProjectTypes with given list of ids |
| ProjectTypes.batch_restore | `batchRestoreProjectTypes` | ProjectTypes.batch_restore. Restores ProjectTypes with given list of ids |
| ProjectTypes.create | `createProjectType` | ProjectTypes.create. Creates new ProjectType |
| ProjectTypes.delete | `deleteProjectType` | ProjectTypes.delete. Removes ProjectType with given id |
| ProjectTypes.get | `getProjectType` | ProjectTypes.get. Returns ProjectType with given id |
| ProjectTypes.list | `listProjectTypes` | ProjectTypes.list. Returns all defined ProjectTypes |
| ProjectTypes.update | `updateProjectType` | ProjectTypes.update. Modifies ProjectType or ProjectTypes with given id(s) |
| QuoteAccountRelations.batch_create_or_update | `batchUpsertQuoteAccountRelations` | QuoteAccountRelations.batch_create_or_update. Create or update an batch of QuoteAccountRelations |
| QuoteAccountRelations.batch_delete | `batchDeleteQuoteAccountRelations` | QuoteAccountRelations.batch_delete. Removes QuoteAccountRelations with given list of ids |
| QuoteAccountRelations.batch_restore | `batchRestoreQuoteAccountRelations` | QuoteAccountRelations.batch_restore. Restores QuoteAccountRelations with given list of ids |
| QuoteAccountRelations.create | `createQuoteAccountRelation` | QuoteAccountRelations.create. Creates new QuoteAccountRelation |
| QuoteAccountRelations.delete | `deleteQuoteAccountRelation` | QuoteAccountRelations.delete. Removes QuoteAccountRelation with given id |
| QuoteAccountRelations.get | `getQuoteAccountRelation` | QuoteAccountRelations.get. Returns QuoteAccountRelation with given id |
| QuoteAccountRelations.list | `listQuoteAccountRelations` | QuoteAccountRelations.list. Returns all defined QuoteAccountRelations |
| QuoteAccountRelations.update | `updateQuoteAccountRelation` | QuoteAccountRelations.update. Modifies QuoteAccountRelation or QuoteAccountRelations with given id(s) |
| QuoteContactRelations.batch_create_or_update | `batchUpsertQuoteContactRelations` | QuoteContactRelations.batch_create_or_update. Create or update an batch of QuoteContactRelations |
| QuoteContactRelations.batch_delete | `batchDeleteQuoteContactRelations` | QuoteContactRelations.batch_delete. Removes QuoteContactRelations with given list of ids |
| QuoteContactRelations.batch_restore | `batchRestoreQuoteContactRelations` | QuoteContactRelations.batch_restore. Restores QuoteContactRelations with given list of ids |
| QuoteContactRelations.create | `createQuoteContactRelation` | QuoteContactRelations.create. Creates new QuoteContactRelation |
| QuoteContactRelations.delete | `deleteQuoteContactRelation` | QuoteContactRelations.delete. Removes QuoteContactRelation with given id |
| QuoteContactRelations.get | `getQuoteContactRelation` | QuoteContactRelations.get. Returns QuoteContactRelation with given id |
| QuoteContactRelations.list | `listQuoteContactRelations` | QuoteContactRelations.list. Returns all defined QuoteContactRelations |
| QuoteContactRelations.update | `updateQuoteContactRelation` | QuoteContactRelations.update. Modifies QuoteContactRelation or QuoteContactRelations with given id(s) |
| QuoteDataExRelations.batch_create_or_update | `batchUpsertQuoteDataExRelations` | QuoteDataExRelations.batch_create_or_update. Create or update an batch of QuoteDataExRelations |
| QuoteDataExRelations.batch_delete | `batchDeleteQuoteDataExRelations` | QuoteDataExRelations.batch_delete. Removes QuoteDataExRelations with given list of ids |
| QuoteDataExRelations.batch_restore | `batchRestoreQuoteDataExRelations` | QuoteDataExRelations.batch_restore. Restores QuoteDataExRelations with given list of ids |
| QuoteDataExRelations.create | `createQuoteDataExRelation` | QuoteDataExRelations.create. Creates new QuoteDataExRelation |
| QuoteDataExRelations.delete | `deleteQuoteDataExRelation` | QuoteDataExRelations.delete. Removes QuoteDataExRelation with given id |
| QuoteDataExRelations.get | `getQuoteDataExRelation` | QuoteDataExRelations.get. Returns QuoteDataExRelation with given id |
| QuoteDataExRelations.list | `listQuoteDataExRelations` | QuoteDataExRelations.list. Returns all defined QuoteDataExRelations |
| QuoteDataExRelations.update | `updateQuoteDataExRelation` | QuoteDataExRelations.update. Modifies QuoteDataExRelation or QuoteDataExRelations with given id(s) |
| QuoteKPIs.batch_create_or_update | `batchUpsertQuoteKPIs` | QuoteKPIs.batch_create_or_update. Create or update an batch of QuoteKPIs |
| QuoteKPIs.batch_delete | `batchDeleteQuoteKPIs` | QuoteKPIs.batch_delete. Removes QuoteKPIs with given list of ids |
| QuoteKPIs.batch_restore | `batchRestoreQuoteKPIs` | QuoteKPIs.batch_restore. Restores QuoteKPIs with given list of ids |
| QuoteKPIs.create | `createQuoteKPI` | QuoteKPIs.create. Creates new QuoteKPI |
| QuoteKPIs.delete | `deleteQuoteKPI` | QuoteKPIs.delete. Removes QuoteKPI with given id |
| QuoteKPIs.get | `getQuoteKPI` | QuoteKPIs.get. Returns QuoteKPI with given id |
| QuoteKPIs.list | `listQuoteKPIs` | QuoteKPIs.list. Returns all defined QuoteKPIs |
| QuoteKPIs.update | `updateQuoteKPI` | QuoteKPIs.update. Modifies QuoteKPI or QuoteKPIs with given id(s) |
| QuoteProcesses.batch_create_or_update | `batchUpsertQuoteProcesses` | QuoteProcesses.batch_create_or_update. Create or update an batch of QuoteProcesses |
| QuoteProcesses.batch_delete | `batchDeleteQuoteProcesses` | QuoteProcesses.batch_delete. Removes QuoteProcesses with given list of ids |
| QuoteProcesses.batch_restore | `batchRestoreQuoteProcesses` | QuoteProcesses.batch_restore. Restores QuoteProcesses with given list of ids |
| QuoteProcesses.create | `createQuoteProcess` | QuoteProcesses.create. Creates new QuoteProcess |
| QuoteProcesses.delete | `deleteQuoteProcess` | QuoteProcesses.delete. Removes QuoteProcess with given id |
| QuoteProcesses.get | `getQuoteProcess` | QuoteProcesses.get. Returns QuoteProcess with given id |
| QuoteProcesses.list | `listQuoteProcesses` | QuoteProcesses.list. Returns all defined QuoteProcesses |
| QuoteProcesses.update | `updateQuoteProcess` | QuoteProcesses.update. Modifies QuoteProcess or QuoteProcesses with given id(s) |
| Quotes.batch_create_or_update | `batchUpsertQuotes` | Quotes.batch_create_or_update. Create or update an batch of Quotes |
| Quotes.batch_delete | `batchDeleteQuotes` | Quotes.batch_delete. Removes Quotes with given list of ids |
| Quotes.batch_restore | `batchRestoreQuotes` | Quotes.batch_restore. Restores Quotes with given list of ids |
| QuoteSharingClientRelations.batch_create_or_update | `batchUpsertQuoteSharingClientRelations` | QuoteSharingClientRelations.batch_create_or_update. Create or update an batch of QuoteSharingClientRelations |
| QuoteSharingClientRelations.batch_delete | `batchDeleteQuoteSharingClientRelations` | QuoteSharingClientRelations.batch_delete. Removes QuoteSharingClientRelations with given list of ids |
| QuoteSharingClientRelations.batch_restore | `batchRestoreQuoteSharingClientRelations` | QuoteSharingClientRelations.batch_restore. Restores QuoteSharingClientRelations with given list of ids |
| QuoteSharingClientRelations.create | `createQuoteSharingClientRelation` | QuoteSharingClientRelations.create. Creates new QuoteSharingClientRelation |
| QuoteSharingClientRelations.delete | `deleteQuoteSharingClientRelation` | QuoteSharingClientRelations.delete. Removes QuoteSharingClientRelation with given id |
| QuoteSharingClientRelations.get | `getQuoteSharingClientRelation` | QuoteSharingClientRelations.get. Returns QuoteSharingClientRelation with given id |
| QuoteSharingClientRelations.list | `listQuoteSharingClientRelations` | QuoteSharingClientRelations.list. Returns all defined QuoteSharingClientRelations |
| QuoteSharingClientRelations.update | `updateQuoteSharingClientRelation` | QuoteSharingClientRelations.update. Modifies QuoteSharingClientRelation or QuoteSharingClientRelations with given id(s) |
| QuoteSharingSalesUnitRelations.batch_create_or_update | `batchUpsertQuoteSharingSalesUnitRelations` | QuoteSharingSalesUnitRelations.batch_create_or_update. Create or update an batch of QuoteSharingSalesUnitRelations |
| QuoteSharingSalesUnitRelations.batch_delete | `batchDeleteQuoteSharingSalesUnitRelations` | QuoteSharingSalesUnitRelations.batch_delete. Removes QuoteSharingSalesUnitRelations with given list of ids |
| QuoteSharingSalesUnitRelations.batch_restore | `batchRestoreQuoteSharingSalesUnitRelations` | QuoteSharingSalesUnitRelations.batch_restore. Restores QuoteSharingSalesUnitRelations with given list of ids |
| QuoteSharingSalesUnitRelations.create | `createQuoteSharingSalesUnitRelation` | QuoteSharingSalesUnitRelations.create. Creates new QuoteSharingSalesUnitRelation |
| QuoteSharingSalesUnitRelations.delete | `deleteQuoteSharingSalesUnitRelation` | QuoteSharingSalesUnitRelations.delete. Removes QuoteSharingSalesUnitRelation with given id |
| QuoteSharingSalesUnitRelations.get | `getQuoteSharingSalesUnitRelation` | QuoteSharingSalesUnitRelations.get. Returns QuoteSharingSalesUnitRelation with given id |
| QuoteSharingSalesUnitRelations.list | `listQuoteSharingSalesUnitRelations` | QuoteSharingSalesUnitRelations.list. Returns all defined QuoteSharingSalesUnitRelations |
| QuoteSharingSalesUnitRelations.update | `updateQuoteSharingSalesUnitRelation` | QuoteSharingSalesUnitRelations.update. Modifies QuoteSharingSalesUnitRelation or QuoteSharingSalesUnitRelations with given id(s) |
| QuoteTypes.batch_create_or_update | `batchUpsertQuoteTypes` | QuoteTypes.batch_create_or_update. Create or update an batch of QuoteTypes |
| QuoteTypes.batch_delete | `batchDeleteQuoteTypes` | QuoteTypes.batch_delete. Removes QuoteTypes with given list of ids |
| QuoteTypes.batch_restore | `batchRestoreQuoteTypes` | QuoteTypes.batch_restore. Restores QuoteTypes with given list of ids |
| QuoteTypes.create | `createQuoteType` | QuoteTypes.create. Creates new QuoteType |
| QuoteTypes.delete | `deleteQuoteType` | QuoteTypes.delete. Removes QuoteType with given id |
| QuoteTypes.get | `getQuoteType` | QuoteTypes.get. Returns QuoteType with given id |
| QuoteTypes.list | `listQuoteTypes` | QuoteTypes.list. Returns all defined QuoteTypes |
| QuoteTypes.update | `updateQuoteType` | QuoteTypes.update. Modifies QuoteType or QuoteTypes with given id(s) |
| ReportFolders.get | `getReportFolder` | ReportFolders.get. Returns ReportFolder with given id |
| ReportFolders.list | `listReportFolders` | ReportFolders.list. Returns all defined ReportFolders |
| Reports.get | `getReport` | Reports.get. Returns Report with given id |
| Reports.list | `listReports` | Reports.list. Returns all defined Reports |
| ReportSchedules.batch_create_or_update | `batchUpsertReportSchedules` | ReportSchedules.batch_create_or_update. Create or update an batch of ReportSchedules |
| ReportSchedules.batch_delete | `batchDeleteReportSchedules` | ReportSchedules.batch_delete. Removes ReportSchedules with given list of ids |
| ReportSchedules.batch_restore | `batchRestoreReportSchedules` | ReportSchedules.batch_restore. Restores ReportSchedules with given list of ids |
| ReportSchedules.create | `createReportSchedule` | ReportSchedules.create. Creates new ReportSchedule |
| ReportSchedules.delete | `deleteReportSchedule` | ReportSchedules.delete. Removes ReportSchedule with given id |
| ReportSchedules.get | `getReportSchedule` | ReportSchedules.get. Returns ReportSchedule with given id |
| ReportSchedules.list | `listReportSchedules` | ReportSchedules.list. Returns all defined ReportSchedules |
| ReportSchedules.update | `updateReportSchedule` | ReportSchedules.update. Modifies ReportSchedule or ReportSchedules with given id(s) |
| ReportSharingClientRelations.get | `getReportSharingClientRelation` | ReportSharingClientRelations.get. Returns ReportSharingClientRelation with given id |
| ReportSharingClientRelations.list | `listReportSharingClientRelations` | ReportSharingClientRelations.list. Returns all defined ReportSharingClientRelations |
| ReportSharingSalesUnitRelations.get | `getReportSharingSalesUnitRelation` | ReportSharingSalesUnitRelations.get. Returns ReportSharingSalesUnitRelation with given id |
| ReportSharingSalesUnitRelations.list | `listReportSharingSalesUnitRelations` | ReportSharingSalesUnitRelations.list. Returns all defined ReportSharingSalesUnitRelations |
| SalesRoles.batch_create_or_update | `batchUpsertSalesRoles` | SalesRoles.batch_create_or_update. Create or update an batch of SalesRoles |
| SalesRoles.batch_delete | `batchDeleteSalesRoles` | SalesRoles.batch_delete. Removes SalesRoles with given list of ids |
| SalesRoles.batch_restore | `batchRestoreSalesRoles` | SalesRoles.batch_restore. Restores SalesRoles with given list of ids |
| SalesRoles.create | `createSalesRole` | SalesRoles.create. Creates new SalesRole |
| SalesRoles.delete | `deleteSalesRole` | SalesRoles.delete. Removes SalesRole with given id |
| SalesRoles.get | `getSalesRole` | SalesRoles.get. Returns SalesRole with given id |
| SalesRoles.list | `listSalesRoles` | SalesRoles.list. Returns all defined SalesRoles |
| SalesRoles.update | `updateSalesRole` | SalesRoles.update. Modifies SalesRole or SalesRoles with given id(s) |
| SalesUnitClientRelations.get | `getSalesUnitClientRelation` | SalesUnitClientRelations.get. Returns SalesUnitClientRelation with given id |
| SalesUnitClientRelations.list | `listSalesUnitClientRelations` | SalesUnitClientRelations.list. Returns all defined SalesUnitClientRelations |
| SalesUnits.batch_create_or_update | `batchUpsertSalesUnits` | SalesUnits.batch_create_or_update. Create or update an batch of SalesUnits |
| SalesUnits.batch_delete | `batchDeleteSalesUnits` | SalesUnits.batch_delete. Removes SalesUnits with given list of ids |
| SalesUnits.batch_restore | `batchRestoreSalesUnits` | SalesUnits.batch_restore. Restores SalesUnits with given list of ids |
| SalesUnits.create | `createSalesUnit` | SalesUnits.create. Creates new SalesUnit |
| SalesUnits.delete | `deleteSalesUnit` | SalesUnits.delete. Removes SalesUnit with given id |
| SalesUnits.get | `getSalesUnit` | SalesUnits.get. Returns SalesUnit with given id |
| SalesUnits.list | `listSalesUnits` | SalesUnits.list. Returns all defined SalesUnits |
| SalesUnits.update | `updateSalesUnit` | SalesUnits.update. Modifies SalesUnit or SalesUnits with given id(s) |
| Solutions.batch_create_or_update | `batchUpsertSolutions` | Solutions.batch_create_or_update. Create or update an batch of Solutions |
| Solutions.batch_delete | `batchDeleteSolutions` | Solutions.batch_delete. Removes Solutions with given list of ids |
| Solutions.batch_restore | `batchRestoreSolutions` | Solutions.batch_restore. Restores Solutions with given list of ids |
| Solutions.create | `createSolution` | Solutions.create. Creates new Solution |
| Solutions.delete | `deleteSolution` | Solutions.delete. Removes Solution with given id |
| Solutions.get | `getSolution` | Solutions.get. Returns Solution with given id |
| Solutions.list | `listSolutions` | Solutions.list. Returns all defined Solutions |
| Solutions.update | `updateSolution` | Solutions.update. Modifies Solution or Solutions with given id(s) |
| SolutionTemplates.batch_create_or_update | `batchUpsertSolutionTemplates` | SolutionTemplates.batch_create_or_update. Create or update an batch of SolutionTemplates |
| SolutionTemplates.batch_delete | `batchDeleteSolutionTemplates` | SolutionTemplates.batch_delete. Removes SolutionTemplates with given list of ids |
| SolutionTemplates.batch_restore | `batchRestoreSolutionTemplates` | SolutionTemplates.batch_restore. Restores SolutionTemplates with given list of ids |
| SolutionTemplates.create | `createSolutionTemplate` | SolutionTemplates.create. Creates new SolutionTemplate |
| SolutionTemplates.delete | `deleteSolutionTemplate` | SolutionTemplates.delete. Removes SolutionTemplate with given id |
| SolutionTemplates.get | `getSolutionTemplate` | SolutionTemplates.get. Returns SolutionTemplate with given id |
| SolutionTemplates.list | `listSolutionTemplates` | SolutionTemplates.list. Returns all defined SolutionTemplates |
| SolutionTemplates.update | `updateSolutionTemplate` | SolutionTemplates.update. Modifies SolutionTemplate or SolutionTemplates with given id(s) |
| StepChecklists.batch_create_or_update | `batchUpsertStepChecklists` | StepChecklists.batch_create_or_update. Create or update an batch of StepChecklists |
| StepChecklists.batch_delete | `batchDeleteStepChecklists` | StepChecklists.batch_delete. Removes StepChecklists with given list of ids |
| StepChecklists.batch_restore | `batchRestoreStepChecklists` | StepChecklists.batch_restore. Restores StepChecklists with given list of ids |
| StepChecklists.create | `createStepChecklist` | StepChecklists.create. Creates new StepChecklist |
| StepChecklists.delete | `deleteStepChecklist` | StepChecklists.delete. Removes StepChecklist with given id |
| StepChecklists.get | `getStepChecklist` | StepChecklists.get. Returns StepChecklist with given id |
| StepChecklists.list | `listStepChecklists` | StepChecklists.list. Returns all defined StepChecklists |
| StepChecklists.update | `updateStepChecklist` | StepChecklists.update. Modifies StepChecklist or StepChecklists with given id(s) |
| StepChecklistSalesRoleRelations.batch_create_or_update | `batchUpsertStepChecklistSalesRoleRelations` | StepChecklistSalesRoleRelations.batch_create_or_update. Create or update an batch of StepChecklistSalesRoleRelations |
| StepChecklistSalesRoleRelations.batch_delete | `batchDeleteStepChecklistSalesRoleRelations` | StepChecklistSalesRoleRelations.batch_delete. Removes StepChecklistSalesRoleRelations with given list of ids |
| StepChecklistSalesRoleRelations.batch_restore | `batchRestoreStepChecklistSalesRoleRelations` | StepChecklistSalesRoleRelations.batch_restore. Restores StepChecklistSalesRoleRelations with given list of ids |
| StepChecklistSalesRoleRelations.create | `createStepChecklistSalesRoleRelation` | StepChecklistSalesRoleRelations.create. Creates new StepChecklistSalesRoleRelation |
| StepChecklistSalesRoleRelations.delete | `deleteStepChecklistSalesRoleRelation` | StepChecklistSalesRoleRelations.delete. Removes StepChecklistSalesRoleRelation with given id |
| StepChecklistSalesRoleRelations.get | `getStepChecklistSalesRoleRelation` | StepChecklistSalesRoleRelations.get. Returns StepChecklistSalesRoleRelation with given id |
| StepChecklistSalesRoleRelations.list | `listStepChecklistSalesRoleRelations` | StepChecklistSalesRoleRelations.list. Returns all defined StepChecklistSalesRoleRelations |
| StepChecklistSalesRoleRelations.update | `updateStepChecklistSalesRoleRelation` | StepChecklistSalesRoleRelations.update. Modifies StepChecklistSalesRoleRelation or StepChecklistSalesRoleRelations with given id(s) |
| Steps.batch_create_or_update | `batchUpsertSteps` | Steps.batch_create_or_update. Create or update an batch of Steps |
| Steps.batch_delete | `batchDeleteSteps` | Steps.batch_delete. Removes Steps with given list of ids |
| Steps.batch_restore | `batchRestoreSteps` | Steps.batch_restore. Restores Steps with given list of ids |
| Steps.create | `createStep` | Steps.create. Creates new Step |
| Steps.delete | `deleteStep` | Steps.delete. Removes Step with given id |
| Steps.get | `getStep` | Steps.get. Returns Step with given id |
| Steps.list | `listSteps` | Steps.list. Returns all defined Steps |
| Steps.update | `updateStep` | Steps.update. Modifies Step or Steps with given id(s) |
| TagRelations.batch_create_or_update | `batchUpsertTagRelations` | TagRelations.batch_create_or_update. Create or update an batch of TagRelations |
| TagRelations.batch_delete | `batchDeleteTagRelations` | TagRelations.batch_delete. Removes TagRelations with given list of ids |
| TagRelations.batch_restore | `batchRestoreTagRelations` | TagRelations.batch_restore. Restores TagRelations with given list of ids |
| TagRelations.create | `createTagRelation` | TagRelations.create. Creates new TagRelation |
| TagRelations.delete | `deleteTagRelation` | TagRelations.delete. Removes TagRelation with given id |
| TagRelations.get | `getTagRelation` | TagRelations.get. Returns TagRelation with given id |
| TagRelations.list | `listTagRelations` | TagRelations.list. Returns all defined TagRelations |
| TagRelations.update | `updateTagRelation` | TagRelations.update. Modifies TagRelation or TagRelations with given id(s) |
| Tags.batch_create_or_update | `batchUpsertTags` | Tags.batch_create_or_update. Create or update an batch of Tags |
| Tags.batch_delete | `batchDeleteTags` | Tags.batch_delete. Removes Tags with given list of ids |
| Tags.batch_restore | `batchRestoreTags` | Tags.batch_restore. Restores Tags with given list of ids |
| Tags.create | `createTag` | Tags.create. Creates new Tag |
| Tags.delete | `deleteTag` | Tags.delete. Removes Tag with given id |
| Tags.get | `getTag` | Tags.get. Returns Tag with given id |
| Tags.list | `listTags` | Tags.list. Returns all defined Tags |
| Tags.update | `updateTag` | Tags.update. Modifies Tag or Tags with given id(s) |
| TargetRelations.batch_create_or_update | `batchUpsertTargetRelations` | TargetRelations.batch_create_or_update. Create or update an batch of TargetRelations |
| TargetRelations.batch_delete | `batchDeleteTargetRelations` | TargetRelations.batch_delete. Removes TargetRelations with given list of ids |
| TargetRelations.batch_restore | `batchRestoreTargetRelations` | TargetRelations.batch_restore. Restores TargetRelations with given list of ids |
| TargetRelations.create | `createTargetRelation` | TargetRelations.create. Creates new TargetRelation |
| TargetRelations.delete | `deleteTargetRelation` | TargetRelations.delete. Removes TargetRelation with given id |
| TargetRelations.get | `getTargetRelation` | TargetRelations.get. Returns TargetRelation with given id |
| TargetRelations.list | `listTargetRelations` | TargetRelations.list. Returns all defined TargetRelations |
| TargetRelations.update | `updateTargetRelation` | TargetRelations.update. Modifies TargetRelation or TargetRelations with given id(s) |
| Targets.batch_create_or_update | `batchUpsertTargets` | Targets.batch_create_or_update. Create or update an batch of Targets |
| Targets.batch_delete | `batchDeleteTargets` | Targets.batch_delete. Removes Targets with given list of ids |
| Targets.batch_restore | `batchRestoreTargets` | Targets.batch_restore. Restores Targets with given list of ids |
| Targets.create | `createTarget` | Targets.create. Creates new Target |
| Targets.delete | `deleteTarget` | Targets.delete. Removes Target with given id |
| Targets.get | `getTarget` | Targets.get. Returns Target with given id |
| Targets.list | `listTargets` | Targets.list. Returns all defined Targets |
| Targets.update | `updateTarget` | Targets.update. Modifies Target or Targets with given id(s) |
| TaskRecurrences.batch_create_or_update | `batchUpsertTaskRecurrences` | TaskRecurrences.batch_create_or_update. Create or update an batch of TaskRecurrences |
| TaskRecurrences.batch_delete | `batchDeleteTaskRecurrences` | TaskRecurrences.batch_delete. Removes TaskRecurrences with given list of ids |
| TaskRecurrences.batch_restore | `batchRestoreTaskRecurrences` | TaskRecurrences.batch_restore. Restores TaskRecurrences with given list of ids |
| TaskRecurrences.create | `createTaskRecurrence` | TaskRecurrences.create. Creates new TaskRecurrence |
| TaskRecurrences.delete | `deleteTaskRecurrence` | TaskRecurrences.delete. Removes TaskRecurrence with given id |
| TaskRecurrences.get | `getTaskRecurrence` | TaskRecurrences.get. Returns TaskRecurrence with given id |
| TaskRecurrences.list | `listTaskRecurrences` | TaskRecurrences.list. Returns all defined TaskRecurrences |
| TaskRecurrences.update | `updateTaskRecurrence` | TaskRecurrences.update. Modifies TaskRecurrence or TaskRecurrences with given id(s) |
| TaskReminders.batch_create_or_update | `batchUpsertTaskReminders` | TaskReminders.batch_create_or_update. Create or update an batch of TaskReminders |
| TaskReminders.batch_delete | `batchDeleteTaskReminders` | TaskReminders.batch_delete. Removes TaskReminders with given list of ids |
| TaskReminders.batch_restore | `batchRestoreTaskReminders` | TaskReminders.batch_restore. Restores TaskReminders with given list of ids |
| TaskReminders.create | `createTaskReminder` | TaskReminders.create. Creates new TaskReminder |
| TaskReminders.delete | `deleteTaskReminder` | TaskReminders.delete. Removes TaskReminder with given id |
| TaskReminders.get | `getTaskReminder` | TaskReminders.get. Returns TaskReminder with given id |
| TaskReminders.list | `listTaskReminders` | TaskReminders.list. Returns all defined TaskReminders |
| TaskReminders.update | `updateTaskReminder` | TaskReminders.update. Modifies TaskReminder or TaskReminders with given id(s) |
| Tasks.batch_create_or_update | `batchUpsertTasks` | Tasks.batch_create_or_update. Create or update an batch of Tasks |
| Tasks.batch_delete | `batchDeleteTasks` | Tasks.batch_delete. Removes Tasks with given list of ids |
| Tasks.batch_restore | `batchRestoreTasks` | Tasks.batch_restore. Restores Tasks with given list of ids |
| TaskSharingClientRelations.batch_create_or_update | `batchUpsertTaskSharingClientRelations` | TaskSharingClientRelations.batch_create_or_update. Create or update an batch of TaskSharingClientRelations |
| TaskSharingClientRelations.batch_delete | `batchDeleteTaskSharingClientRelations` | TaskSharingClientRelations.batch_delete. Removes TaskSharingClientRelations with given list of ids |
| TaskSharingClientRelations.batch_restore | `batchRestoreTaskSharingClientRelations` | TaskSharingClientRelations.batch_restore. Restores TaskSharingClientRelations with given list of ids |
| TaskSharingClientRelations.create | `createTaskSharingClientRelation` | TaskSharingClientRelations.create. Creates new TaskSharingClientRelation |
| TaskSharingClientRelations.delete | `deleteTaskSharingClientRelation` | TaskSharingClientRelations.delete. Removes TaskSharingClientRelation with given id |
| TaskSharingClientRelations.get | `getTaskSharingClientRelation` | TaskSharingClientRelations.get. Returns TaskSharingClientRelation with given id |
| TaskSharingClientRelations.list | `listTaskSharingClientRelations` | TaskSharingClientRelations.list. Returns all defined TaskSharingClientRelations |
| TaskSharingClientRelations.update | `updateTaskSharingClientRelation` | TaskSharingClientRelations.update. Modifies TaskSharingClientRelation or TaskSharingClientRelations with given id(s) |
| TaskSharingSalesUnitRelations.batch_create_or_update | `batchUpsertTaskSharingSalesUnitRelations` | TaskSharingSalesUnitRelations.batch_create_or_update. Create or update an batch of TaskSharingSalesUnitRelations |
| TaskSharingSalesUnitRelations.batch_delete | `batchDeleteTaskSharingSalesUnitRelations` | TaskSharingSalesUnitRelations.batch_delete. Removes TaskSharingSalesUnitRelations with given list of ids |
| TaskSharingSalesUnitRelations.batch_restore | `batchRestoreTaskSharingSalesUnitRelations` | TaskSharingSalesUnitRelations.batch_restore. Restores TaskSharingSalesUnitRelations with given list of ids |
| TaskSharingSalesUnitRelations.create | `createTaskSharingSalesUnitRelation` | TaskSharingSalesUnitRelations.create. Creates new TaskSharingSalesUnitRelation |
| TaskSharingSalesUnitRelations.delete | `deleteTaskSharingSalesUnitRelation` | TaskSharingSalesUnitRelations.delete. Removes TaskSharingSalesUnitRelation with given id |
| TaskSharingSalesUnitRelations.get | `getTaskSharingSalesUnitRelation` | TaskSharingSalesUnitRelations.get. Returns TaskSharingSalesUnitRelation with given id |
| TaskSharingSalesUnitRelations.list | `listTaskSharingSalesUnitRelations` | TaskSharingSalesUnitRelations.list. Returns all defined TaskSharingSalesUnitRelations |
| TaskSharingSalesUnitRelations.update | `updateTaskSharingSalesUnitRelation` | TaskSharingSalesUnitRelations.update. Modifies TaskSharingSalesUnitRelation or TaskSharingSalesUnitRelations with given id(s) |
| TaskTypes.batch_create_or_update | `batchUpsertTaskTypes` | TaskTypes.batch_create_or_update. Create or update an batch of TaskTypes |
| TaskTypes.batch_delete | `batchDeleteTaskTypes` | TaskTypes.batch_delete. Removes TaskTypes with given list of ids |
| TaskTypes.batch_restore | `batchRestoreTaskTypes` | TaskTypes.batch_restore. Restores TaskTypes with given list of ids |
| TaskTypes.create | `createTaskType` | TaskTypes.create. Creates new TaskType |
| TaskTypes.delete | `deleteTaskType` | TaskTypes.delete. Removes TaskType with given id |
| TaskTypes.get | `getTaskType` | TaskTypes.get. Returns TaskType with given id |
| TaskTypes.list | `listTaskTypes` | TaskTypes.list. Returns all defined TaskTypes |
| TaskTypes.update | `updateTaskType` | TaskTypes.update. Modifies TaskType or TaskTypes with given id(s) |
| TextMessageConversationRelationses.batch_create_or_update | `batchUpsertTextMessageConversationRelationses` | TextMessageConversationRelationses.batch_create_or_update. Create or update an batch of TextMessageConversationRelationses |
| TextMessageConversationRelationses.batch_delete | `batchDeleteTextMessageConversationRelationses` | TextMessageConversationRelationses.batch_delete. Removes TextMessageConversationRelationses with given list of ids |
| TextMessageConversationRelationses.batch_restore | `batchRestoreTextMessageConversationRelationses` | TextMessageConversationRelationses.batch_restore. Restores TextMessageConversationRelationses with given list of ids |
| TextMessageConversationRelationses.create | `createTextMessageConversationRelationse` | TextMessageConversationRelationses.create. Creates new TextMessageConversationRelations |
| TextMessageConversationRelationses.delete | `deleteTextMessageConversationRelationse` | TextMessageConversationRelationses.delete. Removes TextMessageConversationRelations with given id |
| TextMessageConversationRelationses.get | `getTextMessageConversationRelationse` | TextMessageConversationRelationses.get. Returns TextMessageConversationRelations with given id |
| TextMessageConversationRelationses.list | `listTextMessageConversationRelationses` | TextMessageConversationRelationses.list. Returns all defined TextMessageConversationRelationses |
| TextMessageConversationRelationses.update | `updateTextMessageConversationRelationse` | TextMessageConversationRelationses.update. Modifies TextMessageConversationRelations or TextMessageConversationRelationses with given id(s) |
| TextMessageConversations.batch_create_or_update | `batchUpsertTextMessageConversations` | TextMessageConversations.batch_create_or_update. Create or update an batch of TextMessageConversations |
| TextMessageConversations.batch_delete | `batchDeleteTextMessageConversations` | TextMessageConversations.batch_delete. Removes TextMessageConversations with given list of ids |
| TextMessageConversations.batch_restore | `batchRestoreTextMessageConversations` | TextMessageConversations.batch_restore. Restores TextMessageConversations with given list of ids |
| TextMessageConversations.create | `createTextMessageConversation` | TextMessageConversations.create. Creates new TextMessageConversation |
| TextMessageConversations.delete | `deleteTextMessageConversation` | TextMessageConversations.delete. Removes TextMessageConversation with given id |
| TextMessageConversations.get | `getTextMessageConversation` | TextMessageConversations.get. Returns TextMessageConversation with given id |
| TextMessageConversations.list | `listTextMessageConversations` | TextMessageConversations.list. Returns all defined TextMessageConversations |
| TextMessageConversations.update | `updateTextMessageConversation` | TextMessageConversations.update. Modifies TextMessageConversation or TextMessageConversations with given id(s) |
| TextMessages.batch_create_or_update | `batchUpsertTextMessages` | TextMessages.batch_create_or_update. Create or update an batch of TextMessages |
| TextMessages.batch_delete | `batchDeleteTextMessages` | TextMessages.batch_delete. Removes TextMessages with given list of ids |
| TextMessages.batch_restore | `batchRestoreTextMessages` | TextMessages.batch_restore. Restores TextMessages with given list of ids |
| TextMessages.create | `createTextMessage` | TextMessages.create. Creates new TextMessage |
| TextMessages.delete | `deleteTextMessage` | TextMessages.delete. Removes TextMessage with given id |
| TextMessages.get | `getTextMessage` | TextMessages.get. Returns TextMessage with given id |
| TextMessages.list | `listTextMessages` | TextMessages.list. Returns all defined TextMessages |
| TextMessages.update | `updateTextMessage` | TextMessages.update. Modifies TextMessage or TextMessages with given id(s) |
| Timeframes.get | `getTimeframe` | Timeframes.get. Returns Timeframe with given id |
| Timeframes.list | `listTimeframes` | Timeframes.list. Returns all defined Timeframes |
| Translations.batch_create_or_update | `batchUpsertTranslations` | Translations.batch_create_or_update. Create or update an batch of Translations |
| Translations.batch_delete | `batchDeleteTranslations` | Translations.batch_delete. Removes Translations with given list of ids |
| Translations.batch_restore | `batchRestoreTranslations` | Translations.batch_restore. Restores Translations with given list of ids |
| Translations.create | `createTranslation` | Translations.create. Creates new Translation |
| Translations.delete | `deleteTranslation` | Translations.delete. Removes Translation with given id |
| Translations.get | `getTranslation` | Translations.get. Returns Translation with given id |
| Translations.list | `listTranslations` | Translations.list. Returns all defined Translations |
| Translations.update | `updateTranslation` | Translations.update. Modifies Translation or Translations with given id(s) |
| Types.get | `getType` | Types.get. Returns Type with given id |
| Types.list | `listTypes` | Types.list. Returns all defined Types |
| UnsubscribedPhones.batch_create_or_update | `batchUpsertUnsubscribedPhones` | UnsubscribedPhones.batch_create_or_update. Create or update an batch of UnsubscribedPhones |
| UnsubscribedPhones.batch_delete | `batchDeleteUnsubscribedPhones` | UnsubscribedPhones.batch_delete. Removes UnsubscribedPhones with given list of ids |
| UnsubscribedPhones.batch_restore | `batchRestoreUnsubscribedPhones` | UnsubscribedPhones.batch_restore. Restores UnsubscribedPhones with given list of ids |
| UnsubscribedPhones.create | `createUnsubscribedPhone` | UnsubscribedPhones.create. Creates new UnsubscribedPhone |
| UnsubscribedPhones.delete | `deleteUnsubscribedPhone` | UnsubscribedPhones.delete. Removes UnsubscribedPhone with given id |
| UnsubscribedPhones.get | `getUnsubscribedPhone` | UnsubscribedPhones.get. Returns UnsubscribedPhone with given id |
| UnsubscribedPhones.list | `listUnsubscribedPhones` | UnsubscribedPhones.list. Returns all defined UnsubscribedPhones |
| UnsubscribedPhones.update | `updateUnsubscribedPhone` | UnsubscribedPhones.update. Modifies UnsubscribedPhone or UnsubscribedPhones with given id(s) |
| Update Account | `updateAccount` | Accounts.update. Modifies Account or Accounts with given id(s) |
| Update Account KPI | `updateAccountKPI` | AccountKPIs.update. Modifies AccountKPI or AccountKPIs with given id(s) |
| Update Account Product Pricing | `updateAccountProductPricing` | AccountProductPricings.update. Modifies AccountProductPricing or AccountProductPricings with given id(s) |
| Update Account Relation | `updateAccountRelation` | AccountRelations.update. Modifies AccountRelation or AccountRelations with given id(s) |
| Update Account Relation Label | `updateAccountRelationLabel` | AccountRelationLabels.update. Modifies AccountRelationLabel or AccountRelationLabels with given id(s) |
| Update Account Relation Type | `updateAccountRelationType` | AccountRelationTypes.update. Modifies AccountRelationType or AccountRelationTypes with given id(s) |
| Update Account Role | `updateAccountRole` | AccountRoles.update. Modifies AccountRole or AccountRoles with given id(s) |
| Update Account Sharing Client Relation | `updateAccountSharingClientRelation` | AccountSharingClientRelations.update. Modifies AccountSharingClientRelation or AccountSharingClientRelations with given id(s) |
| Update Account Sharing Sales Unit Relation | `updateAccountSharingSalesUnitRelation` | AccountSharingSalesUnitRelations.update. Modifies AccountSharingSalesUnitRelation or AccountSharingSalesUnitRelations with given id(s) |
| Update Contact | `updateContact` | Contacts.update. Modifies Contact or Contacts with given id(s) |
| Update Custom Field | `updateField` | Fields.update. Modifies Field or Fields with given id(s) |
| Update Lead | `updateLead` | Leads.update. Modifies Lead or Leads with given id(s) |
| Update Opportunity | `updateOpportunity` | Opportunities.update. Modifies Opportunity or Opportunities with given id(s) |
| Update Pipeline | `updatePipeline` | Pipelines.update. Modifies Pipeline or Pipelines with given id(s) |
| Update Product | `updateProduct` | Products.update. Modifies Product or Products with given id(s) |
| Update Quote | `updateQuote` | Quotes.update. Modifies Quote or Quotes with given id(s) |
| Update Task | `updateTask` | Tasks.update. Modifies Task or Tasks with given id(s) |
| Update Webhook | `updateWebhook` | Webhooks.update. Modifies Webhook or Webhooks with given id(s) |
| WebhookEvents.batch_create_or_update | `batchUpsertWebhookEvents` | WebhookEvents.batch_create_or_update. Create or update an batch of WebhookEvents |
| WebhookEvents.batch_delete | `batchDeleteWebhookEvents` | WebhookEvents.batch_delete. Removes WebhookEvents with given list of ids |
| WebhookEvents.batch_restore | `batchRestoreWebhookEvents` | WebhookEvents.batch_restore. Restores WebhookEvents with given list of ids |
| WebhookEvents.create | `createWebhookEvent` | WebhookEvents.create. Creates new WebhookEvent |
| WebhookEvents.delete | `deleteWebhookEvent` | WebhookEvents.delete. Removes WebhookEvent with given id |
| WebhookEvents.get | `getWebhookEvent` | WebhookEvents.get. Returns WebhookEvent with given id |
| WebhookEvents.list | `listWebhookEvents` | WebhookEvents.list. Returns all defined WebhookEvents |
| WebhookEvents.update | `updateWebhookEvent` | WebhookEvents.update. Modifies WebhookEvent or WebhookEvents with given id(s) |
| Webhooks.batch_create_or_update | `batchUpsertWebhooks` | Webhooks.batch_create_or_update. Create or update an batch of Webhooks |
| Webhooks.batch_delete | `batchDeleteWebhooks` | Webhooks.batch_delete. Removes Webhooks with given list of ids |
| Webhooks.batch_restore | `batchRestoreWebhooks` | Webhooks.batch_restore. Restores Webhooks with given list of ids |
| Webresources.batch_create_or_update | `batchUpsertWebresources` | Webresources.batch_create_or_update. Create or update an batch of Webresources |
| Webresources.batch_delete | `batchDeleteWebresources` | Webresources.batch_delete. Removes Webresources with given list of ids |
| Webresources.batch_restore | `batchRestoreWebresources` | Webresources.batch_restore. Restores Webresources with given list of ids |
| Webresources.create | `createWebresource` | Webresources.create. Creates new Webresource |
| Webresources.delete | `deleteWebresource` | Webresources.delete. Removes Webresource with given id |
| Webresources.get | `getWebresource` | Webresources.get. Returns Webresource with given id |
| Webresources.list | `listWebresources` | Webresources.list. Returns all defined Webresources |
| Webresources.update | `updateWebresource` | Webresources.update. Modifies Webresource or Webresources with given id(s) |
