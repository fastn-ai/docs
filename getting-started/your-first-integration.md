---
description: >-
  Build a working integration using the AI Setup Assistant from use case
  analysis to live workflows.
---

# Your First Integration

This walkthrough takes you from a fresh Fastn account to a working integration. The AI Setup Assistant handles most of the work you describe what you need, review what the AI builds, and go live.

**Prerequisites:** A Fastn account with dashboard access.

### Building via Setup Assistant

When you first log in (or reset onboarding), you'll see a setup screen that prompts you to setup your company:

> **Screenshot: Enter domain URL**

Enter your **SaaS domain** (e.g., `gamma.app`) and click **Start setup →**.

This kicks off the 5-step Setup Assistant pipeline.

> **Screenshot:** Initial setup screen showing the SaaS domain field and Start setup button.

### Step 1: Use cases

The AI agent researches your company automatically. It analyzes:

* **Company profile** — what you build, who your customers are
* **Existing integrations** — what you already offer
* **Customer reviews** — real feedback from Reddit, Trustpilot, G2, community forums
* **Competitive landscape** — how your integration offering compares to competitors
* **Integration gaps** — where you're falling behind peers

The right sidebar tracks research progress with checkmarks focusing on but not limited to:

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

The AI then shows you an **Integration gap vs. peers** table comparing your integration count against competitors, with each competitor's advantage explained.

#### You pick the pain points

The AI will then ask: **"Which of these pain points are real for your customers?"**

You'll see checkboxes with specific pain points the AI identified from its research. For example:

* Manual presentation requests from email and chat
* Painful export and editing outside Gamma
* Missing downstream page and CMS workflows
* Manually re-keying CRM or sheet data into Gamma

Select the ones that matter or you can also type **"Something else"** to add your own custom pain points and then click **Send**.

You can also click on **"View detailed report →"** for the full research output to ensure your own validation against the output.

> **Screenshot needed:** Step 1 showing the pain points selection with checkboxes and the Send button.

### Step 2: Connectors

Based on your selected pain points, the AI then recommends which connectors to build first prioritized by customer impact.

For example, if you selected "Manually re-keying CRM or sheet data," the AI might recommend:

1. **HubSpot** (build first) — maps to the sales and marketing workflows your users already run
2. **Salesforce** — enterprise gap
3. **Google Sheets** — common manual handoff
4. **Notion** (nice-to-have) — visible demand but less direct revenue signal

The AI explains its reasoning with links to real sources.

#### You pick which to build

The AI asks: **"Which would you like to build first?"**

Options appear as selectable cards, for example: HubSpot, Salesforce, Google Sheets, Notion, **Skip - go straight to widget**, or type **"Something else"**.

Select one and the AI starts building.

> **Screenshot needed:** Connector selection showing the recommended apps and the "Skip - go straight to widget" option.

{% hint style="info" %}
If your desired options do not arrive, you can type in your desired application you want your connector to work with.
{% endhint %}

### Step 3: Building the integration

Once you select a connector (e.g., HubSpot), the AI moves to building the integration. The right sidebar shows sub-steps as shown below:

* ✓ Building partner connectors
* ◎ Planning the integration
* ○ Building the integration

#### The AI builds your connectors

If your own app also needs a connector, the AI detects this automatically:

> "Gamma needs its own connector before I can plan the HubSpot integration. How do you want to proceed?"
>
> 1. Build the Gamma connector
> 2. Cancel

{% hint style="info" %}
If your app already has a connector in Fastn. the AI will then inform you that a connector already exists and will prompt you to connect.
{% endhint %}

Select option 1 and the AI starts building. The AI also tells you the estimated time when the connector will be ready, the duration though varies and depends upon how complex is your application.

#### Credentials and Authentication process

The AI then asks you to authenticate each connector inline right in the chat:

{% hint style="info" %}
**Note:** Every connector setup varies per application and its permissions.
{% endhint %}

**For API Key connectors:**

During a connector setup, the AI might prompt you to input an API key with a message as follows:

> **Connect your Gamma account** Connect your Gamma account so I can finish the connector and verify it works.

{% hint style="info" %}
You can access your desired connectors' API keys through the developer platform of your application.
{% endhint %}

Enter your API key and click on **Connect.**

**For OAuth connectors:**

Some connectors, require more details such as Client IDs, Secrets, and OAuth Scopes for a complete setup. Following below is an example:

> **HUBSPOT CREDENTIALS**
>
> * CLIENT ID \*
> * CLIENT SECRET \*
> * OAUTH SCOPES \* (pre-filled with recommended scopes like `crm.objects.contacts.read crm.objects.deals.read oauth`)

For such setup, you will find a **Portal** link that takes you directly to the third-party's developer settings where you can find these values. Enter the credentials and click **Submit**.

