---
description: "TikTok Shop Open API connector — products, orders, fulfillment, logistics, returns/refunds, finance, promotions, analytics, customer service, FBT, affiliate,…"
---

# TikTok Shop

TikTok Shop Open API connector — products, orders, fulfillment, logistics, returns/refunds, finance, promotions, analytics, customer service, FBT, affiliate, and webhooks. Global region (open-api.tiktokglobalshop.com).

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [tiktokglobalshop.com](https://tiktokglobalshop.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 172 |
| **Events** | 8 |
| **Slug** | `tiktokShop` |

## Use it

Add TikTok Shop from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tiktokShop.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Products | `activateProducts` | Activate (list) products. Body JSON: {"product_ids":["..."]}. |
| Add External Order References | `addExternalOrderReferences` | Link external platform order references (v202406). POST body. |
| Approve Cancellation | `approveCancellation` | Approve a buyer cancellation by cancel_id. POST body. |
| Approve Return | `approveReturn` | Approve a return request by return_id. POST body. |
| Batch Ship Packages | `batchShipPackages` | Ship multiple packages at once. POST body with packages[]. |
| Calculate Refund | `calculateRefund` | Compute the refund amount for items. POST body. |
| Calculate Refund v2 | `calculateRefundV2` | Calculate Refund (TikTok 202602). Side-by-side v2 of the action that stays on 202309. Read-only calculation, does not issue a refund. |
| Cancel Order (seller) | `cancelOrder` | Seller-initiated order cancellation. POST body. |
| Cancel Order (seller) v2 | `cancelOrderV2` | Cancel Order, seller initiated (TikTok 202602). Side-by-side v2 of the action that stays on 202309. WRITE ACTION - cancels a real order. |
| Check Listing Prerequisites | `checkListingPrerequisites` | Check whether the seller meets prerequisites to list products. |
| Check Listing Prerequisites v2 | `checkListingPrerequisitesV2` | Check Listing Prerequisites (TikTok 202312). Side-by-side v2 of the action that stays on 202309. Returns per-item check results with failure reasons. |
| Combine Packages | `combinePackages` | Combine multiple packages into one. POST body. |
| Confirm Package Shipment (Supply Chain) | `confirmPackageShipment` | Sync/confirm package shipment with a 3PL warehouse provider (supply_chain v202309). POST body with package data. |
| Create Conversation | `createConversation` | Start a new conversation with a buyer. POST body (customer_service v202309). |
| Create Custom Brand | `createCustomBrand` | Register a custom brand. Body JSON: {"name":"..."}. |
| Create Global Product | `createGlobalProduct` | Create a cross-border global product. Pass full global product body JSON (title, description, category_id, skus, etc.) (product global_products v202309). |
| Create Manufacturer | `createManufacturer` | Add a new EU GPSR manufacturer. POST body with name, address, contact (product compliance v202409). |
| Create Open Collaboration | `createOpenCollaboration` | Create an affiliate open collaboration (affiliate_seller v202405). POST body. |
| Create Open Collaboration v2 | `createOpenCollaborationV2` | Create Open Collaboration (TikTok 202412). Side-by-side v2 of the action that stays on 202405. Typed request body replaces the old opaque bodyJson string. |
| Create Packages | `createPackages` | Create packages from order line items. POST body. |
| Create Packages v2 | `createPackagesV2` | Create Packages (TikTok 202512). Side-by-side v2 of the action that stays on 202309. |
| Create Product | `createProduct` | Create a product listing. Pass full product body JSON (title, description, category_id, skus, package_weight, etc.). |
| Create Promotion Activity | `createActivity` | Create a promotion activity (flash sale / direct discount). POST body. |
| Create Responsible Person | `createResponsiblePerson` | Add a new EU GPSR responsible person. POST body with name, address, contact, email/phone (product compliance v202409). |
| Create Return | `createReturn` | Initiate a return/refund request. POST body. |
| Create Return v2 | `createReturnV2` | Create Return (TikTok 202602). Side-by-side v2 of the action that stays on 202309. WRITE ACTION - creates a real return request. |
| Create Target Collaboration | `createTargetCollaboration` | Create an affiliate target collaboration with a specific creator (affiliate_seller v202405). POST body. |
| Create Target Collaboration v2 | `createTargetCollaborationV2` | Create Target Collaboration (TikTok 202508). Side-by-side v2 of the action that stays on 202405. |
| Deactivate Products | `deactivateProducts` | Deactivate (unlist) products. Body JSON: {"product_ids":["..."]}. |
| Deactivate Promotion Activity | `deactivateActivity` | Deactivate a promotion activity by activity_id. POST. |
| Delete Global Products | `deleteGlobalProducts` | Delete one or more cross-border global products. Body JSON: {"global_product_ids":["..."]} (product global_products v202309). |
| Delete Products | `deleteProducts` | Delete one or more products. Body JSON: {"product_ids":["..."]}. |
| Delete Shop Webhook | `deleteShopWebhook` | Delete a webhook subscription by event_type (event v202309). Body: {"event_type":"..."}. |
| Edit Global Product | `editGlobalProduct` | Full edit of an existing cross-border global product by global_product_id. Pass full global product body JSON (product global_products v202309). |
| Edit Product | `editProduct` | Full edit of an existing product by product_id. Pass full product body JSON. |
| Edit Product v2 | `editProductV2` | Edit Product (TikTok 202509). Side-by-side v2 of the action that stays on 202309. Full product replacement. |
| Fulfillment Upload File | `fulfillmentUploadFile` | Upload a delivery document for fulfillment. POST body. |
| Fulfillment Upload Image | `fulfillmentUploadImage` | Upload a delivery proof image for fulfillment. POST body. |
| Generate Product Promotion Link | `generateProductPromotionLink` | Generate a shareable affiliate promotion link for a product (affiliate_seller v202405). POST body. |
| Get Active Shops | `getActiveShops` | Get the seller's active shops (seller-level). |
| Get Aftersale Eligibility | `getAftersaleEligibility` | Check return/refund eligibility for an order. |
| Get Aftersale Eligibility v2 | `getAftersaleEligibilityV2` | Get Aftersale Eligibility (TikTok 202602). Side-by-side v2 of the action that stays on 202309. Returns per-SKU, per-line-item eligibility for CANCEL / RETURN / RETURN_AND_REFUND. |
| Get Agent Settings | `getAgentSettings` | Get the customer-service agent configuration (customer_service v202309). |
| Get Authorized Category Assets | `getAuthorizedCategoryAssets` | Get the category assets the app is authorized to access for the shop. |
| Get Authorized Shops | `getAuthorizedShops` | List shops the seller authorized to this app. Returns shop_cipher + shop_id needed for all other calls. CALL FIRST. Note: TikTok request signing (app_key/sign/timestamp) is applied by the platform signing layer. |
| Get Brands | `getBrands` | List brands available to the shop. Query page_size/page_token/category_id. |
| Get Categories | `getCategories` | Get the product category tree. Optional locale/category_version query. |
| Get Category Attributes | `getCategoryAttributes` | Get required/optional attributes for a category_id. |
| Get Category Rules | `getCategoryRules` | Get listing rules/requirements for a category_id. |
| Get Conversation Messages | `getConversationMessages` | List messages in a conversation by conversation_id (customer_service v202309). |
| Get Conversations | `getConversations` | List buyer-seller conversations. Query page params (customer_service v202309). |
| Get Coupon | `getCoupon` | Get a coupon by coupon_id. |
| Get Eligible Shipping Service | `getEligibleShippingService` | Query available shipping options for an order. POST body. |
| Get External Order References | `getExternalOrderReferences` | Retrieve external references for a TikTok order (v202406). |
| Get FBT Inbound Orders | `getFbtInboundOrders` | Get FBT inbound orders by IDs (fbt v202409). Query inbound_order_ids. |
| Get FBT Inbound Orders v2 | `getFbtInboundOrdersV2` | Get FBT Inbound Orders (TikTok 202602). Side-by-side v2 of the action that stays on 202409. |
| Get FBT Onboarded Regions | `getFbtMerchantOnboardedRegions` | List regions where the merchant's Fulfilled-by-TikTok is active (fbt v202409). |
| Get FBT Warehouse List | `getFbtWarehouseList` | List Fulfilled-by-TikTok warehouses (fbt v202408). |
| Get Global Attributes | `getGlobalAttributes` | Get required/optional global attributes for a category_id used when creating global products. Optional locale query (product categories global_attributes v202309). |
| Get Global Categories | `getGlobalCategories` | Get the global (cross-border) product category tree. Optional locale/keyword/category_version query (product global_categories v202309). |
| Get Global Category Rules | `getGlobalCategoryRules` | Get the additional listing rules/requirements for a category_id when creating global products (product categories global_rules v202309). |
| Get Global Product | `getGlobalProduct` | Get full detail of a single cross-border global product by global_product_id (product global_products v202309). |
| Get Global Seller Warehouses | `getGlobalSellerWarehouses` | List global (cross-border) seller warehouses. |
| Get Open Collaboration Settings | `getOpenCollaborationSettings` | Get affiliate open-collaboration settings (affiliate_seller v202409). |
| Get Order Detail | `getOrderDetail` | Get full detail for one or more orders by IDs (comma-separated in ids). |
| Get Order Detail v2 | `getOrderDetailV2` | Get Order Detail (TikTok 202507). Side-by-side v2 of the action that stays on 202309. Used by the settlement sync on every run. Response shape differs between versions. |
| Get Order Price Detail | `getPriceDetail` | Get detailed price breakdown for an order (v202407). |
| Get Order Split Attributes | `getOrderSplitAttributes` | Check split eligibility for orders. Query order_ids. |
| Get Order Statement Transactions | `getOrderStatementTransactions` | Get settlement transactions linked to a specific order. |
| Get Order Statement Transactions v2 | `getOrderStatementTransactionsV2` | Get Order Statement Transactions (TikTok 202501). Side-by-side v2 of the action that stays on 202309. Returns the settlement breakdown for a single order with typed fee/tax sub-objects. |
| Get Order Tracking | `getTracking` | Get tracking/delivery progress for an order. |
| Get Package Detail | `getPackageDetail` | Get detail of a package by package_id. |
| Get Package Handover Time Slots | `getPackageHandoverTimeSlots` | Get available pickup/handover time windows for a package. |
| Get Package Shipping Document | `getPackageShippingDocument` | Get the shipping label/document for a package. Query document_type. |
| Get Payments | `getPayments` | List payment records sorted by create time. Query page params. |
| Get Payments v2 | `getPaymentsV2` | Get Payments (TikTok 202605). Side-by-side v2 of 'Get Payments', which stays on 202309. Returns payment/payout records with typed amount objects. |
| Get Product | `getProduct` | Get full detail of a single product by product_id. |
| Get Promotion Activity | `getActivity` | Get a promotion activity by activity_id. |
| Get Reject Reasons | `getRejectReasons` | Get available rejection reasons for returns/cancellations. Query biz fields. |
| Get Return Records | `getReturnRecords` | Get the history/records of a return by return_id. |
| Get Seller Permissions | `getSellerPermissions` | Get the API permissions granted to the seller. |
| Get Shipping Providers | `getShippingProviders` | Get shipping providers for a delivery option. |
| Get Shop Performance | `getShopPerformance` | Get overall shop performance metrics (GMV, orders, etc.) for a date range (analytics v202405). |
| Get Shop Performance v2 | `getShopPerformanceV2` | Get Shop Performance (TikTok 202509). Side-by-side v2 of the action that stays on 202405. |
| Get Shop Product Performance | `getShopProductPerformance` | Get performance for a single product by product_id (analytics v202405). |
| Get Shop Product Performance List | `getShopProductPerformanceList` | List performance metrics across all products (analytics v202405). |
| Get Shop Product Performance List v2 | `getShopProductPerformanceListV2` | Get Shop Product Performance List (TikTok 202605). Side-by-side v2 of the action that stays on 202405. |
| Get Shop Product Performance v2 | `getShopProductPerformanceV2` | Get Shop Product Performance (TikTok 202509). Side-by-side v2 of the action that stays on 202405. |
| Get Shop SKU Performance | `getShopSkuPerformance` | Get performance for a single SKU by sku_id (analytics v202405). |
| Get Shop SKU Performance List | `getShopSkuPerformanceList` | List performance metrics across all SKUs (analytics v202405). |
| Get Shop Video Performance | `getShopVideoPerformance` | Get performance for a single video by video_id (analytics v202405). |
| Get Shop Video Performance List | `getShopVideoPerformanceList` | List performance metrics across shop videos (analytics v202405). |
| Get Shop Video Performance List v2 | `getShopVideoPerformanceListV2` | Get Shop Video Performance List (TikTok 202605). Side-by-side v2 of the action that stays on 202409. |
| Get Shop Video Performance Overview | `getShopVideoPerformanceOverview` | Get a summary overview of video performance (analytics v202405). |
| Get Shop Video Performance Overview v2 | `getShopVideoPerformanceOverviewV2` | Get Shop Video Performance Overview (TikTok 202509). Side-by-side v2 of the action that stays on 202409. |
| Get Shop Video Performance v2 | `getShopVideoPerformanceV2` | Get Shop Video Performance (TikTok 202509). Side-by-side v2 of the action that stays on 202409. |
| Get Shop Video Product Performance List | `getShopVideoProductPerformanceList` | List product performance within a specific video (analytics v202405). |
| Get Shop Video Product Performance List v2 | `getShopVideoProductPerformanceListV2` | Get Shop Video Product Performance List (TikTok 202509). Side-by-side v2 of the action that stays on 202409. |
| Get Shop Webhooks | `getShopWebhooks` | List the shop's registered webhook subscriptions (event v202309). Webhook-management action. |
| Get Statement Transactions | `getStatementTransactions` | Get transactions for a settlement statement by statement_id. |
| Get Statement Transactions v2 | `getStatementTransactionsV2` | Get Transactions by Statement (TikTok 202501). Side-by-side v2 of 'Get Statement Transactions', which stays on 202309. Shape differs: rows are under data.transactions (202309 used data.statement_transactions) with a typed `type` enum incl. FBT_WAREHOUSE_SERVICE_FEE and GMV_PAYMENT_FOR_ADS. sort_field is REQUIRED on 202501. |
| Get Statements | `getStatements` | List settlement statements. Query page params, sort, time range. |
| Get Target Collaboration Detail | `queryTargetCollaborationDetail` | Get a target collaboration by id (affiliate_seller v202409). |
| Get Target Collaboration Detail v2 | `queryTargetCollaborationDetailV2` | Get Target Collaboration Detail (TikTok 202508). Side-by-side v2 of the action that stays on 202409. |
| Get Warehouse Delivery Options | `getWarehouseDeliveryOptions` | Get delivery options for a warehouse. |
| Get Warehouse List | `getWarehouseList` | List the shop's warehouses. |
| Get Withdrawals | `getWithdrawals` | List withdrawal/transfer/settlement records. Query page params and types. |
| Mark Package as Shipped (by order) | `markPackageAsShipped` | Register a shipment for an order. POST body. |
| Partial Edit Manufacturer | `partialEditManufacturer` | Partially edit an EU GPSR manufacturer by manufacturer_id. POST body (product compliance v202409). |
| Partial Edit Product | `partialEditProduct` | Partially edit specific fields of a product by product_id. |
| Partial Edit Product v2 | `partialEditProductV2` | Partial Edit Product (TikTok 202509). Side-by-side v2 of the action that stays on 202309. Updates only supplied fields. |
| Partial Edit Responsible Person | `partialEditResponsiblePerson` | Partially edit an EU GPSR responsible person by responsible_person_id. POST body (product compliance v202409). |
| Publish Global Product | `publishGlobalProduct` | Publish a cross-border global product to target local markets by global_product_id. POST body with publish_target markets (product global_products v202309). |
| Read Message | `readMessage` | Mark conversation messages as read by conversation_id (customer_service v202309). |
| Recommend Category | `recommendCategory` | Recommend a category for a product based on title/description. POST body. |
| Recommend Global Categories | `recommendGlobalCategories` | Recommend global categories for a product based on title/description/images. POST body (product global_categories v202309). |
| Recover Products | `recoverProducts` | Recover previously deleted products. Body JSON: {"product_ids":["..."]}. |
| Reject Cancellation | `rejectCancellation` | Reject a buyer cancellation by cancel_id. POST body with reason. |
| Reject Return | `rejectReturn` | Reject a return request by return_id. POST body with reason. |
| Reject Return v2 | `rejectReturnV2` | Reject Return (TikTok 202606). Side-by-side v2 of the action that stays on 202309. WRITE ACTION - rejects a real return request. |
| Remove Activity Products | `removeActivityProducts` | Remove products/SKUs from a promotion activity. DELETE body. |
| Remove Target Collaboration | `removeTargetCollaboration` | End a target collaboration by id (affiliate_seller v202409). DELETE. |
| Search Cancellations | `searchCancellations` | Search cancellation requests. POST body; page params via query. |
| Search Cancellations v2 | `searchCancellationsV2` | Search Cancellations (TikTok 202602). Side-by-side v2 of the action that stays on 202309. |
| Search Combinable Packages | `searchCombinablePackages` | Find packages eligible to be combined. |
| Search Coupons | `searchCoupons` | Search coupons. POST body; page params via query. |
| Search FBT Goods | `searchFbtGoods` | Search FBT goods info (fbt v202409). POST body. |
| Search FBT Goods v2 | `searchFbtGoodsV2` | Search FBT Goods (TikTok 202607). Side-by-side v2 of the action that stays on 202409. |
| Search FBT Inventory | `searchFbtInventory` | Search FBT inventory (fbt v202408). POST body; page params via query. |
| Search FBT Inventory Records | `searchFbtInventoryRecords` | Search FBT inventory movement records (fbt v202410). POST body. |
| Search Global Products | `searchGlobalProducts` | Search/list cross-border global products. POST body filters; page_size/page_token via query (product global_products v202309). |
| Search Global Products v2 | `searchGlobalProductsV2` | Search Global Products (TikTok 202312). Side-by-side v2 of the action that stays on 202309. Seller-level endpoint - no shop_cipher required. |
| Search Inventory | `inventorySearch` | Search inventory across products/SKUs. POST body filters. |
| Search Manufacturers | `searchManufacturers` | Search EU GPSR manufacturers by ID or keyword. POST body; page_size/page_token via query (product compliance v202409). |
| Search Marketplace Creators | `searchMarketplaceCreators` | Find creators on the affiliate marketplace (affiliate_seller v202406). POST body. |
| Search Marketplace Creators v2 | `searchMarketplaceCreatorsV2` | Search Marketplace Creators (TikTok 202608). Side-by-side v2 of the action that stays on 202406. |
| Search Open Collaboration Products | `searchOpenCollaborationProduct` | Search products in affiliate open collaborations (affiliate_seller v202405). POST body. |
| Search Open Collaborations | `searchOpenCollaboration` | Search affiliate open collaborations (affiliate_seller v202409). POST body. |
| Search Open Collaborations v2 | `searchOpenCollaborationV2` | Search Open Collaborations (TikTok 202412). Side-by-side v2 of the action that stays on 202409. |
| Search Orders | `searchOrders` | Search/list orders by status, time range, etc. POST body filters; page_size/page_token via query. |
| Search Orders by External References | `searchOrderByExternalReferences` | Find TikTok orders by external platform order IDs (v202406). POST body. |
| Search Packages | `searchPackages` | Search packages by status/time. POST body; page params via query. |
| Search Products | `searchProducts` | Search/list products in the shop. POST body supports status, seller_skus, etc. page_size/page_token via query. |
| Search Products v2 | `searchProductsV2` | Search Products (TikTok 202502). Side-by-side v2 of the action that stays on 202309. |
| Search Promotion Activities | `searchActivities` | Search promotion activities. POST body; page params via query. |
| Search Responsible Persons | `searchResponsiblePersons` | Search EU GPSR responsible persons by ID or keyword. POST body; page_size/page_token via query (product compliance v202501). |
| Search Returns | `searchReturns` | Search return requests by status/time. POST body; page params via query. |
| Search Returns v2 | `searchReturnsV2` | Search Returns (TikTok 202602). Side-by-side v2 of the action that stays on 202309. Called by the settlement sync on every run. Typed request body replaces the old opaque bodyJson string. |
| Search Seller Affiliate Orders | `searchSellerAffiliateOrders` | Search affiliate-attributed orders (affiliate_seller v202405). POST body. |
| Search Seller Affiliate Orders v2 | `searchSellerAffiliateOrdersV2` | Search Seller Affiliate Orders (TikTok 202410). Side-by-side v2 of the action that stays on 202405. |
| Search Target Collaborations | `searchTargetCollaborations` | Search affiliate target collaborations (affiliate_seller v202409). POST body. |
| Search Target Collaborations v2 | `searchTargetCollaborationsV2` | Search Target Collaborations (TikTok 202508). Side-by-side v2 of the action that stays on 202409. |
| Send Message | `sendMessage` | Send a message in a conversation by conversation_id. POST body (customer_service v202309). |
| Send Message v2 | `sendMessageV2` | Send Message (TikTok 202606). Side-by-side v2 of the action that stays on 202309. Sends a message into a customer service conversation. |
| Ship Package | `shipPackage` | Mark a package as shipped (provide tracking). POST body. |
| Split Orders | `splitOrders` | Split an order into multiple packages. POST body. |
| Uncombine Packages | `uncombinePackages` | Split a combined package back apart. POST body. |
| Update Activity Products | `updateActivityProducts` | Add/update products in a promotion activity. PUT body. |
| Update Agent Settings | `updateAgentSettings` | Update the customer-service agent configuration. PUT body (customer_service v202309). |
| Update Global Inventory | `updateGlobalInventory` | Update warehouse stock for a cross-border global product by global_product_id. Body JSON with global_skus[]/warehouse inventory (product global_products v202309). |
| Update Order Shipping Info | `updateShippingInfo` | Update tracking/carrier on an order. POST body. |
| Update Package Delivery Status | `updatePackageDeliveryStatus` | Mark packages delivered. POST body with delivery info. |
| Update Package Shipping Info | `updatePackageShippingInfo` | Update tracking/carrier on a package. POST body. |
| Update Product Inventory | `updateInventory` | Update SKU stock for a product. Body JSON with skus[]. |
| Update Product Price | `updatePrice` | Update SKU prices for a product. Body JSON with skus[]. |
| Update Promotion Activity | `updateActivity` | Update a promotion activity title/time window by activity_id. PUT body. |
| Update Shop Webhook | `updateShopWebhook` | Create or update a webhook subscription for an event_type to a callback address (event v202309). Body: {"event_type":"ORDER_STATUS_CHANGE","address":"https://..."}. |
| Update Target Collaboration | `updateTargetCollaboration` | Update a target collaboration by id (affiliate_seller v202409). PUT body. |
| Update Target Collaboration v2 | `updateTargetCollaborationV2` | Update Target Collaboration (TikTok 202508). Side-by-side v2 of the action that stays on 202409. |
| Upload Buyer Messages Image | `uploadBuyerMessagesImage` | Upload an image to send in buyer messaging. POST body (customer_service v202309). |
| Upload Product File | `uploadProductFile` | Upload a product document/file. Body JSON with base64 data and name. |
| Upload Product Image | `uploadProductImage` | Upload a product image. Body JSON with base64 data or use_case. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Order Status Change (1) | `ORDER_STATUS_UPDATE` | Fired when an order's status changes (e.g. UNPAID, AWAITING_SHIPMENT, IN_TRANSIT, DELIVERED, CANCELLED). Numeric type code 1. |
| Package Update (4) | `PACKAGE_UPDATE` | Fired when a package status changes. Numeric type code 4. |
| Product Status Change (5) | `PRODUCT_STATUS_UPDATE` | Fired when a product's status changes (e.g. ACTIVATE, DEACTIVATED, DELETED, FROZEN). Numeric type code 5. |
| Recipient Address Update (3) | `RECIPIENT_ADDRESS_UPDATE` | Fired when a buyer updates the recipient address on an order. Numeric type code 3. |
| Return Status Change (12) | `RETURN_STATUS_UPDATE` | Fired when a return request status changes. Numeric type code 12. |
| Reverse (Cancellation/Return) Status Change (2) | `REVERSE_ORDER_STATUS_UPDATE` | Fired when a reverse order (cancellation/return) status changes. Numeric type code 2. |
| Seller Deauthorization (6) | `SELLER_DEAUTHORIZATION` | Fired when a seller deauthorizes the app. Numeric type code 6. |
| Upcoming Authorization Expiration (7) | `UPCOMING_AUTHORIZATION_EXPIRATION` | Fired when the app's authorization for a shop is about to expire. Numeric type code 7. |
