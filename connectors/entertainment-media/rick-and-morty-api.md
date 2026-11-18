---
description: "The Rick and Morty API is a free REST and GraphQL API with every character, location and episode of the Rick and Morty TV show: list with filters and…"
hidden: true
---

# Rick and Morty API

<img src="../../.gitbook/assets/connectors/lg/rick-and-morty-api.png" alt="Rick and Morty API logo">

The Rick and Morty API is a free REST and GraphQL API with every character, location and episode of the Rick and Morty TV show: list with filters and pagination, get one or many by id, or run GraphQL queries. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [rickandmortyapi.com](https://rickandmortyapi.com) |
| **Authentication** | No authentication |
| **Slug** | `rickAndMortyApi` |

## Use it

Add Rick and Morty API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rickAndMortyApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get API Resources | `getApiRoot` | List the available REST resources and their URLs (GET /api). Docs: https://rickandmortyapi.com/documentation |
| Get Character | `getCharacter` | Get one character by id (GET /api/character/{id}). Docs: https://rickandmortyapi.com/documentation |
| Get Episode | `getEpisode` | Get one episode by id (GET /api/episode/{id}). Docs: https://rickandmortyapi.com/documentation |
| Get Location | `getLocation` | Get one location by id (GET /api/location/{id}). Docs: https://rickandmortyapi.com/documentation |
| Get Multiple Characters | `getMultipleCharacters` | Get several characters at once by a comma-separated id list (GET /api/character/{ids}). Docs: https://rickandmortyapi.com/documentation |
| Get Multiple Episodes | `getMultipleEpisodes` | Get several episodes at once by a comma-separated id list (GET /api/episode/{ids}). Docs: https://rickandmortyapi.com/documentation |
| Get Multiple Locations | `getMultipleLocations` | Get several locations at once by a comma-separated id list (GET /api/location/{ids}). Docs: https://rickandmortyapi.com/documentation |
| List Characters | `listCharacters` | List characters, 20 per page, optionally filtered (GET /api/character). Filters combine; when nothing matches the API returns 404 with error 'There is nothing here'. Docs: https://rickandmortyapi.com/documentation |
| List Episodes | `listEpisodes` | List episodes, 20 per page, optionally filtered (GET /api/episode). Filters combine; when nothing matches the API returns 404 with error 'There is nothing here'. Docs: https://rickandmortyapi.com/documentation |
| List Locations | `listLocations` | List locations, 20 per page, optionally filtered (GET /api/location). Filters combine; when nothing matches the API returns 404 with error 'There is nothing here'. Docs: https://rickandmortyapi.com/documentation |

<details>

<summary>See 1 more action</summary>

* **Run GraphQL Query** `runGraphqlQuery`: Run a GraphQL query against the Rick and Morty GraphQL endpoint (POST /graphql). Queries include characters, character, charactersByIds, locations, location, locationsByIds, episodes, episode and episodesByIds with page and filter arguments. Docs: https://rickandmortyapi.com/documentation

</details>
