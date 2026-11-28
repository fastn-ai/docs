---
description: "TheMealDB is an open database of recipes from around the world. Search meals, get recipes and filter by area, category or ingredient."
hidden: true
---

# TheMealDB

<img src="../../.gitbook/assets/connectors/lg/themealdb.png" alt="TheMealDB logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [themealdb.com](https://themealdb.com) |
| **Authentication** | API key |
| **Slug** | `themealdb` |

## Setup

Your customers enter their API key for TheMealDB when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect TheMealDB from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **TheMealDB**.
2. Select **Connect** on the TheMealDB card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use TheMealDB's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Filter Meals by Area</td><td><code>filterByArea</code></td><td>List meals from an area (cuisine) Docs: https://www.themealdb.com/api.php</td></tr><tr><td>Filter Meals by Category</td><td><code>filterByCategory</code></td><td>List meals in a category Docs: https://www.themealdb.com/api.php</td></tr><tr><td>Filter Meals by Ingredient</td><td><code>filterByMainIngredient</code></td><td>List meals that use an ingredient Use underscores for spaces, e.g. chicken_breast. Multi-ingredient filtering needs a premium key. Docs: https://www.themealdb.com/api.php</td></tr><tr><td>Get Meal</td><td><code>getMeal</code></td><td>Get full details of one meal by id Docs: https://www.themealdb.com/api.php</td></tr><tr><td>Get Random Meal</td><td><code>getRandomMeal</code></td><td>Get one random meal with full details Docs: https://www.themealdb.com/api.php</td></tr><tr><td>List Areas</td><td><code>listAreas</code></td><td>List all areas (cuisines) with their country Docs: https://www.themealdb.com/api.php</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>List all meal categories with description and image Docs: https://www.themealdb.com/api.php</td></tr><tr><td>List Category Names</td><td><code>listCategoryNames</code></td><td>List the names of all meal categories Docs: https://www.themealdb.com/api.php</td></tr><tr><td>List Ingredients</td><td><code>listIngredients</code></td><td>List all ingredients with id and description Docs: https://www.themealdb.com/api.php</td></tr><tr><td>List Meals by First Letter</td><td><code>listMealsByFirstLetter</code></td><td>List all meals whose name starts with a letter, with full details Docs: https://www.themealdb.com/api.php</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Meals by Name</td><td><code>searchMealsByName</code></td><td>Search meals by name and get full details Docs: https://www.themealdb.com/api.php</td></tr></tbody></table>

</details>

