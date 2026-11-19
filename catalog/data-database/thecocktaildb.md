---
description: "TheCocktailDB is an open database of drinks and cocktails. Search cocktails, get recipes and ingredients and filter by category or glass."
hidden: true
---

# TheCocktailDB

<img src="../../.gitbook/assets/connectors/lg/thecocktaildb.png" alt="TheCocktailDB logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [thecocktaildb.com](https://thecocktaildb.com) |
| **Authentication** | API key |
| **Slug** | `thecocktaildb` |

## Setup

Your customers enter their API key for TheCocktailDB when they connect. Nothing else needs setting up.

## Use it

Add TheCocktailDB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.thecocktaildb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Filter Cocktails by Alcoholic</td><td><code>filterByAlcoholic</code></td><td>List cocktails by alcohol content Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Filter Cocktails by Category</td><td><code>filterByCategory</code></td><td>List cocktails in a category Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Filter Cocktails by Glass</td><td><code>filterByGlass</code></td><td>List cocktails served in a glass type Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Filter Cocktails by Ingredient</td><td><code>filterByIngredient</code></td><td>List cocktails that use an ingredient Use underscores for spaces, e.g. Dry_Vermouth. Multi-ingredient filtering needs a premium key. Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Get Cocktail</td><td><code>getCocktail</code></td><td>Get full details of one cocktail by id Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Get Ingredient</td><td><code>getIngredient</code></td><td>Get one ingredient by id Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Get Random Cocktail</td><td><code>getRandomCocktail</code></td><td>Get one random cocktail with full details Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>List Alcoholic Filters</td><td><code>listAlcoholicFilters</code></td><td>List the alcoholic filter values Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>List Categories</td><td><code>listCategoryNames</code></td><td>List all cocktail category names Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>List Cocktails by First Letter</td><td><code>listCocktailsByFirstLetter</code></td><td>List all cocktails whose name starts with a letter, with full details Docs: https://www.thecocktaildb.com/api.php</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Glasses</td><td><code>listGlasses</code></td><td>List all glass types Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>List Ingredients</td><td><code>listIngredients</code></td><td>List all ingredient names Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Search Cocktails by Name</td><td><code>searchCocktailsByName</code></td><td>Search cocktails by name and get full details Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Search Ingredients by Name</td><td><code>searchIngredientsByName</code></td><td>Search ingredients by name and get description, type and alcohol details Docs: https://www.thecocktaildb.com/api.php</td></tr></tbody></table>

</details>

## Events

TheCocktailDB has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
