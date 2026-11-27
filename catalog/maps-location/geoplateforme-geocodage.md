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

## Connect in Fastn

Your customers connect Géoplateforme Geocoding (IGN) from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Géoplateforme Geocoding (IGN)**.
2. Select **Connect** on the Géoplateforme Geocoding (IGN) card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Géoplateforme Geocoding (IGN) needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Géoplateforme Geocoding (IGN)'s actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Geocode (Search)</td><td><code>geocode</code></td><td>Recherche par géocodage direct. Docs: https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage (OpenAPI https://data.geopf.fr/geocodage/openapi.yaml)</td></tr><tr><td>Get Capabilities</td><td><code>getCapabilities</code></td><td>Découvrir le service. Découvrir le service: les opérations possibles, les ressources disponibles et les options proposées. Docs: https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage (OpenAPI https://data.geopf.fr/geocodage/openapi.yaml)</td></tr><tr><td>Reverse Geocode</td><td><code>reverseGeocode</code></td><td>Recherche par géocodage inverse. Docs: https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage (OpenAPI https://data.geopf.fr/geocodage/openapi.yaml)</td></tr></tbody></table>

