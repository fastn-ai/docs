---
description: "OSV (osv.dev, by Google) is a free, open database of vulnerabilities in open-source packages across PyPI, npm, Go, Maven, crates.io, Debian, Ubuntu and more."
hidden: true
---

# OSV

OSV (osv.dev, by Google) is a free, open database of vulnerabilities in open-source packages across PyPI, npm, Go, Maven, crates.io, Debian, Ubuntu and more. Query vulnerabilities by package version, purl or git commit (single or batch), fetch full vulnerability records, find C/C++ library versions from file hashes, and map Ubuntu binary packages to source packages. No API key needed.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [osv.dev](https://osv.dev) |
| **Authentication** | No authentication |
| **Actions** | 6 |
| **Events** | 0 |
| **Slug** | `osvDev` |

## Use it

Add OSV from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.osvDev.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Determine C/C++ Library Version | `determineVersion` | Find the likely repository and version of a C/C++ library from the MD5 hashes of its source files (POST /v1experimental/determineversion). Experimental; covers OSS-Fuzz projects. Docs: https://google.github.io/osv.dev/post-v1-determineversion/ |
| Get Vulnerability | `getVulnerability` | Get the full OSV record for one vulnerability id (GET /v1/vulns/{id}). Ids are case-sensitive. Docs: https://google.github.io/osv.dev/get-v1-vulns/ |
| List Import Findings | `listImportFindings` | List records from one OSV data source that failed import-time quality checks (GET /v1experimental/importfindings/{source}). Experimental. An empty object means no failing records. Docs: https://google.github.io/osv.dev/get-v1-importfindings/ |
| Map Ubuntu Binary to Source Packages | `mapUbuntuBinaryToSource` | Map Ubuntu binary package names (up to 1000) to the source package names OSV indexes advisories by (POST /v1experimental/ubuntu/binary-to-source). Experimental. Docs: https://google.github.io/osv.dev/post-v1-ubuntu-binary-to-source/ |
| Query Vulnerabilities | `queryVulnerabilities` | List the known vulnerabilities affecting a package version (name + ecosystem, or purl) or a git commit (POST /v1/query). Use either version or a versioned purl, not both. Large results are paged with next_page_token. Docs: https://google.github.io/osv.dev/post-v1-query/ |
| Query Vulnerabilities in Batch | `queryVulnerabilitiesBatch` | Run many package/commit queries in one call; results come back in the same order with only vulnerability ids and modified times (POST /v1/querybatch). Docs: https://google.github.io/osv.dev/post-v1-querybatch/ |
