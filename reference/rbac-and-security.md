---
description: >-
  Role definitions, permission matrix, Row-Level Security policies, scope
  conditions, and auth middleware.
---

# RBAC & Security

Fastn uses role-based access control to determine what each member of your organization can do. Roles are assigned when you invite a user (see [Setting Up Your Organization](https://claude.ai/fastn/tutorials/saas-admin/setting-up-your-organization)).

### System roles

There are six system roles. Each has a fixed set of permissions across the platform's resource categories.

| Role          | Permissions | Scope                                                                                                                  |
| ------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Owner**     | 39          | Full access, including ownership transfer and organization deletion. One per organization.                             |
| **Admin**     | 39          | Full access — connectors, workflows, customers, billing, settings. Cannot transfer ownership.                          |
| **Developer** | 34          | Build connectors, workflows, and agents. No billing or organization settings.                                          |
| **Operator**  | 18          | Run workflows and monitor activity. Cannot create or modify connectors or workflows.                                   |
| **Viewer**    | 7           | Read-only access across the platform.                                                                                  |
| **End User**  | 9           | Widget-only access — connect apps, view sync status, and configure their own integrations through the embedded widget. |

> **VERIFY:** Permission counts (39/39/34/18/7/9) are from an earlier platform observation. Confirm against **Settings → ADVANCED → Roles** before publishing, as counts may change.

### Permission categories

Permissions are grouped by resource type. Each role has a different number of permissions in each category:

| Category    | Permissions |
| ----------- | ----------- |
| Connectors  | 6           |
| Connections | 6           |
| Workflows   | 7           |
| Agents      | 5           |
| Tools       | 5           |

> **VERIFY:** Confirm these category counts against the Roles page.

### Custom roles

If the system roles don't fit, you can create custom roles. Go to **Settings → ADVANCED → Roles**:

* **Create Custom Role** — Build a role from scratch, selecting individual permissions.
* **Duplicate as Custom** — Start from an existing system role and modify its permissions.

### Where roles are managed

| Task                              | Location                                                   |
| --------------------------------- | ---------------------------------------------------------- |
| Assign a role to a user           | Settings → People → Invite User (or edit an existing user) |
| View role permissions             | Settings → ADVANCED → Roles                                |
| Create or duplicate a custom role | Settings → ADVANCED → Roles                                |

### Tenancy and data isolation

Beyond user roles, Fastn isolates data between your customers. Each customer's connections, data, and sync history are isolated from one another. For how connections are scoped within a customer (shared across their organization vs per individual user), see [Tenancy](https://claude.ai/fastn/tutorials/developer/tenancy).
