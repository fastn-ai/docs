---
description: "ClinicalTrials.gov is the US registry of clinical studies worldwide. Search studies, get a study by its ID and read field statistics."
hidden: true
---

# ClinicalTrials.gov

<img src="../../.gitbook/assets/connectors/lg/clinical-trials-gov.png" alt="ClinicalTrials.gov logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [clinicaltrials.gov](https://clinicaltrials.gov) |
| **Authentication** | No sign-in needed |
| **Slug** | `clinicalTrialsGov` |

## Setup

ClinicalTrials.gov needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add ClinicalTrials.gov from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.clinicalTrialsGov.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Version</td><td><code>getVersion</code></td><td>Version. API and data versions. API version follows [Semantic Versioning 2.0.0 Schema](https://semver.org/spec/v2.0.0.html). Data version is UTC timestamp in `yyyy-MM-dd'T'HH:mm:ss` format. Docs: https://clinicaltrials.gov/data-api/api</td></tr><tr><td>Get Field Value Statistics</td><td><code>getFieldValueStats</code></td><td>Field Values. Value statistics of the study leaf fields. Docs: https://clinicaltrials.gov/data-api/api</td></tr><tr><td>Get List Field Size Statistics</td><td><code>getListFieldSizeStats</code></td><td>List Field Sizes. Sizes of list/array fields. To search studies by a list field size, use `AREA[FieldName:size]` search operator. For example, [AREA\[Phase:size\] 2](https://clinicaltrials.gov/search?term=AREA%5BPhase:size%5D%202) query finds studies with 2 phases. Docs: https://clinicaltrials.gov/data-api/api</td></tr><tr><td>Get Study</td><td><code>getStudy</code></td><td>Single Study. Returns data of a single study. Docs: https://clinicaltrials.gov/data-api/api</td></tr><tr><td>Get Study Data Model</td><td><code>getStudyDataModel</code></td><td>Data Model Fields. Returns study data model fields. Docs: https://clinicaltrials.gov/data-api/api</td></tr><tr><td>Get Study Size Statistics</td><td><code>getStudySizeStats</code></td><td>Study Sizes. Statistics of study JSON sizes. Docs: https://clinicaltrials.gov/data-api/api</td></tr><tr><td>List Enumeration Types</td><td><code>listEnums</code></td><td>Enums. Returns enumeration types and their values. Every item of the returning array represents enum type and contains the following properties: * `type` - enum type name * `pieces` - array of names of all data pieces having the enum type * `values` - all available values of the enum; every item contains the following properties: * `value` - data value * `legacyValue` - data value in legacy API * `exceptions` - map from data piece name to legacy value when different from `legacyValue` (some data pieces had special enum values in legacy API) Docs: https://clinicaltrials.gov/data-api/api</td></tr><tr><td>List Search Areas</td><td><code>listSearchAreas</code></td><td>Search Areas. Search Docs and their Search Areas. Docs: https://clinicaltrials.gov/data-api/api</td></tr><tr><td>Search Studies</td><td><code>listStudies</code></td><td>Studies. Returns data of studies matching query and filter parameters. The studies are returned page by page. If response contains `nextPageToken`, use its value in `pageToken` to get next page. The last page will not contain `nextPageToken`. A page may have empty `studies` array. Request for each subsequent page **must** have the same parameters as for the first page, except `countTotal`, `pageSize`, and `pageToken` parameters. If neither queries nor filters are set, all studies will be returned. If any query parameter contains only NCT IDs (comma- and/or space-separated), filters are ignored. `query.*` parameters are in [Essie expression syntax](/find-studies/constructing-complex-search-queries). Those parameters affect ranking of studies, if sorted by relevance. See `sort` parameter for details. `filter.*` and `postFilter.*` parameters have same effect as there is no aggregation calculation. Both are available just to simplify applying parameters from search request. Both do not...</td></tr></tbody></table>

## Events

ClinicalTrials.gov has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
