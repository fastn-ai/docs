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

## Connect in Fastn

Your customers connect AbstractAPI IP Intelligence from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AbstractAPI IP Intelligence**.
2. Select **Connect** on the AbstractAPI IP Intelligence card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AbstractAPI IP Intelligence's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get IP Intelligence</td><td><code>getIpIntelligence</code></td><td>Looks up an IPv4 or IPv6 address (or the caller's own public IP when none is given) and returns its security signals (VPN/proxy/Tor/hosting/relay/mobile/abuse), ASN and company/ISP details, associated domains, geolocation, timezone, country flag, and currency.</td></tr></tbody></table>

