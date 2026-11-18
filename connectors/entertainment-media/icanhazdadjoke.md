---
description: "icanhazdadjoke is the largest free collection of dad jokes online."
hidden: true
---

# icanhazdadjoke

<img src="../../.gitbook/assets/connectors/icanhazdadjoke.png" alt="icanhazdadjoke logo" width="64">

icanhazdadjoke is the largest free collection of dad jokes online. Get a random joke, fetch a joke by id (also as an image), search jokes with paging, get a Slack-formatted joke, or query by GraphQL. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [icanhazdadjoke.com](https://icanhazdadjoke.com) |
| **Authentication** | No authentication |
| **Slug** | `icanhazdadjoke` |

## Use it

Add icanhazdadjoke from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.icanhazdadjoke.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Joke | `getJoke` | Get one dad joke by its id (GET /j/{id}). Unknown ids return status 404 with a message. Docs: https://icanhazdadjoke.com/api |
| Get Joke Image | `getJokeImage` | Get one dad joke rendered as a PNG image (GET /j/{id}.png). Docs: https://icanhazdadjoke.com/api |
| Get Joke via GraphQL | `queryJokeGraphql` | Fetch a random dad joke with id, text and permalink through the GraphQL endpoint (POST /graphql, query { joke { id joke permalink } }). Docs: https://icanhazdadjoke.com/api |
| Get Random Joke | `getRandomJoke` | Get one random dad joke (GET /). Docs: https://icanhazdadjoke.com/api |
| Get Random Joke for Slack | `getRandomJokeSlack` | Get one random dad joke formatted as a Slack message (GET /slack). Docs: https://icanhazdadjoke.com/api |
| Search Jokes | `searchJokes` | Search dad jokes by a term, or list all jokes when no term is given, with paging (GET /search). Docs: https://icanhazdadjoke.com/api |
