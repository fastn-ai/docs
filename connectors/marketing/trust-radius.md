---
description: "TrustRadius software review data."
hidden: true
---

# TrustRadius

<img src="../../.gitbook/assets/connectors/lg/trust-radius.png" alt="TrustRadius logo">

TrustRadius software review data. Reads the public TrustRadius JSON catalogue API for products, product reviews, categories and vendors, returning structured records with ratings, reviewer verbatims and firmographics. Read-only and requires no credentials.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [trustradius.com](https://trustradius.com) |
| **Authentication** | No authentication |
| **Slug** | `trustRadius` |

## Use it

Add TrustRadius from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.trustRadius.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Product</td><td><code>getProduct</code></td><td>Retrieves a single TrustRadius product by its product id, returning the full record including description, categories, competitors, vendor and the aggregate rating breakdown. Use List Products to resolve a product id from a slug.</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>Lists the TrustRadius software categories, returning each category's name, slug, hierarchy level and parent category. Filter by category slug to resolve a single category, and use the returned category id with List Products to list every product in that category.</td></tr><tr><td>List Product Reviews</td><td><code>scrapeProductReviews</code></td><td>Lists published TrustRadius reviews for a single product, identified by its TrustRadius product slug. Returns the full review records including rating, heading, verbatim answers, reviewer role, company industry and company size. Supports limit and skip for pagination.</td></tr><tr><td>List Products</td><td><code>getTopProductSlugs</code></td><td>Lists products in the TrustRadius catalogue, returning each product's name, slug, description and category ids. Filter by product slug to resolve a single product, or by category id to list every product in a category. Use limit and skip to page through the catalogue.</td></tr><tr><td>List Vendors</td><td><code>listVendors</code></td><td>Lists the software vendors TrustRadius tracks, returning each vendor's name and slug. Filter by vendor slug to resolve a single vendor, and use limit and skip to page through the list.</td></tr></tbody></table>
