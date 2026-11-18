---
description: "Billsby subscription billing and recurring payments."
hidden: true
---

# Billsby

Billsby subscription billing and recurring payments. Manage products, plans, cycles, customers, subscriptions, add-ons, allowances, feature tags, custom fields, invoices, credit notes, refunds, payment details and usage counters through the Billsby public REST API.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [billsby.com](https://billsby.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `billsby` |

## Use it

Add Billsby from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.billsby.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Feature Tags To Subscriptions | `addSubscriptionFeatureTags` | Adds one or more custom feature tags to one or more Billsby subscriptions, granting those subscriptions access to the matching features. |
| Add Subscription To Customer | `addSubscriptionToCustomer` | Starts a new subscription on an existing Billsby customer against a plan cycle. Billing begins immediately unless the cycle has a free trial, so only use a cycle you intend the customer to be charged for. |
| Cancel Subscription | `cancelSubscription` | Cancels a Billsby subscription so it stops renewing and no further invoices are raised. The customer record itself is kept. |
| Change Subscription Plan | `changeSubscriptionPlan` | Moves a Billsby subscription onto a different plan and cycle. Depending on the plan change type this can raise a pro-rata invoice immediately or issue a refund, so it can move real money. |
| Clear Customer Data For GDPR | `clearCustomerDataGdpr` | Anonymises a Billsby customer's personal data to satisfy a GDPR erasure request. The customer's billing history is retained but their identifying details are permanently scrubbed and cannot be restored. |
| Create Custom Field | `createCustomField` | Creates a custom field that can be added to a Billsby product's checkout to collect extra information from customers. |
| Create Customer | `createCustomer` | Creates a customer in Billsby without a subscription. Name, email and a full billing address are required. Card details are optional and, when supplied, must be a payment card token produced by the Billsby checkout - never a raw card number. |
| Create Cycle | `createCycle` | Creates one or more billing cycles on a Billsby plan and optionally attaches add-ons and allowances. A cycle defines the frequency, price, free trial and contract term customers are billed on. |
| Create One-Time Charge | `createOneTimeCharge` | Raises an ad-hoc invoice against a Billsby customer and attempts to collect it from their stored payment card. This charges the customer for real, so only run it for a charge you intend to take. |
| Create Plan | `createPlan` | Creates a new plan under an existing Billsby product. A plan defines the pricing model and feature tags; billing cycles are added separately with Create Cycle. |

<details>

<summary>See 48 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Product | `createProduct` | Creates a new product in the Billsby account. A product is the top-level container that holds plans and cycles. Name, billing currency and product type are required by the API. |
| Create Subscription For New Customer | `createSubscription` | Creates a new Billsby customer and their first subscription in a single call. Billing starts immediately unless the cycle has a free trial, so this charges the supplied payment card. Card details must be a token from the Billsby checkout, never a raw card number. |
| Delete Customer | `deleteCustomer` | Permanently deletes a Billsby customer and their subscription history. This cannot be undone, so use Clear Customer Data For GDPR instead when billing records must be retained. |
| Delete Feature Tag | `deleteFeatureTag` | Removes a custom feature tag from one Billsby subscription. The subscription id is required - the API rejects the call without it. |
| Get Add-On | `getAddOn` | Returns the configuration of a single Billsby add-on, including its name, pricing model and per-currency prices. |
| Get Allowance | `getAllowance` | Returns the configuration of a single Billsby allowance, including its included units, overage pricing and the counter it tracks. |
| Get Customer | `getCustomer` | Returns the full record of a single Billsby customer, including name, email, status, billing address, phone number and stored payment details summary. |
| Get Invoice | `getInvoice` | Returns a single Billsby invoice by its invoice number, including line items, tax, totals and payment status. This route is account-wide and does not take the company domain. |
| Get Product | `getProduct` | Returns the full configuration of a single Billsby product, including its display name, billing currency, visibility, address and checkout requirements and attached custom fields. |
| Get Subscription | `getSubscription` | Returns the full detail of a single Billsby subscription, including product, plan, cycle, units, status, free trial state and next renewal date. |
| Get Subscription Shipping Address | `getSubscriptionShippingAddress` | Returns the shipping address held against a Billsby subscription for products that collect one. |
| Get Usage Counter Value | `getCounterValue` | Returns the recorded value of a usage counter on a Billsby subscription between two dates, used for allowance and usage-based billing. |
| List Add-Ons | `listAddOns` | Returns every add-on configured in the Billsby account that can be attached to a plan or subscription. |
| List Allowances | `listAllowances` | Returns every allowance configured in the Billsby account that can be attached to a plan or subscription for usage-based billing. |
| List Company Credit Notes | `listCompanyCreditNotes` | Returns a paginated list of every credit note issued across the whole Billsby account, filterable by pending, paid and failed status. |
| List Company Invoices | `listCompanyInvoices` | Returns a paginated list of every invoice raised across the whole Billsby account, filterable by paid, unpaid, pending, paid-offline and written-off status. |
| List Custom Field Responses | `listCustomFieldResponses` | Returns the answers customers gave to a Billsby product's custom fields, filtered by product and customer. |
| List Custom Fields | `listCustomFields` | Returns every custom field defined in the Billsby account, with its type, label, options and whether it is compulsory at checkout. |
| List Customer Credit Notes | `listCustomerCreditNotes` | Returns every credit note issued to one Billsby customer, including credit note number, amount, currency and status. |
| List Customer Feature Tags | `listCustomerFeatureTags` | Returns the feature tags granted to a Billsby customer across all of their active subscriptions, so an application can gate features on them. |
| List Customer Invoices | `listCustomerInvoices` | Returns every invoice raised against one Billsby customer, including invoice number, amount, currency, status and the period it covers. |
| List Customer Payment Logs | `listCustomerPaymentLogs` | Returns the payment attempt log for one invoice belonging to a Billsby customer, including each attempt's date, amount, gateway response and outcome. |
| List Customer Subscriptions | `listCustomerSubscriptions` | Returns every subscription belonging to one Billsby customer, including subscription unique id, product, plan, cycle, status and renewal dates. |
| List Customers | `listCustomers` | Returns a paginated list of every customer in the Billsby account, including customer id, name, email, status and billing address. Optionally filter by a full or partial name with the search parameter. |
| List Plans | `listPlans` | Returns every plan configured under a Billsby product, including plan id, name, pricing model, visibility and the billing cycles attached to each plan. |
| List Products | `listProducts` | Returns a paginated list of the products configured in the Billsby account, including product id, name, display name, billing currency and visibility. |
| List Subscription Add-Ons | `listSubscriptionAddOns` | Returns the add-ons currently attached to one Billsby subscription, with their quantities and prices. |
| List Subscription Allowances | `listSubscriptionAllowances` | Returns the allowances currently attached to one Billsby subscription, with their included units and overage pricing. |
| List Subscription Event Logs | `listSubscriptionEventLogs` | Returns the paginated event log for one Billsby subscription, showing every lifecycle event such as creation, plan change, payment and cancellation. |
| List Subscription Feature Tags | `listSubscriptionFeatureTags` | Returns the combined list of feature tags active on one Billsby subscription, from both its plan and any custom tags added to it. |
| List Subscription Feature Tags By Source | `listSubscriptionFeatureTagsSplit` | Returns the feature tags on one Billsby subscription split into those inherited from the plan and those added as custom tags, so each source can be handled separately. |
| List Subscriptions | `listSubscriptions` | Returns a paginated list of every subscription in the Billsby account, filterable by active state, free trial state, product name and plan name. |
| Mark Invoice Paid Offline | `markInvoicePaidOffline` | Marks a Billsby invoice as settled outside Billsby, for example by bank transfer or cheque. This records the invoice as paid without taking a payment through the gateway. |
| Reattempt Credit Note Payment | `reattemptCreditNotePayment` | Retries paying out a Billsby credit note to the customer. This moves real money back to the customer, so only run it on a credit note you intend to settle. |
| Reattempt Invoice Payment | `reattemptInvoicePayment` | Retries collection of an unpaid Billsby invoice against the customer's stored payment card. This charges the customer's card for real, so only run it on an invoice you intend to collect. |
| Refund Invoice | `createRefund` | Refunds all or part of a paid Billsby invoice back to the customer's payment card and raises a credit note. This moves real money, so only run it for a refund you intend to make. |
| Request Payment Details Update | `requestPaymentDetailsUpdate` | Asks Billsby to email the customer a secure link inviting them to update their stored payment card. This sends a real email to the customer's registered address. |
| Update Custom Field | `updateCustomField` | Updates the label, helper text, dropdown options or compulsory flag of an existing Billsby custom field. The field type cannot be changed. |
| Update Custom Field Response | `updateCustomFieldResponse` | Replaces the answer a customer gave to one Billsby custom field. |
| Update Customer | `updateCustomer` | Updates a Billsby customer's name, email, phone number and billing address. The API requires the full name, email and billing address on every call, so send the current values for any field you are not changing. |
| Update Next Renewal Date | `updateNextRenewalDate` | Moves the next renewal date of a Billsby subscription, or pauses the subscription indefinitely. Extending the date delays the next invoice. |
| Update Payment Card Token | `updatePaymentCard` | Replaces the tokenised payment card stored against a Billsby customer. The token must already exist in Billsby, created by the Billsby checkout - raw card numbers are never accepted here. |
| Update Plan And Cycle | `updatePlan` | Updates an existing Billsby plan and, optionally, the billing cycles on it. Supply every cycle you want to keep visible: the API resets the visibility of any cycle you omit to Off sale. |
| Update Plan Order | `updatePlanOrder` | Sets the order the plans of a Billsby product are displayed in during checkout, using the supplied sequence of plan ids. |
| Update Product | `updateProduct` | Updates an existing Billsby product. Only the fields supplied are sent, so omitted fields keep their current values. |
| Update Subscription Shipping Address | `updateSubscriptionShippingAddress` | Replaces the shipping address held against a Billsby subscription. Every address line supplied overwrites the stored value. |
| Update Usage Counter | `updateCounter` | Records usage against a counter on a Billsby subscription by incrementing, decrementing or setting its value. Usage recorded here drives allowance overage charges on the next invoice. |
| Write Off Invoice | `markInvoiceWrittenOff` | Writes off a Billsby invoice as bad debt so it is no longer chased for payment. The invoice remains on the customer's record marked as written off. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Credit Note Created | `CreditNoteCreated` | Fires when a credit note is raised against a customer. REGISTRATION IS MANUAL: Billsby control panel &gt; Settings &gt; Configuration &gt; API keys and webhooks &gt; Webhooks &gt; 'Add a webhook' &gt; paste the fastn webhook URL &gt; tick 'Credit note created' &gt; Save. |
| Credit Note Updated | `CreditNoteUpdated` | Fires when a credit note changes status, for example Pending to Paid. REGISTRATION IS MANUAL: Billsby control panel &gt; Settings &gt; Configuration &gt; API keys and webhooks &gt; Webhooks &gt; 'Add a webhook' &gt; paste the fastn webhook URL &gt; tick 'Credit note updated' &gt; Save. |
| Customer Created | `CustomerCreated` | Fires when a customer is created during the checkout flow or in the Billsby app. REGISTRATION IS MANUAL (Billsby has no webhook registration API): in the Billsby control panel go to Settings &gt; Configuration &gt; API keys and webhooks, scroll to Webhooks, click 'Add a webhook', paste the fastn webhook URL, tick 'Customer created', then Save. |
| Customer Deleted | `CustomerDeleted` | Fires when a customer is deleted, including via the GDPR cleanup route. REGISTRATION IS MANUAL: Billsby control panel &gt; Settings &gt; Configuration &gt; API keys and webhooks &gt; Webhooks &gt; 'Add a webhook' &gt; paste the fastn webhook URL &gt; tick 'Customer deleted' &gt; Save. |
| Customer Updated | `CustomerUpdated` | Fires when a customer record is changed. REGISTRATION IS MANUAL: Billsby control panel &gt; Settings &gt; Configuration &gt; API keys and webhooks &gt; Webhooks &gt; 'Add a webhook' &gt; paste the fastn webhook URL &gt; tick 'Customer updated' &gt; Save. |
| Invoice Created | `InvoiceCreated` | Fires when an invoice is created and sent to the customer. REGISTRATION IS MANUAL: Billsby control panel &gt; Settings &gt; Configuration &gt; API keys and webhooks &gt; Webhooks &gt; 'Add a webhook' &gt; paste the fastn webhook URL &gt; tick 'Invoice created' &gt; Save. |
| Invoice Updated | `InvoiceUpdated` | Fires when an invoice changes status, for example Pending to Paid, written off or paid offline. REGISTRATION IS MANUAL: Billsby control panel &gt; Settings &gt; Configuration &gt; API keys and webhooks &gt; Webhooks &gt; 'Add a webhook' &gt; paste the fastn webhook URL &gt; tick 'Invoice updated' &gt; Save. |
| Subscription Created | `SubscriptionCreated` | Fires when a subscription is created during checkout or in the Billsby app. REGISTRATION IS MANUAL: Billsby control panel &gt; Settings &gt; Configuration &gt; API keys and webhooks &gt; Webhooks &gt; 'Add a webhook' &gt; paste the fastn webhook URL &gt; tick 'Subscription created' &gt; Save. |
| Subscription Updated | `SubscriptionUpdated` | Fires when a subscription changes plan, cycle, units, status or next billing date. REGISTRATION IS MANUAL: Billsby control panel &gt; Settings &gt; Configuration &gt; API keys and webhooks &gt; Webhooks &gt; 'Add a webhook' &gt; paste the fastn webhook URL &gt; tick 'Subscription updated' &gt; Save. |
