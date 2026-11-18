---
description: "ClinicalTrials.gov (U.S."
hidden: true
---

# ClinicalTrials.gov

ClinicalTrials.gov (U.S. National Library of Medicine) is the registry of clinical studies run around the world. Its API v2 lets you search studies with rich query and filter options, fetch a study by NCT ID, and read the data model, search areas, enumerations and statistics. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [clinicaltrials.gov](https://clinicaltrials.gov) |
| **Authentication** | No authentication |
| **Actions** | 9 |
| **Events** | 0 |
| **Slug** | `clinicalTrialsGov` |

## Use it

Add ClinicalTrials.gov from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.clinicalTrialsGov.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get API Version | `getVersion` | Version. API and data versions. API version follows [Semantic Versioning 2.0.0 Schema](https://semver.org/spec/v2.0.0.html). Data version is UTC timestamp in `yyyy-MM-dd'T'HH:mm:ss` format. (GET /version). Docs: https://clinicaltrials.gov/data-api/api |
| Get Field Value Statistics | `getFieldValueStats` | Field Values. Value statistics of the study leaf fields. (GET /stats/field/values). Docs: https://clinicaltrials.gov/data-api/api |
| Get List Field Size Statistics | `getListFieldSizeStats` | List Field Sizes. Sizes of list/array fields. To search studies by a list field size, use `AREA[FieldName:size]` search operator. For example, [AREA\[Phase:size\] 2](https://clinicaltrials.gov/search?term=AREA%5BPhase:size%5D%202) query finds studies with 2 phases. (GET /stats/field/sizes). Docs: https://clinicaltrials.gov/data-api/api |
| Get Study | `getStudy` | Single Study. Returns data of a single study. (GET /studies/{nctId}). Docs: https://clinicaltrials.gov/data-api/api |
| Get Study Data Model | `getStudyDataModel` | Data Model Fields. Returns study data model fields. (GET /studies/metadata). Docs: https://clinicaltrials.gov/data-api/api |
| Get Study Size Statistics | `getStudySizeStats` | Study Sizes. Statistics of study JSON sizes. (GET /stats/size). Docs: https://clinicaltrials.gov/data-api/api |
| List Enumeration Types | `listEnums` | Enums. Returns enumeration types and their values. Every item of the returning array represents enum type and contains the following properties: * `type` - enum type name * `pieces` - array of names of all data pieces having the enum type * `values` - all available values of the enum; every item contains the following properties: * `value` - data value * `legacyValue` - data value in legacy API * `exceptions` - map from data piece name to legacy value when different from `legacyValue` (some data pieces had special enum values in legacy API) (GET /studies/enums). Docs: https://clinicaltrials.gov/data-api/api |
| List Search Areas | `listSearchAreas` | Search Areas. Search Docs and their Search Areas. (GET /studies/search-areas). Docs: https://clinicaltrials.gov/data-api/api |
| Search Studies | `listStudies` | Studies. Returns data of studies matching query and filter parameters. The studies are returned page by page. If response contains `nextPageToken`, use its value in `pageToken` to get next page. The last page will not contain `nextPageToken`. A page may have empty `studies` array. Request for each subsequent page **must** have the same parameters as for the first page, except `countTotal`, `pageSize`, and `pageToken` parameters. If neither queries nor filters are set, all studies will be returned. If any query parameter contains only NCT IDs (comma- and/or space-separated), filters are ignored. `query.*` parameters are in [Essie expression syntax](/find-studies/constructing-complex-search-queries). Those parameters affect ranking of studies, if sorted by relevance. See `sort` parameter for details. `filter.*` and `postFilter.*` parameters have same effect as there is no aggregation calculation. Both are available just to simplify applying parameters from search request. Both do not ... |
