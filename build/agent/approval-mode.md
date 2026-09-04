---
description: "How far the agent goes without checking in: Auto versus Manual."
---

# Approval mode

The chip under the message box decides how far the agent goes without checking in.

| Mode     | Behaviour                                                                |
| -------- | ------------------------------------------------------------------------ |
| **Auto** | The default. Does not ask. Fastest for exploration.                      |
| Manual   | Asks before any create, update or delete. Use when touching live data.   |

You can change it mid-session. Switching to **Auto** after a few approvals is a common pattern — watch what the agent reaches for while it is unfamiliar, then let it run.

### The approval gate

In **Manual** mode the agent stops and posts a card for each pending call. Nothing happens until you answer it.

<figure><img src="../../.gitbook/assets/agent-approval-gate.jpg" alt="Two stacked approval cards, each headed Create connect link with the tool name create_connect_link, a JSON payload containing a connectorId, a VIEW RAW INPUT toggle, a note-to-agent textarea, and Accept, Always allow and Reject buttons"><figcaption>One card per pending call. Each shows the exact tool name and the exact arguments.</figcaption></figure>

Every card carries the same parts:

| Part | What it shows |
| ---- | ------------- |
| Title | The action in plain language — e.g. **Create connect link** |
| Tool badge | The literal tool being invoked — e.g. `create_connect_link` |
| Payload | The exact JSON arguments, such as the `connectorId` it will act on |
| **VIEW RAW INPUT** | Expands the full, untruncated payload |
| **NOTE TO AGENT (OPTIONAL)** | Free text — *"On reject, this note is sent to the agent so it can re-plan…"* |

### The three responses

* **Accept** — runs this one call, and only this one. The next call gates again.
* **Always allow** — stops asking for *that tool* for the remainder of the session. Useful once you have seen a read-only call a few times; think harder before using it on a tool that writes.
* **Reject** — refuses the call. Whatever you typed in the note goes back to the agent, which re-plans around it.

{% hint style="info" %}
The note is what makes rejection useful. *"Use the sandbox sheet, not the production one"* produces a corrected plan. A bare **Reject** with no explanation usually produces the same call again.
{% endhint %}

{% hint style="warning" %}
**Always allow** is scoped to the session, not to the tool forever — but within a long session it can cover a lot of ground. If the agent is about to touch production data, leave the gate in place.
{% endhint %}

See [the worked example](worked-example.md) for a gate in the middle of a real build.
