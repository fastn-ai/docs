---
description: "Cisco AppDynamics (Splunk AppDynamics) Controller REST API — full-stack application performance monitoring."
hidden: true
---

# AppDynamics

<img src="../../.gitbook/assets/connectors/lg/app-dynamics.png" alt="AppDynamics logo">

Cisco AppDynamics (Splunk AppDynamics) Controller REST API — full-stack application performance monitoring. Manage business applications, tiers, nodes, business transactions, metrics, transaction snapshots, health rules, policies, actions, schedules, action suppressions, events and health rule violations, custom dashboards, controller configuration, licensing, and role-based access control (users, groups, roles).

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [appdynamics.com](https://appdynamics.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `appDynamics` |

## Use it

Add AppDynamics from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.appDynamics.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Role To Group | `addRoleToGroup` | Grants an existing role to an existing group, applying it to every member of that group. |
| Add Role To User | `addRoleToUser` | Grants an existing role directly to an existing user. |
| Add User To Group | `addUserToGroup` | Adds an existing user as a member of an existing group. |
| Configure Metric Retention By Account | `configureMetricRetentionByAccount` | Configures the Controller to purge stale EUM and SIM metrics older than the given number of days for the whole account. Requires administrator-level permission beyond a standard API Client role; SaaS accounts commonly see a 500 permission error here. |
| Configure Metric Retention By Application | `configureMetricRetentionByApplication` | Configures the Controller to purge stale EUM and SIM metrics older than the given number of days for a single business application. Requires administrator-level permission beyond a standard API Client role; SaaS accounts commonly see a 500 permission error here. |
| Create Action Suppression | `createActionSuppression` | Creates an action suppression window on a business application, temporarily preventing alerting actions from firing (for example, during planned maintenance). |
| Create Alert Action | `createAlertAction` | Creates an alerting action (email, SMS, thread dump, HTTP request, run script, diagnose transactions, or Jira ticket) that a policy can trigger when its bound events occur. |
| Create Custom Event | `createCustomEvent` | Records a CUSTOM event against a business application, optionally attributed to a specific node, tier, or business transaction, for correlation on the AppDynamics timeline. |
| Create Deployment Event | `createDeploymentEvent` | Records an APPLICATION_DEPLOYMENT event against a business application, useful for marking a release on the AppDynamics timeline. |
| Create Group | `createGroup` | Creates a new user group on the Controller for organizing role assignments. |
| Create Health Rule | `createHealthRule` | Creates a health rule on a business application that evaluates a metric condition and raises a violation when it is met. |
| Create License Allocation | `createLicenseAllocation` | Creates a new license allocation rule on the account, controlling how many agent license units a matching filter/tag scope may consume. |
| Create Policy | `createPolicy` | Creates a policy on a business application that binds one or more events (health rule violations, transaction anomalies, or other events) to one or more actions. |
| Create Role | `createRole` | Creates a new RBAC role with an explicit list of permissions to assign to users or groups. |
| Create Schedule | `createSchedule` | Creates a schedule that defines a recurring or one-time window used to enable or suppress health rule evaluation for a business application. |
| Create User | `createUser` | Creates a new Controller user with an internal, LDAP, or SAML security provider. |
| Delete Action Suppression | `deleteActionSuppression` | Permanently deletes an action suppression window from a business application. |
| Delete Alert Action | `deleteAlertAction` | Permanently deletes an alerting action from a business application. |
| Delete Group | `deleteGroup` | Permanently deletes a user group by numeric id. |
| Delete Health Rule | `deleteHealthRule` | Permanently deletes a health rule from a business application. |
| Delete License Allocation | `deleteLicenseAllocation` | Permanently deletes a license allocation rule from the account. |
| Delete Policy | `deletePolicy` | Permanently deletes a policy from a business application. |
| Delete Role | `deleteRole` | Permanently deletes an RBAC role by numeric id. |
| Delete Schedule | `deleteSchedule` | Permanently deletes a schedule from a business application. |
| Delete User | `deleteUser` | Permanently deletes a Controller user by numeric id. |
| Export Custom Dashboard | `exportCustomDashboard` | Exports a custom dashboard definition as JSON by dashboard id, for backup or migration to another Controller. This endpoint always answers HTTP 200; check the response's `success` field - a missing dashboard returns `{success:false, errors:[...]}`. |
| Get Account License Usage | `getAccountUsageByAccount` | Retrieves agent license usage for the account over a chosen date range. |
| Get Action Suppression | `getActionSuppression` | Retrieves the full definition of a single action suppression window by id. |
| Get Action Suppression By Name | `getActionSuppressionByName` | Retrieves the full definition of a single action suppression window by its exact name. |
| Get Alert Action | `getAlertAction` | Retrieves the full definition of a single alerting action by id. |
| Get Controller Audit History | `getControllerAuditHistory` | Retrieves the audit trail of configuration changes made on the Controller within a chosen date range (maximum one day per call). |
| Get Controller Setting | `getControllerSetting` | Retrieves a single Controller setting by its exact name. |
| Get Group By ID | `getGroupById` | Retrieves a single user group by numeric id, including its affiliated roles. |
| Get Group By Name | `getGroupByName` | Retrieves a single user group by exact name, including its affiliated roles. |
| Get Grouped Usage By Application | `getGroupedUsageByApplication` | Retrieves agent license usage grouped by business application name, including vCPU counts and agent details per application. |
| Get Grouped Usage By Host | `getGroupedUsageByHost` | Retrieves agent license usage grouped by host, including container and node information per host. |
| Get Health Rule | `getHealthRule` | Retrieves the full definition of a single health rule by id. |
| Get License Allocation | `getLicenseAllocation` | Retrieves a single license allocation rule by its id. |
| Get Metric Data | `getMetricData` | Retrieves time-series data points for a single fully-qualified metric path within a business application over a chosen time window. |
| Get Metric Hierarchy | `getMetricHierarchy` | Browses the metric tree of a business application starting at an optional metric path, returning the folders and leaf metrics available at that level. |
| Get My Account | `getMyAccount` | Retrieves the numeric account id and resource links for the account the current API Client belongs to. Use the returned id to feed the License and Accounts actions. |
| Get Node By Name | `getNodeByName` | Retrieves details for a single named node within a business application. |
| Get Policy | `getPolicy` | Retrieves the full definition of a single policy by id. |
| Get Role By ID | `getRoleById` | Retrieves a single RBAC role by numeric id, optionally including its full permission list. |
| Get Role By Name | `getRoleByName` | Retrieves a single RBAC role by exact name, optionally including its full permission list. |
| Get Schedule | `getSchedule` | Retrieves the full definition of a single schedule by id. |
| Get Tier By Name | `getTierByName` | Retrieves details for a single named tier within a business application. |
| Get Transaction Snapshots | `getTransactionSnapshots` | Retrieves detailed transaction snapshots (request-level traces) captured for a business application within a chosen time window. |
| Get User By ID | `getUserById` | Retrieves a single Controller user by numeric id, including their affiliated groups and roles. |
| Get User By Name | `getUserByName` | Retrieves a single Controller user by exact username, including their affiliated groups and roles. |
| Import Custom Dashboard | `importCustomDashboard` | Imports a custom dashboard definition (previously exported as JSON) into this Controller, creating a new dashboard. This endpoint always answers HTTP 200; check the response's `success` field for the real outcome. |
| List Action Suppressions | `listActionSuppressions` | Retrieves every action suppression window configured on a business application. |
| List Alert Actions | `listAlertActions` | Retrieves every alerting action configured on a business application. |
| List Applications | `listApplications` | Retrieves every business application registered in this AppDynamics Controller account, with each application's numeric id and name. |
| List Backends | `listBackends` | Retrieves every backend (external call target such as a database or web service) registered for a business application, with their properties. |
| List Business Transactions | `listBusinessTransactions` | Retrieves every business transaction defined in a specific business application, identified by application id or name. |
| List Controller Settings | `listControllerSettings` | Retrieves every configurable Controller setting, its current value, scope, and whether it is updatable. |
| List Events | `listEvents` | Retrieves events (deployments, errors, diagnostic sessions, custom events, and more) recorded for a business application within a chosen time window, optionally filtered by event type and severity. |
| List Groups | `listGroups` | Retrieves every user group configured on this Controller account. |
| List Health Rule Violations | `listHealthRuleViolations` | Retrieves every health rule violation (problem) recorded for a business application within a chosen time window. |
| List Health Rules | `listHealthRules` | Retrieves every health rule configured on a business application. |
| List License Allocations | `listLicenseAllocations` | Retrieves every license allocation rule configured on the account, each defining a package, unit limit, and optional filters/tags for how agent licenses are consumed. |
| List Nodes | `listNodes` | Retrieves node information for every node across all tiers in a business application. |
| List Nodes In Tier | `listNodesInTier` | Retrieves every node (application server agent instance) running within a specific tier of a business application. |
| List Policies | `listPolicies` | Retrieves every policy configured on a business application. |
| List Roles | `listRoles` | Retrieves every RBAC role configured on this Controller account. |
| List Schedules | `listSchedules` | Retrieves every schedule configured for a business application. |
| List Tiers | `listTiers` | Retrieves every tier configured in a specific business application, identified by application id or name. |
| List Users | `listUsers` | Retrieves every user configured on this Controller account. |
| Mark Nodes Historical | `markNodesHistorical` | Marks up to 25 nodes as historical, removing them from active monitoring lists while preserving their historical data. |
| Remove Role From Group | `removeRoleFromGroup` | Revokes a role that was granted to a group. |
| Remove Role From User | `removeRoleFromUser` | Revokes a role that was directly granted to a user. |
| Remove User From Group | `removeUserFromGroup` | Removes a user from a group's membership. |
| Set Business Transaction Monitoring | `setBusinessTransactionMonitoring` | Includes or excludes one or more business transactions from monitoring in a business application by posting their identifiers as an XML payload. |
| Update Action Suppression | `updateActionSuppression` | Replaces the definition of an existing action suppression window. |
| Update Alert Action | `updateAlertAction` | Replaces the definition of an existing alerting action. |
| Update Controller Setting | `updateControllerSetting` | Updates the value of a global Controller setting by name. On SaaS controllers this typically 403s (ConfigurationManagerBean.setConfigurationValue permission check) even for a fully-privileged API Client; it is intended for On-Premises and Virtual Appliance controllers. |
| Update Group | `updateGroup` | Updates the name or description of an existing user group. |
| Update Health Rule | `updateHealthRule` | Replaces the definition of an existing health rule. |
| Update License Allocation | `updateLicenseAllocation` | Replaces the definition of an existing license allocation rule. |
| Update Policy | `updatePolicy` | Replaces the definition of an existing policy. |
| Update Role | `updateRole` | Updates the name or description of an existing RBAC role. |
| Update Schedule | `updateSchedule` | Replaces the definition of an existing schedule. |
| Update User | `updateUser` | Updates the display name or username of an existing Controller user. |
