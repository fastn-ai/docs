---
description: Short answers to the questions that come up most.
---

# FAQs

## Getting started

<details>

<summary>Do my customers need a fastn account?</summary>

No. Your customers work through the [widget](../embed/README.md) embedded in your product, authorising their own accounts there. They reach it with an embed token your backend mints, which carries the role `end_user` — not a fastn login of their own.

</details>

<details>

<summary>Do I have to write workflow code?</summary>

No. The [agent](../build/agent.md) writes workflows from a plain description, and iterates on follow-up messages. Some workspaces have code editing switched off entirely — you can still test, wire connectors and edit the contract. It can be switched on if you want to write code yourself; ask fastn to enable it.

</details>

<details>

<summary>What is the difference between a customer and a tenant?</summary>

They are the same thing under two names, and **both are current**. *Customer* is what the dashboard calls it — the Customers screen, the ⌘K search group, the Connections column. *Tenant* is what the plumbing calls it: it is the column header on all three Triggers tables, and the last segment of a connection id, `ucl:org_<org>:<env>:<connectorId>:<authId>:<tenant>`.

So do not read *tenant* as legacy vocabulary you can ignore. If a screen or an identifier says tenant, it means one of your customers.

</details>

---

## Connectors and connections

<details>

<summary>What is the difference between a connector and a connection?</summary>

A **connector** is the definition of a system — its actions, auth methods and webhooks. A **connection** is one customer's authorised link to it, holding the encrypted credential. One connector, many connections.

</details>

<details>

<summary>My customers see "fastn.ai" on the OAuth consent screen. How do I show my own brand?</summary>

Start on the connector's **Auth** tab, which is where a connector's OAuth providers are configured — it shows the auth methods and a providers list. Whether that lets you register your own OAuth application, and what the consent screen then shows, is not something this page can confirm; check the tab for your connector, and ask fastn if it is not there. See [Connectors](../build/connectors.md).

</details>

<details>

<summary>A connection says Expired or Failed. Can I fix it from the dashboard?</summary>

Not by re-entering the credential — it belongs to the customer, and they re-authorise through your widget. What the dashboard offers on the row is **Reconnect** and **Disconnect**.

The precise meaning of each status is not documented here; treat *Expired* and *Failed* as "this credential no longer works, ask the customer to reconnect" and read the connection's own **Token and activity** section for `Expires`, `Last refreshed` and `Last used`.

{% hint style="warning" %}
The **Active** / **Inactive** / **Expired** / **Failed** filter chips on the Connections tab currently return zero rows whichever one you pick, even when every row in the unfiltered list shows Active. Do not conclude from an empty filtered list that you have no connections in that state — clear the filter and read the Status column.
{% endhint %}

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

| Tier         | Behaviour                                       | Maximum      | Timeout slider |
| ------------ | ----------------------------------------------- | ------------ | -------------- |
| **Instant**  | The caller blocks and gets the result inline.    | **30 seconds** | 1s – 30s     |
| **Standard** | Returns 202, runs in the background.             | **15 minutes** | 5s – 15min   |
| **Long**     | Returns 202, runs in the background.             | **36 hours**   | 30s – 36h    |

**Instant** only when something is genuinely waiting on the answer — 30 seconds is not much once you are calling two systems in sequence. **Standard** for almost everything else. **Long** for batch imports and backfills.

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

No. It retries transient failures. **Code errors, data errors and out-of-memory never retry** — a bug does not get better on the second attempt, and neither does a payload that was always malformed.

</details>

<details>

<summary>I called the API and nothing ran.</summary>

Check whether the workflow has ever been published. Until a snapshot exists, every call returns `WORKFLOW_NOT_PUBLISHED` — the workflow list shows this as status **Not published** and latest version **Unpublished**. See [HTTP API](api.md).

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

Secret if exposure would be an incident — tokens, passwords, keys. Config if you would happily show it to a colleague — endpoints, feature flags, batch sizes. When in doubt, secret.

</details>

<details>

<summary>What happens when I hit a plan limit?</summary>

New work stops rather than being charged for, and nothing already running is interrupted. Check [Billing](../manage/billing.md) — a sync that stops because of a quota looks exactly like a broken sync until you do.

</details>

<details>

<summary>I deleted something by mistake.</summary>

Connectors, connector actions and workflows are in [Trash](../manage/trash.md) and restore with slug and history intact. Other resources — widgets and their integrations among them — are deleted immediately and cannot be restored from that page.

</details>

---

## Things that look broken

<details>

<summary>Why does the same connector appear twice in the catalogue?</summary>

Because two entries exist for one system — typically one badged **managed** and one badged **Custom**. Asana, HubSpot, Salesforce, Slack, Notion and Cin7 Core all show up this way.

The practical consequence: the connector count is a count of *entries*, not of distinct systems, so "156 connectors" is not 156 different products. Check the badge and the provenance line before you connect, so you do not authorise the copy you did not mean.

</details>

<details>

<summary>A connector says Connected but its detail page says 0 connections.</summary>

That is a known inconsistency between the list badge and the detail page's count, not a lost connection. Confirm on the [Connections](../build/connections.md) tab, which lists actual connections with their customer and status.

</details>

<details>

<summary>A connector shows "Created: Invalid Date".</summary>

A display defect in the Overview tab's Created row. It says nothing about the connector's health.

</details>

<details>

<summary>The Trash Actions tab never finishes loading.</summary>

Known: the **Actions** tab on [Trash](../manage/trash.md) sits on *Loading deleted actions…* and does not resolve. The Connectors and Workflows tabs work normally.

</details>

<details>

<summary>The Connections status filters return nothing.</summary>

Also known — every status chip returns zero rows. Clear the filter and read the Status column instead.

</details>

---

## Still stuck

Work through [Troubleshooting](../operate/troubleshooting.md) — it is organised by symptom.
