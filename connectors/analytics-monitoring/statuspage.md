---
description: "Atlassian Statuspage REST API v1."
hidden: true
---

# Statuspage

<img src="../../.gitbook/assets/connectors/lg/statuspage.png" alt="Statuspage logo">

Atlassian Statuspage REST API v1. Manage status pages, components and component groups, incidents and incident updates, postmortems, scheduled maintenance, uptime reporting, custom metrics and metrics providers, page and incident subscribers, audience-specific page access users and groups, the status embed widget, and organization users and permissions. Single host https://api.statuspage.io/v1 with API key authentication sent as an Authorization: OAuth header.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [statuspage.io](https://statuspage.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `statuspage` |

## Use it

Add Statuspage from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.statuspage.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Components To Page Access Group | `addComponentsToPageAccessGroup` | Add components to page access group. Scoped to the Statuspage status page given by the Page ID input. |
| Add Components To Page Access User | `addComponentsToPageAccessUser` | Add components for page access user. Scoped to the Statuspage status page given by the Page ID input. |
| Add Data Point To Metric | `addDataPointToMetric` | Add data to a metric. Scoped to the Statuspage status page given by the Page ID input. |
| Add Data Points To Metrics | `addDataPointsToMetrics` | Append data points to several self-reported metrics in one call. The request and the response are both maps keyed by metric ID: each key is the ID of a self-reported metric and each value is an array of {timestamp, value} points, for example {"gmwtxqyy34n5": [{"timestamp": 1590603000, "value": 1.23}]}. Statuspage answers 202 Accepted and echoes the accepted points back in the same map shape. Scoped to the Statuspage status page given by the Page ID input. |
| Add Metrics To Page Access User | `addMetricsToPageAccessUser` | Add metrics for page access user. Scoped to the Statuspage status page given by the Page ID input. |
| Add Page Access Groups To Component | `addPageAccessGroupsToComponent` | Add page access groups to a component. Scoped to the Statuspage status page given by the Page ID input. |
| Add Page Access Users To Component | `addPageAccessUsersToComponent` | Add page access users to a component. Scoped to the Statuspage status page given by the Page ID input. |
| Create Component | `createComponent` | Create a component. Scoped to the Statuspage status page given by the Page ID input. |
| Create Component Group | `createComponentGroup` | Create a component group. Scoped to the Statuspage status page given by the Page ID input. |
| Create Incident | `createIncident` | Create an incident. Scoped to the Statuspage status page given by the Page ID input. |

<details>

<summary>See 89 more actions</summary>

