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

## Use it

Add Bored API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.boredApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Filter Activities</td><td><code>filterActivities</code></td><td>List activities filtered by type and/or number of participants' when nothing matches. Docs: https://bored-api.appbrewery.com/</td></tr><tr><td>Get Activity</td><td><code>getActivity</code></td><td>Get one activity by its key Unknown keys return 404 'Activity not found'. Docs: https://bored-api.appbrewery.com/</td></tr><tr><td>Get Random Activity</td><td><code>getRandomActivity</code></td><td>Get one randomly selected activity suggestion Docs: https://bored-api.appbrewery.com/</td></tr></tbody></table>

## Events

Bored API has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
