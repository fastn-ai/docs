---
description: "Mailchimp Marketing API v3.0 (base https://{dc}.api.mailchimp.com/3.0)."
hidden: true
---

# Mailchimp

<img src="../../.gitbook/assets/connectors/lg/mailchimp.png" alt="Mailchimp logo">

Mailchimp Marketing API v3.0 (base https://{dc}.api.mailchimp.com/3.0). Manage audiences (lists), members + tags, merge fields, segments, campaigns (create/content/send/schedule/test), templates, reports, automations, and list webhooks. Auth: HTTP Basic (any username + API key as password); the datacenter prefix (e.g. us21) comes from the API key suffix.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [mailchimp.com](https://mailchimp.com) |
| **Authentication** | Basic auth |
| **Slug** | `mailchimp` |

## Use it

Add Mailchimp from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailchimp.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Member | `addMember` | Add a member to an audience (POST /lists/{list_id}/members). |
| Add Member Tags | `addMemberTags` | Add or remove tags on a member (POST /lists/{list_id}/members/{subscriber_hash}/tags). Returns 204. |
| Archive Member | `archiveMember` | Archive a member (DELETE /lists/{list_id}/members/{subscriber_hash}). Returns 204. |
| Create Audience | `createAudience` | Create an audience/list (POST /lists). |
| Create Audience Webhook | `createListWebhook` | Create a webhook for an audience (POST /lists/{list_id}/webhooks). Used by the webhook config. |
| Create Campaign | `createCampaign` | Create a campaign (POST /campaigns). |
| Create Merge Field | `createMergeField` | Create a merge field (POST /lists/{list_id}/merge-fields). |
| Create Segment | `createSegment` | Create a segment or static tag (POST /lists/{list_id}/segments). |
| Delete Audience | `deleteAudience` | Delete an audience (DELETE /lists/{list_id}). Returns 204. |
| Delete Audience Webhook | `deleteListWebhook` | Delete an audience webhook (DELETE /lists/{list_id}/webhooks/{webhook_id}). Returns 204. |
| Delete Campaign | `deleteCampaign` | Delete a campaign (DELETE /campaigns/{campaign_id}). Returns 204. |
| Delete Member Permanently | `deleteMemberPermanently` | Permanently delete all personally identifiable information for an audience member and remove them from the audience. The member cannot be re-imported afterwards (POST /lists/{list_id}/members/{subscriber_hash}/actions/delete-permanent). Returns 204 on success. |
| Delete Merge Field | `deleteMergeField` | Delete a merge field from an audience (DELETE /lists/{list_id}/merge-fields/{merge_id}). Returns 204. |
| Delete Segment | `deleteSegment` | Delete a segment or static tag from an audience (DELETE /lists/{list_id}/segments/{segment_id}). Returns 204. |
| Get Audience | `getAudience` | Get an audience by id (GET /lists/{list_id}). |
| Get Campaign | `getCampaign` | Get a campaign (GET /campaigns/{campaign_id}). |
| Get Member | `getMember` | Get a member by subscriber hash or email (GET /lists/{list_id}/members/{subscriber_hash}). |
| Get Report | `getReport` | Get a campaign report (GET /reports/{campaign_id}). |
| List Audience Webhooks | `listListWebhooks` | List webhooks for an audience (GET /lists/{list_id}/webhooks). |
| List Audiences | `listAudiences` | List audiences (lists) (GET /lists). |
| List Campaigns | `listCampaigns` | List campaigns (GET /campaigns). |
| List Members | `listMembers` | List members of an audience (GET /lists/{list_id}/members). |
| List Merge Fields | `listMergeFields` | List merge fields for an audience (GET /lists/{list_id}/merge-fields). |
| List Reports | `listReports` | List campaign reports (GET /reports). |
| List Segments | `listSegments` | List segments/tags for an audience (GET /lists/{list_id}/segments). |
| List Templates | `listTemplates` | List templates (GET /templates). |
| Ping | `ping` | Health check / verify credentials (GET /ping). |
| Schedule Campaign | `scheduleCampaign` | Schedule a campaign (POST /campaigns/{campaign_id}/actions/schedule). Returns 204. |
| Send Campaign | `sendCampaign` | Send a campaign immediately (POST /campaigns/{campaign_id}/actions/send). Returns 204. |
| Send Test Email | `sendTestEmail` | Send a test email for a campaign (POST /campaigns/{campaign_id}/actions/test). Returns 204. |
| Set Campaign Content | `setCampaignContent` | Set a campaign's HTML or template content (PUT /campaigns/{campaign_id}/content). |
| Update Audience | `updateAudience` | Update an audience (PATCH /lists/{list_id}). |
| Update Member | `updateMember` | Update an existing member (PATCH /lists/{list_id}/members/{subscriber_hash}). |
| Upsert Member | `upsertMember` | Add or update a member (PUT /lists/{list_id}/members/{subscriber_hash}). |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Campaign Sent | `campaign` | A campaign finished sending. |
| Email Changed | `upemail` | A member changed their email address. |
| Email Cleaned | `cleaned` | An email was cleaned (bounced/abuse). |
| Profile Update | `profile` | A member's profile/merge fields changed. |
| Subscribe | `subscribe` | A member subscribed to the audience. |
| Unsubscribe | `unsubscribe` | A member unsubscribed or was removed. |
