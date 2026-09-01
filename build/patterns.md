---
description: The handful of workflow shapes that come up again and again.
---

# Common patterns

You can describe any of these to the [agent](agent.md) in a sentence. They are here so you know what to ask for, and what the result should look like.

Every one of them ends up as JavaScript in a workflow's `<slug>.js`. The runtime surfaces they use — `fastn.state` (scopes `ORG` and `INVOCATION`), `fastn.db`, `fastn.secrets`, `fastn.envConfig`, `fastn.unified`, `fastn.connector` — are listed on the editor's **Docs** tab; check the exact method signatures there before copying a snippet, since they are the authority and this page is a sketch.

---

## Idempotent event sync

**The problem.** A webhook fires, the workflow writes a record. The sender retries, or someone replays the event, and you have two records.

**The shape.** Three defences, cheapest first.

1. A **deduplication key** on the [trigger](triggers.md) — the field in the payload that identifies the event, so a retried delivery does not run the workflow twice.
2. An **idempotency guard** in the workflow, using `fastn.state`:

   ```javascript
   const seen = await fastn.state.get(`deal:${dealId}`);
   if (seen) return { success: true, skipped: true, reason: "already_processed" };
   // … do the work …
   await fastn.state.set(`deal:${dealId}`, { processedAt: new Date().toISOString() });
   ```
3. **Sequential execution mode** on the trigger, if two concurrent events for the same record could race.

**Ask for it as:** *"Make this idempotent — if the same order comes in twice, only create it once."*

---

## Change detection with a hash

**The problem.** A scheduled sync pulls 5,000 records every hour and rewrites all of them, most of which have not changed.

**The shape.** Hash the fields you care about, store the hash in `fastn.state` keyed by record id, and skip when it matches. Only changed records reach the destination.

The cost is one state read per record instead of one write to the destination, which is almost always the cheaper of the two.

**Ask for it as:** *"Only write records whose fields actually changed since the last run."*

---

## Two-stage sync for large volumes

**The problem.** A single run has to pull a large dataset and push it, and it either times out or hammers the destination's rate limit.

**The shape.** Split it.

| Stage           | Does                                                         | Tier             |
| --------------- | -------------------------------------------------------------- | ---------------- |
| **Ingestion**   | Pulls from the source into `fastn.db`.                        | Long             |
| **Publishing**  | Pushes stored records to the destination in batches.          | Standard         |

Each stage retries independently, and a failure in publishing does not mean re-pulling everything. It also gives you a table you can query when someone asks what was actually fetched.

**Ask for it as:** *"Pull into the database first, then push in batches of 200."*

---

## Per-customer business rules

**The problem.** Every customer wants a slightly different filter — a category, a threshold, a warehouse — and you do not want a code change per customer.

**The shape.** Put the rule in configuration rather than code. The workflow reads it at runtime, so changing a customer's rule is an edit, not a deploy.

| The rule is…                        | Put it in                                                              | Read it with          |
| ----------------------------------- | ------------------------------------------------------------------------ | --------------------- |
| Structured, and differs per customer | A table in [`fastn.db`](../manage/database.md), with a tenant column   | `fastn.db.query`      |
| Sensitive, and differs per customer  | A [secret](../manage/secrets.md) scoped to that customer                | `fastn.secrets.get`   |
| The same for everyone, but differs between test and live | A [config](../manage/configs.md)                    | `fastn.envConfig.get` |

Configs vary by *environment*, not by customer — so a per-customer rule belongs in the database or in a customer-scoped secret, not in a config.

{% hint style="warning" %}
`fastn.db` isolates one Postgres schema **per workspace**, not per customer. Rows are not scoped to a customer for you. If a table holds per-customer rules, put the customer on the row yourself and filter on it in every query.
{% endhint %}

Which customer a run belongs to arrives in the request headers — `x-end-org-id`, `x-end-org-ref`, `x-installation-id`, `x-fastn-connections`, `x-fastn-installation-config` — and reaches your code through `ctx.headers`. That is also how you invoke a workflow as a specific customer from outside.

