---
description: The chat-driven builder that picks connectors, drafts workflows and shows you the diff.
---

# Agent

**Home → What do you want to build?**

<figure><img src="../.gitbook/assets/agent-home.jpg" alt="The agent start screen"><figcaption></figcaption></figure>

The agent is the primary way integrations get built in fastn. You reach it from the **What do you want to build?** prompt on Home — there is no separate sidebar item for it. The pane is headed **Build an integration**, and states its own contract:

> Describe what you need in plain words. The agents pick the connectors, draft the workflow, and show you the diff before anything runs.

What it drafts is JavaScript — a `<slug>.js` module exporting `export default async function(ctx)`, opened in the [workflow editor](workflows.md) for you to read, test and publish.

### Sessions

The left rail, headed **Sessions**, holds your session history. Each session keeps its full conversation, so you can come back to an integration weeks later and continue where you left off rather than re-explaining it. Before you start anything it reads *No sessions yet. Click New session to start.*

* **New session** starts a fresh build.
* **Search sessions** (⌘K) filters the rail by name.
* **Collapse sessions sidebar** widens the workspace when you are reading a long diff.

### Starting from an example

Four cards sit under **START FROM AN EXAMPLE**:

* *Sync deals into billing*
* *Alert before an SLA breaches*
* *Keep a sheet current*
* *Give an agent scoped access*

They are written in the shape a good first message takes, and are worth reading before you write your own.

### Writing a good first message

The agent handles ambiguity by asking, but you get a better first draft by being specific about four things:

| Say                         | Example                                                     |
| --------------------------- | ------------------------------------------------------------ |
| **The systems**             | "HubSpot", "Cin7 Core", not "our CRM"                        |
| **What starts it**          | "when a deal is closed-won", "every night at 2am"            |
| **What moves**              | "the company name, the deal amount, and the line items"      |
| **The rules**               | "skip anything under $500", "only the EU warehouse"          |

The composer carries **Attach a file**, the message box (*Write a message…*) and **Send**.

### Approval mode

The chip under the message box decides how far the agent goes without checking in.

| Mode     | Behaviour                                                              |
| -------- | ------------------------------------------------------------------------ |
| **Auto** | The default. Does not ask. Fastest for exploration.                     |
| Manual   | Asks before any create, update or delete. Use when touching live data.   |

### What it does

The product's own summary is the reliable one: the agents pick the connectors, draft the workflow, and show you the diff before anything runs. In practice that means working out which systems are involved, reusing connectors that already exist and creating the ones that do not, handling authentication in the chat — inline API-key fields, or an OAuth form with client ID, secret and pre-filled scopes — and then writing the workflow code and opening it in the editor.

Generated test cases land on the editor's **Test cases** tab, grouped as `happy-path`, `pagination`, `fields`, `edge-cases` and `error-handling`, each row badged `LIVE` or `MOCK`.

### Iterating

Follow-up messages refine what exists rather than starting over:

* "Add error handling for when the API is down"
* "Filter out records without an email address"
* "Change the schedule to hourly"
* "Notify Slack on failure"

The agent updates code, mappings and test cases together, so they do not drift apart.

### Attachments

**Attach a file** accepts an API spec, a sample payload, a field-mapping spreadsheet. Giving the agent a real payload is the single fastest way to get accurate mappings.

{% hint style="info" %}
Agent usage draws on the AI credits shown in the top bar — click it for the balance, an org total, and the reset date. Quota resets at the start of each calendar month, UTC. The popover also breaks usage down **By agent**, naming the ones doing this work: *Orchestrator V2 Orchestrator*, *Docs Agent*, *Error Diagnosis* and *Orchestrator V2 Title*. Plan and quota detail live under [Billing](../manage/billing.md), which is visible to Owners and Admins.
{% endhint %}

{% hint style="warning" %}
Using the AI assistant is gated by role rather than by an individual permission, so a role that cannot use it cannot be granted access to it one permission at a time.
{% endhint %}
