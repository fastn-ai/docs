---
description: "Payhip is an e-commerce platform for selling digital downloads, courses, memberships and coupons."
---

# Payhip

Payhip is an e-commerce platform for selling digital downloads, courses, memberships and coupons. This connector covers the complete Payhip public REST API: coupon management (create, list, retrieve) and software license key enforcement on both the current product-secret-key API (v2) and the legacy account API key API (v1) - verify, enable, disable and adjust usage counters. Payhip store events (paid, refunded, subscription.created, subscription.deleted) are delivered as webhooks configured in the Payhip dashboard.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [payhip.com](https://payhip.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 13 |
| **Events** | 4 |
| **Slug** | `payhip` |

## Use it

Add Payhip from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.payhip.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Coupon | `createCoupon` | Creates a discount coupon on your Payhip account. Supply either percent_off or amount_off - Payhip rejects a request that has neither. Coupons for subscription products with a recurring amount cannot be created through the API. |
| Decrease Legacy License Key Usage | `decreaseLegacyLicenseKeyUsage` | Decrements the usage counter of a software license key through Payhip's legacy (v1) license system. Authenticates with your account API key and requires the product link alongside the key. |
| Decrease License Key Usage | `decreaseLicenseKeyUsage` | Decrements the usage counter of a Payhip software license key by one, for example when a customer deactivates one of their installations. Authenticate with the Product Secret Key auth method for the product that issued the key; the account API key is also accepted. |
| Disable Legacy License Key | `disableLegacyLicenseKey` | Disables a software license key through Payhip's legacy (v1) license system so it no longer verifies. Authenticates with your account API key and requires the product link alongside the key. |
| Disable License Key | `disableLicenseKey` | Disables a Payhip software license key so it no longer verifies, for example when a customer breaks your terms of service. Payhip disables a key automatically when its transaction is refunded. Authenticate with the Product Secret Key auth method for the product that issued the key; the account API key is also accepted. |
| Enable Legacy License Key | `enableLegacyLicenseKey` | Re-enables a previously disabled software license key through Payhip's legacy (v1) license system. Authenticates with your account API key and requires the product link alongside the key. |
| Enable License Key | `enableLicenseKey` | Re-enables a Payhip software license key that was previously disabled, so it verifies again. Authenticate with the Product Secret Key auth method for the product that issued the key; the account API key is also accepted. |
| Get Coupon | `getCoupon` | Retrieves a single discount coupon from your Payhip account by its numeric coupon ID. |
| Increase Legacy License Key Usage | `increaseLegacyLicenseKeyUsage` | Increments the usage counter of a software license key through Payhip's legacy (v1) license system. Authenticates with your account API key and requires the product link alongside the key. |
| Increase License Key Usage | `increaseLicenseKeyUsage` | Increments the usage counter of a Payhip software license key by one, so you can enforce how many times a customer may activate your software. Authenticate with the Product Secret Key auth method for the product that issued the key; the account API key is also accepted. |
| List Coupons | `listCoupons` | Retrieves a paginated list of all discount coupons created on your Payhip account. Use limit and offset to page through the results. |
| Verify Legacy License Key | `verifyLegacyLicenseKey` | Verifies a software license key through Payhip's legacy (v1) license system, which authenticates with your account API key and requires the product link alongside the key. Use this when your products predate the product secret key system. When the key cannot be verified Payhip returns an empty data array instead of an error. |
| Verify License Key | `verifyLicenseKey` | Verifies a software license key issued by Payhip and returns the purchase it belongs to. Authenticate the connection with the Product Secret Key auth method for the product that issued the key; the account API key is also accepted. When the key cannot be verified Payhip returns an empty data array instead of an error. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Payment Received | `paid` | Fires whenever a customer is charged for a purchase in your Payhip store. Payhip has no webhook registration API, so the customer registers the fastn trigger URL by hand: open the Payhip dashboard, go to Account &gt; Settings &gt; Developer, paste the fastn trigger URL into the webhook endpoint field (multiple endpoints are comma separated), tick the 'paid' event and save. All money amounts are in the smallest currency unit, so 1000 means 10.00. Payload schema modelled from Payhip's documented sample at https://help.payhip.com/article/115-webhooks, not from a captured delivery. |
| Payment Refunded | `refunded` | Fires whenever a payment in your Payhip store is refunded, in full or in part. Compare amount_refunded with price to tell the two apart. Payhip has no webhook registration API, so the customer registers the fastn trigger URL by hand: open the Payhip dashboard, go to Account &gt; Settings &gt; Developer, paste the fastn trigger URL into the webhook endpoint field, tick the 'refunded' event and save. Payload schema modelled from Payhip's documented sample at https://help.payhip.com/article/115-webhooks, not from a captured delivery. |
| Subscription Cancelled | `subscription.deleted` | Fires whenever a customer's subscription to one of your Payhip memberships or plans is cancelled. Payhip has no webhook registration API, so the customer registers the fastn trigger URL by hand: open the Payhip dashboard, go to Account &gt; Settings &gt; Developer, paste the fastn trigger URL into the webhook endpoint field, tick the 'subscription.deleted' event and save. Payload schema modelled from Payhip's documented sample at https://help.payhip.com/article/115-webhooks, not from a captured delivery. |
| Subscription Created | `subscription.created` | Fires whenever a customer starts a subscription to one of your Payhip memberships or plans. Payhip has no webhook registration API, so the customer registers the fastn trigger URL by hand: open the Payhip dashboard, go to Account &gt; Settings &gt; Developer, paste the fastn trigger URL into the webhook endpoint field, tick the 'subscription.created' event and save. Payload schema modelled from Payhip's documented sample at https://help.payhip.com/article/115-webhooks, not from a captured delivery. |
