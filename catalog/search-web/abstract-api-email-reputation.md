---
description: "AbstractAPI Email Reputation checks an email address. Get its deliverability, quality score, risk and known data breaches."
hidden: true
---

# AbstractAPI Email Reputation

<img src="../../.gitbook/assets/connectors/lg/abstract-api-email-reputation.png" alt="AbstractAPI Email Reputation logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiEmailReputation` |

## Setup

Your customers enter their API key for AbstractAPI Email Reputation when they connect. Nothing else needs setting up.

## Use it

Add AbstractAPI Email Reputation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiEmailReputation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Check Email Reputation</td><td><code>checkEmailReputation</code></td><td>Validates and enriches an email address, returning deliverability status, MX/SMTP checks, a quality score, sender and domain details, risk status, and any known data breaches associated with the address.</td></tr></tbody></table>

## Events

AbstractAPI Email Reputation has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
