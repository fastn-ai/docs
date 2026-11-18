---
description: "Pushinator push notifications."
hidden: true
---

# Pushinator

<img src="../../.gitbook/assets/connectors/lg/pushinator.png" alt="Pushinator logo">

Pushinator push notifications. Covers the public REST API (api.pushinator.com/api/v2 — send notifications, manage channels, current user) and the full console API (api.pushinator.com/api/console/v2 — channels, subscribers, notification drafts/history/deliveries, API tokens, inbound channel webhooks, domain-uptime alerts, Polymarket price alerts, plans and account).

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [pushinator.com](https://pushinator.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `pushinator` |

## Use it

Add Pushinator from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pushinator.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Change Console Password (Console API) | `consoleAuthUpdatePassword` | Console API: changes the console password of the signed-in account. The stored credentials for this connection will no longer match afterwards. PUT /api/console/v2/auth/password. |
| Console Sign In (Console API) | `consoleAuthLogin` | Console API: exchanges a Pushinator console email and password for the session token used by every other Console API action. Unauthenticated. Run this to obtain the consoleToken credential for this connection. POST /api/console/v2/auth/login. |
| Console Sign Out (Console API) | `consoleAuthLogout` | Console API: revokes the console session token presented in the request. Calling this invalidates the consoleToken this connection stores, so every other Console API action will start returning 401 until a new token is issued. POST /api/console/v2/auth/logout. |
| Create API Token (Console API) | `consoleCreateApiToken` | Console API: issues a new Pushinator API token. The response carries plain_text_token, the only time the secret is ever shown - treat the response as a credential. Takes no body. POST /api/console/v2/tokens. |
| Create Channel (Console API) | `consoleCreateChannel` | Console API: creates a notification channel. POST /api/console/v2/channels. |
| Create Channel (Public API) | `apiCreateChannel` | Public API: creates a new notification channel and returns it with its generated UUID. POST /api/v2/channels. |
| Create Channel Inbound Webhook (Console API) | `consoleCreateChannelWebhook` | Console API: creates an inbound webhook endpoint on a channel so an external system can raise notifications by POSTing to it. Requires a Pushinator API token to bind the endpoint to. POST /api/console/v2/channels/{channelId}/webhooks. |
| Create Notification Draft (Console API) | `consoleCreateNotification` | Console API: creates a notification in status "created" WITHOUT dispatching it. Dispatch it afterwards with Dispatch Notification (Console API). POST /api/console/v2/notifications. |
| Create Polymarket Condition (Console API) | `consoleCreatePolymarketCondition` | Console API: adds a Polymarket price-alert condition to a channel. condition_type is price_threshold, price_change or resolution. POST /api/console/v2/channels/{channelId}/polymarket-alerts/conditions. |
| Delete Channel (Console API) | `consoleDeleteChannel` | Console API: permanently deletes a channel with its subscribers and notification history. DELETE /api/console/v2/channels/{channelId}. |
| Delete Channel (Public API) | `apiDeleteChannel` | Public API: permanently deletes a channel, its subscribers and its notification history. DELETE /api/v2/channels/{channelId} (undocumented but live). |
| Delete Channel Inbound Webhook (Console API) | `consoleDeleteChannelWebhook` | Console API: removes a channel inbound webhook endpoint. DELETE /api/console/v2/channels/{channelId}/webhooks/{webhookId}. |
| Delete Console Account (Console API) | `consoleDeleteAccount` | Console API: permanently deletes the signed-in Pushinator account with all its channels, subscribers, tokens and history. Irreversible and removes the identity this connection authenticates as. DELETE /api/console/v2/user. |
| Delete Notification (Console API) | `consoleDeleteNotification` | Console API: removes a notification and its history row. DELETE /api/console/v2/notifications/{notificationId}. |
| Delete Polymarket Condition (Console API) | `consoleDeletePolymarketCondition` | Console API: removes a Polymarket alert condition from a channel. DELETE /api/console/v2/channels/{channelId}/polymarket-alerts/conditions/{conditionId}. |
| Dispatch Notification (Console API) | `consoleDispatchNotification` | Console API: dispatches an already-created notification draft to every device subscribed to its channel. This reaches real devices. POST /api/console/v2/notifications/{notificationId}/send. |
| Get Account (Console API) | `consoleGetAccount` | Console API: the signed-in account profile plus its plan, plan renewal/expiry dates, monthly notification usage and subscription status. GET /api/console/v2/user. |
| Get Account Metrics (Console API) | `consoleGetAccountMetrics` | Console API: account totals - number of channels, subscribers, notifications and deliveries. GET /api/console/v2/user/metrics. |
| Get Billing Portal Link (Console API) | `consoleGetCustomerPortal` | Console API: mints a Paddle customer-portal URL for managing the subscription and invoices. Requires an existing paid subscription. POST /api/console/v2/customer_portal. |
| Get Channel (Console API) | `consoleGetChannel` | Console API: one channel by UUID, including subscribers_count. GET /api/console/v2/channels/{channelId}. |
| Get Channel (Public API) | `apiGetChannel` | Public API: fetches one channel by UUID. GET /api/v2/channels/{channelId} (undocumented but live). |
| Get Channel QR Code (Console API) | `consoleGetChannelQrCode` | Console API: returns the subscribe QR code for a channel, which the Pushinator mobile app scans to become a subscriber. GET /api/console/v2/channels/{channelId}/qr?size=&format= (format svg or png). |
| Get Current User (Public API) | `apiGetCurrentUser` | Public API: returns the id and name of the Pushinator account that owns the API token. GET /api/v2/user. |
| Get Domain Alerts Status (Console API) | `consoleGetDomainAlertsStatus` | Console API: whether the domain-uptime alert feature is linked on a channel, the last four characters of the linked Pushinator token and the acknowledgment flag. GET /api/console/v2/channels/{channelId}/domain-alerts/status. |
| Get Domain Alerts Usage (Console API) | `consoleGetDomainAlertsUsage` | Console API: how many domain-alert watches the channel is using against its plan allowance. GET /api/console/v2/channels/{channelId}/domain-alerts/usage. |
| Get Notification (Console API) | `consoleGetNotification` | Console API: a single notification by UUID with its delivery status. GET /api/console/v2/notifications/{notificationId}. |
| Get Polymarket Alerts Status (Console API) | `consoleGetPolymarketStatus` | Console API: whether the Polymarket price-alert feature is linked on a channel, plus the last four characters of the linked Pushinator token. GET /api/console/v2/channels/{channelId}/polymarket-alerts/status. |
| Link Domain Alerts Token (Console API) | `consoleLinkDomainAlertsToken` | Console API: links a Pushinator API token to a channel so the domain-uptime alert engine can push to it. Required before any domain watch will fire. PUT /api/console/v2/channels/{channelId}/domain-alerts/token. |
| Link Polymarket Alerts Token (Console API) | `consoleLinkPolymarketToken` | Console API: links a Pushinator API token to a channel so the Polymarket price-alert engine can push to it. PUT /api/console/v2/channels/{channelId}/polymarket-alerts/token. |
| List API Tokens (Console API) | `consoleListApiTokens` | Console API: lists the account's API tokens as id, name, last_used_at and timestamps. The secret value is never returned. GET /api/console/v2/tokens. |
| List Channel Inbound Webhooks (Console API) | `consoleListChannelWebhooks` | Console API: lists the inbound webhook endpoints attached to a channel. These are URLs an external system POSTs to in order to raise a push notification - Pushinator receives them, it does not call out. GET /api/console/v2/channels/{channelId}/webhooks. |
| List Channels (Console API) | `consoleListChannels` | Console API: lists channels including the live subscribers_count per channel, which the public API does not return. GET /api/console/v2/channels. |
| List Channels (Public API) | `apiListChannels` | Public API: lists every channel on the account with id, name, description and acknowledgment_enabled. GET /api/v2/channels (undocumented but live). |
| List Notification Deliveries (Console API) | `consoleListNotificationDeliveries` | Console API: per-subscriber delivery rows for one notification - which devices received or acknowledged it. GET /api/console/v2/notification_subscribers/{notificationId}. |
| List Notifications For Channel (Console API) | `consoleListNotifications` | Console API: notification history for a channel - content, status, created_via, dispatched_at and sent_at. GET /api/console/v2/notifications?channel_id=... |
| List Polymarket Conditions (Console API) | `consoleListPolymarketConditions` | Console API: the Polymarket price-alert conditions configured on a channel. GET /api/console/v2/channels/{channelId}/polymarket-alerts/conditions. |
| List Public Plans (Console API) | `consoleListPlans` | Console API: the Free, Pro and Scale plans with their prices, subscriber limits and monthly notification limits. GET /api/console/v2/public/plans. |
| List Subscribers (Console API) | `consoleListSubscribers` | Console API: lists the devices subscribed to a channel. Read this before sending - it is how you tell whether a send will reach real devices. GET /api/console/v2/subscribers?channel_id=... |
| List Watched Domains (Console API) | `consoleListDomainAlerts` | Console API: the domains this channel watches, each with its enabled alert types and their status. GET /api/console/v2/channels/{channelId}/domain-alerts/domains. |
| Ping Subscriber (Console API) | `consolePingSubscriber` | Console API: sends a test push to a single subscribed device to verify it can receive notifications. This reaches a real device. POST /api/console/v2/subscribers/ping. |
| Regenerate Channel Inbound Webhook (Console API) | `consoleRegenerateChannelWebhook` | Console API: rotates a channel inbound webhook, invalidating the old endpoint identifier. POST /api/console/v2/channels/{channelId}/webhooks/{webhookId}/regenerate. |
| Register Console Account (Console API) | `consoleAuthRegister` | Console API: creates a brand new Pushinator account and returns its session token. Unauthenticated. POST /api/console/v2/auth/register. |
| Remove Subscriber From Channel (Console API) | `consoleDeleteSubscriber` | Console API: unsubscribes one device from a channel. DELETE /api/console/v2/subscribers?channel_id=... with {subscriber_id} in the body. |
| Rename API Token (Console API) | `consoleUpdateApiToken` | Console API: changes the display name of an API token. PUT /api/console/v2/tokens/{tokenId}. |
| Rename Channel Inbound Webhook (Console API) | `consoleRenameChannelWebhook` | Console API: changes the display name of a channel inbound webhook. PUT /api/console/v2/channels/{channelId}/webhooks/{webhookId}. |
| Revoke API Token (Console API) | `consoleRevokeApiToken` | Console API: permanently revokes an API token. Revoking the token this connection authenticates with will break the connection. DELETE /api/console/v2/tokens/{tokenId}. |
| Search Polymarket Markets (Console API) | `consoleSearchPolymarketMarkets` | Console API: free-text search over Polymarket prediction markets, returning the condition ids, slugs, outcomes and token ids needed to build a price-alert condition. POST /api/console/v2/polymarket-alerts/markets/search. |
| Send Feedback To Pushinator (Console API) | `consoleSendFeedback` | Console API: sends a free-text message to the Pushinator team. This is read by real people at the vendor - do not call it for testing. POST /api/console/v2/feedback. |
| Send Notification (Public API) | `apiSendNotification` | Public API: creates and immediately dispatches a push notification to every device subscribed to a channel. POST /api/v2/notifications/send. acknowledgment_required is a paid-plan feature. |
| Set Channel Inbound Webhook Acknowledgment (Console API) | `consoleSetChannelWebhookAcknowledgment` | Console API: turns the acknowledgment-required retry behaviour on or off for notifications raised through a channel inbound webhook. PUT /api/console/v2/channels/{channelId}/webhooks/{webhookId}/acknowledgment. |
| Set Channel Inbound Webhook Secret (Console API) | `consoleSetChannelWebhookSecret` | Console API: sets the shared secret an external system must present when calling a channel inbound webhook. POST /api/console/v2/channels/{channelId}/webhooks/{webhookId}/secret. |
| Set Polymarket Condition Status (Console API) | `consoleSetPolymarketConditionStatus` | Console API: pauses or resumes a Polymarket alert condition. PUT /api/console/v2/channels/{channelId}/polymarket-alerts/conditions/{conditionId}/status. |
| Unlink Domain Alerts Token (Console API) | `consoleUnlinkDomainAlertsToken` | Console API: removes the Pushinator token from a channel's domain-alert configuration, pausing every domain watch on it. DELETE /api/console/v2/channels/{channelId}/domain-alerts/token. |
| Unlink Polymarket Alerts Token (Console API) | `consoleUnlinkPolymarketToken` | Console API: removes the Pushinator token from a channel's Polymarket alert configuration, pausing its conditions. DELETE /api/console/v2/channels/{channelId}/polymarket-alerts/token. |
| Unwatch Domain (Console API) | `consoleDeleteDomainAlert` | Console API: stops watching a domain on this channel. The path segment is the domain name, url-encoded. DELETE /api/console/v2/channels/{channelId}/domain-alerts/domains/{domain}. |
| Update Account Profile (Console API) | `consoleUpdateAccount` | Console API: changes the display name and email address of the signed-in account. Changing the email changes the console sign-in identity. PUT /api/console/v2/user. |
| Update Channel (Console API) | `consoleUpdateChannel` | Console API: renames a channel or changes its description. PUT /api/console/v2/channels/{channelId}. |
| Update Channel (Public API) | `apiUpdateChannel` | Public API: renames a channel or changes its description. PUT /api/v2/channels/{channelId}. The name field is required by the vendor. |
| Update Notification Draft (Console API) | `consoleUpdateNotification` | Console API: edits the content or acknowledgment flag of a notification that has not been dispatched yet. PUT /api/console/v2/notifications/{notificationId}. |
| Update Polymarket Condition (Console API) | `consoleUpdatePolymarketCondition` | Console API: edits the label, direction, threshold price or change percentage of a Polymarket alert condition. PUT /api/console/v2/channels/{channelId}/polymarket-alerts/conditions/{conditionId}. |
| Update Watched Domain (Console API) | `consoleUpdateDomainAlert` | Console API: changes the label, target domain or enabled alert types of a watched domain. The path segment is the CURRENT domain name, url-encoded. PUT /api/console/v2/channels/{channelId}/domain-alerts/domains/{domain}. |
| Upgrade Plan (Console API) | `consoleUpgradePlan` | Console API: starts a paid plan change for the account. This spends real money - it is the checkout step for the Pro and Scale plans. POST /api/console/v2/upgrade. |
| Watch Domain (Console API) | `consoleCreateDomainAlert` | Console API: starts watching a domain on this channel. alerts is a map keyed by alert type - expiry_threshold {enabled, threshold_days}, registrar_change {enabled}, ns_change {enabled}, available_now {enabled}. At least one must be enabled. POST /api/console/v2/channels/{channelId}/domain-alerts/domains. |
