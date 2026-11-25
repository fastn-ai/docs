---
description: "Advice Slip is a free service of short pieces of advice. Get random advice, look up advice by ID or search advice slips."
hidden: true
---

# Advice Slip API

<img src="../../.gitbook/assets/connectors/lg/adviceslip.png" alt="Advice Slip API logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [api.adviceslip.com](https://api.adviceslip.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `adviceslip` |

## Setup

Advice Slip API needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Advice Slip API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.adviceslip.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Advice By Id</td><td><code>getAdviceById</code></td><td>Fetches a specific advice slip by its numeric id. If the id does not correspond to an existing slip, the API Docs: https://api.adviceslip.com/</td></tr><tr><td>Get Daily Advice RSS</td><td><code>getDailyAdviceRss</code></td><td>Fetch the Daily Advice Slip RSS 2.0 feed: one piece of advice chosen at random each day. Returns XML. Docs: https://api.adviceslip.com/</td></tr><tr><td>Get Random Advice</td><td><code>getRandomAdvice</code></td><td>Fetches a single random advice slip. Returns a short fortune-cookie style piece of advice with its numeric id. Each call may return a different slip; results are lightly cached upstream for a few seconds. Docs: https://api.adviceslip.com/</td></tr><tr><td>Search Advice Slips</td><td><code>searchAdviceSlips</code></td><td>Searches all advice slips for a keyword and returns every matching slip with its id, text, and date. Docs: https://api.adviceslip.com/</td></tr></tbody></table>

## Events

Advice Slip API has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
