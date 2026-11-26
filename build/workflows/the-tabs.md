---
description: "Every tool tab in the editor: Test, Connectors, Contract, Diagram, Compare, Test cases, Executions, Sync reports, and API."
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

The tool tabs on the right of the [workflow editor](the-editor.md) are where you test a workflow and check what it does. This page covers each tab.

A new workflow shows three tabs: **Test**, **Connectors** and **Contract**. Once you save it, the rest appear: **Diagram**, **Compare** (when there is code to compare), **Test cases**, **Executions**, **Sync reports** and **API**. If they don't all fit, the extra tabs move into a **More** menu.

### Test

Runs the workflow once with an input you type, without saving it. Use it while you build.

Put the input in the `ctx.input` editor and any headers in `ctx.headers`. **Use contract** fills the input from the workflow's [input contract](#contract). Then pick a mode beside the run button:

* **Live:** calls the connected apps for real, so changes really happen in those apps.
* **Partial Mock:** calls an app for real where it has an active connection, and uses a stored stand-in response (a mock) where it doesn't.
* **Fully Mock:** uses stored mock responses only and calls no app.

The run button follows the mode: **Run Live**, **Run Partial Mock** or **Run Fully Mock**.

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

The editor's **Test cases** tab shows the suite itself: a header with the case count, **+ New group**, and **Refresh**, then the cases. On the workflow detail view (it opens when you select **Run** on a workflow's row) the same suite sits under two tabs, and the difference between them is the part worth understanding: **Test Cases** is the specification, **Validation** is the result of running it.

A saved set of test scenarios for the workflow, which Fastn's validator agent runs to check the whole workflow.

**Who writes them.** The Fastn agent or your AI tool generates a suite while it builds the workflow, grouped into `happy-path`, `pagination`, `fields`, `edge-cases`, and `error-handling`. After that the list is yours to maintain: each group has an add control, and every case can be edited or deleted.

A case is three fields and a mode:

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

None of this is the [Test](#test) tab above. **Test** runs one payload you type, once, right now. **Test cases** are a saved suite the validator agent runs against the whole workflow.

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
