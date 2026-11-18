---
description: "Mailgun transactional email and email automation API."
hidden: true
---

# Mailgun

<img src="../../.gitbook/assets/connectors/lg/mailgun.png" alt="Mailgun logo">

Mailgun transactional email and email automation API. Send email, manage domains, mailing lists, templates, routes, suppressions, events, stats, tags, IPs, and webhooks. HTTP Basic Auth with username 'api' and your Mailgun API key. Base host api.mailgun.net (US) or api.eu.mailgun.net (EU). Most endpoints v3, some v4.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [mailgun.com](https://mailgun.com) |
| **Authentication** | Basic auth |
| **Slug** | `mailgun` |

## Use it

Add Mailgun from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailgun.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Add Members | `bulkAddMembers` | Bulk add members to a mailing list (max 1000). POST /v3/lists/{address}/members.json, form-urlencoded with a JSON members array. |
| Create Bounce | `createBounce` | Add an address to the bounce list. POST /v3/{domain}/bounces, form-urlencoded. |
| Create Complaint | `createComplaint` | Add an address to the complaint list. POST /v3/{domain}/complaints, form-urlencoded. |
| Create Domain | `createDomain` | Create a new sending domain on the account. POST /v4/domains, multipart/form-data. Requires a paid Mailgun account (sandbox-only accounts will receive 400). |
| Create Mailing List | `createMailingList` | Create a mailing list. POST /v3/lists, form-urlencoded. |
| Create Member | `createMember` | Add a member to a mailing list. POST /v3/lists/{address}/members, form-urlencoded. |
| Create Route | `createRoute` | Create a route. POST /v3/routes, form-urlencoded. |
| Create Template | `createTemplate` | Create a template. POST /v3/{domain}/templates, form-urlencoded. |
| Create Template Version | `createTemplateVersion` | Create a new template version. POST /v3/{domain}/templates/{name}/versions, form-urlencoded. |
| Create Unsubscribe | `createUnsubscribe` | Add an address to the unsubscribe list. POST /v3/{domain}/unsubscribes, form-urlencoded. |
| Create Webhook | `createWebhook` | Create/register a webhook for an event type on a domain. POST /v3/domains/{domain}/webhooks, form-urlencoded with id (event type) and url. |
| Create Whitelist | `createWhitelist` | Add an address or domain to the whitelist. POST /v3/{domain}/whitelists, form-urlencoded. |
| Delete Bounce | `deleteBounce` | Remove an address from the bounce list. DELETE /v3/{domain}/bounces/{address}. |
| Delete Complaint | `deleteComplaint` | Remove an address from the complaint list. DELETE /v3/{domain}/complaints/{address}. |
| Delete Domain | `deleteDomain` | Delete a domain. DELETE /v3/domains/{domain}. |
| Delete Domain Envelopes | `deleteScheduledMessage` | Delete all scheduled and undelivered messages from the domain queue. DELETE /v3/{domain}/envelopes. NOTE: must be called on the storage API host matching the mail's generated storage URL (e.g. storage-us-east4.api.mailgun.net). |
| Delete Mailing List | `deleteMailingList` | Delete a mailing list. DELETE /v3/lists/{address}. |
| Delete Member | `deleteMember` | Remove a member from a mailing list. DELETE /v3/lists/{address}/members/{member}. |
| Delete Queued Message | `deleteQueuedMessage` | Cancel a scheduled/queued message by message ID. DELETE /v3/{domain}/messages/{messageId}. Returns 200 with message on success. |
| Delete Route | `deleteRoute` | Delete a route. DELETE /v3/routes/{id}. |
| Delete Tag | `deleteTag` | Delete a tag. DELETE /v3/{domain}/tags/{tag}. |
| Delete Template | `deleteTemplate` | Delete a template. DELETE /v3/{domain}/templates/{name}. |
| Delete Template Version | `deleteTemplateVersion` | Delete a template version. DELETE /v3/{domain}/templates/{name}/versions/{tag}. |
| Delete Unsubscribe | `deleteUnsubscribe` | Remove an address from the unsubscribe list. DELETE /v3/{domain}/unsubscribes/{address}. |
| Delete Webhook | `deleteWebhook` | Delete a webhook for an event type. DELETE /v3/domains/{domain}/webhooks/{webhookName}. |
| Delete Whitelist | `deleteWhitelist` | Remove a whitelist record. DELETE /v3/{domain}/whitelists/{value}. |
| Get Bounce | `getBounce` | Get a single bounce. GET /v3/{domain}/bounces/{address}. |
| Get Complaint | `getComplaint` | Get a single complaint. GET /v3/{domain}/complaints/{address}. |
| Get Connection Settings | `getConnectionSettings` | Get domain connection (TLS) settings. GET /v3/domains/{domain}/connection. |
| Get Domain | `getDomain` | Get a single domain's details. GET /v4/domains/{domain}. |
| Get IP | `getIp` | Get details for a specific IP. GET /v3/ips/{ip}. |
| Get Mailing List | `getMailingList` | Get a single mailing list. GET /v3/lists/{address}. |
| Get Member | `getMember` | Get a single mailing list member. GET /v3/lists/{address}/members/{member}. |
| Get Metrics | `getMetrics` | Query the Mailgun analytics Metrics API. POST /v1/analytics/metrics, JSON body. |
| Get Route | `getRoute` | Get a route by id. GET /v3/routes/{id}. |
| Get Stored Message | `getStoredMessage` | Retrieve a stored/received message by its storage key. GET /v3/domains/{domain}/messages/{storageKey}. |
| Get Tag | `getTag` | Get a single tag. GET /v3/{domain}/tags/{tag}. |
| Get Tag Stats | `getTagStats` | Get stats for a specific tag. GET /v3/{domain}/tags/{tag}/stats. |
| Get Template | `getTemplate` | Get a template. GET /v3/{domain}/templates/{name}. |
| Get Template Version | `getTemplateVersion` | Get a specific template version. GET /v3/{domain}/templates/{name}/versions/{tag}. |
| Get Total Stats | `getTotalStats` | Get aggregated total stats for a domain. GET /v3/{domain}/stats/total. |
| Get Tracking Settings | `getTrackingSettings` | Get open/click/unsubscribe tracking settings for a domain. GET /v3/domains/{domain}/tracking. |
| Get Unsubscribe | `getUnsubscribe` | Get a single unsubscribe. GET /v3/{domain}/unsubscribes/{address}. |
| Get Webhook | `getWebhook` | Get a single webhook by event type. GET /v3/domains/{domain}/webhooks/{webhookName}. |
| Get Whitelist | `getWhitelist` | Get a single whitelist record. GET /v3/{domain}/whitelists/{value}. |
| List Bounces | `listBounces` | List bounce suppressions for a domain. GET /v3/{domain}/bounces. |
| List Complaints | `listComplaints` | List complaint suppressions. GET /v3/{domain}/complaints. |
| List Domains | `listDomains` | List all domains on the account. GET /v4/domains. |
| List Events | `listEvents` | Retrieve a paginated list of message events (logs). GET /v3/{domain}/events. |
| List IP Pools | `listIpPools` | List IP pools on the account. GET /v1/ip_pools. |
| List IPs | `listIps` | List all IPs assigned to the account. GET /v3/ips. |
| List Mailing Lists | `listMailingLists` | List all mailing lists on the account. GET /v3/lists/pages. |
| List Members | `listMembers` | List members of a mailing list. GET /v3/lists/{address}/members/pages. |
| List Routes | `listRoutes` | List routes. GET /v3/routes. |
| List Tags | `listTags` | List tags for a domain. GET /v3/{domain}/tags. |
| List Template Versions | `listTemplateVersions` | List versions of a template. GET /v3/{domain}/templates/{name}/versions. |
| List Templates | `listTemplates` | List templates for a domain. GET /v3/{domain}/templates. |
| List Unsubscribes | `listUnsubscribes` | List unsubscribe suppressions. GET /v3/{domain}/unsubscribes. |
| List Webhooks | `listWebhooks` | List all webhooks configured for a domain. GET /v3/domains/{domain}/webhooks. |
| List Whitelists | `listWhitelists` | List whitelist suppressions. GET /v3/{domain}/whitelists. |
| Send Message | `sendMessage` | Send an email via Mailgun by submitting individual parts (from, to, subject, text/html). POST /v3/{domain}/messages, form-urlencoded. Every optional field given (html, cc, bcc, template, testMode, tag, tracking, deliveryTime) is sent under Mailgun's name (o:testmode, o:tag, o:tracking, o:deliverytime); fields not given are left out. Values are URL-encoded. |
| Send MIME Message | `sendMimeMessage` | Send a pre-built MIME message. POST /v3/{domain}/messages.mime, form-urlencoded with 'to' and 'message' (MIME string). |
| Update Click Tracking | `updateClickTracking` | Update click tracking settings. PUT /v3/domains/{domain}/tracking/click, form-urlencoded. |
| Update Connection Settings | `updateConnectionSettings` | Update domain TLS connection settings. PUT /v3/domains/{domain}/connection, form-urlencoded. |
| Update DKIM Authority | `updateDkimAuthority` | Update DKIM authority for a domain. PUT /v3/domains/{domain}/dkim_authority, form-urlencoded. |
| Update Domain | `updateDomain` | Update domain settings. PUT /v4/domains/{domain}, form-urlencoded. |
| Update Mailing List | `updateMailingList` | Update a mailing list. PUT /v3/lists/{address}, form-urlencoded. |
| Update Member | `updateMember` | Update a mailing list member. PUT /v3/lists/{address}/members/{member}, form-urlencoded. |
| Update Open Tracking | `updateOpenTracking` | Update open tracking settings. PUT /v3/domains/{domain}/tracking/open, form-urlencoded. |
| Update Route | `updateRoute` | Update a route. PUT /v3/routes/{id}, form-urlencoded. |
| Update Tag | `updateTag` | Update the description of a tag. PUT /v3/{domain}/tags/{tag}, JSON body. |
| Update Template | `updateTemplate` | Update template metadata. PUT /v3/{domain}/templates/{name}, form-urlencoded. |
| Update Template Version | `updateTemplateVersion` | Update a template version. PUT /v3/{domain}/templates/{name}/versions/{tag}, form-urlencoded. |
| Update Webhook | `updateWebhook` | Update a webhook's URL for an event type. PUT /v3/domains/{domain}/webhooks/{webhookName}, form-urlencoded. |
| Verify Domain | `verifyDomain` | Trigger domain DNS verification. PUT /v4/domains/{domain}/verify. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Accepted | `accepted` | Mailgun accepted the request to send/forward the message. |
| Clicked | `clicked` | The recipient clicked a link (click tracking must be enabled). |
| Complained | `complained` | The recipient marked the message as spam. |
| Delivered | `delivered` | Mailgun successfully delivered the message to the recipient mail server. |
| Opened | `opened` | The email recipient opened the message (tracking must be enabled). |
| Permanent Failure (Bounced) | `permanent_fail` | The message permanently failed (hard bounce). |
| Temporary Failure | `temporary_fail` | The message temporarily failed (soft bounce); Mailgun will retry. |
| Unsubscribed | `unsubscribed` | The recipient unsubscribed. |
