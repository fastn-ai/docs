---
description: "Goody corporate gifting platform."
hidden: true
---

# Goody

<img src="../../.gitbook/assets/connectors/lg/goody.png" alt="Goody logo">

Goody corporate gifting platform. Browse the Goody catalog (products, brands, categories, greeting cards, collections), price and create gift order batches, track orders and shipments, manage payment methods, and register webhook endpoints for order and order-batch events. Supports both the Goody Automation API and Commerce API on the production and sandbox environments.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [ongoody.com](https://ongoody.com) |
| **Authentication** | API key |
| **Slug** | `goody` |

## Use it

Add Goody from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.goody.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Calculate Order Batch Price | `calculateOrderBatchPrice` | Calculate what a Goody order batch would cost before creating it, given a cart, a recipient list and a send method. Returns the per-recipient product, shipping, processing-fee and estimated-tax breakdown in cents plus the estimated group total. This is a read-only price quote: it never creates an order, charges a card or notifies a recipient. |
| Cancel Order | `cancelOrder` | Cancel a Goody order that the recipient has not yet accepted, releasing the hold on the payment method and firing the order.canceled webhook. Returns 404 with {"error":"Order not found"} for an unknown order id. |
| Create Commerce User Payment Method | `createCommerceUserPaymentMethod` | Commerce API only. Save a credit card for one of your application's end users after they enter it into Goody's embedded payment form, which returns an interim card key. The returned payment method id is then used as payment_method_id, together with the same commerce_end_user_id, when creating an order batch. Requires a Commerce API key; an Automation API key is rejected with 401 {"error":"Not authorized"}. |
| Create Order Batch | `createOrderBatch` | Send a Goody gift: create an order batch that charges the account's payment method and delivers to every recipient. SPENDS REAL MONEY AND NOTIFIES REAL RECIPIENTS - with send_method email_and_link Goody emails each recipient, and with direct_send it ships a physical item. Call Calculate Order Batch Price first to confirm the cost. Ten or fewer recipients are created synchronously with orders_preview populated; more than ten, or a scheduled_send_on in the future, returns send_status pending. Use customer_reference_id as an idempotency key to prevent duplicate sends. |
| Create Webhook Endpoint | `createWebhookEndpoint` | Register a URL to receive Goody order and order-batch webhooks, optionally limited to specific event types. Webhooks are delivered by Svix and fire for every order in the organization, so the API key must belong to an organization admin. Returns 201 with the new endpoint id, which Delete Webhook Endpoint takes. |
| Delete Webhook Endpoint | `deleteWebhookEndpoint` | Remove a registered Goody webhook endpoint by its id so it stops receiving order and order-batch events. Returns 204 with an empty body on success; a second delete of the same id returns 400 with {"error":"Webhook endpoint not found"}. |
| List Brands | `listBrands` | List every brand active in the Goody catalog, paginated. Each brand carries its id, name, logo image, shipping price and whether it ships internationally. Filter by country_code to see the brands available for recipients in that country. |
| List Catalog Categories | `listCatalogCategories` | List the Goody catalog browse categories and occasions, such as All, New, Best Sellers, Employee Appreciation and seasonal collections. Each entry carries its id, display name, slug, inline SVG icon and whether it is featured. The endpoint returns the complete set in one response and accepts no pagination or filter parameters. Undocumented endpoint, verified live against the Goody API. |
| List Collections | `listCollections` | List the curated product collections across every Goody workspace the API key can access. Automation API only. Set published to true to return only collections that have a published version. Collections are authored in the Goody web app; there is no API to create one. |
| List Greeting Cards | `listGreetingCards` | List the digital greeting cards available to attach to a Goody gift, paginated. Use a returned card id as the card_id when creating an order batch; a card is required whenever a gift message is supplied. |
| List Order Activities | `listOrderActivities` | List Goody order activity events across the account, newest first, with optional time-window and status filters. Use it to poll for order lifecycle changes such as gift opened, accepted, shipped, delivered, canceled or refunded when webhooks are not in use. |
| List Order Batches | `listOrderBatches` | List the Goody order batches on the account, paginated. An order batch groups the orders created by one send: it carries the sender name, message, cart, send method, send status and a preview of the first ten orders. |
| List Orders | `listOrders` | List the Goody orders on the account, paginated, optionally restricted to a creation-time window. Each order is one gift to one recipient and carries its status, recipient, gift link, shipments and the order batch it belongs to. |
| List Payment Methods | `listPaymentMethods` | List the payment methods available on the Goody account, such as saved credit cards, invoicing and account balance. Use a returned id as the payment_method_id when creating an order batch; if the account has no payment methods, order batch creation fails with "Payment method not found". |
| List Products | `listProducts` | List every product active in the Goody gift catalog, paginated. Each product carries its id, name, brand, description, price in cents, variants, images, shipping country groups and status. Use a returned product id as the cart item product_id when pricing or creating an order batch. |
| List Workspaces | `listWorkspaces` | List every Goody workspace the API key has access to. Use a returned workspace id as the workspace_id when creating an order batch; if omitted, Goody creates the batch in the oldest accessible workspace. |
| Retrieve Collection | `retrieveCollection` | Retrieve one curated Goody collection by id, including its published version. To reach the products in a collection, traverse published_version &gt; collection_categories &gt; collection_products &gt; product. Automation API only. Returns 404 with {"error":"Collection not found"} when the id does not exist. |
| Retrieve Current User | `retrieveCurrentUser` | Retrieve the Goody user account that owns the API key, including the account email, display name, and which optional capabilities (smart links, email lookup) are enabled. Use it to verify that a Goody connection is valid. |
| Retrieve Order | `retrieveOrder` | Retrieve one Goody order by id, including its lifecycle status, recipient, sender, cart, gift link, thank-you note, expiration and shipment tracking. Returns 404 with {"error":"Order not found"} for an unknown id. |
| Retrieve Order Batch | `retrieveOrderBatch` | Retrieve one Goody order batch by id, including its send status, cart, greeting card, payment method and the preview of the first ten orders. Poll this endpoint to learn when a batch of more than ten recipients, or a scheduled batch, has finished creating its orders. Returns 404 with {"error":"Order batch not found"} for an unknown id. |
| Retrieve Orders For Order Batch | `retrieveOrdersForOrderBatch` | Page through every order created by one Goody order batch. Use this instead of the batch's orders_preview field whenever a batch has more than ten recipients. Returns 404 with {"error":"Order batch not found"} for an unknown batch id. |
| Retrieve Product | `retrieveProduct` | Retrieve one Goody catalog product by its id, including brand, full recipient-facing description, price in cents, variants and variant groups, images, restricted states and shipping country groups. Returns 404 with {"error":"Product not found"} when the id does not exist. |
| Retrieve Recipients For Order Batch | `retrieveRecipientsForOrderBatch` | Page through the recipients attached to one Goody order batch, including each recipient's name, email, phone and mailing address as submitted. Returns 404 with {"error":"Order batch not found"} for an unknown batch id. |
| Update Order Expiration | `updateOrderExpiration` | Change the date and time at which an unaccepted Goody gift expires, extending or shortening how long the recipient has to accept it. Returns 404 with {"error":"Order not found"} for an unknown order id. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Gift Accepted | `order.gift_accepted` | Emitted when a recipient accepts a Goody gift and the final costs are calculated. is_swapped shows whether they swapped, and cart shows what they swapped to. Payload schema modelled from Goody's documented sample on https://developer.ongoody.com/webhooks/events/order.gift_accepted. |
| Gift Opened | `order.gift_opened` | Emitted when a Goody gift is first opened by the recipient. Opening the gift link yourself also triggers it. Order status reads 'opened'. Payload schema modelled from Goody's documented sample on https://developer.ongoody.com/webhooks/events/order.gift_opened. |
| Order Batch Completed | `order_batch.completed` | Emitted when an order batch has finished processing and every recipient's order exists. For scheduled batches this fires at the scheduled send time. NOTE: Goody's documented sample carries the legacy value 'gift_batch.completed' in the event_type field even though the subscription API takes 'order_batch.completed'. Payload schema modelled from https://developer.ongoody.com/webhooks/events/order_batch.completed. |
| Order Batch Created | `order_batch.created` | Emitted when an order batch is created in the organization. Batches of ten or fewer recipients arrive with every order already present; larger or scheduled batches arrive with none. NOTE: Goody's documented sample carries the legacy value 'gift_batch.created' in the event_type field even though the subscription API takes 'order_batch.created'. Payload schema modelled from https://developer.ongoody.com/webhooks/events/order_batch.created. |
| Order Canceled | `order.canceled` | Emitted when a Goody order is canceled, for example via the Cancel Order action. Payload schema modelled from Goody's documented sample on https://developer.ongoody.com/webhooks/events/order.canceled. |
| Order Created | `order.created` | Emitted when a Goody order is created and the gift is ready to be opened and accepted. The individual_gift_link is populated. Payload schema modelled from Goody's documented sample on https://developer.ongoody.com/webhooks/events/order.created (not captured live: sending a real order spends money). |
| Order Delivered | `order.delivered` | Emitted when a Goody order is fully delivered. For multi-shipment orders this fires once every shipment is delivered. Payload schema modelled from Goody's documented sample on https://developer.ongoody.com/webhooks/events/order.delivered. |
| Order Refunded | `order.refunded` | Emitted when a Goody order is refunded. The amounts object carries the final settled figures in cents. Payload schema modelled from Goody's documented sample on https://developer.ongoody.com/webhooks/events/order.refunded. |
| Order Shipped | `order.shipped` | Emitted when a Goody order ships. For multi-shipment orders this fires when the first shipment is in transit, and the shipments array may still be incomplete. Payload schema modelled from Goody's documented sample on https://developer.ongoody.com/webhooks/events/order.shipped. |
| Thank You Note Added | `order.thank_you_note_added` | Emitted when a recipient adds a thank-you note after accepting a Goody gift. The note text is on data.thank_you_note. Payload schema modelled from Goody's documented sample on https://developer.ongoody.com/webhooks/events/order.thank_you_note_added. |
