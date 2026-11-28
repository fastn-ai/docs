---
description: "The V&A Collections service shares the Victoria and Albert Museum's collection. Search and look up objects, archives and authorities."
hidden: true
---

# V&A Collections

<img src="../../.gitbook/assets/connectors/lg/va-collections.png" alt="V&A Collections logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [vam.ac.uk](https://vam.ac.uk) |
| **Authentication** | No sign-in needed |
| **Slug** | `vaCollections` |

## Setup

V&A Collections needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect V&A Collections from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **V&A Collections**.
2. Select **Connect** on the V&A Collections card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. V&A Collections needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use V&A Collections's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Browse Controlled Term</td><td><code>browseControlledTerm</code></td><td>Controlled Term Browse. Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Browse Controlled Term (Search)</td><td><code>browseControlledTermSearch</code></td><td>Controlled Term Browse. Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Get Object</td><td><code>getObject</code></td><td>Collection Object. Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Search Archives</td><td><code>searchArchives</code></td><td>Archive Search. fully featured ESQuery function to be called by specific API endpoint functions Returns: results, two items returned from ESQuery Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Search Authorities (Search As You Type)</td><td><code>searchAuthorities</code></td><td>Authorities Sayt Search. Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Search Object Clusters</td><td><code>searchObjectClusters</code></td><td>Object Cluster Search. Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Search Object Clusters by Type</td><td><code>searchObjectClustersByType</code></td><td>Object Cluster Search. Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr><tr><td>Search Objects</td><td><code>searchObjects</code></td><td>Object Full Search. Docs: https://developers.vam.ac.uk/guide/v2/welcome.html</td></tr></tbody></table>

