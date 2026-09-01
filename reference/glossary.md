---
description: Terms used across fastn, defined once.
---

# Glossary

**Action** — one operation a connector exposes, such as `getSale` or `createOrder`. Actions are versioned and can be pinned per workflow.

**Agent** — fastn's AI builder. Discovers connectors, wires auth, drafts workflows, generates test cases, and shows a diff before anything runs.

**Alert** — a rule that notifies you when a run fails or a metric crosses a threshold. Threshold alerts are evaluated every 15 minutes.

**App event trigger** — starts a workflow when something changes in a connected system.

**Backoff strategy** — how long fastn waits between delivery attempts: Exponential, Linear or Fixed.

**Connection** — one customer's authorised link to one connector. Holds the encrypted credential.

**Connector** — the definition of an external system: actions, auth methods, webhook config, versions. Managed by fastn, or custom.

**Connector update** — a proposed fix for an upstream API change. Nothing applies until you accept it.

**Contract** — the declared input and output shape of a workflow.

**Customer** — one of your customers; an isolated container for their connections and data. Called a *tenant* in older material and some API parameters.

**Customer tier** — a bundle of limits, and optionally a role, that every customer sits on exactly one of.

**Deduplication key** — a field in an incoming payload that uniquely identifies an event, so a retried delivery does not run the workflow twice.

**Embed token** — a short-lived credential scoping the widget to one customer.

**Environment** — a deployment stage. `test` and `live` are built in; you can add named ones. In the `x-fastn-env` header, `test` means *latest published version*.

**Escalate on timeout** — retry one tier up on timeout, with the higher tier's full time budget.

**Event** — one inbound arrival: a webhook fired, a schedule reached, a manual run.

**Execution** — one workflow run, with a status, duration, tier and version.

**Execution tier** — Instant, Standard or Long. Decides whether the caller waits and how long the run may take.

**Execution mode** — Parallel or Sequential, on a webhook trigger.

**fastn.db** — customer-scoped SQL available inside a workflow.

**fastn.state** — durable key-value storage across runs, scoped ORG or INVOCATION.

**MCP gateway** — lets an AI client reach your connectors as tools, scoped by customer, role and action. See [MCP gateway](../build/mcp-gateway.md).

**Organisation** — you, the SaaS company. Holds connectors, workflows, widgets, people and settings.

**Per customer / workspace** — whether a connector in a workflow uses the running customer's connection or one your organisation owns.

**Publish** — creates an immutable version snapshot (v1, v2, …).

**Deploy** — sends a published version to an environment so it handles real events.

**Replay** — re-deliver a past event to its workflow.

**Retry policy** — automatic retries for transient failures. Code errors, data errors and out-of-memory never retry.

**Route** — on a webhook trigger, one destination for an arriving payload. Multiple routes fan out.

**Secret** — an encrypted value read at runtime with `fastn.secrets.get`. Write-once, never displayed.

**Config** — a per-environment value read with `fastn.envConfig.get`. Not encrypted.

**Sync report** — a record-by-record account of what a run changed. Produced when a workflow calls `fastn.diff.compare`.

**Trace** — a record of the connected-system calls a run made, with durations.

**Trash** — where deleted connectors, actions and workflows are kept until removed permanently. Nothing expires on its own.

**Trigger** — what starts a workflow: webhook, schedule or app event.

**Unified API** — one canonical endpoint per business entity, routed to whichever provider a customer connected.

**Version pin** — holding a specific customer on a specific connector version.

**Widget** — the integrations panel your customers see inside your product.

**Workflow** — the code that runs on a trigger, a schedule, or an agent call.
