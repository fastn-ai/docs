---
description: "IPinfo provides IP address data. Look up location, hostname and network details for an IP, your own IP, a network or a batch."
hidden: true
---

# IPinfo

<img src="../../.gitbook/assets/connectors/lg/ipinfo.png" alt="IPinfo logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ipinfo.io](https://ipinfo.io) |
| **Authentication** | Access token |
| **Slug** | `ipinfo` |

## Setup

Your customers enter their access token for IPinfo when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect IPinfo from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **IPinfo**.
2. Select **Connect** on the IPinfo card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use IPinfo's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Lookup IP Addresses</td><td><code>batchLookupIpAddresses</code></td><td>Looks up up to 1000 IP addresses in a single call and returns a map of each IP to its geolocation and network details. Optionally drops entries with no data via the filter parameter.</td></tr><tr><td>Lookup ASN</td><td><code>lookupAsn</code></td><td>Returns details for an Autonomous System Number (ASN), including the organization name, allocated IP prefixes, registry, country, and domain. This is a paid-plan feature on IPinfo - accounts on the free Lite plan receive a 401 'Token does not have access to this API' response.</td></tr><tr><td>Lookup IP Address</td><td><code>lookupIpAddress</code></td><td>Returns geolocation and network details for a specific IPv4 or IPv6 address, including city, region, country, coordinates, hostname, timezone, and the organization/ASN operating it.</td></tr><tr><td>Lookup My IP Address</td><td><code>lookupMyIpAddress</code></td><td>Returns geolocation and network details for the caller's own public IP address, as seen by IPinfo, including city, region, country, coordinates, hostname, timezone, and the organization/ASN operating it.</td></tr></tbody></table>

