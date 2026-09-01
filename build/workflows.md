---
description: The code that runs on a trigger, a schedule, or an agent call.
---

# Workflows

**Integrations → Workflows**

<figure><img src="../.gitbook/assets/workflows-list.jpg" alt="The workflows list"><figcaption></figcaption></figure>

### The list

| Column         | Notes                                                       |
| -------------- | ------------------------------------------------------------- |
| **Workflow**   | Name, slug and description.                                 |
| **Status**     | Active or inactive.                                         |
| **Latest**     | Highest published version.                                  |
| **live**       | Which version is deployed to the live environment, if any.  |
| **Updated**    | Last change.                                                |

Filter chips split the list by execution tier: **All**, **Instant**, **Standard**, **Long**. **Run** executes a workflow on demand; the **…** menu holds duplicate, export and delete.

Three buttons sit top-right:

* **Create workflow** — an empty workflow you configure yourself.
* **Build with AI** — hands the job to the [agent](agent.md).
* **Sync to GitHub** — mirrors workflows to the repository connected under [Environments](../manage/environments.md).

### The editor

Open a workflow and the editor takes over the screen. Configuration on the left, nine tabs on the right, and Discard / Save workflow / Publish along the top.

<figure><img src="../.gitbook/assets/workflow-config-panel.jpg" alt="The configuration panel"><figcaption></figcaption></figure>

#### Configuration panel

**Identity**

| Field           | Notes                                            |
| --------------- | -------------------------------------------------- |
| **Name**        | Required.                                        |
| **Slug**        | Derived from the name; used in code and API paths. |
| **Description** | What it does. The agent writes one; edit freely. |

**Execution**

| Field                 | Notes                                                                  |
| --------------------- | ------------------------------------------------------------------------ |
| **Execution tier**    | Instant, Standard or Long. Each states its behaviour underneath.       |
| **Execution timeout** | A slider constrained to the tier's range.                              |
| **Status**            | Enabled accepts new runs; disabled stops them without deleting anything. |

**When a run fails**

| Field                  | Notes                                                                                                                             |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Retry policy**       | Retries transient failures — and timeouts, when *Escalate on timeout* is off — up to the attempt count. Code errors, data errors and out-of-memory never retry. |
| **Escalate on timeout** | On timeout, retry one tier up (standard → long) with the higher tier's full budget. An escalated instant run returns a queued execution id to poll instead of a synchronous result. Subject to your plan. |

**Publish & deploy**

* **Publish snapshot** — freezes code and configuration as an immutable version.
* **Deploy to environment** — sends a published version to an environment.
* Underneath: the latest version, how it was created, and which environments it is live in.

### The tabs

#### Test

<figure><img src="../.gitbook/assets/workflow-test.jpg" alt="The Test tab"><figcaption></figcaption></figure>

Edit `ctx.input` and `ctx.headers`, then **Run Live**. **Use contract** fills the input from the declared contract, and the dropdown beside it chooses which code runs. Runs execute without saving, and are not recorded in [Executions](../operate/executions.md) — that log is for real traffic only.

#### Connectors

<figure><img src="../.gitbook/assets/workflow-connectors-tab.jpg" alt="The Connectors tab"><figcaption></figcaption></figure>

Which connectors this workflow may call, which actions it uses, and at which action version. Each carries a **Per customer** or workspace badge — see [Core concepts](../getting-started/concepts.md). The gear icon opens scope settings; **Add** wires in another connector.

{% hint style="warning" %}
Pinned action versions (`getSale V1.1`, `createOrder V1.1`) are what stop an upstream change breaking you silently. When fastn proposes a newer action, it arrives through [Connector updates](connector-updates.md) for you to accept.
{% endhint %}

#### Contract

<figure><img src="../.gitbook/assets/workflow-contract.jpg" alt="Input and output contracts"><figcaption></figcaption></figure>

Input and output shapes, each viewable as **JSON** or **Schema**. Write an example payload in the JSON view and the schema is generated live. Both are saved with the workflow; the schema is the contract and is also hand-editable.

#### Diagram

Three sub-views: **Flow** (the node graph), **Sequence** (the same logic as an ordered timeline), and **Docs** (generated reference for the workflow). Node types are labelled TRIGGER, PROCESS, DECISION, READ, WRITE and DONE, and decision branches show both paths including skips and errors.

#### Test cases

Scenarios generated during the build. Each has a name, a MOCK or LIVE badge, a description, a feedback field and an Approve button. The header shows the total and how many run live.

#### Executions

This workflow's run history — time, tier, version, status, duration and what triggered it. The workspace-wide view is [Activity → Executions](../operate/executions.md).

#### Sync reports

What changed on the last run, record by record. Populated when a workflow calls `fastn.diff.compare`. See [Sync reports](../operate/sync-reports.md).

#### API

<figure><img src="../.gitbook/assets/workflow-api-tab.jpg" alt="The API tab with endpoint and curl"><figcaption></figcaption></figure>

How to call this workflow over HTTP, with a copyable curl. Covered in full in the [HTTP API reference](../reference/api.md).

#### Docs

Generated reference documentation for the workflow — the contract, the connectors it touches, and the steps it takes.

### Code editing

Some workspaces have code editing switched off, and show this banner:

> Code editing is switched off for this workspace — workflows here are generated and updated by the AI builder. You can still test, wire connectors and edit the contract. It can be switched on if you want to write workflow code yourself; ask fastn to enable it.

With it off, you change behaviour by talking to the agent rather than editing a file. The runtime API is documented in [Workflow runtime API](../reference/workflow-runtime.md) either way.

### Lifecycle

```
Create → Save (draft) → Publish (immutable version) → Deploy (to an environment)
```

| Stage       | Effect                                                                |
| ----------- | ----------------------------------------------------------------------- |
| **Save**    | Persists the draft. Nothing goes live.                                 |
| **Publish** | Creates v1, v2, … Immutable, so rollback is just deploying an older one. |
| **Deploy**  | The version starts handling real events in that environment.           |

If **Require review before publishing** is on for the connected GitHub repository, a publish opens a pull request instead of deploying — see [Environments](../manage/environments.md).
