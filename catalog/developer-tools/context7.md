---
description: "Context7 serves up-to-date library documentation to AI coding agents. Add repositories, websites and specs, and fetch documentation context."
hidden: true
---

# Context7

<img src="../../.gitbook/assets/connectors/lg/context7.png" alt="Context7 logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [context7.com](https://context7.com) |
| **Authentication** | Access token |
| **Slug** | `context7` |

## Setup

Your customers enter their access token for Context7 when they connect. Nothing else needs setting up.

## Use it

Add Context7 from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.context7.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Bitbucket Repository</td><td><code>addBitbucketRepository</code></td><td>Submits a Bitbucket repository to Context7 for documentation indexing. Supports private repositories with an access token, optional version-page filtering, and source-code documentation generation. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API.</td></tr><tr><td>Add Confluence Space</td><td><code>addConfluenceSpace</code></td><td>Indexes a Confluence Cloud space (or selected pages within it) as a private Context7 library. Requires the Confluence cloud ID, site URL, space key and space name plus a library title and description. Optionally limits indexing to specific page IDs and associates the library with a team project. Adding a library is permanent: there is no delete endpoint in the Context7 API.</td></tr><tr><td>Add Git Repository</td><td><code>addGitRepository</code></td><td>Submits a repository hosted on any other Git provider (for example Codeberg or a self-hosted Git server) to Context7 for documentation indexing. Supports private repositories with an access token, optional version-page filtering, and source-code documentation generation. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API.</td></tr><tr><td>Add GitHub Repository</td><td><code>addGitHubRepository</code></td><td>Submits a GitHub repository to Context7 for documentation indexing. Supports private repositories with a personal access token (or the token from your Context7 GitHub OAuth connection), optional version-page filtering, and source-code documentation generation. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API.</td></tr><tr><td>Add GitLab Repository</td><td><code>addGitLabRepository</code></td><td>Submits a GitLab repository to Context7 for documentation indexing. Supports private repositories with a personal access token, optional version-page filtering, and source-code documentation generation. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API.</td></tr><tr><td>Add llms.txt File</td><td><code>addLlmsTxtFile</code></td><td>Submits an llms.txt, llms-full.txt or llms-small.txt file by URL to Context7 for indexing as a library. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API.</td></tr><tr><td>Add Notion Pages</td><td><code>addNotionPages</code></td><td>Indexes selected Notion pages as a private Context7 library. Requires the Notion workspace ID and name, the page IDs to index, and a library title and description; optionally associates the library with a team project. Adding a library is permanent: there is no delete endpoint in the Context7 API.</td></tr><tr><td>Add OpenAPI Specification</td><td><code>addOpenApiSpecification</code></td><td>Submits an OpenAPI specification (JSON or YAML) by URL to Context7 for indexing as a library. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API.</td></tr><tr><td>Add Website</td><td><code>addWebsite</code></td><td>Submits a documentation website to Context7 for crawling and indexing as a library. Optionally restricts the crawl to pages under a base URL. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API.</td></tr><tr><td>Get Documentation Context</td><td><code>getDocumentationContext</code></td><td>Fetches the most relevant documentation for a library, ranked against the user's question or task. With type 'json' the response contains structured code snippets and documentation snippets plus any team or library rules; with type 'txt' it is a plain-text block ready to paste into a prompt. Use Search Libraries first to find the Context7 library ID.</td></tr></tbody></table>

<details>

<summary>View 5 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Library Metrics</td><td><code>getLibraryMetrics</code></td><td>Returns usage metrics for a library you own: lifetime request totals by surface (web page, plain text, MCP, CLI), per-day request history, daily MCP client unique-user breakdown, and lifetime topic and country distributions. Only library owners can read metrics; other callers receive 403 forbidden.</td></tr><tr><td>Get Teamspace Policies</td><td><code>getTeamspacePolicies</code></td><td>Returns the complete access policy configuration of the API key's teamspace: which documentation source types are enabled, the library filter mode with its quality thresholds, blocked and excepted libraries, repository and website quality filters, the manually selected library list, and the number of libraries currently accessible.</td></tr><tr><td>Refresh Library</td><td><code>refreshLibrary</code></td><td>Triggers a re-index of an existing Context7 library so its documentation reflects the latest source. Optionally targets a specific branch, and accepts a Git access token for private repositories (otherwise the stored OAuth token is used).</td></tr><tr><td>Search Libraries</td><td><code>searchLibraries</code></td><td>Searches the Context7 library index by library name, ranking results by relevance to the user's question or task. Returns matching libraries with their Context7 library ID, processing state, snippet and token counts, trust and benchmark scores, and available version tags.</td></tr><tr><td>Update Teamspace Policies</td><td><code>updateTeamspacePolicies</code></td><td>Incrementally updates the teamspace's access policies. Only the fields you provide are changed. Enable or disable documentation source types, switch the library filter mode, set quality thresholds (verified only, minimum trust score, maximum age, minimum stars, allowed SPDX licenses, website backlink and traffic minimums), add or remove blocked and excepted libraries, or maintain the manually selected library list. At least one of sourceTypes or libraryFilters must be supplied. Returns the full updated policy.</td></tr></tbody></table>

</details>

## Events

Context7 has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
