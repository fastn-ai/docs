---
description: "Payhip is a platform for selling digital products and courses. Create and look up coupons and manage license keys."
hidden: true
---

# Payhip

<img src="../../.gitbook/assets/connectors/lg/payhip.png" alt="Payhip logo">

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [payhip.com](https://payhip.com) |
| **Authentication** | API key |
| **Slug** | `payhip` |

## Setup

Your customers enter their API key for Payhip when they connect. Nothing else needs setting up.

## Use it

Add Payhip from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.payhip.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Coupon</td><td><code>createCoupon</code></td><td>Creates a discount coupon on your Payhip account. Supply either percent_off or amount_off - Payhip rejects a request that has neither. Coupons for subscription products with a recurring amount cannot be created through the API.</td></tr><tr><td>Decrease Legacy License Key Usage</td><td><code>decreaseLegacyLicenseKeyUsage</code></td><td>Decrements the usage counter of a software license key through Payhip's legacy (v1) license system. Authenticates with your account API key and requires the product link alongside the key.</td></tr><tr><td>Decrease License Key Usage</td><td><code>decreaseLicenseKeyUsage</code></td><td>Decrements the usage counter of a Payhip software license key by one, for example when a customer deactivates one of their installations. Authenticate with the Product Secret Key auth method for the product that issued the key; the account API key is also accepted.</td></tr><tr><td>Disable Legacy License Key</td><td><code>disableLegacyLicenseKey</code></td><td>Disables a software license key through Payhip's legacy (v1) license system so it no longer verifies. Authenticates with your account API key and requires the product link alongside the key.</td></tr><tr><td>Disable License Key</td><td><code>disableLicenseKey</code></td><td>Disables a Payhip software license key so it no longer verifies, for example when a customer breaks your terms of service. Payhip disables a key automatically when its transaction is refunded. Authenticate with the Product Secret Key auth method for the product that issued the key; the account API key is also accepted.</td></tr><tr><td>Enable Legacy License Key</td><td><code>enableLegacyLicenseKey</code></td><td>Re-enables a previously disabled software license key through Payhip's legacy (v1) license system. Authenticates with your account API key and requires the product link alongside the key.</td></tr><tr><td>Enable License Key</td><td><code>enableLicenseKey</code></td><td>Re-enables a Payhip software license key that was previously disabled, so it verifies again. Authenticate with the Product Secret Key auth method for the product that issued the key; the account API key is also accepted.</td></tr><tr><td>Get Coupon</td><td><code>getCoupon</code></td><td>Retrieves a single discount coupon from your Payhip account by its numeric coupon ID.</td></tr><tr><td>Increase Legacy License Key Usage</td><td><code>increaseLegacyLicenseKeyUsage</code></td><td>Increments the usage counter of a software license key through Payhip's legacy (v1) license system. Authenticates with your account API key and requires the product link alongside the key.</td></tr><tr><td>Increase License Key Usage</td><td><code>increaseLicenseKeyUsage</code></td><td>Increments the usage counter of a Payhip software license key by one, so you can enforce how many times a customer may activate your software. Authenticate with the Product Secret Key auth method for the product that issued the key; the account API key is also accepted.</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Coupons</td><td><code>listCoupons</code></td><td>Retrieves a paginated list of all discount coupons created on your Payhip account. Use limit and offset to page through the results.</td></tr><tr><td>Verify Legacy License Key</td><td><code>verifyLegacyLicenseKey</code></td><td>Verifies a software license key through Payhip's legacy (v1) license system, which authenticates with your account API key and requires the product link alongside the key. Use this when your products predate the product secret key system. When the key cannot be verified Payhip returns an empty data array instead of an error.</td></tr><tr><td>Verify License Key</td><td><code>verifyLicenseKey</code></td><td>Verifies a software license key issued by Payhip and returns the purchase it belongs to. Authenticate the connection with the Product Secret Key auth method for the product that issued the key; the account API key is also accepted. When the key cannot be verified Payhip returns an empty data array instead of an error.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Payment Received</td><td><code>paid</code></td><td>Fires whenever a customer is charged for a purchase in your Payhip store. Payhip has no webhook registration API, so the customer registers the Fastn trigger URL by hand: open the Payhip dashboard, go to Account &gt; Settings &gt; Developer, paste the Fastn trigger URL into the webhook endpoint field (multiple endpoints are comma separated), tick the 'paid' event and save. All money amounts are in the smallest currency unit, so 1000 means 10.00.</td></tr><tr><td>Payment Refunded</td><td><code>refunded</code></td><td>Fires whenever a payment in your Payhip store is refunded, in full or in part. Compare amount_refunded with price to tell the two apart. Payhip has no webhook registration API, so the customer registers the Fastn trigger URL by hand: open the Payhip dashboard, go to Account &gt; Settings &gt; Developer, paste the Fastn trigger URL into the webhook endpoint field, tick the 'refunded' event and save.</td></tr><tr><td>Subscription Cancelled</td><td><code>subscription.deleted</code></td><td>Fires whenever a customer's subscription to one of your Payhip memberships or plans is cancelled. Payhip has no webhook registration API, so the customer registers the Fastn trigger URL by hand: open the Payhip dashboard, go to Account &gt; Settings &gt; Developer, paste the Fastn trigger URL into the webhook endpoint field, tick the 'subscription.deleted' event and save.</td></tr><tr><td>Subscription Created</td><td><code>subscription.created</code></td><td>Fires whenever a customer starts a subscription to one of your Payhip memberships or plans. Payhip has no webhook registration API, so the customer registers the Fastn trigger URL by hand: open the Payhip dashboard, go to Account &gt; Settings &gt; Developer, paste the Fastn trigger URL into the webhook endpoint field, tick the 'subscription.created' event and save.</td></tr></tbody></table>
