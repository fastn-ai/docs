---
description: "ShipEngine (ShipStation API) multi-carrier shipping API."
hidden: true
---

# ShipEngine

<img src="../../.gitbook/assets/connectors/lg/shipengine.png" alt="ShipEngine logo">

ShipEngine (ShipStation API) multi-carrier shipping API. Manage carriers, validate and parse addresses, create shipments, compare and estimate rates, buy and void labels, track packages, schedule pickups, build manifests and batches, manage warehouses, custom package types, insurance, tags, and webhooks.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [shipengine.com](https://shipengine.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `shipengine` |

## Use it

Add ShipEngine from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.shipengine.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Funds To Carrier | `addFundsToCarrier` | Add funds to a carrier account that requires a prepaid balance (e.g. USPS via Stamps.com). |
| Add Funds To Insurance | `addFundsToInsurance` | Add funds to the connected Shipsurance insurance account in the specified currency and amount. |
| Add To Batch | `addToBatch` | Add shipments and/or rates to an existing batch. |
| Calculate Rates | `calculateRates` | Calculate shipping rates for a shipment (by shipment_id or an inline shipment) across the specified carriers. |
| Cancel Label Refund | `cancelLabelRefund` | Cancel a pending refund request for a label. |
| Cancel Shipment | `cancelShipment` | Cancel a shipment so it can no longer be used to purchase a label. |
| Compare Bulk Rates | `compareBulkRates` | Compare rates for a large group of shipments in a single request. |
| Connect Carrier Account | `connectCarrierAccount` | Connect a carrier account to ShipEngine. The carrier_name path segment selects the carrier (e.g. stamps_com, ups, fedex). Required credential fields vary per carrier (e.g. nickname/username/password for stamps_com). |
| Connect Shipsurance Insurer | `connectInsurer` | Connect a Shipsurance insurance account to ShipEngine using the account email and policy ID. |
| Create Account Image | `createAccountImage` | Upload a new account label image (e.g. a logo) from base64-encoded image data. |

<details>

<summary>See 82 more actions</summary>

* **Create Batch** `createBatch`: Create a batch of shipments and/or rates for bulk label processing.
* **Create Combined Label Document** `createCombinedLabelDocument`: Combine up to 30 existing shipping labels into a single downloadable document (PDF).
* **Create Custom Package Type** `createPackageType`: Create a custom package type with dimensions for use when creating shipments and labels.
* **Create Label** `createLabel`: Purchase a shipping label directly from a full shipment definition.
* **Create Label From Rate** `createLabelFromRate`: Purchase a shipping label using a previously calculated rate_id.
* **Create Label From Rate Shopper** `createLabelFromRateShopper`: Purchase a shipping label using a rate_shopper_id from a rate-shopping session.
* **Create Label From Shipment** `createLabelFromShipment`: Purchase a shipping label for an existing shipment identified by shipment_id.
* **Create Manifest** `createManifest`: Create a manifest for a warehouse, bundling labels for carrier pickup.
* **Create Return Label** `createReturnLabel`: Create a return label for an existing outbound label.
* **Create Shipments** `createShipments`: Create one or more shipments in ShipEngine. Returns the created shipments with their shipment_id values.
* **Create Tag** `createTag`: Create a new shipment tag with a name and optional color.
* **Create Warehouse** `createWarehouse`: Create a warehouse (ship-from location) with an origin address and optional return address.
* **Create Webhook** `createWebhook`: Subscribe to a ShipEngine event by registering a webhook URL. ShipEngine will POST to the URL when the chosen event occurs (e.g. tracking updates, rates, batch or report completion).
* **Delete Account Image By ID** `deleteAccountImage`: Delete an account label image by its label image ID.
* **Delete Batch** `deleteBatch`: Archive (delete) a batch by its batch_id.
* **Delete Custom Package Type By ID** `deletePackageType`: Delete a custom package type by its package ID.
* **Delete Pickup** `deletePickup`: Cancel a scheduled pickup by its pickup_id.
* **Delete Tag** `deleteTag`: Delete a shipment tag by its name.
* **Delete Warehouse By ID** `deleteWarehouse`: Delete (deactivate) a warehouse by its warehouse ID.
* **Delete Webhook By ID** `deleteWebhook`: Delete (unsubscribe) a webhook by its webhook ID.
* **Disconnect Carrier Account** `disconnectCarrierAccount`: Disconnect a carrier account from ShipEngine by carrier name and carrier ID.
* **Disconnect Carrier By ID** `disconnectCarrierById`: Disconnect a carrier account from this ShipEngine account by its carrier ID.
* **Disconnect Shipsurance Insurer** `disconnectInsurer`: Disconnect the Shipsurance insurance account from ShipEngine.
* **Download File** `downloadFile`: Download a generated document (label, batch, form) in PDF, PNG, or ZPL format by its download directory path.
* **Estimate Rates** `estimateRates`: Get quick rate estimates between two locations without creating a shipment.
* **Get Account Image By ID** `getAccountImageById`: Retrieve a single account label image by its label image ID.
* **Get Account Settings** `getAccountSettings`: Retrieve all account settings for the ShipEngine account.
* **Get Batch By External ID** `getBatchByExternalId`: Retrieve a batch using your own external_batch_id.
* **Get Batch By ID** `getBatchById`: Retrieve a single batch by its batch_id.
* **Get Batch Errors** `getBatchErrors`: Retrieve the errors that occurred while processing a batch.
* **Get Carrier By ID** `getCarrierById`: Retrieve a single connected carrier account by its ShipEngine carrier ID (e.g. se-28529731).
* **Get Carrier Options** `getCarrierOptions`: List the advanced options available for a connected carrier account (e.g. saturday delivery, signature confirmation).
* **Get Carrier Settings** `getCarrierSettings`: Retrieve the account-level settings for a connected carrier by carrier name and carrier ID.
* **Get Custom Package Type By ID** `getPackageTypeById`: Retrieve a single custom package type by its package ID.
* **Get Ephemeral Token** `getEphemeralToken`: Generate a short-lived (10 second) ephemeral token that can be passed to an application for authorized access.
* **Get Insurance Balance** `getInsuranceBalance`: Retrieve the current funds balance of the connected Shipsurance insurance account.
* **Get Label By External Shipment ID** `getLabelByExternalShipmentId`: Retrieve a label using the external_shipment_id of its shipment.
* **Get Label By ID** `getLabelById`: Retrieve a single shipping label by its label_id.
* **Get Label Tracking Info** `getLabelTrackingInfo`: Retrieve tracking information for a purchased label.
* **Get Manifest By ID** `getManifestById`: Retrieve a single manifest by its manifest_id.
* **Get Manifest Request By ID** `getManifestRequestById`: Retrieve the status of an asynchronous manifest creation request.
* **Get Pickup By ID** `getPickupById`: Retrieve a single scheduled pickup by its pickup_id.
* **Get Rate By ID** `getRateById`: Retrieve a single rate by its rate_id.
* **Get Service Point By ID** `getServicePointById`: Retrieve a single carrier service point by carrier code, country code, and service point ID.
* **Get Shipment By External ID** `getShipmentByExternalId`: Retrieve a shipment using your own external_shipment_id.
* **Get Shipment By ID** `getShipmentById`: Retrieve a single shipment by its ShipEngine shipment_id.
* **Get Tracking Info** `getTrackingInfo`: Retrieve tracking information for a package by carrier code and tracking number.
* **Get Warehouse By ID** `getWarehouseById`: Retrieve a single warehouse by its warehouse ID.
* **Get Webhook By ID** `getWebhookById`: Retrieve a single webhook by its webhook ID.
* **List Account Images** `listAccountImages`: List all account label images configured on the ShipEngine account.
* **List Batches** `listBatches`: Retrieve a paginated list of batches, optionally filtered by status or date range.
* **List Carrier Package Types** `listCarrierPackageTypes`: List all package types (e.g. envelope, box) supported by a connected carrier account.
* **List Carrier Services** `listCarrierServices`: List all shipping services offered by a connected carrier account.
* **List Carriers** `listCarriers`: List all carrier accounts connected to this ShipEngine account, including balances, services, and supported package types.
* **List Custom Package Types** `listPackageTypes`: List all custom package types configured on the account.
* **List Labels** `listLabels`: Retrieve a paginated list of shipping labels, optionally filtered by status, carrier, tracking number, or date range.
* **List Manifests** `listManifests`: Retrieve a paginated list of manifests, optionally filtered by warehouse, carrier, or date range.
* **List Scheduled Pickups** `listScheduledPickups`: Retrieve a paginated list of scheduled pickups, optionally filtered by carrier or warehouse.
* **List Service Points** `listServicePoints`: List carrier service points (drop-off/pickup locations) near a location for the given providers. Only carriers that support service points (e.g. DHL, UPS Access Point) return results.
* **List Shipment Rates** `listShipmentRates`: Retrieve the rates already calculated for a shipment.
* **List Shipments** `listShipments`: Retrieve a paginated list of shipments, optionally filtered by status, batch, tag, or date range.
* **List Tags** `listTags`: List all shipment tags defined on the account.
* **List Warehouses** `listWarehouses`: List all warehouses (ship-from locations) configured on the account.
* **List Webhooks** `listWebhooks`: List all webhooks currently enabled for the ShipEngine environment.
* **Parse An Address** `parseAddress`: Parse the recipient, sender, and address details out of unstructured text using ShipEngine's address recognition engine.
* **Process Batch Labels** `processBatchLabels`: Enqueue a batch for label processing.
* **Remove From Batch** `removeFromBatch`: Remove shipments and/or rates from an existing batch.
* **Rename Tag** `renameTag`: Rename an existing shipment tag to a new name.
* **Schedule Pickup** `schedulePickup`: Schedule a carrier pickup for one or more labels at a warehouse.
* **Start Tracking** `startTracking`: Subscribe to tracking webhook updates for a package by carrier code and tracking number.
* **Stop Tracking** `stopTracking`: Unsubscribe from tracking webhook updates for a package.
* **Tag Shipment** `tagShipment`: Add a custom tag to a shipment.
* **Untag Shipment** `untagShipment`: Remove a tag from a shipment.
* **Update Account Image By ID** `updateAccountImage`: Update an account label image's name, default flag, content type, or image data by its label image ID.
* **Update Carrier Settings** `updateCarrierSettings`: Update the account-level settings for a connected carrier (e.g. nickname, primary account flag) by carrier name and carrier ID.
* **Update Custom Package Type By ID** `updatePackageType`: Update a custom package type's name, description, and dimensions by its package ID.
* **Update Shipment** `updateShipment`: Update an existing shipment identified by shipment_id. Provide the full shipment body.
* **Update Shipments Tags** `updateShipmentsTags`: Bulk-assign tags to multiple shipments in a single request.
* **Update Warehouse By ID** `updateWarehouse`: Update a warehouse's name, origin address, and return address by its warehouse ID.
* **Update Webhook** `updateWebhook`: Update an existing webhook's URL, headers, name, or store ID by its webhook ID.
* **Validate An Address** `validateAddress`: Validate one or more addresses against ShipEngine's address validation service, returning normalized addresses and validation messages. The body is a JSON array of address objects.
* **Void Label** `voidLabel`: Void a shipping label and request a refund where supported.

</details>
