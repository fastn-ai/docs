---
description: "SWAPI, the Star Wars API, is a free read-only API with Star Wars people, films, starships, vehicles, species and planets: list with search and pagination or…"
hidden: true
---

# SWAPI (Star Wars API)

<img src="../../.gitbook/assets/connectors/lg/swapi.png" alt="SWAPI (Star Wars API) logo">

SWAPI, the Star Wars API, is a free read-only API with Star Wars people, films, starships, vehicles, species and planets: list with search and pagination or get one by id, in JSON or Wookiee encoding. No API key needed (10,000 requests per day per IP).

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [swapi.dev](https://swapi.dev) |
| **Authentication** | No authentication |
| **Slug** | `swapi` |

## Use it

Add SWAPI (Star Wars API) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.swapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Resources</td><td><code>getApiRoot</code></td><td>List every SWAPI resource and its root URL (GET /api/). Docs: https://swapi.dev/documentation</td></tr><tr><td>Get Film</td><td><code>getFilm</code></td><td>Get one film by id (GET /api/films/{id}/). Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation</td></tr><tr><td>Get Person</td><td><code>getPerson</code></td><td>Get one person by id (GET /api/people/{id}/). Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation</td></tr><tr><td>Get Planet</td><td><code>getPlanet</code></td><td>Get one planet by id (GET /api/planets/{id}/). Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation</td></tr><tr><td>Get Species</td><td><code>getSpecies</code></td><td>Get one species by id (GET /api/species/{id}/). Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation</td></tr><tr><td>Get Starship</td><td><code>getStarship</code></td><td>Get one starship by id (GET /api/starships/{id}/). Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation</td></tr><tr><td>Get Vehicle</td><td><code>getVehicle</code></td><td>Get one vehicle by id (GET /api/vehicles/{id}/). Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation</td></tr><tr><td>List Films</td><td><code>listFilms</code></td><td>List films 10 per page, optionally filtered by a case-insensitive partial match on title (GET /api/films/). Docs: https://swapi.dev/documentation</td></tr><tr><td>List People</td><td><code>listPeople</code></td><td>List people 10 per page, optionally filtered by a case-insensitive partial match on name (GET /api/people/). Docs: https://swapi.dev/documentation</td></tr><tr><td>List Planets</td><td><code>listPlanets</code></td><td>List planets 10 per page, optionally filtered by a case-insensitive partial match on name (GET /api/planets/). Docs: https://swapi.dev/documentation</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Species</td><td><code>listSpecies</code></td><td>List species 10 per page, optionally filtered by a case-insensitive partial match on name (GET /api/species/). Docs: https://swapi.dev/documentation</td></tr><tr><td>List Starships</td><td><code>listStarships</code></td><td>List starships 10 per page, optionally filtered by a case-insensitive partial match on name or model (GET /api/starships/). Docs: https://swapi.dev/documentation</td></tr><tr><td>List Vehicles</td><td><code>listVehicles</code></td><td>List vehicles 10 per page, optionally filtered by a case-insensitive partial match on name or model (GET /api/vehicles/). Docs: https://swapi.dev/documentation</td></tr></tbody></table>

</details>
