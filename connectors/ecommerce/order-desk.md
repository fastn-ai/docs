---
description: "Order Desk (order management) connector."
---

# Order Desk

Order Desk (order management) connector. Base https://app.orderdesk.me/api/v2. Two-header auth: ORDERDESK-STORE-ID + ORDERDESK-API-KEY. Full coverage (26 actions): test, store, orders CRUD + order history, order items CRUD, shipments CRUD + batch, move orders, inventory items CRUD + batch. Webhooks are UI/Rules-only (no management API).

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [orderdesk.me](https://orderdesk.me) |
| **Authentication** | Credentials you enter |
| **Actions** | 26 |
| **Events** | 0 |
| **Slug** | `orderDesk` |

## Use it

Add Order Desk from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.orderDesk.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Order Item | `addOrderItem` | Add an item to an order (POST /orders/{orderId}/order-items). name and code required. |
| Add Shipment | `addShipment` | Add a shipment to an order. |
| Append Order History | `appendOrderHistory` | Append a history/note entry to an order (POST /orders/{orderId}/order-history). |
| Batch Add Shipments | `batchShipments` | Add shipments to multiple orders in one call. |
| Batch Add/Update Inventory Items | `batchInventoryItems` | Create or update many inventory items at once (PUT /batch-inventory-items). |
| Create Inventory Item | `createInventoryItem` | Create an inventory item. name and code (unique SKU) required. |
| Create Order | `createOrder` | Create an order. order_items array is required. |
| Delete Inventory Item | `deleteInventoryItem` | Delete an inventory item by id. |
| Delete Order | `deleteOrder` | Delete an order by id. |
| Delete Order Item | `deleteOrderItem` | Delete an order item (DELETE /orders/{orderId}/order-items/{itemId}). |
| Delete Shipment | `deleteShipment` | Delete a shipment (DELETE /orders/{orderId}/shipments/{shipmentId}). |
| Get Inventory Item | `getInventoryItem` | Get an inventory item by id. |
| Get Order | `getOrder` | Get an order by id. |
| Get Order Item | `getOrderItem` | Get a single order item (GET /orders/{orderId}/order-items/{itemId}). |
| Get Shipment | `getShipment` | Get a single shipment (GET /orders/{orderId}/shipments/{shipmentId}). |
| Get Store | `getStore` | Get store metadata, settings, and folder id-&gt;name map. |
| List Inventory Items | `listInventoryItems` | List inventory items. |
| List Order Items | `listOrderItems` | List all items on an order (GET /orders/{orderId}/order-items). |
| List Orders | `listOrders` | List orders with optional filters. |
| List Shipments | `listShipments` | List shipments for an order. |
| Move Orders | `moveOrders` | Move one or more orders to a folder (by name or id). |
| Test Connection | `testConnection` | Validate the store credentials. |
| Update Inventory Item | `updateInventoryItem` | Update an inventory item. Send all fields to retain (omitted fields are blanked). |
| Update Order | `updateOrder` | Update an order by id (partial). |
| Update Order Item | `updateOrderItem` | Update an order item (PUT /orders/{orderId}/order-items/{itemId}). |
| Update Shipment | `updateShipment` | Update a shipment (PUT /orders/{orderId}/shipments/{shipmentId}). |
