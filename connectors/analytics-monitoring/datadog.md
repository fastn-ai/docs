---
description: "Datadog monitoring and observability platform."
hidden: true
---

# Datadog

<img src="../../.gitbook/assets/connectors/lg/datadog.png" alt="Datadog logo">

Datadog monitoring and observability platform. Manage dashboards, monitors, downtimes, events, metrics, hosts, SLOs, tags, users, roles, notebooks, synthetics, and incidents via the Datadog v1 and v2 REST APIs.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [datadoghq.com](https://datadoghq.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `datadog` |

## Use it

Add Datadog from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.datadog.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Host Tags | `addHostTags` | Adds tags to a host by name (v1). The host must be known to Datadog. |
| Cancel Downtime | `cancelDowntime` | Cancels a scheduled downtime by its ID (v2). Returns an empty body on success. |
| Create Dashboard | `createDashboard` | Creates a new dashboard in Datadog with the given title, layout type, and widgets. |
| Create Downtime | `createDowntime` | Schedules a new downtime (v2) that mutes monitor notifications for the given scope. |
| Create Incident | `createIncident` | Creates a new incident with a title and customer-impact flag (v2). Requires Incident Management. |
| Create Metric Tag Configuration | `createMetricTagConfiguration` | Creates a tag configuration for a custom metric, defining which tag keys are queryable and the metric type (v2). |
| Create Monitor | `createMonitor` | Creates a new monitor of the given type with a query, name, and notification message. |
| Create Notebook | `createNotebook` | Creates a new notebook with the given name, cells, and global time settings (v1). |
| Create SLO | `createSLO` | Creates a Service Level Objective (SLO). For monitor SLOs provide monitor_ids; for metric SLOs provide query with numerator and denominator (v1). |
| Create Synthetic API Test | `createSyntheticApiTest` | Creates a new Synthetic API test with a request config, assertions, locations, and options (v1). |

<details>

<summary>See 56 more actions</summary>

* **Create User** `createUser`: Creates (invites) a new user in the organization by email (v2).
* **Delete Dashboard** `deleteDashboard`: Deletes a dashboard by its ID.
* **Delete Incident** `deleteIncident`: Deletes an incident by its ID (v2). Requires Incident Management.
* **Delete Metric Tag Configuration** `deleteMetricTagConfiguration`: Deletes the tag configuration for a custom metric (v2). Returns an empty body on success.
* **Delete Monitor** `deleteMonitor`: Deletes a monitor by its numeric ID.
* **Delete Notebook** `deleteNotebook`: Deletes a notebook by its numeric ID (v1). Returns an empty body on success.
* **Delete SLO** `deleteSLO`: Deletes a Service Level Objective by its ID (v1).
* **Delete Synthetic Tests** `deleteSyntheticTests`: Deletes one or more Synthetic tests by their public IDs (v1).
* **Disable User** `disableUser`: Disables a user by their ID (v2). Returns an empty body on success.
* **Get Dashboard** `getDashboard`: Retrieves a single dashboard by its ID, including all widgets and configuration.
* **Get Downtime** `getDowntime`: Retrieves a single scheduled downtime by its ID (v2).
* **Get Event** `getEvent`: Retrieves a single event from the event stream by its numeric ID (v1).
* **Get Host Tags** `getHostTags`: Returns the tags applied to a single host by name (v1).
* **Get Host Totals** `getHostTotals`: Returns the total number of active and up hosts reporting to Datadog (v1).
* **Get Incident** `getIncident`: Retrieves a single incident by its ID (v2). Requires Incident Management.
* **Get Metric Metadata** `getMetricMetadata`: Retrieves the metadata (type, description, unit) for a metric by name (v1).
* **Get Metric Tag Configuration** `getMetricTagConfiguration`: Retrieves the tag configuration for a metric name (v2). Returns 404 if no tag configuration is defined for the metric.
* **Get Monitor** `getMonitor`: Retrieves the details of a single monitor by its numeric ID.
* **Get Notebook** `getNotebook`: Retrieves a single notebook by its numeric ID (v1).
* **Get Role** `getRole`: Retrieves a single role by its ID, including its permissions (v2).
* **Get SLO** `getSLO`: Retrieves a single Service Level Objective by its ID (v1).
* **Get Synthetic Test** `getSyntheticTest`: Retrieves the details of a single Synthetic test by its public ID (v1).
* **Get User** `getUser`: Retrieves a single user by their ID (v2).
* **List Active Metrics** `listActiveMetrics`: Lists metrics that have been actively reporting since a given time (v1).
* **List Dashboards** `listDashboards`: Retrieves a list of all dashboards in the Datadog organization.
* **List Downtimes** `listDowntimes`: Retrieves all scheduled downtimes (v2). Optionally include current-only downtimes.
* **List Events** `listEvents`: Retrieves events from the event stream within a time window (v1).
* **List Host Tags** `listHostTags`: Returns a mapping of tags to the hosts that carry them (v1).
* **List Hosts** `listHosts`: Retrieves all hosts reporting to Datadog, with optional filtering and pagination (v1).
* **List Incidents** `listIncidents`: Retrieves a list of incidents (v2). Requires the Incident Management feature to be enabled on the account.
* **List Metric Tags** `listMetricTags`: Lists all indexed tag key-values for a metric name (v2 all-tags).
* **List Monitors** `listMonitors`: Retrieves all monitors, optionally filtered by name, tags, or monitor tags.
* **List Notebooks** `listNotebooks`: Retrieves a list of notebooks, with optional filtering and pagination (v1).
* **List Roles** `listRoles`: Retrieves all roles in the organization, with optional filtering and pagination (v2).
* **List SLOs** `listSLOs`: Retrieves a list of Service Level Objectives (SLOs), with optional query and pagination (v1).
* **List Synthetic Tests** `listSyntheticTests`: Retrieves the list of all Synthetic tests (API and browser) in the organization (v1).
* **List Users** `listUsers`: Retrieves all users in the organization, with optional filtering, sorting, and pagination (v2).
* **Mute Host** `muteHost`: Mutes all monitors for a host by name (v1), optionally with an end time and message.
* **Mute Monitor** `muteMonitor`: Mutes a monitor by its ID, optionally scoped and with an end time.
* **Post Event** `postEvent`: Posts an event to the Datadog event stream (v1) with a title and text body.
* **Query Timeseries Points** `queryMetrics`: Queries timeseries points for a metric over a time window (v1 metrics query).
* **Remove Host Tags** `removeHostTags`: Removes all user-source tags from a host by name (v1).
* **Search Events** `searchEventsV2`: Searches the event stream using the v2 Events API with an optional query filter and time window.
* **Search Monitors** `searchMonitors`: Searches monitors using a monitor search query, with pagination and sorting.
* **Submit Metrics** `submitMetrics`: Submits one or more metric timeseries points to Datadog (v1 series intake). Each series item has a metric name, points, type, and optional host and tags.
* **Unmute Host** `unmuteHost`: Unmutes all monitors for a host by name (v1).
* **Unmute Monitor** `unmuteMonitor`: Unmutes a monitor by its ID, optionally for a specific scope or all scopes.
* **Update Dashboard** `updateDashboard`: Updates an existing dashboard by its ID. The full dashboard definition (title, layout type, widgets) must be supplied.
* **Update Downtime** `updateDowntime`: Updates a scheduled downtime by its ID (v2), such as changing its message or scope.
* **Update Host Tags** `updateHostTags`: Replaces all user-source tags on a host by name (v1).
* **Update Monitor** `updateMonitor`: Updates an existing monitor by its ID. Only the fields provided are changed.
* **Update Notebook** `updateNotebook`: Updates a notebook by its ID (v1). The full notebook definition (name, cells, time) must be provided.
* **Update SLO** `updateSLO`: Updates a Service Level Objective by its ID (v1). The full SLO definition must be provided as this is a replacing update.
* **Update User** `updateUser`: Updates a user's name by their ID (v2).
* **Validate API Key** `validateApiKey`: Validates that the configured Datadog API key is valid. Returns {valid:true} on success.
* **Validate Monitor** `validateMonitor`: Validates a monitor definition without creating it. Returns 200 with an empty body if the definition is valid.

</details>
