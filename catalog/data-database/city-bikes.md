---
description: "CityBikes is an open data service for bike sharing. List bike share networks worldwide and get live station availability."
hidden: true
---

# CityBikes

<img src="../../.gitbook/assets/connectors/lg/city-bikes.png" alt="CityBikes logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [citybik.es](https://citybik.es) |
| **Authentication** | No sign-in needed |
| **Slug** | `cityBikes` |

## Setup

CityBikes needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add CityBikes from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cityBikes.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Bike Share Network</td><td><code>getNetwork</code></td><td>Get one bike sharing network with live station availability (free bikes, empty slots) and free-floating vehicles Unknown ids return 404 'Not Found'. Large networks can return several hundred KB - use fields to limit it. Docs: https://api.citybik.es/v2/</td></tr><tr><td>List Bike Share Networks</td><td><code>listNetworks</code></td><td>List every bike sharing network CityBikes tracks (about 800 systems worldwide) with id, name, operator and location Use fields to trim the response. Docs: https://api.citybik.es/v2/</td></tr></tbody></table>

## Events

CityBikes has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
