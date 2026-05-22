---
description: >-
  Fastn's AI agents build workflows for you. Describe what you need in plain
  language and the agent handles the rest
---

# Creating a Workflow via AI

**Prerequisites:** [Your First Integration,](../../getting-started/your-first-integration.md) by now you should know what workflows and triggers are.&#x20;

### Where to start

You can build workflows with AI from two places in the platform:

**From the Home page** — The AI assistant on the Home page accepts natural language prompts like "Help me create an automation" or "Sync Salesforce leads to my CRM." This is the general-purpose entry point and will route you to the right agent.

**From the Integrations page** — Go to **Integrations → Workflows** and click **Build with AI** (next to "Create Workflow"). This opens the dedicated Workflow Builder, which is focused specifically on creating and validating workflows.

Both paths use the same AI agents underneath. This tutorial focuses on the Workflow Builder via **Integrations → Workflows → Build with AI**.

> **Screenshot needed:** Integrations → Workflows page with the "Build with AI" button highlighted next to "Create Workflow."

### Opening the Workflow Builder

1. Go to **Integrations → Workflows**.
2. Click **"Build with AI"** (next to the Create Workflow button).
3. The **Standalone Workflow Builder** page opens.

> **Screenshot:** Standalone Workflow Builder page showing the chat input, quick-start prompts, and the left sidebar with builder info and tasks.

### Describing what you need

Type a plain-language description of the workflow you want. The more specific you are about three things, the better the result:

**What data** — Name the systems and records involved. "HubSpot contacts," "Shopify orders above $100," "yesterday's Stripe payouts."

**What to do with it** — Describe the action. "Sync to Cin7 customers," "send a Slack notification to #orders," "generate a summary report."

**When it should run** — Describe the timing. "On every new order," "daily at 6 AM," "when a contact is updated."

#### Example prompts

**Data sync:**

> "Sync HubSpot contacts to Cin7 customers. Match by email. Create new Cin7 customers for any HubSpot contacts that don't exist yet."

**Notification:**

> "When a new Shopify order comes in, send a summary to the #orders Slack channel with the customer name, order total, and line items."

**Scheduled report:**

> "Every day at 6 AM, pull yesterday's Stripe payouts and send a summary to Slack with the total amount and number of transactions."

> **Screenshot needed:** Chat interface showing a user prompt (e.g., the HubSpot-to-Cin7 example) and the agent beginning to analyze the request.

### What the agent does

After you describe your workflow, the agent works through several stages. You'll see each one happen in the chat.

#### 1. Analyzes your request

The agent breaks down what you've asked for which systems are involved, what data needs to move, what transformations are needed, and what trigger to use.

#### 2. Sets up connectors

If the systems you mentioned don't have connectors configured yet, the agent will flag this and either create one or ask you for credentials. For example, if you ask for a HubSpot sync but haven't connected HubSpot yet, the agent will say something like "Gamma needs its own connector before I can plan the HubSpot integration."

#### 3. Handles authentication inline

When a connector needs credentials, the auth form appears right inside the chat so you never leave the conversation.

For **API key auth**, you'll see a tabbed form with fields for the key and any required configuration. For **OAuth** (e.g., HubSpot, Shopify), you'll see a form with fields for Client ID, Client Secret, and pre-filled OAuth scopes, plus a link to the provider's portal to get your credentials.

> **Screenshot needed:** Inline OAuth form in the chat showing CLIENT ID, CLIENT SECRET, OAUTH SCOPES fields, and a portal link.

#### 4. Maps fields between systems

Once connectors are ready, the agent generates field mappings between source and target systems. You'll see a **"WE'VE SET THIS UP FOR YOU"** banner with a summary of each mapping.

Each mapping row shows a plain-language description of what it does (e.g., "Contact email → Customer email"), the source field, the target field, and a **Change** button to modify it. Fixed values appear as colored badges, for example, a yellow badge showing `Format: "presentation"` or a green badge showing `Text Mode: "generate"`.

Below the mappings you'll find:

* **Record Matching Strategy** — How the workflow tracks records across systems (e.g., "Track IDs via fastn.state")
* **+ Add Mapping** — Add a field mapping the agent didn't include
* **Add Filters** — Narrow which records get synced
* A natural-language input where you can describe changes and the agent will update the mappings

