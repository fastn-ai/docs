---
description: "Packagist is the main PHP package repository. Get package details, metadata, download stats, dependents and security advisories."
hidden: true
---

# Packagist

<img src="../../.gitbook/assets/connectors/lg/packagist.png" alt="Packagist logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [packagist.org](https://packagist.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `packagist` |

## Setup

Packagist needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Packagist from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Packagist**.
2. Select **Connect** on the Packagist card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Packagist needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Packagist's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Metadata Changes</td><td><code>getMetadataChanges</code></td><td>Poll the feed of package metadata changes since a timestamp (10000 x unix time). Without since, returns the current timestamp to start from; changes are kept 24 hours Docs: https://packagist.org/apidoc</td></tr><tr><td>Get Package</td><td><code>getPackage</code></td><td>Get full package data: description, maintainers, all versions with their composer.json data, type, repository, download totals, favers, dependents and GitHub stats Cached up to 12 hours. Docs: https://packagist.org/apidoc</td></tr><tr><td>Get Package Dev Metadata (Composer v2)</td><td><code>getPackageDevMetadata</code></td><td>Get the Composer v2 metadata of a package's development branches (dev versions) from the static repository (GET https://repo.packagist.org/p2/{vendor}/{package}~dev.json). Docs: https://packagist.org/apidoc</td></tr><tr><td>Get Package Download Stats</td><td><code>getPackageStats</code></td><td>Get a package's total, monthly and daily downloads, its version list and the stats start date Docs: https://packagist.org/apidoc</td></tr><tr><td>Get Package Metadata (Composer v2)</td><td><code>getPackageMetadata</code></td><td>Get the Composer v2 metadata of a package's tagged releases from the static repository (GET https://repo.packagist.org/p2/{vendor}/{package}.json). Data is minified: each version only lists keys that changed from the previous one. Docs: https://packagist.org/apidoc</td></tr><tr><td>Get Statistics</td><td><code>getStatistics</code></td><td>Get Packagist overall statistics (total downloads) Docs: https://packagist.org/apidoc</td></tr><tr><td>List Package Dependents</td><td><code>listPackageDependents</code></td><td>List packages that require a package order_by=none walks the full list via 'next'; order_by=downloads gives the most installed first (top 500). Docs: https://packagist.org/apidoc</td></tr><tr><td>List Package Names</td><td><code>listPackageNames</code></td><td>List all package names on Packagist, optionally only one vendor's or one package type's. With a field set, returns an object keyed by package name with that field Docs: https://packagist.org/apidoc</td></tr><tr><td>List Popular Packages</td><td><code>listPopularPackages</code></td><td>List the most popular packages, ranked by downloads over the last week Docs: https://packagist.org/apidoc</td></tr><tr><td>List Security Advisories</td><td><code>listSecurityAdvisories</code></td><td>List security advisories for a package, or all advisories updated since a unix timestamp Pass a package name or updatedSince. Docs: https://packagist.org/apidoc</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Packages</td><td><code>searchPackages</code></td><td>Search packages by name/keyword, optionally narrowed by tag and package type, paginated Docs: https://packagist.org/apidoc</td></tr></tbody></table>

</details>

