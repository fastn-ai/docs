---
description: Short answers to the questions that come up most.
---

# FAQs

## Getting started

<details>

<summary>Do my customers need a fastn account?</summary>

No. Your customers only ever see the [widget](../embed/README.md) embedded in your product. They authorise their own accounts there and never sign in to fastn.

</details>

<details>

<summary>Do I have to write workflow code?</summary>

No. The [agent](../build/agent.md) writes workflows from a plain description, and iterates on follow-up messages. Some workspaces have code editing switched off entirely — you can still test, wire connectors and edit the contract. It can be switched on if you want to write code yourself; ask fastn to enable it.

</details>

<details>

<summary>What is the difference between a customer and a tenant?</summary>

Nothing. *Tenant* is the older name, still used in some API parameters and in the V1 documentation. Both mean one isolated container for a customer's connections and data.

</details>

---

## Connectors and connections

<details>

<summary>What is the difference between a connector and a connection?</summary>

A **connector** is the definition of a system — its actions, auth methods and webhooks. A **connection** is one customer's authorised link to it, holding the encrypted credential. One connector, many connections.

</details>

<details>

<summary>My customers see "fastn.ai" on the OAuth consent screen. How do I show my own brand?</summary>

Register your own OAuth app for that connector under its **Auth** tab. Until you do, the consent screen shows fastn.ai. See [Connectors](../build/connectors.md).

</details>

<details>

<summary>A connection says Expired or Failed. Can I fix it from the dashboard?</summary>

No, and that is deliberate — the credential belongs to the customer. They re-authorise through your widget. Expired means the credential ran out and could not be refreshed; Failed means the last verification was rejected, usually revoked access or a rotated key.

</details>

<details>

<summary>What is a workspace connection for?</summary>

Systems your organisation owns rather than your customers — your Slack, your warehouse. In a workflow, each connector is wired either **per customer** or **workspace**, which decides whose credential the call uses.

</details>

<details>

<summary>Can I stop one customer taking a connector change?</summary>

Yes. Pin them to a specific connector version under **Version pins** on the connector. Everyone else moves forward.

</details>

---

## Workflows and triggers

<details>

<summary>Which execution tier should I pick?</summary>

**Instant** only when something is waiting on the answer — the caller blocks, up to 2 minutes. **Standard** for almost everything else; it returns 202 and runs in the background, up to 15 minutes. **Long** for batch imports and backfills, up to 6 hours.

</details>

<details>

<summary>Why don't my test runs appear in Executions?</summary>

By design. Test runs from a workflow's own Run Live button execute without saving and are not recorded — the [Executions](../operate/executions.md) log is the record of real traffic.

</details>

<details>

<summary>What is the difference between Publish and Deploy?</summary>

**Publish** creates an immutable version snapshot (v1, v2, …). **Deploy** sends a published version to an environment so it starts handling real events. Rollback is just deploying an earlier version.

</details>

<details>

<summary>What does `test` mean in the environment dropdown?</summary>

`test` runs the workflow's latest published version. Any named environment runs the version deployed *there*, and the fire fails if nothing is deployed to it.

</details>

<details>

<summary>How do I stop duplicate records after a replay?</summary>

Set a **deduplication key** on the webhook trigger, and add an idempotency guard using `fastn.state` in the workflow. See [Common patterns](../build/patterns.md).

</details>

<details>

<summary>Does a retry policy retry everything?</summary>

No. It retries transient failures — and timeouts as well, when **Escalate on timeout** is off. Code errors, data errors and out-of-memory never retry.

</details>

---

## Security and access

<details>

<summary>Is a test API key a sandbox?</summary>

No. A test key reaches the same live connections as a live key and causes the same real writes. It is a separate, separately revocable credential — not a safe one. It is also refused unless the caller sends `X-fastn-Test-Mode: true`.

</details>

<details>

<summary>Can I put an API key in my frontend?</summary>

No. Browser-facing widgets use short-lived embed tokens minted by your backend. See [Embedding the widget](../embed/embedding.md).

</details>

<details>

<summary>Someone left the team. What do I need to do?</summary>

Remove them under [People](../manage/people.md) — their audit history stays. Then check [API keys](../manage/api-keys.md): keys belong to the workspace, not to a person, so removing someone does not revoke keys they created.

</details>

<details>

<summary>Who can read the audit log?</summary>

Account owners and admins only. It is enforced at the API layer and cannot be granted per user.

</details>

<details>

<summary>Can I limit an agent to read-only access for one customer?</summary>

Yes — that is what the action checkboxes on a connector are for, combined with a narrow role on the API key. See [MCP gateway](../build/mcp-gateway.md).

</details>

---

## Data and limits

<details>

<summary>Where does `fastn.db` data actually live?</summary>

In fastn's shared managed Postgres by default, in a schema isolated to your workspace. You can point it at a Postgres you operate instead, under [Settings → Database](../manage/database.md). Rows are never copied between the two, so switching changes where new reads and writes go and nothing else.

</details>

<details>

<summary>Secret or config?</summary>

Secret if exposure would be an incident — tokens, passwords, keys. Config if you would happily show it to a colleague — endpoints, feature flags, batch sizes. When in doubt, secret.

</details>

<details>

<summary>What happens when I hit a plan limit?</summary>

New work stops rather than being charged for, and nothing already running is interrupted. Check [Billing](../manage/billing.md) — a sync that stops because of a quota looks exactly like a broken sync until you do.

</details>

<details>

<summary>I deleted something by mistake.</summary>

Connectors, connector actions and workflows are in [Trash](../manage/trash.md) and restore with slug and history intact. Widgets, customers, connections, triggers and secrets are deleted immediately and cannot be restored.

</details>

---

## Still stuck

Work through [Troubleshooting](../operate/troubleshooting.md) — it is organised by symptom.
