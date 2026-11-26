---
description: "Google Programmable Search runs searches against a custom search engine. Search the web or a restricted set of sites."
hidden: true
---

# Google Programmable Search

<img src="../../.gitbook/assets/connectors/lg/google-programmable-search.png" alt="Google Programmable Search logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [programmablesearchengine.google.com](https://programmablesearchengine.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleProgrammableSearch` |

## Setup

Your customers sign in to Google Programmable Search through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Programmable Search from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleProgrammableSearch.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search</td><td><code>search</code></td><td>Runs a query against a Programmable Search Engine and returns ranked results with title, snippet, display link and full link.</td></tr><tr><td>Search Site Restricted</td><td><code>searchSiteRestricted</code></td><td>Same as Search but against an engine configured to cover only specific sites; it has no daily query limit.</td></tr></tbody></table>

## Events

Google Programmable Search has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
