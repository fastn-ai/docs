---
description: "API Géo is the French government's free service for administrative areas. Search communes by postcode, name or location, and read departments and regions."
hidden: true
---

# API Géo

<img src="../../.gitbook/assets/connectors/lg/api-geo-gouv.png" alt="API Géo logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [geo.api.gouv.fr](https://geo.api.gouv.fr) |
| **Authentication** | No sign-in needed |
| **Slug** | `apiGeoGouv` |

## Setup

API Géo needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add API Géo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.apiGeoGouv.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Associated or Delegated Commune</td><td><code>getAssociatedDelegatedCommune</code></td><td>Get one associated or delegated commune by its INSEE code Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Get Commune</td><td><code>getCommune</code></td><td>Get one French commune by its INSEE code, with optional fields such as population, postcodes, surface, centre and contour Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Get Department</td><td><code>getDepartement</code></td><td>Get one French department by code Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Get EPCI</td><td><code>getEpci</code></td><td>Get one EPCI by its SIREN code Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Get Region</td><td><code>getRegion</code></td><td>Get one French region by code Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>List Department Communes</td><td><code>listDepartementCommunes</code></td><td>List all communes of a French department Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>List EPCI Communes</td><td><code>listEpciCommunes</code></td><td>List the communes that belong to an EPCI Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>List Region Departments</td><td><code>listRegionDepartements</code></td><td>List the departments of a French region Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Search Associated and Delegated Communes</td><td><code>searchAssociatedDelegatedCommunes</code></td><td>Search associated and delegated communes (former communes merged into a new one) by coordinates, name, code, EPCI, department or region Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Search Communes</td><td><code>searchCommunes</code></td><td>Search French communes by postcode, coordinates, name (fuzzy, use boost=population to rank big towns first), INSEE code, SIREN, EPCI, department or region Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Departments</td><td><code>searchDepartements</code></td><td>List or search French departments by code, region or name Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Search EPCIs</td><td><code>searchEpcis</code></td><td>Search EPCIs (French inter-municipal cooperation bodies) by name, code, department or region Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr><tr><td>Search Regions</td><td><code>searchRegions</code></td><td>List or search French regions by code or name Docs: https://geo.api.gouv.fr/decoupage-administratif (OpenAPI https://geo.api.gouv.fr/definition.yml)</td></tr></tbody></table>

</details>

## Events

API Géo has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
