---
description: "The Rick and Morty API covers the TV show's characters, locations and episodes. List and look up characters, locations and episodes."
hidden: true
---

# Rick and Morty API

<img src="../../.gitbook/assets/connectors/lg/rick-and-morty-api.png" alt="Rick and Morty API logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [rickandmortyapi.com](https://rickandmortyapi.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `rickAndMortyApi` |

## Setup

Rick and Morty API needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Rick and Morty API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rickAndMortyApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Resources</td><td><code>getApiRoot</code></td><td>List the available REST resources and their URLs Docs: https://rickandmortyapi.com/documentation</td></tr><tr><td>Get Character</td><td><code>getCharacter</code></td><td>Get one character by id Docs: https://rickandmortyapi.com/documentation</td></tr><tr><td>Get Episode</td><td><code>getEpisode</code></td><td>Get one episode by id Docs: https://rickandmortyapi.com/documentation</td></tr><tr><td>Get Location</td><td><code>getLocation</code></td><td>Get one location by id Docs: https://rickandmortyapi.com/documentation</td></tr><tr><td>Get Multiple Characters</td><td><code>getMultipleCharacters</code></td><td>Get several characters at once by a comma-separated id list Docs: https://rickandmortyapi.com/documentation</td></tr><tr><td>Get Multiple Episodes</td><td><code>getMultipleEpisodes</code></td><td>Get several episodes at once by a comma-separated id list Docs: https://rickandmortyapi.com/documentation</td></tr><tr><td>Get Multiple Locations</td><td><code>getMultipleLocations</code></td><td>Get several locations at once by a comma-separated id list Docs: https://rickandmortyapi.com/documentation</td></tr><tr><td>List Characters</td><td><code>listCharacters</code></td><td>List characters, 20 per page, optionally filtered Filters combine; when nothing matches the API Docs: https://rickandmortyapi.com/documentation</td></tr><tr><td>List Episodes</td><td><code>listEpisodes</code></td><td>List episodes, 20 per page, optionally filtered Filters combine; when nothing matches the API Docs: https://rickandmortyapi.com/documentation</td></tr><tr><td>List Locations</td><td><code>listLocations</code></td><td>List locations, 20 per page, optionally filtered Filters combine; when nothing matches the API Docs: https://rickandmortyapi.com/documentation</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Run GraphQL Query</td><td><code>runGraphqlQuery</code></td><td>Run a GraphQL query against the Rick and Morty GraphQL endpoint Queries include characters, character, charactersByIds, locations, location, locationsByIds, episodes, episode and episodesByIds with page and filter arguments. Docs: https://rickandmortyapi.com/documentation</td></tr></tbody></table>

</details>

## Events

Rick and Morty API has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
