---
description: "Zenodo is CERN's open research repository for datasets, software, papers and more, each with a DOI."
hidden: true
---

# Zenodo

<img src="../../.gitbook/assets/connectors/lg/zenodo.png" alt="Zenodo logo">

Zenodo is CERN's open research repository for datasets, software, papers and more, each with a DOI. Search and read published records, their versions, files and communities, and look up communities, licenses, funders, awards, affiliations, subjects and controlled vocabularies. Read-only public access, no API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [zenodo.org](https://zenodo.org) |
| **Authentication** | No authentication |
| **Slug** | `zenodo` |

## Use it

Add Zenodo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zenodo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Affiliation | `getAffiliation` | Get one affiliation by ROR id (GET /api/affiliations/{id}). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Get Award | `getAward` | Get one award by id, formatted {funderId}::{awardNumber} (GET /api/awards/{id}). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Get Community | `getCommunity` | Get one community by slug or id with its title, description, curation policy and links (GET /api/communities/{id}). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Get Funder | `getFunder` | Get one funder by id (ROR id without prefix) (GET /api/funders/{id}). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Get Latest Record Version | `getLatestRecordVersion` | Get the latest version of a record from any version or concept id (GET /api/records/{id}/versions/latest - the API redirects to the latest record). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Get License | `getLicense` | Get one license by its id, e.g. cc-by-4.0 or mit (GET /api/vocabularies/licenses/{id}). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Get Record | `getRecord` | Get one published record with full metadata, files summary, DOI, stats and links (GET /api/records/{id}). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Get Record File Metadata | `getRecordFile` | Get metadata of one file of a record: size, checksum, mimetype, links to content (GET /api/records/{id}/files/{key}). Download the bytes from links.content. Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Get Vocabulary Term | `getVocabularyTerm` | Get one term of a controlled vocabulary (GET /api/vocabularies/{type}/{id}). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| List Community Records | `listCommunityRecords` | Search the records included in a community (GET /api/communities/{id}/records). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| List Record Communities | `listRecordCommunities` | List the communities a record belongs to (GET /api/records/{id}/communities). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| List Record Files | `listRecordFiles` | List the files of a record with key, size, checksum, mimetype and download links (GET /api/records/{id}/files). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| List Record Versions | `listRecordVersions` | List all versions of a record, newest first (GET /api/records/{id}/versions). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Search Affiliations | `searchAffiliations` | Search organizations used as creator affiliations (ROR-based) (GET /api/affiliations). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Search Awards | `searchAwards` | Search grants/awards by title, number or acronym (GET /api/awards). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Search Communities | `searchCommunities` | Search Zenodo communities (curated collections) (GET /api/communities). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Search Funders | `searchFunders` | Search research funders (from the ROR / Open Funder registry) (GET /api/funders). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Search Licenses | `searchLicenses` | Search the license vocabulary (SPDX ids and names) used in records (GET /api/vocabularies/licenses). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Search Records | `searchRecords` | Search published Zenodo records (datasets, software, papers...) with free text and filters for community, resource type, access and all versions (GET /api/records). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Search Subjects | `searchSubjects` | Search subject terms (e.g. FAST, Euroscivoc) used to classify records (GET /api/subjects). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
| Search Vocabulary | `searchVocabulary` | Search a controlled vocabulary such as resourcetypes, languages, creatorsroles, contributorsroles, relationtypes, datetypes, titletypes, descriptiontypes (GET /api/vocabularies/{type}). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/) |
