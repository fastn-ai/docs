---
description: "Doppler is a secrets management platform for storing, syncing, and rotating environment variables, API keys, and secrets across projects, environments, and…"
hidden: true
---

# Doppler

Doppler is a secrets management platform for storing, syncing, and rotating environment variables, API keys, and secrets across projects, environments, and services. This connector wraps Doppler's v3 REST API covering workplace settings, projects, environments, configs, secrets, activity/config logs, service tokens, integrations, syncs, webhooks, and Doppler Share.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [doppler.com](https://doppler.com) |
| **Authentication** | Bearer token |
| **Actions** | 59 |
| **Events** | 0 |
| **Slug** | `doppler` |

## Use it

Add Doppler from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.doppler.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Config Trusted IP | `addConfigTrustedIp` | Adds a trusted IP address or CIDR range that is allowed to access a config. |
| Add Webhook | `addWebhook` | Creates a new webhook that Doppler will POST to whenever a secret changes. |
| Clone Config | `cloneConfig` | Clones an existing branch config, including its secrets, into a new branch config. |
| Create Config | `createConfig` | Creates a new branch config under an environment within a project. |
| Create Environment | `createEnvironment` | Creates a new environment within a Doppler project. |
| Create Project | `createProject` | Creates a new Doppler project, which is a top-level container for environments, configs, and secrets. |
| Create Service Token | `createServiceToken` | Creates a new read-only or read/write service token scoped to a config, for use by applications and services. |
| Create Sync | `createSync` | Creates a secret sync from a config to a configured third-party integration destination. |
| Delete Config | `deleteConfig` | Permanently deletes a branch config and its secrets. |
| Delete Config Trusted IP | `deleteConfigTrustedIp` | Removes a trusted IP address or CIDR range from a config. |
| Delete Environment | `deleteEnvironment` | Permanently deletes an environment and all of its configs and secrets. |
| Delete Project | `deleteProject` | Permanently deletes a Doppler project and all of its environments, configs, and secrets. |
| Delete Secret | `deleteSecret` | Deletes a single secret from a config. |
| Delete Service Token | `deleteServiceToken` | Revokes and deletes a service token by its slug. |
| Delete Sync | `deleteSync` | Deletes an existing secret sync, optionally purging the synced data from the destination integration. |
| Delete Webhook | `deleteWebhook` | Permanently deletes a webhook. |
| Disable Webhook | `disableWebhook` | Disables a webhook without deleting it. |
| Download Secrets | `downloadSecrets` | Downloads all secrets in a config as a rendered file in the requested format (json, env, yaml, docker, etc). |
| Enable Webhook | `enableWebhook` | Enables a previously disabled webhook. |
| Get Activity Log | `getActivityLog` | Retrieves a single workplace-wide activity log entry by id. |
| Get Config | `getConfig` | Retrieves a single config (environment branch) by name within a project. |
| Get Config Log | `getConfigLog` | Retrieves a single config change log entry, including its secret-level diff. |
| Get Current Token | `getCurrentToken` | Retrieves metadata about the authentication token currently in use, including its slug, name, type, and the workplace it belongs to. Useful for verifying that a connection's credentials are valid. |
| Get Environment | `getEnvironment` | Retrieves a single environment by its slug within a project. |
| Get Integration | `getIntegration` | Retrieves a single third-party integration by its slug. |
| Get Project | `getProject` | Retrieves a single Doppler project by its unique identifier. |
| Get Secret | `getSecret` | Retrieves a single secret's raw and computed value within a config. |
| Get Sync | `getSync` | Retrieves a single secret sync by its slug. |
| Get Webhook | `getWebhook` | Retrieves a single webhook by its slug. |
| Get Workplace | `getWorkplace` | Retrieves the workplace's name and billing/security contact emails. |
| Get Workplace User | `getWorkplaceUser` | Retrieves a single workplace user by their slug. |
| List Activity Logs | `listActivityLogs` | Lists workplace-wide activity log entries, paginated. |
| List Config Logs | `listConfigLogs` | Lists the change history log entries for a specific config. |
| List Config Trusted IPs | `listConfigTrustedIps` | Lists the trusted IP addresses or CIDR ranges allowed to access a config. |
| List Configs | `listConfigs` | Lists configs (environment branches) within a project, optionally filtered to one environment. |
| List Environments | `listEnvironments` | Lists all environments belonging to a Doppler project. |
| List Integrations | `listIntegrations` | Lists the third-party integrations configured for the workplace, such as secret sync destinations. |
| List Invites | `listInvites` | Lists pending invitations to join the workplace. |
| List Projects | `listProjects` | Lists all projects in the workplace, paginated. |
| List Secret Names | `listSecretNames` | Lists just the names of the secrets in a config, without their values. |
| List Secrets | `listSecrets` | Lists all secrets and their raw/computed values within a config. |
| List Service Tokens | `listServiceTokens` | Lists the service tokens created for a config. |
| List Webhooks | `listWebhooks` | Lists the webhooks configured for a project, or all webhooks in the workplace if no project is given. |
| List Workplace Users | `listWorkplaceUsers` | Lists the users who are members of the workplace. |
| Lock Config | `lockConfig` | Locks a config, preventing it from being renamed or deleted. |
| Rename Environment | `renameEnvironment` | Renames or re-slugs an existing environment, and optionally toggles personal configs. |
| Revoke Token | `revokeToken` | Revokes a Doppler authentication token, such as a personal or service token, making it unusable for future requests. |
| Rollback Config Log | `rollbackConfigLog` | Rolls a config's secrets back to the state captured by a specific change log entry. |
| Set Config Inheritable | `setConfigInheritable` | Sets whether a config can be inherited by other configs. |
| Set Config Inherits | `setConfigInherits` | Sets the list of configs that a given config inherits secrets from. |
| Set Secrets | `setSecrets` | Creates or updates one or more secrets (key-value pairs) within a config. |
| Share Secret | `shareSecret` | Shares a single plain-text secret via a self-destructing Doppler Share link that expires after a number of views or days. |
| Unlock Config | `unlockConfig` | Unlocks a config, allowing it to be renamed or deleted again. |
| Update Config | `updateConfig` | Renames an existing branch config. |
| Update Project | `updateProject` | Updates the name and/or description of an existing Doppler project. |
| Update Secret Note | `updateSecretNote` | Sets a note on a secret, applied across all environments of the project. |
| Update Webhook | `updateWebhook` | Updates an existing webhook's URL, name, signing secret, payload, or enabled configs. |
| Update Workplace | `updateWorkplace` | Updates the workplace's name and/or billing/security contact emails. |
| Update Workplace User | `updateWorkplaceUser` | Updates a workplace user's role/access level. |
