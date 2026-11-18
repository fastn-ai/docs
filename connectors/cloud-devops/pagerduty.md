---
description: "PagerDuty is an incident response and digital operations platform."
---

# PagerDuty

PagerDuty is an incident response and digital operations platform. This connector covers the PagerDuty REST API v2 (incidents, services, escalation policies, schedules, users, teams, extensions, add-ons, log entries, maintenance windows, event orchestrations, business services, analytics, tags, rulesets, and webhook subscription management) plus the Events API v2 for triggering and enqueuing alert and change events.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [pagerduty.com](https://pagerduty.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 90 |
| **Events** | 0 |
| **Slug** | `pagerduty` |

## Use it

Add PagerDuty from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pagerduty.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add User To Team | `addUserToTeam` | Adds a user to a team with a given role. |
| Create Business Service | `createBusinessService` | Creates a new business service. |
| Create Escalation Policy | `createEscalationPolicy` | Creates a new escalation policy with a single rule targeting a user. |
| Create Event Orchestration | `createEventOrchestration` | Creates a new event orchestration (global event router). |
| Create Extension | `createExtension` | Creates a new extension (outbound integration) attached to a service. |
| Create Incident | `createIncident` | Creates (triggers) a new incident on a service. Requires a valid user email as the From header. |
| Create Incident Note | `createIncidentNote` | Adds a note to an incident. |
| Create Maintenance Window | `createMaintenanceWindow` | Creates a maintenance window that suppresses notifications for a service. |
| Create Ruleset | `createRuleset` | Creates a new global event ruleset. |
| Create Schedule | `createSchedule` | Creates a new on-call schedule with a single layer and one user. |
| Create Schedule Override | `createScheduleOverride` | Creates a temporary schedule override. |
| Create Service | `createService` | Creates a new service. |
| Create Tag | `createTag` | Creates a new tag. |
| Create Team | `createTeam` | Creates a new team. |
| Create User | `createUser` | Creates a new user and sends an invitation email. |
| Create Webhook Subscription | `createWebhookSubscription` | Creates a v3 webhook subscription scoped to a service. |
| Delete Addon | `deleteAddon` | Deletes (uninstalls) an addon. |
| Delete Business Service | `deleteBusinessService` | Deletes a business service. |
| Delete Escalation Policy | `deleteEscalationPolicy` | Deletes an escalation policy. |
| Delete Event Orchestration | `deleteEventOrchestration` | Deletes an event orchestration. |
| Delete Extension | `deleteExtension` | Deletes an extension. |
| Delete Maintenance Window | `deleteMaintenanceWindow` | Deletes a maintenance window. |
| Delete Ruleset | `deleteRuleset` | Deletes a global event ruleset. |
| Delete Schedule | `deleteSchedule` | Deletes an on-call schedule. |
| Delete Service | `deleteService` | Deletes a service. |
| Delete Tag | `deleteTag` | Deletes a tag. |
| Delete Team | `deleteTeam` | Deletes a team. |
| Delete User | `deleteUser` | Deletes a user. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | Deletes a webhook subscription. |
| Get Addon | `getAddon` | Retrieves a single addon by ID. |
| Get Alert | `getAlert` | Retrieves a single alert on an incident. |
| Get Business Service | `getBusinessService` | Retrieves a single business service by ID. |
| Get Current User | `getCurrentUser` | Returns the user profile associated with the API key used to authenticate this request. Used to verify connectivity and identify the authenticated PagerDuty user. |
| Get Escalation Policy | `getEscalationPolicy` | Retrieves a single escalation policy by ID. |
| Get Event Orchestration | `getEventOrchestration` | Retrieves a single event orchestration by ID. |
| Get Event Orchestration Router | `getEventOrchestrationRouter` | Retrieves the router rules for an event orchestration. |
| Get Extension | `getExtension` | Retrieves a single extension by ID. |
| Get Incident | `getIncident` | Retrieves a single incident by ID. |
| Get Incident Analytics | `getIncidentAnalytics` | Returns aggregate incident analytics/metrics for a date range. |
| Get Log Entry | `getLogEntry` | Retrieves a single log entry by ID. |
| Get Maintenance Window | `getMaintenanceWindow` | Retrieves a single maintenance window by ID. |
| Get Ruleset | `getRuleset` | Retrieves a single global event ruleset by ID. |
| Get Schedule | `getSchedule` | Retrieves a single on-call schedule by ID. |
| Get Service | `getService` | Retrieves a single service by ID. |
| Get Tag | `getTag` | Retrieves a single tag by ID. |
| Get Team | `getTeam` | Retrieves a single team by ID. |
| Get User | `getUser` | Retrieves a single user by ID. |
| Get Webhook Subscription | `getWebhookSubscription` | Retrieves a single webhook subscription by ID. |
| Install Addon | `installAddon` | Installs a full-page add-on. |
| List Abilities | `listAbilitiesKeyCheck` | Lists the abilities (features/entitlements) enabled for the PagerDuty account. |
| List Addons | `listAddons` | Lists installed add-ons (UI-embedded third-party links). |
| List Business Services | `listBusinessServices` | Lists business services (higher-level services representing business capabilities). |
| List Escalation Policies | `listEscalationPolicies` | Lists existing escalation policies. |
| List Event Orchestrations | `listEventOrchestrations` | Lists existing event orchestrations (global event routing/processing rulesets). |
| List Extension Schemas | `listExtensionSchemas` | Lists the vendor extension schemas available for creating extensions. |
| List Extensions | `listExtensions` | Lists existing extensions (outbound integrations wired to services, e.g. Slack, ServiceNow). |
| List Incident Alerts | `listIncidentAlerts` | Lists alerts attached to an incident. |
| List Incident Log Entries | `listIncidentLogEntries` | Lists log entries for a specific incident. |
| List Incident Notes | `listIncidentNotes` | Lists notes added to an incident. |
| List Incidents | `listIncidents` | Lists existing incidents, optionally filtered by status, service, date range, or urgency. |
| List Log Entries | `listLogEntries` | Lists log entries across the account (audit trail of incident-related activity). |
| List Maintenance Windows | `listMaintenanceWindows` | Lists maintenance windows (scheduled periods to disable notifications for a set of services). |
| List Notifications | `listNotifications` | Lists notifications sent to users during a given time range. |
| List On-Calls | `listOnCalls` | Lists the on-call entries during a given time range, showing which user is on-call for which escalation policy/schedule. |
| List Ruleset Rules | `listRulesetRules` | Lists the rules within a global event ruleset. |
| List Rulesets | `listRulesets` | Lists global event rulesets (legacy Event Rules, superseded by Event Orchestrations but still supported). |
| List Schedule Overrides | `listScheduleOverrides` | Lists overrides for a schedule within a given time range. |
| List Schedules | `listSchedules` | Lists existing on-call schedules. |
| List Services | `listServices` | Lists existing services (technical or business services monitored by PagerDuty). |
| List Tag Users | `listTagUsers` | Lists users assigned to a tag. |
| List Tags | `listTags` | Lists tags defined in the account. |
| List Teams | `listTeams` | Lists teams in the PagerDuty account. |
| List User Contact Methods | `listUserContactMethods` | Lists contact methods (email/phone/SMS) for a user. |
| List User Notification Rules | `listUserNotificationRules` | Lists notification rules for a user. |
| List Users | `listUsers` | Lists users in the PagerDuty account. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | Lists v3 webhook subscriptions (event destinations for account activity). |
| Merge Incidents | `mergeIncidents` | Merges one or more source incidents into a target incident. |
| Remove User From Team | `removeUserFromTeam` | Removes a user from a team. |
| Update Alert | `updateAlert` | Updates (resolves) an individual alert on an incident. |
| Update Business Service | `updateBusinessService` | Updates a business service. |
| Update Escalation Policy | `updateEscalationPolicy` | Updates an existing escalation policy. |
| Update Event Orchestration | `updateEventOrchestration` | Updates an event orchestration. |
| Update Incident | `updateIncident` | Updates an incident's status (acknowledge or resolve). |
| Update Maintenance Window | `updateMaintenanceWindow` | Updates a maintenance window. |
| Update Ruleset | `updateRuleset` | Updates a global event ruleset. |
| Update Schedule | `updateSchedule` | Updates an existing on-call schedule. |
| Update Service | `updateService` | Updates an existing service. |
| Update Team | `updateTeam` | Updates an existing team. |
| Update User | `updateUser` | Updates an existing user. |
| Update Webhook Subscription | `updateWebhookSubscription` | Updates a webhook subscription. |
