---
description: "Placekey is a universal identifier for physical places. Get a Placekey for an address or point of interest, one at a time or in bulk."
hidden: true
---

# Placekey

<img src="../../.gitbook/assets/connectors/lg/placekey.png" alt="Placekey logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [placekey.io](https://placekey.io) |
| **Authentication** | API key |
| **Slug** | `placekey` |

## Setup

Your customers enter their API key for Placekey when they connect. Nothing else needs setting up.

## Use it

Add Placekey from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.placekey.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Placekey</td><td><code>getPlacekey</code></td><td>Resolves a single place to its Placekey identifier. Supply an address, a point-of-interest name with its address, or a latitude and longitude pair. Coordinates alone return only the "Where" part of the Placekey; an address is required to receive the full What@Where format. Optional enrichment fields such as the address Placekey, building Placekey, match confidence, normalized address, geocode, RESO UPI, parcel number, census GEOID and Overture Maps GERS identifier can be requested through the options field.</td></tr><tr><td>Get Placekeys In Bulk</td><td><code>getPlacekeysInBulk</code></td><td>Resolves up to 100 places to their Placekey identifiers in a single request. Every query in the batch must share the same ISO country code. Each query may carry its own query_id which is echoed back so results can be matched to inputs. The options field is set once at the top level and applies to every query in the batch. Placekey returns results as a JSON array in the same order as the submitted queries.</td></tr></tbody></table>

## Events

Placekey has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
