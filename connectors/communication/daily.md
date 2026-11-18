---
description: "Daily is a real-time video and audio conferencing API."
hidden: true
---

# Daily

<img src="../../.gitbook/assets/connectors/lg/daily.png" alt="Daily logo">

Daily is a real-time video and audio conferencing API. Create and manage rooms, issue meeting tokens, control recordings, transcription and live streaming, inspect meetings, participants and presence, run dial-in and dial-out telephony, submit batch post-processing jobs, and manage webhooks.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [daily.co](https://daily.co) |
| **Authentication** | Bearer token |
| **Slug** | `daily` |

## Use it

Add Daily from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.daily.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Buy Phone Number | `buyPhoneNumber` | Purchase a phone number for dial-in on your Daily domain. Billing applies per number. |
| Create Dial-In Configuration | `createDomainDialConfigInfo` | Register a new dial-in configuration mapping a purchased phone number to a room creation flow. |
| Create Meeting Token | `createMeetingToken` | Create a meeting token granting a participant access to a room, with optional owner rights, identity, and expiry. |
| Create Room | `createRoom` | Create a video call room with optional privacy and room properties. |
| Create Rooms In Batch | `batchRoomCreate` | Create up to 500 rooms in a single request. Returns the created rooms and any per-room errors. |
| Create Webhook | `createWebhook` | Register a webhook endpoint to receive Daily event notifications. |
| Delete Batch Processor Job | `deleteBatchProcessorJob` | Delete a batch processor job and any output objects stored in Daily's bucket. Objects in a custom bucket are not deleted. |
| Delete Dial-In Configuration | `deleteDomainDialinConfig` | Delete a dial-in configuration by its identifier. |
| Delete Recording | `deleteRecording` | Delete a cloud recording and its stored media by identifier. |
| Delete Room | `deleteRoom` | Delete a room by name. Participants currently in the room are disconnected. |
| Delete Rooms In Batch | `batchRoomDelete` | Delete multiple rooms in a single request by room name. |
| Delete Transcript | `deleteTranscript` | Delete a stored transcript by its identifier. |
| Delete Webhook | `deleteWebhook` | Delete a webhook endpoint by its identifier. |
| Eject Participants | `eject` | Remove participants from a room by session ID or user ID, optionally banning them. |
| Get Batch Processor Job | `getBatchProcessorJob` | Retrieve a batch processor job by ID, including its input, output, and status. |
| Get Batch Processor Job Download Link | `getBatchProcessorJobAccessLink` | Create download links for the outputs of a finished batch processor job. Returns 400 if the job is not finished. |
| Get Dial-In Configuration | `getDomainDialinConfigInfo` | Retrieve a single dial-in configuration by its identifier. |
| Get Domain Configuration | `getDomainConfig` | Retrieve the configuration and default settings for your Daily domain. |
| Get Domain Presence | `getPresence` | Retrieve the participants currently present in every room on your domain. |
| Get Meeting Session | `getIndividualMeetingInfo` | Retrieve a single meeting session, including its participants, by session identifier. |
| Get Recording | `getRecordingInfo` | Retrieve metadata for a single cloud recording by its identifier. |
| Get Recording Download Link | `getRecordingLink` | Create a time-limited download link for a finished cloud recording. |
| Get Room | `getRoomConfig` | Retrieve a single room and its configuration by room name. |
| Get Room Presence | `getRoomPresence` | Retrieve the participants currently present in a specific room. |
| Get Session Data | `getSessionData` | Retrieve the shared session data object associated with a room's current meeting session. |
| Get Transcript | `getTranscriptInfo` | Retrieve metadata for a single stored transcript by its identifier. |
| Get Transcript Download Link | `getTranscriptLink` | Create a time-limited download link for a stored transcript. |
| Get Webhook | `getWebhookConfig` | Retrieve a single webhook configuration by its identifier. |
| List API Logs | `listAPILogs` | Retrieve a log of REST API requests made against your Daily domain. |
| List Available Phone Numbers | `listAvailableNumbers` | Search phone numbers that are available to purchase, filtered by area code, region, city, or pattern. |
| List Batch Processor Jobs | `listBatchProcessorJobs` | List post-processing jobs submitted to the batch processor, optionally filtered by recording. |
| List Dial-In Configurations | `listDomainDialinConfigs` | List the dial-in (pinless or PIN) configurations registered on your domain. |
| List Meeting Participants | `getMeetingParticipants` | List the participants of a meeting session, with their join and leave times. |
| List Meeting Sessions | `getMeetingInfo` | List meeting sessions on your domain, filtered by room, time range, or ongoing status. |
| List Purchased Phone Numbers | `purchasedPhoneNumbers` | List the phone numbers currently purchased on your Daily domain. |
| List Recordings | `listRecordings` | List cloud recordings on your domain, optionally filtered by room name. |
| List Rooms | `listRooms` | List the rooms on your Daily domain with cursor-based pagination. |
| List Session Logs | `listLogs` | Retrieve call quality logs and metrics for meeting sessions. You must supply at least one of userSessionId or mtgSessionId; the API returns 400 if both are omitted. |
| List Transcripts | `listTranscript` | List stored transcripts on your domain, optionally filtered by room or meeting session. |
| List Webhooks | `getWebhooks` | List the webhook endpoints configured on your Daily domain. |
| Refer SIP Call | `roomSipRefer` | Issue a SIP REFER to hand off an active SIP call to another endpoint. |
| Release Phone Number | `releasePhoneNumber` | Release a purchased phone number, stopping billing and removing it from your domain. |
| Send App Message | `sendAppMessage` | Broadcast an application message to participants in a room's active session. |
| Send DTMF Tones | `roomDialOutSendDTMF` | Send DTMF tones into an active dial-out session, for navigating phone menus. |
| Set Session Data | `setSessionData` | Set or merge the shared session data object for a room's current meeting session. |
| Start Dial-Out | `roomDialOutStart` | Dial out from a room to a phone number or SIP endpoint and add the callee to the call. Billed per minute. |
| Start Live Stream | `roomLivestreamingStart` | Start an RTMP live stream from a room to one or more streaming endpoints. Billed per minute. |
| Start Recording | `roomRecordingsStart` | Start a cloud recording of a room's active meeting session. Billed per minute. |
| Start Transcription | `roomTranscriptionStart` | Start live transcription of a room's active meeting session. Billed per minute. |
| Stop Dial-Out | `roomDialOutStop` | End an active dial-out session in a room. |
| Stop Live Stream | `roomLivestreamingStop` | Stop an active live stream in a room. |
| Stop Recording | `roomRecordingsStop` | Stop an active cloud recording in a room. |
| Stop Transcription | `roomTranscriptionStop` | Stop an active live transcription in a room. |
| Submit Batch Processor Job | `submitBatchProcessorJob` | Submit a post-processing job (transcript or summary) for a recording or media URL. Requires a paid Daily plan. |
| Transfer SIP Call | `roomSipCallTransfer` | Transfer an active SIP or PSTN call in a room to another endpoint. |
| Update Dial-In Configuration | `updateDomainDialConfigInfo` | Update an existing dial-in configuration. |
| Update Domain Configuration | `setDomainConfig` | Update domain-wide default settings that apply to every room on your Daily domain. |
| Update Live Stream | `roomLivestreamingUpdate` | Update the layout or settings of an active live stream. |
| Update Participant Permissions | `updatePermissions` | Update the permissions of participants in a room's active meeting session. |
| Update Pinless Dial-In Call | `pinlessCallUpdate` | Route an inbound pinless dial-in call to a SIP URI once the room is ready. |
| Update Recording | `roomRecordingsUpdate` | Update the layout or settings of an active cloud recording. |
| Update Room | `setRoomConfig` | Update the privacy or properties of an existing room. |
| Update Transcription | `roomTranscriptionUpdate` | Update which participants are included in an active live transcription. |
| Update Webhook | `updateWebhookConfig` | Update the URL, event types, or authentication of an existing webhook. |
| Validate Meeting Token | `validateMeetingToken` | Validate a meeting token and return the properties encoded within it. |
