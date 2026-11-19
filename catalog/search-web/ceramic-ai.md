---
description: "Ceramic AI is a web search service built for AI agents. Run keyword or natural-language web searches."
hidden: true
---

# Ceramic AI

<img src="../../.gitbook/assets/connectors/lg/ceramic-ai.png" alt="Ceramic AI logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ceramic.ai](https://ceramic.ai) |
| **Authentication** | Access token |
| **Slug** | `ceramicAi` |

## Setup

Your customers enter their access token for Ceramic AI when they connect. Nothing else needs setting up.

## Use it

Add Ceramic AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ceramicAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Web</td><td><code>searchWeb</code></td><td>Searches the web with Ceramic Search and returns ranked results, each with a page title, URL and a content snippet. The query should be in keyword form and contain between 1 and 50 words. Each call consumes one search credit.</td></tr></tbody></table>

## Events

Ceramic AI has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