**Ask for it as:** *"Make the warehouse and the minimum order value configurable per customer, not hard-coded."*

---

## Fan-out from one webhook

**The problem.** One inbound event needs to do three unrelated things — create an invoice, notify Slack, update a sheet.

**The shape.** One webhook trigger, three [routes](triggers.md). Each route names its own workflow, and they run independently, so a Slack outage does not stop the invoice.

Prefer this over one workflow that does all three. Three workflows means three execution records, three retry policies, and a failure you can read at a glance.

**Ask for it as:** *"Fan this webhook out to three workflows."*

---

## Backfill without disturbing the live sync

**The problem.** You need to load two years of history, and the hourly sync must keep running.

**The shape.** A separate workflow on the **Long** tier, triggered manually or by API rather than by a schedule.

The guard has to be somewhere both workflows can see. A table in `fastn.db` is the safe choice: the live sync records what it has written, the backfill checks that table before writing, and neither redoes the other's work. `fastn.state` has two scopes, `ORG` and `INVOCATION` — `INVOCATION` is definitively too narrow, and if you intend to lean on `ORG` reaching across two different workflows, confirm that on the editor's Docs tab first rather than assuming it from the name.

```javascript
const done = await fastn.db.query(
  `SELECT 1 FROM synced_orders WHERE source_id = $1`, [order.id]
);
if (done.rows.length) return { skipped: true };
```

Run it against one customer first, and read the [sync report](../operate/sync-reports.md) before running it against everyone.

**Ask for it as:** *"A one-off backfill for the last two years, safe to run alongside the hourly sync."*

---

## Workspace-level notifications

**The problem.** You want failures posted to *your* Slack, not the customer's.

**The shape.** Use a Slack connection your organisation owns — one created from **New connection** and scoped `Account level` — rather than one belonging to a customer. On the workflow's [Connectors tab](workflows.md) it is the row *without* a **Per customer** badge, so it behaves the same no matter whose data is being processed.

For failure notification specifically, an [alert](../operate/alerts.md) with a Slack destination is simpler than building it into the workflow — and it also catches the case where the workflow itself never ran.

---

## Let the platform retry before you write retry code

**The problem.** A destination is flaky, and the workflow is growing a hand-rolled retry loop.

**The shape.** Turn on **Retry policy** in the workflow's configuration panel instead. It gives you `Max attempts` (1–10, default 3), `Initial interval (ms)` (5000), `Backoff coefficient` (2) and `Max interval (ms)` (60000), applied to the run as a whole.

Know its boundary: it retries transient failures. Code errors, data errors and out-of-memory never retry, so a bug will not be papered over by attempt three.

If the failure is a timeout rather than a rejection, **Escalate on timeout** retries one tier up — instant → standard — and the escalated instant run returns a queued execution id to poll instead of a synchronous result. The toggle is hidden on the Long tier, which has nowhere further to go.

**Ask for it as:** *"Retry this three times with backoff if the destination is down."*

---

## One code path across three CRMs

**The problem.** Customer A is on HubSpot, B on Salesforce, C on Zoho, and the workflow has grown a branch per vendor for what is one operation.

**The shape.** Call the [unified API](unified-apis.md) through `fastn.unified` instead of the individual connectors, and let fastn route to whichever provider that customer authorised. `/api/v1/unified/crm/contact` is the same call regardless of the stack underneath.

Keep the vendor-specific parts on the direct connector — the two mix freely in one workflow. Watch the entity limits: `Note`, `Channel Message` and `Direct Message` are create-only.

**Ask for it as:** *"Create the contact through the unified CRM endpoint, not through HubSpot directly."*

---

## Reconciliation

**The problem.** Everything reports success and the two systems still disagree.

**The shape.** A nightly workflow that reads counts or checksums from both sides and writes the difference to `fastn.db`, plus an [alert](../operate/alerts.md) on **Records failed above 0**.

It is the pattern people add after the first silent divergence. It is cheaper to add before.

**Ask for it as:** *"A nightly check that both systems have the same number of open orders, and tell me when they don't."*
