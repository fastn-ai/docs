---
description: "Connect AbstractAPI IP Intelligence to your product with fastn."
hidden: true
---

# AbstractAPI IP Intelligence

<img src="../../.gitbook/assets/connectors/lg/abstract-api-ip-intelligence.png" alt="AbstractAPI IP Intelligence logo">

AbstractAPI IP Intelligence maps an IPv4 or IPv6 address (or the caller's own IP) to geolocation, ISP/company, security threat signals, timezone, and currency data.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [abstractapi.com](https://abstractapi.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `abstractApiIpIntelligence` |

## Use it

Add AbstractAPI IP Intelligence from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.abstractApiIpIntelligence.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get IP Intelligence</td><td><code>getIpIntelligence</code></td><td>Looks up an IPv4 or IPv6 address (or the caller's own public IP when none is given) and returns its security signals (VPN/proxy/Tor/hosting/relay/mobile/abuse), ASN and company/ISP details, associated domains, geolocation, timezone, country flag, and currency.</td></tr></tbody></table>
