---
description: "ShipStation is an order shipping platform. Create and update orders, create labels, and list carriers, customers and products."
hidden: true
---

# ShipStation

<img src="../../.gitbook/assets/connectors/lg/shipstation.png" alt="ShipStation logo">

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [shipstation.com](https://shipstation.com) |
| **Authentication** | Username and password |
| **Slug** | `shipstation` |

## Setup

Your customers enter their username and password for ShipStation when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect ShipStation from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **ShipStation**.
2. Select **Connect** on the ShipStation card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use ShipStation's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Label</td><td><code>createLabel</code></td><td>Create a shipping label for a shipment.</td></tr><tr><td>Create Or Update Order</td><td><code>createOrder</code></td><td>Create or update an order. Provide orderKey matching an existing order to update.</td></tr><tr><td>Delete Order</td><td><code>deleteOrder</code></td><td>Delete (inactivate) an order by id.</td></tr><tr><td>Get Order</td><td><code>getOrder</code></td><td>Get an order by id.</td></tr><tr><td>List Carriers</td><td><code>listCarriers</code></td><td>List carriers connected to the account.</td></tr><tr><td>List Customers</td><td><code>listCustomers</code></td><td>List customers.</td></tr><tr><td>List Orders</td><td><code>listOrders</code></td><td>List orders with optional filters.</td></tr><tr><td>List Products</td><td><code>listProducts</code></td><td>List products.</td></tr><tr><td>List Shipments</td><td><code>listShipments</code></td><td>List shipments with optional filters.</td></tr><tr><td>List Webhooks</td><td><code>listWebhooks</code></td><td>List webhook subscriptions.</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Mark As Shipped</td><td><code>markAsShipped</code></td><td>Mark an order as shipped with tracking info.</td></tr><tr><td>Subscribe Webhook</td><td><code>subscribeWebhook</code></td><td>Subscribe to a webhook event.</td></tr><tr><td>Unsubscribe Webhook</td><td><code>unsubscribeWebhook</code></td><td>Delete a webhook subscription by id.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Item Order Notify</td><td><code>ITEM_ORDER_NOTIFY</code></td><td>Fires for order item-level notifications.</td></tr><tr><td>Item Ship Notify</td><td><code>ITEM_SHIP_NOTIFY</code></td><td>Fires for shipment item-level notifications.</td></tr><tr><td>Order Notify</td><td><code>ORDER_NOTIFY</code></td><td>Fires when an order is created or imported into ShipStation.</td></tr><tr><td>Ship Notify</td><td><code>SHIP_NOTIFY</code></td><td>Fires when a shipment is created (label printed) for an order.</td></tr></tbody></table>
