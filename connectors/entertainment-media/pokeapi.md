---
description: "PokeAPI (pokeapi.co) is a free, fully keyless RESTful API providing comprehensive Pokemon data - species, moves, abilities, types, items, berries, locations,…"
hidden: true
---

# PokeAPI

<img src="../../.gitbook/assets/connectors/pokeapi.png" alt="PokeAPI logo" width="64">

PokeAPI (pokeapi.co) is a free, fully keyless RESTful API providing comprehensive Pokemon data - species, moves, abilities, types, items, berries, locations, evolution chains, games, and more. Read-only (GET), no authentication or API key required.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [pokeapi.co](https://pokeapi.co) |
| **Authentication** | No authentication |
| **Slug** | `pokeapi` |

## Use it

Add PokeAPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pokeapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Ability | `getAbility` | Returns data for a single Pokemon ability by name or ID, including its effect text, the generation it was introduced in, and which Pokemon can have it. |
| Get Berry | `getBerry` | Returns data for a single berry by name or ID, including growth time, harvest yield, firmness, flavor potencies, and the item/natural-gift data associated with it. |
| Get Egg Group | `getEggGroup` | Returns data for a single Pokemon egg group by name or ID, including the list of Pokemon species that belong to it (used for breeding compatibility). |
| Get Encounter Method | `getEncounterMethod` | Returns data for a single wild Pokemon encounter method by name or ID (e.g. walk, surf, old-rod), including its ordering value used to sort encounter methods. |
| Get Evolution Chain | `getEvolutionChain` | Returns the full evolution chain tree for a chain ID (found via Get Pokemon Species' evolution_chain.url), showing the baby-trigger item if any and the recursive evolves_to structure with each stage's species and evolution trigger details. |
| Get Generation | `getGeneration` | Returns data for a single game generation by name or ID, including its main region and the abilities, moves, Pokemon species, types, and version groups introduced in it. |
| Get Growth Rate | `getGrowthRate` | Returns data for a single Pokemon growth rate by name or ID, including its experience formula, the experience-to-level table, and which Pokemon species use it. |
| Get Item | `getItem` | Returns data for a single game item by name or ID, including cost, fling power/effect, category, effect text, sprites, and which Pokemon are found holding it. |
| Get Location | `getLocation` | Returns data for a single in-game location by name or ID, including its region and the location areas within it. |
| Get Move | `getMove` | Returns data for a single Pokemon move by name or ID, including power, accuracy, PP, priority, damage class, type, target, effect text, and battle metadata (ailment, crit rate, drain, healing). |

<details>

<summary>See 14 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Nature | `getNature` | Returns data for a single Pokemon nature by name or ID, including which stat it increases/decreases and its berry flavor preferences. |
| Get Pokedex | `getPokedex` | Returns data for a single regional or national Pokedex by name or ID, including whether it is part of the main series, its region, and the full list of Pokemon species entries with their entry numbers. |
| Get Pokemon | `getPokemon` | Returns detailed data for a single Pokemon by name or numeric Pokedex ID, including base stats, types, abilities, held items, moves, sprites, and a reference to its species. |
| Get Pokemon Species | `getPokemonSpecies` | Returns species-level data for a Pokemon by name or ID - evolution chain reference, habitat, color, shape, growth rate, egg groups, capture rate, and localized flavor text describing the species. |
| Get Region | `getRegion` | Returns data for a single game region by name or ID, including its locations, main generation, Pokedexes, and version groups. |
| Get Type | `getType` | Returns data for a single Pokemon elemental type by name or ID, including its damage relations (what it is strong/weak/immune to and from) and the Pokemon and moves of that type. |
| List Abilities | `listAbilities` | Returns a paginated list of Pokemon ability names and resource URLs. Use limit and offset to page through all abilities. |
| List Berries | `listBerries` | Returns a paginated list of berry names and resource URLs. Use limit and offset to page through all berries. |
| List Items | `listItems` | Returns a paginated list of game item names and resource URLs. Use limit and offset to page through all items. |
| List Locations | `listLocations` | Returns a paginated list of in-game location names and resource URLs. Use limit and offset to page through all locations. |
| List Moves | `listMoves` | Returns a paginated list of Pokemon move names and resource URLs. Use limit and offset to page through all moves. |
| List Pokemon | `listPokemon` | Returns a paginated list of Pokemon names and resource URLs. Use limit and offset to page through the full National Pokedex. |
| List Regions | `listRegions` | Returns a paginated list of game region names and resource URLs (e.g. Kanto, Johto, Hoenn). |
| List Types | `listTypes` | Returns a paginated list of the 18 (plus special) Pokemon elemental type names and resource URLs. |

</details>
