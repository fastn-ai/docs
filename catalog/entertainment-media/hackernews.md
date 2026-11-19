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

## Use it

Add Hacker News from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hackernews.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Item</td><td><code>getItem</code></td><td>Retrieve a story or comment by id with full nested comment tree.</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Retrieve an HN user profile.</td></tr><tr><td>Search By Date</td><td><code>searchByDate</code></td><td>Same as search but ordered by date (newest first). Use this for time-based polling of new HN content.</td></tr><tr><td>Search By Relevance</td><td><code>searchByRelevance</code></td><td>Full-text search.</td></tr></tbody></table>

## Events

Hacker News has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
