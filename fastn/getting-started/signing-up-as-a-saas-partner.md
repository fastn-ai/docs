---
description: A guide on how to use Fastn if you're a SaaS
---

# Signing Up as a SaaS Partner

Fastn is built for SaaS companies. The signup process includes a validation step to confirm you're a legitimate software business.

### Before you sign up

You'll need:

* **A business email address** — Personal email providers (Gmail, Yahoo, Outlook, etc.) are blocked.
* **A SaaS product** — Fastn validates that your company builds and sells software.
* **A use case in mind** — Know which integrations your customers need.

### What happens during signup

1. **Email validation** — Domain checked against a blocklist of \~40 personal email providers.
2. **Duplicate check** — If your domain is already registered, you'll be directed to join the existing organization.
3. **Company classification** — AI classifier analyzes your company based on public information.
4. **Outcome** — Approved (immediate), Provisional (limited access, pending review), Manual review, or Rejected.

Most SaaS companies with a live product get approved within minutes.

### What you get after signup

#### Dashboard access

Log in at [live.fastn.ai](https://live.fastn.ai/). The dashboard has four top-level sections: **Home**, **Integrations**, **Activity**, and **Settings**.

Your first experience is the **Setup Assistants** on the Home page — a 5-step AI-guided onboarding that researches your company, recommends connectors, and walks you through building your first integration.

> **Screenshot:** Home page after first login showing the Setup Assistants with step 1 (Research) active.

#### Organization settings

Go to **Settings → General** to configure:

* **Organization Name** — how your company appears in the platform
* **Timezone** — used for scheduled triggers and activity timestamps
* **Domain & Access Control** — set your email domain so team members can request to join. Toggle "Auto-approve domain users" to skip manual approval.

> **Screenshot:** Settings → General showing Organization Name, Timezone, and Domain & Access Control sections.

#### API Keys

Go to **Settings → API Keys** to create keys for programmatic access:

* **Test** keys — for development and testing
* **Live** keys — for production

Click **"+ Create API Key"** and select Test or Live. Copy the key immediately — it won't be shown again.

> **Screenshot:** Settings → API Keys showing the Test/Live toggle and Create API Key button.

#### Free plan

New accounts start on the **Free** plan ($0/mo):

* 500 events per day
* 10 events per minute
* 1,000 API calls per day
* 20 API calls per minute

View your quota usage and upgrade from **Settings → Billing**.

### Inviting team members

1. Go to **Settings → People**.
2. Click **"Invite User"**.
3. Enter their email address.
4. Select a role:

| Role          | Permissions | What they can do                                                          |
| ------------- | ----------- | ------------------------------------------------------------------------- |
| **Admin**     | 39          | Full access — connectors, workflows, customers, billing, settings         |
| **Developer** | 34          | Build access — connectors, workflows, agents. No billing or org settings. |
| **Operator**  | 18          | Operational access — run workflows, monitor activity                      |
| **Viewer**    | 7           | Read-only access                                                          |

5. Click send. They'll receive an email to join your organization.

Users are listed in a table with columns: USER, ROLE, TEAMS, STATUS, LAST ACTIVE.

> **Screenshot:** Settings → People showing the user table and Invite User button.

> **GIF:** Full invite flow — clicking Invite User, entering email, selecting role, sending.

### First steps after signup

The Setup Assistants on the Home page guide you through this automatically, but here's the manual order:

1. **Create your first connector** — Go to **Integrations → Connectors** → **+ Create** or **Build with AI**
2. **Build a workflow** — Go to **Integrations → Workflows** → **Create Workflow** or **Build with AI**
3. **Set up a trigger** — Go to **Integrations → Triggers** → **Add Trigger** (Webhook, Scheduler, or App Event)
4. **Create a customer** — Go to **Settings → Customers** → **Create Customer**
5. **Monitor** — Go to **Activity → Executions** to see your workflow runs

Each of these steps has detailed documentation in the [Tutorials](https://claude.ai/tutorials/tutorials.md) section.
