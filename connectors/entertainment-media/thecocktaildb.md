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

| Action | Slug | What it does |
| --- | --- | --- |
| Filter Cocktails by Alcoholic | `filterByAlcoholic` | List cocktails by alcohol content (GET /filter.php?a=). Docs: https://www.thecocktaildb.com/api.php |
| Filter Cocktails by Category | `filterByCategory` | List cocktails in a category (GET /filter.php?c=). Docs: https://www.thecocktaildb.com/api.php |
| Filter Cocktails by Glass | `filterByGlass` | List cocktails served in a glass type (GET /filter.php?g=). Docs: https://www.thecocktaildb.com/api.php |
| Filter Cocktails by Ingredient | `filterByIngredient` | List cocktails that use an ingredient (GET /filter.php?i=). Use underscores for spaces, e.g. Dry_Vermouth. Multi-ingredient filtering needs a premium key. Docs: https://www.thecocktaildb.com/api.php |
| Get Cocktail | `getCocktail` | Get full details of one cocktail by id (GET /lookup.php?i=). Docs: https://www.thecocktaildb.com/api.php |
| Get Ingredient | `getIngredient` | Get one ingredient by id (GET /lookup.php?iid=). Docs: https://www.thecocktaildb.com/api.php |
| Get Random Cocktail | `getRandomCocktail` | Get one random cocktail with full details (GET /random.php). Docs: https://www.thecocktaildb.com/api.php |
| List Alcoholic Filters | `listAlcoholicFilters` | List the alcoholic filter values (GET /list.php?a=list). Docs: https://www.thecocktaildb.com/api.php |
| List Categories | `listCategoryNames` | List all cocktail category names (GET /list.php?c=list). Docs: https://www.thecocktaildb.com/api.php |
| List Cocktails by First Letter | `listCocktailsByFirstLetter` | List all cocktails whose name starts with a letter, with full details (GET /search.php?f=). Docs: https://www.thecocktaildb.com/api.php |
| List Glasses | `listGlasses` | List all glass types (GET /list.php?g=list). Docs: https://www.thecocktaildb.com/api.php |
| List Ingredients | `listIngredients` | List all ingredient names (GET /list.php?i=list). Docs: https://www.thecocktaildb.com/api.php |
| Search Cocktails by Name | `searchCocktailsByName` | Search cocktails by name and get full details (GET /search.php?s=). Docs: https://www.thecocktaildb.com/api.php |
| Search Ingredients by Name | `searchIngredientsByName` | Search ingredients by name and get description, type and alcohol details (GET /search.php?i=). Docs: https://www.thecocktaildb.com/api.php |
