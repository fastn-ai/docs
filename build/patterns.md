---
description: The handful of workflow shapes that come up again and again.
---

# Common patterns

You can describe any of these to the [agent](agent.md) in a sentence. They are here so you know what to ask for, and what the result should look like.

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
| Structured, and differs per customer | A table in [`fastn.db`](../manage/database.md) — customer-scoped automatically | `fastn.db.query`   |
| Sensitive, and differs per customer  | A [secret](../manage/secrets.md) scoped to that customer                | `fastn.secrets.get`   |
| The same for everyone, but differs between test and live | A [config](../manage/configs.md)                    | `fastn.envConfig.get` |

Configs vary by *environment*, not by customer — so a per-customer rule belongs in the database or in a customer-scoped secret, not in a config.

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

The guard has to be somewhere both workflows can see. `fastn.state` will not do it — its default ORG scope is shared across runs of *the same workflow*, not between two different ones. Use a table in `fastn.db` instead: the live sync records what it has written, the backfill checks that table before writing, and neither redoes the other's work.

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

**The shape.** Wire the Slack connector as **workspace** rather than **per customer** on the workflow's [Connectors tab](workflows.md). It then uses a connection your organisation owns, so it behaves the same no matter whose data is being processed.

For failure notification specifically, an [alert](../operate/alerts.md) with a Slack destination is simpler than building it into the workflow — and it also catches the case where the workflow itself never ran.

---

## Reconciliation

**The problem.** Everything reports success and the two systems still disagree.

**The shape.** A nightly workflow that reads counts or checksums from both sides and writes the difference to `fastn.db`, plus an [alert](../operate/alerts.md) on **Records failed above 0**.

It is the pattern people add after the first silent divergence. It is cheaper to add before.

**Ask for it as:** *"A nightly check that both systems have the same number of open orders, and tell me when they don't."*
