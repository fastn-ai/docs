---
description: "emailvalidation.io real-time email address validation."
hidden: true
---

# emailvalidation

<img src="../../.gitbook/assets/connectors/lg/emailvalidation.png" alt="emailvalidation logo">

emailvalidation.io real-time email address validation. Validates a single email address and returns syntax, MX, SMTP, disposable, role, free-provider, catch-all and quality-score signals, plus account quota status. Metered: each validation consumes one credit; /v1/status is free.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [emailvalidation.io](https://emailvalidation.io) |
| **Authentication** | API key |
| **Slug** | `emailvalidation` |

## Use it

Add emailvalidation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.emailvalidation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Account Quota Status | `getAccountQuotaStatus` | Returns the authenticated emailvalidation.io account's current monthly and grace quota usage (total, used, remaining) plus the account id. Free: requests to this endpoint do not count against your credit quota or rate limit. Use it before a batch of validations to check remaining credits. |
| List MCP Tools | `listMcpTools` | Discovery call against emailvalidation.io's Model Context Protocol endpoint (POST https://api.emailvalidation.io/mcp, JSON-RPC 2.0 tools/list). Returns the machine-readable tool catalogue the vendor exposes - getInfo and getStatus - with their input schemas. Free: does not consume a validation credit. Useful to confirm the vendor's live surface has not changed; the two REST actions on this connector cover both tools. |
| Validate Email Address | `validateEmailAddress` | Validates a single email address and returns deliverability signals: format_valid, mx_found, smtp_check, role, disposable, free, did_you_mean typo suggestion, a quality score (0-1), and an overall state (deliverable / undeliverable / risky / unknown) with a reason. METERED: each call consumes one credit from the account's monthly quota (check it first with Get Account Quota Status). Pass catch_all="1" to additionally run a catch-all domain check; that option is a paid-plan feature and on a free plan returns HTTP 200 with the body {"error":{"code":235,"type":"catch_all_not_allowed"}} while still consuming a credit. Omit catch_all and the catch_all response field is null. |
