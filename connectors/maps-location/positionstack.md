---
description: "Positionstack forward and reverse geocoding API by APILayer."
hidden: true
---

# Positionstack

<img src="../../.gitbook/assets/connectors/lg/positionstack.png" alt="Positionstack logo">

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

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Forward Geocoding</td><td><code>forwardGeocode</code></td><td>Converts an address or place name into geographic coordinates (latitude/longitude). Available on the free plan.</td></tr><tr><td>Forward Geocoding Batch</td><td><code>forwardGeocodeBatch</code></td><td>Converts up to 50 addresses/place names into coordinates in a single call. Positionstack restricts batch requests to paid subscription plans only - on the free plan this returns a plan-restriction error (function_access_restricted).</td></tr><tr><td>Reverse Geocoding</td><td><code>reverseGeocode</code></td><td>Converts a coordinate pair (latitude, longitude) into a human-readable address. Available on the free plan.</td></tr><tr><td>Reverse Geocoding Batch</td><td><code>reverseGeocodeBatch</code></td><td>Converts up to 50 coordinate pairs into addresses in a single call. Positionstack restricts batch requests to paid subscription plans only - on the free plan this returns a plan-restriction error (function_access_restricted).</td></tr></tbody></table>