* **Create Incident Subscriber** `createIncidentSubscriber`: Create an incident subscriber. Scoped to the Statuspage status page given by the Page ID input.
* **Create Incident Template** `createIncidentTemplate`: Create a template. Scoped to the Statuspage status page given by the Page ID input.
* **Create Metric For Metrics Provider** `createMetricForMetricsProvider`: Create a metric for a metric provider. Scoped to the Statuspage status page given by the Page ID input.
* **Create Metrics Provider** `createMetricsProvider`: Create a metric provider. Scoped to the Statuspage status page given by the Page ID input.
* **Create Or Update Postmortem** `createOrUpdatePostmortem`: Create Postmortem. Scoped to the Statuspage status page given by the Page ID input.
* **Create Organization User** `createOrganizationUser`: Create a user. Scoped to the Statuspage organization given by the Organization ID input.
* **Create Page Access Group** `createPageAccessGroup`: Create a page access group. Scoped to the Statuspage status page given by the Page ID input.
* **Create Page Access User** `createPageAccessUser`: Add a page access user. Scoped to the Statuspage status page given by the Page ID input.
* **Create Subscriber** `createSubscriber`: Create a subscriber. Not applicable for Slack subscribers. Scoped to the Statuspage status page given by the Page ID input.
* **Delete Component** `deleteComponent`: Delete a component. Scoped to the Statuspage status page given by the Page ID input.
* **Delete Component Group** `deleteComponentGroup`: Delete a component group. Scoped to the Statuspage status page given by the Page ID input.
* **Delete Incident** `deleteIncident`: Delete an incident. Scoped to the Statuspage status page given by the Page ID input.
* **Delete Metric** `deleteMetric`: Delete a metric. Scoped to the Statuspage status page given by the Page ID input.
* **Delete Metrics Provider** `deleteMetricsProvider`: Delete a metric provider. Scoped to the Statuspage status page given by the Page ID input.
* **Delete Organization User** `deleteOrganizationUser`: Delete a user. Scoped to the Statuspage organization given by the Organization ID input.
* **Delete Page Access Group** `deletePageAccessGroup`: Remove a page access group. Scoped to the Statuspage status page given by the Page ID input.
* **Delete Page Access User** `deletePageAccessUser`: Delete page access user. Scoped to the Statuspage status page given by the Page ID input.
* **Delete Postmortem** `deletePostmortem`: Delete Postmortem. Scoped to the Statuspage status page given by the Page ID input.
* **Get Component** `getComponent`: Get a component. Scoped to the Statuspage status page given by the Page ID input.
* **Get Component Group** `getComponentGroup`: Get a component group. Scoped to the Statuspage status page given by the Page ID input.
* **Get Component Group Uptime** `getComponentGroupUptime`: Get uptime data for a component group that has uptime showcase enabled for at least one component. Scoped to the Statuspage status page given by the Page ID input.
* **Get Component Uptime** `getComponentUptime`: Get uptime data for a component that has uptime showcase enabled. Scoped to the Statuspage status page given by the Page ID input.
* **Get Incident** `getIncident`: Get an incident. Scoped to the Statuspage status page given by the Page ID input.
* **Get Incident Subscriber** `getIncidentSubscriber`: Get an incident subscriber. Scoped to the Statuspage status page given by the Page ID input.
* **Get Metric** `getMetric`: Get a metric. Scoped to the Statuspage status page given by the Page ID input.
* **Get Metrics Provider** `getMetricsProvider`: Get a metric provider. Scoped to the Statuspage status page given by the Page ID input.
* **Get Page** `getPage`: Get a page. Scoped to the Statuspage status page given by the Page ID input.
* **Get Page Access Group** `getPageAccessGroup`: Get a page access group. Scoped to the Statuspage status page given by the Page ID input.
* **Get Page Access User** `getPageAccessUser`: Get page access user. Scoped to the Statuspage status page given by the Page ID input.
* **Get Postmortem** `getPostmortem`: Get Postmortem. Scoped to the Statuspage status page given by the Page ID input.
* **Get Status Embed Config** `getStatusEmbedConfig`: Get status embed config settings. Scoped to the Statuspage status page given by the Page ID input.
* **Get Subscriber** `getSubscriber`: Get a subscriber. Scoped to the Statuspage status page given by the Page ID input.
* **Get Subscriber Count** `getSubscriberCount`: Get a count of subscribers by type. Scoped to the Statuspage status page given by the Page ID input.
* **Get Subscriber Histogram By State** `getSubscriberHistogramByState`: Get a histogram of subscribers by type and then state. Scoped to the Statuspage status page given by the Page ID input.
* **Get User Permissions** `getUserPermissions`: Get a user's permissions. Scoped to the Statuspage organization given by the Organization ID input.
* **List Active Maintenances** `listActiveMaintenances`: Get a list of active maintenances. Scoped to the Statuspage status page given by the Page ID input.
* **List Component Groups** `listComponentGroups`: Get a list of component groups. Scoped to the Statuspage status page given by the Page ID input.
* **List Components** `listComponents`: Get a list of components. Scoped to the Statuspage status page given by the Page ID input.
* **List Incident Subscribers** `listIncidentSubscribers`: Get a list of incident subscribers. Scoped to the Statuspage status page given by the Page ID input.
* **List Incident Templates** `listIncidentTemplates`: Get a list of templates. Scoped to the Statuspage status page given by the Page ID input.
* **List Incidents** `listIncidents`: Get a list of incidents. Scoped to the Statuspage status page given by the Page ID input.
* **List Metrics** `listMetrics`: Get a list of metrics. Scoped to the Statuspage status page given by the Page ID input.
* **List Metrics For Metrics Provider** `listMetricsForMetricsProvider`: List metrics for a metric provider. Scoped to the Statuspage status page given by the Page ID input.
* **List Metrics Providers** `listMetricsProviders`: Get a list of metric providers. Scoped to the Statuspage status page given by the Page ID input.
* **List Organization Users** `listOrganizationUsers`: Get a list of users. Scoped to the Statuspage organization given by the Organization ID input.
* **List Page Access Group Components** `listPageAccessGroupComponents`: List components for a page access group. Scoped to the Statuspage status page given by the Page ID input.
* **List Page Access Groups** `listPageAccessGroups`: Get a list of page access groups. Scoped to the Statuspage status page given by the Page ID input.
* **List Page Access User Components** `listPageAccessUserComponents`: Get components for page access user. Scoped to the Statuspage status page given by the Page ID input.
* **List Page Access User Metrics** `listPageAccessUserMetrics`: Get metrics for page access user. Scoped to the Statuspage status page given by the Page ID input.
* **List Page Access Users** `listPageAccessUsers`: Get a list of page access users. Scoped to the Statuspage status page given by the Page ID input.
* **List Pages** `listPages`: Get a list of pages. Covers every status page the authenticated Statuspage API key can access.
* **List Scheduled Incidents** `listScheduledIncidents`: Get a list of scheduled incidents. Scoped to the Statuspage status page given by the Page ID input.
* **List Subscribers** `listSubscribers`: Get a list of subscribers. Scoped to the Statuspage status page given by the Page ID input.
* **List Unresolved Incidents** `listUnresolvedIncidents`: Get a list of unresolved incidents. Scoped to the Statuspage status page given by the Page ID input.
* **List Unsubscribed Subscribers** `listUnsubscribedSubscribers`: Get a list of unsubscribed subscribers. Scoped to the Statuspage status page given by the Page ID input.
* **List Upcoming Incidents** `listUpcomingIncidents`: Get a list of upcoming incidents. Scoped to the Statuspage status page given by the Page ID input.
* **Publish Postmortem** `publishPostmortem`: Publish Postmortem. Scoped to the Statuspage status page given by the Page ID input.
* **Reactivate Subscribers** `reactivateSubscribers`: Reactivate a list of quarantined subscribers. Scoped to the Statuspage status page given by the Page ID input.
* **Remove Component From Page Access Group** `removeComponentFromPageAccessGroup`: Remove a component from a page access group. Scoped to the Statuspage status page given by the Page ID input.
* **Remove Component From Page Access User** `removeComponentFromPageAccessUser`: Remove component for page access user. Scoped to the Statuspage status page given by the Page ID input.
* **Remove Components From Page Access Group** `removeComponentsFromPageAccessGroup`: Delete components for a page access group. Scoped to the Statuspage status page given by the Page ID input.
* **Remove Components From Page Access User** `removeComponentsFromPageAccessUser`: Remove components for page access user. Scoped to the Statuspage status page given by the Page ID input.
* **Remove Metric From Page Access User** `removeMetricFromPageAccessUser`: Delete metric for page access user. Scoped to the Statuspage status page given by the Page ID input.
* **Remove Metrics From Page Access User** `removeMetricsFromPageAccessUser`: Delete metrics for page access user. Scoped to the Statuspage status page given by the Page ID input.
* **Remove Page Access Groups From Component** `removePageAccessGroupsFromComponent`: Remove page access groups from a component. Scoped to the Statuspage status page given by the Page ID input.
* **Remove Page Access Users From Component** `removePageAccessUsersFromComponent`: Remove page access users from component. Scoped to the Statuspage status page given by the Page ID input.
* **Replace Page Access Group Components** `replacePageAccessGroupComponents`: Replace components for a page access group. Scoped to the Statuspage status page given by the Page ID input.
* **Replace Page Access User Components** `replacePageAccessUserComponents`: Replace components for page access user. Scoped to the Statuspage status page given by the Page ID input.
* **Replace Page Access User Metrics** `replacePageAccessUserMetrics`: Replace metrics for page access user. Scoped to the Statuspage status page given by the Page ID input.
* **Resend Incident Subscriber Confirmation** `resendIncidentSubscriberConfirmation`: Resend confirmation to an incident subscriber. Scoped to the Statuspage status page given by the Page ID input.
* **Resend Subscriber Confirmation** `resendSubscriberConfirmation`: Resend confirmation to a subscriber. Scoped to the Statuspage status page given by the Page ID input.
* **Resend Subscriber Confirmations** `resendSubscriberConfirmations`: Resend confirmations to a list of subscribers. Scoped to the Statuspage status page given by the Page ID input.
* **Reset Metric Data** `resetMetricData`: Reset data for a metric. Scoped to the Statuspage status page given by the Page ID input.
* **Revert Postmortem** `revertPostmortem`: Revert Postmortem. Scoped to the Statuspage status page given by the Page ID input.
* **Unsubscribe Incident Subscriber** `unsubscribeIncidentSubscriber`: Unsubscribe an incident subscriber. Scoped to the Statuspage status page given by the Page ID input.
* **Unsubscribe Subscriber** `unsubscribeSubscriber`: Unsubscribe a subscriber. Scoped to the Statuspage status page given by the Page ID input.
* **Unsubscribe Subscribers** `unsubscribeSubscribers`: Unsubscribe a list of subscribers. Scoped to the Statuspage status page given by the Page ID input.
* **Update Component** `updateComponent`: Update a component. If group_id is "null" then the component will be removed from a group. Scoped to the Statuspage status page given by the Page ID input.
* **Update Component Group** `updateComponentGroup`: Update a component group. Scoped to the Statuspage status page given by the Page ID input.
* **Update Incident** `updateIncident`: Update an incident. Scoped to the Statuspage status page given by the Page ID input.
* **Update Incident Update** `updateIncidentUpdate`: Update a previous incident update. Scoped to the Statuspage status page given by the Page ID input.
* **Update Metric** `updateMetric`: Update a metric. Scoped to the Statuspage status page given by the Page ID input.
* **Update Metrics Provider** `updateMetricsProvider`: Update a metric provider. Scoped to the Statuspage status page given by the Page ID input.
* **Update Page** `updatePage`: Update a page. Scoped to the Statuspage status page given by the Page ID input.
* **Update Page Access Group** `updatePageAccessGroup`: Update a page access group. Scoped to the Statuspage status page given by the Page ID input.
* **Update Page Access User** `updatePageAccessUser`: Update page access user. Scoped to the Statuspage status page given by the Page ID input.
* **Update Status Embed Config** `updateStatusEmbedConfig`: Update status embed config settings. Scoped to the Statuspage status page given by the Page ID input.
* **Update Subscriber** `updateSubscriber`: Update a subscriber. Scoped to the Statuspage status page given by the Page ID input.
* **Update User Role Permissions** `updateUserRolePermissions`: Update a user's role permissions. Payload should contain a mapping of pages to a set of the desired roles, if the page has Role Based Access Control. Otherwise, the pages should map to an empty hash. User will lose access to any pages omitted from the payload. Scoped to the Statuspage organization given by the Organization ID input.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Component Status Updated | `componentUpdate` | Sent each time a component changes status. Statuspage dispatches this only for status transitions, not for changes to a component's name or position, and the payload carries both the old and the new status. Statuspage sends no event-type field in the payload, so the two events are told apart by shape: a component notification carries component_update and a incident notification carries incident. Statuspage does not sign webhook deliveries, so no signature verification is configured. Webhook notifications must be enabled on the page first (Subscribers &gt; Options &gt; Settings &gt; select Webhook as a delivery type), otherwise Statuspage rejects webhook subscriber creation. |
| Incident Created Or Updated | `incidentUpdate` | Sent each time an incident is created or updated, including scheduled maintenance transitions and postmortem publication. The payload carries the full incident together with all of its incident updates. Statuspage sends no event-type field in the payload, so the two events are told apart by shape: a component notification carries component_update and a incident notification carries incident. Statuspage does not sign webhook deliveries, so no signature verification is configured. Webhook notifications must be enabled on the page first (Subscribers &gt; Options &gt; Settings &gt; select Webhook as a delivery type), otherwise Statuspage rejects webhook subscriber creation. |
