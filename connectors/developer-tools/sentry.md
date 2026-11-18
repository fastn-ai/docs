---
description: "Sentry API v0 (default base https://sentry.io, configurable for self-hosted)."
hidden: true
---

# Sentry

<img src="../../.gitbook/assets/connectors/lg/sentry.png" alt="Sentry logo">

Sentry API v0 (default base https://sentry.io, configurable for self-hosted). Manage organizations, projects, issues (list/get/update/delete/assign/resolve), events, issue comments and tags, releases and deploys, teams, members, project client keys (DSNs), and service hooks (webhooks). Auth: Bearer auth token / internal integration token.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [sentry.io](https://sentry.io) |
| **Authentication** | Bearer token |
| **Slug** | `sentry` |

## Use it

Add Sentry from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sentry.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Issue Comment | `createIssueComment` | Add a comment (note) to an issue (POST /api/0/organizations/{org}/issues/{issueId}/comments/). |
| Create Project | `createProject` | Create a project under a team (POST /api/0/teams/{org}/{team}/projects/). |
| Create Release | `createRelease` | Create a release (POST /api/0/organizations/{org}/releases/). |
| Create Release Deploy | `createReleaseDeploy` | Create a deploy for a release (POST /api/0/organizations/{org}/releases/{version}/deploys/). |
| Create Service Hook | `createServiceHook` | Create a project service hook/webhook (POST /api/0/projects/{org}/{project}/hooks/). Used by the webhook config. |
| Create Team | `createTeam` | Create a team (POST /api/0/organizations/{org}/teams/). |
| Delete Issue | `deleteIssue` | Delete an issue (DELETE /api/0/organizations/{org}/issues/{issueId}/). Returns 202. |
| Delete Project | `deleteProject` | Delete a project (DELETE /api/0/projects/{org}/{project}/). Returns 204. |
| Delete Release | `deleteRelease` | Delete a release (DELETE /api/0/organizations/{org}/releases/{version}/). Returns 204. |
| Delete Service Hook | `deleteServiceHook` | Delete a project service hook (DELETE /api/0/projects/{org}/{project}/hooks/{hookId}/). Returns 204. |

<details>

<summary>See 23 more actions</summary>

* **Delete Team** `deleteTeam`: Schedules a team for deletion in a Sentry organization. The team is marked pending deletion and removed asynchronously; its projects are not deleted and remain in the organization. Returns 204 No Content on success.
* **Get Issue** `getIssue`: Get an issue by ID (GET /api/0/organizations/{org}/issues/{issueId}/).
* **Get Issue Tag Values** `getIssueTagValues`: List values for a tag key on an issue (GET /api/0/organizations/{org}/issues/{issueId}/tags/{key}/values/).
* **Get Latest Event** `getLatestEvent`: Get the latest event for an issue (GET /api/0/organizations/{org}/issues/{issueId}/events/latest/).
* **Get Organization** `getOrganization`: Get an organization by slug (GET /api/0/organizations/{org}/).
* **Get Project** `getProject`: Get a project (GET /api/0/projects/{org}/{project}/).
* **Get Project Event** `getProjectEvent`: Get a specific event in a project (GET /api/0/projects/{org}/{project}/events/{eventId}/).
* **Get Release** `getRelease`: Get a release by version (GET /api/0/organizations/{org}/releases/{version}/).
* **List Issue Comments** `listIssueComments`: List activity notes/comments on an issue (GET /api/0/organizations/{org}/issues/{issueId}/comments/).
* **List Issue Events** `listIssueEvents`: List events for an issue (GET /api/0/organizations/{org}/issues/{issueId}/events/).
* **List Issue Tags** `listIssueTags`: List tag keys for an issue (GET /api/0/organizations/{org}/issues/{issueId}/tags/).
* **List Issues** `listIssues`: List a project's issues (GET /api/0/projects/{org}/{project}/issues/).
* **List Members** `listMembers`: List organization members (GET /api/0/organizations/{org}/members/).
* **List Organization Projects** `listOrganizationProjects`: List projects in an organization (GET /api/0/organizations/{org}/projects/).
* **List Organizations** `listOrganizations`: List organizations the user belongs to (GET /api/0/organizations/).
* **List Project Events** `listProjectEvents`: List events for a project (GET /api/0/projects/{org}/{project}/events/).
* **List Project Keys** `listProjectKeys`: List a project's client keys (DSNs) (GET /api/0/projects/{org}/{project}/keys/).
* **List Releases** `listReleases`: List releases for an organization (GET /api/0/organizations/{org}/releases/).
* **List Service Hooks** `listServiceHooks`: List a project's service hooks (GET /api/0/projects/{org}/{project}/hooks/).
* **List Teams** `listTeams`: List teams in an organization (GET /api/0/organizations/{org}/teams/).
* **Update Issue** `updateIssue`: Update an issue: resolve/ignore, assign, bookmark (PUT /api/0/organizations/{org}/issues/{issueId}/).
* **Update Project** `updateProject`: Update a project (PUT /api/0/projects/{org}/{project}/).
* **Update Release** `updateRelease`: Update a release (PUT /api/0/organizations/{org}/releases/{version}/).

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Event Alert | `event.alert` | An event triggered an alert rule. |
| Event Created | `event.created` | A new event was ingested in the project. |
