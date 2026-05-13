---
description: >-
  Configure your organization profile, environments, API keys, and project
  settings after your first Fastn login.
---

# Setting Up Your Organization

**Prerequisites:** Complete [Signing Up as a SaaS Partner](https://app.gitbook.com/o/d4yvP9A8wMsLuRwerHPU/s/3iSr2Tx8FvvuoLPncziH/~/edit/~/changes/517/fastn-v2/getting-started/signing-up-as-a-saas-partner) first.

### Step 1: Configure organization settings

1. Click **Settings** in the top nav.
2. Click **General** in the left sidebar.

Here you can configure:

* **Organization Name** — how your company appears in the platform
* **Timezone** — used for scheduled triggers and activity timestamps
* **Domain & Access Control** — set your email domain (e.g., `yourcompany.com`) so team members signing up with that domain can request to join. Toggle **"Auto-approve domain users"** to skip manual approval.

> **Screenshot needed:** Settings → General showing Organization Name, Timezone, and Domain & Access Control sections.

### Step 2: Create API keys

API keys authenticate programmatic requests. Fastn has two types:

| Type     | Purpose                                           |
| -------- | ------------------------------------------------- |
| **Test** | Development and testing — safe to experiment with |
| **Live** | Production use — real customer data               |

1. Go to **Settings → API Keys**.
2. Click **"+ Create API Key"**.
3. Select **Test** or **Live**.
4. Name the key descriptively (e.g., `dev-key`, `production-key`).
5. Copy the key immediately — it won't be shown again.

> **📷 Screenshot needed:** Settings → API Keys showing the Test/Live toggle and a newly created key.

{% hint style="info" %}
⚠️ **Security:** Treat API keys like passwords. Don't commit them to Git repositories. Use environment variables or secrets in your application code.
{% endhint %}

### Step 3: Set up secrets

Secrets store sensitive values — third-party API tokens, database credentials — that your workflows read at runtime. Unlike API keys (which authenticate to Fastn), secrets are values your workflow code uses internally.

1. Go to **Settings → Secrets**.
2. Click **"Create your first secret"** (or **"Add Secret"** if you already have some).
3. Enter a key name (e.g., `SHOPIFY_API_TOKEN`) and the value.
4. Click **Save**.

In your workflow code, access secrets through the context object.

> **Screenshot needed:** Settings → Secrets showing the secret creation form.

### Step 4: Create environments

Environments separate development from production. Each environment can have its own connections, secrets, and configuration.

1. Go to **Settings → Environments**.
2. Click **"Create your first environment"**.
3. Name it (e.g., `staging`, `production`).

When you deploy workflows, you target a specific environment.

> **Screenshot needed:** Settings → Environments showing the environment creation flow.

### Step 5: Review OAuth Apps

Fastn manages OAuth apps on your behalf for common platforms. This means you can authenticate connectors for supported platforms without creating your own OAuth application in the third-party's developer portal.

1. Go to **Settings → OAuth Apps**.
2. You'll see the list of platforms Fastn manages OAuth for.

If your connector's platform isn't listed, you'll need to create your own OAuth app in the third-party's developer settings and configure it in your connector.

> **Screenshot needed:** Settings → OAuth Apps showing the managed OAuth apps list.

### Step 6: Invite your team

1. Go to **Settings → People**.
2. Click **"Invite User"**.
3. Enter their email address.
4. Select a role:

| Role          | Permissions | What they can do                                                   |
| ------------- | ----------- | ------------------------------------------------------------------ |
| **Admin**     | 39          | Full access — connectors, workflows, customers, billing, settings  |
| **Developer** | 34          | Build — connectors, workflows, agents. No billing or org settings. |
| **Operator**  | 18          | Operate — run workflows, monitor activity                          |
| **Viewer**    | 7           | Read-only access across the platform                               |

5. Click send. They'll receive an email to join.

The People page shows a table with columns: USER, ROLE, TEAMS, STATUS, LAST ACTIVE. Filter by role, status, or team.

> **Screenshot needed:** Settings → People showing the user table with the Invite User button.

> **GIF needed:** Invite flow — clicking Invite User, entering email, selecting role, sending.

### Step 7: Check your plan and quotas

1. Go to **Settings → Billing**.
2. **Current Plan** shows your tier (Free $0/mo for new accounts).
3. **Quota Usage** table shows each dimension with:
   * Plan default
   * Current usage (progress bar)
   * % used
   * Enforcement mode (Hard Block)
   * Source (Plan)

Key limits on the Free plan:

| Dimension            | Default | Enforcement |
| -------------------- | ------- | ----------- |
| Events per day       | 500     | Hard Block  |
| Events per minute    | 10      | Hard Block  |
| API calls per day    | 1,000   | Hard Block  |
| API calls per minute | 20      | Hard Block  |

Click **"Customize Customer Limits"** to set per-customer quota overrides.

> **Screenshot needed:** Settings → Billing showing the plan card and quota usage table.

### What you've configured

* Organization name, timezone, and domain access control
* Test and Live API keys
* Secrets for sensitive workflow values
* Environments for deployment separation
* Reviewed Fastn-managed OAuth apps
* Team members invited with appropriate roles
* Plan limits reviewed
