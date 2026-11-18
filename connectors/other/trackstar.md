---
description: "Trackstar Unified API for Supply Chain Logistics (WMS / 3PL)."
hidden: true
---

# Trackstar

<img src="../../.gitbook/assets/connectors/lg/trackstar.png" alt="Trackstar logo">

Trackstar Unified API for Supply Chain Logistics (WMS / 3PL). Integrate once to read and write orders, inventory, products, inbound shipments, returns, warehouses, locations, suppliers, shipping methods, and billing across dozens of warehouse management systems.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [trackstarhq.com](https://trackstarhq.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `trackstar` |

## Use it

Add Trackstar from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.trackstar.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Adjust Inventory Item | `adjustInventoryItem` | Adjust (increase or decrease) the inventory quantity for the specified inventory item at a warehouse. |
| Cancel Order | `cancelOrder` | Cancels an order by its order_id. |
| Cancel Return | `cancelReturn` | Cancels a return by its return_id. |
| Create Inbound Shipment | `createInboundShipment` | Creates an Inbound Shipment (ASN). Use the integrations endpoint to discover integration-specific fields. |
| Create Kit Product | `createKitProduct` | Creates a Kit (bundle) Product made up of component products. |
| Create Link Token | `createLinkToken` | Creates a temporary link token to initiate Trackstar Link. Requires only the API key. |
| Create Magic Link | `createMagicLink` | Create a Magic Link letting an end user connect their integration via a hosted link. |
| Create Order | `createOrder` | Creates an outbound Order. Use the integrations endpoint to discover integration-specific fields. Body uses the unified base schema. Fields depend on the warehouse system: call Get Integration Write Info for the exact fields your integration accepts. Only the fields you send are passed to Trackstar; any other field from write-info is passed through as well. |
| Create Order File | `createOrderFile` | Attach a file (e.g. label or document) to the specified order. |
| Create Product | `createProduct` | Creates a Product. Use the integrations endpoint for integration-specific fields. |

<details>

<summary>See 57 more actions</summary>

* **Create Return** `createReturn`: Creates a Return. Use the integrations endpoint to discover integration-specific fields.
* **Create Webhook** `createWebhook`: Register a Trackstar webhook so fastn is notified when WMS/cart events occur. POST /webhooks with url and the event_types to subscribe to.
* **Delete Connection** `deleteConnection`: Deletes the connection associated with the provided access token.
* **Delete Magic Link** `deleteMagicLink`: Delete a Magic Link by its ID.
* **Delete Webhook** `deleteWebhook`: Deletes a registered Trackstar webhook by id so events stop being delivered.
* **Exchange Auth Code** `exchangeAuthCode`: Exchanges a temporary auth code from the Link flow for a permanent access token and connection details.
* **Generate Sandbox** `generateSandbox`: Generates a sandbox connection with mocked-out data for testing. Reuses the same connection ID each time and RESETS any existing sandbox for that integration type.
* **Get All Bills** `getBills`: Returns all Bills (billing records) for the WMS connection.
* **Get All Inbound Shipment Suppliers** `getInboundShipmentSuppliers`: Returns all Inbound Shipment Suppliers for the WMS connection.
* **Get All Inbound Shipments** `getInboundShipments`: Returns all Inbound Shipments (ASNs) for the WMS connection with filtering and pagination.
* **Get All Inventory Items** `getInventory`: Returns all Inventory items for the WMS connection with filtering and pagination.
* **Get All Order Channels** `getOrderChannels`: Returns all Order Channels for the WMS connection.
* **Get All Orders** `getOrders`: Returns all outbound Orders for the WMS connection with filtering and pagination.
* **Get All Products** `getProducts`: Returns all Products for the WMS connection with filtering and pagination. Use sku for one exact SKU, or sku_in for a comma-separated list of up to 100 SKUs in one call.
* **Get All Returns** `getReturns`: Returns all Returns for the WMS connection with filtering and pagination.
* **Get All Shipping Methods** `getShippingMethods`: Returns all Shipping Methods for the WMS connection.
* **Get All Warehouse Customers** `getWarehouseCustomers`: Returns all Warehouse Customers for the WMS connection.
* **Get All Warehouse Locations** `getWarehouseLocations`: Returns all Warehouse Locations for the specified warehouse.
* **Get All Warehouses** `getWarehouses`: Returns all Warehouses for the WMS connection.
* **Get All Webhooks** `getWebhooks`: Returns all registered Trackstar webhooks for the connection.
* **Get Bill** `getBill`: Returns a single Bill by its bill_id.
* **Get Connection** `getConnection`: Returns the specified connection by connection_id, including sync status.
* **Get Connections** `getConnections`: Returns connected integrations for your organization.
* **Get Inbound Shipment** `getInboundShipment`: Returns a single Inbound Shipment by its ID.
* **Get Integration Info** `getIntegration`: Returns information about the data provided by a single integration.
* **Get Integration Write Info** `getIntegrationWriteInfo`: Returns the OpenAPI 3.1.0 spec for all write operations supported by an integration, including required/optional/integration-specific fields.
* **Get Integrations Info** `getIntegrations`: Returns information about the data and capabilities provided by each supported integration of one type (wms, freight, cart, carrier or erp).
* **Get Inventory Item** `getInventoryItem`: Returns a single Inventory Item by its inventory_id.
* **Get Inventory Ledger** `getInventoryLedger`: Returns the Inventory Ledger (history of inventory changes) for the WMS connection.
* **Get Magic Link** `getMagicLink`: Get a Magic Link by its ID.
* **Get Magic Links** `getMagicLinks`: Returns a list of all Magic Links for your organization.
* **Get Order** `getOrder`: Returns a single Order by its order_id.
* **Get Order Packs** `getOrderPacks`: Returns the packs for the specified order.
* **Get Product** `getProduct`: Returns a single Product by its product_id.
* **Get Return** `getReturn`: Returns a single Return by its return_id.
* **Get Shipping Method** `getShippingMethod`: Returns a single Shipping Method by its ID.
* **Get Warehouse** `getWarehouse`: Returns a single Warehouse by its warehouse_id.
* **Get Warehouse Customer** `getWarehouseCustomer`: Returns a single Warehouse Customer by its ID.
* **Get Warehouse Location** `getWarehouseLocation`: Returns a single Warehouse Location by warehouse_id and location_id.
* **Get Webhook** `getWebhook`: Returns a single registered Trackstar webhook by id.
* **Passthrough Request** `passthroughRequest`: Sends a raw request directly to the connected integration when no unified Trackstar endpoint covers it. Trackstar handles authentication with the integration; the response is the integration's native format, not Trackstar's unified schema. Returns status_code, headers and body from the integration.
* **Receive Inbound Shipment** `receiveInboundShipment`: Receives an inbound shipment, recording received line items at a warehouse location.
* **Ship Order** `shipOrder`: Marks an order as fulfilled and passes the shipment and package tracking information.
* **Sync Connection** `syncConnection`: Manually trigger a sync for the connection associated with the access token.
* **Toggle Connection Schedule** `toggleConnectionSchedule`: Pause or unpause the sync schedule for the connection associated with the access token.
* **Update Connection** `updateConnection`: Manually update properties of the connection for the provided access token.
* **Update Inbound Shipment** `updateInboundShipment`: Updates an Inbound Shipment by ID using the unified schema.
* **Update Inbound Shipment Trackstar Tags** `updateInboundShipmentTags`: Update the trackstar_tags for the specified inbound shipment.
* **Update Inventory Trackstar Tags** `updateInventoryTags`: Update the trackstar_tags for the specified inventory item.
* **Update Kit Product** `updateKitProduct`: Updates a Kit (bundle) Product by ID.
* **Update Order** `updateOrder`: Updates an Order by ID using the unified base schema. Fields depend on the warehouse system: call Get Integration Write Info for the exact fields your integration accepts. Only the fields you send are passed to Trackstar; any other field from write-info is passed through as well.
* **Update Order Trackstar Tags** `updateOrderTags`: Update the trackstar_tags for the specified order.
* **Update Product** `updateProduct`: Updates a Product by ID. Only sku is required.
* **Update Product Trackstar Tags** `updateProductTags`: Update the trackstar_tags for the specified product.
* **Update Return** `updateReturn`: Updates a Return by ID using the unified schema.
* **Update Return Trackstar Tags** `updateReturnTags`: Update the trackstar_tags for the specified return.
* **Update Warehouse Trackstar Tags** `updateWarehouseTags`: Update the trackstar_tags for the specified warehouse.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Bill Created | `bill.created` | When a Bill is created. |
| Bill Updated | `bill.updated` | When a Bill is updated. |
| Carrier Invoice Line Item Created | `carrier_invoice_line_item.created` | When a Carrier Invoice Line Item is created. |
| Carrier Invoice Line Item Updated | `carrier_invoice_line_item.updated` | When a Carrier Invoice Line Item is updated. |
| Cart Order Created | `cart_order.created` | When a Cart Order is created. |
| Cart Order Shipment Created | `cart_order_shipment.created` | When a shipment is created for a cart order. |
| Cart Order Updated | `cart_order.updated` | When a Cart Order is updated. |
| Cart Product Created | `cart_product.created` | When a Cart Product is created. |
| Cart Product Updated | `cart_product.updated` | When a Cart Product is updated. |
| Cart Warehouse Created | `cart_warehouse.created` | When a Cart Warehouse is created. |

<details>

<summary>See 42 more events</summary>

* **Cart Warehouse Updated** `cart_warehouse.updated`: When a Cart Warehouse is updated.
* **Connection Created** `connection.created`: When a Connection is created.
* **Connection Deleted** `connection.deleted`: When a Connection is deleted.
* **Connection Error Created** `connection_error.created`: When a Connection Error is created.
* **Connection Error Deleted** `connection_error.deleted`: When a Connection Error is resolved.
* **Connection Error Updated** `connection_error.updated`: When a Connection Error is updated.
* **Connection Historical Sync Completed** `connection.historical-sync-completed`: Triggered when historical sync for a resource (orders, inventory, etc.) completes.
* **Connection Updated** `connection.updated`: The WMS connection status or sync state changed.
* **Freight Shipment Created** `freight_shipment.created`: When a Freight Shipment is created.
* **Freight Shipment Updated** `freight_shipment.updated`: When a Freight Shipment is updated.
* **Inbound Shipment Created** `inbound_shipment.created`: When an Inbound Shipment is created.
* **Inbound Shipment Created** `inbound_shipment.created`: A new inbound shipment (purchase order / ASN) was created.
* **Inbound Shipment Receipt Created** `inbound_shipment_receipt.created`: When a receipt is created for the inbound shipment.
* **Inbound Shipment Updated** `inbound_shipment.updated`: When an Inbound Shipment is updated.
* **Inbound Shipment Updated** `inbound_shipment.updated`: An inbound shipment was updated or received.
* **Inventory Created** `inventory.created`: When an Inventory Item is created.
* **Inventory Ledger Created** `inventory_ledger.created`: When an Inventory Ledger entry is created.
* **Inventory Ledger Updated** `inventory_ledger.updated`: When an Inventory Ledger entry is updated.
* **Inventory Updated** `inventory.updated`: When an Inventory Item is updated.
* **Inventory Updated** `inventory.updated`: Inventory levels for one or more SKUs changed.
* **Order Created** `order.created`: When an outbound Order is created.
* **Order Created** `order.created`: A new outbound order was created in the WMS.
* **Order Shipment Created** `order_shipment.created`: When a shipment is created for an order.
* **Order Updated** `order.updated`: When an outbound Order is updated.
* **Order Updated** `order.updated`: An existing outbound order was updated (status, fulfillment, tags).
* **Product Created** `product.created`: When a Product (Kit) is created.
* **Product Created** `product.created`: A new product was created in the WMS.
* **Product Updated** `product.updated`: When a Product (Kit) is updated.
* **Product Updated** `product.updated`: An existing product was updated.
* **Return Created** `return.created`: When a Return is created.
* **Return Created** `return.created`: A new return was created.
* **Return Updated** `return.updated`: When a Return is updated.
* **Return Updated** `return.updated`: An existing return was updated.
* **Shipment Created** `shipment.created`: A shipment was created for an order.
* **Shipping Method Created** `shipping_method.created`: When a Shipping Method is created.
* **Shipping Method Updated** `shipping_method.updated`: When a Shipping Method is updated.
* **Warehouse Created** `warehouse.created`: When a Warehouse is created.
* **Warehouse Customer Created** `warehouse_customer.created`: When a Warehouse Customer is created.
* **Warehouse Customer Updated** `warehouse_customer.updated`: When a Warehouse Customer is updated.
* **Warehouse Location Created** `warehouse_location.created`: When a Warehouse Location is created.
* **Warehouse Location Updated** `warehouse_location.updated`: When a Warehouse Location is updated.
* **Warehouse Updated** `warehouse.updated`: When a Warehouse is updated.

</details>
