---
description: "TheCocktailDB is an open, crowd-sourced database of drinks and cocktails."
hidden: true
---

# TheCocktailDB

<img src="../../.gitbook/assets/connectors/lg/thecocktaildb.png" alt="TheCocktailDB logo">

TheCocktailDB is an open, crowd-sourced database of drinks and cocktails. Search cocktails by name or first letter, look up full recipes, search and look up ingredients, get a random cocktail, filter by ingredient, alcohol, category or glass, and list categories, glasses, ingredients and alcohol filters. Use API key 1 (free developer test key) or your own supporter key.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [thecocktaildb.com](https://thecocktaildb.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `thecocktaildb` |

## Use it

Add TheCocktailDB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.thecocktaildb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Filter Cocktails by Alcoholic</td><td><code>filterByAlcoholic</code></td><td>List cocktails by alcohol content (GET /filter.php?a=). Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Filter Cocktails by Category</td><td><code>filterByCategory</code></td><td>List cocktails in a category (GET /filter.php?c=). Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Filter Cocktails by Glass</td><td><code>filterByGlass</code></td><td>List cocktails served in a glass type (GET /filter.php?g=). Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Filter Cocktails by Ingredient</td><td><code>filterByIngredient</code></td><td>List cocktails that use an ingredient (GET /filter.php?i=). Use underscores for spaces, e.g. Dry_Vermouth. Multi-ingredient filtering needs a premium key. Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Get Cocktail</td><td><code>getCocktail</code></td><td>Get full details of one cocktail by id (GET /lookup.php?i=). Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Get Ingredient</td><td><code>getIngredient</code></td><td>Get one ingredient by id (GET /lookup.php?iid=). Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Get Random Cocktail</td><td><code>getRandomCocktail</code></td><td>Get one random cocktail with full details (GET /random.php). Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>List Alcoholic Filters</td><td><code>listAlcoholicFilters</code></td><td>List the alcoholic filter values (GET /list.php?a=list). Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>List Categories</td><td><code>listCategoryNames</code></td><td>List all cocktail category names (GET /list.php?c=list). Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>List Cocktails by First Letter</td><td><code>listCocktailsByFirstLetter</code></td><td>List all cocktails whose name starts with a letter, with full details (GET /search.php?f=). Docs: https://www.thecocktaildb.com/api.php</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Glasses</td><td><code>listGlasses</code></td><td>List all glass types (GET /list.php?g=list). Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>List Ingredients</td><td><code>listIngredients</code></td><td>List all ingredient names (GET /list.php?i=list). Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Search Cocktails by Name</td><td><code>searchCocktailsByName</code></td><td>Search cocktails by name and get full details (GET /search.php?s=). Docs: https://www.thecocktaildb.com/api.php</td></tr><tr><td>Search Ingredients by Name</td><td><code>searchIngredientsByName</code></td><td>Search ingredients by name and get description, type and alcohol details (GET /search.php?i=). Docs: https://www.thecocktaildb.com/api.php</td></tr></tbody></table>

</details>
