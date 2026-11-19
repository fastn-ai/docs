---
description: "Fireflies.ai is an AI meeting notetaker. Manage transcripts, soundbites and AskFred threads, add the bot to live meetings, and upload audio."
hidden: true
---

# Fireflies

<img src="../../.gitbook/assets/connectors/lg/fireflies.png" alt="Fireflies logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [fireflies.ai](https://fireflies.ai) |
| **Authentication** | Access token |
| **Slug** | `fireflies` |

## Setup

Your customers enter their access token for Fireflies when they connect. Nothing else needs setting up.

## Use it

Add Fireflies from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fireflies.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Bot To Live Meeting</td><td><code>addToLiveMeeting</code></td><td>Send the Fireflies notetaker bot to join a live meeting by its link. Rate limit: 3 requests per 20 minutes.</td></tr><tr><td>Confirm Upload</td><td><code>confirmUpload</code></td><td>Confirm a direct file upload (created via Create Upload URL) so Fireflies begins transcription.</td></tr><tr><td>Continue AskFred Thread</td><td><code>continueAskFredThread</code></td><td>Add a follow-up question to an existing AskFred conversation thread. Consumes AI credits.</td></tr><tr><td>Create AskFred Thread</td><td><code>createAskFredThread</code></td><td>Start a new AskFred AI conversation about a meeting (or multiple meetings). Consumes AI credits.</td></tr><tr><td>Create Bite</td><td><code>createBite</code></td><td>Create a soundbite (clip) from a meeting transcript between start_time and end_time (in seconds).</td></tr><tr><td>Create Live Action Item</td><td><code>createLiveActionItem</code></td><td>Generate a live action item in an in-progress meeting from a prompt.</td></tr><tr><td>Create Live Soundbite</td><td><code>createLiveSoundbite</code></td><td>Generate a live soundbite in an in-progress meeting from a prompt.</td></tr><tr><td>Create Upload URL</td><td><code>createUploadUrl</code></td><td>Create a pre-signed URL to directly upload an audio/video file for transcription. Returns the upload URL and meeting ID.</td></tr><tr><td>Delete AskFred Thread</td><td><code>deleteAskFredThread</code></td><td>Delete an AskFred conversation thread by ID.</td></tr><tr><td>Delete Transcript</td><td><code>deleteTranscript</code></td><td>Permanently delete a meeting transcript. Rate limit: 10 requests per minute. DESTRUCTIVE.</td></tr></tbody></table>

<details>

<summary>View 28 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Analytics</td><td><code>getAnalytics</code></td><td>Get team and per-user meeting analytics. Optionally pass a Unix-ms time range.</td></tr><tr><td>Get AskFred Thread</td><td><code>getAskFredThread</code></td><td>Get a single AskFred thread by ID, including its message history.</td></tr><tr><td>Get Bite</td><td><code>getBite</code></td><td>Get a single soundbite (clip) by ID.</td></tr><tr><td>Get Channel</td><td><code>getChannel</code></td><td>Get a single channel by ID, including members.</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Get details for the authenticated user (the API key owner).</td></tr><tr><td>Get Live Action Items</td><td><code>getLiveActionItems</code></td><td>Get live action items generated for an in-progress meeting.</td></tr><tr><td>Get Transcript</td><td><code>getTranscript</code></td><td>Get a single transcript by ID with full detail: summary, sentences, speakers, attendees, analytics and meeting info.</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Get a single user's details by user ID.</td></tr><tr><td>List Active Meetings</td><td><code>listActiveMeetings</code></td><td>List currently in-progress (live) meetings being recorded.</td></tr><tr><td>List AI App Outputs</td><td><code>listApps</code></td><td>List AI App (Fireflies Apps) outputs generated for meetings.</td></tr><tr><td>List AskFred Threads</td><td><code>listAskFredThreads</code></td><td>List AskFred AI conversation threads.</td></tr><tr><td>List Audit Events</td><td><code>listAuditEvents</code></td><td>List organization audit log events (Enterprise). Cursor-paginated.</td></tr><tr><td>List Bites</td><td><code>listBites</code></td><td>List soundbites (clips) created from meetings, with pagination.</td></tr><tr><td>List Channels</td><td><code>listChannels</code></td><td>List channels accessible to the user.</td></tr><tr><td>List Contacts</td><td><code>listContacts</code></td><td>List the user's meeting contacts.</td></tr><tr><td>List Rule Executions By Meeting</td><td><code>listRuleExecutions</code></td><td>List automation rule executions grouped by meeting (Enterprise). Cursor-paginated.</td></tr><tr><td>List Transcripts</td><td><code>listTranscripts</code></td><td>List recent meeting transcripts with pagination. Returns core transcript fields, speakers and summary highlights.</td></tr><tr><td>List User Groups</td><td><code>listUserGroups</code></td><td>List user groups in the team.</td></tr><tr><td>List Users</td><td><code>listUsers</code></td><td>List all users on the team/workspace.</td></tr><tr><td>Revoke Shared Meeting Access</td><td><code>revokeSharedMeetingAccess</code></td><td>Revoke a specific user's access to a previously shared meeting.</td></tr><tr><td>Search Transcripts</td><td><code>searchTranscripts</code></td><td>Search meeting transcripts by keyword across titles/content with pagination.</td></tr><tr><td>Set User Role</td><td><code>setUserRole</code></td><td>Update a team user's role. Requires admin privileges.</td></tr><tr><td>Share Meeting</td><td><code>shareMeeting</code></td><td>Share a meeting transcript with email recipients. Rate limit: 10 requests per hour.</td></tr><tr><td>Update Meeting Channel</td><td><code>updateMeetingChannel</code></td><td>Assign one or more meeting transcripts (1-5) to a channel.</td></tr><tr><td>Update Meeting Privacy</td><td><code>updateMeetingPrivacy</code></td><td>Change a meeting transcript's privacy/visibility level.</td></tr><tr><td>Update Meeting State</td><td><code>updateMeetingState</code></td><td>Pause or resume recording of a live meeting.</td></tr><tr><td>Update Meeting Title</td><td><code>updateMeetingTitle</code></td><td>Update the title of a meeting transcript.</td></tr><tr><td>Upload Audio</td><td><code>uploadAudio</code></td><td>Upload an audio/video file by URL for transcription. Returns processing status; the transcript is created asynchronously.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Meeting Summarized</td><td><code>meeting.summarized</code></td><td>Triggers when a meeting summary has been generated. Use the meeting_id to fetch the summary via the GraphQL API.</td></tr><tr><td>Meeting Transcribed</td><td><code>meeting.transcribed</code></td><td>Triggers when a meeting has been transcribed and the transcript is ready. Use the meeting_id to fetch the transcript via the GraphQL API.</td></tr></tbody></table>
