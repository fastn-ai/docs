---
description: "Placekey is a free, universal standard identifier for any physical place."
hidden: true
---

# Placekey

<img src="../../.gitbook/assets/connectors/lg/placekey.png" alt="Placekey logo">

Placekey is a free, universal standard identifier for any physical place. This connector covers the complete Placekey API: resolving a single address, point-of-interest or coordinate pair to a Placekey, and resolving up to 100 places in one bulk request, with optional enrichment fields such as address and building Placekeys, match confidence, normalized address, geocode, RESO UPI, parcel number, census GEOID and Overture Maps GERS identifier.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [placekey.io](https://placekey.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `placekey` |

## Use it

Add Placekey from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.placekey.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Placekey | `getPlacekey` | Resolves a single place to its Placekey identifier. Supply an address, a point-of-interest name with its address, or a latitude and longitude pair. Coordinates alone return only the "Where" part of the Placekey; an address is required to receive the full What@Where format. Optional enrichment fields such as the address Placekey, building Placekey, match confidence, normalized address, geocode, RESO UPI, parcel number, census GEOID and Overture Maps GERS identifier can be requested through the options field. |
| Get Placekeys In Bulk | `getPlacekeysInBulk` | Resolves up to 100 places to their Placekey identifiers in a single request. Every query in the batch must share the same ISO country code. Each query may carry its own query_id which is echoed back so results can be matched to inputs. The options field is set once at the top level and applies to every query in the batch. Placekey returns results as a JSON array in the same order as the submitted queries. |
