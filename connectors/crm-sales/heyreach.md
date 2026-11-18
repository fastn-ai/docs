---
description: "HeyReach LinkedIn outreach automation."
hidden: true
---

# HeyReach

<img src="../../.gitbook/assets/connectors/heyreach.jpg" alt="HeyReach logo" width="64">

HeyReach LinkedIn outreach automation. Manage campaigns, lead lists, leads, LinkedIn sender accounts, inbox conversations, network, webhooks, and analytics via the HeyReach public API (X-API-KEY auth).

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [heyreach.io](https://heyreach.io) |
| **Authentication** | API key |
| **Slug** | `heyreach` |

## Use it

Add HeyReach from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.heyreach.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Leads To Campaign | `addLeadsToCampaign` | Add LinkedIn leads to an ACTIVE campaign (with assigned sender accounts). Body: { campaignId, accountLeadPairs:[{ linkedInAccountId, lead:{ profileUrl, firstName, lastName, ... } }] }. |
| Add Leads To List | `addLeadsToList` | Add leads to a list. Body: { listId, leads:[{ profileUrl, firstName, lastName, ... }] }. |
| Add Tags To Lead | `addTagsToLead` | Add tags to a lead (additive, keeps existing tags). Body: { leadProfileUrl, tags:[] }. Optionally createTagIfNotExisting. |
| Check API Key | `checkApiKey` | Validate that the configured HeyReach API key is working. Returns 200 when valid. |
| Create Empty List | `createEmptyList` | Create a new empty lead or company list in HeyReach that leads can subsequently be added to. |
| Create Webhook | `createWebhook` | Create a HeyReach webhook subscription that delivers the selected event type to your endpoint, either for all campaigns or for a specific set of campaigns. |
| Delete Leads From List | `deleteLeadsFromList` | Remove one or more leads from a HeyReach list, identifying each lead by its LinkedIn profile URL. |
| Delete Webhook | `deleteWebhook` | Permanently delete a HeyReach webhook subscription. The webhook must first be deactivated with Update Webhook (isActive set to false), otherwise the API rejects the request. |
| Get Campaign | `getCampaign` | Get a single campaign by ID (query param campaignId). |
| Get Campaigns For Lead | `getCampaignsForLead` | Get all campaigns a lead belongs to. Body: { profileUrl }. |

<details>

<summary>See 22 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Chatroom | `getChatroom` | Retrieve a single LinkedIn conversation thread, including all of its messages, for a given sender account and conversation. |
| Get Companies From List | `getCompaniesFromList` | Get companies from a company list. Body: { listId, offset, limit }. |
| Get Conversations | `getConversations` | Get inbox conversations with filters. Body: { offset, limit, filters:{ linkedInAccountIds, campaignIds, seen } }. |
| Get Lead | `getLead` | Get details for a single lead by LinkedIn profile URL. Body: { profileUrl }. |
| Get Lead Tags | `getLeadTags` | Get the tags assigned to a lead by LinkedIn profile URL. Body: { profileUrl }. |
| Get Leads From Campaign | `getLeadsFromCampaign` | Get leads in a campaign with status filters. Body: { campaignId, offset, limit }. |
| Get Leads From List | `getLeadsFromList` | Get leads from a list with pagination. Body: { listId, offset, limit }. |
| Get LinkedIn Account | `getLinkedInAccount` | Get a LinkedIn sender account by ID (query param accountId). |
| Get List | `getList` | Get a list by ID (query param listId). |
| Get My Network For Sender | `getMyNetworkForSender` | Retrieve the LinkedIn network (first-degree connections) visible to a specific sender account, with paging controlled by page number and page size. |
| Get Overall Stats | `getOverallStats` | Get aggregate analytics (sends, connections, replies, etc). Body: { accountIds, campaignIds, startDate, endDate }. |
| Get Overall Stats By Campaign | `getOverallStatsByCampaign` | Get aggregate analytics broken down per campaign. Body: { accountIds:[], campaignIds:[], startDate?, endDate? }. |
| List Campaigns | `listCampaigns` | List all campaigns with pagination. Body: { offset, limit }. Optional statuses/accountIds filters. |
| List LinkedIn Accounts | `listLinkedInAccounts` | List LinkedIn sender accounts with pagination. Body: { offset, limit }. |
| List Lists | `listLists` | List all lead/company lists with pagination. Body: { offset, limit }. |
| List Webhooks | `listWebhooks` | List all configured webhooks. Body: { offset, limit }. |
| Pause Campaign | `pauseCampaign` | Pause an active campaign (query param campaignId). |
| Replace Lead Tags | `replaceLeadTags` | Replace ALL tags on a lead with the provided set. Body: { leadProfileUrl, tags:[] }. Optionally createTagIfNotExisting. |
| Resume Campaign | `resumeCampaign` | Resume a paused campaign (query param campaignId). |
| Send Message | `sendMessage` | Send a message in a conversation. Body: { conversationId, linkedInAccountId, message, subject? }. |
| Stop Lead In Campaign | `stopLeadInCampaign` | Stop an individual lead's progress in a campaign so no further outreach steps are executed for that lead. Identify the lead by LinkedIn profile URL or by LinkedIn member id. |
| Update Webhook | `updateWebhook` | Update an existing HeyReach webhook subscription. Only the fields you supply are changed; omitted fields keep their current values. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Connection Request Accepted | `CONNECTION_REQUEST_ACCEPTED` | A lead accepted a connection request. |
| Connection Request Sent | `CONNECTION_REQUEST_SENT` | A connection request was sent to a lead. |
| Follow Sent | `FOLLOW_SENT` | A lead was followed. |
| InMail Sent | `INMAIL_SENT` | An InMail was sent to a lead. |
| Lead Tag Updated | `LEAD_TAG_UPDATED` | A lead's status/tag was updated. |
| Liked Post | `LIKED_POST` | A lead's post was liked. |
| Message Reply Received | `MESSAGE_REPLY_RECEIVED` | A lead replied to a message (or InMail reply). |
| Message Sent | `MESSAGE_SENT` | A message was sent to a lead. |
| Viewed Profile | `VIEWED_PROFILE` | A lead's profile was viewed. |
