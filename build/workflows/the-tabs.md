---
description: "Every tool tab in the workflow editor: Test, Connectors, Contract, Diagram, Compare, Test cases, Executions, Sync reports and API."
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

# Editor tabs

**Build → Integrations → Workflows** → open a workflow · [Open in Fastn](https://app.fastn.dev/integrations?tab=workflows)

The tool tabs on the right of the [workflow editor](the-editor.md) are where you test a workflow, check what it calls and returns, and see its runs. This page covers each tab. For a step-by-step guide to testing, see [Test a workflow](testing.md).

A new workflow shows three tabs: **Test**, **Connectors** and **Contract**. Once you save it, the rest appear: **Diagram**, **Compare** (when there is code to compare), **Test cases**, **Executions**, **Sync reports** and **API**. If they don't all fit, the extra tabs move into a **More** menu.

{% hint style="info" %}
**Do this from your AI tool.** Fastn recommends connecting your preferred AI agent, such as Claude, Cursor or VS Code, to the [Fastn MCP server](../mcp-gateway/README.md) and using its tools to test a workflow and check what it calls. For example, ask it: *"Test the sync-new-contacts workflow and show me the result."* To connect your AI agent, see [Connect your AI tool](../mcp-gateway/README.md#open-the-connect-dialog), or the setup guide for [Claude](../mcp-gateway/claude.md), [Claude Code](../mcp-gateway/claude-code.md), [Cursor](../mcp-gateway/cursor.md), [VS Code](../mcp-gateway/vscode.md) or [any other MCP client](../mcp-gateway/README.md#how-your-ai-tool-connects).
{% endhint %}

### Test

Runs the workflow once with an input you type, in **Live**, **Partial Mock** or **Fully Mock** mode, without saving it. See [Run a quick test](testing.md#run-a-quick-test).

### Connectors

Lists the connectors and actions the workflow calls. Fastn reads them from the workflow's code every time you save, so the list always matches what the workflow does. Use **Add** for a connector the code calls in a way Fastn can't detect.

Each row shows the connector, the organization that owns it, the action and its version, plus a **Per customer** badge when the workflow uses each customer's own connection. See [Per-customer versus platform-wide connectors](../connectors/README.md#per-customer-versus-platform-wide-connectors).

{% hint style="info" %}
Each action is pinned to a version, so a change to the app's API can't silently break your workflow. When Fastn proposes a newer version of an action, it arrives in [Pending updates](../connector-updates.md) for you to accept.
{% endhint %}

### Contract

Defines the shape of the data the workflow accepts and returns:

* **Input contract:** the fields a caller must send.
* **Output contract:** the fields the workflow returns.

You can view each as **JSON** or **Schema**. Paste an example in the JSON view and Fastn generates the schema from it. The schema is the contract, and you can edit it by hand.

### Diagram

Explains what the workflow does, generated from its code. You can't edit the workflow here: change the workflow, and the diagram follows. It has three sub-tabs:

* **Flow:** a read-only diagram of the workflow's steps. Step types are `TRIGGER`, `READ`, `PROCESS`, `WRITE`, `DECISION` and `DONE`. Use Zoom In, Zoom Out and Fit View to move around it.
* **Sequence:** the same logic as an ordered list of phases.
* **Docs:** generated documentation, with an **End user** / **Technical** toggle, an **Out of date** badge when the code has moved on, and **Regenerate** / **Generate**. Docs are generated when you first open them, not on every save. You can **Edit** and **Save** either document; your version is kept separately, shows an **Edited** badge, survives regeneration, and **Reset to generated** discards it.

The customer-facing document has nine sections: *What this integration does*, *Before you start*, *Connected apps*, *How it works*, *Field mapping*, *Smart features*, *When it runs*, *Troubleshooting*, and *Related links*.

### Test cases

The workflow's saved test scenarios, which Fastn's validator agent runs against the whole workflow. See [Check the test cases](testing.md#check-the-test-cases).

### Executions

Shows this workflow's run history. Filter it with the HTTP status pills: **All**, **200**, **201**, **400**, **404**, **422**, **500**. The organization-wide view is [Operate → Logs → Executions](../../operate/executions.md).

### Sync reports

Shows what a sync changed, record by record. It stays empty until the workflow's code calls `fastn.diff.compare` to compare records between runs. See [Sync reports](../../operate/sync-reports.md).

### API

Shows how to call this workflow from your backend, with a curl command you can copy:

```http
POST https://api.fastn.dev/api/v1/workflows/<wfId>/execute
```

Two headers steer it (`X-fastn-Test-Mode` and `x-fastn-env`) and you authenticate with an API key. The copied curl uses a test key (`fsk_test_<your-key>`) with `X-fastn-Test-Mode: true` and `x-fastn-env: test`; with a live key (`fsk_live_<your-key>`), drop the test-mode header. The [HTTP API reference](../../reference/api.md) covers it in full.

### Where the runtime reference lives

There is no separate runtime reference tab (the **Docs** view under **Diagram** documents this workflow, not the runtime). What `ctx` and `fastn.*` expose inside the function shows up in the code editor's autocomplete, and is documented in full in [Workflow runtime API](../../reference/workflow-runtime.md). In short:

| Surface                 | For                                                              |
| ----------------------- | ------------------------------------------------------------------ |
| `ctx.input`             | The request body, shaped by the input contract.                   |
| `ctx.headers`           | The request headers.                                              |
| `fastn.envConfig`       | Per-environment values. See [Configs](../../manage/configs.md).      |
| `fastn.unified`         | The [unified API](../unified-apis/README.md) surface.                        |
| `fastn.connector`       | A connector call: `fastn.connector.<slug>.<action>()`.             |
| `fastn.db`              | Your organization's Postgres schema. See [Database](../../manage/database.md). |
| `fastn.state`           | Key/value state, with scopes `ORG` (the default) and `INVOCATION`. |
| `fastn.secrets`         | Encrypted values. See [Secrets](../../manage/secrets.md).            |

Calls made for a specific customer are addressed with headers: `x-org-id`, `x-installation-id`, `x-fastn-connections`, `x-fastn-installation-config`.

{% hint style="warning" %}
`fastn.connector` (singular) and `fastn.connectors` (plural) both work: the Connectors tab's extractor recognizes both, and the runtime answers to both. A dynamic call such as `fastn.connectors[slug]` cannot be detected, so add that connector by hand on the **Connectors** tab.
{% endhint %}
