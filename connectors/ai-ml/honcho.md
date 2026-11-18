---
description: "Honcho by Plastic Labs is a memory and social-cognition layer for AI agents."
hidden: true
---

# Honcho

Honcho by Plastic Labs is a memory and social-cognition layer for AI agents. This connector covers the Honcho v3 REST API: workspaces, peers, sessions, messages, conclusions, scopes, peer cards, representations, session context and summaries, search, the dialectic chat endpoints, queue status, dreams, API keys and webhook endpoints.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [honcho.dev](https://honcho.dev) |
| **Authentication** | Credentials you enter |
| **Actions** | 54 |
| **Events** | 2 |
| **Slug** | `honcho` |

## Use it

Add Honcho from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.honcho.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Peers To Session | `addPeersToSession` | Adds peers to a session with their per-session observation settings. Peers that do not exist yet are created automatically. Scope peers cannot be added here. Returns the session. |
| Add Sessions To Scope | `addSessionsToScope` | Adds existing sessions to a scope. Sessions must already exist (404 otherwise); adding a session that is already a member is a no-op. Sessions that already have messages trigger an asynchronous backfill into the scope, trackable with Get Scope Status. |
| Clone Session | `cloneSession` | Clones a session into a new session, optionally only up to (and including) a specific message. Returns the new session. |
| Create API Key | `createKey` | Creates a new Honcho API key, optionally scoped to a workspace and to either a peer or a session within it (not both). Requires an admin key. Returns the new key; store it securely as it is not shown again. Keys cannot be listed or revoked via the API. |
| Create Conclusions | `createConclusions` | Creates one or more explicit conclusions in a workspace. A conclusion is a fact an observer peer holds about an observed peer (optionally tied to a session) and forms part of the observed peer's representation. Returns the created conclusions. |
| Create Messages | `createMessages` | Adds one or more messages to a session. Each message carries its content and the peer that sent it, plus optional metadata, per-message reasoning configuration and an explicit created_at timestamp. Honcho queues background reasoning on the new messages. Returns the created messages. |
| Delete Conclusion | `deleteConclusion` | Permanently deletes a single conclusion by ID. This cannot be undone. |
| Delete Session | `deleteSession` | Deletes a session and all of its messages. The session is marked inactive immediately (202 Accepted) and its data is removed asynchronously. This cannot be undone. |
| Delete Webhook Endpoint | `deleteWebhookEndpoint` | Deletes a webhook endpoint from a workspace by endpoint ID. Available on self-hosted Honcho; on Honcho Cloud (api.honcho.dev) this route returns 405 and endpoints are managed in the dashboard at https://app.honcho.dev/webhooks. |
| Delete Workspace | `deleteWorkspace` | Permanently deletes a workspace and all of its peers, messages, conclusions and other resources. The request is accepted (202) and processed in the background. Returns 409 if the workspace still contains active sessions; delete all sessions first. This cannot be undone. |
| Get Deriver Metrics | `getDeriverMetrics` | Returns the server-wide background reasoning (deriver) backlog: seconds of outstanding work plus the raw counts behind it (eligible, claimed and pending work units, pending embeddings and dreams due). |
| Get Message | `getMessage` | Retrieves a single message by ID from a session. |
| Get Or Create Peer | `getOrCreatePeer` | Gets a peer by ID in a workspace, creating it if it does not exist yet. Optionally sets initial metadata and configuration. |
| Get Or Create Scope | `getOrCreateScope` | Gets a scope (a named set of sessions acting as a visibility boundary for recall) by ID in a workspace, creating it if it does not exist. Returns 201 when created and 200 when it already existed. |
| Get Or Create Session | `getOrCreateSession` | Gets a session by ID in a workspace, creating it if it does not exist yet. Optionally sets metadata, initial peers with their observation settings, reasoning configuration and scope membership. |
| Get Or Create Webhook Endpoint | `getOrCreateWebhookEndpoint` | Registers an HTTPS URL to receive Honcho webhook events (queue.empty, test.event) for a workspace, or returns the existing endpoint if the URL is already registered. Available on self-hosted Honcho; on Honcho Cloud (api.honcho.dev) this route returns 405 and endpoints must be registered in the dashboard at https://app.honcho.dev/webhooks. |
| Get Or Create Workspace | `getOrCreateWorkspace` | Gets a workspace by ID, creating it if it does not exist yet. Returns 201 when created and 200 when it already existed. Optionally sets initial metadata and reasoning configuration. |
| Get Peer Card | `getPeerCard` | Returns the peer card (a short list of stable biographical facts) that an observer peer holds about a target peer, or the observer's own card when no target is given. Returns null when no card exists yet. |
| Get Peer Context | `getPeerContext` | Returns everything needed to reason about a peer in one call: a curated representation and the peer card. With a target, returns the target's context from the observer peer's perspective; otherwise the peer's own context. Optionally curate the representation around a semantic search query. |
| Get Peer Representation | `getPeerRepresentation` | Returns a curated subset of a peer's representation (what Honcho knows about them). Optionally scope to a session or scopes, view a target peer from this peer's perspective, or curate the representation around a semantic search query. |
| Get Queue Status | `getQueueStatus` | Returns the background reasoning queue status for a workspace (representation, summary and dream work units), optionally filtered by observer peer, sender peer and/or session. Completed counts reflect items since the last periodic queue cleanup. |
| Get Scope | `getScope` | Retrieves a single scope by ID in a workspace. |
| Get Scope Status | `getScopeStatus` | Returns the backfill and reconciliation job status of a scope as a per-session map (pending, completed or failed, with the number of documents copied once complete). Empty when no backfill has been enqueued. |
| Get Session Context | `getSessionContext` | Produces an LLM-ready context object for a session: recent messages plus, when available, a summary, and optionally the representation and peer card of a target peer from a given perspective. Use tokens to cap the total size (40% summary, 60% recent messages). |
| Get Session Peer Config | `getSessionPeerConfig` | Returns a peer's per-session configuration (observe_me and observe_others) within a session. |
| Get Session Summaries | `getSessionSummaries` | Returns the available short and long summaries of a session, including the message each covers up to, its creation time and token count. Summaries are null until Honcho has generated them. |
| Health Check | `healthCheck` | Checks that the Honcho API server is reachable and healthy. |
| List Conclusions | `listConclusions` | Lists the conclusions of a workspace, paginated and ordered by recency, with optional filters such as observer_id, observed_id, session_id or level. |
| List Messages | `listMessages` | Lists the messages of a session, paginated, with optional filters on message fields and metadata. |
| List Peer Sessions | `listPeerSessions` | Lists the sessions a peer participates in, paginated, with optional filters. |
| List Peers | `listPeers` | Lists the peers of a workspace, paginated, with optional filters. Scope peers are excluded by default; set kind to scope for scope peers only or all for everything. |
| List Scope Sessions | `listScopeSessions` | Lists the sessions that are members of a scope, paginated, ordered by membership age (longest-standing first, or most recently added first when reverse is true). |
| List Scopes | `listScopes` | Lists the scopes of a workspace, paginated. |
| List Session Peers | `listSessionPeers` | Lists the peers that are members of a session, paginated. |
| List Sessions | `listSessions` | Lists the sessions of a workspace, paginated, with optional filters on session fields and metadata. |
| List Webhook Endpoints | `listWebhookEndpoints` | Lists the webhook endpoints registered on a workspace, paginated. Available on self-hosted Honcho; on Honcho Cloud (api.honcho.dev) this route returns 405 and endpoints are managed in the dashboard at https://app.honcho.dev/webhooks. |
| List Workspaces | `listWorkspaces` | Lists all workspaces the API key can access, paginated, with optional filters on workspace fields and metadata. |
| Peer Chat | `peerChat` | Asks a natural-language question about a peer (dialectic chat). Honcho performs agentic search and reasoning over everything it knows about the peer from their messages and conclusions. Optionally scope to a session or scopes, ask about a target peer from this peer's perspective, choose a reasoning level, or request a JSON-schema-shaped answer. |
| Query Conclusions | `queryConclusions` | Semantically searches the conclusions of a workspace with a natural-language query, returning the top_k closest conclusions, optionally within a maximum cosine distance. The filters object must name the observer and observed peers. |
| Remove Peers From Session | `removePeersFromSession` | Removes the given peers from a session by peer ID. Scope peers cannot be removed here. Returns the session. |
| Remove Session From Scope | `removeSessionFromScope` | Removes a session from a scope. Documents derived while the session was a member are reconciled asynchronously and the scope's card is rebuilt from the remaining evidence. |
| Schedule Dream | `scheduleDream` | Manually schedules an immediate dream (memory consolidation) task for an observer/observed peer pair in a workspace, bypassing the automatic dream conditions. Choose an omni dream or a peer card refresh. |
| Search Peer Messages | `searchPeer` | Searches a peer's messages with a text query, optional filters and a result limit. Returns the matching messages. |
| Search Session Messages | `searchSession` | Searches the messages of a session with a text query, optional filters and a result limit. Returns the matching messages. |
| Search Workspace | `searchWorkspace` | Searches messages across an entire workspace with a text query, optional filters, a result limit and an optional scope restricting the search to that scope's member sessions. Returns the matching messages. |
| Send Test Webhook Event | `sendTestWebhookEvent` | Emits a test.event to every webhook endpoint registered on a workspace, to confirm a receiver and its signature check end to end. Available on self-hosted Honcho; on Honcho Cloud (api.honcho.dev) this route returns 405. |
| Set Peer Card | `setPeerCard` | Sets the peer card (a list of stable biographical facts) that an observer peer holds about a target peer, or the observer's own card when no target is given. Replaces any existing card. |
| Set Session Peer Config | `setSessionPeerConfig` | Sets a peer's per-session configuration within a session: whether Honcho observes the peer (observe_me) and whether the peer observes others (observe_others). |
| Set Session Peers | `setSessionPeers` | Replaces the full set of peers in a session with the given peers and their per-session observation settings. Peers that do not exist yet are created automatically. Scope peers cannot be set here. Returns the session. |
| Update Message | `updateMessage` | Replaces the metadata of a message in a session. Any existing metadata on the message is overwritten. |
| Update Peer | `updatePeer` | Updates a peer's metadata and/or configuration. Returns 422 if the peer is a scope; manage scopes with the scope actions. |
| Update Session | `updateSession` | Updates a session's metadata and/or reasoning configuration. Only the fields you pass are changed. |
| Update Workspace | `updateWorkspace` | Updates a workspace's metadata and/or reasoning configuration. Only the fields you pass are changed. |
| Workspace Chat | `workspaceChat` | Asks a natural-language question across an entire workspace (dialectic chat) and returns Honcho's answer. Optionally scope message tools to a session or restrict recall to named scopes (session_id and scope are mutually exclusive), choose a reasoning level, or request a JSON-schema-shaped answer. With stream false the response is {content}; with stream true the response is the raw server-sent-event text. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Queue Empty | `queue.empty` | Fires when a unit of Honcho background work (one queue_type - representation or summary - for one session and observer/observed pair) has finished draining. Registration: on Honcho Cloud open https://app.honcho.dev/webhooks, click Add endpoint, paste this trigger's webhook URL and save (Honcho Cloud does not expose the webhook API; it returns 405). On a self-hosted Honcho server, run the connector's Get Or Create Webhook Endpoint action with the trigger URL instead. Every event for the workspace is delivered to every registered endpoint; delivery is fire-and-forget with no retries. Payload schema is modelled from the vendor's documented sample (https://honcho.dev/docs/v3/documentation/features/advanced/webhooks.md), not from a captured delivery. |
| Test Event | `test.event` | Fires when a test emission is triggered for the workspace (GET /v3/workspaces/{workspace_id}/webhooks/test on self-hosted Honcho, or the Test button on https://app.honcho.dev/webhooks on Honcho Cloud). Registration: on Honcho Cloud open https://app.honcho.dev/webhooks, click Add endpoint, paste this trigger's webhook URL and save; on self-hosted Honcho run the connector's Get Or Create Webhook Endpoint action with the trigger URL. Payload schema is modelled from the vendor's documented sample, not from a captured delivery. |
