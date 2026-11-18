---
description: "Grafana Cloud connector for the Grafana instance HTTP API — manage dashboards, folders, data sources, alerting, annotations, teams, users, service accounts,…"
hidden: true
---

# Grafana Cloud

Grafana Cloud connector for the Grafana instance HTTP API — manage dashboards, folders, data sources, alerting, annotations, teams, users, service accounts, library elements, playlists, and snapshots on a Grafana Cloud stack.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [grafana.com](https://grafana.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 72 |
| **Events** | 0 |
| **Slug** | `grafanaCloud` |

## Use it

Add Grafana Cloud from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.grafanaCloud.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Datasource Health | `checkDatasourceHealth` | Run the datasource plugin's own health check against a datasource and report whether Grafana can reach and query it. Use this to diagnose broken dashboards and alert rules. Requires the datasources:query permission. |
| Create Alert Rule | `createAlertRule` | Create a new Grafana-managed alert rule in a folder and evaluation group. The data array carries the queries and server-side expressions, and condition names the RefId whose result decides the alert state. Requires the alert.provisioning:write permission. |
| Create Annotation | `createAnnotation` | Create an annotation. Attach it to a dashboard/panel via dashboardUID and panelId, or create an organization-wide annotation. Requires annotations:create. |
| Create Contact Point | `createContactPoint` | Create a Grafana-managed alerting contact point integration that notification policies can route alerts to. Requires the alert.provisioning:write permission. |
| Create Data Source | `createDatasource` | Create a new data source. Requires a name, type, and access mode; connection details vary by type. Requires datasources:create. |
| Create Folder | `createFolder` | Create a new dashboard folder. Requires a title; a UID and parent folder UID are optional. Requires the folders:create permission. |
| Create Or Update Dashboard | `createOrUpdateDashboard` | Create a new dashboard or update an existing one. The dashboard object holds the full panel model; set overwrite to true to update an existing dashboard by UID. Requires dashboards:create or dashboards:write. |
| Create Playlist | `createPlaylist` | Create a playlist that cycles through a set of dashboards at a fixed interval. Requires the playlists write permission. |
| Create Service Account | `createServiceAccount` | Create a new service account in the organization with a name and optional org role. Requires serviceaccounts:create. |
| Create Short URL | `createShortUrl` | Create a short link for a Grafana path such as a dashboard, panel or Explore query, so a long deep link can be shared compactly. Pass the path relative to the Grafana root, without a leading slash. |
| Create Silence | `createSilence` | Create a silence in the built-in Grafana Alertmanager so that notifications for alerts matching the given labels are suppressed between the start and end times. Passing an existing silence id recreates that silence with the new values. Requires the alert.silences:create permission. |
| Create Snapshot | `createSnapshot` | Create a dashboard snapshot, a point-in-time copy of a dashboard and its data that can be shared without granting access to the datasources. Returns the access key and the delete key. Requires the snapshots:create permission. |
| Create Team | `createTeam` | Create a new team in the organization. Requires a name; email is optional. Requires teams:create. |
| Delete Alert Rule | `deleteAlertRule` | Permanently delete a Grafana-managed alert rule by its UID. Rules whose provenance is set by file provisioning cannot be deleted through the API. Requires the alert.provisioning:write permission. |
| Delete Annotation | `deleteAnnotation` | Permanently delete an annotation by its numeric identifier. Requires the annotations:delete permission. |
| Delete Contact Point | `deleteContactPoint` | Delete a Grafana-managed alerting contact point integration by its UID. The call is rejected if a notification policy still routes to it. Requires the alert.provisioning:write permission. |
| Delete Dashboard | `deleteDashboard` | Delete a dashboard by its UID. The dashboard is moved to the Recently deleted list where the instance retention policy applies. Requires dashboards:delete. |
| Delete Datasource | `deleteDatasource` | Permanently delete a datasource identified by its UID. Datasources provisioned from a file are read only and reject this call. Dashboards and alert rules that query the deleted datasource will stop returning data, so confirm nothing depends on it first. Requires the datasources:delete permission. |
| Delete Folder | `deleteFolder` | Delete a folder and all dashboards it contains by UID. Requires folders:delete. |
| Delete Playlist | `deletePlaylist` | Delete a playlist by its UID, removing it and all of its dashboard items from the organization. Requires the playlists write permission. |
| Delete Silence | `deleteSilence` | Expire a silence in the built-in Grafana Alertmanager so that notifications for the matching alerts resume immediately. Requires the alert.silences:write permission. |
| Delete Snapshot | `deleteSnapshot` | Permanently delete a dashboard snapshot by its access key. The underlying dashboard is not affected. Requires the snapshots:delete permission. |
| Get Alert Rule | `getAlertRule` | Retrieve a single Grafana-managed alert rule by its UID, including its query model, condition, evaluation interval and notification settings. Requires the alert.provisioning:read permission. |
| Get Annotation Tags | `getAnnotationTags` | List the tags used on annotations in this organization, with how many annotations carry each tag. Use it to discover the tag vocabulary before filtering annotations. Requires the annotations:read permission. |
| Get Current Organization | `getCurrentOrg` | Get details of the current organization for the authenticated Grafana instance. |
| Get Current User | `getCurrentUser` | Get the profile of the currently authenticated user or service account. |
| Get Dashboard By UID | `getDashboardByUid` | Get a dashboard by its UID. Uses the Grafana App Platform API (/apis/dashboard.grafana.app/v2beta1/namespaces/default/dashboards/{uid}). The legacy /api/dashboards/uid/{uid} endpoint was retired in Grafana 12 and now returns 406 "dashboard api version not supported". Returns the full dashboard resource: metadata (name, uid, resourceVersion, folder annotation) and spec (panels/elements, layout, variables, time settings, annotations). |
| Get Dashboard Resource | `getDashboardResource` | Read a dashboard through the Grafana App Platform resource API, which returns the dashboard in its stored schema version. Use this when Get Dashboard By UID answers 406 'dashboard api version not supported', which happens for dashboards saved in the v2 schema on Grafana 12 and later. |
| Get Dashboard Tags | `getDashboardTags` | Return all dashboard tags in the organization along with the count of dashboards using each tag. |
| Get Datasource By Name | `getDatasourceByName` | Retrieve a single datasource by its display name. Use this when only the name shown in the Grafana UI is known; prefer Get Datasource By UID for stable references. Requires the datasources:read permission. |
| Get Datasource By UID | `getDatasourceByUid` | Retrieve a single datasource by its UID, including its type, URL, access mode and type-specific JSON settings. Secure fields are never returned. Requires the datasources:read permission. |
| Get Folder By UID | `getFolderByUid` | Get a single folder by its UID, including title, parent folder, and version. Requires folders:read on the folder. |
| Get Frontend Settings | `getFrontendSettings` | Return the Grafana frontend configuration, including the list of configured data sources, the default data source, build info, and feature toggles. |
| Get Health | `getHealth` | Return the health and version information of the Grafana instance, including database status and build version. |
| Get Home Dashboard | `getHomeDashboard` | Return the organization or user home dashboard definition, or a redirect URI when the home dashboard is an app page. |
| Get Notification Policy Tree | `getNotificationPolicyTree` | Retrieve the Grafana-managed alerting notification policy tree, which routes firing alerts to contact points by label matchers. Requires the alert.provisioning:read permission. |
| Get Plugin | `getPlugin` | Retrieve the settings and metadata of a single installed plugin, including its version, whether it is enabled, and the pages it contributes. Returns 404 when the plugin is not installed, which is how you check installation. Requires the plugins:write permission or a signed-in user. |
| Get Silence | `getSilence` | Retrieve a single alert silence from the built-in Grafana Alertmanager by its identifier, including its matchers, window and current state. Requires the alert.silences:read permission. |
| Get Snapshot | `getSnapshot` | Retrieve a dashboard snapshot by its access key, returning the frozen dashboard model and its metadata. Requires the snapshots:read permission. |
| Install Plugin | `installPlugin` | Install a plugin from the Grafana plugin catalogue onto this instance, optionally pinning a specific version. Installing a plugin changes the running instance, so restrict this to a Grafana admin. Requires the plugins:install permission. |
| List Alert Rules | `listAlertRules` | List all provisioned Grafana-managed alert rules. Requires the alert.provisioning:read permission. |
| List Annotations | `listAnnotations` | List annotations, optionally filtered by time range, dashboard, panel, tags, and type. Requires the annotations:read permission. |
| List Contact Points | `listContactPoints` | List the Grafana-managed alerting contact points, optionally filtered by name. Each entry gives the integration type and its settings, with secure fields redacted. Requires the alert.provisioning:read permission. |
| List Data Sources | `listDatasources` | List all data sources configured in the organization. Requires the datasources:read permission. |
| List Folders | `listFolders` | List all folders the authenticated user has access to. Supports pagination via limit and page query parameters. |
| List Library Elements | `listLibraryElements` | List reusable library elements (library panels and variables) with optional search and pagination. Requires the library.panels:read permission. |
| List Loki Label Names | `listLokiLabelNames` | List the label names present in a Loki datasource for a time window, through the Grafana datasource proxy. Use it to discover which stream selectors are available before writing a LogQL query. Requires the datasources:query permission. |
| List Loki Label Values | `listLokiLabelValues` | List the values a given label takes in a Loki datasource for a time window, through the Grafana datasource proxy. Requires the datasources:query permission. |
| List Playlists | `listPlaylists` | List all playlists in the organization. Optionally filter by query text and limit the number of results. |
| List Plugins | `listPlugins` | List the plugins installed on this Grafana instance, optionally narrowed to a plugin type or excluding core and embedded plugins. Use it to discover which panel, datasource and app plugins are available. Requires the plugins:write permission or a signed-in user. |
| List Prometheus Label Names | `listPrometheusLabelNames` | List the label names present in a Prometheus-compatible datasource, optionally restricted to a time window or to the series matching a selector. Use it to discover what you can group or filter by. Requires the datasources:query permission. |
| List Prometheus Label Values | `listPrometheusLabelValues` | List the values a given label takes in a Prometheus-compatible datasource, optionally restricted to a time window or to the series matching a selector. Requires the datasources:query permission. |
| List Prometheus Metric Metadata | `listPrometheusMetricMetadata` | Retrieve the type, unit and help text a Prometheus-compatible datasource holds for its metrics, either for one named metric or across the catalogue. Use it to understand what a metric measures before querying it. Requires the datasources:query permission. |
| List Prometheus Metric Names | `listPrometheusMetricNames` | List the metric names available in a Prometheus-compatible datasource. This reads the values of the reserved __name__ label, so the result is the metric catalogue for the requested window. Requires the datasources:query permission. |
| List Provisioning Repositories | `listProvisioningRepositories` | List the Git Sync provisioning repositories configured on this Grafana instance, returning each repository's slug, type and sync status. Use the slug to reference a repository in other provisioning calls. Requires Grafana 11.5 or later with the provisioning app enabled. |
| List Silences | `listSilences` | List the alert silences held by the built-in Grafana Alertmanager, optionally narrowed by label matchers. A silence suppresses notifications for alerts whose labels match it. Requires the alert.silences:read permission. |
| List Snapshots | `listSnapshots` | List dashboard snapshots in the organization. Requires the snapshots:read permission. |
| List Users | `listUsers` | List the users in the current Grafana organization. Uses the Organization HTTP API (/api/org/users), which is the endpoint Grafana documents for service-account tokens; the server-admin /api/users endpoint is not reachable by any Grafana Cloud credential. |
| Query Loki Logs | `queryLokiLogs` | Run a LogQL query against a Loki datasource over a time window through the Grafana datasource proxy, returning matching log lines or, for a metric query, the computed series. Always set a stream selector and a limit, since unbounded queries are rejected. Requires the datasources:query permission. |
| Query Loki Patterns | `queryLokiPatterns` | Retrieve the automatically detected log patterns for the streams matching a selector in a Loki datasource, with how often each pattern occurred over the window. Use it to summarise high-volume logs without reading every line. Requires Loki pattern ingestion to be enabled on the backend. |
| Query Loki Stats | `queryLokiStats` | Retrieve index-level statistics for the log streams matching a label selector in a Loki datasource: how many streams, chunks, index entries and bytes they cover. Use it to size a query before running it. The selector must be a plain label matcher, with no line filters or aggregations. |
| Query Prometheus | `queryPrometheus` | Run an instant PromQL query against a Prometheus-compatible datasource through the Grafana datasource proxy, returning the value of each matching series at a single point in time. Use Query Prometheus Range for a time series over a window. Requires the datasources:query permission. |
| Query Prometheus Range | `queryPrometheusRange` | Run a PromQL range query against a Prometheus-compatible datasource through the Grafana datasource proxy, returning a time series for each matching label set at a fixed step. This is also the endpoint used for histogram quantile queries such as histogram_quantile(0.95, sum by (le) (rate(bucket[5m]))). Requires the datasources:query permission. |
| Search Dashboards And Folders | `search` | Search across dashboards and folders. Filter by query text, type (dash-db or dash-folder), tags, starred state, and folder UIDs. |
| Search Service Accounts | `searchServiceAccounts` | Search service accounts in the organization with optional query and pagination. Requires the serviceaccounts:read permission. |
| Search Teams | `searchTeams` | Search teams in the organization with optional name query and pagination. Requires the teams:read permission. |
| Update Alert Rule | `updateAlertRule` | Replace an existing Grafana-managed alert rule identified by its UID. The request body is the complete rule, so send every field you want to keep. Requires the alert.provisioning:write permission. |
| Update Annotation | `updateAnnotation` | Replace an existing annotation by its numeric identifier, changing its text, tags or time range. Fields that are omitted are cleared, so send the complete annotation. Requires the annotations:write permission. |
| Update Contact Point | `updateContactPoint` | Replace an existing Grafana-managed alerting contact point integration identified by its UID. Send the complete integration, as omitted fields are not preserved. Requires the alert.provisioning:write permission. |
| Update Datasource | `updateDatasource` | Update an existing datasource identified by its UID. Datasources provisioned from a file are read only and reject this call. Requires the datasources:write permission. |
| Update Folder | `updateFolder` | Update a folder's title. Provide the current version, or set overwrite to true to bypass optimistic locking. Requires folders:write. |
| Update Notification Policy Tree | `updateNotificationPolicyTree` | Replace the entire Grafana-managed alerting notification policy tree. This overwrites every existing route, so send the complete tree including the default receiver. Requires the alert.provisioning:write permission. |
