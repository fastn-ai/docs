---
description: "Zylvie is creator-commerce cart software for selling digital products, subscriptions and lead magnets."
---

# Zylvie

Zylvie is creator-commerce cart software for selling digital products, subscriptions and lead magnets. This connector wraps the Zylvie REST API (https://api.zylvie.com) covering the authenticated brand, products, coupons and per-email coupon grants, license keys, subscriptions, transactions and webhook workflow subscriptions.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [zylvie.com](https://zylvie.com) |
| **Authentication** | Bearer token |
| **Actions** | 19 |
| **Events** | 5 |
| **Slug** | `zylvie` |

## Use it

Add Zylvie from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zylvie.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Coupon | `createCoupon` | Creates a discount coupon for the authenticated brand. Coupons are inactive until is_live is set to true. Storewide coupons work over the API; product-scoped coupons do not, because the products field rejects the public product id (see that field's description). |
| Create Coupon Email Grant | `createCouponEmailGrant` | Starts a per-email redemption window for a shared coupon code, so that email may redeem a coupon that has valid_for_days set. The first grant for an email wins: later calls return the original granted_at and do not reset the clock. Identify the coupon with either code or id. |
| Create Product | `createProduct` | Creates a product in your Zylvie store. Set display to 'unpublished' to keep it off the public storefront. Returns the created product including its id. |
| Delete Coupon | `deleteCoupon` | Deletes a coupon by id. If the coupon has been used in paid transactions, Zylvie archives it instead of deleting it and says so in the message field. |
| Delete Product | `deleteProduct` | Deletes a product by id. If the product has paid transactions, active subscriptions, or variants with paid transactions, Zylvie archives it instead of deleting it and says so in the message field. |
| Get Authenticating Brand | `getAuthenticatingBrand` | Returns the Zylvie account that the API key authenticates as, including the account email and the brand (store) name. Useful as a connection health check. |
| Get Coupon Email Grant | `getCouponEmailGrant` | Looks up an existing per-email coupon grant and returns when eligibility started and when it expires. Identify the coupon with either code or id. |
| List Coupons | `listCoupons` | Lists every coupon belonging to the authenticated brand, with its discount type, amount, validity window and current redemption count. Set archived to true to list archived coupons instead of active ones. |
| List Subscriptions | `listSubscriptions` | Lists paginated subscriptions for the authenticated brand, newest first, with status, trial window, product and subscriber. Monetary amounts are in the currency's major unit (unlike Verify Subscription, which returns cents). |
| List Transactions | `listTransactions` | Lists paginated transactions for the authenticated brand, newest first, covering one-time purchases, subscription sign-ups and renewals, with payment and refund status. Monetary amounts are in the currency's major unit. |
| List Uploaded License Codes | `listUploadedLicenseCodes` | Inspects the pool of license codes you uploaded by CSV for a product: which codes are still unused and which have been assigned to buyers, with the redeem and refund status of each assigned code. |
| Redeem License Key | `redeemLicenseKey` | Marks a buyer's license key as redeemed/used. If the key was already redeemed, Zylvie returns HTTP 200 with an error envelope carrying error = 'Already redeemed' plus the original redeemed_at - check the body, not just the status code. |
| Refund License Key | `refundLicenseKey` | Marks a buyer's license key as refunded/invalidated. This only flags the key inside Zylvie; it does not move any money. If the key was already refunded, Zylvie returns HTTP 200 with an error envelope carrying error = 'Already refunded' plus the original refunded_at - check the body, not just the status code. |
| Subscribe Webhook | `subscribeWebhook` | Creates a Zylvie workflow that POSTs the chosen event to your webhook URL, and returns the workflow including its HMAC-SHA1 signing_secret. If a workflow already exists for the same webhook URL, the existing workflow is returned unchanged. |
| Unsubscribe Webhook | `unsubscribeWebhook` | Deletes the Zylvie workflow registered for the given webhook URL. Returns HTTP 200 with an empty body. If no workflow matches the URL, nothing changes. |
| Update Coupon | `updateCoupon` | Updates a coupon by id. NOTE, proven live and contrary to Zylvie's docs: this is a REPLACE, not a merge - code and type are rejected as required if omitted, and fields you leave out are reset (is_storewide and limit_one_per_email fall back to false, valid_for_days to null). Send the coupon's full current state with your changes applied. Supplying products replaces the existing product list. |
| Update Product | `updateProduct` | Updates a product by id. NOTE, proven live and contrary to Zylvie's docs: this is a REPLACE, not a merge - id, title, url, currency, price and pricing_model are all rejected as required if omitted, and fields you leave out are reset to their defaults. Send the product's full current state with your changes applied. categories, tags, productimages and productfiles likewise replace the existing values. |
| Verify License Key | `verifyLicenseKey` | Verifies that a license key supplied by a buyer is valid, paid for, and belongs to the given product. Returns the key with its buyer email and redeem/refund status. Zylvie answers with a 404 page when the key is not found for that product. |
| Verify Subscription By Email | `verifySubscriptionByEmail` | Checks whether an email address has any subscriptions and returns their status. The response is a TOP-LEVEL JSON ARRAY of subscription objects, each with subscription_id, created_at, cancel_at, canceled_at, trial_start, trial_end, currency, amount (in CENTS, unlike List Subscriptions), interval, interval_count, status, product.title and a subscriber block. Zylvie answers 404 {"status":"error","message":"No subscriptions found"} when the email has none. No outputContract is declared because the fastn engine rejects a top-level array output schema. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| New Affiliate Sign-Up | `affiliate` | Fires when an affiliate signs up or accepts your private affiliate invitation. Payload schema is MODELLED from Zylvie's documented sample at https://developers.zylvie.com/webhooks/affiliate, not captured from a live delivery. |
| New Lead | `lead` | Fires when someone submits their name and email to download a free product or lead magnet. Payload schema is MODELLED from Zylvie's documented sample at https://developers.zylvie.com/webhooks/lead, not captured from a live delivery. |
| New Sale | `sale` | Fires when a buyer completes a paid purchase in your Zylvie store (money is transacted). Not fired for free products - use the Lead event for those. Payload schema is MODELLED from Zylvie's documented sample at https://developers.zylvie.com/webhooks/sale, not captured from a live delivery. |
| New Subscription | `subscription` | Fires when a buyer subscribes to a subscription product, including sign-ups that start with a free trial. Payload schema is MODELLED from Zylvie's documented sample at https://developers.zylvie.com/webhooks/subscription, not captured from a live delivery. |
| Subscription Cancelled | `cancel` | Fires when a current subscriber cancels their subscription to a subscription product. Payload schema is MODELLED from Zylvie's documented sample at https://developers.zylvie.com/webhooks/cancel, not captured from a live delivery. |
