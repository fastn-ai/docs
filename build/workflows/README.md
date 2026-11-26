---
description: What a workflow is, how it runs, and how to read the Workflows list.
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

**Build → Integrations → Workflows** · [Open in Fastn](https://app.fastn.dev/integrations?tab=workflows)

A **workflow** is the logic of an integration: the steps that run each time it is triggered. It uses [connectors](../connectors/README.md) to read from and write to apps. For example, a workflow can fetch new deals from a CRM, reshape them and create matching invoices in an accounting app.

A workflow runs when a [trigger](../triggers/README.md) fires or when your backend calls it through the API. Each run is for one customer and uses that customer's own [connections](../connections/README.md).

### How you build one

You describe the workflow to your AI tool through the [Fastn MCP server](../mcp-gateway/README.md), or to the [Fastn agent](../agent/README.md), and it writes the workflow for you. You then test it, publish it and deploy it.

Under the hood, a workflow is a JavaScript function in one file, `<slug>.js`. You see that file in the editor only when code editing is on for your organization, which is off by default. Either way, you configure, test, publish and deploy the workflow the same way. See [The workflow editor](the-editor.md).

### Execution tiers

Each workflow has an execution tier. The tier sets how long a run can take and whether the caller waits for the result.

* **Instant:** The caller waits and gets the result in the response. A run can take up to 25 seconds, or 2 minutes if Fastn has raised the limit for your organization. Use it when something is waiting on the answer, such as a quick lookup.
* **Standard:** The caller gets `202 Accepted` straight away, and the run continues in the background for up to 15 minutes (2 minutes by default). Use it for most syncs and multi-step processes.
* **Long:** Like Standard, but a run can take up to 36 hours (15 minutes by default). Use it for large imports, backfills and reports.

You set the tier and the timeout in the editor's [Configuration panel](the-editor.md#configuration-panel).

### Versions and environments

Fastn keeps *what the code is* separate from *where it runs*.

* **Version:** A frozen copy of the workflow, created each time you publish. Versions are numbered v1, v2 and so on.
* **Environment:** A place where a version runs. `test` and `live` are built in. You can add your own, such as `staging`, and you can require a GitHub pull request before anything is deployed to one. [Learn more](../../manage/environments.md)
* **API key mode:** Every API key is either `Test` or `Live`. A call with a Test key must also send `X-fastn-Test-Mode: true`, or it is refused.

Test keys act on real data. See [API keys](../../manage/api-keys.md).

To publish and deploy versions, see [Test and release](lifecycle.md).

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

When a call fails because nothing is published or deployed, the list's tooltips explain why. The first message is the error you are most likely to search for:

> Never published. Every call returns WORKFLOW\_NOT\_PUBLISHED until a snapshot is published. Draft edits alone do not make a workflow runnable.

> Nothing deployed to \<environment>. A call naming this environment fails until a version is deployed to it.

**Search workflows** filters by name, and the **All**, **Instant**, **Standard** and **Long** pills filter by execution tier.

Two buttons sit at the top right:

* **Connect GitHub:** connects your organization to a GitHub repository, so publishing and deploying can go through pull requests.
* **Create workflow:** opens the editor with an empty workflow.

### In this section

* [The workflow editor](the-editor.md): the editor's layout and every Configuration setting.
* [Write a workflow in code](../../tutorials/saas-admin/configuring-a-workflow-in-code.md): write and test a workflow by hand, when code editing is on.
* [Test a workflow](the-tabs.md): every tool tab in the editor, from Test to API.
* [Test and release](lifecycle.md): save, publish and deploy, and roll back.
