---
description: "Gumroad is a commerce platform for creators to sell digital products, memberships and subscriptions."
hidden: true
---

# Gumroad

<img src="../../.gitbook/assets/connectors/gumroad.png" alt="Gumroad logo" width="64">

Gumroad is a commerce platform for creators to sell digital products, memberships and subscriptions. This connector covers products, variant categories and variants, offer codes, custom fields, sales, subscribers, licenses, and resource subscriptions (webhooks).

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [gumroad.com](https://gumroad.com) |
| **Authentication** | Bearer token |
| **Slug** | `gumroad` |

## Use it

Add Gumroad from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gumroad.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Custom Field | `createCustomField` | Create a custom field on a product, collected from the buyer at checkout. The required flag is only honoured when sent as form-urlencoded, which this action does. |
| Create Offer Code | `createOfferCode` | Create an offer code (discount code) for a product. The discount is a fixed amount in cents by default; set offer_type to percent for a percentage discount. A universal offer code applies to every product on the account. |
| Create Product | `createProduct` | Create a new Gumroad product. The product is published immediately unless draft is set to true or published is set to false. Price is in the smallest currency unit (cents). Requires the edit_products or account scope. |
| Create Resource Subscription | `createResourceSubscription` | Register a webhook that Gumroad will POST to when the given event occurs (sale, refund, dispute, cancellation, subscription lifecycle, etc.). |
| Create Variant | `createVariant` | Create a variant (option) within a variant category. |
| Create Variant Category | `createVariantCategory` | Create a variant category on a product. Add at least one variant afterwards to keep the product valid. |
| Decrement License Uses Count | `decrementLicenseUses` | Decrement the uses count of a license key for a product. |
| Delete Custom Field | `deleteCustomField` | Delete a custom field from a product, identified by its name. |
| Delete Offer Code | `deleteOfferCode` | Delete an offer code from a product. |
| Delete Product | `deleteProduct` | Permanently delete a product from the Gumroad account. |

<details>

<summary>See 34 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Resource Subscription | `deleteResourceSubscription` | Delete a webhook resource subscription by its ID. |
| Delete Variant | `deleteVariant` | Delete a variant from a variant category. |
| Delete Variant Category | `deleteVariantCategory` | Delete a variant category from a product. |
| Disable License | `disableLicense` | Disable a license key for a product. |
| Disable Product | `disableProduct` | Unpublish a product so it is no longer available for sale. |
| Enable License | `enableLicense` | Enable a previously disabled license key for a product. |
| Enable Product | `enableProduct` | Publish a product for sale. Requires a payment method connected to the account. |
| Get Earnings | `getEarnings` | Retrieve the seller's earnings overview. |
| Get Offer Code | `getOfferCode` | Retrieve a single offer code for a product. |
| Get Product | `getProduct` | Retrieve a single product by its Gumroad product ID. |
| Get Sale | `getSale` | Retrieve a single sale by its ID. |
| Get Sales Summary | `getSalesSummary` | Retrieve an aggregate summary of the seller's sales. |
| Get Subscriber | `getSubscriber` | Retrieve a single subscriber by its ID. |
| Get User | `getUser` | Retrieve the authenticated Gumroad user's profile information. |
| Get Variant | `getVariant` | Retrieve a single variant within a variant category. |
| Get Variant Category | `getVariantCategory` | Retrieve a single variant category of a product. |
| List Custom Fields | `listCustomFields` | List all custom fields configured on a product. |
| List Offer Codes | `listOfferCodes` | List all offer codes (discount codes) for a product. |
| List Payouts | `listPayouts` | List the seller's payouts. |
| List Product Reviews | `listProductReviews` | List customer reviews for a product. |
| List Products | `listProducts` | List all products for the authenticated Gumroad account. |
| List Resource Subscriptions | `listResourceSubscriptions` | List all webhook resource subscriptions of a given type for the account. |
| List Sales | `listSales` | List successful sales for the account, optionally filtered by date, product, or buyer email. |
| List Subscribers | `listSubscribers` | List subscribers for a subscription or membership product, optionally filtered by email. |
| List Variant Categories | `listVariantCategories` | List all variant categories for a product. |
| List Variants | `listVariants` | List all variants within a variant category. |
| Mark Sale As Shipped | `markSaleAsShipped` | Mark a physical-product sale as shipped, optionally recording a tracking URL. Returns the updated sale. |
| Refund Sale | `refundSale` | Refund a sale in full, or partially when an amount in cents is supplied. Returns the updated sale. |
| Update Custom Field | `updateCustomField` | Update a product custom field, identified by its current name. Only the required flag and the variant scope can be changed; the field name and type are fixed at creation, so delete and recreate the field to change either. |
| Update Offer Code | `updateOfferCode` | Update an existing offer code on a product. Gumroad allows changing the code text, its usage limit and its minimum order total; the discount amount cannot be changed after creation. |
| Update Product | `updateProduct` | Update an existing Gumroad product. Only the fields you send are changed, except tags, cover_ids and files, which fully replace the existing collection. Price is not allowed for tiered memberships; use the variant actions for tier pricing. |
| Update Variant | `updateVariant` | Update a variant's name, price difference, or maximum purchase count. |
| Update Variant Category | `updateVariantCategory` | Update the title of a variant category. |
| Verify License | `verifyLicense` | Verify a license key for a product and optionally increment its uses count. |

</details>
