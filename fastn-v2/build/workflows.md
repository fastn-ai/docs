---
description: The code that runs on a trigger, a schedule, or an agent call.
---

# Workflows

**Integrations → Workflows** · `/integrations?tab=workflows`

![The workflows list](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/workflows-list.jpg)

A workflow is JavaScript. One file, `<slug>.js`, exporting one function:

```javascript
export default async function (ctx) {
  // ctx.input, ctx.headers, ctx.connectors
}
```

There is no node palette and no drag-and-drop step builder. Everything else on this screen configures, describes, tests or deploys that function.

### The list

| Column          | Notes                                                               |
| --------------- | ------------------------------------------------------------------- |
| checkbox        | Selects rows.                                                       |
| **Workflow**    | Name, slug and description.                                         |
| **Status**      | `Active` or `Not published`.                                        |
| **Latest**      | `v2`, or `Unpublished` when no snapshot exists yet.                 |
| **live**        | Which version is deployed to the live environment, if any.          |
| **Updated**     | Last change.                                                        |
| **Run** + **⋯** | Run executes on demand; the `⋯` menu holds **Edit** and **Delete**. |

Three status tooltips explain the unpublished state, and the middle one is the string you will search for when a call fails:

> Never published — this workflow cannot run yet.

> Every call returns WORKFLOW\_NOT\_PUBLISHED until a snapshot is published

> Nothing deployed to Live.

**Search workflows** filters by name; pills split the list by execution tier — **All**, **Instant**, **Standard**, **Long**.

Two buttons sit top-right: **Connect GitHub**, which connects the workspace to a GitHub repository, and **Create workflow**, which gives you an empty one.

### The workflow editor, tab by tab

![The workflow editor: Configuration, code, and Test panel](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/workflow-editor.jpg)

_The workflow editor — Configuration on the left, the JavaScript code in the middle, the Test panel on the right._

Opening a workflow — **Create workflow**, or **Edit** from a row's `⋯` menu — drops you into a three-column drawer: **Configuration** on the left, the `<slug>.js` code in the middle, and the tool tabs on the right. This is roughly the order you move through it.

{% stepper %}
{% step %}
#### Set up Configuration

Under **Identity**, give it a **Name** (required) and, on a new workflow, a **Slug** — the slug is fixed once the workflow exists, so choose it deliberately. **Description** is free text. Under **Execution**, pick an **Execution tier**: `Instant` runs synchronously and caps at 30s, `Standard` returns `202` and runs up to 15 min, `Long` returns `202` and runs up to 36 h. The **Execution timeout** slider is then constrained to that tier.

Full ranges and defaults are in the Configuration panel reference below.
{% endstep %}

{% step %}
#### Decide what happens when a run fails

**Retry policy** is off by default; turning it on exposes **Max attempts**, **Initial interval (ms)**, **Backoff coefficient** and **Max interval (ms)**. It only retries transient failures — code errors, data errors and out-of-memory never retry. **Escalate on timeout** is a separate toggle that retries one tier up on a timeout, and is hidden on the `Long` tier.
{% endstep %}

{% step %}
#### Write the function

The middle column is one `<slug>.js` file exporting `export default async function (ctx)`. You reach the request through `ctx.input` and `ctx.headers`, and connected systems through `ctx.connectors` and `fastn.*`.

Where a workspace has code editing switched off, the file is generated and updated by the AI builder instead — you change behaviour by talking to the [agent](agent.md), and everything else on this screen still works.
{% endstep %}

{% step %}
#### Test it — `Test` tab

Put a body in the `ctx.input` editor and headers in `ctx.headers`, or press **Use contract** to fill the input from the declared contract. Pick what the run actually touches — `Live`, `Partial Mock` or `Fully Mock` — then **Run Live** (or **Run**).
{% endstep %}

{% step %}
#### Check the wiring — `Connectors` tab

Every `fastn.connectors.X.Y(…)` call in your code is extracted here each time you save, so this tab is a readout of what the workflow actually talks to. **Add** covers anything you need to wire by hand.
{% endstep %}

{% step %}
#### Declare the shape — `Contract` tab

**Input contract** and **Output contract**, each viewable as **JSON** or **Schema**. Paste an example payload in the JSON view and the schema is generated live; the schema is the contract, and is hand-editable.
{% endstep %}

{% step %}
#### Read the logic back — `Diagram` tab

