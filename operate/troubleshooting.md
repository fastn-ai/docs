---
description: Symptom, where to look, and what usually fixes it.
---

# Troubleshooting

Find your symptom in the table below, then go to its section. Each section names the screen that holds the answer.

### Start here

| Symptom                                       | Look first at                                         |
| --------------------------------------------- | ------------------------------------------------------- |
| Nothing happened at all                       | [Events](events.md): did anything arrive?             |
| Something ran but ended badly                 | [Executions](executions.md): expand the row, read the **Error** tab. Codes explained in [Errors and failure states](../reference/errors.md) |
| It succeeded but the data is wrong            | [Sync reports](sync-reports.md)                        |
| It is slow                                    | [Traces](traces.md) (open `/activity/traces` directly) |
| It worked yesterday and not today             | [Connections](../build/connections/README.md), then [Pending updates](../build/connector-updates.md) |
| One customer is affected, others are not      | [Connections](../build/connections/README.md), scoped to that customer |

---

## Nothing ran

### No event in the log

If [Events](events.md) shows nothing, the problem is before fastn.

| Trigger type  | Check                                                                                       |
| ------------- | --------------------------------------------------------------------------------------------- |
| **Webhook**   | Is the sending system pointed at the right URL? If the trigger's auth is API key, is the sender sending the key in the `x-api-key` header, or as `Authorization: Bearer fsk_…`? (`x-fastn-access-key` is still accepted. `x-fastn-api-key` is not read.) |
| **Schedule**  | Is the trigger Active rather than Disabled? Is its timezone what you assumed?                |
| **App event** | Is the connector's **Webhook config** set up, and does the customer have an active connection? |

Filter the Events chips by **Scheduled**: a count of zero on a schedule you expected to fire is the answer.

### Event Delivered, but no execution

A Delivered event means the payload arrived and was handed on. If no execution followed:

* **The workflow was never published.** Every call returns `WORKFLOW_NOT_PUBLISHED` until a snapshot is published, so nothing runs and nothing appears in Executions. The workflows list shows its status as **Unpublished**, with "-" in the version cell (its tooltip reads "No published version yet."). This is the likeliest cause of *nothing ran at all*. Publish a snapshot from the editor.
* The workflow is **disabled**. Check the Status toggle in its Configuration panel.
* The trigger route points at an environment with **nothing deployed to it**. A named environment runs the version deployed there, and the fire fails if nothing is. Either deploy, or point the route at `test`, which runs the latest published version.

### Event never Delivered

It exhausted its delivery attempts. The row shows a failure state in the **Status** column; fix the cause, then **Replay** it. Attempt count and backoff are on the webhook trigger. See [Triggers](../build/triggers/README.md).

---

## It ran and failed

### Status: Failed

Expand the execution row and open the **Error** tab (**AI Diagnosis** and **Error Details**), then check [Traces](traces.md) for the call that was rejected. The usual causes, in order of frequency:

1. **The connection is Expired or Failed.** The customer re-authorizes through your widget.
2. **The upstream API changed.** Check [Pending updates](../build/connector-updates.md) for a proposal against that connector.
3. **The data did not match the contract.** A field the mapping expects is absent or the wrong type.
4. **A permission is missing.** The customer's OAuth grant may not cover the scope the action needs.

### Status: Failed with a `Dependency Error` tag

This is the most common failure. It means a system the workflow *called* rejected the request. The cause is almost always a connector action, not your code. These runs usually stop in under a second, at the first call that fails.

Expand the row and open the **Error** tab. The **AI Diagnosis** names the step that broke and, usually, the fix; **Error Details** beside it carries the raw message. Most of the time the answer is a connection that is expired, revoked, pinned to something unusable, or belonging to another organization.

**It will not clear on its own.** Retry policies cover transient failures, and an invalid connection is not transient: a daily schedule in this state fails at the same minute every day until someone acts.

