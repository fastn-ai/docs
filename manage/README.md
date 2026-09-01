---
description: Organisation settings, access, credentials and billing.
---

# Settings

**Settings** in the MANAGE group of the left rail. Its sub-navigation holds eleven pages; Customers, which also lives under Settings in the app, is documented with [Operate](../operate/customers.md) because that is where you use it.

| Page                                    | Covers                                                        |
| --------------------------------------- | --------------------------------------------------------------- |
| [People](people.md)                     | Who is in the workspace, invitations, statuses.                |
| [Roles](roles.md)                       | What each role can do, and how to narrow one.                  |
| [General](general.md)                   | Organisation name, timezone, domain joining, deletion.         |
| [API keys](api-keys.md)                 | Programmatic access, test and live modes.                      |
| [Secrets](secrets.md)                   | Encrypted values read at runtime.                              |
| [Configs](configs.md)                   | Per-environment values read at runtime.                        |
| [Environments and GitHub](environments.md) | Deployment stages and review gates.                         |
| [Database](database.md)                 | Which Postgres your workflows read and write through.          |
| [Billing and limits](billing.md)        | Plan, credits, quotas and customer tiers.                      |
| [Audit log](audit-log.md)               | Every action taken in the organisation.                        |
| [Trash](trash.md)                       | Deleted connectors, actions and workflows.                     |

Your own account is separate from the organisation:

{% content-ref url="profile.md" %}[Your profile](profile.md){% endcontent-ref %}

### Who can reach what

| Page                     | Minimum role                            |
| ------------------------ | ----------------------------------------- |
| Audit log                | Owner or Admin — enforced at the API layer |
| Secrets, API keys        | Roles holding the matching permissions   |
| Everything else          | Per the permission matrix in [Roles](roles.md) |
