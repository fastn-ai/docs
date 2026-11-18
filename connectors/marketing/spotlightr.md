---
description: "Spotlightr (formerly vooPlayer) interactive video hosting and marketing platform."
hidden: true
---

# Spotlightr

Spotlightr (formerly vooPlayer) interactive video hosting and marketing platform. Create videos from a URL or upload, organise them into projects, replace video sources, delete videos, read per-video analytics and viewer-level view records, list top-performing videos, manage whitelisted embed domains, and create course/gallery students.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [spotlightr.com](https://spotlightr.com) |
| **Authentication** | API key |
| **Actions** | 19 |
| **Events** | 2 |
| **Slug** | `spotlightr` |

## Use it

Add Spotlightr from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.spotlightr.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Whitelisted Domain | `addWhitelistedDomain` | Whitelists a domain so your Spotlightr videos may be embedded on it. Returns an empty 200 body, so confirm with List Whitelisted Domains afterwards. |
| Create Course Student | `createCourseStudents` | Creates a student record for your Spotlightr courses and galleries and returns the new student's numeric ID. IMPORTANT: Spotlightr's published documentation describes this as POST /spotlight/students taking email, password and quantity. That route is gone - it returns the host's route-not-found page - and the live route POST /student rejects email, name and quantity with "Column &lt;x&gt; does not exists in Student table." The real columns, confirmed by creating a record and reading it back, are userID, id, created, customViewerID, data, progress and password. SECURITY: List Course Students returns the password column in clear text, so do not store a real secret here. |
| Create Project | `createProject` | Creates a new project (video group) to organise videos in. Returns the numeric ID of the new project as a bare value. |
| Create Video From Link | `createVideo` | Creates a new Spotlightr video from an external link (YouTube, Vimeo, Google Drive, Dropbox or a direct file URL). Returns the numeric ID of the new video as a bare value. Note: direct .mp4 URLs were observed to return HTTP 500 from Spotlightr while platform links (YouTube etc.) succeed. File upload is not supported by this action - the vendor's file variant needs a binary multipart part, which the fastn engine cannot send. |
| Delete Course Student | `deleteCourseStudent` | Deletes a Spotlightr course or gallery student by numeric ID. KNOWN LIMITATION: this route is live but belongs to Spotlightr's app session-token auth family, not the API-key family. With an API key it always answers 401 "Missing token or parameter id." - id was supplied in the query string and in the form body with the same result. Removing a student currently has to be done in the Spotlightr web app. The action is shipped so it works if Spotlightr extends API-key auth to this route. |
| Delete Project | `deleteProject` | Deletes a Spotlightr project (video group) by numeric ID. KNOWN LIMITATION: this route is live but belongs to Spotlightr's app session-token auth family, not the API-key family. With an API key it always answers 401 "Missing token or parameter id." - id was supplied in the query string and in the form body, and vooKey in the body, with the same result. Deleting a project currently has to be done in the Spotlightr web app. The action is shipped so it works if Spotlightr extends API-key auth to this route. |
| Delete Videos | `deleteVideo` | Permanently deletes one or more videos from your Spotlightr account by numeric ID. Spotlightr returns HTTP 200 with an empty body whether or not the IDs existed, so always confirm the removal with List Videos afterwards. |
| Get Top Videos | `getTopVideos` | Returns your best-performing videos over a reporting window, as an array ordered by engagement. Use days to set the window (default 30) and total to set how many videos to return (default 3). |
| Get Video Metrics | `getVideoMetrics` | Returns aggregate analytics for one video: loads, average percent watched, plays, play rate, completion rate and share count. SECURITY WARNING: this Spotlightr endpoint performs no authentication and no ownership check - it answers for any video ID on the platform, including other customers' videos, and returns fabricated numbers for a non-numeric ID. Treat its output as untrusted and never expose the videoID input to end users. |
| List Course Students | `listCourseStudents` | Returns the students enrolled in your Spotlightr courses and galleries as an array. This route is not in Spotlightr's published documentation but is live on the API. |
| List Playlists | `listPlaylists` | Returns the playlists in your Spotlightr account in a paginated envelope under "playlists". This route is not in Spotlightr's published documentation but is live on the API. |
| List Projects | `listProjects` | Returns every project (video group) in your Spotlightr account as a flat array, including the built-in Uncategorized project with id 0. Each entry carries id, name, userID, numberOfVideos, created, updated, theme, archived, numberOfSeconds and numberOfGB. |
| List Projects Paginated | `listProjectsPaginated` | Returns your Spotlightr projects in a paginated envelope with total, per_page, current_page, last_page and a data array of id/name/created. This route is not in Spotlightr's published documentation but is live on the API. Unlike List Projects it omits the built-in Uncategorized project and the per-project usage counters. |
| List Subscription Plans | `listSubscriptionPlans` | Returns Spotlightr's catalogue of subscription plans with pricing, storage and bandwidth allowances, team seats, transcription minutes and the marketing benefit list for each tier. This route is not in Spotlightr's published documentation but is live on the API. |
| List Video Views | `listVideoViews` | Returns individual viewer sessions for one video as a paginated list, plus a summary with total watch time. Filter to a known viewer with customViewerID, restrict to sessions with more than 1 percent watched using onlyWatched, or disable pagination with allViews. SECURITY WARNING: this Spotlightr endpoint performs no authentication and no ownership check - it answers for any video ID on the platform. |
| List Videos | `listVideos` | Lists the videos in your Spotlightr account. Returns a paginated envelope under "videos" containing total, per_page, current_page, last_page and a data array of video objects. Optionally narrow the result to a single video with videoID, or to one project with videoGroup. |
| List Whitelisted Domains | `listWhitelistedDomains` | Returns the list of domains whitelisted for embedding your Spotlightr videos, as an array of domain strings. |
| Remove Whitelisted Domain | `removeWhitelistedDomain` | Removes a domain from the embed whitelist. This route is not in Spotlightr's published documentation but is live on the API. It returns an empty 200 body whether or not the domain was present, so confirm with List Whitelisted Domains afterwards. |
| Replace Video Source | `setVideoSource` | Points an existing Spotlightr video at a new source URL, keeping the same video ID, player settings and embed code. Spotlightr implements this as a GET and returns an empty 200 body, so confirm the change with List Videos afterwards. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Lead Opt-In Submitted | `optin` | Fires when a viewer submits an opt-in / lead-capture overlay on one of your Spotlightr videos. REGISTRATION IS UI-ONLY - Spotlightr exposes no webhook registration API (GET/POST /webhooks and /api/webhooks both return the host's route-not-found page). A human must register the endpoint once: open the Spotlightr app, go to App Settings &gt; Integrations, add a custom webhook integration and paste the fastn trigger URL as the endpoint. Spotlightr then posts opt-in and watching data to it. PAYLOAD SCHEMA IS MODELLED from Spotlightr's help-centre description, NOT captured from a real delivery - no delivery could be captured because registration requires a browser login. Reconcile the schema against the first real delivery. |
| Video Watched Threshold Reached | `watched` | Fires when a viewer reaches the watched threshold configured on a video. REGISTRATION IS UI-ONLY AND TWO-STEP. First, a human registers the endpoint: Spotlightr app &gt; App Settings &gt; Integrations &gt; add a custom webhook integration and paste the fastn trigger URL. Second, the notification must be enabled per video: edit the video &gt; Settings tab &gt; Advanced Options &gt; Watched Email Notification &gt; enable the switch, then click the gear icon and select the webhook integration created in step one. Spotlightr exposes no API for either step. PAYLOAD SCHEMA IS MODELLED from Spotlightr's help-centre description, NOT captured from a real delivery. Reconcile it against the first real delivery. |
