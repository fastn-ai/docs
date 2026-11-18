---
description: "Positionstack forward and reverse geocoding API by APILayer."
hidden: true
---

# Positionstack

<img src="../../.gitbook/assets/connectors/positionstack.png" alt="Positionstack logo" width="64">

Positionstack forward and reverse geocoding API by APILayer. Forward geocoding converts addresses/place names into latitude/longitude coordinates; reverse geocoding converts coordinates into human-readable addresses. Batch variants of both are available on paid plans only.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [positionstack.com](https://positionstack.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `positionstack` |

## Use it

Add Positionstack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.positionstack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Forward Geocoding | `forwardGeocode` | Converts an address or place name into geographic coordinates (latitude/longitude). Available on the free plan. |
| Forward Geocoding Batch | `forwardGeocodeBatch` | Converts up to 50 addresses/place names into coordinates in a single call. Positionstack restricts batch requests to paid subscription plans only - on the free plan this returns a plan-restriction error (function_access_restricted). |
| Reverse Geocoding | `reverseGeocode` | Converts a coordinate pair (latitude, longitude) into a human-readable address. Available on the free plan. |
| Reverse Geocoding Batch | `reverseGeocodeBatch` | Converts up to 50 coordinate pairs into addresses in a single call. Positionstack restricts batch requests to paid subscription plans only - on the free plan this returns a plan-restriction error (function_access_restricted). |
