---
description: "verifi.email is an email validation and deliverability API."
hidden: true
---

# verifi.email

<img src="../../.gitbook/assets/connectors/lg/verifi-email.png" alt="verifi.email logo">

verifi.email is an email validation and deliverability API. This connector wraps the live verifi.email REST API at https://api.verifi.email: real-time validation of a single email address (RFC compliance, MX record, spoof-free, disposable detection), bulk validation of many addresses in one request (JSON array or comma-separated list), and a domain email-authentication health check that scores SPF, DKIM, DMARC and BIMI and returns actionable recommendations.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [verifi.email](https://verifi.email) |
| **Authentication** | API key |
| **Slug** | `verifiEmail` |

## Use it

Add verifi.email from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.verifiEmail.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Domain Email Health</td><td><code>checkDomainEmailHealth</code></td><td>Assess a sending domain's email-authentication health with verifi.email. Returns a per-protocol breakdown for SPF, DKIM, DMARC and BIMI - whether each record exists, the policy in force, the raw DNS records, a score against a target score, and a written recommendation - plus an overall grade. Use it to audit deliverability posture before a sending campaign. Pass the bare domain without a scheme or www prefix.</td></tr><tr><td>Validate Email Address</td><td><code>validateEmailAddress</code></td><td>Validate a single email address with verifi.email and return its deliverability verdict: RFC compliance, whether the domain has a valid MX record, whether the domain is spoof-free, whether the address belongs to a disposable-email provider, and the detected MX provider and records. Consumes one verification credit per call. The same handler is also reachable at the API root (GET https://api.verifi.email/), which is an alias of this route and needs no separate action. NOTE: the published docs at https://verifi.email/docs describe this route as GET /v1/validate; that path does not exist on the live API, which serves it at GET /check.</td></tr><tr><td>Validate Emails In Bulk</td><td><code>validateEmailsInBulk</code></td><td>Validate many email addresses in one verifi.email request by POSTing them as a JSON array. Returns one validation result per address, in the order supplied, each with the same deliverability detail as the single-address check. Consumes one verification credit per address. Use the 'Validate Emails In Bulk From List' action instead when the addresses are more convenient as a comma-separated string.</td></tr><tr><td>Validate Emails In Bulk From List</td><td><code>validateEmailsInBulkFromList</code></td><td>Validate many email addresses in one verifi.email request by passing them as a single comma-separated string on the query string, the GET form of the bulk check. Returns one validation result per address, in the order supplied. Consumes one verification credit per address. Prefer 'Validate Emails In Bulk' for long lists, because a very long query string can exceed the server's URL length limit.</td></tr></tbody></table>
