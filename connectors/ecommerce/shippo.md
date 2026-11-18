---
description: "Shippo multi-carrier shipping API — create addresses, parcels, and shipments, shop rates across carriers, buy shipping labels, track packages, manage customs,…"
hidden: true
---

# Shippo

Shippo multi-carrier shipping API — create addresses, parcels, and shipments, shop rates across carriers, buy shipping labels, track packages, manage customs, refunds, orders, manifests, batches, carrier accounts, and webhooks.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [goshippo.com](https://goshippo.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 61 |
| **Events** | 0 |
| **Slug** | `shippo` |

## Use it

Add Shippo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.shippo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Shipments To Batch | `addShipmentsToBatch` | Add one or more batch shipments to an existing batch. Provide the shipments as a JSON array string of batch shipment objects. |
| Create Address | `createAddress` | Create a new address object that can be used as the sender or recipient of a shipment. |
| Create Batch | `createBatch` | Create a batch of shipments for bulk label purchase using a default carrier account and service level. |
| Create Carrier Account | `createCarrierAccount` | Connect a carrier account by providing the carrier name, account ID, and carrier-specific credential parameters. |
| Create Customs Declaration | `createCustomsDeclaration` | Create a customs declaration referencing one or more customs items, required for international shipments. |
| Create Customs Item | `createCustomsItem` | Create a customs item describing a single line of goods for an international customs declaration. |
| Create Manifest | `createManifest` | Create a manifest (end-of-day SCAN form) that closes out a set of transactions for a carrier account. |
| Create Order | `createOrder` | Create an order representing a customer purchase to be fulfilled, including recipient address and line items. |
| Create Parcel | `createParcel` | Create a parcel object describing the dimensions and weight of a package to be shipped. |
| Create Pickup | `createPickup` | Schedule a carrier pickup for one or more purchased transactions at a location within a requested time window. |
| Create Refund | `createRefund` | Request a refund for a purchased shipping label transaction. |
| Create Service Group | `createServiceGroup` | Create a service group that bundles carrier service levels for presenting live checkout rates. |
| Create Shipment | `createShipment` | Create a shipment from a sender address, recipient address, and one or more parcels. Returns available rates across all connected carriers. Pass async false to receive rates synchronously. |
| Create Shipping Label | `createTransaction` | Purchase a shipping label. Provide a rate object_id from a shipment's rates, or provide an inline shipment plus carrier_account and servicelevel_token for an instant label. Pass async false to get the label URL synchronously. |
| Create Shippo Account | `createShippoAccount` | Create a managed Shippo account under a Platform Pro account. Requires a Platform-tier Shippo account. |
| Create User Parcel Template | `createUserParcelTemplate` | Create a reusable user parcel template with fixed dimensions for frequently shipped package types. |
| Create Webhook | `createWebhook` | Create a webhook subscription that posts event notifications to a URL for the chosen event type. |
| Delete Service Group | `deleteServiceGroup` | Delete a service group by its object ID. |
| Delete User Parcel Template | `deleteUserParcelTemplate` | Delete a user parcel template by its object ID. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription by its object ID. |
| Get Address | `getAddress` | Retrieve a single address object by its object ID. |
| Get Batch | `getBatch` | Retrieve a batch object by its object ID, including the status of each batch shipment. |
| Get Carrier Account | `getCarrierAccount` | Retrieve a single carrier account by its object ID. |
| Get Customs Declaration | `getCustomsDeclaration` | Retrieve a single customs declaration object by its object ID. |
| Get Customs Item | `getCustomsItem` | Retrieve a single customs item object by its object ID. |
| Get Manifest | `getManifest` | Retrieve a single manifest object by its object ID. |
| Get Order | `getOrder` | Retrieve a single order object by its object ID. |
| Get Parcel | `getParcel` | Retrieve a single parcel object by its object ID. |
| Get Rate | `getRate` | Retrieve a single rate object by its object ID. |
| Get Refund | `getRefund` | Retrieve a single refund object by its object ID. |
| Get Shipment | `getShipment` | Retrieve a single shipment object by its object ID. |
| Get Shipping Label | `getTransaction` | Retrieve a single shipping label transaction by its object ID. |
| Get Shippo Account | `getShippoAccount` | Retrieve a single managed Shippo account by its object ID. |
| Get Tracking Status | `getTrackingStatus` | Retrieve the current tracking status and full history for a package by carrier and tracking number. |
| Get User Parcel Template | `getUserParcelTemplate` | Retrieve a single user parcel template by its object ID. |
| Get Webhook | `getWebhook` | Retrieve a single webhook subscription by its object ID. |
| List Addresses | `listAddresses` | Return a paginated list of all address objects created on the account. |
| List Carrier Accounts | `listCarrierAccounts` | Return all carrier accounts connected to the Shippo account, including Shippo default carriers. |
| List Customs Declarations | `listCustomsDeclarations` | Return a paginated list of all customs declaration objects on the account. |
| List Customs Items | `listCustomsItems` | Return a paginated list of all customs item objects on the account. |
| List Manifests | `listManifests` | Return a paginated list of all manifest objects on the account. |
| List Orders | `listOrders` | Return a paginated list of all order objects on the account. |
| List Parcels | `listParcels` | Return a paginated list of all parcel objects created on the account. |
| List Refunds | `listRefunds` | Return a paginated list of all refund objects on the account. |
| List Service Groups | `listServiceGroups` | Return all service groups configured on the account. |
| List Shipment Rates | `listShipmentRates` | Return all rates generated for a shipment across connected carriers. |
| List Shipment Rates In Currency | `listShipmentRatesInCurrency` | Return all rates for a shipment converted into the requested ISO 4217 currency. |
| List Shipments | `listShipments` | Return a paginated list of all shipment objects created on the account. |
| List Shipping Labels | `listTransactions` | Return a paginated list of all shipping label transactions, filterable by object and tracking status. |
| List Shippo Accounts | `listShippoAccounts` | Return all managed Shippo accounts under a Platform Pro account. |
| List User Parcel Templates | `listUserParcelTemplates` | Return all user parcel templates on the account. |
| List Webhooks | `listWebhooks` | Return all webhook subscriptions configured on the account. |
| Purchase Batch | `purchaseBatch` | Purchase all valid labels in a batch once its shipments have finished rating. |
| Register Tracking | `registerTracking` | Register a carrier tracking number so that track_updated webhook notifications are sent as its status changes. |
| Remove Shipments From Batch | `removeShipmentsFromBatch` | Remove one or more batch shipments from an existing batch. Provide the batch shipment object IDs as a JSON array string. |
| Update Carrier Account | `updateCarrierAccount` | Update a carrier account, for example to activate or deactivate it or change its parameters. |
| Update Service Group | `updateServiceGroup` | Update an existing service group by its object ID. |
| Update Shippo Account | `updateShippoAccount` | Update a managed Shippo account by its object ID. |
| Update User Parcel Template | `updateUserParcelTemplate` | Update an existing user parcel template by its object ID. |
| Update Webhook | `updateWebhook` | Update an existing webhook subscription, for example to change its URL, event, or active status. |
| Validate Address | `validateAddress` | Validate an existing address object and return deliverability results and any corrections. |
