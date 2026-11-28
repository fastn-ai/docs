---
description: "OSV is an open database of vulnerabilities in open-source packages. Query known vulnerabilities for packages, one at a time or in batches."
hidden: true
---

# OSV

<img src="../../.gitbook/assets/connectors/lg/osv-dev.png" alt="OSV logo">

| | |
| --- | --- |
| **Category** | [Security](README.md) |
| **Website** | [osv.dev](https://osv.dev) |
| **Authentication** | No sign-in needed |
| **Slug** | `osvDev` |

## Setup

OSV needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect OSV from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **OSV**.
2. Select **Connect** on the OSV card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. OSV needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use OSV's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Determine C/C++ Library Version</td><td><code>determineVersion</code></td><td>Find the likely repository and version of a C/C++ library from the MD5 hashes of its source files Experimental; covers OSS-Fuzz projects. Docs: https://google.github.io/osv.dev/post-v1-determineversion/</td></tr><tr><td>Get Vulnerability</td><td><code>getVulnerability</code></td><td>Get the full OSV record for one vulnerability id Ids are case-sensitive. Docs: https://google.github.io/osv.dev/get-v1-vulns/</td></tr><tr><td>List Import Findings</td><td><code>listImportFindings</code></td><td>List records from one OSV data source that failed import-time quality checks Experimental. An empty object means no failing records. Docs: https://google.github.io/osv.dev/get-v1-importfindings/</td></tr><tr><td>Map Ubuntu Binary to Source Packages</td><td><code>mapUbuntuBinaryToSource</code></td><td>Map Ubuntu binary package names (up to 1000) to the source package names OSV indexes advisories by Experimental. Docs: https://google.github.io/osv.dev/post-v1-ubuntu-binary-to-source/</td></tr><tr><td>Query Vulnerabilities</td><td><code>queryVulnerabilities</code></td><td>List the known vulnerabilities affecting a package version (name + ecosystem, or purl) or a git commit Use either version or a versioned purl, not both. Large results are paged with next_page_token. Docs: https://google.github.io/osv.dev/post-v1-query/</td></tr><tr><td>Query Vulnerabilities in Batch</td><td><code>queryVulnerabilitiesBatch</code></td><td>Run many package/commit queries in one call; results come back in the same order with only vulnerability ids and modified times Docs: https://google.github.io/osv.dev/post-v1-querybatch/</td></tr></tbody></table>

