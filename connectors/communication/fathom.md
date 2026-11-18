---
description: "Fathom AI meeting notetaker."
hidden: true
---

# Fathom

<img src="../../.gitbook/assets/connectors/lg/fathom.png" alt="Fathom logo">

Fathom AI meeting notetaker. Poll meetings, teams, and team members, fetch recording summaries and transcripts, and register webhooks for new meeting content. Wraps the Fathom External API (https://api.fathom.ai/external/v1).

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [fathom.video](https://fathom.video) |
| **Authentication** | API key |
| **Slug** | `fathom` |

## Use it

Add Fathom from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fathom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Create a webhook. Create a webhook to receive new meeting content. At least one of `include_transcript`, `include_crm_matches`, `include_summary`, or `include_action_items` must be true. Live API: at least one of include_transcript, include_summary, include_action_items or include_crm_matches must be true, else 400 'At least one content type must be included'.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Delete a webhook. Delete a webhook.</td></tr><tr><td>Get download status</td><td><code>getRecordingDownload</code></td><td>Get download status. Returns the status of a download created with the request-a-download endpoint. When the download is completed, the payload carries a short-lived signed URL for the generated file. Only the API client that created the download can read it.</td></tr><tr><td>Get Recording Summary</td><td><code>getRecordingSummary</code></td><td>Get summary. This endpoint has two behaviors depending on your request payload: - If you send `destination_url`, the endpoint will behave in an asynchronous manner. - If you do not send `destination_url`, the endpoint will return the data directly.</td></tr><tr><td>Get Recording Transcript</td><td><code>getRecordingTranscript</code></td><td>Get transcript. This endpoint has two behaviors depending on your request payload: - If you send `destination_url`, the endpoint will behave in an asynchronous manner. - If you do not send `destination_url`, the endpoint will return the data directly.</td></tr><tr><td>List meeting types</td><td><code>listMeetingTypes</code></td><td>List meeting types. List your org's meeting types, including both `active` and `inactive`. Use the returned `name` values as the meeting_type filter on GET /meetings.</td></tr><tr><td>List Meetings</td><td><code>listMeetings</code></td><td>List meetings.</td></tr><tr><td>List Team Members</td><td><code>listTeamMembers</code></td><td>List team members.</td></tr><tr><td>List Teams</td><td><code>listTeams</code></td><td>List teams.</td></tr><tr><td>List users and their permissions</td><td><code>listUsers</code></td><td>List users and their permissions. List all users in the account with their permissions. Admin only. Returns 403 Forbidden unless the API key belongs to a user with `settings_access` of `account_admin`. Results include active, deactivated, then pending members; page through with `next_cursor`, or filter with `status`. Invited users have no permissions object yet, and their `created_at` is the invite date.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Request a download</td><td><code>createRecordingDownload</code></td><td>Request a download. Starts async generation of a downloadable file and returns a `download_id` to poll. Video is generated in the background; audio-only recordings complete immediately, so the response may already return `status: completed` with the file payload. Downloads are private to the API client that created them, and URLs expire ~24 hours after generation—request a new one when it expires. Only the owner, teammates who can view the recording, and people it was shared with at standard or admin level can download it. Limited-access shares get `403 Forbidden`.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>New Meeting Content Ready</td><td><code>new_meeting_content_ready</code></td><td>Sent after a meeting finishes processing and its content (summary/transcript/action items/CRM matches, per the webhook's include_* flags) is ready. Delivered as a Meeting object. Headers webhook-id, webhook-timestamp, and webhook-signature (Svix format: version,base64signature) accompany the POST for verification using the per-webhook secret.</td></tr></tbody></table>
