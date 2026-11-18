---
description: "The npm Registry is the public JavaScript package registry."
hidden: true
---

# npm Registry

<img src="../../.gitbook/assets/connectors/lg/npm-registry.png" alt="npm Registry logo">

The npm Registry is the public JavaScript package registry. Search packages, get package metadata, versions and dist-tags, check versions against npm security advisories, and get download counts (totals, per day, per version, bulk). Public read APIs need no token.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [npmjs.com](https://npmjs.com) |
| **Authentication** | No authentication |
| **Slug** | `npmRegistry` |

## Use it

Add npm Registry from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.npmRegistry.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Bulk Security Advisories | `getBulkAdvisories` | Get known security advisories for a set of packages and versions in one call, the endpoint npm audit uses (POST /-/npm/v1/security/advisories/bulk). Returns advisories keyed by package name; empty object when none apply. Docs: https://docs.npmjs.com/cli/commands/npm-audit |
| Get Daily Package Downloads | `getDailyPackageDownloads` | Get downloads per day of a package, or of up to 128 unscoped packages (comma-separated), for a period (GET /downloads/range/{period}/{package}). Docs: https://github.com/npm/registry/blob/main/docs/download-counts.md |
| Get Daily Total Downloads | `getDailyTotalDownloads` | Get downloads per day of all npm packages for a period (GET /downloads/range/{period}). Docs: https://github.com/npm/registry/blob/main/docs/download-counts.md |
| Get Dist Tags | `getDistTags` | Get a package's distribution tags and the versions they point to (GET /-/package/{package}/dist-tags). Docs: https://docs.npmjs.com/cli/commands/npm-dist-tag |
| Get Package | `getPackage` | Get the full package metadata document (packument): all versions, dist-tags, publish times, maintainers and readme (GET /{package}). Popular packages return very large documents; prefer Get Package Version or Get Package (Abbreviated). Docs: https://github.com/npm/registry/blob/main/docs/REGISTRY-API.md |
| Get Package (Abbreviated) | `getPackageAbbreviated` | Get the abbreviated install metadata of a package: dist-tags, modified time and per-version dependencies, dist and engines only (GET /{package} with Accept: application/vnd.npm.install-v1+json). Docs: https://github.com/npm/registry/blob/main/docs/responses/package-metadata.md |
| Get Package Downloads | `getPackageDownloads` | Get total downloads of a package, or of up to 128 unscoped packages (comma-separated), for a period (GET /downloads/point/{period}/{package}). Docs: https://github.com/npm/registry/blob/main/docs/download-counts.md |
| Get Package Version | `getPackageVersion` | Get the manifest of one version of a package, or of a dist-tag such as latest (GET /{package}/{version}). Docs: https://github.com/npm/registry/blob/main/docs/REGISTRY-API.md |
| Get Total Downloads | `getTotalDownloads` | Get total downloads of all npm packages for a period (GET /downloads/point/{period}). Docs: https://github.com/npm/registry/blob/main/docs/download-counts.md |
| Get Version Downloads Last Week | `getVersionDownloads` | Get downloads per version of a package for the previous 7 days (GET /versions/{package}/last-week). Docs: https://github.com/npm/registry/blob/main/docs/download-counts.md |

<details>

<summary>See 1 more action</summary>

* **Search Packages** `searchPackages`: Search packages by text with optional weighting of quality, popularity and maintenance (GET /-/v1/search). Text supports qualifiers like author:, maintainer:, keywords:, scope:, not:unstable, is:insecure. Docs: https://github.com/npm/registry/blob/main/docs/REGISTRY-API.md

</details>
