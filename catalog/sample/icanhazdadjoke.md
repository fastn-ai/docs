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

## Connect in Fastn

Your customers connect icanhazdadjoke from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **icanhazdadjoke**.
2. Select **Connect** on the icanhazdadjoke card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. icanhazdadjoke needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use icanhazdadjoke's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Joke</td><td><code>getJoke</code></td><td>Get one dad joke by its id Unknown ids return status 404 with a message. Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Get Joke Image</td><td><code>getJokeImage</code></td><td>Get one dad joke rendered as a PNG image Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Get Joke via GraphQL</td><td><code>queryJokeGraphql</code></td><td>Fetch a random dad joke with id, text and permalink through the GraphQL endpoint, query { joke { id joke permalink } }). Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Get Random Joke</td><td><code>getRandomJoke</code></td><td>Get one random dad joke Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Get Random Joke for Slack</td><td><code>getRandomJokeSlack</code></td><td>Get one random dad joke formatted as a Slack message Docs: https://icanhazdadjoke.com/api</td></tr><tr><td>Search Jokes</td><td><code>searchJokes</code></td><td>Search dad jokes by a term, or list all jokes when no term is given, with paging Docs: https://icanhazdadjoke.com/api</td></tr></tbody></table>

