---
description: "Order Desk is an order management platform. Create orders, add items and shipments, and manage inventory items."
hidden: true
---

# Order Desk

<img src="../../.gitbook/assets/connectors/lg/order-desk.png" alt="Order Desk logo">

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [orderdesk.me](https://orderdesk.me) |
| **Authentication** | Store ID and API key |
| **Slug** | `orderDesk` |

## Setup

Your customers enter their store id and api key for Order Desk when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Order Desk from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Order Desk**.
2. Select **Connect** on the Order Desk card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Order Desk's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Order Item</td><td><code>addOrderItem</code></td><td>Add an item to an order name and code required.</td></tr><tr><td>Add Shipment</td><td><code>addShipment</code></td><td>Add a shipment to an order.</td></tr><tr><td>Append Order History</td><td><code>appendOrderHistory</code></td><td>Append a history/note entry to an order</td></tr><tr><td>Batch Add Shipments</td><td><code>batchShipments</code></td><td>Add shipments to multiple orders in one call.</td></tr><tr><td>Batch Add/Update Inventory Items</td><td><code>batchInventoryItems</code></td><td>Create or update many inventory items at once</td></tr><tr><td>Create Inventory Item</td><td><code>createInventoryItem</code></td><td>Create an inventory item. name and code (unique SKU) required.</td></tr><tr><td>Create Order</td><td><code>createOrder</code></td><td>Create an order. order_items array is required.</td></tr><tr><td>Delete Inventory Item</td><td><code>deleteInventoryItem</code></td><td>Delete an inventory item by id.</td></tr><tr><td>Delete Order</td><td><code>deleteOrder</code></td><td>Delete an order by id.</td></tr><tr><td>Delete Order Item</td><td><code>deleteOrderItem</code></td><td>Delete an order item</td></tr></tbody></table>

<details>

<summary>View 16 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Shipment</td><td><code>deleteShipment</code></td><td>Delete a shipment</td></tr><tr><td>Get Inventory Item</td><td><code>getInventoryItem</code></td><td>Get an inventory item by id.</td></tr><tr><td>Get Order</td><td><code>getOrder</code></td><td>Get an order by id.</td></tr><tr><td>Get Order Item</td><td><code>getOrderItem</code></td><td>Get a single order item</td></tr><tr><td>Get Shipment</td><td><code>getShipment</code></td><td>Get a single shipment</td></tr><tr><td>Get Store</td><td><code>getStore</code></td><td>Get store metadata, settings, and folder id-&gt;name map.</td></tr><tr><td>List Inventory Items</td><td><code>listInventoryItems</code></td><td>List inventory items.</td></tr><tr><td>List Order Items</td><td><code>listOrderItems</code></td><td>List all items on an order</td></tr><tr><td>List Orders</td><td><code>listOrders</code></td><td>List orders with optional filters.</td></tr><tr><td>List Shipments</td><td><code>listShipments</code></td><td>List shipments for an order.</td></tr><tr><td>Move Orders</td><td><code>moveOrders</code></td><td>Move one or more orders to a folder (by name or id).</td></tr><tr><td>Test Connection</td><td><code>testConnection</code></td><td>Validate the store credentials.</td></tr><tr><td>Update Inventory Item</td><td><code>updateInventoryItem</code></td><td>Update an inventory item. Send all fields to retain (omitted fields are blanked).</td></tr><tr><td>Update Order</td><td><code>updateOrder</code></td><td>Update an order by id (partial).</td></tr><tr><td>Update Order Item</td><td><code>updateOrderItem</code></td><td>Update an order item</td></tr><tr><td>Update Shipment</td><td><code>updateShipment</code></td><td>Update a shipment</td></tr></tbody></table>

</details>

