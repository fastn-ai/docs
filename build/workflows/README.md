---
description: The code that runs on a trigger, a schedule, or an API call.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Workflows

**Build → Integrations → Workflows** · `/integrations?tab=workflows`

A workflow is JavaScript. One file, `<slug>.js`, exporting one function:

```javascript
export default async function (ctx) {
  // ctx.input, ctx.headers; connectors via fastn.connector.<slug>.<action>()
}
```

There is no node palette and no drag-and-drop step builder. Everything else on this screen configures, describes, tests, or deploys that function. The editor's Diagram tab is AI-generated documentation of that code: a read-only picture that regenerates when the code has changed.

### Execution tiers

Every workflow declares how long it may run and how it answers the caller.

| Tier         | Behavior                                        | Returns       | Timeout range | Default |
| ------------ | ----------------------------------------------- | ------------- | ------------- | ------- |
| **Instant**  | Synchronous; the caller waits                   | Result inline | 1s - 25s      | 25s     |
| **Standard** | Asynchronous, run via Temporal                  | 202 Accepted  | 5s - 15min    | 2min    |
| **Long**     | Asynchronous, for large volumes                 | 202 Accepted  | 30s - 36h     | 15min   |

Instant's 25-second ceiling rises to 2 minutes only for organizations where Fastn has turned on the longer Instant timeout. Long runs for up to 36 hours. Pick Instant only when something is waiting on the answer. Most syncs are Standard.


### Test and live

Fastn separates *what the code is* from *where it runs*.

* **Versions** are snapshots created by Publish, numbered v1, v2, … in the workflows list.
* **Environments** are where versions are deployed. `test` and `live` are built in and protected; you can add named ones such as `staging`, and mark any environment **Requires review** so promoting to it opens a pull request on a connected GitHub repository instead of deploying directly.
* **API keys** carry a mode, `Test` or `Live`. A Test key is refused unless the caller sends `X-fastn-Test-Mode: true`.

Test keys act on real data. See [API keys](../../manage/api-keys.md).

### The list

| Column         | Notes                                                                          |
| -------------- | -------------------------------------------------------------------------------- |
| checkbox       | Selects rows.                                                                   |
| **Workflow**   | Name, slug, and description.                                                     |
| **Status**     | One of `Live`, `Published`, `Paused`, `In review`, or `Unpublished` (see below). |
| **Latest**     | The newest published version, for example `v2`. This is what the test environment runs. A dash means there is no published version yet (tooltip: *No published version yet.*). |
| one column per environment | Headed by the environment's slug, and shown only when your organization has environments. Each cell shows the version deployed there, for example `v2`, or `v1 · 1 behind` when newer published versions have not been deployed to it. A dash means nothing is deployed there. |
| **Updated**    | Last change.                                                                    |
| actions        | An **Executions** link to the workflow's runs, **Run** to execute on demand, and a `⋯` menu with **Edit** (or **View** for an inherited workflow) and **Delete**. |

What each status means:

| Status | Meaning |
| ------ | ------- |
| `Live` | A published version is deployed to the default (live) environment. |
| `Published` | Published; the test environment runs it, but it is not deployed to live yet. |
| `Paused` | Published, but disabled: calls are refused until it is enabled again. |
| `In review` | A publish is waiting on a GitHub pull request; the version is created when the PR merges. |
| `Unpublished` | Never published. |

Two tooltips explain why a call fails, and the first is the error string you are most likely to search for:

> Never published. Every call returns WORKFLOW\_NOT\_PUBLISHED until a snapshot is published. Draft edits alone do not make a workflow runnable.

> Nothing deployed to \<environment>. A call naming this environment fails until a version is deployed to it.

**Search workflows** filters by name; pills split the list by execution tier: **All**, **Instant**, **Standard**, **Long**.

Two buttons sit top-right: **Connect GitHub**, which connects your organization to a GitHub repository, and **Create workflow**, which gives you an empty one.

### In this section

* [The editor](the-editor.md)
* [Write a workflow in code](../../tutorials/saas-admin/configuring-a-workflow-in-code.md)
* [Test a workflow](the-tabs.md)
* [Test and release](lifecycle.md)
