---
description: Symptom, where to look, and what usually fixes it.
---

# Troubleshooting

Work down this page in order. Most problems resolve at the first or second step, and each step tells you which screen holds the answer.

### Start here

| Symptom                                       | Look first at                                         |
| --------------------------------------------- | ------------------------------------------------------- |
| Nothing happened at all                       | [Events](events.md) — did anything arrive?             |
| Something ran but ended badly                 | [Executions](executions.md) — what status?             |
| It succeeded but the data is wrong            | [Sync reports](sync-reports.md)                        |
| It is slow                                    | [Traces](traces.md)                                    |
| It worked yesterday and not today             | [Connections](../build/connections.md), then [Connector updates](../build/connector-updates.md) |
| One customer is affected, others are not      | [Connections](../build/connections.md), scoped to that customer |

---

## Nothing ran

### No event in the log

If [Events](events.md) shows nothing, the problem is before fastn.

| Trigger type  | Check                                                                                       |
| ------------- | --------------------------------------------------------------------------------------------- |
| **Webhook**   | Is the sending system pointed at the right URL? Does it require the `x-fastn-access-key` header, and is the sender sending it? |
| **Schedule**  | Is the trigger Active rather than Disabled? Is its timezone what you assumed?                |
| **App event** | Is the connector's **Webhook config** set up, and does the customer have an active connection? |

Filter the Events chips by **Scheduled** — a count of zero on a schedule you expected to fire is the answer.

### Event Delivered, but no execution

A Delivered event means the payload arrived and was handed on. If no execution followed:

* The workflow is **disabled**. Check the Status toggle in its Configuration panel.
* The trigger route points at an environment with **nothing deployed to it**. A named environment runs the version deployed there, and the fire fails if nothing is. Either deploy, or point the route at `test`, which runs the latest published version.

### Event never Delivered

It exhausted its delivery attempts and is parked under **Failed deliveries**. Fix the cause, then **Replay**. Attempt count and backoff are on the webhook trigger — see [Triggers](../build/triggers.md).

---

## It ran and failed

### Status: Failed

Open the execution for the error and logs, then check [Traces](traces.md) for the call that was rejected. The usual causes, in order of frequency:

1. **The connection is Expired or Failed.** The customer re-authorises through your widget.
2. **The upstream API changed.** Check [Connector updates](../build/connector-updates.md) for a proposal against that connector.
3. **The data did not match the contract.** A field the mapping expects is absent or the wrong type.
4. **A permission is missing.** The customer's OAuth grant may not cover the scope the action needs.

### Status: Timeout

The tier's budget ran out. Before raising the timeout, open [Traces](traces.md):

* **One slow call** — the fix is upstream, or batching, not a longer timeout.
* **Hundreds of calls** — batch them, or move to the Long tier.
* **A Pending trace that never resolved** — the upstream system accepted the request and never answered.

**Escalate on timeout** retries one tier up with the higher tier's full budget, which buys time without redesigning. It is subject to your plan.

### Status: Queued for a long time

You are probably at the concurrent-workflows cap. Check [Billing](../manage/billing.md).

### Retries that look like repeated failures

With a retry policy on, each attempt is a separate execution. A cluster of failures ending in a success is the policy working.

The policy retries transient failures, and timeouts too when **Escalate on timeout** is off. Code errors, data errors and out-of-memory never retry, however many attempts you allow.

---

## It succeeded but the data is wrong

Open [Sync reports](sync-reports.md). It shows what the run created, updated, skipped and rejected, record by record — which distinguishes *the record was filtered out* from *the record was never seen*.

If the page is empty, the workflow does not call `fastn.diff.compare`. Ask the agent to add diff reporting; reconstructing this from logs afterwards is far harder.

Common causes:

| Cause                     | Where to fix it                                                        |
| ------------------------- | ------------------------------------------------------------------------ |
| A field was never mapped  | The workflow's field mappings — tell the agent what is missing.        |
| A filter is too broad     | The include/exclude rules in the workflow.                             |
| Duplicates downstream     | No deduplication key on the trigger, or no `fastn.state` idempotency guard. |
| Stale values              | A pinned connector version that predates a field. See Version pins on the connector. |

---

## Duplicates after a replay

Replay re-runs the workflow for real. Without protection it will write twice.

Two defences, and you want both:

1. A **deduplication key** on the webhook trigger — a field that uniquely identifies each event, so a retried delivery from the sender does not run the workflow twice.
2. An **idempotency guard** in the workflow using `fastn.state`:

```javascript
const seen = await fastn.state.get(`deal:${dealId}`);
if (seen) return { success: true, skipped: true, reason: "already_processed" };
```

See [Workflow runtime API](../reference/workflow-runtime.md).

---

## It works for one customer and not another

Almost always a connection. Open [Connections](../build/connections.md) — the Customer column tells you whose each one is, and the search box narrows the list.

| Status       | Fix                                                          |
| ------------ | -------------------------------------------------------------- |
| **Expired**  | The customer re-authorises through your widget.               |
| **Failed**   | Access was revoked, a password changed, or a key was rotated. Same fix. |
| **Inactive** | Re-enable from the row menu.                                  |
| Missing      | They never connected that system.                             |

Also check whether that customer is **pinned to an older connector version**, and whether their [customer tier](../manage/billing.md) has a limit they have hit.

---

## API calls are rejected

| Response                       | Cause                                                                            |
| ------------------------------ | ---------------------------------------------------------------------------------- |
| Rejected with a test key       | Missing `X-fastn-Test-Mode: true`. A test key is refused without it.             |
| Rejected with a live key       | Sending `X-fastn-Test-Mode: true` with an `fsk_live_` key. Drop the header.      |
| Wrong code ran                 | `x-fastn-env`. `test` means the latest published version; any other slug means the version deployed there. |
| Empty `ctx.input`              | The body is missing its `input` wrapper. Copy the curl from the workflow's API tab. |
| Forbidden                      | The key's role does not carry the permission. See [Roles](../manage/roles.md).   |

---

## Everything stopped at once

Check [Billing](../manage/billing.md). Going over a limit stops new work rather than charging you, and nothing already running is interrupted — which reads exactly like a broken platform until you look at the usage figures. The page flags how many limits are close enough to matter, so it is a quick scan rather than a full read.

---

## You deleted something by mistake

Connectors, connector actions and workflows go to [Trash](../manage/trash.md) and restore with slug and history intact. Widgets, customers, connections, triggers and secrets are deleted immediately and cannot be restored.

---

## Making the next one easier

| Do this once                                                  | Saves you                                     |
| ------------------------------------------------------------- | ----------------------------------------------- |
| **Turn on failure alerts** on [Alerts](alerts.md)             | Finding out from a customer                    |
| Add an alert on **Broken connectors above 0**                 | Expired credentials going unnoticed            |
| Add an alert on **Total runs below 1 over 24 hours**          | A schedule that silently stopped               |
| Set a **deduplication key** on every webhook trigger          | Duplicate records after any replay             |
| Add `fastn.diff.compare` to every sync                        | Reconstructing a run from logs                 |
