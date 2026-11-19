---
description: "chucknorris.io is a free JSON API of hand-curated Chuck Norris facts."
hidden: true
---

# Chuck Norris Jokes

<img src="../../.gitbook/assets/connectors/lg/chuck-norris-jokes.png" alt="Chuck Norris Jokes logo">

Get a random joke (optionally by category), list categories, search jokes by text, or fetch a joke by id. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [chucknorris.io](https://chucknorris.io) |
| **Authentication** | No authentication |
| **Slug** | `chuckNorrisJokes` |

## Use it

Add Chuck Norris Jokes from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.chuckNorrisJokes.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Joke</td><td><code>getJoke</code></td><td>Get one joke by its id, the permalink given in each joke's url field (GET /jokes/{id}). Unknown ids return 404. Docs: https://api.chucknorris.io/</td></tr><tr><td>Get Random Joke</td><td><code>getRandomJoke</code></td><td>Get one random Chuck Norris joke, optionally from a given category (GET /jokes/random). An unknown category returns 404. Docs: https://api.chucknorris.io/</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>List all joke categories (GET /jokes/categories). Docs: https://api.chucknorris.io/</td></tr><tr><td>Search Jokes</td><td><code>searchJokes</code></td><td>Free-text search across all jokes (GET /jokes/search). The query must be 3 to 120 characters. Docs: https://api.chucknorris.io/</td></tr></tbody></table>
