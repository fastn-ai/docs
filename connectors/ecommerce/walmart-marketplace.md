---
description: "Walmart Marketplace (US) Seller API — environment-switchable (production or sandbox)."
hidden: true
---

# Walmart Marketplace

<img src="../../.gitbook/assets/connectors/walmart-marketplace.png" alt="Walmart Marketplace logo" width="64">

Walmart Marketplace (US) Seller API — environment-switchable (production or sandbox). Orders, items, prices, inventory (single/multi-node/WFS), feeds, reports, reconciliation, returns, refunds, rules/repricer, insights, fulfillment/WFS, and webhook management. OAuth2 client_credentials; Default host is PRODUCTION (marketplace.walmartapis.com).

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [walmart.com](https://walmart.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Slug** | `walmartMarketplace` |

## Use it

Add Walmart Marketplace from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.walmartMarketplace.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Acknowledge Order | `acknowledgeOrder` |  |
| Acknowledge Order (Dynamic Sandbox) | `dynSandboxAcknowledgeOrder` | Acknowledge Order (Dynamic Sandbox) Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Activate Rule | `activateRule` |  |
| Approve Return | `approveReturn` |  |
| Assign Items To Default Incentive Strategy | `assignRepricerIncentive` |  |
| Assign Items To Repricer Strategy | `assignRepricerFeed` |  |
| Associate 3PL Ship Node | `associate3plShipNode` |  |
| Available Recon Files | `availableReconFiles` |  |
| Cancel Customer Return Order | `cancelCustomerReturnOrder` | Cancel a return order created by the seller for the Walmart Multichannel Solutions (MCF) flow. |
| Cancel Order Lines | `cancelOrderLines` |  |

<details>

<summary>See 205 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Order Lines (Dynamic Sandbox) | `dynSandboxCancelOrderLines` | Cancel Order Lines (Dynamic Sandbox) Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| CAP Program Reference | `capProgramReference` |  |
| Catalog Search | `catalogSearch` |  |
| Change Assortment Type | `changeAssortmentType` |  |
| Create Account Shipping Settings | `createAccountShippingSettings` | Create account-level shipping settings (carrier weekend calendar and day-off overrides) for the seller account. |
| Create Customer Return Order | `createCustomerReturnOrder` | Create a return order by the seller for the Walmart Multichannel Solutions (MCF) flow. |
| Create MCS Sales Channel Details | `createMcsSalesChannelDetails` | Multichannel Solutions (MCS): register a new external sales channel (e.g. Amazon, eBay) with its return address so WFS can fulfil orders from it. |
| Create Override Exceptions | `createOverrideExceptions` |  |
| Create Report Request | `createReportRequest` |  |
| Create Repricer Strategy | `createRepricerStrategy` |  |
| Create Rule | `createItemRule` |  |
| Create Ship Node | `createShipNode` |  |
| Create Ship Node (Dynamic Sandbox) | `dynSandboxCreateShipNode` | Create Ship Node (Dynamic Sandbox) Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Create Shipping Label | `createShippingLabel` |  |
| Create Shipping Template | `createShippingTemplate` |  |
| Create Simplified Shipping Settings | `createSimplifiedShippingSettings` | Create the account-level Simplified Shipping Settings configuration. |
| Create Test Items (Dynamic Sandbox Simulation) | `dynSandboxCreateTestItems` | Simulation API: create up to 25 test items in the dynamic sandbox (POST /v1/simulations/items). Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Create Test Order (Dynamic Sandbox Simulation) | `dynSandboxCreateTestOrder` | Simulation API: place a customer test order, multi-line supported (POST /v1/simulations/orders). Limit 5 per hour, 25 per sandbox reset. Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Create Webhook Subscription | `createWebhookSubscription` |  |
| Delete Exceptions | `deleteExceptions` |  |
| Delete Repricer Strategy | `deleteRepricerStrategy` |  |
| Delete Rule | `deleteRule` |  |
| Delete Shipping Template | `deleteShippingTemplate` |  |
| Delete Webhook Subscription | `deleteWebhookSubscription` |  |
| Deliver Order Lines (Dynamic Sandbox Simulation) | `dynSandboxDeliverOrderLines` | Simulation API: carrier delivers shipped order lines (POST /v1/simulations/orders/{purchaseOrderId}/deliver). Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Discard Shipping Label | `discardShippingLabel` |  |
| Download Commercial Invoice | `downloadCommercialInvoice` |  |
| Download Exceptions | `downloadExceptions` |  |
| Download Report | `downloadReport` |  |
| Download Shipping Label | `downloadShippingLabel` |  |
| Download Simulation Result | `downloadSimulationResult` |  |
| Get 3PL Providers | `get3plProviders` |  |
| Get Access Token | `getAccessToken` | Obtain access tokens for API authentication using OAuth 2.0 by providing Client ID and Client Secret. |
| Get Account Shipping Settings | `getAccountShippingSettings` | The Get account level settings API retrieves account-level shipping settings such as calendar day configurations, weekends, and additional days off. |
| Get All Areas | `getAllAreas` |  |
| Get All Departments | `getTaxonomyDepartments` |  |
| Get All Exceptions | `getAllExceptions` |  |
| Get All Feed Statuses | `getAllFeedStatuses` |  |
| Get All Items | `getAllItems` |  |
| Get All Orders | `getAllOrders` |  |
| Get All Orders (Dynamic Sandbox) | `dynSandboxGetAllOrders` | Get All Orders (Dynamic Sandbox) Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Get All Released Orders | `getAllReleasedOrders` |  |
| Get All Report Requests | `getAllReportRequests` |  |
| Get All Rules | `getAllRules` |  |
| Get All Sub-categories | `getAllSubCategories` |  |
| Get API Status | `getApiStatus` |  |
| Get Assortment Recommendation Trends | `getAssortmentRecommendationTrends` | Fetch monthly and weekly trends for demand and price for assortment recommendations. |
| Get Assortment Recommendation Variants | `getAssortmentRecommendationVariants` | Fetch variant items corresponding to a recommended primary variant item. |
| Get Assortment Recommendations | `getAssortmentRecommendations` |  |
| Get Cancellations Summary | `getCancellationsSummary` | Returns Cancellations metrics, such as the percentage of orders cancelled. |
| Get Cancelled Orders Report | `getCancellationsOrdersReport` | Returns the xlsx report of all orders impacting Cancellations metrics. |
| Get Carrier Method Accuracy Report | `getSssCmaReport` | Returns the xlsx report of all orders impacting Simplified Shipping Settings Metrics - Carrier Method Accuracy. |
| Get Carrier Method Accuracy Summary | `getSssCmaSummary` | Returns Carrier Method Accuracy from Simplified Shipping Settings Metrics. |
| Get Carrier Methods | `getCarrierMethods` |  |
| Get Carrier Package Types | `getCarrierPackageTypes` |  |
| Get Categories By Department | `getTaxonomyCategories` |  |
| Get Customer Return Orders Status | `getCustomerReturnOrdersStatus` | Multichannel Solutions (MCS): list customer return orders created for WFS items with their status. Filter by order date range; paginate with limit/offset. |
| Get Dispute Status | `getDisputeStatus` | Retrieve the status of up to 100 disputed (duplicate) items at a time. productIdType accepts WPID, GTIN, UPC, EAN or SKU. |
| Get Feed Error Report | `getFeedErrorReport` | Downloads an error report for a submitted feed as a zipped CSV file, which contains item level detailed error messages. |
| Get Feed Status | `getFeedStatus` |  |
| Get GTIN Exemption Status | `getGtinExemptionStatus` | Items / WFS setup: list GTIN exemption requests and their status (approved, denied, processing, needs info, closed). |
| Get Inventory | `getInventory` |  |
| Get Inventory (Dynamic Sandbox) | `dynSandboxGetInventory` | GET /v3/inventory?sku=: read the inventory of one SKU (non-WFS). Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox. Use with a sandbox connection. |
| Get Item | `getItem` |  |
| Get Item Associations | `getItemAssociations` |  |
| Get Item Count | `getItemCount` |  |
| Get Item Groups Count | `getItemGroupsCount` |  |
| Get Item Spec | `getItemSpec` |  |
| Get Labels For Purchase Order | `getLabelsForPurchaseOrder` |  |
| Get Lag Time | `getLagTime` |  |
| Get Listing Quality Count | `getListingQualityCount` |  |
| Get Listing Quality Items | `getListingQualityItems` |  |
| Get Listing Quality Score | `getListingQualityScore` |  |
| Get MCS Sales Channel Details | `getMcsSalesChannelDetails` | Multichannel Solutions (MCS): list the sales channels already registered for a seller, including orderChannelId, channel name, return address and status. |
| Get Multi-Node Inventory | `getMultiNodeInventory` |  |
| Get Multi-Node Inventory All | `getMultiNodeInventoryAll` |  |
| Get On Time Delivery Orders Report | `getOtdOrdersReport` | Returns the xlsx report of all orders impacting On Time Delivery metrics. |
| Get On Time Delivery Summary | `getOtdSummary` | Returns On Time Delivery metrics, such as orders shipped on expected delivery time versus not shipped on EDT. |
| Get On Time Shipment Rate Report | `getSssOtsReport` | Returns the xlsx report of all orders impacting Simplified Shipping Settings Metrics - On-time Shipment rate. |
| Get On Time Shipment Rate Summary | `getSssOtsSummary` | Returns On-time Shipment rates from Simplified Shipping Settings Metrics. |
| Get Order | `getOrder` |  |
| Get Order (Dynamic Sandbox) | `dynSandboxGetOrder` | Get Order (Dynamic Sandbox) Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Get Partner Profile | `getPartnerProfile` |  |
| Get Payment Statement Report | `getPaymentStatement` |  |
| Get Pro Seller Badge | `getProSellerBadge` |  |
| Get Recommendation Categorization Counts | `getRecommendationCategorizationCounts` |  |
| Get Recon Report JSON | `getReconReportJson` |  |
| Get Refund Performance Summary | `getRefundsSummary` | Returns refunds metrics for orders which were returned. |
| Get Refunded Orders Report | `getRefundsOrdersReport` | Returns the xlsx report of all orders impacting Refunds metrics. |
| Get Report Legacy | `getReportLegacy` |  |
| Get Report Request Status | `getReportRequestStatus` |  |
| Get Returns | `getReturns` |  |
| Get Returns (Dynamic Sandbox) | `dynSandboxGetReturns` | Get Returns (Dynamic Sandbox) Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Get Reviews Accelerator Categories | `getReviewsAcceleratorCategories` |  |
| Get Reviews Accelerator Items | `getReviewsAcceleratorItems` |  |
| Get Rule | `getRule` |  |
| Get Seller Performance Report | `getSellerPerformanceReport` |  |
| Get Seller Response Rate Orders Report | `getSrrOrdersReport` | Returns the xlsx report of all orders impacting Seller Response Rate metrics. |
| Get Seller Response Rate Summary | `getSrrSummary` | Returns Seller Response Rate metrics, such as the percentage of customer inquiries responded to within 48 hours of receipt. |
| Get Ship From Location Accuracy Report | `getSssSflaReport` | Returns the xlsx report of all orders impacting Simplified Shipping Settings Metrics - Ship-from location accuracy. |
| Get Ship From Location Accuracy Summary | `getSssSflaSummary` | Returns Ship-from Location accuracies from Simplified Shipping Settings Metrics. |
| Get Ship Nodes | `getShipNodes` |  |
| Get Ship Nodes (Dynamic Sandbox) | `dynSandboxGetShipNodes` | Get Ship Nodes (Dynamic Sandbox) Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Get Ship Nodes Coverage | `getShipNodesCoverage` |  |
| Get Shipping Estimate | `getShippingEstimate` |  |
| Get Shipping Profile | `getShippingProfile` |  |
| Get Shipping Template Activation Status | `getShippingTemplateActivationStatus` |  |
| Get Shipping Template Details | `getShippingTemplate` |  |
| Get Shipping Templates | `getShippingTemplates` |  |
| Get Simplified Shipping Settings | `getSimplifiedShippingSettings` | Fetch the Simplified Shipping Settings for a seller account and its fulfillment-center-level configurations. |
| Get Simulation Count | `getSimulationCount` |  |
| Get Supported Carriers | `getSupportedCarriers` |  |
| Get Taxonomy | `getTaxonomy` |  |
| Get Taxonomy | `getUtilitiesTaxonomy` |  |
| Get Test Items (Dynamic Sandbox Simulation) | `dynSandboxGetTestItems` | Simulation API: list dynamic sandbox test items (GET /v1/simulations/items). Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Get Token Detail | `getTokenDetail` |  |
| Get Trending Items | `getTrendingItems` |  |
| Get Unpublished Counts | `getUnpublishedCounts` |  |
| Get Unpublished Items | `getUnpublishedItems` |  |
| Get Valid Tracking Rate Orders Report | `getVtrOrdersReport` | Returns the xlsx report of all orders impacting Valid Tracking Rate metrics. |
| Get Valid Tracking Rate Summary | `getVtrSummary` | Returns Valid Tracking Rate (VTR) performance metrics, such as the percent of orders with valid tracking information provided. Maps to Full Service use case "Valid Tracking Rate Performance". |
| Get Webhook Subscriptions | `getWebhookSubscriptions` |  |
| Get WFS Inventory | `getWfsInventory` |  |
| Get WFS Inventory (New) | `getWfsInventoryNew` | Get Available-to-Sell inventory for WFS items (GET /v3/wfs/inventory). Replaces the legacy /v3/fulfillment/inventory endpoint, which Walmart is retiring in 2026. |
| Inactivate Rule | `inactivateRule` |  |
| Initiate Customer Return (Dynamic Sandbox Simulation) | `dynSandboxInitiateReturn` | Simulation API: customer initiates a return for one delivered order line (POST /v3/simulations/returns). Limit 10 per hour. Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Issue Return Refund | `issueReturnRefund` |  |
| Issue Return Refund (Dynamic Sandbox) | `dynSandboxIssueReturnRefund` | Issue Return Refund (Dynamic Sandbox) Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| List Event Types | `listEventTypes` |  |
| List Promotional Prices For SKU | `listPromotionalPrices` |  |
| List Repricer Incentive Items | `listRepricerIncentive` | List price incentive items (GET /v3/price/incentives): item, price, incentive type/status and expiry for your catalog. |
| List Repricer Strategies | `listRepricerStrategies` |  |
| OAuth Test - Get All Items | `oauthTestGetAllItems` | Use this API endpoint to retrieve all items from a partner’s catalog. |
| Recon File | `reconFile` |  |
| Refund Order Lines | `refundOrderLines` |  |
| Reject Assortment Recommendations | `rejectAssortmentRecommendations` |  |
| Reject Return | `rejectReturn` |  |
| Retire Item | `retireItem` |  |
| Returns Reason Codes | `returnsReasonCodes` |  |
| Search Catalog | `searchCatalog` |  |
| Ship Order Lines | `shipOrderLines` |  |
| Ship Order Lines (Dynamic Sandbox) | `dynSandboxShipOrderLines` | Ship Order Lines (Dynamic Sandbox) Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Sim Create Item | `simCreateItem` |  |
| Sim Create Order | `simCreateOrder` |  |
| Sim Deliver Order | `simDeliverOrder` |  |
| Sim Get Item | `simGetItem` | Gets one test item by SKU from the Walmart Marketplace dynamic sandbox. |
| Sim Get Items | `simGetItems` |  |
| Sim Update Item | `simUpdateItem` |  |
| Simulate Initiate Return | `simInitiateReturn` |  |
| Simulate Update Return | `simUpdateReturn` |  |
| Submit Dispute | `submitDispute` | Submit a dispute (contest) for up to 100 duplicate items at a time. Returns an itemResponse array with status ACKNOWLEDGED. |
| Submit Feed | `submitFeed` |  |
| Submit Feed File | `submitFeedFile` | Upload a bulk feed file to Walmart (items, inventory, price, promotions, maintenance) as multipart/form-data. Pass the feed document text in content (JSON or XML) and its contentType. Returns the feedId; track it with Get Feed Status. |
| Test Notification | `testNotification` |  |
| Update Account Shipping Settings | `updateAccountShippingSettings` |  |
| Update Customer Return (Dynamic Sandbox Simulation) | `dynSandboxUpdateReturn` | Simulation API: move a return to in-transit or delivered at the return center (PUT /v3/simulations/returns). Limit 10 per hour. Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Use with a sandbox connection. |
| Update FC Level Simplified Shipping Settings | `updateFcSimplifiedShippingSettings` | Override Simplified Shipping Settings configuration at one or more fulfillment centers. |
| Update Inventory | `updateInventory` |  |
| Update Inventory (Dynamic Sandbox) | `dynSandboxUpdateInventory` | PUT /v3/inventory?sku=: set the inventory of one SKU (non-WFS). Dynamic sandbox only: sends WM_SANDBOX: v2 so Walmart routes the call to the Marketplace dynamic sandbox (stateful test data). Listed in Walmart's Dynamic sandbox guide under Inventory. Use with a sandbox connection. A test order needs stock on the test SKU first. |
| Update Item Inventory Per Ship Node (Dynamic Sandbox) | `dynSandboxUpdateInventoryPerShipNode` | PUT /v3/inventory?sku={sku}&shipNode={shipNode}: set the inventory of one SKU at one ship node, with the values passed in the query string and a body of sku and quantity. Dynamic sandbox only: sends WM_SANDBOX: v2. Use with a sandbox connection. |
| Update MCS Sales Channel Details | `updateMcsSalesChannelDetails` | Multichannel Solutions (MCS): update an existing sales channel (name, return address, active flag, carrier preference) by orderChannelId. |
| Update Multi-Node Inventory | `updateMultiNodeInventory` |  |
| Update Price | `updatePrice` |  |
| Update Promotional Price | `updatePromotionalPrice` |  |
| Update Repricer Feed | `updateRepricerFeed` | Assign or unassign items to a repricer strategy with a repricer feed (POST /v3/repricerFeeds). Returns a feedId. |
| Update Repricer Strategy | `updateRepricerStrategy` |  |
| Update Reviews Accelerator Item Status | `updateReviewsAcceleratorItemStatus` |  |
| Update Rule | `updateRule` |  |
| Update Ship Node | `updateShipNode` |  |
| Update Shipping Area to Rule | `updateShippingAreaToRule` |  |
| Update Shipping Template | `updateShippingTemplate` |  |
| Update Simplified Shipping Settings | `updateSimplifiedShippingSettings` | Update the account-level Simplified Shipping Settings configuration. |
| Update Webhook Subscription | `updateWebhookSubscription` |  |
| WFS Cancel Booking | `wfsCancelBooking` | WFS Preferred Carriers: cancel a booking (within 24h for parcel, 1h for LTL/FTL after accepting the charges). |
| WFS Cancel Inbound Shipment | `wfsCancelInboundShipment` |  |
| WFS Cancel MCF Order | `wfsCancelMcfOrder` |  |
| WFS Confirm Carrier Rate Quote | `wfsConfirmCarrierRateQuote` |  |
| WFS Create Booking | `wfsCreateBooking` | WFS Preferred Carriers: accept a carrier rate quote (Parcel, LTL or FTL) and book the inbound shipment. Accepting a quote commits the seller to the carrier charges. |
| WFS Create Carrier Rate Quotes | `wfsCreateCarrierRateQuotes` |  |
| WFS Create Inbound Shipment | `wfsCreateInboundShipment` |  |
| WFS Create Inbound Shipment Label | `wfsCreateInboundShipmentLabel` |  |
| WFS Create MCF Order | `wfsCreateMcfOrder` |  |
| WFS Download Label | `wfsDownloadLabel` | WFS Preferred Carriers: download the generated labels (PDF, base64 in data). Returns 202 while the label is still being generated. |
| WFS Fetch Order Promise Options | `wfsFetchOrderPromiseOptions` |  |
| WFS Generate Label | `wfsGenerateLabel` | WFS Preferred Carriers: request carrier labels for a booked small-parcel inbound shipment. Then call WFS Download Label. |
| WFS Get Booking | `wfsGetBooking` | WFS Preferred Carriers: get booking details (status, quote, carrier, locations, packages, charges) for an inbound shipment. |
| WFS Get Carrier Rate Quote | `wfsGetCarrierRateQuote` |  |
| WFS Get Fulfillment Orders Status | `wfsGetFulfillmentOrdersStatus` |  |
| WFS Get Inbound Shipment Errors | `wfsGetInboundShipmentErrors` |  |
| WFS Get Inbound Shipment Items | `wfsGetInboundShipmentItems` |  |
| WFS Get Inbound Shipment Label | `wfsGetInboundShipmentLabel` |  |
| WFS Get Inbound Shipment Tracking | `wfsGetInboundShipmentTracking` | WFS Preferred Carriers: tracking numbers, carrier and status of inbound shipments for Parcel, LTL or FTL. |
| WFS Get Inbound Shipments | `wfsGetInboundShipments` |  |
| WFS Get Inventory Health Report | `wfsGetInventoryHealthReport` |  |
| WFS Get Inventory Log | `wfsGetInventoryLog` |  |
| WFS Get Inventory Reconciliation Report | `wfsGetInventoryReconciliationReport` | WFS: download the monthly inventory reconciliation report (CSV) for all WFS items or one GTIN. |
| WFS Get Pickup Schedule | `wfsGetPickupSchedule` | WFS Preferred Carriers: scheduled carrier pickup for a booked LTL shipment (confirmation number, date, ready/close time, status). |
| WFS Inbound Shipment Preview | `wfsInboundPreview` |  |
| WFS Print Bill Of Lading | `wfsPrintBillOfLading` | WFS Preferred Carriers: download the Bill of Lading (PDF, base64 in data) for a booked LTL/FTL inbound shipment. |
| WFS Print Carrier Label | `wfsPrintCarrierLabel` |  |
| WFS Search On-Hold Items | `wfsSearchOnHoldItems` |  |
| WFS Update Pickup Schedule | `wfsUpdatePickupSchedule` | WFS Preferred Carriers: reschedule a confirmed LTL carrier pickup (new date/time window, location or contact). |
| WFS Update Shipment Quantities | `wfsUpdateShipmentQuantities` |  |
| WFS Update Shipment Tracking | `wfsUpdateShipmentTracking` |  |
| WFS Void Carrier Rate Quote | `wfsVoidCarrierRateQuote` |  |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Buy Box Changed | `BUY_BOX_CHANGED` | The buy box for an item changed (PRICE resource). |
| Offer Unpublished | `OFFER_UNPUBLISHED` | An item offer was unpublished (ITEM resource). |
| PO Line Auto-Cancelled | `PO_LINE_AUTOCANCELLED` | A purchase order line was auto-cancelled (ORDER resource). |
| Purchase Order Created | `PO_CREATED` | A new purchase order was created (ORDER resource). |
| Report Status | `REPORT_STATUS` | A report request changed status (REPORTS resource). |
