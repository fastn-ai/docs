---
description: "endoflife.date tracks support and end-of-life dates for 400+ products. List products by category or tag and get release lifecycles."
hidden: true
---

# endoflife.date

<img src="../../.gitbook/assets/connectors/lg/endoflife-date.png" alt="endoflife.date logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [endoflife.date](https://endoflife.date) |
| **Authentication** | No sign-in needed |
| **Slug** | `endoflifeDate` |

## Setup

endoflife.date needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect endoflife.date from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **endoflife.date**.
2. Select **Connect** on the endoflife.date card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. endoflife.date needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use endoflife.date's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Index</td><td><code>getApiIndex</code></td><td>API index. List the main endoflife.date API endpoints. Docs: https://endoflife.date/docs/api/v1/</td></tr><tr><td>Get Latest Product Release</td><td><code>getLatestProductRelease</code></td><td>Get a product latest release cycle. Get the latest release cycle information for the given product. Docs: https://endoflife.date/docs/api/v1/</td></tr><tr><td>Get Product</td><td><code>getProduct</code></td><td>Get a product. Get the given product data. This endpoint is returning all endoflife.date knows about the product, including release cycles data. Docs: https://endoflife.date/docs/api/v1/</td></tr><tr><td>Get Product Release</td><td><code>getProductRelease</code></td><td>Get a product release cycle. Get the given product release cycle information. Docs: https://endoflife.date/docs/api/v1/</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>List all categories. List all endoflife.date categories. Docs: https://endoflife.date/docs/api/v1/</td></tr><tr><td>List Identifier Types</td><td><code>listIdentifierTypes</code></td><td>List all identifier types. List all identifier types, such as a purl, known in endoflife.date. Docs: https://endoflife.date/docs/api/v1/</td></tr><tr><td>List Identifiers by Type</td><td><code>listIdentifiersByType</code></td><td>List all identifiers for a given type.. List all identifiers referenced on endoflife.date for the given identifier type. Each identifier reference its related product. Docs: https://endoflife.date/docs/api/v1/</td></tr><tr><td>List Products</td><td><code>listProducts</code></td><td>List all products. List all the products referenced on endoflife.date. Only a summary of each product is returned by this endpoint. Docs: https://endoflife.date/docs/api/v1/</td></tr><tr><td>List Products by Category</td><td><code>listProductsByCategory</code></td><td>List all products in a category. List all the products referenced on endoflife.date for the given category. Only a summary of each product is returned by this endpoint. Docs: https://endoflife.date/docs/api/v1/</td></tr><tr><td>List Products by Tag</td><td><code>listProductsByTag</code></td><td>List all products with a tag. List all the products referenced on endoflife.date for the given tag. Only a summary of each product is returned by this endpoint. Docs: https://endoflife.date/docs/api/v1/</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Products With Full Details</td><td><code>listProductsFull</code></td><td>List all products (full). List all the products referenced on endoflife.date, with all their details. The full products data is returned by this endpoint, making the result a dump of nearly all endoflife.date data. Preferably, use the /products endpoint to get a summary of the products and reduce the amount of data transferred. Returns about 3 MB. Docs: https://endoflife.date/docs/api/v1/</td></tr><tr><td>List Tags</td><td><code>listTags</code></td><td>List all tags. List all endoflife.date tags. Docs: https://endoflife.date/docs/api/v1/</td></tr></tbody></table>

</details>

