---
description: "Whereby provides embeddable video meetings. Create and delete meetings, and manage recordings, transcriptions and summaries."
hidden: true
---

# Whereby

<img src="../../.gitbook/assets/connectors/lg/whereby.png" alt="Whereby logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [whereby.com](https://whereby.com) |
| **Authentication** | Access token |
| **Slug** | `whereby` |

## Setup

Your customers enter their access token for Whereby when they connect. Nothing else needs setting up.

## Use it

Add Whereby from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.whereby.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Bulk Delete Recordings</td><td><code>bulkDeleteRecordings</code></td><td>Permanently deletes multiple cloud recordings in a single request. Returns no content on success.</td></tr><tr><td>Bulk Delete Transcriptions</td><td><code>bulkDeleteTranscriptions</code></td><td>Permanently deletes multiple transcriptions in a single request. Returns no content on success.</td></tr><tr><td>Create Meeting</td><td><code>createMeeting</code></td><td>Creates a transient Whereby meeting room that is available from creation until one hour after the given end date, after which it is deleted automatically. Returns the room URL and meeting ID.</td></tr><tr><td>Create Summary</td><td><code>createSummary</code></td><td>Generates an AI summary of an existing transcription using the selected summary template. The summary is processed asynchronously.</td></tr><tr><td>Create Transcription</td><td><code>createTranscription</code></td><td>Starts generating a transcription from an existing cloud recording. The transcription is processed asynchronously.</td></tr><tr><td>Delete Meeting</td><td><code>deleteMeeting</code></td><td>Deletes a meeting by its meeting ID, making the room immediately unavailable. Returns no content on success.</td></tr><tr><td>Delete Recording</td><td><code>deleteRecording</code></td><td>Permanently deletes a single cloud recording by its recording ID. Returns no content on success.</td></tr><tr><td>Delete Summary</td><td><code>deleteSummary</code></td><td>Permanently deletes a single AI summary by its summary ID. Returns no content on success.</td></tr><tr><td>Delete Transcription</td><td><code>deleteTranscription</code></td><td>Permanently deletes a single transcription by its transcription ID. Returns no content on success.</td></tr><tr><td>Get Meeting</td><td><code>getMeeting</code></td><td>Retrieves a single meeting by its meeting ID.</td></tr></tbody></table>

<details>

<summary>View 17 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Recording</td><td><code>getRecording</code></td><td>Retrieves the metadata of a single cloud recording by its recording ID.</td></tr><tr><td>Get Recording Access Link</td><td><code>getRecordingAccessLink</code></td><td>Generates a time-limited download link for a cloud recording stored in Whereby-hosted storage.</td></tr><tr><td>Get Session Participant</td><td><code>getSessionParticipant</code></td><td>Retrieves detailed connection and quality insights for a single participant in a room session.</td></tr><tr><td>Get Summary</td><td><code>getSummary</code></td><td>Retrieves a single AI summary, including its generated content, by its summary ID.</td></tr><tr><td>Get Transcription</td><td><code>getTranscription</code></td><td>Retrieves the metadata of a single transcription by its transcription ID.</td></tr><tr><td>Get Transcription Access Link</td><td><code>getTranscriptionAccessLink</code></td><td>Generates a time-limited download link for a transcription stored in Whereby-hosted storage.</td></tr><tr><td>List Meetings</td><td><code>listMeetings</code></td><td>Retrieves a paginated list of the meetings that currently exist for your Whereby organization.</td></tr><tr><td>List Recordings</td><td><code>listRecordings</code></td><td>Retrieves a paginated list of cloud recordings stored for your Whereby organization, optionally filtered by room name.</td></tr><tr><td>List Room Insights</td><td><code>listRoomInsights</code></td><td>Retrieves usage and quality insights aggregated per room, optionally filtered by room name and creation date.</td></tr><tr><td>List Room Session Insights</td><td><code>listRoomSessionInsights</code></td><td>Retrieves insights for the individual sessions that took place in a room. A session starts once at least two participants are present.</td></tr><tr><td>List Session Participants</td><td><code>listSessionParticipants</code></td><td>Retrieves the participants of a room session, including when each participant joined and left.</td></tr><tr><td>List Summaries</td><td><code>listSummaries</code></td><td>Retrieves a paginated list of AI summaries generated for your Whereby organization.</td></tr><tr><td>List Transcriptions</td><td><code>listTranscriptions</code></td><td>Retrieves a paginated list of transcriptions for your Whereby organization, optionally filtered by room name.</td></tr><tr><td>Reset Room Logo</td><td><code>resetRoomLogo</code></td><td>Resets a room's logo to the organization default. Uploading a custom logo image is only supported through the Whereby Embedded dashboard. Returns no content on success.</td></tr><tr><td>Set Room Background</td><td><code>setRoomBackground</code></td><td>Sets a room's background to a predefined color palette and image. Uploading a custom background image is only supported through the Whereby Embedded dashboard. Returns no content on success.</td></tr><tr><td>Set Room Colors</td><td><code>setRoomColors</code></td><td>Sets the primary, secondary and focus colors of a room, or resets them to the organization defaults. Returns no content on success.</td></tr><tr><td>Set Room Knock Page Background</td><td><code>setRoomKnockPageBackground</code></td><td>Sets the background of a room's knock (waiting room) page to a predefined color palette and image. Uploading a custom image is only supported through the Whereby Embedded dashboard. Returns no content on success.</td></tr></tbody></table>

</details>

## Events

Whereby has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
