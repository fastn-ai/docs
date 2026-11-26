---
description: "Zylvie is a platform for selling digital products and subscriptions. Create and manage products and coupons."
hidden: true
---

# Zylvie

<img src="../../.gitbook/assets/connectors/lg/zylvie.png" alt="Zylvie logo">

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [zylvie.com](https://zylvie.com) |
| **Authentication** | Access token |
| **Slug** | `zylvie` |

## Setup

Your customers enter their access token for Zylvie when they connect. Nothing else needs setting up.

## Use it

Add Zylvie from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zylvie.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Coupon</td><td><code>createCoupon</code></td><td>Creates a discount coupon for the authenticated brand. Coupons are inactive until is_live is set to true. Storewide coupons work over the API; product-scoped coupons do not, because the products field rejects the public product id (see that field's description).</td></tr><tr><td>Create Coupon Email Grant</td><td><code>createCouponEmailGrant</code></td><td>Starts a per-email redemption window for a shared coupon code, so that email may redeem a coupon that has valid_for_days set. The first grant for an email wins: later calls return the original granted_at and do not reset the clock. Identify the coupon with either code or id.</td></tr><tr><td>Create Product</td><td><code>createProduct</code></td><td>Creates a product in your Zylvie store. Set display to 'unpublished' to keep it off the public storefront. Returns the created product including its id.</td></tr><tr><td>Delete Coupon</td><td><code>deleteCoupon</code></td><td>Deletes a coupon by id. If the coupon has been used in paid transactions, Zylvie archives it instead of deleting it and says so in the message field.</td></tr><tr><td>Delete Product</td><td><code>deleteProduct</code></td><td>Deletes a product by id. If the product has paid transactions, active subscriptions, or variants with paid transactions, Zylvie archives it instead of deleting it and says so in the message field.</td></tr><tr><td>Get Authenticating Brand</td><td><code>getAuthenticatingBrand</code></td><td>Returns the Zylvie account that the API key authenticates as, including the account email and the brand (store) name. Useful as a connection health check.</td></tr><tr><td>Get Coupon Email Grant</td><td><code>getCouponEmailGrant</code></td><td>Looks up an existing per-email coupon grant and returns when eligibility started and when it expires. Identify the coupon with either code or id.</td></tr><tr><td>List Coupons</td><td><code>listCoupons</code></td><td>Lists every coupon belonging to the authenticated brand, with its discount type, amount, validity window and current redemption count. Set archived to true to list archived coupons instead of active ones.</td></tr><tr><td>List Subscriptions</td><td><code>listSubscriptions</code></td><td>Lists paginated subscriptions for the authenticated brand, newest first, with status, trial window, product and subscriber. Monetary amounts are in the currency's major unit (unlike Verify Subscription, which returns cents).</td></tr><tr><td>List Transactions</td><td><code>listTransactions</code></td><td>Lists paginated transactions for the authenticated brand, newest first, covering one-time purchases, subscription sign-ups and renewals, with payment and refund status. Monetary amounts are in the currency's major unit.</td></tr></tbody></table>

<details>

<summary>View 9 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Uploaded License Codes</td><td><code>listUploadedLicenseCodes</code></td><td>Inspects the pool of license codes you uploaded by CSV for a product: which codes are still unused and which have been assigned to buyers, with the redeem and refund status of each assigned code.</td></tr><tr><td>Redeem License Key</td><td><code>redeemLicenseKey</code></td><td>Marks a buyer's license key as redeemed/used. If the key was already redeemed, Zylvie</td></tr><tr><td>Refund License Key</td><td><code>refundLicenseKey</code></td><td>Marks a buyer's license key as refunded/invalidated. This only flags the key inside Zylvie; it does not move any money. If the key was already refunded, Zylvie</td></tr><tr><td>Subscribe Webhook</td><td><code>subscribeWebhook</code></td><td>Creates a Zylvie workflow that POSTs the chosen event to your webhook URL, and returns the workflow including its HMAC-SHA1 signing_secret. If a workflow already exists for the same webhook URL, the existing workflow is returned unchanged.</td></tr><tr><td>Unsubscribe Webhook</td><td><code>unsubscribeWebhook</code></td><td>Deletes the Zylvie workflow registered for the given webhook URL. If no workflow matches the URL, nothing changes.</td></tr><tr><td>Update Coupon</td><td><code>updateCoupon</code></td><td>Updates a coupon by id. NOTE, proven live and contrary to Zylvie's docs: this is a REPLACE, not a merge - code and type are rejected as required if omitted, and fields you leave out are reset (is_storewide and limit_one_per_email fall back to false, valid_for_days to null). Send the coupon's full current state with your changes applied. Supplying products replaces the existing product list.</td></tr><tr><td>Update Product</td><td><code>updateProduct</code></td><td>Updates a product by id. NOTE, proven live and contrary to Zylvie's docs: this is a REPLACE, not a merge - id, title, url, currency, price and pricing_model are all rejected as required if omitted, and fields you leave out are reset to their defaults. Send the product's full current state with your changes applied. categories, tags, productimages and productfiles likewise replace the existing values.</td></tr><tr><td>Verify License Key</td><td><code>verifyLicenseKey</code></td><td>Verifies that a license key supplied by a buyer is valid, paid for, and belongs to the given product. Returns the key with its buyer email and redeem/refund status. Zylvie answers with a 404 page when the key is not found for that product.</td></tr><tr><td>Verify Subscription By Email</td><td><code>verifySubscriptionByEmail</code></td><td>Checks whether an email address has any subscriptions and returns their status. The response is a TOP-LEVEL JSON ARRAY of subscription objects, each with subscription_id, created_at, cancel_at, canceled_at, trial_start, trial_end, currency, amount (in CENTS, unlike List Subscriptions), interval, interval_count, status, product.title and a subscriber block. No outputContract is declared because the Fastn engine rejects a top-level array output schema.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>New Affiliate Sign-Up</td><td><code>affiliate</code></td><td>Fires when an affiliate signs up or accepts your private affiliate invitation.</td></tr><tr><td>New Lead</td><td><code>lead</code></td><td>Fires when someone submits their name and email to download a free product or lead magnet.</td></tr><tr><td>New Sale</td><td><code>sale</code></td><td>Fires when a buyer completes a paid purchase in your Zylvie store (money is transacted). Not fired for free products - use the Lead event for those.</td></tr><tr><td>New Subscription</td><td><code>subscription</code></td><td>Fires when a buyer subscribes to a subscription product, including sign-ups that start with a free trial.</td></tr><tr><td>Subscription Cancelled</td><td><code>cancel</code></td><td>Fires when a current subscriber cancels their subscription to a subscription product.</td></tr></tbody></table>
