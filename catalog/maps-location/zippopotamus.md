---
description: "Zippopotam.us is a free postal code lookup for over 60 countries. Find the places for a postal code or the postal codes for a city."
hidden: true
---

# Zippopotam.us

<img src="../../.gitbook/assets/connectors/lg/zippopotamus.png" alt="Zippopotam.us logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [zippopotam.us](https://zippopotam.us) |
| **Authentication** | No sign-in needed |
| **Slug** | `zippopotamus` |

## Setup

Zippopotam.us needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Zippopotam.us from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Zippopotam.us**.
2. Select **Connect** on the Zippopotam.us card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Zippopotam.us needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Zippopotam.us's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Look Up City Postal Codes</td><td><code>lookupCity</code></td><td>Returns the postal codes and coordinates of a city in a state/region of a country. Docs: https://docs.zippopotam.us/docs/getting-started/</td></tr><tr><td>Look Up Postal Code</td><td><code>lookupPostalCode</code></td><td>Returns the places (name, state, latitude, longitude) for a postal code in a country. Docs: https://docs.zippopotam.us/docs/getting-started/</td></tr></tbody></table>

