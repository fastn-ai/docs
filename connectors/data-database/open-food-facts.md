---
description: "Open Food Facts is a free, open database of 3M+ food products from around the world."
hidden: true
---

# Open Food Facts

<img src="../../.gitbook/assets/connectors/lg/open-food-facts.png" alt="Open Food Facts logo">

Open Food Facts is a free, open database of 3M+ food products from around the world. Read-only keyless access: look up products by barcode (ingredients, nutrition facts, Nutri-Score, NOVA, allergens, packaging, images), search products by category, brand, label or country, and use taxonomy suggestions, attribute groups and knowledge panels. Data is ODbL-licensed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [openfoodfacts.org](https://openfoodfacts.org) |
| **Authentication** | No authentication |
| **Slug** | `openFoodFacts` |

## Use it

Add Open Food Facts from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openFoodFacts.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Taxonomy | `autocompleteTaxonomy` | Autocompletes taxonomy entries (categories, labels, brands, ingredients...) for a typed prefix. Docs: https://search.openfoodfacts.org/docs |
| Canonicalize Taxonomy Tags | `canonicalizeTags` | Converts local-language tag names into canonical taxonomy tag ids (e.g. 'chocolat' -&gt; en:chocolates). Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/ |
| Full-Text Search Products | `fullTextSearchProducts` | Full-text searches products with Lucene query syntax (e.g. 'orange juice', brands:ferrero, nutriscore_grade:a) on the Open Food Facts search service, with sorting, facets and paging. Docs: https://search.openfoodfacts.org/docs |
| Get Nutrients List | `getNutrients` | Returns the list of nutrients (with units and display order) used in nutrition facts tables for a country and language. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/ |
| Get Product | `getProduct` | Returns a product by barcode (API v2): name, brands, quantity, ingredients, nutrition facts, Nutri-Score, NOVA group, allergens, packaging, images. status 1 = found, 0 = not found. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/ |
| Get Product (API v3) | `getProductV3` | Returns a product by barcode using API v3, with structured status, warnings and errors. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/ |
| Get Product Search Document | `getSearchDocument` | Returns the indexed search document of one product (by barcode) from the Open Food Facts search service. Docs: https://search.openfoodfacts.org/docs |
| Get Tag Knowledge Panels | `getTagKnowledgePanels` | Returns knowledge panels for a tag (e.g. packaging statistics for a category). Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/ |
| Get Tag Suggestions | `getSuggestions` | Returns taxonomy entries of a tag type that contain a term (autocomplete for categories, labels, packaging shapes...). Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/ |
| Get Taxonomy Display Tags | `getDisplayTags` | Returns display names in a language for canonical taxonomy tag ids. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/ |
| Get Taxonomy Suggestions | `getTaxonomySuggestions` | Returns taxonomy suggestions for a tag type, optionally filtered by a starting string, categories or packaging shape. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/ |
| List Attribute Groups | `listAttributeGroups` | Returns the product attribute groups (nutritional quality, allergens, processing, labels, environment) used for personal search scoring. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/ |
| List Attribute Groups (API v3.4) | `listAttributeGroupsV3` | Returns attribute groups and attributes using API v3.4. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/ |
| List External Knowledge Panel Sources | `listExternalSources` | Returns the external knowledge panel sources configured on the server. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/ |
| List Preference Weights | `listPreferences` | Returns the importance levels (not important, important, very important, mandatory) and their weights used to compute personal product scores. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/ |
| List Preference Weights (API v3) | `listPreferencesV3` | Returns the preference importance values using API v3. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/ |
| Search Products | `searchProducts` | Searches products by tag filters (category, brand, label, country, Nutri-Score...), sorted and paged. Limited to 10 requests per minute. Docs: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/ |
