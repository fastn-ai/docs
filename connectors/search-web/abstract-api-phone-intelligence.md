---
description: "AbstractAPI Phone Intelligence validates a phone number and returns its formatting, carrier, line type, location, messaging, registration, and risk/breach…"
hidden: true
---

# AbstractAPI Phone Intelligence

<img src="../../.gitbook/assets/connectors/abstract-api-phone-intelligence.png" alt="AbstractAPI Phone Intelligence logo" width="64">

AbstractAPI Phone Intelligence validates a phone number and returns its formatting, carrier, line type, location, messaging, registration, and risk/breach data in a single lookup.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `abstractApiPhoneIntelligence` |

## Use it

Add AbstractAPI Phone Intelligence from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiPhoneIntelligence.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Validate Phone Number | `validatePhoneNumber` | Validates and enriches a phone number, returning its formatting, carrier and line type, geographic location, SMS messaging address, registration name, risk level, and any known data breaches associated with it. |
