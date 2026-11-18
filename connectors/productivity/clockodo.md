---
description: "Clockodo time tracking, absence management and project reporting."
hidden: true
---

# Clockodo

<img src="../../.gitbook/assets/connectors/clockodo.png" alt="Clockodo logo" width="64">

Clockodo time tracking, absence management and project reporting. Wraps the Clockodo REST API at https://my.clockodo.com/api (per-resource versioning: v2, v3 and v4 paths coexist).

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [clockodo.com](https://clockodo.com) |
| **Authentication** | API key |
| **Slug** | `clockodo` |

## Use it

Add Clockodo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.clockodo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Approve Work Times Change Request | `approveWorkTimesChangeRequest` | Approve Work Times Change Request (POST /api/v3/workTimes/changeRequests/{id}/approve). Manage work times. Work times cannot be edited directly. To edit work times, edit the respective time entries or use requests for change of work time. Docs: https://docs.clockodo.com/#tag/WorkTime/operation/approveWorkTimesChangeRequestByIdV3 |
| Clear Individual User Access | `clearIndividualUserAccess` | Clear Individual User Access (POST /api/v2/individualUserAccess/{usersId}/clear). Manage individual user rights. Docs: https://docs.clockodo.com/#tag/IndividualUserAccess/operation/clearIndividualUserAccessByIdV2 |
| Complete Project | `completeProject` | Complete Project (PUT /api/v4/projects/{id}/complete). Manage projects. Docs: https://docs.clockodo.com/#tag/Project/operation/completeProjectByIdV4 |
| Complete Subproject | `completeSubproject` | Complete Subproject (PUT /api/v3/subprojects/{id}/complete). Manage subprojects. Docs: https://docs.clockodo.com/#tag/Subproject/operation/completeSubprojectByIdV3 |
| Count Projects Per Customer | `countProjectsPerCustomer` | Count Projects Per Customer (GET /api/v3/customers/countProjects). Manage customers. Docs: https://docs.clockodo.com/#tag/Customer/operation/getCustomersCountProjectsV3 |
| Create Absence | `createAbsence` | Create Absence (POST /api/v4/absences). Manage absences (holidays, sick days, etc.). Docs: https://docs.clockodo.com/#tag/Absence/operation/createAbsenceV4 |
| Create Access Group | `createAccessGroup` | Create Access Group (POST /api/v2/accessGroups). Manage access groups names and assigned users. Docs: https://docs.clockodo.com/#tag/AccessGroup/operation/createAccessGroupV2 |
| Create Clock | `createClock` | Create Clock (POST /api/v2/clock). Control the clock. Docs: https://docs.clockodo.com/#tag/Clock/operation/createClockV2 |
| Create Customer | `createCustomer` | Create Customer (POST /api/v3/customers). Manage customers. Docs: https://docs.clockodo.com/#tag/Customer/operation/createCustomerV3 |
| Create Entry | `createEntry` | Create Entry (POST /api/v2/entries). Manage time and lump sum entries. If the project has subprojects, subprojects_id is required. Docs: https://docs.clockodo.com/#tag/Entry/operation/createEntryV2 |

<details>

<summary>See 139 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Favorite | `createFavorite` | Create Favorite (POST /api/v2/favorites). Manage favorites. Docs: https://docs.clockodo.com/#tag/Favorite/operation/createFavoriteV2 |
| Create Holiday Carryover | `createHolidayCarryover` | Create Holiday Carryover (POST /api/v3/holidaysCarry). Manage holiday carryovers. Docs: https://docs.clockodo.com/#tag/HolidayCarryover/operation/createHolidayCarryoverV3 |
| Create Holiday Quota | `createHolidayQuota` | Create Holiday Quota (POST /api/v2/holidaysQuota). Manage holiday quotas. Docs: https://docs.clockodo.com/#tag/HolidayQuota/operation/createHolidayQuotaV2 |
| Create Lump Sum Service | `createLumpSumService` | Create Lump Sum Service (POST /api/v4/lumpSumServices). Manage lump sum services. Docs: https://docs.clockodo.com/#tag/LumpSumService/operation/createLumpSumServiceV4 |
| Create Next Project Interval | `createNextProjectInterval` | Create Next Project Interval (POST /api/v2/projects/{id}/createNextInterval). Manage projects. Only for retainer projects (project budget with an interval). Docs: https://docs.clockodo.com/#tag/Project/operation/createProjectNextIntervalByIdV2 |
| Create Nonbusiness Day | `createNonbusinessDay` | Create Nonbusiness Day (POST /api/v2/nonbusinessDays). Query and manage nonbusiness days. Docs: https://docs.clockodo.com/#tag/NonbusinessDay/operation/createNonbusinessDayV2 |
| Create Nonbusiness Group | `createNonbusinessGroup` | Create Nonbusiness Group (POST /api/v2/nonbusinessGroups). Query and manage nonbusiness groups. Docs: https://docs.clockodo.com/#tag/NonbusinessGroup/operation/createNonbusinessGroupV2 |
| Create Overtime Carry | `createOvertimeCarry` | Create Overtime Carry (POST /api/v3/overtimeCarry). Manage overtime carryovers. Docs: https://docs.clockodo.com/#tag/OvertimeCarry/operation/createOvertimeCarryV3 |
| Create Overtime Reduction | `createOvertimeReduction` | Create Overtime Reduction (POST /api/v3/overtimeReductions). Manage overtime reductions. Docs: https://docs.clockodo.com/#tag/OvertimeReduction/operation/createOvertimeReductionV3 |
| Create Project | `createProject` | Create Project (POST /api/v4/projects). Manage projects. Docs: https://docs.clockodo.com/#tag/Project/operation/createProjectV4 |
| Create Rate | `createRate` | Create Rate (POST /api/v4/rates). Manage rates. Docs: https://docs.clockodo.com/#tag/Rate/operation/createRateV4 |
| Create Register | `createRegister` | Create Register (POST /api/register). Create Clockodo accounts. Creates a NEW Clockodo company account (signup). Use with care. Docs: https://docs.clockodo.com/#tag/Register/operation/createRegister |
| Create Service | `createService` | Create Service (POST /api/v4/services). Manage services. Docs: https://docs.clockodo.com/#tag/Service/operation/createServiceV4 |
| Create Subproject | `createSubproject` | Create Subproject (POST /api/v3/subprojects). Manage subprojects. Docs: https://docs.clockodo.com/#tag/Subproject/operation/createSubprojectV3 |
| Create Target Hour | `createTargetHour` | Create Target Hour (POST /api/targethours). Manage target hours (planned hours). Docs: https://docs.clockodo.com/#tag/TargetHour/operation/createTargetHour |
| Create Team | `createTeam` | Create Team (POST /api/v3/teams). Manage teams. Docs: https://docs.clockodo.com/#tag/Team/operation/createTeamV3 |
| Create User | `createUser` | Create User (POST /api/v3/users). Manage co-workers. Docs: https://docs.clockodo.com/#tag/User/operation/createUserV3 |
| Create Users Nonbusiness Group | `createUsersNonbusinessGroup` | Create Users Nonbusiness Group (POST /api/v3/usersNonbusinessGroups). Assign non-business day groups to users and manage time periods. Docs: https://docs.clockodo.com/#tag/UserNonbusinessGroup/operation/createUsersNonbusinessGroupV3 |
| Create Webhook Subscription | `createWebhookSubscription` | Registers a webhook subscription so Clockodo posts events to the given URL. The route is live but undocumented, and its request body could not be confirmed on this account because every write is blocked by the account approval gate - the field names below are modelled from the delivered webhook payload schema and must be re-verified against a live 201. |
| Create Work Times Change Request | `createWorkTimesChangeRequest` | Create Work Times Change Request (POST /api/v2/workTimes/changeRequests). Manage work times. Work times cannot be edited directly. To edit work times, edit the respective time entries or use requests for change of work time. Clockodo rejects intervals that do not fit the day's entries (400 'Work times must match the day's entries'). Docs: https://docs.clockodo.com/#tag/WorkTime/operation/createWorkTimesChangeRequestV2 |
| Delete Absence | `deleteAbsence` | Delete Absence (DELETE /api/v4/absences/{id}). Manage absences (holidays, sick days, etc.). The absence must be declined or its approval cancelled first (updateAbsence status 2 or 3), else 422 AbsenceHasToBeDeclined. Docs: https://docs.clockodo.com/#tag/Absence/operation/deleteAbsenceByIdV4 |
| Delete Access Group | `deleteAccessGroup` | Delete Access Group (DELETE /api/v2/accessGroups/{id}). Manage access groups names and assigned users. Docs: https://docs.clockodo.com/#tag/AccessGroup/operation/deleteAccessGroupByIdV2 |
| Delete Clock | `deleteClock` | Delete Clock (DELETE /api/v2/clock/{id}). Control the clock. Docs: https://docs.clockodo.com/#tag/Clock/operation/deleteClockByIdV2 |
| Delete Customer | `deleteCustomer` | Delete Customer (DELETE /api/v3/customers/{id}). Manage customers. Set the customer inactive first (active=false). Docs: https://docs.clockodo.com/#tag/Customer/operation/deleteCustomerByIdV3 |
| Delete Entry | `deleteEntry` | Delete Entry (DELETE /api/v2/entries/{id}). Manage time and lump sum entries. Docs: https://docs.clockodo.com/#tag/Entry/operation/deleteEntryByIdV2 |
| Delete Entry Groups | `deleteEntryGroups` | Delete Entry Groups (DELETE /api/v2/entrygroups). Query and manage groups of time entries (particularly useful for evaluation and invoicing purposes). Two-step: the first call returns confirm_key and affected_entries; repeat with confirm_key to delete. Docs: https://docs.clockodo.com/#tag/EntryGroup/operation/deleteEntryGroupsV2 |
| Delete Favorite | `deleteFavorite` | Delete Favorite (DELETE /api/v2/favorites/{id}). Manage favorites. Docs: https://docs.clockodo.com/#tag/Favorite/operation/deleteFavoriteByIdV2 |
| Delete Holiday Carryover | `deleteHolidayCarryover` | Delete Holiday Carryover (DELETE /api/v3/holidaysCarry/{id}). Manage holiday carryovers. Docs: https://docs.clockodo.com/#tag/HolidayCarryover/operation/deleteHolidayCarryoverByIdV3 |
| Delete Holiday Quota | `deleteHolidayQuota` | Delete Holiday Quota (DELETE /api/v2/holidaysQuota/{id}). Manage holiday quotas. Docs: https://docs.clockodo.com/#tag/HolidayQuota/operation/deleteHolidayQuotaByIdV2 |
| Delete Lump Sum Service | `deleteLumpSumService` | Delete Lump Sum Service (DELETE /api/v4/lumpSumServices/{id}). Manage lump sum services. Set the lump sum service inactive first (active=false). Docs: https://docs.clockodo.com/#tag/LumpSumService/operation/deleteLumpSumServiceByIdV4 |
| Delete Nonbusiness Day | `deleteNonbusinessDay` | Delete Nonbusiness Day (DELETE /api/v2/nonbusinessDays/{id}). Query and manage nonbusiness days. Docs: https://docs.clockodo.com/#tag/NonbusinessDay/operation/deleteNonbusinessDayByIdV2 |
| Delete Nonbusiness Group | `deleteNonbusinessGroup` | Delete Nonbusiness Group (DELETE /api/v2/nonbusinessGroups/{id}). Query and manage nonbusiness groups. Docs: https://docs.clockodo.com/#tag/NonbusinessGroup/operation/deleteNonbusinessGroupByIdV2 |
| Delete Overtime Carry | `deleteOvertimeCarry` | Delete Overtime Carry (DELETE /api/v3/overtimeCarry/{id}). Manage overtime carryovers. Docs: https://docs.clockodo.com/#tag/OvertimeCarry/operation/deleteOvertimeCarryByIdV3 |
| Delete Overtime Reduction | `deleteOvertimeReduction` | Delete Overtime Reduction (DELETE /api/v3/overtimeReductions/{id}). Manage overtime reductions. Docs: https://docs.clockodo.com/#tag/OvertimeReduction/operation/deleteOvertimeReductionByIdV3 |
| Delete Project | `deleteProject` | Delete Project (DELETE /api/v4/projects/{id}). Manage projects. Set the project inactive first (active=false). Docs: https://docs.clockodo.com/#tag/Project/operation/deleteProjectByIdV4 |
| Delete Rate | `deleteRate` | Delete Rate (DELETE /api/v4/rates/{id}). Manage rates. Docs: https://docs.clockodo.com/#tag/Rate/operation/deleteRateByIdV4 |
| Delete Service | `deleteService` | Delete Service (DELETE /api/v4/services/{id}). Manage services. The service must be set inactive first (updateService active=false), else 422 HasToBeInactive. Docs: https://docs.clockodo.com/#tag/Service/operation/deleteServiceByIdV4 |
| Delete Subproject | `deleteSubproject` | Delete Subproject (DELETE /api/v3/subprojects/{id}). Manage subprojects. Docs: https://docs.clockodo.com/#tag/Subproject/operation/deleteSubprojectByIdV3 |
| Delete Target Hour | `deleteTargetHour` | Delete Target Hour (DELETE /api/targethours/{id}). Manage target hours (planned hours). Docs: https://docs.clockodo.com/#tag/TargetHour/operation/deleteTargetHourById |
| Delete Team | `deleteTeam` | Delete Team (DELETE /api/v3/teams/{id}). Manage teams. Docs: https://docs.clockodo.com/#tag/Team/operation/deleteTeamByIdV3 |
| Delete User | `deleteUser` | Delete User (DELETE /api/v3/users/{id}). Manage co-workers. Docs: https://docs.clockodo.com/#tag/User/operation/deleteUserByIdV3 |
| Delete Users Nonbusiness Group | `deleteUsersNonbusinessGroup` | Delete Users Nonbusiness Group (DELETE /api/v3/usersNonbusinessGroups/{id}). Assign non-business day groups to users and manage time periods. Docs: https://docs.clockodo.com/#tag/UserNonbusinessGroup/operation/deleteUsersNonbusinessGroupByIdV3 |
| Delete Webhook Subscription | `deleteWebhookSubscription` | Removes a Clockodo webhook subscription by its numeric id so deliveries stop. Route is live but undocumented. |
| Delete Work Times Change Request | `deleteWorkTimesChangeRequest` | Delete Work Times Change Request (DELETE /api/v2/workTimes/changeRequests/{id}). Manage work times. Work times cannot be edited directly. To edit work times, edit the respective time entries or use requests for change of work time. Docs: https://docs.clockodo.com/#tag/WorkTime/operation/deleteWorkTimesChangeRequestByIdV2 |
| Get Absence | `getAbsence` | Get Absence (GET /api/v4/absences/{id}). Manage absences (holidays, sick days, etc.). Docs: https://docs.clockodo.com/#tag/Absence/operation/getAbsenceByIdV4 |
| Get Access Group | `getAccessGroup` | Get Access Group (GET /api/v2/accessGroups/{id}). Manage access groups names and assigned users. Docs: https://docs.clockodo.com/#tag/AccessGroup/operation/getAccessGroupByIdV2 |
| Get Company Subscription | `getSubscription` | Get Company Subscription (GET /api/v2/subscription). Get subscription info. Docs: https://docs.clockodo.com/#tag/Subscription/operation/getSubscriptionV2 |
| Get Current User | `getCurrentUser` | Get Current User (GET /api/v4/users/me). Manage co-workers. Docs: https://docs.clockodo.com/#tag/User/operation/getUsersMeV4 |
| Get Customer | `getCustomer` | Get Customer (GET /api/v3/customers/{id}). Manage customers. Docs: https://docs.clockodo.com/#tag/Customer/operation/getCustomerByIdV3 |
| Get Entry | `getEntry` | Get Entry (GET /api/v2/entries/{id}). Manage time and lump sum entries. Docs: https://docs.clockodo.com/#tag/Entry/operation/getEntryByIdV2 |
| Get Favorite | `getFavorite` | Get Favorite (GET /api/v2/favorites/{id}). Manage favorites. Docs: https://docs.clockodo.com/#tag/Favorite/operation/getFavoriteByIdV2 |
| Get Holiday Carryover | `getHolidayCarryover` | Get Holiday Carryover (GET /api/v3/holidaysCarry/{id}). Manage holiday carryovers. Docs: https://docs.clockodo.com/#tag/HolidayCarryover/operation/getHolidayCarryoverByIdV3 |
| Get Holiday Quota | `getHolidayQuota` | Get Holiday Quota (GET /api/v2/holidaysQuota/{id}). Manage holiday quotas. Docs: https://docs.clockodo.com/#tag/HolidayQuota/operation/getHolidayQuotaByIdV2 |
| Get Lump Sum Service | `getLumpSumService` | Get Lump Sum Service (GET /api/v4/lumpSumServices/{id}). Manage lump sum services. Docs: https://docs.clockodo.com/#tag/LumpSumService/operation/getLumpSumServiceByIdV4 |
| Get Nonbusiness Day | `getNonbusinessDay` | Get Nonbusiness Day (GET /api/v2/nonbusinessDays/{id}). Query and manage nonbusiness days. Docs: https://docs.clockodo.com/#tag/NonbusinessDay/operation/getNonbusinessDayByIdV2 |
| Get Nonbusiness Group | `getNonbusinessGroup` | Get Nonbusiness Group (GET /api/v2/nonbusinessGroups/{id}). Query and manage nonbusiness groups. Docs: https://docs.clockodo.com/#tag/NonbusinessGroup/operation/getNonbusinessGroupByIdV2 |
| Get Overtime Carry | `getOvertimeCarry` | Get Overtime Carry (GET /api/v3/overtimeCarry/{id}). Manage overtime carryovers. Docs: https://docs.clockodo.com/#tag/OvertimeCarry/operation/getOvertimeCarryByIdV3 |
| Get Overtime Reduction | `getOvertimeReduction` | Get Overtime Reduction (GET /api/v3/overtimeReductions/{id}). Manage overtime reductions. Docs: https://docs.clockodo.com/#tag/OvertimeReduction/operation/getOvertimeReductionByIdV3 |
| Get Project | `getProject` | Get Project (GET /api/v4/projects/{id}). Manage projects. Docs: https://docs.clockodo.com/#tag/Project/operation/getProjectByIdV4 |
| Get Rate | `getRate` | Get Rate (GET /api/v4/rates/{id}). Manage rates. Docs: https://docs.clockodo.com/#tag/Rate/operation/getRateByIdV4 |
| Get Running Clock | `getRunningClock` | Get Running Clock (GET /api/v2/clock). Control the clock. Docs: https://docs.clockodo.com/#tag/Clock/operation/getClockV2 |
| Get Service | `getService` | Get Service (GET /api/v4/services/{id}). Manage services. Docs: https://docs.clockodo.com/#tag/Service/operation/getServiceByIdV4 |
| Get Subproject | `getSubproject` | Get Subproject (GET /api/v3/subprojects/{id}). Manage subprojects. Docs: https://docs.clockodo.com/#tag/Subproject/operation/getSubprojectByIdV3 |
| Get Target Hour | `getTargetHour` | Get Target Hour (GET /api/targethours/{id}). Manage target hours (planned hours). Docs: https://docs.clockodo.com/#tag/TargetHour/operation/getTargetHourById |
| Get Team | `getTeam` | Get Team (GET /api/v3/teams/{id}). Manage teams. Docs: https://docs.clockodo.com/#tag/Team/operation/getTeamByIdV3 |
| Get User | `getUser` | Get User (GET /api/v3/users/{id}). Manage co-workers. Docs: https://docs.clockodo.com/#tag/User/operation/getUserByIdV3 |
| Get Userreport | `getUserreport` | Get Userreport (GET /api/userreports/{id}). Query user reports (e. g. work time evaluation of each day and holiday account of each co-worker). Docs: https://docs.clockodo.com/#tag/UserReport/operation/getUserreportById |
| Get Users Nonbusiness Group | `getUsersNonbusinessGroup` | Get Users Nonbusiness Group (GET /api/v3/usersNonbusinessGroups/{id}). Assign non-business day groups to users and manage time periods. Docs: https://docs.clockodo.com/#tag/UserNonbusinessGroup/operation/getUsersNonbusinessGroupByIdV3 |
| List Absences | `listAbsences` | List Absences (GET /api/v4/absences). Manage absences (holidays, sick days, etc.). Docs: https://docs.clockodo.com/#tag/Absence/operation/getAbsencesV4 |
| List Access Group Customers Projects | `listAccessGroupCustomersProjects` | List Access Group Customers Projects (GET /api/v2/accessGroups/{accessGroupsId}/customersProjects). Manage access group rights. Docs: https://docs.clockodo.com/#tag/AccessGroupAccess/operation/getAccessGroupCustomersProjectsByIdV2 |
| List Access Group Services | `listAccessGroupServices` | List Access Group Services (GET /api/v2/accessGroups/{accessGroupsId}/services). Manage access group rights. Docs: https://docs.clockodo.com/#tag/AccessGroupAccess/operation/getAccessGroupServicesByIdV2 |
| List Access Groups | `listAccessGroups` | List Access Groups (GET /api/v2/accessGroups). Manage access groups names and assigned users. Docs: https://docs.clockodo.com/#tag/AccessGroup/operation/getAccessGroupsV2 |
| List Customers | `listCustomers` | List Customers (GET /api/v3/customers). Manage customers. Docs: https://docs.clockodo.com/#tag/Customer/operation/getCustomersV3 |
| List Entries Texts | `listEntriesTexts` | List Entries Texts (GET /api/v3/entriesTexts). Query descriptions of time and lump sum entries. Docs: https://docs.clockodo.com/#tag/EntryText/operation/getEntriesTextsV3 |
| List Entry Groups | `listEntryGroups` | List Entry Groups (GET /api/v2/entrygroups). Query and manage groups of time entries (particularly useful for evaluation and invoicing purposes). Docs: https://docs.clockodo.com/#tag/EntryGroup/operation/getEntryGroupsV2 |
| List Favorites | `listFavorites` | List Favorites (GET /api/v2/favorites). Manage favorites. Docs: https://docs.clockodo.com/#tag/Favorite/operation/getFavoritesV2 |
| List Holiday Carryovers | `listHolidayCarryovers` | List Holiday Carryovers (GET /api/v3/holidaysCarry). Manage holiday carryovers. Docs: https://docs.clockodo.com/#tag/HolidayCarryover/operation/getHolidayCarryoversV3 |
| List Holiday Quotas | `listHolidaysQuota` | List Holiday Quotas (GET /api/v2/holidaysQuota). Manage holiday quotas. Docs: https://docs.clockodo.com/#tag/HolidayQuota/operation/getHolidayQuotasV2 |
| List Hourly Rates | `listRates` | List Hourly Rates (GET /api/v4/rates). Manage rates. Docs: https://docs.clockodo.com/#tag/Rate/operation/getRatesV4 |
| List Individual User Access Customers Projects | `listIndividualUserAccessCustomersProjects` | List Individual User Access Customers Projects (GET /api/v2/individualUserAccess/{usersId}/customersProjects). Manage individual user rights. Docs: https://docs.clockodo.com/#tag/IndividualUserAccess/operation/getIndividualUserAccessCustomersProjectsByIdV2 |
| List Individual User Access Services | `listIndividualUserAccessServices` | List Individual User Access Services (GET /api/v2/individualUserAccess/{usersId}/services). Manage individual user rights. Docs: https://docs.clockodo.com/#tag/IndividualUserAccess/operation/getIndividualUserAccessServicesByIdV2 |
| List Lump Sum Services | `listLumpSumServices` | List Lump Sum Services (GET /api/v4/lumpSumServices). Manage lump sum services. Docs: https://docs.clockodo.com/#tag/LumpSumService/operation/getLumpSumServicesV4 |
| List Non-Business Groups | `listNonbusinessGroups` | List Non-Business Groups (GET /api/v2/nonbusinessGroups). Query and manage nonbusiness groups. Docs: https://docs.clockodo.com/#tag/NonbusinessGroup/operation/getNonbusinessGroupsV2 |
| List Nonbusiness Days | `listNonbusinessDays` | List Nonbusiness Days (GET /api/v2/nonbusinessDays). Query and manage nonbusiness days. Docs: https://docs.clockodo.com/#tag/NonbusinessDay/operation/getNonbusinessDaysV2 |
| List Overtime Carries | `listOvertimeCarries` | List Overtime Carries (GET /api/v3/overtimeCarry). Manage overtime carryovers. Docs: https://docs.clockodo.com/#tag/OvertimeCarry/operation/getOvertimeCarriesV3 |
| List Overtime Reductions | `listOvertimeReductions` | List Overtime Reductions (GET /api/v3/overtimeReductions). Manage overtime reductions. Docs: https://docs.clockodo.com/#tag/OvertimeReduction/operation/getOvertimeReductionsV3 |
| List Project Reports | `listProjectReports` | List Project Reports (GET /api/v4/projects/reports). Query projects. Docs: https://docs.clockodo.com/#tag/ProjectReport/operation/getProjectsReportsV4 |
| List Project Reports (API v3) | `listProjectReportsV3` | List Project Reports (API v3) (GET /api/v3/projects/reports). Query projects. Docs: https://docs.clockodo.com/#tag/ProjectReport/operation/getProjectsReportsV3 |
| List Projects | `listProjects` | List Projects (GET /api/v4/projects). Manage projects. Docs: https://docs.clockodo.com/#tag/Project/operation/getProjectsV4 |
| List Services | `listServices` | List Services (GET /api/v4/services). Manage services. Docs: https://docs.clockodo.com/#tag/Service/operation/getServicesV4 |
| List Subprojects | `listSubprojects` | List Subprojects (GET /api/v3/subprojects). Manage subprojects. Docs: https://docs.clockodo.com/#tag/Subproject/operation/getSubprojectsV3 |
| List Target Hours | `listTargetHours` | List Target Hours (GET /api/targethours). Manage target hours (planned hours). Docs: https://docs.clockodo.com/#tag/TargetHour/operation/getTargetHours |
| List Teams | `listTeams` | List Teams (GET /api/v3/teams). Manage teams. Docs: https://docs.clockodo.com/#tag/Team/operation/getTeamsV3 |
| List Time Entries | `listEntries` | List Time Entries (GET /api/v2/entries). Manage time and lump sum entries. Docs: https://docs.clockodo.com/#tag/Entry/operation/getEntriesV2 |
| List User Access Customers Projects | `listUserAccessCustomersProjects` | List User Access Customers Projects (GET /api/v2/users/{id}/access/customers-projects). Manage co-workers. Docs: https://docs.clockodo.com/#tag/User/operation/getUserAccessCustomersProjectsByIdV2 |
| List User Access Services | `listUserAccessServices` | List User Access Services (GET /api/v2/users/{id}/access/services). Manage co-workers. Docs: https://docs.clockodo.com/#tag/User/operation/getUserAccessServicesByIdV2 |
| List Userreports | `listUserreports` | List Userreports (GET /api/userreports). Query user reports (e. g. work time evaluation of each day and holiday account of each co-worker). Docs: https://docs.clockodo.com/#tag/UserReport/operation/getUserreports |
| List Users | `listUsers` | List Users (GET /api/v3/users). Manage co-workers. Docs: https://docs.clockodo.com/#tag/User/operation/getUsersV3 |
| List Users Nonbusiness Days | `listUsersNonbusinessDays` | List Users Nonbusiness Days (GET /api/v2/usersNonbusinessDays). Get non-business days of user. Docs: https://docs.clockodo.com/#tag/UserNonbusinessDay/operation/getUsersNonbusinessDaysV2 |
| List Users Nonbusiness Groups | `listUsersNonbusinessGroups` | List Users Nonbusiness Groups (GET /api/v3/usersNonbusinessGroups). Assign non-business day groups to users and manage time periods. Docs: https://docs.clockodo.com/#tag/UserNonbusinessGroup/operation/getUsersNonbusinessGroupsV3 |
| List Webhook Subscriptions | `listWebhookSubscriptions` | Lists the webhook subscriptions registered for the Clockodo company. This route is live but is not present in the published Clockodo OpenAPI document. |
| List Work Time Change Requests | `listWorkTimeChangeRequests` | List Work Time Change Requests (GET /api/v2/workTimes/changeRequests). Manage work times. Work times cannot be edited directly. To edit work times, edit the respective time entries or use requests for change of work time. Docs: https://docs.clockodo.com/#tag/WorkTime/operation/getWorkTimesChangeRequestsV2 |
| List Work Times | `listWorkTimes` | List Work Times (GET /api/v2/workTimes). Manage work times. Work times cannot be edited directly. To edit work times, edit the respective time entries or use requests for change of work time. Docs: https://docs.clockodo.com/#tag/WorkTime/operation/getWorkTimesV2 |
| Set Project Billed | `setProjectBilled` | Set Project Billed (PUT /api/v3/projects/{id}/setBilled). Manage projects. Docs: https://docs.clockodo.com/#tag/Project/operation/updateProjectBilledByIdV3 |
| Start Favorite | `startFavorite` | Start Favorite (POST /api/v2/favorites/{id}/start). Manage favorites. Docs: https://docs.clockodo.com/#tag/Favorite/operation/startFavoriteByIdV2 |
| Update Absence | `updateAbsence` | Update Absence (PUT /api/v4/absences/{id}). Manage absences (holidays, sick days, etc.). Docs: https://docs.clockodo.com/#tag/Absence/operation/updateAbsenceByIdV4 |
| Update Access Group | `updateAccessGroup` | Update Access Group (PUT /api/v2/accessGroups/{id}). Manage access groups names and assigned users. Docs: https://docs.clockodo.com/#tag/AccessGroup/operation/updateAccessGroupByIdV2 |
| Update Access Group Customers | `updateAccessGroupCustomers` | Update Access Group Customers (PUT /api/v2/accessGroups/{accessGroupsId}/customers). Manage access group rights. Docs: https://docs.clockodo.com/#tag/AccessGroupAccess/operation/updateAccessGroupCustomersByIdV2 |
| Update Access Group Customers General | `updateAccessGroupCustomersGeneral` | Update Access Group Customers General (PUT /api/v2/accessGroups/{accessGroupsId}/customers/general). Manage access group rights. Docs: https://docs.clockodo.com/#tag/AccessGroupAccess/operation/updateAccessGroupCustomersGeneralByIdV2 |
| Update Access Group Projects | `updateAccessGroupProjects` | Update Access Group Projects (PUT /api/v2/accessGroups/{accessGroupsId}/projects). Manage access group rights. Docs: https://docs.clockodo.com/#tag/AccessGroupAccess/operation/updateAccessGroupProjectsByIdV2 |
| Update Access Group Services | `updateAccessGroupServices` | Update Access Group Services (PUT /api/v2/accessGroups/{accessGroupsId}/services). Manage access group rights. Docs: https://docs.clockodo.com/#tag/AccessGroupAccess/operation/updateAccessGroupServicesByIdV2 |
| Update Access Group Services General | `updateAccessGroupServicesGeneral` | Update Access Group Services General (PUT /api/v2/accessGroups/{accessGroupsId}/services/general). Manage access group rights. Docs: https://docs.clockodo.com/#tag/AccessGroupAccess/operation/updateAccessGroupServicesGeneralByIdV2 |
| Update Clock | `updateClock` | Update Clock (PUT /api/v2/clock/{id}). Control the clock. Docs: https://docs.clockodo.com/#tag/Clock/operation/updateClockByIdV2 |
| Update Customer | `updateCustomer` | Update Customer (PUT /api/v3/customers/{id}). Manage customers. Docs: https://docs.clockodo.com/#tag/Customer/operation/updateCustomerByIdV3 |
| Update Entry | `updateEntry` | Update Entry (PUT /api/v2/entries/{id}). Manage time and lump sum entries. Docs: https://docs.clockodo.com/#tag/Entry/operation/updateEntryByIdV2 |
| Update Entry Groups | `updateEntryGroups` | Update Entry Groups (PUT /api/v2/entrygroups). Query and manage groups of time entries (particularly useful for evaluation and invoicing purposes). Two-step: the first call returns confirm_key and affected_entries; repeat with confirm_key to apply. Body filter object narrows the entries. Docs: https://docs.clockodo.com/#tag/EntryGroup/operation/updateEntryGroupsV2 |
| Update Favorite | `updateFavorite` | Update Favorite (PUT /api/v2/favorites/{id}). Manage favorites. Docs: https://docs.clockodo.com/#tag/Favorite/operation/updateFavoriteByIdV2 |
| Update Holiday Carryover | `updateHolidayCarryover` | Update Holiday Carryover (PUT /api/v3/holidaysCarry/{id}). Manage holiday carryovers. Docs: https://docs.clockodo.com/#tag/HolidayCarryover/operation/updateHolidayCarryoverByIdV3 |
| Update Holiday Quota | `updateHolidayQuota` | Update Holiday Quota (PUT /api/v2/holidaysQuota/{id}). Manage holiday quotas. Docs: https://docs.clockodo.com/#tag/HolidayQuota/operation/updateHolidayQuotaByIdV2 |
| Update Individual User Access Customers | `updateIndividualUserAccessCustomers` | Update Individual User Access Customers (PUT /api/v2/individualUserAccess/{usersId}/customers). Manage individual user rights. Docs: https://docs.clockodo.com/#tag/IndividualUserAccess/operation/updateIndividualUserAccessCustomersByIdV2 |
| Update Individual User Access Customers General | `updateIndividualUserAccessCustomersGeneral` | Update Individual User Access Customers General (PUT /api/v2/individualUserAccess/{usersId}/customers/general). Manage individual user rights. Docs: https://docs.clockodo.com/#tag/IndividualUserAccess/operation/updateIndividualUserAccessCustomersGeneralByIdV2 |
| Update Individual User Access Projects | `updateIndividualUserAccessProjects` | Update Individual User Access Projects (PUT /api/v2/individualUserAccess/{usersId}/projects). Manage individual user rights. Docs: https://docs.clockodo.com/#tag/IndividualUserAccess/operation/updateIndividualUserAccessProjectsByIdV2 |
| Update Individual User Access Services | `updateIndividualUserAccessServices` | Update Individual User Access Services (PUT /api/v2/individualUserAccess/{usersId}/services). Manage individual user rights. Docs: https://docs.clockodo.com/#tag/IndividualUserAccess/operation/updateIndividualUserAccessServicesByIdV2 |
| Update Individual User Access Services General | `updateIndividualUserAccessServicesGeneral` | Update Individual User Access Services General (PUT /api/v2/individualUserAccess/{usersId}/services/general). Manage individual user rights. Docs: https://docs.clockodo.com/#tag/IndividualUserAccess/operation/updateIndividualUserAccessServicesGeneralByIdV2 |
| Update Lump Sum Service | `updateLumpSumService` | Update Lump Sum Service (PUT /api/v4/lumpSumServices/{id}). Manage lump sum services. Docs: https://docs.clockodo.com/#tag/LumpSumService/operation/updateLumpSumServiceByIdV4 |
| Update Nonbusiness Day | `updateNonbusinessDay` | Update Nonbusiness Day (PUT /api/v2/nonbusinessDays/{id}). Query and manage nonbusiness days. Docs: https://docs.clockodo.com/#tag/NonbusinessDay/operation/updateNonbusinessDayByIdV2 |
| Update Nonbusiness Group | `updateNonbusinessGroup` | Update Nonbusiness Group (PUT /api/v2/nonbusinessGroups/{id}). Query and manage nonbusiness groups. Docs: https://docs.clockodo.com/#tag/NonbusinessGroup/operation/updateNonbusinessGroupByIdV2 |
| Update Overtime Carry | `updateOvertimeCarry` | Update Overtime Carry (PUT /api/v3/overtimeCarry/{id}). Manage overtime carryovers. Docs: https://docs.clockodo.com/#tag/OvertimeCarry/operation/updateOvertimeCarryByIdV3 |
| Update Overtime Reduction | `updateOvertimeReduction` | Update Overtime Reduction (PUT /api/v3/overtimeReductions/{id}). Manage overtime reductions. Docs: https://docs.clockodo.com/#tag/OvertimeReduction/operation/updateOvertimeReductionByIdV3 |
| Update Project | `updateProject` | Update Project (PUT /api/v4/projects/{id}). Manage projects. Docs: https://docs.clockodo.com/#tag/Project/operation/updateProjectByIdV4 |
| Update Rate | `updateRate` | Update Rate (PUT /api/v4/rates/{id}). Manage rates. Docs: https://docs.clockodo.com/#tag/Rate/operation/updateRateByIdV4 |
| Update Rate Order | `updateRateOrder` | Update Rate Order (PUT /api/v4/rates/{id}/sort). Manage rates. Docs: https://docs.clockodo.com/#tag/Rate/operation/updateRateOrderByIdV4 |
| Update Rates Default | `updateRatesDefault` | Update Rates Default (PUT /api/v4/rates/default). Manage rates. Docs: https://docs.clockodo.com/#tag/Rate/operation/updateRatesDefaultV4 |
| Update Service | `updateService` | Update Service (PUT /api/v4/services/{id}). Manage services. Docs: https://docs.clockodo.com/#tag/Service/operation/updateServiceByIdV4 |
| Update Subproject | `updateSubproject` | Update Subproject (PUT /api/v3/subprojects/{id}). Manage subprojects. Docs: https://docs.clockodo.com/#tag/Subproject/operation/updateSubprojectByIdV3 |
| Update Target Hour | `updateTargetHour` | Update Target Hour (PUT /api/targethours/{id}). Manage target hours (planned hours). PUT replaces the whole row: send type, date_since and every day field (monday..sunday) plus compensation_daily/compensation_monthly, else 400 Missing data. Docs: https://docs.clockodo.com/#tag/TargetHour/operation/updateTargetHourById |
| Update Team | `updateTeam` | Update Team (PUT /api/v3/teams/{id}). Manage teams. Docs: https://docs.clockodo.com/#tag/Team/operation/updateTeamByIdV3 |
| Update User | `updateUser` | Update User (PUT /api/v3/users/{id}). Manage co-workers. Docs: https://docs.clockodo.com/#tag/User/operation/updateUserByIdV3 |
| Update Users Nonbusiness Group | `updateUsersNonbusinessGroup` | Update Users Nonbusiness Group (PUT /api/v3/usersNonbusinessGroups/{id}). Assign non-business day groups to users and manage time periods. Docs: https://docs.clockodo.com/#tag/UserNonbusinessGroup/operation/updateUsersNonbusinessGroupByIdV3 |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Absence Approved | `absence.approved` |  |
| Absence Created | `absence.created` |  |
| Absence Deleted | `absence.deleted` |  |
| Absence Updated | `absence.updated` |  |
| Customer Created | `customer.created` |  |
| Customer Deleted | `customer.deleted` |  |
| Customer Updated | `customer.updated` |  |
| Holiday Carry-Over Created | `holidays_carry.created` |  |
| Holiday Carry-Over Deleted | `holidays_carry.deleted` |  |
| Holiday Carry-Over Updated | `holidays_carry.updated` |  |

