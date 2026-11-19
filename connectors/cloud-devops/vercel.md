---
description: "Vercel REST API (base https://api.vercel.com)."
hidden: true
---

# Vercel

<img src="../../.gitbook/assets/connectors/lg/vercel.png" alt="Vercel logo">

Manage projects, deployments (create/get/cancel/delete/events), environment variables, domains and project domains, DNS records, teams, the current user, and webhooks. Auth: Bearer access token. Team-scoped resources accept a teamId query param.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [vercel.com](https://vercel.com) |
| **Authentication** | Bearer token |
| **Slug** | `vercel` |

## Use it

Add Vercel from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.vercel.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Domain</td><td><code>addDomain</code></td><td>Add/register a domain to the account (POST /v5/domains).</td></tr><tr><td>Add Project Domain</td><td><code>addProjectDomain</code></td><td>Assign a domain to a project (POST /v10/projects/{idOrName}/domains).</td></tr><tr><td>Cancel Deployment</td><td><code>cancelDeployment</code></td><td>Cancel a running deployment (PATCH /v12/deployments/{id}/cancel).</td></tr><tr><td>Create Deployment</td><td><code>createDeployment</code></td><td>Create a new deployment (POST /v13/deployments). Provide gitSource for a Git deploy or files for an inline deploy.</td></tr><tr><td>Create DNS Record</td><td><code>createDnsRecord</code></td><td>Create a DNS record for a domain (POST /v2/domains/{domain}/records).</td></tr><tr><td>Create Project</td><td><code>createProject</code></td><td>Create a project (POST /v11/projects).</td></tr><tr><td>Create Project Env Var</td><td><code>createProjectEnv</code></td><td>Create an environment variable on a project (POST /v10/projects/{idOrName}/env).</td></tr><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Create a webhook (POST /v1/webhooks). Used by the webhook config.</td></tr><tr><td>Delete Deployment</td><td><code>deleteDeployment</code></td><td>Delete a deployment (DELETE /v13/deployments/{id}).</td></tr><tr><td>Delete DNS Record</td><td><code>deleteDnsRecord</code></td><td>Delete a DNS record (DELETE /v2/domains/{domain}/records/{recordId}).</td></tr></tbody></table>

<details>

<summary>View 21 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Project</td><td><code>deleteProject</code></td><td>Delete a project (DELETE /v9/projects/{idOrName}). Returns 204.</td></tr><tr><td>Delete Project Env Var</td><td><code>deleteProjectEnv</code></td><td>Delete a project environment variable (DELETE /v9/projects/{idOrName}/env/{envId}).</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Delete a webhook (DELETE /v1/webhooks/{id}). Returns 204.</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Get the authenticated user (GET /v2/user).</td></tr><tr><td>Get Deployment</td><td><code>getDeployment</code></td><td>Get a deployment by id or URL (GET /v13/deployments/{idOrUrl}).</td></tr><tr><td>Get Domain</td><td><code>getDomain</code></td><td>Get a domain's configuration (GET /v5/domains/{domain}).</td></tr><tr><td>Get Project</td><td><code>getProject</code></td><td>Get a project by id or name (GET /v9/projects/{idOrName}).</td></tr><tr><td>Get Team</td><td><code>getTeam</code></td><td>Get a team by ID (GET /v2/teams/{teamId}).</td></tr><tr><td>List Deployment Events</td><td><code>listDeploymentEvents</code></td><td>Get build/runtime logs (events) for a deployment (GET /v3/deployments/{id}/events).</td></tr><tr><td>List Deployments</td><td><code>listDeployments</code></td><td>List deployments (GET /v6/deployments).</td></tr><tr><td>List DNS Records</td><td><code>listDnsRecords</code></td><td>List DNS records for a domain (GET /v4/domains/{domain}/records).</td></tr><tr><td>List Domains</td><td><code>listDomains</code></td><td>List domains owned by the account (GET /v5/domains).</td></tr><tr><td>List Project Domains</td><td><code>listProjectDomains</code></td><td>List domains assigned to a project (GET /v9/projects/{idOrName}/domains).</td></tr><tr><td>List Project Env Vars</td><td><code>listProjectEnv</code></td><td>List environment variables of a project (GET /v9/projects/{idOrName}/env).</td></tr><tr><td>List Projects</td><td><code>listProjects</code></td><td>List projects (GET /v9/projects).</td></tr><tr><td>List Teams</td><td><code>listTeams</code></td><td>List teams the user belongs to (GET /v2/teams).</td></tr><tr><td>List Webhooks</td><td><code>listWebhooks</code></td><td>List webhooks (GET /v1/webhooks).</td></tr><tr><td>Remove Domain</td><td><code>removeDomain</code></td><td>Remove a domain from the account (DELETE /v6/domains/{domain}).</td></tr><tr><td>Remove Project Domain</td><td><code>removeProjectDomain</code></td><td>Remove a domain from a project (DELETE /v9/projects/{idOrName}/domains/{domain}).</td></tr><tr><td>Update Project</td><td><code>updateProject</code></td><td>Update a project (PATCH /v9/projects/{idOrName}).</td></tr><tr><td>Update Project Env Var</td><td><code>updateProjectEnv</code></td><td>Update a project environment variable (PATCH /v9/projects/{idOrName}/env/{envId}).</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Deployment Canceled</td><td><code>deployment.canceled</code></td><td>A deployment was canceled.</td></tr><tr><td>Deployment Created</td><td><code>deployment.created</code></td><td>A deployment was created.</td></tr><tr><td>Deployment Error</td><td><code>deployment.error</code></td><td>A deployment failed.</td></tr><tr><td>Deployment Promoted</td><td><code>deployment.promoted</code></td><td>A deployment was promoted to production.</td></tr><tr><td>Deployment Succeeded</td><td><code>deployment.succeeded</code></td><td>A deployment finished successfully.</td></tr><tr><td>Domain Created</td><td><code>domain.created</code></td><td>A domain was created.</td></tr><tr><td>Project Created</td><td><code>project.created</code></td><td>A project was created.</td></tr><tr><td>Project Removed</td><td><code>project.removed</code></td><td>A project was removed.</td></tr></tbody></table>
