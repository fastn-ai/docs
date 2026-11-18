---
description: "SolarWinds Pingdom website and transaction monitoring."
hidden: true
---

# Pingdom

SolarWinds Pingdom website and transaction monitoring. Manage uptime checks, transaction (TMS) checks, maintenance windows, alerting contacts and teams, and read alerting actions, root-cause analysis, raw results, summary reports, probe servers and account credits via the Pingdom REST API 3.1.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [pingdom.com](https://pingdom.com) |
| **Authentication** | API key |
| **Actions** | 50 |
| **Events** | 2 |
| **Slug** | `pingdom` |

## Use it

Add Pingdom from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pingdom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Check | `createCheck` | Creates a new Pingdom uptime check (http, httpcustom, tcp, ping, dns, udp, smtp, pop3 or imap) against a target host. Consumes an uptime check slot on the plan - confirm availability with Get Account Credits first. Returns the new check id and name. |
| Create Contact | `createContact` | Creates a Pingdom alerting contact with one or more notification targets. Alerts sent to this contact reach a real inbox or phone, so only create contacts for addresses you control. |
| Create Maintenance Window | `createMaintenanceWindow` | Creates a maintenance window that suppresses Pingdom alerts for the assigned uptime and transaction checks between the given start and end times, optionally recurring daily, weekly or monthly. |
| Create Team | `createTeam` | Creates a Pingdom alerting team from a set of existing contact identifiers. Checks can then be pointed at the team so every member is alerted. |
| Create Transaction Check | `createTransactionCheck` | Creates a Pingdom transaction (TMS) check that replays a scripted sequence of browser steps against a site on a schedule. Consumes a transaction check slot on the plan - confirm availability with Get Account Credits first. |
| Delete Check | `deleteCheck` | Permanently deletes a single Pingdom uptime check by id, along with all of its collected monitoring data. This is irreversible. |
| Delete Contact | `deleteContact` | Deletes a Pingdom alerting contact by id together with all of its notification targets. Checks and teams that referenced the contact stop alerting it. |
| Delete Maintenance Occurrence | `deleteMaintenanceOccurrence` | Deletes a single maintenance occurrence by id, cancelling that one scheduled run of the maintenance window while leaving the window itself in place. |
| Delete Maintenance Window | `deleteMaintenanceWindow` | Deletes a single maintenance window by id. Checks assigned to it stop being suppressed and resume normal alerting. |
| Delete Multiple Checks | `deleteChecks` | Permanently deletes a list of Pingdom uptime checks and all of their collected monitoring data. This is irreversible. |
| Delete Multiple Maintenance Occurrences | `deleteMaintenanceOccurrences` | Deletes several maintenance occurrences in one call by their identifiers. The value is sent under both the 'occurrenceids' and 'occurenceids' query keys because the Pingdom 3.1 specification names the parameter inconsistently; the API ignores the spelling it does not use. |
| Delete Multiple Maintenance Windows | `deleteMaintenanceWindows` | Deletes several maintenance windows in one call by their identifiers. |
| Delete Team | `deleteTeam` | Deletes a Pingdom alerting team by id. The contacts that were members are not deleted, but checks pointed at the team stop alerting it. |
| Delete Transaction Check | `deleteTransactionCheck` | Deletes a Pingdom transaction (TMS) check by id, freeing its transaction check slot. The check's collected results are removed with it. |
| Get Account Credits | `getCredits` | Returns the Pingdom account's check limits and usage: uptime check limit, transaction check limit, available and used checks, available SMS credits, RUM site allowances and alerting user seats. Use it before creating checks to confirm the plan has an available slot. |
| Get All Transaction Checks Status Report | `getTransactionChecksStatusReport` | Returns the status change report for every Pingdom transaction (TMS) check in the organization over a time window, so you can see all transaction outages in one call. |
| Get Average Summary | `getSummaryAverage` | Returns the average response time and optional uptime figures for a Pingdom uptime check over a period, optionally split by country or by probe. |
| Get Check | `getCheck` | Returns the full detailed configuration of a single Pingdom uptime check by id, including its type-specific settings, alert policy, probe filters, tags and current status. |
| Get Contact | `getContact` | Returns a single Pingdom alerting contact by id, with its notification targets, paused state and team memberships. |
| Get Hours Of Day Summary | `getSummaryHoursOfDay` | Returns the average response time of a Pingdom uptime check for each hour of the day over a period, which shows when in the day the target is slowest. |
| Get Maintenance Occurrence | `getMaintenanceOccurrence` | Returns the details of a single maintenance occurrence by id, including its parent maintenance window and its start and end times. |
| Get Maintenance Window | `getMaintenanceWindow` | Returns a single maintenance window by id, with its schedule, recurrence settings and the uptime and transaction checks assigned to it. |
| Get Outage Summary | `getSummaryOutage` | Returns the list of status changes (up/down periods) for a Pingdom uptime check over a period, each with its status and start and end timestamps. This is the outage history for the check. |
| Get Performance Summary | `getSummaryPerformance` | Returns a Pingdom uptime check's performance broken into hourly, daily or weekly sub-intervals, each with the average response time and optional uptime figures. |
| Get Probes Summary | `getSummaryProbes` | Returns the list of Pingdom probe servers that performed tests for a given uptime check during a period, so you can see which locations produced the check's results. |
| Get Reference Data | `getReference` | Returns Pingdom's reference lists used by account settings: regions, time zones, date and time formats, number formats, countries and phone codes, each with the identifier other endpoints expect. |
| Get Root Cause Analysis Result | `getAnalysisResult` | Returns the raw root cause analysis result for a specified analysis of a Pingdom uptime check - the diagnostic data Pingdom collected when the check went down, such as the failing probe's response and traceroute. |
| Get Team | `getTeam` | Returns a single Pingdom alerting team by id, with the contacts that belong to it. |
| Get Transaction Check | `getTransactionCheck` | Returns a single Pingdom transaction (TMS) check by id with its full step script, schedule, region, alert recipients and current status. |
| Get Transaction Check Performance Report | `getTransactionCheckPerformanceReport` | Returns a performance report for a single Pingdom transaction (TMS) check, broken into hourly, daily or weekly intervals with average response times and optional uptime figures. |
| Get Transaction Check Status Report | `getTransactionCheckStatusReport` | Returns the status change report for a single Pingdom transaction (TMS) check - the up and down periods it went through over a time window. |
| List Alert Actions | `listAlertActions` | Returns the Pingdom alerting log: the alerts that were sent for the account's checks, with the check id, recipient user, medium (email, sms, etc), status and message. Filter by time window, check, user, status or medium. |
| List Checks | `listChecks` | Returns an overview list of all uptime checks in the Pingdom account, with each check's id, name, host, type, current status, resolution and last test timestamps. Optionally filter by tags and include tag, severity and encryption details. |
| List Contacts | `listContacts` | Returns all Pingdom alerting contacts in the organization with their notification targets (email addresses, SMS numbers, mobile push devices), paused state, whether they are a login user, and the teams they belong to. |
| List Maintenance Occurrences | `listMaintenanceOccurrences` | Returns the individual occurrences generated by the account's maintenance windows - one entry per scheduled run of a recurring window. Filter by parent maintenance window or effective period. |
| List Maintenance Windows | `listMaintenanceWindows` | Returns the account's maintenance windows - the scheduled periods during which Pingdom suppresses alerts for the assigned uptime and transaction checks. |
| List Probe Servers | `listProbes` | Returns the Pingdom probe servers that run checks, each with its id, city, country, hostname, IP addresses and active state. Use the ids to filter results or to target a single test. |
| List Raw Check Results | `listResults` | Returns the raw individual test results for a Pingdom uptime check - one row per probe test with its timestamp, probe id, status, response time and status description. Filter by period, probe, status and response-time range. |
| List Root Cause Analyses | `listAnalyses` | Returns the list of the latest root cause analysis results for a specified Pingdom uptime check, each with an analysis id and the timestamps of the first and last failing test. Use the analysis id with Get Root Cause Analysis Result to read the raw diagnosis. |
| List Teams | `listTeams` | Returns all Pingdom alerting teams in the organization together with their members, so you can see who is alerted for a check that targets a team. |
| List Transaction Checks | `listTransactionChecks` | Returns an overview of all Pingdom transaction (TMS) checks and WPM recordings in the organization, with their name, status, interval, region and tags. Filter by type or tags. |
| Modify Multiple Checks | `modifyChecks` | Pauses, resumes or changes the test resolution for many Pingdom uptime checks in one bulk call. Omitting the check id list applies the change to every check in the account. |
| Run Single Test | `runSingleTest` | Runs one ad-hoc test against a target from a Pingdom probe and returns the result immediately, without creating a check. Supports http, httpcustom, tcp, ping, dns, udp, smtp, pop3 and imap. Intended for occasional use, not as a monitoring substitute. |
| Run Traceroute | `runTraceroute` | Runs a traceroute to a target host from a Pingdom probe and returns the raw hop-by-hop output, plus the probe id and location that produced it. Useful when diagnosing where a check's traffic is being lost. |
| Update Check | `updateCheck` | Modifies the settings of an existing Pingdom uptime check: rename it, change the target host, pause or resume it, change the test resolution, alert policy, tags, probe filters or notification recipients. Returns a confirmation message. |
| Update Contact | `updateContact` | Updates a Pingdom alerting contact: rename it, pause or resume its alerts, and replace its notification targets. The notification target list is a full replacement. |
| Update Maintenance Occurrence | `updateMaintenanceOccurrence` | Reschedules a single maintenance occurrence by changing its start and end times, without affecting the other occurrences of the same recurring maintenance window. |
| Update Maintenance Window | `updateMaintenanceWindow` | Modifies an existing maintenance window: its description, start and end times, recurrence, and the uptime and transaction checks it covers. |
| Update Team | `updateTeam` | Renames a Pingdom alerting team and replaces its membership with the supplied contact identifiers. The member list is a full replacement, not an addition. |
| Update Transaction Check | `updateTransactionCheck` | Modifies an existing Pingdom transaction (TMS) check: rename it, activate or deactivate it, change its step script, interval, region, severity, tags or alert recipients. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Check Recovered | `UP` | A Pingdom uptime or transaction check changed state back to UP. Registration is manual and identical to the DOWN event: My Pingdom &gt; Integrations &gt; Integrations &gt; Add integration &gt; Type: Webhook &gt; paste the fastn trigger URL &gt; name it &gt; Active &gt; Save; then Edit each check &gt; Connect integrations &gt; tick the webhook &gt; Save. The check must also have 'Notify when back up again' enabled or Pingdom never sends the recovery call. Payload schema is modelled from Pingdom's documented webhook sample, not captured from a live delivery. |
| Check Went Down | `DOWN` | A Pingdom uptime or transaction check changed state to DOWN. Pingdom has NO REST API for creating webhook integrations (GET /api/3.1/integrations, /api/3.1/webhooks and /api/3.1/alerting/integrations all return 404 'Please specify a valid API resource.'), so the customer must register this URL by hand: log in to My Pingdom &gt; Integrations &gt; Integrations &gt; Add integration &gt; Type: Webhook &gt; paste the fastn trigger URL as the URL &gt; give it a name &gt; Active &gt; Save. Then open each check that should fire this trigger (Experience Monitoring &gt; Uptime, or Synthetics &gt; Transaction) &gt; Edit check &gt; Connect integrations &gt; tick the new webhook &gt; Save. Without that second step Pingdom sends nothing. Payload schema is modelled from Pingdom's documented webhook sample, not captured from a live delivery - this account's plan grants zero uptime check slots and its API token is read-only, so no check could be created to fire one. |
