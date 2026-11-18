---
description: "WooCommerce is the open-source e-commerce plugin for WordPress."
hidden: true
---

# WooCommerce

<img src="../../.gitbook/assets/connectors/woocommerce.png" alt="WooCommerce logo" width="64">

WooCommerce is the open-source e-commerce plugin for WordPress. This connector covers the WooCommerce REST API v3 (wp-json/wc/v3) of your own store: products, variations, attributes and terms, categories, tags, shipping classes, reviews, custom fields, orders, order notes, refunds, order actions, coupons, customers, reports, tax rates and classes, webhooks, settings, payment gateways, shipping zones, locations and methods, system status and tools, and store data (continents, countries, currencies).

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [woocommerce.com](https://woocommerce.com) |
| **Authentication** | Basic auth |
| **Slug** | `woocommerce` |

## Use it

Add WooCommerce from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.woocommerce.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Shipping Zone Method | `addShippingZoneMethod` | Adds a shipping method (e.g. flat_rate, free_shipping, local_pickup) to a shipping zone. |
| Batch Update Coupons | `batchUpdateCoupons` | Creates, updates and deletes up to 100 coupons in one request. |
| Batch Update Customers | `batchUpdateCustomers` | Creates, updates and deletes up to 100 customers in one request. |
| Batch Update Orders | `batchUpdateOrders` | Creates, updates and deletes up to 100 orders in one request. |
| Batch Update Product Attribute Terms | `batchUpdateProductAttributeTerms` | Creates, updates and deletes up to 100 terms of one global product attribute in a single request. |
| Batch Update Product Attributes | `batchUpdateProductAttributes` | Creates, updates and deletes up to 100 global product attributes in one request. |
| Batch Update Product Categories | `batchUpdateProductCategories` | Creates, updates and deletes up to 100 product categories in one request. |
| Batch Update Product Reviews | `batchUpdateProductReviews` | Creates, updates and deletes up to 100 product reviews in one request. |
| Batch Update Product Shipping Classes | `batchUpdateProductShippingClasses` | Creates, updates and deletes up to 100 product shipping classes in one request. |
| Batch Update Product Tags | `batchUpdateProductTags` | Creates, updates and deletes up to 100 product tags in one request. |

<details>

<summary>See 129 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Update Product Variations | `batchUpdateProductVariations` | Creates, updates and deletes up to 100 variations of one variable product in a single request. |
| Batch Update Products | `batchUpdateProducts` | Creates, updates and deletes up to 100 products in one request. |
| Batch Update Setting Options | `batchUpdateSettingOptions` | Updates several setting options of one settings group in a single request. |
| Batch Update Tax Rates | `batchUpdateTaxRates` | Creates, updates and deletes up to 100 tax rates in one request. |
| Batch Update Webhooks | `batchUpdateWebhooks` | Creates, updates and deletes up to 100 webhooks in one request. |
| Create Coupon | `createCoupon` | Creates a new coupon. |
| Create Customer | `createCustomer` | Creates a new customer with optional billing and shipping addresses. |
| Create Order | `createOrder` | Creates a new order with billing and shipping addresses, line items, shipping, fee and coupon lines. Set set_paid to true to mark it paid (status processing, stock reduced). |
| Create Order Note | `createOrderNote` | Creates a new note on an order. A customer note is shown to the customer and they are notified; otherwise it is for admin reference only. |
| Create Order Refund | `createOrderRefund` | Creates a refund for an order, for a total amount or for specific line items. With api_refund true the payment gateway is asked to refund the money; with api_restock true refunded items go back into stock. |
| Create Product | `createProduct` | Creates a new product (simple, grouped, external or variable) with prices, stock, shipping, categories, tags, images and attributes. |
| Create Product Attribute | `createProductAttribute` | Creates a new global product attribute, such as Color or Size, that products and variations can use. |
| Create Product Attribute Term | `createProductAttributeTerm` | Creates a new term (a value such as Red or XL) for a global product attribute. |
| Create Product Category | `createProductCategory` | Creates a new product category, optionally under a parent category and with an image. |
| Create Product Review | `createProductReview` | Creates a new product review for a product, with reviewer details and an optional 0-5 rating. |
| Create Product Shipping Class | `createProductShippingClass` | Creates a new product shipping class, used to group products for shipping rates. |
| Create Product Tag | `createProductTag` | Creates a new product tag. |
| Create Product Variation | `createProductVariation` | Creates a new variation of a variable product, with its attributes, prices, stock and image. |
| Create Shipping Zone | `createShippingZone` | Creates a new shipping zone. Add locations and methods to it with the zone location and zone method actions. |
| Create Tax Class | `createTaxClass` | Creates a new tax class. WooCommerce makes the slug from the name. |
| Create Tax Rate | `createTaxRate` | Creates a new tax rate for a country, state, postcodes or cities, in a tax class. |
| Create Webhook | `createWebhook` | Creates a new webhook that sends a topic (such as order.created) to a delivery URL. |
| Delete Coupon | `deleteCoupon` | Deletes a coupon. Set force to true to delete it permanently; otherwise it is moved to the trash. |
| Delete Customer | `deleteCustomer` | Permanently deletes a customer. Customers cannot be trashed, so force must be true; reassign moves the customer's posts to another user ID. |
| Delete Order | `deleteOrder` | Deletes an order. Set force to true to delete it permanently; otherwise it is moved to the trash. |
| Delete Order Note | `deleteOrderNote` | Permanently deletes a note from an order. Notes cannot be trashed, so force must be true. |
| Delete Order Refund | `deleteOrderRefund` | Permanently deletes a refund from an order. Refunds cannot be trashed, so force must be true. |
| Delete Product | `deleteProduct` | Deletes a product. Set force to true to delete it permanently; otherwise it is moved to the trash. |
| Delete Product Attribute | `deleteProductAttribute` | Permanently deletes a global product attribute. Attributes cannot be trashed, so force must be true. |
| Delete Product Attribute Term | `deleteProductAttributeTerm` | Permanently deletes a term of a global product attribute. Terms cannot be trashed, so force must be true. |
| Delete Product Category | `deleteProductCategory` | Permanently deletes a product category. Categories cannot be trashed, so force must be true. |
| Delete Product Review | `deleteProductReview` | Deletes a product review. By default it goes to the trash; set force to true to delete it permanently. |
| Delete Product Shipping Class | `deleteProductShippingClass` | Permanently deletes a product shipping class. Shipping classes cannot be trashed, so force must be true. |
| Delete Product Tag | `deleteProductTag` | Permanently deletes a product tag. Tags cannot be trashed, so force must be true. |
| Delete Product Variation | `deleteProductVariation` | Deletes a variation of a variable product. Set force to true to delete it permanently; otherwise it is moved to the trash. |
| Delete Shipping Zone | `deleteShippingZone` | Permanently deletes a shipping zone. Shipping zones cannot be trashed, so force must be true. |
| Delete Shipping Zone Method | `deleteShippingZoneMethod` | Removes a shipping method from a shipping zone. Methods cannot be trashed, so force must be true. |
| Delete Tax Class | `deleteTaxClass` | Permanently deletes a tax class by its slug. Tax classes cannot be trashed, so force must be true. |
| Delete Tax Rate | `deleteTaxRate` | Permanently deletes a tax rate. Tax rates cannot be trashed, so force must be true. |
| Delete Webhook | `deleteWebhook` | Permanently deletes a webhook. Webhooks cannot be trashed, so force must be true. |
| Duplicate Product | `duplicateProduct` | Duplicates an existing product and returns the new copy. |
| Get Continent | `getContinent` | Retrieves one continent by its 2 character code (e.g. EU, NA) with its countries and states. |
| Get Country | `getCountry` | Retrieves one country by its ISO3166 alpha-2 code (e.g. US) with its states. |
| Get Coupon | `getCoupon` | Retrieves a specific coupon by ID. |
| Get Coupons Totals | `getCouponsTotals` | Retrieves the number of coupons per coupon type. |
| Get Currency | `getCurrency` | Retrieves one currency by its ISO4217 code (e.g. USD) with name and symbol. |
| Get Current Currency | `getCurrentCurrency` | Retrieves the store's current currency: its ISO 4217 code, full name and symbol. |
| Get Customer | `getCustomer` | Retrieves a specific customer by ID, including billing and shipping addresses. |
| Get Customers Totals | `getCustomersTotals` | Retrieves the number of customers per customer type (paying and non-paying). |
| Get Order | `getOrder` | Retrieves a specific order by ID, with its addresses, line items, tax, shipping, fee and coupon lines, and refunds. |
| Get Order Note | `getOrderNote` | Retrieves a specific note from an order. |
| Get Order Refund | `getOrderRefund` | Retrieves a specific refund from an order. |
| Get Orders Totals | `getOrdersTotals` | Retrieves the number of orders per order status. |
| Get Payment Gateway | `getPaymentGateway` | Retrieves one payment gateway and its settings, e.g. bacs, cheque or cod. |
| Get Product | `getProduct` | Retrieves a specific product by ID, with prices, stock, shipping, categories, tags, images, attributes and variation IDs. |
| Get Product Attribute | `getProductAttribute` | Retrieves a specific global product attribute by ID. |
| Get Product Attribute Term | `getProductAttributeTerm` | Retrieves a specific term of a global product attribute by ID. |
| Get Product Category | `getProductCategory` | Retrieves a specific product category by ID. |
| Get Product Review | `getProductReview` | Retrieves a specific product review by ID. |
| Get Product Shipping Class | `getProductShippingClass` | Retrieves a specific product shipping class by ID. |
| Get Product Tag | `getProductTag` | Retrieves a specific product tag by ID. |
| Get Product Variation | `getProductVariation` | Retrieves a specific variation of a variable product by ID. |
| Get Products Totals | `getProductsTotals` | Retrieves the number of products per product type. |
| Get Reviews Totals | `getReviewsTotals` | Retrieves the number of product reviews per rating. |
| Get Sales Report | `getSalesReport` | Retrieves the sales report for a period (week, month, last_month, year) or a date range. |
| Get Setting Option | `getSettingOption` | Retrieves one setting option from a settings group, e.g. group general, id woocommerce_currency. |
| Get Shipping Method | `getShippingMethod` | Retrieves one shipping method type available in the store, e.g. flat_rate. |
| Get Shipping Zone | `getShippingZone` | Retrieves a specific shipping zone by ID. Zone 0 is the built-in "Locations not covered by your other zones" zone. |
| Get Shipping Zone Method | `getShippingZoneMethod` | Retrieves one shipping method of a shipping zone by its instance ID. |
| Get System Status | `getSystemStatus` | Retrieves the store's system status report: environment, database, plugins, theme, settings, security, pages and logging. |
| Get System Status Tool | `getSystemStatusTool` | Retrieves one system status tool by ID, e.g. clear_transients. |
| Get Tax Rate | `getTaxRate` | Retrieves a specific tax rate by ID. |
| Get Top Sellers Report | `getTopSellersReport` | Retrieves the top selling products for a period or a date range. |
| Get Webhook | `getWebhook` | Retrieves a specific webhook by ID. |
| List Continents | `listContinents` | Lists all continents with their countries, states and local formats (currency, units, separators). |
| List Countries | `listCountries` | Lists all countries with their states. |
| List Coupons | `listCoupons` | Lists all the coupons that have been created, with paging, search, date, ID and code filters. |
| List Currencies | `listCurrencies` | Lists all currencies WooCommerce supports, with name and symbol. |
| List Customer Downloads | `listCustomerDownloads` | Retrieves a customer's download permissions: the downloadable files they bought, with remaining downloads and expiry. |
| List Customers | `listCustomers` | Lists the store's customers, with paging, search, email and role filters. |
| List Data Endpoints | `listDataEndpoints` | Lists the available store data endpoints (continents, countries, currencies). |
| List Order Email Templates | `listOrderEmailTemplates` | Retrieves the email templates that are available for the given order, to use with Send Order Email To Customer. |
| List Order Notes | `listOrderNotes` | Lists all the notes on an order, optionally only customer or internal notes. |
| List Order Refunds | `listOrderRefunds` | Lists all the refunds of an order, with paging, search and date filters. |
| List Orders | `listOrders` | Lists the store's orders, with paging, search, date, status, customer, product and source filters. |
| List Payment Gateways | `listPaymentGateways` | Lists all payment gateways installed in the store, with their settings. |
| List Product Attribute Terms | `listProductAttributeTerms` | Lists all terms of a global product attribute, with paging, search and sorting. |
| List Product Attributes | `listProductAttributes` | Lists all global product attributes. |
| List Product Categories | `listProductCategories` | Lists all product categories, with paging, search, parent, product and slug filters. |
| List Product Custom Field Names | `listProductCustomFieldNames` | Retrieves the names of custom fields (product meta keys) used on products, with paging and search. |
| List Product Reviews | `listProductReviews` | Lists product reviews, with filters for product, reviewer, status, dates, paging and sorting. |
| List Product Shipping Classes | `listProductShippingClasses` | Lists all product shipping classes, with paging, search and sorting. |
| List Product Tags | `listProductTags` | Lists all product tags, with paging, search, product and slug filters. |
| List Product Variations | `listProductVariations` | Lists the variations of a variable product, with paging, search, SKU, status, price and stock filters. |
| List Products | `listProducts` | Lists the store's products, with paging, search, SKU, status, type, category, tag, attribute, price, stock and other filters. |
| List Refunds | `listRefunds` | Lists refunds from the whole store, regardless of which order they belong to, with date, parent and paging filters. |
| List Reports | `listReports` | Retrieves the list of available reports (slug and description of each). |
| List Setting Options | `listSettingOptions` | Lists all setting options in a settings group, e.g. general. |
| List Settings Groups | `listSettingsGroups` | Lists all settings groups (general, products, tax, shipping, checkout, account, email, advanced and more). |
| List Shipping Methods | `listShippingMethods` | Lists all shipping method types available in the store. |
| List Shipping Zone Locations | `listShippingZoneLocations` | Lists all locations (countries, states, postcodes, continents) of a shipping zone. |
| List Shipping Zone Methods | `listShippingZoneMethods` | Lists all shipping methods of a shipping zone. |
| List Shipping Zones | `listShippingZones` | Lists all shipping zones in the store. |
| List System Status Tools | `listSystemStatusTools` | Lists all system status tools (maintenance tasks such as clearing transients). |
| List Tax Classes | `listTaxClasses` | Lists all tax classes in the store. |
| List Tax Rates | `listTaxRates` | Lists all tax rates, with paging, sorting and a tax class filter. |
| List Webhooks | `listWebhooks` | Lists all webhooks, with status, date, search and paging filters. |
| Preview Order Refund | `previewOrderRefund` | Previews a refund for an order without creating it: returns the product, shipping and fee breakdown and the maximum refundable amount (WooCommerce 11.1.0 or later). |
| Run System Status Tool | `runSystemStatusTool` | Runs a system status tool by ID and returns whether it succeeded and its message. |
| Send Order Details To Customer | `sendOrderDetailsToCustomer` | Triggers an email to the customer with the details of their order. If the order has no billing email you can give one; if it already has one, the call fails unless force_email_update is true. |
| Send Order Email To Customer | `sendOrderEmailToCustomer` | Triggers an email to a customer about the status of their order, using a chosen email template that fits the order (for example customer_on_hold_order). If no template is given, the best one is picked from the order status. |
| Update Coupon | `updateCoupon` | Makes changes to a coupon. Only the fields you send are changed. |
| Update Customer | `updateCustomer` | Makes changes to a customer. Only the fields you send are changed. |
| Update Order | `updateOrder` | Makes changes to an order, such as its status, addresses or lines. Only the fields you send are changed; to change an existing line item, send its id with the new values. |
| Update Payment Gateway | `updatePaymentGateway` | Makes changes to a payment gateway: enable or disable it, change title, description, order or its settings. |
| Update Product | `updateProduct` | Makes changes to a product. Only the fields you send are changed. |
| Update Product Attribute | `updateProductAttribute` | Makes changes to a global product attribute. Only the fields you send are changed. |
| Update Product Attribute Term | `updateProductAttributeTerm` | Makes changes to a term of a global product attribute. Only the fields you send are changed. |
| Update Product Category | `updateProductCategory` | Makes changes to a product category. Only the fields you send are changed. |
| Update Product Review | `updateProductReview` | Makes changes to a product review, such as its status, text or rating. Only the fields you send are changed. |
| Update Product Shipping Class | `updateProductShippingClass` | Makes changes to a product shipping class. Only the fields you send are changed. |
| Update Product Tag | `updateProductTag` | Makes changes to a product tag. Only the fields you send are changed. |
| Update Product Variation | `updateProductVariation` | Makes changes to a variation of a variable product. Only the fields you send are changed. |
| Update Setting Option | `updateSettingOption` | Changes the value of one setting option in a settings group. |
| Update Shipping Zone | `updateShippingZone` | Makes changes to a shipping zone's name or order. |
| Update Shipping Zone Locations | `updateShippingZoneLocations` | Replaces all locations of a shipping zone with the list you send. Send an empty list [] to remove all locations. |
| Update Shipping Zone Method | `updateShippingZoneMethod` | Makes changes to a shipping method of a shipping zone: order, enabled, or settings such as title and cost. |
| Update Tax Rate | `updateTaxRate` | Makes changes to a tax rate. Only the fields you send are changed. |
| Update Webhook | `updateWebhook` | Makes changes to a webhook, such as pausing it or changing its topic. Only the fields you send are changed. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Coupon Created | `coupon.created` | Sent when a coupon is created. The body is the full coupon object, as returned by Get Coupon. Captured from a live WooCommerce 11.3 delivery. Headers carry X-WC-Webhook-Topic (coupon.created) and X-WC-Webhook-Signature. |
| Coupon Deleted | `coupon.deleted` | Sent when a coupon is deleted (trashed or deleted permanently). The body holds only the coupon ID. Captured from a live WooCommerce 11.3 delivery. |
| Coupon Restored | `coupon.restored` | Sent when a coupon is restored from the trash. Per the WooCommerce docs the body is the full coupon object (same fields as coupon.updated). Not captured live in testing. |
| Coupon Updated | `coupon.updated` | Sent when a coupon is updated. The body is the full coupon object, as returned by Get Coupon. Captured from a live WooCommerce 11.3 delivery. |
| Customer Created | `customer.created` | Sent when a customer is created. The body is the full customer object, as returned by Get Customer. Captured from a live WooCommerce 11.3 delivery. Headers carry X-WC-Webhook-Topic (customer.created) and X-WC-Webhook-Signature. |
| Customer Deleted | `customer.deleted` | Sent when a customer is deleted. The body holds only the customer ID. Captured from a live WooCommerce 11.3 delivery. |
| Customer Updated | `customer.updated` | Sent when a customer is updated. The body is the full customer object, as returned by Get Customer. Captured from a live WooCommerce 11.3 delivery. |
| Order Created | `order.created` | Sent when an order is created. The body is the full order object, as returned by Get Order. Captured from a live WooCommerce 11.3 delivery. Headers carry X-WC-Webhook-Topic (order.created) and X-WC-Webhook-Signature (base64 HMAC-SHA256 of the body with the webhook secret). |
| Order Deleted | `order.deleted` | Sent when an order is deleted (trashed or deleted permanently). The body holds only the order ID. Captured from a live WooCommerce 11.3 delivery. |
| Order Restored | `order.restored` | Sent when an order is restored from the trash. Per the WooCommerce docs the body is the full order object (same fields as order.updated). Not captured live in testing. |

<details>

<summary>See 5 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Order Updated | `order.updated` | Sent when an order is updated (including status changes and refunds). The body is the full order object, as returned by Get Order. Captured from a live WooCommerce 11.3 delivery. Headers carry X-WC-Webhook-Topic (order.updated) and X-WC-Webhook-Signature. |
| Product Created | `product.created` | Sent when a product is created. The body is the full product object, as returned by Get Product. Captured from a live WooCommerce 11.3 delivery. Headers carry X-WC-Webhook-Topic (product.created) and X-WC-Webhook-Signature (base64 HMAC-SHA256 of the body with the webhook secret). |
| Product Deleted | `product.deleted` | Sent when a product is deleted (trashed or deleted permanently). The body holds only the product ID. Captured from a live WooCommerce 11.3 delivery. |
| Product Restored | `product.restored` | Sent when a product is restored from the trash. Per the WooCommerce docs the body is the full product object (same fields as product.updated). Not captured live in testing. |
| Product Updated | `product.updated` | Sent when a product is updated. The body is the full product object, as returned by Get Product. Captured from a live WooCommerce 11.3 delivery. Headers carry X-WC-Webhook-Topic (product.updated) and X-WC-Webhook-Signature. |

</details>
