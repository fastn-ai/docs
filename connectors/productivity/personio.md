---
description: "Personio is a European HR platform for SMBs covering people data, time off, attendances, compensation, recruiting, and org structure."
hidden: true
---

# Personio

<img src="../../.gitbook/assets/connectors/lg/personio.png" alt="Personio logo">

Personio is a European HR platform for SMBs covering people data, time off, attendances, compensation, recruiting, and org structure. This connector wraps Personio's v2 Public API (OAuth 2.0 client credentials) plus select v1 endpoints not yet available in v2.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [personio.de](https://personio.de) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `personio` |

## Use it

Add Personio from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.personio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Project Members | `addProjectMembers` | Adds one or more persons as members of a project so they can track time against it. If the project was assigned to all employees, it converts to a members-only project. |
| Create Absence Period | `createAbsencePeriod` | Creates a new absence period for a person against a given absence type. Timestamps are local time without a timezone offset, and skip_approval bypasses any approval workflow the write would otherwise require. |
| Create Attendance Period | `createAttendancePeriod` | Creates a work or break attendance period for a person. Start and end are local date-times without a timezone offset, and skip_approval bypasses any approval workflow the write would otherwise require. |
| Create Compensation | `createCompensation` | Creates a payroll compensation for a person, such as a one-time, recurring, fixed, or hourly compensation type. Requires a credential with both compensations read and write scopes. |
| Create Compensation Type | `createCompensationType` | Creates a new Compensation Type and returns its UUID, which can then be used to create a compensation. Hourly types are not supported through this endpoint; bonuses should use RECURRING or ONE_TIME. |
| Create Employee (v1) | `createEmployeeV1` | Creates a new employee using the legacy v1 Employee endpoint. Status defaults to active or onboarding based on the hire date unless explicitly provided. The created record is also reachable and deletable via the v2 Persons API using the same ID. |
| Create Person | `createPerson` | Creates a new Person resource and an associated Employment resource using the v2 Persons API. |
| Create Project | `createProject` | Creates a time-tracking project that attendance periods can reference. |
| Create Webhook | `createWebhook` | Creates a new webhook subscription that Personio will POST event deliveries to. Requires the personio:webhooks:write scope. If auth_type is TOKEN (the default), a token is required; if CUSTOM, custom_headers is required instead. |
| Delete Absence Period | `deleteAbsencePeriod` | Deletes an absence period by its ID. |
| Delete Attendance Period | `deleteAttendancePeriod` | Deletes an attendance period by its ID. |
| Delete Document | `deleteDocument` | Deletes a document by its ID. |
| Delete Person | `deletePerson` | Permanently deletes a Person resource and its associated Employment resources using the v2 Persons API. |
| Delete Project | `deleteProject` | Deletes a time-tracking project and its sub-projects by ID. Fails with a 422 if the project or any sub-project has attendances. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook configuration by its ID. Requires the personio:webhooks:write scope. |
| Download Document File | `downloadDocumentFile` | Downloads the binary file associated with the given document ID. |
| Get Absence Period | `getAbsencePeriod` | Retrieves a single absence period by its ID. |
| Get Absence Period Breakdowns | `getAbsencePeriodBreakdowns` | Retrieves daily absence period breakdowns for a given absence period ID. |
| Get Absence Type | `getAbsenceType` | Retrieves a single absence type by its ID. |
| Get Application | `getApplication` | Retrieves a single recruiting application by its ID. |
| Get Attendance Period | `getAttendancePeriod` | Retrieves a single attendance period by its ID. |
| Get Candidate | `getCandidate` | Retrieves a single recruiting candidate by their ID. |
| Get Employee (v1) | `getEmployeeV1` | Retrieves a single employee by their numeric employee ID using the legacy v1 Employee endpoint, including whitelisted and custom attributes. |
| Get Employee Absence Balance | `getEmployeeAbsenceBalance` | Retrieves the remaining absence balance per absence type for a specific employee. |
| Get Employee Profile Picture | `getEmployeeProfilePicture` | Downloads the profile picture of an employee at the given pixel width. The Profile Picture attribute must be whitelisted for the API credential, and a 404 is returned if no picture is set. |
| Get Employment | `getEmployment` | Retrieves a single employment resource for a person by employment ID. |
| Get Job | `getJob` | Retrieves a single Job from the job catalog by its ID. |
| Get Job Category | `getJobCategory` | Retrieves a single recruiting job category by its ID. |
| Get Legal Entity | `getLegalEntity` | Retrieves a single legal entity by its ID. |
| Get Org Unit | `getOrgUnit` | Retrieves a single Org Unit by ID, optionally including its ancestor chain. |
| Get Person | `getPerson` | Retrieves a single person by ID using the v2 Persons API. |
| Get Project | `getProject` | Retrieves a single time-tracking project by its ID. |
| Get Recruiting Job | `getRecruitingJob` | Retrieves a single recruiting job (open position) by its ID. |
| Get Report | `getReport` | Retrieves a custom report, including its rows and fields, by its ID. |
| Get Salary Band | `getSalaryBand` | Retrieves a single Salary Band by its ID. |
| Get Webhook | `getWebhook` | Retrieves a webhook configuration by its ID. Requires the personio:webhooks:read scope. |
| Get Webhook Delivery Activity | `getWebhookActivity` | Returns delivery activity for a webhook from the last 30 days. Requires the personio:webhooks:read scope. |
| Get Webhook Events | `getWebhookEvents` | Returns events for a webhook from the last 30 days. Requires the personio:webhooks:read scope. |
| List Absence Periods | `listAbsencePeriods` | Lists absence periods taken by employees, with cursor-based pagination and filtering by person, absence type, or date range. |
| List Absence Types | `listAbsenceTypes` | Lists the absence types configured for the company, such as paid vacation, sick leave, or parental leave. |
| List Allowed Custom Attributes | `listAllowedCustomAttributes` | Lists the custom (dynamic) employee attributes that this API credential is allowed to read or write, keyed by their dynamic attribute ID. |
| List Allowed Employee Attributes | `listAllowedAttributes` | Lists all employee attributes, including custom (dynamic) attributes, that this API credential is allowed to read or write. |
| List Application Stage Transitions | `listApplicationStageTransitions` | Returns a list of application stage transitions for a given application ID, ordered latest first. |
| List Applications | `listApplications` | Returns a list of recruiting applications for an authorized company, sorted by last updated date newest first. |
| List Attendance Periods | `listAttendancePeriods` | Lists attendance periods (work or break time) by given filters, with cursor-based pagination. |
| List Candidates | `listCandidates` | Returns a list of recruiting candidates for an authorized company, sorted by last updated date newest first. |
| List Compensation Types | `listCompensationTypes` | Returns a list of Compensation Types for an authorized company, including one-time and recurring types for salary workers. |
| List Compensations | `listCompensations` | Returns a list of payroll compensations of people for an authorized company, including base salary, hourly, one-time, recurring compensation, and bonuses, for a date range up to one month. |
| List Cost Centers | `listCostCenters` | Returns a list of existing cost centers for an authorized company, with optional filtering by name or ID. |
| List Document Categories | `listDocumentCategories` | Lists all document categories configured for the company, such as Certificates of Employment or Other Documents. |
| List Documents | `listDocuments` | Lists the metadata of documents belonging to a given owner (typically a person ID), optionally filtered by category or creation date. |
| List Employees (v1) | `listEmployeesV1` | Lists all employees in the company using the legacy v1 Employee endpoint, including whitelisted employee attributes and custom attributes. Supports offset-based pagination. |
| List Employments | `listEmployments` | Lists the employments of a given person, most recent employment first. |
| List Job Categories | `listJobCategories` | Returns a list of recruiting job categories for an authorized company. |
| List Jobs | `listJobs` | Returns a list of existing Jobs (the job catalog) for an authorized company, with optional filtering by name or ID. |
| List Legal Entities | `listLegalEntities` | Lists the legal entities for an authorized company, most recently created first, with optional filtering by country or ID. |
| List Org Units | `listOrgUnits` | Returns a paginated list of Org Units, such as departments and teams, for the authenticated company. |
| List Persons | `listPersons` | Lists persons for the authorized company using the v2 Persons API, with cursor-based pagination and filtering by ID, email, name, status, or creation/update date. |
| List Project Members | `listProjectMembers` | Lists all members assigned to a given project. |
| List Projects | `listProjects` | Lists all time-tracking projects that attendance periods can reference, by given filters. |
| List Recruiting Jobs | `listRecruitingJobs` | Returns a list of recruiting jobs (open positions) for an authorized company, sorted by last updated date newest first. |
| List Report Attributes | `listReportAttributes` | Lists the reports company attributes, including attribute type, display, and filtering details. |
| List Reports | `listReports` | Lists the custom reports available for the company, most recently created first. |
| List Salary Bands | `listSalaryBands` | Returns a list of existing Salary Bands for an authorized company, with optional filtering by ID. |
| List Webhooks | `listWebhooks` | Returns a list of webhooks configured for the company. Requires the personio:webhooks:read scope. |
| List Workplaces | `listWorkplaces` | Returns a list of existing workplaces (offices) for an authorized company, with optional filtering by name or ID. |
| Redeliver Webhook Events | `redeliverWebhookEvents` | Redelivers events for a webhook selected by an occurred-at date range. At least one of occurred_at.lte or occurred_at.gte must be provided. Only events from the last 30 days can be redelivered, up to 100 per request. Requires the personio:webhooks:write scope. |
| Remove Project Members | `removeProjectMembers` | Removes a member from a project. If no person ID is provided, all members are removed. |
| Rotate Webhook Signing Secret | `rotateWebhookSigningSecret` | Generates a new active signing secret for a webhook, moving the previous active secret into a 7-day retiring grace window. The new secret value is returned only once. Requires the personio:webhooks:write scope. |
| Send Webhook Ping | `pingWebhook` | Triggers a test event of type ping for a webhook, to verify it is configured correctly and can receive events. Requires the personio:webhooks:write scope. |
| Send Webhook Test Event | `sendWebhookTestEvent` | Triggers a test event with a specific event type and custom payload data for a webhook. The event must already be enabled on the webhook. Requires the personio:webhooks:write scope. |
| Update Absence Period | `updateAbsencePeriod` | Updates an existing absence period, such as its comment or substitute. |
| Update Attendance Period | `updateAttendancePeriod` | Updates fields of an existing attendance period, such as its comment, start, or end time. Fields not supplied keep their current value. |
| Update Document Metadata | `updateDocumentMetadata` | Updates the metadata of a document, such as its category, using the provided document ID. |
| Update Employee (v1) | `updateEmployeeV1` | Updates fields of an existing employee using the legacy v1 Employee endpoint, such as name, position, department, office, hire date, or weekly working hours. The email field cannot be changed. |
| Update Employment | `updateEmployment` | Updates fields of an existing Employment resource, such as position, status, cost centers, or working hours, using the v2 Persons API. Only the fields supplied are changed. |
| Update Person | `updatePerson` | Updates fields of an existing Person resource, such as name, gender, language, or custom attributes, using the v2 Persons API. |
| Update Project | `updateProject` | Updates fields of an existing time-tracking project, such as its name, status, or description. |
| Update Webhook | `updateWebhook` | Updates a webhook configuration, such as its URL, description, status, or enabled events. Requires the personio:webhooks:write scope. |
