---
description: "Easyship global shipping API (v2024-09)."
---

# Easyship

Easyship global shipping API (v2024-09). Rate shopping across 550+ courier services, shipment and label creation, tracking, pickups, manifests, customs taxes and duties, insurance, address and box management, shipping rules, batches, and webhooks.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [easyship.com](https://easyship.com) |
| **Authentication** | Bearer token |
| **Actions** | 133 |
| **Events** | 0 |
| **Slug** | `easyship` |

## Use it

Add Easyship from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.easyship.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Address | `activateAddress` | Activate an address on the Easyship account by its ID. |
| Activate Asset | `activateAsset` | Activate a branding asset on the Easyship account by its ID. |
| Activate Shipping Rule | `activateShippingRule` | Activates a shipping rule so that it begins applying to matching shipments. |
| Activate Webhook | `activateWebhook` | Activates a webhook so that it begins delivering event notifications to its endpoint. |
| Add Credit | `addCredit` | Add credit to the Easyship account balance using a stored payment source. |
| Calculate Taxes And Duties | `calculateTaxesAndDuties` | Calculates estimated import taxes and duties for a shipment based on origin, destination, and item details. |
| Cancel Insurance Policy | `cancelInsurancePolicy` | Cancels an existing insurance policy by its policy ID. |
| Cancel Pickup | `cancelPickup` | Cancels a previously scheduled courier pickup by its Easyship pickup ID. |
| Cancel Shipment | `cancelShipment` | Cancels an existing shipment by its Easyship shipment ID. |
| Confirm Credit Top-up | `confirmCreditTopup` | Confirm a credit top-up that requires 3D Secure authentication by submitting the payment intent identifier. |
| Confirm Payment Source | `confirmPaymentSource` | Confirm a payment source that requires additional authentication by submitting the payment intent identifier. |
| Create Address | `createAddress` | Create a new address on the Easyship account, optionally marking it as the default for pickup, billing, sender, or return. |
| Create App Access | `createAppAccess` | Create an app access link that grants entry to a specific Easyship application flow such as onboarding. |
| Create Batch Of Addresses | `createBatchAddresses` | Creates multiple addresses in a single batch request, optionally validating each address. |
| Create Batch Of Labels | `createBatchLabels` | Generates shipping labels for multiple shipments in a single batch request. |
| Create Batch Of Shipments | `createBatchShipments` | Creates multiple shipments in a single batch request, optionally applying shared default settings across all shipments. |
| Create Box | `createBox` | Create a custom packaging box on the Easyship account with the given name, outer dimensions, and weight. |
| Create Courier | `createCourier` | Creates a new courier (link-your-own-courier account) on the Easyship account. |
| Create Insurance Policy | `createInsurancePolicy` | Creates an insurance policy for a shipment using a tracking number, courier, and insurance coverage details. |
| Create Insurance Policy From Quote | `createInsurancePolicyFromQuote` | Creates an insurance policy from a previously generated quote, including policy holder, shipping, and billing details. |
| Create Insurance Quote | `createInsuranceQuote` | Requests an insurance quote for a shipment based on insured value, route, and product details. |
| Create Label | `createLabel` | Purchases a shipping label for a shipment using the selected courier service and printing options. |
| Create Manifest | `createManifest` | Creates an end-of-day manifest for a courier, optionally scoped to specific shipments. |
| Create Payment Source | `createPaymentSource` | Add a new payment source to the Easyship account using a Stripe token. |
| Create Pickup | `createPickup` | Schedules a courier pickup for one or more Easyship shipments on a selected date and time slot. |
| Create Product | `createProduct` | Creates a new product in the Easyship product catalog. |
| Create Redirect | `createRedirect` | Create a redirect link that sends the user to a specific Easyship dashboard target. |
| Create Return Shipment | `createReturnShipment` | Creates a return shipment for an existing shipment, reversing origin and destination. |
| Create Shipment | `createShipment` | Creates a new shipment with origin, destination, parcels, and optional courier and shipping settings. |
| Create Shipping Rule | `createShippingRule` | Creates a new shipping rule with conditions and actions that automatically apply courier preferences to matching shipments. |
| Create Shipping Rule Action | `createShippingRuleAction` | Adds a new action to a shipping rule that is applied to shipments matching the rule conditions. |
| Create Shipping Rule Condition | `createShippingRuleCondition` | Adds a new condition to a shipping rule that determines when the rule applies. |
| Create Tag | `createTag` | Creates a new tag on the Easyship account. |
| Create Tracking | `createTracking` | Creates a standalone tracking record for a shipment using a tracking number and optional courier, address, and item details. |
| Create Webhook | `createWebhook` | Creates a new webhook that delivers event notifications to the specified HTTPS endpoint for the selected event types. |
| Deactivate Address | `deactivateAddress` | Deactivate an address on the Easyship account by its ID. |
| Deactivate Asset | `deactivateAsset` | Deactivate a branding asset on the Easyship account by its ID. |
| Deactivate Shipping Rule | `deactivateShippingRule` | Deactivates a shipping rule so that it stops applying to matching shipments. |
| Deactivate Webhook | `deactivateWebhook` | Deactivates a webhook so that it stops delivering event notifications to its endpoint. |
| Delete Asset | `deleteAsset` | Delete a branding asset from the Easyship account by its ID. |
| Delete Box | `deleteBox` | Delete a packaging box from the Easyship account by its ID. |
| Delete Courier | `deleteCourier` | Deletes an existing courier by its identifier. |
| Delete Payment Source | `deletePaymentSource` | Delete a payment source from the Easyship account by its ID. |
| Delete Product | `deleteProduct` | Deletes a product from the Easyship product catalog by its identifier. |
| Delete Shipment | `deleteShipment` | Deletes a shipment by its Easyship shipment ID. |
| Delete Shipping Rule | `deleteShippingRule` | Deletes an existing shipping rule by its unique identifier. |
| Delete Shipping Rule Action | `deleteShippingRuleAction` | Deletes an action from a shipping rule by its unique identifier. |
| Delete Shipping Rule Condition | `deleteShippingRuleCondition` | Deletes a condition from a shipping rule by its unique identifier. |
| Delete Tracking | `deleteTracking` | Deletes a standalone tracking record by its tracking ID. |
| Delete Webhook | `deleteWebhook` | Deletes an existing webhook by its unique identifier so it stops receiving event notifications. |
| Download Billing Document | `downloadBillingDocument` | Retrieves a downloadable link or content for a specific billing document by its ID. |
| Get Account | `getAccount` | Retrieve the details of the authenticated Easyship account, including billing address, credit balance, company ID, and payment sources. |
| Get Auto Recharge Settings | `getAutoRecharge` | Retrieve the automatic credit recharge settings configured for the Easyship account. |
| Get Batch | `getBatch` | Retrieves the details and status of a single batch job by its batch ID. |
| Get Courier | `getCourier` | Retrieves the details of a single courier by its identifier. |
| Get Credit | `getCredit` | Retrieve the current credit balance for the Easyship account. |
| Get Manifest | `getManifest` | Retrieves the details of a single manifest by its manifest ID. |
| Get Pickup | `getPickup` | Retrieves the details of a single scheduled pickup by its Easyship pickup ID. |
| Get Sales Channels Analytics | `getSalesChannelsAnalytics` | Returns analytics on shipment volume broken down by sales channel over a date range. |
| Get Shipment | `getShipment` | Retrieves the details of a single shipment by its Easyship shipment ID. |
| Get Shipment Status Analytics | `getShipmentStatusAnalytics` | Returns analytics on shipments grouped by their delivery status over a date range. |
| Get Shipments Analytics | `getShipmentsAnalytics` | Returns aggregate shipment analytics over a date range. |
| Get Shipments Shipped Analytics | `getShipmentsShippedAnalytics` | Returns analytics on the number of shipments shipped over a date range. |
| Get Shipping Rule | `getShippingRule` | Retrieves the details of a single shipping rule by its unique identifier. |
| Get Stripe Public Key | `getStripeKey` | Retrieve the Stripe publishable key used to tokenize payment methods for the Easyship account. |
| Get Top Couriers Analytics | `getTopCouriersAnalytics` | Returns analytics on the top couriers used by shipment volume over a date range. |
| Get Top Destinations Analytics | `getTopDestinationsAnalytics` | Returns analytics on the top shipment destinations by volume over a date range. |
| Get Tracking | `getTracking` | Retrieves the details and checkpoints of a single tracking record by its tracking ID. |
| Get Webhook | `getWebhook` | Retrieves the details of a single webhook by its unique identifier. |
| Insure Shipment | `insureShipment` | Adds insurance coverage to an existing shipment for the specified amount and currency. |
| List Account Settings | `listAccountSettings` | Retrieve the settings configured for the authenticated Easyship account, including tracking email and tracking page configuration. |
| List Addresses | `listAddresses` | Retrieve the list of addresses stored on the Easyship account, such as sender, pickup, billing, and return addresses. |
| List Assets | `listAssets` | Retrieve the list of branding assets configured on the Easyship account. |
| List Batch Items | `listBatchItems` | Returns the individual items and their processing results for a specific batch job. |
| List Batches | `listBatches` | Returns a paginated list of batch jobs for the account. |
| List Billing Document Transactions | `listBillingDocumentTransactions` | Returns the transaction records associated with a specific billing document. |
| List Billing Documents | `listBillingDocuments` | Returns a paginated list of billing documents such as invoices and statements for the account. |
| List Boxes | `listBoxes` | Retrieve the list of packaging boxes configured on the Easyship account, including their dimensions and associated couriers. |
| List Canada Post Locations | `listCanadaPostLocations` | Retrieve nearby Canada Post drop-off locations for a given country. |
| List Countries | `listCountries` | Retrieve the list of countries supported by Easyship, including their ISO alpha-2 codes and names. |
| List Courier Services | `listCourierServices` | Retrieves a paginated list of all courier services available on the Easyship account. |
| List Courier Services Of Courier | `listCourierServicesOfCourier` | Retrieves the courier services available for a specific courier. |
| List Couriers | `listCouriers` | Retrieves a paginated list of couriers configured on the Easyship account. |
| List Estimated Delivery Dates | `listEstimatedDeliveryDates` | Retrieves estimated delivery dates for a courier service between origin and destination countries. |
| List External Courier Services | `listExternalCourierServices` | Returns the list of external courier services available for standalone tracking. |
| List FedEx Locations | `listFedexLocations` | Retrieve nearby FedEx drop-off locations for a given country, city, and postal code. |
| List HS Codes | `listHsCodes` | Retrieve the list of Harmonized System (HS) codes used for customs classification, optionally filtered by a search term. |
| List Insurance Policies | `listInsurancePolicies` | Returns a paginated list of insurance policies for the account. |
| List Item Categories | `listItemCategories` | Retrieve the list of item categories used to classify shipment contents in Easyship. |
| List Linked Own Couriers (LYOC) | `listLyoc` | Retrieves the list of link-your-own-courier (LYOC) accounts connected to the Easyship account. |
| List Manifests | `listManifests` | Returns a paginated list of manifests generated for the account. |
| List Payment Sources | `listPaymentSources` | Retrieve the list of payment sources stored on the Easyship account. |
| List Pickup Shipments | `listPickupShipments` | Returns the shipments associated with a specific scheduled pickup. |
| List Pickup Slots | `listPickupSlots` | Retrieves the available pickup slots for a specific courier service. |
| List Pickups | `listPickups` | Returns a paginated list of scheduled courier pickups for the account. |
| List Products | `listProducts` | Retrieves a paginated list of products in the Easyship product catalog. |
| List Shipment Documents | `listShipmentDocuments` | Retrieves documents (such as label, commercial invoice, or packing slip) associated with a shipment. |
| List Shipment Trackings | `listAllShipmentTrackings` | Retrieves a paginated list of tracking records across all shipments on the account. |
| List Shipment Transaction Records | `listShipmentTransactionRecords` | Retrieves the transaction records (charges and adjustments) for a specific shipment. |
| List Shipments | `listShipments` | Retrieves a paginated list of shipments, optionally filtered by shipment ID, order number, countries, or status. |
| List Shipping Rule Actions | `listShippingRuleActions` | Retrieves all actions configured for a specific shipping rule. |
| List Shipping Rule Conditions | `listShippingRuleConditions` | Retrieves all conditions configured for a specific shipping rule. |
| List Shipping Rule Platforms | `listShippingRulePlatforms` | Retrieves the list of platforms available for use in shipping rule conditions. |
| List Shipping Rules | `listShippingRules` | Retrieves a paginated list of all shipping rules configured on the Easyship account. |
| List States | `listStates` | Retrieve the list of states and provinces supported by Easyship. |
| List Stores | `listStores` | Retrieves a paginated list of stores connected to the Easyship account. |
| List Supported Tracking Couriers | `listSupportedTrackingCouriers` | Returns the list of couriers supported for standalone tracking. |
| List Tags | `listTags` | Retrieves a paginated list of tags available on the Easyship account. |
| List Trackings | `listTrackings` | Returns a paginated list of standalone tracking records for the account. |
| List Transaction Records | `listTransactionRecords` | Returns a paginated list of account transaction records, including charges, credits, and adjustments. |
| List Unavailable Couriers | `listUnavailableCouriers` | Retrieves the couriers that are unavailable for a specific shipment along with the reasons. |
| List UPS Locations | `listUpsLocations` | Retrieve nearby UPS drop-off locations for a given address. |
| List USPS Locations | `listUspsLocations` | Retrieve nearby USPS drop-off locations for a given country and optional address details. |
| List Webhooks | `listWebhooks` | Retrieves a paginated list of all webhooks configured on the Easyship account. |
| Refund Credit | `refundCredit` | Refund a specified amount of credit from the Easyship account balance. |
| Request Rates | `requestRates` | Requests available shipping rates from couriers for a given origin, destination, and set of parcels. |
| Test Webhook | `testWebhook` | Sends a test event of the specified type to a webhook endpoint to verify that it is receiving notifications correctly. |
| Update Account Settings | `updateAccountSettings` | Update the account settings for tracking email and tracking page presentation, including display options, buttons, footnotes, and advertising. |
| Update Address | `updateAddress` | Update an existing address on the Easyship account by its ID. |
| Update Asset | `updateAsset` | Update the name or active status of a branding asset on the Easyship account. |
| Update Auto Recharge Settings | `updateAutoRecharge` | Update the automatic credit recharge settings, including whether it is enabled, the trigger threshold, and the recharge amount. |
| Update Box | `updateBox` | Update a packaging box on the Easyship account, including its active status and auto-selection setting. |
| Update Courier | `updateCourier` | Updates the configuration of an existing courier by its identifier. |
| Update Payment Source | `updatePaymentSource` | Update an existing payment source, including its holder details or default status. |
| Update Product | `updateProduct` | Updates an existing product in the Easyship product catalog by its identifier. |
| Update Sandbox Tracking | `updateSandboxTracking` | Updates a sandbox tracking record to simulate status changes and checkpoints for testing purposes. |
| Update Shipment | `updateShipment` | Updates an existing shipment by its Easyship shipment ID. Any field sent overwrites the existing value. |
| Update Shipping Rule | `updateShippingRule` | Updates the name, description, recalculation setting, or priority of an existing shipping rule. |
| Update Shipping Rule Action | `updateShippingRuleAction` | Updates the type or options of an existing action on a shipping rule. |
| Update Shipping Rule Condition | `updateShippingRuleCondition` | Updates the type or options of an existing condition on a shipping rule. |
| Update Warehouse States | `updateWarehouseStates` | Updates the warehouse fulfillment state for a batch of shipments. |
| Update Webhook | `updateWebhook` | Updates the endpoint, subscribed event types, version, or configuration of an existing webhook. |
| Validate Address | `validateAddress` | Validate an address against carrier and postal databases, optionally replacing the input with the validated result. |
