---
description: "Dub is the modern link attribution platform for short links, conversion tracking, and affiliate (partner) programs."
hidden: true
---

# Dub

<img src="../../.gitbook/assets/connectors/dub.png" alt="Dub logo" width="64">

Dub is the modern link attribution platform for short links, conversion tracking, and affiliate (partner) programs. This connector covers the complete Dub REST API (https://api.dub.co): links (create, retrieve, list, count, update, upsert, delete, bulk create/update/delete), analytics and events, tags, folders, domains (create, list, update, delete, register, availability check), conversion tracking (lead, sale, open), customers, partners and partner applications, partner links and analytics, discount codes, commissions, payouts, bounties, referral embed tokens, QR codes, workspace info, and webhook management (list, create, get, update, delete). Authentication is a workspace API key sent as a Bearer token. Partner-program, customer, discount-code, webhook and analytics endpoints require a paid Dub plan.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [dub.co](https://dub.co) |
| **Authentication** | Credentials you enter |
| **Slug** | `dub` |

## Use it

Add Dub from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dub.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Approve a bounty submission | `approveBountySubmission` | Approve a bounty submission, optionally with a custom reward amount. Approving creates partner earnings. Requires a Dub plan with partner programs. |
| Approve a partner application | `approvePartnerApplication` | Approve a pending partner application. The partner is enrolled in the specified group and notified by email. Requires a Dub plan with partner programs. |
| Ban a partner | `banPartner` | Ban a partner from your program. This disables all their links and marks all their commissions as canceled. Identify the partner with partnerId (takes precedence) or tenantId. Requires a Dub plan with partner programs. |
| Bulk create links | `bulkCreateLinks` | Bulk create up to 100 links for the authenticated workspace. The request body is a top-level JSON array, so the links are passed as a pre-stringified JSON array. Note: bulk endpoints do not trigger webhook events. |
| Bulk delete links | `bulkDeleteLinks` | Bulk delete up to 100 links for the authenticated workspace. Note: bulk endpoints do not trigger webhook events. |
| Bulk update commissions | `bulkUpdateCommissions` | Bulk update up to 100 commissions to the same status. Requires a Dub plan with partner programs. |
| Bulk update links | `bulkUpdateLinks` | Bulk update up to 100 links with the same data for the authenticated workspace. Identify the links with linkIds (takes precedence) or externalIds, and pass the shared changes in data. Note: bulk endpoints do not trigger webhook events. |
| Check domain availability | `checkDomainStatus` | Check if one or more .link domain names are available for purchase. |
| Create a commission | `createCommission` | Create a custom, lead or sale commission for a partner. Custom commissions accept a negative amount to create a clawback. Creation is asynchronous (202 Accepted) - poll List all commissions or use the commission.created webhook to see the result. Requires a Dub plan with partner programs. Warning: commissions are real partner earnings. |
| Create a discount code | `createDiscountCode` | Create a discount code for a partner. The partner's group must already have a discount assigned, and the target link must not already have a discount code. Requires a Dub plan with partner programs. |

<details>

<summary>See 54 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create a domain | `createDomain` | Create (add) a custom domain for the authenticated workspace. The domain must then be verified via DNS before links on it resolve. |
| Create a folder | `createFolder` | Create a folder for the authenticated workspace. |
| Create a link | `createLink` | Create a link for the authenticated workspace. |
| Create a link for a partner | `createPartnerLink` | Create an additional referral link for a partner enrolled in your program. Identify the partner with partnerId (takes precedence) or tenantId. Requires a Dub plan with partner programs. |
| Create a referrals embed token | `createReferralsEmbedToken` | Create a short-lived token for embedding Dub's referrals dashboard for a partner. The endpoint first looks up an enrollment by tenantId, then resolves the partner by email and creates the enrollment if needed (upsert-style), so it always returns a usable embed token. Requires a Dub plan with partner programs. |
| Create a tag | `createTag` | Create a tag for the authenticated workspace. |
| Create a webhook | `createWebhook` | Create a webhook subscription for the workspace. Dub POSTs each subscribed event to the URL with a Dub-Signature header (hex HMAC-SHA256 of the raw body using the returned secret). Requires a Dub Business plan or above and an API key with the webhooks.write permission. |
| Create or update a partner | `createPartner` | Create or update (upsert) a partner record in your partner program. If a partner with the same email already exists, their program enrollment is updated with the provided tenantId; otherwise a new partner is created and enrolled. Requires a Dub plan with partner programs. Note: enrolling a partner sends them an email. |
| Deactivate a partner | `deactivatePartner` | Deactivate a partner from your program and disable all their active links. Their commissions and payouts remain intact and they can be reactivated later. Identify the partner with partnerId (takes precedence) or tenantId. Requires a Dub plan with partner programs. |
| Delete a customer | `deleteCustomer` | Delete a customer from the workspace. Requires a paid Dub plan. |
| Delete a discount code | `deleteDiscountCode` | Delete a partner discount code by its unique ID or alphanumeric code. This also disables the code in your connected discount provider (Stripe, Shopify, or custom via the discount_code.deleted webhook). Requires a Dub plan with partner programs. |
| Delete a domain | `deleteDomain` | Delete a domain from a workspace. It cannot be undone. This will also delete all the links associated with the domain. |
| Delete a folder | `deleteFolder` | Delete a folder from the workspace. All existing links will still work, but they will no longer be associated with this folder. |
| Delete a link | `deleteLink` | Delete a link for the authenticated workspace. |
| Delete a tag | `deleteTag` | Delete a tag from the workspace. All existing links will still work, but they will no longer be associated with this tag. |
| Delete a webhook | `deleteWebhook` | Delete a webhook by ID. Requires a Dub Business plan or above and an API key with the webhooks.write permission. |
| List all commissions | `listCommissions` | Retrieve a paginated list of commissions for your partner program. Requires a Dub plan with partner programs. |
| List all customers | `getCustomers` | Retrieve a paginated list of customers for the authenticated workspace. Requires a paid Dub plan. |
| List all domains | `listDomains` | Retrieve a paginated list of domains for the authenticated workspace. |
| List all events | `listEvents` | Retrieve a paginated list of raw click, lead or sale events for the authenticated workspace. Accepts the same filters as Retrieve analytics plus pagination and sorting. Note: the events endpoint has per-second rate limits and is not available on the Dub Free plan. |
| List all folders | `listFolders` | Retrieve a paginated list of folders for the authenticated workspace. |
| List all links | `getLinks` | Retrieve a paginated list of links for the authenticated workspace. |
| List all partners | `listPartners` | List all partners enrolled in your partner program. Requires a Dub plan with partner programs. |
| List all payouts | `listPayouts` | Retrieve a paginated list of payouts for your partner program. Read-only; payouts are created and confirmed inside Dub. Requires a Dub plan with partner programs. |
| List all tags | `getTags` | Retrieve a paginated list of tags for the authenticated workspace. |
| List bounty submissions | `listBountySubmissions` | List all submissions for a specific bounty in your partner program. Requires a Dub plan with partner programs. |
| List discount codes | `listDiscountCodes` | Retrieve a paginated list of discount codes for a partner, for a given discount, or for the whole program. Requires a Dub plan with partner programs. |
| List pending partner applications | `listPartnerApplications` | Retrieve a paginated list of pending applications to your partner program. Requires a Dub plan with partner programs. |
| List webhooks | `listWebhooks` | List all webhooks configured for the workspace. Requires a Dub Business plan or above and an API key with the webhooks.read permission. |
| Register a domain | `registerDomain` | Register (purchase) a .link domain for the authenticated workspace. Only available for Enterprise plans. Warning: this provisions a real domain registration. |
| Reject a bounty submission | `rejectBountySubmission` | Reject a bounty submission with a reason and optional note. Requires a Dub plan with partner programs. |
| Reject a partner application | `rejectPartnerApplication` | Reject a pending partner application. The partner is notified by email that their application was not approved. Requires a Dub plan with partner programs. |
| Retrieve a customer | `getCustomer` | Retrieve a customer by ID for the authenticated workspace. To retrieve by external ID, prefix the ID with ext_. Requires a paid Dub plan. |
| Retrieve a link | `getLinkInfo` | Retrieve the info for a link. Identify it by linkId, by externalId, or by domain + key. |
| Retrieve a partner's links | `retrievePartnerLinks` | Retrieve a partner's referral links by their partner ID or tenant ID. Requires a Dub plan with partner programs. |
| Retrieve a QR code | `getQRCode` | Generate a QR code image (PNG) for a URL. The engine returns it as an inline file object with base64 data (name, mime, size, data). |
| Retrieve a webhook | `getWebhook` | Retrieve a webhook by ID. Requires a Dub Business plan or above and an API key with the webhooks.read permission. |
| Retrieve a workspace | `getWorkspace` | Retrieve the workspace the API key belongs to, by workspace ID (ws_...) or slug. Returns plan, usage, limits, domains and users. Requires the workspaces.read permission. |
| Retrieve analytics | `retrieveAnalytics` | Retrieve analytics for a link, a domain, or the authenticated workspace. The response shape depends on event and groupBy: groupBy=count returns a single totals object, every other groupBy returns an array of rows keyed by that dimension (start, country, device, referer, ...). Most string filters support advanced filtering: one value, several comma-separated values, or exclusion by prefixing with '!'. Note: the analytics endpoints have per-second rate limits and are not available on the Dub Free plan. |
| Retrieve analytics for a partner | `retrievePartnerAnalytics` | Retrieve analytics for a partner within a program. The response shape varies with groupBy: count returns totals, timeseries and top_links return arrays. Requires a Dub plan with partner programs. |
| Retrieve links count | `getLinksCount` | Retrieve the number of links for the authenticated workspace. |
| Track a deep link open | `trackOpen` | Track when a user opens your app via a Dub-powered deep link (iOS and Android). |
| Track a lead | `trackLead` | Track a lead conversion event for a short link. Requires conversion tracking to be enabled on the workspace. |
| Track a sale | `trackSale` | Track a sale conversion event for a short link. Requires conversion tracking to be enabled on the workspace. Recording a sale can generate partner commissions, so use it only with real sales data. |
| Update a commission | `updateCommission` | Update an existing commission's amount or status - useful for refunds (partial or full) and fraudulent sales. Paid commissions cannot be updated. Requires a Dub plan with partner programs. |
| Update a customer | `updateCustomer` | Update a customer for the authenticated workspace. Requires a paid Dub plan. |
| Update a domain | `updateDomain` | Update a domain for the authenticated workspace. The path slug identifies the existing domain; pass a new slug in the body to rename it. |
| Update a folder | `updateFolder` | Update a folder in the workspace. |
| Update a link | `updateLink` | Update a link for the authenticated workspace. Only the fields you pass are changed; if there's no change the link is returned as it is. |
| Update a tag | `updateTag` | Update a tag in the workspace. |
| Update a webhook | `updateWebhook` | Update a webhook's name, URL, triggers or link scope. Requires a Dub Business plan or above and an API key with the webhooks.write permission. |
| Update a workspace | `updateWorkspace` | Update the workspace the API key belongs to (name, slug, logo, conversion tracking settings). Requires the workspaces.write permission. |
| Upsert a link | `upsertLink` | Upsert a link for the authenticated workspace by its destination URL. If a link with the same URL already exists it is returned (or updated if there are changes); otherwise a new link is created. |
| Upsert a link for a partner | `upsertPartnerLink` | Upsert a referral link for a partner enrolled in your program. If a link with the same URL already exists it is returned (or updated); otherwise a new link is created. Requires a Dub plan with partner programs. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Bounty created | `bounty.created` | Occurs whenever a bounty is created in your program. Accepted by the API (WEBHOOK_TRIGGERS in dubinc/dub apps/web/lib/webhook/constants.ts) but Dub publishes no payload sample, so no payloadSchema is declared - capture one from a real delivery before relying on its shape. |
| Bounty updated | `bounty.updated` | Occurs whenever a bounty in your program is updated. Accepted by the API (WEBHOOK_TRIGGERS in dubinc/dub apps/web/lib/webhook/constants.ts) but Dub publishes no payload sample, so no payloadSchema is declared - capture one from a real delivery before relying on its shape. |
| Commission created | `commission.created` | Occurs whenever a commission is created for a partner; clawbacks fire this event with a negative amount. Payload schema captured from the documented sample at https://dub.co/docs/webhooks/events/commission-created. |
| Discount code created | `discount_code.created` | Occurs whenever a discount code is created for a partner. Payload schema captured from the documented sample at https://dub.co/docs/webhooks/events/discount-code-created. |
| Discount code deleted | `discount_code.deleted` | Occurs whenever a partner discount code is deleted. Use it to disable the code in your own discount provider. Payload schema captured from the documented sample at https://dub.co/docs/webhooks/events/discount-code-deleted. |
| Lead created | `lead.created` | Occurs whenever a lead conversion event is tracked (POST /track/lead). Requires conversion tracking on the workspace. Payload schema captured from the documented sample at https://dub.co/docs/webhooks/events/lead-created. |
| Link clicked | `link.clicked` | Occurs whenever a link is clicked or its QR code is scanned. This trigger requires a link scope: set the linkScope input to all, links or folders (and linkIds / folderIds accordingly) before subscribing. Payload schema captured from the documented sample at https://dub.co/docs/webhooks/events/link-clicked. |
| Link created | `link.created` | Occurs whenever a link is created (POST /links or PUT /links/upsert). Bulk link endpoints do not fire webhooks. Payload schema modelled from the documented sample at https://dub.co/docs/webhooks/events/link-created. |
| Link deleted | `link.deleted` | Occurs whenever a link is deleted (DELETE /links/{linkId}). Bulk link endpoints do not fire webhooks. Payload is the deleted link object. Modelled from the documented sample at https://dub.co/docs/webhooks/events/link-deleted. |
| Link updated | `link.updated` | Occurs whenever a link is updated (PATCH /links/{linkId}). Bulk link endpoints do not fire webhooks. Payload is the same link object as link.created. Modelled from the documented sample at https://dub.co/docs/webhooks/events/link-updated. |

<details>

<summary>See 5 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Partner application submitted | `partner.application_submitted` | Occurs whenever a partner submits an application to your program. Payload schema captured from the documented sample at https://dub.co/docs/webhooks/events/partner-application-submitted. |
| Partner enrolled | `partner.enrolled` | Occurs whenever a partner is enrolled in your program (application approved, invite accepted, or created via the API). Payload schema captured from the documented sample at https://dub.co/docs/webhooks/events/partner-enrolled. |
| Partner merged | `partner.merged` | Occurs when two partner accounts are merged. Payload schema captured from the documented sample at https://dub.co/docs/webhooks/events/partner-merged. |
| Payout confirmed | `payout.confirmed` | Occurs whenever a payout in your program is confirmed. Accepted by the API (WEBHOOK_TRIGGERS in dubinc/dub apps/web/lib/webhook/constants.ts) but Dub publishes no payload sample, so no payloadSchema is declared - capture one from a real delivery before relying on its shape. |
| Sale created | `sale.created` | Occurs whenever a sale conversion event is tracked (POST /track/sale). Requires conversion tracking on the workspace. Payload schema captured from the documented sample at https://dub.co/docs/webhooks/events/sale-created. |

</details>
