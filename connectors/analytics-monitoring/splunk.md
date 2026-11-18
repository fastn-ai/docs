---
description: "Splunk Enterprise / Splunk Cloud REST API connector."
hidden: true
---

# Splunk

Splunk Enterprise / Splunk Cloud REST API connector. Manage search jobs, saved searches, indexes, data inputs, KV store collections, apps, users, roles, alerts, server info, and send events via HTTP Event Collector (HEC). Auth via Bearer token against the management port (8089); HEC uses port 8088.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [splunk.com](https://splunk.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 60 |
| **Events** | 0 |
| **Slug** | `splunk` |

## Use it

Add Splunk from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.splunk.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Save KV Store Data | `batchSaveKvData` | Insert or update multiple records in one call. POST storage/collections/data/{collection}/batch_save with a JSON array body. Returns an array of saved _keys. |
| Control Search Job | `controlSearchJob` | Perform a control action on a search job (pause, unpause, finalize, cancel, touch, setttl, setpriority, enablepreview, disablepreview, save, unsave). POST search/jobs/{sid}/control. |
| Create App | `createApp` | Create/install a new app. POST apps/local with a name. |
| Create Index | `createIndex` | Create a new data index. POST data/indexes with a name. |
| Create KV Store Collection | `createKvCollection` | Create a new KV store collection definition. POST storage/collections/config with a name. |
| Create Monitor Input | `createMonitorInput` | Create a file/directory monitor data input. POST data/inputs/monitor with a name (the path to monitor). |
| Create Role | `createRole` | Create a new authorization role. POST authorization/roles with a name. |
| Create Saved Search | `createSavedSearch` | Create a new saved search. POST saved/searches with name and search string. |
| Create Search Job | `createSearchJob` | Create a new search job. POST search/jobs with a search string (SPL). Returns the search job ID (sid). |
| Create User | `createUser` | Create a new user. POST authentication/users with name, password, and roles. |
| Delete All KV Store Data | `deleteAllKvData` | Delete all records in a KV store collection. DELETE storage/collections/data/{collection}. |
| Delete App | `deleteApp` | Uninstall/delete an app by name. DELETE apps/local/{name}. |
| Delete Index | `deleteIndex` | Delete a data index by name. DELETE data/indexes/{name}. |
| Delete KV Store Collection | `deleteKvCollection` | Delete a KV store collection definition. DELETE storage/collections/config/{collection}. |
| Delete KV Store Record | `deleteKvRecord` | Delete a single record from a KV store collection by key. DELETE storage/collections/data/{collection}/{key}. |
| Delete Monitor Input | `deleteMonitorInput` | Delete a monitor data input by name (path). DELETE data/inputs/monitor/{name}. |
| Delete Role | `deleteRole` | Delete an authorization role by name. DELETE authorization/roles/{name}. |
| Delete Saved Search | `deleteSavedSearch` | Delete a saved search by name. DELETE saved/searches/{name}. |
| Delete Search Job | `deleteSearchJob` | Delete a search job and free its resources. DELETE search/jobs/{sid}. |
| Delete User | `deleteUser` | Delete a user by username. DELETE authentication/users/{name}. |
| Dispatch Saved Search | `dispatchSavedSearch` | Run (dispatch) a saved search, creating a new search job. POST saved/searches/{name}/dispatch. Returns the sid. |
| Get App | `getApp` | Get a specific installed app by name. GET apps/local/{name}. |
| Get Fired Alerts For Saved Search | `getFiredAlertsForSavedSearch` | Get fired alert instances for a specific saved search. GET alerts/fired_alerts/{name}. |
| Get Index | `getIndex` | Get a specific index by name. GET data/indexes/{name}. |
| Get KV Store Collection | `getKvCollection` | Get a specific KV store collection definition. GET storage/collections/config/{collection}. |
| Get KV Store Record | `getKvRecord` | Get a single record from a KV store collection by key. GET storage/collections/data/{collection}/{key}. |
| Get Role | `getRole` | Get a specific role by name. GET authorization/roles/{name}. |
| Get Saved Search | `getSavedSearch` | Get a specific saved search by name. GET saved/searches/{name}. |
| Get Saved Search History | `getSavedSearchHistory` | Get the list of search jobs created from a saved search. GET saved/searches/{name}/history. |
| Get Search Job | `getSearchJob` | Get the status and metadata of a specific search job by its sid. GET search/jobs/{sid}. |
| Get Search Job Events | `getSearchJobEvents` | Retrieve the raw events (untransformed) matched by a search job. GET search/jobs/{sid}/events. |
| Get Search Job Results | `getSearchJobResults` | Retrieve the transformed/final results of a completed search job. GET search/jobs/{sid}/results. |
| Get Search Job Summary | `getSearchJobSummary` | Get a field summary (field/value statistics) for a search job. GET search/jobs/{sid}/summary. |
| Get Server Health | `getServerHealth` | Get the deployment health report (splunkd health tree). GET server/health/splunkd. |
| Get Server Info | `getServerInfo` | Get general server/instance information (version, build, license, server roles, OS). GET server/info. |
| Get Server Settings | `getServerSettings` | Get server settings (ports, paths, session timeout, etc). GET server/settings. |
| Get User | `getUser` | Get a specific user by username. GET authentication/users/{name}. |
| HEC Send Event | `hecSendEvent` | Send a single event to Splunk via the HTTP Event Collector (HEC) on port 8088. POST services/collector/event. Uses the HEC token (auth.token) as 'Splunk &lt;token&gt;'. |
| HEC Send Raw Event | `hecSendRaw` | Send raw (unstructured) data to Splunk via HEC on port 8088. POST services/collector/raw. Body is sent as plain text. |
| Insert KV Store Record | `insertKvRecord` | Insert a new record into a KV store collection. POST storage/collections/data/{collection} with a JSON body. Returns the generated _key. |
| List Alert Actions | `listAlertActions` | List all configured alert action types (email, webhook, script, etc). GET alerts/alert_actions. |
| List Apps | `listApps` | List all installed apps. GET apps/local. |
| List Capabilities | `listCapabilities` | List all available authorization capabilities. GET authorization/capabilities. |
| List Data Inputs | `listDataInputs` | List all data inputs across input types. GET data/inputs/all. |
| List Fired Alerts | `listFiredAlerts` | List all fired alert groups across saved searches. GET alerts/fired_alerts. |
| List Indexes | `listIndexes` | List all data indexes. GET data/indexes. |
| List KV Store Collections | `listKvCollections` | List all KV store collection definitions. GET storage/collections/config. |
| List KV Store Data | `listKvData` | Query/list all records in a KV store collection. GET storage/collections/data/{collection}. Returns a JSON array of records. |
| List Monitor Inputs | `listMonitorInputs` | List file/directory monitor data inputs. GET data/inputs/monitor. |
| List Roles | `listRoles` | List all authorization roles. GET authorization/roles. |
| List Saved Searches | `listSavedSearches` | List all saved searches. GET saved/searches. |
| List Search Jobs | `listSearchJobs` | List all current search jobs. GET search/jobs. |
| List TCP Inputs | `listTcpInputs` | List raw TCP data inputs. GET data/inputs/tcp/raw. |
| List Users | `listUsers` | List all users. GET authentication/users. |
| Update App | `updateApp` | Update settings of an installed app. POST apps/local/{name}. |
| Update Index | `updateIndex` | Update index settings. POST data/indexes/{name}. |
| Update KV Store Record | `updateKvRecord` | Replace an existing record in a KV store collection by key. POST storage/collections/data/{collection}/{key} with a JSON body. |
| Update Role | `updateRole` | Update an authorization role. POST authorization/roles/{name}. |
| Update Saved Search | `updateSavedSearch` | Update an existing saved search. POST saved/searches/{name} with fields to change (name cannot be changed). |
| Update User | `updateUser` | Update an existing user. POST authentication/users/{name}. |
