---
description: "Context7 delivers up-to-date, version-specific library documentation and code examples to AI coding agents."
hidden: true
---

# Context7

<img src="../../.gitbook/assets/connectors/lg/context7.png" alt="Context7 logo">

Context7 delivers up-to-date, version-specific library documentation and code examples to AI coding agents. This connector covers the complete Context7 Public REST API (https://context7.com/api): searching the library index, fetching ranked documentation context for a library and question, library usage metrics, refreshing an indexed library, reading and updating teamspace access policies, and adding new libraries from GitHub, GitLab, Bitbucket and other Git hosts, OpenAPI specifications, llms.txt files, websites, Confluence spaces and Notion pages.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [context7.com](https://context7.com) |
| **Authentication** | Bearer token |
| **Slug** | `context7` |

## Use it

Add Context7 from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.context7.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Bitbucket Repository | `addBitbucketRepository` | Submits a Bitbucket repository to Context7 for documentation indexing. Supports private repositories with an access token, optional version-page filtering, and source-code documentation generation. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API. Returns 400 repository-not-found when the repository does not exist or is inaccessible, and 409 when it was already added. |
| Add Confluence Space | `addConfluenceSpace` | Indexes a Confluence Cloud space (or selected pages within it) as a private Context7 library. Requires the Confluence cloud ID, site URL, space key and space name plus a library title and description. Optionally limits indexing to specific page IDs and associates the library with a team project. Adding a library is permanent: there is no delete endpoint in the Context7 API. |
| Add Git Repository | `addGitRepository` | Submits a repository hosted on any other Git provider (for example Codeberg or a self-hosted Git server) to Context7 for documentation indexing. Supports private repositories with an access token, optional version-page filtering, and source-code documentation generation. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API. Returns 400 invalid-git-repository when the URL is not a reachable Git repository. |
| Add GitHub Repository | `addGitHubRepository` | Submits a GitHub repository to Context7 for documentation indexing. Supports private repositories with a personal access token (or the token from your Context7 GitHub OAuth connection), optional version-page filtering, and source-code documentation generation. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API. Returns 400 repository-not-found when the repository does not exist or is inaccessible, and 409 when it was already added. |
| Add GitLab Repository | `addGitLabRepository` | Submits a GitLab repository to Context7 for documentation indexing. Supports private repositories with a personal access token, optional version-page filtering, and source-code documentation generation. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API. Returns 400 repository-not-found when the repository does not exist or is inaccessible, and 409 when it was already added. |
| Add llms.txt File | `addLlmsTxtFile` | Submits an llms.txt, llms-full.txt or llms-small.txt file by URL to Context7 for indexing as a library. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API. Returns 400 unresolvable-url when the URL cannot be fetched. |
| Add Notion Pages | `addNotionPages` | Indexes selected Notion pages as a private Context7 library. Requires the Notion workspace ID and name, the page IDs to index, and a library title and description; optionally associates the library with a team project. Adding a library is permanent: there is no delete endpoint in the Context7 API. |
| Add OpenAPI Specification | `addOpenApiSpecification` | Submits an OpenAPI specification (JSON or YAML) by URL to Context7 for indexing as a library. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API. Returns 400 unresolvable-url when the URL cannot be fetched. |
| Add Website | `addWebsite` | Submits a documentation website to Context7 for crawling and indexing as a library. Optionally restricts the crawl to pages under a base URL. Returns the assigned library ID. Adding a library is permanent: there is no delete endpoint in the Context7 API. Returns 400 unresolvable-url when the site cannot be reached. |
| Get Documentation Context | `getDocumentationContext` | Fetches the most relevant documentation for a library, ranked against the user's question or task. With type 'json' the response contains structured code snippets and documentation snippets plus any team or library rules; with type 'txt' it is a plain-text block ready to paste into a prompt. Use Search Libraries first to find the Context7 library ID. |

<details>

<summary>See 5 more actions</summary>

* **Get Library Metrics** `getLibraryMetrics`: Returns usage metrics for a library you own: lifetime request totals by surface (web page, plain text, MCP, CLI), per-day request history, daily MCP client unique-user breakdown, and lifetime topic and country distributions. Only library owners can read metrics; other callers receive 403 forbidden.
* **Get Teamspace Policies** `getTeamspacePolicies`: Returns the complete access policy configuration of the API key's teamspace: which documentation source types are enabled, the library filter mode with its quality thresholds, blocked and excepted libraries, repository and website quality filters, the manually selected library list, and the number of libraries currently accessible.
* **Refresh Library** `refreshLibrary`: Triggers a re-index of an existing Context7 library so its documentation reflects the latest source. Optionally targets a specific branch, and accepts a Git access token for private repositories (otherwise the stored OAuth token is used). Returns 404 library_not_found when the library has not been added yet.
* **Search Libraries** `searchLibraries`: Searches the Context7 library index by library name, ranking results by relevance to the user's question or task. Returns matching libraries with their Context7 library ID, processing state, snippet and token counts, trust and benchmark scores, and available version tags. Returns 404 no_libraries_found when nothing matches.
* **Update Teamspace Policies** `updateTeamspacePolicies`: Incrementally updates the teamspace's access policies. Only the fields you provide are changed. Enable or disable documentation source types, switch the library filter mode, set quality thresholds (verified only, minimum trust score, maximum age, minimum stars, allowed SPDX licenses, website backlink and traffic minimums), add or remove blocked and excepted libraries, or maintain the manually selected library list. At least one of sourceTypes or libraryFilters must be supplied. Returns the full updated policy.

</details>
