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

## Connect in Fastn

Your customers connect Advice Slip API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Advice Slip API**.
2. Select **Connect** on the Advice Slip API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Advice Slip API needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Advice Slip API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Advice By Id</td><td><code>getAdviceById</code></td><td>Fetches a specific advice slip by its numeric id. If the id does not correspond to an existing slip, the API Docs: https://api.adviceslip.com/</td></tr><tr><td>Get Daily Advice RSS</td><td><code>getDailyAdviceRss</code></td><td>Fetch the Daily Advice Slip RSS 2.0 feed: one piece of advice chosen at random each day. Returns XML. Docs: https://api.adviceslip.com/</td></tr><tr><td>Get Random Advice</td><td><code>getRandomAdvice</code></td><td>Fetches a single random advice slip. Returns a short fortune-cookie style piece of advice with its numeric id. Each call may return a different slip; results are lightly cached upstream for a few seconds. Docs: https://api.adviceslip.com/</td></tr><tr><td>Search Advice Slips</td><td><code>searchAdviceSlips</code></td><td>Searches all advice slips for a keyword and returns every matching slip with its id, text, and date. Docs: https://api.adviceslip.com/</td></tr></tbody></table>

