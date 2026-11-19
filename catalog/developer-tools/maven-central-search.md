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

## Use it

Add Maven Central Search from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mavenCentralSearch.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Artifact Versions</td><td><code>listArtifactVersions</code></td><td>List all released versions of one artifact, newest first Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr><tr><td>Search Artifacts</td><td><code>searchArtifacts</code></td><td>Search Maven Central like the basic search box, or with Solr field syntax (g:, a:, v:, p:, l:, c:, fc:, 1:, tags:, AND). Returns artifacts with their latest version Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr><tr><td>Search by Class Name</td><td><code>searchByClassName</code></td><td>Find artifact versions that contain a class by simple name Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr><tr><td>Search by Coordinates</td><td><code>searchByCoordinates</code></td><td>Find artifact versions matching full coordinates: groupId, artifactId, version and classifier (the vendor times out when packaging p: is added to this query; use Search Artifacts for other fields) Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr><tr><td>Search by Fully Qualified Class Name</td><td><code>searchByFullyQualifiedClassName</code></td><td>Find artifact versions that contain a fully qualified class Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr><tr><td>Search by SHA-1</td><td><code>searchBySha1</code></td><td>Find the artifact file with a given SHA-1 checksum Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr><tr><td>Search by Tag</td><td><code>searchByTag</code></td><td>Find artifacts with a tag, e.g. sbtplugin or scalaVersion-2.9 Docs: https://central.sonatype.org/search/rest-api-guide/</td></tr></tbody></table>

## Events

Maven Central Search has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
