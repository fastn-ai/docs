---
description: "Fireflies.ai connector — GraphQL API for AI meeting notetaker."
hidden: true
---

# Fireflies

<img src="../../.gitbook/assets/connectors/lg/fireflies.png" alt="Fireflies logo">

Fireflies.ai connector — GraphQL API for AI meeting notetaker. Manage transcripts, summaries, soundbites (bites), users, channels, AskFred AI threads, live meetings, and audio uploads. Auth via Bearer API key.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [fireflies.ai](https://fireflies.ai) |
| **Authentication** | Bearer token |
| **Slug** | `fireflies` |

## Use it

Add Fireflies from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fireflies.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Bot To Live Meeting | `addToLiveMeeting` | Send the Fireflies notetaker bot to join a live meeting by its link. Rate limit: 3 requests per 20 minutes. |
| Confirm Upload | `confirmUpload` | Confirm a direct file upload (created via Create Upload URL) so Fireflies begins transcription. |
| Continue AskFred Thread | `continueAskFredThread` | Add a follow-up question to an existing AskFred conversation thread. Consumes AI credits. |
| Create AskFred Thread | `createAskFredThread` | Start a new AskFred AI conversation about a meeting (or multiple meetings). Consumes AI credits. |
| Create Bite | `createBite` | Create a soundbite (clip) from a meeting transcript between start_time and end_time (in seconds). |
| Create Live Action Item | `createLiveActionItem` | Generate a live action item in an in-progress meeting from a prompt. |
| Create Live Soundbite | `createLiveSoundbite` | Generate a live soundbite in an in-progress meeting from a prompt. |
| Create Upload URL | `createUploadUrl` | Create a pre-signed URL to directly upload an audio/video file for transcription. Returns the upload URL and meeting ID. |
| Delete AskFred Thread | `deleteAskFredThread` | Delete an AskFred conversation thread by ID. |
| Delete Transcript | `deleteTranscript` | Permanently delete a meeting transcript. Rate limit: 10 requests per minute. DESTRUCTIVE. |
| Get Analytics | `getAnalytics` | Get team and per-user meeting analytics. Optionally pass a Unix-ms time range. |
| Get AskFred Thread | `getAskFredThread` | Get a single AskFred thread by ID, including its message history. |
| Get Bite | `getBite` | Get a single soundbite (clip) by ID. |
| Get Channel | `getChannel` | Get a single channel by ID, including members. |
| Get Current User | `getCurrentUser` | Get details for the authenticated user (the API key owner). |
| Get Live Action Items | `getLiveActionItems` | Get live action items generated for an in-progress meeting. |
| Get Transcript | `getTranscript` | Get a single transcript by ID with full detail: summary, sentences, speakers, attendees, analytics and meeting info. |
| Get User | `getUser` | Get a single user's details by user ID. |
| List Active Meetings | `listActiveMeetings` | List currently in-progress (live) meetings being recorded. |
| List AI App Outputs | `listApps` | List AI App (Fireflies Apps) outputs generated for meetings. |
| List AskFred Threads | `listAskFredThreads` | List AskFred AI conversation threads. |
| List Audit Events | `listAuditEvents` | List organization audit log events (Enterprise). Cursor-paginated. |
| List Bites | `listBites` | List soundbites (clips) created from meetings, with pagination. |
| List Channels | `listChannels` | List channels accessible to the user. |
| List Contacts | `listContacts` | List the user's meeting contacts. |
| List Rule Executions By Meeting | `listRuleExecutions` | List automation rule executions grouped by meeting (Enterprise). Cursor-paginated. |
| List Transcripts | `listTranscripts` | List recent meeting transcripts with pagination. Returns core transcript fields, speakers and summary highlights. |
| List User Groups | `listUserGroups` | List user groups in the team. |
| List Users | `listUsers` | List all users on the team/workspace. |
| Revoke Shared Meeting Access | `revokeSharedMeetingAccess` | Revoke a specific user's access to a previously shared meeting. |
| Search Transcripts | `searchTranscripts` | Search meeting transcripts by keyword across titles/content with pagination. |
| Set User Role | `setUserRole` | Update a team user's role. Requires admin privileges. |
| Share Meeting | `shareMeeting` | Share a meeting transcript with email recipients. Rate limit: 10 requests per hour. |
| Update Meeting Channel | `updateMeetingChannel` | Assign one or more meeting transcripts (1-5) to a channel. |
| Update Meeting Privacy | `updateMeetingPrivacy` | Change a meeting transcript's privacy/visibility level. |
| Update Meeting State | `updateMeetingState` | Pause or resume recording of a live meeting. |
| Update Meeting Title | `updateMeetingTitle` | Update the title of a meeting transcript. |
| Upload Audio | `uploadAudio` | Upload an audio/video file by URL for transcription. Returns processing status; the transcript is created asynchronously. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Meeting Summarized | `meeting.summarized` | Triggers when a meeting summary has been generated. Use the meeting_id to fetch the summary via the GraphQL API. |
| Meeting Transcribed | `meeting.transcribed` | Triggers when a meeting has been transcribed and the transcript is ready. Use the meeting_id to fetch the transcript via the GraphQL API. |
