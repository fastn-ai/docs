---
description: "Updown.io website and uptime monitoring."
hidden: true
---

# Updown.io

Updown.io website and uptime monitoring. Create and manage HTTP/HTTPS, ICMP, TCP and pulse checks, read uptime metrics and downtime history, manage alert recipients and public status pages, and list the monitoring node IP addresses.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [updown.io](https://updown.io) |
| **Authentication** | API key |
| **Actions** | 18 |
| **Events** | 7 |
| **Slug** | `updownIo` |

## Use it

Add Updown.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.updownIo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Check | `createCheck` | Create a new Updown.io check and immediately begin monitoring the given URL. Supports https, http, icmp, tcp, tcps and pulse checks. Returns the new check including its token. Requires a read-write API key. |
| Create Recipient | `createRecipient` | Add a new alert recipient to the Updown.io account. Only email, sms, webhook, slack_compatible and msteams can be created through the API; Slack, Telegram, Zapier and Statuspage integrations must be set up in the web UI. Creating a webhook recipient is how you subscribe an endpoint to the Updown.io push events. Returns the new (or already existing) recipient with its id. Requires a read-write API key. |
| Create Status Page | `createStatusPage` | Create a new Updown.io status page showing the given checks in order. Returns the new status page with its token and public URL. Requires a read-write API key. |
| Delete Check | `deleteCheck` | Permanently delete an Updown.io check by token, stopping its monitoring. Returns {"deleted": true} on success. Requires a read-write API key. |
| Delete Recipient | `deleteRecipient` | Delete an alert recipient from the Updown.io account by its id (e.g. webhook:1159873859 or email:3719031852). Returns {"deleted": true} on success. Requires a read-write API key. |
| Delete Status Page | `deleteStatusPage` | Permanently delete an Updown.io status page by token. Returns {"deleted": true} on success. Requires a read-write API key. |
| Get Check | `getCheck` | Fetch a single Updown.io check by its token. |
| Get Check Metrics | `getCheckMetrics` | Get aggregated performance metrics for an Updown.io check: uptime, APDEX, request counts bucketed by response time, and timing breakdown (redirect, DNS lookup, connection, TLS handshake, response, total) in milliseconds. Stats are aggregated hourly, by day after 2 days and by month after 40 days, so the range must span at least one hour. The uptime attribute is not returned when grouping. |
| List Check Downtimes | `listCheckDowntimes` | List all recorded downtimes of an Updown.io check, newest first, 100 per page. Each entry carries the downtime id, details URL, error reason, start and end timestamps, duration in seconds and whether it was partial. |
| List Checks | `listChecks` | List every monitoring check on your Updown.io account, including its token, monitored URL, current up/down state, uptime percentage, check interval, SSL certificate status and domain expiry information. Takes no parameters. Note that monitored URLs only include HTTP basic-auth credentials when a read-write API key is used. |
| List Node IPs | `listNodeIps` | List every Updown.io monitoring server IP address, both IPv4 and IPv6, as an array of strings. Useful for firewall allow-listing. Takes no parameters. |
| List Node IPv4 Addresses | `listNodeIpv4` | List the IPv4 addresses of all Updown.io monitoring servers as an array of strings. Useful for firewall allow-listing. Takes no parameters. |
| List Node IPv6 Addresses | `listNodeIpv6` | List the IPv6 addresses of all Updown.io monitoring servers as an array of strings. Useful for firewall allow-listing. Takes no parameters. |
| List Nodes | `listNodes` | List all Updown.io monitoring and webhook servers, keyed by short node name (e.g. tok, fra, mia). Each node carries its IPv4 and IPv6 address, city, country, country code, latitude and longitude. Takes no parameters. |
| List Recipients | `listRecipients` | List every alert recipient / notification channel on the Updown.io account - email, SMS, Slack, Telegram, webhook, Zapier and similar. Each entry gives the id (used to select recipients on a check), type, name and value. Takes no parameters. |
| List Status Pages | `listStatusPages` | List all Updown.io status pages on the account. Each page gives its token, public URL, name, description, visibility (public, protected or private), access key and the ordered list of check tokens it shows. Takes no parameters. |
| Update Check | `updateCheck` | Update an existing Updown.io check identified by its token. Only the fields you supply are changed. Returns the updated check. Requires a read-write API key. |
| Update Status Page | `updateStatusPage` | Update an existing Updown.io status page by token. Only the fields you supply are changed. Returns the updated status page. Requires a read-write API key. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Check Down | `check.down` | Fires when a check goes down, after confirmation from a second monitoring node. Payload is a JSON ARRAY of event objects; each carries event, time, description, the full check object and the downtime object. payloadSchema MODELLED from the vendor's documented sample at https://updown.io/api (no signed delivery could be captured in this environment). |
| Check Up | `check.up` | Fires when a check recovers after a check.down event. Payload is a JSON ARRAY; each element carries event, time, description, check and the now-closed downtime (ended_at and duration populated). payloadSchema MODELLED from the vendor's documented sample at https://updown.io/api. |
| Performance Drop | `check.performance_drop` | Fires when the check's Apdex drops more than 30 percent below the lowest of the last 5 hours. Payload is a JSON ARRAY; each element carries event, time, description, check, apdex_dropped (a percentage string) and last_metrics keyed by hour. payloadSchema MODELLED from the vendor's documented sample at https://updown.io/api. |
| SSL Certificate Expiring | `check.ssl_expiration` | Fires when the SSL certificate approaches its expiration date (30, 14, 7 and 1 day before for one-year certificates). Payload is a JSON ARRAY; each element carries event, time, description, check and an ssl object with the certificate and days_before_expiration. payloadSchema MODELLED from the vendor's documented sample at https://updown.io/api. |
| SSL Certificate Invalid | `check.ssl_invalid` | Fires when the monitored host's SSL certificate is considered invalid. Payload is a JSON ARRAY; each element carries event, time, description, check and an ssl object holding cert (subject, issuer, from, to, algorithm) and error. payloadSchema MODELLED from the vendor's documented sample at https://updown.io/api. |
| SSL Certificate Renewed | `check.ssl_renewed` | Fires when the SSL certificate is renewed close to expiration, recovering from check.ssl_expiration. Payload is a JSON ARRAY; each element carries event, time, description, check and an ssl object with old_cert and new_cert. payloadSchema MODELLED from the vendor's documented sample at https://updown.io/api. |
| SSL Certificate Valid | `check.ssl_valid` | Fires when the SSL certificate becomes valid again after a check.ssl_invalid event. Payload is a JSON ARRAY; each element carries event, time, description, check and an ssl object. payloadSchema MODELLED from the vendor's documented sample at https://updown.io/api. |
