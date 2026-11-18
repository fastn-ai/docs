---
description: "HP Workforce Experience Platform (WXP) — device analytics, health scores, warranty, Windows 11 readiness, app performance, and incident management via the…"
hidden: true
---

# HP Workforce Experience

<img src="../../.gitbook/assets/connectors/hp-workforce-experience.png" alt="HP Workforce Experience logo" width="64">

HP Workforce Experience Platform (WXP) — device analytics, health scores, warranty, Windows 11 readiness, app performance, and incident management via the TechPulse Analytics and Incident Integration APIs.

| | |
| --- | --- |
| **Category** | [IT and service management](README.md) |
| **Website** | [hp.com](https://hp.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `hpWorkforceExperience` |

## Use it

Add HP Workforce Experience from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hpWorkforceExperience.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Incident Comment | `addIncidentComment` | Post a comment on an existing incident. The comment is attributed to the connected user and appears in the incident's comment thread in the Workforce Experience portal. |
| Bulk Update Incidents | `bulkUpdateIncidents` | Apply the same status, priority or assignee change to several incidents of a tenant in one call. System-generated incidents accept status, priority and assignee changes only. |
| Check Alerts Service Health | `checkAlertsServiceHealth` | Check that the Workforce Experience alerts service is reachable for the configured environment. Useful for verifying connectivity and the configured host before running other calls. |
| Create Incident | `createIncident` | Create a new incident. Title and description are required. Source type USER_GENERATED is used for third-party created incidents. |
| Delete Incident | `deleteIncident` | Soft-delete an incident. The incident is hidden from APIs but kept for GDPR/historical purposes. Note: incidentId is a numeric integer, not a UUID. |
| Get Application Errors Report | `getApplicationErrorsReport` | Retrieve application crash and error counts per device and application (swerrorsV2/details), including the failing module, Windows event id and provider, for troubleshooting unstable software. |
| Get Asset Count By Type | `getAssetCountByType` | Retrieve how many assets of each type a tenant has, from the Workforce Experience asset management query service. Useful as a headline count for dashboards. |
| Get Asset Service Status | `getAssetServiceStatus` | Check the status of the TechPulse asset management query service for the configured environment, to confirm connectivity and credentials before running asset searches. |
| Get Battery Replacement Report | `getBatteryReplacementReport` | Retrieve batteries due for replacement (batteryrep/details), with battery health, serial number, replacement timeframe and reason, plus the device's warranty status. |
| Get Battery Status And Risk Factors Report | `getBatteryRiskFactorsReport` | Retrieve battery status with its risk factors (batteryStatRiskFact/batteryRepAndRiskFact), combining battery health, HP Battery Health Manager settings, installed versus recommended BIOS version and the replacement reason per device. |

<details>

<summary>See 60 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Battery Usage Optimization Report | `getBatteryUsageOptimizationReport` | Retrieve battery usage optimization detail per device (batteryUsageOpt/details), showing HP Battery Health Manager configuration and the BIOS level required to apply the recommended battery setting. |
| Get BIOS Inventory Report | `getBiosInventoryReport` | Retrieve installed versus latest BIOS versions per device (biosinventory/details), including criticality of the available update, release dates, SoftPaq numbers and download links, so out-of-date firmware can be targeted. |
| Get Blue Screen Details Report | `getBlueScreenDetailsReport` | Retrieve Windows blue-screen (stop error) events per device (hwbluescreen/details), including the bug check code, the driver that caused the crash, its version and the hardware health indicators recorded at the time. |
| Get Component Inventory Report | `getComponentInventoryReport` | Retrieve the peripherals attached to enrolled devices (componentInv/details), such as monitors and docking stations, with manufacturer, model and firmware detail. HP's published specification does not enumerate the row columns for this view, so the rows are returned as-is. |
| Get Data Health Report | `getDataHealthReport` | Retrieve the telemetry data health detail for a tenant (datahealth/dataHealthDetails), showing which devices are returning complete analytics data. HP's published specification does not enumerate the row columns for this view, so the rows are returned as-is. |
| Get Deployment Status Report | `getDeploymentStatusReport` | Retrieve the rollout status of the HP TechPulse and Touchpoint agents per device (deploymentStatus/deploymentDetails), to track enrolment progress and installation errors. HP's published specification does not enumerate the row columns for this view, so the rows are returned as-is. |
| Get Device Analytics | `getDeviceAnalytics` | Retrieve device analytics including health scores, utilization, warranty status, and Windows 11 readiness. Optionally filter by devicetype or date range. |
| Get Device Utilization By Application Report | `getDeviceUtilizationByApplicationReport` | Retrieve device CPU and memory utilization broken down by application (deviceutiV3/swPerfByApplication), to find the software consuming the most resources. HP's published specification does not enumerate the row columns for this view, so the rows are returned as-is. |
| Get Device Utilization By Time Report | `getDeviceUtilizationByTimeReport` | Retrieve device CPU and memory utilization broken down by time period (deviceutiV3/swPerfByTime). HP's published specification does not enumerate the row columns for this view, so the rows are returned as-is. |
| Get Disk Capacity Report | `getDiskCapacityReport` | Retrieve disk capacity and free space per device (diskcap/details), with disk model, type, firmware revision and the storage status HP derives from them. |
| Get Disk Replacement Report | `getDiskReplacementReport` | Retrieve disks predicted to need replacement (diskrep/details), with the replacement timeframe, the detected drive issue, storage status and the device's warranty position. |
| Get Driver Inventory Report | `getDriverInventoryReport` | Retrieve installed versus latest device driver versions (driver/details), with driver category, criticality of the available update, release notes and SoftPaq download links. |
| Get Hardware Health Report | `getHardwareHealthReport` | Retrieve the hardware health summary per device (hwhealthNew/details), showing the health and resource summaries HP calculates each month and which resources are affected. |
| Get Hardware Inventory Report | `getHardwareInventoryReport` | Retrieve the full hardware inventory of enrolled devices (hwinv/allData), one row per device with model, serial number, processor, memory, operating system, warranty status, enrolment and last-online dates. |
| Get Hardware Replacement Report | `getHardwareReplacementReport` | Retrieve HP's device replacement grading per device (hwgradeNew/details), including the recommended replacement, the affected resources behind the recommendation and the health improvement scale. |
| Get Hardware Warranty Report | `getHardwareWarrantyReport` | Retrieve warranty coverage per device (hwwarV2/details), including overall warranty status, days remaining, obligation start and end dates and the offer description of each support contract. |
| Get Incident | `getIncident` | Retrieve a single incident by ID. Uses GET /analytics/v1/incidents/1.1/tenants/{tenantId}/incidents/{id}. Note: incidentId is a numeric integer, not a UUID. |
| Get Incident Management Report | `getIncidentManagementReport` | Retrieve incident analytics per device (incidentmgmt/details), including incident type, priority, status, first response time and closure time, for reporting on support performance. |
| Get Incident Subscription Settings | `getIncidentSubscriptions` | Retrieve which incident types and subtypes a tenant is subscribed to, so you can see which conditions HP TechPulse will raise incidents for. |
| Get Network Inventory Report | `getNetworkInventoryReport` | Retrieve the network adapters present on enrolled devices (networkinv/allData), with adapter product name and type per device. HP's published specification does not enumerate the row columns for this view, so the rows are returned as-is. |
| Get Non-Reporting Devices Report | `getNonReportingDevicesReport` | Retrieve enrolled devices that have stopped sending telemetry (nonrepodevice/details), with the last online date and enrolment details, so agent or connectivity problems can be chased. |
| Get Recommended Actions | `getRecommendedActions` | Retrieve the remediation actions HP recommends for a tenant's device estate, the prioritised list shown on the device experience dashboard. |
| Get Software Inventory Report | `getSoftwareInventoryReport` | Retrieve the applications installed across enrolled devices (swinv/details), one row per device and application with publisher, version, install date and application state. |
| Get Software Utilization By Device Report | `getSoftwareUtilizationByDeviceReport` | Retrieve application usage per device and month (softuti/softwareUtilizationByDevice), with usage hours, usage percentage and the usage band each device falls into for an application. |
| Get Software Utilization Summary Report | `getSoftwareUtilizationSummaryReport` | Retrieve application usage aggregated across the estate (softuti/summary), with the number of devices, usage hours, usage percentage and average session time per application, to spot unused licences. |
| Get Tenant | `getTenant` | Retrieve the profile of a single HP TechPulse tenant, including its display name, type, domain, subscription state and regional data centre. |
| Get Tenant Entitlement Summary | `getTenantEntitlementSummary` | Retrieve a tenant's resource entitlement summary, showing the seats and services purchased, how many are consumed and when the subscription expires. |
| Get Tenant Feature Flags | `getTenantFeatureFlags` | Retrieve the Workforce Experience features enabled for a tenant by its subscription plan, so an integration can check entitlement before calling a gated endpoint. |
| Get Top Devices With Blue Screen Errors | `getTopDevicesWithBlueScreenErrors` | Retrieve the devices with the most Windows blue-screen crashes over time (hwbluescreen/topDevicesWithError), aggregated per month with the crash count and the number of affected devices. |
| Get User | `getUser` | Retrieve a single HP TechPulse user by UUID, including profile, organization, locale and status. |
| Get User Roles | `getUserRoles` | Retrieve the Workforce Experience roles assigned to a user, optionally limited to the roles that are visible in the portal and translated into a chosen language. |
| Get Windows 11 Readiness Report | `getWindows11ReadinessReport` | Retrieve the Windows 11 readiness assessment per device (win11ReadinessV2/details), including compatibility status, blocking hardware attributes such as TPM version and secure boot, and HP's upgrade or replace recommendation. |
| Get Workforce Experience Score | `getWorkforceExperienceScore` | Retrieve a tenant's overall Workforce Experience (WEX) score and its contributing sub-scores, the headline figure shown on the Workforce Experience dashboard. |
| Get Workforce Experience Tenant | `getWorkforceExperienceTenant` | Retrieve a tenant's profile from the Workforce Experience Platform tenant service, which carries the portal-side attributes such as display name, domain, type and status. |
| List Child Tenants | `listChildTenants` | List the child tenants (managed companies) beneath the tenant the connection authenticates as. Partners use it to enumerate the customers whose analytics and incidents they can query. |
| List Custom Alert Devices | `listCustomAlertDevices` | List the devices currently matching a tenant's custom device alerts, with filtering, sorting and paging, so an integration can act on the devices an alert has flagged. |
| List Devices (Hardware Inventory) | `listDevices` | Retrieve hardware inventory for all enrolled HP devices — model, serial number, status, health, warranty. Uses POST to /analytics/v1/reports/hwinv/details/type/grid. |
| List Incident Comments | `listIncidentComments` | Retrieve the comment thread of a single incident, including automatic status-change entries, with SCIM-style pagination. The incident identifier is the numeric incident id, not the display id. |
| List Incident Priorities | `listIncidentPriorities` | List the incident priority values supported by HP TechPulse, returned as key/display-value pairs in the caller's language. Use it to populate a priority picker before creating or updating an incident. |
| List Incident Statuses | `listIncidentStatuses` | List the incident status values supported by HP TechPulse, returned as key/display-value pairs in the caller's language. Use it to populate a status picker before updating an incident. |
| List Incidents | `listIncidents` | List incidents for a tenant. Uses POST /analytics/v1/incidents/1.2/tenants/{tenantId}/incidents with tenantIds in body. |
| List Role Abilities | `listRoleAbilities` | List the role-based access control abilities (permissions) defined in Workforce Experience, which roles are composed from. |
| List Support Members | `listSupportMembers` | List the support members of a tenant who can be assigned to an incident, with search, sorting and pagination. Use the returned member id as the assigneeId when updating an incident. |
| List Tenants | `listTenants` | List the HP TechPulse tenants the connected credentials can see, with SCIM-style pagination. Use it to discover the tenant UUIDs required by the analytics and incident actions. |
| List Users | `listUsers` | List the HP TechPulse users visible to the connected credentials, with their profile, organization and status. Use the returned user id when creating an incident on behalf of a user. |
| Look Up Identity Provider | `lookUpIdentityProvider` | Find which identity provider a Workforce Experience user signs in with, by email address. Used during sign-in to route a user to their federated identity provider. |
| Map Identities In Bulk | `mapIdentitiesInBulk` | Translate a batch of company, user or device identifiers into their HP TechPulse UUIDs in one call, for joining analytics report rows to the identity and incident APIs. |
| Map Identity By Integer ID | `mapIdentityByIntegerId` | Translate the integer id of a company, user or device used inside analytics report rows into its HP TechPulse UUID, so report output can be joined to the identity and incident APIs. |
| Query Assets | `queryAssets` | Query the Workforce Experience Platform asset store for devices and peripherals, with filters, sorting and pagination. The request body follows the WXP asset query document rather than the published TechPulse specification. |
| Query Insights | `queryInsights` | Run an insights query against the Workforce Experience Platform insights service, the query interface behind the WXP experience dashboards. The request body is the platform's insights query document; its shape is defined by the WXP insights service rather than by the published TechPulse specification, so the fields below follow the query documents used by the platform. |
| Run Analytics Graph Report | `runAnalyticsGraphReport` | Run any HP TechPulse Analytics aggregate (graph) report by report family and view name, for example hwinv/summary for device counts or hwbluescreen/bseTopErrorsByDriver for blue-screen error trends. Returns the aggregated series behind a Workforce Experience dashboard widget. |
| Run Analytics Grid Report | `runAnalyticsGridReport` | Run any HP TechPulse Analytics tabular (grid) report by report family and view name, for example hwinv/details for hardware inventory or swerrorsV2/details for application errors. The 44 report families published in HP's Analytics API specification are listed on the Report Family field; the View Name field selects the view within the family. Returns SCIM-style paginated rows. |
| Run Workforce Experience Grid Report | `runWorkforceExperienceGridReport` | Run an analytics grid report through the Workforce Experience Platform host instead of the TechPulse host, for tenants whose reporting is served by WXP. Takes the same report family and view name as Run Analytics Grid Report. |
| Search Assets (TechPulse) | `searchAssetsTechPulse` | Search a tenant's assets through the TechPulse asset management query service, the equivalent of Search Tenant Assets for tenants served from the TechPulse host. |
| Search Child Tenants | `searchChildTenants` | Search the tenants managed beneath a Workforce Experience tenant, with free-text search, paging and sorting. Use it when a partner needs to find a specific customer among many child tenants. |
| Search Experience Pulses | `searchExperiencePulses` | Search a tenant's employee experience pulses (survey campaigns) in the Workforce Experience campaign service, with their status and schedule. |
| Search Tenant Assets | `searchTenantAssets` | Search a tenant's assets through the Workforce Experience asset management query service, with filters, paging and sorting. The tenant is supplied as an input rather than hardcoded, so the action works for any tenant the connection can see. |
| Search Tenant Notification Workflows | `searchTenantNotificationWorkflows` | Search a tenant's Workforce Experience notification workflow assignments, the rules that decide who is notified when a condition is detected. |
| Update Incident | `updateIncident` | Partially update an incident. Supports status, priority, and assigneeId. Note: incidentId is a numeric integer, not a UUID. |
| Update Incident Subscription Settings | `updateIncidentSubscriptions` | Subscribe or unsubscribe a tenant's incident types and subtypes and set how often HP emails about incidents. Read the current settings with Get Incident Subscription Settings first and send back the full type list, because the call replaces the tenant's subscription selection. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Critical Alert | `critical` | Fired when a monitor rule threshold reaches Critical level — immediate action required. |
| Info Alert | `info` | Fired when a monitor rule threshold reaches Info level — informational notification. |
| Warning Alert | `warn` | Fired when a monitor rule threshold reaches Warn level — review recommended. |
