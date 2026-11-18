---
description: "endoflife.date tracks end-of-life dates and support lifecycles for 400+ products: languages, frameworks, databases, operating systems, cloud services and…"
hidden: true
---

# endoflife.date

endoflife.date tracks end-of-life dates and support lifecycles for 400+ products: languages, frameworks, databases, operating systems, cloud services and devices. List products, categories, tags and identifiers (purl, CPE), and get every release of a product with its EOL, LTS and latest version. No API key needed.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [endoflife.date](https://endoflife.date) |
| **Authentication** | No authentication |
| **Actions** | 12 |
| **Events** | 0 |
| **Slug** | `endoflifeDate` |

## Use it

Add endoflife.date from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.endoflifeDate.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get API Index | `getApiIndex` | API index. List the main endoflife.date API endpoints. Docs: https://endoflife.date/docs/api/v1/ (GET /) |
| Get Latest Product Release | `getLatestProductRelease` | Get a product latest release cycle. Get the latest release cycle information for the given product. Docs: https://endoflife.date/docs/api/v1/ (GET /products/{product}/releases/latest) |
| Get Product | `getProduct` | Get a product. Get the given product data. This endpoint is returning all endoflife.date knows about the product, including release cycles data. Docs: https://endoflife.date/docs/api/v1/ (GET /products/{product}) |
| Get Product Release | `getProductRelease` | Get a product release cycle. Get the given product release cycle information. Docs: https://endoflife.date/docs/api/v1/ (GET /products/{product}/releases/{release}) |
| List Categories | `listCategories` | List all categories. List all endoflife.date categories. Docs: https://endoflife.date/docs/api/v1/ (GET /categories) |
| List Identifier Types | `listIdentifierTypes` | List all identifier types. List all identifier types, such as a purl, known in endoflife.date. Docs: https://endoflife.date/docs/api/v1/ (GET /identifiers) |
| List Identifiers by Type | `listIdentifiersByType` | List all identifiers for a given type.. List all identifiers referenced on endoflife.date for the given identifier type. Each identifier reference its related product. Docs: https://endoflife.date/docs/api/v1/ (GET /identifiers/{identifier_type}) |
| List Products | `listProducts` | List all products. List all the products referenced on endoflife.date. Only a summary of each product is returned by this endpoint. Docs: https://endoflife.date/docs/api/v1/ (GET /products) |
| List Products by Category | `listProductsByCategory` | List all products in a category. List all the products referenced on endoflife.date for the given category. Only a summary of each product is returned by this endpoint. Docs: https://endoflife.date/docs/api/v1/ (GET /categories/{category}) |
| List Products by Tag | `listProductsByTag` | List all products with a tag. List all the products referenced on endoflife.date for the given tag. Only a summary of each product is returned by this endpoint. Docs: https://endoflife.date/docs/api/v1/ (GET /tags/{tag}) |
| List Products With Full Details | `listProductsFull` | List all products (full). List all the products referenced on endoflife.date, with all their details. The full products data is returned by this endpoint, making the result a dump of nearly all endoflife.date data. Preferably, use the /products endpoint to get a summary of the products and reduce the amount of data transferred. Returns about 3 MB. Docs: https://endoflife.date/docs/api/v1/ (GET /products/full) |
| List Tags | `listTags` | List all tags. List all endoflife.date tags. Docs: https://endoflife.date/docs/api/v1/ (GET /tags) |
