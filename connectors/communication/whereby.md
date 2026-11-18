---
description: "Whereby Embedded is a video meeting API for embedding branded video rooms into your product."
hidden: true
---

# Whereby

<img src="../../.gitbook/assets/connectors/lg/whereby.png" alt="Whereby logo">

Whereby Embedded is a video meeting API for embedding branded video rooms into your product. Create and manage transient meeting rooms, retrieve cloud recordings, transcriptions and AI summaries with time-limited access links, customize room branding, and query quality and usage insights for rooms, sessions and participants.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [whereby.com](https://whereby.com) |
| **Authentication** | Bearer token |
| **Slug** | `whereby` |

## Use it

Add Whereby from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.whereby.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Delete Recordings | `bulkDeleteRecordings` | Permanently deletes multiple cloud recordings in a single request. Returns no content on success. |
| Bulk Delete Transcriptions | `bulkDeleteTranscriptions` | Permanently deletes multiple transcriptions in a single request. Returns no content on success. |
| Create Meeting | `createMeeting` | Creates a transient Whereby meeting room that is available from creation until one hour after the given end date, after which it is deleted automatically. Returns the room URL and meeting ID. |
| Create Summary | `createSummary` | Generates an AI summary of an existing transcription using the selected summary template. The summary is processed asynchronously. |
| Create Transcription | `createTranscription` | Starts generating a transcription from an existing cloud recording. The transcription is processed asynchronously. |
| Delete Meeting | `deleteMeeting` | Deletes a meeting by its meeting ID, making the room immediately unavailable. Returns no content on success. |
| Delete Recording | `deleteRecording` | Permanently deletes a single cloud recording by its recording ID. Returns no content on success. |
| Delete Summary | `deleteSummary` | Permanently deletes a single AI summary by its summary ID. Returns no content on success. |
| Delete Transcription | `deleteTranscription` | Permanently deletes a single transcription by its transcription ID. Returns no content on success. |
| Get Meeting | `getMeeting` | Retrieves a single meeting by its meeting ID. |

<details>

<summary>See 17 more actions</summary>

* **Get Recording** `getRecording`: Retrieves the metadata of a single cloud recording by its recording ID.
* **Get Recording Access Link** `getRecordingAccessLink`: Generates a time-limited download link for a cloud recording stored in Whereby-hosted storage.
* **Get Session Participant** `getSessionParticipant`: Retrieves detailed connection and quality insights for a single participant in a room session.
* **Get Summary** `getSummary`: Retrieves a single AI summary, including its generated content, by its summary ID.
* **Get Transcription** `getTranscription`: Retrieves the metadata of a single transcription by its transcription ID.
* **Get Transcription Access Link** `getTranscriptionAccessLink`: Generates a time-limited download link for a transcription stored in Whereby-hosted storage.
* **List Meetings** `listMeetings`: Retrieves a paginated list of the meetings that currently exist for your Whereby organization.
* **List Recordings** `listRecordings`: Retrieves a paginated list of cloud recordings stored for your Whereby organization, optionally filtered by room name.
* **List Room Insights** `listRoomInsights`: Retrieves usage and quality insights aggregated per room, optionally filtered by room name and creation date.
* **List Room Session Insights** `listRoomSessionInsights`: Retrieves insights for the individual sessions that took place in a room. A session starts once at least two participants are present.
* **List Session Participants** `listSessionParticipants`: Retrieves the participants of a room session, including when each participant joined and left.
* **List Summaries** `listSummaries`: Retrieves a paginated list of AI summaries generated for your Whereby organization.
* **List Transcriptions** `listTranscriptions`: Retrieves a paginated list of transcriptions for your Whereby organization, optionally filtered by room name.
* **Reset Room Logo** `resetRoomLogo`: Resets a room's logo to the organization default. Uploading a custom logo image is only supported through the Whereby Embedded dashboard. Returns no content on success.
* **Set Room Background** `setRoomBackground`: Sets a room's background to a predefined color palette and image. Uploading a custom background image is only supported through the Whereby Embedded dashboard. Returns no content on success.
* **Set Room Colors** `setRoomColors`: Sets the primary, secondary and focus colors of a room, or resets them to the organization defaults. Returns no content on success.
* **Set Room Knock Page Background** `setRoomKnockPageBackground`: Sets the background of a room's knock (waiting room) page to a predefined color palette and image. Uploading a custom image is only supported through the Whereby Embedded dashboard. Returns no content on success.

</details>
