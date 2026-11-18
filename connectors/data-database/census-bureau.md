---
description: "The U.S."
hidden: true
---

# U.S. Census Bureau Data API

<img src="../../.gitbook/assets/connectors/lg/census-bureau.png" alt="U.S. Census Bureau Data API logo">

The U.S. Census Bureau Data API exposes more than 1,800 datasets from the American Community Survey, Decennial Census, Population Estimates, County Business Patterns, Economic Indicators, International Trade and other programs. This connector covers the discovery endpoints (dataset catalog, dataset descriptors, variables, geography, groups, examples, tags and sorts), a generic data query for any dataset, and ready-made query actions for the most used datasets.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [census.gov](https://census.gov) |
| **Authentication** | Credentials you enter |
| **Slug** | `censusBureau` |

## Use it

Add U.S. Census Bureau Data API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.censusBureau.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Dataset | `getDataset` | Returns the catalog descriptor of one dataset: title, description, vintage, path segments, whether it is a time series, and links to its variables, geography, groups, examples, tags, sorts and documentation. |
| Get Group Variables | `getGroupVariables` | Returns the variables that belong to one group (table) of a dataset, keyed by variable name, with label, concept, predicate type, universe and predicate-only flag. |
| Get Variable | `getVariable` | Returns the definition of a single variable in a dataset: its name, label, concept, predicate type, group, allowed values when enumerated, and whether it is required or predicate-only. |
| List Datasets | `listDatasets` | Returns the complete Census Data API catalog (DCAT format) describing every available dataset with its vintage, path segments, title, description and links to its variables, geography, groups, examples, tags and sorts. The catalog is large (over 1,800 datasets). |
| List Datasets By Vintage | `listDatasetsByVintage` | Returns the catalog of datasets available for one vintage year (or for all time series datasets when the vintage is timeseries), with each dataset's path segments, title, description and discovery links. |
| List Examples | `listExamples` | Returns example query components for a dataset: sample get variables and, for every supported geographic level, an example value and the required parent geographies. Use it to build a valid for and in predicate. |
| List Geographies | `listGeographies` | Returns the geographic levels a dataset supports (us, region, state, county, place, tract and so on) with each level's summary-level code, reference date, required parent geographies and wildcard support. Use these names in the for and in predicates of a data query. |
| List Groups | `listGroups` | Returns the variable groups (tables) defined in a dataset, each with its name, description, universe and a link to the variables it contains. A whole group can be requested in a data query with get=group(NAME). |
| List Sorts | `listSorts` | Returns the sort options published for a dataset (the sorts link in its catalog descriptor). Many datasets publish an empty list. |
| List Tags | `listTags` | Returns the topic tags (such as income, poverty, housing or employment) attached to a dataset's variables, useful for discovering which subjects the dataset covers. |

<details>

<summary>See 17 more actions</summary>

* **List Variables** `listVariables`: Returns every variable available in a dataset, keyed by variable name, with its label, concept, predicate type, group, whether it is required in queries and whether it can only be used as a predicate. Use the names in the get parameter of a data query.
* **Query ACS 1-Year Data Product** `queryAcs1YearDataProduct`: Queries an American Community Survey 1-Year data product table set (data profiles, comparison profiles, subject tables, selected population profiles, or public use microdata) for a vintage year. Returns a JSON array of rows with a header row.
* **Query ACS 1-Year Detailed Tables** `queryAcs1YearDetailedTables`: Queries the American Community Survey 1-Year Estimates detailed tables (dataset acs/acs1) for a vintage year. Covers geographies with 65,000 or more people. Returns a JSON array of rows with a header row.
* **Query ACS 1-Year Supplemental Estimates** `queryAcsSupplementalEstimates`: Queries the American Community Survey 1-Year Supplemental Estimates (dataset acs/acsse), simplified tables for geographies with 20,000 or more people. Returns a JSON array of rows with a header row.
* **Query ACS 5-Year Data Product** `queryAcs5YearDataProduct`: Queries an American Community Survey 5-Year data product table set (data profiles, comparison profiles, subject tables, AIAN or selected population tables, EEO tabulation or public use microdata) for a vintage year. Returns a JSON array of rows with a header row.
* **Query ACS 5-Year Detailed Tables** `queryAcs5YearDetailedTables`: Queries the American Community Survey 5-Year Estimates detailed tables (dataset acs/acs5) for a vintage year. Covers all geographies down to block group and ZIP Code Tabulation Area. Returns a JSON array of rows with a header row.
* **Query Business Dynamics Statistics** `queryBusinessDynamicsStatistics`: Queries the Business Dynamics Statistics time series (timeseries/bds): annual establishment and firm counts, job creation and destruction, entries and exits by industry, firm age and size at national, state, metro and county levels. Returns a JSON array of rows with a header row.
* **Query County Business Patterns** `queryCountyBusinessPatterns`: Queries County Business Patterns (dataset cbp) for a year: establishment counts, employment and payroll by industry, employment size and legal form of organization at national, state, county, metro and congressional district levels. Returns a JSON array of rows with a header row.
* **Query Dataset** `queryDataset`: Runs a data query against any Census Data API dataset by vintage and path. Returns a JSON array of rows; the first row is the header of variable names followed by the geography columns. Dataset-specific predicate variables (for example POPGROUP or NAICS2017) are not accepted here; use the dataset-specific query actions for those.
* **Query Decennial Census** `queryDecennialCensus`: Queries a Decennial Census dataset (dataset dec/&lt;table set&gt;) such as the 2020 Redistricting Data (pl), Demographic and Housing Characteristics (dhc), Demographic Profile (dp), Detailed DHC-A/B, or the 2010 and 2000 Summary Files. Returns a JSON array of rows with a header row.
* **Query Economic Indicators Time Series** `queryEconomicIndicators`: Queries an Economic Indicators Time Series dataset (timeseries/eits/&lt;indicator&gt;) such as Monthly Retail Trade (marts, mrts), Manufacturers' Shipments (m3, advm3), New Residential Construction and Sales (resconst, ressales), Housing Vacancies (hv), Business Formation Statistics (bfs), Quarterly Financial Report (qfr) and others. Returns a JSON array of rows with a header row.
* **Query International Data Base** `queryInternationalDataBase`: Queries the International Data Base time series (timeseries/idb/1year or 5year): population estimates and projections by single year or five-year age group, sex and country for 1950 through 2100. Returns a JSON array of rows with a header row.
* **Query International Trade Time Series** `queryInternationalTrade`: Queries the International Trade monthly time series (timeseries/intltrade/&lt;flow&gt;/&lt;classification&gt;) for U.S. exports or imports by Harmonized System, NAICS, end-use, SITC, advanced technology, port, state or USDA classification. Returns a JSON array of rows with a header row.
* **Query Population Estimates** `queryPopulationEstimates`: Queries a Population Estimates Program dataset (dataset pep/&lt;table&gt;) for a vintage year, such as total population, components of change, characteristics by age, sex, race and Hispanic origin, housing units, or national monthly estimates. Returns a JSON array of rows with a header row.
* **Query Small Area Health Insurance Estimates** `querySahie`: Queries the Small Area Health Insurance Estimates time series (timeseries/healthins/sahie): annual health insurance coverage estimates for states and counties by age, sex, race and income-to-poverty ratio. Returns a JSON array of rows with a header row.
* **Query Small Area Income And Poverty Estimates** `querySaipe`: Queries the Small Area Income and Poverty Estimates time series (timeseries/poverty/saipe): annual median household income and poverty estimates for the nation, states and counties. For the school district variant use Query Dataset with vintage timeseries and path poverty/saipe/schdist. Returns a JSON array of rows with a header row.
* **Query ZIP Code Business Patterns** `queryZipCodeBusinessPatterns`: Queries ZIP Code Business Patterns (dataset zbp) for a year: establishment counts, employment and payroll by industry and employment size for five-digit ZIP codes. Available for 1994 through 2018; later years are published as ZIP-level rows in County Business Patterns. Returns a JSON array of rows with a header row.

</details>