**Flow**, **Sequence** and **Docs** are all generated from the code and read-only — you edit the code and they follow. **Docs** carries an **End user** / **Technical** toggle and consumes AI credits when you **Regenerate**.
{% endstep %}

{% step %}
#### Confirm the scenarios — `Test cases` tab

The cases drafted during the build, grouped `happy-path`, `pagination`, `fields`, `edge-cases` and `error-handling`, each row an id such as `TC-01` with a `LIVE` or `MOCK` badge.
{% endstep %}

{% step %}
#### Watch it run — `Executions` tab

This workflow's own run history, filtered by the HTTP-status pills `All`, `200`, `201`, `400`, `404`, `422`, `500`. The neighbouring **Sync reports** tab fills in the first time the workflow runs `fastn.diff.compare`.
{% endstep %}

{% step %}
#### Hand it to callers — `API` and `Docs` tabs

**API** gives the `POST …/api/v1/workflows/<wfId>/execute` endpoint with a copyable curl and the two headers that steer it, `X-fastn-Test-Mode` and `x-fastn-env`. **Docs** is the runtime reference for what `ctx` and `fastn.*` expose inside the function.
{% endstep %}
{% endstepper %}

### The editor

Opening a workflow opens a drawer with three columns: **configuration on the left, the code editor in the middle, and nine tool tabs on the right**. The middle column is labelled `<slug>.js` and `JavaScript · export default async function(ctx)`.

Along the top: **Discard**, the workflow name, **Close tab**, **Save workflow** and **Publish**. Closing with unsaved edits asks first — _Discard unsaved changes?_ / "This workflow has edits that have not been saved. Closing the tab throws them away." / **Keep editing** / **Discard changes**.

![The configuration panel](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/workflow-config-panel.jpg)

#### Configuration panel

**Identity**

| Field           | Notes                                                                        |
| --------------- | ---------------------------------------------------------------------------- |
| **Name**        | Required. Empty saves are refused with _Name is required._                   |
| **Slug**        | Required when you create the workflow, and **cannot be changed afterwards**. |
| **Description** | What it does. The agent writes one; edit freely.                             |

**Execution**

| Field                 | Notes                                                                                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Execution tier**    | `Instant` (default) — synchronous, result inline, max 30s. `Standard` — asynchronous via Temporal, returns 202, max 15 min. `Long` — asynchronous, returns 202, max 36 h. |
| **Execution timeout** | A slider constrained to the tier: 1s–30s, 5s–15min, or 30s–36h. Defaults are 30s, 2.0m and 15.0m respectively.                                                            |
| **Status**            | A toggle, on by default, and shown only on workflows that already exist. Off stops new runs without deleting anything.                                                    |

**WHEN A RUN FAILS**

The **Retry policy** toggle is off by default. Its own description sets the boundary: it retries transient failures, and code errors, data errors and out-of-memory never retry. Turning it on exposes four fields.

| Field                     | Range | Default |
| ------------------------- | ----- | ------- |
| **Max attempts**          | 1–10  | 3       |
| **Initial interval (ms)** | —     | 5000    |
| **Backoff coefficient**   | —     | 2       |
| **Max interval (ms)**     | —     | 60000   |

**Escalate on timeout** is a separate toggle, off by default and hidden on the Long tier. On timeout it retries one tier up — instant → standard — and an escalated instant run returns a queued execution id to poll rather than a synchronous result.

**PUBLISH & DEPLOY** (existing workflows only)

* **Publish snapshot** — freezes the current code and configuration as a version.
* **Deploy to environment** — sends a published version to an environment.
* Underneath: a row showing the environment's current status.

### The tabs

#### Test

![The Test tab](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/workflow-test.jpg)

Two JSON editors, `ctx.input` and `ctx.headers`. **Use contract** fills the input from the declared contract. The mode select beside the run button chooses what the run actually calls:

| Mode             | What runs                            |
| ---------------- | ------------------------------------ |
| **Live**         | Real calls to the connected systems. |
| **Partial Mock** | A mix of real calls and stubs.       |
| **Fully Mock**   | Stubs only.                          |

Then **Run Live** (or **Run**).

#### Connectors

![The Connectors tab](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/workflow-connectors-tab.jpg)

This list is **auto-extracted from the `fastn.connectors.X.Y(…)` calls in your code every time you save** — it is a readout of the code, not a separate configuration. **Add** exists for anything you need to wire manually. Each row shows a **Per customer** badge where it applies, plus the connector slug, the owning org, the action and its version.

