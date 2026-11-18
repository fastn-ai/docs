---
description: "Tableau Cloud and Tableau Server REST API."
hidden: true
---

# Tableau

<img src="../../.gitbook/assets/connectors/tableau.png" alt="Tableau logo" width="64">

Tableau Cloud and Tableau Server REST API. Manage sites, projects, workbooks, views, data sources, users, groups, extract refresh jobs and tasks, flows, subscriptions, favorites and webhooks. Sign in with username and password, or with a personal access token; fastn signs in and renews the Tableau session for you.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [tableau.com](https://tableau.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `tableau` |

## Use it

Add Tableau from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tableau.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add User to Group | `addUserToGroup` | Adds the specified user to the specified group. |
| Add User to Site | `addUser` | Adds a user to the site with the specified site role and authentication setting. |
| Add Workbook to Favorites | `addFavorite` | Adds a workbook to the specified user's favorites with a label. |
| Cancel Job | `cancelJob` | Cancels the specified background job. Returns 204 No Content. |
| Create Group | `createGroup` | Creates a local group on the site with an optional minimum site role. |
| Create Project | `createProject` | Creates a project on the site. Optionally nests under a parent project. |
| Create Subscription | `createSubscription` | Creates a subscription that emails a view or workbook to a user. Tableau Cloud: give frequency, startTime and weekDay. Tableau Server: give serverSchedule with the schedule id. |
| Create Webhook | `createWebhook` | Creates a webhook on the site that POSTs to a destination URL when the specified Tableau event fires. The event is specified via webhook-source (e.g. webhook-source-event-workbook-created) or the preferred 'event' attribute. |
| Delete Data Source | `deleteDataSource` | Deletes the specified published data source from the site. Returns 204 No Content. |
| Delete Extract Refresh Task | `deleteExtractRefreshTask` | Deletes the specified extract refresh task from the site. Returns 204 No Content. |

<details>

<summary>See 57 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Flow | `deleteFlow` | Deletes the specified flow from the site. Returns 204 No Content. |
| Delete Group | `deleteGroup` | Deletes the specified group from the site. Returns 204 No Content. |
| Delete Project | `deleteProject` | Deletes the specified project and all content within it. Returns 204 No Content. |
| Delete Subscription | `deleteSubscription` | Deletes the specified subscription. Returns 204 No Content. |
| Delete Webhook | `deleteWebhook` | Deletes the specified webhook from the site. Returns 204 No Content. |
| Delete Workbook | `deleteWorkbook` | Deletes the specified workbook from the site. Returns 204 No Content. |
| Delete Workbook from Favorites | `deleteFavorite` | Removes a workbook from the specified user's favorites. Returns 204 No Content. |
| Download Data Source | `downloadDataSource` | Downloads a published data source as a .tds or .tdsx file. Set includeExtract=false to exclude extract data. |
| Download Workbook | `downloadWorkbook` | Downloads a workbook as a .twb or .twbx file. Set includeExtract=false to exclude extract data. |
| Get Current Server Info | `getServerInfo` | Returns the version of Tableau Server/Cloud and the supported REST API version. Does not require authentication. |
| Get Current Session | `getCurrentSession` | Returns the signed-in user and site for this connection (Tableau Cloud and Tableau Server). Used as the connection check. |
| Get Data Source | `getDataSource` | Returns information about the specified published data source. |
| Get Extract Refresh Task | `getExtractRefreshTask` | Returns details about a specific extract refresh task on the site. |
| Get Favorites for User | `listFavorites` | Returns the favorite content (workbooks, views, data sources, projects, flows) for the specified user. |
| Get Flow | `getFlow` | Returns information about the specified flow. |
| Get Job | `getJob` | Returns the status and details of a specific background job (e.g. an extract refresh). |
| Get Site | `getSite` | Returns information about the specified site. Uses the site LUID from sign-in. |
| Get Subscription | `getSubscription` | Returns details about the specified subscription. |
| Get User | `getUser` | Returns information about the specified user on the site. |
| Get Users in Group | `getUsersInGroup` | Returns the users that are members of the specified group. |
| Get View | `getView` | Returns details about the specified view. |
| Get View Data (CSV) | `getViewData` | Returns the underlying data of the specified view as CSV. Supports view filters via vf_ query parameters. |
| Get View Image (PNG) | `getViewImage` | Returns a PNG image of the specified view. Supports resolution and view filters. |
| Get View PDF | `getViewPdf` | Returns a PDF of the specified view. Supports page type/orientation and view filters. |
| Get Webhook | `getWebhook` | Returns information about the specified webhook. |
| Get Workbook | `getWorkbook` | Returns information about the specified workbook, including views and connections metadata. |
| List Data Sources | `listDataSources` | Returns the published data sources on the site. Supports filtering, sorting, fields, and pagination. |
| List Extract Refresh Tasks | `listExtractRefreshTasks` | Returns the extract refresh tasks for the site. Each task is associated with a schedule and a workbook or data source. |
| List Flows | `listFlows` | Returns the Tableau Prep flows on the site. Supports filtering, sorting, and pagination. |
| List Groups | `listGroups` | Returns the groups on the site. Supports filtering, sorting, and pagination. |
| List Projects | `listProjects` | Returns a list of projects on the site. Supports filtering, sorting, and pagination. |
| List Schedules | `listSchedules` | Tableau Server only: returns the server schedules used for extract refresh and subscription tasks. Not available on Tableau Cloud: Tableau answers 403 "Admin schedules are not supported for this site" (Tableau REST docs, List Server Schedules). On Tableau Cloud, schedules are set on each task instead. |
| List Sites | `listSites` | Tableau Server only: returns the sites this sign-in can see (a server admin sees every site). Not available on Tableau Cloud: Tableau answers 403 "Sites query is unsupported for Tableau Cloud" (Tableau REST docs, Query Sites). Supports pagination. |
| List Subscriptions | `listSubscriptions` | Returns the subscriptions on the site (scheduled email deliveries of views/workbooks). |
| List Users | `listUsers` | Returns the users on the site. Supports filtering, sorting, fields, and pagination. |
| List Views for Site | `listViews` | Returns all views on the site that the user can access. Supports filtering, sorting, fields, includeUsageStatistics, and pagination. |
| List Views for Workbook | `listViewsForWorkbook` | Returns all views contained in the specified workbook. |
| List Webhooks | `listWebhooks` | Returns the webhooks configured on the site. |
| List Workbooks | `listWorkbooks` | Returns the workbooks on the site that the signed-in user can read. Supports filtering, sorting, fields, and pagination. |
| Query Jobs | `listJobs` | Returns a list of active and recent background jobs on the site. Supports filtering by job type, status, and creation date. |
| Refresh Data Source Now | `refreshDataSource` | Starts an extract refresh for the specified data source. Returns a background job. |
| Refresh Workbook Now | `refreshWorkbook` | Starts an extract refresh for the specified workbook. Returns a background job. Body must be an empty XML/JSON request. |
| Remove User from Group | `removeUserFromGroup` | Removes the specified user from the specified group. Returns 204 No Content. |
| Remove User from Site | `removeUser` | Removes the specified user from the site. Returns 204 No Content. Optionally map assets to another user. |
| Run Extract Refresh Task | `runExtractRefreshTask` | Runs the specified extract refresh task immediately. Returns a background job. |
| Run Flow Now | `runFlow` | Runs the specified flow immediately. Returns a background job. |
| Sign In | `signIn` | Signs in to Tableau with the connection's own login (username and password, or personal access token) and returns the session token, site id and user id. Runs automatically when a call is rejected, so other actions never need it called by hand. |
| Sign Out | `signOut` | Sign out of Tableau, invalidating the current credentials token. Returns 204 No Content. |
| Test Webhook | `testWebhook` | Tests the specified webhook by sending an empty payload to its destination URL and returning the response status. |
| Update Data Source | `updateDataSource` | Updates the name or certification of a published data source. |
| Update Flow | `updateFlow` | Updates a flow's project or owner. |
| Update Group | `updateGroup` | Updates the name or minimum site role of a local group. |
| Update Project | `updateProject` | Updates the name, description, parent, or content permissions of a project. |
| Update Site | `updateSite` | Tableau Server only: updates the name or state of the current site. Tableau docs: "This method can only be called by server administrators." Tableau Cloud has no customer server admin, so Cloud answers 403 "Only system administrators can update sites". |
| Update Subscription | `updateSubscription` | Updates the subject or schedule of an existing subscription. |
| Update User | `updateUser` | Updates a user's site role, full name or email. |
| Update Workbook | `updateWorkbook` | Updates a workbook's name or whether sheets show as tabs. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Admin Demoted | `AdminDemoted` | Fires when a user is demoted from admin. |
| Admin Promoted | `AdminPromoted` | Fires when a user is promoted to admin. |
| Data Source Created | `DatasourceCreated` | Fires when a data source is published/created. |
| Data Source Deleted | `DatasourceDeleted` | Fires when a data source is deleted. |
| Data Source Refresh Failed | `DatasourceRefreshFailed` | Fires when an extract refresh for a data source fails. |
| Data Source Refresh Started | `DatasourceRefreshStarted` | Fires when an extract refresh for a data source starts. |
| Data Source Refresh Succeeded | `DatasourceRefreshSucceeded` | Fires when an extract refresh for a data source completes successfully. |
| Data Source Updated | `DatasourceUpdated` | Fires when a data source is updated. |
| Label Created | `LabelCreated` | Fires when a data quality/sensitivity label is created on a workbook or data source. |
| Label Deleted | `LabelDeleted` | Fires when a label is deleted. |

<details>

<summary>See 12 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Label Updated | `LabelUpdated` | Fires when a label is updated. |
| Site Created | `SiteCreated` | Fires when a site is created. |
| Site Deleted | `SiteDeleted` | Fires when a site is deleted. |
| Site Updated | `SiteUpdated` | Fires when a site is updated. |
| User Deleted | `UserDeleted` | Fires when a user is deleted from the site. |
| View Deleted | `ViewDeleted` | Fires when a view is deleted. |
| Workbook Created | `WorkbookCreated` | Fires when a workbook is published/created on the site. |
| Workbook Deleted | `WorkbookDeleted` | Fires when a workbook is deleted. |
| Workbook Refresh Failed | `WorkbookRefreshFailed` | Fires when an extract refresh for a workbook fails. |
| Workbook Refresh Started | `WorkbookRefreshStarted` | Fires when an extract refresh for a workbook starts. |
| Workbook Refresh Succeeded | `WorkbookRefreshSucceeded` | Fires when an extract refresh for a workbook completes successfully. |
| Workbook Updated | `WorkbookUpdated` | Fires when a workbook is updated. |

</details>
