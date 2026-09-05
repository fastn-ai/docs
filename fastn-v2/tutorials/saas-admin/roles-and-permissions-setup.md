---
description: >-
  Assign system roles (Owner, Admin, Developer, Operator, Viewer, End User),
  create custom roles, and manage team access.
---

# Roles & Permissions Setup

### The 6 system roles

Fastn has 6 system roles. View them under **Settings → ADVANCED → Roles**:

| Role          | Permissions | Description                                                      |
| ------------- | ----------- | ---------------------------------------------------------------- |
| **Owner**     | 39          | Full access within organization and customers                    |
| **Admin**     | 39          | Full access within organization and customers                    |
| **Developer** | 34          | Build connectors, workflows, agents. No billing or org settings. |
| **Operator**  | 18          | Operational access — run workflows, monitor activity             |
| **Viewer**    | 7           | Read-only access                                                 |
| **End User**  | 9           | Customer-facing widget access                                    |

> **Screenshot:** Settings → ADVANCED → Roles showing the 6 system roles with permission counts.

### Permission categories

Each role has granular permissions across 5 categories:

| Category            | Available actions                                               |
| ------------------- | --------------------------------------------------------------- |
| **Connectors** (6)  | create, read, update, delete, deploy test, deploy prod          |
| **Connections** (6) | create, read, update, delete, execute, share                    |
| **Workflows** (7)   | create, read, update, delete, execute, deploy test, deploy prod |
| **Agents** (5)      | create, read, update, delete, execute                           |
| **Tools** (5)       | create, read, update, delete, execute                           |

#### What each role gets

**Owner / Admin** — All 39 permissions. Full access to everything.

**Developer** — 34 permissions. Can build and deploy connectors, workflows, and agents. Cannot manage billing, organization settings, or user roles.

**Operator** — 18 permissions. Can run workflows, monitor executions, and manage connections. Cannot create new connectors or workflows.

**Viewer** — 7 permissions. Read-only across all categories. Can view connectors, workflows, and executions but cannot modify or run anything.

**End User** — 9 permissions. Customer-facing access through the widget. Can use connections and view their own data.

> **Screenshot:** Role detail view for "Admin" showing the permission categories with checkboxes — Connectors 6/6, Connections 6/6, Workflows 7/7, Agents 5/5, Tools 5/5.

### Assigning roles

1. Go to **Settings → People**.
2. Find the team member in the user table.
3. Click the three-dot menu (⋮) on their row.
4. Select their role from the options.

The People table shows: USER, ROLE (badge), TEAMS, STATUS, LAST ACTIVE.

Filter by role, status, or team using the dropdown filters at the top.

> **Screenshot:** Settings → People showing the role badge on a user and the filter dropdowns.

### Creating custom roles

If the system roles don't fit your needs, create a custom role:

1. Go to **Settings → ADVANCED → Roles**.
2. Click **"Create Custom Role"**.
3. Name the role and select which permissions to grant.
4. Save.

Alternatively, duplicate an existing system role and modify it:

1. Click on a system role (e.g., Developer).
2. Click **"Duplicate as Custom"**.
3. Adjust the permissions as needed.
4. Save.

> **Screenshot:** Create Custom Role form or the "Duplicate as Custom" button on a system role.

### Teams

The People section supports **Teams i.e.** groups of users that can be assigned collectively. The user table has a TEAMS column and the filter bar includes an "All Teams" dropdown.

### Audit trail

Every permission-gated action is logged:

1. Go to **Settings → Audit Log**.
2. Filter by: All Users, All Actions, All Types, date range.
3. Columns: **Timestamp, User, Action, Resource, Outcome**.
4. Actions include: `auth.login`, `credential.token_refresh`, and others.
5. Outcomes: **Success** (green badge), **Failure**, **Denied**.

> **Screenshot:** Audit Log showing entries with timestamp, user, action, resource, and outcome columns.

### What you've learned

* The 6 system roles and their permission levels
* 5 permission categories with granular actions
* How to assign roles to team members
* How to create custom roles or duplicate system roles
* Teams support for group management
* Audit log for tracking all actions
