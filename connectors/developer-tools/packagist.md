---
description: "Packagist is the main PHP package repository used by Composer."
hidden: true
---

# Packagist

<img src="../../.gitbook/assets/connectors/lg/packagist.png" alt="Packagist logo">

Packagist is the main PHP package repository used by Composer. Its free public API lists and searches packages, gets package details, Composer v2 metadata, download stats, dependents, popular packages, the metadata change feed, overall statistics and security advisories. No API key needed for these read endpoints.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [packagist.org](https://packagist.org) |
| **Authentication** | No authentication |
| **Slug** | `packagist` |

## Use it

Add Packagist from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.packagist.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Metadata Changes | `getMetadataChanges` | Poll the feed of package metadata changes since a timestamp (10000 x unix time). Without since, returns the current timestamp to start from; changes are kept 24 hours (GET /metadata/changes.json). Docs: https://packagist.org/apidoc |
| Get Package | `getPackage` | Get full package data: description, maintainers, all versions with their composer.json data, type, repository, download totals, favers, dependents and GitHub stats (GET /packages/{vendor}/{package}.json). Cached up to 12 hours. Docs: https://packagist.org/apidoc |
| Get Package Dev Metadata (Composer v2) | `getPackageDevMetadata` | Get the Composer v2 metadata of a package's development branches (dev versions) from the static repository (GET https://repo.packagist.org/p2/{vendor}/{package}~dev.json). Docs: https://packagist.org/apidoc |
| Get Package Download Stats | `getPackageStats` | Get a package's total, monthly and daily downloads, its version list and the stats start date (GET /packages/{vendor}/{package}/stats.json). Docs: https://packagist.org/apidoc |
| Get Package Metadata (Composer v2) | `getPackageMetadata` | Get the Composer v2 metadata of a package's tagged releases from the static repository (GET https://repo.packagist.org/p2/{vendor}/{package}.json). Data is minified: each version only lists keys that changed from the previous one. Docs: https://packagist.org/apidoc |
| Get Statistics | `getStatistics` | Get Packagist overall statistics (total downloads) (GET /statistics.json). Docs: https://packagist.org/apidoc |
| List Package Dependents | `listPackageDependents` | List packages that require a package (GET /packages/{vendor}/{package}/dependents.json). order_by=none walks the full list via 'next'; order_by=downloads gives the most installed first (top 500). Docs: https://packagist.org/apidoc |
| List Package Names | `listPackageNames` | List all package names on Packagist, optionally only one vendor's or one package type's. With a field set, returns an object keyed by package name with that field (GET /packages/list.json). Docs: https://packagist.org/apidoc |
| List Popular Packages | `listPopularPackages` | List the most popular packages, ranked by downloads over the last week (GET /explore/popular.json). Docs: https://packagist.org/apidoc |
| List Security Advisories | `listSecurityAdvisories` | List security advisories for a package, or all advisories updated since a unix timestamp (GET /api/security-advisories/). Pass a package name or updatedSince. Docs: https://packagist.org/apidoc |
| Search Packages | `searchPackages` | Search packages by name/keyword, optionally narrowed by tag and package type, paginated (GET /search.json). Docs: https://packagist.org/apidoc |
