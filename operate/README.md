---
description: Watching what actually happens once integrations are live.
---

# Activity

Build tells you what should happen. Operate tells you what did.

<figure><img src="../.gitbook/assets/activity-events.jpg" alt="The events log"><figcaption></figcaption></figure>

Five logs, each answering a different question, plus the customer list.

| Page                              | Answers                                                          |
| --------------------------------- | ------------------------------------------------------------------ |
| [Events](events.md)               | What arrived, from where, and was it delivered?                   |
| [Traces](traces.md)               | Which connected systems did a run call, and how slow were they?   |
| [Alerts](alerts.md)               | What should tell us something is wrong, and where does it go?     |
| [Executions](executions.md)       | Which runs happened, and how did each end?                        |
| [Sync reports](sync-reports.md)   | What actually changed, record by record?                          |
| [Customers](customers.md)         | Who is using your embedded integrations?                          |
| [Troubleshooting](troubleshooting.md) | Something is wrong — where do I look?                         |

### How to debug in the right order

When a customer says "it stopped working", walk down rather than around:

1. **Events** — did the event arrive at all? If not, the problem is upstream or in the trigger.
2. **Executions** — did a run start, and how did it end? Failed, Timeout and Cancelled each point somewhere different.
3. **Traces** — which external call failed or hung?
4. **Sync reports** — if the run succeeded but the data is wrong, this shows what it actually wrote.
5. **Connections** — if calls are being rejected, check for an Expired or Failed connection.

{% hint style="success" %}
The step most teams skip is the first one: setting an [alert](alerts.md), so you reach step one before your customer does.
{% endhint %}

[Troubleshooting](troubleshooting.md) walks the same path organised by symptom.
