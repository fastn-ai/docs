---
description: "Sendspark personalised video outreach API (api-gw.sendspark.com/v1): workspaces, dynamic video campaigns, prospects, video transcripts and webhooks."
hidden: true
---

# Sendspark

<img src="../../.gitbook/assets/connectors/lg/sendspark.png" alt="Sendspark logo">

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [sendspark.com](https://sendspark.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `sendspark` |

## Use it

Add Sendspark from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sendspark.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Prospect To Dynamic Campaign</td><td><code>addProspectToDynamicCampaign</code></td><td>Add a single prospect to a dynamic video campaign. Set processAndAuthorizeCharge=true to immediately render the personalised video (this consumes dynamic-video minutes); leave it false to only store the prospect. POST /v1/workspaces/{workspaceId}/dynamics/{dynamicsId}/prospect.</td></tr><tr><td>Bulk Add Prospects To Dynamic Campaign</td><td><code>bulkAddProspectsToDynamicCampaign</code></td><td>Add many prospects to a dynamic video campaign in one call. Vendor rate limit: 1 request per minute for this route. Set processAndAuthorizeCharge=true to render videos immediately (consumes dynamic-video minutes). POST /v1/workspaces/{workspaceId}/dynamics/{dynamicsId}/prospects/bulk.</td></tr><tr><td>Create Dynamic Video Campaign</td><td><code>createDynamicCampaign</code></td><td>Create an empty dynamic video campaign in the workspace. Note: the Sendspark v1 API has no delete route for campaigns - removing one is web-app only. POST /v1/workspaces/{workspaceId}/dynamics.</td></tr><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Register a webhook subscription on the workspace. module is 'global' (all videos) or 'dynamics' (restricted to the campaign ids in identifiers). events selects the video events delivered. POST /v1/workspaces/{workspaceId}/webhooks.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Delete a webhook subscription by id. Returns HTTP 204 with an empty body on success - confirm with List Webhooks. DELETE /v1/workspaces/{workspaceId}/webhooks/{webhookId}.</td></tr><tr><td>Get Campaign Transcript Status</td><td><code>getCampaignTranscriptStatus</code></td><td>Check whether the transcript for a campaign video has finished processing. GET /v1/workspaces/{workspaceId}/campaigns/{campaignId}/transcript/status.</td></tr><tr><td>Get Campaign Video Transcript</td><td><code>getCampaignTranscript</code></td><td>Get the transcript of a recorded campaign video. format accepts json (default), vtt or srt. GET /v1/workspaces/{workspaceId}/campaigns/{campaignId}/transcript.</td></tr><tr><td>Get Dynamic Video Campaign</td><td><code>getDynamicCampaign</code></td><td>Fetch one dynamic video campaign by id, including its video, buttons, calendar and prospect configuration. GET /v1/workspaces/{workspaceId}/dynamics/{dynamicId}.</td></tr><tr><td>Get Dynamics Workspace Settings</td><td><code>getDynamicsSettings</code></td><td>Get the workspace-level dynamic video settings (supported languages, greeting placeholders, fallbacks). GET /v1/workspaces/{workspaceId}/dynamics/settings.</td></tr><tr><td>Get Prospect By Email</td><td><code>getProspectByEmail</code></td><td>Fetch the prospect record (and its generated personalised video data) for one contact email inside a dynamic campaign. GET /v1/workspaces/{workspaceId}/dynamics/{dynamicId}/prospects/{contactEmail}.</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Webhook</td><td><code>getWebhook</code></td><td>Fetch a single webhook subscription by its id. GET /v1/workspaces/{workspaceId}/webhooks/{webhookId}.</td></tr><tr><td>Get Workspace Id From Api Key</td><td><code>getWorkspaceIdentifier</code></td><td>Resolve the workspace id that the supplied API key belongs to. GET /v1/workspaces/identifier.</td></tr><tr><td>List Dynamic Video Campaigns</td><td><code>listDynamicCampaigns</code></td><td>List the dynamic video campaigns in the connected workspace, paginated. offset is 1-based - the vendor returns HTTP 500 for offset=0. GET /v1/workspaces/{workspaceId}/dynamics.</td></tr><tr><td>List Webhooks</td><td><code>listWebhooks</code></td><td>List all webhook subscriptions registered on the connected workspace. The raw vendor response is a JSON array of webhook objects. GET /v1/workspaces/{workspaceId}/webhooks.</td></tr><tr><td>List Workspaces</td><td><code>listWorkspaces</code></td><td>List the Sendspark workspaces the authenticated user belongs to, with plan and member details. GET /v1/workspaces.</td></tr><tr><td>Update Webhook</td><td><code>updateWebhook</code></td><td>Modify an existing webhook subscription: rename it, change the delivery url, change subscribed events or enable/disable it. PATCH /v1/workspaces/{workspaceId}/webhooks/{webhookId}.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Dynamic Video Generated</td><td><code>video_generated_dv</code></td><td>A personalised dynamic video finished generating for a prospect.</td></tr><tr><td>Video CTA Clicked</td><td><code>video_cta_clicked</code></td><td>A viewer clicked the call-to-action button on the video page.</td></tr><tr><td>Video Generation Failed</td><td><code>video_generated_error</code></td><td>Generation of a personalised video failed for a prospect.</td></tr><tr><td>Video Liked</td><td><code>video_liked</code></td><td>A viewer liked the video.</td></tr><tr><td>Video MP4 Ready To Download</td><td><code>video_mp4_ready</code></td><td>The MP4 render is ready; the payload carries low/medium/high download links.</td></tr><tr><td>Video Page Viewed</td><td><code>video_viewed</code></td><td>The video landing page was viewed.</td></tr><tr><td>Video Played</td><td><code>video_played</code></td><td>A viewer started playing the video.</td></tr><tr><td>Video Request Received</td><td><code>video_request_received</code></td><td>A video submitted through a Sendspark request link was received.</td></tr><tr><td>Video Watched To The End</td><td><code>video_watched</code></td><td>A viewer watched the video to the end; the payload carries watchPercentage.</td></tr></tbody></table>
