---
description: "Stripe is an online payments platform. Manage customers, payment intents, payment methods, subscriptions and checkout sessions."
hidden: true
---

# Stripe

<img src="../../.gitbook/assets/connectors/lg/stripe.png" alt="Stripe logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [stripe.com](https://stripe.com) |
| **Authentication** | Access token |
| **Slug** | `stripe` |

## Setup

Your customers enter their access token for Stripe when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Stripe from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Stripe**.
2. Select **Connect** on the Stripe card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Stripe's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Advance Test Clock</td><td><code>advanceTestClock</code></td><td>Advance a Stripe test clock to a future timestamp</td></tr><tr><td>Attach Payment Method</td><td><code>attachPaymentMethod</code></td><td>Attach a payment method to a customer</td></tr><tr><td>Cancel Payment Intent</td><td><code>cancelPaymentIntent</code></td><td>Cancel a payment intent</td></tr><tr><td>Cancel Subscription</td><td><code>cancelSubscription</code></td><td>Cancel a subscription immediately</td></tr><tr><td>Capture Payment Intent</td><td><code>capturePaymentIntent</code></td><td>Capture an authorized payment intent</td></tr><tr><td>Confirm Payment Intent</td><td><code>confirmPaymentIntent</code></td><td>Confirm a payment intent</td></tr><tr><td>Create Checkout Session</td><td><code>createCheckoutSession</code></td><td>Create a Checkout Session with a single line item</td></tr><tr><td>Create Customer</td><td><code>createCustomer</code></td><td>Create a customer</td></tr><tr><td>Create Customer On Clock</td><td><code>createCustomerOnClock</code></td><td>Create a customer on a test clock</td></tr><tr><td>Create Invoice</td><td><code>createInvoice</code></td><td>Create a draft invoice for a customer</td></tr></tbody></table>

<details>

