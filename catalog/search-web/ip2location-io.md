---
description: "IP2Location.io looks up where an IP address is located. Get geolocation for one or many IP addresses."
hidden: true
---

# IP2Location.io

<img src="../../.gitbook/assets/connectors/lg/ip2location-io.png" alt="IP2Location.io logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ip2location.io](https://ip2location.io) |
| **Authentication** | API key |
| **Slug** | `ip2locationIo` |

## Setup

Your customers enter their API key for IP2Location.io when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect IP2Location.io from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **IP2Location.io**.
2. Select **Connect** on the IP2Location.io card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use IP2Location.io's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Bulk IP Geolocation</td><td><code>bulkIpGeolocation</code></td><td>Looks up the geolocation of up to 1,000 IPv4 or IPv6 addresses in a single request and returns a result object keyed by IP address, optionally limited to selected fields. This endpoint requires a paid IP2Location.io plan; free-plan keys receive error 401 'Bulk lookup is not available with your plan'.</td></tr><tr><td>Get IP Geolocation</td><td><code>getIpGeolocation</code></td><td>Looks up the geolocation of an IPv4 or IPv6 address, returning country, region, city, ZIP code, latitude and longitude, time zone, ASN and proxy indicator. Higher plans add ISP, domain, usage type, mobile carrier, continent, country, region, city and time-zone objects, AS details, full proxy and threat flags, fraud score, advertising category and district. Translations via the lang parameter require the Plus plan or above.</td></tr></tbody></table>

