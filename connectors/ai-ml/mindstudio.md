---
description: "MindStudio developer API (api.mindstudio.ai/developer/v2): run published AI agents/apps synchronously or asynchronously with launch variables, load the…"
hidden: true
---

# MindStudio

<img src="../../.gitbook/assets/connectors/lg/mindstudio.png" alt="MindStudio logo">

MindStudio developer API (api.mindstudio.ai/developer/v2): run published AI agents/apps synchronously or asynchronously with launch variables, load the workspace's agent catalog, and inspect an agent's workflows.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [mindstudio.ai](https://mindstudio.ai) |
| **Authentication** | API key |
| **Slug** | `mindstudio` |

## Use it

Add MindStudio from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mindstudio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Agent Workflows</td><td><code>listAgentWorkflows</code></td><td>Returns the workflows published inside one MindStudio agent, including each workflow's launch variables and output schema. Used by the official NPM SDK to generate typed clients. Requires the agent's UUID.</td></tr><tr><td>List Apps</td><td><code>listApps</code></td><td>Returns just the array of AI agents/apps in the workspace, without the organization wrapper returned by Load Workspace Apps. Undocumented route discovered by live sweep.</td></tr><tr><td>Load Workspace Apps</td><td><code>loadApps</code></td><td>Loads the MindStudio workspace that owns the API token: returns orgId, orgName and the list of published AI agents/apps available to run. Use it to discover a valid appId before calling Run App.</td></tr><tr><td>Load Workspace Workers</td><td><code>loadWorkers</code></td><td>Worker-namespace alias of Load Workspace Apps, used by the official MindStudio NPM SDK for agent discovery. Returns orgId, orgName and the workspace's agents/workers.</td></tr><tr><td>Run App</td><td><code>runApp</code></td><td>Executes a published MindStudio AI agent/app. Synchronous by default (returns threadId, thread and result). Supply callbackUrl to run asynchronously and receive the result by HTTP POST to that URL instead. WARNING: each run invokes a real LLM and consumes workspace credits.</td></tr><tr><td>Run Worker</td><td><code>runWorker</code></td><td>Worker-namespace alias of Run App, the route used by the official MindStudio NPM SDK. Executes a published agent workflow with launch variables. WARNING: each run invokes a real LLM and consumes workspace credits.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>App Run Completed</td><td><code>app.run.completed</code></td><td>Fires when an asynchronous MindStudio agent run finishes. To receive it, pass this webhook's URL as the callbackUrl input of the Run App or Run Worker action; MindStudio has no webhook registration API, so delivery is opted into per run. Payload schema is MODELLED from the documented synchronous run response (success/threadId/thread/result/billingCost) because the callback body is not documented and could not be captured: the credentialed workspace contains zero agents, so no run could be started.</td></tr></tbody></table>
