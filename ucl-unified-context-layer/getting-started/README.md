---
description: >-
  Connect your AI agents to 250+ enterprise apps with managed authentication,
  multi-tenant support, and sub-second execution through Fastn's Unified Context
  Layer (UCL).
---

# AI agent integrations

Unified Context Layer (UCL) enables your SaaS platforms to deliver embedded, secure, and scalable AI integrations. This section covers setting up your account, connecting apps, embedding AI clients, and understanding how UCL manages external systems, connections, and actions.&#x20;

{% hint style="success" %}
**Ready to embed UCL into your AI agent?** Jump straight to the [Embedding UCL onto your AI Agent](about-unified-context-layer/embedding-ucl-onto-your-ai-agent.md) guide for a step-by-step walkthrough.
{% endhint %}

## **1. Workspace Selection**

After you log in to [UCL](https://app.ucl.dev/), you can select a workspace or create a new one by clicking on **Create Workspace** button, after which you'll be directed to the next page to set up your integrations.

{% hint style="info" %}
When you first log in to UCL, a workspace titled "My Workspace" is created by default.&#x20;
{% endhint %}

<figure><img src="../../.gitbook/assets/image (571).png" alt="UCL workspace selection screen with option to select or create a workspace"><figcaption></figcaption></figure>

## 3. Start Building

* After selecting your workspace, complete the quick onboarding questions.
* This will lead you to the next page where you can click on **Start Building** to open the apps you selected during onboarding.

<figure><img src="../../.gitbook/assets/image (555).png" alt="UCL onboarding page with Start Building button to begin app setup"><figcaption></figcaption></figure>

### Select Your Apps Then Chat

* Next, you can see the interface for the first step, where you can see all the apps you have selected.&#x20;

> You can connect each app using the **Connect** button or remove an app by clicking on 'x'.

<figure><img src="../../.gitbook/assets/image (558).png" alt="UCL app selection interface showing selected apps with Connect buttons"><figcaption></figcaption></figure>

* Once an App is connected, you will see the button labelled 'Connected'.&#x20;
* UCL's AI Assistant Playground would now be seen on the left side of the screen, where you can give a prompt to perform actions with the selected apps.

{% hint style="info" %}
You need to have at least one app connected to see the AI Assistant.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (557).png" alt="UCL dashboard with connected apps and AI Assistant Playground visible on the left"><figcaption></figcaption></figure>

{% hint style="info" %}
Use **Modify Selection** in the "Selected Apps" section to adjust your choices.
{% endhint %}

Click on **Continue** in the top-right corner to move to the next step.

## &#x20;4. Finalize Connection Setup

* You will now be moved to the second step, where you can finalize your connection setup.

<figure><img src="../../.gitbook/assets/image (559).png" alt="UCL connection setup screen for finalizing integration configuration"><figcaption></figcaption></figure>

* You can choose **Sandbox** to try UCL in the interactive test environment. Or select **Favorite Client** to test UCL with your preferred client app

<figure><img src="../../.gitbook/assets/image (561).png" alt="UCL setup options showing Sandbox and Favorite Client choices for testing"><figcaption></figcaption></figure>

* Click **Complete Setup** (top right) to move to the **Connect** page.

<figure><img src="../../.gitbook/assets/image (562).png" alt="UCL setup page with Complete Setup button in the top-right corner"><figcaption></figcaption></figure>

## 5. Choose Apps & Actions

* On the **Connect** Page in your Dashboard, you can **Choose the Apps You Need**, along with viewing your selected apps and enabled actions.

<figure><img src="../../.gitbook/assets/image (563).png" alt="UCL Connect page showing selected apps and enabled actions on the dashboard"><figcaption></figcaption></figure>

> Actions represent the functions you can perform within each app.

<figure><img src="../../.gitbook/assets/image (564).png" alt="UCL dashboard displaying available actions for selected apps"><figcaption></figcaption></figure>

### Connecting Existing Apps

* From the **Connecting Existing Apps** button, browse and connect to any app available in UCL.

<figure><img src="../../.gitbook/assets/image (565).png" alt="UCL app catalog for browsing and connecting available apps"><figcaption></figcaption></figure>

> You can select any app by checking the top-right box on the app and click on **Select Tools** to modify your action selection and then finalize this setup by clicking the **Confirm Action** button in the right-bottom.

<figure><img src="../../.gitbook/assets/image (566).png" alt="UCL app selection panel with checkboxes, Select Tools, and Confirm Action buttons"><figcaption></figcaption></figure>

### Custom Apps

You can also **create a Custom App**, which means:

* Building your own application with preferred actions, or
* Adding new actions to existing tools.
* Learn more about custom tools [here](about-unified-context-layer/creating-a-custom-tool.md).

<figure><img src="../../.gitbook/assets/image (567).png" alt="UCL interface for creating a custom app with preferred actions"><figcaption></figcaption></figure>

## 6. Embed AI Clients

* Open the **Embed** section (top corner) to access detailed instructions for connecting any AI client with UCL.
* You can navigate and select through the list of **Clients** and have a complete step-by-step guide to connect with any of the listed prebuilt AI clients or your own AI agent.

<figure><img src="../../.gitbook/assets/image (568).png" alt="UCL Embed section showing list of AI clients with step-by-step connection guides"><figcaption></figcaption></figure>

* From the sidebar, you can:
  * Browse Platform [Documentation](https://docs.fastn.ai)
  * Launch [Sandbox](https://codesandbox.io/p/sandbox/github/fastnai/embedded-multitenant-ai-assistant?file=%2F.env)
  * Join the [Discord Community](https://discord.gg/rePMvnURzg)

## 7. Monitor with Insights

*   The **Insights** dashboard provides monitoring metrics, including:

    * Active tenants and tools
    * Tenant requests and success rate
    * Usage stats (monthly, weekly, today)
    * Connection success rate and vulnerability checks

    Learn more about UCL Monitoring [here](about-unified-context-layer/monitoring/).

    <figure><img src="../../.gitbook/assets/Screenshot 2025-09-11 at 11.40.40 PM.png" alt="UCL Insights dashboard showing active tenants, request success rate, and usage metrics"><figcaption></figcaption></figure>

## 8. Test in Playground

* You can use the **Playground** (from the three-dot menu, top right) to test all connected apps.

<figure><img src="../../.gitbook/assets/image (572).png" alt="UCL Playground for testing connected apps with AI agent commands"><figcaption></figcaption></figure>

> Run commands directly with your AI agent against the integrated apps.

### Example Use Cases

{% embed url="https://docs.fastn.ai/ucl-use-cases/create-a-google-doc-and-share-it-to-slack-using-ucl" %}

{% embed url="https://docs.fastn.ai/ucl-use-cases/connect-ucl-for-task-assignment-in-jira" %}

{% embed url="https://docs.fastn.ai/ucl-use-cases/connect-ucl-to-cursor-and-access-data-from-notion" %}
