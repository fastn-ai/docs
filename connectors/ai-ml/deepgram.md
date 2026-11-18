---
description: "Deepgram voice AI platform: speech-to-text transcription (listen), text-to-speech (speak), text intelligence (read), and full management API (projects, keys,…"
hidden: true
---

# Deepgram

<img src="../../.gitbook/assets/connectors/lg/deepgram.png" alt="Deepgram logo">

Deepgram voice AI platform: speech-to-text transcription (listen), text-to-speech (speak), text intelligence (read), and full management API (projects, keys, members, invitations, usage, balances, models, auth grant). Auth: Authorization: Token &lt;api_key&gt;.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [deepgram.com](https://deepgram.com) |
| **Authentication** | API key |
| **Slug** | `deepgram` |

## Use it

Add Deepgram from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.deepgram.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Analyze Text (Read)</td><td><code>read</code></td><td>Run text intelligence (summarize, topics, intents, sentiment) over input text. Requires language=en and at least one feature flag enabled. Costs credits per token.</td></tr><tr><td>Create Auth Grant (Temporary Token)</td><td><code>createAuthGrant</code></td><td>Create a short-lived JWT access token (default TTL 30s) for the voice APIs. Free management call.</td></tr><tr><td>Create Project Invite</td><td><code>createProjectInvite</code></td><td>Send an invitation to join a project.</td></tr><tr><td>Create Project Key</td><td><code>createProjectKey</code></td><td>Create a new API key for a project with the given scopes. The raw key is returned once in the response.</td></tr><tr><td>Delete Project</td><td><code>deleteProject</code></td><td>Delete a Deepgram project by id.</td></tr><tr><td>Delete Project Invite</td><td><code>deleteProjectInvite</code></td><td>Delete a pending project invitation by invitee email.</td></tr><tr><td>Delete Project Key</td><td><code>deleteProjectKey</code></td><td>Delete an API key from a project.</td></tr><tr><td>Get Model</td><td><code>getModel</code></td><td>Get a single public Deepgram model by id. Free read.</td></tr><tr><td>Get Project</td><td><code>getProject</code></td><td>Get a single Deepgram project by id. Free read — credit-safe for validation.</td></tr><tr><td>Get Project Balance</td><td><code>getProjectBalance</code></td><td>Get a single credit balance for a project by balance id. Free read.</td></tr></tbody></table>

<details>

<summary>View 21 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Project Balances</td><td><code>getProjectBalances</code></td><td>List credit balances for a project. Free read — credit-safe for validation.</td></tr><tr><td>Get Project Billing Breakdown</td><td><code>getProjectBillingBreakdown</code></td><td>Get a billing (dollars) breakdown for a project. Free read.</td></tr><tr><td>Get Project Key</td><td><code>getProjectKey</code></td><td>Get a single API key for a project by key id. Free read.</td></tr><tr><td>Get Project Model</td><td><code>getProjectModel</code></td><td>Get a single model available to a project by model id. Free read.</td></tr><tr><td>Get Project Request</td><td><code>getProjectRequest</code></td><td>Get a single API request record by id. Free read.</td></tr><tr><td>Get Project Usage</td><td><code>getProjectUsage</code></td><td>Get usage summary for a project over a date range. Free read — credit-safe for validation.</td></tr><tr><td>Get Project Usage Breakdown</td><td><code>getProjectUsageBreakdown</code></td><td>Get a grouped usage breakdown for a project. Free read.</td></tr><tr><td>List Member Scopes</td><td><code>listMemberScopes</code></td><td>List the scopes assigned to a project member. Free read.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>List all public Deepgram models (STT and TTS). Free read — credit-safe for validation.</td></tr><tr><td>List Project Invites</td><td><code>listProjectInvites</code></td><td>List pending invitations for a project. Free read.</td></tr><tr><td>List Project Keys</td><td><code>listProjectKeys</code></td><td>List API keys for a project. Free read — credit-safe for validation.</td></tr><tr><td>List Project Members</td><td><code>listProjectMembers</code></td><td>List members of a project. Free read — credit-safe for validation.</td></tr><tr><td>List Project Models</td><td><code>listProjectModels</code></td><td>List models available to a project, including custom models. Free read.</td></tr><tr><td>List Project Requests</td><td><code>listProjectRequests</code></td><td>List API request records (usage) for a project. Free read — credit-safe for validation.</td></tr><tr><td>List Project Usage Fields</td><td><code>listProjectUsageFields</code></td><td>List available usage fields (models, methods, features, tags) for a project. Free read.</td></tr><tr><td>List Projects</td><td><code>listProjects</code></td><td>List all Deepgram projects the API key can access. Free read — credit-safe for validation.</td></tr><tr><td>Remove Project Member</td><td><code>removeProjectMember</code></td><td>Remove a member from a project.</td></tr><tr><td>Text to Speech (Speak)</td><td><code>speak</code></td><td>Convert text to speech audio using a Deepgram Aura voice. Returns binary audio (or request_id if callback is set). Costs credits per character.</td></tr><tr><td>Transcribe Pre-recorded Audio (URL)</td><td><code>transcribeUrl</code></td><td>Transcribe pre-recorded audio from a hosted URL using Deepgram speech-to-text. Supply the audio url and optional feature flags (model, smart_format, diarize, summarize, etc.). Costs credits per audio second.</td></tr><tr><td>Update Member Scopes</td><td><code>updateMemberScopes</code></td><td>Update the scope assigned to a project member.</td></tr><tr><td>Update Project</td><td><code>updateProject</code></td><td>Update a Deepgram project's name.</td></tr></tbody></table>

</details>
