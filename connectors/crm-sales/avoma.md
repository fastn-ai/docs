---
description: "Avoma conversation intelligence — meetings, recordings, transcriptions, AI notes, smart categories, scorecards, sentiments, calls, users, engagement,…"
hidden: true
---

# Avoma

Avoma conversation intelligence — meetings, recordings, transcriptions, AI notes, smart categories, scorecards, sentiments, calls, users, engagement, snippets, and webhooks.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [avoma.com](https://avoma.com) |
| **Authentication** | Bearer token |
| **Actions** | 54 |
| **Events** | 0 |
| **Slug** | `avoma` |

## Use it

Add Avoma from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.avoma.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Clear Webhook Signing Secret | `clearWebhookSigningSecret` | Clear/delete the webhook signing secret. |
| Create Call | `createCall` | Create an external call record in Avoma from a dialer/telephony system. |
| Create Meeting Outcome | `createMeetingOutcome` | Create a meeting outcome. |
| Create Meeting Type | `createMeetingType` | Create a meeting type (purpose). |
| Create Smart Category | `createSmartCategory` | Create a smart category with settings, prompts and keywords. |
| Create Template | `createTemplate` | Create a note template from categories and meeting types. |
| Create Webhook | `createWebhook` | Register a webhook subscription for an event type. Event types: AINOTE, new_conversation. |
| Delete Meeting Outcome | `deleteMeetingOutcome` | Delete a meeting outcome by UUID. |
| Delete Meeting Type | `deleteMeetingType` | Delete a meeting type by UUID. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription by UUID. |
| Drop Meeting Bot | `dropMeetingBot` | Drop the Avoma recording bot from an ongoing meeting. |
| Get Call | `getCall` | Retrieve a single call by its external_id. |
| Get Custom Category | `getCustomCategory` | Retrieve a single custom category by UUID. |
| Get Engagement Summary | `getEngagementSummary` | Get overall engagement summary for all users within a date range. |
| Get Meeting | `getMeeting` | Retrieve a single meeting by UUID. |
| Get Meeting Insights | `getMeetingInsights` | Get AI-generated notes and keyword insights for a meeting. |
| Get Meeting Outcome | `getMeetingOutcome` | Retrieve a single meeting outcome by UUID. |
| Get Meeting Sentiments | `getMeetingSentiments` | Get sentiment analysis (positive/negative/neutral tone) for a meeting. |
| Get Meeting Type | `getMeetingType` | Retrieve a single meeting type by UUID. |
| Get Recording | `getRecording` | Retrieve a single recording by UUID. |
| Get Revenue Intel Timeline | `getRevenueTimeline` | Get aggregated timeline engagement metrics for a CRM entity. |
| Get Revenue Intel Timeline Details | `getRevenueTimelineDetails` | Get detailed engagement records (meetings/calls/emails) for a CRM entity with pagination. |
| Get Scorecard | `getScorecard` | Retrieve a single scorecard by UUID. |
| Get Smart Category | `getSmartCategory` | Retrieve a single smart category by UUID. |
| Get Template | `getTemplate` | Retrieve a single note template by UUID. |
| Get Transcription | `getTranscription` | Retrieve a single transcription by UUID. |
| Get User | `getUser` | Retrieve a single user by UUID. |
| Get User Engagement Metrics | `getUserEngagement` | Get engagement metrics for a specific user within a date range. |
| Get User Engagement Summary | `getUserEngagementSummary` | Get engagement summary for a specific user's participants within a date range. |
| Get Webhook Signing Secret | `getWebhookSigningSecret` | Get the current webhook signing secret used to verify payloads. |
| List Calls | `listCalls` | List calls in the organization within a date range. Returns paginated results. |
| List Custom Categories | `listCustomCategories` | List custom (smart) categories used to extract AI notes. |
| List Engagement Metrics | `listEngagement` | List engagement metrics for all users within a date range. |
| List Meeting Outcomes | `listMeetingOutcomes` | List meeting outcomes. |
| List Meeting Segments | `listMeetingSegments` | List AI-generated smart chapters/segments for a meeting. |
| List Meeting Types | `listMeetingTypes` | List meeting types (purposes). |
| List Meetings | `listMeetings` | List meetings in the organization within a date range (paginated). |
| List Notes | `listNotes` | List AI-generated meeting notes within a date range (paginated). |
| List Recordings | `listRecordings` | List recordings for a meeting. |
| List Scorecard Evaluations | `listScorecardEvaluations` | List scorecard evaluations (call scoring results). |
| List Scorecards | `listScorecards` | List scorecard definitions used for call scoring. |
| List Smart Categories | `listSmartCategories` | List smart categories (AI note extraction categories). |
| List Snippets | `listSnippets` | List meeting snippets (soundbites), optionally filtered. |
| List Templates | `listTemplates` | List note templates. |
| List Transcriptions | `listTranscriptions` | List meeting transcriptions within a date range (paginated). |
| List Users | `listUsers` | List users in the organization. |
| List Webhooks | `listWebhooks` | List registered webhook subscriptions. |
| Rotate Webhook Signing Secret | `rotateWebhookSigningSecret` | Rotate (regenerate) the webhook signing secret. |
| Set Webhook Signing Secret | `setWebhookSigningSecret` | Set/update the webhook signing secret. |
| Update Call | `updateCall` | Partially update a call by external_id. Only provided fields are updated. |
| Update Meeting Outcome | `updateMeetingOutcome` | Partially update a meeting outcome. |
| Update Meeting Type | `updateMeetingType` | Partially update a meeting type. |
| Update Smart Category | `updateSmartCategory` | Partially update a smart category's settings, prompts, or keywords. |
| Update Template | `updateTemplate` | Replace a note template (full update). |
