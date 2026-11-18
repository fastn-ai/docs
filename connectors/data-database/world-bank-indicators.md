---
description: "The World Bank Indicators API (v2) gives free access to tens of thousands of development indicators and their time series for every country, region and income…"
hidden: true
---

# World Bank Indicators API

<img src="../../.gitbook/assets/connectors/lg/world-bank-indicators.png" alt="World Bank Indicators API logo">

The World Bank Indicators API (v2) gives free access to tens of thousands of development indicators and their time series for every country, region and income group: countries, regions, income levels, lending types, topics, sources, indicators and their data, plus the advanced data and metadata APIs (concepts, metatypes, metadata search). No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [worldbank.org](https://worldbank.org) |
| **Authentication** | No authentication |
| **Slug** | `worldBankIndicators` |

## Use it

Add World Bank Indicators API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.worldBankIndicators.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Country | `getCountry` | Get one or more countries by ISO code (GET /v2/country/{country}). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information |
| Get Country Metadata | `getCountryMetadata` | Get all metadata of one or more countries in a source (GET /v2/sources/{source}/country/{country}/metadata). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information |
| Get Country Metadata by Type | `getCountryMetatypeMetadata` | Get one metadata type (e.g. incomegroup) for one or more countries in a source (GET /v2/sources/{source}/country/{country}/metatypes/{metatype}/metadata). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information |
| Get Country Series Metadata | `getSeriesMetadata` | Get metadata for a series in one or more countries of a source (footnotes, sources) (GET /v2/sources/{source}/country/{country}/series/{series}/metadata). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information |
| Get Income Level | `getIncomeLevel` | Get one income level by code (GET /v2/incomeLevel/{code}). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information |
| Get Indicator | `getIndicator` | Get an indicator's name, source, definition, source organization and topics (GET /v2/indicator/{indicator}). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information |
| Get Indicator Data | `getIndicatorData` | Get indicator values for one or more countries and years (GET /v2/country/{country}/indicator/{indicator}). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information |
| Get Lending Type | `getLendingType` | Get one lending type by code (GET /v2/lendingType/{code}). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information |
| Get Region | `getRegion` | Get one region by code (GET /v2/region/{code}). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information |
| Get Source | `getSource` | Get one data source by id (GET /v2/sources/{source}). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information |

<details>

<summary>See 23 more actions</summary>

* **Get Source Data** `getSourceData`: Get data points from a source by country, series and time with the advanced data API (GET /v2/sources/{source}/country/{country}/series/{series}/time/{time}/data). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **Get Topic** `getTopic`: Get one or more topics by id (GET /v2/topic/{topic}). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Concept Metatypes** `listConceptMetatypes`: List the metadata types of one concept of a source (GET /v2/sources/{source}/concepts/{concept}/metatypes). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Countries** `listCountries`: List countries and aggregates with region, income level, lending type, capital and coordinates; filter by region, income level or lending type (GET /v2/country). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Income Level Countries** `listIncomeLevelCountries`: List the countries in a income level (GET /v2/incomeLevel/{code}/country). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Income Levels** `listIncomeLevels`: List all income levels (GET /v2/incomeLevel). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Indicators** `listIndicators`: List all indicators, optionally only those of one source (to list a topic's indicators use List Topic Indicators) (GET /v2/indicator). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Languages** `listLanguages`: List the languages the API supports for localized names (GET /v2/languages). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Lending Type Countries** `listLendingTypeCountries`: List the countries in a lending type (GET /v2/lendingType/{code}/country). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Lending Types** `listLendingTypes`: List all lending types (GET /v2/lendingType). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Metadata Concepts** `listMetadataConcepts`: List the concepts that carry metadata for a source (GET /v2/sources/{source}/concepts/metadata). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Region Countries** `listRegionCountries`: List the countries in a region (GET /v2/region/{code}/country). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Regions** `listRegions`: List all regions (GET /v2/region). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Source Concept Values** `listSourceConceptValues`: List the values of one concept of a source, e.g. all countries or series (GET /v2/sources/{source}/{concept}/data). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Source Concepts** `listSourceConcepts`: List the concepts (dimensions such as Country, Series, Time) of a source for the advanced data API (GET /v2/sources/{source}/concepts/data). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Source Indicators** `listSourceIndicators`: List the indicators of a data source (GET /v2/source/{source}/indicator). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Source Metatypes** `listSourceMetatypes`: List the metadata types (fields such as IncomeGroup, Region, LongDefinition) of a source (GET /v2/sources/{source}/metatypes). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Sources** `listSources`: List all data sources (databases) such as World Development Indicators (GET /v2/sources). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Topic Indicators** `listTopicIndicators`: List the indicators of a topic (GET /v2/topic/{topic}/indicator). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **List Topics** `listTopics`: List all topics (e.g. Agriculture, Education) (GET /v2/topic). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **Search Concept Metadata** `searchConceptMetadata`: Search the metadata of one concept of a source, e.g. countries matching a name (GET /v2/sources/{source}/concepts/{concept}/search/{query}). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **Search Metatype Metadata** `searchMetatypeMetadata`: Search the values of one metadata type of a source (GET /v2/sources/{source}/metatypes/{metatype}/search/{query}). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
* **Search Source Metadata** `searchSourceMetadata`: Search all metadata of a source for a phrase (GET /v2/sources/{source}/search/{query}). Responses are JSON: a [paging info, records] pair for lists; an invalid value returns HTTP 200 with a message array instead. Docs: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information

</details>
