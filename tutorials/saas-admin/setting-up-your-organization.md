---
description: >-
  Configure your organization profile, team access, customers, plan limits, and
  audit log after your first fastn login.
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

# Set up your organization

Onboarding (at `/onboarding`) sets up your product, your integrations, and the widget; see [Set up fastn](../../getting-started/onboarding/README.md). Alongside it, a handful of organization-level settings control your company profile, team access, customer management, and billing. Set each one up once, after your first sign-in.

### Before you start

* A fastn account with the **Owner** or **Admin** role. **General**, **People**, **Billing**, **Roles**, and **Audit log** in Settings need Admin or higher.

### Step 1: Configure organization settings

1. Click **Settings**, the last item in the left sidebar.
2. Click **General**.

The **Organization** card holds:

**Name** - How your company appears across the platform.

**Timezone** - Sets the default timezone for new schedules. Dates elsewhere are shown in each viewer's own timezone.

The **Joining by email domain** card lets people sign up and ask to join instead of waiting for an invite:

* **Email domain** - Your company's domain (for example `yourcompany.com`). It has to be a domain your organization controls, not a mailbox provider.
* **Approve automatically** - Off means an admin has to approve each request. Leave it off unless the domain is yours alone.
* **Role people joining on this domain get** - The starting role for people who join through the domain. It also preselects the role when you invite someone on that domain.

### Step 2: Invite your team

1. Go to **Settings → People**.
2. Click **Invite someone**.
3. Enter their email address.
4. Select a role.
5. Send the invite. They receive an email to join.

**You should see:** the person in the **People** table, which has the columns **Person**, **Role**, **Status**, **Added**, and **Access** (Access shows when a time-limited grant ends).

#### Roles

fastn has these built-in roles. **Settings → Roles** counts each role's permissions across 11 resources (Connectors, Connections, Workflows, Users, Settings, Events, Secrets, Executions, Widgets, Customers, and Unified API), 44 permissions in all:

| Role          | Permissions | What they can do                                                                                                      |
| ------------- | ----------- | --------------------------------------------------------------------------------------------------------------------- |
| **Owner**     | 44          | Everything an Admin can do, plus managing admins and transferring ownership. One per organization.                    |
| **Admin**     | 44          | Full access within the organization and its customers: connectors, workflows, customers, billing, and settings.          |
| **Developer** | 36          | Builds and deploys connectors and workflows, and can use the fastn agent (paid plans). No billing, people management, or audit log.                     |
| **Operator**  | 21          | Configures connections and runs workflows. Deploys to test only.                                                      |
| **Viewer**    | 6           | Read-only access to connectors, connections, workflows, widgets, events, and the Unified API. Not executions, users, settings, or secrets, and no AI assistant. |
| **End User**  | 35          | The role for people at your customers using the embedded widget: create connections and use the widget's assistant inside their own customer. |

To see the full permission breakdown or build your own role, go to **Settings → Roles** and click **Custom role**. A custom role is based on a built-in role and can't go beyond it.

### Step 3: Manage customers

Your customers are the companies using your product, who turn on integrations in your widget.

1. Go to **Operate → Customers**.

**You should see:** the page description "Every customer using your embedded integrations. Your widget is what they see; this is where you watch each one's installs and connections."

Each customer is isolated: its own connections, data, sync history, and configuration. Your backend registers each customer, and its connections show up once it connects an app in the widget.

From this page you can view customer details and monitor their integrations. Per-customer limit overrides are set from Billing (Step 4).

### Step 4: Check your plan and limits

1. Go to **Settings → Billing**.

**You should see:** your plan at the top, with its name and price and **See plans** (on Launch) or **Request plan change**. The **Limits** card lists each limit with its name, a usage bar, used against the cap, and the percentage used. For most limits, going over stops new work rather than charging you, and nothing already running is interrupted. The exception is customer connections on Scale: past the 10 included, each extra one is billed rather than refused.

Key limits on the **Launch** plan:

| Limit                                           | Default on Launch |
| ----------------------------------------------- | ----------------- |
| Events per day                                  | 500               |
| API calls per day                               | 1,000             |
| API requests per minute (a rate limit per organization, not shown on the Limits card) | 100 |

There is no events-per-minute cap on Launch unless an admin sets one.

Click **Customize customer limits** on the Limits card to set per-customer overrides. Overrides win over the plan default, which is useful when specific customers need higher limits, or when you want to throttle individual customers to protect shared capacity.

### Step 5: Review the audit log

1. Go to **Settings → Audit log**.

**You should see:** a table with the columns **Who**, **Action**, **Resource**, **Customer**, **Result**, and **When**.

Significant actions in your organization are recorded here, from workflow deployments and connector changes to customer connections. Use it for compliance, debugging, or understanding who changed what. The audit log is for Owners and Admins.

### For your development team

Your developers use these pages:

* **API keys** - Under **Embed → API keys**: Test and Live keys for programmatic access to the fastn API, including the key your backend uses to mint embed tokens.
* **Secrets** - Under **Settings → Secrets**: sensitive values (third-party tokens, database credentials) that workflows read at runtime.
* **Environments** - Under **Settings → Environments**: where published workflow versions are deployed, such as test, live, and your own named ones.
* **Your own OAuth apps** - fastn manages OAuth apps for many common platforms. To use your own OAuth application for a connector instead, set it on that connector's **Auth** tab.

See the [Developer tutorials](../developer/README.md) for the full setup guide.

### What you've configured

* Organization name, timezone, and joining by email domain
* Team members invited with appropriate roles
* Customer management set up
* Plan limits reviewed, with per-customer overrides where needed
* Audit log available for compliance and debugging
* Developer team pointed to API keys, Secrets, Environments, and connector auth

### Next steps

* [Set up roles and permissions](roles-and-permissions-setup.md) to give each person the access they need.
* [Manage customers](managing-customers.md) to register customers and set their tiers.
* Hand the [Embedding quickstart](../developer/embedding-quickstart.md) to your developers.
