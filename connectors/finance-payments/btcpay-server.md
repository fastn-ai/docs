---
description: "BTCPay Server Greenfield API v1."
hidden: true
---

# BTCPay Server

<img src="../../.gitbook/assets/connectors/lg/btcpay-server.png" alt="BTCPay Server logo">

BTCPay Server Greenfield API v1. Self-hosted, open-source Bitcoin and Lightning payment processor. Manage stores, invoices, payment requests, apps, payment methods, rates, users, notifications and webhooks on any BTCPay Server instance.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [btcpayserver.org](https://btcpayserver.org) |
| **Authentication** | Basic auth, Credentials you enter |
| **Slug** | `btcpayServer` |

## Use it

Add BTCPay Server from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.btcpayServer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Or Update Store Lightning Address | `addOrUpdateStoreLightningAddress` | Registers or updates a Lightning address (username@yourserver) on a store so anyone can pay it over LNURL-pay. This only lets the store RECEIVE; it never sends. Usernames are unique across the whole server. |
| Add Or Update Wallet Object | `addOrUpdateStoreWalletObject` | Creates or replaces a wallet bookkeeping object such as a label or an annotated address, with an arbitrary data payload and optional links to other objects. Metadata only - it cannot spend, sign or broadcast anything. |
| Archive Invoice | `archiveInvoice` | Archives an invoice so it no longer appears in the default invoice list. BTCPay never hard-deletes invoices; use Unarchive Invoice to restore one. |
| Archive Payment Request | `archivePaymentRequest` | Archives a payment request so it stops accepting payment and drops out of the default list. Pass Include Archived on List Payment Requests to see archived ones. |
| Archive Pull Payment | `archivePullPayment` | Archives a pull payment so no further claims can be made against it and it drops out of the default list. Payouts already approved are unaffected. This is the safe way to close a withdrawal offer. |
| Create Crowdfund App | `createCrowdfundApp` | Creates a crowdfunding page on a store with a target amount, optional start and end dates and a JSON perks template. Only App Name is required; everything else falls back to a default. |
| Create Invoice | `createInvoice` | Creates an invoice for a store and returns its id and public checkout link. The store must have at least one payment method configured, otherwise BTCPay refuses with "No wallet has been linked to your BTCPay Store". |
| Create Payment Request | `createPaymentRequest` | Creates a shareable payment request page on a store. Unlike an invoice it does not expire by default and can optionally let the payer choose the amount. |
| Create Point Of Sale App | `createPointOfSaleApp` | Creates a point-of-sale page on a store: a hosted checkout with a keypad or an item list that produces invoices. Template is a JSON string describing the items. Only App Name is required; everything else falls back to a default. |
| Create Pull Payment | `createPullPayment` | Creates a pull payment on a store: a withdrawal offer, capped at Amount, that a recipient can claim through its public view link. CAUTION - the response contains a public claim URL, and with Auto Approve Claims on, claims are approved without review. Creating one does not move funds; approving a payout does. |
| Create Store | `createStore` | Creates a new store on the BTCPay Server instance. Only the name is required; every other setting falls back to the server default and can be changed later with Update Store. |
| Create Store Lightning Invoice | `createStoreLightningInvoice` | Issues a BOLT11 Lightning invoice on the node backing a store, so someone can pay the store. Amount is in millisatoshis. This is receive-only: it requests funds and never sends them. |
| Create Store Webhook | `createStoreWebhook` | Registers a webhook on a store so BTCPay POSTs event callbacks to your URL. The response contains the signing secret used for the BTCPay-Sig HMAC-SHA256 header, and this is the only time the secret is ever returned - store it immediately. |
| Delete App | `deleteApp` | Permanently deletes a point-of-sale or crowdfund app and its public page. Invoices already created through the app are kept on the store. This cannot be undone. |
| Delete App Item Image | `deleteAppItemImage` | Removes an image previously uploaded for an app item, by the file id returned when it was uploaded. The item itself is unaffected; only the picture is detached and deleted. |
| Delete Notification | `deleteNotification` | Permanently removes one of the authenticated user's notifications. This affects only that user's notification list; nothing else on the server changes. |
| Delete Store | `deleteStore` | Permanently removes a store and everything scoped to it, including its invoices, payment requests, apps and webhooks. This cannot be undone. If the store is the last one the account owns, the account loses its store context. |
| Delete Store Lightning Address | `deleteStoreLightningAddress` | Removes a Lightning address from a store so it stops resolving for LNURL-pay. Invoices it already produced are unaffected. |
| Delete Store Payment Method | `deleteStorePaymentMethod` | Removes a payment method from a store, unlinking its wallet or Lightning node configuration. A store with no payment methods can no longer create invoices. For BTC-CHAIN this detaches the derivation scheme; the underlying funds are unaffected but you must re-import the wallet to use it again. |
| Delete Store Webhook | `deleteStoreWebhook` | Removes a webhook from a store so BTCPay stops sending it events. Its delivery history is discarded with it. |
| Delete Wallet Object | `deleteStoreWalletObject` | Removes one wallet bookkeeping object by type and id. This discards BTCPay's own annotation, such as a label or an address note; it does not touch coins, keys or the blockchain. |
| Get App | `getApp` | Returns the basic record of any app by id - its type, name, owning store, archived flag and creation time - without the type-specific settings. Use Get Point Of Sale App or Get Crowdfund App for the full configuration. |
| Get App Sales Statistics | `getAppSales` | Returns a daily sales count series for an app over the last N days, plus the total count. Use it to chart how a point-of-sale or crowdfund page is performing. |
| Get App Top Items | `getAppTopItems` | Returns the best-selling items or perks of an app, ranked by sales, with the total value taken for each. Returns an empty array for an app that has never been paid. |
| Get Crowdfund App | `getCrowdfundApp` | Returns the full configuration of a crowdfund app: target amount and currency, schedule, perks and display options. Requires a key with btcpay.store.canmodifystoresettings on the owning store. |
| Get Current User | `getCurrentUser` | Returns the BTCPay Server account that the current API key or Basic credentials authenticate as, including its id, email, roles and store quota. Use it to confirm a connection is live and to discover the caller's user id. |
| Get Internal Lightning Balance | `getInternalLightningBalance` | Returns the on-chain and channel balances of the server's internal Lightning node. Read-only and server-admin only; a non-admin key gets 403 missing-permission btcpay.server.canuseinternallightningnode. |
| Get Internal Lightning Balance Histogram | `getInternalLightningHistogram` | Returns a time series of the internal Lightning node's balance over a chosen window, for charting. Read-only and server-admin only. |
| Get Internal Lightning Invoice | `getInternalLightningInvoice` | Returns one Lightning invoice issued by the server's internal node, by its invoice id, with status, BOLT11 string and settlement details. Read-only. |
| Get Internal Lightning Node Info | `getInternalLightningNodeInfo` | Returns information about the BTCPay server's own internal Lightning node - node URIs, alias, block height, peer and channel counts. Server-admin only: a non-admin key gets 403 missing-permission btcpay.server.canuseinternallightningnode. |
| Get Internal Lightning Payment | `getInternalLightningPayment` | Returns one outgoing Lightning payment made by the server's internal node, by payment hash, with status, amount, fee and preimage. Read-only and server-admin only. |
| Get Invoice | `getInvoice` | Returns a single invoice by id, including its current status, amount paid, metadata and public checkout link. |
| Get Notification | `getNotification` | Returns one of the authenticated user's notifications by id, with its body, link, type and seen flag. |
| Get Notification Settings | `getNotificationSettings` | Returns which notification types the authenticated user has enabled, each with its identifier, display name and enabled flag. Use the identifiers with Update Notification Settings. |
| Get On-Chain Fee Rate | `getStoreWalletFeeRate` | Returns the fee rate in satoshis per virtual byte that the node currently recommends for confirmation within the given number of blocks. Read-only; useful before quoting a withdrawal cost. |
| Get Payment Request | `getPaymentRequest` | Returns a single payment request by id, including its current status, amount already paid and archive state. |
| Get Payout | `getPayout` | Returns one payout by id with its state, destination, amount, payout method and the pull payment it belongs to. Read-only - it reports a claim, it never approves or pays it. |
| Get Point Of Sale App | `getPointOfSaleApp` | Returns the full configuration of a point-of-sale app: its items, currency, view mode, tipping and discount options and button texts. Requires a key with btcpay.store.canmodifystoresettings on the owning store. |
| Get Pull Payment | `getPullPayment` | Returns one pull payment by id with its amount, currency, schedule, archive state and public claim link. This endpoint is public - no API key is required - because claimants need to read it. |
| Get Pull Payment LNURL | `getPullPaymentLnurl` | Returns the LNURL-withdraw string and QR-friendly link for a pull payment, so a claimant can withdraw over Lightning. Only pull payments that allow a Lightning payout method have one; the others answer 400 lnurl-not-supported. |
| Get Server Health | `getServerHealth` | Returns the health of the BTCPay Server instance, including whether its blockchain nodes are fully synchronized. This is the only Greenfield endpoint that does not require authentication, so it is the cheapest way to confirm a server URL is reachable. |
| Get Server Info | `getServerInfo` | Returns BTCPay Server version, onion address, node sync status per blockchain, supported payment methods and which server features are enabled. Requires the btcpay.server.canviewstatus permission. |
| Get Store | `getStore` | Returns the full configuration of a single store by its id, including branding, checkout behaviour, receipt options and payment tolerance. |
| Get Store Email Settings | `getStoreEmailSettings` | Returns the SMTP settings a store uses to send customer emails - server, port, login, from address and whether a password is set. The password itself is never returned, only the passwordSet flag. |
| Get Store Lightning Address | `getStoreLightningAddress` | Returns one Lightning address on a store by its username, with its pricing currency, min and max amounts and any metadata stamped onto invoices it creates. |
| Get Store Lightning Balance | `getStoreLightningBalance` | Returns the on-chain and off-chain balances of the Lightning node backing a store, split into local, remote, opening and closing channel amounts. Read-only - it never moves funds. |
| Get Store Lightning Balance Histogram | `getStoreLightningHistogram` | Returns a time series of the store's Lightning balance over a chosen window, for charting. Read-only. |
| Get Store Lightning Invoice | `getStoreLightningInvoice` | Returns one Lightning invoice issued by the node backing a store, by its invoice id, with status, BOLT11 string, amount and settlement details. Read-only. |
| Get Store Lightning Node Info | `getStoreLightningNodeInfo` | Returns information about the Lightning node backing a store's Lightning payment method: node id, peer URIs, alias, block height and version. Read-only. A store with no Lightning method configured answers 404 lightning-not-configured; a store pointed at the server's internal node needs an admin key. |
| Get Store Lightning Payment | `getStoreLightningPayment` | Returns one outgoing Lightning payment made by the node backing a store, looked up by its payment hash, with status, amount, fee and preimage. Read-only. |
| Get Store Payment Method | `getStorePaymentMethod` | Returns one payment method on a store by its id, such as BTC-CHAIN or BTC-LN, with its enabled flag. Set Include Config to also return the method's configuration; for BTC-CHAIN that includes the wallet derivation scheme. |
| Get Store Rate Configuration | `getStoreRateConfiguration` | Returns a store's rate-provider settings for one rate source - the spread applied, whether a custom rate script is in use, and the script itself. Rate Source is an id from List Rate Sources. This route was added after BTCPay 2.4.4, so older servers answer 404 with an empty body. |
| Get Store Rates | `getStoreRates` | Returns the current exchange rates the store would use to price an invoice, for the currency pairs you ask for. Pass Currency Pair as e.g. BTC_USD. With no pair the store returns rates for its configured default pairs, which is an empty array on a new store. |
| Get Store Wallet Balance Histogram | `getStoreWalletHistogram` | Returns a time series of the store wallet's on-chain balance over a chosen window, suitable for charting. Each entry in series pairs with the same index in labels. Read-only. |
| Get Store Wallet Overview | `getStoreWalletOverview` | Returns the on-chain wallet summary for a store's payment method: total, confirmed and unconfirmed balance, plus the wallet label. Read-only - it never moves funds. |
| Get Store Webhook | `getStoreWebhook` | Returns a single webhook on a store by its id, including its target URL, enabled state and subscribed events. The signing secret is redacted. |
| Get Wallet Object | `getStoreWalletObject` | Returns one wallet bookkeeping object by its type and id, with its data payload and the objects it links to. Metadata only - no keys or funds are exposed. |
| Get Wallet Receive Address | `getStoreWalletReceiveAddress` | Returns the store wallet's current unused receive address with its key path and a BIP21 payment link, reserving it so it is not handed out again. This only receives funds; it never sends. Use Unreserve Wallet Receive Address to release it. |
| Get Wallet Transaction | `getStoreWalletTransaction` | Returns one on-chain transaction seen by the store wallet, by its transaction id, including amount, confirmations, status and any labels or comment attached in BTCPay. Read-only. |
| Get Webhook Delivery | `getWebhookDelivery` | Returns a single webhook delivery attempt by id, with the HTTP status BTCPay received back, any error message and whether it was a redelivery. |
| Get Webhook Delivery Payload | `getWebhookDeliveryPayload` | Returns the exact JSON event body BTCPay POSTed for a delivery attempt. This is the authoritative way to inspect a real webhook payload, for example when building or debugging a receiver. |
| Label Wallet Transaction | `patchStoreWalletTransaction` | Attaches a comment and labels to an on-chain transaction for bookkeeping inside BTCPay. This only annotates BTCPay's own record - it does not alter, resend or reprioritise the transaction on the Bitcoin network. |
| List All Apps | `listApps` | Lists every app across all stores the authenticated account can access, each with its id, type (PointOfSale or Crowdfund), owning store and archived flag. |
| List API Permissions | `listApiPermissions` | Lists every Greenfield API permission string an API key can hold, and which narrower permissions each one implies. Use it to build a least-privilege key instead of requesting "unrestricted". Served from /misc, outside the /api/v1 prefix. |
| List Internal Lightning Channels | `listInternalLightningChannels` | Lists the payment channels of the server's internal Lightning node, with remote node, capacity and local balance. Read-only and server-admin only; opening channels is deliberately not exposed by this connector. |
| List Internal Lightning Invoices | `listInternalLightningInvoices` | Lists the Lightning invoices issued by the server's internal node, with BOLT11 string, status, amount and expiry. Read-only; requires btcpay.server.canviewlightninginvoiceinternalnode. |
| List Internal Lightning Payments | `listInternalLightningPayments` | Lists outgoing Lightning payments made by the server's internal node, with status, amount, fee and payment hash. Read-only and server-admin only - listing payments never sends one. |
| List Invoices | `listInvoices` | Lists invoices for a store, newest first. Filter by status, order id, text search or a created-date range, and page with skip and take. |
| List Language Codes | `listLanguageCodes` | Lists the languages the BTCPay Server checkout page can be rendered in, as language codes with their native names. Use a code as the defaultLanguage on a store or invoice. Served from /misc, outside the /api/v1 prefix. |
| List My Notifications | `listNotifications` | Lists the in-app notifications raised for the authenticated user - new versions, store invitations, payout approvals and similar. Filter by seen state and page with skip and take. BTCPay generates these itself; there is no API to create one. |
| List Payment Requests | `listPaymentRequests` | Lists the payment requests belonging to a store. A payment request is a reusable, shareable payment page, unlike an invoice which is a single fixed charge. |
| List Payout Processors | `listPayoutProcessors` | Lists the payout processor factories installed on the server (automated on-chain sender, automated Lightning sender) and which payout methods each supports. These names are the {processor} segment used by the store payout processor endpoints. |
| List Pull Payment Payouts | `listPullPaymentPayouts` | Lists the payouts claimed against a pull payment, with each claim's state, destination and amount. Read-only - it reports claims, it does not create or approve them. |
| List Rate Sources | `listRateSources` | Lists every exchange rate source BTCPay Server can pull prices from, with the id to use when configuring a store's rate provider. Served from /misc, outside the /api/v1 prefix, and needs no store context. |
| List Server Store Roles | `listServerStoreRoles` | Lists the server-wide store role templates (Owner, Manager, Employee, Guest) available to every store on the instance. Requires a server-admin key with btcpay.server.canmodifyserversettings; a non-admin key gets a 403 missing-permission body naming that permission. |
| List Store Apps | `listStoreApps` | Lists the apps belonging to one store - its point-of-sale and crowdfund pages - with each app's id, type and archived flag. |
| List Store Invitations | `listStoreInvitations` | Lists pending invitations to join a store - users who have been added by email but have not accepted yet. Returns an empty array when every invited user has accepted. |
| List Store Lightning Addresses | `listStoreLightningAddresses` | Lists the human-readable Lightning addresses (username@yourserver) registered on a store, with the currency each one prices in and any min/max limits. A store must have a Lightning payment method configured for these to resolve. |
| List Store Lightning Channels | `listStoreLightningChannels` | Lists the payment channels of the Lightning node backing a store, with remote node, capacity, local balance and active flag. Read-only; opening or closing channels is deliberately not exposed by this connector. |
| List Store Lightning Invoices | `listStoreLightningInvoices` | Lists the Lightning invoices issued by the node backing a store, each with its BOLT11 string, status, amount and expiry. Read-only. Set Pending Only to see just the unpaid ones. |
| List Store Lightning Payments | `listStoreLightningPayments` | Lists outgoing Lightning payments made by the node backing a store, with status, amount, fee and payment hash. Read-only - listing payments never sends one. |
| List Store Payment Methods | `listStorePaymentMethods` | Lists the payment methods configured on a store, such as BTC-CHAIN for on-chain Bitcoin or BTC-LN for Lightning, and whether each is enabled. A store with none cannot create invoices. |
| List Store Payouts | `listStorePayouts` | Lists every payout on a store, across all its pull payments, with each one's state, destination, amount and payout method. Read-only; this connector deliberately does not expose creating, approving or paying out. |
| List Store Pull Payments | `listStorePullPayments` | Lists the pull payments on a store - the withdrawal offers that let a recipient claim funds up to a set amount. Read-only. Set Include Archived to also return closed ones. |
| List Store Roles | `listStoreRoles` | Lists the roles that can be assigned to users on this store, each with the permissions it grants and whether it is a server-wide template or a store-local role. Use a returned role id when adding a store user. |
| List Store Users | `listStoreUsers` | Lists the users who have access to a store, with each user's id, email and assigned role id. The store owner always appears here. |
| List Store Webhooks | `listStoreWebhooks` | Lists every webhook registered on a store, with its target URL, enabled flag and subscribed event types. The signing secret is not returned here; it is shown only once, when the webhook is created. |
| List Stores | `listStores` | Lists every BTCPay Server store the authenticated account can access, with each store's id, name, branding, invoice expiry and checkout settings. |
| List Wallet Objects | `listStoreWalletObjects` | Lists the bookkeeping objects BTCPay stores alongside a wallet - addresses, labels, payouts and their links. These are metadata records only; they hold no keys and control no funds. |
| List Wallet Transactions | `listStoreWalletTransactions` | Lists the on-chain transactions seen by a store's wallet, newest first, with amount, confirmation count and any labels or comment. Filter by status or label and page with skip and limit. Read-only. |
| List Wallet UTXOs | `listStoreWalletUtxos` | Lists the unspent transaction outputs currently held by a store's on-chain wallet, each with its outpoint, amount, address, confirmations and labels. Read-only; this is the coin set a withdrawal would draw from. |
| List Webhook Deliveries | `listWebhookDeliveries` | Lists recent delivery attempts for a webhook, each with its id, timestamp, HTTP status and success flag. Use it to diagnose why a subscriber is not receiving events. |
| Mark Notification Seen | `updateNotification` | Marks one of the authenticated user's notifications as seen or unseen and returns the updated record. Leave Seen null to toggle it. |
| Preview Addresses For Derivation Scheme | `previewStoreWalletDerivationScheme` | Derives a page of addresses from a derivation scheme you supply, without saving it to the store. Use it to confirm an xpub produces the addresses you expect before wiring it up as the store's wallet. Read-only and non-destructive. Note: BTCPay's published swagger shows a bare derivationScheme body, but the live server requires it nested under config. |
| Preview Store Rate Configuration | `previewStoreRateConfiguration` | Dry-runs a proposed rate configuration against the requested currency pairs and returns the rates it would produce, without saving anything to the store. Use it to validate a spread or a custom rate script before applying it. |
| Preview Wallet Addresses | `getStoreWalletPreview` | Returns a page of addresses derived from the store wallet's existing derivation scheme, each with its key path and index. Read-only - deriving an address neither reserves it nor moves funds. |
| Redeliver Webhook Delivery | `redeliverWebhookDelivery` | Queues a fresh delivery attempt of a past webhook event and returns the new delivery id. Use it to replay an event after fixing a receiver that was down or returning errors. |
| Unarchive Invoice | `unarchiveInvoice` | Restores a previously archived invoice so it appears in the default invoice list again, and returns the full invoice. |
| Unreserve Wallet Receive Address | `unreserveStoreWalletReceiveAddress` | Releases the receive address currently reserved by Get Wallet Receive Address so the wallet can hand it out again. Nothing is spent or deleted - only the reservation flag is cleared. |
| Update Crowdfund App | `updateCrowdfundApp` | Replaces a crowdfund app's configuration. BTCPay overwrites the whole record, so send every value you want to keep, including the Perks Template. |
| Update Invoice Metadata | `updateInvoice` | Replaces an invoice's metadata object. Only metadata is editable once an invoice exists; the amount, currency and checkout settings are fixed at creation. |
| Update Notification Settings | `updateNotificationSettings` | Chooses which notification types the authenticated user does NOT receive. Pass the identifiers to disable in Disabled (identifiers come from Get Notification Settings), the single value "all" to disable every type, or an empty list to enable every type. |
| Update Payment Request | `updatePaymentRequest` | Replaces a payment request's details. BTCPay overwrites the whole record, so send every value you want to keep including title, amount and currency. |
| Update Point Of Sale App | `updatePointOfSaleApp` | Replaces a point-of-sale app's configuration. BTCPay overwrites the whole record, so send every value you want to keep, including the items Template. |
| Update Store | `updateStore` | Updates a store's settings. BTCPay replaces the whole store record, so send the full set of values you want to keep; fields you omit revert to their defaults. |
| Update Store Email Settings | `updateStoreEmailSettings` | Replaces the SMTP settings a store uses to send customer emails. Leave Password null or empty to keep the stored one. The response never echoes the password, only passwordSet. |
| Update Store Payment Method | `updateStorePaymentMethod` | Enables, disables or reconfigures one payment method on a store. For BTC-LN pass config {"connectionString":"Internal Node"} to use the server's own Lightning node; for BTC-CHAIN pass a derivation scheme. Sending only enabled leaves the existing configuration intact. |
| Update Store Rate Configuration | `updateStoreRateConfiguration` | Replaces a store's rate-provider settings for one rate source: the preferred exchange, the spread to apply and optionally a custom rate script. This route was added after BTCPay 2.4.4, so older servers answer 404 with an empty body. |
| Update Store Webhook | `updateStoreWebhook` | Replaces a webhook's configuration. Send the complete desired state, including the target URL and authorized events, because BTCPay overwrites the whole record. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Invoice Created | `InvoiceCreated` | Fires as soon as an invoice is created on the store. Payload schema below is a REAL captured delivery from BTCPay Server 2.4.4. |
| Invoice Expired | `InvoiceExpired` | Fires when an invoice passes its expiry without sufficient payment. Schema MODELLED from the BTCPay Greenfield spec. |
| Invoice Invalid | `InvoiceInvalid` | Fires when an invoice is marked invalid, for example after a failed or reverted payment. Schema MODELLED from the BTCPay Greenfield spec. |
| Invoice Payment Settled | `InvoicePaymentSettled` | Fires when an individual payment against an invoice reaches the required confirmations. Schema MODELLED from the BTCPay Greenfield spec. |
| Invoice Processing | `InvoiceProcessing` | Fires when an invoice is fully paid but not yet settled to the store's speed policy. Schema MODELLED from the BTCPay Greenfield spec. |
| Invoice Received Payment | `InvoiceReceivedPayment` | Fires when a payment is seen for an invoice, before it is confirmed. Schema MODELLED from the BTCPay Greenfield spec, not captured, because settling an invoice requires moving real funds. |
| Invoice Settled | `InvoiceSettled` | Fires when an invoice is fully paid and confirmed. This is the event most order-fulfilment flows listen for. Schema MODELLED from the BTCPay Greenfield spec. |
| Payment Request Archived | `PaymentRequestArchived` | Fires when a payment request is archived. Schema MODELLED from the BTCPay Greenfield spec. |
| Payment Request Created | `PaymentRequestCreated` | Fires when a payment request is created on the store. Schema MODELLED from the BTCPay Greenfield spec. |
| Payment Request Status Changed | `PaymentRequestStatusChanged` | Fires when a payment request moves between Pending, Completed and Expired. Schema MODELLED from the BTCPay Greenfield spec. |
| Payment Request Updated | `PaymentRequestUpdated` | Fires when a payment request's details change. Schema MODELLED from the BTCPay Greenfield spec. |
| Payout Approved | `PayoutApproved` | Fires when a payout is approved for payment. Schema MODELLED from the BTCPay Greenfield spec; payout routes move real funds and were deliberately not driven. |
| Payout Created | `PayoutCreated` | Fires when a payout is created against a pull payment. Schema MODELLED from the BTCPay Greenfield spec; payout routes move real funds and were deliberately not driven. |
| Payout Updated | `PayoutUpdated` | Fires when a payout changes state, for example to InProgress or Completed. Schema MODELLED from the BTCPay Greenfield spec; payout routes move real funds and were deliberately not driven. |
