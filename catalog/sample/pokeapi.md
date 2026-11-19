---
description: "PokeAPI is a free database of Pokemon data. Look up abilities, berries, items, evolution chains, generations and more."
hidden: true
---

# PokeAPI

<img src="../../.gitbook/assets/connectors/lg/pokeapi.png" alt="PokeAPI logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [pokeapi.co](https://pokeapi.co) |
| **Authentication** | No sign-in needed |
| **Slug** | `pokeapi` |

## Setup

PokeAPI needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add PokeAPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pokeapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Ability</td><td><code>getAbility</code></td><td>Returns data for a single Pokemon ability by name or ID, including its effect text, the generation it was introduced in, and which Pokemon can have it.</td></tr><tr><td>Get Berry</td><td><code>getBerry</code></td><td>Returns data for a single berry by name or ID, including growth time, harvest yield, firmness, flavor potencies, and the item/natural-gift data associated with it.</td></tr><tr><td>Get Egg Group</td><td><code>getEggGroup</code></td><td>Returns data for a single Pokemon egg group by name or ID, including the list of Pokemon species that belong to it (used for breeding compatibility).</td></tr><tr><td>Get Encounter Method</td><td><code>getEncounterMethod</code></td><td>Returns data for a single wild Pokemon encounter method by name or ID (e.g. walk, surf, old-rod), including its ordering value used to sort encounter methods.</td></tr><tr><td>Get Evolution Chain</td><td><code>getEvolutionChain</code></td><td>Returns the full evolution chain tree for a chain ID (found via Get Pokemon Species' evolution_chain.url), showing the baby-trigger item if any and the recursive evolves_to structure with each stage's species and evolution trigger details.</td></tr><tr><td>Get Generation</td><td><code>getGeneration</code></td><td>Returns data for a single game generation by name or ID, including its main region and the abilities, moves, Pokemon species, types, and version groups introduced in it.</td></tr><tr><td>Get Growth Rate</td><td><code>getGrowthRate</code></td><td>Returns data for a single Pokemon growth rate by name or ID, including its experience formula, the experience-to-level table, and which Pokemon species use it.</td></tr><tr><td>Get Item</td><td><code>getItem</code></td><td>Returns data for a single game item by name or ID, including cost, fling power/effect, category, effect text, sprites, and which Pokemon are found holding it.</td></tr><tr><td>Get Location</td><td><code>getLocation</code></td><td>Returns data for a single in-game location by name or ID, including its region and the location areas within it.</td></tr><tr><td>Get Move</td><td><code>getMove</code></td><td>Returns data for a single Pokemon move by name or ID, including power, accuracy, PP, priority, damage class, type, target, effect text, and battle metadata (ailment, crit rate, drain, healing).</td></tr></tbody></table>

<details>

<summary>View 14 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Nature</td><td><code>getNature</code></td><td>Returns data for a single Pokemon nature by name or ID, including which stat it increases/decreases and its berry flavor preferences.</td></tr><tr><td>Get Pokedex</td><td><code>getPokedex</code></td><td>Returns data for a single regional or national Pokedex by name or ID, including whether it is part of the main series, its region, and the full list of Pokemon species entries with their entry numbers.</td></tr><tr><td>Get Pokemon</td><td><code>getPokemon</code></td><td>Returns detailed data for a single Pokemon by name or numeric Pokedex ID, including base stats, types, abilities, held items, moves, sprites, and a reference to its species.</td></tr><tr><td>Get Pokemon Species</td><td><code>getPokemonSpecies</code></td><td>Returns species-level data for a Pokemon by name or ID - evolution chain reference, habitat, color, shape, growth rate, egg groups, capture rate, and localized flavor text describing the species.</td></tr><tr><td>Get Region</td><td><code>getRegion</code></td><td>Returns data for a single game region by name or ID, including its locations, main generation, Pokedexes, and version groups.</td></tr><tr><td>Get Type</td><td><code>getType</code></td><td>Returns data for a single Pokemon elemental type by name or ID, including its damage relations (what it is strong/weak/immune to and from) and the Pokemon and moves of that type.</td></tr><tr><td>List Abilities</td><td><code>listAbilities</code></td><td>Returns a paginated list of Pokemon ability names and resource URLs. Use limit and offset to page through all abilities.</td></tr><tr><td>List Berries</td><td><code>listBerries</code></td><td>Returns a paginated list of berry names and resource URLs. Use limit and offset to page through all berries.</td></tr><tr><td>List Items</td><td><code>listItems</code></td><td>Returns a paginated list of game item names and resource URLs. Use limit and offset to page through all items.</td></tr><tr><td>List Locations</td><td><code>listLocations</code></td><td>Returns a paginated list of in-game location names and resource URLs. Use limit and offset to page through all locations.</td></tr><tr><td>List Moves</td><td><code>listMoves</code></td><td>Returns a paginated list of Pokemon move names and resource URLs. Use limit and offset to page through all moves.</td></tr><tr><td>List Pokemon</td><td><code>listPokemon</code></td><td>Returns a paginated list of Pokemon names and resource URLs. Use limit and offset to page through the full National Pokedex.</td></tr><tr><td>List Regions</td><td><code>listRegions</code></td><td>Returns a paginated list of game region names and resource URLs (e.g. Kanto, Johto, Hoenn).</td></tr><tr><td>List Types</td><td><code>listTypes</code></td><td>Returns a paginated list of the 18 (plus special) Pokemon elemental type names and resource URLs.</td></tr></tbody></table>

</details>

## Events

PokeAPI has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
