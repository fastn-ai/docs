---
description: A guide on how to use Fastn if you're a SaaS company.
---

# Signing Up as a SaaS Partner

Fastn is the embedded integration layer for SaaS companies whether you're building a product or an AI agent. It sits inside your product so your customers configure their own integrations, without engineering tickets or implementation projects. Your team manages the platform; your customers self-serve.

You can sign up with a business email, Fastn validates your company, and the Setup Assistant walks you through configuring your integration platform.

### Before you sign up

You'll need:

* **A business email address** — Personal email providers (Gmail, Yahoo, Outlook, etc.) are blocked. Use your company email.
* **Your SaaS product URL** — Fastn's AI will research your company using this to understand your product, customers, and integration needs.

From here on, the Setup Assistant handles integration discovery and configuration during onboarding.

### Signing up

1. Go to [live.fastn.ai](https://live.fastn.ai/).
2. Enter your business email address and company details.
3. Fastn validates your company in the background — it checks that you're a legitimate SaaS business using publicly available information about your domain and product.
4. Once validated, you land in the dashboard and the Setup Assistant starts immediately.

The process takes a few minutes. If your domain is already registered with Fastn, you'll be directed to join the existing organization rather than creating a new one.

> **Screenshot needed:** The signup form at live.fastn.ai showing the email and company fields.

### What you see after signup

After approval, you log into the dashboard at [live.fastn.ai](https://live.fastn.ai/). Your first experience is the **Setup Assistant** on the Home page which is a 5-step AI-guided pipeline that configures your integration platform.&#x20;

> &#x20;**Screenshot needed:** Home page after first login showing the Setup Assistant with Step 1 active and the YOUR SETUP sidebar showing 0/5 progress.

### The Setup Assistant

The Setup Assistant walks you through each stage of configuring your integration platform. Each step uses AI agents to research, recommend, and build you provide direction and approve the results.

#### Step 1: Use cases

The AI researches your company automatically. It doesn't just ask you what you need — it analyzes publicly available data across ten categories:

* Company profile
* Existing integrations
* Customer reviews
* Community feedback
* Competitive landscape
* Customer ecosystem
* Business opportunities
* Customer discovery
* Integration gaps
* News & social

The AI produces a competitor comparison table showing how your integration offering compares to platforms like Workato, Zapier, and Tray.ai. It then asks: **"Which of these pain points are real for your customers?"** with checkboxes for each identified gap.

Click **"View detailed report →"** to see the full research. This report is saved to your account and available later under **Settings → General → Company Research Report**.

Click **"Skip to next phase"** if you want to move ahead.

> **Screenshot needed:** Step 1 showing the AI research results with competitor comparison table and pain point checkboxes.

> **Screenshot needed:** The "View detailed report" expanded view showing the full company research.

#### Step 2: Connectors

Based on the research, the AI recommends connectors prioritized by impact on your customers. For example:

1. HubSpot (highest impact)
2. Salesforce
3. Google Sheets
4. Nice-to-have: Notion

The AI asks: **"Which would you like to build first?"** with selectable options. You can also choose **"Skip — go straight to widget"** or **"Something else"** to describe a connector not on the list.

> **Screenshot needed:** Step 2 showing the AI's prioritized connector recommendations with selectable options.

#### Step 3: Workflows

This is where the AI builds your integration logic. The right sidebar shows sub-steps: ✓ Building partner connectors → ◎ Planning the integration → ○ Building workflows.

**Connector setup happens inline.** If your own app needs a connector (which it usually does), the AI flags this: "Your app needs its own connector before I can plan the integration." Auth forms appear right in the chat:

* **API Key auth** — A tabbed form with fields for the key and configuration.
* **OAuth** — A form with Client ID, Client Secret, and pre-filled OAuth scopes, plus a link to the provider's portal.

**Field mapping happens inline.** Once connectors are ready, the AI generates field mappings between systems. You see a **"WE'VE SET THIS UP FOR YOU"** banner with mapping rows showing source fields, target fields, and a **Change** button for each. Fixed values appear as colored badges. Click **"Looks good, turn on"** to approve.

**Test cases happen inline.** The AI generates test scenarios with **MOCK** and **LIVE** badges. Review them, provide feedback, and click **Approve** on the ones that look correct.

> **Screenshot needed:** Step 3 showing inline OAuth form in the chat with Client ID, Client Secret fields, and portal link.

> **Screenshot needed:** Field mapping panel with "WE'VE SET THIS UP FOR YOU" banner, mapping rows, and "Looks good, turn on" button.

> **Screenshot needed:** Test cases panel showing MOCK/LIVE badges, scenario descriptions, and Approve buttons.

#### Step 4: Embed

The Widget Builder opens. Configure what your customers will see — the integration portal embedded inside your product. You control which integrations appear, the layout, branding, and which widget sections are visible (AI Assistant, Search Bar, Apps, Workflows, Insights).

> **Screenshot needed:** Widget Builder showing the left builder panel and right live preview.

#### Step 5: Live

Your integration platform is ready for customers. The Setup Assistant summarizes what was built and your dashboard transitions to the post-onboarding state.

### After onboarding: the Home page

Once the Setup Assistant completes, the Home page changes to a daily dashboard where you can input new builds anytime.

> **Screenshot needed:** Post-onboarding Home page showing the greeting, stats, AI assistant prompt, quick prompts, and dashboard cards.
