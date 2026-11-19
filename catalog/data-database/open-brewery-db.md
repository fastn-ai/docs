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

## Use it

Add Open Brewery DB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openBreweryDb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Brewery</td><td><code>getBrewery</code></td><td>Returns one brewery by its Open Brewery DB id: name, type, address, coordinates, phone and website. Docs: https://www.openbrewerydb.org/documentation</td></tr><tr><td>Get Brewery Metadata</td><td><code>getBreweryMetadata</code></td><td>Returns the total count of breweries matching the same filters as List Breweries, with counts by state and type. Docs: https://www.openbrewerydb.org/documentation</td></tr><tr><td>Get Random Breweries</td><td><code>getRandomBreweries</code></td><td>Returns one or more random breweries. Docs: https://www.openbrewerydb.org/documentation</td></tr><tr><td>List Breweries</td><td><code>listBreweries</code></td><td>Lists breweries with filters by city, country, distance, ids, name, state, postal code and type, sorted and paged. Docs: https://www.openbrewerydb.org/documentation</td></tr><tr><td>Search Breweries</td><td><code>searchBreweries</code></td><td>Searches breweries by a partial, case-insensitive name match. Docs: https://www.openbrewerydb.org/documentation</td></tr></tbody></table>

## Events

Open Brewery DB has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
