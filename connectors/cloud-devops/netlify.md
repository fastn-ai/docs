---
description: "Netlify web hosting and deployment platform."
hidden: true
---

# Netlify

<img src="../../.gitbook/assets/connectors/lg/netlify.png" alt="Netlify logo">

Netlify web hosting and deployment platform. Manage sites, deploys, builds, forms and submissions, files, snippets, DNS zones and records, build hooks, deploy keys, environment variables, accounts and members, service instances, and split tests via the Netlify REST API.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [netlify.com](https://netlify.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `netlify` |

## Use it

Add Netlify from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.netlify.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Account Member | `addMember` | Invite a new member to an account/team by email with a given role. |
| Cancel Site Deploy | `cancelSiteDeploy` | Cancel an in-progress deploy by its deploy ID. |
| Create Deploy Key | `createDeployKey` | Create a new deploy key. The generated public key can be added to a Git provider to grant repository access. |
| Create DNS Record | `createDnsRecord` | Create a new DNS record in a zone. Hostname, type, and value are required. |
| Create DNS Zone | `createDnsZone` | Create a new DNS zone for a domain under an account. Name and account ID are required. |
| Create Environment Variables | `createEnvVars` | Create an environment variable for an account or, with site_id, for one site. Key, values and secret flag are required. Netlify applies all scopes (builds, functions, runtime, post-processing) by default; this action does not set specific scopes. |
| Create Hook | `createHook` | Create a notification hook for a site that fires on a given event. The hook type and event are required. |
| Create Service Instance | `createServiceInstance` | Provision an add-on service instance for a site by add-on slug. |
| Create Site | `createSite` | Create a new site in the default account. All fields are optional; when name is omitted Netlify auto-generates one. |
| Create Site Build | `createSiteBuild` | Trigger a new build for a site. Optionally clear the build cache. Requires the site to have a linked repository. |

<details>

<summary>See 78 more actions</summary>

* **Create Site Deploy** `createSiteDeploy`: Create a new deploy for a site by supplying a file digest. Pass an empty files object to create a draft deploy.
* **Create Site In Team** `createSiteInTeam`: Create a new site under a specific account/team identified by its slug.
* **Create Site Snippet** `createSiteSnippet`: Create a custom code snippet injected into a site's pages. Title, general code, and its position are required.
* **Create Split Test** `createSplitTest`: Create a branch-based split test for a site. Branch tests defining branches and their traffic weights are required.
* **Delete Deploy** `deleteDeploy`: Delete a deploy directly by its deploy ID. Returns no content on success.
* **Delete Deploy Key** `deleteDeployKey`: Delete a deploy key by its ID. Returns no content on success.
* **Delete DNS Record** `deleteDnsRecord`: Delete a DNS record by zone ID and record ID. Returns no content on success.
* **Delete DNS Zone** `deleteDnsZone`: Delete a DNS zone by its ID. Returns no content on success.
* **Delete Environment Variable** `deleteEnvVar`: Delete an environment variable by account and key. Returns no content on success.
* **Delete Environment Variable Value** `deleteEnvVarValue`: Delete a single value of an environment variable by account, key, and value ID. Returns no content on success.
* **Delete Hook** `deleteHook`: Delete a hook by its ID. Returns no content on success.
* **Delete Service Instance** `deleteServiceInstance`: Delete an add-on service instance by site, add-on, and instance ID. Returns no content on success.
* **Delete Site** `deleteSite`: Permanently delete a site by its ID. Returns no content on success.
* **Delete Site Deploy** `deleteSiteDeploy`: Delete a deploy of a site by site ID and deploy ID. Returns no content on success.
* **Delete Site Form** `deleteSiteForm`: Delete a form from a site by site ID and form ID. Returns no content on success.
* **Delete Site Snippet** `deleteSiteSnippet`: Delete a code snippet from a site by site ID and snippet ID. Returns no content on success.
* **Delete Submission** `deleteSubmission`: Delete a form submission by its ID. Returns no content on success.
* **Disable Site** `disableSite`: Disable a site, taking it offline. A reason is required.
* **Disable Split Test** `disableSplitTest`: Unpublish (disable) an active split test. Returns no content on success.
* **Enable Hook** `enableHook`: Enable a previously disabled hook by its ID.
* **Enable Site** `enableSite`: Re-enable a site that was previously disabled. Returns no content on success.
* **Enable Split Test** `enableSplitTest`: Publish (enable) a split test so traffic is split across the configured branches. Returns no content on success.
* **Get Account** `getAccount`: Retrieve a single account/team by its ID.
* **Get Account Build Status** `getAccountBuildStatus`: Get the build status and concurrency usage for an account/team.
* **Get Account Member** `getMember`: Retrieve a single member of an account/team by slug and member ID.
* **Get Current User** `getCurrentUser`: Retrieve the profile of the authenticated user.
* **Get Deploy** `getDeploy`: Retrieve a deploy directly by its deploy ID.
* **Get Deploy Key** `getDeployKey`: Retrieve a single deploy key by its ID.
* **Get DNS Record** `getDnsRecord`: Retrieve a single DNS record by zone ID and record ID.
* **Get DNS Zone** `getDnsZone`: Retrieve a single DNS zone by its ID.
* **Get Environment Variable** `getEnvVar`: Retrieve a single environment variable by account and key.
* **Get Hook** `getHook`: Retrieve a single hook by its ID.
* **Get Service Instance** `getServiceInstance`: Retrieve a single add-on service instance by site, add-on, and instance ID.
* **Get Site** `getSite`: Retrieve a single site by its ID.
* **Get Site Build** `getSiteBuild`: Retrieve a single build by its build ID.
* **Get Site Deploy** `getSiteDeploy`: Retrieve a specific deploy of a site by site ID and deploy ID.
* **Get Site File** `getSiteFile`: Retrieve metadata for a single file in a site's published deploy by its path.
* **Get Site Snippet** `getSiteSnippet`: Retrieve a single code snippet of a site by site ID and snippet ID.
* **Get Split Test** `getSplitTest`: Retrieve a single split test by site ID and split test ID.
* **Get Submission** `getSubmission`: Retrieve a single form submission by its ID.
* **List Account Audit Events** `listAccountAuditEvents`: List audit log events for an account/team. Audit logging may require a paid plan.
* **List Account Members** `listMembers`: List all members of an account/team by its slug.
* **List Account Types** `listAccountTypes`: List the account/team plan types available to the authenticated user.
* **List Accounts** `listAccounts`: List all accounts/teams the authenticated user is a member of.
* **List Build Hooks** `listHooks`: List all notification and build hooks configured for a site.
* **List Deploy Keys** `listDeployKeys`: List all deploy keys for the authenticated user.
* **List DNS Records** `listDnsRecords`: List all DNS records in a DNS zone.
* **List DNS Zones** `listDnsZones`: List all DNS zones the user has access to, optionally filtered by account slug.
* **List Environment Variables** `getEnvVars`: List environment variables for an account, optionally scoped to a site or context.
* **List Form Submissions** `listFormSubmissions`: List all submissions for a specific form, with pagination.
* **List Hook Types** `listHookTypes`: List all available hook types and the events they support.
* **List Service Instances** `listServiceInstances`: List all add-on service instances provisioned for a site.
* **List Site Builds** `listSiteBuilds`: List all builds for a site, with pagination.
* **List Site Deploys** `listSiteDeploys`: List all deploys for a site, with optional filtering by state, branch, and deploy type.
* **List Site Files** `listSiteFiles`: List all files in the current published deploy of a site.
* **List Site Forms** `listSiteForms`: List all forms configured for a site.
* **List Site Snippets** `listSiteSnippets`: List all custom code snippets injected into a site's pages.
* **List Site Submissions** `listSiteSubmissions`: List all form submissions across every form on a site, with pagination.
* **List Sites** `listSites`: List all sites the authenticated user has access to. Supports filtering by name and ownership, with pagination.
* **List Sites For Account** `listSitesForAccount`: List all sites belonging to a specific account/team, identified by its slug.
* **List Split Tests** `listSplitTests`: List all branch-based split tests (A/B tests) configured for a site.
* **Lock Deploy** `lockDeploy`: Lock a deploy to prevent it from being overwritten by future deploys.
* **Remove Account Member** `removeMember`: Remove a member from an account/team by slug and member ID. Returns no content on success.
* **Restore Site Deploy** `restoreSiteDeploy`: Restore a previous deploy, republishing it as the current live deploy.
* **Rollback Site Deploy** `rollbackSiteDeploy`: Roll a site back to its previous published deploy. Returns no content on success.
* **Set Environment Variable Value** `setEnvVarValue`: Set or update the value of an environment variable for a specific deploy context.
* **Transfer DNS Zone** `transferDnsZone`: Transfer a DNS zone to another account and user. All target identifiers are required.
* **Unlink Site Repository** `unlinkSiteRepo`: Disconnect the linked Git repository from a site.
* **Unlock Deploy** `unlockDeploy`: Unlock a previously locked deploy so it can be overwritten by future deploys.
* **Update Account** `updateAccount`: Update an account/team's settings such as name and billing details.
* **Update Account Member** `updateMember`: Update an account/team member's role or site access.
* **Update Environment Variable** `updateEnvVar`: Replace an environment variable's values and secret flag for a given key; existing values are replaced by the values sent. Scopes are not changed (Netlify keeps all scopes by default).
* **Update Hook** `updateHook`: Update an existing hook's event, type, or configuration data.
* **Update Service Instance** `updateServiceInstance`: Update the configuration of an add-on service instance. Returns no content on success.
* **Update Site** `updateSite`: Update an existing site's settings. Only the fields you provide are changed.
* **Update Site Deploy** `updateSiteDeploy`: Update a deploy of a site with a new file digest.
* **Update Site Snippet** `updateSiteSnippet`: Update an existing code snippet of a site. Returns no content on success.
* **Update Split Test** `updateSplitTest`: Update the branch tests of an existing split test.

</details>
