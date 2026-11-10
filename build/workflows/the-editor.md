---
description: The workflow editor walked through tab by tab, plus the configuration panel reference.
---

# The workflow editor, tab by tab

Opening a workflow (**Create workflow**, or **Edit** from a row's `⋯` menu), drops you into a drawer with **Configuration** on the left and the tool tabs on the right. Whether there is a code column between them depends on your organization.

{% hint style="warning" %}
**Code editing is a per-organization entitlement, off by default and enabled by fastn.** Unless fastn has switched it on for your organization, you will not see the middle column at all: the editor shows Configuration and the tool tabs, and the banner reads:

> Code editing is switched off for this organization - workflows here are generated and updated by the AI builder. You can still test, wire connectors and edit the contract. It can be switched on if you want to write workflow code yourself; ask fastn to enable it.

Everything else on this page still applies. You change a workflow's behavior by asking [Build with AI](../agent/README.md) instead of typing into the file, and you still configure, test, wire connectors, edit the contract, publish and deploy exactly as described below. **If you want to write workflow code yourself, ask fastn to switch it on.**
{% endhint %}

The walkthrough below assumes the code column is present. This is roughly the order you move through it.

{% stepper %}
{% step %}
#### Set up Configuration

Under **Identity**, give it a **Name** (required) and, on a new workflow, a **Slug**: the slug is fixed once the workflow exists, so choose it deliberately. **Description** is free text. Under **Execution**, pick an **Execution tier**: `Instant` runs synchronously and caps at 25s (2 minutes if fastn has granted your organization the "Increase Instant timeout" entitlement), `Standard` returns `202` and runs up to 15 min, `Long` returns `202` and runs up to 36 hours. The **Execution timeout** slider is then constrained to that tier.

Full ranges and defaults are in the Configuration panel reference below.
{% endstep %}

{% step %}
#### Decide what happens when a run fails

**Retry policy** is off by default; turning it on exposes **Max attempts**, **Initial interval (ms)**, **Backoff coefficient** and **Max interval (ms)**. It only retries transient failures: code errors, data errors and out-of-memory never retry. **Escalate on timeout** is a separate toggle that retries one tier up on a timeout (instant → standard, or standard → long), subject to your plan, and is hidden on the `Long` tier.
{% endstep %}

{% step %}
#### Write the function

The middle column is one `<slug>.js` file exporting `export default async function (ctx)`. You reach the request through `ctx.input` and `ctx.headers`, and connected systems through `fastn.*`, for example `fastn.connector.<slug>.<action>()`. A new workflow is scaffolded for you:

```javascript
export default async function(ctx) {
  const { input, headers } = ctx;
  // Your workflow logic here
  return { result: "Hello from workflow!", input };
}
```

**This step does not apply when code editing is off** (the default). The file is then generated and updated by [Build with AI](../agent/README.md), and you describe the change you want there rather than editing it here. Skip to the next step; everything from there on is identical.
{% endstep %}

{% step %}
#### Test it: `Test` tab

Put a body in the `ctx.input` editor and headers in `ctx.headers`, or press **Use contract** to fill the input from the declared contract. Pick what the run actually touches (`Live`, `Partial Mock` or `Fully Mock`); the run button follows the mode and reads **Run Live**, **Run Partial Mock** or **Run Fully Mock**.
{% endstep %}

{% step %}
#### Check the wiring: `Connectors` tab

Every `fastn.connector.<slug>.<action>(…)` call in your code is extracted here each time you save, so this tab is a readout of what the workflow actually talks to. **Add** covers anything you need to wire by hand.
{% endstep %}

{% step %}
#### Declare the shape: `Contract` tab

**Input contract** and **Output contract**, each viewable as **JSON** or **Schema**. Paste an example payload in the JSON view and the schema is generated live; the schema is the contract, and is hand-editable.
{% endstep %}

{% step %}
#### Read the logic back: `Diagram` tab

**Flow** and **Sequence** are generated from the code and read-only: you edit the code and they follow. **Docs** is generated too, with an **End user** / **Technical** toggle and **Regenerate**, but you can also **Edit** and **Save** it; an edited doc shows an **Edited** badge, survives regeneration, and **Reset to generated** returns to the generated version.
{% endstep %}

{% step %}
#### Confirm the scenarios: `Test cases` tab

The cases drafted during the build, grouped `happy-path`, `pagination`, `fields`, `edge-cases` and `error-handling`, each row an id such as `TC-01` with a `LIVE` or `MOCK` badge.
{% endstep %}

{% step %}
#### Watch it run: `Executions` tab

This workflow's own run history, filtered by the HTTP-status pills `All`, `200`, `201`, `400`, `404`, `422`, `500`. The neighboring **Sync reports** tab fills in the first time the workflow runs `fastn.diff.compare`.
{% endstep %}

{% step %}
#### Hand it to callers: `API` tab

**API** gives the `POST …/api/v1/workflows/<wfId>/execute` endpoint with a copyable curl and the two headers that steer it, `X-fastn-Test-Mode` and `x-fastn-env`. There is no separate runtime reference tab: what `ctx` and `fastn.*` expose inside the function shows up in the code editor's autocomplete and is documented in [Workflow runtime API](../../reference/workflow-runtime.md).
{% endstep %}
{% endstepper %}

### The editor

Opening a workflow opens a drawer laid out as **configuration on the left, the tool tabs on the right, and (where code editing is enabled), the code editor between them**. That middle column is labelled `<slug>.js` and `JavaScript · export default async function(ctx)`. An organization without code editing gets the same drawer minus that column.

Along the top: **Discard**, the workflow name, **Close tab**, **Save workflow** and **Publish**. Closing with unsaved edits asks first: *Discard unsaved changes?* / "\"\<name>\" has edits that have not been saved. Closing this tab throws them away." / **Keep editing** / **Discard changes**.

#### Configuration panel

**Identity**

| Field           | Notes                                                                             |
| --------------- | ----------------------------------------------------------------------------------- |
| **Name**        | Required. Empty saves are refused with *Name is required.*                         |
| **Slug**        | Required when you create the workflow, and **cannot be changed afterwards**.        |
| **Description** | What it does. Build with AI writes one; edit freely.                                |

**Execution**

| Field                 | Notes                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------- |
| **Execution tier**    | `Instant` (default): synchronous, returns the result inline, max 25s (help text: *Synchronous. Returns the result inline. Max 25s.*), or 2 min with the "Increase Instant timeout" entitlement. `Standard`: asynchronous via Temporal, returns 202, max 15 min. `Long`: asynchronous, returns 202, max 36 hours. |
| **Execution timeout** | A slider constrained to the tier: 1s to 25s (or 2 min with the entitlement) for Instant, 5s to 15min for Standard, 30s to 36h for Long. Defaults are 25s, 2.0m and 15.0m respectively. |
| **Status**            | A toggle, on by default, and shown only on workflows that already exist. Off stops new runs without deleting anything. |

**WHEN A RUN FAILS**

The **Retry policy** toggle is off by default (off means a single attempt). Its own description sets the boundary: it retries transient failures (and timeouts, when **Escalate on timeout** is off), and code errors, data errors and out-of-memory never retry. Turning it on exposes four fields.

| Field                    | Range | Default |
| ------------------------ | ----- | ------- |
| **Max attempts**         | 2-10  | 3       |
| **Initial interval (ms)** | - | 5000    |
| **Backoff coefficient**  | - | 2       |
| **Max interval (ms)**    | - | 60000   |

**Escalate on timeout** is a separate toggle, off by default and hidden on the Long tier. On timeout it retries one tier up (instant → standard, or standard → long) with the higher tier's full time budget, subject to your plan. An escalated instant run returns a queued execution id to poll rather than a synchronous result.

**PUBLISH & DEPLOY** (existing workflows only)

* **Publish snapshot**: freezes the current code and configuration as a version.
* **Deploy to environment**: sends a published version to an environment.
* Underneath: a **Latest: vN** line for the newest published version, then one row per environment showing its current status.
