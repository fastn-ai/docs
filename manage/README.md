---
description: Organisation settings, access, credentials and billing.
---

# Settings

**Settings** in the MANAGE group of the left rail.

**Its sub-navigation is role-scoped — you will not see every page below.** An Owner or Admin sees People, General, API keys, Secrets, Environments, Configs, Database, SaaS Connectors, Billing, Roles, Audit log and Trash; a Developer sees API keys, Secrets, Environments, Configs, Database and Trash. The pages a Developer does not get are the administrative ones — People, General, Billing, Roles and the Audit log; Trash shows for everyone.

The table follows the Owner sidebar order, with Trash last.

| Page                                    | Covers                                                        |
| --------------------------------------- | --------------------------------------------------------------- |
| [People](people.md)                     | Who is in the workspace, invitations, statuses.                |
| [General](general.md)                   | Organisation name, timezone, joining by email domain.          |
| [API keys](api-keys.md)                 | Programmatic access, test and live modes.                      |
| [Secrets](secrets.md)                   | Encrypted values read at runtime.                              |
| [Environments and GitHub](environments.md) | Deployment stages and review gates.                         |
| [Configs](configs.md)                   | Per-environment values read at runtime.                        |
| [Database](database.md)                 | Which Postgres your workflows read and write through.          |
| [SaaS Connectors](saas-connectors.md)   | Your own SaaS API, and the scopes tenants connect under.       |
| [Billing and limits](billing.md)        | Plan, credits and limits.                                      |
| [Roles](roles.md)                       | What each role can do, and how to narrow one.                  |
| [Audit log](audit-log.md)               | Every action taken in the organisation.                        |
| [Trash](trash.md)                       | Deleted connectors, actions and workflows.                     |

**Customers** is not here — it is a top-level item in the OPERATE group, and is documented with [Operate](../operate/customers.md).

Your own account is separate from the organisation:

{% content-ref url="profile.md" %}[Your profile](profile.md){% endcontent-ref %}

### Who can reach what

The sidebar itself changes by role, so the first answer to "why can't I see that page" is usually the role you are signed in as.

| Page                     | Who reaches it                                                        |
| ------------------------ | ----------------------------------------------------------------------- |
| Audit log                | Owner or Admin — gated by role, enforced at the API layer on `/api/v1/audit-log` |
| People, General, Billing, Roles | In the Owner and Admin sidebar; absent from a Developer's.      |
| Secrets                  | The `Secrets` permissions — `read`, `write`, `delete`.                  |
| API keys, Environments, Configs, Database | In both the Owner/Admin and Developer sidebars.       |
| Trash                    | In the Owner, Admin and Developer sidebars, at `/settings/trash`.       |
| Everything else          | Per the permission matrix in [Roles](roles.md).                        |
