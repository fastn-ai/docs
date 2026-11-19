---
description: "Connect AbstractAPI Email Reputation to your product with fastn."
hidden: true
---

# AbstractAPI Email Reputation

<img src="../../.gitbook/assets/connectors/lg/abstract-api-email-reputation.png" alt="AbstractAPI Email Reputation logo">

AbstractAPI Email Reputation validates and enriches an email address, returning deliverability, domain, sender, quality-score, risk, and known-breach data in a single lookup.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `abstractApiEmailReputation` |

## Use it

Add AbstractAPI Email Reputation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiEmailReputation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Email Reputation</td><td><code>checkEmailReputation</code></td><td>Validates and enriches an email address, returning deliverability status, MX/SMTP checks, a quality score, sender and domain details, risk status, and any known data breaches associated with the address.</td></tr></tbody></table>
