---
description: Short answers to the questions that come up most.
---

# FAQs

## Getting started

<details>

<summary>Do my customers need a fastn account?</summary>

No. Your customers work through the [widget](../embed/README.md) embedded in your product, authorizing their own accounts there. They reach it with an embed token your backend mints, which carries the role `end_user`, not a fastn login of their own.

</details>

<details>

<summary>Do I have to write workflow code?</summary>

No. [Build with AI](../build/agent/README.md) (or your AI tool) writes workflows from a plain description, and iterates on follow-up messages. Code editing is a per-organization setting that is off by default, so writing the code yourself is the exception rather than the norm. You can still test, wire connectors, edit the contract, publish and deploy. If you want to write code yourself, ask fastn to turn it on for your organization; fastn can enable it for any organization.

</details>

<details>

<summary>What is the difference between a customer and a tenant?</summary>

They are the same thing. *Customer* is what the dashboard calls one of the companies using your product: the Customers screen, the ⌘K search group, the Connections column. *Tenant* survives only in some identifiers and older API material, for example the second segment of a connection id, `ucl:<workspace>:<customer or default>:<connectorId>:<identity>[:<account>]`.

If an identifier says tenant, it means one of your customers.

</details>

---

## Connectors and connections

<details>

<summary>What is the difference between a connector and a connection?</summary>

A **connector** is the definition of an app: its actions, auth methods and webhooks. A **connection** is one customer's authorized link to it, holding the encrypted credential. One connector, many connections.

</details>

<details>

<summary>My customers see "fastn.ai" on the OAuth consent screen. How do I show my own brand?</summary>

Use your own OAuth application. You set it on the connector's **Auth** tab, which is where a connector's auth methods and OAuth providers are configured; there is no separate OAuth apps page in Settings. Register the app in the provider's developer portal first, then configure it on that tab. See [Connectors](../build/connectors/README.md).

</details>

<details>

<summary>A connection says Expired or Failed. Can I fix it from the dashboard?</summary>

Not by re-entering the credential. It belongs to the customer, and they re-authorize through your widget. What the dashboard offers on the row is **Reconnect** and **Disconnect**.

The precise meaning of each status is not documented here; treat *Expired* and *Failed* as "this credential no longer works, ask the customer to reconnect" and read the connection's own **Token and activity** section for `Expires`, `Last refreshed` and `Last used`.

</details>

<details>

<summary>What is a platform-wide connector for?</summary>

Apps your organization owns rather than your customers: your Slack, your warehouse. In a workflow, each connector is wired either **Per customer** or **Platform-wide** (the badge on the workflow's Connectors tab), which decides whose credential the call uses. A platform-wide call uses a connection your organization holds; on that connection's detail page, **Scope** reads `Account level`.

</details>

<details>

<summary>Can I stop one customer taking a connector change?</summary>

Yes. Pin them to a specific connector version under **Version pins** on the connector. Everyone else moves forward.

</details>

---

## Workflows and triggers

<details>

<summary>Which execution tier should I pick?</summary>

| Tier         | Behavior                                        | Maximum      | Timeout slider |
| ------------ | ----------------------------------------------- | ------------ | -------------- |
| **Instant**  | The caller blocks and gets the result inline.    | **25 seconds** | 1s - 25s     |
| **Standard** | Returns 202, runs in the background.             | **15 minutes** | 5s - 15min   |
| **Long**     | Returns 202, runs in the background.             | **Up to 36 hours** | 30s - 36h |

Instant's ceiling is 2 minutes only where fastn has turned on the longer Instant timeout for your organization. **Instant** only when something is genuinely waiting on the answer: 25 seconds is not much once you are calling two apps in sequence. **Standard** for almost everything else. **Long** for batch imports and backfills.

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

No. It retries transient failures. **Code errors, data errors and out-of-memory never retry**: a bug does not get better on the second attempt, and neither does a payload that was always malformed.

</details>

<details>

<summary>I called the API and nothing ran.</summary>

Check whether the workflow has ever been published. Until a snapshot exists, every call returns `WORKFLOW_NOT_PUBLISHED`: the workflow list shows this as status **Unpublished**, with a dash in the **Latest** column. See [HTTP API](api.md).

</details>

---

## Security and access

<details>

<summary>Is a test API key a sandbox?</summary>

No. A test key reaches the same live connections as a live key and causes the same real writes. It is a separate, separately revocable credential, not a safe one. It is also refused unless the caller sends `X-fastn-Test-Mode: true`.

</details>

<details>

<summary>Can I put an API key in my frontend?</summary>

No. Browser-facing widgets use short-lived embed tokens minted by your backend. See [Embedding the widget](../embed/embedding/README.md).

</details>

<details>

<summary>Someone left the team. What do I need to do?</summary>

Remove them under [People](../manage/people.md): their audit history stays. Then check [API keys](../manage/api-keys.md): keys belong to the workspace, not to a person, so removing someone does not revoke keys they created.

</details>

<details>

<summary>Who can read the audit log?</summary>

Account owners and admins only. It is enforced at the API layer and cannot be granted per user.

</details>

<details>

<summary>Can I limit an agent to read-only access for one customer?</summary>

Yes. Combine the action selection on the connector with a narrow API key: pick the **Viewer** preset, or **Custom** with only the read boxes ticked in the `What it can touch` matrix, and set **Customers it can reach** to **Only the ones I pick**. See [API keys](../manage/api-keys.md).

</details>

---

## Data and limits

<details>

<summary>Where does `fastn.db` data actually live?</summary>

In fastn's shared managed Postgres by default, in a schema isolated to your workspace. You can point it at a Postgres you operate instead, under [Settings → Database](../manage/database.md). Rows are never copied between the two, so switching changes where new reads and writes go and nothing else.

</details>

<details>

<summary>Secret or config?</summary>

Secret if exposure would be an incident (tokens, passwords, keys). Config if you would happily show it to a colleague (endpoints, feature flags, batch sizes). When in doubt, secret.

</details>

<details>

<summary>What happens when I hit a plan limit?</summary>

New work stops rather than being charged for, and nothing already running is interrupted. Check [Billing](../manage/billing.md): a sync that stops because of a quota looks exactly like a broken sync until you do.

Customer connections are the exception on Scale: past the 10 included, each extra one is billed at $50 a month and is never refused. On Launch, the fourth customer connection is refused.

</details>

<details>

<summary>I deleted something by mistake.</summary>

Connectors, connector actions and workflows are in [Trash](../manage/trash.md) and restore with slug and history intact. Other resources (widgets and their integrations among them), are deleted immediately and cannot be restored from that page.

</details>

---

## Things that look broken

<details>

<summary>Why does the same connector appear twice in the catalog?</summary>

Because two entries exist for one app: typically one badged **managed** and one badged **Custom**. Asana, HubSpot, Salesforce, Slack, Notion and Cin7 Core all show up this way.

The practical consequence: the connector count is a count of *entries*, not of distinct apps, so the total on the Connectors page is not a count of distinct products. Check the badge and the provenance line before you connect, so you do not authorize the copy you did not mean.

</details>

---

## Still stuck

Work through [Troubleshooting](../operate/troubleshooting.md). It is organized by symptom.
