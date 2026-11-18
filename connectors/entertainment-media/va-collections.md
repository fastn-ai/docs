---
description: "The V&A Collections API (v2) is the free public API of the Victoria and Albert Museum, London."
hidden: true
---

# V&A Collections

<img src="../../.gitbook/assets/connectors/va-collections.png" alt="V&A Collections logo" width="64">

The V&A Collections API (v2) is the free public API of the Victoria and Albert Museum, London. Search and browse more than a million collection objects and archive records by keyword, maker, place, material, technique, date and more, get full object records, group results into clusters, browse controlled terms and look up authorities. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [vam.ac.uk](https://vam.ac.uk) |
| **Authentication** | No authentication |
| **Slug** | `vaCollections` |

## Use it

Add V&A Collections from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.vaCollections.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Browse Controlled Term | `browseControlledTerm` | Controlled Term Browse. (GET /v2/objects/browse/{cluster_type}/{controlled_term}). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html |
| Browse Controlled Term (Search) | `browseControlledTermSearch` | Controlled Term Browse. (GET /v2/objects/browse/{cluster_type}/{controlled_term}/search). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html |
| Get Object | `getObject` | Collection Object. (GET /v2/object/O{object_num}). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html |
| Search Archives | `searchArchives` | Archive Search. fully featured ESQuery function to be called by specific API endpoint functions Returns: results, two items returned from ESQuery (GET /v2/archives/search). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html |
| Search Authorities (Search As You Type) | `searchAuthorities` | Authorities Sayt Search. (GET /v2/sayt/search). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html |
| Search Object Clusters | `searchObjectClusters` | Object Cluster Search. (GET /v2/objects/clusters/search). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html |
| Search Object Clusters by Type | `searchObjectClustersByType` | Object Cluster Search. (GET /v2/objects/clusters/{cluster_type}/search). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html |
| Search Objects | `searchObjects` | Object Full Search. (GET /v2/objects/search). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html |