When everything looks right, click **"Looks good, turn on"** to approve the field mapping configuration.

> **Screenshot needed:** Field mapping panel showing the "WE'VE SET THIS UP FOR YOU" banner, 3-4 mapping rows with source/target dropdowns and Change buttons, fixed value badges, and the "Looks good, turn on" button.

#### 5. Generates test cases

The agent creates test cases to validate the workflow before it goes live. You'll see a test case panel showing with named test groups.

Each test case has:

* A **MOCK** or **LIVE** badge

{% hint style="info" %}
Mock tests use simulated data whereas live tests hit the actual APIs
{% endhint %}

* A description of the scenario being tested
* A **Feedback** field where you can flag issues

You can easily review the test cases, approve the ones that look correct and then flag any that need changes and the agent will revise them.

> **Screenshot needed:** Test cases panel showing MOCK/LIVE badges, scenario descriptions, Feedback fields, and Approve buttons.

#### 6. Reports the result

The agent summarizes what was built from the workflow, the trigger, the field mappings to the test results. The workflow is now ready for deployment.

> **GIF needed:** Full sequence — typing a prompt, agent analyzing, setting up auth, showing field mappings, generating test cases, final summary. (This is the hero visual for this page — should be \~15-20 seconds showing the AI doing the work.)

### Iterating on the workflow

In case you want changes on your workflow, you can ask follow-up questions to refine what the agent built such as:

* "Add error handling for when the Cin7 API is down"
* "Filter out contacts without email addresses"
* "Change the schedule to every hour instead of daily"
* "Add a Slack notification when the sync fails"
* "Only sync contacts created in the last 30 days"

The agent then updates the workflow, field mappings, and test cases based on your follow-up. The **TASKS** panel on the left sidebar tracks what the agent has completed and what's still pending.

### Reviewing what the agent built

Once the agent finishes, the workflow appears in your **Integrations → Workflows** list. Click on it to open the Workflow Editor.

The editor has three panels. As a SaaS admin, the one that matters most is the right panel specifically the **Docs** tab.

#### Visualizing the workflow (Docs → Flow)

The **Docs** tab has three sub-tabs: **Flow**, **Sequence**, and **Docs**.

The **Flow** sub-tab renders a visual flowchart of the entire workflow as a node graph. Its the very workflow in result that would have taken you manually to build without Fastn's agents. Every step the agent generated appears as a connected node  consisting decision points, API calls, data retrieval, and skip/error paths are all mapped out visually.&#x20;

This is the fastest way to verify the agent built the right logic. You can trace the flow from trigger to completion and spot missing branches or wrong conditions with no code reading required.

The **Sequence** sub-tab shows the same logic as a step-by-step timeline, useful for understanding the order things happen in.

The **Docs** sub-tab shows auto-generated documentation describing what the workflow does.

{% hint style="info" %}
This same visualization appears in the customer-facing widget when end users click into an active workflow. What you see here is what your customers see so reviewing it now also means reviewing your customers' experience.
{% endhint %}

> **Screenshot needed:** Right panel Docs tab with the Flow sub-tab active, showing the full visual flowchart with connected nodes, decision branches, and action steps.

#### What else is in the editor

The **left panel** shows the workflow's configuration i.e. its name, description, execution settings, and the **Publish & Deploy** buttons you'll use to go live. The agent sets these up for you, but you can adjust them if needed.

The **center panel** shows the generated code. You don't need to touch this and it's there for visibility. The footer shows metadata like `Edited via agent`, confirming the AI wrote it.

### Tips for better results

1. **Be concrete about your prompts**\
   "Sync HubSpot contacts to Cin7 customers, match by email" works better than "integrate HubSpot and Cin7."
2. **Name the specific fields if you care about them.**\
   "Include the customer name, order total, and line items in the Slack message" gives the agent enough to build the right field mapping.
3. **Iterate rather than rewrite**\
   If the first result is 80% right, send a follow-up to fix the remaining 20%. The agent keeps context from the conversation.

### What you've learned

* How to open the Workflow Builder from Integrations → Workflows → Build with AI
* How to describe a workflow in plain language so the agent can build it
* How the agent handles the full cycle: connector setup, inline auth, field mapping, test case generation
* How to iterate on the generated workflow with follow-up prompts
