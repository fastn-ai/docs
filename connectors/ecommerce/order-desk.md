---
description: "Order Desk (order management) connector."
hidden: true
---

# Order Desk

<img src="../../.gitbook/assets/connectors/lg/order-desk.png" alt="Order Desk logo">

Base https://app.orderdesk.me/api/v2. Two-header auth: ORDERDESK-STORE-ID + ORDERDESK-API-KEY. Full coverage (26 actions): test, store, orders CRUD + order history, order items CRUD, shipments CRUD + batch, move orders, inventory items CRUD + batch. Webhooks are UI/Rules-only (no management API).

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [orderdesk.me](https://orderdesk.me) |
| **Authentication** | Credentials you enter |
| **Slug** | `orderDesk` |

## Use it

Add Order Desk from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.orderDesk.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Order Item</td><td><code>addOrderItem</code></td><td>Add an item to an order (POST /orders/{orderId}/order-items). name and code required.</td></tr><tr><td>Add Shipment</td><td><code>addShipment</code></td><td>Add a shipment to an order.</td></tr><tr><td>Append Order History</td><td><code>appendOrderHistory</code></td><td>Append a history/note entry to an order (POST /orders/{orderId}/order-history).</td></tr><tr><td>Batch Add Shipments</td><td><code>batchShipments</code></td><td>Add shipments to multiple orders in one call.</td></tr><tr><td>Batch Add/Update Inventory Items</td><td><code>batchInventoryItems</code></td><td>Create or update many inventory items at once (PUT /batch-inventory-items).</td></tr><tr><td>Create Inventory Item</td><td><code>createInventoryItem</code></td><td>Create an inventory item. name and code (unique SKU) required.</td></tr><tr><td>Create Order</td><td><code>createOrder</code></td><td>Create an order. order_items array is required.</td></tr><tr><td>Delete Inventory Item</td><td><code>deleteInventoryItem</code></td><td>Delete an inventory item by id.</td></tr><tr><td>Delete Order</td><td><code>deleteOrder</code></td><td>Delete an order by id.</td></tr><tr><td>Delete Order Item</td><td><code>deleteOrderItem</code></td><td>Delete an order item (DELETE /orders/{orderId}/order-items/{itemId}).</td></tr></tbody></table>

<details>

<summary>View 16 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Shipment</td><td><code>deleteShipment</code></td><td>Delete a shipment (DELETE /orders/{orderId}/shipments/{shipmentId}).</td></tr><tr><td>Get Inventory Item</td><td><code>getInventoryItem</code></td><td>Get an inventory item by id.</td></tr><tr><td>Get Order</td><td><code>getOrder</code></td><td>Get an order by id.</td></tr><tr><td>Get Order Item</td><td><code>getOrderItem</code></td><td>Get a single order item (GET /orders/{orderId}/order-items/{itemId}).</td></tr><tr><td>Get Shipment</td><td><code>getShipment</code></td><td>Get a single shipment (GET /orders/{orderId}/shipments/{shipmentId}).</td></tr><tr><td>Get Store</td><td><code>getStore</code></td><td>Get store metadata, settings, and folder id-&gt;name map.</td></tr><tr><td>List Inventory Items</td><td><code>listInventoryItems</code></td><td>List inventory items.</td></tr><tr><td>List Order Items</td><td><code>listOrderItems</code></td><td>List all items on an order (GET /orders/{orderId}/order-items).</td></tr><tr><td>List Orders</td><td><code>listOrders</code></td><td>List orders with optional filters.</td></tr><tr><td>List Shipments</td><td><code>listShipments</code></td><td>List shipments for an order.</td></tr><tr><td>Move Orders</td><td><code>moveOrders</code></td><td>Move one or more orders to a folder (by name or id).</td></tr><tr><td>Test Connection</td><td><code>testConnection</code></td><td>Validate the store credentials.</td></tr><tr><td>Update Inventory Item</td><td><code>updateInventoryItem</code></td><td>Update an inventory item. Send all fields to retain (omitted fields are blanked).</td></tr><tr><td>Update Order</td><td><code>updateOrder</code></td><td>Update an order by id (partial).</td></tr><tr><td>Update Order Item</td><td><code>updateOrderItem</code></td><td>Update an order item (PUT /orders/{orderId}/order-items/{itemId}).</td></tr><tr><td>Update Shipment</td><td><code>updateShipment</code></td><td>Update a shipment (PUT /orders/{orderId}/shipments/{shipmentId}).</td></tr></tbody></table>

</details>
