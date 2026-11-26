---
description: "Fathom is an AI meeting notetaker. Read meetings, teams and team members, and fetch recording summaries and transcripts."
hidden: true
---

# Fathom MCP

<img src="../../.gitbook/assets/connectors/lg/fathom-mcp.png" alt="Fathom MCP logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [fathom.video](https://fathom.video) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `fathomMcp` |

## Setup

Your customers sign in to Fathom MCP through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Fathom MCP from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fathomMcp.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Events

Fathom MCP has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
