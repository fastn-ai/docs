---
description: "RubyGems.org is the Ruby community's gem hosting service."
hidden: true
---

# RubyGems.org

<img src="../../.gitbook/assets/connectors/lg/rubygems-org.png" alt="RubyGems.org logo">

RubyGems.org is the Ruby community's gem hosting service. Its free public API gets gem and version details, searches and autocompletes gems, lists versions, reverse dependencies, file checksums, sigstore attestations, owners, user profiles, download counts and new or updated gems. No API key needed for these read endpoints.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [rubygems.org](https://rubygems.org) |
| **Authentication** | No authentication |
| **Slug** | `rubygemsOrg` |

## Use it

Add RubyGems.org from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rubygemsOrg.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Gem Names | `autocompleteGems` | Get gem names that match a partial query, for search boxes (GET /api/v1/search/autocomplete). Docs: https://guides.rubygems.org/rubygems-org-api/ |
| Get Gem | `getGem` | Get a gem's latest version details: downloads, authors, info, licenses, metadata, URIs, SHA and runtime/development dependencies (GET /api/v1/gems/{gem}.json). Docs: https://guides.rubygems.org/rubygems-org-api/ |
| Get Gem Version | `getGemVersion` | Get full details of one gem version, optionally for a specific platform or content-addressable ruby_abi (GET /api/v2/rubygems/{gem}/versions/{version}.json). Docs: https://guides.rubygems.org/rubygems-org-api-v2/ |
| Get Gem Version Contents | `getGemVersionContents` | Get the SHA-256 checksum of every file packaged in a gem version (GET /api/v2/rubygems/{gem}/versions/{version}/contents.json). Older versions answer 404 'Content is unavailable for this version.' Docs: https://guides.rubygems.org/rubygems-org-api-v2/ |
| Get Latest Gem Version | `getLatestGemVersion` | Get the latest version number of a gem (GET /api/v1/versions/{gem}/latest.json). Unknown gems return version 'unknown'. Docs: https://guides.rubygems.org/rubygems-org-api/ |
| Get Total Downloads | `getTotalDownloads` | Get the total number of downloads across RubyGems.org (GET /api/v1/downloads.json). Docs: https://guides.rubygems.org/rubygems-org-api/ |
| Get User Profile | `getProfile` | Get a user's public profile (id, handle, public e-mail) by handle or id (GET /api/v1/profiles/{handle}.json). Docs: https://guides.rubygems.org/rubygems-org-api/ |
| Get Version Downloads | `getVersionDownloads` | Get total downloads of a gem and of one of its versions (GET /api/v1/downloads/{gem}-{version}.json). Docs: https://guides.rubygems.org/rubygems-org-api/ |
| List Gem Attestations | `listGemAttestations` | Get the sigstore attestation bundles published with a gem version; empty when none (GET /api/v1/attestations/{gem}-{version}.json). Docs: https://guides.rubygems.org/rubygems-org-api/ |
| List Gem Owners | `listGemOwners` | List the owners and maintainers of a gem (GET /api/v1/gems/{gem}/owners.json). E-mail appears only when public. Docs: https://guides.rubygems.org/rubygems-org-api/ |

<details>

<summary>See 8 more actions</summary>

* **List Gem Versions** `listGemVersions`: List every version of a gem with authors, build/created dates, downloads, platform, Ruby/RubyGems requirements, prerelease flag and SHA (GET /api/v1/versions/{gem}.json). Docs: https://guides.rubygems.org/rubygems-org-api/
* **List Most Downloaded Versions** `listTopDownloads`: List the 50 most downloaded gem versions, each as a [version record, download count] pair (GET /api/v1/downloads/all.json). Docs: https://guides.rubygems.org/rubygems-org-api/
* **List Newest Gems** `listLatestGems`: List the 50 gems most recently added to RubyGems.org for the first time (GET /api/v1/activity/latest.json). Docs: https://guides.rubygems.org/rubygems-org-api/
* **List Owner Gems** `listOwnerGems`: List all gems a user can push to, by handle or user id (GET /api/v1/owners/{handle}/gems.json). Docs: https://guides.rubygems.org/rubygems-org-api/
* **List Recently Updated Gems** `listJustUpdatedGems`: List the 50 most recently updated gems (GET /api/v1/activity/just_updated.json). Docs: https://guides.rubygems.org/rubygems-org-api/
* **List Reverse Dependencies** `listReverseDependencies`: List gems whose latest version depends on a gem, optionally only runtime or development dependants (GET /api/v1/gems/{gem}/reverse_dependencies.json). Docs: https://guides.rubygems.org/rubygems-org-api/
* **List Versions In Timeframe** `listTimeframeVersions`: List gem versions created between two times (max 7-day span), 30 per page (GET /api/v1/timeframe_versions.json). Docs: https://guides.rubygems.org/rubygems-org-api/
* **Search Gems** `searchGems`: Search active gems like the site search; 30 results per page (GET /api/v1/search.json). Docs: https://guides.rubygems.org/rubygems-org-api/

</details>
