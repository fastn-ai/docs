---
description: >-
  Configure your organization profile, environments, API keys, and project
  settings after your first Fastn login.
---

# Setting Up Your Organization

After the Setup Assistant configures your core integrations, workflows, and widget, there are a handful of organization-level settings that allows you to control your company profile, team access, customer management, and billing. This tutorial walks through each one.

### Step 1: Configure organization settings

1. Click **Settings** in the top nav.
2. Click **General** in the left sidebar.

Here you can configure:

**Organization Name** — How your company appears across the platform.

**Timezone** — Used for scheduled triggers and activity timestamps.

**Domain & Access Control** — Set your email domain (e.g., `yourcompany.com`) so team members signing up with that domain can request to join. Toggle **"Auto-approve domain users"** to skip manual approval for teammates with matching email domains.

#### Company Research Report

During onboarding, the Setup Assistant's AI researched your company automatically and analyzed your existing integrations, customer ecosystem, competitive landscape, and integration gaps. The results are saved here.

Scroll down on the General page to find the **Company Research Report** card.

This report is what informed the AI's connector recommendations and workflow suggestions during onboarding. Revisit it when planning new integrations or evaluating which connectors to prioritize next.

> **Screenshot:** Settings → General showing Organization Name, Timezone, Domain & Access Control, and the Company Research Report card with the "View research report" button.

#### Reset Onboarding

At the bottom of the General page: **Reset Onboarding**. This reruns the Setup Assistant from scratch.

{% hint style="danger" %}
&#x20;This is irreversible. It deletes your qualification wizard answers and every Setup Assistant thread. Only use this for testing or if you need to completely restart your onboarding configuration.
{% endhint %}

### Step 2: Review OAuth Apps

The Setup Assistant may have already configured OAuth for your connectors during onboarding  when the AI set up inline auth, those configurations were saved here.

1. Go to **Settings → OAuth Apps**.
2. You'll see the list of platforms Fastn manages OAuth for.

Fastn manages OAuth apps on your behalf for common platforms, meaning you can authenticate connectors without creating your own OAuth application in the third-party's developer portal. If your connector's platform isn't listed, your development team will need to create an OAuth app in the third-party's developer settings and configure it here.

> **Screenshot needed:** Settings → OAuth Apps showing the managed OAuth apps list with platform icons and status indicators.

### Step 3: Invite your team

1. Go to **Settings → People**.
2. Click **"Invite User"**.
3. Enter their email address.
4. Select a role.
5. Click send andhey'll receive an email to join.

The People page shows a table with columns: **USER, ROLE, TEAMS, STATUS, LAST ACTIVE**. Filter by role, status, or team.

#### Roles

Fastn has six system roles. Each role has a fixed set of permissions across Connectors, Connections, Workflows, Agents, and Tools:

| Role          | Permissions | What they can do                                                                                                      |
| ------------- | ----------- | --------------------------------------------------------------------------------------------------------------------- |
| **Owner**     | 39          | Full access to everything an Admin can do, plus ownership transfer and organization deletion. One per organization.   |
| **Admin**     | 39          | Full access to connectors, workflows, customers, billing, settings. Cannot transfer ownership.                        |
| **Developer** | 34          | Allows a user to build connectors, workflows, agents. No billing or organization settings.                            |
| **Operator**  | 18          | Can run workflows, monitor activity. Cannot create or modify connectors or workflows.                                 |
| **Viewer**    | 7           | Read-only access across the platform.                                                                                 |
| **End User**  | 9           | Widget-only access. Can connect apps, view sync status, configure their own integrations through the embedded widget. |

To see the full permission breakdown or create custom roles: go to **Settings → ADVANCED → Roles**. Each system role can be duplicated as a custom role and modified. Click **"Create Custom Role"** to build one from scratch.

> **Screenshot needed:** Settings → People showing the user table with the Invite User button and role/status columns.

### Step 4: Manage customers

Your customers (the end users of your SaaS product who use the integrations) are managed under:

1. Go to **Settings → Customers**.
2. The page reads: "Manage customers under your account."

Each customer gets their own isolated environment i.e. their own connections, data, sync history, and configuration. When a customer connects an app through the embedded widget, they appear here automatically.

From this page you can view customer details, monitor their integration status, and set per-customer quota overrides.

> **Screenshot needed:** Settings → Customers page showing the customer list (or empty state for new accounts).

### Step 5: Check your plan and quotas

1. Go to **Settings → Billing**.
2. **Current Plan** shows your tier.
3. **Quota Usage** table shows each dimension with:
   * Plan default
   * Current usage (progress bar)
   * % used
   * Enforcement mode
   * Source

Key limits on the Free plan:

| Dimension            | Default | Enforcement |
| -------------------- | ------- | ----------- |
| Events per day       | 500     | Hard Block  |
| Events per minute    | 10      | Hard Block  |
| API calls per day    | 1,000   | Hard Block  |
| API calls per minute | 20      | Hard Block  |

Click **"Customize Customer Limits"** to set per-customer quota overrides which is useful when specific customers need higher limits than your plan default, or when you want to throttle individual customers to protect shared capacity.

> **Screenshot needed:** Settings → Billing showing the plan card and quota usage table with progress bars.

### Step 6: Review the Audit Log

1. Go to **Settings → Audit Log**.
2. The log shows a table with columns: **TIMESTAMP, USER, ACTION, RESOURCE, OUTCOME**.

Every significant action in your organization is recorded here from user logins, workflow deployments, connector changes to customer connections. Use it for compliance, debugging, or understanding who changed what.

> **Screenshot needed:** Settings → Audit Log showing a few example entries with timestamps and actions.

### For your development team

The Settings section also includes pages your developers will need:

* **API Keys** — Test and Live keys for programmatic access to the Fastn API
* **Secrets** — Sensitive values (third-party tokens, database credentials) that workflows read at runtime
* **Environments** — Separate configurations for development, staging, and production deployments

See more details in the [Developer](../developer/) tutorials for the full setup guide.

### What you've configured

* Organization name, timezone, and domain access control
* Reviewed the Company Research Report from onboarding
* Reviewed Fastn-managed OAuth apps
* Team members invited with appropriate roles
* Customer management set up
* Plan limits and quota enforcement reviewed
* Audit log available for compliance and debugging
* Developer team pointed to API Keys, Secrets, and Environments setup
