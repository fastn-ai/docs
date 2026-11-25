---
description: >-
  Assign built-in roles (Owner, Admin, Developer, Operator, Viewer, End User),
  create custom roles, and manage team access.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Set up roles and permissions

Give each person on your team the access they need: assign a built-in role, or create a custom role that narrows one.

### Before you start

* The **Owner** or **Admin** role. **Settings → Roles** and **Settings → People** need one of them.

### The 6 built-in roles

fastn has 6 built-in roles. View them under **Settings → Roles** (Owners and Admins):

| Role          | Permissions | Description                                                      |
| ------------- | ----------- | ---------------------------------------------------------------- |
| **Owner**     | 44          | Can manage admins and transfer ownership.                        |
| **Admin**     | 44          | Full access within the organization and its customers.           |
| **Developer** | 36          | Builds and deploys connectors and workflows.                     |
| **Operator**  | 21          | Configures connections and runs workflows. Deploys to test only. |
| **Viewer**    | 6           | Read-only on connectors, connections, workflows, widgets, events, and the Unified API. |
| **End User**  | 35          | Uses the embed widget and creates connections.                   |

Each built-in role carries a **Built in** badge. Selecting one shows its permission matrix and the count it holds out of 44.

### Permission categories

Permissions are grouped into 11 resources, 44 in all:

| Resource            | Available actions                                               |
| ------------------- | --------------------------------------------------------------- |
| **Connectors** (5)  | create, read, update, delete, write                             |
| **Connections** (6) | create, read, update, delete, share, decrypt                    |
| **Workflows** (7)   | create, read, update, delete, execute, deploy test, deploy prod |
| **Users** (5)       | create, read, update, invite, remove                            |
| **Settings** (3)    | read, update, manage                                            |
| **Events** (5)      | create, read, update, delete, replay                            |
| **Secrets** (3)     | read, write, delete                                             |
| **Executions** (2)  | create, read                                                    |
| **Widgets** (4)     | create, read, update, delete                                    |
| **Customers** (1)   | create                                                          |
| **Unified API** (3) | read, execute, customize                                        |

Agents and tools are no longer grantable permissions. Using the AI assistant and reading the audit log are gated by role instead, and the Roles screen names them separately.

#### What each role gets

**Owner / Admin** - All 44 permissions. Full access to everything.

**Developer** - 36 permissions: every Connectors, Connections, Workflows (including deploy prod), Events, Secrets, Widgets, and Unified API permission, plus read on Users and Settings, and create on Customers. Cannot manage people, change settings, or read the audit log.

**Operator** - 21 permissions. Can create, read, and update connectors, manage connections, run workflows and deploy them to test, manage widgets, and read, update, and replay events. Cannot create new workflows or deploy to production, and has no Secrets permissions.

**Viewer** - 6 permissions. Read-only on connectors, connections, workflows, widgets, events, and the Unified API. Cannot read executions, users, settings, or secrets, and cannot run anything.

**End User** - 35 permissions. Customer-facing access through the widget. Can create and manage connections, author and run workflows, and manage users and settings inside their own customer.

### Assign roles

1. Go to **Settings → People**.
2. Find the team member in the table.
3. Click **Change role** on their row.
4. Pick the new role.

**You should see:** the new role in the person's **Role** column. The People table shows **Person**, **Role**, **Status**, **Added**, and **Access** (time-limited access, if any).

Filter by role with the chips above the table, or by status with the dropdown. To change several people at once, tick their rows and use **Change role…** in the bar that appears.

**Change role** is disabled on Owner rows (an owner's role moves through **Transfer ownership**) and on your own row.

### Create custom roles

If the built-in roles don't fit your needs, create a custom role:

1. Go to **Settings → Roles**.
2. Click **Custom role**.
3. Pick the built-in role it is **Based on**, enter a **Role Name**, and untick the permissions it should not have.
4. Click **Create Role**.

Alternatively, duplicate an existing role and modify it:

1. Click a role (for example, Developer).
2. Click **Duplicate**.
3. Adjust the permissions as needed.
4. Click **Create Role**.

A custom role can only narrow its base role: ticking a permission the base role does not hold grants nothing. Assign a custom role to a person on the People screen, or to a customer tier under Settings → Billing.

### Review the audit trail

Actions across the organization are logged:

1. Go to **Settings → Audit log** (Owners and Admins).
2. Filter by **All people**, **All actions**, **All types**, and a date range.

The columns are **Who**, **Action**, **Resource**, **Customer**, **Result**, and **When**. Actions include `auth.login`, `workflow.execute`, `connection.update`, and others. Results are **Success**, **Failed**, or **Not recorded**.

### What you've learned

* The 6 built-in roles and their permission counts
* The 11 resources permissions are grouped into
* How to assign roles to team members
* How to create custom roles or duplicate existing ones
* Audit log for tracking actions

### Next steps

* Invite people and set up the rest of your organization: [Set up your organization](setting-up-your-organization.md).
* Every permission in detail: [Roles](../../manage/roles.md).
