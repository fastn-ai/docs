---
description: "Open-Elevation is a free, open-source elevation API."
---

# Open-Elevation

Open-Elevation is a free, open-source elevation API. Get the ground elevation in metres for any latitude/longitude points worldwide, one at a time or in bulk, from SRTM terrain data. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [open-elevation.com](https://open-elevation.com) |
| **Authentication** | No authentication |
| **Actions** | 2 |
| **Events** | 0 |
| **Slug** | `openElevation` |

## Use it

Add Open-Elevation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openElevation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Lookup Elevation | `lookupElevation` | Get the elevation in metres for one or more latitude/longitude points (GET /api/v1/lookup?locations=lat,lng\|lat,lng). The GET request line is limited to 1024 bytes - use Lookup Elevation (POST) for many points. Invalid input returns 400 invalid_locations. Docs: https://github.com/Jorl17/open-elevation/blob/master/docs/api.md |
| Lookup Elevation (POST) | `lookupElevationPost` | Get the elevation in metres for a list of points sent as JSON - no size limit on the request (POST /api/v1/lookup). Docs: https://github.com/Jorl17/open-elevation/blob/master/docs/api.md |
