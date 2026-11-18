---
description: "Stripe API (base https://api.stripe.com)."
hidden: true
---

# Stripe

<img src="../../.gitbook/assets/connectors/stripe.png" alt="Stripe logo" width="64">

Stripe API (base https://api.stripe.com). Customers, payment intents, charges, refunds, products, prices, subscriptions, invoices, checkout sessions, payouts, balance, events, and webhook endpoints. Auth: Bearer secret key (sk_...). Write requests use application/x-www-form-urlencoded.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [stripe.com](https://stripe.com) |
| **Authentication** | Bearer token |
| **Slug** | `stripe` |

## Use it

Add Stripe from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.stripe.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Advance Test Clock | `advanceTestClock` | Advance a Stripe test clock to a future timestamp (POST /v1/test_helpers/test_clocks/{id}/advance). |
| Attach Payment Method | `attachPaymentMethod` | Attach a payment method to a customer (POST /v1/payment_methods/{id}/attach). |
| Cancel Payment Intent | `cancelPaymentIntent` | Cancel a payment intent (POST /v1/payment_intents/{id}/cancel). |
| Cancel Subscription | `cancelSubscription` | Cancel a subscription immediately (DELETE /v1/subscriptions/{id}). |
| Capture Payment Intent | `capturePaymentIntent` | Capture an authorized payment intent (POST /v1/payment_intents/{id}/capture). |
| Confirm Payment Intent | `confirmPaymentIntent` | Confirm a payment intent (POST /v1/payment_intents/{id}/confirm). |
| Create Checkout Session | `createCheckoutSession` | Create a Checkout Session with a single line item (POST /v1/checkout/sessions). |
| Create Customer | `createCustomer` | Create a customer (POST /v1/customers). |
| Create Customer On Clock | `createCustomerOnClock` | Create a customer on a test clock (POST /v1/customers). |
| Create Invoice | `createInvoice` | Create a draft invoice for a customer (POST /v1/invoices). |

<details>

<summary>See 37 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Invoice For Customer | `createInvoiceForCustomer` | Create an invoice for a customer (POST /v1/invoices). |
| Create Invoice Item | `createInvoiceItem` | Create an invoice item (POST /v1/invoice_items). |
| Create Invoice Item Fixed | `createInvoiceItemFixed` | Create an invoice item (POST /v1/invoiceitems). |
| Create Payment Intent | `createPaymentIntent` | Create a payment intent (POST /v1/payment_intents). |
| Create Price | `createPrice` | Create a price for a product (POST /v1/prices). |
| Create Product | `createProduct` | Create a product (POST /v1/products). |
| Create Recurring Price | `createPriceRecurring` | Create a recurring price (POST /v1/prices). |
| Create Refund | `createRefund` | Refund a charge or payment intent (POST /v1/refunds). |
| Create Subscription | `createSubscription` | Create a subscription (POST /v1/subscriptions). Provide a single price via priceId. |
| Create Subscription Custom | `createSubCustom` | Create a subscription with customer and price (POST /v1/subscriptions). |
| Create Webhook Endpoint | `createWebhookEndpoint` | Create a webhook endpoint subscribed to a single event (POST /v1/webhook_endpoints). Used by the webhook config. |
| Delete Customer | `deleteCustomer` | Delete a customer (DELETE /v1/customers/{id}). |
| Delete Webhook Endpoint | `deleteWebhookEndpoint` | Delete a webhook endpoint (DELETE /v1/webhook_endpoints/{id}). |
| Finalize Invoice | `finalizeInvoice` | Finalize a draft invoice (POST /v1/invoices/{id}/finalize). |
| Get Balance | `getBalance` | Retrieve the account balance (GET /v1/balance). |
| Get Charge | `getCharge` | Retrieve a charge (GET /v1/charges/{id}). |
| Get Checkout Session | `getCheckoutSession` | Retrieve a Checkout Session (GET /v1/checkout/sessions/{id}). |
| Get Customer | `getCustomer` | Retrieve a customer (GET /v1/customers/{id}). |
| Get Event | `getEvent` | Retrieve a Stripe event (GET /v1/events/{id}). |
| Get Payment Intent | `getPaymentIntent` | Retrieve a payment intent (GET /v1/payment_intents/{id}). |
| Get Subscription | `getSubscription` | Retrieve a subscription (GET /v1/subscriptions/{id}). |
| List Charges | `listCharges` | List charges (GET /v1/charges). |
| List Customers | `listCustomers` | List customers (GET /v1/customers). |
| List Events | `listEvents` | List Stripe events (GET /v1/events). |
| List Invoices | `listInvoices` | List invoices (GET /v1/invoices). |
| List Payment Intents | `listPaymentIntents` | List payment intents (GET /v1/payment_intents). |
| List Payouts | `listPayouts` | List payouts (GET /v1/payouts). |
| List Prices | `listPrices` | List prices (GET /v1/prices). |
| List Products | `listProducts` | List products (GET /v1/products). |
| List Refunds | `listRefunds` | List refunds (GET /v1/refunds). |
| List Subscriptions | `listSubscriptions` | List subscriptions (GET /v1/subscriptions). |
| List Webhook Endpoints | `listWebhookEndpoints` | List webhook endpoints (GET /v1/webhook_endpoints). |
| Pay Invoice | `payInvoice` | Pay an invoice (POST /v1/invoices/{id}/pay). |
| Pay Invoice With Method | `payInvoiceWithMethod` | Pay an invoice with a specific payment method (POST /v1/invoices/{id}/pay). |
| Search Customers | `searchCustomers` | Search customers with a query (GET /v1/customers/search). |
| Update Customer | `updateCustomer` | Update a customer (POST /v1/customers/{id}). |
| Update Customer Invoice Settings | `updateCustomerInvoiceSettings` | Update default payment method on customer invoice settings (POST /v1/customers/{id}). |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Charge Refunded | `charge.refunded` | A charge was refunded. |
| Charge Succeeded | `charge.succeeded` | A charge succeeded. |
| Checkout Completed | `checkout.session.completed` | A Checkout Session completed. |
| Checkout Expired | `checkout.session.expired` | A Checkout Session expired. |
| Invoice Paid | `invoice.paid` | An invoice was paid. |
| Invoice Payment Failed | `invoice.payment_failed` | An invoice payment failed. |
| Payment Intent Failed | `payment_intent.payment_failed` | A PaymentIntent failed. |
| Payment Intent Succeeded | `payment_intent.succeeded` | A PaymentIntent successfully completed. |
| Payout Paid | `payout.paid` | A payout was paid out. |
| Refund Created | `refund.created` | A refund was created. |

<details>

<summary>See 3 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Subscription Canceled | `customer.subscription.deleted` | A subscription was canceled. |
| Subscription Created | `customer.subscription.created` | A subscription was created. |
| Subscription Updated | `customer.subscription.updated` | A subscription changed. |

</details>
