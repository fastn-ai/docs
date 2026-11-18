---
description: "Chargify, now Maxio Advanced Billing, is a SaaS recurring billing and subscription management platform."
hidden: true
---

# Chargify (Maxio Advanced Billing)

<img src="../../.gitbook/assets/connectors/lg/chargify.png" alt="Chargify (Maxio Advanced Billing) logo">

Chargify, now Maxio Advanced Billing, is a SaaS recurring billing and subscription management platform. This connector covers subscriptions, customers, products, product families, components and metered usage, invoices, payment profiles, coupons, credit notes, events, and webhook subscriptions.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [chargify.com](https://chargify.com) |
| **Authentication** | Basic auth |
| **Slug** | `chargify` |

## Use it

Add Chargify (Maxio Advanced Billing) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.chargify.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Subscription | `activateSubscription` | Immediately activates a subscription that is currently in a trial or awaiting-signup state, ending the trial and beginning the paid period. |
| Allocate Component | `allocateComponent` | Sets the allocated quantity of a quantity-based or on/off component on a subscription. |
| Apply Coupon To Subscription | `applyCouponToSubscription` | Applies a coupon code to an existing subscription. |
| Archive Component | `archiveComponent` | Archives a billing component so it can no longer be added to new subscriptions. This is the platform's mechanism for deactivating a component; there is no hard delete. |
| Archive Coupon | `archiveCoupon` | Archives a coupon so it can no longer be applied to new or existing subscriptions. |
| Archive Product | `archiveProduct` | Archives a product so it can no longer be selected for new subscriptions. This is the platform's mechanism for deactivating a product; there is no hard delete. |
| Cancel Subscription | `cancelSubscription` | Cancels an active subscription immediately, ending its billing. |
| Create Coupon | `createCoupon` | Creates a new coupon within a product family, offering a percentage or fixed-amount discount. |
| Create Customer | `createCustomer` | Creates a new customer record used as the billing contact for subscriptions and payment profiles. |
| Create Endpoint | `createEndpoint` | Registers a webhook endpoint URL and subscribes it to a set of webhook event topics. |
| Create Invoice | `createInvoice` | Creates an ad-hoc invoice for a subscription from a list of custom line items. |
| Create Metered Component | `createMeteredComponent` | Creates a metered usage-based billing component within a product family, priced per unit consumed. |
| Create On/Off Component | `createOnOffComponent` | Creates an on/off billing component within a product family, a flat recurring charge that is either fully applied or not applied to a subscription. |
| Create Payment Profile | `createPaymentProfile` | Creates a payment profile (credit card or bank account) for a customer. Supports importing a token from the 'bogus' test vault for sandbox testing. |
| Create Product | `createProduct` | Creates a new product (pricing plan) inside a product family, defining its price, billing interval, and trial settings. |
| Create Product Family | `createProductFamily` | Creates a new product family, a top-level grouping used to organize related products, components, and coupons in the billing catalog. |
| Create Quantity-Based Component | `createQuantityBasedComponent` | Creates a quantity-based billing component within a product family, priced per unit allocated by the customer (e.g. number of seats). |
| Create Subscription | `createSubscription` | Creates a new subscription, signing up an existing or new customer to a product. |
| Create Usage | `createUsage` | Records metered usage against a metered billing component on a subscription. |
| Delete Customer | `deleteCustomer` | Deletes a customer record. The customer must have no active subscriptions. |
| Delete Unused Payment Profile | `deleteUnusedPaymentProfile` | Deletes a payment profile that is not currently assigned as the active payment method on any subscription. |
| Enable Webhooks | `enableWebhooks` | Enables or disables webhook delivery for the site. |
| Find Coupon By Code | `findCouponByCode` | Finds a coupon on the site by its unique code. |
| Issue Invoice | `issueInvoice` | Issues a draft or pending invoice, moving it into the open, collectible state. |
| List Chargify JS Public Keys | `listChargifyJsPublicKeys` | Lists the public keys used to tokenize payment details client-side with Maxio.js (formerly Chargify.js). |
| List Components | `listComponents` | Lists all billing components across every product family on the site. |
| List Components For Product Family | `listComponentsForProductFamily` | Lists all billing components (metered, quantity-based, or on/off) defined within a product family. |
| List Coupons For Product Family | `listCouponsForProductFamily` | Lists all coupons defined within a product family. |
| List Credit Notes | `listCreditNotes` | Lists credit notes issued on the site, with pagination. This sandbox site has no credit notes yet, so the response is a genuinely empty list rather than an unfiltered one; the sibling Invoices list endpoint was verified live to ignore customer_id/subscription_id filters, so those params are intentionally not exposed here. |
| List Customer Subscriptions | `listCustomerSubscriptions` | Lists every subscription that belongs to a given customer. |
| List Customers | `listCustomers` | Lists customers on the site, with pagination and optional filtering by email or organization. |
| List Endpoints | `listEndpoints` | Lists registered webhook endpoints and the event topics each is subscribed to. |
| List Events | `listEvents` | Lists site-wide billing events (subscription state changes, payments, renewals), with pagination and since-id filtering. |
| List Invoice Events | `listInvoiceEvents` | Lists the audit trail of events (issued, paid, voided, etc.) for a single invoice. |
| List Invoices | `listInvoices` | Lists invoices on the site, with pagination and an optional status filter. The API does not support filtering this endpoint by customer_id or subscription_id (verified live — those params are silently ignored); use List Customer Subscriptions plus Read Invoice, or List Invoice Events, to find a specific customer's or subscription's invoices. |
| List Payment Profiles | `listPaymentProfiles` | Lists payment profiles (stored credit cards or bank accounts) on the site, optionally filtered to a single customer. |
| List Product Families | `listProductFamilies` | Lists all product families (billing catalog groupings) configured on the Advanced Billing site, with pagination support. |
| List Products | `listProducts` | Lists all products across every product family on the site, with pagination and date filters. |
| List Products For Product Family | `listProductsForProductFamily` | Lists all products (pricing plans) that belong to a given product family. |
| List Subscription Components | `listSubscriptionComponents` | Lists the billing components currently allocated on a subscription, with their current allocated quantity. |
| List Subscription Events | `listSubscriptionEvents` | Lists billing events for a single subscription. |
| List Subscriptions | `listSubscriptions` | Lists subscriptions on the site, with pagination and optional filtering by state. |
| List Usages | `listUsages` | Lists recorded usage entries for a metered component on a subscription. |
| List Webhooks | `listWebhooks` | Lists the webhook delivery queue (attempted webhook payloads and their status), with filters by status and event id range. |
| Preview Subscription | `previewSubscription` | Previews the charges and proration that would result from creating a subscription, without actually creating it. |
| Reactivate Subscription | `reactivateSubscription` | Reactivates a canceled or expired subscription, optionally preserving its trial and balance. |
| Read Component | `readComponent` | Retrieves a single billing component by its numeric id. |
| Read Coupon | `readCoupon` | Retrieves a single coupon by its numeric id within a product family. |
| Read Credit Note | `readCreditNote` | Retrieves a single credit note by its unique id (uid). |
| Read Customer | `readCustomer` | Retrieves a single customer by their numeric id. |
| Read Customer By Reference | `readCustomerByReference` | Looks up a customer by the reference id assigned from your own system, instead of the Advanced Billing internal id. |
| Read Events Count | `readEventsCount` | Returns the total count of billing events on the site, optionally since a given event id. |
| Read Invoice | `readInvoice` | Retrieves a single invoice by its unique id (uid), including line items, payments, and applied taxes. |
| Read Payment Profile | `readPaymentProfile` | Retrieves a single payment profile by its numeric id. |
| Read Product | `readProduct` | Retrieves a single product (pricing plan) by its numeric id. |
| Read Product By Handle | `readProductByHandle` | Retrieves a single product by its unique handle instead of its numeric id. |
| Read Product Family | `readProductFamily` | Retrieves a single product family by its numeric id, including its name, handle, and accounting code. |
| Read Site | `readSite` | Retrieves the current site's settings, including currency, billing configuration, and organization details. |
| Read Subscription | `readSubscription` | Retrieves a single subscription by its numeric id, including its current product, customer, and billing state. |
| Read Subscription Component | `readSubscriptionComponent` | Retrieves the allocation detail for a single billing component on a subscription. |
| Record Payment For Invoice | `recordPaymentForInvoice` | Records an external (offline) payment against an invoice, such as a check or bank transfer. |
| Refund Invoice | `refundInvoice` | Issues a refund against a paid invoice, optionally voiding it in the same operation. |
| Remove Coupon From Subscription | `removeCouponFromSubscription` | Removes a previously applied coupon from a subscription. |
| Replay Webhooks | `replayWebhooks` | Re-sends previously delivered (or failed) webhook payloads by their id. |
| Send Invoice | `sendInvoice` | Delivers an invoice to the customer by email. |
| Update Component | `updateComponent` | Updates the name, description, or tax settings of an existing billing component. |
| Update Coupon | `updateCoupon` | Updates an existing coupon's name, description, or end date. |
| Update Customer | `updateCustomer` | Updates an existing customer's contact or billing address details. |
| Update Endpoint | `updateEndpoint` | Updates a registered webhook endpoint's URL or its subscribed event topics. |
| Update Invoice | `updateInvoice` | Updates a draft invoice's line items, dates, or memo before it is issued. |
| Update Payment Profile | `updatePaymentProfile` | Updates an existing payment profile's card expiration or billing address. |
| Update Product | `updateProduct` | Updates non-pricing attributes of an existing product, such as its name, description, or accounting code. |
| Update Subscription | `updateSubscription` | Updates an existing subscription's payment collection method, billing date, or coupon. |
| Validate Coupon | `validateCoupon` | Checks whether a coupon code is valid and currently usable, optionally scoped to a specific product. |
| Void Invoice | `voidInvoice` | Voids an open invoice, cancelling any amount due on it. |
