---
description: "kanye.rest is a free REST API of Kanye West quotes."
hidden: true
---

# Kanye Rest

<img src="../../.gitbook/assets/connectors/lg/kanye-rest.png" alt="Kanye Rest logo">

kanye.rest is a free REST API of Kanye West quotes. Get a random quote as JSON or plain text, or the full list of quotes. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [kanye.rest](https://kanye.rest) |
| **Authentication** | No authentication |
| **Slug** | `kanyeRest` |

## Use it

Add Kanye Rest from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.kanyeRest.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Random Quote</td><td><code>getRandomQuote</code></td><td>Get one random Kanye West quote as JSON (GET /). Docs: https://github.com/ajzbc/kanye.rest#usage</td></tr><tr><td>Get Random Quote as Text</td><td><code>getRandomQuoteText</code></td><td>Get one random Kanye West quote as plain text (GET /text). Docs: https://github.com/ajzbc/kanye.rest#usage</td></tr><tr><td>List All Quotes</td><td><code>listQuotes</code></td><td>Get every quote in the collection as a list of strings (GET /quotes). The vendor notes this response format may change. Docs: https://github.com/ajzbc/kanye.rest#usage</td></tr></tbody></table>
