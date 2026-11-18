---
description: "Fireflies.ai connector — GraphQL API (single POST https://api.fireflies.ai/graphql) for the AI meeting notetaker."
hidden: true
---

# Fireflies.ai

<img src="../../.gitbook/assets/connectors/lg/firefliesai.png" alt="Fireflies.ai logo">

Fireflies.ai connector — GraphQL API (single POST https://api.fireflies.ai/graphql) for the AI meeting notetaker. Query and manage transcripts, summaries, analytics, soundbites (bites), users, user groups, channels, contacts, AskFred AI threads, live/active meetings, audit events, and automation rule executions; upload audio; and run live/meeting mutations. Auth via Bearer API key.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [fireflies.ai](https://fireflies.ai) |
| **Authentication** | Bearer token |
| **Slug** | `firefliesai` |

## Use it

Add Fireflies.ai from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.firefliesai.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Fireflies To Live Meeting | `addToLiveMeeting` | Send the Fireflies bot to join an ongoing meeting by its link. GraphQL: addToLiveMeeting(meeting_link). Rate limited to 3 requests / 20 minutes. |
| Continue AskFred Thread | `continueAskFredThread` | Ask a follow-up question in an existing AskFred thread. GraphQL: continueAskFredThread(input:{thread_id, query, response_language, format_mode}). |
| Create AskFred Thread | `createAskFredThread` | Start a new AskFred AI conversation asking a question about your meetings. GraphQL: createAskFredThread(input:{query, response_language, format_mode}). Optionally scope to one transcript in the Fireflies app. |
| Create Bite | `createBite` | Create a soundbite (clip) from a completed transcript between two timestamps (seconds). GraphQL: createBite(transcript_id, start_time, end_time). |
| Create Live Action Item | `createLiveActionItem` | Create an action item during a live meeting via a natural-language prompt. GraphQL: createLiveActionItem(input:{meeting_id, prompt}). 10 req/hour, requires AI credits. |
| Create Live Soundbite | `createLiveSoundbite` | Create a soundbite during a live meeting via a natural-language prompt. GraphQL: createLiveSoundbite(input:{meeting_id, prompt}). 10 req/hour, requires AI credits. |
| Delete AskFred Thread | `deleteAskFredThread` | Permanently delete an AskFred thread and its messages. GraphQL: deleteAskFredThread(id). Returns the deleted thread. |
| Delete Transcript | `deleteTranscript` | Delete a transcript by id (returns fields from the deleted transcript). GraphQL: deleteTranscript(id). 10 req/min; deleting others' meetings needs team-admin. |
| Get Analytics | `getAnalytics` | Team meeting analytics for a date range (ISO 8601). GraphQL: analytics(start_time, end_time). Requires a Business+ plan (returns paid_required otherwise). |
| Get AskFred Thread | `getAskFredThread` | Get one AskFred thread by id including all messages (query/answer/suggested_queries). GraphQL: askfred_thread(id). |
| Get Bite | `getBite` | Get one soundbite (bite) by id with captions, sources and origin. GraphQL: bite(id). |
| Get Channel | `getChannel` | Get a single channel by id with its members. GraphQL: channel(id). |
| Get Transcript | `getTranscript` | Get one transcript by id with full detail: sentences, summary, speakers, attendees, meeting_info, apps_preview, shared_with. GraphQL: transcript(id). |
| Get User | `getUser` | Get a single user by id. GraphQL: user(id). Omit-less: pass the user_id from List Users. |
| List Active Meetings | `listActiveMeetings` | List meetings currently in progress (active/paused) that the Fireflies bot is in. GraphQL: active_meetings. |
| List AI App Outputs | `listAppOutputs` | List AI App outputs generated from transcripts (paginated). GraphQL: apps(limit, skip). Optionally filter by app_id/transcript_id via the extra fields (only supplied ones are sent). |
| List AskFred Threads | `listAskFredThreads` | List AskFred AI conversation threads. GraphQL: askfred_threads. Returns thread summaries (no messages). |
| List Audit Events | `listAuditEvents` | List OCSF audit-log events for the team, filtered by category. GraphQL: auditEvents(limit, filters:{category}). category one of MEETING_OPERATIONS/TEAM_OPERATIONS/USER_OPERATIONS/AUTHENTICATION. Requires an Enterprise plan. |
| List Bites | `listBites` | List soundbites (bites). GraphQL: bites(mine). mine=true limits to the caller's bites. |
| List Channels | `listChannels` | List channels the caller can access. GraphQL: channels. |
| List Contacts | `listContacts` | List contacts derived from the caller's meetings. GraphQL: contacts. |
| List Live Action Items | `listLiveActionItems` | List AI-generated action items for a live meeting. GraphQL: live_action_items(meeting_id). Only valid while a meeting is live. |
| List Rule Executions By Meeting | `listRuleExecutionsByMeeting` | List automation-rule execution logs grouped by meeting. GraphQL: rule_executions_by_meeting(limit). Requires an Enterprise plan (returns paid_required otherwise). |
| List Transcripts | `listTranscripts` | List recent meeting transcripts (paginated). GraphQL: transcripts(limit, skip). Returns core transcript fields, speakers, summary highlights, meeting_info. |
| List Transcripts By Date Range | `listTranscriptsByDateRange` | List transcripts created between fromDate and toDate (ISO 8601, e.g. 2024-07-08T22:13:46.660Z). GraphQL: transcripts(fromDate, toDate, limit, skip). |
| List Transcripts By Host | `listTranscriptsByHost` | List transcripts where a given email is the meeting host. GraphQL: transcripts(host_email, limit, skip). |
| List Transcripts By Participant | `listTranscriptsByParticipant` | List transcripts that include a given email as a participant/attendee. GraphQL: transcripts(participants:[email], limit, skip). |
| List User Groups | `listUserGroups` | List user groups (teams within the workspace). GraphQL: user_groups(mine). mine=true limits to the caller's groups. |
| List Users | `listUsers` | List all users on the team/workspace. GraphQL: users. Returns user_id, name, email, admin flag, usage stats, groups. |
| Revoke Shared Meeting Access | `revokeSharedMeetingAccess` | Revoke a previously shared user's access to a meeting transcript. GraphQL: revokeSharedMeetingAccess(input:{meeting_id, email}). |
| Search Transcripts | `searchTranscripts` | Search transcripts by keyword within title/sentences/all. GraphQL: transcripts(keyword, scope, limit, skip). scope is a quoted string: title \| sentences \| all. |
| Set User Role | `setUserRole` | Set a team member's role to admin or user. GraphQL: setUserRole(user_id, role). Requires team-admin; cannot change your own role. |
| Share Meeting | `shareMeeting` | Share a meeting transcript externally with an email address. GraphQL: shareMeeting(input:{meeting_id, emails:[email]}). Up to 50 emails per request (this action sends one). |
| Update Meeting Channel | `updateMeetingChannel` | Move a meeting/transcript into a channel. GraphQL: updateMeetingChannel(input:{transcript_ids:[id], channel_id}). Returns updated transcripts (array). This action sends one transcript id. |
| Update Meeting Privacy | `updateMeetingPrivacy` | Set a meeting's privacy level. GraphQL: updateMeetingPrivacy(input:{id, privacy}). privacy one of link/owner/participants/teammatesandparticipants/teammates. |
| Update Meeting State | `updateMeetingState` | Pause or resume recording for a live meeting. GraphQL: updateMeetingState(input:{meeting_id, action}). action one of pause_recording/resume_recording. |
| Update Meeting Title | `updateMeetingTitle` | Rename a meeting/transcript. GraphQL: updateMeetingTitle(input:{title, id}). Title 5-256 chars; requires admin. |
| Upload Audio | `uploadAudio` | Queue an audio/video file (public URL) for transcription. GraphQL: uploadAudio(input:{url,title}). Requires a Pro+ plan (returns paid_required otherwise). Optional per-upload webhook/attendees are set in the Fireflies dashboard. |
