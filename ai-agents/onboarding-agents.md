---
description: >-
  Two agents that guide onboarding — one for SaaS companies setting up the
  platform, one for end customers connecting their tools through the widget.
---

# Onboarding Agents

Fastn has two onboarding agents that handle different sides of the same process. The **SaaS Onboarding** agent helps your team set up the platform. The **Tenant Onboarding** agent helps your customers connect their tools. They operate in different contexts, with different audiences, but together they cover the full onboarding lifecycle.

|                     | SaaS Onboarding                                    | Tenant Onboarding                                      |
| ------------------- | -------------------------------------------------- | ------------------------------------------------------ |
| **Who uses it**     | SaaS Admin (your team)                             | End User (your customer)                               |
| **Where it runs**   | Fastn dashboard                                    | Embedded widget in your product                        |
| **Technical depth** | Assumes knowledge of APIs and integrations         | Plain language — assumes no technical knowledge        |
| **Scope**           | Platform-wide: connectors, flows, widgets, go-live | Single tenant: connections, mappings, sync preferences |

***

### SaaS Onboarding

Walks SaaS Admins through the complete platform setup — from first login to go-live. Available through the **AI Agent** section in the dashboard sidebar.

#### What it does

1. **Understands your product** — Asks about your SaaS product, your customers, and what integrations they need.
2. **Recommends connectors** — Based on your industry and use case, suggests which connectors to configure first.
3. **Guides connector setup** — Walks you through adding and authenticating each connector, including OAuth configuration and credential management.
4. **Configures integration packs** — Helps you bundle connectors and workflows into integration packs that make sense for your customers.
5. **Sets up the widget** — Guides widget creation, dependency connector configuration, action setup (Activation/Deactivation), and branding.
6. **Validates go-live readiness** — Runs a checklist to confirm everything is production-ready.

#### What it asks

The agent tailors the setup to your situation through conversation:

* "What does your product do and who are your customers?"
* "Which apps do your customers most frequently ask to connect with?"
* "Do your customers need real-time sync or is scheduled sync (hourly/daily) sufficient?"
* "Will your customers need to customize field mappings, or should you set defaults?"
* "Do you want a single integration hub widget, or separate widgets per integration?"

> **📷 Screenshot needed:** SaaS Onboarding agent conversation showing the initial questions about the SaaS product and connector recommendations based on industry.

#### Go-live checklist

Before the agent considers onboarding complete, it validates:

| Check                       | What it verifies                                                       |
| --------------------------- | ---------------------------------------------------------------------- |
| Connectors configured       | At least one connector added and authenticated                         |
| Flows deployed              | At least one flow in **Live** status                                   |
| Widget created              | At least one widget configured with dependency connectors and actions  |
| Widget embed code generated | The embed code has been generated                                      |
| Test tenant created         | At least one tenant exists for testing                                 |
| Test execution successful   | At least one flow execution completed successfully for the test tenant |

> **📷 Screenshot needed:** Go-live readiness check showing the checklist with pass/fail status for each item.

#### When to use it

* Initial platform setup (first week after signup)
* Adding a new integration vertical (e.g., adding accounting connectors after starting with e-commerce)
* Preparing for a new customer segment with different integration needs

***

### Tenant Onboarding

Guides your end customers through their first integration setup. Operates within the embedded widget — your customers interact with it inside your product, not the Fastn dashboard.

#### What it does

1. **Guides app connection** — Walks the user through the OAuth flow, explaining what permissions are requested and why.
2. **Assists field mapping** — Shows which fields auto-map to the CDM and which need manual configuration.
3. **Configures sync settings** — Helps choose sync direction (one-way, two-way), frequency (real-time, scheduled), and scope (all records, filtered subset).
4. **Sets up automations** — Collects user preferences that flows need (which Slack channel, what order amount triggers an alert, etc.).
5. **Runs a first sync** — Triggers a test sync so the user can verify data flows correctly before going live.
6. **Troubleshoots issues** — If the test sync fails, diagnoses the problem and guides the user to fix it.

#### What the tenant sees

The agent uses plain language since your customers may not be technical:

* "Let's connect your Shopify store. Click Connect and sign in with your Shopify admin account."
* "I've found 3 product fields that need mapping. Your Shopify 'Title' maps to 'Product Name' here. Does 'Variant SKU' map to your inventory code?"
* "How often should orders sync? Real-time means every new order syncs immediately. Daily means orders sync once at the end of each day."
* "Let's test the connection. I'm pulling your 5 most recent orders to verify everything looks right."

> **📷 Screenshot needed:** Tenant Onboarding conversation inside the embedded widget — showing the agent guiding a user through field mapping.

> **📷 Screenshot needed:** The agent running a test sync and showing the results to the tenant.

#### How preferences become configuration

The agent translates the tenant's plain-language choices into platform configuration:

| User preference                       | Platform configuration                             |
| ------------------------------------- | -------------------------------------------------- |
| "Sync orders in real-time"            | Event-driven trigger on `order.created` webhook    |
| "Only sync orders above $100"         | Filter step with condition `order.total > 100`     |
| "Post to #sales-alerts channel"       | Slack connector step with `channel: #sales-alerts` |
| "Map 'Variant SKU' to 'Product Code'" | Field mapping entry in the CDM configuration       |
| "Sync daily at 6 AM"                  | Cron trigger with schedule `0 6 * * *`             |

These configurations are saved at the **tenant level** in the 5-level hierarchy — they override organization defaults but can be further overridden at the flow or integration level.

#### When it activates

* A tenant connects their first app through the widget
* A tenant adds a new integration that requires configuration
* A tenant's existing integration needs reconfiguration

It's optional — tenants can also configure everything manually through the widget's settings screens if configuration flows are set up.

***

### How the two agents connect

The SaaS Onboarding agent sets up the platform. The Tenant Onboarding agent helps each customer use it. The handoff looks like this:

```
SaaS Onboarding                          Tenant Onboarding
─────────────────                        ──────────────────
Adds Shopify connector            →      Guides tenant to connect their Shopify store
Builds order sync flow            →      Collects tenant's sync preferences
Creates widget with actions       →      Presents the widget to the tenant
Sets organization-level defaults  →      Overrides with tenant-level preferences
Validates go-live readiness       →      Runs first sync for the specific tenant
```

> **🖼️ Diagram needed:** Visual showing the handoff between SaaS Onboarding (left, dashboard context) and Tenant Onboarding (right, widget context). Show the SaaS Admin setting up connectors/flows/widgets, then the end user interacting through the widget with the Tenant Onboarding agent.

### Related pages

* [**Setting Up Your Organization**](https://claude.ai/tutorials/saas-admin/setting-up-your-organization.md) — Manual walkthrough of platform setup
* [**Connecting Apps via Widget**](https://claude.ai/tutorials/end-user/connecting-apps-via-widget.md) — End user tutorial for manual connection
* [**Configuration Agent**](https://claude.ai/chat/configuration-agent.md) — Handles complex field mapping and filter configuration that the Tenant Onboarding agent may invoke
