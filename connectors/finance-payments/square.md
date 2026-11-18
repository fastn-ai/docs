---
description: "Square commerce platform connector."
---

# Square

Square commerce platform connector. Take and manage payments, refunds, customers, catalog, orders, invoices, locations, payment links, and webhook subscriptions via Square's v2 REST API (Square-Version 2026-05-20). OAuth 2.0 primary auth; switchable sandbox/live host.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [squareup.com](https://squareup.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Actions** | 49 |
| **Events** | 12 |
| **Slug** | `square` |

## Use it

Add Square from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.square.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Upsert Catalog Objects | `batchUpsertCatalogObjects` | Create/update up to 10,000 catalog objects in batches. POST /v2/catalog/batch-upsert. |
| Calculate Order | `calculateOrder` | Calculate adjustments (taxes/discounts/totals) for an order without creating it. POST /v2/orders/calculate. |
| Cancel Invoice | `cancelInvoice` | Cancel a published invoice. POST /v2/invoices/{invoice_id}/cancel. |
| Cancel Payment | `cancelPayment` | Cancel (void) a payment with APPROVED status. POST /v2/payments/{payment_id}/cancel. |
| Clone Order | `cloneOrder` | Create a new draft order by duplicating an existing order. POST /v2/orders/clone. |
| Complete Payment | `completePayment` | Complete an APPROVED payment. POST /v2/payments/{payment_id}/complete. |
| Create Customer | `createCustomer` | Create a customer profile. POST /v2/customers. |
| Create Invoice | `createInvoice` | Create a draft invoice for an order. POST /v2/invoices. |
| Create Location | `createLocation` | Create a new location. POST /v2/locations. |
| Create Order | `createOrder` | Create a new order. POST /v2/orders. |
| Create Payment | `createPayment` | Create (take) a payment using a source (payment token or card on file). POST /v2/payments. |
| Create Payment Link | `createPaymentLink` | Create a Square Online checkout payment link. POST /v2/online-checkout/payment-links. |
| Create Refund | `createRefund` | Refund a payment. POST /v2/refunds. |
| Create Webhook Subscription | `createWebhookSubscription` | Create a webhook subscription. Uses the application Personal Access Token. POST /v2/webhooks/subscriptions. |
| Delete Catalog Object | `deleteCatalogObject` | Delete a catalog object and its children. DELETE /v2/catalog/object/{object_id}. |
| Delete Customer | `deleteCustomer` | Delete a customer profile. DELETE /v2/customers/{customer_id}. |
| Delete Invoice | `deleteInvoice` | Delete a draft invoice. DELETE /v2/invoices/{invoice_id}. |
| Delete Payment Link | `deletePaymentLink` | Delete a payment link. DELETE /v2/online-checkout/payment-links/{id}. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | Delete a webhook subscription. DELETE /v2/webhooks/subscriptions/{subscription_id}. |
| Get Customer | `getCustomer` | Retrieve a customer profile. GET /v2/customers/{customer_id}. |
| Get Invoice | `getInvoice` | Retrieve an invoice by id. GET /v2/invoices/{invoice_id}. |
| Get Location | `getLocation` | Retrieve a single location by id (use 'main' for the main location). GET /v2/locations/{location_id}. |
| Get Payment | `getPayment` | Retrieve details for a specific payment. GET /v2/payments/{payment_id}. |
| Get Payment Link | `getPaymentLink` | Retrieve a payment link by id. GET /v2/online-checkout/payment-links/{id}. |
| Get Refund | `getRefund` | Retrieve a specific refund. GET /v2/refunds/{refund_id}. |
| Get Webhook Subscription | `getWebhookSubscription` | Retrieve a webhook subscription by id. GET /v2/webhooks/subscriptions/{subscription_id}. |
| List Catalog | `listCatalog` | List catalog objects of given types. GET /v2/catalog/list. |
| List Customers | `listCustomers` | List customer profiles. GET /v2/customers. |
| List Invoices | `listInvoices` | List invoices for a location. GET /v2/invoices. |
| List Locations | `listLocations` | List all locations for the merchant. GET /v2/locations. |
| List Payment Links | `listPaymentLinks` | List Square Online checkout payment links. GET /v2/online-checkout/payment-links. |
| List Payments | `listPayments` | List payments taken by the account. GET /v2/payments. Supports begin_time, end_time, location_id, cursor, limit. |
| List Refunds | `listRefunds` | List refunds for the account. GET /v2/refunds. |
| List Webhook Event Types | `listWebhookEventTypes` | List all webhook event types that can be subscribed to. GET /v2/webhooks/event-types. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | List webhook subscriptions owned by the application. GET /v2/webhooks/subscriptions. |
| Pay Order | `payOrder` | Pay for an order using payment ids. POST /v2/orders/{order_id}/pay. |
| Publish Invoice | `publishInvoice` | Publish a draft invoice (sends per delivery method). POST /v2/invoices/{invoice_id}/publish. |
| Retrieve Catalog Object | `retrieveCatalogObject` | Retrieve a single catalog object by id, optionally with related objects. GET /v2/catalog/object/{object_id}. |
| Retrieve Order | `retrieveOrder` | Retrieve a single order by id. GET /v2/orders/{order_id}. |
| Search Catalog Objects | `searchCatalogObjects` | Search catalog objects with structured queries. POST /v2/catalog/search. |
| Search Customers | `searchCustomers` | Search customers with filters/sorting. POST /v2/customers/search. |
| Search Orders | `searchOrders` | Search orders across locations with filters/sort. POST /v2/orders/search. |
| Test Webhook Subscription | `testWebhookSubscription` | Send a test event to a webhook subscription's notification URL. POST /v2/webhooks/subscriptions/{subscription_id}/test. |
| Update Customer | `updateCustomer` | Update a customer profile. PUT /v2/customers/{customer_id}. |
| Update Invoice | `updateInvoice` | Update a draft invoice. PUT /v2/invoices/{invoice_id}. |
| Update Order | `updateOrder` | Update an open order (add/remove line items, fields). PUT /v2/orders/{order_id}. |
| Update Payment Link | `updatePaymentLink` | Update a payment link. PUT /v2/online-checkout/payment-links/{id}. |
| Update Webhook Subscription | `updateWebhookSubscription` | Update a webhook subscription (name, event types, url, enabled). PUT /v2/webhooks/subscriptions/{subscription_id}. |
| Upsert Catalog Object | `upsertCatalogObject` | Create or update a catalog object (item, variation, etc.). POST /v2/catalog/object. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Catalog Version Updated | `catalog.version.updated` | The catalog version changed (any catalog object created/updated/deleted). |
| Customer Created | `customer.created` | A customer profile was created. |
| Customer Updated | `customer.updated` | A customer profile was updated. |
| Invoice Payment Made | `invoice.payment_made` | A payment was made against an invoice. |
| Invoice Published | `invoice.published` | An invoice was published. |
| Order Created | `order.created` | An order was created. |
| Order Fulfillment Updated | `order.fulfillment.updated` | An order fulfillment state changed. |
| Order Updated | `order.updated` | An order was updated. |
| Payment Created | `payment.created` | A payment was created. |
| Payment Updated | `payment.updated` | A payment changed status (e.g. completed). |
| Refund Created | `refund.created` | A refund was created. |
| Refund Updated | `refund.updated` | A refund changed status. |
