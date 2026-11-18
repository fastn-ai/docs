---
description: "HitPay payments platform for APAC."
hidden: true
---

# HitPay

<img src="../../.gitbook/assets/connectors/lg/hitpay.png" alt="HitPay logo">

HitPay payments platform for APAC. Create hosted payment requests and checkout links, accept PayNow, FPX, QRIS, GrabPay, DuitNow, PromptPay and cards, issue refunds, run recurring billing on saved cards, manage customers, products, orders, invoices, locations, static QR codes, card readers, virtual accounts, balances, payouts (beneficiaries, remitters, transfers) and webhook event subscriptions.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [hit-pay.com](https://hit-pay.com) |
| **Authentication** | API key, OAuth 2.0 |
| **Slug** | `hitpay` |

## Use it

Add HitPay from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hitpay.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Recurring Billing | `deleteRecurringBilling` | Cancel a recurring billing subscription by id. No further charges are taken. Returns the cancelled subscription. |
| Cancel Terminal Reader | `cancelReader` | Cancel the transaction currently in progress on a card reader terminal, returning it to its idle screen. |
| Charge Saved Payment Method | `chargeRecurringBilling` | Charge the payment method saved against a recurring billing subscription for an ad-hoc amount. This takes money from the customer immediately, so only call it with an amount you have authorisation for. |
| Create Beneficiary | `createBeneficiary` | Register a payout beneficiary: the person or business that will receive transferred funds. The exact required fields depend on country, currency, transfer method and transfer type, so call Get Beneficiary Schema first. HitPay currently supports local beneficiaries within the same country. |
| Create Customer | `createCustomer` | Create a customer record on the HitPay business. Email and phone number are required; the phone country code must be 1-5 digits with no plus sign. |
| Create Invoice | `createInvoice` | Raise an invoice for a customer, billed either by a flat amount or by line-item products. Supports due dates, partial payments, tax settings, discounts, extra recipients and a webhook for payment notifications. Set send_email to 1 only when you intend HitPay to email the real customer. |
| Create Location | `createLocation` | Create a new physical location for the business. All address fields are required. Newly created locations are active by default. Returns the created location including its id. |
| Create Order | `createOrder` | Create an order in draft status against a customer and location. The channel must be one of point_of_sale, quick_sale or self_serve. |
| Create Payment Request | `createPaymentRequest` | Create a HitPay payment request and receive a hosted checkout URL to redirect the buyer to. Supports cards, PayNow, FPX, GrabPay, ShopeePay, Atome and other local APMs, optional QR generation, expiry, admin fee, email/SMS receipts and arbitrary metadata. |
| Create Product | `createProduct` | Create a catalogue product with a name and price. Optionally set description, SKU, barcode, stock quantity and alert level, category ids, sales channels, locations, weight and publish state. Product images must be uploaded from the HitPay dashboard. |
| Create Recurring Billing | `createRecurringBilling` | Start a recurring billing subscription for a customer, either from an existing subscription plan or with inline cycle and amount. Set save_payment_method to true to tokenise the customer's card or wallet for later charges. Returns a URL where the customer enters their payment details. |
| Create Refund | `createRefund` | Refund a completed HitPay payment in full or in part. Moves money back to the payer, so supply the exact payment id and amount. Optionally send the customer an email receipt and receive a webhook when the refund settles. |
| Create Remitter | `createRemitter` | Register a remitter for payout transfers, with the identity and address details required for compliance screening. Use entity_type company together with company_name for a business remitter. |
| Create Static QR | `createStaticQr` | Create a static QR code for accepting repeat payments at a fixed location. Returns the QR payload string plus the resolved payment provider and logos. |
| Create Subscription Plan | `createSubscriptionPlan` | Define a recurring billing plan: a name, an amount and a billing cycle such as weekly, monthly, yearly or a custom interval. Returns the plan plus a shareable signup URL customers can use to subscribe. |
| Create Transfer | `createTransfer` | Send a payout transfer to a beneficiary. This moves real money out of the business's balance to a third party's bank account, so confirm the beneficiary and amount before calling it. Pass either beneficiary_id or an inline beneficiary, and either source_amount or payment_amount. |
| Create Virtual Account | `createVirtualAccount` | Provision a virtual bank account for the business. HitPay picks the payment provider and method from the business configuration, and a business may hold only one virtual account per method. Takes no request body. Virtual accounts cannot be deleted through the API. |
| Create Webhook Event | `createWebhookEvent` | Register an HTTPS endpoint to receive HitPay event notifications. The response includes a salt used to verify the HMAC-SHA256 signature on every delivery, so store it securely and never log it. |
| Delete Beneficiary | `deleteBeneficiary` | Remove a payout beneficiary by id. Transfers already sent to the beneficiary are unaffected. |
| Delete Customer | `deleteCustomer` | Permanently delete a customer record from the HitPay business. |
| Delete Invoice | `deleteInvoice` | Delete an invoice by id. |
| Delete Location | `deleteLocation` | Permanently delete a location. The location must be deactivated first via Toggle Location Active Status. Deletion is rejected while the location is still the main location or has dependent records. |
| Delete Order | `deleteOrder` | Delete an order by id. |
| Delete Payment Request | `deletePaymentRequest` | Delete a payment request by id. HitPay rejects deletion of payment requests that have already been completed. |
| Delete Product | `deleteProduct` | Permanently delete a catalogue product by id. |
| Delete Remitter | `deleteRemitter` | Remove a remitter by id. |
| Delete Static QR | `deleteStaticQr` | Delete a static QR code by id. Printed copies of the code stop working immediately. |
| Delete Subscription Plan | `deleteSubscriptionPlan` | Delete a subscription plan by id. Subscriptions already created from the plan are not cancelled by this call. |
| Delete Webhook Event | `deleteWebhookEvent` | Unregister a webhook endpoint by id. HitPay stops delivering events to it immediately. |
| Estimate Transfer Fees | `estimateTransfer` | Quote the exchange rate and fees for a payout transfer before sending it. No money moves. Supply either source_amount or payment_amount. |
| Export Balance Breakdown | `exportBalanceBreakdown` | Queue a balance breakdown export for one payment provider. HitPay emails the generated file to the business's admin address. Only the adyen provider is supported. |
| Export Charges | `exportCharges` | Export charges matching the given filters. Supports keyword search, payment method, status list, date range and before/after charge-id cursors, plus a with parameter to embed related charge and product objects. |
| Get Account Status | `getAccountStatus` | Retrieve the HitPay business account's onboarding and verification status, including bank account status, owner and business verification state, and the setup state of each connected payment provider. Returns an object describing the account's readiness to accept payments and receive payouts. |
| Get Balance Transactions | `getBalanceTransactions` | Return the balance transaction ledger for one payment provider, cursor-paginated and filterable by date range. Only the adyen provider exposes this route; other provider names return a route-not-found error. |
| Get Balances | `getBalances` | Return the business's wallet balances per currency, broken down into available, deposit, pending and reserve amounts. |
| Get Beneficiary | `getBeneficiary` | Retrieve one payout beneficiary by id, including bank details, screening status and who created it. |
| Get Beneficiary Schema | `getBeneficiarySchema` | Return the field list and validation rules required to create a beneficiary for a given country, currency, transfer method and transfer type. Call this first, then pass the fields it names to Create Beneficiary. |
| Get Business Info | `getBusinessInfo` | Return the connected merchant's business profile. This route is reachable only with an OAuth access token (any granted scope); a Business API key is rejected with 401 Unauthenticated. Use it after connecting a merchant account through the OAuth auth method. |
| Get Charge Details | `getCharge` | Retrieve one charge by id, including amount, fees, currency and exchange rate, payment method, customer, refunds, webhook delivery logs, terminal and location. |
| Get Coupon | `getCoupon` | Retrieve a single coupon by id. Undocumented route, verified live. |
| Get Customer Detail | `getCustomer` | Retrieve a single customer by id, including contact details and address. |
| Get Discount | `getDiscount` | Retrieve a single discount by id. Undocumented route, verified live. |
| Get Location | `getLocation` | Retrieve a single business location by its id. Returns 404 if the location does not exist or belongs to another business. |
| Get Notification Settings | `getNotificationSettings` | Return the business's notification preferences as a list of event and channel pairs, for example customer_receipt over email or incoming_payment over push notification. |
| Get Order Details | `getOrder` | Retrieve one order by id with its line items, products, charges, totals and fulfilment status. |
| Get Payment Request Status | `getPaymentRequest` | Retrieve a payment request by id and check its current status, along with its checkout URL, line items and any payments recorded against it. |
| Get Pickup | `getPickup` | Retrieve a single pickup option by id. Undocumented route, verified live. |
| Get Product Detail | `getProduct` | Retrieve one catalogue product by id, including pricing, inventory settings, variations, images and publish state. |
| Get Recurring Billing | `getRecurringBilling` | Retrieve one recurring billing subscription by id. When a payment method has been saved, the response includes the card brand and last four digits so you can charge it later. |
| Get Refund Details | `getRefund` | Retrieve a single refund by id, including the amount refunded, the original payment, the payment method, provider fees and the settlement timestamp. |
| Get Remitter | `getRemitter` | Retrieve one remitter by id, including their screening status and identity details. |
| Get Shipping Method | `getShippingMethod` | Retrieve a single shipping method by id. Undocumented route, verified live. |
| Get Shipping Settings | `getShippingSettings` | Return the online store's shipping configuration: whether shipping and pickup are enabled and every shipping method with its pricing rules. Undocumented route, verified live. |
| Get Staff Detail | `getStaff` | Retrieve a single staff member by id, including their role, email, invitation timestamp and the locations they are assigned to. |
| Get Static QR Detail | `getStaticQr` | Retrieve one static QR code by id, including its QR payload, amount, currency and linked location or device. |
| Get Subscription Plan Details | `getSubscriptionPlan` | Retrieve one subscription plan by id, including its cycle, amount and signup URL. |
| Get Tax Setting | `getTax` | Retrieve a single tax setting by id. Undocumented route, verified live. |
| Get Transfer | `getTransfer` | Retrieve one payout transfer by id, including amounts, exchange rate, fees, status and approval history. |
| Get Virtual Account | `getVirtualAccount` | Retrieve one virtual bank account by id, including its account number, holder name, provisioning status and supported currencies. |
| Get Webhook Event Detail | `getWebhookEvent` | Retrieve a single registered webhook endpoint by id, with its destination URL and subscribed event types. |
| List Beneficiaries | `listBeneficiaries` | Return the payout beneficiaries registered on the business, optionally searched by holder name or nickname. |
| List Card Readers | `listReaders` | Return the card reader terminals paired with the business, for in-person card and QR payments. |
| List Charges | `listCharges` | Return a cursor-paginated list of charges (individual payments captured by the business). Filter by status, date range, amount range, payment request, customer, payout, location or staff. |
| List Coupons | `listCoupons` | Return the coupons configured on the business's online store. Undocumented route, verified live. |
| List Customers | `listCustomers` | Return a paginated list of the business's saved customers. |
| List Discounts | `listDiscounts` | Return the discounts configured on the business. Undocumented route, verified live. |
| List Invoices | `listInvoices` | Return the business's invoices, optionally filtered by customer email, status or reference. |
| List Locations | `listLocations` | Return a paginated list of the business's physical locations (stores, outlets, branches). Optionally filter by name keywords or an exact location UUID. Returns data, links and meta pagination objects. |
| List Orders | `listOrders` | Return the business's point-of-sale and online orders. By default HitPay excludes draft orders, so pass statuses to include them. Filter by keywords, status, order version or creation date range, and use the with parameter to embed products or charges. |
| List Payment Requests | `listPaymentRequests` | Return a paginated list of payment requests. Search by email, id or reference number, filter to default payment links, or filter by a single metadata key/value pair. |
| List Payouts | `listPayouts` | Return the settlement payouts HitPay has made to the business's bank account. Undocumented route, verified live. |
| List Pickups | `listPickups` | Return the pickup options configured across the business's locations. Undocumented route, verified live. |
| List Product Categories | `listProductCategories` | Return the business's product categories, optionally filtered by active state, parent category or name keywords. Each category reports its children and total product count. |
| List Products | `listProducts` | Return a paginated list of catalogue products, optionally filtered by keywords, status, category, source, inventory, sales channel or location. |
| List Recurring Billings | `listRecurringBillings` | Return the business's recurring billing subscriptions, optionally filtered by customer email, reference, plan or status. |
| List Remitters | `listRemitters` | Return the remitters registered on the business. A remitter is the individual or company legally sending funds in a payout transfer. |
| List Staff | `listStaffs` | Return every staff member on the HitPay business account, each with their id, name and role. Use a staff id when creating payment requests attributed to a cashier. |
| List Static QRs | `listStaticQrs` | Return every static QR code on the business. Static QRs are fixed printed codes customers scan to pay at a counter or table. |
| List Subscription Plans | `listSubscriptionPlans` | Return a paginated list of recurring billing subscription plans defined on the business. |
| List Tax Settings | `listTaxes` | Return the tax settings configured on the business, used on invoices and products. Undocumented route, verified live. |
| List Transfers | `listTransfers` | Return the business's outgoing payout transfers, optionally filtered by beneficiary, keywords or status. |
| List Virtual Accounts | `listVirtualAccounts` | Return the business's virtual bank accounts, newest first, using cursor pagination. Customers transferring to a virtual account have the funds credited to the HitPay balance automatically. |
| List Webhook Events | `listWebhookEvents` | Return every webhook endpoint registered on the business, with the event types each one subscribes to. |
| Print Charge Receipt | `printChargeReceipt` | Print a charge or refund receipt on a HitPay All-in-One terminal. Only available to Singapore merchants using an All-in-One Terminal; the terminal must be registered to the business. |
| Request Payout | `createPayout` | Trigger a settlement payout of the business's available balance to its linked bank account. This moves real money out of the HitPay balance. Requires a verified bank account on the business. Undocumented route, verified live. |
| Toggle Location Active Status | `toggleLocationActive` | Activate or deactivate a location. A location must be deactivated before it can be deleted. Deactivation is rejected if it is the only active location or if it is the business's main location. |
| Update Beneficiary | `updateBeneficiary` | Update a beneficiary's nickname, remark or favourite flag. HitPay does not allow bank details to be changed after creation. |
| Update Customer | `updateCustomer` | Update a customer's name, contact details, remark, birth date, gender or address. HitPay requires at least one of email or phone_number on every update, even when only the name is changing. |
| Update Invoice | `updateInvoice` | Update an unpaid invoice's dates, amount, line items, payment methods, discounts or recipients. |
| Update Location | `updateLocation` | Update an existing location's name and address. All fields are required; supply the full record. Returns the updated location. |
| Update Notification Settings | `updateNotificationSettings` | Turn each notification on or off per channel. Field names combine the event and the channel with an at sign, for example daily_payout@email. |
| Update Order | `updateOrder` | Update an order's amount, remark, customer, location, discount or channel. HitPay requires the full field set on every update. |
| Update Payment Request | `updatePaymentRequest` | Update a pending payment request's amount, currency, buyer details, payment methods, expiry or receipt settings. Completed payment requests cannot be changed. |
| Update Product | `updateProduct` | Update a catalogue product's name, price, description, inventory settings, weight or publish state. HitPay requires name and price on every update. |
| Update Recurring Billing | `updateRecurringBilling` | Change a recurring billing subscription's amount, cycle, customer details, payment methods or reference. Cycle changes take effect at the end of the current cycle. |
| Update Static QR | `updateStaticQr` | Update a static QR code's name, linked location or fixed amount. The payment provider method cannot be changed after creation. |
| Update Subscription Plan | `updateSubscriptionPlan` | Update a subscription plan's name, amount, cycle or settings. Changes do not affect subscriptions already running on the plan; use Update Recurring Billing for those. Name, cycle and amount must always be supplied. |
| Update Webhook Event | `updateWebhookEvent` | Change a registered webhook endpoint's name, destination URL or subscribed event types. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Beneficiary Approved | `beneficiary.approved` | A payout beneficiary passed screening. Requires the payouts entitlement. |
| Beneficiary Information Requested | `beneficiary.rfi_requested` | Compliance requested more information about a beneficiary. Requires the payouts entitlement. |
| Beneficiary Rejected | `beneficiary.rejected_screening` | A payout beneficiary failed screening. Requires the payouts entitlement. |
| Charge Created | `charge.created` | A payment was captured. Delivery carries Hitpay-Event-Object: charge and Hitpay-Event-Type: created. Payload schema modelled from HitPay's documented sample, not captured live. |
| Charge Failed | `charge.failed` | A payment attempt failed. Hitpay-Event-Object: charge. Payload schema modelled from HitPay's documented charge sample. |
| Charge Updated | `charge.updated` | A charge changed state, for example when it is refunded. Hitpay-Event-Object: charge, Hitpay-Event-Type: updated. Payload schema modelled from HitPay's documented charge sample. |
| Invoice Created | `invoice.created` | An invoice was raised. Hitpay-Event-Object: invoice. Payload schema modelled from HitPay's documented samples. |
| Invoice Updated | `invoice.updated` | An invoice changed, for example when it is paid. Hitpay-Event-Object: invoice. Payload schema modelled from HitPay's documented samples. |
| Order Created | `order.created` | A new order was raised. Hitpay-Event-Object: order. Payload schema modelled from HitPay's documented samples. |
| Order Updated | `order.updated` | An order changed. Hitpay-Event-Object: order. Payload schema modelled from HitPay's documented samples. |
| Payment Request Completed | `payment_request.completed` | A payment request was paid in full. Payload schema modelled from HitPay's documented samples. |
| Payment Request Failed | `payment_request.failed` | A payment request could not be paid. Payload schema modelled from HitPay's documented samples. |
| Payout Created | `payout.created` | A settlement payout to the business's bank account was created. Hitpay-Event-Object: payout. Payload schema modelled from HitPay's documented samples. |
| Recurring Billing Method Attached | `recurring_billing.method_attached` | A customer saved a card or wallet against a subscription. Payload schema modelled from HitPay's documented samples. |
| Recurring Billing Method Detached | `recurring_billing.method_detached` | A saved payment method was removed from a subscription. Payload schema modelled from HitPay's documented samples. |
| Recurring Billing Subscription Updated | `recurring_billing.subscription_updated` | A subscription's amount, cycle or status changed. Payload schema modelled from HitPay's documented samples. |
| Remitter Approved | `remitter.approved` | A remitter passed screening. Requires the payouts entitlement. |
| Remitter Information Requested | `remitter.rfi_requested` | Compliance requested more information about a remitter. Requires the payouts entitlement. |
| Remitter Rejected | `remitter.rejected_screening` | A remitter failed screening. Requires the payouts entitlement. |
| Transfer Canceled | `transfer.canceled` | A payout transfer was cancelled. Requires the payouts entitlement. |
| Transfer Compliance Approved | `transfer.compliance_approved` | Compliance approved a transfer. Requires the payouts entitlement. |
| Transfer Compliance Rejected | `transfer.compliance_rejected` | Compliance rejected a transfer. Requires the payouts entitlement. |
| Transfer Created | `transfer.created` | A payout transfer to a beneficiary was created. Hitpay-Event-Object: transfer. Requires the payouts entitlement. |
| Transfer Failed | `transfer.failed` | A payout transfer failed. Requires the payouts entitlement. |
| Transfer Information Provided | `transfer.rfi_responded` | A compliance information request on a transfer was answered. Requires the payouts entitlement. |
| Transfer Information Requested | `transfer.rfi_requested` | Compliance requested more information about a transfer. Requires the payouts entitlement. |
| Transfer Paid | `transfer.paid` | A payout transfer reached the beneficiary. Requires the payouts entitlement. |
| Transfer Pending Funding | `transfer.pending_funding` | A payout transfer is waiting for funding. Requires the payouts entitlement. |
| Transfer Processing | `transfer.processing` | A payout transfer is being processed. Requires the payouts entitlement. |
| Transfer Scheduled | `transfer.scheduled` | A payout transfer was scheduled. Requires the payouts entitlement. |
| Transfer Updated | `transfer.updated` | A payout transfer changed. Requires the payouts entitlement. |
