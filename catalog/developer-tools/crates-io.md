---
description: "crates.io is the Rust package registry. Get crates, versions, download stats, categories and keywords."
hidden: true
---

# crates.io

<img src="../../.gitbook/assets/connectors/lg/crates-io.png" alt="crates.io logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [crates.io](https://crates.io) |
| **Authentication** | No sign-in needed |
| **Slug** | `cratesIo` |

## Setup

crates.io needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect crates.io from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **crates.io**.
2. Select **Connect** on the crates.io card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. crates.io needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use crates.io's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Accept Owner Invitation with Token</td><td><code>acceptOwnerInvitationWithToken</code></td><td>Accept a crate owner invitation with a token. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Confirm User Email</td><td><code>confirmUserEmail</code></td><td>Marks the email belonging to the given token as verified. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Download Crate Version</td><td><code>downloadCrateVersion</code></td><td>Download a crate version. This returns a URL to the location where the crate is stored. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Exchange Trusted Publishing Token</td><td><code>exchangeTrustedPublishingToken</code></td><td>Exchange an OIDC token for a temporary access token. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Get Category</td><td><code>getCategory</code></td><td>Get category metadata. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Get Crate</td><td><code>getCrate</code></td><td>Gets crate metadata. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Get Crate Downloads</td><td><code>getCrateDownloads</code></td><td>Get the download counts for a crate. This includes the per-day downloads for the last 90 days and for the latest 5 versions plus the sum of the rest. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Get Crate Version</td><td><code>getCrateVersion</code></td><td>Get crate version metadata. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Get Keyword</td><td><code>getKeyword</code></td><td>Get keyword metadata. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Get Registry Summary</td><td><code>getRegistrySummary</code></td><td>Get front page data. This endpoint returns a summary of the most important data for the front page of crates.io. Docs: https://crates.io/api/openapi.json</td></tr></tbody></table>

<details>

<summary>View 16 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Site Metadata</td><td><code>getSiteMetadata</code></td><td>Get crates.io metadata. Returns the current deployed commit SHA1 (or `unknown`), and whether the system is in read-only mode. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Get Team</td><td><code>getTeam</code></td><td>Find team by login. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Find user by login. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Get User Stats</td><td><code>getUserStats</code></td><td>Get user stats. This currently only returns the total number of downloads for crates owned by the user. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Get Version Downloads</td><td><code>getVersionDownloads</code></td><td>Get the download counts for a crate version. This includes the per-day downloads for the last 90 days. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>Get Version Readme</td><td><code>getVersionReadme</code></td><td>Get the readme of a crate version. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>List all categories. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>List Category Slugs</td><td><code>listCategorySlugs</code></td><td>List all available category slugs. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>List Crate Owners</td><td><code>listCrateOwners</code></td><td>Lists crate owners. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>List Crate Team Owners</td><td><code>listCrateTeamOwners</code></td><td>Lists team owners of a crate. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>List Crate User Owners</td><td><code>listCrateUserOwners</code></td><td>Lists user owners of a crate. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>List Crate Versions</td><td><code>listCrateVersions</code></td><td>List all versions of a crate. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>List Crates</td><td><code>listCrates</code></td><td>Returns a list of crates. Called in a variety of scenarios in the front end, including: - Alphabetical listing of crates - List of crates under a specific owner - Listing a user's followed crates When sorting by relevance, only the first 1000 results can be accessed, even though `meta.total` may report a higher number of matching crates. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>List Keywords</td><td><code>listKeywords</code></td><td>List all keywords. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>List Reverse Dependencies</td><td><code>listReverseDependencies</code></td><td>Lists reverse dependencies of a crate. Docs: https://crates.io/api/openapi.json</td></tr><tr><td>List Version Dependencies</td><td><code>listVersionDependencies</code></td><td>Get crate version dependencies. This information can also be obtained directly from the index. In addition to returning cached data from the index, this returns fields for `id`, `version_id`, and `downloads` (which appears to always be 0) Docs: https://crates.io/api/openapi.json</td></tr></tbody></table>

</details>

