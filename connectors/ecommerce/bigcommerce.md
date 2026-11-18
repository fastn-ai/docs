---
description: "BigCommerce REST Management API — Catalog (products, categories, brands, variants, images, modifiers), Orders (V2), Customers (V3), and Carts & Checkouts (V3)."
---

# BigCommerce

BigCommerce REST Management API — Catalog (products, categories, brands, variants, images, modifiers), Orders (V2), Customers (V3), and Carts & Checkouts (V3). Supports OAuth 2.0 app installs and store-level X-Auth-Token API accounts.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [bigcommerce.com](https://bigcommerce.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 607 |
| **Events** | 90 |
| **Slug** | `bigcommerce` |

## Use it

Add BigCommerce from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bigcommerce.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate a Theme | `activateStoreTheme` | Activates a store Theme variation. Required: variation_id and which (original, last_activated, last_created). Returns 204 on success. |
| Add Cart Line Items | `addCartLineItems` | Add line_items to an existing cart. |
| Add Checkout Billing Address | `addCheckoutBillingAddress` | Add a billing address to a checkout. Required before order conversion. |
| Add Checkout Consignments | `addCheckoutConsignments` | Add consignments (shipping addresses + line items + chosen shipping method) to a checkout. |
| Add Checkout Coupon | `addCheckoutCoupon` | Apply a coupon code to a checkout. |
| Add Wishlist Item | `addWishlistItem` | Adds one or more items to a wishlist. Body has an items array of objects with product_id and optional variant_id. |
| Apply Checkout Discount | `applyCheckoutDiscount` | Manually apply a discount to a checkout (V3). |
| Archive Order | `archiveOrder` | Soft-delete (archive) an order. Order is hidden but recoverable via control panel. |
| Capture Order Payment | `captureOrderPayment` | Capture the payment for an order (v3). No request body. Sets payment_status to 'capture pending'. |
| Create a Blog Post | `createBlogPost` | Creates a blog post (Content v2). Required: title, body. Field-by-field body. |
| Create a Currency | `createCurrency` | Creates a currency (v2). Required: currency_code, currency_exchange_rate, name, token, token_location, decimal_token, thousands_token, decimal_places. |
| Create a Customer (v2) | `createCustomerV2` | Creates a customer (v2, deprecated). Required fields: first_name, last_name, email. |
| Create a Customer Address (v2) | `createCustomerV2Address` | Creates a new customer address (v2, deprecated). Required: first_name, last_name, phone, street_1, city, state, zip, country. State cannot be null; pass a space for no state. |
| Create a Page (v2) | `createPageV2` | Creates a page (Content v2, deprecated). Required: type, name, body. Field-by-field body. |
| Create a Placement | `createPlacement` | Creates a widget Placement, positioning a widget in a region on a template file. Required: widget_uuid, template_file. |
| Create a Redirect (v2) | `createRedirectV2` | Creates a redirect URL (Content v2, deprecated). Required: path, forward. Field-by-field body. |
| Create a Script | `createScript` | Creates a Script. Required: name. If kind is 'src' supply src; if 'script_tag' supply html. Limit 50 scripts per channel. |
| Create a Site | `createSite` | Create a site that links a headless storefront to a sales channel. POST /v3/sites. |
| Create a Site Route | `createSiteRoute` | Create a route that tells BigCommerce how to link to pages on a headless storefront. POST /v3/sites/{site_id}/routes. |
| Create a Widget | `createWidget` | Creates a Widget. Required: name, widget_template_uuid. Limit of 100,000 widgets per store and 150 per page. |
| Create a Widget Template | `createWidgetTemplate` | Creates a Widget Template (reusable Handlebars HTML). Required: name, template. Limit of 1000 custom widget templates per store. |
| Create a Wishlist | `createWishlist` | Creates a wishlist. Required: customer_id. Optionally include name, is_public, and items. |
| Create Abandoned Cart Email Template | `createAbandonedCartEmail` | Create an abandoned cart email template. The template object must contain subject, body, and translations. |
| Create Absolute Inventory Adjustments | `createAbsoluteInventoryAdjustments` | Set inventory on-hand quantities to ABSOLUTE values for one or more items at specific locations. Body is a JSON object {reason, items[]}; each item has location_id, ONE of sku/product_id/variant_id (flat on the item, NOT nested), and an absolute quantity (&gt;= 0). Pass the entire payload as a JSON-encoded string in 'items'. Returns a transaction_id (processed asynchronously). |
| Create Banner | `createBanner` | Creates a Banner. Required: name, content, page, location, date_type. |
| Create Brand | `createBrand` | Creates a brand in the store catalog. Only 'name' is required; it must be unique. Use custom_url to control the storefront SEO URL (/b/&lt;slug&gt;/), otherwise BigCommerce autogenerates it from the name. |
| Create Brand Image | `createBrandImage` | Uploads a brand image via multipart form-data (field image_file). Only one image at a time. Returns the resulting image_url. [BLOCKED: multipart binary upload unsupported by HTTP executor] |
| Create Brand Metafield | `createBrandMetafield` | Creates a metafield on a brand. Required: namespace, key, value, permission_set. Max 250 metafields per resource per client ID. |
| Create Brand Metafields (Batch) | `createBrandMetafieldsBatch` | Creates up to 50 brand metafields in a single request. |
| Create Bulk Pricing Rule | `createBulkPricingRule` | Creates a bulk pricing rule for a product. Required: quantity_min, quantity_max, type, amount. Returns {data,meta}. |
| Create Carrier Connection | `createCarrierConnection` | Creates a Carrier Connection (v2). Returns 204 for both successful and unsuccessful connect attempts; 400 if a required field is missing. The connection object varies by carrier. |
| Create Cart | `createCart` | Create a new cart. Pass line_items as an array of product/variant references with quantity. Optionally set customer_id, channel_id, currency.code. |
| Create Cart Metafield | `createCartMetafield` | Create a metafield for a cart. permission_set, namespace, key, and value are required. |
| Create Cart Metafields (Batch) | `createCartMetafieldsBatch` | Creates up to 50 cart metafields in a single request. |
| Create Cart Redirect URLs | `createCartRedirectUrls` | Generate cart_url, checkout_url, embedded_checkout_url for a cart. URLs expire in 24 hours. |
| Create Category | `createCategory` | Create a category in a category tree (POST /catalog/trees/categories). Required: name, url (path), tree_id, parent_id. parent_id=0 makes it top-level. Returns {data:[category],meta}. Use tree_id 6 for the default channel_id=1 storefront on this store. The legacy POST /catalog/categories is unavailable on this multi-tree store (422 category_id). |
| Create Category Image | `createCategoryImage` | Uploads a category image via multipart form-data (field image_file). Max 1MB. Returns the resulting image_url. [BLOCKED: multipart binary upload unsupported by HTTP executor] |
| Create Category Metafield | `createCategoryMetafield` | Creates a metafield on a category. Required: namespace, key, value, permission_set. Max 250 metafields per resource per client ID. |
| Create Category Metafields (Batch) | `createCategoryMetafieldsBatch` | Creates up to 50 category metafields in a single request. |
| Create Channel | `createChannel` | Creates a Channel. name, type and platform are required. |
| Create Channel Currency Assignments | `createSingleChannelCurrencyAssignments` | Sets enabled currencies and default currency for a specific channel. |
| Create Channel Listings | `createChannelListings` | Creates one or more Channel Listings for a specific channel. Body is a JSON array string; each item has product_id, state, variants (required), and optional external_id, name, description. |
| Create Channel Menus | `createChannelMenus` | Creates or replaces the list of control panel side navigation menus for a channel. |
| Create Channel Metafield | `createChannelMetafield` | Creates a channel metafield. namespace, key, value and permission_set are required. |
| Create Channel Metafields (Batch) | `createChannelMetafieldsBatch` | Creates up to 50 channel metafields in a single request. |
| Create Channel Site | `createChannelSite` | Creates a site for the provided channel (alias of POST /sites). |
| Create Checkout Order | `createCheckoutOrder` | Convert a fully-prepared checkout into an order. Returns the created order. |
| Create Checkout Token | `createCheckoutToken` | Create a single-use checkout token used to display a guest order confirmation page. |
| Create Complex Rule | `createComplexRule` | Creates a product complex rule. Required: product_id and a conditions array where each condition references modifier_id, modifier_value_id, and variant_id. Returns {data,meta}. |
| Create Coupon | `createCoupon` | Creates a Coupon. Required: name, code, type, amount, applies_to. |
| Create Customer Addresses | `createCustomerAddresses` | Create addresses for customers (V3 expects an array). Each address must include customer_id, first_name, last_name, address1, city, state_or_province, postal_code, country_code. |
| Create Customer Attributes | `createCustomerAttributes` | Create customer attribute definitions (max 50 per store). |
| Create Customer Group | `createCustomerGroup` | Creates a customer group. Only name is required; category access, discount rules and default/guest flags are optional. |
| Create Customer Impersonation Token | `createCustomerImpersonationToken` | Returns a Storefront API token that allows impersonating customers on GraphQL POST requests. channel_id and expires_at required. POST /v3/storefront/api-token-customer-impersonation. |
| Create Customer Metafield | `createCustomerMetafield` | Creates a metafield on a customer. Namespace, key, value and permission_set are required. |
| Create Customer Metafields (Batch) | `createCustomerMetafieldsBatch` | Creates up to 50 customer metafields in a single request. |
| Create Customers | `createCustomers` | Create one or more customers (V3 expects an array). For a single customer, wrap in customers=[customer]. Each customer requires first_name, last_name, email. |
| Create Favicon Image | `createFaviconImage` | Uploads an image file (GIF/JPEG/PNG) to use as the storefront favicon. Pass the file in the FaviconFile input. Returns 204 No Content. |
| Create Gift Certificate | `createGiftCertificate` | Creates a Gift Certificate. Required: to_name, to_email, from_name, from_email, amount. No email notification is triggered. |
| Create Inventory Locations | `createInventoryLocations` | Create one or more inventory locations (bulk async endpoint). Body is a JSON array of location objects passed as a JSON-encoded string in 'items'. Each object requires code, label, type_id, enabled, description, managed_by_external_source, time_zone, and a non-empty address (with address1, city, state, zip, country_code, phone, email and a geo_coordinates object {latitude, longitude}). Returns a transaction_id (processed asynchronously). |
| Create Location Metafield | `createLocationMetafield` | Create a metafield on a specific inventory location. Requires namespace, key, value, and permission_set. |
| Create Location Metafields (Batch) | `createLocationMetafieldsBatch` | Creates up to 50 location metafields in a single request. |
| Create Logo Image | `createLogoImage` | Uploads an image file (GIF/JPEG/PNG) to use as the storefront logo. Pass the file in the LogoFile input. Returns 204 No Content. |
| Create Modifier Value | `createModifierValue` | Creates a value for a product modifier. Requires label and sort_order; optional value_data and adjusters. |
| Create Modifier Value Image | `createModifierValueImage` | Uploads an image for a modifier value via multipart form-data. The image shows on the storefront when the value is selected. |
| Create Multiple Channels Currency Assignments | `createMultipleChannelsCurrencyAssignments` | Sets enabled currencies and default currency for multiple channels. Body is a JSON array string of objects each with channel_id, enabled_currencies, default_currency. |
| Create Order | `createOrder` | Create a new order (V2). Requires billing_address and products. status_id 11 = Awaiting Fulfillment. |
| Create Order Metafield | `createOrderMetafield` | Creates an order Metafield (v3). |
| Create Order Metafields (Batch) | `createOrderMetafieldsBatch` | Creates up to 50 order metafields in a single request. |
| Create Order Refund | `createOrderRefund` | Creates a refund for an order (v3). Provide items and payments arrays; optional merchant_calculated_override. |
| Create Order Refund Quote | `createOrderRefundQuote` | Calculate tax/total refund amount and available payment options for a single order refund (v3). Provide items to refund as a JSON array. |
| Create Order Shipment | `createOrderShipment` | Create a shipment for an order with tracking info. Marks order as Shipped when all items shipped. |
| Create Pages | `createPages` | Creates one or more content pages (Pages v3 bulk). Accepts a JSON array string of page objects in the 'items' input. |
| Create Payment Access Token (v3) | `createPaymentAccessToken` | Creates a single-use payment access token (PAT) tied to a specific order. The returned token is required to process a payment via the BigCommerce Payments API. |
| Create Price List | `createPriceList` | Creates a Price List. Required field: name. |
| Create Price List Assignments | `createPriceListAssignments` | Creates a batch of Price List Assignments (limit 25). Body is a JSON array string of assignment objects, each with price_list_id (required), customer_group_id, channel_id. |
| Create Product | `createProduct` | Creates a product in the store catalog. Requires name, type, weight and price. Supports the full BigCommerce product model including SEO fields (custom_url, page_title, meta_keywords), Open Graph fields, shipping dimensions, pre-order settings, gift wrapping, and nested custom_fields, images, videos, bulk_pricing_rules and variants. |
| Create Product Custom Field | `createProductCustomField` | Add a custom field (name/value pair) to a product. |
| Create Product Image | `createProductImage` | Attach an image to a product via URL or base64. is_thumbnail marks it as primary. |
| Create Product Metafield | `createProductMetafield` | Creates a product metafield. Required: namespace, key, value, permission_set. Returns {data,meta}. |
| Create Product Metafields (Batch) | `createProductMetafieldsBatch` | Creates up to 50 product metafields in a single request. |
| Create Product Modifier | `createProductModifier` | Create a modifier for a product. |
| Create Product Review | `createProductReview` | Creates a product review. Required: title, date_reviewed. Returns {data,meta}. |
| Create Product Variant | `createProductVariant` | Create a new variant for a product. |
| Create Product Variant Metafield | `createVariantMetafield` | Creates a metafield (arbitrary key-value attribute) on a product variant. |
| Create Product Variant Option | `createProductOption` | Creates a variant option on a product. Requires display_name, type, and an option_values array. |
| Create Product Variant Option Value | `createOptionValue` | Creates a value for a product variant option. Requires label and sort_order. |
| Create Product Video | `createProductVideo` | Creates a product video. Required: video_id (ID of the video on the host site, e.g. YouTube). Returns {data,meta}. |
| Create Promotion | `createPromotion` | Creates a promotion. redemption_type and rules are required. Returns the created promotion in a {data} envelope. |
| Create Promotion Code | `createPromotionCode` | Creates a single coupon code on a COUPON-type promotion. code is required. Returns the created code in a {data} envelope. |
| Create Redirects Export Job | `createRedirectExportJob` | Creates a new 301 Redirects export job (Redirects v3 Import-Export). Returns the job ID. |
| Create Redirects Import Job | `createRedirectImportJob` | Creates a new 301 Redirects import job from a CSV file (Redirects v3 Import-Export). The import_file is provided as multipart form-data. |
| Create Refund Quotes (Batch) | `createRefundQuotesBatch` | Calculate tax/total refund amount and available payment options for a batch of one or more order refunds (v3). Accepts a JSON array string of refund quote requests. [BLOCKED: provider returns 422 'tax_adjustment_amount must be present' even when the field is present and the body exactly matches the documented batch example (with or without order_id). The single-order endpoint createOrderRefundQuote works with the identical item shape, confirming this is a store-side bug in the batch /orders/payment_actions/refund_quotes endpoint.] |
| Create Relative Inventory Adjustments | `createRelativeInventoryAdjustments` | Increment/decrement inventory on-hand quantities by RELATIVE amounts for one or more items at specific locations. Body is a JSON object {reason, items[]}; each item has location_id, ONE of sku/product_id/variant_id (flat on the item, NOT nested), and a quantity delta (must be &gt; 0; the relative endpoint rejects 0). Pass the entire payload as a JSON-encoded string in 'items'. Returns a transaction_id (processed asynchronously). |
| Create Shipping Method | `createShippingMethod` | Creates a Shipping Method in a zone (v2). Requires name, type and settings. |
| Create Shipping Zone | `createShippingZone` | Creates a Shipping Zone (v2). Requires name and type. Locations vary by type (zip\|country\|state\|global). |
| Create Store Metafields (Batch) | `createStoreMetafieldsBatch` | Creates up to 50 store metafields in a single request. |
| Create Storefront API Token | `createStorefrontApiToken` | Creates a Storefront API token. allowed_cors_origins lists allowed CORS domains (single element). POST /v3/storefront/api-token. |
| Create Subscriber | `createSubscriber` | Create a newsletter subscriber. |
| Create Tax Properties | `createTaxProperties` | Create one or more tax properties (v3). Body is a JSON array string; each item requires code and display_name. |
| Create Tax Rates | `createTaxRates` | Create one or more tax rates (v3). Each rate must be associated with a tax_zone_id. Body is a JSON array string. |
| Create Tax Zones | `createTaxZones` | Create one or more tax zones (v3). You cannot create a default tax zone. Body is a JSON array string; each item requires name. |
| Create Tree Categories (Bulk) | `createTreeCategories` | Bulk creates categories. Body is a JSON array of category objects; each requires name, url, and tree_id or parent_id. Pass as a JSON array string in 'items'. |
| Create Variant Image | `createVariantImage` | Sets the image for a product variant from a publicly accessible image URL. Overwrites any existing variant image. |
| Create Variant Metafields (Batch) | `createVariantMetafieldsBatch` | Creates up to 50 variant metafields in a single request. |
| Create Webhook | `createWebhook` | Creates a webhook subscription. scope and destination are required. Destination must be served on port 443. POST /v3/hooks. |
| Delete a Blog Post | `deleteBlogPost` | Deletes a single blog post by ID (Content v2). Returns 204 No Content. |
| Delete a Currency | `deleteCurrency` | Deletes a single currency by ID (v2). Returns 204. |
| Delete a Customer (v2) | `deleteCustomerV2` | Deletes a single customer by ID (v2, deprecated). Returns 204 No Content. |
| Delete a Customer Address (v2) | `deleteCustomerV2Address` | Deletes a single customer address by ID (v2, deprecated). Returns 204 No Content. |
| Delete a Page | `deletePage` | Deletes a single content page by ID (Pages v3). Returns 204 No Content. |
| Delete a Page (v2) | `deletePageV2` | Deletes a single page by ID (Content v2, deprecated). Returns 204 No Content. |
| Delete a Placement | `deletePlacement` | Deletes a widget Placement by uuid. Returns 204 No Content. |
| Delete a Price List | `deletePriceList` | Deletes a single Price List by ID. Associated price records are also removed. Returns 204. |
| Delete a Price Record by Currency Code | `deletePriceListRecord` | Deletes a single Price List Record for a variant in a given currency. Returns 204. |
| Delete a Redirect (v2) | `deleteRedirectV2` | Deletes a single redirect URL by ID (Content v2, deprecated). Returns 204 No Content. |
| Delete a Script | `deleteScript` | Deletes a Script by uuid. Returns 204 No Content. |
| Delete a Site | `deleteSite` | Delete a site by site ID. Returns HTTP 200 with empty data and meta objects ({"data":{},"meta":{}}). DELETE /v3/sites/{site_id}. |
| Delete a Site Route | `deleteSiteRoute` | Delete a site route. Returns HTTP 200 with empty data and meta objects ({"data":{},"meta":{}}). DELETE /v3/sites/{site_id}/routes/{route_id}. |
| Delete a Theme | `deleteStoreTheme` | Deletes a store Theme by uuid (deletes the theme and all variations). Returns 204 No Content. |
| Delete a Webhook | `deleteWebhook` | Deletes a webhook. Returns the deleted webhook with a 200 OK. DELETE /v3/hooks/{webhook_id}. |
| Delete a Widget | `deleteWidget` | Deletes a Widget by uuid. Returns 204 No Content. |
| Delete a Widget Template | `deleteWidgetTemplate` | Deletes a Widget Template by uuid. Returns 204 No Content. |
| Delete a Wishlist | `deleteWishlist` | Deletes a wishlist by ID. Returns 204. |
| Delete Abandoned Cart Email Template | `deleteAbandonedCartEmail` | Delete an abandoned cart email template by ID. Returns 204 No Content. |
| Delete All Banners | `deleteAllBanners` | Deletes all Banners. Returns 204 No Content. |
| Delete All Coupons | `deleteAllCoupons` | Deletes all Coupons, or a comma-separated batch via idIn filter (id:in). Returns 204 No Content. |
| Delete All Currencies | `deleteCurrencies` | Deletes all non-default store currencies (v2). Returns 204. |
| Delete All Customer Groups (v2) | `deleteAllCustomerGroups` | Deletes all customer groups. All existing customers are unassigned from a group when it is deleted. Returns 204 No Content. |
| Delete All Gift Certificates | `deleteAllGiftCertificates` | Deletes all Gift Certificates. Returns 204 No Content. |
| Delete All Order Shipments | `deleteAllOrderShipments` | Deletes all shipments associated with an order (v2). Returns 204 empty. |
| Delete All Orders | `deleteAllOrders` | Archive/delete multiple orders matching filter parameters (DELETE /v2/orders). DESTRUCTIVE delete-all. BLOCKED on this shared live store: not exercisable — round-1 execution 502'd ('Unexpected end of JSON input') and running it would archive real orders. Filters (min_id/max_id/status_id/customer_id/email) are appended as query params. On success the provider returns 204 No Content with an empty body. |
| Delete All Price Lists | `deletePriceLists` | Deletes Price Lists matching the optional id/name filters. All associated price records are also removed. Returns 204. |
| Delete All Redirects (v2) | `deleteAllRedirectsV2` | Deletes all redirect URLs in a store (Content v2, deprecated). Returns 204 No Content. |
| Delete Banner | `deleteBanner` | Deletes a single Banner by id. Returns 204 No Content. |
| Delete Blog Posts | `deleteBlogPosts` | Deletes a page of blog posts (Content v2). Returns 204 No Content. |
| Delete Brand | `deleteBrand` | Delete a brand by ID. |
| Delete Brand Image | `deleteBrandImage` | Deletes the image of a brand. Returns 204 No Content. |
| Delete Brand Metafield | `deleteBrandMetafield` | Deletes a brand metafield by ID. Returns 204 No Content. |
| Delete Brand Metafields (Batch) | `deleteBrandMetafieldsBatch` | Deletes up to 50 brand metafields in a single request, identified by metafield id. The response reports per-item success in meta.success / meta.failed and lists any per-item failures in errors. |
| Delete Brands (Bulk) | `deleteBrands` | Bulk delete brands. A filter is required; name is required. Returns 204 No Content. |
| Delete Bulk Pricing Rule | `deleteBulkPricingRule` | Deletes a bulk pricing rule by ID for a product. Returns 204 No Content. |
| Delete Carrier Connection | `deleteCarrierConnection` | Deletes a Carrier Connection (v2). Requires carrier_id in the body. Returns 204. |
| Delete Cart | `deleteCart` | Delete a cart by ID. Returns 204. |
| Delete Cart Line Item | `deleteCartLineItem` | Remove an item from a cart. If it is the last item, the cart itself is deleted. |
| Delete Cart Metafield | `deleteCartMetafield` | Deletes a cart metafield by cart ID and metafield ID. Returns 204 No Content. |
| Delete Cart Metafields (Batch) | `deleteCartMetafieldsBatch` | Deletes up to 50 cart metafields in a single request, identified by metafield id. The response reports per-item success in meta.success / meta.failed and lists any per-item failures in errors. |
| Delete Categories (Bulk) | `deleteCategories` | Bulk delete categories. At least one filter parameter is required (e.g. id:in). Deleting a category that contains products returns 422. Returns 204 No Content. |
| Delete Category | `deleteCategory` | Delete a category by ID. Categories with assigned products will reassign them to the parent. |
| Delete Category Image | `deleteCategoryImage` | Deletes the image of a category. Returns 204 No Content. |
| Delete Category Metafield | `deleteCategoryMetafield` | Deletes a category metafield by ID. Returns 204 No Content. |
| Delete Category Metafields (Batch) | `deleteCategoryMetafieldsBatch` | Deletes up to 50 category metafields in a single request, identified by metafield id. The response reports per-item success in meta.success / meta.failed and lists any per-item failures in errors. |
| Delete Category Trees | `deleteCategoryTrees` | Deletes category trees. A filter (id:in) must be supplied. Returns 204 No Content. |
| Delete Channel Currency Assignments | `deleteSingleChannelCurrencyAssignments` | Deletes currency assignments for a specific channel. The channel then inherits store currency settings. |
| Delete Channel Menus | `deleteChannelMenus` | Deletes the control panel side navigation menus for a channel. |
| Delete Channel Metafield | `deleteChannelMetafield` | Deletes a single channel metafield. Returns 204 No Content. |
| Delete Channel Metafields (Batch) | `deleteChannelMetafieldsBatch` | Deletes up to 50 channel metafields in a single request, identified by metafield id. The response reports per-item success in meta.success / meta.failed and lists any per-item failures in errors. |
| Delete Channel Site | `deleteChannelSite` | Deletes the channel's site. |
| Delete Channel Site Checkout URL | `deleteChannelSiteCheckoutUrl` | Deletes a site's checkout URL. After deletion a shared checkout URL is used. Returns empty data and meta objects. |
| Delete Checkout Consignment | `deleteCheckoutConsignment` | Remove a consignment from a checkout. |
| Delete Checkout Coupon | `deleteCheckoutCoupon` | Remove a coupon from a checkout. |
| Delete Complex Rule | `deleteComplexRule` | Deletes a product complex rule by ID. Returns 204 No Content. |
| Delete Coupon | `deleteCoupon` | Deletes a single Coupon by id. Returns 204 No Content. |
| Delete Custom Template Associations | `deleteCustomTemplateAssociations` | Delete custom template associations. At least one query parameter must be used. Returns 204 No Content. |
| Delete Customer Addresses | `deleteCustomerAddresses` | Bulk delete customer addresses matching id:in. |
| Delete Customer Addresses (v2) | `deleteAllCustomerV2Addresses` | Deletes all addresses for a customer (v2, deprecated). Returns 204 No Content. |
| Delete Customer Attribute Values | `deleteCustomerAttributeValues` | Delete attribute values by id:in. |
| Delete Customer Attributes | `deleteCustomerAttributes` | Delete attribute definitions by id:in. |
| Delete Customer Group | `deleteCustomerGroup` | Delete a customer group (V2). |
| Delete Customer Metafield | `deleteCustomerMetafield` | Deletes a metafield from a customer. Returns 204 No Content on success. |
| Delete Customer Metafields (Batch) | `deleteCustomerMetafieldsBatch` | Deletes up to 50 customer metafields in a single request, identified by metafield id. The response reports per-item success in meta.success / meta.failed and lists any per-item failures in errors. |
| Delete Customers | `deleteCustomers` | Bulk delete customers matching the id:in filter. Returns 204. |
| Delete Customers (v2) | `deleteAllCustomersV2` | Deletes customers (v2, deprecated). By default deletes all customers; up to 100 per batch. Returns 204 No Content. |
| Delete Customs Information | `deleteCustomsInformation` | Deletes customs information objects for one or more products (v3). Requires product_id:in. Returns 204. |
| Delete Email Template Override | `deleteEmailTemplateOverride` | Removes a channel-specific email template override, restoring the global default. Requires channel_id. |
| Delete Gift Certificate | `deleteGiftCertificate` | Deletes a single Gift Certificate by id. Returns 204 No Content. |
| Delete Inventory Locations | `deleteInventoryLocations` | Delete one or more inventory locations by id. Requires the location_id:in query filter (comma-separated location IDs). Returns 204 No Content. |
| Delete Location Metafield | `deleteLocationMetafield` | Delete a single metafield by id from a specific inventory location. Returns 204 No Content. |
| Delete Location Metafields (Batch) | `deleteLocationMetafieldsBatch` | Deletes up to 50 inventory location metafields in a single request, identified by metafield id. The response reports per-item success in meta.success / meta.failed and lists any per-item failures in errors. |
| Delete Modifier Value | `deleteModifierValue` | Deletes a value of a product modifier. Returns 204 No Content. |
| Delete Order | `deleteOrder` | Deletes (archives) a single order. Returns 204 No Content on success. |
| Delete Order Metafield | `deleteOrderMetafield` | Deletes an order Metafield (v3). Returns 204 empty. |
| Delete Order Metafields (Batch) | `deleteOrderMetafieldsBatch` | Deletes up to 50 order metafields in a single request, identified by metafield id. The response reports per-item success in meta.success / meta.failed and lists any per-item failures in errors. |
| Delete Order Shipment | `deleteOrderShipment` | Delete a shipment. |
| Delete Pages | `deletePages` | Deletes one or more content pages (Pages v3 bulk) by id:in. Returns 204 No Content. |
| Delete Price List Assignments | `deletePriceListAssignments` | Deletes Price List Assignments matching the supplied filters. At least one filter is required. Returns 204. |
| Delete Price List Records | `deletePriceListRecords` | Deletes Price List Records for a Price List, optionally filtered by variant_id:in. Returns 204. |
| Delete Product | `deleteProduct` | Permanently delete a product by ID. |
| Delete Product Custom Field | `deleteProductCustomField` | Delete a custom field from a product. |
| Delete Product Image | `deleteProductImage` | Delete a product image. |
| Delete Product Metafield | `deleteProductMetafield` | Deletes a product metafield by ID. Returns 204 No Content. |
| Delete Product Metafields (Batch) | `deleteProductMetafieldsBatch` | Deletes up to 50 product metafields in a single request, identified by metafield id. The response reports per-item success in meta.success / meta.failed and lists any per-item failures in errors. |
| Delete Product Modifier | `deleteProductModifier` | Delete a product modifier. |
| Delete Product Review | `deleteProductReview` | Deletes a product review by ID. Returns 204 No Content. |
| Delete Product Tax Properties | `deleteProductTaxProperties` | Delete tax properties associated with one or more products (v3) by product_id:in (required). Returns 204. |
| Delete Product Variant | `deleteProductVariant` | Delete a variant from a product. |
| Delete Product Variant Metafield | `deleteVariantMetafield` | Deletes a metafield on a product variant. Returns 204 No Content. |
| Delete Product Variant Option | `deleteProductOption` | Deletes a variant option from a product. Returns 204 No Content. |
| Delete Product Variant Option Value | `deleteOptionValue` | Deletes a value of a product variant option. Returns 204 No Content. |
| Delete Product Video | `deleteProductVideo` | Deletes a product video by ID. Returns 204 No Content. |
| Delete Products (bulk) | `deleteProducts` | Bulk delete products matching the supplied filter parameters (e.g. by id:in, sku, etc.). Returns 204. |
| Delete Products Category Assignments | `deleteProductsCategoryAssignments` | Deletes product-to-category assignments. At least one filter (productIdIn or categoryIdIn, comma-separated id lists) MUST be supplied. Returns 204 on success. |
| Delete Products Channel Assignments | `deleteProductsChannelAssignments` | Deletes product-to-channel assignments. At least one filter (productIdIn or channelIdIn, comma-separated id lists) MUST be supplied. Returns 204 on success. |
| Delete Promotion | `deletePromotion` | Deletes a single promotion by ID. Returns 204 No Content. |
| Delete Promotion Code | `deletePromotionCode` | Deletes a single coupon code by its code_id on the given promotion. Returns 204 No Content. |
| Delete Promotion Codes | `deletePromotionCodes` | Deletes coupon codes from a promotion, optionally filtered by code IDs (id:in). Returns 204 No Content. |
| Delete Promotions | `deletePromotions` | Deletes multiple promotions matching the required id:in filter. Returns 204 No Content. The id:in filter MUST be supplied (explicit query param). |
| Delete Redirects | `deleteRedirects` | Deletes redirects by id:in (Redirects v3), optionally scoped to a site. Returns 204 No Content. |
| Delete Shipping Method | `deleteShippingMethod` | Deletes a Shipping Method in a zone (v2). Returns 204. |
| Delete Shipping Zone | `deleteShippingZone` | Deletes a Shipping Zone by id (v2). Returns 204. |
| Delete Store Metafields (Batch) | `deleteStoreMetafieldsBatch` | Deletes up to 50 store metafields in a single request, identified by metafield id. The response reports per-item success in meta.success / meta.failed and lists any per-item failures in errors. |
| Delete Subscriber | `deleteSubscriber` | Delete a subscriber by ID. |
| Delete Subscribers (bulk) | `deleteSubscribers` | Bulk delete subscribers matching filter (email, first_name, last_name, source, order_id). |
| Delete Tax Properties | `deleteTaxProperties` | Delete one or more tax properties (v3) by id:in. A tax property must have zero usages in product tax properties before deletion. Returns 204. |
| Delete Tax Rates | `deleteTaxRates` | Delete one or more tax rates (v3) by id:in (required). Returns 204. |
| Delete Tax Zones | `deleteTaxZones` | Delete one or more tax zones (v3) by id:in (required). Deleting a tax zone removes all associated tax rates. Returns 204. |
| Delete Tree Categories (Bulk) | `deleteTreeCategories` | Bulk deletes categories across trees. Provide at least one filter (category_id:in, category_uuid:in, tree_id:in, parent_id:in). Returns 204 with a meta summary. |
| Delete Variant Metafields (Batch) | `deleteVariantMetafieldsBatch` | Deletes up to 50 product variant metafields in a single request, identified by metafield id. The response reports per-item success in meta.success / meta.failed and lists any per-item failures in errors. |
| Delete Wishlist Item | `deleteWishlistItem` | Removes a single item from a wishlist by item_id. Returns 204 No Content. |
| Download a Theme | `downloadTheme` | Downloads a store Theme by uuid. 'which' selects which revision: original, last_activated, or last_created. Returns a job_id for the background download job. |
| Download Redirect Export | `getRedirectExportDownload` | Downloads the CSV file containing the results of a redirect export job (Redirects v3 Import-Export). |
| Generate Promotion Codes Batch | `generatePromotionCodesBatch` | Generates a batch of coupon codes for a bulk-coupon promotion. POST /v3/promotions/{promotion_id}/codegen. batch_size is required and capped at 250; code_length must be 6-16. Verified working against a live store 2026-09-01. |
| Get a Blog Post | `getBlogPost` | Returns a single blog post by ID (Content v2). |
| Get a Count of Customer Addresses (v2) | `getCustomerV2AddressesCount` | Returns a count of addresses for a customer (v2, deprecated). |
| Get a Count of Customer Groups (v2) | `getCustomerGroupsCount` | Returns a count of all customer groups. |
| Get a Count of Customers (v2) | `getCustomersV2Count` | Returns a count of all customers (v2, deprecated). |
| Get a Currency | `getCurrency` | Returns a single currency by ID (v2). |
| Get a Customer (v2) | `getCustomerV2` | Returns a single customer by ID (v2, deprecated). |
| Get a Customer Address (v2) | `getCustomerV2Address` | Returns a single customer address by ID (v2, deprecated). |
| Get a Page | `getPage` | Returns one content page by ID (Pages v3). |
| Get a Page (v2) | `getPageV2` | Returns a single page by ID (Content v2, deprecated). |
| Get a Placement | `getPlacement` | Returns a single widget Placement by its uuid. |
| Get a Price List | `getPriceList` | Returns a single Price List by ID. |
| Get a Price Record by Currency Code | `getPriceListRecord` | Returns a single Price List Record for a variant in a given currency. |
| Get a Redirect (v2) | `getRedirectV2` | Returns a single redirect URL by ID (Content v2, deprecated). |
| Get a Script | `getScript` | Returns a single Script by uuid. |
| Get a Site | `getSite` | Get a site by site ID. GET /v3/sites/{site_id}. |
| Get a Site Route | `getSiteRoute` | Get a single site route. GET /v3/sites/{site_id}/routes/{route_id}. |
| Get a Site's Certificate | `getSiteCertificate` | Obtain information about a site's SSL/TLS certificate. GET /v3/sites/{site_id}/certificate. |
| Get a Theme | `getStoreTheme` | Returns a single store Theme by uuid (theme variation not included at this endpoint). |
| Get a Theme Job | `getThemeJob` | Returns a theme Job by job_id. When complete, the result provides a link/theme_id. The download link is active for 60 seconds. |
| Get a Webhook | `getWebhook` | Return a single webhook by ID. GET /v3/hooks/{webhook_id}. |
| Get a Widget | `getWidget` | Returns a single Widget by uuid. |
| Get a Widget Template | `getWidgetTemplate` | Returns a single Widget Template by uuid. Optional version_uuid query param fetches a specific version. |
| Get a Wishlist | `getWishlist` | Returns a single wishlist by ID. |
| Get Abandoned Cart by Token | `getAbandonedCartByToken` | Returns the cart_id corresponding to the abandoned cart token passed in (from abandoned cart email links). |
| Get Abandoned Cart Email Settings | `getAbandonedCartEmailSettings` | Read abandoned cart email template settings for a channel (use_global inheritance flag). |
| Get Abandoned Cart Email Template | `getAbandonedCartEmail` | Get a single abandoned cart email template by ID. |
| Get Accepted Payment Methods (v3) | `getAcceptedPaymentMethods` | Returns a list of accepted payment methods based on the order_id or checkout_id, including supported and stored instruments per gateway. One of order_id or checkout_id is required. |
| Get All Blog Posts | `listBlogPosts` | Returns all blog posts (Content v2). Response is a JSON array of post objects. Default sort by published_date, newest first. |
| Get All Blog Tags | `listBlogTags` | Returns a list of blog tags (Content v2). Response is a JSON array of tag objects. |
| Get All Currencies | `listCurrencies` | Returns a list of all store currencies (v2, raw array response). |
| Get All Order Taxes | `listOrderTaxes` | Gets all order taxes for an order (v2). Returns a JSON array of tax objects. Pass details=true for extra detail. |
| Get All Pages (v2) | `listPagesV2` | Returns a list of pages (Content v2, deprecated). Response is a JSON array of page objects. |
| Get All Payment Methods (v2) | `getPaymentMethods` | Deprecated v2 endpoint. Gets the list of enabled payment methods, sorted alphabetically. Returns a raw array of payment method objects (code, name, test_mode). |
| Get All Placements | `getPlacements` | Returns a list of widget Placements. Supports filtering by template_file, widget_uuid, widget_template_uuid, channel_id, site_id, and pagination. |
| Get All Redirects (v2) | `listRedirectsV2` | Returns a list of all redirect URLs (Content v2, deprecated). Response is a JSON array. |
| Get All Scripts | `getScripts` | Returns a list of Scripts created by the API key/password used originally. Supports pagination, sort, direction, and channel_id filtering. |
| Get All Themes | `getStoreThemes` | Returns a list of store Themes including variations, is_active and is_private flags. |
| Get All Tree Categories | `getAllTreeCategories` | Returns a list of categories across trees. Supports many filters (category_id:in, tree_id:in, parent_id:in, name, etc.) and pagination. Returns a {data,meta} envelope. |
| Get All Widget Templates | `getWidgetTemplates` | Returns a list of Widget Templates. Supports pagination and filtering by widget_template_kind and channel_id. |
| Get All Widgets | `getWidgets` | Returns a list of Widgets. Supports pagination and filtering by widget_template_kind, widget_template_uuid, name, channel_id, site_id. |
| Get an Email Template | `getEmailTemplate` | Get a single global email template or a channel-specific override by template name. |
| Get Analytics Provider | `getAnalyticsProvider` | Returns a single web analytics provider by ID for the default (or specified) channel. |
| Get Available Search Filters | `getAvailableSearchFilters` | Returns the list of filters available to power Product Filtering. Optionally narrow by channel_id and category_id. |
| Get Banner | `getBanner` | Returns a single Banner by id. |
| Get Brand | `getBrand` | Get a brand by ID. |
| Get Brand Metafield | `getBrandMetafield` | Returns a single brand metafield by ID. Optional include_fields/exclude_fields. |
| Get Bulk Pricing Rule | `getBulkPricingRule` | Returns a single bulk pricing rule by ID for a product. Returns {data,meta}. |
| Get Cart | `getCart` | Retrieve a cart by ID. Use include to expand line items and redirect URLs. |
| Get Cart Metafield | `getCartMetafield` | Gets a single cart metafield by cart ID and metafield ID. |
| Get Catalog Settings | `getCatalogSettings` | Returns catalog settings (review auto-approval, product comparisons). Optionally scope with channel_id. |
| Get Catalog Summary | `getCatalogSummary` | Returns a lightweight inventory summary of the catalog (counts, values, price extremes, primary category). Returns {data,meta}. |
| Get Category | `getCategory` | Get a single category by ID. |
| Get Category Metafield | `getCategoryMetafield` | Returns a single category metafield by ID. Optional include_fields/exclude_fields. |
| Get Category Product Sort Order | `getCategoryProductSortOrder` | Returns the list of products and their sort_order for a specific category, in ascending order. Returns a raw array (no envelope). |
| Get Category Tree | `getCategoryTree` | Retrieve all categories as a hierarchical tree. |
| Get Category Tree By Tree ID | `getCategoryTreeByTreeId` | Returns the category tree (nested CategoryNode structure) for a specific tree. Optional depth limits tree depth. Returns a {data,meta} envelope. |
| Get Category Trees | `getCategoryTrees` | Returns a list of category trees. Optional filters id:in and channel_id:in. Returns a {data,meta} envelope. |
| Get Channel | `getChannel` | Returns a single Channel by ID. Channel ID 1 returns the default storefront. |
| Get Channel Abandoned Cart Settings | `getChannelAbandonedCartSettings` | Returns the per-channel overrides for the abandoned cart settings of a store. |
| Get Channel Active Theme | `getChannelActiveTheme` | Returns details of the theme active on the specified channel. |
| Get Channel Cart Settings | `getChannelCartSettings` | Returns the per-channel overrides for the cart settings of a store. |
| Get Channel Currency Assignments | `getSingleChannelCurrencyAssignments` | Returns currency assignments for a specific channel. |
| Get Channel Listing | `getChannelListing` | Returns a single Channel Listing for a specific channel. |
| Get Channel Menus | `getChannelMenus` | Returns the list of control panel side navigation menus for a channel. |
| Get Channel Metafield | `getChannelMetafield` | Returns a single channel metafield. |
| Get Channel Order Settings | `getChannelOrderSettings` | Returns order settings for a specific channel (v3). |
| Get Channel Site | `getChannelSite` | Returns site data for the specified channel (alias of GET /sites?channel_id=channel_id). |
| Get Checkout | `getCheckout` | Get a checkout by ID. include can expand consignments, payments, etc. |
| Get Checkout Settings | `getCheckoutSettings` | Get the store's checkout settings (custom checkout/order confirmation script URLs). |
| Get Complex Rule | `getComplexRule` | Returns a single product complex rule by ID. Returns {data,meta}. |
| Get Consignment Shipping Quotes | `getConsignmentShippingQuotes` | Get all shipping quotes persisted on an order for a shipping consignment (v2). Returns 204 when no quote exists. |
| Get Contextual Search Filters | `getSearchFilterContexts` | Returns contextual filters enabled for a particular channel or category. |
| Get Count of Banners | `getBannersCount` | Returns a count of Banners in the store. |
| Get Count of Blog Posts | `getBlogPostsCount` | Returns a count of all blog posts (Content v2). |
| Get Count of Coupons | `getCouponsCount` | Returns a count of all Coupons in the store. |
| Get Count of Order Shipments | `getOrderShipmentsCount` | Gets a count of shipments made for a single order (v2). |
| Get Count of Redirects (v2) | `getRedirectsV2Count` | Gets a count of redirect URLs in a store (Content v2, deprecated). |
| Get Countries Count | `getCountriesCount` | Returns a count of all countries (v2). |
| Get Country | `getCountry` | Returns a single Country by id (v2). |
| Get Country State | `getCountryState` | Returns a single state belonging to a country (v2). |
| Get Country States Count | `getCountryStatesCount` | Returns a count of a country's states (v2). |
| Get Custom Template Associations | `listCustomTemplateAssociations` | Get a collection of the store's custom template associations across all storefronts. |
| Get Custom Templates | `getThemeCustomTemplates` | Enumerates available custom templates in the theme files of a specific theme version, grouped by entity type (product, category, brand, page). |
| Get Customer Consent | `getCustomerConsent` | Gets the status of a customer's consent to allow data collection by cookies and scripts while shopping on a storefront. |
| Get Customer Group | `getCustomerGroup` | Get a single customer group by ID (V2). |
| Get Customer Metafield | `getCustomerMetafield` | Returns a single metafield attached to a customer. |
| Get Customer Settings | `getCustomerSettings` | Returns the global-level customer settings (privacy settings and customer group settings). |
| Get Customer Settings per Channel | `getCustomerChannelSettings` | Returns the customer settings for a specific channel. null indicates no override per channel and values are inherited from the global level. |
| Get Customs Information | `listCustomsInformation` | Get customs information for products (v3). Optionally filter by product_id:in (comma-separated list). |
| Get Default Abandoned Cart Email Template | `getDefaultAbandonedCartEmail` | Return the default abandoned cart email template (subject, body, translations). |
| Get Email Statuses | `getEmailStatuses` | Returns transactional email (status) settings, globally or per channel. |
| Get Email Templates | `listEmailTemplates` | Get a list of email templates (Marketing). Requires opting into the new email management experience. |
| Get Enabled Search Filters | `getSearchFilters` | Returns the list of enabled default Product Filtering filters used when no contextual overrides exist. |
| Get Gift Certificate | `getGiftCertificate` | Returns a single Gift Certificate by id. |
| Get Global Abandoned Cart Settings | `getAbandonedCartSettings` | Returns the global abandoned cart settings of a store. |
| Get Global Cart Settings | `getCartSettings` | Returns the global cart settings of a store (allow_purchasing flag). |
| Get Global Order Settings | `getGlobalOrderSettings` | Returns global order settings (v3). |
| Get Inventory Notifications Settings | `getInventoryNotifications` | Returns inventory notification settings (low/out-of-stock notification addresses), globally or per channel. |
| Get Inventory Settings | `getInventorySettings` | Returns inventory settings (out-of-stock behavior, stock display, etc.), globally or per channel. |
| Get Location Metafield | `getLocationMetafield` | Get a single metafield by id from a specific inventory location. |
| Get Logo Settings | `getLogoSettings` | Returns store logo settings (type, logo text, image/favicon URLs), globally or per channel. |
| Get Modifier Value | `getModifierValue` | Returns a single value of a product modifier by value ID. |
| Get Order | `getOrder` | Retrieve a single order by ID (V2). |
| Get Order Count | `getOrdersCount` | Return the total order count grouped by status. |
| Get Order Metafield | `getOrderMetafield` | Gets a single order Metafield by metafield ID (v3). |
| Get Order Payment Access Token | `getOrderPaymentAccessToken` | Create/get a one-time-use Payment Access Token (PAT) for an order. The PAT is a single-use JWT tied to the order, required to call the Payments Processing API (/payments). Created via the v3 Payments API on api.bigcommerce.com. |
| Get Order Product | `getOrderProduct` | Gets a single product line item associated with an order (v2). |
| Get Order Shipment | `getOrderShipment` | Get a single shipment by ID. |
| Get Order Shipping Address | `getOrderShippingAddress` | Get a single shipping address on an order. |
| Get Order Shipping Address Quotes | `getOrderShippingAddressQuotes` | Gets all shipping quotes persisted on an order for a shipping address (v2). Returns 204 when no quote exists. |
| Get Order Status | `getOrderStatus` | Get a single order status definition. |
| Get Price Records by Variant | `getPriceListRecordsByVariant` | Returns Price List Records for a given variant within a Price List, including currency records. |
| Get Product | `getProduct` | Retrieve a single product by its ID. Use `include` to fetch sub-resources (variants, images, custom_fields, bulk_pricing_rules, modifiers, options, videos). |
| Get Product By SKU | `getProductBySku` | Look up a catalog product by its SKU. BigCommerce V3 has no /products/sku/{sku} path; this filters the catalog products list with ?sku=. Returns a products list ({data:[...],meta:{pagination}}) — SKUs are unique per product, so the caller takes data[0]. Supports optional include and include_fields. |
| Get Product Custom Field | `getProductCustomField` | Returns a single product custom field by ID. Returns {data:{id,name,value},meta}. |
| Get Product Image | `getProductImage` | Get a single product image. |
| Get Product Metafield | `getProductMetafield` | Returns a single product metafield by ID. Returns {data,meta}. |
| Get Product Modifier | `getProductModifier` | Returns a single product modifier by modifier ID. |
| Get Product Review | `getProductReview` | Returns a single product review by ID. Returns {data,meta}. |
| Get Product Tax Properties | `listProductTaxProperties` | Retrieve the tax properties associated with one or more products (v3). Filter by product_id:in (required). |
| Get Product Variant | `getProductVariant` | Get a single variant for a product. |
| Get Product Variant Metafield | `getVariantMetafield` | Returns a single metafield on a product variant by metafield ID. |
| Get Product Variant Option | `getProductOption` | Returns a single variant option for a product by option ID. |
| Get Product Variant Option Value | `getOptionValue` | Returns a single value of a product variant option by value ID. |
| Get Product Video | `getProductVideo` | Returns a single product video by ID. Returns {data,meta}. |
| Get Promotion | `getPromotion` | Returns a single promotion by its ID. v3 {data} envelope. |
| Get Promotion Code | `getPromotionCode` | Returns a single coupon code by its code_id on the given promotion. v3 {data} envelope. |
| Get Redirect Import-Export Jobs | `listRedirectImexJobs` | Returns a collection of the store's redirect import-export jobs (Redirects v3 Import-Export). |
| Get Redirects | `listRedirects` | Returns a collection of the store's 301 redirects across all sites (Redirects v3). |
| Get Refund By ID | `getRefundById` | Returns a single refund by refund ID (v3). |
| Get Robots.txt Settings | `getRobotsTxtSettings` | Returns Robots.txt settings (robots_txt_ssl content), globally or per channel. |
| Get Shipping Method | `getShippingMethod` | Returns a single Shipping Method in a zone (v2). |
| Get Shipping Methods | `listShippingMethods` | Returns the shipping methods for a zone (v2). Real-time carrier connections are also returned. Response is a raw JSON array. |
| Get Shipping Zone | `getShippingZone` | Returns a single Shipping Zone by id (v2). |
| Get States Count | `getStatesCount` | Returns a count of all states (v2). |
| Get Store Information | `getStoreInformation` | Returns metadata about the store (domain, plan, currency, timezone, features, etc.). GET /v2/store. |
| Get Store Locale | `getStoreLocale` | Returns global (or channel) locale settings: default shopper language, selection method, store country. |
| Get Store Profile | `getStoreProfile` | Returns store profile settings (name, address, email, phone), globally or per channel. |
| Get Store Time | `getStoreTime` | Returns the system timestamp at the time of the request. Useful for validating API auth and testing connections. GET /v2/time. |
| Get Storefront Category Settings | `getStorefrontCategorySettings` | Returns storefront category settings (tree depth, default sort, listing mode), globally or per channel. |
| Get Storefront Product Settings | `getStorefrontProductSettings` | Returns storefront product settings (price/SKU/weight/brand visibility etc.), globally or per channel. |
| Get Storefront Search Settings | `getStorefrontSearchSettings` | Returns storefront search settings (sort, filtering enabled, search suggest), globally or per channel. |
| Get Storefront Security Settings | `getStorefrontSecuritySettings` | Returns storefront security settings (CSP, HSTS, HTTPS, X-Frame-Options), globally or per channel. |
| Get Storefront SEO Settings | `getStorefrontSeoSettings` | Returns storefront SEO settings (meta description/keywords, page title, www redirect), globally or per channel. |
| Get Storefront Status | `getStorefrontStatus` | Returns storefront status settings (maintenance/prelaunch messages, prelaunch password), globally or per channel. |
| Get Subscriber | `getSubscriber` | Get a subscriber by ID. |
| Get Tax Class | `getTaxClass` | Returns a single Tax Class by its id (v2, read-only). |
| Get Tax Properties | `listTaxProperties` | Retrieve all tax properties defined in this store (v3). Optionally filter by a comma-separated list of tax property IDs. |
| Get Tax Rates | `listTaxRates` | Retrieve a list of tax rates (v3). Optionally filter by tax rate id:in and/or tax_zone_id:in. |
| Get Tax Settings | `getTaxSettings` | Retrieves global-level tax settings (v3). |
| Get Tax Zones | `listTaxZones` | Retrieve tax zones (v3). Optionally filter by a comma-separated list of zone IDs via id:in; otherwise returns all tax zones. |
| Get Theme Configurations | `getThemeConfigurations` | Returns a list of a theme's configurations. site_id:in is required; at least one filter must be provided. Supports uuid:in, channel_id:in, variation_uuid, pagination. |
| Get Theme Regions | `getContentRegions` | Returns a list of unique Theme Regions in a file. template_file is required. |
| Get Units of Measurement Settings | `getUnitsOfMeasurement` | Returns units-of-measurement settings (weight/length units, tokens, decimal places), globally or per channel. |
| Get Webhooks Admin Info | `getWebhooksAdmin` | List all notification emails, webhooks, and denylisted domains associated with the API account. GET /v3/hooks/admin. |
| List Abandoned Cart Emails | `listAbandonedCartEmails` | Get all abandoned cart email templates for a store. Optionally scope to a channel. |
| List All Brand Metafields | `listAllBrandMetafields` | Lists brand metafields across the whole store in one call, rather than one brand at a time. Supports filtering by key, namespace and created/modified dates. |
| List All Cart Metafields | `listAllCartMetafields` | Lists cart metafields across the whole store in one call, rather than one cart at a time. Supports filtering by key, namespace and created/modified dates. |
| List All Category Metafields | `listAllCategoryMetafields` | Lists category metafields across the whole store in one call, rather than one category at a time. Supports filtering by key, namespace and created/modified dates. |
| List All Channel Metafields | `listAllChannelMetafields` | Lists channel metafields across the whole store in one call, rather than one channel at a time. Supports filtering by key, namespace and created/modified dates. |
| List All Currency Assignments | `listAllCurrencyAssignments` | Returns a list of currency assignments for all channels. |
| List All Customer Metafields | `listAllCustomerMetafields` | Lists customer metafields across the whole store in one call, rather than one customer at a time. Supports filtering by key, namespace and created/modified dates. |
| List All Location Metafields | `listAllLocationMetafields` | Lists location metafields across the whole store in one call, rather than one location at a time. Supports filtering by key, namespace and created/modified dates. |
| List All Order Metafields | `listAllOrderMetafields` | Lists order metafields across the whole store in one call, rather than one order at a time. Supports filtering by key, namespace and created/modified dates. |
| List All Product Metafields | `listAllProductMetafields` | Lists product metafields across the whole store in one call, rather than one product at a time. Supports filtering by key, namespace and created/modified dates. |
| List All Refunds | `listAllRefunds` | Returns a list of all refunds ordered by refund ID ascending (v3). Supports filtering by order_id:in, id:in, created:min/max. |
| List All States | `listAllStates` | Returns a list of all states (v2). Response is a raw JSON array. |
| List All Variant Metafields | `listAllVariantMetafields` | Lists variant metafields across the whole store in one call, rather than one variant at a time. Supports filtering by key, namespace and created/modified dates. |
| List All Variants | `listAllVariants` | Returns a list of all variants across the catalog. Filter by id, sku, upc, or product_id. |
| List Analytics Providers | `listAnalyticsProviders` | Returns a list of web analytics providers configured for the store. Optionally scope to a channel with channel_id. |
| List Banners | `listBanners` | Returns a list of Banners. Default sorting is by banner id, from lowest to highest. Supports optional filters min_id, max_id, page, limit. Response is a raw JSON array. |
| List Brand Metafields | `listBrandMetafields` | Returns a list of metafields on a brand. Supports filtering by key, namespace, id filters, and pagination. Returns a {data,meta} envelope. |
| List Brands | `listBrands` | List brands in the catalog. |
| List Bulk Pricing Rules | `listBulkPricingRules` | Returns a list of bulk pricing rules for a product. Returns {data:[...],meta}. |
| List Cart Metafields | `listCartMetafields` | Get all metafields for a cart. Supports filtering by key, namespace, pagination, and sort direction. |
| List Categories | `listCategories` | List categories. Supports filtering by name, parent_id, is_visible. |
| List Category Metafields | `listCategoryMetafields` | Returns a list of metafields on a category. Supports filtering by key, namespace, id filters, and pagination. Returns a {data,meta} envelope. |
| List Channel Listings | `listChannelListings` | Returns a list of Channel Listings for a specific channel. |
| List Channel Metafields | `listChannelMetafields` | Returns a list of metafields on a channel. Optional filter parameters can be passed in. |
| List Channels | `listChannels` | Returns a list of Channels. Supports filtering by status, type, platform, dates and includes. |
| List Complex Rules | `listComplexRules` | Returns a list of product complex rules. Returns {data:[...],meta}. |
| List Countries | `listCountries` | Get a list of all countries available (v2). Optionally filter by country name, country_iso2, country_iso3. Response is a raw JSON array. |
| List Country States | `listCountryStates` | Returns a list of states belonging to a country (v2). Optionally filter by state name or state_abbreviation. Response is a raw JSON array. |
| List Coupons | `listCoupons` | Returns a list of Coupons. Default sorting is by coupon id. Supports filters id, code, name, type, min_id, max_id, page, limit, exclude_type. Response is a raw JSON array. |
| List Customer Addresses | `listCustomerAddresses` | List addresses across customers. Filter by customer_id:in to restrict. |
| List Customer Addresses (v2) | `listCustomerV2Addresses` | Returns a list of addresses belonging to a customer (v2, deprecated). Default sorting by address ID ascending. Max limit 250, default 50. Response is a raw JSON array. |
| List Customer Attribute Values | `listCustomerAttributeValues` | List attribute values across customers. Filter by customer_id:in and attribute_id:in. |
| List Customer Attributes | `listCustomerAttributes` | List custom customer attribute definitions. |
| List Customer Form Field Values | `listCustomerFormFieldValues` | List form field values across customers. Filter by customer_id. |
| List Customer Groups | `listCustomerGroups` | List customer groups (V2). |
| List Customer Metafields | `listCustomerMetafields` | Lists every metafield attached to a single customer. |
| List Customer Stored Instruments | `listCustomerStoredInstruments` | Lists all available stored instruments for a customer, including stored cards, PayPal accounts, and bank accounts. |
| List Customers | `listCustomers` | List customers (V3). Filters: id:in, company:in, customer_group_id:in, date_created, date_modified, email:in, name:in, registration_ip_address:in. Include: addresses, storecredit, attributes, formfields, shopper_profile_id, segment_ids. |
| List Customers (v2) | `listCustomersV2` | Returns a list of all customers (v2, deprecated). Default sorting is by customer ID ascending. Supports optional filter query parameters. Response is a raw JSON array. |
| List Gift Certificates | `listGiftCertificates` | Returns a list of Gift Certificates. Supports filters min_id, max_id, code, order_id, to_name, to_email, from_name, from_email, page, limit. Max limit 250, default 50. Response is a raw JSON array. |
| List Inventory Items | `listInventoryItems` | Get a paginated list of inventory items aggregated across all locations. Returns total on-hand quantities and per-location breakdowns. Supports filtering by sku and location. |
| List Inventory Locations | `listInventoryLocations` | Get a paginated list of inventory locations for the store. Supports filtering by id, code, type, enabled state, and free-text on label. |
| List Location Inventory Items | `listLocationInventoryItems` | Get a paginated list of inventory items for a single location. Returns available-to-sell and on-hand quantities plus item settings for that location. |
| List Location Metafields | `listLocationMetafields` | Get a paginated list of metafields attached to a specific inventory location. Supports filtering by namespace, key, and resource permission. |
| List Modifier Values | `listModifierValues` | Returns a list of all values for a product modifier. |
| List Order Consignments | `listOrderConsignments` | Get all consignments for an order (v2). Optionally include consignments.line_items. |
| List Order Coupons | `listOrderCoupons` | List coupons applied to an order. |
| List Order Messages | `listOrderMessages` | List internal staff messages on an order. |
| List Order Metafields | `listOrderMetafields` | Gets a list of Metafield objects for an order (v3). |
| List Order Products | `listOrderProducts` | List the products in an order (line items). V2 returns a JSON array root. |
| List Order Refunds | `listOrderRefunds` | Returns a list of refunds for a given order ordered by refund ID ascending (v3). |
| List Order Shipments | `listOrderShipments` | List shipments created for an order. |
| List Order Shipping Addresses | `listOrderShippingAddresses` | List shipping addresses associated with an order. |
| List Order Statuses | `listOrderStatuses` | List all order statuses defined for the store (e.g. Pending, Awaiting Payment, Shipped). |
| List Order Transactions | `listOrderTransactions` | List payment transactions associated with an order (V3 endpoint). |
| List Orders | `listOrders` | List orders (V2). Supports filters: status_id, customer_id, email, min_date_created, max_date_created, min_total, max_total, payment_method, channel_id, is_deleted, page, limit (max 250). NOTE: V2 list endpoints return a top-level JSON array, not an object. |
| List Pages | `listPages` | Returns one or more content pages (Pages v3). Supports filtering by channel_id, id:in, name, name:like, and pagination. |
| List Payment Methods | `listOrderPaymentMethods` | List payment methods available for an order. Use to populate checkout payment choices. |
| List Price List Assignments | `listPriceListAssignments` | Fetches Price List Assignments matching customer group, price list, and channel filters. |
| List Price List Records | `listPriceListRecords` | Returns Price List Records associated with a Price List. Supports filtering by variant/product/currency/price and pagination. |
| List Price Lists | `listPriceLists` | Returns a list of Price Lists. Supports filtering by id, name, dates, and pagination. |
| List Product Custom Fields | `listProductCustomFields` | List custom fields on a product. |
| List Product Images | `listProductImages` | List images attached to a product. |
| List Product Metafields | `listProductMetafields` | Returns a list of product metafields. Optional filters key and namespace. Returns {data:[...],meta}. |
| List Product Modifiers | `listProductModifiers` | List modifiers for a product (configurable attributes like engraving text). |
| List Product Reviews | `listProductReviews` | Returns a list of product reviews. Optional status filter (1=approved, 0=pending). Returns {data:[...],meta}. |
| List Product Variant Metafields | `listVariantMetafields` | Returns a list of metafields for a product variant. Filter by key/namespace and paginate. |
| List Product Variant Option Values | `listOptionValues` | Returns a list of all values for a product variant option. |
| List Product Variant Options | `listProductOptions` | Returns a list of variant options for a product (e.g. Color, Size). Paginate with page/limit. |
| List Product Variants | `listProductVariants` | List variants for a product. |
| List Product Videos | `listProductVideos` | Returns a list of product videos. Returns {data:[...],meta}. |
| List Products | `listProducts` | List products in the catalog. Supports filtering by name, sku, price, brand_id, category, is_visible, keyword and pagination via page/limit. Returns up to 250 per page. |
| List Products Category Assignments | `listProductsCategoryAssignments` | Returns a list of product-to-category assignments. Optional filters product_id:in and category_id:in (comma-separated id lists). Returns {data:[{product_id,category_id}],meta}. |
| List Products Channel Assignments | `listProductsChannelAssignments` | Returns a list of product-to-channel assignments. Optional filters product_id:in and channel_id:in (comma-separated id lists). Returns {data:[{product_id,channel_id}],meta}. |
| List Promotion Codes | `listPromotionCodes` | Returns a paginated list of coupon codes attached to a COUPON-type promotion. v3 {data,meta} envelope. |
| List Promotions | `listPromotions` | Returns a paginated list of promotions in the store. Supports filtering by id, name, channel, code, currency_code, redemption_type, status. v3 {data,meta} envelope. |
| List Shipping Zones | `listShippingZones` | Returns a list of all Shipping Zones (v2). Response is a raw JSON array. |
| List Site Certificates | `listSiteCertificates` | Return all SSL certificates connected to domains within a store. GET /v3/sites/certificates. |
| List Site Routes | `listSiteRoutes` | Get a site's routes. GET /v3/sites/{site_id}/routes. |
| List Sites | `listSites` | Get sites linked to headless storefront sales channels. GET /v3/sites. |
| List Store Metafields | `listStoreMetafields` | Lists every metafield attached to the store object. |
| List Subscribers | `listSubscribers` | List newsletter subscribers (V3). |
| List System Logs | `listSystemLogs` | Get store system logs, filterable by type, module, severity and date. GET /v3/store/systemlogs. |
| List Tax Classes | `listTaxClasses` | Returns a list of all Tax Classes in a store (v2, read-only). Response is a raw JSON array of tax class objects. Sorted by id ascending. |
| List Webhook Events | `listWebhookEvents` | Get a list of events that were sent but not successfully received. DEPRECATED by BigCommerce. GET /v3/hooks/events. BLOCKED: provider returns HTTP 400 'Input is invalid' (empty errors object) even on a bare GET with no params and with only limit=1 — the endpoint is deprecated and no longer serviceable on this store. Not exercisable to 200; provider account/endpoint-state block, not a config defect. |
| List Webhooks | `listWebhooks` | Returns a list of all webhooks on a store associated to the client_id used to authenticate. GET /v3/hooks. |
| List Wishlists | `listWishlists` | Returns a list of wishlists. Optional filters: customer_id, page, limit. |
| Open Redirect Export Event Stream | `getRedirectExportEvents` | Opens an event stream to receive live updates from a redirect export job (Redirects v3 Import-Export). |
| Open Redirect Import Event Stream | `getRedirectImportEvents` | Opens an event stream to receive live updates from a redirect import job (Redirects v3 Import-Export). |
| Process Order Payment | `processOrderPayment` | Process a payment against an order using a single-use Payment Access Token (PAT). Runs on the PCI-compliant payments.bigcommerce.com host. The PAT is passed as Authorization: PAT &lt;token&gt;. instrument shape depends on type (card, stored_card, stored_paypal_account, gift_certificate, store_credit, tokenized_card). |
| Render a Widget Template Preview | `previewWidgetTemplate` | Renders a widget template with the provided widget_configuration data and returns the widget HTML. |
| Revoke Storefront API Token | `revokeStorefrontApiToken` | Revoke access for a Storefront API token. Pass the JWT to revoke via the Sf-Api-Token header. DELETE /v3/storefront/api-token. |
| Set Price Record by Currency Code | `setPriceListRecord` | Creates or updates a single Price List Record using the currency code. Required field: price. |
| Update a Blog Post | `updateBlogPost` | Updates a blog post by ID (Content v2). Required: title, body. Field-by-field body. |
| Update a Currency | `updateCurrency` | Updates a currency by ID (v2). Required: currency_code. |
| Update a Customer (v2) | `updateCustomerV2` | Updates a customer by ID (v2, deprecated). Read-only fields (id, date_created, date_modified, accepts_marketing) cannot be set. |
| Update a Customer Address (v2) | `updateCustomerV2Address` | Updates a customer address by ID (v2, deprecated). Required: first_name, last_name, phone, street_1, city, state, zip, country. Read-only: id, country_iso2. |
| Update a Page | `updatePage` | Updates a single content page by ID (Pages v3). Field-by-field body. |
| Update a Page (v2) | `updatePageV2` | Updates a page by ID (Content v2, deprecated). Required: type, name, body. Field-by-field body. |
| Update a Placement | `updatePlacement` | Updates a widget Placement identified by uuid. Allows changing region, template_file, status, sort_order. |
| Update a Price List | `updatePriceList` | Updates a Price List by ID. Required field: name. |
| Update a Redirect (v2) | `updateRedirectV2` | Updates a redirect URL by ID (Content v2, deprecated). Required: path, forward. Field-by-field body. |
| Update a Script | `updateScript` | Updates a Script by uuid. Send the fields to change (name, src/html per kind, load_method, location, visibility, kind, consent_category). |
| Update a Site | `updateSite` | Update a site by site ID. PUT /v3/sites/{site_id}. |
| Update a Site Route | `updateSiteRoute` | Update a single site route. PUT /v3/sites/{site_id}/routes/{route_id}. |
| Update a Webhook | `updateWebhook` | Updates a webhook. PUT /v3/hooks/{webhook_id}. |
| Update a Widget | `updateWidget` | Updates a Widget by uuid. Can update name, widget_configuration, widget_template_uuid, and upgrade to latest template version. |
| Update a Widget Template | `updateWidgetTemplate` | Updates a Widget Template by uuid. Set create_new_version to create a new version instead of overwriting. |
| Update a Wishlist | `updateWishlist` | Updates a wishlist by ID. Required: customer_id, items. |
| Update Abandoned Cart Email Settings | `updateAbandonedCartEmailSettings` | Update abandoned cart email template settings. Optionally scope to a channel. |
| Update Abandoned Cart Email Template | `updateAbandonedCartEmail` | Update an abandoned cart email template by ID. Sends is_active, coupon_code, notify_at_minutes, and the template object. |
| Update an Email Template | `updateEmailTemplate` | Update a global email template or create a channel-specific override. Field-by-field body. |
| Update Analytics Provider | `updateAnalyticsProvider` | Updates a single web analytics provider for the default (or specified) channel. |
| Update Banner | `updateBanner` | Updates a Banner by id. |
| Update Brand | `updateBrand` | Updates a brand. Partial update - only the fields you supply are sent, so omitted fields keep their current values. Use custom_url to change the storefront SEO URL. |
| Update Brand Metafield | `updateBrandMetafield` | Updates a brand metafield. namespace, key, and permission_set can only be modified by the app that created the metafield. |
| Update Brand Metafields (Batch) | `updateBrandMetafieldsBatch` | Updates up to 50 brand metafields in a single request. Each item is a partial update keyed by the metafield id. |
| Update Bulk Pricing Rule | `updateBulkPricingRule` | Updates a bulk pricing rule for a product. Returns {data,meta}. |
| Update Carrier Connection | `updateCarrierConnection` | Updates a Carrier Connection (v2) using the same information as creating it; can be used to update credentials. Returns 204. |
| Update Cart Customer ID | `updateCart` | Assign a customer to a cart, or update its channel. |
| Update Cart Line Item | `updateCartLineItem` | Replace a cart line item's product_id/variant_id/quantity. |
| Update Cart Metafield | `updateCartMetafield` | Update a cart metafield by cart ID and metafield ID. |
| Update Cart Metafields (Batch) | `updateCartMetafieldsBatch` | Updates up to 50 cart metafields in a single request. Each item is a partial update keyed by the metafield id. |
| Update Catalog Settings | `updateCatalogSettings` | Updates catalog settings. Partial updates are not supported; supply all fields. |
| Update Category | `updateCategory` | Updates a category in the store catalog. This is a partial update: only the fields you supply are sent, so omitted fields keep their current values. BigCommerce requires name and parent_id on every update. Note: the Catalog V3 categories endpoints are deprecated in favour of the Category Trees endpoints, but remain supported. |
| Update Category Metafield | `updateCategoryMetafield` | Updates a category metafield. namespace, key, and permission_set can only be modified by the app that created the metafield. |
| Update Category Metafields (Batch) | `updateCategoryMetafieldsBatch` | Updates up to 50 category metafields in a single request. Each item is a partial update keyed by the metafield id. |
| Update Category Product Sort Order | `updateCategoryProductSortOrder` | Updates the sort order of products within a category. Body is a JSON array of {product_id, sort_order} objects. Pass it as a JSON array string in 'items'. |
| Update Channel | `updateChannel` | Updates a sales channel. This is a partial update: only the fields you supply are sent, so omitted fields keep their current values. |
| Update Channel Abandoned Cart Settings | `updateChannelAbandonedCartSettings` | Updates the per-channel overrides for the abandoned cart settings of a store. |
| Update Channel Cart Settings | `updateChannelCartSettings` | Update the per-channel overrides for the cart settings of a store. |
| Update Channel Currency Assignments | `updateSingleChannelCurrencyAssignments` | Updates enabled currencies and default currency for a specific channel. |
| Update Channel Listings | `updateChannelListings` | Updates one or more Channel Listings for a specific channel. Body is a JSON array string; each item requires listing_id, product_id, state, variants. |
| Update Channel Metafield | `updateChannelMetafield` | Updates a single channel metafield. All write fields are sent; modifying namespace/key/permission_set with a different client ID returns 403. |
| Update Channel Metafields (Batch) | `updateChannelMetafieldsBatch` | Updates up to 50 channel metafields in a single request. Each item is a partial update keyed by the metafield id. |
| Update Channel Order Settings | `updateChannelOrderSettings` | Updates order settings for a specific channel (v3). Accepts a JSON object string for the settings body. Both notification email_addresses must be set together or both null. |
| Update Channel Site | `updateChannelSite` | Updates the site for the provided channel. |
| Update Checkout Billing Address | `updateCheckoutBillingAddress` | Replace the billing address on a checkout. |
| Update Checkout Consignment | `updateCheckoutConsignment` | Update a consignment — e.g. set the selected shipping_option_id. |
| Update Checkout Customer Message | `updateCheckout` | Update checkout customer message. |
| Update Checkout Settings | `updateCheckoutSettings` | Update the store's checkout settings. Pass empty strings for script URLs to reset to optimized one-page checkout. |
| Update Complex Rule | `updateComplexRule` | Updates a product complex rule. Pass product_id and the conditions array (each with modifier_id, modifier_value_id, variant_id). Returns {data,meta}. |
| Update Coupon | `updateCoupon` | Updates a Coupon by id. If applies_to is omitted, its existing value is cleared. |
| Update Customer Addresses | `updateCustomerAddresses` | Update customer addresses (V3 expects an array). Each item must include its id. |
| Update Customer Attributes | `updateCustomerAttributes` | Update customer attribute definitions (array, each with id). |
| Update Customer Consent | `updateCustomerConsent` | Updates the status of a customer's consent to allow data collection by cookies and scripts while shopping on a storefront. |
| Update Customer Group | `updateCustomerGroup` | Updates a customer group. This is a partial update: only the fields you supply are sent, so omitted fields keep their current values. |
| Update Customer Metafield | `updateCustomerMetafield` | Updates a metafield on a customer. This is a partial update: only the fields you supply are sent, so omitted fields keep their current values. |
| Update Customer Metafields (Batch) | `updateCustomerMetafieldsBatch` | Updates up to 50 customer metafields in a single request. Each item is a partial update keyed by the metafield id. |
| Update Customer Settings | `updateCustomerSettings` | Updates the customer settings on the global level (privacy settings and customer group settings). |
| Update Customer Settings per Channel | `updateCustomerChannelSettings` | Updates the customer settings for a specific channel. Setting null deletes the override for the channel and values are inherited from the global level. |
| Update Customers | `updateCustomers` | Update one or more customers (V3 expects an array). Each customer object must include its id. Only included fields are updated. |
| Update Email Statuses | `updateEmailStatuses` | Updates transactional email (status) settings, globally or per channel. |
| Update Enabled Search Filters | `updateSearchFilters` | Updates enabled default Product Filtering filters. Body is a JSON array string of filter objects. |
| Update Gift Certificate | `updateGiftCertificate` | Updates a Gift Certificate by id. Read-only: id, order_id. |
| Update Global Abandoned Cart Settings | `updateAbandonedCartSettings` | Updates the global abandoned cart settings of a store. |
| Update Global Cart Settings | `updateCartSettings` | Update the global cart settings of a store. Set allow_purchasing. |
| Update Global Order Settings | `updateGlobalOrderSettings` | Updates global order settings (v3). Accepts a JSON object string for the settings body (notifications object). |
| Update Inventory Locations | `updateInventoryLocations` | Update one or more inventory locations (bulk endpoint). The request body is a JSON array of location objects, each MUST include its id plus the fields to change. Pass the array as a JSON-encoded string in 'items'. |
| Update Inventory Notifications Settings | `updateInventoryNotifications` | Updates inventory notification settings. Partial updates not supported; supply all fields. |
| Update Inventory Settings | `updateInventorySettings` | Updates inventory settings. Partial updates are not supported; supply all fields. |
| Update Location Metafield | `updateLocationMetafield` | Update a metafield on a specific inventory location. Send only the fields to change; value is the most common. |
| Update Location Metafields (Batch) | `updateLocationMetafieldsBatch` | Updates up to 50 location metafields in a single request. Each item is a partial update keyed by the metafield id. |
| Update Logo Settings | `updateLogoSettings` | Updates the logo type and logo text. To upload images use createLogoImage. Supply all fields. |
| Update Modifier Value | `updateModifierValue` | Updates a value of a product modifier by value ID. |
| Update Multiple Channels Currency Assignments | `updateMultipleChannelsCurrencyAssignments` | Updates enabled currencies and default currency for multiple channels. Body is a JSON array string. |
| Update Order | `updateOrder` | Updates an order using the Orders V2 API. This is a partial update: only the fields you supply are sent, so omitted fields keep their current values. Supports order totals and cost overrides, billing and shipping addresses, line items, fees, consignments, channel and source attribution, and archiving via is_deleted. |
| Update Order Metafield | `updateOrderMetafield` | Updates an order Metafield object (v3). |
| Update Order Metafields (Batch) | `updateOrderMetafieldsBatch` | Updates up to 50 order metafields in a single request. Each item is a partial update keyed by the metafield id. |
| Update Order Shipment | `updateOrderShipment` | Update a shipment (e.g. correct the tracking number, tracking link or shipping method). |
| Update Order Shipping Address | `updateOrderShippingAddress` | Update a shipping address on an order. |
| Update Pages | `updatePages` | Updates one or more content pages (Pages v3 bulk). Accepts a JSON array string of page objects (each must include id) in the 'items' input. |
| Update Product | `updateProduct` | Update an existing product. Only include fields you want to change. |
| Update Product Custom Field | `updateProductCustomField` | Update a custom field on a product. |
| Update Product Image | `updateProductImage` | Update a product image's metadata or replace its URL. |
| Update Product Metafield | `updateProductMetafield` | Updates a product metafield by ID. Returns {data,meta}. |
| Update Product Metafields (Batch) | `updateProductMetafieldsBatch` | Updates up to 50 product metafields in a single request. Each item is a partial update keyed by the metafield id. |
| Update Product Modifier | `updateProductModifier` | Update a product modifier. |
| Update Product Review | `updateProductReview` | Updates a product review by ID. Returns {data,meta}. |
| Update Product Tax Properties | `updateProductTaxProperties` | Update the tax properties associated with one or more products (v3). Additive; overwrites existing values. Body is a JSON array string. |
| Update Product Variant | `updateProductVariant` | Updates a single product variant. This is a partial update: only the fields you supply are sent, so omitted fields keep their current values. For a product with no options the variant is the base variant, and changes propagate to the parent product. |
| Update Product Variant Metafield | `updateVariantMetafield` | Updates a metafield on a product variant by metafield ID. |
| Update Product Variant Option | `updateProductOption` | Updates a product option. This is a partial update: only the fields you supply are sent, so omitted fields keep their current values. |
| Update Product Variant Option Value | `updateOptionValue` | Updates a value of a product variant option by value ID. |
| Update Product Video | `updateProductVideo` | Updates a product video by ID. Returns {data,meta}. |
| Update Products (Batch) | `updateProducts` | Bulk-updates a batch of existing products. Pass a JSON array string of product objects (each must include its id). Returns {data:[...products],meta}. |
| Update Products Category Assignments | `updateProductsCategoryAssignments` | Creates/updates product-to-category assignments in bulk. Pass a JSON array string of {product_id,category_id} objects. Returns 204 No Content on success. |
| Update Products Channel Assignments | `updateProductsChannelAssignments` | Creates/updates product-to-channel assignments in bulk. Pass a JSON array string of {product_id,channel_id} objects. Returns 204 No Content on success. |
| Update Promotion | `updatePromotion` | Updates an existing promotion by ID. Send only the fields to change; rules must be sent in full when changed. Returns the updated promotion in a {data} envelope. |
| Update Robots.txt Settings | `updateRobotsTxtSettings` | Updates Robots.txt settings. Supply all fields. |
| Update Shipping Method | `updateShippingMethod` | Updates a Shipping Method in a zone (v2). |
| Update Shipping Zone | `updateShippingZone` | Updates a Shipping Zone (v2). Requires name. id is read-only. |
| Update Site Routes (Bulk) | `updateSiteRoutes` | Upsert multiple routes for a site. Accepts a JSON array string of route objects (id required when updating an existing route). PUT /v3/sites/{site_id}/routes. |
| Update Store Locale | `updateStoreLocale` | Updates global (or channel) locale settings. |
| Update Store Metafields (Batch) | `updateStoreMetafieldsBatch` | Updates up to 50 store metafields in a single request. Each item is a partial update keyed by the metafield id. |
| Update Store Profile | `updateStoreProfile` | Updates store profile settings. Supply all fields. |
| Update Storefront Category Settings | `updateStorefrontCategorySettings` | Updates storefront category settings. Supply all fields. |
| Update Storefront Product Settings | `updateStorefrontProductSettings` | Updates storefront product settings. Supply all fields. |
| Update Storefront Search Settings | `updateStorefrontSearchSettings` | Updates storefront search settings. Supply all fields. |
| Update Storefront Security Settings | `updateStorefrontSecuritySettings` | Updates storefront security settings. Pass nested objects (csp_header, hsts, x_frame_options_header) as JSON strings; sitewide_https_enabled as boolean. |
| Update Storefront SEO Settings | `updateStorefrontSeoSettings` | Updates storefront SEO settings. Supply all fields. |
| Update Storefront Status | `updateStorefrontStatus` | Updates storefront status settings (maintenance/prelaunch messages). prelaunch_password is read-only. |
| Update Subscriber | `updateSubscriber` | Update a subscriber. |
| Update Tax Properties | `updateTaxProperties` | Update one or more tax properties (v3). Body is a JSON array string; each item requires id. Only specified fields are adjusted. |
| Update Tax Rates | `updateTaxRates` | Update one or more tax rates (v3). Only id is required; unspecified fields retain current state. Body is a JSON array string. |
| Update Tax Settings | `updateTaxSettings` | Updates global-level tax settings (v3). Send the fields you wish to change. |
| Update Tax Zones | `updateTaxZones` | Update one or more tax zones (v3). Only id is required; unspecified fields retain current state. Body is a JSON array string. |
| Update Tree Categories (Bulk) | `updateTreeCategories` | Bulk updates categories. Body is a JSON array of category objects; each requires category_id. Pass as a JSON array string in 'items'. Returns 204/207 with a meta summary. |
| Update Units of Measurement Settings | `updateUnitsOfMeasurement` | Updates units-of-measurement settings. Partial updates not supported; supply all fields. |
| Update Variant Metafields (Batch) | `updateVariantMetafieldsBatch` | Updates up to 50 variant metafields in a single request. Each item is a partial update keyed by the metafield id. |
| Update Variants (Batch) | `updateVariantsBatch` | Updates a batch of variant objects (limit 50). Pass a JSON array string of variant objects; each must include id to update, or product_id + sku + option_values to create. |
| Update WL Product | `updateWishlistItem` | Update the products on a wishlist. BigCommerce has no per-item update endpoint; this PUTs the full wishlist (name, is_public, customer_id, and the complete items array) to /v3/wishlists/{wishlist_id}. Pass the full desired items list — items omitted from the array are removed. Returns the updated wishlist resource. |
| Upload a Theme | `uploadTheme` | Uploads a new Theme (.zip) to the store via multipart/form-data. Pass the file in the 'file' input. Returns a job_id for the background processing job (201). |
| Upsert a Site's Certificate | `upsertSiteCertificate` | Upsert a site's SSL/TLS certificate. If url is omitted, applies to the site's primary URL. Overwrites any existing certificate. PUT /v3/sites/{site_id}/certificate. |
| Upsert Batch of Price List Records (Multi-List) | `upsertPriceListRecordsBatch` | Creates a batch of Price List Records that may span more than one price list. Body is a JSON array string of records, each with price_list_id, variant_id or sku, currency, and price fields. |
| Upsert Category Trees | `upsertCategoryTrees` | Upserts category trees. Body is a JSON array of tree objects {id?, name, channels[]}. An object with an id is updated; one without is created. channel_id required to create. Pass as a JSON array string in 'items'. |
| Upsert Channel Site Checkout URL | `putChannelSiteCheckoutUrl` | Creates or updates (upserts) a site's checkout URL for a channel. [BLOCKED: provider returns 422 "Failed to save site on saving domain for store 1003251411. Probably this domain is already in use for this or other store." — reproduced with both the requested domain and a unique random subdomain of the site's primary URL; the store's domain-save subsystem rejects all checkout-URL writes (account-state block).] |
| Upsert Contextual Search Filters | `upsertSearchFilterContexts` | Upserts contextual filters for a particular channel or category. Body is a JSON array string of override objects, each with a context {channel_id\|category_id} and a data array of filters. BigCommerce rejects the call with 422 'Invalid Facet Input' if a filter object omits items_to_show (must be 5, 10 or 15) even though the official spec does not list it as required - always include it, along with is_enabled and type, or read the filter's current shape back from getSearchFilterContexts/getSearchFilters first and round-trip it. |
| Upsert Custom Template Associations | `upsertCustomTemplateAssociations` | Upsert custom template associations across all storefronts. Accepts a JSON array string of association objects in the 'items' input. |
| Upsert Customer Attribute Values | `upsertCustomerAttributeValues` | Upsert attribute values for customers (array of {attribute_id, value, customer_id}). PUT acts as upsert. |
| Upsert Customer Form Field Values | `upsertCustomerFormFieldValues` | Upsert form field values for customers (array). Use to attach custom checkout field data to customer records. |
| Upsert Customs Information | `putCustomsInformation` | Creates and updates product customs information (v3). Batch operation, up to 50 objects per PUT. Body is a JSON array string. |
| Upsert Price List Assignment | `upsertPriceListAssignment` | Upserts a single Price List Assignment for a Price List. Required fields: customer_group_id, channel_id. |
| Upsert Price List Records | `upsertPriceListRecords` | Creates or updates Price List Records for a single Price List. Body is a JSON array string of records (variant_id or sku, currency required, price fields). |
| Upsert Redirects | `upsertRedirects` | Upserts new redirect data across all storefronts (Redirects v3). Accepts a JSON array string of redirect objects in the 'items' input. |
| Upsert Webhook Notification Emails | `upsertWebhookNotificationEmails` | Upsert the email addresses notified when a domain is denylisted or a webhook is deactivated. Returns 204 No Content. PUT /v3/hooks/admin. |
| Validate a Customer Password (v2) | `validateCustomerPasswordV2` | Validates a customer's password by ID (v2, deprecated). Returns success true/false indicating whether the provided password matches the customer's current password. Has special rate limiting. |
| Validate Customer Credentials | `validateCustomerCredentials` | Validate a storefront customer's email + password. Used for headless storefront auth. |
| Validate Theme Configuration | `validateThemeConfiguration` | DEPRECATED - confirmed retired by BigCommerce, do not attempt to fix. Spec route was POST /v3/themes/{uuid}/configurations/validate. Confirmed against theme uuid e3d82ce0-9bae-0133-0de7-525400970412 with a valid variation_id; sibling GET /configurations on the same base path returns 200, but POST .../configurations/validate returns 404. Re-confirmed 2026-09-02 against BigCommerce's official OpenAPI source (github.com/bigcommerce/api-specs-1) and current docs pages theme-configurations and theme-actions: neither documents a validate endpoint anywhere under /v3/themes today - only GET /v3/themes/{uuid}/configurations and POST /v3/themes/{uuid}/actions/download exist. Provider-side removal, not a catalog defect. |
| Void Order Payment | `voidOrderPayment` | Void the payment for an order (v3). No request body. Sets payment_status to 'void pending'. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| App Uninstalled | `store/app/uninstalled` | Fires when the app is uninstalled from the store. |
| App Uninstalled | `store/app/uninstalled` | Fires when the app is uninstalled from the store. |
| Cart Abandoned | `store/cart/abandoned` | Fires when a cart is abandoned. |
| Cart Abandoned | `store/cart/abandoned` | Fires when a cart is considered abandoned. |
| Cart Converted | `store/cart/converted` | Fires when a cart is converted to an order. |
| Cart Converted | `store/cart/converted` | Fires when a cart converts to an order. |
| Cart Coupon Applied | `store/cart/couponApplied` | Fires when a coupon is applied to a cart. |
| Cart Coupon Applied | `store/cart/couponApplied` | Fires when a coupon is applied to a cart. |
| Cart Created | `store/cart/created` | Fires when a new cart is created. |
| Cart Created | `store/cart/created` | Fires when a cart is created. |
| Cart Deleted | `store/cart/deleted` | Fires when a cart is deleted. |
| Cart Deleted | `store/cart/deleted` | Fires when a cart is deleted. |
| Cart Line Item Created | `store/cart/lineItem/created` | Fires when a line item is added to a cart. |
| Cart Line Item Created | `store/cart/lineItem/created` | Fires when a line item is added to a cart. |
| Cart Line Item Deleted | `store/cart/lineItem/deleted` | Fires when a cart line item is deleted. |
| Cart Line Item Deleted | `store/cart/lineItem/deleted` | Fires when a cart line item is removed. |
| Cart Line Item Updated | `store/cart/lineItem/updated` | Fires when a cart line item is updated. |
| Cart Line Item Updated | `store/cart/lineItem/updated` | Fires when a cart line item is updated. |
| Cart Updated | `store/cart/updated` | Fires when a cart is updated. |
| Cart Updated | `store/cart/updated` | Fires when a cart is updated. |
| Category Created | `store/category/created` | Fires when a category is created. |
| Category Created | `store/category/created` | Fires when a category is created. |
| Category Deleted | `store/category/deleted` | Fires when a category is deleted. |
| Category Deleted | `store/category/deleted` | Fires when a category is deleted. |
| Category Updated | `store/category/updated` | Fires when a category is updated. |
| Category Updated | `store/category/updated` | Fires when a category is updated. |
| Channel Created | `store/channel/created` | Fires when a channel is created. |
| Channel Created | `store/channel/created` | Fires when a sales channel is created. |
| Channel Updated | `store/channel/updated` | Fires when a channel is updated. |
| Channel Updated | `store/channel/updated` | Fires when a sales channel is updated. |
| Customer Address Created | `store/customer/address/created` | Fires when a customer address is created. |
| Customer Address Created | `store/customer/address/created` | Fires when a customer address is created. |
| Customer Address Deleted | `store/customer/address/deleted` | Fires when a customer address is deleted. |
| Customer Address Deleted | `store/customer/address/deleted` | Fires when a customer address is deleted. |
| Customer Address Updated | `store/customer/address/updated` | Fires when a customer address is updated. |
| Customer Address Updated | `store/customer/address/updated` | Fires when a customer address is updated. |
| Customer Created | `store/customer/created` | Fires when a customer is created. |
| Customer Created | `store/customer/created` | Fires when a customer account is created. |
| Customer Default Payment Instrument Updated | `store/customer/payment/instrument/default/updated` | Fires when a customer's default payment instrument is updated. |
| Customer Default Payment Instrument Updated | `store/customer/payment/instrument/default/updated` | Fires when a customer's default stored payment instrument changes. |
| Customer Deleted | `store/customer/deleted` | Fires when a customer is deleted. |
| Customer Deleted | `store/customer/deleted` | Fires when a customer account is deleted. |
| Customer Updated | `store/customer/updated` | Fires when a customer is updated. |
| Customer Updated | `store/customer/updated` | Fires when a customer account is updated. |
| Order Archived | `store/order/archived` | Fires when an order is archived. |
| Order Archived | `store/order/archived` | Fires when an order is archived. |
| Order Created | `store/order/created` | Fires when an order is created. |
| Order Created | `store/order/created` | Fires when a new order is created. Payload carries the order id under data.id. |
| Order Message Created | `store/order/message/created` | Fires when an order message is created. |
| Order Message Created | `store/order/message/created` | Fires when a message is added to an order. |
| Order Refund Created | `store/order/refund/created` | Fires when a refund is created on an order. |
| Order Refund Created | `store/order/refund/created` | Fires when a refund is created for an order. |
| Order Status Updated | `store/order/statusUpdated` | Fires when an order status is updated. |
| Order Status Updated | `store/order/statusUpdated` | Fires when an order's status changes. Payload includes previous and new status under data.status. |
| Order Updated | `store/order/updated` | Fires when an order is updated. |
| Order Updated | `store/order/updated` | Fires when an order is updated (e.g. status change). |
| Product Created | `store/product/created` | Fires when a product is created. |
| Product Created | `store/product/created` | Fires when a product is created. |
| Product Deleted | `store/product/deleted` | Fires when a product is deleted. |
| Product Deleted | `store/product/deleted` | Fires when a product is deleted. |
| Product Inventory Order Updated | `store/product/inventory/order/updated` | Fires when product inventory is updated due to an order. |
| Product Inventory Order Updated | `store/product/inventory/order/updated` | Fires when product inventory changes as a result of an order. |
| Product Inventory Updated | `store/product/inventory/updated` | Fires when product inventory is updated. |
| Product Inventory Updated | `store/product/inventory/updated` | Fires when a product's inventory is updated. |
| Product Updated | `store/product/updated` | Fires when a product is updated. |
| Product Updated | `store/product/updated` | Fires when a product is updated. |
| Shipment Created | `store/shipment/created` | Fires when a shipment is created. |
| Shipment Created | `store/shipment/created` | Fires when a shipment is created for an order. |
| Shipment Deleted | `store/shipment/deleted` | Fires when a shipment is deleted. |
| Shipment Deleted | `store/shipment/deleted` | Fires when a shipment is deleted. |
| Shipment Updated | `store/shipment/updated` | Fires when a shipment is updated. |
| Shipment Updated | `store/shipment/updated` | Fires when a shipment is updated. |
| SKU Created | `store/sku/created` | Fires when a SKU (variant) is created. |
| SKU Created | `store/sku/created` | Fires when a product variant (SKU) is created. |
| SKU Deleted | `store/sku/deleted` | Fires when a SKU is deleted. |
| SKU Deleted | `store/sku/deleted` | Fires when a product variant (SKU) is deleted. |
| SKU Inventory Order Updated | `store/sku/inventory/order/updated` | Fires when SKU inventory is updated due to an order. |
| SKU Inventory Order Updated | `store/sku/inventory/order/updated` | Fires when SKU inventory changes as a result of an order. |
| SKU Inventory Updated | `store/sku/inventory/updated` | Fires when SKU inventory is updated. |
| SKU Inventory Updated | `store/sku/inventory/updated` | Fires when a SKU's inventory is updated. |
| SKU Updated | `store/sku/updated` | Fires when a SKU is updated. |
| SKU Updated | `store/sku/updated` | Fires when a product variant (SKU) is updated. |
| Store Information Updated | `store/information/updated` | Fires when store information is updated. |
| Store Information Updated | `store/information/updated` | Fires when store profile/settings information is updated. |
| Subscriber Created | `store/subscriber/created` | Fires when a subscriber is created. |
| Subscriber Created | `store/subscriber/created` | Fires when a newsletter/email subscriber is created. |
| Subscriber Deleted | `store/subscriber/deleted` | Fires when a subscriber is deleted. |
| Subscriber Deleted | `store/subscriber/deleted` | Fires when a subscriber is deleted. |
| Subscriber Updated | `store/subscriber/updated` | Fires when a subscriber is updated. |
| Subscriber Updated | `store/subscriber/updated` | Fires when a subscriber is updated. |
