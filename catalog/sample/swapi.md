---
description: "SWAPI is a free Star Wars database. List and look up films, people, planets, species, starships and vehicles."
hidden: true
---

# SWAPI (Star Wars API)

<img src="../../.gitbook/assets/connectors/lg/swapi.png" alt="SWAPI (Star Wars API) logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [swapi.dev](https://swapi.dev) |
| **Authentication** | No sign-in needed |
| **Slug** | `swapi` |

## Setup

SWAPI (Star Wars API) needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect SWAPI (Star Wars API) from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **SWAPI (Star Wars API)**.
2. Select **Connect** on the SWAPI (Star Wars API) card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. SWAPI (Star Wars API) needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use SWAPI (Star Wars API)'s actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Resources</td><td><code>getApiRoot</code></td><td>List every SWAPI resource and its root URL Docs: https://swapi.dev/documentation</td></tr><tr><td>Get Film</td><td><code>getFilm</code></td><td>Get one film by id Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation</td></tr><tr><td>Get Person</td><td><code>getPerson</code></td><td>Get one person by id Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation</td></tr><tr><td>Get Planet</td><td><code>getPlanet</code></td><td>Get one planet by id Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation</td></tr><tr><td>Get Species</td><td><code>getSpecies</code></td><td>Get one species by id Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation</td></tr><tr><td>Get Starship</td><td><code>getStarship</code></td><td>Get one starship by id Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation</td></tr><tr><td>Get Vehicle</td><td><code>getVehicle</code></td><td>Get one vehicle by id Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation</td></tr><tr><td>List Films</td><td><code>listFilms</code></td><td>List films 10 per page, optionally filtered by a case-insensitive partial match on title Docs: https://swapi.dev/documentation</td></tr><tr><td>List People</td><td><code>listPeople</code></td><td>List people 10 per page, optionally filtered by a case-insensitive partial match on name Docs: https://swapi.dev/documentation</td></tr><tr><td>List Planets</td><td><code>listPlanets</code></td><td>List planets 10 per page, optionally filtered by a case-insensitive partial match on name Docs: https://swapi.dev/documentation</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Species</td><td><code>listSpecies</code></td><td>List species 10 per page, optionally filtered by a case-insensitive partial match on name Docs: https://swapi.dev/documentation</td></tr><tr><td>List Starships</td><td><code>listStarships</code></td><td>List starships 10 per page, optionally filtered by a case-insensitive partial match on name or model Docs: https://swapi.dev/documentation</td></tr><tr><td>List Vehicles</td><td><code>listVehicles</code></td><td>List vehicles 10 per page, optionally filtered by a case-insensitive partial match on name or model Docs: https://swapi.dev/documentation</td></tr></tbody></table>

</details>

