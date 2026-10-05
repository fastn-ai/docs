---
description: "How to reach the fastn team: support email, in-app chat, and what to include."
---

# Getting help

### Email

**[support@fastn.ai](mailto:support@fastn.ai)** reaches the team directly. Use it for anything that needs detail: a failing sync, a connector that will not authorise, a billing question, or a step in these docs that does not match what you see.

### Chat

The chat bubble in the bottom corner of the dashboard is the quickest route for a short question. It reaches the same team.

### What to include

A few details turn a report into a fix on the first reply:

| Include | Why |
| ------- | --- |
| The **execution id** (`exec_…`) and **workflow id** (`wf_…`) | Both sit in the footer of an expanded execution. They identify the exact run |
| What you expected, and what happened instead | Separates a wrong result from a failed one |
| The **connector** and **action** that failed | The Error tab shows it as `connector.<slug>.<action>` |
| Whether it is reproducible | A one-off and a permanent failure need different answers |

Before reporting a failed run, open the **Error** tab on the execution. Its AI Diagnosis names the failing step and usually the fix, and most failures resolve there without needing us. See [Errors and failure states](reference/errors.md) and [Troubleshooting](operate/troubleshooting.md).

### Evaluating fastn

If you are still deciding whether fastn fits, book time with the team rather than emailing support: [calendly.com/fastn/discovery](https://calendly.com/fastn/discovery).
