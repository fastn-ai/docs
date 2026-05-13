---
description: >-
  Role definitions, permission matrix, Row-Level Security policies, scope
  conditions, and auth middleware.
---

# RBAC & Security

### System roles

6 system roles managed under **Settings → ADVANCED → Roles**:

| Role          | Permissions | Description                                                      |
| ------------- | ----------- | ---------------------------------------------------------------- |
| **Owner**     | 39          | Full access within organization and customers                    |
| **Admin**     | 39          | Full access within organization and customers                    |
| **Developer** | 34          | Build connectors, workflows, agents. No billing or org settings. |
| **Operator**  | 18          | Operational access — run workflows, monitor activity             |
| **Viewer**    | 7           | Read-only access                                                 |
| **End User**  | 9           | Customer-facing widget access                                    |

### Permission categories

5 categories with granular actions:

#### Connectors (6 actions)

create, read, update, delete, deploy test, deploy prod

#### Connections (6 actions)

create, read, update, delete, execute, share

#### Workflows (7 actions)

create, read, update, delete, execute, deploy test, deploy prod

#### Agents (5 actions)

create, read, update, delete, execute

#### Tools (5 actions)

create, read, update, delete, execute

### Permission matrix

| Category    | Owner | Admin | Developer | Operator | Viewer    | End User |
| ----------- | ----- | ----- | --------- | -------- | --------- | -------- |
| Connectors  | 6/6   | 6/6   | 6/6       | varies   | read only | —        |
| Connections | 6/6   | 6/6   | 6/6       | varies   | read only | varies   |
| Workflows   | 7/7   | 7/7   | 7/7       | varies   | read only | —        |
| Agents      | 5/5   | 5/5   | 5/5       | varies   | read only | —        |
| Tools       | 5/5   | 5/5   | 5/5       | varies   | read only | —        |

{% hint style="info" %}
⚠️ **VERIFY:** Exact permissions for Operator, Viewer, and End User roles per category. The screenshot confirms totals (18p, 7p, 9p) but not the exact distribution.
{% endhint %}

### Custom roles

* Click **"Create Custom Role"** to build a role from scratch
* Click **"Duplicate as Custom"** on any system role to copy and modify
* Custom roles have the same permission categories and actions as system roles

### People management

Managed under **Settings → People**:

| Column      | Description                         |
| ----------- | ----------------------------------- |
| USER        | Name + email                        |
| ROLE        | Role badge (Admin, Developer, etc.) |
| TEAMS       | Team assignments                    |
| STATUS      | Active (green dot), Inactive        |
| LAST ACTIVE | Last login timestamp                |

Filters: All Roles, All Status, All Teams

**"Invite User"** button sends email invitations with role assignment.

### Row-Level Security (RLS)

PostgreSQL policies enforce customer data isolation at the database level:

* Session variables `app.tenant_id` and `app.role` set per request
* Every query on customer-scoped tables automatically filters by customer ID
* No application-level filtering — enforced by the database engine

### Authentication

#### Keycloak integration

| Property     | Value           |
| ------------ | --------------- |
| Provider     | Keycloak (OIDC) |
| Realm        | `fastn`         |
| Social login | GitHub, Google  |
| Token format | JWT             |

#### Auth middleware

1. Validates JWT via JWKS endpoint
2. Extracts user context (user ID, role, customer)
3. Sets PostgreSQL session variables
4. Checks permissions
5. Applies rate limiting

### Audit Log

All permission-gated actions are logged under **Settings → Audit Log**:

| Column        | Description                                                    |
| ------------- | -------------------------------------------------------------- |
| **TIMESTAMP** | When the action occurred                                       |
| **USER**      | Who performed it (user name or "system")                       |
| **ACTION**    | What was done (e.g., `auth.login`, `credential.token_refresh`) |
| **RESOURCE**  | What was affected (resource ID + type)                         |
| **OUTCOME**   | Success (green), Failure, Denied                               |

Filters: All Users, All Actions, All Types, date range (From/To).
