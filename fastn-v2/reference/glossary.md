---
description: Terms used across fastn, defined once.
---

# Glossary

**Action** — one operation a connector exposes, such as `getSale` or `createOrder`. Actions are versioned and can be pinned per workflow.

**Agent** — fastn's AI builder. Discovers connectors, wires auth, drafts workflows, generates test cases, and shows a diff before anything runs.

**Alert** — a rule that notifies you when a run fails or a metric crosses a threshold. Threshold alerts are evaluated every 15 minutes.

**App event trigger** — starts a workflow when something changes in a connected system.

**Approval mode** — on the [agent](../build/agent.md), whether it asks before it acts. **Auto** (the default) creates, updates and deletes without asking; **Manual** asks first.

**Backoff strategy** — how long fastn waits between delivery attempts: Exponential, Linear or Fixed.

**Config** — a per-environment value read with `fastn.envConfig.get`. Entered and edited in the dashboard rather than write-once, unlike a secret.

**Connection** — one customer's authorised link to one connector. Holds the encrypted credential. Its id has the form `ucl:org_<org>:<env>:<connectorId>:<authId>:<tenant>`.

**Connector** — the definition of an external system: actions, auth methods, webhook config, versions. Managed by fastn, or custom.

**Connector update** — a proposed fix for an upstream API change. Nothing applies until you accept it.

**Contract** — the declared input and output shape of a workflow.

**Customer** — one of your customers, and the unit your connections and embedded integrations are scoped to. **Tenant** is the same thing under a different name, and both are current vocabulary: _Tenant_ is the column header on all three Triggers tables and the last segment of a connection id, while _Customer_ is what the dashboard screens call it.

**Customer tier** — referred to on the Roles screen as an _embed tier_ under Billing, to which a custom role can be assigned. Beyond that, how tiers behave is not documented here — read the Billing screen before planning around them.

**Deduplication key** — a field in an incoming payload that uniquely identifies an event, so a retried delivery does not run the workflow twice.

**Deploy** — sends a published version to an environment so it handles real events.

**Embed session** — one customer's session inside your embedded widget, opened with an embed token and capped at seven days of refreshing, after which the widget posts `fastn:session-expired` to the parent. A **shareable link** is the alternative way in: created on the widget's Embed tab, and carrying no token — but the reference in the URL is itself the credential, so it is revocable and should be treated as a secret.

**Embed token** — a credential scoping the widget to one customer. Minted at `POST /api/v1/embed/token`, prefixed `emb_`, valid for eight hours.

**Environment** — a deployment stage. `test` and `live` are built in; you can add named ones. In the `x-fastn-env` header, `test` means _latest published version_.

**Escalate on timeout** — on a timeout, retry one tier up (instant → standard). It changes the caller's response shape: instead of an inline result, the caller gets a queued execution id to poll. Hidden on the Long tier, which has nothing above it.

**Event** — one inbound arrival: a webhook fired, a schedule reached, a manual run.

**Execution** — one workflow run, with a status, duration, tier and version.

**Execution mode** — Parallel or Sequential, on a webhook trigger.

**Execution tier** — how long a run may take and whether the caller waits. **Instant** — synchronous, result inline, **30 seconds**. **Standard** — asynchronous, 202, **15 minutes**. **Long** — asynchronous, 202, **36 hours**.

**fastn.db** — SQL inside a workflow, against **your workspace's** own Postgres schema (`ws_<hash>`). The schema isolates your workspace from every other workspace; it does not separate one of your customers from another inside it.

**fastn.state** — durable key-value storage across runs, in scope ORG or INVOCATION.

**fastn.unified** — the runtime handle for [unified APIs](../build/unified-apis.md): call one canonical entity and let fastn route to whichever provider the customer connected.

**Installation** — one customer's set-up of one of your integrations, carrying its own configuration. Identified at runtime by the `x-installation-id` header, alongside `x-fastn-installation-config`.

**MCP access** — reaching your connectors as tools from an AI client. The surface in the product is **Connect to Claude** in the top bar, which supplies an MCP URL and a deep link. See [MCP gateway](../build/mcp-gateway.md).

**Organisation** — you, the SaaS company. Holds connectors, workflows, widgets, people and settings.

**Per customer / workspace** — whether a connector in a workflow uses the running customer's connection or one your organisation owns.

**Platform Admin** — a platform-level role held by fastn, visible in the organisation switcher. Not a role you assign to someone inside your own organisation.

**Publish** — creates an immutable version snapshot (v1, v2, …). Until a workflow has one, every call returns `WORKFLOW_NOT_PUBLISHED`.

**Replay** — re-deliver a past event to its workflow.

**Retry policy** — automatic retries for transient failures. Code errors, data errors and out-of-memory never retry.

**Route** — on a webhook trigger, one destination for an arriving payload. Multiple routes fan out.

**Secret** — an encrypted value read at runtime with `fastn.secrets.get`. Written once and not shown again.

**Sync report** — a record-by-record account of what a run changed. Produced when a workflow calls `fastn.diff.compare`.

**Trace** — a record of the connected-system calls a run made, with durations.

**Trash** — where deleted connectors, actions and workflows are kept until removed permanently. Nothing expires on its own.

**Trigger** — what starts a workflow: webhook, schedule or app event.

**Unified API** — one canonical endpoint per business entity, routed to whichever provider a customer connected.

**Version pin** — holding a specific customer on a specific connector version.

**Widget** — the integrations panel your customers see inside your product.

**Workflow** — the code that runs on a trigger, a schedule, or an agent call.
