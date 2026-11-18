---
description: "Google Meet REST API v2 connector (https://meet.googleapis.com/v2)."
hidden: true
---

# Google Meet

<img src="../../.gitbook/assets/connectors/google-meet.png" alt="Google Meet logo" width="64">

Google Meet REST API v2 connector (https://meet.googleapis.com/v2). Create and manage meeting spaces, end active conferences, and read conference records, participants, participant sessions, recordings, transcripts, and transcript entries. Also manages Google Workspace Events API subscriptions (https://workspaceevents.googleapis.com/v1) for Meet conference and participant events delivered to a Cloud Pub/Sub topic. OAuth 2.0 (Google) authorization-code auth.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [meet.google.com](https://meet.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleMeet` |

## Use it

Add Google Meet from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleMeet.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Connect to Active Conference (Media API) | `connectActiveConference` | Starts a Google Meet Media API session for a meeting that is in progress (spaces.connectActiveConference, Meet REST v2beta). Sends the client's WebRTC SDP offer and returns Google's SDP answer, which a WebRTC client uses to receive the meeting's live audio and/or video streams (e.g. for a meeting assistant producing live transcripts). A successful answer means Google accepted the media connection request; the media itself then flows over WebRTC. Requires a conference currently running in the space and a Cloud project enrolled in the Meet Media API developer preview. Google scopes (one of): meetings.conference.media.readonly (audio + video), meetings.conference.media.audio.readonly (audio only), meetings.conference.media.video.readonly (video only). |
| Create Space | `createSpace` | Create a meeting space (a virtual location or persistent object used to host Google Meet conferences). Returns the space with its meetingUri and meetingCode. POST https://meet.googleapis.com/v2/spaces. Requires scope meetings.space.created. |
| Create Subscription | `createSubscription` | Create a Google Workspace Events API subscription so Meet events for a target resource (a Meet space) are delivered to a Cloud Pub/Sub topic. POST https://workspaceevents.googleapis.com/v1/subscriptions. The Pub/Sub topic must exist in the same Cloud project and grant publish rights to the Workspace Events service agent. eventTypes use the google.workspace.meet.* CloudEvents format; targetResource is //meet.googleapis.com/spaces/{space}. Requires the relevant Meet OAuth scope(s) for the requested event types. |
| Delete Subscription | `deleteSubscription` | Delete a Workspace Events subscription. DELETE https://workspaceevents.googleapis.com/v1/subscriptions/{subscription}. Returns a long-running operation; on completion the subscription is removed. |
| End Active Conference | `endActiveConference` | End the active conference (if any) currently being held in the given meeting space. POST https://meet.googleapis.com/v2/spaces/{space}:endActiveConference. Returns an empty body on success. Requires scope meetings.space.created. |
| Get Conference Record | `getConferenceRecord` | Get a conference record (a single instance of a meeting held in a space) by its conference id. GET https://meet.googleapis.com/v2/conferenceRecords/{conferenceRecord}. Requires scope meetings.space.created or meetings.space.readonly. |
| Get Participant | `getParticipant` | Get a participant of a conference record by participant id. GET https://meet.googleapis.com/v2/conferenceRecords/{conferenceRecord}/participants/{participant}. Requires scope meetings.space.created or meetings.space.readonly. |
| Get Participant Session | `getParticipantSession` | Get a participant session by id. A participant session is one device-join interval of a participant. GET https://meet.googleapis.com/v2/conferenceRecords/{conferenceRecord}/participants/{participant}/participantSessions/{participantSession}. Requires scope meetings.space.created or meetings.space.readonly. |
| Get Recording | `getRecording` | Get a recording of a conference record by id. GET https://meet.googleapis.com/v2/conferenceRecords/{conferenceRecord}/recordings/{recording}. Returns the recording metadata including the Drive file destination. Requires scope meetings.space.created or meetings.space.readonly. |
| Get Space | `getSpace` | Get details about a meeting space by name or meetingCode. GET https://meet.googleapis.com/v2/spaces/{space}. The {space} path segment accepts either the space id, the meetingCode, or a full resource name segment. Requires scope meetings.space.created or meetings.space.readonly. |

<details>

<summary>See 13 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Subscription | `getSubscription` | Get details about a Workspace Events subscription by id. GET https://workspaceevents.googleapis.com/v1/subscriptions/{subscription}. |
| Get Transcript | `getTranscript` | Get a transcript of a conference record by id. GET https://meet.googleapis.com/v2/conferenceRecords/{conferenceRecord}/transcripts/{transcript}. Returns transcript metadata including the Google Docs destination. Requires scope meetings.space.created or meetings.space.readonly. |
| Get Transcript Entry | `getTranscriptEntry` | Get a transcript entry (one segment of transcribed speech by a participant) by id. GET https://meet.googleapis.com/v2/conferenceRecords/{conferenceRecord}/transcripts/{transcript}/entries/{entry}. Requires scope meetings.space.created or meetings.space.readonly. |
| List Conference Records | `listConferenceRecords` | List the conference records for conferences the user is a participant in or the host of. GET https://meet.googleapis.com/v2/conferenceRecords. Ordered by start time descending. Supports filter (e.g. space.meeting_code, space.name, start_time, end_time). Requires scope meetings.space.created or meetings.space.readonly. |
| List Participant Sessions | `listParticipantSessions` | List the participant sessions of a participant in a conference record. GET https://meet.googleapis.com/v2/conferenceRecords/{conferenceRecord}/participants/{participant}/participantSessions. Ordered by start time ascending. Requires scope meetings.space.created or meetings.space.readonly. |
| List Participants | `listParticipants` | List the participants in a conference record. GET https://meet.googleapis.com/v2/conferenceRecords/{conferenceRecord}/participants. Ordered by join time ascending. Supports filter on earliest_start_time and latest_end_time. Requires scope meetings.space.created or meetings.space.readonly. |
| List Recordings | `listRecordings` | List the recordings of a conference record. GET https://meet.googleapis.com/v2/conferenceRecords/{conferenceRecord}/recordings. Ordered by start time ascending. Requires scope meetings.space.created or meetings.space.readonly. |
| List Subscriptions | `listSubscriptions` | List Workspace Events subscriptions created by the calling app for the authenticated user. GET https://workspaceevents.googleapis.com/v1/subscriptions. A filter is REQUIRED (e.g. event_types:"google.workspace.meet.conference.v2.started" OR target_resource="//meet.googleapis.com/spaces/{space}"). |
| List Transcript Entries | `listTranscriptEntries` | List the transcript entries of a transcript. GET https://meet.googleapis.com/v2/conferenceRecords/{conferenceRecord}/transcripts/{transcript}/entries. Ordered by start time ascending. Note: Google does not guarantee transcript entry ordering or completeness. Requires scope meetings.space.created or meetings.space.readonly. |
| List Transcripts | `listTranscripts` | List the transcripts of a conference record. GET https://meet.googleapis.com/v2/conferenceRecords/{conferenceRecord}/transcripts. Ordered by start time ascending. Requires scope meetings.space.created or meetings.space.readonly. |
| Reactivate Subscription | `reactivateSubscription` | Reactivate a suspended Workspace Events subscription. POST https://workspaceevents.googleapis.com/v1/subscriptions/{subscription}:reactivate. Only works if the subscription is in the SUSPENDED state and not past its expiration. Returns a long-running operation. |
| Update Space | `updateSpace` | Update details about a meeting space (its config). PATCH https://meet.googleapis.com/v2/spaces/{space}. Pass updateMask as a query param listing the config fields to update (e.g. config.moderation,config.accessType). Requires scope meetings.space.settings. |
| Update Subscription | `updateSubscription` | Update a Workspace Events subscription (e.g. its eventTypes, payloadOptions, or ttl). PATCH https://workspaceevents.googleapis.com/v1/subscriptions/{subscription}. updateMask lists the fields to change. targetResource and notificationEndpoint.pubsubTopic are immutable. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Conference Ended | `google.workspace.meet.conference.v2.ended` | An active conference in a subscribed Meet space ends. Delivered via Cloud Pub/Sub. The data payload contains the conferenceRecord resource including endTime. |
| Conference Started | `google.workspace.meet.conference.v2.started` | A new conference is started in a subscribed Meet space. Delivered via Cloud Pub/Sub as a CloudEvent. The data payload contains the conferenceRecord resource (name = conferenceRecords/{conferenceRecord}). |
| Participant Joined | `google.workspace.meet.participant.v2.joined` | A participant joins a conference in a subscribed Meet space. Delivered via Cloud Pub/Sub. The data payload contains the participantSession and/or participant resource. |
| Participant Left | `google.workspace.meet.participant.v2.left` | A participant leaves a conference in a subscribed Meet space. Delivered via Cloud Pub/Sub. The data payload contains the participantSession with endTime. |
