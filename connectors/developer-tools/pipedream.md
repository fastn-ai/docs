---
description: "Pipedream is a workflow automation platform for developers. Manage workflows, sources, components, subscriptions and webhooks."
hidden: true
---

# Pipedream

<img src="../../.gitbook/assets/connectors/lg/pipedream.png" alt="Pipedream logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [pipedream.com](https://pipedream.com) |
| **Authentication** | API key or token |
| **Slug** | `pipedream` |

## Setup

Your customers enter their API key or token for Pipedream when they connect. Nothing else needs setting up.

## Use it

Add Pipedream from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pipedream.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Auto Subscription</td><td><code>createAutoSubscription</code></td><td>Automatically subscribe a listener to a named event channel on every workflow and source created in the workspace from now on.</td></tr><tr><td>Create Component</td><td><code>createComponent</code></td><td>Register a component in the workspace from raw component code or from a URL where the code is hosted. The returned component ID can then be deployed as a source.</td></tr><tr><td>Create Source</td><td><code>createSource</code></td><td>Deploy a component as a running event source in the workspace. Supply exactly one of component_id, component_code or component_url.</td></tr><tr><td>Create Subscription</td><td><code>createSubscription</code></td><td>Subscribe a listener (a source, workflow or webhook) to the events emitted by another source or workflow.</td></tr><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Create a webhook that delivers subscribed events to an HTTP endpoint you control. Subscribe it to a source or workflow with Create Subscription.</td></tr><tr><td>Create Workflow</td><td><code>createWorkflow</code></td><td>Create a workflow in a project from a workflow template, supplying the trigger, step and settings definitions.</td></tr><tr><td>Delete Source</td><td><code>deleteSource</code></td><td>Permanently delete a deployed event source and stop it from emitting further events.</td></tr><tr><td>Delete Source Events</td><td><code>deleteSourceEvents</code></td><td>Delete events emitted by a source. Passing neither start_id nor end_id deletes every event for the source.</td></tr><tr><td>Delete Subscription</td><td><code>deleteSubscription</code></td><td>Remove an event subscription between an emitter and a listener.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Permanently delete a webhook and stop event delivery to its endpoint.</td></tr></tbody></table>

<details>

<summary>View 17 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get App</td><td><code>getApp</code></td><td>Retrieve a single app from Pipedream's integration registry by its app ID or name slug.</td></tr><tr><td>Get Component</td><td><code>getComponent</code></td><td>Retrieve a component saved in the workspace by its component key or component ID.</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Retrieve the profile of the user that owns the API key, including their email and the workspaces they belong to.</td></tr><tr><td>Get OAuth Access Token</td><td><code>getOauthAccessToken</code></td><td>Exchange a workspace OAuth client's credentials for a short-lived Pipedream API access token using the client_credentials grant.</td></tr><tr><td>Get Registry Component</td><td><code>getRegistryComponent</code></td><td>Retrieve a component from Pipedream's global public registry by its key.</td></tr><tr><td>Get Workflow</td><td><code>getWorkflow</code></td><td>Retrieve a workflow's definition, including its triggers and steps.</td></tr><tr><td>Get Workspace</td><td><code>getWorkspace</code></td><td>Retrieve the workspace configured on this connection, including its name, billing email and daily credit quota.</td></tr><tr><td>List Apps</td><td><code>listApps</code></td><td>List the apps available in Pipedream's integration registry, optionally filtered by a search string or by whether the app publishes components.</td></tr><tr><td>List Source Events</td><td><code>listSourceEvents</code></td><td>Retrieve the most recent events emitted by a source, newest last.</td></tr><tr><td>List Workflow Emits</td><td><code>listWorkflowEmits</code></td><td>Retrieve the events a workflow emitted on its default channel, newest last.</td></tr><tr><td>List Workflow Errors</td><td><code>listWorkflowErrors</code></td><td>Retrieve the errors a workflow has thrown, newest last, including the original event and context.</td></tr><tr><td>List Workspace Sources</td><td><code>listWorkspaceSources</code></td><td>List every event source configured in the workspace configured on this connection.</td></tr><tr><td>List Workspace Subscriptions</td><td><code>listWorkspaceSubscriptions</code></td><td>List every event subscription configured in the workspace configured on this connection.</td></tr><tr><td>Revoke OAuth Access Token</td><td><code>revokeOauthAccessToken</code></td><td>Revoke a previously issued Pipedream OAuth access token so it can no longer be used.</td></tr><tr><td>Search Registry Components</td><td><code>searchRegistryComponents</code></td><td>Search Pipedream's global component registry with a natural-language query and return the matching sources and actions.</td></tr><tr><td>Update Source</td><td><code>updateSource</code></td><td>Update a deployed source: change its code, its name, or activate and deactivate it.</td></tr><tr><td>Update Workflow</td><td><code>updateWorkflow</code></td><td>Activate or deactivate a deployed workflow.</td></tr></tbody></table>

</details>

## Events

Pipedream has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
