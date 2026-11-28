---
description: "MindStudio is a platform for building AI agents. List and run published apps and workers in your workspace."
hidden: true
---

# MindStudio

<img src="../../.gitbook/assets/connectors/lg/mindstudio.png" alt="MindStudio logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [mindstudio.ai](https://mindstudio.ai) |
| **Authentication** | API key |
| **Slug** | `mindstudio` |

## Setup

Your customers enter their API key for MindStudio when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect MindStudio from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **MindStudio**.
2. Select **Connect** on the MindStudio card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use MindStudio's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Agent Workflows</td><td><code>listAgentWorkflows</code></td><td>Returns the workflows published inside one MindStudio agent, including each workflow's launch variables and output schema. Used by the official NPM SDK to generate typed clients. Requires the agent's UUID.</td></tr><tr><td>List Apps</td><td><code>listApps</code></td><td>Returns just the array of AI agents/apps in the workspace, without the organization wrapper returned by Load Workspace Apps. Undocumented route discovered by live sweep.</td></tr><tr><td>Load Workspace Apps</td><td><code>loadApps</code></td><td>Loads the MindStudio workspace that owns the API token: returns orgId, orgName and the list of published AI agents/apps available to run. Use it to discover a valid appId before calling Run App.</td></tr><tr><td>Load Workspace Workers</td><td><code>loadWorkers</code></td><td>Worker-namespace alias of Load Workspace Apps, used by the official MindStudio NPM SDK for agent discovery. Returns orgId, orgName and the workspace's agents/workers.</td></tr><tr><td>Run App</td><td><code>runApp</code></td><td>Executes a published MindStudio AI agent/app. Synchronous by default (returns threadId, thread and result). Supply callbackUrl to run asynchronously and receive the result by HTTP POST to that URL instead. WARNING: each run invokes a real LLM and consumes workspace credits.</td></tr><tr><td>Run Worker</td><td><code>runWorker</code></td><td>Worker-namespace alias of Run App, the route used by the official MindStudio NPM SDK. Executes a published agent workflow with launch variables. WARNING: each run invokes a real LLM and consumes workspace credits.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>App Run Completed</td><td><code>app.run.completed</code></td><td>Fires when an asynchronous MindStudio agent run finishes. To receive it, pass this webhook's URL as the callbackUrl input of the Run App or Run Worker action; MindStudio has no webhook registration API, so delivery is opted into per run.</td></tr></tbody></table>
