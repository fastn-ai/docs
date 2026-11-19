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

## Use it

Add emailvalidation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.emailvalidation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Account Quota Status</td><td><code>getAccountQuotaStatus</code></td><td>Returns the authenticated emailvalidation.io account's current monthly and grace quota usage (total, used, remaining) plus the account id. Free: requests to this endpoint do not count against your credit quota or rate limit. Use it before a batch of validations to check remaining credits.</td></tr><tr><td>List MCP Tools</td><td><code>listMcpTools</code></td><td>Discovery call against emailvalidation.io's Model Context Protocol endpoint (POST https://api.emailvalidation.io/mcp, JSON-RPC 2.0 tools/list). Returns the machine-readable tool catalogue the vendor exposes - getInfo and getStatus - with their input schemas. Free: does not consume a validation credit. Useful to confirm the vendor's live surface has not changed; the two REST actions on this connector cover both tools.</td></tr><tr><td>Validate Email Address</td><td><code>validateEmailAddress</code></td><td>Validates a single email address and returns deliverability signals: format_valid, mx_found, smtp_check, role, disposable, free, did_you_mean typo suggestion, a quality score (0-1), and an overall state (deliverable / undeliverable / risky / unknown) with a reason. METERED: each call consumes one credit from the account's monthly quota (check it first with Get Account Quota Status). Pass catch_all="1" to additionally run a catch-all domain check; that option is a paid-plan feature and on a free plan Omit catch_all and the catch_all response field is null.</td></tr></tbody></table>

## Events

emailvalidation has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
