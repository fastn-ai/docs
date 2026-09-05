---
description: >-
  The chat-driven builder that picks connectors, drafts workflows and shows you
  the diff.
---

# Agent

**Home → What do you want to build?**

![The agent start screen](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/agent-home.jpg)

The agent is the primary way integrations get built in fastn. You reach it from the **What do you want to build?** prompt on Home — there is no separate sidebar item for it. The pane is headed **Build an integration**, and states its own contract:

> Describe what you need in plain words. The agents pick the connectors, draft the workflow, and show you the diff before anything runs.

What it drafts is JavaScript — a `<slug>.js` module exporting `export default async function(ctx)`, opened in the [workflow editor](workflows.md) for you to read, test and publish.

### Sessions

The left rail, headed **Sessions**, holds your session history. Each session keeps its full conversation, so you can come back to an integration weeks later and continue where you left off rather than re-explaining it. Before you start anything it reads _No sessions yet. Click New session to start._

* **New session** starts a fresh build.
* **Search sessions** (⌘K) filters the rail by name.
* **Collapse sessions sidebar** widens the workspace when you are reading a long diff.

### Starting from an example

Four cards sit under **START FROM AN EXAMPLE**:

* _Sync deals into billing_
* _Alert before an SLA breaches_
* _Keep a sheet current_
* _Give an agent scoped access_

They are written in the shape a good first message takes, and are worth reading before you write your own.

### Writing a good first message

The agent handles ambiguity by asking, but you get a better first draft by being specific about four things:

| Say                | Example                                                 |
| ------------------ | ------------------------------------------------------- |
| **The systems**    | "HubSpot", "Cin7 Core", not "our CRM"                   |
| **What starts it** | "when a deal is closed-won", "every night at 2am"       |
| **What moves**     | "the company name, the deal amount, and the line items" |
| **The rules**      | "skip anything under $500", "only the EU warehouse"     |

The composer carries **Attach a file**, the message box (_Write a message…_) and **Send**.

### Approval mode

The chip under the message box decides how far the agent goes without checking in.

| Mode     | Behaviour                                                              |
| -------- | ---------------------------------------------------------------------- |
| **Auto** | The default. Does not ask. Fastest for exploration.                    |
| Manual   | Asks before any create, update or delete. Use when touching live data. |

### What it does

The product's own summary is the reliable one: the agents pick the connectors, draft the workflow, and show you the diff before anything runs. In practice that means working out which systems are involved, reusing connectors that already exist and creating the ones that do not, handling authentication in the chat — inline API-key fields, or an OAuth form with client ID, secret and pre-filled scopes — and then writing the workflow code and opening it in the editor.

Generated test cases land on the editor's **Test cases** tab, grouped as `happy-path`, `pagination`, `fields`, `edge-cases` and `error-handling`, each row badged `LIVE` or `MOCK`.

### Using the agent: a worked example

![Describing an integration in the agent prompt](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/agent-prompt.jpg)

_Describe the integration in plain words on Home; the agent plans the connectors and drafts the workflow._

Say you want this: _when a new contact is created in HubSpot, add a row to a Google Sheet with their name, email and company._ Here is how that request becomes a running integration.

{% stepper %}
{% step %}
#### Describe it in plain words

On Home, type the whole thing into **What do you want to build?** and press **Send** — there is no need to name connectors or pick a trigger yourself:

> When a new contact is created in HubSpot, add a row to a Google Sheet with their name, email, and company.

The prompt opens the agent's **Build an integration** pane and starts a session.
{% endstep %}

{% step %}
#### The agent picks the connectors

It works out the systems involved — HubSpot as the source, Google Sheets as the destination — reusing connectors that already exist and creating any that do not. Where a system needs authorising, it handles that in the chat: an inline API-key field, or an OAuth form with client ID, secret and pre-filled scopes.
{% endstep %}

{% step %}
#### It drafts the workflow and shows a diff

The agent writes the workflow — a `<slug>.js` module — with the trigger (a new HubSpot contact), the field mapping (name, email, company) and the Google Sheets write. It then **shows you the diff before anything runs**: nothing is created or changed until you have seen what it proposes.
{% endstep %}

{% step %}
#### You review — Approval mode decides how much it did unattended

The **Approval mode** chip governs how far it goes on its own. **Auto**, the default, acts without asking — quickest for exploring. **Manual** asks before any create, update or delete — the mode to use when it is touching live data. Read the diff, then accept it or reply with a correction.
{% endstep %}

{% step %}
#### Test and publish

The draft opens in the [workflow editor](workflows.md), where the generated scenarios sit on the **Test cases** tab. Run it from the **Test** tab, then **Publish** when it does what you meant.
{% endstep %}
{% endstepper %}

From here you refine it in the same conversation rather than starting over, as the next section covers.

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
Agent usage draws on the AI credits shown in the top bar — click it for the balance, an org total, and the reset date. Quota resets at the start of each calendar month, UTC. The popover also breaks usage down **By agent**, naming the ones doing this work: _Orchestrator V2 Orchestrator_, _Docs Agent_, _Error Diagnosis_ and _Orchestrator V2 Title_. Plan and quota detail live under Billing, which is visible to Owners and Admins.
{% endhint %}

{% hint style="warning" %}
Using the AI assistant is gated by role rather than by an individual permission, so a role that cannot use it cannot be granted access to it one permission at a time.
{% endhint %}
