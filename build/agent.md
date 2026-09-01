---
description: The chat-driven builder that picks connectors, drafts workflows and shows you the diff.
---

# Agent

**Integrations → Agent**

<figure><img src="../.gitbook/assets/agent-home.jpg" alt="The agent start screen"><figcaption></figcaption></figure>

The agent is the primary way integrations get built in fastn. You describe the outcome; it works out which connectors are involved, sets up authentication, drafts the workflow, generates test cases, and presents the result for review.

### Sessions

The left sidebar holds your session history. Each session keeps its full conversation, so you can come back to an integration weeks later and continue where you left off rather than re-explaining it.

* **New session** starts a fresh build.
* The search icon filters sessions by name.
* The collapse icon widens the workspace when you are reading a long diff.

### Writing a good first message

The agent handles ambiguity by asking, but you get a better first draft by being specific about four things:

| Say                         | Example                                                     |
| --------------------------- | ------------------------------------------------------------ |
| **The systems**             | "HubSpot", "Cin7 Core", not "our CRM"                        |
| **What starts it**          | "when a deal is closed-won", "every night at 2am"            |
| **What moves**              | "the company name, the deal amount, and the line items"      |
| **The rules**               | "skip anything under $500", "only the EU warehouse"          |

The example cards on the start screen are written in exactly this shape and are a good template.

### Approval mode

The control under the message box decides how far the agent goes without checking in.

| Mode     | Behaviour                                                                        |
| -------- | ---------------------------------------------------------------------------------- |
| **Auto** | Runs the build end to end and presents the finished draft. Fastest for exploration. |
| Manual   | Pauses for confirmation at each significant step. Use when touching live data.      |

### What it does, in order

1. **Analyse** — which systems, what data, what transformations, which trigger.
2. **Connector setup** — reuse what exists, create what does not.
3. **Auth** — inline API-key fields, or an OAuth form with client ID, secret and pre-filled scopes.
4. **Field mapping** — proposed source-to-target mappings, a record matching strategy, and any filters.
5. **Test cases** — generated scenarios, marked MOCK or LIVE, for you to approve.
6. **Workflow** — the code, opened in the editor.

### Iterating

Follow-up messages refine what exists rather than starting over:

* "Add error handling for when the API is down"
* "Filter out records without an email address"
* "Change the schedule to hourly"
* "Notify Slack on failure"

The agent updates code, mappings and test cases together, so they do not drift apart.

### Attachments

The paperclip accepts files — an API spec, a sample payload, a field-mapping spreadsheet. Giving the agent a real payload is the single fastest way to get accurate mappings.

{% hint style="info" %}
Agent usage draws on the AI credits shown in the top bar. The balance and its reset date are under [Billing](../manage/billing.md).
{% endhint %}
