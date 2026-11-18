---
description: "Google Maps Platform Grounding Lite MCP server (https://mapstools.googleapis.com/mcp), Google's hosted remote Model Context Protocol server (Streamable HTTP)…"
hidden: true
---

# Google Maps Grounding Lite

<img src="../../.gitbook/assets/connectors/lg/google-maps-grounding-lite.png" alt="Google Maps Grounding Lite logo">

Google Maps Platform Grounding Lite MCP server (https://mapstools.googleapis.com/mcp), Google's hosted remote Model Context Protocol server (Streamable HTTP) that grounds AI answers in Google Maps data. Its tools are discovered live from the server and include search_places (find places, businesses and addresses), lookup_weather (current conditions and hourly/daily forecasts), compute_routes (DRIVE or WALK routes between an origin and destination), resolve_names (batch-resolve place names or addresses to place IDs) and resolve_maps_urls (convert Google Maps URLs to place IDs). Authorizes with Google OAuth 2.0 using the scope https://www.googleapis.com/auth/maps-platform.mapstools.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [mapstools.googleapis.com](https://mapstools.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleMapsGroundingLite` |

## Use it

Add Google Maps Grounding Lite from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleMapsGroundingLite.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).
