---
description: "The French national mapping agency's geocoding service. Geocode French addresses and places, and reverse geocode coordinates."
hidden: true
---

# Géoplateforme Geocoding (IGN)

<img src="../../.gitbook/assets/connectors/lg/geoplateforme-geocodage.png" alt="Géoplateforme Geocoding (IGN) logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [geopf.fr](https://geopf.fr) |
| **Authentication** | No sign-in needed |
| **Slug** | `geoplateformeGeocodage` |

## Setup

Géoplateforme Geocoding (IGN) needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Géoplateforme Geocoding (IGN) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.geoplateformeGeocodage.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Geocode (Search)</td><td><code>geocode</code></td><td>Recherche par géocodage direct. Docs: https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage (OpenAPI https://data.geopf.fr/geocodage/openapi.yaml)</td></tr><tr><td>Get Capabilities</td><td><code>getCapabilities</code></td><td>Découvrir le service. Découvrir le service: les opérations possibles, les ressources disponibles et les options proposées. Docs: https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage (OpenAPI https://data.geopf.fr/geocodage/openapi.yaml)</td></tr><tr><td>Reverse Geocode</td><td><code>reverseGeocode</code></td><td>Recherche par géocodage inverse. Docs: https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage (OpenAPI https://data.geopf.fr/geocodage/openapi.yaml)</td></tr></tbody></table>

## Events

Géoplateforme Geocoding (IGN) has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
