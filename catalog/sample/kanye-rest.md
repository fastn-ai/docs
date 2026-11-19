---
description: "Kanye Rest is a free collection of Kanye West quotes. Get a random quote or list all quotes."
hidden: true
---

# Kanye Rest

<img src="../../.gitbook/assets/connectors/lg/kanye-rest.png" alt="Kanye Rest logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [kanye.rest](https://kanye.rest) |
| **Authentication** | No sign-in needed |
| **Slug** | `kanyeRest` |

## Setup

Kanye Rest needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Kanye Rest from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.kanyeRest.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Random Quote</td><td><code>getRandomQuote</code></td><td>Get one random Kanye West quote as JSON Docs: https://github.com/ajzbc/kanye.rest#usage</td></tr><tr><td>Get Random Quote as Text</td><td><code>getRandomQuoteText</code></td><td>Get one random Kanye West quote as plain text Docs: https://github.com/ajzbc/kanye.rest#usage</td></tr><tr><td>List All Quotes</td><td><code>listQuotes</code></td><td>Get every quote in the collection as a list of strings The vendor notes this response format may change. Docs: https://github.com/ajzbc/kanye.rest#usage</td></tr></tbody></table>

## Events

Kanye Rest has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
