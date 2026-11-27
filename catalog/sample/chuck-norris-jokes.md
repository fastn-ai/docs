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

## Connect in Fastn

Your customers connect Chuck Norris Jokes from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Chuck Norris Jokes**.
2. Select **Connect** on the Chuck Norris Jokes card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Chuck Norris Jokes needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Chuck Norris Jokes's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Joke</td><td><code>getJoke</code></td><td>Get one joke by its id, the permalink given in each joke's url field Unknown ids return 404. Docs: https://api.chucknorris.io/</td></tr><tr><td>Get Random Joke</td><td><code>getRandomJoke</code></td><td>Get one random Chuck Norris joke, optionally from a given category An unknown category Docs: https://api.chucknorris.io/</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>List all joke categories Docs: https://api.chucknorris.io/</td></tr><tr><td>Search Jokes</td><td><code>searchJokes</code></td><td>Free-text search across all jokes The query must be 3 to 120 characters. Docs: https://api.chucknorris.io/</td></tr></tbody></table>

