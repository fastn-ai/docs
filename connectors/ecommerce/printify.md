---
description: "Printify print-on-demand API."
hidden: true
---

# Printify

Printify print-on-demand API. Manage shops, browse the product catalog (blueprints, print providers, variants, shipping), create and publish products, submit and manage orders, upload artwork, and manage webhooks.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [printify.com](https://printify.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 40 |
| **Events** | 0 |
| **Slug** | `printify` |

## Use it

Add Printify from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.printify.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Upload | `archiveUpload` | Archive (soft-delete) an uploaded image from the merchant's media library. |
| Calculate Shipping | `calculateShipping` | Calculate shipping costs for a set of line items to a destination address before ordering. |
| Cancel Order | `cancelOrder` | Cancel an unpaid order that has not yet been sent to production. |
| Create Express Order | `createExpressOrder` | Submit a new Printify Express order to the shop with line items and a shipping address. |
| Create Order | `createOrder` | Submit a new order to the shop with line items and a shipping address. |
| Create Product | `createProduct` | Create a new product in the shop from a blueprint, print provider, variants, and print areas (artwork placement). |
| Create Webhook | `createWebhook` | Create a webhook subscription that delivers POST notifications to a URL when the given event topic occurs. |
| Delete Product | `deleteProduct` | Delete a product from the shop by its ID. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription from the shop. |
| Disconnect Shop | `disconnectShop` | Disconnect the current shop from the Printify account. Destructive: removes the store connection. |
| Get Blueprint | `getBlueprint` | Retrieve a specific catalog blueprint by its ID. |
| Get Economy Shipping | `getEconomyShipping` | Retrieve economy shipping rates (v2) for a blueprint and print provider. |
| Get Express Shipping | `getExpressShipping` | Retrieve express shipping rates (v2) for a blueprint and print provider. |
| Get Order | `getOrder` | Retrieve a specific order in the shop by its ID. |
| Get Print Provider | `getPrintProvider` | Retrieve a specific print provider and its details by ID. |
| Get Priority Shipping | `getPriorityShipping` | Retrieve priority shipping rates (v2) for a blueprint and print provider. |
| Get Product | `getProduct` | Retrieve a specific product in the shop by its ID. |
| Get Product GPSR | `getProductGpsr` | Retrieve the GPSR (General Product Safety Regulation) compliance information for a product. |
| Get Shipping Information | `getShippingInfo` | Retrieve shipping cost information (v1) for a blueprint and print provider. |
| Get Shipping Information V2 | `getShippingInfoV2` | Retrieve the available shipping methods (v2) for a blueprint and print provider, with links to each method's details. |
| Get Standard Shipping | `getStandardShipping` | Retrieve standard shipping rates (v2) for a blueprint and print provider. |
| Get Upload | `getUpload` | Retrieve details of a specific uploaded image by its ID. |
| List Blueprints | `listBlueprints` | List all available catalog blueprints (base products) offered by Printify. |
| List Orders | `listOrders` | List orders in the shop. Supports pagination and filters. |
| List Print Providers | `listPrintProviders` | List all print providers available in the Printify catalog. |
| List Print Providers For Blueprint | `listPrintProvidersForBlueprint` | List all print providers that can fulfill a specific blueprint. |
| List Products | `listProducts` | List products in the shop. Supports pagination via limit and page. |
| List Shops | `listShops` | Retrieve the list of shops (stores) connected to the Printify account. |
| List Uploads | `listUploads` | List images uploaded to the merchant's media library. Supports pagination. |
| List Variants | `listVariants` | List all variants (and their options) available for a blueprint from a specific print provider. |
| List Webhooks | `listWebhooks` | List all webhook subscriptions configured for the shop. |
| Publish Product | `publishProduct` | Lock and publish a product to its connected sales channel. Boolean flags control which properties are published. |
| Send Order To Production | `sendOrderToProduction` | Send an on-hold order to production for fulfillment. |
| Set Publishing Failed | `setPublishFailed` | Notify Printify that publishing of a product to the external sales channel failed. Unlocks the product. |
| Set Publishing Succeeded | `setPublishSucceeded` | Notify Printify that publishing of a product to the external sales channel succeeded, providing the external product id and handle. Unlocks the product. |
| Simulate Webhook | `simulateWebhook` | Trigger a simulated delivery of a webhook subscription for testing the receiving endpoint. |
| Unpublish Product | `unpublishProduct` | Unpublish a product and unlock it (removes the publish lock). |
| Update Product | `updateProduct` | Update an existing product. Only the fields you send are changed (partial update). |
| Update Webhook | `updateWebhook` | Update the destination URL of an existing webhook subscription. |
| Upload Image | `uploadImage` | Upload an image to the merchant's media library by URL or base64 contents. Provide file_name plus either url or contents. |
