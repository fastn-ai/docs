---
description: "AbstractAPI Phone Intelligence validates a phone number. Get its format, carrier, line type, location and risk signals."
hidden: true
---

# AbstractAPI Phone Intelligence

<img src="../../.gitbook/assets/connectors/lg/abstract-api-phone-intelligence.png" alt="AbstractAPI Phone Intelligence logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiPhoneIntelligence` |

## Setup

Your customers enter their API key for AbstractAPI Phone Intelligence when they connect. Nothing else needs setting up.

## Use it

Add AbstractAPI Phone Intelligence from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiPhoneIntelligence.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Validate Phone Number</td><td><code>validatePhoneNumber</code></td><td>Validates and enriches a phone number, returning its formatting, carrier and line type, geographic location, SMS messaging address, registration name, risk level, and any known data breaches associated with it.</td></tr></tbody></table>

## Events

AbstractAPI Phone Intelligence has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
