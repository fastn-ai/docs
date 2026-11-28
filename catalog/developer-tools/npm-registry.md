---
description: "The npm Registry hosts JavaScript packages. Get package details, versions, tags, download counts and security advisories."
hidden: true
---

# npm Registry

<img src="../../.gitbook/assets/connectors/lg/npm-registry.png" alt="npm Registry logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [npmjs.com](https://npmjs.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `npmRegistry` |

## Setup

npm Registry needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect npm Registry from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **npm Registry**.
2. Select **Connect** on the npm Registry card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. npm Registry needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use npm Registry's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Bulk Security Advisories</td><td><code>getBulkAdvisories</code></td><td>Get known security advisories for a set of packages and versions in one call, the endpoint npm audit uses Returns advisories keyed by package name; empty object when none apply. Docs: https://docs.npmjs.com/cli/commands/npm-audit</td></tr><tr><td>Get Daily Package Downloads</td><td><code>getDailyPackageDownloads</code></td><td>Get downloads per day of a package, or of up to 128 unscoped packages (comma-separated), for a period Docs: https://github.com/npm/registry/blob/main/docs/download-counts.md</td></tr><tr><td>Get Daily Total Downloads</td><td><code>getDailyTotalDownloads</code></td><td>Get downloads per day of all npm packages for a period Docs: https://github.com/npm/registry/blob/main/docs/download-counts.md</td></tr><tr><td>Get Dist Tags</td><td><code>getDistTags</code></td><td>Get a package's distribution tags and the versions they point to Docs: https://docs.npmjs.com/cli/commands/npm-dist-tag</td></tr><tr><td>Get Package</td><td><code>getPackage</code></td><td>Get the full package metadata document (packument): all versions, dist-tags, publish times, maintainers and readme Popular packages return very large documents; prefer Get Package Version or Get Package (Abbreviated). Docs: https://github.com/npm/registry/blob/main/docs/REGISTRY-API.md</td></tr><tr><td>Get Package (Abbreviated)</td><td><code>getPackageAbbreviated</code></td><td>Get the abbreviated install metadata of a package: dist-tags, modified time and per-version dependencies, dist and engines only with Accept: application/vnd.npm.install-v1+json). Docs: https://github.com/npm/registry/blob/main/docs/responses/package-metadata.md</td></tr><tr><td>Get Package Downloads</td><td><code>getPackageDownloads</code></td><td>Get total downloads of a package, or of up to 128 unscoped packages (comma-separated), for a period Docs: https://github.com/npm/registry/blob/main/docs/download-counts.md</td></tr><tr><td>Get Package Version</td><td><code>getPackageVersion</code></td><td>Get the manifest of one version of a package, or of a dist-tag such as latest Docs: https://github.com/npm/registry/blob/main/docs/REGISTRY-API.md</td></tr><tr><td>Get Total Downloads</td><td><code>getTotalDownloads</code></td><td>Get total downloads of all npm packages for a period Docs: https://github.com/npm/registry/blob/main/docs/download-counts.md</td></tr><tr><td>Get Version Downloads Last Week</td><td><code>getVersionDownloads</code></td><td>Get downloads per version of a package for the previous 7 days Docs: https://github.com/npm/registry/blob/main/docs/download-counts.md</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Packages</td><td><code>searchPackages</code></td><td>Search packages by text with optional weighting of quality, popularity and maintenance Text supports qualifiers like author:, maintainer:, keywords:, scope:, not:unstable, is:insecure. Docs: https://github.com/npm/registry/blob/main/docs/REGISTRY-API.md</td></tr></tbody></table>

</details>

