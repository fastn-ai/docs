---
description: "MailerLite (new API) connector: subscribers (CRUD + group assign), groups, campaigns (create/schedule), fields, automations, and webhooks."
hidden: true
---

# MailerLite

MailerLite (new API) connector: subscribers (CRUD + group assign), groups, campaigns (create/schedule), fields, automations, and webhooks. Bearer token auth. Base https://connect.mailerlite.com/api.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [mailerlite.com](https://mailerlite.com) |
| **Authentication** | Bearer token |
| **Actions** | 21 |
| **Events** | 13 |
| **Slug** | `mailerlite` |

## Use it

Add MailerLite from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailerlite.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Assign Subscriber To Group | `assignToGroup` | Assign a subscriber to a group. |
| Create Campaign | `createCampaign` | Create a campaign. |
| Create Group | `createGroup` | Create a group. |
| Create Or Update Subscriber | `createSubscriber` | Create or upsert a subscriber by email. |
| Create Webhook | `createWebhook` | Create a webhook. Set batchable true for campaign.open/click. |
| Delete Campaign | `deleteCampaign` | Delete a campaign by its identifier. Only campaigns that have not been sent can be removed. |
| Delete Group | `deleteGroup` | Delete a subscriber group by its identifier. Subscribers in the group are not deleted, only their membership. |
| Delete Subscriber | `deleteSubscriber` | Delete a subscriber by id. |
| Delete Webhook | `deleteWebhook` | Delete a webhook by id. |
| Get Campaign | `getCampaign` | Get a campaign by id. |
| Get Subscriber | `getSubscriber` | Get a subscriber by id or email. |
| List Automations | `listAutomations` | List automations. |
| List Campaigns | `listCampaigns` | List campaigns. |
| List Fields | `listFields` | List custom fields. |
| List Groups | `listGroups` | List groups. |
| List Segments | `listSegments` | List the segments defined in the account. |
| List Subscribers | `listSubscribers` | List subscribers (cursor pagination). |
| List Webhooks | `listWebhooks` | List webhooks. |
| Schedule Campaign | `scheduleCampaign` | Schedule a campaign for delivery. |
| Unassign Subscriber From Group | `unassignFromGroup` | Remove a subscriber from a group. |
| Update Subscriber | `updateSubscriber` | Update a subscriber by id. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Campaign Clicked | `campaign.click` | Fires when a link in a campaign is clicked. Batchable event. |
| Campaign Opened | `campaign.open` | Fires when a campaign email is opened. Batchable event. |
| Campaign Sent | `campaign.sent` | Fires when a campaign is sent. |
| Subscriber Added To Group | `subscriber.added_to_group` | Fires when a subscriber is added to a group. |
| Subscriber Automation Completed | `subscriber.automation_completed` | Fires when an automation completes for a subscriber. |
| Subscriber Automation Triggered | `subscriber.automation_triggered` | Fires when an automation is triggered for a subscriber. |
| Subscriber Bounced | `subscriber.bounced` | Fires when a subscriber email bounces. |
| Subscriber Created | `subscriber.created` | Fires when a new subscriber is created. |
| Subscriber Deleted | `subscriber.deleted` | Fires when a subscriber is deleted. Batchable event. |
| Subscriber Removed From Group | `subscriber.removed_from_group` | Fires when a subscriber is removed from a group. |
| Subscriber Spam Reported | `subscriber.spam_reported` | Fires when a subscriber reports a campaign as spam. |
| Subscriber Unsubscribed | `subscriber.unsubscribed` | Fires when a subscriber unsubscribes. |
| Subscriber Updated | `subscriber.updated` | Fires when a subscriber is updated. |
