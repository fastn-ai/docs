---
description: Build a workflow by describing it in plain words to Build with AI.
---

# Create a workflow with Build with AI

**Build with AI** is fastn's own builder. You describe the workflow, what data to sync and between which systems, and it sets up the connectors, handles authentication, maps the fields, writes test cases, and then produces the workflow code and a diagram of it.

**Prerequisites:** [Your First Integration](../../getting-started/quickstart.md). By now you should know what workflows and triggers are.

{% hint style="info" %}
Build with AI needs the **Operator** role or above, and Build with AI switched on for your organization. If either is missing, it does not appear in the sidebar. See [Build with AI](../../build/agent/README.md).
{% endhint %}

### Where to start

There are two ways in, and both open the same screen:

* **Build → Build with AI** in the sidebar (`/agent`).
* The **What should your customers be able to do?** prompt on **Home**. Type your request there and send it.

The screen is headed **Build an integration**. On the left, the **Sessions** rail keeps every earlier build with its full conversation; **New session** starts a fresh one. Under **Start from an example** there are four example cards you can click to start from.

### Describing what you need

Type a plain-language description of the workflow you want into the message box (*Write a message…*). The more specific you are about three things, the better the result:

**What data** - Name the systems and records involved. "HubSpot contacts," "Shopify orders above $100," "yesterday's Stripe payouts."

**What to do with it** - Describe the action. "Sync to Cin7 customers," "send a Slack notification to #orders," "generate a summary report."

**When it should run** - Describe the timing. "On every new order," "daily at 6 AM," "when a contact is updated."

**Attach a file** lets you add an API spec, a sample payload or a field-mapping spreadsheet. A real payload is the fastest way to accurate mappings.

#### Example prompts

**Data sync:**

> "Sync HubSpot contacts to Cin7 customers. Match by email. Create new Cin7 customers for any HubSpot contacts that don't exist yet."

**Notification:**

> "When a new Shopify order comes in, send a summary to the #orders Slack channel with the customer name, order total, and line items."

**Scheduled report:**

> "Every day at 6 AM, pull yesterday's Stripe payouts and send a summary to Slack with the total amount and number of transactions."

### Choose how much it asks first

The chip under the message box sets the approval mode:

* **Auto** creates, updates and deletes without asking.
* **Manual** asks before creating, updating or deleting anything, with a card for each call that you **Accept**, **Always allow** or **Reject**.

You can switch at any time. See [Approval mode](../../build/agent/approval-mode.md).

### What the agent does

After you send your description, the agent works through the build in the chat. The **Build progress** section of the right-hand rail tracks it as a step count across up to four phases: **Use cases**, **Connectors**, **Workflows** and **Widget**. Only phases the agent has written steps into are shown.

#### 1. Asks what you meant

Where your brief is ambiguous, the agent asks rather than guesses, with selectable answer cards. Every question also offers **Other…** for a free-form answer.

#### 2. Sets up connectors

The agent works out which systems are involved, reuses connectors that already exist and creates the ones that don't, asking you for anything it needs.

For example, if you ask for a HubSpot sync but haven't connected HubSpot yet, the agent tells you it needs to set up that connector first.

#### 3. Handles authentication inline

When a connector needs credentials, the auth form appears right inside the chat, so you don't have to leave the conversation.

For **API key auth**, you'll see a tabbed form with fields for the key and any required configuration. For **OAuth** (e.g., HubSpot, Shopify), you'll see a form with fields for Client ID, Client Secret, and pre-filled OAuth scopes, plus a link to the provider's portal to get your credentials.

#### 4. Maps fields between systems

Once connectors are ready, the agent proposes field mappings between the source and target systems, under a **WE'VE SET THIS UP FOR YOU** banner.

Each mapping row shows a plain-language description of what it does (e.g., "Contact email → Customer email"), the source field, the target field, and a **Change** button to modify it. Fixed values appear as colored badges.

Below the mappings you'll find:

* **Record Matching Strategy** - how the workflow tracks records across systems (e.g., "Track IDs via fastn.state")
* **+ Add Mapping** - add a field mapping the agent didn't include
* **Add Filters** - narrow which records get synced
* A text box where you can describe changes and the agent will update the mappings

When everything looks right, click **Looks good, turn on** to approve the field mappings.

#### 5. Writes test cases

The agent writes test cases to validate the workflow before it goes live, in groups it names for your integration. Each test case has:

* A **Live** or **Mock** badge

{% hint style="info" %}
Mock tests use simulated data, whereas live tests hit the real APIs.
{% endhint %}

* A description of the scenario being tested

To have the agent change them, type into **Feedback (optional)...** and click **Revise**. When they look right, click **Approve**.

#### 6. Builds the workflow and reports back

The agent builds and tests the workflow, binds its trigger, and summarizes what it built: the workflow, the trigger, the field mappings and the test results.

> **GIF needed:** Full sequence - typing a prompt, agent analyzing, setting up auth, showing field mappings, generating test cases, final summary. (This is the hero visual for this page - should be \~15-20 seconds showing the AI doing the work.)

### Iterating on the workflow

To change what the agent built, send a follow-up in the same session, such as:

* "Add error handling for when the Cin7 API is down"
* "Filter out contacts without email addresses"
* "Change the schedule to every hour instead of daily"
* "Add a Slack notification when the sync fails"
* "Only sync contacts created in the last 30 days"

The agent updates the workflow, field mappings and test cases together. **Build progress** in the right-hand rail shows what is done and what is still pending, and the session stays in the **Sessions** rail so you can come back to it later.

### Reviewing what the agent built

Once the agent finishes, the workflow appears under **Build → Integrations → Workflows**. Click it to open the workflow editor. If you change anything there, click **Save workflow**.

#### Visualizing the workflow

The editor's **Diagram** tab has three sub-tabs: **Flow**, **Sequence** and **Docs**.

The **Flow** sub-tab renders the whole workflow as a node graph. Every step the agent generated appears as a connected node, with decision points, API calls, data retrieval and skip or error paths all mapped out.

Use it to check the agent built the right logic: trace the flow from the trigger to completion and look for missing branches or wrong conditions.

The **Sequence** sub-tab shows the same logic as a step-by-step timeline, useful for understanding the order things happen in.

The **Docs** sub-tab shows auto-generated documentation describing what the workflow does.

{% hint style="info" %}
The people at your customer see the same flow diagram in the widget only if you turn on **Workflow Diagram** in the widget's features. It is off by default.
{% endhint %}

#### What else is in the editor

The editor also holds the workflow's configuration (its name, description and execution settings) and the **Publish & Deploy** controls you'll use to go live. The agent sets these up for you, but you can adjust them. Generated scenarios sit on the **Test cases** tab, each badged **Live** or **Mock**.

### Tips for better results

1. **Be concrete in your prompts**\
   "Sync HubSpot contacts to Cin7 customers, match by email" works better than "integrate HubSpot and Cin7."
2. **Name the specific fields if you care about them.**\
   "Include the customer name, order total, and line items in the Slack message" gives the agent enough to build the right field mapping.
3. **Iterate rather than rewrite**\
   If the first result is 80% right, send a follow-up to fix the remaining 20%. The agent keeps context from the conversation.

### What you've learned

* How to open Build with AI from the sidebar or the Home prompt
* How to describe a workflow in plain language so the agent can build it
* How the agent handles the full cycle: connector setup, inline auth, field mapping, test cases
* How to visualize the workflow the agent built, end to end
* How to iterate on the generated workflow with follow-up prompts