> **Screenshot:** Inline auth for an API Key connector (Gamma) and inline auth for an OAuth connector (HubSpot) showing the credentials form.

#### The AI sets up the integration

Once both connectors are built and authenticated, the AI configures how data flows between them:

You'll see a mapping screen showing you how can you connect your application to a third party application. This includes:

* **Direction pills** — e.g., `Gamma Presentation Generation ← HubSpot Deal`
* **Mapping count** — e.g., "7 mappings ready to go"
* **Each mapping row** with:
  * A plain-language description (e.g., "Input Text in Gamma Presentation Generation will be the `Description` from HubSpot Deal")
  * Source and target field dropdowns
  * A **Change** button to modify

Some mappings use **fixed values,** values the AI sets as defaults, however you can change them as needed.

#### Reviewing and adjusting your mapping

Each mapping has a **Change** button. When clicking to it you can either:

* **Set a fixed value** — always use the same value
* **Combine fields** — merge multiple source fields
* **Conditional value** — different values based on conditions
* **Pick a source field** — choose from the source app's fields (e.g., "Load 99 more fields")
* **Pick a target field** — choose from the target app's fields

Additionally in the bottom you will find options like:

* **Add Mapping** — add custom mappings the AI didn't create
* **Add Filters** — only sync records matching certain conditions
* **Record Matching Strategy** — shows how Fastn tracks which records have already been synced&#x20;

{% hint style="info" %}
You can also additionaly tweak the whole setup in natural language in a text input.
{% endhint %}

When everything looks right, click on **"Looks good, turn on"** on the top.

> **Screenshot needed:** Field mapping screen showing mappings with Change buttons, fixed values, and the "Looks good, turn on" button.

> **Screenshot needed:** The "Want to tweak the whole setup?" input field at the bottom.

#### Test cases

After you approve the mappings, the AI generates test cases to validate the integration and the third party application you want to connect with. Test cases allows you to validate the mappings and connections that you have established without any manual effort.

Test cases are organized into groups of cases where each test case (e.g., TC-07, TC-08) has:

* A **MOCK** or **LIVE** badge

{% hint style="info" %}
Mock tests do not consume API credits.
{% endhint %}

* A detailed scenario describing exactly what's tested
* Pass criteria explaining what must be true

You can expand any group to see individual test cases, add groups with and provide optional feedback.

Click **Approve** (the green button below) to confirm the test cases and proceed.

> **Screenshot needed:** Test cases screen showing groups, individual test cases with MOCK badges, and the Approve button.

### Step 4: Embed

Embedding is a crucial part of Fastn where you get to configure the customer-facing widget your customers will use inside your product.

The Widget Builder opens where you set up:

* **Layout** — title, subtitle, workflow templates
* **Style** — colors, typography, themes
* **Embed** — get the React SDK or Headless SDK code snippet

### Step 5: Live

Your platform is ready for customers. Connectors are built, integrations are configured with field mappings, test cases are validated, and the widget is set up.

## Alternative: Build with AI from the Integrations section

If you already have a Fastn account and you have gone through the onboarding process prior, you don't have to reset and use the Setup Assistant. After onboarding (or anytime), you can build new integrations directly:

1. Click **Integrations** in the top nav
2. Click **"Build with AI"** on top-right corner
3. The integration builder opens which give you a chat like interface and with a set of quick start prompts you can execute or type in your preffered prompt

> **Screenshot: Build an integration**

The left sidebar shows **SESSIONS** which is your build history and the right sidebar shows **ACTIVITY** which gives you an overview what the agents are doing on the backend.

The AI agents handle the entire build from connectors, configuration to testing just like the Setup Assistant, but without the guided pipeline. Use this when you already know what you want to build.

### Connectors page

After you have built your first integration using the Setup Assistant or with Integration Builder, your connectors will appear under **Integrations → Connectors.** There are two types of connectors:

* **Managed** connectors — pre-built by Fastn for common apps like HubSpot CRM, Cin7 Core, Shopify, Slack, ServiceNow
* **Personal** connectors — built by you or by the AI on your behalf

Each connector card shows a **Connect** button (if not yet authenticated) or **+ Add Connection** (if already connected).

You can also:

* **Import** — import a connector definition
* **Create** — manually create a connector (advanced)
* **Build with AI** — have the Connector Agent build one

> **Screenshot needed:** Connectors page showing MANAGED and PERSONAL connector cards with Connect buttons.

{% hint style="warning" %}
**Tip:** You can reset the Setup Assistant anytime from **Settings → General → Reset Onboarding** (bottom of page). However, this is irreversible and it deletes your qualification wizard answers and every Setup Assistant thread.
{% endhint %}
