---
description: "Hacker News search via the Algolia HN Search API."
hidden: true
---

# Hacker News

Hacker News search via the Algolia HN Search API. Public read-only access to stories, comments, polls, and users. Used to ingest HN discussions as pain signals.

| | |
| --- | --- |
| **Category** | [Social media](README.md) |
| **Website** | [hn.algolia.com](https://hn.algolia.com) |
| **Authentication** | No authentication |
| **Actions** | 4 |
| **Events** | 0 |
| **Slug** | `hackernews` |

## Use it

Add Hacker News from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hackernews.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Item | `getItem` | Retrieve a story or comment by id with full nested comment tree. |
| Get User | `getUser` | Retrieve an HN user profile. |
| Search By Date | `searchByDate` | Same as search but ordered by date (newest first). Use this for time-based polling of new HN content. |
| Search By Relevance | `searchByRelevance` | Full-text search. |
