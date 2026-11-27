---
description: "Hacker News is a tech news community. Search stories and comments by relevance or date, and read items and users."
hidden: true
---

# Hacker News

<img src="../../.gitbook/assets/connectors/lg/hackernews.png" alt="Hacker News logo">

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [hn.algolia.com](https://hn.algolia.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `hackernews` |

## Setup

Hacker News needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Hacker News from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Hacker News**.
2. Select **Connect** on the Hacker News card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Hacker News needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Hacker News's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Item</td><td><code>getItem</code></td><td>Retrieve a story or comment by id with full nested comment tree.</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Retrieve an HN user profile.</td></tr><tr><td>Search By Date</td><td><code>searchByDate</code></td><td>Same as search but ordered by date (newest first). Use this for time-based polling of new HN content.</td></tr><tr><td>Search By Relevance</td><td><code>searchByRelevance</code></td><td>Full-text search.</td></tr></tbody></table>

