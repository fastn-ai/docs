---
description: "Open Food Facts is a free, open database of food products. Search products, get a product by barcode and read nutrient and taxonomy data."
hidden: true
---

# Open Food Facts

<img src="../../.gitbook/assets/connectors/lg/open-food-facts.png" alt="Open Food Facts logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [openfoodfacts.org](https://openfoodfacts.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `openFoodFacts` |

## Setup

Open Food Facts needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Open Food Facts from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openFoodFacts.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Autocomplete Taxonomy</td><td><code>autocompleteTaxonomy</code></td><td>Autocompletes taxonomy entries (categories, labels, brands, ingredients...) for a typed prefix. Docs: https://search.openfoodfacts.org/docs</td></tr><tr><td>Canonicalize Taxonomy Tags</td><td><code>canonicalizeTags</code></td><td>Converts local-language tag names into canonical taxonomy tag ids (e.g. 'chocolat' -&gt; en:chocolates). Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/</td></tr><tr><td>Full-Text Search Products</td><td><code>fullTextSearchProducts</code></td><td>Full-text searches products with Lucene query syntax (e.g. 'orange juice', brands:ferrero, nutriscore_grade:a) on the Open Food Facts search service, with sorting, facets and paging. Docs: https://search.openfoodfacts.org/docs</td></tr><tr><td>Get Nutrients List</td><td><code>getNutrients</code></td><td>Returns the list of nutrients (with units and display order) used in nutrition facts tables for a country and language. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/</td></tr><tr><td>Get Product</td><td><code>getProduct</code></td><td>Returns a product by barcode (API v2): name, brands, quantity, ingredients, nutrition facts, Nutri-Score, NOVA group, allergens, packaging, images. status 1 = found, 0 = not found. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/</td></tr><tr><td>Get Product (API v3)</td><td><code>getProductV3</code></td><td>Returns a product by barcode using API v3, with structured status, warnings and errors. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/</td></tr><tr><td>Get Product Search Document</td><td><code>getSearchDocument</code></td><td>Returns the indexed search document of one product (by barcode) from the Open Food Facts search service. Docs: https://search.openfoodfacts.org/docs</td></tr><tr><td>Get Tag Knowledge Panels</td><td><code>getTagKnowledgePanels</code></td><td>Returns knowledge panels for a tag (e.g. packaging statistics for a category). Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/</td></tr><tr><td>Get Tag Suggestions</td><td><code>getSuggestions</code></td><td>Returns taxonomy entries of a tag type that contain a term (autocomplete for categories, labels, packaging shapes...). Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/</td></tr><tr><td>Get Taxonomy Display Tags</td><td><code>getDisplayTags</code></td><td>Returns display names in a language for canonical taxonomy tag ids. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/</td></tr></tbody></table>

<details>

<summary>View 7 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Taxonomy Suggestions</td><td><code>getTaxonomySuggestions</code></td><td>Returns taxonomy suggestions for a tag type, optionally filtered by a starting string, categories or packaging shape. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/</td></tr><tr><td>List Attribute Groups</td><td><code>listAttributeGroups</code></td><td>Returns the product attribute groups (nutritional quality, allergens, processing, labels, environment) used for personal search scoring. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/</td></tr><tr><td>List Attribute Groups (API v3.4)</td><td><code>listAttributeGroupsV3</code></td><td>Returns attribute groups and attributes using API v3.4. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/</td></tr><tr><td>List External Knowledge Panel Sources</td><td><code>listExternalSources</code></td><td>Returns the external knowledge panel sources configured on the server. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/</td></tr><tr><td>List Preference Weights</td><td><code>listPreferences</code></td><td>Returns the importance levels (not important, important, very important, mandatory) and their weights used to compute personal product scores. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/</td></tr><tr><td>List Preference Weights (API v3)</td><td><code>listPreferencesV3</code></td><td>Returns the preference importance values using API v3. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/</td></tr><tr><td>Search Products</td><td><code>searchProducts</code></td><td>Searches products by tag filters (category, brand, label, country, Nutri-Score...), sorted and paged. Limited to 10 requests per minute. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/</td></tr></tbody></table>

</details>

## Events

Open Food Facts has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
