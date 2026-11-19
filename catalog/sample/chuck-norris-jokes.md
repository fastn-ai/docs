---
description: "Chuck Norris Jokes is a free collection of Chuck Norris facts. Get a random joke, list categories or search jokes."
hidden: true
---

# Chuck Norris Jokes

<img src="../../.gitbook/assets/connectors/lg/chuck-norris-jokes.png" alt="Chuck Norris Jokes logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [chucknorris.io](https://chucknorris.io) |
| **Authentication** | No sign-in needed |
| **Slug** | `chuckNorrisJokes` |

## Setup

Chuck Norris Jokes needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Chuck Norris Jokes from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.chuckNorrisJokes.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Joke</td><td><code>getJoke</code></td><td>Get one joke by its id, the permalink given in each joke's url field Unknown ids return 404. Docs: https://api.chucknorris.io/</td></tr><tr><td>Get Random Joke</td><td><code>getRandomJoke</code></td><td>Get one random Chuck Norris joke, optionally from a given category An unknown category Docs: https://api.chucknorris.io/</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>List all joke categories Docs: https://api.chucknorris.io/</td></tr><tr><td>Search Jokes</td><td><code>searchJokes</code></td><td>Free-text search across all jokes The query must be 3 to 120 characters. Docs: https://api.chucknorris.io/</td></tr></tbody></table>

## Events

Chuck Norris Jokes has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
