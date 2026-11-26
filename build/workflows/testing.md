---
description: Run a workflow with a sample input, check its saved test cases, and read the results before you publish.
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

# Test a workflow

**Build → Integrations → Workflows** → open a workflow · [Open in Fastn](https://app.fastn.dev/integrations?tab=workflows)

Test a workflow before you publish it, to check that it does what you expect. There are two ways to test, and they do different jobs:

* **Quick test:** runs the workflow once with an input you type, on the editor's **Test** tab. Use it while you build.
* **Test cases:** a saved set of scenarios that Fastn's validator agent runs against the whole workflow. Use them to check every scenario before you publish.

{% hint style="info" %}
**Do this from your AI tool.** Fastn recommends connecting your preferred AI agent, such as Claude, Cursor or VS Code, to the [Fastn MCP server](../mcp-gateway/README.md) and using its tools to test workflows and fix what fails. For example, ask it: *"Run the test cases for the sync-new-contacts workflow and fix any that fail."* To connect your AI agent, see [Connect your AI tool](../mcp-gateway/README.md#open-the-connect-dialog), or the setup guide for [Claude](../mcp-gateway/claude.md), [Claude Code](../mcp-gateway/claude-code.md), [Cursor](../mcp-gateway/cursor.md), [VS Code](../mcp-gateway/vscode.md) or [any other MCP client](../mcp-gateway/README.md#how-your-ai-tool-connects).
{% endhint %}

### Before you start

* A workflow open in the [workflow editor](the-editor.md).
* For a test that calls apps for real, an active [connection](../connections/README.md) to each app the workflow uses.

### Run a quick test

{% hint style="warning" %}
A **Live** test is real: it calls the connected apps, and any changes it makes in them really happen. Use **Fully Mock** to try the workflow without touching any app.
{% endhint %}

1. Open the **Test** tab.
2. Enter the input in `ctx.input`, or select **Use contract** to fill it from the workflow's [input contract](the-tabs.md#contract). Add any headers in `ctx.headers`.
3. Pick a mode beside the run button:
   * **Live:** calls the connected apps for real.
   * **Partial Mock:** calls an app for real where it has an active connection, and uses a stored stand-in response (a mock) where it doesn't.
   * **Fully Mock:** uses stored mock responses only and calls no app.
4. Select the run button. It follows the mode: **Run Live**, **Run Partial Mock** or **Run Fully Mock**.

**You should see:** the workflow's output below the run button. A quick test doesn't save the workflow.

### Check the test cases

Test cases are listed on the editor's **Test cases** tab, with the case count, **+ New group** and **Refresh**. You can also select **Run** on the workflow's row to open its detail view, where the suite is split into two tabs:

* **Test Cases:** the scenarios, meaning what should happen.
* **Validation:** the result of the validator agent's last run against them.

**Who writes them.** The Fastn agent or your AI tool generates a suite while it builds the workflow, grouped into `happy-path`, `pagination`, `fields`, `edge-cases`, and `error-handling`. After that the list is yours to maintain: each group has an add control, and every case can be edited or deleted.

Each case has these fields:

| Field | Notes |
| ----- | ------- |
| **Group** | Free text, with existing groups suggested. Left blank it becomes `Ungrouped`. |
| **Scenario** | What is being exercised. |
| **Pass criteria** | What has to be true for the case to pass. Required. |
| **Mode** | `MOCK` (the default) or `LIVE`. This is the badge on the row. |

**Who runs them.** The workflow validator agent does, not you and not the Run button. Until it has run, the **Validation** tab on the detail view reads *Not validated yet. The workflow validator agent will populate this tab after it runs against the test cases.* Once it has, that tab carries the status, the mode it ran in, when it ran, and a result for each case against the total.

The pass, fail, and untested counters above the list reflect that last validation run. **Untested** means the validator has not reached that case, not that the case failed.

{% hint style="info" %}
**`LIVE` and `MOCK` are set per case, and `MOCK` is the default.** A `MOCK` case is served from stored mock stubs and never reaches the third-party API; a `LIVE` case makes real calls. A suite that is entirely `MOCK` proves your logic, not your connections, so promote the few cases that actually matter to `LIVE` before you trust a green run.
{% endhint %}

### What's next

* [Test and release](lifecycle.md): publish the workflow and deploy it to an environment.
* [Editor tabs](the-tabs.md): see the workflow's runs on the **Executions** tab, and every other tab in the editor.
