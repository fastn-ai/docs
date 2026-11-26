---
description: "Google Maps Grounding Lite gives AI agents Google Maps data. Search places, look up weather, compute routes and resolve place names."
hidden: true
---

# Google Maps Grounding Lite

<img src="../../.gitbook/assets/connectors/lg/google-maps-grounding-lite.png" alt="Google Maps Grounding Lite logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [mapstools.googleapis.com](https://mapstools.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleMapsGroundingLite` |

## Setup

Your customers sign in to Google Maps Grounding Lite through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Maps Grounding Lite from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleMapsGroundingLite.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Events

Google Maps Grounding Lite has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
