---
description: "Sentry is an error and performance monitoring platform. Manage projects, issues, releases, deploys, teams and service hooks."
hidden: true
---

# Sentry

<img src="../../.gitbook/assets/connectors/lg/sentry.png" alt="Sentry logo">

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [sentry.io](https://sentry.io) |
| **Authentication** | Access token |
| **Slug** | `sentry` |

## Setup

Your customers enter their access token for Sentry when they connect. Nothing else needs setting up.

## Use it

Add Sentry from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sentry.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Issue Comment</td><td><code>createIssueComment</code></td><td>Add a comment (note) to an issue</td></tr><tr><td>Create Project</td><td><code>createProject</code></td><td>Create a project under a team</td></tr><tr><td>Create Release</td><td><code>createRelease</code></td><td>Create a release</td></tr><tr><td>Create Release Deploy</td><td><code>createReleaseDeploy</code></td><td>Create a deploy for a release</td></tr><tr><td>Create Service Hook</td><td><code>createServiceHook</code></td><td>Create a project service hook/webhook Used by the webhook config.</td></tr><tr><td>Create Team</td><td><code>createTeam</code></td><td>Create a team</td></tr><tr><td>Delete Issue</td><td><code>deleteIssue</code></td><td>Delete an issue</td></tr><tr><td>Delete Project</td><td><code>deleteProject</code></td><td>Delete a project</td></tr><tr><td>Delete Release</td><td><code>deleteRelease</code></td><td>Delete a release</td></tr><tr><td>Delete Service Hook</td><td><code>deleteServiceHook</code></td><td>Delete a project service hook</td></tr></tbody></table>

<details>

<summary>View 23 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Team</td><td><code>deleteTeam</code></td><td>Schedules a team for deletion in a Sentry organization. The team is marked pending deletion and removed asynchronously; its projects are not deleted and remain in the organization.</td></tr><tr><td>Get Issue</td><td><code>getIssue</code></td><td>Get an issue by ID</td></tr><tr><td>Get Issue Tag Values</td><td><code>getIssueTagValues</code></td><td>List values for a tag key on an issue</td></tr><tr><td>Get Latest Event</td><td><code>getLatestEvent</code></td><td>Get the latest event for an issue</td></tr><tr><td>Get Organization</td><td><code>getOrganization</code></td><td>Get an organization by slug</td></tr><tr><td>Get Project</td><td><code>getProject</code></td><td>Get a project</td></tr><tr><td>Get Project Event</td><td><code>getProjectEvent</code></td><td>Get a specific event in a project</td></tr><tr><td>Get Release</td><td><code>getRelease</code></td><td>Get a release by version</td></tr><tr><td>List Issue Comments</td><td><code>listIssueComments</code></td><td>List activity notes/comments on an issue</td></tr><tr><td>List Issue Events</td><td><code>listIssueEvents</code></td><td>List events for an issue</td></tr><tr><td>List Issue Tags</td><td><code>listIssueTags</code></td><td>List tag keys for an issue</td></tr><tr><td>List Issues</td><td><code>listIssues</code></td><td>List a project's issues</td></tr><tr><td>List Members</td><td><code>listMembers</code></td><td>List organization members</td></tr><tr><td>List Organization Projects</td><td><code>listOrganizationProjects</code></td><td>List projects in an organization</td></tr><tr><td>List Organizations</td><td><code>listOrganizations</code></td><td>List organizations the user belongs to</td></tr><tr><td>List Project Events</td><td><code>listProjectEvents</code></td><td>List events for a project</td></tr><tr><td>List Project Keys</td><td><code>listProjectKeys</code></td><td>List a project's client keys (DSNs)</td></tr><tr><td>List Releases</td><td><code>listReleases</code></td><td>List releases for an organization</td></tr><tr><td>List Service Hooks</td><td><code>listServiceHooks</code></td><td>List a project's service hooks</td></tr><tr><td>List Teams</td><td><code>listTeams</code></td><td>List teams in an organization</td></tr><tr><td>Update Issue</td><td><code>updateIssue</code></td><td>Update an issue: resolve/ignore, assign, bookmark</td></tr><tr><td>Update Project</td><td><code>updateProject</code></td><td>Update a project</td></tr><tr><td>Update Release</td><td><code>updateRelease</code></td><td>Update a release</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Event Alert</td><td><code>event.alert</code></td><td>An event triggered an alert rule.</td></tr><tr><td>Event Created</td><td><code>event.created</code></td><td>A new event was ingested in the project.</td></tr></tbody></table>
