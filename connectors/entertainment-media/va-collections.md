---
description: "The V&A Collections API (v2) is the free public API of the Victoria and Albert Museum, London."
hidden: true
---

# V&A Collections

<img src="../../.gitbook/assets/connectors/lg/va-collections.png" alt="V&A Collections logo">

Search and browse more than a million collection objects and archive records by keyword, maker, place, material, technique, date and more, get full object records, group results into clusters, browse controlled terms and look up authorities. No API key needed.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [vam.ac.uk](https://vam.ac.uk) |
| **Authentication** | No authentication |
| **Slug** | `vaCollections` |

## Use it

Add V&A Collections from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.vaCollections.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Browse Controlled Term</td><td><code>browseControlledTerm</code></td><td>Controlled Term Browse. (GET /v2/objects/browse/{cluster_type}/{controlled_term}). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Browse Controlled Term (Search)</td><td><code>browseControlledTermSearch</code></td><td>Controlled Term Browse. (GET /v2/objects/browse/{cluster_type}/{controlled_term}/search). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Get Object</td><td><code>getObject</code></td><td>Collection Object. (GET /v2/object/O{object_num}). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Search Archives</td><td><code>searchArchives</code></td><td>Archive Search. fully featured ESQuery function to be called by specific API endpoint functions Returns: results, two items returned from ESQuery (GET /v2/archives/search). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Search Authorities (Search As You Type)</td><td><code>searchAuthorities</code></td><td>Authorities Sayt Search. (GET /v2/sayt/search). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Search Object Clusters</td><td><code>searchObjectClusters</code></td><td>Object Cluster Search. (GET /v2/objects/clusters/search). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Search Object Clusters by Type</td><td><code>searchObjectClustersByType</code></td><td>Object Cluster Search. (GET /v2/objects/clusters/{cluster_type}/search). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Search Objects</td><td><code>searchObjects</code></td><td>Object Full Search. (GET /v2/objects/search). Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr></tbody></table>
