---
description: "ShipStation V1 (ssapi) connector: orders (list/get/create/update/mark-shipped/delete), shipments (list/create label), carriers, products, customers, and…"
hidden: true
---

# ShipStation

ShipStation V1 (ssapi) connector: orders (list/get/create/update/mark-shipped/delete), shipments (list/create label), carriers, products, customers, and webhooks. HTTP Basic auth (API Key + API Secret). Base https://ssapi.shipstation.com.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [shipstation.com](https://shipstation.com) |
| **Authentication** | Basic auth |
| **Actions** | 13 |
| **Events** | 4 |
| **Slug** | `shipstation` |

## Use it

Add ShipStation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.shipstation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Label | `createLabel` | Create a shipping label for a shipment. |
| Create Or Update Order | `createOrder` | Create or update an order. Provide orderKey matching an existing order to update. |
| Delete Order | `deleteOrder` | Delete (inactivate) an order by id. |
| Get Order | `getOrder` | Get an order by id. |
| List Carriers | `listCarriers` | List carriers connected to the account. |
| List Customers | `listCustomers` | List customers. |
| List Orders | `listOrders` | List orders with optional filters. |
| List Products | `listProducts` | List products. |
| List Shipments | `listShipments` | List shipments with optional filters. |
| List Webhooks | `listWebhooks` | List webhook subscriptions. |
| Mark As Shipped | `markAsShipped` | Mark an order as shipped with tracking info. |
| Subscribe Webhook | `subscribeWebhook` | Subscribe to a webhook event. |
| Unsubscribe Webhook | `unsubscribeWebhook` | Delete a webhook subscription by id. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Item Order Notify | `ITEM_ORDER_NOTIFY` | Fires for order item-level notifications. |
| Item Ship Notify | `ITEM_SHIP_NOTIFY` | Fires for shipment item-level notifications. |
| Order Notify | `ORDER_NOTIFY` | Fires when an order is created or imported into ShipStation. |
| Ship Notify | `SHIP_NOTIFY` | Fires when a shipment is created (label printed) for an order. |
