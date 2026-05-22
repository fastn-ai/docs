---
description: A guide on how to use Fastn if you're a SaaS company
---

# Signing Up as a SaaS Partner

Fastn is built for SaaS companies. The signup process includes a validation step to confirm you're a legitimate software business.

### Before you sign up

You'll need:

* **A business email address** — Personal email providers (Gmail, Yahoo, Outlook, etc.) are blocked.
* **A SaaS product** — Fastn validates that your company builds and sells software. Preferably just the URL to your SaaS product.
* **A use case in mind** — Know which integrations your customers need.

{% hint style="info" %}
Alternatively Fastn can suggest usecases based on the research it will do according to what your company is focused on and what customers say about your product.
{% endhint %}

### What happens during signup

1. **Email validation** — Domain checked against a blocklist of \~40 personal email providers.
2. **Duplicate check** — If your domain is already registered, you'll be directed to join the existing organization.
3. **Company classification** — AI classifier analyzes your company based on public information.
4. **Outcome** — Approved (immediate), Provisional (limited access, pending review), Manual review, or Rejected.

Most SaaS companies with a live product get approved within minutes.

### What you get after signup

#### Dashboard access

Log in at [live.fastn.ai](https://live.fastn.ai). The dashboard has five top-level sections: **Home**, **Integrations**, **Widgets**, **Activity**, and **Settings**.

#### The onboarding experience

Your first experience is the **Setup Assistant** on the Home page which is a 5-step AI-guided pipeline that takes you from zero to a working integration platform:

| Name           | What it does                                                                                                                                                                              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Use cases**  | AI researches your company, analyzes your customers' integration needs, compares your integration gap vs peers (Workato, Zapier, Tray.ai), identifies manual workflows your customers run |
| **Connectors** | Set up the integration building blocks your platform offers. Connectors are set up once and reused everywhere.                                                                            |
| **Workflows**  | Build the integration logic your customers will configure. AI agents create the workflows for you.                                                                                        |
| **Embed**      | Configure the customer-facing experience inside your product — the widget hub.                                                                                                            |
| **Live**       | Your platform is ready for customers.                                                                                                                                                     |

The right sidebar shows **YOUR SETUP** progress (0/5 → 5/5) with a description for each step.

Each step has a **"Skip to next phase"** button if you want to move ahead without completing the current step.

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

#### Credits

The top-right of the dashboard shows your **credits counter**. Credits track AI agent usage across the platform.

New accounts start on the **Free** plan which includes but may be subjected to changes:

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

| Role          | Permissions | What they can do                                                                         |
| ------------- | ----------- | ---------------------------------------------------------------------------------------- |
| **Admin**     | 39          | Full access which includes access to connectors, workflows, customers, billing, settings |
| **Developer** | 34          | Build access i.e. connectors, workflows, agents. No billing or org settings.             |
| **Operator**  | 18          | Operational access which allows the user to run workflows and monitor activity           |
| **Viewer**    | 7           | Only includes read-only access                                                           |

5. Click send. They'll receive an email to join your organization.

Users are listed in a table with columns: USER, ROLE, TEAMS, STATUS, LAST ACTIVE.

> **Screenshot:** Settings → People showing the user table and Invite User button.

> **GIF:** Full invite flow — clicking Invite User, entering email, selecting role, sending.

### First steps after signup

The Setup Assistant handles all of this automatically through the 5-step pipeline. But if you prefer to work manually or want to explore on your own, then following are the steps you can follow in order:

1. **Describe your use case** — On the Home page, tell the AI what integrations your customers need
2. **Build connectors** — Go to **Integrations → Connectors** → **Build with AI** (recommended) or **+ Create** (manual)
3. **Build workflows** — Go to **Integrations → Workflows** → **Build with AI** (recommended) or **Create Workflow** (manual code editor)
4. **Set up triggers** — Go to **Integrations → Triggers** → **Add Trigger** (Webhook, Scheduler, or App Event)
5. **Build the widget** — Go to **Widgets** to configure the customer-facing integration hub
6. **Create a customer** — Go to **Settings → Customers** → **Create Customer**
7. **Monitor** — Go to **Activity → Executions** to see your workflow runs

{% hint style="info" %}
If you're a new user, the recommended path is the Setup Assistant pipeline. It uses Fastn's AI Agents to research your company, recommend connectors, build workflows, and get you to production faster than manual setup.
{% endhint %}
