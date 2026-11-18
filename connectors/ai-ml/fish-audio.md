---
description: "Fish Audio is an AI voice platform for text-to-speech, speech-to-text and voice cloning."
hidden: true
---

# Fish Audio

<img src="../../.gitbook/assets/connectors/fish-audio.png" alt="Fish Audio logo" width="64">

Fish Audio is an AI voice platform for text-to-speech, speech-to-text and voice cloning. This connector covers the full Fish Audio REST API at https://api.fish.audio: text to speech (including streaming with word timestamps), speech to text, voice design, voice model management (list, create, get, update, delete), wallet package and API credit, and the Fish Agents voice-agent platform (agents, draft configuration and publishing, versions, sessions and recordings, tools, knowledge sources, phone numbers and outbound phone calls). Post-call agent webhooks (call.ended, call.analyzed, phone_call.dial_finished) are supported as events.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [fish.audio](https://fish.audio) |
| **Authentication** | Bearer token |
| **Slug** | `fishAudio` |

## Use it

Add Fish Audio from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fishAudio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Agent | `createAgent` | Create a voice agent, optionally with its full initial draft configuration (prompt, voice, conversation, tools, webhooks, knowledge base, analysis, guardrails and LLM sections). The agent starts as a draft: publish it before creating sessions. Requires access to the Fish Agents platform (private beta). |
| Create Agent Session | `createAgentSession` | Start a conversation session with a published voice agent and receive a join token for the session transport (LiveKit WebRTC). Supports per-session overrides, dynamic prompt variables, an end-user identifier and metadata that are echoed in webhooks. |
| Create Knowledge Source | `createKnowledgeSource` | Upload a plain-text or Markdown document (UTF-8, up to 1 MB) as a knowledge source that agents can retrieve from. Fish Audio requires multipart/form-data with the file in the source part; name defaults to the file name. Attach it to agents via the agent config's knowledge_base.knowledge_source_ids. |
| Create Phone Call | `createPhoneCall` | Place an outbound call from one of your Twilio phone numbers to a US, Canada or Japan destination, answered by the given agent. Returns immediately with the session queued for dialing; subscribe to the phone_call.dial_finished webhook or poll Get Agent Session for the outcome. An optional idempotency key makes retries safe for 24 hours. |
| Create Tool | `createTool` | Create a workspace tool for agents. A webhook tool calls your HTTP endpoint during conversations (with arguments, headers, body template and mock responses); a client tool is executed by your own frontend through the SDK. Attach it to agents via the agent config's tools.tool_ids. Credential header values are write-only. |
| Create Voice Model | `createModel` | Create (clone) a voice model from one or more reference audio files. Fish Audio requires the audio as multipart/form-data file uploads; with train_mode 'fast' the model is available immediately. Pass the audio file as the voices field and, optionally, its transcript as texts. |
| Delete Agent | `deleteAgent` | Delete a voice agent together with its configuration and version history. Existing session records are retained. |
| Delete Knowledge Source | `deleteKnowledgeSource` | Delete a knowledge source. Returns 409 while any agent still references it in its draft or published configuration; check List Agents Using Knowledge Source and detach it first. |
| Delete Tool | `deleteTool` | Delete an agent tool. Returns 409 while any agent's draft configuration still references it; check List Agents Using Tool and detach it first. |
| Delete Voice Model | `deleteModel` | Permanently delete a voice model you own by its ID. Fish Audio returns 204 No Content on success. |

<details>

