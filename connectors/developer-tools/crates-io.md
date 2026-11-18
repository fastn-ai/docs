---
description: "crates.io is the Rust community's package registry."
hidden: true
---

# crates.io

<img src="../../.gitbook/assets/connectors/crates-io.png" alt="crates.io logo" width="64">

crates.io is the Rust community's package registry. Search and browse crates, versions, dependencies, reverse dependencies, download stats, readmes, owners, categories, keywords, users, teams and registry summary through its public API, and use the token-based routes for email confirmation, owner invitations and trusted publishing. Read routes need no API key; crates.io asks for a descriptive User-Agent and at most 1 request per second.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [crates.io](https://crates.io) |
| **Authentication** | No authentication |
| **Slug** | `cratesIo` |

## Use it

Add crates.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cratesIo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Owner Invitation with Token | `acceptOwnerInvitationWithToken` | Accept a crate owner invitation with a token. (PUT /api/v1/me/crate_owner_invitations/accept/{token}). Docs: https://crates.io/api/openapi.json |
| Confirm User Email | `confirmUserEmail` | Marks the email belonging to the given token as verified. (PUT /api/v1/confirm/{email_token}). Docs: https://crates.io/api/openapi.json |
| Download Crate Version | `downloadCrateVersion` | Download a crate version. This returns a URL to the location where the crate is stored. (GET /api/v1/crates/{name}/{version}/download). Docs: https://crates.io/api/openapi.json |
| Exchange Trusted Publishing Token | `exchangeTrustedPublishingToken` | Exchange an OIDC token for a temporary access token. (POST /api/v1/trusted_publishing/tokens). Docs: https://crates.io/api/openapi.json |
| Get Category | `getCategory` | Get category metadata. (GET /api/v1/categories/{category}). Docs: https://crates.io/api/openapi.json |
| Get Crate | `getCrate` | Gets crate metadata. (GET /api/v1/crates/{name}). Docs: https://crates.io/api/openapi.json |
| Get Crate Downloads | `getCrateDownloads` | Get the download counts for a crate. This includes the per-day downloads for the last 90 days and for the latest 5 versions plus the sum of the rest. (GET /api/v1/crates/{name}/downloads). Docs: https://crates.io/api/openapi.json |
| Get Crate Version | `getCrateVersion` | Get crate version metadata. (GET /api/v1/crates/{name}/{version}). Docs: https://crates.io/api/openapi.json |
| Get Keyword | `getKeyword` | Get keyword metadata. (GET /api/v1/keywords/{keyword}). Docs: https://crates.io/api/openapi.json |
| Get Registry Summary | `getRegistrySummary` | Get front page data. This endpoint returns a summary of the most important data for the front page of crates.io. (GET /api/v1/summary). Docs: https://crates.io/api/openapi.json |

<details>

<summary>See 16 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Site Metadata | `getSiteMetadata` | Get crates.io metadata. Returns the current deployed commit SHA1 (or `unknown`), and whether the system is in read-only mode. (GET /api/v1/site_metadata). Docs: https://crates.io/api/openapi.json |
| Get Team | `getTeam` | Find team by login. (GET /api/v1/teams/{team}). Docs: https://crates.io/api/openapi.json |
| Get User | `getUser` | Find user by login. (GET /api/v1/users/{user}). Docs: https://crates.io/api/openapi.json |
| Get User Stats | `getUserStats` | Get user stats. This currently only returns the total number of downloads for crates owned by the user. (GET /api/v1/users/{id}/stats). Docs: https://crates.io/api/openapi.json |
| Get Version Downloads | `getVersionDownloads` | Get the download counts for a crate version. This includes the per-day downloads for the last 90 days. (GET /api/v1/crates/{name}/{version}/downloads). Docs: https://crates.io/api/openapi.json |
| Get Version Readme | `getVersionReadme` | Get the readme of a crate version. (GET /api/v1/crates/{name}/{version}/readme). Docs: https://crates.io/api/openapi.json |
| List Categories | `listCategories` | List all categories. (GET /api/v1/categories). Docs: https://crates.io/api/openapi.json |
| List Category Slugs | `listCategorySlugs` | List all available category slugs. (GET /api/v1/category_slugs). Docs: https://crates.io/api/openapi.json |
| List Crate Owners | `listCrateOwners` | Lists crate owners. (GET /api/v1/crates/{name}/owners). Docs: https://crates.io/api/openapi.json |
| List Crate Team Owners | `listCrateTeamOwners` | Lists team owners of a crate. (GET /api/v1/crates/{name}/owner_team). Docs: https://crates.io/api/openapi.json |
| List Crate User Owners | `listCrateUserOwners` | Lists user owners of a crate. (GET /api/v1/crates/{name}/owner_user). Docs: https://crates.io/api/openapi.json |
| List Crate Versions | `listCrateVersions` | List all versions of a crate. (GET /api/v1/crates/{name}/versions). Docs: https://crates.io/api/openapi.json |
| List Crates | `listCrates` | Returns a list of crates. Called in a variety of scenarios in the front end, including: - Alphabetical listing of crates - List of crates under a specific owner - Listing a user's followed crates When sorting by relevance, only the first 1000 results can be accessed, even though `meta.total` may report a higher number of matching crates. (GET /api/v1/crates). Docs: https://crates.io/api/openapi.json |
| List Keywords | `listKeywords` | List all keywords. (GET /api/v1/keywords). Docs: https://crates.io/api/openapi.json |
| List Reverse Dependencies | `listReverseDependencies` | Lists reverse dependencies of a crate. (GET /api/v1/crates/{name}/reverse_dependencies). Docs: https://crates.io/api/openapi.json |
| List Version Dependencies | `listVersionDependencies` | Get crate version dependencies. This information can also be obtained directly from the index. In addition to returning cached data from the index, this returns fields for `id`, `version_id`, and `downloads` (which appears to always be 0) (GET /api/v1/crates/{name}/{version}/dependencies). Docs: https://crates.io/api/openapi.json |

</details>
