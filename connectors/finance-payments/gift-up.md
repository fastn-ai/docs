---
description: "Gift Up is a gift card and gift certificate platform for small businesses."
hidden: true
---

# Gift Up

<img src="../../.gitbook/assets/connectors/gift-up.png" alt="Gift Up logo" width="64">

Gift Up is a gift card and gift certificate platform for small businesses. This connector covers the full Gift Up REST API: gift cards (issue, look up, update, redeem, top up, void, reactivate and transfer balances), orders, catalogue items and groups, promotions, locations, users, transaction reports, checkout, email, gift card, artwork and shipping settings, the Stripe integration, partner account provisioning and webhook subscriptions.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [giftup.com](https://giftup.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `giftUp` |

## Use it

Add Gift Up from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.giftUp.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Order Note | `addOrderNote` | Adds an internal note to an order. Notes support line breaks and are limited to 500 characters. |
| Create Item | `createItem` | Creates a new gift card item for sale on the Gift Up checkout. Currency-backed items need a value; unit-backed items need units and an equivalent value per unit. Specify either Group or Group ID, never both. |
| Create Item Group | `createItemGroup` | Creates an item group to organise how gift card items are presented on the Gift Up checkout. |
| Create Order | `createOrder` | Creates an order containing one or more gift cards and optionally emails or posts them to a recipient. Set Disable All Emails to issue cards without notifying anyone. Creating an order in live mode incurs Gift Up's fee - use the connection's Test Mode setting while developing. |
| Create Partner Account | `createPartnerAccount` | Provisions a new Gift Up account on behalf of a customer. This endpoint is restricted to platform partners Gift Up has pre-approved; other keys are refused with 'Open to pre-approved partners only'. Store the returned companyId and send it as the x-giftup-account header to make later calls against that account. |
| Delete Gift Card Artwork | `deleteGiftCardArtwork` | Deletes one gift card artwork design by its id so it is no longer offered on the checkout. |
| Delete Item | `deleteItem` | Deletes a gift card item by its id so it no longer appears on the Gift Up checkout. |
| Delete Item Group | `deleteItemGroup` | Deletes an item group by its id. Gift Up rejects the request with HTTP 400 if the group still contains items, so move or delete those first. |
| Delete User | `deleteUser` | Removes a staff user's access to the Gift Up account. Check the id belongs to the intended person before calling this - the removal takes effect immediately. |
| Delete Webhook | `deleteWebhook` | Removes a webhook subscription by its id so Gift Up stops posting that event to the URL. |

<details>

<summary>See 44 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Checkout Settings | `getCheckoutSettings` | Retrieves the Gift Up checkout settings - branding, wording, tipping, custom fields, taxes and the other options that control how the purchase page behaves. |
| Get Company | `getCompany` | Retrieves the Gift Up company that the stored API key belongs to, including its trading currency, onboarding progress, whether the checkout can render, and suspension state. |
| Get Email Settings | `getEmailSettings` | Retrieves the Gift Up email settings - the sender identity, subject lines and body copy used for the emails sent to purchasers and recipients. |
| Get Gift Card | `getGiftCard` | Retrieves a single gift card by its code, including its balance, validity flags, fulfilment details, download links and full event ledger. |
| Get Gift Card Settings | `getGiftCardSettings` | Retrieves the account-wide gift card settings, including the default terms, expiry rules and the code format template used when Gift Up generates gift card codes. |
| Get Item | `getItem` | Retrieves one gift card item by its id, including its pricing, validity and expiry rules, stock level and pre-generated codes. |
| Get Item Group | `getItemGroup` | Retrieves one item group by its id. |
| Get Order | `getOrder` | Retrieves one gift card order by its id or order number, including its gift cards, fulfilments, notes, taxes, promotions and download links. |
| Get Shipping Settings | `getShippingSettings` | Retrieves the postal shipping settings - the shipping options, prices and destination countries offered when a purchaser chooses to have a gift card posted. |
| Get Stripe Connection | `getStripeConnection` | Retrieves the Stripe connection currently configured on the Gift Up account, so gift card purchases can be charged through Stripe. |
| Get Transaction | `getTransaction` | Retrieves a single ledger transaction by its id. |
| Get User | `getUser` | Retrieves one staff user of the Gift Up account by their id. |
| Get Webhook | `getWebhook` | Retrieves one webhook subscription by its id. |
| List Gift Card Artwork | `listGiftCardArtwork` | Lists the gift card artwork uploaded to the account. The artwork with sort order 1 is the design shown to purchasers first on the checkout. |
| List Gift Cards | `listGiftCards` | Lists gift cards, optionally narrowed by state, creation or update date, order, SKU, recipient or purchaser email, or payment transaction. Results are paginated with limit and offset. |
| List Item Groups | `listItemGroups` | Lists every item group that organises the items shown on the Gift Up checkout. |
| List Items | `listItems` | Lists every gift card item offered on the Gift Up checkout, optionally narrowed to a single item group. |
| List Locations | `listLocations` | Lists the physical or logical locations configured on the Gift Up account. Location ids can be attached to redemptions, top-ups, voids and reactivations to record where each event happened. |
| List Orders | `listOrders` | Lists gift card orders, optionally narrowed by creation date, purchaser email or the channel the order came from. Results are paginated with limit and offset. |
| List Promotions | `listPromotions` | Lists the promotions and discount codes configured on the Gift Up checkout. |
| List Transactions | `listTransactions` | Lists ledger transactions across the account - orders placed, gift cards created, redemptions, top-ups, voids and expiries - optionally narrowed by date range, event type, user, location or gift card code. Gift Up accepts repeated event, user and location parameters; this action sends one value each. |
| List Users | `listUsers` | Lists the staff users who have access to the Gift Up account, with their roles and the locations they are assigned to. |
| List Webhooks | `listWebhooks` | Lists every webhook subscription registered on the Gift Up account, with its delivery URL, event type and whether it fires on test data only. |
| Mark Order As Posted | `markOrderAsPosted` | Marks a postal order as posted and swaps its provisional gift card codes for the codes actually printed. The codes list must cover every code on the order; repeat the old code as the new code to leave one unchanged. |
| Ping | `ping` | Checks that the Gift Up API is reachable and that the stored API key is accepted. Returns the literal text 'pong'. |
| Ping With Post | `pingWithPost` | Checks Gift Up API reachability and key validity over POST, for callers that need to confirm write-verb connectivity as well as read. |
| Reactivate Gift Card | `reactivateGiftCard` | Reactivates a voided gift card so it can be redeemed again, provided it still has a positive balance. Gift Up answers HTTP 422 with isRedeemed or isAlreadyActive when the card cannot be reactivated. |
| Redeem Gift Card | `redeemGiftCard` | Deducts an amount from a gift card's balance. Supply Amount for currency-backed cards or Units for unit-backed cards; the value must not exceed the remaining balance. Returns the transaction id needed to reverse the redemption later. |
| Redeem Gift Card In Full | `redeemGiftCardInFull` | Redeems the entire remaining balance of a gift card in one operation, leaving it with a zero balance. Returns the transaction id needed to reverse the redemption later. |
| Subscribe Webhook | `subscribeWebhook` | Registers a webhook so Gift Up posts an event to your URL. Before the subscription is created Gift Up POSTs {"test": true} to the target URL and requires an HTTP 200 back. Returns the new webhook id, which is what Delete Webhook takes. |
| Top Up Gift Card | `topUpGiftCard` | Adds balance to a gift card. Supply Amount for currency-backed cards or Units for unit-backed cards. A voided gift card cannot be topped up. |
| Transfer Gift Card Balances | `transferGiftCardBalances` | Moves the remaining balance of one or more source gift cards onto a single destination gift card, leaving the sources at zero. |
| Undo Gift Card Redemption | `undoGiftCardRedemption` | Reverses a previous redemption and returns the balance to the gift card. The transaction id comes from the redemption response or from the card's ledger. |
| Update Checkout Settings | `updateCheckoutSettings` | Updates the Gift Up checkout settings using JSON Patch. Supply the patch operations as a JSON array string; read Get Checkout Settings first to see the exact property names available to patch. |
| Update Email Settings | `updateEmailSettings` | Updates the Gift Up email settings using JSON Patch. Supply the patch operations as a JSON array string; read Get Email Settings first to see the exact property names available to patch. |
| Update Gift Card | `updateGiftCard` | Updates a gift card using JSON Patch. Supply the patch operations as a JSON array string, for example [{"op":"replace","path":"/title","value":"All you can eat steak"}]. The patchable paths are /title, /expireson, /validfrom, /receipientemail, /recipientname, /sku and /terms. |
| Update Gift Card Settings | `updateGiftCardSettings` | Updates the account-wide gift card settings using JSON Patch. Supply the patch operations as a JSON array string; read Get Gift Card Settings first to see the exact property names available to patch. |
| Update Item | `updateItem` | Updates a gift card item using JSON Patch. Supply the patch operations as a JSON array string, for example [{"op":"replace","path":"/price","value":99.99}]. Add operations work on collections such as /codes. |
| Update Item Group | `updateItemGroup` | Updates an item group using JSON Patch. Supply the patch operations as a JSON array string. Patchable paths are /name, /description and /autoExpand. |
| Update Order | `updateOrder` | Updates an order using JSON Patch. Supply the patch operations as a JSON array string. Patchable paths are /purchasername and /purchaseremail. |
| Update Stripe Connection | `updateStripeConnection` | Create or update the Stripe gateway connection (POST /integrations/stripe/connection). Sends the documented body: live/test publishable and secret keys, payment-method toggles, Connect fee fields and checkout options. Gift Up tests the keys and returns testResult. |
| Update User | `updateUser` | Updates a staff user of the Gift Up account using JSON Patch. Supply the patch operations as a JSON array string; read Get User first to see the exact property names available to patch. |
| Upload Gift Card Artwork | `uploadGiftCardArtwork` | Adds a new gift card artwork design. Supply either a fully qualified image URL that Gift Up downloads, or a base64 data URI starting with data:image. Optionally replace one existing design or clear them all first. |
| Void Gift Card | `voidGiftCard` | Voids a gift card so it can no longer be redeemed. Gift Up answers HTTP 422 with isRedeemed or isAlreadyVoided when the card cannot be voided. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Gift Card Created | `gift-card-created` | Fires when a new gift card is issued, whether through the checkout, the dashboard or the API. The payload is the full gift card object. |
| Gift Card Redeemed | `gift-card-redeemed` | Fires when balance is redeemed from a gift card. The payload is the full gift card object plus who redeemed it, how much, and when. |
| Gift Card Updated | `gift-card-updated` | Fires when an existing gift card changes - a balance top-up, a void, a reactivation or an edit to its details. The payload is the full gift card object with no extra properties. |
| Order Created | `order-created` | Fires when a gift card order is placed. The payload is the full order object plus the revenue formatted as a currency string. |
