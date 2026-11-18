---
description: "AbstractAPI Email Reputation validates and enriches an email address, returning deliverability, domain, sender, quality-score, risk, and known-breach data in…"
hidden: true
---

# AbstractAPI Email Reputation

AbstractAPI Email Reputation validates and enriches an email address, returning deliverability, domain, sender, quality-score, risk, and known-breach data in a single lookup.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 1 |
| **Events** | 0 |
| **Slug** | `abstractApiEmailReputation` |

## Use it

Add AbstractAPI Email Reputation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiEmailReputation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Email Reputation | `checkEmailReputation` | Validates and enriches an email address, returning deliverability status, MX/SMTP checks, a quality score, sender and domain details, risk status, and any known data breaches associated with the address. |
