---
description: "The UK Office for National Statistics (ONS) open API: browse datasets, editions, versions, dimensions and metadata (e.g."
---

# Office for National Statistics (ONS) API

The UK Office for National Statistics (ONS) open API: browse datasets, editions, versions, dimensions and metadata (e.g. CPIH inflation), code lists, dimension hierarchies, Census 2021 population types, areas and observations, plus search of ONS content, the release calendar and topics. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [ons.gov.uk](https://ons.gov.uk) |
| **Authentication** | No authentication |
| **Actions** | 36 |
| **Events** | 0 |
| **Slug** | `onsApi` |

## Use it

Add Office for National Statistics (ONS) API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.onsApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Area | `getArea` | Get one area by code (GET .../area-types/{area-type}/areas/{area-id}). Docs: https://developer.ons.gov.uk/population-types/ |
| Get Census Observations | `getCensusObservations` | Get Census 2021 counts for an area type (optionally one or more areas) cross-tabulated by up to a few dimensions (GET /population-types/{population-type}/census-observations). Docs: https://developer.ons.gov.uk/population-types/ |
| Get Code | `getCode` | Get one code of a code list edition (GET .../codes/{code_id}). Docs: https://developer.ons.gov.uk/code-list/ |
| Get Code List | `getCodeList` | Get one code list (GET /code-lists/{id}). Docs: https://developer.ons.gov.uk/code-list/ |
| Get Code List Edition | `getCodeListEdition` | Get one edition of a code list (GET /code-lists/{id}/editions/{edition}). Docs: https://developer.ons.gov.uk/code-list/ |
| Get Dataset | `getDataset` | Get one dataset: title, description, contacts, release frequency, latest version links (GET /datasets/{id}). Docs: https://developer.ons.gov.uk/dataset/ |
| Get Dataset Edition | `getDatasetEdition` | Get one edition of a dataset with its latest version link (GET /datasets/{id}/editions/{edition}). Docs: https://developer.ons.gov.uk/dataset/ |
| Get Dataset Version | `getDatasetVersion` | Get one version: release date, dimensions, downloads (CSV/XLSX links) and usage notes (GET /datasets/{id}/editions/{edition}/versions/{version}). Docs: https://developer.ons.gov.uk/dataset/ |
| Get Dimension Hierarchy | `getHierarchy` | Get the root of a hierarchical dimension of a dataset version instance, with its children (GET /hierarchies/{instance_id}/{dimension_name}). Docs: https://developer.ons.gov.uk/hierarchy/ |
| Get Dimension Hierarchy Code | `getHierarchyCode` | Get one code in a dimension hierarchy with its parent breadcrumbs and children (GET /hierarchies/{instance_id}/{dimension_name}/{code_id}). Docs: https://developer.ons.gov.uk/hierarchy/ |
| Get Navigation | `getNavigation` | Get the topic and subtopic tree used for the ONS website navigation (GET /navigation). Docs: https://developer.ons.gov.uk/topic/ |
| Get Population Type | `getPopulationType` | Get one census population type (GET /population-types/{population-type}). Docs: https://developer.ons.gov.uk/population-types/ |
| Get Topic | `getTopic` | Get one topic by id (GET /topics/{id}). Docs: https://developer.ons.gov.uk/topic/ |
| Get Version Metadata | `getVersionMetadata` | Get the metadata of a dataset version: methodology, contacts, keywords, dimensions, downloads (GET .../versions/{version}/metadata). Docs: https://developer.ons.gov.uk/dataset/ |
| List Area Type Parents | `listAreaTypeParents` | List the parent area types of an area type (GET .../area-types/{area-type}/parents). Docs: https://developer.ons.gov.uk/population-types/ |
| List Area Types | `listAreaTypes` | List the geography area types available for a population type, e.g. ctry, rgn, ltla (GET /population-types/{population-type}/area-types). Docs: https://developer.ons.gov.uk/population-types/ |
| List Areas | `listAreas` | List the areas of an area type, optionally filtered by name (GET .../area-types/{area-type}/areas). Docs: https://developer.ons.gov.uk/population-types/ |
| List Census Dimensions | `listPopulationDimensions` | List the census variables (dimensions) of a population type, optionally searched by name (GET /population-types/{population-type}/dimensions). Docs: https://developer.ons.gov.uk/population-types/ |
| List Code List Editions | `listCodeListEditions` | List the editions of a code list (GET /code-lists/{id}/editions). Docs: https://developer.ons.gov.uk/code-list/ |
| List Code Lists | `listCodeLists` | List the code lists (classifications) used by datasets (GET /code-lists). Docs: https://developer.ons.gov.uk/code-list/ |
| List Codes | `listCodes` | List the codes of a code list edition (GET /code-lists/{id}/editions/{edition}/codes). Docs: https://developer.ons.gov.uk/code-list/ |
| List Dataset Editions | `listDatasetEditions` | List the editions of a dataset (GET /datasets/{id}/editions). Docs: https://developer.ons.gov.uk/dataset/ |
| List Dataset Versions | `listDatasetVersions` | List the versions of a dataset edition, newest first, with release dates and download links (GET /datasets/{id}/editions/{edition}/versions). Docs: https://developer.ons.gov.uk/dataset/ |
| List Datasets | `listDatasets` | List ONS datasets available through the API (GET /datasets). Docs: https://developer.ons.gov.uk/dataset/ |
| List Datasets Using Code | `listCodeDatasets` | List the datasets that use a code (GET .../codes/{code_id}/datasets). Docs: https://developer.ons.gov.uk/code-list/ |
| List Dimension Categorisations | `listDimensionCategorisations` | List the categorisations (category groupings) of a census dimension (GET .../dimensions/{dimension}/categorisations). Docs: https://developer.ons.gov.uk/population-types/ |
| List Dimension Options | `listDimensionOptions` | List the options (codes and labels) of one dimension of a dataset version (GET .../dimensions/{dimension}/options). Docs: https://developer.ons.gov.uk/dataset/ |
| List Population Types | `listPopulationTypes` | List the Census 2021 population types (e.g. UR all usual residents, HH households) (GET /population-types). Docs: https://developer.ons.gov.uk/population-types/ |
| List Subtopics | `listSubtopics` | List the subtopics of a topic (GET /topics/{id}/subtopics). Docs: https://developer.ons.gov.uk/topic/ |
| List Topic Content | `listTopicContent` | List published content items (articles, bulletins, datasets) tagged with a topic (GET /topics/{id}/content). Docs: https://developer.ons.gov.uk/topic/ |
| List Topics | `listTopics` | List the root ONS topics, e.g. Economy, People population and community (GET /topics). Docs: https://developer.ons.gov.uk/topic/ |
| List Version Dimensions | `listVersionDimensions` | List the dimensions of a dataset version (GET .../versions/{version}/dimensions). Docs: https://developer.ons.gov.uk/dataset/ |
| Search | `search` | Search ONS website content (bulletins, articles, datasets, time series) with filters by content type and topic, sorted by relevance or date (GET /search). Docs: https://developer.ons.gov.uk/search/ |
| Search by URIs | `searchByUris` | Get search results for specific ONS page URIs (POST /search/uris). Docs: https://developer.ons.gov.uk/search/ |
| Search Dimension Options | `searchDimensionOptions` | Search the options of a dimension in a dataset version by text (GET /dimension-search/datasets/{id}/editions/{edition}/versions/{version}/dimensions/{name}). Docs: https://developer.ons.gov.uk/dimension-search/ |
| Search Release Calendar | `searchReleases` | Search the ONS release calendar (upcoming, published, cancelled and census releases) (GET /search/releases). Docs: https://developer.ons.gov.uk/search/ |
