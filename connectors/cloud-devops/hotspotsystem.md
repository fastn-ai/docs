---
description: "HotspotSystem cloud WiFi hotspot management."
---

# HotspotSystem

HotspotSystem cloud WiFi hotspot management. Read-only access to the HotspotSystem API v2.0: hotspot locations, registered customers, newsletter subscribers, prepaid vouchers, and paid / voucher / MAC / social-login connection transactions, globally or per location.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [hotspotsystem.com](https://hotspotsystem.com) |
| **Authentication** | API key |
| **Actions** | 18 |
| **Events** | 6 |
| **Slug** | `hotspotsystem` |

## Use it

Add HotspotSystem from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hotspotsystem.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Current Operator | `getMe` | Return the HotspotSystem account that owns the API key in use: the numeric user id and the operator username. Useful for confirming which operator a connection is bound to. |
| List Customers | `getCustomers` | List every WiFi customer registered across all of the operator's hotspot locations, including contact details and, for social logins, the linked social profile. Supports field selection, sorting and pagination. Returns end-user personal data. |
| List Customers By Location | `getCustomersByLocationId` | List the WiFi customers registered at one specific hotspot location. Pass the location id from List Locations, or '0' for every location. Returns end-user personal data. |
| List Locations | `getLocations` | List every hotspot location owned by the authenticated HotspotSystem operator, with the total count in metadata. Supports field selection, sorting and pagination. |
| List Locations As Options | `getLocationsAsOptions` | List the operator's hotspot locations in a compact id/name form suitable for populating a dropdown. Always includes the synthetic option with id '0' named 'All', which selects every location. Takes no parameters. |
| List MAC Authentication Transactions | `getMacTransactions` | List free or MAC-address authenticated WiFi connection records across all of the operator's hotspot locations, including the access package used and any custom splash-page survey answers (q1/a1 through q5/a5). |
| List MAC Authentication Transactions By Location | `getMacTransactionsByLocationId` | List free or MAC-address authenticated WiFi connection records for one specific hotspot location. Pass the location id from List Locations, or '0' for every location. |
| List Newsletter Subscribers | `getSubscribers` | List every WiFi user across all of the operator's locations who opted in to the newsletter, with their contact details and social profile where available. Supports field selection, sorting and pagination. Returns end-user personal data. |
| List Newsletter Subscribers By Location | `getSubscribersByLocationId` | List the newsletter opt-ins captured at one specific hotspot location. Pass the location id from List Locations, or '0' for every location. Returns end-user personal data. |
| List Paid Transactions | `getPaidTransactions` | List paid WiFi access transactions (credit card and other paid packages) across all of the operator's hotspot locations, with amount, currency and the purchasing customer's details. |
| List Paid Transactions By Location | `getPaidTransactionsByLocationId` | List paid WiFi access transactions recorded at one specific hotspot location. Pass the location id from List Locations, or '0' for every location. |
| List Social Login Transactions | `getSocialTransactions` | List WiFi connections authenticated through a social network login (Facebook, Twitter, Google and similar) across all of the operator's hotspot locations, with the linked social profile data captured at login. |
| List Social Login Transactions By Location | `getSocialTransactionsByLocationId` | List social network WiFi logins recorded at one specific hotspot location. Pass the location id from List Locations, or '0' for every location. |
| List Voucher Transactions | `getVoucherTransactions` | List WiFi access transactions redeemed with a prepaid voucher across all of the operator's hotspot locations, with the voucher value and the redeeming customer's details. |
| List Voucher Transactions By Location | `getVoucherTransactionsByLocationId` | List voucher redemption transactions recorded at one specific hotspot location. Pass the location id from List Locations, or '0' for every location. |
| List Vouchers | `getVouchers` | List the prepaid WiFi vouchers generated across all of the operator's locations, with their code, usage limits, validity and price. Note: the HotspotSystem API returns HTTP 500 "Cannot read property 'currency' of undefined" for accounts that have no voucher currency configured in the Control Center. |
| List Vouchers By Location | `getVouchersByLocationId` | List the prepaid WiFi vouchers generated for one specific hotspot location. Pass the location id from List Locations, or '0' for every location. Note: the HotspotSystem API returns HTTP 500 "Cannot read property 'currency' of undefined" for accounts that have no voucher currency configured in the Control Center. |
| Ping API | `getPing` | Health check for the HotspotSystem API v2.0. Returns {"ping":"pong"} when the service is reachable and the supplied API key is accepted. Use it to validate a connection before running other actions. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Customer Created | `customer.create` | Fires when a new WiFi customer registers on a splash page. SETUP (manual, HotspotSystem has no webhook registration API): log in to the HotspotSystem Control Center, go to Tools & Settings &gt; Webhooks (https://www.hotspotsystem.com/controlcenter/webhooks.php), add a webhook, select the Location, select Event type 'customer.create', paste this trigger's fastn callback URL, save, and record the API key HotspotSystem shows you - it is the HMAC secret and is displayed only once. Payload schema is MODELLED from the documented Customer entity; no live delivery was captured. |
| MAC Transaction Created | `transaction.mac.create` | Fires when a device gets free or MAC-authenticated WiFi access. SETUP (manual, HotspotSystem has no webhook registration API): HotspotSystem Control Center &gt; Tools & Settings &gt; Webhooks (https://www.hotspotsystem.com/controlcenter/webhooks.php) &gt; add webhook &gt; select Location &gt; Event type 'transaction.mac.create' &gt; paste this trigger's fastn callback URL &gt; save &gt; record the API key shown once, it is the HMAC secret. Payload schema is MODELLED from the documented MacTransaction entity; no live delivery was captured. |
| Newsletter Subscriber Created | `subscriber.create` | Fires when a WiFi user opts in to the newsletter. SETUP (manual, HotspotSystem has no webhook registration API): HotspotSystem Control Center &gt; Tools & Settings &gt; Webhooks (https://www.hotspotsystem.com/controlcenter/webhooks.php) &gt; add webhook &gt; select Location &gt; Event type 'subscriber.create' &gt; paste this trigger's fastn callback URL &gt; save &gt; record the API key shown once, it is the HMAC secret. Payload schema is MODELLED from the documented Subscriber entity; no live delivery was captured. |
| Paid Transaction Created | `transaction.paid.create` | Fires when a WiFi user buys a paid access package. SETUP (manual, HotspotSystem has no webhook registration API): HotspotSystem Control Center &gt; Tools & Settings &gt; Webhooks (https://www.hotspotsystem.com/controlcenter/webhooks.php) &gt; add webhook &gt; select Location &gt; Event type 'transaction.paid.create' &gt; paste this trigger's fastn callback URL &gt; save &gt; record the API key shown once, it is the HMAC secret. Payload schema is MODELLED from the documented PaidTransaction entity; no live delivery was captured. |
| Social Login Transaction Created | `transaction.social.create` | Fires when a WiFi user logs in through a social network. SETUP (manual, HotspotSystem has no webhook registration API): HotspotSystem Control Center &gt; Tools & Settings &gt; Webhooks (https://www.hotspotsystem.com/controlcenter/webhooks.php) &gt; add webhook &gt; select Location &gt; Event type 'transaction.social.create' &gt; paste this trigger's fastn callback URL &gt; save &gt; record the API key shown once, it is the HMAC secret. Payload schema is MODELLED from the documented SocialTransaction entity; no live delivery was captured. |
| Voucher Transaction Created | `transaction.voucher.create` | Fires when a WiFi user redeems a prepaid voucher. SETUP (manual, HotspotSystem has no webhook registration API): HotspotSystem Control Center &gt; Tools & Settings &gt; Webhooks (https://www.hotspotsystem.com/controlcenter/webhooks.php) &gt; add webhook &gt; select Location &gt; Event type 'transaction.voucher.create' &gt; paste this trigger's fastn callback URL &gt; save &gt; record the API key shown once, it is the HMAC secret. Payload schema is MODELLED from the documented VoucherTransaction entity; no live delivery was captured. |
