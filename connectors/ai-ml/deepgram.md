---
description: "Deepgram voice AI platform: speech-to-text transcription (listen), text-to-speech (speak), text intelligence (read), and full management API (projects, keys,…"
hidden: true
---

# Deepgram

Deepgram voice AI platform: speech-to-text transcription (listen), text-to-speech (speak), text intelligence (read), and full management API (projects, keys, members, invitations, usage, balances, models, auth grant). Auth: Authorization: Token &lt;api_key&gt;.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [deepgram.com](https://deepgram.com) |
| **Authentication** | API key |
| **Actions** | 31 |
| **Events** | 0 |
| **Slug** | `deepgram` |

## Use it

Add Deepgram from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.deepgram.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Analyze Text (Read) | `read` | Run text intelligence (summarize, topics, intents, sentiment) over input text. Requires language=en and at least one feature flag enabled. Costs credits per token. |
| Create Auth Grant (Temporary Token) | `createAuthGrant` | Create a short-lived JWT access token (default TTL 30s) for the voice APIs. Free management call. |
| Create Project Invite | `createProjectInvite` | Send an invitation to join a project. |
| Create Project Key | `createProjectKey` | Create a new API key for a project with the given scopes. The raw key is returned once in the response. |
| Delete Project | `deleteProject` | Delete a Deepgram project by id. |
| Delete Project Invite | `deleteProjectInvite` | Delete a pending project invitation by invitee email. |
| Delete Project Key | `deleteProjectKey` | Delete an API key from a project. |
| Get Model | `getModel` | Get a single public Deepgram model by id. Free read. |
| Get Project | `getProject` | Get a single Deepgram project by id. Free read — credit-safe for validation. |
| Get Project Balance | `getProjectBalance` | Get a single credit balance for a project by balance id. Free read. |
| Get Project Balances | `getProjectBalances` | List credit balances for a project. Free read — credit-safe for validation. |
| Get Project Billing Breakdown | `getProjectBillingBreakdown` | Get a billing (dollars) breakdown for a project. Free read. |
| Get Project Key | `getProjectKey` | Get a single API key for a project by key id. Free read. |
| Get Project Model | `getProjectModel` | Get a single model available to a project by model id. Free read. |
| Get Project Request | `getProjectRequest` | Get a single API request record by id. Free read. |
| Get Project Usage | `getProjectUsage` | Get usage summary for a project over a date range. Free read — credit-safe for validation. |
| Get Project Usage Breakdown | `getProjectUsageBreakdown` | Get a grouped usage breakdown for a project. Free read. |
| List Member Scopes | `listMemberScopes` | List the scopes assigned to a project member. Free read. |
| List Models | `listModels` | List all public Deepgram models (STT and TTS). Free read — credit-safe for validation. |
| List Project Invites | `listProjectInvites` | List pending invitations for a project. Free read. |
| List Project Keys | `listProjectKeys` | List API keys for a project. Free read — credit-safe for validation. |
| List Project Members | `listProjectMembers` | List members of a project. Free read — credit-safe for validation. |
| List Project Models | `listProjectModels` | List models available to a project, including custom models. Free read. |
| List Project Requests | `listProjectRequests` | List API request records (usage) for a project. Free read — credit-safe for validation. |
| List Project Usage Fields | `listProjectUsageFields` | List available usage fields (models, methods, features, tags) for a project. Free read. |
| List Projects | `listProjects` | List all Deepgram projects the API key can access. Free read — credit-safe for validation. |
| Remove Project Member | `removeProjectMember` | Remove a member from a project. |
| Text to Speech (Speak) | `speak` | Convert text to speech audio using a Deepgram Aura voice. Returns binary audio (or request_id if callback is set). Costs credits per character. |
| Transcribe Pre-recorded Audio (URL) | `transcribeUrl` | Transcribe pre-recorded audio from a hosted URL using Deepgram speech-to-text. Supply the audio url and optional feature flags (model, smart_format, diarize, summarize, etc.). Costs credits per audio second. |
| Update Member Scopes | `updateMemberScopes` | Update the scope assigned to a project member. |
| Update Project | `updateProject` | Update a Deepgram project's name. |
