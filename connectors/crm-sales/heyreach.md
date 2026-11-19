---
description: "HeyReach automates LinkedIn outreach. Manage campaigns, lead lists, leads, sender accounts and inbox conversations."
hidden: true
---

# HeyReach

<img src="../../.gitbook/assets/connectors/lg/heyreach.png" alt="HeyReach logo">

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [heyreach.io](https://heyreach.io) |
| **Authentication** | API key |
| **Slug** | `heyreach` |

## Setup

Your customers enter their API key for HeyReach when they connect. Nothing else needs setting up.

## Use it

Add HeyReach from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.heyreach.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Leads To Campaign</td><td><code>addLeadsToCampaign</code></td><td>Add LinkedIn leads to an ACTIVE campaign (with assigned sender accounts). Body: { campaignId, accountLeadPairs:[{ linkedInAccountId, lead:{ profileUrl, firstName, lastName,... } }] }.</td></tr><tr><td>Add Leads To List</td><td><code>addLeadsToList</code></td><td>Add leads to a list. Body: { listId, leads:[{ profileUrl, firstName, lastName,... }] }.</td></tr><tr><td>Add Tags To Lead</td><td><code>addTagsToLead</code></td><td>Add tags to a lead (additive, keeps existing tags). Body: { leadProfileUrl, tags:[] }. Optionally createTagIfNotExisting.</td></tr><tr><td>Check API Key</td><td><code>checkApiKey</code></td><td>Validate that the configured HeyReach API key is working.</td></tr><tr><td>Create Empty List</td><td><code>createEmptyList</code></td><td>Create a new empty lead or company list in HeyReach that leads can subsequently be added to.</td></tr><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Create a HeyReach webhook subscription that delivers the selected event type to your endpoint, either for all campaigns or for a specific set of campaigns.</td></tr><tr><td>Delete Leads From List</td><td><code>deleteLeadsFromList</code></td><td>Remove one or more leads from a HeyReach list, identifying each lead by its LinkedIn profile URL.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Permanently delete a HeyReach webhook subscription. The webhook must first be deactivated with Update Webhook (isActive set to false), otherwise the API rejects the request.</td></tr><tr><td>Get Campaign</td><td><code>getCampaign</code></td><td>Get a single campaign by ID (query param campaignId).</td></tr><tr><td>Get Campaigns For Lead</td><td><code>getCampaignsForLead</code></td><td>Get all campaigns a lead belongs to. Body: { profileUrl }.</td></tr></tbody></table>

<details>

<summary>View 22 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Chatroom</td><td><code>getChatroom</code></td><td>Retrieve a single LinkedIn conversation thread, including all of its messages, for a given sender account and conversation.</td></tr><tr><td>Get Companies From List</td><td><code>getCompaniesFromList</code></td><td>Get companies from a company list. Body: { listId, offset, limit }.</td></tr><tr><td>Get Conversations</td><td><code>getConversations</code></td><td>Get inbox conversations with filters. Body: { offset, limit, filters:{ linkedInAccountIds, campaignIds, seen } }.</td></tr><tr><td>Get Lead</td><td><code>getLead</code></td><td>Get details for a single lead by LinkedIn profile URL. Body: { profileUrl }.</td></tr><tr><td>Get Lead Tags</td><td><code>getLeadTags</code></td><td>Get the tags assigned to a lead by LinkedIn profile URL. Body: { profileUrl }.</td></tr><tr><td>Get Leads From Campaign</td><td><code>getLeadsFromCampaign</code></td><td>Get leads in a campaign with status filters. Body: { campaignId, offset, limit }.</td></tr><tr><td>Get Leads From List</td><td><code>getLeadsFromList</code></td><td>Get leads from a list with pagination. Body: { listId, offset, limit }.</td></tr><tr><td>Get LinkedIn Account</td><td><code>getLinkedInAccount</code></td><td>Get a LinkedIn sender account by ID (query param accountId).</td></tr><tr><td>Get List</td><td><code>getList</code></td><td>Get a list by ID (query param listId).</td></tr><tr><td>Get My Network For Sender</td><td><code>getMyNetworkForSender</code></td><td>Retrieve the LinkedIn network (first-degree connections) visible to a specific sender account, with paging controlled by page number and page size.</td></tr><tr><td>Get Overall Stats</td><td><code>getOverallStats</code></td><td>Get aggregate analytics (sends, connections, replies, etc). Body: { accountIds, campaignIds, startDate, endDate }.</td></tr><tr><td>Get Overall Stats By Campaign</td><td><code>getOverallStatsByCampaign</code></td><td>Get aggregate analytics broken down per campaign. Body: { accountIds:[], campaignIds:[], startDate?, endDate? }.</td></tr><tr><td>List Campaigns</td><td><code>listCampaigns</code></td><td>List all campaigns with pagination. Body: { offset, limit }. Optional statuses/accountIds filters.</td></tr><tr><td>List LinkedIn Accounts</td><td><code>listLinkedInAccounts</code></td><td>List LinkedIn sender accounts with pagination. Body: { offset, limit }.</td></tr><tr><td>List Lists</td><td><code>listLists</code></td><td>List all lead/company lists with pagination. Body: { offset, limit }.</td></tr><tr><td>List Webhooks</td><td><code>listWebhooks</code></td><td>List all configured webhooks. Body: { offset, limit }.</td></tr><tr><td>Pause Campaign</td><td><code>pauseCampaign</code></td><td>Pause an active campaign (query param campaignId).</td></tr><tr><td>Replace Lead Tags</td><td><code>replaceLeadTags</code></td><td>Replace ALL tags on a lead with the provided set. Body: { leadProfileUrl, tags:[] }. Optionally createTagIfNotExisting.</td></tr><tr><td>Resume Campaign</td><td><code>resumeCampaign</code></td><td>Resume a paused campaign (query param campaignId).</td></tr><tr><td>Send Message</td><td><code>sendMessage</code></td><td>Send a message in a conversation. Body: { conversationId, linkedInAccountId, message, subject? }.</td></tr><tr><td>Stop Lead In Campaign</td><td><code>stopLeadInCampaign</code></td><td>Stop an individual lead's progress in a campaign so no further outreach steps are executed for that lead. Identify the lead by LinkedIn profile URL or by LinkedIn member id.</td></tr><tr><td>Update Webhook</td><td><code>updateWebhook</code></td><td>Update an existing HeyReach webhook subscription. Only the fields you supply are changed; omitted fields keep their current values.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Connection Request Accepted</td><td><code>CONNECTION_REQUEST_ACCEPTED</code></td><td>A lead accepted a connection request.</td></tr><tr><td>Connection Request Sent</td><td><code>CONNECTION_REQUEST_SENT</code></td><td>A connection request was sent to a lead.</td></tr><tr><td>Follow Sent</td><td><code>FOLLOW_SENT</code></td><td>A lead was followed.</td></tr><tr><td>InMail Sent</td><td><code>INMAIL_SENT</code></td><td>An InMail was sent to a lead.</td></tr><tr><td>Lead Tag Updated</td><td><code>LEAD_TAG_UPDATED</code></td><td>A lead's status/tag was updated.</td></tr><tr><td>Liked Post</td><td><code>LIKED_POST</code></td><td>A lead's post was liked.</td></tr><tr><td>Message Reply Received</td><td><code>MESSAGE_REPLY_RECEIVED</code></td><td>A lead replied to a message (or InMail reply).</td></tr><tr><td>Message Sent</td><td><code>MESSAGE_SENT</code></td><td>A message was sent to a lead.</td></tr><tr><td>Viewed Profile</td><td><code>VIEWED_PROFILE</code></td><td>A lead's profile was viewed.</td></tr></tbody></table>
