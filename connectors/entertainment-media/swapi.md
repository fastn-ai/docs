---
description: "SWAPI, the Star Wars API, is a free read-only API with Star Wars people, films, starships, vehicles, species and planets: list with search and pagination or…"
---

# SWAPI (Star Wars API)

SWAPI, the Star Wars API, is a free read-only API with Star Wars people, films, starships, vehicles, species and planets: list with search and pagination or get one by id, in JSON or Wookiee encoding. No API key needed (10,000 requests per day per IP).

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [swapi.dev](https://swapi.dev) |
| **Authentication** | No authentication |
| **Actions** | 13 |
| **Events** | 0 |
| **Slug** | `swapi` |

## Use it

Add SWAPI (Star Wars API) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.swapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get API Resources | `getApiRoot` | List every SWAPI resource and its root URL (GET /api/). Docs: https://swapi.dev/documentation |
| Get Film | `getFilm` | Get one film by id (GET /api/films/{id}/). Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation |
| Get Person | `getPerson` | Get one person by id (GET /api/people/{id}/). Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation |
| Get Planet | `getPlanet` | Get one planet by id (GET /api/planets/{id}/). Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation |
| Get Species | `getSpecies` | Get one species by id (GET /api/species/{id}/). Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation |
| Get Starship | `getStarship` | Get one starship by id (GET /api/starships/{id}/). Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation |
| Get Vehicle | `getVehicle` | Get one vehicle by id (GET /api/vehicles/{id}/). Unknown ids return 404 'Not found'. Docs: https://swapi.dev/documentation |
| List Films | `listFilms` | List films 10 per page, optionally filtered by a case-insensitive partial match on title (GET /api/films/). Docs: https://swapi.dev/documentation |
| List People | `listPeople` | List people 10 per page, optionally filtered by a case-insensitive partial match on name (GET /api/people/). Docs: https://swapi.dev/documentation |
| List Planets | `listPlanets` | List planets 10 per page, optionally filtered by a case-insensitive partial match on name (GET /api/planets/). Docs: https://swapi.dev/documentation |
| List Species | `listSpecies` | List species 10 per page, optionally filtered by a case-insensitive partial match on name (GET /api/species/). Docs: https://swapi.dev/documentation |
| List Starships | `listStarships` | List starships 10 per page, optionally filtered by a case-insensitive partial match on name or model (GET /api/starships/). Docs: https://swapi.dev/documentation |
| List Vehicles | `listVehicles` | List vehicles 10 per page, optionally filtered by a case-insensitive partial match on name or model (GET /api/vehicles/). Docs: https://swapi.dev/documentation |
