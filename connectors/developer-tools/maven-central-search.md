---
description: "Maven Central Search is the free public search API of the Central Repository (run by Sonatype) for Java/JVM artifacts."
hidden: true
---

# Maven Central Search

<img src="../../.gitbook/assets/connectors/lg/maven-central-search.png" alt="Maven Central Search logo">

Maven Central Search is the free public search API of the Central Repository (run by Sonatype) for Java/JVM artifacts. Search artifacts, list all versions of an artifact, and search by coordinates, class name, fully qualified class name, SHA-1 checksum or tag. No API key needed.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [search.maven.org](https://search.maven.org) |
| **Authentication** | No authentication |
| **Slug** | `mavenCentralSearch` |

## Use it

Add Maven Central Search from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mavenCentralSearch.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| List Artifact Versions | `listArtifactVersions` | List all released versions of one artifact, newest first (GET /solrsearch/select?q=g:..+AND+a:..&core=gav). Docs: https://central.sonatype.org/search/rest-api-guide/ |
| Search Artifacts | `searchArtifacts` | Search Maven Central like the basic search box, or with Solr field syntax (g:, a:, v:, p:, l:, c:, fc:, 1:, tags:, AND). Returns artifacts with their latest version (GET /solrsearch/select). Docs: https://central.sonatype.org/search/rest-api-guide/ |
| Search by Class Name | `searchByClassName` | Find artifact versions that contain a class by simple name (GET /solrsearch/select?q=c:...). Docs: https://central.sonatype.org/search/rest-api-guide/ |
| Search by Coordinates | `searchByCoordinates` | Find artifact versions matching full coordinates: groupId, artifactId, version and classifier (the vendor times out when packaging p: is added to this query; use Search Artifacts for other fields) (GET /solrsearch/select). Docs: https://central.sonatype.org/search/rest-api-guide/ |
| Search by Fully Qualified Class Name | `searchByFullyQualifiedClassName` | Find artifact versions that contain a fully qualified class (GET /solrsearch/select?q=fc:...). Docs: https://central.sonatype.org/search/rest-api-guide/ |
| Search by SHA-1 | `searchBySha1` | Find the artifact file with a given SHA-1 checksum (GET /solrsearch/select?q=1:...). Docs: https://central.sonatype.org/search/rest-api-guide/ |
| Search by Tag | `searchByTag` | Find artifacts with a tag, e.g. sbtplugin or scalaVersion-2.9 (GET /solrsearch/select?q=tags:...). Docs: https://central.sonatype.org/search/rest-api-guide/ |
