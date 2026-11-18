---
description: "Float resource scheduling and capacity planning API (v3)."
hidden: true
---

# Float

Float resource scheduling and capacity planning API (v3). Covers people, roles, departments and accounts, clients, projects, phases, project stages, project tasks, project expenses, rate cards, currencies and project templates, scheduled allocations and milestones, logged time, time off and time off types, public and team holidays, the people and project reports, and the delete log. Authenticates with a Float API key sent as a Bearer token; Float also requires every request to carry a User-Agent header.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [float.com](https://float.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 102 |
| **Events** | 0 |
| **Slug** | `float` |

## Use it

Add Float from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.float.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Allocation | `createAllocation` | Add a new allocation as a task, read-only fields are ignored. Allocations are the scheduled blocks of work Float places on a person's timeline; the API calls them tasks. |
| Create Client | `createClient` | Add a new client. |
| Create Currency | `createCurrency` | Add a new currency. Creates a new currency record for the company. The source_currency is set automatically to the company's base currency and cannot be overridden. Both target_currency and fx_rate are required in the request body. |
| Create Department | `createDepartment` | Add a new department. |
| Create Logged Time Entry | `createLoggedTimeEntry` | Log time for a person. Create a logged time entry for a person. |
| Create Milestone | `createMilestone` | Add a new project milestone. |
| Create Person | `createPerson` | Add a new person. Creating a person does not create an account (can only be done through the UI). Each active person contributes to a billing seat. The role_id is a higher order than job_title, job_title will attempt to match on an existing role.name and create a new role if none exist. Cost rates may be set on a person using the cost_rate field and can include an effective_date field in the format; e.g. 2025-06-10. - If effective_date is omitted when the first cost_rate is added, the date will default to the person's start_date, or fallback to 1970-01-01. - When a further cost_rate is added and the effective_date omitted, the date will default to today. These will be reflected in the person's contracts when expanded in the response. |
| Create Phase | `createPhase` | Add a new phase. |
| Create Project | `createProject` | Add a new project. |
| Create Project Expense | `createProjectExpense` | Create a project expense. Create a new project expense for a project, to view the expenses for a project, use the expand=expenses parameter on the /projects endpoint. |
| Create Project From Template | `createProjectFromTemplate` | Create a project from a template. Creates a new project from a project template. The template's phases, project tasks, milestones, expenses, and team members are copied into the new project, with relative scheduling derived from each item's duration and parent_offset against the request's start_date. Any project-level field included in the request body overrides the corresponding value in the template. Fields not provided fall back to the template's values. Nested entities (phases, project tasks, milestones, expenses, and team members) always come from the template. **Asynchronous behavior:** This endpoint returns 200 immediately with an opaque process ID string once the create job has been accepted. The process ID is not directly useful to API clients. To retrieve the created project, poll GET /projects?project_code={project_code} using the project_code you sent in the request body unti |
| Create Project Stage | `createProjectStage` | Add a new project stage. |
| Create Project Task | `createProjectTask` | Add a new project task. Create project tasks to pre-configure a project before scheduling. **Note:** project tasks may be created automatically through /tasks (allocations) and /logged-time when a new name is used in the request. |
| Create Rate Card | `createRateCard` | Add a new rate card. Creates a new rate card for the company. If currency_code is omitted, it defaults to the company's currency. |
| Create Role | `createRole` | Add a new role. |
| Create Status | `createStatus` | Add a new status. Creating a new status requires a valid status_type_id which can be matched from the UI. |
| Create Team Holiday | `createTeamHoliday` | Create a team holiday that. |
| Create Time Off | `createTimeOff` | Add a new time off, read-only fields are ignored. |
| Create Time Off Type | `createTimeOffType` | Add a new time off type, read-only fields are ignored. |
| Delete Allocation | `deleteAllocation` | Delete an allocation as a task. Allocations are the scheduled blocks of work Float places on a person's timeline; the API calls them tasks. Float returns HTTP 204 with an empty response body on success. |
| Delete Client | `deleteClient` | Delete a client. Float returns HTTP 204 with an empty response body on success. |
| Delete Currency | `deleteCurrency` | Delete a currency. Deletes a currency record. Returns 422 if any projects are assigned this target_currency. Float returns HTTP 204 with an empty response body on success. |
| Delete Department | `deleteDepartment` | Delete a department. Float returns HTTP 204 with an empty response body on success. |
| Delete Logged Time Entry | `deleteLoggedTimeEntry` | Delete an existing logged time entry. Float returns HTTP 204 with an empty response body on success. |
| Delete Milestone | `deleteMilestone` | Delete a milestone. Float returns HTTP 204 with an empty response body on success. |
| Delete Person | `deletePerson` | Delete a person. Deleting a person will delete all their allocations (task_id) and logged time, this is an irreversible action. Float returns HTTP 204 with an empty response body on success. |
| Delete Phase | `deletePhase` | Delete a phase. Deleting a phase will delete all associated allocations (task_id) and logged time, this is an irreversible action. Float returns HTTP 204 with an empty response body on success. |
| Delete Project | `deleteProject` | Delete a project. Deleting a project will delete all associated allocations (task_id) and logged time, as well as any phases and associations, this is an irreversible action. Float returns HTTP 204 with an empty response body on success. |
| Delete Project Expense | `deleteProjectExpense` | Delete a project expense. Float returns HTTP 204 with an empty response body on success. |
| Delete Project Stage | `deleteProjectStage` | Delete a project stage. Deleting a project stage will remove it from the available stages for projects, this is an irreversible action. Float returns HTTP 204 with an empty response body on success. |
| Delete Project Task | `deleteProjectTask` | Delete a project task. Project Tasks may only be deleted if there are zero count associations. To remove associations, filter using the task_meta_id on the respective endpoints (/tasks or /logged-time) to update individually, before retrying this delete operation. Float returns HTTP 204 with an empty response body on success. |
| Delete Rate Card | `deleteRateCard` | Delete a rate card. Deletes a rate card. A rate card cannot be deleted while it is in use by a project or project template. Float returns HTTP 204 with an empty response body on success. |
| Delete Role | `deleteRole` | Delete a role. Float returns HTTP 204 with an empty response body on success. |
| Delete Status | `deleteStatus` | Delete a status. Float returns HTTP 204 with an empty response body on success. |
| Delete Team Holiday | `deleteTeamHoliday` | Delete a team holiday. Float returns HTTP 204 with an empty response body on success. |
| Delete Time Off | `deleteTimeOff` | Delete a time off record. Float returns HTTP 204 with an empty response body on success. |
| Get Account | `getAccount` | Retrieve a single account. |
| Get Allocation | `getAllocation` | Retrieve a single allocation as a task. Returns a single allocation. Allocations are the scheduled blocks of work Float places on a person's timeline; the API calls them tasks. |
| Get Client | `getClient` | Retrieve a single client. Returns a single client. |
| Get Currency | `getCurrency` | Retrieve a single currency. Returns a single currency record by ID. |
| Get Department | `getDepartment` | Retrieve a single department. Returns a single department. |
| Get Logged Time Entry | `getLoggedTimeEntry` | Retrieve a single logged time entry. Returns a single logged time entry. |
| Get Milestone | `getMilestone` | Retrieve a single milestone. Returns a single milestone. |
| Get People Report | `getPeopleReport` | Retrieve report data for a list of people. Returns an array of people with aggregated data alongside person-specific attributes. The **start_date** and **end_date** query parameters are required to set the duration of the report, and the response can be filtered per person. **Note:** Pagination is not available, and request limits are lower for report endpoints. |
| Get Person | `getPerson` | Retrieve a single person. |
| Get Phase | `getPhase` | Retrieve a single phase. |
| Get Project | `getProject` | Retrieve a single project. |
| Get Project Expense | `getProjectExpense` | Retrieve a single project expense. Retrieve details of a single project expense. |
| Get Project Stage | `getProjectStage` | Retrieve a single project stage. |
| Get Project Task | `getProjectTask` | Retrieve a single project task. |
| Get Project Template | `getProjectTemplate` | Retrieve a single project template. Returns a single project template by ID. Project templates are managed in the Float UI. Project templates are reusable project definitions the schedule can be built from. |
| Get Projects Report | `getProjectsReport` | Retrieve report data for a list of projects. Returns an array of projects with aggregated data alongside project-specific attributes. The **start_date** and **end_date** query parameters are required to set the duration of the report, and the response can be filtered per project. **Note:** Pagination is not available, and request limits are lower for report endpoints. |
| Get Public Holiday | `getPublicHoliday` | Retrieve a single public holiday. |
| Get Rate Card | `getRateCard` | Retrieve a single rate card. Returns a single rate card by ID. |
| Get Role | `getRole` | Retrieve a single role. Returns a single role. |
| Get Status | `getStatus` | Retrieve a single status. Returns a single status. |
| Get Team Holiday | `getTeamHoliday` | Retrieve a single team holiday. Returns a single team holiday. |
| Get Time Off | `getTimeOff` | Retrieve a single time off. Returns a single time off. |
| Get Time Off Type | `getTimeOffType` | Retrieve a single time off type. Returns a single time off type. |
| List Accounts | `listAccounts` | List accounts. |
| List Allocations | `listAllocations` | List allocations as tasks. This version of the API references a task object as an allocation. **Note:** repeating allocations will also be returned if repeat_end_date is within the date range specified. Allocations are the scheduled blocks of work Float places on a person's timeline; the API calls them tasks. |
| List Clients | `listClients` | List clients. |
| List Currencies | `listCurrencies` | List currencies. Returns the list of currencies configured for the company. Each record maps the company's source currency to a project target currency and optionally includes exchange rates. |
| List Deleted Allocations | `listDeletedAllocations` | List deleted allocations as tasks. Returns a list of deleted allocations (as task IDs) and timestamps. Records are retained for 72 hours. Operates on an at-least-once delivery guarantee; use the record ID as a deduplication key. The delete log lists records removed from the schedule so an integration can mirror deletions. |
| List Deleted Logged Time | `listDeletedLoggedTime` | List deleted logged time entries. Returns a list of deleted logged time IDs and timestamps. Records are retained for 72 hours. Operates on an at-least-once delivery guarantee; use the record ID as a deduplication key. The delete log lists records removed from the schedule so an integration can mirror deletions. |
| List Deleted Time Off | `listDeletedTimeOff` | List deleted time off entries. Returns a list of deleted time off IDs and timestamps. Records are retained for 72 hours. Operates on an at-least-once delivery guarantee; use the record ID as a deduplication key. The delete log lists records removed from the schedule so an integration can mirror deletions. |
| List Departments | `listDepartments` | List departments. |
| List Logged Time | `listLoggedTime` | List logged time for a project or person. Returns a list of logged time for the specified person or project within the specified date range. |
| List Milestones | `listMilestones` | List project milestones. |
| List People | `listPeople` | List people. Search for all people in your organization. People are a distinct entity from Accounts. People exist on the schedule and will only have a linked account if they are invited to sign in. Each active person contributes to a billing seat. Archived people do not show on the schedule, they also do not contribute towards billing seats. |
| List Phases | `listPhases` | List phases. |
| List Project Expenses | `listProjectExpenses` | List project expenses. Retrieve a list of project expenses. |
| List Project Stages | `listProjectStages` | List project stages. |
| List Project Tasks | `listProjectTasks` | List project tasks. Project tasks are used in Projects and Phases to associate allocations and logged time, e.g. Design, Admin etc A task_name with an empty string is the default for allocations and logged time when a project task has not been selected. They may be set to non-billable if the Project or Phase is billable (otherwise the non-billable status cascades). |
| List Project Templates | `listProjectTemplates` | List project templates. Returns the list of project templates configured for the company. Project templates are managed in the Float UI. Project templates are reusable project definitions the schedule can be built from. |
| List Projects | `listProjects` | List projects. |
| List Public Holidays | `listPublicHolidays` | List public holidays. |
| List Rate Cards | `listRateCards` | List rate cards. Returns the list of rate cards configured for the company. |
| List Roles | `listRoles` | List roles. |
| List Statuses | `listStatuses` | List statuses. An individual Status is determined by a date range for a single person and linked to a status type which can only be defined in Admin Settings area of the UI, the default values are 1 = Home, 2 = Travel, 3 = Custom and 4 = Office. **Note:** repeating statues will also be returned if repeat_end_date is within the date range specified. |
| List Team Holidays | `listTeamHolidays` | List team holidays. |
| List Time Off | `listTimeOff` | List of time off scheduled. |
| List Time Off Types | `listTimeOffTypes` | List of time off types. |
| Merge Project Tasks | `mergeProjectTasks` | Merges project tasks and all associations into a single, new or existing, project task. |
| Update Allocation | `updateAllocation` | Update an allocations details as a task, read-only fields are ignored. Accepts the same fields as the create operation; omitted fields are left unchanged and read-only fields are ignored. Allocations are the scheduled blocks of work Float places on a person's timeline; the API calls them tasks. |
| Update Client | `updateClient` | Update a client's name, read-only fields are ignored. Accepts the same fields as the create operation; omitted fields are left unchanged and read-only fields are ignored. |
| Update Currency | `updateCurrency` | Update a currency, read-only fields are ignored. Updates the exchange rate for an existing currency record. target_currency cannot be changed after create. Set the rate with "fx_rate": 1.39 in the request body. |
| Update Department | `updateDepartment` | Update a department's details, read-only fields are ignored. Accepts the same fields as the create operation; omitted fields are left unchanged and read-only fields are ignored. |
| Update Logged Time Entry | `updateLoggedTimeEntry` | Modify an existing logged time entry. |
| Update Milestone | `updateMilestone` | Update a milestone's details, read-only fields are ignored. Accepts the same fields as the create operation; omitted fields are left unchanged and read-only fields are ignored. |
| Update Person | `updatePerson` | Update a person's details, read-only fields are ignored. Accepts the same fields as the create operation; omitted fields are left unchanged and read-only fields are ignored. If a person is changed to archived (active = 0) then their access to the team is revoked by deleting the account and this can only be re-established through the UI. The role_id is a higher order than job_title, job_title will attempt to match on an existing role.name and create a new role if none exist. Cost rates may be updated on a person using the cost_rate field and Role changes may be updated using the role_id field along with the effective_date field with the format example 2025-06-10 (defaults to today if omitted). These will be reflected in the person's contracts available to be expanded on the response. |
| Update Phase | `updatePhase` | Update a phase's details. Accepts the same fields as the create operation; omitted fields are left unchanged and read-only fields are ignored. To update the phase team including unassigned roles there are 3 actions on the phase_team field; set, add and del: * Use set as an array of phase team objects of people_id, role_id and hourly_rate to replace all people and their phase roles & rates * Use add as an array of phase team objects of people_id, role_id and hourly_rate to add additional people and their roles & rates * Use del as an array of people_id to remove people from the phase_team To assign a role to a phase, set or add a role_id to the phase_team object without a people_id. An unassigned role placeholder will be returned in the response. See the Using unassigned roles tutorial for more details. CAUTION: set and del actions that remove people will cascade delete all associated All |
| Update Project | `updateProject` | Update a project's details, read-only fields are ignored. Accepts the same fields as the create operation; omitted fields are left unchanged and read-only fields are ignored. To update the project team including unassigned roles there are 3 actions on the project_team field; set, add and del: * Use set as an array of project team objects of people_id,role_id and hourly_rate to replace all people and their project rates * Use add as an array of project team objects of people_id, role_id and hourly_rate to add additional people and their roles & rates * Use del as an array of people_id to remove people from the project_team To assign a role to a project, set or add a role_id to the project_team object without a people_id. An unassigned role placeholder will be returned in the response. See the Using unassigned roles tutorial for more details. CAUTION: set and del actions that remove people |
| Update Project Expense | `updateProjectExpense` | Update a project expense. Update an existing project expense. |
| Update Project Stage | `updateProjectStage` | Update a project stage's details, read-only fields are ignored. Stages may be updated or archived, project_status cannot be changed. |
| Update Project Task | `updateProjectTask` | Update a project tasks details. |
| Update Rate Card | `updateRateCard` | Update a rate card, read-only fields are ignored. Updates a rate card. roles and client_ids, when included, replace the full existing set rather than merging with it. The currency_code cannot be changed once a project is using this rate card. |
| Update Role | `updateRole` | Update a role, read-only fields are ignored.. Accepts the same fields as the create operation; omitted fields are left unchanged and read-only fields are ignored. To update cost_rate_history see Role cost rate changes. |
| Update Status | `updateStatus` | Update a status's details, read-only fields are ignored. Accepts the same fields as the create operation; omitted fields are left unchanged and read-only fields are ignored. |
| Update Team Holiday | `updateTeamHoliday` | Update a holiday's details, read-only fields are ignored. Accepts the same fields as the create operation; omitted fields are left unchanged and read-only fields are ignored. |
| Update Time Off | `updateTimeOff` | Update a time off's details, read-only fields are ignored. Accepts the same fields as the create operation; omitted fields are left unchanged and read-only fields are ignored. |
| Update Time Off Type | `updateTimeOffType` | Update a time off type's details, read-only fields are ignored. Accepts the same fields as the create operation; omitted fields are left unchanged and read-only fields are ignored. |
