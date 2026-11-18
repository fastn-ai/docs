---
description: "endoflife.date tracks end-of-life dates and support lifecycles for 400+ products: languages, frameworks, databases, operating systems, cloud services and…"
hidden: true
---

# endoflife.date

<img src="../../.gitbook/assets/connectors/lg/endoflife-date.png" alt="endoflife.date logo">

endoflife.date tracks end-of-life dates and support lifecycles for 400+ products: languages, frameworks, databases, operating systems, cloud services and devices. List products, categories, tags and identifiers (purl, CPE), and get every release of a product with its EOL, LTS and latest version. No API key needed.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [endoflife.date](https://endoflife.date) |
| **Authentication** | No authentication |
| **Slug** | `endoflifeDate` |

## Use it

Add endoflife.date from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.endoflifeDate.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Index</td><td><code>getApiIndex</code></td><td>API index. List the main endoflife.date API endpoints. Docs: https://endoflife.date/docs/api/v1/ (GET /)</td></tr><tr><td>Get Latest Product Release</td><td><code>getLatestProductRelease</code></td><td>Get a product latest release cycle. Get the latest release cycle information for the given product. Docs: https://endoflife.date/docs/api/v1/ (GET /products/{product}/releases/latest)</td></tr><tr><td>Get Product</td><td><code>getProduct</code></td><td>Get a product. Get the given product data. This endpoint is returning all endoflife.date knows about the product, including release cycles data. Docs: https://endoflife.date/docs/api/v1/ (GET /products/{product})</td></tr><tr><td>Get Product Release</td><td><code>getProductRelease</code></td><td>Get a product release cycle. Get the given product release cycle information. Docs: https://endoflife.date/docs/api/v1/ (GET /products/{product}/releases/{release})</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>List all categories. List all endoflife.date categories. Docs: https://endoflife.date/docs/api/v1/ (GET /categories)</td></tr><tr><td>List Identifier Types</td><td><code>listIdentifierTypes</code></td><td>List all identifier types. List all identifier types, such as a purl, known in endoflife.date. Docs: https://endoflife.date/docs/api/v1/ (GET /identifiers)</td></tr><tr><td>List Identifiers by Type</td><td><code>listIdentifiersByType</code></td><td>List all identifiers for a given type.. List all identifiers referenced on endoflife.date for the given identifier type. Each identifier reference its related product. Docs: https://endoflife.date/docs/api/v1/ (GET /identifiers/{identifier_type})</td></tr><tr><td>List Products</td><td><code>listProducts</code></td><td>List all products. List all the products referenced on endoflife.date. Only a summary of each product is returned by this endpoint. Docs: https://endoflife.date/docs/api/v1/ (GET /products)</td></tr><tr><td>List Products by Category</td><td><code>listProductsByCategory</code></td><td>List all products in a category. List all the products referenced on endoflife.date for the given category. Only a summary of each product is returned by this endpoint. Docs: https://endoflife.date/docs/api/v1/ (GET /categories/{category})</td></tr><tr><td>List Products by Tag</td><td><code>listProductsByTag</code></td><td>List all products with a tag. List all the products referenced on endoflife.date for the given tag. Only a summary of each product is returned by this endpoint. Docs: https://endoflife.date/docs/api/v1/ (GET /tags/{tag})</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Products With Full Details</td><td><code>listProductsFull</code></td><td>List all products (full). List all the products referenced on endoflife.date, with all their details. The full products data is returned by this endpoint, making the result a dump of nearly all endoflife.date data. Preferably, use the /products endpoint to get a summary of the products and reduce the amount of data transferred. Returns about 3 MB. Docs: https://endoflife.date/docs/api/v1/ (GET /products/full)</td></tr><tr><td>List Tags</td><td><code>listTags</code></td><td>List all tags. List all endoflife.date tags. Docs: https://endoflife.date/docs/api/v1/ (GET /tags)</td></tr></tbody></table>

</details>
