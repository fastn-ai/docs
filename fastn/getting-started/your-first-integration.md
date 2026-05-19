---
description: >-
  Build a working integration from scratch i.e. create a connector, write a
  workflow, set up a trigger, and test the full loop.
---

# Your First Integration

This walkthrough takes you from an empty Fastn project to a working integration. You'll create a connector, write a workflow, set up a trigger, create a customer, and monitor executions.

**Prerequisites:** A Fastn account with dashboard access.

### What you'll build

A HubSpot contact sync workflow. When a webhook trigger fires, the workflow fetches contact data and processes it. This demonstrates:

* Creating a connector (HubSpot)
* Writing a workflow in the code editor
* Setting up a webhook trigger with routes
* Testing the workflow
* Monitoring executions in Activity

### Step 1: Create a connector

1. Click **Integrations** in the top nav.
2. You're on the **Connectors** sub-tab. Click **+ Create**.
3. Fill in the Create Connector dialog:
   * **Name:** HubSpot CRM
   * **Slug:** hubspot-crm (auto-generated from name)
   * **Description:** HubSpot CRM integration
   * **Domain:** hubspot.com
   * **Visibility:** Private
   * **Auth Methods:** Click the auth dropdown and select **OAuth 2.0**
4. Click **Create**.

> **Screenshot:** Create Connector dialog filled in with HubSpot details and OAuth 2.0 selected.

{% hint style="info" %}
Alternatively, click **Build with AI** to open the **Connector Agent**. Describe what you need (e.g., "HubSpot CRM") and the agent will discover the API, build actions and events, and test them automatically.
{% endhint %}

> **Screenshot:** Connector Agent page showing the chat input with quick-start prompts.

#### Add a connection

After creating the connector, you need to authenticate it:

1. Find your connector card on the Connectors page.
2. Click **Connect** (or **+ Add Connection**).
3. Complete the OAuth flow — sign in to HubSpot and authorize Fastn.
4. The connection is stored under **Integrations → Connections**.

> **GIF:** Clicking Connect on a connector card, completing the OAuth popup, seeing the connected state.

### Step 2: Create a workflow

1. Click the **Workflows** sub-tab under Integrations.
2. Click **Create Workflow**.
3. The workflow editor opens with three panels:

**Left — Configuration:**

* **Name:** `hubspot-contact-sync`
* **Description:** Syncs HubSpot contacts on webhook trigger
* **Execution Tier:** Standard
* **Execution Timeout:** 1.0m
* **Retry Policy:** Off (for now)

**Center — Code editor** (`workflow.js`):

```javascript
export default async function(ctx) {
  const { input, headers } = ctx;
  
  // Log the incoming data
  console.log("Received:", JSON.stringify(input));
  
  // Process the contact data
  const contact = input.contact || {};
  
  return {
    result: "Contact processed",
    contactEmail: contact.email,
    receivedAt: new Date().toISOString()
  };
}
```

**Right — Test panel:**

* **CTX.INPUT:** Enter sample JSON
* **CTX.HEADERS:** Optional headers
* **Run** button to execute without saving

> **Screenshot:** Workflow editor showing all three panels — Configuration on left with Name and Execution Tier filled in, code in center, Test panel on right.

### Step 3: Test the workflow

Before creating it, test directly in the editor:

1. Click the **Test** tab in the right panel.
2. In **CTX.INPUT**, enter sample data:

```json
{
  "contact": {
    "email": "test@acme.com",
    "firstName": "Jane",
    "lastName": "Doe"
  }
}
```

3. Click **Run**.
4. The output appears below — you should see your return object with `"result": "Contact processed"`.

> **Screenshot:** Test panel showing the input JSON and the successful output after clicking Run.

{% hint style="info" %}
**Note:** "Hit Run to execute without saving" this lets you iterate on the code before committing.
{% endhint %}

### Step 4: Create the workflow

Once the test passes:

1. Click **Create Workflow** (bottom-left of the editor).
2. The workflow appears in the Workflows table with status **active**.

> **Screenshot:** Workflows table showing the new workflow with active status, version, and updated date.

### Step 5: Set up a trigger

Triggers are managed separately from workflows. You need to create a trigger and route it to your workflow.

1. Click the **Triggers** sub-tab under Integrations.
2. Click **Add Trigger**.
3. Select **Webhook** (for this tutorial).

#### Configure the webhook trigger

4. Fill in the **Name** and optional **Description**.
5. Under **Routes**, click **+ Add route**:
   * **Workflow:** Select `hubspot-contact-sync` from the dropdown
   * **Key/Value filters:** Leave empty for now (all payloads will trigger this route)
   * **Headers:** Optional — leave empty
6. Click **Create**.

> **Screenshot:** Webhook trigger configuration with a route pointing to the hubspot-contact-sync workflow.

Your webhook now has a URL. Any HTTP POST to this URL will trigger the workflow.

#### Alternative: Set up a scheduler

To test with a scheduled trigger instead:

1. Click **Add Trigger** → **Scheduler**.
2. Set **Name:** "Daily contact sync"
3. Under **Schedule**, select a preset:
   * **Interval** — Run every X minutes
   * **Daily** — Run once per day
   * **Weekly** / **Monthly** / **Custom**
4. For testing, set **Interval** → Run every **5 minutes**.
5. Click **Create**.

> **Screenshot:** Scheduler trigger configuration showing the preset buttons and interval settings.

### Step 6: Create a test customer

1. Go to **Settings → Customers**.
2. Click **Create Customer**.
3. Enter a name (e.g., "Acme Corp Test").
4. Note the customer ID — you'll use this for customer-scoped API calls.

> **Screenshot:** Settings → Customers showing the Create Customer button and the customer creation form.

### Step 7: Test the webhook trigger

Send a test request to your webhook URL:

```bash
curl -X POST YOUR_WEBHOOK_URL \
  -H "Content-Type: application/json" \
  -d '{
    "contact": {
      "email": "jane@acme.com",
      "firstName": "Jane",
      "lastName": "Doe"
    }
  }'
```

### Step 8: Monitor in Activity

1. Click **Activity** in the top nav.
2. Click the **Executions** sub-tab.
3. You should see your workflow execution:
   * **Time:** just now
   * **Workflow:** hubspot-contact-sync
   * **Tier:** STANDARD
   * **Version:** v1
   * **Status:** Completed (green) or Failed (red)
   * **Duration:** execution time
   * **Triggered By:** webhook
4. Click on the execution row to see details.

> **Screenshot:** Activity → Executions showing the successful execution with all columns visible.

You can also check:

* **Activity → Events** to see the incoming webhook event
* **Activity → Traces** to see the connector execution trace

### What you've built

1. Created a connector (HubSpot CRM) with OAuth 2.0 auth
2. Wrote a workflow in the code editor with test data
3. Set up a webhook trigger with a route to the workflow
4. Created a test customer
5. Triggered the webhook and verified execution in Activity

This is the core pattern for every integration on Fastn: **Connector → Workflow → Trigger → Customer isolation → Monitor**.
