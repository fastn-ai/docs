---
description: "CityBikes is an open data service for bike sharing. List bike share networks worldwide and get live station availability."
hidden: true
---

# CityBikes

<img src="../../.gitbook/assets/connectors/lg/city-bikes.png" alt="CityBikes logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [citybik.es](https://citybik.es) |
| **Authentication** | No sign-in needed |
| **Slug** | `cityBikes` |

## Setup

CityBikes needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect CityBikes from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **CityBikes**.
2. Select **Connect** on the CityBikes card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. CityBikes needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use CityBikes's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Bike Share Network</td><td><code>getNetwork</code></td><td>Get one bike sharing network with live station availability (free bikes, empty slots) and free-floating vehicles Unknown ids return 404 'Not Found'. Large networks can return several hundred KB - use fields to limit it. Docs: https://api.citybik.es/v2/</td></tr><tr><td>List Bike Share Networks</td><td><code>listNetworks</code></td><td>List every bike sharing network CityBikes tracks (about 800 systems worldwide) with id, name, operator and location Use fields to trim the response. Docs: https://api.citybik.es/v2/</td></tr></tbody></table>

