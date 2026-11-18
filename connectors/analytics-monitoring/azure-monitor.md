---
description: "Azure Monitor over the Microsoft.Insights Azure Resource Manager API at https://management.azure.com."
---

# Azure Monitor

Azure Monitor over the Microsoft.Insights Azure Resource Manager API at https://management.azure.com. Read platform metrics, metric definitions and metric namespaces for any Azure resource, query subscription and tenant activity logs and event categories, and manage the alerting and collection surface - action groups, metric alert rules and their status, activity log alert rules, scheduled query (log search) alert rules, autoscale settings, diagnostic settings and diagnostic setting categories, log profiles, and data collection rules, endpoints and associations. Also runs Log Analytics KQL queries through the ARM proxy endpoint. Connect with Microsoft Entra ID OAuth 2.0; the signed-in user needs Azure RBAC rights such as Monitoring Reader or Monitoring Contributor on the target scope.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [monitor.azure.com](https://monitor.azure.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 68 |
| **Events** | 0 |
| **Slug** | `azureMonitor` |

## Use it

Add Azure Monitor from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.azureMonitor.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Action Group Test Notifications | `createActionGroupTestNotifications` | Sends a test notification through the receivers of an existing action group. The call is asynchronous and returns a notification id to poll with Get Action Group Test Notification Status. This really delivers messages to the configured recipients. |
| Create Data Collection Endpoint | `createDataCollectionEndpoint` | Creates or replaces a data collection endpoint. The service generates the ingestion and configuration URLs; the caller supplies the region, an optional description and the public network access setting. |
| Create Data Collection Rule | `createDataCollectionRule` | Creates or replaces a data collection rule. Data Sources declares what is collected (performance counters, syslog, Windows event logs, extensions, log files), Destinations declares where it goes (Log Analytics workspaces, Azure Monitor metrics, storage), and Data Flows connects named streams to destinations. |
| Create Data Collection Rule Association | `createDataCollectionRuleAssociation` | Associates a data collection rule or a data collection endpoint with an Azure resource, which is what starts collection on that resource. Supply exactly one of Data Collection Rule ID or Data Collection Endpoint ID. |
| Create or Update Action Group | `createOrUpdateActionGroup` | Creates a new action group or replaces an existing one, including its full list of email, SMS, webhook, ITSM, mobile push, runbook, voice, logic app, Azure function, ARM role and event hub receivers. Action groups are global resources, so Location is normally "Global". |
| Create or Update Activity Log Alert | `createOrUpdateActivityLogAlert` | Creates a new activity log alert rule or replaces an existing one. Activity log alert rules are global resources, so Location is normally "global". The condition is an allOf list of field comparisons over activity log event properties such as category, level, operationName and resourceGroup. |
| Create or Update Autoscale Setting | `createOrUpdateAutoscaleSetting` | Creates a new autoscale setting or replaces an existing one. Each profile defines an instance-count range and a set of rules that pair a metric trigger with a scale action; profiles may also carry a fixed date window or a weekly recurrence. |
| Create or Update Diagnostic Setting | `createOrUpdateDiagnosticSetting` | Creates or replaces a diagnostic setting on an Azure resource, routing selected log and metric categories to a Log Analytics workspace, storage account, event hub or marketplace partner. At least one destination must be supplied. |
| Create or Update Metric Alert | `createOrUpdateMetricAlert` | Creates a new metric alert rule or replaces an existing one. Metric alert rules are global resources, so Location is normally "global". The Criteria object is a discriminated union selected by its odata.type field; see the Azure Monitor metric alerts reference for the shape of each variant. |
| Create or Update Scheduled Query Rule | `createOrUpdateScheduledQueryRule` | Creates a new scheduled query (log search) alert rule or replaces an existing one. Each condition in the criteria carries the Kusto query, the metric measure, the operator and threshold, and how many evaluation periods must fail before the alert fires. |
| Delete Action Group | `deleteActionGroup` | Deletes an action group. Alert rules that still reference it will no longer notify anyone. |
| Delete Activity Log Alert | `deleteActivityLogAlert` | Deletes an activity log alert rule. |
| Delete Autoscale Setting | `deleteAutoscaleSetting` | Deletes an autoscale setting. The target resource keeps its current instance count but stops scaling automatically. |
| Delete Data Collection Endpoint | `deleteDataCollectionEndpoint` | Deletes a data collection endpoint. Rules and associations that reference it stop ingesting. |
| Delete Data Collection Rule | `deleteDataCollectionRule` | Deletes a data collection rule. Delete its associations first, or the call is rejected. |
| Delete Data Collection Rule Association | `deleteDataCollectionRuleAssociation` | Removes a data collection rule association from an Azure resource, stopping collection on that resource without deleting the rule itself. |
| Delete Diagnostic Setting | `deleteDiagnosticSetting` | Deletes a named diagnostic setting from an Azure resource, stopping the export of its logs and metrics to that destination. |
| Delete Metric Alert | `deleteMetricAlert` | Deletes a metric alert rule. |
| Delete Scheduled Query Rule | `deleteScheduledQueryRule` | Deletes a scheduled query (log search) alert rule. |
| Enable Action Group Receiver | `enableActionGroupReceiver` | Re-enables a receiver in an action group that was disabled because the recipient unsubscribed. Applies only to SMS, voice and Azure mobile app push receivers. |
| Get Action Group | `getActionGroup` | Gets a single action group with all of its configured receivers. |
| Get Action Group Test Notification Status | `getActionGroupTestNotificationStatus` | Gets the delivery status of a test notification previously started with Create Action Group Test Notifications, broken down per receiver. |
| Get Activity Log Alert | `getActivityLogAlert` | Gets a single activity log alert rule, including the condition it matches and the action groups it fires into. |
| Get Autoscale Setting | `getAutoscaleSetting` | Gets a single autoscale setting with its full profile, rule and notification configuration. |
| Get Data Collection Endpoint | `getDataCollectionEndpoint` | Gets a single data collection endpoint, including the logs ingestion and configuration access URLs that clients post to. |
| Get Data Collection Rule | `getDataCollectionRule` | Gets a single data collection rule with its data sources, destinations, stream declarations and data flows. |
| Get Data Collection Rule Association | `getDataCollectionRuleAssociation` | Gets a single named data collection rule association on an Azure resource. |
| Get Diagnostic Setting | `getDiagnosticSetting` | Gets a single named diagnostic setting on an Azure resource, including its destinations and the log and metric categories it routes. |
| Get Metric Alert | `getMetricAlert` | Gets a single metric alert rule, including its full criteria definition and the action groups it fires into. |
| Get Metric Alert Status by Name | `getMetricAlertStatusByName` | Gets the firing status of a metric alert rule for one named dimension combination, as returned by List Metric Alert Status. |
| Get Predictive Metric | `getPredictiveMetric` | Gets the predictive autoscale forecast for an autoscale setting over a time range, so you can compare the predicted metric against the actual one before enabling predictive scaling. |
| Get Scheduled Query Rule | `getScheduledQueryRule` | Gets a single scheduled query (log search) alert rule, including its query, threshold criteria, schedule and actions. |
| List Action Groups by Resource Group | `listActionGroupsByResourceGroup` | Lists the action groups in a single resource group. |
| List Action Groups by Subscription | `listActionGroupsBySubscription` | Lists every action group in a subscription. An action group is the reusable set of notification and automation receivers that alert rules fire into. |
| List Activity Log Alerts by Resource Group | `listActivityLogAlertsByResourceGroup` | Lists the activity log alert rules in a single resource group. |
| List Activity Log Alerts by Subscription | `listActivityLogAlertsBySubscription` | Lists every activity log alert rule in a subscription. These rules fire on control-plane events rather than metric thresholds. |
| List Activity Logs | `listActivityLogs` | Lists control-plane activity log events for a subscription. A filter over eventTimestamp is required and must span no more than 90 days, for example "eventTimestamp ge '2026-01-01T00:00:00Z' and eventTimestamp le '2026-01-08T00:00:00Z'". |
| List Autoscale Settings by Resource Group | `listAutoscaleSettingsByResourceGroup` | Lists the autoscale settings in a single resource group. |
| List Autoscale Settings by Subscription | `listAutoscaleSettingsBySubscription` | Lists every autoscale setting in a subscription. An autoscale setting drives instance counts of a scalable resource from metric rules and schedules. |
| List Data Collection Endpoints by Resource Group | `listDataCollectionEndpointsByResourceGroup` | Lists the data collection endpoints in a single resource group. |
| List Data Collection Endpoints by Subscription | `listDataCollectionEndpointsBySubscription` | Lists every data collection endpoint in a subscription. A data collection endpoint provides the ingestion and configuration URLs agents and custom log senders connect to. |
| List Data Collection Rule Associations by Endpoint | `listDataCollectionRuleAssociationsByEndpoint` | Lists every association of a single data collection endpoint, showing which resources use that endpoint for ingestion. |
| List Data Collection Rule Associations by Resource | `listDataCollectionRuleAssociationsByResource` | Lists the data collection rule associations attached to a single Azure resource, such as a virtual machine or Arc-enabled server. An association is what actually applies a rule to a machine. |
| List Data Collection Rule Associations by Rule | `listDataCollectionRuleAssociationsByRule` | Lists every association of a single data collection rule, which is how you discover the resources the rule is applied to. |
| List Data Collection Rules by Resource Group | `listDataCollectionRulesByResourceGroup` | Lists the data collection rules in a single resource group. |
| List Data Collection Rules by Subscription | `listDataCollectionRulesBySubscription` | Lists every data collection rule in a subscription. A data collection rule defines what the Azure Monitor agent collects and where it sends it. |
| List Diagnostic Settings | `listDiagnosticSettings` | Lists the diagnostic settings on an Azure resource. A diagnostic setting routes the resource's platform logs and metrics to a Log Analytics workspace, storage account, event hub or partner destination. |
| List Event Categories | `listEventCategories` | Lists the activity log event categories supported by Azure Monitor, such as Administrative, Security, ServiceHealth, Alert, Recommendation, Policy and Autoscale. Use the returned values in activity log filters. |
| List Metric Alert Status | `listMetricAlertStatus` | Lists the current firing status of a metric alert rule, one entry per monitored dimension combination. |
| List Metric Alerts by Resource Group | `listMetricAlertsByResourceGroup` | Lists the metric alert rules in a single resource group. |
| List Metric Alerts by Subscription | `listMetricAlertsBySubscription` | Lists every metric alert rule in a subscription, with its scopes, criteria, evaluation frequency and actions. |
| List Metric Definitions | `listMetricDefinitions` | Lists the metric definitions available for a single Azure resource, including each metric's unit, supported aggregations, time grains and dimensions. Use it to discover the metric names accepted by List Metrics. |
| List Metric Definitions at Subscription Scope | `listMetricDefinitionsAtSubscriptionScope` | Lists the metric definitions available in one region of a subscription for a given metric namespace, rather than for a single resource. |
| List Metric Namespaces | `listMetricNamespaces` | Lists the metric namespaces available for a single Azure resource, including custom namespaces emitted by the resource. Use it to discover the value to pass as Metric Namespace on the metric actions. |
| List Metrics | `listMetrics` | Reads platform metric values for a single Azure resource over a time range. The resource is addressed by its subscription, resource group, provider namespace, resource type and name, which together form the resource URI. Requires the Monitoring Reader role or equivalent on the resource. |
| List Metrics at Subscription Scope | `listMetricsAtSubscriptionScope` | Reads platform metric values across every resource of a given metric namespace in one region of a subscription, rather than for a single resource. Region and Metric Namespace are both required by the service. |
| List Monitor Operations | `listMonitorOperations` | Lists all Azure Resource Manager operations exposed by the Microsoft.Insights provider, with their display names and descriptions. Useful for discovering the RBAC actions Azure Monitor defines. |
| List Scheduled Query Rules by Resource Group | `listScheduledQueryRulesByResourceGroup` | Lists the scheduled query (log search) alert rules in a single resource group. |
| List Scheduled Query Rules by Subscription | `listScheduledQueryRulesBySubscription` | Lists every scheduled query (log search) alert rule in a subscription. These rules run a Kusto query on a schedule and alert on its result. |
| List Tenant Activity Logs | `listTenantActivityLogs` | Lists activity log events across the whole tenant rather than a single subscription. Everything the caller can see is returned; a filter over eventTimestamp is strongly recommended because the tenant log is large. |
| Run Log Analytics Query | `runLogAnalyticsQuery` | Runs a Kusto (KQL) query against a Log Analytics workspace through the Azure Resource Manager proxy endpoint, so the same Entra token used for the rest of this connector applies. Returns tables of columns and rows. |
| Update Action Group | `updateActionGroup` | Updates only the tags and enabled state of an existing action group. Use Create or Update Action Group to change its receivers. |
| Update Activity Log Alert | `updateActivityLogAlert` | Updates the tags or enabled state of an existing activity log alert rule. Use Create or Update Activity Log Alert to change its condition or actions. |
| Update Autoscale Setting | `updateAutoscaleSetting` | Updates the tags or selected properties of an existing autoscale setting without replacing the whole resource. |
| Update Data Collection Endpoint | `updateDataCollectionEndpoint` | Updates the tags of an existing data collection endpoint. |
| Update Data Collection Rule | `updateDataCollectionRule` | Updates the tags of an existing data collection rule. Use Create Data Collection Rule to change its data sources, destinations or data flows. |
| Update Metric Alert | `updateMetricAlert` | Updates the tags or selected properties of an existing metric alert rule without replacing the whole resource. |
| Update Scheduled Query Rule | `updateScheduledQueryRule` | Updates the tags or selected properties of an existing scheduled query alert rule without replacing the whole resource. |
