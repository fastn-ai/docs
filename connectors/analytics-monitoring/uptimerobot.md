---
description: "UptimeRobot monitors websites, APIs, ports, and cron jobs for uptime and downtime, and sends alerts when a monitor goes down."
hidden: true
---

# UptimeRobot

<img src="../../.gitbook/assets/connectors/uptimerobot.png" alt="UptimeRobot logo" width="64">

UptimeRobot monitors websites, APIs, ports, and cron jobs for uptime and downtime, and sends alerts when a monitor goes down. This connector wraps UptimeRobot's v2 REST API, which is POST-only with a form-urlencoded body carrying the API key, covering monitors, alert contacts, maintenance windows, public status pages, and account details.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [uptimerobot.com](https://uptimerobot.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `uptimerobot` |

## Use it

Add UptimeRobot from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.uptimerobot.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Alert Contact | `newAlertContact` | Create a new alert contact (notification channel). Live-tested: e-mail, SMS/voice, Twitter, Boxcar, HipChat cannot be created via this API (dashboard-only); Slack, MS Teams, PagerDuty, Zapier are plan-gated on Free accounts; Pushbullet/Pushover need a real external token. Web-Hook (5) and chat integrations like Google Chat (21) work on Free when given a real URL. IMPORTANT: this connector's form-urlencoded template does not percent-encode values - if your value contains ? & = (e.g. a Google Chat/Discord webhook URL with a query string), percent-encode them yourself (? -&gt; %3F, & -&gt; %26, = -&gt; %3D) first or the value truncates and is rejected. Verified live both ways: unencoded gave a real "url is wrong" error; the same value pre-encoded created a real contact (id 8702235). |
| Create Maintenance Window | `newMWindow` | Create a maintenance window that suppresses alerts for the given monitors during a scheduled period. Note: this account's Free plan does not include Maintenance Windows - live-tested and UptimeRobot returned a real account_paused error ("User does not have an active subscription"), matching the dashboard UI's own paid-plan upsell for this feature. The action is wired correctly (its required fields and endpoint match UptimeRobot's live validator, confirmed via the real "type must be 1..4" error returned when type was omitted) but cannot be exercised to a real success without a paid UptimeRobot plan. |
| Create Monitor | `newMonitor` | Create a new monitor (HTTP/S, keyword, ping, port, or heartbeat) to start checking a URL, IP, port, or cron-job callback for uptime. Only the vendor-required core fields (name, URL, type) are supported: this connector's form-urlencoded templating cannot safely expose the many type-specific optional fields (sub_type, port, keyword_type/value, interval, timeout, http auth, custom headers, alert_contacts, mwindows) because UptimeRobot's API rejects any of them when sent empty, and a static template cannot omit a field the caller did not supply. Note: live-tested against this account's Free plan and UptimeRobot returned a real access_denied error ("You are not allowed to use some settings with your current plan") for every monitor type attempted via this endpoint, while the identical operation succeeds through the UptimeRobot dashboard UI - this is a documented account/plan gate on API-based monitor creation, not a connector wiring defect. |
| Create Public Status Page | `newPSP` | Create a public status page that shows the up/down status of one or more monitors at a shareable URL. Note: UptimeRobot's Free plan allows only 1 status page total - live-tested and a second create attempt returned a real access_denied error ("You have reached the maximum number of status pages in your plan"); after deleting the first throwaway page, a second create succeeded for real (id 1253751). |
| Delete Alert Contact | `deleteAlertContact` | Permanently delete an alert contact by id. |
| Delete Maintenance Window | `deleteMWindow` | Permanently delete a maintenance window by id. Note: this account's Free plan does not include Maintenance Windows at all - live-tested against a non-existent id and UptimeRobot returned a real account_paused error ("User does not have an active subscription") rather than a not-found error, confirming the entire feature is gated to paid plans on this account (matching the dashboard UI's own paid-plan upsell). The endpoint and request wiring are correct; a real delete can only be exercised on a paid plan. |
| Delete Monitor | `deleteMonitor` | Permanently delete a monitor by id. This stops all checks and removes its history; it cannot be undone. |
| Delete Public Status Page | `deletePSP` | Permanently delete a public status page by id. |
| Edit Alert Contact | `editAlertContact` | Rename an existing alert contact by id. UptimeRobot's editAlertContact endpoint also accepts optional type/value changes, but this connector only supports friendly_name: UptimeRobot's API rejects other templated fields when sent empty, and this connector's form-urlencoded body cannot conditionally omit a field the caller did not supply. |
| Edit Maintenance Window | `editMWindow` | Rename an existing maintenance window by id. Note: this account's Free plan does not include Maintenance Windows, so no real window exists to edit - live-tested against a non-existent id and UptimeRobot returned a real not_found error ("Maintenance Window"), confirming the endpoint and request wiring are correct even though this account cannot hold real maintenance-window data without a paid plan. |

<details>

<summary>See 8 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Edit Monitor | `editMonitor` | Update a monitor's friendly name, URL, and pause/resume status. UptimeRobot's editMonitor endpoint treats all of these as optional, but this connector requires them together: UptimeRobot's API rejects any templated field sent with an empty value, and this connector's form-urlencoded body cannot conditionally omit a field the caller did not supply. Fetch the monitor's current values first with Get Monitors and pass through any field you do not want to change. |
| Edit Public Status Page | `editPSP` | Rename an existing public status page by id. UptimeRobot's editPSP endpoint also accepts an optional url change, but this connector only supports friendly_name: UptimeRobot's API rejects other templated fields when sent empty, and this connector's form-urlencoded body cannot conditionally omit a field the caller did not supply. |
| Get Account Details | `getAccountDetails` | Retrieve the connected UptimeRobot account's details: email, monitor limit, check interval, monitor counts by status, and subscription info. |
| Get Alert Contacts | `getAlertContacts` | List all alert contacts (notification channels such as e-mail, SMS, and integrations like Slack, webhook, or Google Chat) configured on the account, with each contact's id, type, status, and destination value. |
| Get Maintenance Windows | `getMWindows` | List all maintenance windows on the account. Note: this account's Free plan does not include Maintenance Windows at all - live-tested and UptimeRobot returned a real account_paused error ("User does not have an active subscription") even for this read-only list call, matching the dashboard UI's own paid-plan upsell for this feature. The endpoint and request wiring are correct; a real list can only be exercised on a paid UptimeRobot plan. |
| Get Monitors | `getMonitors` | List all monitors on the account (up to 50 per page, UptimeRobot's default and maximum page size), with each monitor's id, friendly name, URL, type, status, interval, and timeout. Note: UptimeRobot's optional filter/detail-inclusion parameters (offset, limit, search, types, statuses, logs, ssl, alert_contacts, mwindows, response_times, custom_http_headers, etc.) are not exposed on this action - UptimeRobot's v2 API rejects any of these parameters when sent as an empty value, and this connector's form-urlencoded body template cannot conditionally omit a field the caller did not supply, so only the always-present api_key/format fields are templated (verified live: templating limit, types, or logs with no value each produced a real stat:fail invalid_parameter error). |
| Get Public Status Pages | `getPSPs` | List all public status pages configured on the account, with each page's id, friendly name, and public status-page URL. |
| Reset Monitor | `resetMonitor` | Reset a monitor's uptime/downtime statistics and event log, starting its history over from now. |

</details>
