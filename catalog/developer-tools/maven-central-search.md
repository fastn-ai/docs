---
description: "Maven Central is the main repository for Java libraries. Search artifacts by name, coordinates, class or checksum and list their versions."
hidden: true
---

# Maven Central Search

<img src="../../.gitbook/assets/connectors/lg/maven-central-search.png" alt="Maven Central Search logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [search.maven.org](https://search.maven.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `mavenCentralSearch` |

## Setup

Maven Central Search needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Maven Central Search from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Maven Central Search**.
2. Select **Connect** on the Maven Central Search card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Maven Central Search needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Maven Central Search's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Artifact Versions</td><td><code>listArtifactVersions</code></td><td>List all released versions of one artifact, newest first Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr><tr><td>Search Artifacts</td><td><code>searchArtifacts</code></td><td>Search Maven Central like the basic search box, or with Solr field syntax (g:, a:, v:, p:, l:, c:, fc:, 1:, tags:, AND). Returns artifacts with their latest version Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr><tr><td>Search by Class Name</td><td><code>searchByClassName</code></td><td>Find artifact versions that contain a class by simple name Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr><tr><td>Search by Coordinates</td><td><code>searchByCoordinates</code></td><td>Find artifact versions matching full coordinates: groupId, artifactId, version and classifier (the vendor times out when packaging p: is added to this query; use Search Artifacts for other fields) Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr><tr><td>Search by Fully Qualified Class Name</td><td><code>searchByFullyQualifiedClassName</code></td><td>Find artifact versions that contain a fully qualified class Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr><tr><td>Search by SHA-1</td><td><code>searchBySha1</code></td><td>Find the artifact file with a given SHA-1 checksum Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr><tr><td>Search by Tag</td><td><code>searchByTag</code></td><td>Find artifacts with a tag, e.g. sbtplugin or scalaVersion-2.9 Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr></tbody></table>

