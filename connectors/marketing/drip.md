---
description: "Drip is an ecommerce marketing automation platform (email, SMS, subscribers, campaigns, workflows, broadcasts, and shopper activity)."
---

# Drip

Drip is an ecommerce marketing automation platform (email, SMS, subscribers, campaigns, workflows, broadcasts, and shopper activity). This connector covers the Drip REST API v2/v3.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [getdrip.com](https://getdrip.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Actions** | 59 |
| **Events** | 0 |
| **Slug** | `drip` |

## Use it

Add Drip from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.drip.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Campaign | `activateCampaign` | Activates a paused email series campaign so it resumes sending. |
| Activate Workflow | `activateWorkflow` | Activates a paused or draft workflow so it starts running. |
| Apply Tag to Subscriber | `applyTagToSubscriber` | Applies a tag to a subscriber identified by email. |
| Batch Cart Activity | `batchCartActivity` | Records up to 1000 cart shopper-activity events in one batch (Shopper Activity API v3). |
| Batch Create or Update Orders (Legacy) | `batchOrders` | Creates or updates up to 1000 orders in one batch via the legacy Orders API. |
| Batch Create or Update Subscribers | `batchUpsertSubscribers` | Creates or updates up to 1000 subscribers in a single batch request. |
| Batch Order Activity | `batchOrderActivity` | Records up to 1000 order shopper-activity events in one batch (Shopper Activity API v3). |
| Batch Product Activity | `batchProductActivity` | Records up to 1000 product shopper-activity events in one batch (Shopper Activity API v3). |
| Batch Record Events | `batchRecordEvents` | Records up to 1000 custom events in a single batch request. |
| Batch Unsubscribe Subscribers | `batchUnsubscribe` | Unsubscribes up to 1000 subscribers from all mailings in a single batch request. |
| Create Broadcast | `createBroadcast` | Creates a draft single-email campaign (broadcast). Content is an object with an 'html' key (and optional 'text'). |
| Create or Update Cart Activity | `createCartActivity` | Records a cart shopper-activity event (Shopper Activity API v3). Action is one of created, updated, deleted. |
| Create or Update Order (Legacy) | `createOrder` | Creates or updates an order via the legacy Orders API. Prefer Order Activity (Shopper Activity v3) for new integrations. |
| Create or Update Order Activity | `createOrderActivity` | Records an order shopper-activity event (Shopper Activity API v3). Action is one of placed, updated, paid, fulfilled, refunded, canceled. |
| Create or Update Product Activity | `createProductActivity` | Records a product shopper-activity event (Shopper Activity API v3). Action is one of created, updated, deleted. |
| Create or Update Refund (Legacy) | `createRefund` | Records a refund against an order via the legacy Refunds API. |
| Create or Update Subscriber | `upsertSubscriber` | Creates a new subscriber or updates an existing one (matched by email). Supports name, phone, tags and custom fields. Drip also accepts address, consent, timezone and lead-score fields on the subscriber record via the raw API. |
| Create Webhook | `createWebhook` | Creates a webhook subscription. Events is a list of Drip event type strings such as 'subscriber.created', 'subscriber.applied_tag', 'subscriber.opened_email'. |
| Create Workflow Trigger | `createWorkflowTrigger` | Creates one or more triggers on a workflow. Each trigger object follows the Drip trigger schema. |
| Delete Broadcast | `deleteBroadcast` | Deletes a broadcast (single-email campaign) by ID. |
| Delete Subscriber | `deleteSubscriber` | Permanently deletes a subscriber from the account by ID or email. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook subscription by its ID. |
| Get Account | `getAccount` | Fetches a single Drip account by its account ID. |
| Get Authenticated User | `getUser` | Fetches the currently authenticated Drip user, including the list of accounts they belong to. |
| Get Broadcast | `getBroadcast` | Fetches a single broadcast (single-email campaign) by its ID. |
| Get Campaign | `getCampaign` | Fetches a single email series campaign by its ID. |
| Get Conversion | `getConversion` | Fetches a single conversion (goal) by its ID. |
| Get Email Metrics | `getEmailMetrics` | Retrieves aggregate email performance metrics such as sends, opens, clicks, and revenue for a date range, optionally limited to one Single-Email Campaign or one workflow. |
| Get Form | `getForm` | Fetches a single form by its ID. |
| Get Subscriber | `getSubscriber` | Fetches a single subscriber by their Drip subscriber ID or email address. |
| Get Webhook | `getWebhook` | Fetches a single webhook subscription by its ID. |
| Get Workflow | `getWorkflow` | Fetches a single workflow by its ID. |
| Get Workflow Details | `getWorkflowDetails` | Retrieves the full read-only structure of a workflow, including its entry triggers, ordered steps, and nested decisions, goals, forks, and split tests. |
| List Accounts | `listAccounts` | Lists all Drip accounts the authenticated user has access to. |
| List Broadcasts | `listBroadcasts` | Lists single-email campaigns (broadcasts), optionally filtered by status. |
| List Campaign Subscribers | `listCampaignSubscribers` | Lists the subscribers of a specific email series campaign. |
| List Campaigns | `listCampaigns` | Lists email series campaigns, optionally filtered by status. |
| List Conversions | `listConversions` | Lists conversions (goals) configured in the account. |
| List Custom Field Identifiers | `listCustomFieldIdentifiers` | Lists all custom field identifiers (keys) that have been used on subscribers in the account. |
| List Event Actions | `listEventActions` | Lists the custom event action names that have been recorded in the account. |
| List Forms | `listForms` | Lists all forms in the account. |
| List Subscriber Campaign Subscriptions | `listSubscriberCampaignSubscriptions` | Lists the email series campaigns a subscriber is subscribed to. |
| List Subscribers | `listSubscribers` | Lists subscribers in the account with optional filtering by status, tags, IDs and subscription date range. |
| List Tags | `listTags` | Lists all tags defined in the account. |
| List Webhooks | `listWebhooks` | Lists all webhook subscriptions configured on the account. |
| List Workflow Triggers | `listWorkflowTriggers` | Lists the triggers configured on a workflow. |
| List Workflows | `listWorkflows` | Lists all workflows in the account. |
| Pause Campaign | `pauseCampaign` | Pauses an active email series campaign. |
| Pause Workflow | `pauseWorkflow` | Pauses an active workflow. |
| Record Event | `recordEvent` | Records a custom event for a subscriber identified by email. Properties is a free-form object; occurred_at defaults to now. |
| Remove Subscriber From Campaign | `removeSubscriberFromCampaign` | Removes a subscriber from one Email Series Campaign, or from all Email Series Campaigns when no campaign ID is given. |
| Remove Subscriber From Workflow | `removeSubscriberFromWorkflow` | Removes a subscriber from a workflow by workflow ID and subscriber ID or email. |
| Remove Tag From Subscriber | `removeTagFromSubscriber` | Removes a tag from a subscriber identified by ID or email. |
| Send Broadcast Test Email | `sendBroadcastTest` | Sends a test of a broadcast to 1-5 verified email addresses. |
| Start Subscriber on Workflow | `startSubscriberOnWorkflow` | Starts a subscriber on a workflow, creating or updating the subscriber. |
| Subscribe to Campaign | `subscribeToCampaign` | Subscribes a person to an email series campaign, creating or updating the subscriber. |
| Unsubscribe Subscriber From All Mailings | `unsubscribeSubscriberFromAll` | Unsubscribes a subscriber from all mailings (email marketing and campaigns) by ID or email. |
| Update Broadcast | `updateBroadcast` | Updates a draft broadcast (single-email campaign). Only draft broadcasts can be updated. |
| Update Workflow Trigger | `updateWorkflowTrigger` | Updates an existing trigger on a workflow. |
