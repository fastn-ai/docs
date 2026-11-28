---
description: "ipstack finds the location of an IP address. Look up any IP address or the caller's own IP."
hidden: true
---

# IPstack

<img src="../../.gitbook/assets/connectors/lg/ipstack.png" alt="IPstack logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ipstack.com](https://ipstack.com) |
| **Authentication** | API key |
| **Slug** | `ipstack` |

## Setup

Your customers enter their API key for IPstack when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect IPstack from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **IPstack**.
2. Select **Connect** on the IPstack card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use IPstack's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Requester IP Location</td><td><code>getRequesterIpLocation</code></td><td>Looks up real-time geolocation data for the IP address the API request originates from (the caller's own public IP). Returns location fields by default; hostname lookup and additional response language can be requested via optional parameters.</td></tr><tr><td>Look Up IP Address</td><td><code>lookUpIpAddress</code></td><td>Resolves one IPv4/IPv6 address, or up to 50 comma-separated addresses in a single bulk request, to geolocation data. A single address returns one result object; multiple comma-separated addresses return an array of result objects (Bulk Endpoint).</td></tr></tbody></table>

