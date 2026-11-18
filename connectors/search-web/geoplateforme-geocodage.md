---
description: "The Géoplateforme geocoding service from IGN (the French national mapping agency, successor of api-adresse.data.gouv.fr) geocodes and reverse geocodes French…"
---

# Géoplateforme Geocoding (IGN)

The Géoplateforme geocoding service from IGN (the French national mapping agency, successor of api-adresse.data.gouv.fr) geocodes and reverse geocodes French addresses (Base Adresse Nationale), points of interest and cadastral parcels, with autocomplete and filters by postcode, INSEE code, department and type. No API key needed.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [geopf.fr](https://geopf.fr) |
| **Authentication** | No authentication |
| **Actions** | 3 |
| **Events** | 0 |
| **Slug** | `geoplateformeGeocodage` |

## Use it

Add Géoplateforme Geocoding (IGN) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.geoplateformeGeocodage.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Geocode (Search) | `geocode` | Recherche par géocodage direct. Docs: https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage (OpenAPI https://data.geopf.fr/geocodage/openapi.yaml) (GET /search) |
| Get Capabilities | `getCapabilities` | Découvrir le service. Découvrir le service: les opérations possibles, les ressources disponibles et les options proposées. Docs: https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage (OpenAPI https://data.geopf.fr/geocodage/openapi.yaml) (GET /getCapabilities) |
| Reverse Geocode | `reverseGeocode` | Recherche par géocodage inverse. Docs: https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage (OpenAPI https://data.geopf.fr/geocodage/openapi.yaml) (GET /reverse) |
