---
description: "Placekey is a universal identifier for physical places. Get a Placekey for an address or point of interest, one at a time or in bulk."
hidden: true
---

# Placekey

<img src="../../.gitbook/assets/connectors/lg/placekey.png" alt="Placekey logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [placekey.io](https://placekey.io) |
| **Authentication** | API key |
| **Slug** | `placekey` |

## Setup

Your customers enter their API key for Placekey when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Placekey from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Placekey**.
2. Select **Connect** on the Placekey card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Placekey's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Placekey</td><td><code>getPlacekey</code></td><td>Resolves a single place to its Placekey identifier. Supply an address, a point-of-interest name with its address, or a latitude and longitude pair. Coordinates alone return only the "Where" part of the Placekey; an address is required to receive the full What@Where format. Optional enrichment fields such as the address Placekey, building Placekey, match confidence, normalized address, geocode, RESO UPI, parcel number, census GEOID and Overture Maps GERS identifier can be requested through the options field.</td></tr><tr><td>Get Placekeys In Bulk</td><td><code>getPlacekeysInBulk</code></td><td>Resolves up to 100 places to their Placekey identifiers in a single request. Every query in the batch must share the same ISO country code. Each query may carry its own query_id which is echoed back so results can be matched to inputs. The options field is set once at the top level and applies to every query in the batch. Placekey returns results as a JSON array in the same order as the submitted queries.</td></tr></tbody></table>

