---
description: >-
  Use the AI Workflow Builder agent to create a flow by describing what you need
  in plain language.
---

# Creating a Workflow via Chat

**Prerequisites:** [Your First Integration](https://app.gitbook.com/o/d4yvP9A8wMsLuRwerHPU/s/3iSr2Tx8FvvuoLPncziH/~/edit/~/changes/517/fastn-v2/getting-started/your-first-integration) — you should know what workflows and triggers are.&#x20;

### Opening the Workflow Builder

1. Go to **Integrations → Workflows**.
2. Click **"Build with AI"** (next to the Create Workflow button).
3. The **Standalone Workflow Builder** page opens.

> **Screenshot needed:** Standalone Workflow Builder page showing the chat input, quick-start prompts, and the left sidebar with builder info and tasks.

{% hint style="info" %}
**Note:** There are two workflow builder variants. The **Standalone Builder** (accessed via "Build with AI" on the Workflows page) builds and validates workflows directly. The **Workflow Agent (Orchestrator)** coordinates the Planner, Builder, and Test Case agents for complex multi-step builds with handback support. This tutorial covers the Standalone Builder.
{% endhint %}

### Describing your workflow

In the chat input at the bottom, describe what you want. Quick-start prompts are provided:

* "Sync HubSpot contacts to Cin7 customers"
* "Shopify orders to Slack notifications"
* "Daily Stripe payout report"

#### Writing effective prompts

Be specific about:

* **What data to work with** — "HubSpot contacts", "Shopify orders above $100"
* **What to do with it** — "sync to Cin7 customers", "send a Slack notification"
* **When it should run** — "daily", "on every new order", "when a contact is updated"

#### Example prompts

**Data sync:**

> "Sync HubSpot contacts to Cin7 customers — match by email, create new Cin7 customers for any HubSpot contacts that don't exist yet."

**Notification:**

> "When a new Shopify order comes in, send a summary to the #orders Slack channel with the customer name, order total, and line items."

**Scheduled report:**

> "Every day at 6 AM, pull yesterday's Stripe payouts and send a summary to Slack."

> **Screenshot needed:** Chat interface showing a user prompt and the agent's response.

### Reviewing the generated workflow

After you describe your workflow, the builder:

1. Analyzes your request
2. Generates the workflow code
3. Validates it against test cases
4. Reports the result

The generated workflow appears as code — the same `export default async function(ctx)` format as the manual code editor. You can copy it, modify it, or let the builder iterate.

> **Screenshot needed:** Builder output showing generated workflow code and validation results.

### Iterating

Ask follow-up questions to refine:

* "Add error handling for when the Cin7 API is down"
* "Filter out contacts without email addresses"
* "Change the schedule to every hour instead of daily"

The **TASKS** panel on the left tracks what the builder has done and what's pending.

### When to use Build with AI vs code editor

| Use Build with AI when...                         | Use the code editor when...                      |
| ------------------------------------------------- | ------------------------------------------------ |
| You know _what_ you want but not _how_ to code it | You need precise control over the logic          |
| You're prototyping quickly                        | You're debugging specific lines                  |
| You want a starting point to modify               | You're working with complex data transformations |
| You want the builder to validate your workflow    | You already have working code to paste in        |

Most SaaS Admins use both — Build with AI for the starting point, code editor for fine-tuning.

### What you've learned

* How to access the Standalone Workflow Builder via "Build with AI"
* How to write effective prompts
* How to review and iterate on generated workflows
* When to use Build with AI vs the code editor
