---
description: "Cat Facts is a free service of cat facts. Get a random cat fact or list facts and cat breeds."
hidden: true
---

# Cat Facts API

<img src="../../.gitbook/assets/connectors/lg/catfactninja.png" alt="Cat Facts API logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [catfact.ninja](https://catfact.ninja) |
| **Authentication** | No sign-in needed |
| **Slug** | `catfactninja` |

## Setup

Cat Facts API needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Cat Facts API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.catfactninja.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Call MCP Server</td><td><code>callMcpServer</code></td><td>Send a JSON-RPC 2.0 request to the catfact.ninja MCP server endpoint, Streamable HTTP). Methods include initialize, tools/list and tools/call. Tools: random-cat-fact (max_length), list-cat-facts (max_length, limit default 10 max 1000), list-breeds (limit default 25 max 1000). Rate limited to 100 requests/minute. Docs: https://catfact.ninja/docs</td></tr><tr><td>Get Random Fact</td><td><code>getRandomFact</code></td><td>Returns a single random cat fact. Optionally cap the fact length with max_length so only facts at or under that character count are returned. Docs: https://catfact.ninja/docs</td></tr><tr><td>List Breeds</td><td><code>listBreeds</code></td><td>Returns a paginated list of cat breeds with their country, origin, coat, and pattern attributes. Supports page for pagination. Docs: https://catfact.ninja/docs</td></tr><tr><td>List Facts</td><td><code>listFacts</code></td><td>Returns a paginated list of cat facts. Optionally filter by max_length and control page size with limit. Supports page for pagination. Docs: https://catfact.ninja/docs</td></tr></tbody></table>

## Events

Cat Facts API has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
