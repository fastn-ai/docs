---
description: "Beebole is a time-tracking, project-costing, absence and resource-planning platform for teams."
hidden: true
---

# Beebole

<img src="../../.gitbook/assets/connectors/lg/beebole.png" alt="Beebole logo">

Beebole is a time-tracking, project-costing, absence and resource-planning platform for teams. This connector wraps Beebole's single GraphQL endpoint (POST https://app.beebole.com/graphql), exposing its people, roles, projects, tasks, tags, time records, expense records, absence types, schedule types, custom fields, approvals, budgets, reports, holidays, journal messages and integration-webhook operations as individual actions.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [beebole.com](https://beebole.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `beebole` |

## Use it

Add Beebole from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.beebole.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Integration Webhook | `addIntegrationWebhook` | Registers a new outgoing integration webhook on the organisation. Beebole sends a signed POST to the given URL whenever one of the subscribed events occurs, and auto-generates a 36-character signing secret. WARNING: the response includes every webhook's signing secret. Note Beebole does NOT validate event names - an unrecognised name is stored silently and simply never fires. |
| Add Person | `addPerson` | Creates a new person in the organisation with the given name, unique email and authorisation role. The person is created but not invited - use the Beebole UI or the invite flow to send them an invitation. Confirm creation with a follow-up Get Persons call. |
| Add Project | `addProject` | Creates a project, or a sub-project when parentId is given. The category is inferred from the parent if omitted. Confirm creation with a follow-up Get Projects call. |
| Add Time Record | `addTimeRecord` | Logs a time entry for a person. Provide either taskId plus projectIds for worked time, or absenceId for leave. startTime is the Unix millisecond timestamp of the day and duration is in milliseconds (one hour = 3600000). Confirm with a follow-up Get Time Records call over the same window. |
| Count Persons | `countPersons` | Returns the number of people matching the given filter conditions, without fetching the rows. Use it for pagination totals or seat counts. Omit the filter to count all active people. |
| Delete Integration Webhook | `deleteIntegrationWebhook` | Permanently removes an integration webhook by id. The returned top-level id is the ORGANISATION id, not the deleted webhook id, and the returned webhook list still shows the pre-delete state - confirm removal with a follow-up Get Current Organisation call. |
| Delete Person | `deletePerson` | Permanently deletes a person and their references. DESTRUCTIVE AND IRREVERSIBLE - pass check:true first to report what would be affected without deleting anything. Never call this on the person your API key authenticates as, or on the organisation's only administrator: doing so can lock the account out permanently. Prefer Archive Person for people who have left. |
| Delete Project | `deleteProject` | Permanently deletes a project and its sub-projects. DESTRUCTIVE AND IRREVERSIBLE - pass check:true first to report which time records, budgets and assignments reference it without deleting anything. Prefer Archive Project for projects that have simply finished. |
| Delete Time Records | `deleteTimeRecords` | Deletes one or more logged time entries by id. DESTRUCTIVE AND IRREVERSIBLE - only delete entries you created, and confirm removal with a follow-up Get Time Records call over the same window. Entries inside an approved or locked period may be refused. |
| Edit Integration Webhook Active | `editIntegrationWebhookActive` | Enables or disables an existing integration webhook without deleting it. A disabled webhook keeps its id, URL, secret and event list but receives no deliveries. Beebole returns the PRE-change state here; confirm with a follow-up Get Current Organisation call. |
| Edit Integration Webhook Events | `editIntegrationWebhookEvents` | Replaces the event subscription list of an existing integration webhook. Use ["*"] for all events. WARNING: Beebole does NOT validate event names - an unrecognised name is accepted, persisted, and simply never fires, so use only the names in the enum. Beebole also returns the PRE-change state here; confirm with a follow-up Get Current Organisation call. |
| Edit Integration Webhook Name | `editIntegrationWebhookName` | Renames an existing integration webhook. IMPORTANT: Beebole returns the PRE-change state in this mutation's own response, so confirm the new name with a follow-up Get Current Organisation call. The response also carries every webhook's signing secret. |
| Edit Integration Webhook URL | `editIntegrationWebhookUrl` | Changes the delivery URL of an existing integration webhook. IMPORTANT: Beebole returns the PRE-change state in this mutation's own response, so confirm the new URL with a follow-up Get Current Organisation call. |
| Get Absence Types | `getAbsenceTypes` | Lists the absence types configured for the organisation (for example PTO, Sickness) with their unit (day or hour), cost involvement, accrual configuration and colour. |
| Get API Keys | `getApiKeys` | SECURITY WARNING: this endpoint returns the organisation's Beebole API keys IN CLEAR TEXT, along with each key's expiry and revoked flag. Anyone who can run this action, or read its stored execution record, obtains live credentials for the whole organisation. Grant it only to trusted callers, and never log or persist its response. |
| Get Audit Trails | `getAuditTrails` | Returns the organisation's audit log: which person performed which GraphQL operation, when, and with what arguments. Narrow by start time, acting person, affected person, or a list of operation names. |
| Get Current Organisation | `currentOrganisation` | Returns the Beebole organisation the API key belongs to: name, colour, subscription plan and seat count, SSO configuration, feature availability, onboarding state, any scheduled deletion, and the list of registered integration webhooks. SECURITY: the webhooks block includes each webhook's signing secret. |
| Get Current Person | `currentPerson` | Returns the Beebole person that the API key authenticates as, including name, email, language, colour, start date, role and organisation. Use it to identify the connected account. |
| Get Custom Fields | `getCustomFields` | Lists the custom fields defined for the organisation with their data type (text, number, date, datetime, url, boolean), validation options and which entities they are visible on. |
| Get Expense Records | `getExpenseRecords` | Lists logged expense records in a date window with the person, project, expense type, amount, currency and comment. Bound with startTime/endTime in Unix milliseconds. |
| Get Expense Types | `getExpenseTypes` | Lists the expense types configured for the organisation (for example Hotel, Taxi, Mileage) with whether each is a currency amount or a quantity, its markup percentage and whether it counts against project budgets. |
| Get Holiday Country Codes | `getHolidayCountryCodes` | Lists the country (and region) codes for which Beebole can supply a public-holiday calendar. Use the returned code with Get Holidays. |
| Get Holidays | `getHolidays` | Returns the public-holiday calendar for a country or region code, optionally localised. Use it to populate an organisation's, tag's or person's public-holiday list. |
| Get Pending Approvals | `getPendingApprovals` | Lists timesheets waiting for the connected person's approval, with the submitting person and the period covered. Set showAll to include approvals assigned to other approvers. |
| Get Person | `getPerson` | Fetches a single person by Beebole person id, with role, organisation, email, language, colour, description, start date and invitation state. |
| Get Persons | `getPersons` | Lists people in the organisation with their role, email, language, colour, start date and owned tasks. Supports Beebole's filter-condition array (by id, role, name regex, tags, schedule type) and an archived flag. Omit both to list all active people. |
| Get Project | `getProject` | Fetches a single project or sub-project by id, with its category, parent, hierarchy level, colour, description and archived state. Beebole's BeeboleProject type exposes the parent but not a children list; use Get Projects with a parentId filter to list children. |
| Get Projects | `getProjects` | Lists projects and sub-projects with their category, hierarchy level, parent, colour, description and archived state. Filter by category, by the filter-condition array, or by archived status. |
| Get Reports | `getReports` | Lists the saved reports in the organisation with their folder, record scope, period, grouping and chart configuration, plus any email-delivery schedule. Use the returned id with Run Report. |
| Get Roles | `getRoles` | Lists the authorisation roles defined in the organisation (for example Admin, Employee, People manager, Project manager) with each role's permission matrix and the people assigned to it. |
| Get Schedule Types | `getScheduleTypes` | Lists the working-schedule templates defined for the organisation (for example Full Time, Half Time) with each day's working duration, time pairs and work-from-home flag. |
| Get Tags | `getTags` | Lists tags (Beebole's grouping dimension, for example departments, offices or clients) with their category, parent, colour and description. Tags also carry their own time, localisation and approval settings. |
| Get Tasks | `getTasks` | Lists planning tasks with their category, kanban status, start and end time, effort, recurrence, dependencies and hierarchy. Bound the result with startTime/endTime (Unix milliseconds) to fetch a planning window. |
| Get Time Records | `getTimeRecords` | Lists logged time entries (and absences) in a date window, with person, project chain, task, absence type, duration in hours, comment, billable flag and work-from-home flag. Bound with startTime/endTime in Unix milliseconds; the time, absence and wfh booleans select which kinds of record to include. |
| Regenerate Integration Webhook Secret | `regenerateIntegrationWebhookSecret` | Rotates the signing secret of an existing integration webhook. Deliveries signed with the previous secret stop verifying immediately, so update the receiving endpoint first. SECURITY: the response contains every webhook's signing secret in clear text. |
| Run Report | `runReport` | Executes a saved report by id and returns its computed result matrix, optionally overriding the report's period and filters. Use Get Reports to find the id. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Absence quota changed | `absenceQuotaUpdate` | An absence quota was created, edited or deleted. |
| Absence type changed | `absenceTypeUpdate` | An absence type was created, edited, archived or deleted. |
| Approval event | `approvalEventUpdate` | A timesheet was submitted, approved, rejected or reopened. |
| Billing rate changed | `billingUpdate` | A billing or cost rate was created, edited or deleted. |
| Budget changed | `budgetUpdate` | A project or task budget was created, edited or deleted. |
| Category changed | `categoryUpdate` | A category of any kind was created, edited or deleted. |
| Custom field changed | `customFieldUpdate` | A custom field definition was created, edited, archived or deleted. |
| Custom field value changed | `customFieldValueUpdate` | A custom field value on an entity was set, changed or cleared. |
| Expense record changed | `expenseRecordUpdate` | An expense record was created, edited or deleted. |
| Expense type changed | `expenseTypeUpdate` | An expense type was created, edited, archived or deleted. |
| Organisation changed | `organisationUpdate` | Organisation settings, localisation, availability or integrations changed. |
| Person changed | `personUpdate` | A person was created, edited, archived or deleted. |
| Planning changed | `planningUpdate` | The resource planning (task assignment or scheduling) changed. |
| Project category changed | `projectCategoryUpdate` | A project category was created, edited or deleted. |
| Project changed | `projectUpdate` | A project or sub-project was created, edited, archived or deleted. |
| Role changed | `roleUpdate` | An authorisation role was created, edited or deleted. |
| Schedule type changed | `scheduleTypeUpdate` | A working-schedule template was created, edited, archived or deleted. |
| Tag category changed | `tagCategoryUpdate` | A tag category was created, edited or deleted. |
| Tag changed | `tagUpdate` | A tag was created, edited, archived or deleted. |
| Task category changed | `taskCategoryUpdate` | A task category or one of its kanban statuses was created, edited or deleted. |
| Task changed | `taskUpdate` | A planning task was created, edited, moved, archived or deleted. |
| Task settings changed | `taskSettingsUpdate` | Task-related settings on the organisation, a tag, a project or a person changed. |
| Time record changed | `timeRecordUpdate` | A time entry or absence record was created, edited or deleted. |
