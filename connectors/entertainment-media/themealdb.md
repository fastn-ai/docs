---
description: "TheMealDB is an open, crowd-sourced database of recipes from around the world."
hidden: true
---

# TheMealDB

<img src="../../.gitbook/assets/connectors/themealdb.png" alt="TheMealDB logo" width="64">

TheMealDB is an open, crowd-sourced database of recipes from around the world. Search meals by name or first letter, look up full recipes with ingredients and instructions, get a random meal, filter by ingredient, category or area, and list categories, areas and ingredients. Use API key 1 (free developer test key) or your own supporter key.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [themealdb.com](https://themealdb.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `themealdb` |

## Use it

Add TheMealDB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.themealdb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Filter Meals by Area | `filterByArea` | List meals from an area (cuisine) (GET /filter.php?a=). Docs: https://www.themealdb.com/api.php |
| Filter Meals by Category | `filterByCategory` | List meals in a category (GET /filter.php?c=). Docs: https://www.themealdb.com/api.php |
| Filter Meals by Ingredient | `filterByMainIngredient` | List meals that use an ingredient (GET /filter.php?i=). Use underscores for spaces, e.g. chicken_breast. Multi-ingredient filtering needs a premium key. Docs: https://www.themealdb.com/api.php |
| Get Meal | `getMeal` | Get full details of one meal by id (GET /lookup.php?i=). Docs: https://www.themealdb.com/api.php |
| Get Random Meal | `getRandomMeal` | Get one random meal with full details (GET /random.php). Docs: https://www.themealdb.com/api.php |
| List Areas | `listAreas` | List all areas (cuisines) with their country (GET /list.php?a=list). Docs: https://www.themealdb.com/api.php |
| List Categories | `listCategories` | List all meal categories with description and image (GET /categories.php). Docs: https://www.themealdb.com/api.php |
| List Category Names | `listCategoryNames` | List the names of all meal categories (GET /list.php?c=list). Docs: https://www.themealdb.com/api.php |
| List Ingredients | `listIngredients` | List all ingredients with id and description (GET /list.php?i=list). Docs: https://www.themealdb.com/api.php |
| List Meals by First Letter | `listMealsByFirstLetter` | List all meals whose name starts with a letter, with full details (GET /search.php?f=). Docs: https://www.themealdb.com/api.php |

<details>

<summary>See 1 more action</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Search Meals by Name | `searchMealsByName` | Search meals by name and get full details (GET /search.php?s=). Docs: https://www.themealdb.com/api.php |

</details>
