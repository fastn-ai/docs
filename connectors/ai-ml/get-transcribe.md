---
description: "GetTranscribe transcribes and analyzes social videos from Instagram, TikTok, YouTube, Facebook, X, Pinterest, Google Drive and direct video URLs."
hidden: true
---

# GetTranscribe

<img src="../../.gitbook/assets/connectors/lg/get-transcribe.png" alt="GetTranscribe logo">

GetTranscribe transcribes and analyzes social videos from Instagram, TikTok, YouTube, Facebook, X, Pinterest, Google Drive and direct video URLs. This connector covers the full GetTranscribe REST API: asynchronous transcription jobs (create, poll, list), finished transcriptions with word-level timing and media URLs, direct video download URL resolution, folder organization, and account and usage information.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [gettranscribe.ai](https://gettranscribe.ai) |
| **Authentication** | Credentials you enter |
| **Slug** | `getTranscribe` |

## Use it

Add GetTranscribe from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.getTranscribe.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Folder | `createFolder` | Creates a new folder to organize transcriptions. Pass a parent folder id to create a subfolder, or omit it for a root-level folder. Returns the created folder record. |
| Create Transcription Job | `createTranscriptionJob` | Queues a new transcription job for a public video URL from Instagram, TikTok, YouTube, Facebook, X, Pinterest, Google Drive or a direct video file. Returns immediately with a pending job; poll Get Transcription Job until the status is completed, then load the transcript with Get Transcription using the returned transcription_id. |
| Delete Folder | `deleteFolder` | Soft-deletes a transcription folder by id and returns the folder record with deleted_at set. This route is verified live against the API but is not listed in the public documentation. |
| Delete Transcription | `deleteTranscription` | Soft-deletes a transcription by id and returns the full transcription record with deleted_at set. This route is verified live against the API but is not listed in the public documentation. |
| Delete Transcription Job | `deleteTranscriptionJob` | Soft-deletes a transcription job record by id and returns the job with deleted_at set. Deleting a job does not delete the transcription it produced. This route is verified live against the API but is not listed in the public documentation. |
| Download Video URL | `downloadVideoUrl` | Resolves a fresh, direct media download URL and thumbnail for a public video post from YouTube, Instagram, TikTok, Facebook, X, Pinterest, Google Drive or a direct file URL, without creating a transcription. The returned links are time-limited and expire; call again for a fresh link. Requires a wallet balance of at least 0.01 and records a small debit on success. |
| Get Folder | `getFolder` | Fetches a single transcription folder by id, including its name and optional parent folder. Only folders belonging to your account are returned. |
| Get Transcription | `getTranscription` | Retrieves a finished transcription by id, including the full transcript text, the raw unformatted text, timed segments and words, video metadata (platform, author, channel, title, duration) and time-limited audio and thumbnail download URLs. Use the transcription_id from a completed transcription job. |
| Get Transcription Job | `getTranscriptionJob` | Fetches a single transcription job by id. Use it to poll the status after Create Transcription Job; when the status is completed, transcription_id is set and the transcript can be loaded with Get Transcription. When failed, error_message and error_code explain the failure. |
| Get User Info | `getUserInfo` | Retrieves the connected GetTranscribe user account, including subscription plan and status, minute and message limits, current usage for the period, purchased balances and wallet balance. Uses the user id stored on the connection. |

<details>

<summary>See 4 more actions</summary>

* **List Folders** `listFolders`: Lists your transcription folders with pagination and sorting, optionally filtered to the subfolders of a given parent. Returns a paginated envelope with total, limit, skip and the folder records.
* **List Transcription Jobs** `listTranscriptionJobs`: Lists the transcription jobs belonging to your account with pagination, sorting and optional status or id filters. Returns a paginated envelope with total, limit, skip and the job records. Completed jobs carry a transcription_id for Get Transcription.
* **List Transcriptions** `listTranscriptions`: Lists your transcriptions as a lightweight index with pagination, sorting and optional folder or platform filters. List rows do not include the transcript text or download URLs; use Get Transcription for the full record.
* **Update Folder** `updateFolder`: Updates a transcription folder's name and/or moves it under a different parent folder. Only the fields you pass are changed; pass parent_id as null to move the folder to the root level. Returns the updated folder record.

</details>
