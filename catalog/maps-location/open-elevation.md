---
description: "Open-Elevation is a free elevation service. Look up the ground elevation for any latitude and longitude."
hidden: true
---

# Open-Elevation

<img src="../../.gitbook/assets/connectors/lg/open-elevation.png" alt="Open-Elevation logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [open-elevation.com](https://open-elevation.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `openElevation` |

## Setup

Open-Elevation needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Open-Elevation from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openElevation.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Lookup Elevation</td><td><code>lookupElevation</code></td><td>Get the elevation in metres for one or more latitude/longitude points,lng|lat,lng). The GET request line is limited to 1024 bytes - use Lookup Elevation (POST) for many points. Invalid input Docs: https://github.com/Jorl17/open-elevation/blob/master/docs/api.md</td></tr><tr><td>Lookup Elevation (POST)</td><td><code>lookupElevationPost</code></td><td>Get the elevation in metres for a list of points sent as JSON - no size limit on the request Docs: https://github.com/Jorl17/open-elevation/blob/master/docs/api.md</td></tr></tbody></table>

## Events

Open-Elevation has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
