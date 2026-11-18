---
description: "Open Brewery DB is a free, keyless dataset of breweries, cideries, brewpubs and bottle shops worldwide: list and filter breweries by city, state, country,…"
---

# Open Brewery DB

Open Brewery DB is a free, keyless dataset of breweries, cideries, brewpubs and bottle shops worldwide: list and filter breweries by city, state, country, postal code, type, name or distance, search by name, get one brewery or random ones, and count matches.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [openbrewerydb.org](https://openbrewerydb.org) |
| **Authentication** | No authentication |
| **Actions** | 5 |
| **Events** | 0 |
| **Slug** | `openBreweryDb` |

## Use it

Add Open Brewery DB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openBreweryDb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Brewery | `getBrewery` | Returns one brewery by its Open Brewery DB id: name, type, address, coordinates, phone and website. Docs: https://www.openbrewerydb.org/documentation |
| Get Brewery Metadata | `getBreweryMetadata` | Returns the total count of breweries matching the same filters as List Breweries, with counts by state and type. Docs: https://www.openbrewerydb.org/documentation |
| Get Random Breweries | `getRandomBreweries` | Returns one or more random breweries. Docs: https://www.openbrewerydb.org/documentation |
| List Breweries | `listBreweries` | Lists breweries with filters by city, country, distance, ids, name, state, postal code and type, sorted and paged. Docs: https://www.openbrewerydb.org/documentation |
| Search Breweries | `searchBreweries` | Searches breweries by a partial, case-insensitive name match. Docs: https://www.openbrewerydb.org/documentation |
