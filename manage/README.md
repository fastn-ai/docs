---
description: Organization settings, access, credentials and billing.
---

# Settings

**Settings** at the bottom of the left rail.

**Its menu is role-scoped, so you will not see every page below.** An Owner or Admin sees People, General, Billing, Roles and Audit log, plus everything a Developer sees: Environments, Secrets, Configs, Database, Workflow tags and Trash. API keys and the MCP server moved to **Embed → API keys and MCP**, and Your API moved to **Build → Connect your product**.

The table follows the Settings menu order: People, General, Billing, Roles, Audit log, Environments, Secrets, Configs, Database, Workflow tags, Trash.

| Page                                    | Covers                                                        |
| --------------------------------------- | --------------------------------------------------------------- |
| [People](people.md)                     | Who is in the organization, invitations, statuses.             |
| [General](general.md)                   | Organization name, timezone, joining by email domain.          |
| [Billing and limits](billing.md)        | Plan, credits and limits.                                      |
| [Roles](roles.md)                       | What each role can do, and how to narrow one.                  |
| [Audit log](audit-log.md)               | Every action taken in the organization.                        |
| [Environments and GitHub](environments.md) | Deployment stages and review gates.                         |
| [Secrets](secrets.md)                   | Encrypted values read at runtime.                              |
| [Configs](configs.md)                   | Per-environment values read at runtime.                        |
| [Database](database.md)                 | Which Postgres your workflows read and write through.          |
| [Workflow tags](workflow-tags.md)       | The labels and categories workflows are filtered and grouped by. |
| [Trash](trash.md)                       | Deleted connectors, actions and workflows.                     |

Some pages that used to be here have moved into the sidebar: **API keys and MCP** is under **Embed** ([API keys and MCP](api-keys.md)), **Connect your product** is under **Build** ([Connect your product](saas-connectors.md)), and **Customers** is under **Operate** ([Customers](../operate/customers.md)). Their old Settings addresses redirect.

Your own account is separate from the organization:

{% content-ref url="profile.md" %}[Your profile](profile.md){% endcontent-ref %}

### Who can reach what

The Settings menu itself changes by role, so the first answer to "why can't I see that page" is usually the role you are signed in as.

| Page                     | Who reaches it                                                        |
| ------------------------ | ----------------------------------------------------------------------- |
| People, General, Billing, Roles, Audit log | Owner and Admin. Absent from a Developer's menu. The audit log is also enforced by role at the API layer on `/api/v1/audit-log`. |
| Environments, Secrets, Configs, Database, Trash | Owner, Admin and Developer.                    |
| Workflow tags            | Developer or above.                                                    |
| API keys and MCP         | Not in Settings: under **Embed**. See [API keys and MCP](api-keys.md). |
| Everything else          | Per the permission matrix in [Roles](roles.md).                        |
