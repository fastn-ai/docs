---
description: "Sendcloud shipping and parcel automation platform."
hidden: true
---

# Sendcloud

<img src="../../.gitbook/assets/connectors/lg/sendcloud.png" alt="Sendcloud logo">

Sendcloud shipping and parcel automation platform. Create and manage parcels, shipping methods and products, labels, tracking, sender addresses, returns, integrations, invoices, brands, and webhook (integration) configuration via the Sendcloud v2 REST API.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [sendcloud.com](https://sendcloud.com) |
| **Authentication** | Basic auth |
| **Slug** | `sendcloud` |

## Use it

Add Sendcloud from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sendcloud.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Print Labels | `bulkPrintLabels` | Request combined label PDF download links for multiple parcels at once. The parcel IDs are sent under the required 'label' wrapper. Requires announced parcels with purchased labels. |
| Cancel Parcel | `cancelParcel` | Cancel a parcel by its ID. Unannounced parcels are deleted; announced parcels have their cancellation requested with the carrier. |
| Cancel Shipment (v3) | `cancelShipment` | Cancel a shipment by its ID via the Sendcloud API v3. |
| Create and Announce Shipment (v3) | `createShipment` | Create and announce a shipment synchronously via the API v3, generating the shipping label immediately. WARNING: a successful call announces the shipment and creates a paid label. Requires from/to addresses, a ship_with shipping option, and parcels. |
| Create Integration Log | `createIntegrationLog` | Create an exception log entry for a specific integration, recording a failed outbound request (URL, method, response, exception). |
| Create Integration Shipments | `createIntegrationShipments` | Create or update a batch of shipments (orders) in a specific integration's feed. The body is a JSON array (max 100 orders). Provide it as a JSON string in shipmentsJson. |
| Create or Update Orders (v3) | `createOrders` | Create or update a batch of orders (drafts, no label) via the Sendcloud API v3 Orders endpoint. Upserts by order_id + integration.id. The body is a JSON array (max 100). Provide it as a JSON string in ordersJson. |
| Create Parcel | `createParcel` | Create a single parcel (shipment). Optionally announce it and request a shipping label by setting request_label to true. The parcel object is sent under the required 'parcel' wrapper. |
| Create Parcels (Bulk) | `createParcelsBulk` | Create multiple parcels in one request. The parcels are sent under the required 'parcels' array wrapper. Each parcel has the same shape as Create Parcel. |
| Delete Integration Shipment | `deleteIntegrationShipment` | Delete a shipment from an integration's feed. Provide either shipment_uuid, or both external_order_id and external_shipment_id. |
| Delete Order (v3) | `deleteOrder` | Delete an order by its Sendcloud ID via the API v3. |
| Get Brand | `getBrand` | Retrieve a single brand by its ID, including branding colors, logos, domain, and enabled tracking/returns features. |
| Get Integration | `getIntegration` | Retrieve a single integration by its ID, including webhook and service point configuration. |
| Get Invoice | `getInvoice` | Retrieve a single invoice by its ID, including its line items. |
| Get Order (v3) | `getOrder` | Retrieve a single order by its Sendcloud ID via the API v3. |
| Get Parcel | `getParcel` | Retrieve a single parcel by its ID, including status, label links, tracking and customs details. |
| Get Parcel Label | `getParcelLabel` | Retrieve the label download links (normal printer A4 positions and label printer) for an announced parcel with a purchased label. |
| Get PDF Label (Normal Printer) | `getPdfLabelNormalPrinter` | Download the A4 PDF label for a parcel at a given position (start_from 0-3). Returns a PDF binary. Requires an announced parcel with a purchased label. |
| Get Return | `getReturn` | Retrieve a single return by its ID, including refund, delivery option, and incoming/outgoing parcel details. |
| Get Return Portal Outgoing Parcel | `getReturnPortalOutgoingParcel` | Look up an outgoing parcel in a brand's public return portal by postal code and identifier (tracking or order number), returning eligible products, carriers and an access token for creating a return. Public endpoint. Requires a configured return portal. |
| Get Return Portal Settings | `getReturnPortalSettings` | Retrieve the public return portal settings for a brand domain (branding, delivery options, return methods, refund settings). Public endpoint. Requires a configured return portal with a brand domain. |
| Get Return Portal URL | `getReturnPortalUrl` | Retrieve the return portal URL for a parcel, used to send the customer to the branded returns portal. Requires a configured return portal / connected brand. |
| Get Sender Address | `getSenderAddress` | Retrieve a single sender address by its ID. |
| Get Shipment (v3) | `getShipment` | Retrieve a single shipment by its ID via the Sendcloud API v3. |
| Get Shipping Method | `getShippingMethod` | Retrieve a single shipping method by its ID, including per-country pricing and availability. |
| Get Tracking | `getTracking` | Retrieve tracking information (status history, expected delivery, carrier links) for a parcel by its tracking number. |
| Get User | `getUser` | Retrieve the account and invoice-address details of the authenticated Sendcloud user, including enabled modules. |
| List All Integration Logs | `listAllIntegrationLogs` | Retrieve all integration exception logs across every integration on the account. |
| List Brands | `listBrands` | Retrieve the list of brands configured on the account, used for tracking pages and return portals. |
| List Integration Logs | `listIntegrationLogs` | Retrieve the exception logs for a specific integration. |
| List Integration Shipments | `listIntegrationShipments` | Retrieve the shipments (orders) feed for a specific integration, with optional date, order and shipping-rule filters. |
| List Integrations | `listIntegrations` | Retrieve all integrations (shop connections) on the account, including their webhook configuration and service point settings. |
| List Invoices | `listInvoices` | Retrieve all invoices issued to the account to date. |
| List Orders (v3) | `listOrders` | Retrieve a paginated list of orders via the Sendcloud API v3, with optional integration, status, order number/id and date filters. |
| List Parcel Statuses | `listParcelStatuses` | Retrieve the full list of possible parcel statuses (id and human-readable message). |
| List Parcels | `listParcels` | Retrieve a paginated list of parcels, optionally filtered by status, tracking number, order number, external reference, update/announce time, or a set of IDs. |
| List Returns | `listReturns` | Retrieve a paginated list of returns (incoming return shipments) on the account. |
| List Sender Addresses | `listSenderAddresses` | Retrieve all sender (return/ship-from) addresses configured on the Sendcloud account. |
| List Shipments (v3) | `listShipments` | Retrieve a paginated list of shipments via the Sendcloud API v3, with optional status, tracking number, order number and update-time filters. |
| List Shipping Functionalities | `listShippingFunctionalities` | Retrieve all shipping functionality definitions (capabilities such as delivery speed, insurance, B2B) with their types, default values and allowed values. |
| List Shipping Methods | `listShippingMethods` | Retrieve the list of shipping methods available to the account, optionally filtered by sender address, service point, destination country, or return eligibility. |
| List Shipping Options (v3) | `listShippingOptions` | Retrieve available shipping options (carrier products, functionalities, requirements and optional price quotes) for a shipment via the API v3, based on origin/destination and parcel weight/dimensions. |
| List Shipping Products | `listShippingProducts` | Retrieve the list of shipping products (carrier products and their methods/functionalities) available for a given origin country, with optional destination, carrier, weight and dimension filters. |
| Partially Update Integration | `partialUpdateIntegration` | Partially update an integration. Use this to configure webhooks (set webhook_url and webhook_active) or service point settings. Only the fields you provide are updated. This is how Sendcloud webhook notifications are enabled for an integration. |
| Update Integration | `updateIntegration` | Fully update an integration (all fields required). Replaces the integration's shop details, webhook configuration and service point settings. Use Partially Update Integration for partial changes. |
| Update Order (v3) | `updateOrder` | Partially update an order via the API v3. Only the fields you provide are updated. To add or remove order items, use Create or Update Orders instead. |
| Update Parcel | `updateParcel` | Update an existing, unannounced parcel. Provide the parcel object including its id. Can also announce and request a label by setting request_label to true. The parcel object is sent under the required 'parcel' wrapper. |
