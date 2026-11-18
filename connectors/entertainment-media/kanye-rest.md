---
description: "kanye.rest is a free REST API of Kanye West quotes."
---

# Kanye Rest

kanye.rest is a free REST API of Kanye West quotes. Get a random quote as JSON or plain text, or the full list of quotes. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [kanye.rest](https://kanye.rest) |
| **Authentication** | No authentication |
| **Actions** | 3 |
| **Events** | 0 |
| **Slug** | `kanyeRest` |

## Use it

Add Kanye Rest from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.kanyeRest.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Random Quote | `getRandomQuote` | Get one random Kanye West quote as JSON (GET /). Docs: https://github.com/ajzbc/kanye.rest#usage |
| Get Random Quote as Text | `getRandomQuoteText` | Get one random Kanye West quote as plain text (GET /text). Docs: https://github.com/ajzbc/kanye.rest#usage |
| List All Quotes | `listQuotes` | Get every quote in the collection as a list of strings (GET /quotes). The vendor notes this response format may change. Docs: https://github.com/ajzbc/kanye.rest#usage |
