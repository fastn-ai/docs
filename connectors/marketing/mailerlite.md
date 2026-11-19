---
description: "MailerLite (new API) connector: subscribers (CRUD + group assign), groups, campaigns (create/schedule), fields, automations, and webhooks."
hidden: true
---

# MailerLite

<img src="../../.gitbook/assets/connectors/lg/mailerlite.png" alt="MailerLite logo">

Bearer token auth. Base https://connect.mailerlite.com/api.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [mailerlite.com](https://mailerlite.com) |
| **Authentication** | Bearer token |
| **Slug** | `mailerlite` |

## Use it

Add MailerLite from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailerlite.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Assign Subscriber To Group</td><td><code>assignToGroup</code></td><td>Assign a subscriber to a group.</td></tr><tr><td>Create Campaign</td><td><code>createCampaign</code></td><td>Create a campaign.</td></tr><tr><td>Create Group</td><td><code>createGroup</code></td><td>Create a group.</td></tr><tr><td>Create Or Update Subscriber</td><td><code>createSubscriber</code></td><td>Create or upsert a subscriber by email.</td></tr><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Create a webhook. Set batchable true for campaign.open/click.</td></tr><tr><td>Delete Campaign</td><td><code>deleteCampaign</code></td><td>Delete a campaign by its identifier. Only campaigns that have not been sent can be removed.</td></tr><tr><td>Delete Group</td><td><code>deleteGroup</code></td><td>Delete a subscriber group by its identifier. Subscribers in the group are not deleted, only their membership.</td></tr><tr><td>Delete Subscriber</td><td><code>deleteSubscriber</code></td><td>Delete a subscriber by id.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Delete a webhook by id.</td></tr><tr><td>Get Campaign</td><td><code>getCampaign</code></td><td>Get a campaign by id.</td></tr></tbody></table>

<details>

<summary>View 11 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Subscriber</td><td><code>getSubscriber</code></td><td>Get a subscriber by id or email.</td></tr><tr><td>List Automations</td><td><code>listAutomations</code></td><td>List automations.</td></tr><tr><td>List Campaigns</td><td><code>listCampaigns</code></td><td>List campaigns.</td></tr><tr><td>List Fields</td><td><code>listFields</code></td><td>List custom fields.</td></tr><tr><td>List Groups</td><td><code>listGroups</code></td><td>List groups.</td></tr><tr><td>List Segments</td><td><code>listSegments</code></td><td>List the segments defined in the account.</td></tr><tr><td>List Subscribers</td><td><code>listSubscribers</code></td><td>List subscribers (cursor pagination).</td></tr><tr><td>List Webhooks</td><td><code>listWebhooks</code></td><td>List webhooks.</td></tr><tr><td>Schedule Campaign</td><td><code>scheduleCampaign</code></td><td>Schedule a campaign for delivery.</td></tr><tr><td>Unassign Subscriber From Group</td><td><code>unassignFromGroup</code></td><td>Remove a subscriber from a group.</td></tr><tr><td>Update Subscriber</td><td><code>updateSubscriber</code></td><td>Update a subscriber by id.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Campaign Clicked</td><td><code>campaign.click</code></td><td>Fires when a link in a campaign is clicked. Batchable event.</td></tr><tr><td>Campaign Opened</td><td><code>campaign.open</code></td><td>Fires when a campaign email is opened. Batchable event.</td></tr><tr><td>Campaign Sent</td><td><code>campaign.sent</code></td><td>Fires when a campaign is sent.</td></tr><tr><td>Subscriber Added To Group</td><td><code>subscriber.added_to_group</code></td><td>Fires when a subscriber is added to a group.</td></tr><tr><td>Subscriber Automation Completed</td><td><code>subscriber.automation_completed</code></td><td>Fires when an automation completes for a subscriber.</td></tr><tr><td>Subscriber Automation Triggered</td><td><code>subscriber.automation_triggered</code></td><td>Fires when an automation is triggered for a subscriber.</td></tr><tr><td>Subscriber Bounced</td><td><code>subscriber.bounced</code></td><td>Fires when a subscriber email bounces.</td></tr><tr><td>Subscriber Created</td><td><code>subscriber.created</code></td><td>Fires when a new subscriber is created.</td></tr><tr><td>Subscriber Deleted</td><td><code>subscriber.deleted</code></td><td>Fires when a subscriber is deleted. Batchable event.</td></tr><tr><td>Subscriber Removed From Group</td><td><code>subscriber.removed_from_group</code></td><td>Fires when a subscriber is removed from a group.</td></tr></tbody></table>

<details>

<summary>View 3 more events</summary>

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Subscriber Spam Reported</td><td><code>subscriber.spam_reported</code></td><td>Fires when a subscriber reports a campaign as spam.</td></tr><tr><td>Subscriber Unsubscribed</td><td><code>subscriber.unsubscribed</code></td><td>Fires when a subscriber unsubscribes.</td></tr><tr><td>Subscriber Updated</td><td><code>subscriber.updated</code></td><td>Fires when a subscriber is updated.</td></tr></tbody></table>

</details>
