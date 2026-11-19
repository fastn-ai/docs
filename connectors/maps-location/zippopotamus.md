---
description: "Zippopotam.us is a free postal code lookup for over 60 countries. Find the places for a postal code or the postal codes for a city."
hidden: true
---

# Zippopotam.us

<img src="../../.gitbook/assets/connectors/lg/zippopotamus.png" alt="Zippopotam.us logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [zippopotam.us](https://zippopotam.us) |
| **Authentication** | No sign-in needed |
| **Slug** | `zippopotamus` |

## Setup

Zippopotam.us needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Zippopotam.us from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zippopotamus.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Look Up City Postal Codes</td><td><code>lookupCity</code></td><td>Returns the postal codes and coordinates of a city in a state/region of a country. Docs: https://docs.zippopotam.us/docs/getting-started/</td></tr><tr><td>Look Up Postal Code</td><td><code>lookupPostalCode</code></td><td>Returns the places (name, state, latitude, longitude) for a postal code in a country. Docs: https://docs.zippopotam.us/docs/getting-started/</td></tr></tbody></table>

## Events

Zippopotam.us has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
