---
description: "API Géo is the French government's free API for administrative boundaries: search communes by postcode, name or GPS point, and get communes,…"
hidden: true
---

# API Géo

<img src="../../.gitbook/assets/connectors/lg/api-geo-gouv.png" alt="API Géo logo">

API Géo is the French government's free API for administrative boundaries: search communes by postcode, name or GPS point, and get communes, associated/delegated communes, EPCIs, departments and regions with INSEE codes, population, postcodes and GeoJSON geometry. No API key needed.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [geo.api.gouv.fr](https://geo.api.gouv.fr) |
| **Authentication** | No authentication |
| **Slug** | `apiGeoGouv` |

## Use it

Add API Géo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.apiGeoGouv.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Associated or Delegated Commune</td><td><code>getAssociatedDelegatedCommune</code></td><td>Get one associated or delegated commune by its INSEE code (GET /communes_associees_deleguees/{code}). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Get Commune</td><td><code>getCommune</code></td><td>Get one French commune by its INSEE code, with optional fields such as population, postcodes, surface, centre and contour (GET /communes/{code}). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Get Department</td><td><code>getDepartement</code></td><td>Get one French department by code (GET /departements/{code}). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Get EPCI</td><td><code>getEpci</code></td><td>Get one EPCI by its SIREN code (GET /epcis/{code}). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Get Region</td><td><code>getRegion</code></td><td>Get one French region by code (GET /regions/{code}). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>List Department Communes</td><td><code>listDepartementCommunes</code></td><td>List all communes of a French department (GET /departements/{code}/communes). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>List EPCI Communes</td><td><code>listEpciCommunes</code></td><td>List the communes that belong to an EPCI (GET /epcis/{code}/communes). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>List Region Departments</td><td><code>listRegionDepartements</code></td><td>List the departments of a French region (GET /regions/{code}/departements). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Search Associated and Delegated Communes</td><td><code>searchAssociatedDelegatedCommunes</code></td><td>Search associated and delegated communes (former communes merged into a new one) by coordinates, name, code, EPCI, department or region (GET /communes_associees_deleguees). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Search Communes</td><td><code>searchCommunes</code></td><td>Search French communes by postcode, coordinates, name (fuzzy, use boost=population to rank big towns first), INSEE code, SIREN, EPCI, department or region (GET /communes). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Departments</td><td><code>searchDepartements</code></td><td>List or search French departments by code, region or name (GET /departements). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Search EPCIs</td><td><code>searchEpcis</code></td><td>Search EPCIs (French inter-municipal cooperation bodies) by name, code, department or region (GET /epcis). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Search Regions</td><td><code>searchRegions</code></td><td>List or search French regions by code or name (GET /regions). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr></tbody></table>

</details>
