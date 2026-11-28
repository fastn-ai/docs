---
description: "Square is a commerce and payments platform. Manage payments, orders, invoices, customers and catalog items."
hidden: true
---

# Square

<img src="../../.gitbook/assets/connectors/lg/square.png" alt="Square logo">

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [squareup.com](https://squareup.com) |
| **Authentication** | Access token, OAuth 2.0 |
| **Slug** | `square` |

## Setup

Your customers sign in to Square through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Square from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Square**.
2. Select **Connect** on the Square card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Square offers more than one sign-in method. Choose one in **Auth Method**, then:

   * For a key or credential method, fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

     <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

   * For OAuth 2.0, keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Square and approve access in the window that opens.

     <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Square's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Upsert Catalog Objects</td><td><code>batchUpsertCatalogObjects</code></td><td>Create/update up to 10,000 catalog objects in batches.</td></tr><tr><td>Calculate Order</td><td><code>calculateOrder</code></td><td>Calculate adjustments (taxes/discounts/totals) for an order without creating it.</td></tr><tr><td>Cancel Invoice</td><td><code>cancelInvoice</code></td><td>Cancel a published invoice.</td></tr><tr><td>Cancel Payment</td><td><code>cancelPayment</code></td><td>Cancel (void) a payment with APPROVED status.</td></tr><tr><td>Clone Order</td><td><code>cloneOrder</code></td><td>Create a new draft order by duplicating an existing order.</td></tr><tr><td>Complete Payment</td><td><code>completePayment</code></td><td>Complete an APPROVED payment.</td></tr><tr><td>Create Customer</td><td><code>createCustomer</code></td><td>Create a customer profile.</td></tr><tr><td>Create Invoice</td><td><code>createInvoice</code></td><td>Create a draft invoice for an order.</td></tr><tr><td>Create Location</td><td><code>createLocation</code></td><td>Create a new location.</td></tr><tr><td>Create Order</td><td><code>createOrder</code></td><td>Create a new order.</td></tr></tbody></table>

<details>

<summary>View 39 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Payment</td><td><code>createPayment</code></td><td>Create (take) a payment using a source (payment token or card on file).</td></tr><tr><td>Create Payment Link</td><td><code>createPaymentLink</code></td><td>Create a Square Online checkout payment link.</td></tr><tr><td>Create Refund</td><td><code>createRefund</code></td><td>Refund a payment.</td></tr><tr><td>Create Webhook Subscription</td><td><code>createWebhookSubscription</code></td><td>Create a webhook subscription. Uses the application Personal Access Token.</td></tr><tr><td>Delete Catalog Object</td><td><code>deleteCatalogObject</code></td><td>Delete a catalog object and its children.</td></tr><tr><td>Delete Customer</td><td><code>deleteCustomer</code></td><td>Delete a customer profile.</td></tr><tr><td>Delete Invoice</td><td><code>deleteInvoice</code></td><td>Delete a draft invoice.</td></tr><tr><td>Delete Payment Link</td><td><code>deletePaymentLink</code></td><td>Delete a payment link.</td></tr><tr><td>Delete Webhook Subscription</td><td><code>deleteWebhookSubscription</code></td><td>Delete a webhook subscription.</td></tr><tr><td>Get Customer</td><td><code>getCustomer</code></td><td>Retrieve a customer profile.</td></tr><tr><td>Get Invoice</td><td><code>getInvoice</code></td><td>Retrieve an invoice by id.</td></tr><tr><td>Get Location</td><td><code>getLocation</code></td><td>Retrieve a single location by id (use 'main' for the main location).</td></tr><tr><td>Get Payment</td><td><code>getPayment</code></td><td>Retrieve details for a specific payment.</td></tr><tr><td>Get Payment Link</td><td><code>getPaymentLink</code></td><td>Retrieve a payment link by id.</td></tr><tr><td>Get Refund</td><td><code>getRefund</code></td><td>Retrieve a specific refund.</td></tr><tr><td>Get Webhook Subscription</td><td><code>getWebhookSubscription</code></td><td>Retrieve a webhook subscription by id.</td></tr><tr><td>List Catalog</td><td><code>listCatalog</code></td><td>List catalog objects of given types.</td></tr><tr><td>List Customers</td><td><code>listCustomers</code></td><td>List customer profiles.</td></tr><tr><td>List Invoices</td><td><code>listInvoices</code></td><td>List invoices for a location.</td></tr><tr><td>List Locations</td><td><code>listLocations</code></td><td>List all locations for the merchant.</td></tr><tr><td>List Payment Links</td><td><code>listPaymentLinks</code></td><td>List Square Online checkout payment links.</td></tr><tr><td>List Payments</td><td><code>listPayments</code></td><td>List payments taken by the account. Supports begin_time, end_time, location_id, cursor, limit.</td></tr><tr><td>List Refunds</td><td><code>listRefunds</code></td><td>List refunds for the account.</td></tr><tr><td>List Webhook Event Types</td><td><code>listWebhookEventTypes</code></td><td>List all webhook event types that can be subscribed to.</td></tr><tr><td>List Webhook Subscriptions</td><td><code>listWebhookSubscriptions</code></td><td>List webhook subscriptions owned by the application.</td></tr><tr><td>Pay Order</td><td><code>payOrder</code></td><td>Pay for an order using payment ids.</td></tr><tr><td>Publish Invoice</td><td><code>publishInvoice</code></td><td>Publish a draft invoice (sends per delivery method).</td></tr><tr><td>Retrieve Catalog Object</td><td><code>retrieveCatalogObject</code></td><td>Retrieve a single catalog object by id, optionally with related objects.</td></tr><tr><td>Retrieve Order</td><td><code>retrieveOrder</code></td><td>Retrieve a single order by id.</td></tr><tr><td>Search Catalog Objects</td><td><code>searchCatalogObjects</code></td><td>Search catalog objects with structured queries.</td></tr><tr><td>Search Customers</td><td><code>searchCustomers</code></td><td>Search customers with filters/sorting.</td></tr><tr><td>Search Orders</td><td><code>searchOrders</code></td><td>Search orders across locations with filters/sort.</td></tr><tr><td>Test Webhook Subscription</td><td><code>testWebhookSubscription</code></td><td>Send a test event to a webhook subscription's notification URL.</td></tr><tr><td>Update Customer</td><td><code>updateCustomer</code></td><td>Update a customer profile.</td></tr><tr><td>Update Invoice</td><td><code>updateInvoice</code></td><td>Update a draft invoice.</td></tr><tr><td>Update Order</td><td><code>updateOrder</code></td><td>Update an open order (add/remove line items, fields).</td></tr><tr><td>Update Payment Link</td><td><code>updatePaymentLink</code></td><td>Update a payment link.</td></tr><tr><td>Update Webhook Subscription</td><td><code>updateWebhookSubscription</code></td><td>Update a webhook subscription (name, event types, url, enabled).</td></tr><tr><td>Upsert Catalog Object</td><td><code>upsertCatalogObject</code></td><td>Create or update a catalog object (item, variation, etc.).</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Catalog Version Updated</td><td><code>catalog.version.updated</code></td><td>The catalog version changed (any catalog object created/updated/deleted).</td></tr><tr><td>Customer Created</td><td><code>customer.created</code></td><td>A customer profile was created.</td></tr><tr><td>Customer Updated</td><td><code>customer.updated</code></td><td>A customer profile was updated.</td></tr><tr><td>Invoice Payment Made</td><td><code>invoice.payment_made</code></td><td>A payment was made against an invoice.</td></tr><tr><td>Invoice Published</td><td><code>invoice.published</code></td><td>An invoice was published.</td></tr><tr><td>Order Created</td><td><code>order.created</code></td><td>An order was created.</td></tr><tr><td>Order Fulfillment Updated</td><td><code>order.fulfillment.updated</code></td><td>An order fulfillment state changed.</td></tr><tr><td>Order Updated</td><td><code>order.updated</code></td><td>An order was updated.</td></tr><tr><td>Payment Created</td><td><code>payment.created</code></td><td>A payment was created.</td></tr><tr><td>Payment Updated</td><td><code>payment.updated</code></td><td>A payment changed status (e.g. completed).</td></tr></tbody></table>

<details>

<summary>View 2 more events</summary>

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Refund Created</td><td><code>refund.created</code></td><td>A refund was created.</td></tr><tr><td>Refund Updated</td><td><code>refund.updated</code></td><td>A refund changed status.</td></tr></tbody></table>

</details>
