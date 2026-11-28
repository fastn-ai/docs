---
description: "Positionstack is a geocoding service. Convert addresses to coordinates and coordinates to addresses, one at a time or in batches."
hidden: true
---

# Positionstack

<img src="../../.gitbook/assets/connectors/lg/positionstack.png" alt="Positionstack logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [positionstack.com](https://positionstack.com) |
| **Authentication** | API key |
| **Slug** | `positionstack` |

## Setup

Your customers enter their API key for Positionstack when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Positionstack from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Positionstack**.
2. Select **Connect** on the Positionstack card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Positionstack's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Forward Geocoding</td><td><code>forwardGeocode</code></td><td>Converts an address or place name into geographic coordinates (latitude/longitude). Available on the free plan.</td></tr><tr><td>Forward Geocoding Batch</td><td><code>forwardGeocodeBatch</code></td><td>Converts up to 50 addresses/place names into coordinates in a single call. Positionstack restricts batch requests to paid subscription plans only - on the free plan this returns a plan-restriction error (function_access_restricted).</td></tr><tr><td>Reverse Geocoding</td><td><code>reverseGeocode</code></td><td>Converts a coordinate pair (latitude, longitude) into a human-readable address. Available on the free plan.</td></tr><tr><td>Reverse Geocoding Batch</td><td><code>reverseGeocodeBatch</code></td><td>Converts up to 50 coordinate pairs into addresses in a single call. Positionstack restricts batch requests to paid subscription plans only - on the free plan this returns a plan-restriction error (function_access_restricted).</td></tr></tbody></table>