<details>

<summary>See 37 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Holiday Quota Created | `holidays_quota.created` |  |
| Holiday Quota Deleted | `holidays_quota.deleted` |  |
| Holiday Quota Updated | `holidays_quota.updated` |  |
| Lump Sum Service Created | `lump_sum_service.created` |  |
| Lump Sum Service Deleted | `lump_sum_service.deleted` |  |
| Lump Sum Service Updated | `lump_sum_service.updated` |  |
| Non-Business Group Created | `nonbusiness_group.created` |  |
| Non-Business Group Deleted | `nonbusiness_group.deleted` |  |
| Non-Business Group Updated | `nonbusiness_group.updated` |  |
| Overtime Carry-Over Created | `overtime_carry.created` |  |
| Overtime Carry-Over Deleted | `overtime_carry.deleted` |  |
| Overtime Carry-Over Updated | `overtime_carry.updated` |  |
| Project Budget Threshold Reached | `project.budget_notification` |  |
| Project Completed | `project.completed` |  |
| Project Created | `project.created` |  |
| Project Deleted | `project.deleted` |  |
| Project Updated | `project.updated` |  |
| Service Created | `service.created` |  |
| Service Deleted | `service.deleted` |  |
| Service Updated | `service.updated` |  |
| Subproject Created | `subproject.created` |  |
| Subproject Deleted | `subproject.deleted` |  |
| Subproject Updated | `subproject.updated` |  |
| Team Created | `team.created` |  |
| Team Deleted | `team.deleted` |  |
| Team Updated | `team.updated` |  |
| Time Entry Created | `entry.created` | A time entry was created. |
| Time Entry Deleted | `entry.deleted` | A time entry was deleted. |
| Time Entry Started | `entry.started` | The stop clock was started. |
| Time Entry Stopped | `entry.stopped` | The stop clock was stopped. |
| Time Entry Updated | `entry.updated` | A time entry was changed. |
| User Created | `user.created` |  |
| User Deleted | `user.deleted` |  |
| User Updated | `user.updated` |  |
| Work Time Change Request Created | `work_time_change_request.created` |  |
| Work Time Change Request Deleted | `work_time_change_request.deleted` |  |
| Work Time Change Request Updated | `work_time_change_request.updated` |  |

</details>
