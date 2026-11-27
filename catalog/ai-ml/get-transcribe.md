---
description: "GetTranscribe transcribes videos from social platforms. Create transcription jobs, download videos, and organize transcriptions in folders."
hidden: true
---

# GetTranscribe

<img src="../../.gitbook/assets/connectors/lg/get-transcribe.png" alt="GetTranscribe logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [gettranscribe.ai](https://gettranscribe.ai) |
| **Authentication** | API key |
| **Slug** | `getTranscribe` |

## Setup

Your customers enter their API key for GetTranscribe when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect GetTranscribe from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **GetTranscribe**.
2. Select **Connect** on the GetTranscribe card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use GetTranscribe's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Folder</td><td><code>createFolder</code></td><td>Creates a new folder to organize transcriptions. Pass a parent folder id to create a subfolder, or omit it for a root-level folder. Returns the created folder record.</td></tr><tr><td>Create Transcription Job</td><td><code>createTranscriptionJob</code></td><td>Queues a new transcription job for a public video URL from Instagram, TikTok, YouTube, Facebook, X, Pinterest, Google Drive or a direct video file. Returns immediately with a pending job; poll Get Transcription Job until the status is completed, then load the transcript with Get Transcription using the returned transcription_id.</td></tr><tr><td>Delete Folder</td><td><code>deleteFolder</code></td><td>Soft-deletes a transcription folder by id and returns the folder record with deleted_at set. This route is verified live against the API but is not listed in the public documentation.</td></tr><tr><td>Delete Transcription</td><td><code>deleteTranscription</code></td><td>Soft-deletes a transcription by id and returns the full transcription record with deleted_at set. This route is verified live against the API but is not listed in the public documentation.</td></tr><tr><td>Delete Transcription Job</td><td><code>deleteTranscriptionJob</code></td><td>Soft-deletes a transcription job record by id and returns the job with deleted_at set. Deleting a job does not delete the transcription it produced. This route is verified live against the API but is not listed in the public documentation.</td></tr><tr><td>Download Video URL</td><td><code>downloadVideoUrl</code></td><td>Resolves a fresh, direct media download URL and thumbnail for a public video post from YouTube, Instagram, TikTok, Facebook, X, Pinterest, Google Drive or a direct file URL, without creating a transcription. The returned links are time-limited and expire; call again for a fresh link. Requires a wallet balance of at least 0.01 and records a small debit on success.</td></tr><tr><td>Get Folder</td><td><code>getFolder</code></td><td>Fetches a single transcription folder by id, including its name and optional parent folder. Only folders belonging to your account are returned.</td></tr><tr><td>Get Transcription</td><td><code>getTranscription</code></td><td>Retrieves a finished transcription by id, including the full transcript text, the raw unformatted text, timed segments and words, video metadata (platform, author, channel, title, duration) and time-limited audio and thumbnail download URLs. Use the transcription_id from a completed transcription job.</td></tr><tr><td>Get Transcription Job</td><td><code>getTranscriptionJob</code></td><td>Fetches a single transcription job by id. Use it to poll the status after Create Transcription Job; when the status is completed, transcription_id is set and the transcript can be loaded with Get Transcription. When failed, error_message and error_code explain the failure.</td></tr><tr><td>Get User Info</td><td><code>getUserInfo</code></td><td>Retrieves the connected GetTranscribe user account, including subscription plan and status, minute and message limits, current usage for the period, purchased balances and wallet balance. Uses the user id stored on the connection.</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Folders</td><td><code>listFolders</code></td><td>Lists your transcription folders with pagination and sorting, optionally filtered to the subfolders of a given parent. Returns a paginated envelope with total, limit, skip and the folder records.</td></tr><tr><td>List Transcription Jobs</td><td><code>listTranscriptionJobs</code></td><td>Lists the transcription jobs belonging to your account with pagination, sorting and optional status or id filters. Returns a paginated envelope with total, limit, skip and the job records. Completed jobs carry a transcription_id for Get Transcription.</td></tr><tr><td>List Transcriptions</td><td><code>listTranscriptions</code></td><td>Lists your transcriptions as a lightweight index with pagination, sorting and optional folder or platform filters. List rows do not include the transcript text or download URLs; use Get Transcription for the full record.</td></tr><tr><td>Update Folder</td><td><code>updateFolder</code></td><td>Updates a transcription folder's name and/or moves it under a different parent folder. Only the fields you pass are changed; pass parent_id as null to move the folder to the root level. Returns the updated folder record.</td></tr></tbody></table>

</details>

