---
description: "Positionstack is a geocoding service. Convert addresses to coordinates and coordinates to addresses, one at a time or in batches."
hidden: true
---

# Positionstack

<img src="../../.gitbook/assets/connectors/lg/positionstack.png" alt="Positionstack logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [positionstack.com](https://positionstack.com) |
| **Authentication** | API key |
| **Slug** | `positionstack` |

## Setup

Your customers enter their API key for Positionstack when they connect. Nothing else needs setting up.

## Use it

Add Positionstack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.positionstack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Forward Geocoding</td><td><code>forwardGeocode</code></td><td>Converts an address or place name into geographic coordinates (latitude/longitude). Available on the free plan.</td></tr><tr><td>Forward Geocoding Batch</td><td><code>forwardGeocodeBatch</code></td><td>Converts up to 50 addresses/place names into coordinates in a single call. Positionstack restricts batch requests to paid subscription plans only - on the free plan this returns a plan-restriction error (function_access_restricted).</td></tr><tr><td>Reverse Geocoding</td><td><code>reverseGeocode</code></td><td>Converts a coordinate pair (latitude, longitude) into a human-readable address. Available on the free plan.</td></tr><tr><td>Reverse Geocoding Batch</td><td><code>reverseGeocodeBatch</code></td><td>Converts up to 50 coordinate pairs into addresses in a single call. Positionstack restricts batch requests to paid subscription plans only - on the free plan this returns a plan-restriction error (function_access_restricted).</td></tr></tbody></table>

## Events

Positionstack has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
