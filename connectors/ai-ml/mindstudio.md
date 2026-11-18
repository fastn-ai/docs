---
description: "MindStudio developer API (api.mindstudio.ai/developer/v2): run published AI agents/apps synchronously or asynchronously with launch variables, load the…"
---

# MindStudio

MindStudio developer API (api.mindstudio.ai/developer/v2): run published AI agents/apps synchronously or asynchronously with launch variables, load the workspace's agent catalog, and inspect an agent's workflows.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [mindstudio.ai](https://mindstudio.ai) |
| **Authentication** | API key |
| **Actions** | 6 |
| **Events** | 1 |
| **Slug** | `mindstudio` |

## Use it

Add MindStudio from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mindstudio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| List Agent Workflows | `listAgentWorkflows` | Returns the workflows published inside one MindStudio agent, including each workflow's launch variables and output schema. Used by the official NPM SDK to generate typed clients. Requires the agent's UUID. |
| List Apps | `listApps` | Returns just the array of AI agents/apps in the workspace, without the organization wrapper returned by Load Workspace Apps. Undocumented route discovered by live sweep. |
| Load Workspace Apps | `loadApps` | Loads the MindStudio workspace that owns the API token: returns orgId, orgName and the list of published AI agents/apps available to run. Use it to discover a valid appId before calling Run App. |
| Load Workspace Workers | `loadWorkers` | Worker-namespace alias of Load Workspace Apps, used by the official MindStudio NPM SDK for agent discovery. Returns orgId, orgName and the workspace's agents/workers. |
| Run App | `runApp` | Executes a published MindStudio AI agent/app. Synchronous by default (returns threadId, thread and result). Supply callbackUrl to run asynchronously and receive the result by HTTP POST to that URL instead. WARNING: each run invokes a real LLM and consumes workspace credits. |
| Run Worker | `runWorker` | Worker-namespace alias of Run App, the route used by the official MindStudio NPM SDK. Executes a published agent workflow with launch variables. WARNING: each run invokes a real LLM and consumes workspace credits. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| App Run Completed | `app.run.completed` | Fires when an asynchronous MindStudio agent run finishes. To receive it, pass this webhook's URL as the callbackUrl input of the Run App or Run Worker action; MindStudio has no webhook registration API, so delivery is opted into per run. Payload schema is MODELLED from the documented synchronous run response (success/threadId/thread/result/billingCost) because the callback body is not documented and could not be captured: the credentialed workspace contains zero agents, so no run could be started. |
