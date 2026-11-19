---
description: "CityBikes is a free, open API for bike sharing data."
hidden: true
---

# CityBikes

<img src="../../.gitbook/assets/connectors/lg/city-bikes.png" alt="CityBikes logo">

CityBikes is a free, open API for bike sharing data. List about 800 bike sharing networks worldwide and get live station availability (free bikes, empty docks) and free-floating vehicles for any network. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [citybik.es](https://citybik.es) |
| **Authentication** | No authentication |
| **Slug** | `cityBikes` |

## Use it

Add CityBikes from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cityBikes.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Bike Share Network</td><td><code>getNetwork</code></td><td>Get one bike sharing network with live station availability (free bikes, empty slots) and free-floating vehicles (GET /v2/networks/{network_id}). Unknown ids return 404 'Not Found'. Large networks can return several hundred KB - use fields to limit it. Docs: https://api.citybik.es/v2/</td></tr><tr><td>List Bike Share Networks</td><td><code>listNetworks</code></td><td>List every bike sharing network CityBikes tracks (about 800 systems worldwide) with id, name, operator and location (GET /v2/networks). Use fields to trim the response. Docs: https://api.citybik.es/v2/</td></tr></tbody></table>
