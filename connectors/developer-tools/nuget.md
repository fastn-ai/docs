---
description: "NuGet is the package manager for .NET."
hidden: true
---

# NuGet

<img src="../../.gitbook/assets/connectors/lg/nuget.png" alt="NuGet logo">

NuGet is the package manager for .NET. The free public NuGet V3 API on nuget.org searches and autocompletes packages, gets registration metadata, version lists, .nuspec manifests and readmes, reads the catalog of package changes and the vulnerability database, and lists the repository signing certificates. No API key needed for these read endpoints.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [nuget.org](https://nuget.org) |
| **Authentication** | No authentication |
| **Slug** | `nuget` |

## Use it

Add NuGet from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nuget.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Package IDs | `autocompletePackageIds` | Get package IDs that start with or contain a partial ID (GET azuresearch autocomplete?q=). Docs: https://learn.microsoft.com/en-us/nuget/api/search-autocomplete-service-resource |
| Get Catalog Index | `getCatalogIndex` | Get the NuGet catalog index: the list of catalog pages with commit ids, timestamps and item counts (GET /v3/catalog0/index.json). Large response (about 4.5 MB). Docs: https://learn.microsoft.com/en-us/nuget/api/catalog-resource |
| Get Catalog Leaf | `getCatalogLeaf` | Get one catalog leaf: the full metadata snapshot of a package version at one commit (GET /v3/catalog0/data/{timestamp}/{id}.{version}.json). Take the path from a catalog page item @id. Docs: https://learn.microsoft.com/en-us/nuget/api/catalog-resource |
| Get Catalog Page | `getCatalogPage` | Get one catalog page: the package versions added, updated or deleted in its commits (GET /v3/catalog0/page{N}.json). Docs: https://learn.microsoft.com/en-us/nuget/api/catalog-resource |
| Get Package Manifest (.nuspec) | `getPackageManifest` | Download the .nuspec manifest XML of one package version (GET /v3-flatcontainer/{id}/{version}/{id}.nuspec). Docs: https://learn.microsoft.com/en-us/nuget/api/package-base-address-resource |
| Get Package Readme | `getPackageReadme` | Download the embedded README (Markdown) of one package version, when the package has one (GET /v3-flatcontainer/{id}/{version}/readme). Docs: https://learn.microsoft.com/en-us/nuget/api/readme-template-resource |
| Get Package Registration Index | `getRegistrationIndex` | Get a package's registration index: every version with catalog metadata (authors, description, dependencies, deprecation, vulnerabilities, listed, published). Large packages return page links instead of inline items (GET /v3/registration5-gz-semver2/{id}/index.json). Docs: https://learn.microsoft.com/en-us/nuget/api/registration-base-url-resource |
| Get Package Registration Leaf | `getRegistrationLeaf` | Get the registration leaf of one package version: catalog entry URL, listed flag, publish date and package content URL (GET /v3/registration5-gz-semver2/{id}/{version}.json). Docs: https://learn.microsoft.com/en-us/nuget/api/registration-base-url-resource |
| Get Package Registration Page | `getRegistrationPage` | Get one external registration page of a package with many versions, using the lower and upper versions from the index (GET /v3/registration5-gz-semver2/{id}/page/{lower}/{upper}.json). Docs: https://learn.microsoft.com/en-us/nuget/api/registration-base-url-resource |
| Get Repository Signatures | `getRepositorySignatures` | Get the certificates NuGet.org uses to repository-sign packages, and whether all packages are signed (GET /v3-index/repository-signatures/5.0.0/index.json). Docs: https://learn.microsoft.com/en-us/nuget/api/repository-signatures-resource |

<details>

<summary>See 6 more actions</summary>

* **Get Service Index** `getServiceIndex`: Get the NuGet V3 service index: every resource type (search, autocomplete, registration, package content, catalog, vulnerabilities, ...) with its URL (GET /v3/index.json). Docs: https://learn.microsoft.com/en-us/nuget/api/service-index
* **Get Vulnerability Index** `getVulnerabilityIndex`: Get the vulnerability info index: links to the base and update vulnerability files with their update times (GET /v3/vulnerabilities/index.json). Docs: https://learn.microsoft.com/en-us/nuget/api/vulnerability-info
* **Get Vulnerability Page** `getVulnerabilityPage`: Get one vulnerability file (base or update): a map of package ID -&gt; known vulnerabilities with severity, advisory URL and affected versions (GET /v3-vulnerabilities/...). Take the path from the vulnerability index @id. Docs: https://learn.microsoft.com/en-us/nuget/api/vulnerability-info
* **List Package Versions** `listPackageVersions`: List all versions (listed and unlisted) of a package from the package content resource (GET /v3-flatcontainer/{id}/index.json). Docs: https://learn.microsoft.com/en-us/nuget/api/package-base-address-resource
* **List Package Versions (Autocomplete)** `autocompletePackageVersions`: List the listed versions of one package ID via the autocomplete service (GET azuresearch autocomplete?id=). Docs: https://learn.microsoft.com/en-us/nuget/api/search-autocomplete-service-resource
* **Search Packages** `searchPackages`: Search NuGet.org packages by keywords or field filters (id:, packageid:, version:, title:, tags:, author:, description:, summary:, owner:), with paging, prerelease and package-type filters (GET azuresearch query). Docs: https://learn.microsoft.com/en-us/nuget/api/search-query-service-resource

</details>
