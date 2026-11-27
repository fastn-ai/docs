---
description: "RubyGems.org hosts Ruby gems. Get gem and version details, download counts, owners, contents and attestations."
hidden: true
---

# RubyGems.org

<img src="../../.gitbook/assets/connectors/lg/rubygems-org.png" alt="RubyGems.org logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [rubygems.org](https://rubygems.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `rubygemsOrg` |

## Setup

RubyGems.org needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect RubyGems.org from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **RubyGems.org**.
2. Select **Connect** on the RubyGems.org card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. RubyGems.org needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use RubyGems.org's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Autocomplete Gem Names</td><td><code>autocompleteGems</code></td><td>Get gem names that match a partial query, for search boxes Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>Get Gem</td><td><code>getGem</code></td><td>Get a gem's latest version details: downloads, authors, info, licenses, metadata, URIs, SHA and runtime/development dependencies Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>Get Gem Version</td><td><code>getGemVersion</code></td><td>Get full details of one gem version, optionally for a specific platform or content-addressable ruby_abi Docs: https://guides.rubygems.org/rubygems-org-api-v2/</td></tr><tr><td>Get Gem Version Contents</td><td><code>getGemVersionContents</code></td><td>Get the SHA-256 checksum of every file packaged in a gem version Older versions answer 404 'Content is unavailable for this version.' Docs: https://guides.rubygems.org/rubygems-org-api-v2/</td></tr><tr><td>Get Latest Gem Version</td><td><code>getLatestGemVersion</code></td><td>Get the latest version number of a gem Unknown gems return version 'unknown'. Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>Get Total Downloads</td><td><code>getTotalDownloads</code></td><td>Get the total number of downloads across RubyGems.org Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>Get User Profile</td><td><code>getProfile</code></td><td>Get a user's public profile (id, handle, public e-mail) by handle or id Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>Get Version Downloads</td><td><code>getVersionDownloads</code></td><td>Get total downloads of a gem and of one of its versions Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>List Gem Attestations</td><td><code>listGemAttestations</code></td><td>Get the sigstore attestation bundles published with a gem version; empty when none Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>List Gem Owners</td><td><code>listGemOwners</code></td><td>List the owners and maintainers of a gem E-mail appears only when public. Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Gem Versions</td><td><code>listGemVersions</code></td><td>List every version of a gem with authors, build/created dates, downloads, platform, Ruby/RubyGems requirements, prerelease flag and SHA Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>List Most Downloaded Versions</td><td><code>listTopDownloads</code></td><td>List the 50 most downloaded gem versions, each as a [version record, download count] pair Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>List Newest Gems</td><td><code>listLatestGems</code></td><td>List the 50 gems most recently added to RubyGems.org for the first time Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>List Owner Gems</td><td><code>listOwnerGems</code></td><td>List all gems a user can push to, by handle or user id Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>List Recently Updated Gems</td><td><code>listJustUpdatedGems</code></td><td>List the 50 most recently updated gems Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>List Reverse Dependencies</td><td><code>listReverseDependencies</code></td><td>List gems whose latest version depends on a gem, optionally only runtime or development dependants Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>List Versions In Timeframe</td><td><code>listTimeframeVersions</code></td><td>List gem versions created between two times (max 7-day span), 30 per page Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr><tr><td>Search Gems</td><td><code>searchGems</code></td><td>Search active gems like the site search; 30 results per page Docs: https://guides.rubygems.org/rubygems-org-api/</td></tr></tbody></table>

</details>

