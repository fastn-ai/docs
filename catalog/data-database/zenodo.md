---
description: "Zenodo is CERN's open research repository. Search and read records and their files, communities, funders, awards and licenses."
hidden: true
---

# Zenodo

<img src="../../.gitbook/assets/connectors/lg/zenodo.png" alt="Zenodo logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [zenodo.org](https://zenodo.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `zenodo` |

## Setup

Zenodo needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Zenodo from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Zenodo**.
2. Select **Connect** on the Zenodo card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Zenodo needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Zenodo's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Affiliation</td><td><code>getAffiliation</code></td><td>Get one affiliation by ROR id Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Get Award</td><td><code>getAward</code></td><td>Get one award by id, formatted {funderId}::{awardNumber} Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Get Community</td><td><code>getCommunity</code></td><td>Get one community by slug or id with its title, description, curation policy and links Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Get Funder</td><td><code>getFunder</code></td><td>Get one funder by id (ROR id without prefix) Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Get Latest Record Version</td><td><code>getLatestRecordVersion</code></td><td>Get the latest version of a record from any version or concept id - the API redirects to the latest record). Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Get License</td><td><code>getLicense</code></td><td>Get one license by its id, e.g. cc-by-4.0 or mit Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Get Record</td><td><code>getRecord</code></td><td>Get one published record with full metadata, files summary, DOI, stats and links Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Get Record File Metadata</td><td><code>getRecordFile</code></td><td>Get metadata of one file of a record: size, checksum, mimetype, links to content Download the bytes from links.content. Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Get Vocabulary Term</td><td><code>getVocabularyTerm</code></td><td>Get one term of a controlled vocabulary Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>List Community Records</td><td><code>listCommunityRecords</code></td><td>Search the records included in a community Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr></tbody></table>

<details>

<summary>View 11 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Record Communities</td><td><code>listRecordCommunities</code></td><td>List the communities a record belongs to Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>List Record Files</td><td><code>listRecordFiles</code></td><td>List the files of a record with key, size, checksum, mimetype and download links Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>List Record Versions</td><td><code>listRecordVersions</code></td><td>List all versions of a record, newest first Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Search Affiliations</td><td><code>searchAffiliations</code></td><td>Search organizations used as creator affiliations (ROR-based) Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Search Awards</td><td><code>searchAwards</code></td><td>Search grants/awards by title, number or acronym Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Search Communities</td><td><code>searchCommunities</code></td><td>Search Zenodo communities (curated collections) Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Search Funders</td><td><code>searchFunders</code></td><td>Search research funders (from the ROR / Open Funder registry) Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Search Licenses</td><td><code>searchLicenses</code></td><td>Search the license vocabulary (SPDX ids and names) used in records Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Search Records</td><td><code>searchRecords</code></td><td>Search published Zenodo records (datasets, software, papers...) with free text and filters for community, resource type, access and all versions Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Search Subjects</td><td><code>searchSubjects</code></td><td>Search subject terms (e.g. FAST, Euroscivoc) used to classify records Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr><tr><td>Search Vocabulary</td><td><code>searchVocabulary</code></td><td>Search a controlled vocabulary such as resourcetypes, languages, creatorsroles, contributorsroles, relationtypes, datetypes, titletypes, descriptiontypes Docs: https://developers.zenodo.org/ (InvenioRDM REST API: https://inveniordm.docs.cern.ch/reference/rest_api_index/)</td></tr></tbody></table>

</details>

