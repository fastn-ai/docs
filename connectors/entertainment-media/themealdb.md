---
description: "TheMealDB is an open, crowd-sourced database of recipes from around the world."
hidden: true
---

# TheMealDB

<img src="../../.gitbook/assets/connectors/lg/themealdb.png" alt="TheMealDB logo">

Search meals by name or first letter, look up full recipes with ingredients and instructions, get a random meal, filter by ingredient, category or area, and list categories, areas and ingredients. Use API key 1 (free developer test key) or your own supporter key.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [themealdb.com](https://themealdb.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `themealdb` |

## Use it

Add TheMealDB from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.themealdb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Filter Meals by Area</td><td><code>filterByArea</code></td><td>List meals from an area (cuisine) (GET /filter.php?a=). Docs: https://www.themealdb.com/api.php</td></tr><tr><td>Filter Meals by Category</td><td><code>filterByCategory</code></td><td>List meals in a category (GET /filter.php?c=). Docs: https://www.themealdb.com/api.php</td></tr><tr><td>Filter Meals by Ingredient</td><td><code>filterByMainIngredient</code></td><td>List meals that use an ingredient (GET /filter.php?i=). Use underscores for spaces, e.g. chicken_breast. Multi-ingredient filtering needs a premium key. Docs: https://www.themealdb.com/api.php</td></tr><tr><td>Get Meal</td><td><code>getMeal</code></td><td>Get full details of one meal by id (GET /lookup.php?i=). Docs: https://www.themealdb.com/api.php</td></tr><tr><td>Get Random Meal</td><td><code>getRandomMeal</code></td><td>Get one random meal with full details (GET /random.php). Docs: https://www.themealdb.com/api.php</td></tr><tr><td>List Areas</td><td><code>listAreas</code></td><td>List all areas (cuisines) with their country (GET /list.php?a=list). Docs: https://www.themealdb.com/api.php</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>List all meal categories with description and image (GET /categories.php). Docs: https://www.themealdb.com/api.php</td></tr><tr><td>List Category Names</td><td><code>listCategoryNames</code></td><td>List the names of all meal categories (GET /list.php?c=list). Docs: https://www.themealdb.com/api.php</td></tr><tr><td>List Ingredients</td><td><code>listIngredients</code></td><td>List all ingredients with id and description (GET /list.php?i=list). Docs: https://www.themealdb.com/api.php</td></tr><tr><td>List Meals by First Letter</td><td><code>listMealsByFirstLetter</code></td><td>List all meals whose name starts with a letter, with full details (GET /search.php?f=). Docs: https://www.themealdb.com/api.php</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Meals by Name</td><td><code>searchMealsByName</code></td><td>Search meals by name and get full details (GET /search.php?s=). Docs: https://www.themealdb.com/api.php</td></tr></tbody></table>

</details>
