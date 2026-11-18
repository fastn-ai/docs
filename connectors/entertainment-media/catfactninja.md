---
description: "A free, public, fully keyless API (catfact.ninja) that returns random cat facts and a list of cat breeds with their attributes."
hidden: true
---

# Cat Facts API

<img src="../../.gitbook/assets/connectors/lg/catfactninja.png" alt="Cat Facts API logo">

A free, public, fully keyless API (catfact.ninja) that returns random cat facts and a list of cat breeds with their attributes.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [catfact.ninja](https://catfact.ninja) |
| **Authentication** | No authentication |
| **Slug** | `catfactninja` |

## Use it

Add Cat Facts API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.catfactninja.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Call MCP Server | `callMcpServer` | Send a JSON-RPC 2.0 request to the catfact.ninja MCP server endpoint (POST /mcp, Streamable HTTP). Methods include initialize, tools/list and tools/call. Tools: random-cat-fact (max_length), list-cat-facts (max_length, limit default 10 max 1000), list-breeds (limit default 25 max 1000). Rate limited to 100 requests/minute. Docs: https://catfact.ninja/docs |
| Get Random Fact | `getRandomFact` | Returns a single random cat fact. Optionally cap the fact length with max_length so only facts at or under that character count are returned. Returns 404 'Fact not found' if no fact fits max_length. Docs: https://catfact.ninja/docs |
| List Breeds | `listBreeds` | Returns a paginated list of cat breeds with their country, origin, coat, and pattern attributes. Supports page for pagination. Docs: https://catfact.ninja/docs |
| List Facts | `listFacts` | Returns a paginated list of cat facts. Optionally filter by max_length and control page size with limit. Supports page for pagination. Docs: https://catfact.ninja/docs |
