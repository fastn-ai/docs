---
description: "The Géoplateforme geocoding service from IGN (the French national mapping agency, successor of api-adresse.data.gouv.fr) geocodes and reverse geocodes French…"
hidden: true
---

# Géoplateforme Geocoding (IGN)

<img src="../../.gitbook/assets/connectors/lg/geoplateforme-geocodage.png" alt="Géoplateforme Geocoding (IGN) logo">

The Géoplateforme geocoding service from IGN (the French national mapping agency, successor of api-adresse.data.gouv.fr) geocodes and reverse geocodes French addresses (Base Adresse Nationale), points of interest and cadastral parcels, with autocomplete and filters by postcode, INSEE code, department and type. No API key needed.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [geopf.fr](https://geopf.fr) |
| **Authentication** | No authentication |
| **Slug** | `geoplateformeGeocodage` |

## Use it

Add Géoplateforme Geocoding (IGN) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.geoplateformeGeocodage.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Geocode (Search)</td><td><code>geocode</code></td><td>Recherche par géocodage direct. Docs: https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage (OpenAPI https://data.geopf.fr/geocodage/openapi.yaml) (GET /search)</td></tr><tr><td>Get Capabilities</td><td><code>getCapabilities</code></td><td>Découvrir le service. Découvrir le service: les opérations possibles, les ressources disponibles et les options proposées. Docs: https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage (OpenAPI https://data.geopf.fr/geocodage/openapi.yaml) (GET /getCapabilities)</td></tr><tr><td>Reverse Geocode</td><td><code>reverseGeocode</code></td><td>Recherche par géocodage inverse. Docs: https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage (OpenAPI https://data.geopf.fr/geocodage/openapi.yaml) (GET /reverse)</td></tr></tbody></table>
