---
description: "Open Brewery DB is a free dataset of breweries worldwide. List, search and get breweries, or pick random ones."
hidden: true
---

# Open Brewery DB

<img src="../../.gitbook/assets/connectors/lg/open-brewery-db.png" alt="Open Brewery DB logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [openbrewerydb.org](https://openbrewerydb.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `openBreweryDb` |

## Setup

Open Brewery DB needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Open Brewery DB from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Open Brewery DB**.
2. Select **Connect** on the Open Brewery DB card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Open Brewery DB needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Open Brewery DB's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Brewery</td><td><code>getBrewery</code></td><td>Returns one brewery by its Open Brewery DB id: name, type, address, coordinates, phone and website. Docs: https://www.openbrewerydb.org/documentation</td></tr><tr><td>Get Brewery Metadata</td><td><code>getBreweryMetadata</code></td><td>Returns the total count of breweries matching the same filters as List Breweries, with counts by state and type. Docs: https://www.openbrewerydb.org/documentation</td></tr><tr><td>Get Random Breweries</td><td><code>getRandomBreweries</code></td><td>Returns one or more random breweries. Docs: https://www.openbrewerydb.org/documentation</td></tr><tr><td>List Breweries</td><td><code>listBreweries</code></td><td>Lists breweries with filters by city, country, distance, ids, name, state, postal code and type, sorted and paged. Docs: https://www.openbrewerydb.org/documentation</td></tr><tr><td>Search Breweries</td><td><code>searchBreweries</code></td><td>Searches breweries by a partial, case-insensitive name match. Docs: https://www.openbrewerydb.org/documentation</td></tr></tbody></table>

