---
description: "Webflow is a visual website builder. List the sites you can access and get the connected user."
hidden: true
---

# Webflow

<img src="../../.gitbook/assets/connectors/lg/webflow.png" alt="Webflow logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [webflow.com](https://webflow.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `webflow` |

## Setup

Your customers sign in to Webflow through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Webflow from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.webflow.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Authorized User</td><td><code>getAuthorizedUser</code></td><td>Retrieves the Webflow user who authorized the current access token. Useful for identifying the connected account. Requires the authorized_user:read scope.</td></tr><tr><td>Introspect Token</td><td><code>introspectToken</code></td><td>Retrieves information about the current authorization, including the granted scopes, rate limit, and the sites, workspaces, and users the token is authorized to access, along with details of the Webflow application.</td></tr><tr><td>List Sites</td><td><code>listSites</code></td><td>Lists all Webflow sites the authorized token has access to. Returns an empty list when the token is not authorized to any site. Requires the sites:read scope.</td></tr></tbody></table>

## Events

Webflow has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
