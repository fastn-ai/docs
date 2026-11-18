---
description: "Ceramic AI is a web-scale search API built for LLMs and AI agents."
hidden: true
---

# Ceramic AI

<img src="../../.gitbook/assets/connectors/lg/ceramic-ai.png" alt="Ceramic AI logo">

Ceramic AI is a web-scale search API built for LLMs and AI agents. This connector wraps the Ceramic Search API: send a natural-language or keyword query and receive ranked web results with titles, URLs and content snippets.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ceramic.ai](https://ceramic.ai) |
| **Authentication** | Bearer token |
| **Slug** | `ceramicAi` |

## Use it

Add Ceramic AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ceramicAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Search Web | `searchWeb` | Searches the web with Ceramic Search and returns ranked results, each with a page title, URL and a content snippet. The query should be in keyword form and contain between 1 and 50 words. Each call consumes one search credit. |
