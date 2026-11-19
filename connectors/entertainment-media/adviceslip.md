---
description: "Advice Slip API is a free, public, keyless service that returns short pieces of fortune-cookie style advice."
hidden: true
---

# Advice Slip API

<img src="../../.gitbook/assets/connectors/lg/adviceslip.png" alt="Advice Slip API logo">

Supports fetching a random advice slip, fetching a specific slip by its numeric id, and searching slips by keyword.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [api.adviceslip.com](https://api.adviceslip.com) |
| **Authentication** | No authentication |
| **Slug** | `adviceslip` |

## Use it

Add Advice Slip API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.adviceslip.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Advice By Id</td><td><code>getAdviceById</code></td><td>Fetches a specific advice slip by its numeric id. If the id does not correspond to an existing slip, the API responds with HTTP 200 and an error-shaped message body rather than a 404, so callers should check for the presence of the message field to detect a miss. Docs: https://api.adviceslip.com/</td></tr><tr><td>Get Daily Advice RSS</td><td><code>getDailyAdviceRss</code></td><td>Fetch the Daily Advice Slip RSS 2.0 feed (GET /daily_adviceslip.rss): one piece of advice chosen at random each day. Returns XML. Docs: https://api.adviceslip.com/</td></tr><tr><td>Get Random Advice</td><td><code>getRandomAdvice</code></td><td>Fetches a single random advice slip. Returns a short fortune-cookie style piece of advice with its numeric id. Each call may return a different slip; results are lightly cached upstream for a few seconds. Docs: https://api.adviceslip.com/</td></tr><tr><td>Search Advice Slips</td><td><code>searchAdviceSlips</code></td><td>Searches all advice slips for a keyword and returns every matching slip with its id, text, and date. Returns HTTP 200 with a notice-shaped message body instead of an empty array when nothing matches. Docs: https://api.adviceslip.com/</td></tr></tbody></table>