Full breakdown, with the causes in order of frequency, in [Errors and failure states](../reference/errors.md#dependency-error).

### Status: Timed out

The tier's budget ran out. Before raising the timeout, open [Traces](traces.md):

* **One slow call**: the fix is upstream, or batching, not a longer timeout.
* **Hundreds of calls**: batch them, or move to the Long tier.
* **A Pending trace that never resolved**: the upstream system accepted the request and never answered.

**Escalate on timeout** (in the workflow's settings) retries a timed-out run one tier up, Instant to Standard or Standard to Long, with the higher tier's full time budget. It buys time without redesigning, subject to your plan. The option isn't available on the Long tier, which has nothing above it.

{% hint style="warning" %}
With this on, an Instant run that times out and escalates returns a queued execution id to poll instead of the result, so your caller must handle both responses.
{% endhint %}

### Status: Failed with a `Memory Limit` tag, or no obvious error

A run that ran out of memory carries a `Memory Limit` tag in the Executions list, and **Error Details** on its **Error** tab names the limit it exceeded: `Execution exceeded the <N>MB sandbox memory limit`.

To confirm, or when a failed run has no tag, expand the row and compare two fields:

* `peakSandboxMB`: the most memory the run was seen using. It is sampled during the run, so the true peak can be a little higher.
* `sandboxMemoryLimitMB`: the memory limit the run ran under.

If `peakSandboxMB` is at or near `sandboxMemoryLimitMB`, the run ran out of memory. Fetch less data per call and process smaller batches. Out-of-memory never retries, so a run that hit the limit simply stops rather than recovering on the next attempt.

### Retries

The retry policy retries transient failures. Code errors, data errors and out-of-memory never retry, however many attempts you allow, so if the same run fails identically every time, the policy is not the thing to adjust.

---

## It succeeded but the data is wrong

Open [Sync reports](sync-reports.md). It shows what the run did, record by record, which distinguishes *the record was filtered out* from *the record was never seen*.

If the page is empty, the workflow does not call `fastn.diff.compare`. Ask Build with AI (or your AI tool) to add diff reporting; reconstructing this from logs afterwards is far harder.

Common causes:

| Cause                     | Where to fix it                                                        |
| ------------------------- | ------------------------------------------------------------------------ |
| A field was never mapped  | The workflow's field mappings: tell Build with AI (or your AI tool) what is missing. |
| A filter is too broad     | The include/exclude rules in the workflow.                             |
| Duplicates downstream     | No deduplication key on the trigger, or no `fastn.state` idempotency guard. |
| Stale values              | A pinned connector version that predates a field. See Version pins on the connector. |

---

## Duplicates after a replay

Replay re-runs the workflow for real. Without protection it will write twice.

Two defenses, and you want both:

1. A **deduplication key** on the webhook trigger: a field that uniquely identifies each event, so a retried delivery from the sender does not run the workflow twice.
2. An **idempotency guard** in the workflow using `fastn.state`:

```javascript
const seen = await fastn.state.get(`deal:${dealId}`);
if (seen) return { success: true, skipped: true, reason: "already_processed" };
```

See [Workflow runtime API](../reference/workflow-runtime.md).

---

## It works for one customer and not another

Almost always a connection. Open [Connections](../build/connections/README.md) in its **Customers** view: the Customer column tells you whose each one is, and the search box narrows the list.

| Status       | Fix                                                          |
| ------------ | -------------------------------------------------------------- |
| **Expired**  | The customer re-authorizes through your widget.               |
| **Failed**   | Access was revoked, a password changed, or a key was rotated. Same fix. |
| **Inactive** | The row menu offers **Reconnect**, **Rename** and **Disconnect**. There is no re-enable: reconnect it. |
| Missing      | They never connected that system.                             |

The **Needs action** status chip lists every connection that needs someone to act.

Also check whether that customer is **pinned to an older connector version**. See Version pins on the connector.

---

## API calls are rejected

| Response                       | Cause                                                                            |
| ------------------------------ | ---------------------------------------------------------------------------------- |
| `WORKFLOW_NOT_PUBLISHED`       | No snapshot has been published for that workflow. Publish one from the editor.   |
| Rejected with a test key       | Missing `X-fastn-Test-Mode: true`. A test key is refused without it.             |
| Wrong code ran                 | `x-fastn-env`. `test` means the latest published version; any other slug means the version deployed there. |
| Forbidden                      | The key's permissions do not cover the call. Key permissions are a preset plus a **What it can touch** matrix on the key itself. See [API keys](../manage/api-keys.md). [Roles](../manage/roles.md) govern people, not keys. |

---

## You deleted something by mistake

Connectors, connector actions and workflows go to [Trash](../manage/trash.md) and restore with slug and history intact. Other resources, including widgets and their integrations, are deleted immediately and can't be restored from Trash.

---

## Making the next one easier

| Do this once                                                  | Saves you                                     |
| ------------------------------------------------------------- | ----------------------------------------------- |
| **Turn on failure alerts** on [Alerts](alerts.md) (offered while no alert exists; once one does, switch on **Sync failure notifications** instead) | Finding out from a customer                    |
| Add an alert on **Broken connectors above 0**                 | Expired credentials going unnoticed            |
| Add an alert on **Total runs below 1 over 24 hours**          | A schedule that silently stopped               |
| Set a **deduplication key** on every webhook trigger          | Duplicate records after any replay             |
| Add `fastn.diff.compare` to every sync                        | Reconstructing a run from logs                 |
