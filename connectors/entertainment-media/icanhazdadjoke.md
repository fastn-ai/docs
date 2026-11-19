---
description: "icanhazdadjoke is the largest free collection of dad jokes online."
hidden: true
---

# icanhazdadjoke

<img src="../../.gitbook/assets/connectors/lg/icanhazdadjoke.png" alt="icanhazdadjoke logo">

Get a random joke, fetch a joke by id (also as an image), search jokes with paging, get a Slack-formatted joke, or query by GraphQL. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [icanhazdadjoke.com](https://icanhazdadjoke.com) |
| **Authentication** | No authentication |
| **Slug** | `icanhazdadjoke` |

## Use it

Add icanhazdadjoke from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.icanhazdadjoke.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Joke</td><td><code>getJoke</code></td><td>Get one dad joke by its id (GET /j/{id}). Unknown ids return status 404 with a message. Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Get Joke Image</td><td><code>getJokeImage</code></td><td>Get one dad joke rendered as a PNG image (GET /j/{id}.png). Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Get Joke via GraphQL</td><td><code>queryJokeGraphql</code></td><td>Fetch a random dad joke with id, text and permalink through the GraphQL endpoint (POST /graphql, query { joke { id joke permalink } }). Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Get Random Joke</td><td><code>getRandomJoke</code></td><td>Get one random dad joke (GET /). Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Get Random Joke for Slack</td><td><code>getRandomJokeSlack</code></td><td>Get one random dad joke formatted as a Slack message (GET /slack). Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Search Jokes</td><td><code>searchJokes</code></td><td>Search dad jokes by a term, or list all jokes when no term is given, with paging (GET /search). Docs: https://icanhazdadjoke.com/api</td></tr></tbody></table>
