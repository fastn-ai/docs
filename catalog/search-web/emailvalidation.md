---
description: "emailvalidation.io validates email addresses. Check an address and view your account quota."
hidden: true
---

# emailvalidation

<img src="../../.gitbook/assets/connectors/lg/emailvalidation.png" alt="emailvalidation logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [emailvalidation.io](https://emailvalidation.io) |
| **Authentication** | API key |
| **Slug** | `emailvalidation` |

## Setup

Your customers enter their API key for emailvalidation when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect emailvalidation from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **emailvalidation**.
2. Select **Connect** on the emailvalidation card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use emailvalidation's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Account Quota Status</td><td><code>getAccountQuotaStatus</code></td><td>Returns the authenticated emailvalidation.io account's current monthly and grace quota usage (total, used, remaining) plus the account id. Free: requests to this endpoint do not count against your credit quota or rate limit. Use it before a batch of validations to check remaining credits.</td></tr><tr><td>List MCP Tools</td><td><code>listMcpTools</code></td><td>Discovery call against emailvalidation.io's Model Context Protocol endpoint (POST https://api.emailvalidation.io/mcp, JSON-RPC 2.0 tools/list). Returns the machine-readable tool catalogue the vendor exposes - getInfo and getStatus - with their input schemas. Free: does not consume a validation credit. Useful to confirm the vendor's live surface has not changed; the two REST actions on this connector cover both tools.</td></tr><tr><td>Validate Email Address</td><td><code>validateEmailAddress</code></td><td>Validates a single email address and returns deliverability signals: format_valid, mx_found, smtp_check, role, disposable, free, did_you_mean typo suggestion, a quality score (0-1), and an overall state (deliverable / undeliverable / risky / unknown) with a reason. METERED: each call consumes one credit from the account's monthly quota (check it first with Get Account Quota Status). Pass catch_all="1" to additionally run a catch-all domain check; that option is a paid-plan feature and on a free plan Omit catch_all and the catch_all response field is null.</td></tr></tbody></table>

