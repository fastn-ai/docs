---
description: "icanhazdadjoke is a free collection of dad jokes. Get a random joke, look up a joke by ID or search jokes."
hidden: true
---

# icanhazdadjoke

<img src="../../.gitbook/assets/connectors/lg/icanhazdadjoke.png" alt="icanhazdadjoke logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [icanhazdadjoke.com](https://icanhazdadjoke.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `icanhazdadjoke` |

## Setup

icanhazdadjoke needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add icanhazdadjoke from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.icanhazdadjoke.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Joke</td><td><code>getJoke</code></td><td>Get one dad joke by its id Unknown ids return status 404 with a message. Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Get Joke Image</td><td><code>getJokeImage</code></td><td>Get one dad joke rendered as a PNG image Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Get Joke via GraphQL</td><td><code>queryJokeGraphql</code></td><td>Fetch a random dad joke with id, text and permalink through the GraphQL endpoint, query { joke { id joke permalink } }). Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Get Random Joke</td><td><code>getRandomJoke</code></td><td>Get one random dad joke Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Get Random Joke for Slack</td><td><code>getRandomJokeSlack</code></td><td>Get one random dad joke formatted as a Slack message Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Search Jokes</td><td><code>searchJokes</code></td><td>Search dad jokes by a term, or list all jokes when no term is given, with paging Docs: https://icanhazdadjoke.com/api</td></tr></tbody></table>

## Events

icanhazdadjoke has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
