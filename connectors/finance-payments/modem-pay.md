---
description: "Modem Pay is a payment infrastructure platform for businesses in The Gambia and West Africa, collecting payments through Wave, AfriMoney, QMoney and cards and…"
hidden: true
---

# Modem Pay

<img src="../../.gitbook/assets/connectors/modem-pay.png" alt="Modem Pay logo" width="64">

Modem Pay is a payment infrastructure platform for businesses in The Gambia and West Africa, collecting payments through Wave, AfriMoney, QMoney and cards and sending mobile money payouts. This connector covers the Modem Pay REST API: balances, customers, payment intents, payment links, payment methods and mandates, coupons, transactions and refunds, transfers and bulk payouts with fee checks, split-payment sub-accounts, virtual terminals, invoices, and stablecoin payment requests and off-ramps.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [modempay.com](https://modempay.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `modemPay` |

## Use it

Add Modem Pay from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.modemPay.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Attach Payment Method | `attachPaymentMethod` | Attaches a saved payment method to a customer so it can be used for that customer's future payments. |
| Cancel Payment Intent | `cancelPaymentIntent` | Cancels a payment intent so it can no longer be completed, returning the intent with status cancelled. |
| Create Bulk Payout | `createBulkPayout` | Sends a batch of mobile money payouts in one request, each with its own amount, network, beneficiary and account number, identified by a unique batch reference. |
| Create Coupon | `createCoupon` | Creates a discount coupon offering a percentage or fixed-amount discount, with a duration, redemption limit, expiry date and optional purchase restrictions. Apply it to a payment intent by ID or name. |
| Create Customer | `createCustomer` | Creates a customer profile with a name, email and optional phone number and starting balance. Set config.distinct to true to return an existing customer with matching details instead of creating a duplicate. |
| Create Draft Invoice | `createDraftInvoice` | Creates an invoice as a draft without sending it to the customer. Publish it later with Send Draft Invoice. |
| Create Invoice | `createInvoice` | Creates and publishes an invoice to a customer with a payment link. Use a single amount for a simple invoice or line items with an optional discount for a professional invoice. Invoices are denominated in GMD. |
| Create Off-Ramp | `createOffRamp` | Creates a crypto off-ramp that converts a USDT or USDC deposit into dalasi, settled to your Modem Pay balance or a mobile money account, with an optional reseller markup. Requires the crypto feature to be enabled on the account. |
| Create Payment Intent | `createPaymentIntent` | Creates a payment intent and returns a hosted checkout link and intent secret. Only the amount is required; optionally restrict payment methods, link a customer, apply a coupon, split with a sub-account, or pass network and account number for a direct mobile-money charge. |
| Create Payment Link | `createPaymentLink` | Creates a reusable hosted payment link with a title, description and optional fixed or minimum amount, redirect URLs and custom checkout fields. |

<details>

<summary>See 50 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Payment Method | `createPaymentMethod` | Saves a mobile wallet payment method (such as Wave, AfriMoney or QMoney), optionally attached to a customer, for future payments. |
| Create Stablecoin Payment Request | `createStablecoinPaymentRequest` | Creates a stablecoin (USDT or USDC) payment request with a hosted payment link for a USD or GMD amount. Requires the crypto feature to be enabled on the account and a live API key. |
| Create Sub-Account | `createSubAccount` | Creates a split-payment sub-account that receives a percentage of each linked payment and settles to a Wave or AfriMoney account. |
| Create Transfer | `createTransfer` | Sends a mobile money payout from the payout balance to a beneficiary on a supported network such as Wave or AfriMoney. An idempotency key is required so a retried request never pays out twice. |
| Create Virtual Terminal | `createVirtualTerminal` | Creates a virtual terminal for a shop counter or location, with its own QR payment code and WhatsApp numbers that receive real-time payment notifications. |
| Delete Coupon | `deleteCoupon` | Permanently deletes a coupon by its ID. |
| Delete Customer | `deleteCustomer` | Permanently deletes a customer by its ID. |
| Delete Payment Link | `deletePaymentLink` | Permanently deletes a payment link by its ID. |
| Delete Sub-Account | `deleteSubAccount` | Permanently deletes a split-payment sub-account by its ID. |
| Delete Virtual Terminal | `deleteVirtualTerminal` | Permanently deletes a virtual terminal by its ID. |
| Detach Payment Method | `detachPaymentMethod` | Removes a payment method from its customer. Once detached it cannot be used for payments or attached again. |
| Download Virtual Terminal Poster | `downloadVirtualTerminalPoster` | Downloads the ready-to-print QR payment poster for a virtual terminal as an image file. |
| Get Balance | `getBalance` | Retrieves the account's balances: the available balance (funds from successful payments pending settlement) and the payout balance (settled funds usable for transfers and refunds). |
| Get Bulk Payout | `getBulkPayout` | Retrieves a bulk payout by its ID, including overall progress, success and failure counts and each individual transfer. |
| Get Coupon | `getCoupon` | Retrieves a coupon by its ID, including redemption count and validity. |
| Get Crypto Ramp | `getCryptoRamp` | Retrieves a crypto on-ramp or off-ramp by its ID, including its status, amount actually paid, settlement details and event history. Requires the crypto feature to be enabled on the account. |
| Get Customer | `getCustomer` | Retrieves a single customer by its ID, including contact details and balance. |
| Get Invoice | `getInvoice` | Retrieves an invoice by its ID, including status, line items, payment link and reminder count. |
| Get Mandate | `getMandate` | Retrieves the mandate (customer authorization for future charges) linked to a saved payment method. Mandates are created automatically when a customer chooses to save a payment method at checkout. |
| Get Payment Intent | `getPaymentIntent` | Retrieves a payment intent by its ID, including status, amount, payment method options and checkout link. |
| Get Payment Link | `getPaymentLink` | Retrieves a payment link by its ID. |
| Get Payment Method | `getPaymentMethod` | Retrieves a saved payment method by its ID. |
| Get Stablecoin Payment Request | `getStablecoinPaymentRequest` | Retrieves a stablecoin payment request by its ID with its latest status. Requires the crypto feature to be enabled on the account. |
| Get Sub-Account | `getSubAccount` | Retrieves a split-payment sub-account by its ID, including its percentage, settlement destination and balance. |
| Get Transaction | `getTransaction` | Retrieves a single transaction by its ID, including status, payment method, customer details and gateway. |
| Get Transfer | `getTransfer` | Retrieves a payout transfer by its ID, including status, fee, beneficiary details and balance before and after. |
| Get Transfer Fee | `getTransferFee` | Calculates the fee for a payout of a given amount, currency and network before sending it. |
| Get Virtual Terminal | `getVirtualTerminal` | Retrieves a virtual terminal by its ID, including its QR code URL, notification numbers and status. |
| List Coupons | `listCoupons` | Lists coupons with pagination, optionally filtered by a search term matched against the coupon name. |
| List Customer Payment Methods | `listCustomerPaymentMethods` | Lists the saved payment methods attached to a customer, with pagination. |
| List Customers | `listCustomers` | Lists customers with pagination, optionally filtered by a search term matched against name, email and other customer attributes. |
| List Invoices | `listInvoices` | Lists invoices with pagination. |
| List Payment Intents | `listPaymentIntents` | Lists recent payment intents with pagination. |
| List Payment Links | `listPaymentLinks` | Lists payment links with pagination. |
| List Payment Methods | `listPaymentMethods` | Lists saved payment methods across the account with pagination. |
| List Stablecoin Payment Requests | `listStablecoinPaymentRequests` | Lists stablecoin payment requests with pagination. Requires the crypto feature to be enabled on the account. |
| List Sub-Accounts | `listSubAccounts` | Lists split-payment sub-accounts with pagination, optionally filtered by a search term matched against the business name. |
| List Transactions | `listTransactions` | Lists payment transactions with pagination, optionally filtered by a search term (currency, reference, payment method or customer) and a recent timeframe in minutes. |
| List Virtual Terminals | `listVirtualTerminals` | Lists virtual terminals with pagination, optionally filtered by a search term matched against the terminal name. |
| Mark Invoice Paid | `markInvoicePaid` | Manually marks an invoice as paid, for example when the customer paid offline. |
| Refund Transaction | `refundTransaction` | Refunds a completed transaction in full or in part using its transaction reference. Refunds are allowed only on completed transactions within 48 hours of completion; omit the amount for a full refund. Charges may apply. |
| Send Draft Invoice | `sendDraftInvoice` | Publishes a draft invoice and notifies the customer, setting its sent date. |
| Send Invoice Reminder | `sendInvoiceReminder` | Sends a payment reminder for an outstanding invoice to its customer and increments the invoice's reminder count. |
| Update Coupon | `updateCoupon` | Updates a coupon's name, percentage, redemption limit, expiry, duration in months, metadata or restrictions. Only fields provided inside data are changed. |
| Update Customer | `updateCustomer` | Updates a customer's name, email, phone number or balance. Only the fields provided inside data are changed. |
| Update Invoice | `updateInvoice` | Updates an invoice's amount, customer details, line items, discount, due date, notes or other fields. Only fields provided inside data are changed; updating a published invoice may confuse customers. |
| Update Payment Link | `updatePaymentLink` | Updates a payment link's status, title, description, amount, currency, redirect URLs or custom fields. Only fields provided inside data are changed. |
| Update Sub-Account | `updateSubAccount` | Updates a sub-account's active status, percentage share, settlement provider or account number. Changes apply to future transactions only. |
| Update Virtual Terminal | `updateVirtualTerminal` | Updates a virtual terminal's name, notification WhatsApp numbers or active status. |
| Verify Payment Intent | `verifyPaymentIntent` | Retrieves a payment intent by its intent secret to confirm its current status after a checkout. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Charge Cancelled | `charge.cancelled` | Fires when a charge is cancelled. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the transaction object is in payload. Payload modelled from docs. |
| Charge Created | `charge.created` | Fires when a charge (transaction) is created for a payment intent. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the transaction object is in payload. Payload modelled from the docs charge sample and the live transaction object. |
| Charge Expired | `charge.expired` | Fires when a pending charge expires without payment. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the transaction object is in payload. Payload modelled from docs. |
| Charge Failed | `charge.failed` | Fires when a payment attempt fails. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the transaction object (with failure_reason) is in payload. Payload modelled from docs and the live transaction object. |
| Charge Succeeded | `charge.succeeded` | Fires when a payment completes successfully. Setup (once per Modem Pay account): in the Modem Pay dashboard open Developers &gt; Webhooks and paste this fastn webhook URL as the endpoint. The event type is in the top-level event field and the object in payload. Modem Pay signs deliveries with HMAC-SHA512 (x-modem-signature) using a per-account secret from that page; fastn cannot store per-account secrets, so verify the signature in your workflow if required. Payments created with a callback_url deliver to that URL instead. Payload modelled from the official docs sample (no live delivery captured). |
| Charge Updated | `charge.updated` | Fires when a charge changes, for example after a refund. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the transaction object is in payload. Payload modelled from the live transaction object. |
| Customer Created | `customer.created` | Fires when a customer is created. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the customer is in payload. Payload modelled from the live customer object. |
| Customer Deleted | `customer.deleted` | Fires when a customer is deleted. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the deleted customer is in payload. Payload modelled from the customer object. |
| Customer Updated | `customer.updated` | Fires when a customer is updated. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the customer is in payload. Payload modelled from the live customer object. |
| Invoice Created | `invoice.created` | Fires when an invoice is created. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the invoice is in payload. Payload modelled from the live invoice object. |

<details>

<summary>See 12 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Invoice Deleted | `invoice.deleted` | Fires when an invoice is deleted in the dashboard. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the invoice is in payload. Payload modelled from the invoice object. |
| Invoice Overdue | `invoice.overdue` | Fires in live mode when an invoice passes its due date unpaid (test-mode invoices never go overdue). Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the invoice is in payload. Payload modelled from docs. |
| Invoice Paid | `paymentrequest.success` | Fires when an invoice is paid (the vendor's event name is paymentrequest.success). Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the invoice is in payload. Payload modelled from the live paid invoice object. |
| Invoice Updated | `invoice.update` | Fires when an invoice is updated (the vendor's event name is invoice.update). Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the invoice is in payload. Payload modelled from the live invoice object. |
| Payment Intent Cancelled | `payment_intent.cancelled` | Fires when a payment intent is cancelled. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the payment intent is in payload. Payload modelled from the live cancelled payment intent. |
| Payment Intent Created | `payment_intent.created` | Fires when a payment intent is created. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the payment intent is in payload. Payload modelled from the live payment intent object. |
| Payment Intent Expired | `payment_intent.expired` | Fires when a payment intent passes its expiry time without being paid. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the payment intent is in payload. Payload modelled from docs. |
| Transfer Cancelled | `transfer.cancelled` | Fires when a payout is cancelled. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the transfer is in payload. Payload modelled from the SDK Transfer type. |
| Transfer Failed | `transfer.failed` | Fires when a payout fails. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the transfer is in payload. Payload modelled from the SDK Transfer type. |
| Transfer Flagged | `transfer.flagged` | Fires when a payout is flagged for review. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the transfer is in payload. Payload modelled from the SDK Transfer type. |
| Transfer Reversed | `transfer.reversed` | Fires when a completed payout is reversed. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the transfer is in payload. Payload modelled from the SDK Transfer type. |
| Transfer Succeeded | `transfer.succeeded` | Fires when a mobile money payout completes. Setup: Modem Pay dashboard &gt; Developers &gt; Webhooks, paste this fastn webhook URL. Event type is in the event field; the transfer is in payload. Payouts created with a callback_url deliver there instead. Payload modelled from the SDK Transfer type (no payout could be sent on this account). |

</details>
