---
description: "Zippopotam.us is a free, keyless postal code API for 60+ countries (GeoNames data): look up the places, state and coordinates for a postal code, or the postal…"
hidden: true
---

# Zippopotam.us

<img src="../../.gitbook/assets/connectors/zippopotamus.png" alt="Zippopotam.us logo" width="64">

Zippopotam.us is a free, keyless postal code API for 60+ countries (GeoNames data): look up the places, state and coordinates for a postal code, or the postal codes for a city.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [zippopotam.us](https://zippopotam.us) |
| **Authentication** | No authentication |
| **Slug** | `zippopotamus` |

## Use it

Add Zippopotam.us from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zippopotamus.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Look Up City Postal Codes | `lookupCity` | Returns the postal codes and coordinates of a city in a state/region of a country. Docs: https://docs.zippopotam.us/docs/getting-started/ |
| Look Up Postal Code | `lookupPostalCode` | Returns the places (name, state, latitude, longitude) for a postal code in a country. Docs: https://docs.zippopotam.us/docs/getting-started/ |
