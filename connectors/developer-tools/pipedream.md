---
description: "Pipedream is a workflow automation and integration platform for developers."
hidden: true
---

# Pipedream

Pipedream is a workflow automation and integration platform for developers. This connector covers the Pipedream REST API v1: users, workspaces, apps in the integration registry, components, deployed event sources and their events, event subscriptions, webhooks, workflows and workspace OAuth tokens.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [pipedream.com](https://pipedream.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 27 |
| **Events** | 0 |
| **Slug** | `pipedream` |

## Use it

Add Pipedream from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pipedream.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Auto Subscription | `createAutoSubscription` | Automatically subscribe a listener to a named event channel on every workflow and source created in the workspace from now on. |
| Create Component | `createComponent` | Register a component in the workspace from raw component code or from a URL where the code is hosted. The returned component ID can then be deployed as a source. |
| Create Source | `createSource` | Deploy a component as a running event source in the workspace. Supply exactly one of component_id, component_code or component_url. |
| Create Subscription | `createSubscription` | Subscribe a listener (a source, workflow or webhook) to the events emitted by another source or workflow. |
| Create Webhook | `createWebhook` | Create a webhook that delivers subscribed events to an HTTP endpoint you control. Subscribe it to a source or workflow with Create Subscription. |
| Create Workflow | `createWorkflow` | Create a workflow in a project from a workflow template, supplying the trigger, step and settings definitions. |
| Delete Source | `deleteSource` | Permanently delete a deployed event source and stop it from emitting further events. |
| Delete Source Events | `deleteSourceEvents` | Delete events emitted by a source. Passing neither start_id nor end_id deletes every event for the source. |
| Delete Subscription | `deleteSubscription` | Remove an event subscription between an emitter and a listener. |
| Delete Webhook | `deleteWebhook` | Permanently delete a webhook and stop event delivery to its endpoint. |
| Get App | `getApp` | Retrieve a single app from Pipedream's integration registry by its app ID or name slug. |
| Get Component | `getComponent` | Retrieve a component saved in the workspace by its component key or component ID. |
| Get Current User | `getCurrentUser` | Retrieve the profile of the user that owns the API key, including their email and the workspaces they belong to. |
| Get OAuth Access Token | `getOauthAccessToken` | Exchange a workspace OAuth client's credentials for a short-lived Pipedream API access token using the client_credentials grant. |
| Get Registry Component | `getRegistryComponent` | Retrieve a component from Pipedream's global public registry by its key. |
| Get Workflow | `getWorkflow` | Retrieve a workflow's definition, including its triggers and steps. |
| Get Workspace | `getWorkspace` | Retrieve the workspace configured on this connection, including its name, billing email and daily credit quota. |
| List Apps | `listApps` | List the apps available in Pipedream's integration registry, optionally filtered by a search string or by whether the app publishes components. |
| List Source Events | `listSourceEvents` | Retrieve the most recent events emitted by a source, newest last. |
| List Workflow Emits | `listWorkflowEmits` | Retrieve the events a workflow emitted on its default channel, newest last. |
| List Workflow Errors | `listWorkflowErrors` | Retrieve the errors a workflow has thrown, newest last, including the original event and context. |
| List Workspace Sources | `listWorkspaceSources` | List every event source configured in the workspace configured on this connection. |
| List Workspace Subscriptions | `listWorkspaceSubscriptions` | List every event subscription configured in the workspace configured on this connection. |
| Revoke OAuth Access Token | `revokeOauthAccessToken` | Revoke a previously issued Pipedream OAuth access token so it can no longer be used. |
| Search Registry Components | `searchRegistryComponents` | Search Pipedream's global component registry with a natural-language query and return the matching sources and actions. |
| Update Source | `updateSource` | Update a deployed source: change its code, its name, or activate and deactivate it. |
| Update Workflow | `updateWorkflow` | Activate or deactivate a deployed workflow. |
