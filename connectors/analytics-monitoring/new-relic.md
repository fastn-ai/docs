---
description: "New Relic observability platform."
hidden: true
---

# New Relic

<img src="../../.gitbook/assets/connectors/new-relic.png" alt="New Relic logo" width="64">

New Relic observability platform. NerdGraph (GraphQL) for entities, NRQL, dashboards, alerts, workloads, tags and notifications, plus the REST API v2 for applications, alert policies, deployments, labels and key transactions.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [newrelic.com](https://newrelic.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `newRelic` |

## Use it

Add New Relic from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.newRelic.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Tags to Entity | `addTagsToEntity` | Add one or more tags to an entity via NerdGraph taggingAddTagsToEntity. Pass variables as {guid, tags:[{key, values:[...]}]}. |
| Create Alert Policy | `createAlertPolicy` | Create an alert policy via NerdGraph alertsPolicyCreate. Pass variables as {accountId, policy:{name, incidentPreference}}. incidentPreference is PER_POLICY, PER_CONDITION or PER_CONDITION_AND_TARGET. |
| Create Dashboard | `createDashboard` | Create a dashboard in an account via NerdGraph dashboardCreate. Pass variables as {accountId, dashboard} where dashboard is a DashboardInput (name, permissions, pages with widgets). Returns the new dashboard entity guid. |
| Create Deployment | `createDeployment` | Record a deployment marker for an APM application via the REST API v2. Requires a revision; changelog, description and user are optional. |
| Create Notification Destination | `createNotificationDestination` | Create a notification destination (email, webhook, Slack, etc.) via NerdGraph aiNotificationsCreateDestination. Pass variables as {accountId, destination:{name, type, properties:[{key,value}]}}. |
| Create NRQL Alert Condition | `createNrqlAlertCondition` | Create a static NRQL alert condition on a policy via NerdGraph alertsNrqlConditionStaticCreate. Pass variables as {accountId, policyId, condition} (AlertsNrqlConditionStaticInput: name, enabled, nrql, terms, signal). |
| Create Workload | `createWorkload` | Create a workload (a group of entities) via NerdGraph workloadCreate. Pass variables as {accountId, workload:{name, entityGuids?, entitySearchQueries?}}. |
| Delete Alert Condition | `deleteAlertCondition` | Delete any alert condition (NRQL or other) by id via NerdGraph alertsConditionDelete. Pass variables as {accountId, id}. |
| Delete Alert Policy | `deleteAlertPolicy` | Delete an alert policy by id via NerdGraph alertsPolicyDelete. Pass variables as {accountId, id}. Also removes the policy's conditions. |
| Delete Application | `deleteApplication` | Delete an APM application by id via the REST API v2. The application must not be reporting. |

<details>

<summary>See 32 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Dashboard | `deleteDashboard` | Delete a dashboard by its entity GUID via NerdGraph dashboardDelete. Pass variables as {guid}. |
| Delete Deployment | `deleteDeployment` | Delete a deployment marker from an APM application via the REST API v2. |
| Delete Notification Destination | `deleteNotificationDestination` | Delete a notification destination by id via NerdGraph aiNotificationsDeleteDestination. Pass variables as {accountId, destinationId}. |
| Delete Workload | `deleteWorkload` | Delete a workload by its entity GUID via NerdGraph workloadDelete. Pass variables as {guid}. |
| Get Actor Info | `getActorInfo` | Return the authenticated user together with all New Relic accounts they can access (id and name), via the NerdGraph actor field. |
| Get Application | `getApplication` | Get a single APM application by id via the REST API v2. |
| Get Application Metric Data | `getApplicationMetricData` | Get timeseries metric data for an APM application via the REST API v2. Provide the metric name (names[]) and optional from/to ISO-8601 timestamps and summarize flag. |
| Get Current User | `getCurrentUser` | Return the authenticated user's id, name and email via NerdGraph (actor.user). Use to verify the connection and identify the caller. |
| Get Dashboard | `getDashboard` | Fetch a dashboard's full definition (pages and widgets) by its entity GUID via NerdGraph. Pass variables as {guid}. |
| Get Entity | `getEntity` | Fetch a single New Relic entity by its GUID via NerdGraph. Returns core fields, reporting state and tags. Pass variables as {guid}. |
| Get Key Transaction | `getKeyTransaction` | Get a single key transaction by id via the REST API v2. |
| List Alert Conditions (REST) | `listAlertConditionsRest` | List APM/browser/mobile alert conditions for a policy via the legacy REST API v2 (alerts_conditions). Requires policy_id. |
| List Alert Policies | `listAlertPolicies` | List alert policies in an account via NerdGraph alerts.policiesSearch. Pass variables as {accountId}. |
| List Alert Policies (REST) | `listAlertPoliciesRest` | List alert policies via the legacy REST API v2 (alerts_policies). Supports filter[name] and page query params. |
| List Application Metric Names | `listApplicationMetrics` | List the available metric names for an APM application via the REST API v2. Supports the name query param to filter. |
| List Applications | `listApplications` | List APM applications in the account via the REST API v2. Supports filter[name], filter[ids], filter[language] and page query params. |
| List Dashboards | `listDashboards` | List all dashboards visible to the caller via a NerdGraph entity search for DASHBOARD entities. Returns each dashboard's guid, name, account and permalink. |
| List Deployments | `listDeployments` | List deployment markers recorded for an APM application via the REST API v2. |
| List Key Transactions | `listKeyTransactions` | List key transactions via the REST API v2. Supports filter[name] and page query params. |
| List Notification Channels | `listNotificationChannels` | List notification channels in an account via NerdGraph aiNotifications.channels. Pass variables as {accountId}. |
| List Notification Destinations | `listNotificationDestinations` | List notification destinations in an account via NerdGraph aiNotifications.destinations. Pass variables as {accountId}. |
| List NRQL Alert Conditions | `listNrqlAlertConditions` | List NRQL alert conditions in an account via NerdGraph alerts.nrqlConditionsSearch. Pass variables as {accountId}. |
| List Users | `listUsers` | List users in the account via the REST API v2. Supports filter[email], filter[ids] and page query params. |
| List Workloads | `listWorkloads` | List workloads (collections) in an account via NerdGraph workload.collections. Pass variables as {accountId}. |
| Remove Tags from Entity | `removeTagsFromEntity` | Remove tags (by key) from an entity via NerdGraph taggingDeleteTagFromEntity. Pass variables as {guid, tagKeys:[...]}. |
| Run NerdGraph Query | `runNerdGraph` | Generic NerdGraph (GraphQL) passthrough. Send any query or mutation string plus an optional variables object; returns the raw GraphQL {data, errors} envelope. Use for any NerdGraph operation not covered by a dedicated action. |
| Run NRQL Query | `runNrqlQuery` | Run a NRQL (New Relic Query Language) query against an account and return the result rows. Pass variables as {accountId, nrql}. |
| Search Entities | `searchEntities` | Search New Relic entities (applications, hosts, dashboards, workloads, etc.) using an entity search query string. Pass variables as {query: \"name LIKE 'x' AND type = 'DASHBOARD'\"}. |
| Update Alert Policy | `updateAlertPolicy` | Update an alert policy via NerdGraph alertsPolicyUpdate. Pass variables as {accountId, id, policy:{name, incidentPreference}}. |
| Update Application | `updateApplication` | Update an APM application's name and settings via the REST API v2. |
| Update Dashboard | `updateDashboard` | Replace a dashboard's definition via NerdGraph dashboardUpdate. Pass variables as {guid, dashboard} where dashboard is a full DashboardInput. Overwrites the entire dashboard. |
| Update NRQL Alert Condition | `updateNrqlAlertCondition` | Update a static NRQL alert condition via NerdGraph alertsNrqlConditionStaticUpdate. Pass variables as {accountId, id, condition} (partial AlertsNrqlConditionUpdateStaticInput). |

</details>
