---
description: "Google Merchant Center connector for the Content API for Shopping v2.1 — manage products, product statuses, inventory, orders, accounts, tax, shipping…"
hidden: true
---

# Google Merchant Center

<img src="../../.gitbook/assets/connectors/lg/google-merchant-center.png" alt="Google Merchant Center logo">

Google Merchant Center connector for the Content API for Shopping v2.1 — manage products, product statuses, inventory, orders, accounts, tax, shipping settings, datafeeds, POS, reports, return policies, regions, and promotions.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [shoppingcontent.googleapis.com](https://shoppingcontent.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleMerchantCenter` |

## Use it

Add Google Merchant Center from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleMerchantCenter.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Acknowledge Order | `acknowledgeOrder` | Marks an order as acknowledged. |
| Acknowledge Order Return | `acknowledgeOrderReturn` | Acks an order return in the specified Merchant Center account. |
| Advance Test Order | `advanceTestOrder` | Sandbox only. Moves a test order from the "inProgress" state to the "pendingShipment" state. |
| Batch Account Statuses | `custombatchAccountStatuses` | Retrieves multiple Merchant Center account statuses in a single request. |
| Batch Account Tax | `custombatchAccountTax` | Retrieves and updates tax settings of multiple accounts in a single request. |
| Batch Accounts | `custombatchAccounts` | Retrieves, inserts, updates, links, claims, and deletes multiple Merchant Center (sub-)accounts in a single request. |
| Batch Datafeed Statuses | `custombatchDatafeedStatuses` | Gets multiple Merchant Center datafeed statuses in a single request. |
| Batch Datafeeds | `custombatchDatafeeds` | Deletes, fetches, gets, inserts, and updates multiple datafeeds in a single request. |
| Batch LIA Settings | `custombatchLiaSettings` | Retrieves and/or updates the LIA settings of multiple accounts in a single request. |
| Batch Local Inventory | `custombatchLocalInventory` | Updates local inventory for multiple products or stores in a single request. |
| Batch POS | `custombatchPos` | Batches multiple POS-related calls in a single request. |
| Batch Product Statuses | `custombatchProductStatuses` | Gets the statuses of multiple products in a single request. |
| Batch Products | `custombatchProducts` | Retrieves, inserts, and deletes multiple products in a single request. |
| Batch Regional Inventory | `custombatchRegionalInventory` | Updates regional inventory for multiple products or regions in a single request. |
| Batch Return Addresses | `custombatchReturnAddresses` | Batches multiple return address related calls in a single request. |
| Batch Return Policies | `custombatchReturnPolicies` | Batches multiple return policy related calls in a single request. |
| Batch Shipping Settings | `custombatchShippingSettings` | Retrieves and updates the shipping settings of multiple accounts in a single request. |
| Cancel Line Item | `cancelLineItem` | Cancels a single line item, or part of it, in an order. |
| Cancel Order | `cancelOrder` | Cancels all line items in an order, making a full refund. |
| Cancel Test Order By Customer | `cancelTestOrderByCustomer` | Sandbox only. Cancels a test order for customer-initiated cancellation. |
| Capture Order | `captureOrder` | Captures funds of a manually approved holding order. This method is only available to merchants that use manual approval capture. |
| Claim Website | `claimWebsite` | Claims the website of the specified Merchant Center account. |
| Create Account Credentials | `createAccountCredentials` | Uploads credentials for the specified Merchant Center account. |
| Create Account Label | `createAccountLabel` | Creates a new label, not assigned to any account. |
| Create Charge Invoice | `createChargeInvoice` | Creates a charge invoice for a shipment group, and triggers a charge capture for orderinvoice-enabled orders. |
| Create Collection | `createCollection` | Uploads a collection to your Merchant Center account. If a collection with the same collection ID already exists, this method updates that entry. |
| Create Conversion Source | `createConversionSource` | Creates a new conversion source. |
| Create Online Return Policy | `createReturnPolicyOnline` | Creates a new return policy for the given Merchant Center account. |
| Create Order Return | `createOrderReturn` | Creates order return in the specified Merchant Center account. |
| Create Order Return Label | `createOrderReturnLabel` | Links a return shipping label to a return id in the specified Merchant Center account. |
| Create Order Tracking Signal | `createOrderTrackingSignal` | Creates new order tracking signal to help improve delivery-time estimates and shipping information for customers. |
| Create Promotion | `createPromotion` | Inserts a promotion for your Merchant Center account. If the promotion already exists, then it updates the promotion instead. |
| Create Refund Invoice | `createRefundInvoice` | Creates a refund invoice for one or more shipment groups, and triggers a refund for orderinvoice-enabled orders. |
| Create Region | `createRegion` | Creates a region definition in your Merchant Center account. |
| Create Return Carrier | `createReturnCarrier` | Links a return carrier to a merchant account. |
| Create Test Order | `createTestOrder` | Sandbox only. Creates a test order. |
| Create Test Return | `createTestReturn` | Sandbox only. Creates a test return. |
| Delete Account | `deleteAccount` | Deletes the specified sub-account from a multi-client Merchant Center account. |
| Delete Account Label | `deleteAccountLabel` | Deletes a label and removes it from all accounts to which it was assigned. |
| Delete Checkout Settings | `deleteCheckoutSettings` | Deletes Checkout settings and unenrolls merchant from Checkout program. |
| Delete Collection | `deleteCollection` | Deletes a collection from your Merchant Center account. |
| Delete Conversion Source | `deleteConversionSource` | Archives an existing conversion source. It will be recoverable for 30 days before being permanently deleted. |
| Delete Datafeed | `deleteDatafeed` | Deletes a datafeed configuration from the specified Merchant Center account. |
| Delete Online Return Policy | `deleteReturnPolicyOnline` | Deletes an existing return policy for the given Merchant Center account. |
| Delete POS Store | `deletePosStore` | Deletes a store for the given merchant. |
| Delete Product | `deleteProduct` | Deletes a product from the specified Merchant Center account. |
| Delete Region | `deleteRegion` | Deletes a region definition from your Merchant Center account. |
| Delete Return Address | `deleteReturnAddress` | Deletes a return address for the Merchant Center account. |
| Delete Return Carrier | `deleteReturnCarrier` | Deletes a return carrier from a merchant account. |
| Delete Return Policy | `deleteReturnPolicy` | Deletes a return policy for the Merchant Center account. |
| Fetch Datafeed Now | `fetchNowDatafeed` | Fetches a file-input data source immediately (Merchant API datasources_v1 dataSources.fetch; replaces datafeeds.fetchnow). Returns an empty object on success. |
| Generate Recommendations | `generateRecommendations` | Generates recommendations for a merchant, based on their currently active recommendation types and history. |
| Get Accessible GMB Accounts | `getAccessibleGmbAccounts` | Lists the Google Business Profile accounts available to a Merchant Center account (Merchant API accounts_v1 gbpAccounts.list; replaces liasettings.getaccessiblegmbaccounts). |
| Get Account | `getAccount` | Retrieves a single Merchant Center account by its ID (Merchant API accounts_v1 accounts.get). |
| Get Account Status | `getAccountStatus` | Lists the account-level issues of a Merchant Center account (Merchant API accounts_v1 accounts.issues.list; replaces accountstatuses.get). |
| Get Account Tax | `getAccountTax` | Retrieves the tax settings of the specified Merchant Center account. |
| Get Authenticated User Info | `getAuthinfo` | Returns information about the authenticated user and the Merchant Center account IDs they can access. |
| Get Checkout Settings | `getCheckoutSettings` | Gets the checkout settings of a Merchant Center account (Merchant API accounts_v1 programs.checkoutSettings.getCheckoutSettings, program "checkout"). |
| Get Collection | `getCollection` | Retrieves a collection from your Merchant Center account. |
| Get Collection Status | `getCollectionStatus` | Gets the status of a collection from your Merchant Center account. |
| Get Conversion Source | `getConversionSource` | Fetches a conversion source (Merchant API conversions_v1 conversionSources.get). |
| Get CSS Domain | `getCss` | Retrieves a CSS domain account (CSS API v1 accounts.get; the Content API csses service is deprecated). |
| Get Datafeed | `getDatafeed` | Retrieves a data source configuration (Merchant API datasources_v1 dataSources.get; replaces datafeeds.get). |
| Get Datafeed Status | `getDatafeedStatus` | Retrieves the status of a datafeed from the specified Merchant Center account. |
| Get Free Listings Program | `getFreeListingsProgram` | Retrieves the status and review eligibility for the free listing program. Returns errors and warnings if they require action to resolve, will become disapprovals, or impact impressions. |
| Get LIA Settings | `getLiaSettings` | Retrieves the LIA settings of the specified Merchant Center account. |
| Get Online Return Policy | `getReturnPolicyOnline` | Gets an existing return policy for the given Merchant Center account. |
| Get Order | `getOrder` | Retrieves a single order from the specified Merchant Center account. |
| Get Order By Merchant Order ID | `getOrderByMerchantOrderId` | Retrieves an order using the merchant-provided order ID rather than the Google-assigned ID. |
| Get Order Return | `getOrderReturn` | Retrieves an order return from the specified Merchant Center account. |
| Get POS Store | `getPosStore` | Retrieves information about the given store. |
| Get Product | `getProduct` | Retrieves a single product from the specified Merchant Center account. |
| Get Product Status | `getProductStatus` | Gets the status of a single product from the specified Merchant Center account. |
| Get Promotion | `getPromotion` | Retrieves a promotion from your Merchant Center account. |
| Get Pubsub Notification Settings | `getPubsubNotificationSettings` | Retrieves a Merchant Center account's Pub/Sub notification settings. |
| Get Region | `getRegion` | Retrieves a region defined in your Merchant Center account. |
| Get Return Address | `getReturnAddress` | Gets a return address of the Merchant Center account. |
| Get Return Policy | `getReturnPolicy` | Gets a return policy of the Merchant Center account. |
| Get Shipping Settings | `getShippingSettings` | Retrieves the shipping settings of the specified Merchant Center account. |
| Get Shopping Ads Program | `getShoppingAdsProgram` | Retrieves the status and review eligibility for the Shopping Ads program. Returns errors and warnings if they require action to resolve, will become disapprovals, or impact impressions. |
| Get Supported Carriers | `getSupportedCarriers` | Retrieves supported carriers and carrier services for the specified Merchant Center account. |
| Get Supported Holidays | `getSupportedHolidays` | Retrieves supported holidays for the specified Merchant Center account. |
| Get Supported Pickup Services | `getSupportedPickupServices` | Retrieves supported pickup services for the specified Merchant Center account. |
| Get Test Order Template | `getTestOrderTemplate` | Sandbox only. Retrieves an order template that can be used to quickly create a new order in sandbox. |
| In-store Refund Line Item | `inStoreRefundLineItem` | Deprecated. Issues a partial or total refund for a line item in an order that was returned in-store. |
| Insert Account | `insertAccount` | Creates a new sub-account under the specified multi-client Merchant Center account. |
| Insert Checkout Settings | `insertCheckoutSettings` | Enrolls merchant in Checkout settings program. After a merchant has been enrolled, checkout URL and cart URL will be returned in their products. |
| Insert Datafeed | `insertDatafeed` | Registers a new datafeed configuration with the specified Merchant Center account. |
| Insert Local Inventory | `insertLocalInventory` | Updates the local inventory of a product in the specified Merchant Center account for a specific store. |
| Insert POS Store | `insertPosStore` | Creates a store for the given merchant. |
| Insert Product | `insertProduct` | Uploads a product to the specified Merchant Center account. If an item with the same channel, contentLanguage, offerId, and targetCountry already exists, it is replaced. |
| Insert Regional Inventory | `insertRegionalInventory` | Updates the regional inventory of a product in the specified Merchant Center account for a specific region. |
| Insert Return Address | `insertReturnAddress` | Inserts a return address for the Merchant Center account. |
| Insert Return Policy | `insertReturnPolicy` | Inserts a return policy for the Merchant Center account. |
| Link Account | `linkAccount` | Performs an action on a link between a Merchant Center account and another account, such as an Ads account. |
| List Account Labels | `listAccountLabelsResource` | Lists the labels assigned to an account. |
| List Account Links | `listAccountLinks` | Returns the list of accounts linked to the specified Merchant Center account. |
| List Account Statuses | `listAccountStatuses` | Lists the statuses of the sub-accounts in the specified multi-client Merchant Center account. |
| List Account Tax | `listAccountTax` | Lists the tax settings of the sub-accounts in the specified multi-client Merchant Center account. |
| List Accounts | `listAccounts` | Lists the sub-accounts in the specified multi-client Merchant Center account. |
| List Collection Statuses | `listCollectionStatuses` | Lists the statuses of the collections in the specified Merchant Center account. |
| List Collections | `listCollections` | Lists the collections in the specified Merchant Center account. |
| List Conversion Sources | `listConversionSources` | Retrieves the list of conversion sources the caller has access to. |
| List CSS Domains | `listCsses` | Lists CSS domains affiliated with a CSS group. |
| List Datafeed Statuses | `listDatafeedStatuses` | Lists the statuses of the datafeeds in the specified Merchant Center account. |
| List Datafeeds | `listDatafeeds` | Lists the configurations for datafeeds in the specified Merchant Center account. |
| List LIA Settings | `listLiaSettings` | Lists the LIA settings of the sub-accounts in the specified multi-client Merchant Center account. |
| List Online Return Policies | `listReturnPolicyOnline` | Lists the online return policies of a Merchant Center account (Merchant API accounts_v1 onlineReturnPolicies.list). |
| List Order Disbursements | `listOrderDisbursements` | Retrieves a report for disbursements from an account. |
| List Order Returns | `listOrderReturns` | Lists order returns in the specified Merchant Center account. |
| List Order Transactions | `listOrderTransactions` | Retrieves a list of transactions for a disbursement from an account. |
| List Orders | `listOrders` | Lists the orders in the specified Merchant Center account. |
| List POS Data Providers | `listPosDataProviders` | Retrieves the list of POS data providers that have active settings for the all eiligible countries. |
| List POS Stores | `listPosStores` | Lists the stores of a target merchant (Merchant API lfp_v1 lfpStores.list; replaces pos.list). |
| List Product Statuses | `listProductStatuses` | Lists the statuses of the products in the specified Merchant Center account. |
| List Products | `listProducts` | Lists the processed products in a Merchant Center account (Merchant API products_v1 products.list). |
| List Promotions | `listPromotions` | Lists the promotions in a Merchant Center account (Merchant API promotions_v1 promotions.list). |
| List Quota Groups | `listQuotaGroups` | Lists the daily call quota and usage per group (Merchant API quota_v1 quotas.list). |
| List Regions | `listRegions` | Lists the regions in a Merchant Center account (Merchant API accounts_v1 regions.list). |
| List Return Addresses | `listReturnAddresses` | Lists the return addresses of the Merchant Center account. |
| List Return Carriers | `listReturnCarriers` | Lists the shipping return carriers linked to a merchant account. |
| List Return Policies | `listReturnPolicies` | Lists the return policies of the Merchant Center account. |
| List Shipping Settings | `listShippingSettings` | Lists the shipping settings of the sub-accounts in the specified multi-client Merchant Center account. |
| Process Order Return | `processOrderReturn` | Processes return in the specified Merchant Center account. |
| Refund Item | `refundItem` | Issues a partial or total refund for items and shipment of an order. |
| Refund Order | `refundOrder` | Issues a partial or total refund for an order. |
| Reject Return Line Item | `rejectReturnLineItem` | Rejects the return of a line item in an order. |
| Render Account Issues | `renderAccountIssues` | Provide a list of merchant's issues with a support content and available actions. This content and available actions are meant to be rendered and shown in third-party applications. |
| Render Product Issues | `renderProductIssues` | Provide a list of issues for a merchant's product with a support content and available actions. This content and available actions are meant to be rendered and shown in third-party applications. |
| Report Recommendation Interaction | `reportRecommendationInteraction` | Reports an interaction on a recommendation for a merchant. |
| Request Free Listings Review | `requestFreeListingsReview` | Requests a review of free listings in a specific region. This method deprecated as of the new Products submission API. |
| Request GMB Access | `requestGmbAccess` | Requests access to a specified Google My Business (Business Profile) account. |
| Request Inventory Verification | `requestInventoryVerification` | Requests inventory validation for the specified country. |
| Request Phone Verification | `requestPhoneVerification` | Requests a phone verification code to be sent to the merchant to verify their phone number. |
| Request Shopping Ads Review | `requestShoppingAdsReview` | Requests a review of Shopping ads in a specific region. This method deprecated as of the new Products submission API. |
| Return Refund Line Item | `returnRefundLineItem` | Returns and refunds a line item. Instead of refunding the money, use rejectReturnLineItem to reject a return. |
| Search Reports | `searchReports` | Retrieves merchant performance metrics matching the search query and optionally segmented by selected dimensions, using a Query Language query. |
| Set Inventory Verification Contact | `setInventoryVerificationContact` | Sets the inventory verification contact for the specified country. |
| Set Line Item Metadata | `setLineItemMetadata` | Sets (or overrides if it already exists) merchant-provided annotations in the form of key-value pairs on a line item. |
| Set Omnichannel Experience | `setOmnichannelExperience` | Sets the omnichannel experience for the specified country. |
| Set POS Data Provider | `setPosDataProvider` | Sets the POS data provider for the specified country. |
| Ship Line Items | `shipLineItems` | Marks line item(s) as shipped in an order. |
| Submit POS Inventory | `submitPosInventory` | Submits inventory for the given merchant. |
| Submit POS Sale | `submitPosSale` | Submits a sale event for the given merchant. |
| Trigger Support Action | `triggerSupportAction` | Start an action. The action can be requested by merchants in third-party applications. Before merchants can request the action, the third-party application needs to show them action specific content and display a user input form. |
| Undelete Conversion Source | `undeleteConversionSource` | Re-enables an archived conversion source. |
| Update Account | `updateAccount` | Updates a Merchant Center account. This method supports full resource replacement. |
| Update Account Label | `patchAccountLabel` | Updates an account label (CSS API v1 accounts.labels.patch; replaces Content API accounts.labels.patch). |
| Update Account Labels | `updateAccountLabels` | Updates labels that are assigned to the specified Merchant Center account by the aggregator (multi-client account). |
| Update Account Tax | `updateAccountTax` | Updates the tax settings of the specified Merchant Center account. |
| Update Conversion Source | `patchConversionSource` | Updates a Merchant Center Destination conversion source (Merchant API conversions_v1 conversionSources.patch). |
| Update CSS Domain Labels | `updateCssLabels` | Updates labels that are assigned to a CSS domain by its CSS group. |
| Update Datafeed | `updateDatafeed` | Updates a datafeed configuration of the specified Merchant Center account. This method supports full resource replacement. |
| Update LIA Settings | `updateLiaSettings` | Updates the LIA settings of the specified Merchant Center account. This method supports full resource replacement. |
| Update Line Item Shipping Details | `updateLineItemShippingDetails` | Updates ship-by and delivery-by dates for a line item. |
| Update Merchant Order ID | `updateMerchantOrderId` | Updates the merchant order ID for a given order. |
| Update Online Return Policy | `patchReturnPolicyOnline` | Updates an existing return policy for the given Merchant Center account. |
| Update Product | `updateProduct` | Updates an existing product in the specified Merchant Center account. Only attributes specified in the update mask are updated. |
| Update Pubsub Notification Settings | `updatePubsubNotificationSettings` | Register a Merchant Center account for pubsub notifications. Note that cloud topic name should not be provided as part of the request. |
| Update Region | `patchRegion` | Updates a region definition (Merchant API accounts_v1 regions.patch; requires admin access). |
| Update Return Carrier | `patchReturnCarrier` | Updates a return carrier linked to a merchant account. |
| Update Shipment | `updateShipment` | Updates a shipment's status, carrier, and/or tracking ID for an order. |
| Update Shipping Settings | `updateShippingSettings` | Updates the shipping settings of the specified Merchant Center account. This method supports full resource replacement. |
| Verify Phone Number | `verifyPhoneNumber` | Validates a verification code that was sent to the merchant to verify their phone number. |
