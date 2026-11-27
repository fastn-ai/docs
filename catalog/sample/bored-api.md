---
description: "The Bored API suggests things to do when you are bored. Get a random activity or filter activities by type and number of participants."
hidden: true
---

# Bored API

<img src="../../.gitbook/assets/connectors/lg/bored-api.png" alt="Bored API logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [bored-api.appbrewery.com](https://bored-api.appbrewery.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `boredApi` |

## Setup

Bored API needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Bored API from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Bored API**.
2. Select **Connect** on the Bored API card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Bored API needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Bored API's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Filter Activities</td><td><code>filterActivities</code></td><td>List activities filtered by type and/or number of participants' when nothing matches. Docs: https://bored-api.appbrewery.com/</td></tr><tr><td>Get Activity</td><td><code>getActivity</code></td><td>Get one activity by its key Unknown keys return 404 'Activity not found'. Docs: https://bored-api.appbrewery.com/</td></tr><tr><td>Get Random Activity</td><td><code>getRandomActivity</code></td><td>Get one randomly selected activity suggestion Docs: https://bored-api.appbrewery.com/</td></tr></tbody></table>

