---
description: "Vercel hosts and deploys web apps. Manage projects, deployments, environment variables, domains, DNS records and webhooks."
hidden: true
---

# Vercel

<img src="../../.gitbook/assets/connectors/lg/vercel.png" alt="Vercel logo">

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [vercel.com](https://vercel.com) |
| **Authentication** | Access token |
| **Slug** | `vercel` |

## Setup

Your customers enter their access token for Vercel when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Vercel from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Vercel**.
2. Select **Connect** on the Vercel card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Vercel's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Domain</td><td><code>addDomain</code></td><td>Add/register a domain to the account</td></tr><tr><td>Add Project Domain</td><td><code>addProjectDomain</code></td><td>Assign a domain to a project</td></tr><tr><td>Cancel Deployment</td><td><code>cancelDeployment</code></td><td>Cancel a running deployment</td></tr><tr><td>Create Deployment</td><td><code>createDeployment</code></td><td>Create a new deployment Provide gitSource for a Git deploy or files for an inline deploy.</td></tr><tr><td>Create DNS Record</td><td><code>createDnsRecord</code></td><td>Create a DNS record for a domain</td></tr><tr><td>Create Project</td><td><code>createProject</code></td><td>Create a project</td></tr><tr><td>Create Project Env Var</td><td><code>createProjectEnv</code></td><td>Create an environment variable on a project</td></tr><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Create a webhook Used by the webhook config.</td></tr><tr><td>Delete Deployment</td><td><code>deleteDeployment</code></td><td>Delete a deployment</td></tr><tr><td>Delete DNS Record</td><td><code>deleteDnsRecord</code></td><td>Delete a DNS record</td></tr></tbody></table>

<details>

<summary>View 21 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Project</td><td><code>deleteProject</code></td><td>Delete a project</td></tr><tr><td>Delete Project Env Var</td><td><code>deleteProjectEnv</code></td><td>Delete a project environment variable</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Delete a webhook</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Get the authenticated user</td></tr><tr><td>Get Deployment</td><td><code>getDeployment</code></td><td>Get a deployment by id or URL</td></tr><tr><td>Get Domain</td><td><code>getDomain</code></td><td>Get a domain's configuration</td></tr><tr><td>Get Project</td><td><code>getProject</code></td><td>Get a project by id or name</td></tr><tr><td>Get Team</td><td><code>getTeam</code></td><td>Get a team by ID</td></tr><tr><td>List Deployment Events</td><td><code>listDeploymentEvents</code></td><td>Get build/runtime logs (events) for a deployment</td></tr><tr><td>List Deployments</td><td><code>listDeployments</code></td><td>List deployments</td></tr><tr><td>List DNS Records</td><td><code>listDnsRecords</code></td><td>List DNS records for a domain</td></tr><tr><td>List Domains</td><td><code>listDomains</code></td><td>List domains owned by the account</td></tr><tr><td>List Project Domains</td><td><code>listProjectDomains</code></td><td>List domains assigned to a project</td></tr><tr><td>List Project Env Vars</td><td><code>listProjectEnv</code></td><td>List environment variables of a project</td></tr><tr><td>List Projects</td><td><code>listProjects</code></td><td>List projects</td></tr><tr><td>List Teams</td><td><code>listTeams</code></td><td>List teams the user belongs to</td></tr><tr><td>List Webhooks</td><td><code>listWebhooks</code></td><td>List webhooks</td></tr><tr><td>Remove Domain</td><td><code>removeDomain</code></td><td>Remove a domain from the account</td></tr><tr><td>Remove Project Domain</td><td><code>removeProjectDomain</code></td><td>Remove a domain from a project</td></tr><tr><td>Update Project</td><td><code>updateProject</code></td><td>Update a project</td></tr><tr><td>Update Project Env Var</td><td><code>updateProjectEnv</code></td><td>Update a project environment variable</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Deployment Canceled</td><td><code>deployment.canceled</code></td><td>A deployment was canceled.</td></tr><tr><td>Deployment Created</td><td><code>deployment.created</code></td><td>A deployment was created.</td></tr><tr><td>Deployment Error</td><td><code>deployment.error</code></td><td>A deployment failed.</td></tr><tr><td>Deployment Promoted</td><td><code>deployment.promoted</code></td><td>A deployment was promoted to production.</td></tr><tr><td>Deployment Succeeded</td><td><code>deployment.succeeded</code></td><td>A deployment finished successfully.</td></tr><tr><td>Domain Created</td><td><code>domain.created</code></td><td>A domain was created.</td></tr><tr><td>Project Created</td><td><code>project.created</code></td><td>A project was created.</td></tr><tr><td>Project Removed</td><td><code>project.removed</code></td><td>A project was removed.</td></tr></tbody></table>
