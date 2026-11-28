---
description: "Open-Elevation is a free elevation service. Look up the ground elevation for any latitude and longitude."
hidden: true
---

# Open-Elevation

<img src="../../.gitbook/assets/connectors/lg/open-elevation.png" alt="Open-Elevation logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [open-elevation.com](https://open-elevation.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `openElevation` |

## Setup

Open-Elevation needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Open-Elevation from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Open-Elevation**.
2. Select **Connect** on the Open-Elevation card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Open-Elevation needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Open-Elevation's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Lookup Elevation</td><td><code>lookupElevation</code></td><td>Get the elevation in metres for one or more latitude/longitude points,lng|lat,lng). The GET request line is limited to 1024 bytes - use Lookup Elevation (POST) for many points. Invalid input Docs: https://github.com/Jorl17/open-elevation/blob/master/docs/api.md</td></tr><tr><td>Lookup Elevation (POST)</td><td><code>lookupElevationPost</code></td><td>Get the elevation in metres for a list of points sent as JSON - no size limit on the request Docs: https://github.com/Jorl17/open-elevation/blob/master/docs/api.md</td></tr></tbody></table>

