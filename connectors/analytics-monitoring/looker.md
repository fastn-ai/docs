---
description: "Looker (Google Cloud) BI platform — Looker API 4.0."
hidden: true
---

# Looker

<img src="../../.gitbook/assets/connectors/lg/looker.png" alt="Looker logo">

Looker (Google Cloud) BI platform — Looker API 4.0. Manage Looks, Dashboards, Queries, Folders, Users, Groups, Roles, database Connections, LookML models/projects, Content favorites, Scheduled plans, Render tasks, and Alerts. Auth: API3 credentials (client_id + client_secret) exchanged at POST /login for a short-lived access_token, then sent as 'Authorization: token &lt;access_token&gt;'. Base host is the per-instance API URL, e.g. https://&lt;instance&gt;.cloud.looker.com:19999/api/4.0

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [looker.com](https://looker.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `looker` |

## Use it

Add Looker from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.looker.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add User To Group | `addUserToGroup` | Add a user to a group. |
| Create Alert | `createAlert` | Create a dashboard-element alert that fires when a value crosses a threshold and delivers to destinations. |
| Create Connection | `createConnection` | Create a new database connection. |
| Create Content Favorite | `createContentFavorite` | Mark a Look or dashboard as a favorite for a content metadata id. |
| Create Dashboard | `createDashboard` | Create a new user-defined dashboard in a folder. |
| Create Dashboard Render Task | `createDashboardRenderTask` | Start an asynchronous render of a dashboard to a file format (pdf, png, jpg). Poll the render task for completion, then fetch results. |
| Create Folder | `createFolder` | Create a new folder under a parent folder. |
| Create Group | `createGroup` | Create a new group. |
| Create Look | `createLook` | Create a new Look from an existing query in a folder. |
| Create Look Render Task | `createLookRenderTask` | Start an asynchronous render of a Look to a file format (png, jpg). |
| Create Query | `createQuery` | Create a query definition (model + view/explore + fields) that can then be run. Returns the query with its id. |
| Create Role | `createRole` | Create a new role from a permission set and a model set. |
| Create Scheduled Plan | `createScheduledPlan` | Create a scheduled plan that delivers a dashboard on a crontab to one or more destinations. |
| Create User | `createUser` | Create a new user (first/last name). Set credentials separately. |
| Delete Alert | `deleteAlert` | Delete an alert by id. |
| Delete Content Favorite | `deleteContentFavorite` | Remove a content favorite by id. |
| Delete Dashboard | `deleteDashboard` | Delete a dashboard by id. |
| Delete Folder | `deleteFolder` | Delete a folder by id. |
| Delete Group | `deleteGroup` | Delete a group by id. |
| Delete Look | `deleteLook` | Delete a Look by id. |
| Delete Role | `deleteRole` | Delete a role by id. |
| Delete Scheduled Plan | `deleteScheduledPlan` | Delete a scheduled plan by id. |
| Delete User | `deleteUser` | Delete a user by id. |
| Get Alert | `getAlert` | Get a single alert by id. |
| Get API Versions | `getApiVersions` | Get the API and server version information for this Looker instance. |
| Get Connection | `getConnection` | Get a single database connection by name. |
| Get Current User | `getCurrentUser` | Get the user account associated with the API credentials (the 'me' user). |
| Get Dashboard | `getDashboard` | Get a single dashboard by id. |
| Get Folder | `getFolder` | Get a single folder by id. |
| Get Group | `getGroup` | Get a single group by id. |
| Get Look | `getLook` | Get a single Look by id. |
| Get LookML Model | `getLookmlModel` | Get a single LookML model by name. |
| Get LookML Model Explore | `getLookmlModelExplore` | Get the detailed definition (fields, joins) of an explore within a LookML model. |
| Get Project | `getProject` | Get a single LookML project by id. |
| Get Query | `getQuery` | Get a query definition by id. |
| Get Query By Slug | `getQueryBySlug` | Get a query definition by its slug. |
| Get Render Task | `getRenderTask` | Get the status of a render task. |
| Get Render Task Results | `getRenderTaskResults` | Download the rendered document/image once the render task has completed. |
| Get Role | `getRole` | Get a single role by id. |
| Get Role Users | `getRoleUsers` | Get the users assigned to a role. |
| Get Scheduled Plan | `getScheduledPlan` | Get a single scheduled plan by id. |
| Get Session | `getSession` | Get information about the current API session, including the active workspace id. |
| Get User | `getUser` | Get a single user by id. |
| Get User Roles | `getUserRoles` | Get the roles assigned to a user. |
| List Connections | `listConnections` | Get all database connections configured in Looker. |
| List Dashboard Elements | `listDashboardElements` | Get all elements (tiles) of a dashboard. |
| List Dashboards | `listDashboards` | Get all dashboards (user-defined and LookML). |
| List Folder Children | `listFolderChildren` | Get the child folders of a folder. |
| List Folder Looks | `listFolderLooks` | Get the Looks contained in a folder. |
| List Folders | `listFolders` | Get all folders. |
| List Groups | `listGroups` | Get all groups. |
| List LookML Models | `listLookmlModels` | Get all LookML models. |
| List Looks | `listLooks` | Get all Looks (saved visualizations). Optionally narrow returned fields. |
| List Projects | `listProjects` | Get all LookML projects. |
| List Roles | `listRoles` | Get all roles. |
| List Scheduled Plans | `listScheduledPlans` | Get scheduled plans, optionally filtered to all users (admin) or the current user. |
| List Users | `listUsers` | Get all users. |
| Login | `login` | Exchange API3 client_id + client_secret for a short-lived access_token. Returns access_token to send on every other action as 'Authorization: token &lt;access_token&gt;'. |
| Run Inline Query | `runInlineQuery` | Create and run a query in a single call. Provide model, view, and fields; returns data in the requested result format. |
| Run Look | `runLook` | Run a saved Look and return its data in the requested result format (json, json_detail, csv, txt, html, md, xlsx, png). |
| Run Query | `runQuery` | Run a previously created query by id and return data in the requested result format. |
| Run Scheduled Plan Once | `runScheduledPlanOnce` | Immediately run a scheduled-plan definition once without saving it. |
| Search Alerts | `searchAlerts` | Search alerts by group, owner, fields, and other filters. |
| Search Content Favorites | `searchContentFavorites` | Search content favorites by user, look, dashboard, or content metadata id. |
| Search Dashboards | `searchDashboards` | Search dashboards by title, folder, user, and other filters. |
| Search Folders | `searchFolders` | Search folders by name, parent, and other filters. |
| Search Groups | `searchGroups` | Search groups by name and other filters. |
| Search Looks | `searchLooks` | Search Looks by title, folder, user, and other filters. |
| Search Users | `searchUsers` | Search users by name, email, id, and other filters. |
| Test Connection | `testConnection` | Run connectivity tests against a configured database connection. |
| Update Connection | `updateConnection` | Update settings of an existing database connection. |
| Update Dashboard | `updateDashboard` | Update a dashboard's title and/or description. |
| Update Folder | `updateFolder` | Rename or move a folder. |
| Update Look | `updateLook` | Update a Look's title and/or description. |
| Update Role | `updateRole` | Update a role's name. |
| Update Scheduled Plan | `updateScheduledPlan` | Update a scheduled plan's name or schedule. |
| Update User | `updateUser` | Update a user's name or disabled state. |
