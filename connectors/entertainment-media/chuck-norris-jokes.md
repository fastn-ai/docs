---
description: "chucknorris.io is a free JSON API of hand-curated Chuck Norris facts."
hidden: true
---

# Chuck Norris Jokes

chucknorris.io is a free JSON API of hand-curated Chuck Norris facts. Get a random joke (optionally by category), list categories, search jokes by text, or fetch a joke by id. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [chucknorris.io](https://chucknorris.io) |
| **Authentication** | No authentication |
| **Actions** | 4 |
| **Events** | 0 |
| **Slug** | `chuckNorrisJokes` |

## Use it

Add Chuck Norris Jokes from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.chuckNorrisJokes.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Joke | `getJoke` | Get one joke by its id, the permalink given in each joke's url field (GET /jokes/{id}). Unknown ids return 404. Docs: https://api.chucknorris.io/ |
| Get Random Joke | `getRandomJoke` | Get one random Chuck Norris joke, optionally from a given category (GET /jokes/random). An unknown category returns 404. Docs: https://api.chucknorris.io/ |
| List Categories | `listCategories` | List all joke categories (GET /jokes/categories). Docs: https://api.chucknorris.io/ |
| Search Jokes | `searchJokes` | Free-text search across all jokes (GET /jokes/search). The query must be 3 to 120 characters. Docs: https://api.chucknorris.io/ |
