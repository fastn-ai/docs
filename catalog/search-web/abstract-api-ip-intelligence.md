---
description: "AbstractAPI IP Intelligence looks up an IP address. Get its location, internet provider, company, timezone and security threat signals."
hidden: true
---

# AbstractAPI IP Intelligence

<img src="../../.gitbook/assets/connectors/lg/abstract-api-ip-intelligence.png" alt="AbstractAPI IP Intelligence logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | API key |
| **Slug** | `abstractApiIpIntelligence` |

## Setup

Your customers enter their API key for AbstractAPI IP Intelligence when they connect. Nothing else needs setting up.

## Use it

Add AbstractAPI IP Intelligence from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiIpIntelligence.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get IP Intelligence</td><td><code>getIpIntelligence</code></td><td>Looks up an IPv4 or IPv6 address (or the caller's own public IP when none is given) and returns its security signals (VPN/proxy/Tor/hosting/relay/mobile/abuse), ASN and company/ISP details, associated domains, geolocation, timezone, country flag, and currency.</td></tr></tbody></table>

## Events

AbstractAPI IP Intelligence has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
