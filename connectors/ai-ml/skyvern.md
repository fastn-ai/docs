---
description: "Skyvern AI browser automation."
hidden: true
---

# Skyvern

<img src="../../.gitbook/assets/connectors/lg/skyvern.png" alt="Skyvern logo">

Skyvern AI browser automation. Run natural-language browser tasks and agents, manage workflows/agents, runs, schedules, browser sessions and browser profiles, credentials and TOTP, scripts, folders, tags, artifacts and files through the Skyvern Cloud REST API (https://api.skyvern.com).

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [skyvern.com](https://skyvern.com) |
| **Authentication** | API key |
| **Slug** | `skyvern` |

## Use it

Add Skyvern from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.skyvern.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Apply Agent Tags | `applyAgentTags` | Add or remove tags on a Skyvern agent (workflow). |
| Apply Run Tags | `applyRunTags` | Add or remove tags on a Skyvern workflow run. Tags are key:value strings used to group and filter runs. |
| Apply To Job | `applyToJob` | Fill in and SUBMIT a real job application on the employer's site using a resume URL and optional login. This sends real data to a real company - only run it for an application you intend to send. |
| Batch Get Agent Tags | `batchGetAgentTags` | Fetch the tags of several Skyvern agents in one GET, passing a comma-separated list of agent permanent ids. |
| Batch Get Agent Tags By Body | `batchGetAgentTagsPost` | Fetch the tags of many Skyvern agents by POSTing the id list in the body. Use this instead of the GET form when the list is too long for a URL. |
| Batch Get Run Tags | `batchGetRunTags` | Fetch the tags of several Skyvern workflow runs in one GET, passing a comma-separated list of run ids. |
| Batch Get Run Tags By Body | `batchGetRunTagsPost` | Fetch the tags of many Skyvern workflow runs by POSTing the id list in the body. Use this instead of the GET form when the list is too long for a URL. |
| Bulk Cancel Runs | `bulkCancelRuns` | Cancel several Skyvern runs in one call by passing a list of run ids. Returns per-run cancellation results. |
| Buy Credit Pack | `buyCreditPack` | Purchase additional Skyvern credit packs for the organization. SPENDS REAL MONEY on the card on file - only run this when a top-up is genuinely intended. |
| Cancel Run | `cancelRun` | Cancel a queued or running Skyvern run by id, stopping the browser session and any further credit spend. |

<details>

<summary>See 138 more actions</summary>

* **Cancel Task (Legacy API)** `cancelTaskLegacy`: Cancel a running task through Skyvern's original /api/v1 task API, stopping the browser and further credit spend.
* **Cancel Workflow Run (Legacy API)** `cancelWorkflowRunLegacy`: Cancel a running workflow run through Skyvern's original /api/v1 workflow API, stopping the browser and further credit spend.
* **Change Plan Tier** `changePlanTier`: Move the Skyvern organization to a different subscription tier. CHANGES RECURRING BILLING and can charge the card on file immediately - only run this when a plan change is genuinely intended.
* **Check Server Health** `checkServerHealth`: Liveness probe for the Skyvern API. Returns a plain-text confirmation that the server is running.
* **Close Browser Session** `closeBrowserSession`: Close a live Skyvern browser session, releasing the browser and stopping uptime billing.
* **Convert Curl To HTTP Block** `convertCurlToHttpBlock`: Turn a curl command into the JSON shape of a Skyvern HTTP workflow block, so an existing API call can be pasted straight into an agent.
* **Create Agent** `createAgent`: Create a reusable Skyvern agent (workflow) from a JSON or YAML block definition. Returns the created agent with its workflow_id and workflow_permanent_id.
* **Create Agent Schedule** `createAgentSchedule`: Create a recurring cron schedule that runs a Skyvern agent automatically. Each firing starts a real browser run and consumes credits.
* **Create Browser Profile** `createBrowserProfile`: Create a reusable Skyvern browser profile that stores cookies, local storage and proxy settings so later runs start already logged in.
* **Create Browser Session** `createBrowserSession`: Start a persistent Skyvern browser session that several runs can share. The session stays alive and bills browser uptime until it is closed or times out.
* **Create Credential** `createCredential`: Store a login, credit card or TOTP secret in the Skyvern vault so agents can sign in to a site without the secret ever appearing in a prompt. The secret is write-only: reads return only metadata.
* **Create Credential Folder** `createCredentialFolder`: Create a folder for grouping stored Skyvern credentials.
* **Create Custom LLM** `createCustomLlm`: Register a bring-your-own-key LLM (OpenAI, Anthropic, Azure, Bedrock, Gemini, OpenAI-compatible) that Skyvern agents can be pointed at instead of the built-in models.
* **Create Folder** `createFolder`: Create a folder for organising Skyvern agents.
* **Create Script** `createScript`: Create a Skyvern script from a set of Python files, optionally attached to an agent or generated from a run, so the run can be replayed deterministically.
* **Create Tag Value** `createTagValue`: Define a new value under a Skyvern tag key, optionally with a display colour.
* **Create Task (Legacy API)** `createTaskLegacy`: Start a browser task through Skyvern's original /api/v1 task API, using navigation_goal and data_extraction_goal instead of a single prompt. Drives a real browser and consumes credits.
* **Create UI Session Token** `createUiSessionToken`: Mint a short-lived Skyvern UI session JWT for the organization, used to embed the Skyvern web UI or a live browser stream. SECURITY: the returned token authenticates as the organization - treat it as a credential, never log it, and rely on its short expiry.
* **Create Workflow (Legacy API)** `createWorkflowLegacy`: Create a workflow from a YAML definition through Skyvern's original /api/v1 workflow API. The body is raw YAML, not JSON.
* **Delete Agent** `deleteAgent`: Delete a Skyvern agent (workflow) by id. The agent stops appearing in List Agents and can no longer be run.
* **Delete Agent Schedule** `deleteAgentSchedule`: Permanently delete a cron schedule from a Skyvern agent.
* **Delete Agent Tag** `deleteAgentTag`: Remove one tag key from a Skyvern agent.
* **Delete Browser Profile** `deleteBrowserProfile`: Delete a Skyvern browser profile and the stored cookies and local storage it holds.
* **Delete Credential** `deleteCredential`: Permanently delete a stored Skyvern credential and its vault secret.
* **Delete Credential Folder** `deleteCredentialFolder`: Delete a Skyvern credential folder. The credentials inside are not deleted, only ungrouped.
* **Delete Custom LLM** `deleteCustomLlm`: Remove a registered custom LLM from the Skyvern organization.
* **Delete File** `deleteFile`: Delete a file previously uploaded to Skyvern, by its file id.
* **Delete Folder** `deleteFolder`: Delete a Skyvern agent folder. Optionally delete the agents inside it as well; by default they are moved to the root.
* **Delete Run Tag** `deleteRunTag`: Remove one tag key from a Skyvern workflow run.
* **Delete Tag Key** `deleteTagKey`: Delete a Skyvern tag key and every value under it, removing it from all agents and runs.
* **Delete Tag Value** `deleteTagValue`: Delete one value under a Skyvern tag key, removing it from every agent and run that carried it.
* **Delete Workflow (Legacy API)** `deleteWorkflowLegacy`: Delete a workflow through Skyvern's original /api/v1 workflow API.
* **Deploy Script** `deployScript`: Publish a new revision of a Skyvern script by uploading its files, making that revision the one future runs replay.
* **Disable Agent Schedule** `disableAgentSchedule`: Pause a Skyvern agent schedule so it stops firing, without deleting it.
* **Enable Agent Schedule** `enableAgentSchedule`: Turn a Skyvern agent schedule back on so it fires again on its cron expression.
* **Extend Browser Session** `extendBrowserSession`: Push back the timeout of a live Skyvern browser session by a number of minutes. Extends billed browser uptime.
* **Extract Job Posting** `extractJobPosting`: Open a job advert URL in a browser and extract its structured details (title, company, location, requirements) using the Skyvern jobs recipe. Drives a real browser and consumes credits.
* **Generate AI Suggestion** `generateAiSuggestion`: Ask Skyvern's LLM to draft something for you from a prompt - most commonly a JSON data-extraction schema (suggestion type data_schema).
* **Get Agent** `getAgent`: Get a single Skyvern agent (workflow) by its permanent id, optionally at a specific version.
* **Get Agent Schedule** `getAgentSchedule`: Get one cron schedule of a Skyvern agent by its schedule id.
* **Get Agent Tag History** `getAgentTagHistory`: List the history of tag changes on a Skyvern agent, optionally limited to one tag key or a time window.
* **Get Agent Tags** `getAgentTags`: List the tags currently applied to one Skyvern agent.
* **Get Analytics Action Types** `getAnalyticsActionTypes`: Break down which browser action types (click, input, extract, ...) Skyvern agents performed, for the named agents.
* **Get Analytics Anomalies** `getAnalyticsAnomalies`: List unusual changes Skyvern detected in run health, such as a sudden drop in success rate. Requires the anomaly-detection entitlement on the organization.
* **Get Analytics Summary** `getAnalyticsSummary`: Get run-health analytics for the Skyvern organization: total runs, success rate, average duration, credits consumed and a daily breakdown for the period.
* **Get Artifact Content** `getArtifactContent`: Download the raw content of a single Skyvern artifact (screenshot PNG, recording MP4, HAR, LLM prompt/response JSON) by artifact id. Supports an optional HTTP Range header for partial downloads of large binaries.
* **Get Billing State** `getBillingState`: Get the Skyvern organization's plan tier, included credits, credits consumed and credits remaining for the current billing period. Read this before launching runs, because every run spends credits.
* **Get Browser Profile** `getBrowserProfile`: Get one Skyvern browser profile by id, including its proxy settings and last verified login time.
* **Get Browser Profile Usage** `getBrowserProfileUsage`: List which Skyvern agents and runs currently use a browser profile, so you can see what breaks before deleting it.
* **Get Browser Session** `getBrowserSession`: Get one Skyvern browser session by id, including its CDP browser address and live-view URL.
* **Get Credential** `getCredential`: Get the metadata of one stored Skyvern credential by id. The stored secret itself is never returned.
* **Get Credential Folder** `getCredentialFolder`: Get one Skyvern credential folder by id.
* **Get Folder** `getFolder`: Get one Skyvern agent folder by id.
* **Get Organizations** `getOrganizations`: Get the Skyvern organizations the API key belongs to, including the org id, slug, default webhook callback URL and per-run step limits.
* **Get Run** `getRun`: Get the current status, output, recording URL and request of a single Skyvern run (task run or agent/workflow run) by its run id.
* **Get Run Tag History** `getRunTagHistory`: List the history of tag changes on a Skyvern workflow run, optionally limited to one tag key or a time window.
* **Get Run Tags** `getRunTags`: List the tags currently applied to one Skyvern workflow run.
* **Get Run Timeline** `getRunTimeline`: Get the ordered timeline of a run: every thought, action and block the Skyvern agent produced while executing it.
* **Get Runtime Config** `getRuntimeConfig`: Get the Skyvern deployment's runtime settings: which browser-streaming mode is active, the environment name and any active warnings.
* **Get Script** `getScript`: Get one cached Skyvern script by id, including its revision and file listing.
* **Get Server Version** `getServerVersion`: Return the git commit hash of the running Skyvern API server build.
* **Get Task (Legacy API)** `getTaskLegacy`: Get one task from Skyvern's original /api/v1 task API, including its status, extracted information and failure reason.
* **Get Task V2** `getTaskV2`: Get a Skyvern 2.0 (observer) task by id, including its plan summary, status and extracted output.
* **Get Workflow (Legacy API)** `getWorkflowLegacy`: Get one workflow and its block definition through Skyvern's original /api/v1 workflow API.
* **Get Workflow Run (Legacy API)** `getWorkflowRunLegacy`: Get one workflow run, including its per-block outputs, through Skyvern's original /api/v1 workflow API.
* **Get Workflow Run By ID (Legacy API)** `getWorkflowRunByIdLegacy`: Get a workflow run by its run id alone, without naming the workflow, through Skyvern's original /api/v1 workflow API.
* **Get Workflow Run Timeline (Legacy API)** `getWorkflowRunTimelineLegacy`: Get the block-by-block timeline of a workflow run through Skyvern's original /api/v1 workflow API.
* **List Agent Runs** `listAgentRuns`: List the runs of one Skyvern agent, filterable by status, error code, tag and creation date range.
* **List Agent Schedules** `listAgentSchedules`: List the cron schedules attached to one Skyvern agent.
* **List Agent Versions** `listAgentVersions`: List every saved version of a Skyvern agent, newest first, so a previous definition can be inspected or restored.
* **List Agents** `listAgents`: List the Skyvern agents (workflows) in the organization, with paging, text search, folder, status, tag and template filters.
* **List All Agent Runs** `listAllAgentRuns`: List agent (workflow) runs across every agent in the organization, filterable by status and error code.
* **List All Schedules** `listAllSchedules`: List every cron schedule in the Skyvern organization across all agents, with paging, status and search filters.
* **List All Workflow Runs (Legacy API)** `listAllWorkflowRunsLegacy`: List workflow runs across every workflow through Skyvern's original /api/v1 workflow API.
* **List Artifacts By Step** `listArtifactsByStep`: List the artifacts produced by one agent step, addressed by step id alone without naming the task.
* **List Artifacts By Thought** `listArtifactsByThought`: List the artifacts attached to one agent thought (a planning step of a Skyvern 2.0 task).
* **List Artifacts By Workflow Run Block** `listArtifactsByWorkflowRunBlock`: List the artifacts produced by one block of a workflow run, addressed by workflow run block id.
* **List Available Models** `listAvailableModels`: List the LLM models a Skyvern run can be pointed at, as a map of model key to display name.
* **List Billing History** `listBillingHistory`: List the Skyvern organization's past invoices and credit purchases.
* **List Browser Profiles** `listBrowserProfiles`: List the saved Skyvern browser profiles, with paging, search and filters for deleted and managed profiles.
* **List Browser Sessions** `listBrowserSessions`: List the Skyvern browser sessions that are currently active and still billing browser uptime.
* **List Browser Types** `listBrowserTypes`: List the browser engines a Skyvern browser session can be launched with (Chrome, Microsoft Edge, Stealth Chromium).
* **List Credential Folders** `listCredentialFolders`: List the folders used to organise stored Skyvern credentials.
* **List Credentials** `listCredentials`: List the credentials stored in the Skyvern vault. Only metadata is returned; passwords, card numbers and TOTP seeds are never included.
* **List Custom LLMs** `listCustomLlms`: List the bring-your-own-key LLM configurations registered for the Skyvern organization.
* **List Folders** `listFolders`: List the agent folders in the organization, with paging and a text search.
* **List Google OAuth Credentials** `listGoogleOauthCredentials`: List the Google accounts connected to Skyvern via Google OAuth, which agents use for Google Sheets blocks.
* **List Google Sheets Spreadsheets** `listGoogleSheetsSpreadsheets`: List the Google Sheets spreadsheets reachable through a Google account connected to Skyvern, for use in a Google Sheets workflow block.
* **List Job Recipe Runs** `listJobRecipeRuns`: List the runs created by the Skyvern job-application recipes (extract posting, apply to job), with paging.
* **List Microsoft OAuth Credentials** `listMicrosoftOauthCredentials`: List the Microsoft accounts connected to Skyvern via Microsoft OAuth.
* **List Organization API Keys** `listOrganizationApiKeys`: List the API tokens issued for a Skyvern organization. SECURITY WARNING: the response contains each token in plaintext, including the one this connection authenticates with. Treat the output as a secret and never log or forward it.
* **List Run Artifacts** `listRunArtifacts`: List the artifacts (screenshots, HTML snapshots, recordings, LLM prompts and responses) produced by a run, optionally filtered by artifact type.
* **List Run Tag Suggestions** `listRunTagSuggestions`: List the tag keys and values Skyvern suggests when tagging a run, based on what the organization already uses.
* **List Runs** `listRuns`: List all task and workflow runs in the Skyvern organization, newest first. Supports pagination and status filtering.
* **List Scripts** `listScripts`: List the generated Python scripts Skyvern has cached for agents, which replay a run deterministically instead of re-driving the LLM.
* **List Step Artifacts** `listStepArtifacts`: List the artifacts (screenshots, HTML, LLM prompts and responses) produced by one step of a Skyvern task.
* **List Tag Keys** `listTagKeys`: List every tag key defined in the Skyvern organization, with its description.
* **List Tag Values** `listTagValues`: List the values defined under one Skyvern tag key, with their display colours.
* **List Task Actions** `listTaskActions`: List every browser action (click, type, select, extract) the Skyvern agent performed while running a task, with its reasoning and screenshot.
* **List Task Steps** `listTaskSteps`: List the agent steps of a Skyvern task, each with its order, status and output.
* **List Tasks (Legacy API)** `listTasksLegacy`: List task runs through Skyvern's original /api/v1 task API. Prefer List Runs for new work; this endpoint returns the older task-shaped records.
* **List Workflow Runs For Workflow (Legacy API)** `listWorkflowRunsForWorkflowLegacy`: List the runs of one workflow through Skyvern's original /api/v1 workflow API.
* **List Workflow Versions (Legacy API)** `listWorkflowVersionsLegacy`: List every saved version of a workflow through Skyvern's original /api/v1 workflow API.
* **List Workflows (Legacy API)** `listWorkflowsLegacy`: List workflows through Skyvern's original /api/v1 workflow API. Equivalent to List Agents on the newer API.
* **Move Agent To Folder** `moveAgentToFolder`: Move a Skyvern agent into a folder, or pass a null folder id to move it back to the root.
* **Open Billing Portal** `openBillingPortal`: Create a Stripe billing-portal session for the Skyvern organization and return its URL, where an admin can manage the plan, payment method and invoices. SECURITY: the returned URL grants billing access without further login - treat it as a secret and hand it only to an authorised admin.
* **Preview Run Webhook Payload** `previewRunWebhookPayload`: Return the exact webhook payload and target URL Skyvern would deliver for a given run, without sending it. Use this to build or test a webhook receiver.
* **Rename Tag Value** `renameTagValue`: Rename one value under a Skyvern tag key everywhere it is used.
* **Replay Run Webhook** `replayRunWebhook`: Resend the completion webhook callback for a finished run, optionally to a different webhook URL. Use this to recover a delivery your endpoint missed.
* **Replay Task Webhook (Legacy API)** `replayTaskWebhookLegacy`: Resend the completion webhook for a finished task created through the original /api/v1 task API.
* **Reset Agent Browser Profile** `resetAgentBrowserProfile`: Clear the persisted browser profile (cookies, local storage, logged-in session) that a Skyvern agent reuses between runs, forcing the next run to start from a clean browser.
* **Retry Agent Run** `retryAgentRun`: Re-run a finished agent (workflow) run with the same parameters, creating a new attempt. Consumes Skyvern credits.
* **Rotate Organization API Key** `rotateOrganizationApiKey`: Issue a new Skyvern API token for the organization and invalidate the current one. DESTRUCTIVE: this revokes the key this connection authenticates with, so every existing integration stops working until it is re-connected with the new token.
* **Run Agent** `runAgent`: Start a run of an existing Skyvern agent (workflow), passing its input parameters. Returns the created workflow run. Consumes Skyvern credits.
* **Run File Download Task** `runFileDownloadTask`: Start a Skyvern task whose goal is to navigate a site and download files, returning them on the run. Consumes credits.
* **Run Login Task** `runLoginTask`: Start a Skyvern task that signs in to a website using a vaulted credential (Skyvern vault, Bitwarden, 1Password or Azure Key Vault) and leaves the browser logged in for later runs. Consumes credits.
* **Run Script** `runScript`: Execute a deployed Skyvern script instead of re-running the AI agent. Drives a real browser and consumes credits.
* **Run SDK Action** `runSdkAction`: Execute a single low-level browser action (click, input, extract, goto, scroll) against a URL, the primitive the Skyvern SDKs are built on. Drives a real browser.
* **Run Task** `runTask`: Start a Skyvern browser-automation task from a natural-language prompt. Skyvern opens a real browser, navigates to the given URL and works towards the goal. Returns the created run with its run_id and status. Consumes Skyvern credits.
* **Run Task V2** `runTaskV2`: Start a Skyvern 2.0 (observer) task from a single user prompt. Skyvern plans the whole multi-step browser job itself. Drives a real browser and consumes credits.
* **Run Workflow (Legacy API)** `runWorkflowLegacy`: Start a workflow run through Skyvern's original /api/v1 workflow API, passing workflow parameters. Drives a real browser and consumes credits.
* **Send Test Webhook** `sendTestWebhook`: Have Skyvern POST a sample run payload to a webhook URL so you can verify your receiver and signature check before wiring up real runs.
* **Send TOTP Code** `sendTotpCode`: Push a one-time 2FA code (or the SMS/email text containing it) to Skyvern so a waiting run can complete a two-factor login.
* **Send TOTP Code (Legacy API)** `sendTotpCodeLegacy`: Push a 2FA code to Skyvern through the original /api/v1 TOTP endpoint so a waiting run can finish a two-factor login.
* **Start Billing Checkout** `startBillingCheckout`: Create a Stripe checkout session for a Skyvern subscription and return its URL. Completing that checkout SPENDS REAL MONEY.
* **Update Agent** `updateAgent`: Replace the definition of an existing Skyvern agent, creating a new version of it. Pass the full JSON or YAML definition.
* **Update Agent Schedule** `updateAgentSchedule`: Change the cron expression, timezone, parameters or name of an existing Skyvern agent schedule.
* **Update Browser Profile** `updateBrowserProfile`: Rename a Skyvern browser profile or change its proxy settings, optionally rotating its sticky proxy session.
* **Update Browser Session** `updateBrowserSession`: Change whether a live Skyvern browser session saves its final browser state as a new browser profile when it closes.
* **Update Credential** `updateCredential`: Replace a stored Skyvern credential's name and secret, for example after a password rotation.
* **Update Credential Folder** `updateCredentialFolder`: Rename a Skyvern credential folder or change its description. At least one of title or description must be supplied.
* **Update Custom LLM** `updateCustomLlm`: Replace the configuration of a registered custom LLM, for example to change the model name, endpoint or API key.
* **Update Folder** `updateFolder`: Rename a Skyvern agent folder or change its description.
* **Update Organization** `updateOrganization`: Update organization-wide Skyvern settings: the default webhook callback URL every run reports to, the step limits that cap credit spend per run, and the default LLM.
* **Update Tag Key** `updateTagKey`: Change the description of a Skyvern tag key.
* **Update Tag Value Color** `updateTagValueColor`: Change the display colour of one value under a Skyvern tag key.
* **Update Workflow (Legacy API)** `updateWorkflowLegacy`: Replace a workflow's YAML definition through Skyvern's original /api/v1 workflow API, creating a new version.
* **Upload File** `uploadFile`: Upload a text file to Skyvern so a run can attach it to a form or read it. Returns a file id to pass in file_ids when starting a task or agent run.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Run Canceled | `canceled` | Fires when a Skyvern run is cancelled through Cancel Run, Bulk Cancel Runs or the Skyvern UI. Same payload shape as Run Completed. |
| Run Completed | `completed` | Fires when a Skyvern run (task or agent/workflow run) finishes successfully. Registration is organization-wide: Skyvern stores one webhook_callback_url per organization, which the subscription code sets via PUT /api/v1/organizations; an individual run can override it with its own webhook_url. Skyvern signs each delivery with x-skyvern-signature (HMAC-SHA256 hex over the body, keyed with the organization's own API key) and x-skyvern-timestamp - verify these yourself, because the signing key is per-account and cannot be stored on a shared connector. Payload schema captured live from GET /api/v1/internal/runs/{run_id}/test-webhook for a real workflow_run. |
| Run Failed | `failed` | Fires when a Skyvern run ends in failure. failure_reason and failure_category carry the cause, and output.error carries your custom code when error_code_mapping was supplied. Same payload shape as Run Completed, captured live from GET /api/v1/internal/runs/{run_id}/test-webhook. |
| Run Terminated | `terminated` | Fires when Skyvern stops a run because its terminate_criterion was met or the agent decided the goal is unreachable. Same payload shape as Run Completed. |
| Run Timed Out | `timed_out` | Fires when a Skyvern run exceeds its step or elapsed-time limit. Same payload shape as Run Completed. |