{% hint style="warning" %}
Pinned action versions are what stop an upstream change breaking you silently. When fastn proposes a newer action, it arrives through Pending updates for you to accept.
{% endhint %}

#### Contract

![Input and output contracts](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/workflow-contract.jpg)

**Input contract** and **Output contract**, each viewable as **JSON** or **Schema**. Write an example payload in the JSON view and the schema is generated live. The schema is the contract, and is also hand-editable.

#### Diagram

Three sub-tabs.

**Flow** — a read-only React Flow rendering, generated from your code. Node kinds are `TRIGGER`, `DECISION`, `READ` and `DONE`; the controls are Zoom In, Zoom Out and Fit View. You cannot edit the graph. Edit the code and the graph follows.

**Sequence** — the same logic as an ordered list of phases.

**Docs** — generated documentation, with an **End user** / **Technical** toggle, an **Out of date** badge when the code has moved on, and **Regenerate** / **Generate**.

The end-user document has eight sections: _What this integration does_, _Before you start_, _Connected apps_, _How it works_, _Field mapping_, _Smart features_, _When it runs_, _Troubleshooting_.

{% hint style="info" %}
Generating or regenerating these docs consumes AI credits from the workspace allowance shown in the top bar.
{% endhint %}

#### Test cases

Scenarios generated during the build, organised into groups — `happy-path`, `pagination`, `fields`, `edge-cases`, `error-handling`. The header carries pass, fail and untested counters. Each row is an id such as `TC-01`, a `LIVE` or `MOCK` badge, and the expectation.

#### Executions

This workflow's run history, filtered by status pills: **All**, **200**, **201**, **400**, **404**, **422**, **500**. The workspace-wide view is [Activity → Executions](../operate/executions.md).

#### Sync reports

> A report appears the first time a workflow runs fastn.diff.compare.

See [Sync reports](../operate/sync-reports.md).

#### API

![The API tab with endpoint and curl](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/workflow-api-tab.jpg)

How to call this workflow over HTTP, with a copyable curl:

```http
POST https://live.gcp.fastn.ai/api/v1/workflows/<wfId>/execute
```

Two headers steer it — `X-fastn-Test-Mode` and `x-fastn-env` — and you authenticate with an API key in the `fsk_live_…` format. Covered in full in the HTTP API reference.

#### Docs

The runtime reference for the code you are writing:

| Surface           | For                                                                    |
| ----------------- | ---------------------------------------------------------------------- |
| `ctx.input`       | The request body, shaped by the input contract.                        |
| `ctx.headers`     | The request headers.                                                   |
| `ctx.connectors`  | The connectors wired to this workflow.                                 |
| `fastn.envConfig` | Per-environment values — see [Configs](../manage/configs.md).          |
| `fastn.unified`   | The [unified API](unified-apis.md) surface.                            |
| `fastn.connector` | A connector call.                                                      |
| `fastn.db`        | The workspace Postgres schema — see [Database](../manage/database.md). |
| `fastn.state`     | Key/value state, with scopes `ORG` and `INVOCATION`.                   |
| `fastn.secrets`   | Encrypted values — see [Secrets](../manage/secrets.md).                |

Multi-tenant calls are addressed with headers: `x-end-org-id`, `x-end-org-ref`, `x-installation-id`, `x-fastn-connections`, `x-fastn-installation-config`.

{% hint style="info" %}
This tab uses `fastn.connector` (singular) while the Connectors tab extracts from `fastn.connectors.X.Y(…)` (plural). Both spellings appear in the product; check the Docs tab in your own workspace before relying on either.
{% endhint %}

Fuller treatment in Workflow runtime API.

### When code editing is switched off

Code editing can be turned off per workspace. Where it is, a banner says so: workflows there are generated and updated by the AI builder, and you can still test them, wire connectors and edit the contract. You change behaviour by talking to the [agent](agent.md) rather than editing the file. The runtime surface is the same either way.

### Lifecycle

```
Create → Save (draft) → Publish (snapshot) → Deploy (to an environment)
```

| Stage       | Effect                                                               |
| ----------- | -------------------------------------------------------------------- |
| **Save**    | Persists the draft. Nothing goes live.                               |
| **Publish** | Creates v1, v2, … A snapshot, so rollback is deploying an older one. |
| **Deploy**  | The version starts handling real events in that environment.         |

An environment can be marked **Requires review**. Promoting to one of those opens a pull request on the connected GitHub repository instead of deploying straight away — the setting is per environment, and lives on Environments, which is also where the repository is connected.
