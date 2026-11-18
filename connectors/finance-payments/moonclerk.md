---
description: "MoonClerk is a recurring-payments and checkout platform built on Stripe."
---

# MoonClerk

MoonClerk is a recurring-payments and checkout platform built on Stripe. This connector covers the complete MoonClerk REST API (https://api.moonclerk.com), which is read-only: list and retrieve payment forms, customers (called "Plans" in the MoonClerk interface, each carrying its subscription and plan detail) and payments, with date, status and form filters and count/offset paging. Creating or editing forms, plans and pricing is done in the MoonClerk interface and has no API. MoonClerk events are delivered by webhook endpoints registered in the MoonClerk dashboard.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [moonclerk.com](https://moonclerk.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 6 |
| **Events** | 5 |
| **Slug** | `moonclerk` |

## Use it

Add MoonClerk from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.moonclerk.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Customer | `getCustomer` | Retrieves a single MoonClerk customer by its MoonClerk ID. A customer is a subscription (called a "Plan" in the MoonClerk interface) and the response includes the payer, their payment method, any discount, custom field responses, the originating checkout and the subscription's plan and billing dates. |
| Get Form | `getForm` | Retrieves a single MoonClerk payment form by its MoonClerk ID, returning its title, currency, public checkout access token, total payment volume in cents and successful checkout count. |
| Get Payment | `getPayment` | Retrieves a single MoonClerk payment by its MoonClerk ID, returning the amount and Stripe fee in cents, the payment status, the payer and payment method, custom field responses, any coupon, and the related Stripe charge, customer and invoice references. |
| List Customers | `listCustomers` | Lists MoonClerk customers, each of which is a subscription (called a "Plan" in the MoonClerk interface) together with the payer, their payment method, custom field responses, checkout detail and the subscription's plan and billing dates. Filter by form, by subscription status, by checkout date range or by next-payment date range, and page with count and offset. |
| List Forms | `listForms` | Lists the payment forms in your MoonClerk account, newest first, with each form's title, currency, public checkout access token, total payment volume and successful checkout count. Returns 10 forms per page by default; use count and offset to page through larger sets. |
| List Payments | `listPayments` | Lists payments collected through your MoonClerk forms, with amount, Stripe fee, refunded amount, payer details, payment method, custom field responses and the related Stripe charge, customer and invoice references. Filter by form, by customer, by payment status or by charge date range, and page with count and offset. All money fields are in cents. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Payment Created | `payment_created` | Fires when a payment is created in any state, successful or failed. To receive it, sign in to MoonClerk, choose Settings from the Account dropdown menu, click Webhooks, click Create Webhook Endpoint, paste this trigger's URL (it must be HTTPS), tick the 'Payment Created' topic, leave the state as Active and click Save. The payload carries Payment data. MoonClerk retries a non-2xx response up to 10 times and then sets the endpoint inactive. Payload schema modelled from MoonClerk's published sample at https://github.com/moonclerk/developer/blob/main/webhooks.md, not from a captured delivery. |
| Payment Succeeded | `payment_succeeded` | Fires when a payment succeeds. To receive it, sign in to MoonClerk, choose Settings from the Account dropdown menu, click Webhooks, click Create Webhook Endpoint, paste this trigger's URL (it must be HTTPS), tick the 'Payment Succeeded' topic, leave the state as Active and click Save. The payload carries Payment data. The slug 'payment_succeeded' is derived from the topic name; MoonClerk's published sample only shows the slug for Payment Created. Payload schema modelled from MoonClerk's published sample at https://github.com/moonclerk/developer/blob/main/webhooks.md, not from a captured delivery. |
| Plan Created | `plan_created` | Fires when a plan (a recurring subscription) is created. To receive it, sign in to MoonClerk, choose Settings from the Account dropdown menu, click Webhooks, click Create Webhook Endpoint, paste this trigger's URL (it must be HTTPS), tick the 'Plan Created' topic, leave the state as Active and click Save. The payload carries Customer data, including the subscription and its plan. Payload schema modelled from MoonClerk's published sample at https://github.com/moonclerk/developer/blob/main/webhooks.md, not from a captured delivery. |
| Plan Ended | `plan_ended` | Fires when a plan is canceled or when its set number of billing periods has been exhausted. To receive it, sign in to MoonClerk, choose Settings from the Account dropdown menu, click Webhooks, click Create Webhook Endpoint, paste this trigger's URL (it must be HTTPS), tick the 'Plan Ended' topic, leave the state as Active and click Save. The payload carries Customer data. The slug 'plan_ended' is derived from the topic name; MoonClerk's published sample only shows the slug for Plan Created. Payload schema modelled from MoonClerk's published sample at https://github.com/moonclerk/developer/blob/main/webhooks.md, not from a captured delivery. |
| Plan Payment Failed | `plan_payment_failed` | Fires when a payment related to a plan has failed. To receive it, sign in to MoonClerk, choose Settings from the Account dropdown menu, click Webhooks, click Create Webhook Endpoint, paste this trigger's URL (it must be HTTPS), tick the 'Plan Payment Failed' topic, leave the state as Active and click Save. The payload carries Customer data. The slug 'plan_payment_failed' is derived from the topic name; MoonClerk's published sample only shows the slug for Plan Created. Payload schema modelled from MoonClerk's published sample at https://github.com/moonclerk/developer/blob/main/webhooks.md, not from a captured delivery. |
