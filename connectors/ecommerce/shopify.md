---
description: "Shopify Admin REST API connector for managing orders, products, customers, inventory, discounts, shipping, payments, and more."
hidden: true
---

# Shopify

<img src="../../.gitbook/assets/connectors/lg/shopify.png" alt="Shopify logo">

Shopify Admin REST API connector for managing orders, products, customers, inventory, discounts, shipping, payments, and more.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [shopify.com](https://shopify.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Slug** | `shopify` |

## Use it

Add Shopify from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.shopify.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Fulfillment Order Cancellation Request | `createAcceptJson` | https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/cancellationrequest#accept-2020-01 |
| Accept Fulfillment Request | `createFulfillmentRequestAcceptJson` | https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentrequest#accept-2020-01 |
| Activate Application Charge (Legacy) | `createApplicationChargeActivateJson` | https://shopify.dev/docs/admin-api/rest/reference/billing/applicationcharge#activate-2020-04 |
| Activate Recurring Application Charge | `createRecurringApplicationChargeActivateJson` | https://shopify.dev/docs/admin-api/rest/reference/billing/recurringapplicationcharge#activate-2020-01 |
| Adjust Inventory Level | `createAdjustJson` | https://shopify.dev/docs/admin-api/rest/reference/inventory/inventorylevel#adjust-2020-01 |
| Approve Comment | `createApproveJson` | https://shopify.dev/docs/admin-api/rest/reference/online-store/comment#approve-2020-01 |
| Approve Return Request | `approveReturnRequest` | Approves a return that has status REQUESTED, which moves it to OPEN and creates its reverse fulfillment order (GraphQL returnApproveRequest, API 2026-07). Fires the returns/approve event. Requires write_returns. Check userErrors: Shopify answers HTTP 200 even when the request is refused. |
| Browse Product Taxonomy | `browseProductTaxonomy` | Browse Shopify's Standard Product Taxonomy tree (GraphQL). Returns taxonomy categories with their GID, name, full path, level, and hierarchy - use these GIDs with Set Product Category, and to build a source-category to Shopify-taxonomy-GID mapping table. Pass a variables object: first (page size, required), and optionally search (text filter), childrenOf (a parent category GID to list its children), and after (pagination cursor from pageInfo.endCursor). With no search/childrenOf it returns top-level categories. |
| Bulk Update Customer Addresses | `updateAddresseSetJson` | Performs bulk operations on a customer's addresses. Canonical version — updateSetJson is the duplicate. |
| Calculate Refund | `createCalculateJson` | https://shopify.dev/docs/admin-api/rest/reference/orders/refund#calculate-2020-01 |

<details>

<summary>See 313 more actions</summary>

* **Cancel Fulfillment** `createFulfillmentCancelJson`: Cancels a fulfillment.
* **Cancel Fulfillment Order** `createFulfillmentOrderCancelJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder#cancel-2020-01
* **Cancel Order** `createOrderCancelJson`: https://shopify.dev/docs/admin-api/rest/reference/orders/order#cancel-2020-04
* **Cancel Return** `cancelReturn`: Cancels a return that has no processed items yet; its status becomes CANCELED and the items become returnable again (GraphQL returnCancel, API 2026-07). Fires the returns/cancel event. Requires write_returns. Check userErrors: Shopify answers HTTP 200 even when the request is refused.
* **Close Fulfillment Order** `createFulfillmentOrderCloseJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder#close-2020-01
* **Close Order** `createOrderCloseJson`: https://shopify.dev/docs/admin-api/rest/reference/orders/order#close-2020-04
* **Close Return** `closeReturn`: Closes an OPEN return once it is handled; it can be reopened later with Reopen Return (GraphQL returnClose, API 2026-07). Fires the returns/close event. Requires write_returns. Check userErrors: Shopify answers HTTP 200 even when the request is refused.
* **Complete Checkout** `createCheckoutCompleteJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/checkout#complete-2020-04
* **Complete Fulfillment** `createFulfillmentCompleteJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillment#complete-2020-01
* **Connect Inventory Level** `createConnectJson`: https://shopify.dev/docs/admin-api/rest/reference/inventory/inventorylevel#connect-2020-01
* **Count Checkout Payments** `listPaymentCountJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/payment#count-2020-01
* **Count Customers** `listCustomerCountJson`: Retrieves a count of all customers.
* **Count Locations** `listLocationCountJson`: Retrieves a count of locations for a shop.
* **Count Order Transactions** `countOrderTransactions`: Retrieves a count of transactions for an order.
* **Count Orders** `listOrderCountJson1`: https://shopify.dev/docs/admin-api/rest/reference/orders/order#count-2020-04
* **Count Product Images** `listImageCountJson`: Retrieves a count of images for a given product.
* **Count Products** `getProductsCount`
* **Count Products** `listCountJson`: Retrieves a count of products matching the specified criteria.
* **Count Webhooks** `listWebhookCountJson`: Retrieves a count of existing webhook subscriptions.
* **Create Application Charge** `create202004ApplicationChargesJson`: https://shopify.dev/docs/admin-api/rest/reference/billing/applicationcharge#create-2020-04
* **Create Application Credit** `create202101ApplicationCreditsJson`: https://shopify.dev/docs/admin-api/rest/reference/billing/applicationcredit#create-2021-01
* **Create Article in Blog** `createBlogArticlesJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/article#create-2020-04
* **Create Blog** `createBlogsJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/blog#create-2020-01
* **Create Carrier Service** `create202101CarrierServicesJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/carrierservice#create-2021-01
* **Create Checkout** `create202101CheckoutsJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/checkout#create-2021-01
* **Create Checkout Payment** `createCheckoutPaymentsJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/payment#create_payment-2020-04
* **Create Collect** `create202101CollectsJson`: https://shopify.dev/docs/admin-api/rest/reference/products/collect#create-2021-01
* **Create Comment** `createCommentsJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/comment#create-2020-01
* **Create Country** `create202101CountriesJson`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/country#create-2021-01
* **Create Custom Collection** `create202101CustomCollectionsJson`: https://shopify.dev/docs/admin-api/rest/reference/products/customcollection#create-2021-01
* **Create Customer** `create202101CustomersJson`: https://shopify.dev/docs/admin-api/rest/reference/customers/customer#create-2021-01
* **Create Customer Account Activation URL** `createAccountActivationUrlJson`: https://shopify.dev/docs/admin-api/rest/reference/customers/customer#account_activation_url-2020-01
* **Create Customer Address** `createAddressesJson`: Creates a new address for a customer.
* **Create Customer Saved Search** `create202101CustomerSavedSearchesJson`: https://shopify.dev/docs/admin-api/rest/reference/customers/customersavedsearch#create-2021-01
* **Create Discount Code** `createDiscountCodesJson`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#create-2020-01
* **Create Discount Code Batch** `createBatchJson`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#batch_create-2020-01
* **Create Fulfillment** `create202101FulfillmentsJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillment#createV2-2021-01
* **Create Fulfillment Events** `createFulfillmentEventsJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentevent#create-2020-04
* **Create Fulfillment Order Cancellation Request** `createCancellationRequestJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/cancellationrequest#create-2020-01
* **Create Fulfillment Request** `createFulfillmentOrderFulfillmentRequestJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentrequest#create-2020-04
* **Create Fulfillment Service** `create202101FulfillmentServicesJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentservice#create-2021-01
* **Create Gift Card** `create202101GiftCardsJson`: https://shopify.dev/docs/admin-api/rest/reference/plus/giftcard#create-2021-01
* **Create Metafield** `create202101MetafieldsJson`: https://shopify.dev/docs/admin-api/rest/reference/metafield#create-2021-01
* **Create Order** `create202004OrdersJson`: https://shopify.dev/docs/admin-api/rest/reference/orders/order#create-2020-04
* **Create Order Refund** `createOrderRefundsJson`: https://shopify.dev/docs/admin-api/rest/reference/orders/refund#create-2020-04
* **Create Order Risk** `createOrderRisksJson`: https://shopify.dev/docs/admin-api/rest/reference/orders/order-risk#create-2020-04
* **Create Order Risk (Duplicate)** `createRisksJson`: DUPLICATE of createOrderRisksJson — same endpoint POST /admin/api/2024-01/orders/{order_id}/risks.json. Consider removing this action."
* **Create Order Transaction** `createOrderTransaction`: Creates a transaction for an order. Used to capture authorized payments, void authorizations, create sales, or create refunds.
* **Create Price Rule** `createPriceRule`: Creates a price rule to define discount conditions — percentage off, fixed amount off, or free shipping. Supports entitlements (which items the discount applies to) and prerequisites (conditions that must be met). Associate with a discount code using the Create Discount Code action.
* **Create Price Rule Discount Code** `createPriceRuleDiscountCodesJson`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#create-2020-04
* **Create Price Rule Discount Code Batch** `createPriceRuleBatchJson`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#batch_create-2020-04
* **Create Product** `createProduct`: Create a new product in the Shopify store. POST /admin/api/2024-01/products.json. Requires the write_products scope. Pass a `product` object (title required); vendor, product_type, tags, status, variants, options, and images are optional. Returns the created product with its assigned id and default variant.
* **Create Product Image** `createProductImagesJson`: https://shopify.dev/docs/admin-api/rest/reference/products/product-image#create-2020-04
* **Create Product Variant** `createVariantsJson`: Creates a new variant for a product.
* **Create Recurring Application Charge** `create202101RecurringApplicationChargesJson`: https://shopify.dev/docs/admin-api/rest/reference/billing/recurringapplicationcharge#create-2021-01
* **Create Redirect** `create202101RedirectsJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/redirect#create-2021-01
* **Create Report** `create202101ReportsJson`: https://shopify.dev/docs/admin-api/rest/reference/analytics/report#create-2021-01
* **Create Return** `createReturn`: Creates a return as the merchant, already approved, so it starts with status OPEN and skips the request step (GraphQL returnCreate, API 2026-07). Fires the returns/approve event, not returns/request. Get fulfillmentLineItemId from List Returnable Fulfillments and returnReasonDefinitionId from List Return Reasons. Requires write_returns. Check userErrors: Shopify answers HTTP 200 even when the request is refused.
* **Create Reverse Delivery** `createReverseDelivery`: Adds return shipping to a reverse fulfillment order: the items being shipped back plus a tracking number and/or a label file URL (GraphQL reverseDeliveryCreateWithShipping, API 2026-07). Fires the reverse_deliveries/attach_deliverable event. Requires write_returns. Check userErrors: Shopify answers HTTP 200 even when the request is refused.
* **Create Script Tag** `create202101ScriptTagsJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/scripttag#create-2021-01
* **Create Smart Collection** `create202101SmartCollectionsJson`: https://shopify.dev/docs/admin-api/rest/reference/products/smartcollection#create-2021-01
* **Create Storefront Access Token** `create202101StorefrontAccessTokensJson`: https://shopify.dev/docs/admin-api/rest/reference/access/storefrontaccesstoken#create-2021-01
* **Create Theme** `create202101ThemesJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/theme#create-2021-01
* **Create Usage Charge** `createRecurringApplicationChargeUsageChargesJson`: https://shopify.dev/docs/admin-api/rest/reference/billing/usagecharge#create-2020-04
* **Create Webhook** `create202101WebhooksJson`: https://shopify.dev/docs/admin-api/rest/reference/events/webhook#create-2021-01
* **Customize Recurring Application Charge** `updateCustomizeJson`: https://shopify.dev/docs/admin-api/rest/reference/billing/recurringapplicationcharge#customize-2020-01
* **Decline Return Request** `declineReturnRequest`: Declines a return that has status REQUESTED, with a reason and an optional note to the customer (GraphQL returnDeclineRequest, API 2026-07). The return becomes DECLINED and the returns/decline event fires. Requires write_returns. Check userErrors: Shopify answers HTTP 200 even when the request is refused.
* **Delete Article** `deleteArticle`: https://shopify.dev/docs/admin-api/rest/reference/online-store/article#destroy-2020-01
* **Delete Blog** `deleteBlog`: https://shopify.dev/docs/admin-api/rest/reference/online-store/blog#destroy-2020-01
* **Delete Blog Article** `deleteBlogArticle`: https://shopify.dev/docs/admin-api/rest/reference/online-store/article#destroy-2020-04
* **Delete Carrier Service** `delete202004CarrierService`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/carrierservice#destroy-2020-04
* **Delete Collect** `delete202004Collect`: https://shopify.dev/docs/admin-api/rest/reference/products/collect#destroy-2020-04
* **Delete Collection Listing** `delete202004CollectionListing`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/collectionlisting#destroy-2020-04
* **Delete Country** `delete202004Country`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/country#destroy-2020-04
* **Delete Custom Collection** `delete202004CustomCollection`: https://shopify.dev/docs/admin-api/rest/reference/products/customcollection#destroy-2020-04
* **Delete Customer** `delete202004Customer`: https://shopify.dev/docs/admin-api/rest/reference/customers/customer#destroy-2020-04
* **Delete Customer Address** `deleteAddresse`: https://shopify.dev/docs/admin-api/rest/reference/customers/customer-address#destroy-2020-01
* **Delete Customer Saved Search** `delete202004CustomerSavedSearche`: https://shopify.dev/docs/admin-api/rest/reference/customers/customersavedsearch#destroy-2020-04
* **Delete Discount Code** `deleteDiscountCode`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#destroy-2020-01
* **Delete Fulfillment Event** `deleteEvent`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentevent#destroy-2020-01
* **Delete Fulfillment Service** `delete202004FulfillmentService`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentservice#destroy-2020-04
* **Delete Inventory Level** `delete202004InventoryLevelsJson`: https://shopify.dev/docs/admin-api/rest/reference/inventory/inventorylevel#destroy-2020-04
* **Delete Metafield** `delete202004Metafield`: https://shopify.dev/docs/admin-api/rest/reference/metafield#destroy-2020-04
* **Delete Order** `delete202004Order`: https://shopify.dev/docs/admin-api/rest/reference/orders/order#destroy-2020-04
* **Delete Order Risk** `deleteOrderRisk`: https://shopify.dev/docs/admin-api/rest/reference/orders/order-risk#destroy-2020-04
* **Delete Price Rule Discount Code** `deletePriceRuleDiscountCode`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#destroy-2020-04
* **Delete Product** `delete202004Product`: https://shopify.dev/docs/admin-api/rest/reference/products/product#destroy-2020-04
* **Delete Product Image** `deleteImage`: Deletes an image from a product.
* **Delete Product Listing** `delete202004ProductListing`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/productlisting#destroy-2020-04
* **Delete Recurring Application Charge** `delete202004RecurringApplicationCharge`: https://shopify.dev/docs/admin-api/rest/reference/billing/recurringapplicationcharge#destroy-2020-04
* **Delete Redirect** `delete202004Redirect`: https://shopify.dev/docs/admin-api/rest/reference/online-store/redirect#destroy-2020-04
* **Delete Report** `delete202004Report`: https://shopify.dev/docs/admin-api/rest/reference/analytics/report#destroy-2020-04
* **Delete Script Tag** `delete202004ScriptTag`: https://shopify.dev/docs/admin-api/rest/reference/online-store/scripttag#destroy-2020-04
* **Delete Smart Collection** `delete202004SmartCollection`: https://shopify.dev/docs/admin-api/rest/reference/products/smartcollection#destroy-2020-04
* **Delete Storefront Access Token** `delete202004StorefrontAccessToken`: https://shopify.dev/docs/admin-api/rest/reference/access/storefrontaccesstoken#destroy-2020-04
* **Delete Theme** `delete202004Theme`: https://shopify.dev/docs/admin-api/rest/reference/online-store/theme#destroy-2020-04
* **Delete Theme Assets** `deleteThemeAssetsJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/asset#destroy-2020-04
* **Delete Webhook** `delete202004Webhook`: https://shopify.dev/docs/admin-api/rest/reference/events/webhook#destroy-2020-04
* **Disable Gift Card** `createDisableJson`: https://shopify.dev/docs/admin-api/rest/reference/plus/giftcard#disable-2020-01
* **Dispose Reverse Fulfillment Order** `disposeReverseFulfillmentOrder`: Records what happened to returned goods: restocked at a location, not restocked, missing, or still being processed (GraphQL reverseFulfillmentOrderDispose, API 2026-07). Fires the reverse_fulfillment_orders/dispose event. Get reverse fulfillment order line item IDs from Get Return or Get Reverse Fulfillment Order. Requires write_returns. Check userErrors: Shopify answers HTTP 200 even when the request is refused.
* **Fetch Fulfillment Stock** `listFetchStock`: DO NOT CALL. This is not a Shopify Admin API endpoint. fetch_stock is an endpoint that a third-party fulfillment service must implement at its own registered callback_url - Shopify sends GET requests TO it, it does not serve one. Calling https://{shop}.myshopify.com/admin/api/2024-01/fulfillment_services/fetch_stock returns HTTP 200 carrying the Shopify accounts OAuth sign-in HTML page, never JSON, so any caller that checks only the status code will read a false success. See https://shopify.dev/docs/api/admin-rest/2024-01/resources/fulfillmentservice. Use listLocationInventoryLevelsJson or list202004InventoryLevelsJson for real stock levels.
* **Fetch Fulfillment Tracking Numbers** `listFetchTrackingNumbers`: DO NOT CALL. This is not a Shopify Admin API endpoint. fetch_tracking_numbers is an endpoint that a third-party fulfillment service must implement at its own registered callback_url - Shopify sends GET requests TO it, it does not serve one. Calling https://{shop}.myshopify.com/admin/api/2024-01/fulfillment_services/fetch_tracking_numbers returns HTTP 200 carrying the Shopify accounts OAuth sign-in HTML page, never JSON, so any caller that checks only the status code will read a false success. See https://shopify.dev/docs/api/admin-rest/2024-01/resources/fulfillmentservice. Use listFulfillmentsJson on an order for real tracking numbers.
* **Get Application Charge** `list202004ApplicationCharges`: https://shopify.dev/docs/admin-api/rest/reference/billing/applicationcharge#show-2020-04
* **Get Application Credit** `list202004ApplicationCredits`: https://shopify.dev/docs/admin-api/rest/reference/billing/applicationcredit#show-2020-04
* **Get Blog** `listBlogs`: https://shopify.dev/docs/admin-api/rest/reference/online-store/blog#show-2020-01
* **Get Blog Article** `getArticle`: https://shopify.dev/docs/admin-api/rest/reference/online-store/article#show-2020-01
* **Get Carrier Service** `list202004CarrierServices`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/carrierservice#show-2020-04
* **Get Checkout** `list202004Checkouts`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/checkout#show-2020-04
* **Get Checkout** `list202007Checkouts`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/checkout#show-2020-07
* **Get Checkout Payment** `getCheckoutPayment`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/payment#show-2020-04
* **Get Checkout Payment** `listPaymentsJson`: Retrieves a single payment by ID for a given checkout token.
* **Get Collect** `list202004Collects`: https://shopify.dev/docs/admin-api/rest/reference/products/collect#show-2020-04
* **Get Collection** `list202004Collections`: https://shopify.dev/docs/admin-api/rest/reference/products/collection#show-2020-04
* **Get Collection** `list202007Collections`: https://shopify.dev/docs/admin-api/rest/reference/products/collection#show-2020-07
* **Get Collection Listing** `list202004CollectionListings`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/collectionlisting#show-2020-04
* **Get Comment** `listComments`: https://shopify.dev/docs/admin-api/rest/reference/online-store/comment#show-2020-01
* **Get Country** `list202004Countries`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/country#show-2020-04
* **Get Country Province** `getCountryProvince`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/province#show-2020-04
* **Get Current User** `listCurrentJson`: https://shopify.dev/docs/admin-api/rest/reference/plus/user#current-2020-01
* **Get Current User** `listUserCurrentJson`: https://shopify.dev/docs/admin-api/rest/reference/plus/user#current-2020-04
* **Get Custom Collection** `list202004CustomCollections`: https://shopify.dev/docs/admin-api/rest/reference/products/customcollection#show-2020-04
* **Get Customer** `list202004Customers`: https://shopify.dev/docs/admin-api/rest/reference/customers/customer#show-2020-04
* **Get Customer Address** `getAddresse`: https://shopify.dev/docs/admin-api/rest/reference/customers/customer-address#show-2020-01
* **Get Customer Saved Search** `list202004CustomerSavedSearches`: https://shopify.dev/docs/admin-api/rest/reference/customers/customersavedsearch#show-2020-04
* **Get Discount Code** `getDiscountCode`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#show-2020-01
* **Get Discount Code Batch** `getBatchDiscountCodesJson`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#batch_discount_codes_index-2020-04
* **Get Discount Code Batch** `getPriceRulePriceRule`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#batch_show-2020-04
* **Get Dispute** `listDisputes`: https://shopify.dev/docs/admin-api/rest/reference/shopify_payments/dispute#show-2020-01
* **Get Event** `list202004Events`: https://shopify.dev/docs/admin-api/rest/reference/events/event#show-2020-04
* **Get Fulfillment** `getFulfillment`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillment#show-2020-01
* **Get Fulfillment Event** `getFulfillmentEvent`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentevent#show-2020-04
* **Get Fulfillment Events** `getFulfillmentEventsJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentevent#index-2020-04
* **Get Fulfillment Order** `list202004FulfillmentOrders`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder#show-2020-04
* **Get Fulfillment Service** `list202004FulfillmentServices`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentservice#show-2020-04
* **Get Gift Card** `list202004GiftCards`: https://shopify.dev/docs/admin-api/rest/reference/plus/giftcard#show-2020-04
* **Get Inventory Item Details** `list202004InventoryItems`: https://shopify.dev/docs/admin-api/rest/reference/inventory/inventoryitem#show-2020-04
* **Get Location** `list202004Locations`: https://shopify.dev/docs/admin-api/rest/reference/inventory/location#show-2020-04
* **Get Metafield** `list202004Metafields`: https://shopify.dev/docs/admin-api/rest/reference/metafield#show-2020-04
* **Get Order** `getOrderJson`: Retrieves a single order by its Shopify order ID.
* **Get Order** `list202004Orders`: https://shopify.dev/docs/admin-api/rest/reference/orders/order#show-2020-04
* **Get Order Refund** `getOrderRefund`: https://shopify.dev/docs/admin-api/rest/reference/orders/refund#show-2020-04
* **Get Order Risk** `getOrderRisk`: https://shopify.dev/docs/admin-api/rest/reference/orders/order-risk#show-2020-04
* **Get Order Transaction** `getOrderTransaction`: Retrieves a specific transaction for an order. Transactions attached to multi-currency orders are in the presentment currency by default.
* **Get Payout** `listPayouts`: https://shopify.dev/docs/admin-api/rest/reference/shopify_payments/payout#show-2020-01
* **Get Price Rule Discount Code** `getPriceRuleDiscountCode`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#show-2020-04
* **Get Product** `list202004Products`: https://shopify.dev/docs/admin-api/rest/reference/products/product#show-2020-04
* **Get Product Image** `getImage`: Retrieves a single image for a product by its ID.
* **Get Product Listing** `list202004ProductListings`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/productlisting#show-2020-04
* **Get Province** `getProvince`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/province#show-2020-01
* **Get Recurring Application Charge** `list202004RecurringApplicationCharges`: https://shopify.dev/docs/admin-api/rest/reference/billing/recurringapplicationcharge#show-2020-04
* **Get Redirect** `list202004Redirects`: https://shopify.dev/docs/admin-api/rest/reference/online-store/redirect#show-2020-04
* **Get Report** `list202004Reports`: https://shopify.dev/docs/admin-api/rest/reference/analytics/report#show-2020-04
* **Get Return** `getReturn`: Gets one return by ID with its status, line items (quantities processed and still to process), decline details and reverse fulfillment orders (GraphQL return, API 2026-07). The ID can come from a returns/* event payload (admin_graphql_api_id). Requires read_returns. Check errors: Shopify answers HTTP 200 even when the query fails.
* **Get Reverse Fulfillment Order** `getReverseFulfillmentOrder`: Gets a reverse fulfillment order (the goods coming back for a return) with its line items and their dispositions (GraphQL reverseFulfillmentOrder, API 2026-07). The ID comes from Get Return or a reverse_fulfillment_orders/dispose event. Requires read_returns. Check errors: Shopify answers HTTP 200 even when the query fails.
* **Get Script Tag** `list202004ScriptTags`: https://shopify.dev/docs/admin-api/rest/reference/online-store/scripttag#show-2020-04
* **Get Shop** `list202004ShopJson`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/shop#show-2020-04
* **Get Shop** `listShopJson`: Retrieves the shop's configuration including name, domain, currency, timezone, plan, and address information.
* **Get Shopify Payment Dispute** `getShopifyPaymentDispute`: Retrieves a single Shopify Payments dispute by ID. Requires shopify_payments_payouts or shopify_payments access scope.
* **Get Shopify Payments Balance** `listBalanceJson`: https://shopify.dev/docs/admin-api/rest/reference/shopify_payments/balance#show-2020-01
* **Get Shopify Payments Balance (Duplicate)** `listShopifyPaymentBalanceJson`: DUPLICATE of listBalanceJson — same endpoint GET /admin/api/2024-01/shopify_payments/balance.json. Consider removing this action.
* **Get Theme** `list202004Themes`: https://shopify.dev/docs/admin-api/rest/reference/online-store/theme#show-2020-04
* **Get Usage Charge** `getRecurringApplicationChargeUsageCharge`: https://shopify.dev/docs/admin-api/rest/reference/billing/usagecharge#show-2020-04
* **Get User** `list202004Users`: https://shopify.dev/docs/admin-api/rest/reference/plus/user#show-2020-04
* **Get Webhook** `listWebhooks`: Retrieves a single webhook subscription by ID.
* **List Access Scopes** `listAccessScopesJson`: Retrieves a list of access scopes associated with the current access token.
* **List Application Charges** `list202004ApplicationChargesJson`: https://shopify.dev/docs/admin-api/rest/reference/billing/applicationcharge#index-2020-04
* **List Application Credits** `list202004ApplicationCreditsJson`: https://shopify.dev/docs/admin-api/rest/reference/billing/applicationcredit#index-2020-04
* **List Article Authors** `listArticleAuthorsJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/article#authors-2020-04
* **List Article Count** `listArticleCountJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/article#count-2020-01
* **List Article Tags** `listArticleTagsJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/article#tags-2020-04
* **List Articles** `listArticlesJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/article#index-2020-01
* **List Assets** `listAssetsJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/asset#show-2020-01
* **List Assigned Fulfillment Orders** `list202004AssignedFulfillmentOrdersJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/assignedfulfillmentorder#index-2020-04
* **List Blog Articles** `listBlogArticlesJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/article#index-2020-04
* **List Blog Count** `listBlogCountJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/blog#count-2020-01
* **List Carrier Services** `list202004CarrierServicesJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/carrierservice#index-2020-04
* **List Checkout Count** `listCheckoutCountJson`: https://shopify.dev/docs/admin-api/rest/reference/orders/abandoned-checkouts#count-2020-01
* **List Checkout Payments** `listCheckoutPaymentsJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/payment#index-2020-04
* **List Checkout Shipping Rates** `listCheckoutShippingRatesJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/checkout#shipping_rates-2020-04
* **List Collect Count** `listCollectCountJson`: https://shopify.dev/docs/admin-api/rest/reference/products/collect#count-2020-01
* **List Collection Listing Product Ids** `listCollectionListingProductIdsJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/collectionlisting#product_ids-2020-04
* **List Collection Listings** `list202004CollectionListingsJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/collectionlisting#index-2020-04
* **List Collection Products** `listCollectionProductsJson`: Retrieves a list of products belonging to a collection.
* **List Collects** `list202004CollectsJson`: https://shopify.dev/docs/admin-api/rest/reference/products/collect#index-2020-04
* **List Comment Count** `listCommentCountJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/comment#count-2020-01
* **List Countries** `list202004CountriesJson`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/country#index-2020-04
* **List Country Count** `listCountryCountJson`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/country#count-2020-01
* **List Country Provinces** `listCountryProvincesJson`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/province#index-2020-04
* **List Currencies** `list202004CurrenciesJson`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/currency#index-2020-04
* **List Custom Collection Count** `listCustomCollectionCountJson`: https://shopify.dev/docs/admin-api/rest/reference/products/customcollection#count-2020-01
* **List Custom Collections** `list202004CustomCollectionsJson`: https://shopify.dev/docs/admin-api/rest/reference/products/customcollection#index-2020-04
* **List Customer Addresses** `listAddressesJson`: Retrieves all addresses for a customer.
* **List Customer Orders** `listOrdersJson`: Retrieves all orders belonging to a specific customer.
* **List Customer Saved Searche Count** `listCustomerSavedSearcheCountJson`: https://shopify.dev/docs/admin-api/rest/reference/customers/customersavedsearch#count-2020-01
* **List Customer Saved Searche Customers** `listCustomerSavedSearcheCustomersJson`: https://shopify.dev/docs/admin-api/rest/reference/customers/customersavedsearch#other-2020-01
* **List Customer Saved Searches** `list202004CustomerSavedSearchesJson`: https://shopify.dev/docs/admin-api/rest/reference/customers/customersavedsearch#index-2020-04
* **List Customer Search** `listCustomerSearchJson`: https://shopify.dev/docs/admin-api/rest/reference/customers/customer#search-2020-04
* **List Customers** `list202004CustomersJson`: https://shopify.dev/docs/admin-api/rest/reference/customers/customer#index-2020-04
* **List Deprecated API Calls** `listDeprecatedApiCallsJson`: https://shopify.dev/docs/admin-api/rest/reference/deprecated_api_calls#index-2021-01
* **List Discount Codes in Batch** `getDiscountCodesJson`: Retrieves a list of discount codes for a batch creation job. Duplicate of getBatchDiscountCodesJson — same path but different output schema.
* **List Event Count** `listEventCountJson`: https://shopify.dev/docs/admin-api/rest/reference/events/event#count-2020-01
* **List Events** `list202004EventsJson`: https://shopify.dev/docs/admin-api/rest/reference/events/event#index-2020-04
* **List Fulfillment Count** `listFulfillmentCountJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillment#count-2020-01
* **List Fulfillment Events** `getEventsJson`: Retrieves all events for a fulfillment. Duplicate of getFulfillmentEventsJson — same path.
* **List Fulfillment Order Fulfillments** `listFulfillmentOrderFulfillmentsJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillment#indexV2-2020-01
* **List Fulfillment Order Locations For Move** `listFulfillmentOrderLocationsForMoveJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/locationsformove#index-2020-04
* **List Fulfillment Services** `list202004FulfillmentServicesJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentservice#index-2020-04
* **List Fulfillments** `listFulfillmentsJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillment#index-2020-01
* **List Gift Card Count** `listGiftCardCountJson`: https://shopify.dev/docs/admin-api/rest/reference/plus/giftcard#count-2020-01
* **List Gift Card Search** `listGiftCardSearchJson`: https://shopify.dev/docs/admin-api/rest/reference/plus/giftcard#search-2020-01
* **List Gift Cards** `list202004GiftCardsJson`: https://shopify.dev/docs/admin-api/rest/reference/plus/giftcard#index-2020-04
* **List Inventory** `list202004InventoryItemsJson`: Retrieves a list of inventory items. Each inventory item corresponds to a product variant. Use inventory_item_ids or location_id to filter results.
* **List Inventory Levels** `list202004InventoryLevelsJson`: https://shopify.dev/docs/admin-api/rest/reference/inventory/inventorylevel#index-2020-04
* **List Location Inventory Levels** `listLocationInventoryLevelsJson`: Retrieves all inventory levels at a specific location.
* **List Locations** `list202004LocationsJson`: https://shopify.dev/docs/admin-api/rest/reference/inventory/location#index-2020-04
* **List Locations For Move** `listLocationsForMoveJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/locationsformove#index-2020-01
* **List Metafield Count** `listMetafieldCountJson`: https://shopify.dev/docs/admin-api/rest/reference/metafield#count-2020-01
* **List Metafields** `list202004MetafieldsJson`: https://shopify.dev/docs/admin-api/rest/reference/metafield#index-2020-04
* **List Order Fulfillment Orders** `listFulfillmentOrdersJson`: Retrieves all fulfillment orders associated with a given order.
* **List Order Refunds** `listOrderRefundsJson`: https://shopify.dev/docs/admin-api/rest/reference/orders/refund#index-2020-04
* **List Order Returns** `listOrderReturns`: Lists the returns of one order with their status and totals (GraphQL order.returns, API 2026-07), with cursor pagination. Requires read_returns and read_orders. Check errors: Shopify answers HTTP 200 even when the query fails.
* **List Order Risks** `listOrderRisksJson`: https://shopify.dev/docs/admin-api/rest/reference/orders/order-risk#index-2020-04
* **List Order Transactions** `listOrderTransactions`: Retrieves a list of transactions for an order. Transactions attached to multi-currency orders are in the presentment currency by default.
* **List Orders** `list202004OrdersJson`: https://shopify.dev/docs/admin-api/rest/reference/orders/order#index-2020-04
* **List Policies** `list202004PoliciesJson`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/policy#index-2020-04
* **List Price Rule Discount Codes** `listPriceRuleDiscountCodesJson`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#index-2020-04
* **List Price Rules** `listPriceRules`: Retrieves a list of price rules. Supports filtering by date, limit, and pagination.
* **List Product Ids** `listProductIdsJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/collectionlisting#product_ids-2020-01
* **List Product Images** `listImagesJson`: Retrieves all images for a given product.
* **List Product Listing Count** `listProductListingCountJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/productlisting#count-2020-01
* **List Product Listing IDs** `listProductListingProductIdsJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/productlisting#product_ids-2020-01
* **List Product Listings** `list202004ProductListingsJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/productlisting#index-2020-04
* **List Product Variants** `listVariantsJson`: Retrieves all variants for a given product.
* **List Products** `list202004ProductsJson`: https://shopify.dev/docs/admin-api/rest/reference/products/product#index-2020-04
* **List Products** `listAllProducts`: List Shopify products with pagination (limit, since_id, updated_at_min) and optional filters. Returns array of products under 'products'.
* **List Province Count** `listProvinceCountJson`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/province#count-2020-01
* **List Provinces** `listProvincesJson`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/province#index-2020-01
* **List Recurring Application Charge Usage Charges** `listRecurringApplicationChargeUsageChargesJson`: https://shopify.dev/docs/admin-api/rest/reference/billing/usagecharge#index-2020-04
* **List Recurring Application Charges** `list202004RecurringApplicationChargesJson`: https://shopify.dev/docs/admin-api/rest/reference/billing/recurringapplicationcharge#index-2020-04
* **List Redirect Count** `listRedirectCountJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/redirect#count-2020-01
* **List Return Reasons** `listReturnReasons`: Lists Shopify's return reason definitions (for example Too small, Damaged or defective) with their IDs, for use as returnReasonDefinitionId in Request Return and Create Return (GraphQL returnReasonDefinitions, API 2026-07). Supports a search query and cursor pagination. Requires read_returns.
* **List Returnable Fulfillments** `listReturnableFulfillments`: Lists the fulfilled items of an order that can still be returned (GraphQL returnableFulfillments, API 2026-07). Use it first to get the fulfillmentLineItem IDs and returnable quantities that Request Return and Create Return need. Requires the read_returns scope.
* **List Script Tag Count** `listScriptTagCountJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/scripttag#count-2020-01
* **List Shipping Rates** `listShippingRatesJson`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/checkout#shipping_rates-2020-01
* **List Shipping Zones** `list202004ShippingZonesJson`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/shippingzone#index-2020-04
* **List Shopify Payment Disputes** `listShopifyPaymentDisputesJson`: https://shopify.dev/docs/admin-api/rest/reference/shopify_payments/dispute#index-2020-04
* **List Shopify Payment Payouts** `listShopifyPaymentPayouts`: https://shopify.dev/docs/admin-api/rest/reference/shopify_payments/payout#show-2020-04
* **List Shopify Payment Transactions** `listTransactionsJson`: https://shopify.dev/docs/admin-api/rest/reference/shopify_payments/transaction#index-2020-01
* **List Smart Collection Count** `listSmartCollectionCountJson`: https://shopify.dev/docs/admin-api/rest/reference/products/smartcollection#count-2020-01
* **List Smart Collections** `listSmartCollectionsJson`: Retrieves a list of smart (automated) collections.
* **List Storefront Access Tokens** `list202004StorefrontAccessTokensJson`: https://shopify.dev/docs/admin-api/rest/reference/access/storefrontaccesstoken#index-2020-04
* **List Tender Transactions** `list202004TenderTransactionsJson`: https://shopify.dev/docs/admin-api/rest/reference/tendertransaction#index-2020-04
* **List Theme Assets** `listThemeAssetsJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/asset#show-2020-04
* **List Webhooks** `list202004WebhooksJson`: https://shopify.dev/docs/admin-api/rest/reference/events/webhook#index-2020-04
* **Look Up Discount Code** `listDiscountCodeLookupJson`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#lookup-2020-04
* **Mark Comment Not Spam** `createNotSpamJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/comment#not_spam-2020-01
* **Mark Comment Spam** `createSpamJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/comment#spam-2020-01
* **Move Fulfillment Order** `createFulfillmentOrderMoveJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder#move-2020-04
* **Open Fulfillment** `createFulfillmentOpenJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillment#open-2020-01
* **Open Fulfillment Order** `createFulfillmentOrderOpenJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder#open-2021-01
* **Open Order** `createOrderOpenJson`: https://shopify.dev/docs/admin-api/rest/reference/orders/order#open-2020-04
* **Process Return** `processReturn`: Processes items on an OPEN return: marks quantities as processed, can restock them through dispositions and can refund the customer (GraphQL returnProcess, API 2026-07). Fires the returns/process event. Get return line item IDs from Get Return and the payment transaction ID from the order. Requires write_returns. Check userErrors: Shopify answers HTTP 200 even when the request is refused.
* **Reject Fulfillment Order Cancellation Request** `createCancellationRequestRejectJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/cancellationrequest#reject-2020-04
* **Reject Fulfillment Request** `createFulfillmentRequestRejectJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentrequest#reject-2020-01
* **Remove Comment** `createRemoveJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/comment#remove-2020-01
* **Remove Items From Return** `removeFromReturn`: Removes unprocessed items (or part of their quantity) from a return, for example when the customer keeps one item after all (GraphQL removeFromReturn, API 2026-07). Fires the returns/update event. Requires write_returns. Check userErrors: Shopify answers HTTP 200 even when the request is refused.
* **Reopen Return** `reopenReturn`: Reopens a CLOSED return so more items can be processed (GraphQL returnReopen, API 2026-07). Fires the returns/reopen event. Requires write_returns. Check userErrors: Shopify answers HTTP 200 even when the request is refused.
* **Request Return** `requestReturn`: Creates a return request on an order that the merchant must approve or decline (GraphQL returnRequest, API 2026-07). The return starts with status REQUESTED and fires the returns/request event. Get fulfillmentLineItemId values from List Returnable Fulfillments and returnReasonDefinitionId from List Return Reasons; Shopify refuses an item without a reason. Requires write_returns. Check userErrors: Shopify answers HTTP 200 even when the request is refused.
* **Reschedule Fulfillment Order** `createRescheduleJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder#reschedule-2021-01
* **Restore Comment** `createRestoreJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/comment#restore-2020-01
* **Run GraphQL Query** `runGraphql`: Generic Shopify GraphQL Admin API passthrough. Runs any GraphQL query or mutation against POST /admin/api/2025-01/graphql.json with a query string and optional variables. Use this for capabilities not available in the REST actions (e.g. setting a product's Standard Product Taxonomy category, browsing the taxonomy). Note: GraphQL returns HTTP 200 even on query errors - always check the response `errors` array.
* **Search Customers** `listSearchJson`: Searches for customers matching a supplied query. Supports searching by name, email, phone, and other fields.
* **Send Customer Invite** `createCustomerSendInviteJson`: https://shopify.dev/docs/admin-api/rest/reference/customers/customer#send_invite-2020-04
* **Set Default Customer Address** `updateAddresseDefaultJson`: https://shopify.dev/docs/admin-api/rest/reference/customers/customer-address#default-2020-04
* **Set Inventory Level** `createSetJson`: Sets the inventory level for an inventory item at a location.
* **Set Product Category** `setProductCategory`: Set a product's Standard Product Taxonomy category (GraphQL productUpdate). REST cannot set the taxonomy category, only product_type; this uses the GraphQL Admin API. Provide the product GID and a Shopify taxonomy category GID (get one from Browse Product Taxonomy). Returns the updated product's category and any userErrors. Note: a non-empty userErrors array means the update was rejected even though HTTP status is 200.
* **Update Article** `updateArticle`: https://shopify.dev/docs/admin-api/rest/reference/online-store/article#update-2020-01
* **Update Assets** `updateAssetsJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/asset#update-2020-01
* **Update Blog** `updateBlog`: https://shopify.dev/docs/admin-api/rest/reference/online-store/blog#update-2020-01
* **Update Blog Article** `updateBlogArticle`: https://shopify.dev/docs/admin-api/rest/reference/online-store/article#update-2020-04
* **Update Carrier Service** `update202004CarrierService`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/carrierservice#update-2020-04
* **Update Checkout** `update202004Checkout`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/checkout#update-2020-04
* **Update Collection Listing** `update202004CollectionListing`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/collectionlisting#create-2020-04
* **Update Comment** `updateComment`: https://shopify.dev/docs/admin-api/rest/reference/online-store/comment#update-2020-01
* **Update Country** `update202004Country`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/country#update-2020-04
* **Update Country Province** `updateCountryProvince`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/province#update-2020-04
* **Update Custom Collection** `update202004CustomCollection`: https://shopify.dev/docs/admin-api/rest/reference/products/customcollection#update-2020-04
* **Update Customer** `update202004Customer`: https://shopify.dev/docs/admin-api/rest/reference/customers/customer#update-2020-04
* **Update Customer Address** `updateAddresse`: https://shopify.dev/docs/admin-api/rest/reference/customers/customer-address#update-2020-01
* **Update Customer Saved Search** `update202004CustomerSavedSearche`: https://shopify.dev/docs/admin-api/rest/reference/customers/customersavedsearch#update-2020-04
* **Update Discount Code** `updateDiscountCode`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#update-2020-01
* **Update Fulfillment Service** `update202004FulfillmentService`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentservice#update-2020-04
* **Update Fulfillment Tracking** `createFulfillmentUpdateTrackingJson`: https://shopify.dev/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillment#update_tracking-2020-04
* **Update Gift Card** `update202004GiftCard`: https://shopify.dev/docs/admin-api/rest/reference/plus/giftcard#update-2020-04
* **Update Inventory Item Details** `update202004InventoryItem`: https://shopify.dev/docs/admin-api/rest/reference/inventory/inventoryitem#update-2020-04
* **Update Metafield** `update202004Metafield`: https://shopify.dev/docs/admin-api/rest/reference/metafield#update-2020-04
* **Update Order** `update202004Order`: https://shopify.dev/docs/admin-api/rest/reference/orders/order#update-2020-04
* **Update Order** `updateOrderJson`: Updates fields (e.g. tags) on an existing order.
* **Update Order Risk** `updateOrderRisk`: https://shopify.dev/docs/admin-api/rest/reference/orders/order-risk#update-2020-04
* **Update Price Rule Discount Code** `updatePriceRuleDiscountCode`: https://shopify.dev/docs/admin-api/rest/reference/discounts/discountcode#update-2020-04
* **Update Product** `update202004Product`: https://shopify.dev/docs/admin-api/rest/reference/products/product#update-2020-04
* **Update Product Image** `updateImage`: Updates an existing product image. Can update position, alt text, and variant associations.
* **Update Product Listing** `update202004ProductListing`: https://shopify.dev/docs/admin-api/rest/reference/sales-channels/productlisting#create-2020-04
* **Update Product Variant** `updateVariant`: Updates an existing product variant by ID. Modify price, SKU, barcode, options, weight, inventory policy, image, and more.
* **Update Province** `updateProvince`: https://shopify.dev/docs/admin-api/rest/reference/store-properties/province#update-2020-01
* **Update Redirect** `update202004Redirect`: https://shopify.dev/docs/admin-api/rest/reference/online-store/redirect#update-2020-04
* **Update Report** `update202004Report`: https://shopify.dev/docs/admin-api/rest/reference/analytics/report#update-2020-04
* **Update Script Tag** `update202004ScriptTag`: https://shopify.dev/docs/admin-api/rest/reference/online-store/scripttag#update-2020-04
* **Update Smart Collection** `update202004SmartCollection`: https://shopify.dev/docs/admin-api/rest/reference/products/smartcollection#update-2020-04
* **Update Smart Collection Order** `updateSmartCollectionOrderJson`: https://shopify.dev/docs/admin-api/rest/reference/products/smartcollection#order-2020-04
* **Update Theme** `update202004Theme`: https://shopify.dev/docs/admin-api/rest/reference/online-store/theme#update-2020-04
* **Update Theme Assets** `updateThemeAssetsJson`: https://shopify.dev/docs/admin-api/rest/reference/online-store/asset#update-2020-04
* **Update Webhook** `update202004Webhook`: https://shopify.dev/docs/admin-api/rest/reference/events/webhook#update-2020-04

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| App Uninstalled | `app/uninstalled` | Emitted whenever a shop uninstalls the app. |
| Cart Created | `carts/create` | Emitted whenever a cart is created. |
| Cart Updated | `carts/update` | Emitted whenever a cart is updated. |
| Checkout Created | `checkouts/create` | Emitted whenever a checkout is created. |
| Checkout Deleted | `checkouts/delete` | Emitted whenever a checkout is deleted. |
| Checkout Updated | `checkouts/update` | Emitted whenever a checkout is updated. |
| Customer Created | `customers/create` | Emitted whenever a customer is created. |
| Customer Deleted | `customers/delete` | Emitted whenever a customer is deleted. |
| Customer Updated | `customers/update` | Emitted whenever a customer is updated. |
| Fulfillment Created | `fulfillments/create` | Emitted whenever a fulfillment is created. |

<details>

<summary>See 28 more events</summary>

* **Fulfillment Event Created** `fulfillment_events/create`: Emitted whenever a fulfillment event is created.
* **Fulfillment Updated** `fulfillments/update`: Emitted whenever a fulfillment is updated.
* **Inventory Item Created** `inventory_items/create`: Emitted whenever an inventory item is created.
* **Inventory Item Updated** `inventory_items/update`: Emitted whenever an inventory item is updated.
* **Inventory Level Connected** `inventory_levels/connect`: Emitted whenever an inventory level is connected.
* **Inventory Level Disconnected** `inventory_levels/disconnect`: Emitted whenever an inventory level is disconnected.
* **Inventory Level Updated** `inventory_levels/update`: Emitted whenever an inventory level is updated.
* **Order Cancelled** `orders/cancelled`: Emitted whenever an order is cancelled.
* **Order Created** `orders/create`: Emitted whenever an order is created.
* **Order Deleted** `orders/delete`: Emitted whenever an order is deleted.
* **Order Fulfilled** `orders/fulfilled`: Emitted whenever an order is fulfilled.
* **Order Paid** `orders/paid`: Emitted whenever an order is paid.
* **Order Partially Fulfilled** `orders/partially_fulfilled`: Emitted whenever an order is partially fulfilled.
* **Order Updated** `orders/updated`: Emitted whenever an order is updated.
* **Product Created** `products/create`: Emitted whenever a product is created.
* **Product Deleted** `products/delete`: Emitted whenever a product is deleted.
* **Product Updated** `products/update`: Emitted whenever a product is updated.
* **Refund Created** `refunds/create`: Emitted whenever a refund is created.
* **Return Approved** `returns/approve`: Emitted when a merchant approves a return request (status OPEN).
* **Return Cancelled** `returns/cancel`: Emitted when a return is cancelled.
* **Return Closed** `returns/close`: Emitted when a return is closed.
* **Return Declined** `returns/decline`: Emitted when a merchant declines a return request.
* **Return Processed** `returns/process`: Emitted when return line items are processed (restocked, refunded or exchanged).
* **Return Reopened** `returns/reopen`: Emitted when a closed return is reopened.
* **Return Requested** `returns/request`: Emitted when a customer requests a return (status REQUESTED, waiting for merchant approval).
* **Return Updated** `returns/update`: Emitted when a return is updated, for example when return line items are removed.
* **Reverse Delivery Deliverable Attached** `reverse_deliveries/attach_deliverable`: Emitted when a return shipping label or tracking details are attached to a reverse delivery.
* **Reverse Fulfillment Order Disposed** `reverse_fulfillment_orders/dispose`: Emitted when items on a reverse fulfillment order are disposed (restocked, not restocked, missing or processing later), for example after goods are received back.

</details>
