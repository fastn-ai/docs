---
description: "Updown.io monitors website uptime. Create and manage checks, recipients and status pages, and read uptime metrics and downtime history."
hidden: true
---

# Updown.io

<img src="../../.gitbook/assets/connectors/lg/updown-io.png" alt="Updown.io logo">

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [updown.io](https://updown.io) |
| **Authentication** | API key |
| **Slug** | `updownIo` |

## Setup

Your customers enter their API key for Updown.io when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Updown.io from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Updown.io**.
2. Select **Connect** on the Updown.io card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Updown.io's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Check</td><td><code>createCheck</code></td><td>Create a new Updown.io check and immediately begin monitoring the given URL. Supports https, http, icmp, tcp, tcps and pulse checks. Returns the new check including its token. Requires a read-write API key.</td></tr><tr><td>Create Recipient</td><td><code>createRecipient</code></td><td>Add a new alert recipient to the Updown.io account. Only email, sms, webhook, slack_compatible and msteams can be created through the API; Slack, Telegram, Zapier and Statuspage integrations must be set up in the web UI. Creating a webhook recipient is how you subscribe an endpoint to the Updown.io push events. Returns the new (or already existing) recipient with its id. Requires a read-write API key.</td></tr><tr><td>Create Status Page</td><td><code>createStatusPage</code></td><td>Create a new Updown.io status page showing the given checks in order. Returns the new status page with its token and public URL. Requires a read-write API key.</td></tr><tr><td>Delete Check</td><td><code>deleteCheck</code></td><td>Permanently delete an Updown.io check by token, stopping its monitoring. Returns {"deleted": true} on success. Requires a read-write API key.</td></tr><tr><td>Delete Recipient</td><td><code>deleteRecipient</code></td><td>Delete an alert recipient from the Updown.io account by its id (e.g. webhook:1159873859 or email:3719031852). Returns {"deleted": true} on success. Requires a read-write API key.</td></tr><tr><td>Delete Status Page</td><td><code>deleteStatusPage</code></td><td>Permanently delete an Updown.io status page by token. Returns {"deleted": true} on success. Requires a read-write API key.</td></tr><tr><td>Get Check</td><td><code>getCheck</code></td><td>Fetch a single Updown.io check by its token.</td></tr><tr><td>Get Check Metrics</td><td><code>getCheckMetrics</code></td><td>Get aggregated performance metrics for an Updown.io check: uptime, APDEX, request counts bucketed by response time, and timing breakdown (redirect, DNS lookup, connection, TLS handshake, response, total) in milliseconds. Stats are aggregated hourly, by day after 2 days and by month after 40 days, so the range must span at least one hour. The uptime attribute is not returned when grouping.</td></tr><tr><td>List Check Downtimes</td><td><code>listCheckDowntimes</code></td><td>List all recorded downtimes of an Updown.io check, newest first, 100 per page. Each entry carries the downtime id, details URL, error reason, start and end timestamps, duration in seconds and whether it was partial.</td></tr><tr><td>List Checks</td><td><code>listChecks</code></td><td>List every monitoring check on your Updown.io account, including its token, monitored URL, current up/down state, uptime percentage, check interval, SSL certificate status and domain expiry information. Takes no parameters. Note that monitored URLs only include HTTP basic-auth credentials when a read-write API key is used.</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Node IPs</td><td><code>listNodeIps</code></td><td>List every Updown.io monitoring server IP address, both IPv4 and IPv6, as an array of strings. Useful for firewall allow-listing. Takes no parameters.</td></tr><tr><td>List Node IPv4 Addresses</td><td><code>listNodeIpv4</code></td><td>List the IPv4 addresses of all Updown.io monitoring servers as an array of strings. Useful for firewall allow-listing. Takes no parameters.</td></tr><tr><td>List Node IPv6 Addresses</td><td><code>listNodeIpv6</code></td><td>List the IPv6 addresses of all Updown.io monitoring servers as an array of strings. Useful for firewall allow-listing. Takes no parameters.</td></tr><tr><td>List Nodes</td><td><code>listNodes</code></td><td>List all Updown.io monitoring and webhook servers, keyed by short node name (e.g. tok, fra, mia). Each node carries its IPv4 and IPv6 address, city, country, country code, latitude and longitude. Takes no parameters.</td></tr><tr><td>List Recipients</td><td><code>listRecipients</code></td><td>List every alert recipient / notification channel on the Updown.io account - email, SMS, Slack, Telegram, webhook, Zapier and similar. Each entry gives the id (used to select recipients on a check), type, name and value. Takes no parameters.</td></tr><tr><td>List Status Pages</td><td><code>listStatusPages</code></td><td>List all Updown.io status pages on the account. Each page gives its token, public URL, name, description, visibility (public, protected or private), access key and the ordered list of check tokens it shows. Takes no parameters.</td></tr><tr><td>Update Check</td><td><code>updateCheck</code></td><td>Update an existing Updown.io check identified by its token. Only the fields you supply are changed. Returns the updated check. Requires a read-write API key.</td></tr><tr><td>Update Status Page</td><td><code>updateStatusPage</code></td><td>Update an existing Updown.io status page by token. Only the fields you supply are changed. Returns the updated status page. Requires a read-write API key.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Check Down</td><td><code>check.down</code></td><td>Fires when a check goes down, after confirmation from a second monitoring node. Payload is a JSON ARRAY of event objects; each carries event, time, description, the full check object and the downtime object.</td></tr><tr><td>Check Up</td><td><code>check.up</code></td><td>Fires when a check recovers after a check.down event. Payload is a JSON ARRAY; each element carries event, time, description, check and the now-closed downtime (ended_at and duration populated).</td></tr><tr><td>Performance Drop</td><td><code>check.performance_drop</code></td><td>Fires when the check's Apdex drops more than 30 percent below the lowest of the last 5 hours. Payload is a JSON ARRAY; each element carries event, time, description, check, apdex_dropped (a percentage string) and last_metrics keyed by hour.</td></tr><tr><td>SSL Certificate Expiring</td><td><code>check.ssl_expiration</code></td><td>Fires when the SSL certificate approaches its expiration date (30, 14, 7 and 1 day before for one-year certificates). Payload is a JSON ARRAY; each element carries event, time, description, check and an ssl object with the certificate and days_before_expiration.</td></tr><tr><td>SSL Certificate Invalid</td><td><code>check.ssl_invalid</code></td><td>Fires when the monitored host's SSL certificate is considered invalid. Payload is a JSON ARRAY; each element carries event, time, description, check and an ssl object holding cert (subject, issuer, from, to, algorithm) and error.</td></tr><tr><td>SSL Certificate Renewed</td><td><code>check.ssl_renewed</code></td><td>Fires when the SSL certificate is renewed close to expiration, recovering from check.ssl_expiration. Payload is a JSON ARRAY; each element carries event, time, description, check and an ssl object with old_cert and new_cert.</td></tr><tr><td>SSL Certificate Valid</td><td><code>check.ssl_valid</code></td><td>Fires when the SSL certificate becomes valid again after a check.ssl_invalid event. Payload is a JSON ARRAY; each element carries event, time, description, check and an ssl object.</td></tr></tbody></table>