<summary>See 36 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Design Voice | `voiceDesign` | Generate candidate voices from a natural-language description and return each candidate with base64-encoded preview audio. Billed against API credit. |
| End Agent Session | `endAgentSession` | Hang up a live voice-agent session: the agent disconnects and the call terminates. The session record, transcript and recording are retained. |
| Get Agent | `getAgent` | Retrieve one voice agent's profile fields (name, description, status, publication state and public-access settings). The draft configuration is read with Get Agent Draft Config. |
| Get Agent Draft Config | `getAgentDraftConfig` | Read a voice agent's current draft configuration: prompt, voice, conversation, tools, webhooks, knowledge base, analysis, guardrails and LLM settings. Sessions run the latest published version, not the draft. Webhook signing secrets are write-only and reported as has_secret. |
| Get Agent Session | `getAgentSession` | Retrieve one voice-agent session in full: status, timing, the conversation timeline (transcript turns interleaved with tool calls), LLM usage and the post-call analysis. |
| Get Agent Session Recording | `getAgentSessionRecording` | Retrieve time-limited download URLs for a session's audio recording, one per speaker track (agent and user are recorded separately). |
| Get Agent Version | `getAgentVersion` | Retrieve one published version of a voice agent with its full frozen configuration snapshot. Secrets inside the snapshot are redacted the same way as the draft configuration. |
| Get Agent Widget Config | `getAgentWidgetConfig` | Retrieve the display configuration for the embeddable fish-agent widget of a public agent. Only agents published as public are reachable and the Origin header must match the agent's allowed origins. |
| Get API Credit | `getApiCredit` | Retrieve the API credit balance of a user (default: the authenticated user via 'self'). API credit is billed separately from platform credit and funds text to speech, speech to text and voice design calls. |
| Get Knowledge Source | `getKnowledgeSource` | Retrieve one knowledge source including its full text content and current revision number. |
| Get Phone Number | `getPhoneNumber` | Retrieve one phone number, including its current agent binding and provisioning status. |
| Get Tool | `getTool` | Retrieve one agent tool's full definition. Credential header values are never returned; each credential header reports has_secret instead. |
| Get User Package | `getUserPackage` | Retrieve the platform subscription package of a user (default: the authenticated user via 'self'), including plan type, credit balance, billing period and subscription status. |
| Get Voice Model | `getModel` | Retrieve the details of a single voice model by its ID, including training state, visibility, tags, languages, samples and author. |
| List Agent Sessions | `listAgentSessions` | List your team's voice-agent sessions, newest first. Filter by agent, status, call direction, caller number or creation time. Paginate with cursor (follow next_cursor while has_more is true) or with page for offset pagination; the two are mutually exclusive. |
| List Agent Versions | `listAgentVersions` | List a voice agent's publish history, newest first. The highest version_number is what live sessions run; compare a version's config_hash with the draft's to detect unpublished changes. |
| List Agents | `listAgents` | List your team's voice agents, newest first. Filter by name or description text, archived state and publication state. Paginate with cursor (follow next_cursor while has_more is true) or with page for offset pagination; the two are mutually exclusive. |
| List Agents Using Knowledge Source | `listAgentsUsingKnowledgeSource` | List every agent that references a knowledge source in its draft or currently published configuration; the pre-flight check before deleting the source. |
| List Agents Using Tool | `listAgentsUsingTool` | List every agent whose draft configuration references a tool; the pre-flight check before deleting the tool. |
| List Knowledge Sources | `listKnowledgeSources` | List your team's knowledge sources (text or Markdown documents agents can retrieve from), newest first, with optional name or file-name search. Paginate with cursor or page; the two are mutually exclusive. |
| List Phone Numbers | `listPhoneNumbers` | List your team's phone numbers, newest first. Look a number up by its E.164 value or filter by the agent it is bound to. Released numbers never appear. Paginate with cursor or page; the two are mutually exclusive. |
| List Tools | `listTools` | List your team's agent tools (webhook or client tools), newest first. Filter by name search or by the agent whose draft configuration they are attached to. Paginate with cursor or page; the two are mutually exclusive. |
| List Voice Models | `listModels` | List voice models from the Fish Audio library or, with self=true, the models owned by your workspace. Supports filtering by title, tag, language, author and licensing, with pagination and sorting. |
| Publish Agent | `publishAgent` | Freeze a voice agent's current draft into an immutable, auto-numbered version and make it the live configuration for new sessions. If the draft already matches the live version, that version is returned unchanged. The optional title and description label the version for audit and rollback. |
| Purchase Or Import Phone Number | `purchaseOrImportPhoneNumber` | Buy a phone number from the managed Twilio inventory (provider twilio, billed daily) or import a number you already own at your SIP carrier (provider sip, with inbound and termination trunk settings). Optionally bind an agent to answer inbound calls right away. |
| Release Phone Number | `releasePhoneNumber` | Release a phone number back to the provider's inventory and stop its daily billing. This is irreversible: the number can be bought by anyone afterwards and disappears from the API immediately. |
| Search Available Phone Numbers | `searchAvailablePhoneNumbers` | Search the purchasable phone-number inventory (US and Canada local numbers from the managed Twilio inventory). Availability is not a reservation; buy a listed number with Purchase Or Import Phone Number. |
| Speech To Text | `speechToText` | Transcribe an audio file to text with automatic language detection, optionally returning timestamped segments. The audio is sent as a base64-encoded string in the JSON body. Billed against API credit. |
| Text To Speech | `textToSpeech` | Convert text to speech and return the generated audio file (mp3, wav, pcm or opus). Choose the TTS model with the model input; s2.1-pro-free is available on the free developer tier, other models are billed against API credit. Use reference_id to speak with a voice model from the Fish Audio library or your own models. Inline reference audio (zero-shot cloning) requires MessagePack and is not available here. |
| Text To Speech Stream With Timestamps | `textToSpeechStreamWithTimestamps` | Convert text to speech as a Server-Sent Events stream where every event carries a base64 audio chunk plus a cumulative word-level timestamp alignment. Concatenate the audio_base64 chunks in order to rebuild the full audio. Accepts the same synthesis options as Text To Speech; s2.1-pro-free is available on the free developer tier. |
| Update Agent | `updateAgent` | Update a voice agent's profile fields: name, description, status, public access and the session-override policy. Omitted fields keep their value. Conversation behaviour (voice, prompt, recording) is draft configuration; use Update Agent Draft Config for that. |
| Update Agent Draft Config | `updateAgentDraftConfig` | Patch a voice agent's draft configuration section by section (prompt, voice, conversation, tools, webhooks, knowledge base, analysis, guardrails, LLM). Omitted sections keep their value. Changes only affect live sessions after the next Publish Agent. The webhooks.post_call list (up to 5 endpoints) is replaced wholesale and receives call.ended, call.analyzed and phone_call.dial_finished events. |
| Update Knowledge Source | `updateKnowledgeSource` | Rename or re-describe a knowledge source and/or replace its content by uploading a new file (multipart source part). Replacing content increments revision_number; attached agents' drafts pick it up immediately while published versions keep the revision they were published with. |
| Update Phone Number | `updatePhoneNumber` | Change a phone number's label, repoint it at another agent (or unbind it), set the caller-ID policy for transfers on managed Twilio numbers, or retry a failed caller-ID synchronization. Omitted fields keep their value. |
| Update Tool | `updateTool` | Patch an agent tool's fields; omitted fields keep their value (send an empty string to clear a text field). The headers list is replaced wholesale, so include credential values again whenever you send it. Attached agents' drafts pick up the change immediately. |
| Update Voice Model | `updateModel` | Update the title, description, cover image, visibility or tags of a voice model you own. Only the fields you pass are changed. Fish Audio returns 204 No Content on success; call Get Voice Model to read the updated model. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Call Analyzed | `call.analyzed` | Fires when post-call analysis settles (completed, skipped or error), after call.ended for the same session. Payload carries the session facts plus the full analysis entity (summary, data fields, criteria results). Registered per agent via the agent's webhooks.post_call list (Agent ID input required). Payload modelled from the vendor's documented example; no live delivery could be captured (private beta). |
| Call Ended | `call.ended` | Fires when a voice-agent session reaches a terminal state (every real call, whether or not analysis is configured). Payload carries the session facts plus ended_reason (hangup or error). Registered per agent: the subscription adds the fastn URL to the agent's webhooks.post_call list and publishes the agent, so the Agent ID input is required. Deliveries are signed with X-Fish-Webhook-Signature (t=&lt;unix&gt;,v1=&lt;hex HMAC-SHA256 of '{t}.{body}'&gt;) keyed with the per-endpoint secret. Payload modelled from the vendor's documented example (https://docs.fish.audio/agents/monitor/webhooks); the account is in the Fish Agents private beta so no live delivery could be captured. |
| Phone Call Dial Finished | `phone_call.dial_finished` | Fires for outbound phone calls as soon as the dial attempt resolves (answered, busy, no_answer or failed), before call.ended. Payload carries the session facts plus top-level dial_status and answered_by. Registered per agent via the agent's webhooks.post_call list (Agent ID input required). Payload modelled from the vendor's documented example; no live delivery could be captured (private beta). |
