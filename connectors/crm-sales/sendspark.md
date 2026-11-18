---
description: "Sendspark personalised video outreach API (api-gw.sendspark.com/v1): workspaces, dynamic video campaigns, prospects, video transcripts and webhooks."
hidden: true
---

# Sendspark

<img src="../../.gitbook/assets/connectors/lg/sendspark.png" alt="Sendspark logo">

Sendspark personalised video outreach API (api-gw.sendspark.com/v1): workspaces, dynamic video campaigns, prospects, video transcripts and webhooks.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [sendspark.com](https://sendspark.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `sendspark` |

## Use it

Add Sendspark from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sendspark.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Prospect To Dynamic Campaign | `addProspectToDynamicCampaign` | Add a single prospect to a dynamic video campaign. Set processAndAuthorizeCharge=true to immediately render the personalised video (this consumes dynamic-video minutes); leave it false to only store the prospect. POST /v1/workspaces/{workspaceId}/dynamics/{dynamicsId}/prospect. |
| Bulk Add Prospects To Dynamic Campaign | `bulkAddProspectsToDynamicCampaign` | Add many prospects to a dynamic video campaign in one call. Vendor rate limit: 1 request per minute for this route. Set processAndAuthorizeCharge=true to render videos immediately (consumes dynamic-video minutes). POST /v1/workspaces/{workspaceId}/dynamics/{dynamicsId}/prospects/bulk. |
| Create Dynamic Video Campaign | `createDynamicCampaign` | Create an empty dynamic video campaign in the workspace. Note: the Sendspark v1 API has no delete route for campaigns - removing one is web-app only. POST /v1/workspaces/{workspaceId}/dynamics. |
| Create Webhook | `createWebhook` | Register a webhook subscription on the workspace. module is 'global' (all videos) or 'dynamics' (restricted to the campaign ids in identifiers). events selects the video events delivered. POST /v1/workspaces/{workspaceId}/webhooks. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription by id. Returns HTTP 204 with an empty body on success - confirm with List Webhooks. DELETE /v1/workspaces/{workspaceId}/webhooks/{webhookId}. |
| Get Campaign Transcript Status | `getCampaignTranscriptStatus` | Check whether the transcript for a campaign video has finished processing. GET /v1/workspaces/{workspaceId}/campaigns/{campaignId}/transcript/status. |
| Get Campaign Video Transcript | `getCampaignTranscript` | Get the transcript of a recorded campaign video. format accepts json (default), vtt or srt. GET /v1/workspaces/{workspaceId}/campaigns/{campaignId}/transcript. |
| Get Dynamic Video Campaign | `getDynamicCampaign` | Fetch one dynamic video campaign by id, including its video, buttons, calendar and prospect configuration. GET /v1/workspaces/{workspaceId}/dynamics/{dynamicId}. |
| Get Dynamics Workspace Settings | `getDynamicsSettings` | Get the workspace-level dynamic video settings (supported languages, greeting placeholders, fallbacks). GET /v1/workspaces/{workspaceId}/dynamics/settings. |
| Get Prospect By Email | `getProspectByEmail` | Fetch the prospect record (and its generated personalised video data) for one contact email inside a dynamic campaign. GET /v1/workspaces/{workspaceId}/dynamics/{dynamicId}/prospects/{contactEmail}. |
| Get Webhook | `getWebhook` | Fetch a single webhook subscription by its id. GET /v1/workspaces/{workspaceId}/webhooks/{webhookId}. |
| Get Workspace Id From Api Key | `getWorkspaceIdentifier` | Resolve the workspace id that the supplied API key belongs to. GET /v1/workspaces/identifier. |
| List Dynamic Video Campaigns | `listDynamicCampaigns` | List the dynamic video campaigns in the connected workspace, paginated. offset is 1-based - the vendor returns HTTP 500 for offset=0. GET /v1/workspaces/{workspaceId}/dynamics. |
| List Webhooks | `listWebhooks` | List all webhook subscriptions registered on the connected workspace. The raw vendor response is a JSON array of webhook objects. GET /v1/workspaces/{workspaceId}/webhooks. |
| List Workspaces | `listWorkspaces` | List the Sendspark workspaces the authenticated user belongs to, with plan and member details. GET /v1/workspaces. |
| Update Webhook | `updateWebhook` | Modify an existing webhook subscription: rename it, change the delivery url, change subscribed events or enable/disable it. PATCH /v1/workspaces/{workspaceId}/webhooks/{webhookId}. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Dynamic Video Generated | `video_generated_dv` | A personalised dynamic video finished generating for a prospect. |
| Video CTA Clicked | `video_cta_clicked` | A viewer clicked the call-to-action button on the video page. |
| Video Generation Failed | `video_generated_error` | Generation of a personalised video failed for a prospect. |
| Video Liked | `video_liked` | A viewer liked the video. |
| Video MP4 Ready To Download | `video_mp4_ready` | The MP4 render is ready; the payload carries low/medium/high download links. |
| Video Page Viewed | `video_viewed` | The video landing page was viewed. |
| Video Played | `video_played` | A viewer started playing the video. |
| Video Request Received | `video_request_received` | A video submitted through a Sendspark request link was received. |
| Video Watched To The End | `video_watched` | A viewer watched the video to the end; the payload carries watchPercentage. |