<summary>View 37 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Invoice For Customer</td><td><code>createInvoiceForCustomer</code></td><td>Create an invoice for a customer</td></tr><tr><td>Create Invoice Item</td><td><code>createInvoiceItem</code></td><td>Create an invoice item</td></tr><tr><td>Create Invoice Item Fixed</td><td><code>createInvoiceItemFixed</code></td><td>Create an invoice item</td></tr><tr><td>Create Payment Intent</td><td><code>createPaymentIntent</code></td><td>Create a payment intent</td></tr><tr><td>Create Price</td><td><code>createPrice</code></td><td>Create a price for a product</td></tr><tr><td>Create Product</td><td><code>createProduct</code></td><td>Create a product</td></tr><tr><td>Create Recurring Price</td><td><code>createPriceRecurring</code></td><td>Create a recurring price</td></tr><tr><td>Create Refund</td><td><code>createRefund</code></td><td>Refund a charge or payment intent</td></tr><tr><td>Create Subscription</td><td><code>createSubscription</code></td><td>Create a subscription Provide a single price via priceId.</td></tr><tr><td>Create Subscription Custom</td><td><code>createSubCustom</code></td><td>Create a subscription with customer and price</td></tr><tr><td>Create Webhook Endpoint</td><td><code>createWebhookEndpoint</code></td><td>Create a webhook endpoint subscribed to a single event Used by the webhook config.</td></tr><tr><td>Delete Customer</td><td><code>deleteCustomer</code></td><td>Delete a customer</td></tr><tr><td>Delete Webhook Endpoint</td><td><code>deleteWebhookEndpoint</code></td><td>Delete a webhook endpoint</td></tr><tr><td>Finalize Invoice</td><td><code>finalizeInvoice</code></td><td>Finalize a draft invoice</td></tr><tr><td>Get Balance</td><td><code>getBalance</code></td><td>Retrieve the account balance</td></tr><tr><td>Get Charge</td><td><code>getCharge</code></td><td>Retrieve a charge</td></tr><tr><td>Get Checkout Session</td><td><code>getCheckoutSession</code></td><td>Retrieve a Checkout Session</td></tr><tr><td>Get Customer</td><td><code>getCustomer</code></td><td>Retrieve a customer</td></tr><tr><td>Get Event</td><td><code>getEvent</code></td><td>Retrieve a Stripe event</td></tr><tr><td>Get Payment Intent</td><td><code>getPaymentIntent</code></td><td>Retrieve a payment intent</td></tr><tr><td>Get Subscription</td><td><code>getSubscription</code></td><td>Retrieve a subscription</td></tr><tr><td>List Charges</td><td><code>listCharges</code></td><td>List charges</td></tr><tr><td>List Customers</td><td><code>listCustomers</code></td><td>List customers</td></tr><tr><td>List Events</td><td><code>listEvents</code></td><td>List Stripe events</td></tr><tr><td>List Invoices</td><td><code>listInvoices</code></td><td>List invoices</td></tr><tr><td>List Payment Intents</td><td><code>listPaymentIntents</code></td><td>List payment intents</td></tr><tr><td>List Payouts</td><td><code>listPayouts</code></td><td>List payouts</td></tr><tr><td>List Prices</td><td><code>listPrices</code></td><td>List prices</td></tr><tr><td>List Products</td><td><code>listProducts</code></td><td>List products</td></tr><tr><td>List Refunds</td><td><code>listRefunds</code></td><td>List refunds</td></tr><tr><td>List Subscriptions</td><td><code>listSubscriptions</code></td><td>List subscriptions</td></tr><tr><td>List Webhook Endpoints</td><td><code>listWebhookEndpoints</code></td><td>List webhook endpoints</td></tr><tr><td>Pay Invoice</td><td><code>payInvoice</code></td><td>Pay an invoice</td></tr><tr><td>Pay Invoice With Method</td><td><code>payInvoiceWithMethod</code></td><td>Pay an invoice with a specific payment method</td></tr><tr><td>Search Customers</td><td><code>searchCustomers</code></td><td>Search customers with a query</td></tr><tr><td>Update Customer</td><td><code>updateCustomer</code></td><td>Update a customer</td></tr><tr><td>Update Customer Invoice Settings</td><td><code>updateCustomerInvoiceSettings</code></td><td>Update default payment method on customer invoice settings</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Charge Refunded</td><td><code>charge.refunded</code></td><td>A charge was refunded.</td></tr><tr><td>Charge Succeeded</td><td><code>charge.succeeded</code></td><td>A charge succeeded.</td></tr><tr><td>Checkout Completed</td><td><code>checkout.session.completed</code></td><td>A Checkout Session completed.</td></tr><tr><td>Checkout Expired</td><td><code>checkout.session.expired</code></td><td>A Checkout Session expired.</td></tr><tr><td>Invoice Paid</td><td><code>invoice.paid</code></td><td>An invoice was paid.</td></tr><tr><td>Invoice Payment Failed</td><td><code>invoice.payment_failed</code></td><td>An invoice payment failed.</td></tr><tr><td>Payment Intent Failed</td><td><code>payment_intent.payment_failed</code></td><td>A PaymentIntent failed.</td></tr><tr><td>Payment Intent Succeeded</td><td><code>payment_intent.succeeded</code></td><td>A PaymentIntent successfully completed.</td></tr><tr><td>Payout Paid</td><td><code>payout.paid</code></td><td>A payout was paid out.</td></tr><tr><td>Refund Created</td><td><code>refund.created</code></td><td>A refund was created.</td></tr></tbody></table>

<details>

<summary>View 3 more events</summary>

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Subscription Canceled</td><td><code>customer.subscription.deleted</code></td><td>A subscription was canceled.</td></tr><tr><td>Subscription Created</td><td><code>customer.subscription.created</code></td><td>A subscription was created.</td></tr><tr><td>Subscription Updated</td><td><code>customer.subscription.updated</code></td><td>A subscription changed.</td></tr></tbody></table>

</details>
