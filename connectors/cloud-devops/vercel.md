---
description: "Vercel REST API (base https://api.vercel.com)."
---

# Vercel

Vercel REST API (base https://api.vercel.com). Manage projects, deployments (create/get/cancel/delete/events), environment variables, domains and project domains, DNS records, teams, the current user, and webhooks. Auth: Bearer access token. Team-scoped resources accept a teamId query param.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [vercel.com](https://vercel.com) |
| **Authentication** | Bearer token |
| **Actions** | 31 |
| **Events** | 8 |
| **Slug** | `vercel` |

## Use it

Add Vercel from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.vercel.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Domain | `addDomain` | Add/register a domain to the account (POST /v5/domains). |
| Add Project Domain | `addProjectDomain` | Assign a domain to a project (POST /v10/projects/{idOrName}/domains). |
| Cancel Deployment | `cancelDeployment` | Cancel a running deployment (PATCH /v12/deployments/{id}/cancel). |
| Create Deployment | `createDeployment` | Create a new deployment (POST /v13/deployments). Provide gitSource for a Git deploy or files for an inline deploy. |
| Create DNS Record | `createDnsRecord` | Create a DNS record for a domain (POST /v2/domains/{domain}/records). |
| Create Project | `createProject` | Create a project (POST /v11/projects). |
| Create Project Env Var | `createProjectEnv` | Create an environment variable on a project (POST /v10/projects/{idOrName}/env). |
| Create Webhook | `createWebhook` | Create a webhook (POST /v1/webhooks). Used by the webhook config. |
| Delete Deployment | `deleteDeployment` | Delete a deployment (DELETE /v13/deployments/{id}). |
| Delete DNS Record | `deleteDnsRecord` | Delete a DNS record (DELETE /v2/domains/{domain}/records/{recordId}). |
| Delete Project | `deleteProject` | Delete a project (DELETE /v9/projects/{idOrName}). Returns 204. |
| Delete Project Env Var | `deleteProjectEnv` | Delete a project environment variable (DELETE /v9/projects/{idOrName}/env/{envId}). |
| Delete Webhook | `deleteWebhook` | Delete a webhook (DELETE /v1/webhooks/{id}). Returns 204. |
| Get Current User | `getCurrentUser` | Get the authenticated user (GET /v2/user). |
| Get Deployment | `getDeployment` | Get a deployment by id or URL (GET /v13/deployments/{idOrUrl}). |
| Get Domain | `getDomain` | Get a domain's configuration (GET /v5/domains/{domain}). |
| Get Project | `getProject` | Get a project by id or name (GET /v9/projects/{idOrName}). |
| Get Team | `getTeam` | Get a team by ID (GET /v2/teams/{teamId}). |
| List Deployment Events | `listDeploymentEvents` | Get build/runtime logs (events) for a deployment (GET /v3/deployments/{id}/events). |
| List Deployments | `listDeployments` | List deployments (GET /v6/deployments). |
| List DNS Records | `listDnsRecords` | List DNS records for a domain (GET /v4/domains/{domain}/records). |
| List Domains | `listDomains` | List domains owned by the account (GET /v5/domains). |
| List Project Domains | `listProjectDomains` | List domains assigned to a project (GET /v9/projects/{idOrName}/domains). |
| List Project Env Vars | `listProjectEnv` | List environment variables of a project (GET /v9/projects/{idOrName}/env). |
| List Projects | `listProjects` | List projects (GET /v9/projects). |
| List Teams | `listTeams` | List teams the user belongs to (GET /v2/teams). |
| List Webhooks | `listWebhooks` | List webhooks (GET /v1/webhooks). |
| Remove Domain | `removeDomain` | Remove a domain from the account (DELETE /v6/domains/{domain}). |
| Remove Project Domain | `removeProjectDomain` | Remove a domain from a project (DELETE /v9/projects/{idOrName}/domains/{domain}). |
| Update Project | `updateProject` | Update a project (PATCH /v9/projects/{idOrName}). |
| Update Project Env Var | `updateProjectEnv` | Update a project environment variable (PATCH /v9/projects/{idOrName}/env/{envId}). |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Deployment Canceled | `deployment.canceled` | A deployment was canceled. |
| Deployment Created | `deployment.created` | A deployment was created. |
| Deployment Error | `deployment.error` | A deployment failed. |
| Deployment Promoted | `deployment.promoted` | A deployment was promoted to production. |
| Deployment Succeeded | `deployment.succeeded` | A deployment finished successfully. |
| Domain Created | `domain.created` | A domain was created. |
| Project Created | `project.created` | A project was created. |
| Project Removed | `project.removed` | A project was removed. |
