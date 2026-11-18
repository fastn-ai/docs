---
description: "API Géo is the French government's free API for administrative boundaries: search communes by postcode, name or GPS point, and get communes,…"
hidden: true
---

# API Géo

API Géo is the French government's free API for administrative boundaries: search communes by postcode, name or GPS point, and get communes, associated/delegated communes, EPCIs, departments and regions with INSEE codes, population, postcodes and GeoJSON geometry. No API key needed.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [geo.api.gouv.fr](https://geo.api.gouv.fr) |
| **Authentication** | No authentication |
| **Actions** | 13 |
| **Events** | 0 |
| **Slug** | `apiGeoGouv` |

## Use it

Add API Géo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.apiGeoGouv.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Associated or Delegated Commune | `getAssociatedDelegatedCommune` | Get one associated or delegated commune by its INSEE code (GET /communes_associees_deleguees/{code}). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
| Get Commune | `getCommune` | Get one French commune by its INSEE code, with optional fields such as population, postcodes, surface, centre and contour (GET /communes/{code}). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
| Get Department | `getDepartement` | Get one French department by code (GET /departements/{code}). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
| Get EPCI | `getEpci` | Get one EPCI by its SIREN code (GET /epcis/{code}). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
| Get Region | `getRegion` | Get one French region by code (GET /regions/{code}). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
| List Department Communes | `listDepartementCommunes` | List all communes of a French department (GET /departements/{code}/communes). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
| List EPCI Communes | `listEpciCommunes` | List the communes that belong to an EPCI (GET /epcis/{code}/communes). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
| List Region Departments | `listRegionDepartements` | List the departments of a French region (GET /regions/{code}/departements). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
| Search Associated and Delegated Communes | `searchAssociatedDelegatedCommunes` | Search associated and delegated communes (former communes merged into a new one) by coordinates, name, code, EPCI, department or region (GET /communes_associees_deleguees). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
| Search Communes | `searchCommunes` | Search French communes by postcode, coordinates, name (fuzzy, use boost=population to rank big towns first), INSEE code, SIREN, EPCI, department or region (GET /communes). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
| Search Departments | `searchDepartements` | List or search French departments by code, region or name (GET /departements). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
| Search EPCIs | `searchEpcis` | Search EPCIs (French inter-municipal cooperation bodies) by name, code, department or region (GET /epcis). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
| Search Regions | `searchRegions` | List or search French regions by code or name (GET /regions). Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml) |
