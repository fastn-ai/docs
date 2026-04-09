---
description: >-
  This guide will take you through each step, from setting up your environment
  to seamlessly integrating your tools into your environment.
---

# Embedding UCL onto your AI Agent



{% embed url="https://youtu.be/H_hHMOIq7Zo" %}

**Embedding** refers to integrating UCL directly into your AI agent's environment so it can take real actions, like sending messages, updating records, or triggering workflows, using your connected tools.

When you're integrating **tools** into your SaaS product, **Unified Context Layer (UCL)** makes it easy to connect 1000+ tools (Actions), manage customer environments, and orchestrate real-world actions from a single command layer.

In this guide, we will walk you through step by step from setting up your space to fully embedding your tools into your environment, including but not limited to:

* Setting up your account on UCL
* Enabling your tools and actions
* Connecting your UCL MCP Server
* Implementing it onto your application/product

### Real-World Example: Document Management Workflow

When a marketing team creates a new campaign brief, a single UCL command automatically:

* Creates a new project document in Notion
* Shares the brief via Gmail to stakeholders
* Sets up a dedicated Slack channel for discussions
* Creates a collaborative Google Doc for content drafts

### **How Embedding Works?**

Embedding via UCL refers to the process of integrating the UCL functionality directly into your product or AI agent's codebase. This allows your application to seamlessly interact with external tools and services through UCL's unified interface.

This is how your AI agent looks with and without UCL embedding:

{% tabs %}
{% tab title="With Embedding" %}
<figure><img src="../../../.gitbook/assets/With Embedding.png" alt="Architecture diagram of an AI agent with UCL embedding, showing unified tool access and managed authentication"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Without Embedding" %}
<figure><img src="../../../.gitbook/assets/Frame 1750.png" alt="Architecture diagram of an AI agent without UCL, showing separate manual integrations for each tool"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

The embedding process enables you to:

* Execute commands across multiple tools without managing individual integrations
* Handle authentication and permissions across different customer workspaces
* Maintain secure user separation while accessing various third-party services
* Manage API connections and token storage through a single interface

Let's further understand embedding via a **use case example below**:



## **Step 1: Creating Your UCL Account**

1. Go to [ucl.dev ](https://ucl.dev)and sign up for an account.
2. After you log in, you can select a workspace, after which you'll be directed to the next page to set up your integrations.

{% hint style="info" %}
When you first log in to UCL, a workspace titled "My Workspace" is created by default. If you wish to create new workspaces and select from them, subscribe to UCL.
{% endhint %}

<br>

<figure><img src="../../../.gitbook/assets/image (585).png" alt="UCL workspace selection screen after login"><figcaption></figcaption></figure>



## Step 2: Choose Apps & Actions <a href="#step-1-select-your-apps-then-chat" id="step-1-select-your-apps-then-chat"></a>

* After selecting your workspace, you will be directed to the **Connect** Page in your Dashboard, you can **Choose the Apps You Need** along with viewing your selected apps and enabled actions.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252F13eysHB9Hch1TspTI4vH%252Fimage.png%3Falt%3Dmedia%26token%3Daba8e5be-9d8e-4307-891f-baeb4f18e02d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=2cc731e6&#x26;sv=2" alt="UCL Connect page showing selected apps and enabled actions on the dashboard"><figcaption></figcaption></figure>

> Actions represent the functions you can perform within each app.

* From the **Connecting Existing Apps** button, browse and connect to any app available in UCL.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FGQWhGe1JEY79C97okxzT%252Fimage.png%3Falt%3Dmedia%26token%3Dfed4ca5a-4f5a-4f38-ac35-b679349059f8&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=60aa427c&#x26;sv=2" alt="UCL app catalog for browsing and connecting available apps"><figcaption></figcaption></figure>

> You can select any app by checking the top-right box on the app and click on **Select Tools** to modify your action selection and then finalize this setup by clicking the **Confirm Action** button in the right-bottom.

<figure><img src="https://docs.fastn.ai/~gitbook/image?url=https%3A%2F%2F1255842839-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F3iSr2Tx8FvvuoLPncziH%252Fuploads%252FJGp6o9nxDYMIMqjYxmSG%252Fimage.png%3Falt%3Dmedia%26token%3D1afcd3d7-3eb9-433c-be6e-72805fa6b882&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=324eef49&#x26;sv=2" alt="UCL app selection panel with checkboxes, Select Tools, and Confirm Action buttons"><figcaption></figcaption></figure>

{% hint style="info" %}
UCL handles all OAuth and API token management in the background.
{% endhint %}

## **Step 3: Setting Up Your Environment**

The **Embed** page on your UCL dashboard has step-by-step guides for a number of clients.&#x20;

In this case, you can use the Fastn UCL \[GitHub Template Starter] for embedding UCL into your custom AI Agent.

<figure><img src="../../../.gitbook/assets/image (596).png" alt="UCL Embed page showing step-by-step guides for connecting AI clients"><figcaption></figcaption></figure>

. ToWithin the first embedding step, we'll focus on setting up your codebase environment where you can embed UCL easily, to ensure an easy-to-follow process, you can find an example environment repository to clone below:

{% embed url="https://github.com/fastnai/embedded-multitenant-ai-assistant" %}

```
git clone https://github.com/fastnai/embedded-multitenant-ai-assistant.git
cd embedded-multitenant-ai-assistant
npm install
```

If you wish to run the code locally on your code editor, simply follow the README documentation within the GitHub repository.

### Environment via Code Editor

> Please ensure that you've read the ReadMe file in the GitHub repository before starting.

* Click on the code button to download the ZIP file.

<figure><img src="../../../.gitbook/assets/image (6) (1).png" alt="GitHub repository page for embedded-multitenant-ai-assistant with Code dropdown showing Clone and Download ZIP options"><figcaption></figcaption></figure>

* After downloading, open the file in your respective code editor.

### Setting up your Keys and IDs

* Once you've set up your code environment, you'll see a **.env file** that consists of two environment variables:

```
OPENAI_API_KEY

NEXT_PUBLIC_FASTN_MCP_SERVER_URL
```

<figure><img src="../../../.gitbook/assets/image (303).png" alt="VS Code editor showing the .env file with OPENAI_API_KEY and NEXT_PUBLIC_FASTN_MCP_SERVER_URL placeholder variables"><figcaption></figcaption></figure>

* Then head over to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys) and generate your API key. This API key will ensure that an LLM is integrated with your MCP.
* Head back to the **.env** file and insert your generated API key within the **OPENAI\_API\_KEY** environment variable.

> The **NEXT\_PUBLIC\_FASTN\_MCP\_SERVER\_URL** contains your Space ID and Tenant ID.
>
> Keep in mind that each workspace has a unique Space ID.

* In the next step for setting up the environment variables, copy the command, and paste it into the **NEXT\_PUBLIC\_FASTN\_MCP\_SERVER\_URL** variable in the **.env** file:&#x20;

<figure><img src="../../../.gitbook/assets/image (600).png" alt="UCL Embed page showing steps to clone the repo, generate an OpenAI API key, and set up environment variables with MCP server URL"><figcaption></figcaption></figure>

{% hint style="info" %}
You can check the **Multi Tenant** box above the Command code to enable multitenancy in your integrations.
{% endhint %}

## Step 4: Implementation

Now that you've set up everything, you'll now see UCL embedded in action, simply follow the steps below:

* Head over to your code editor, open your terminal, write and execute command:

```
npm run dev
```

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3iSr2Tx8FvvuoLPncziH%2Fuploads%2FoVXNCzJyqTWVaMRhpXUk%2Fnpm%20run%20dev%20Fastn%20UCL.mp4?alt=media&token=e4f90e2b-c523-4325-a6cd-eac4a365d6a4" %}

Once you have executed the command, you will see a local host site showcasing UCL embedded within an AI agent, where you can put your tools and tools to test as shown below:

<figure><img src="../../../.gitbook/assets/image (14) (1).png" alt="Demo app with AI Assistant chat showing a sent email confirmation and Available Apps panel with Gmail and Google Docs connected"><figcaption></figcaption></figure>

{% hint style="info" %}
You'll see your tools embedded on the web app as per the tools that you have enabled in the UCL "setup" section.
{% endhint %}

Additionally, in the **Tools** section of the demo app, you can also see the actions that you have enabled for each tool as shown below:

<figure><img src="../../../.gitbook/assets/image (15) (1).png" alt="Demo app Tools tab listing available actions including createDoc, updateDoc, getDoc, getDocs, sendMail, and getMessages"><figcaption></figcaption></figure>

## Environment via Codespaces - Alternative Method

{% hint style="info" %}
Alternatively, if you do not want to use your code editor, you can simply set up everything via GitHub Codespaces.
{% endhint %}

Codespaces provides a complete, pre-configured development environment in the cloud, allowing you to start coding instantly without worrying about local setup or dependencies.

* Simply access the repository → Click on **Code → Then click on "Create codespace on main"**

<figure><img src="../../../.gitbook/assets/image (431).png" alt="GitHub repository Codespaces tab with the Create codespace on main button"><figcaption></figcaption></figure>

* After creating a codespace environment you'll see a live code editor waiting for you

<figure><img src="../../../.gitbook/assets/image (5) (1).png" alt="GitHub Codespaces editor showing the .env file with environment variable placeholders for API key and MCP server URL"><figcaption></figcaption></figure>

{% hint style="info" %}
**From here on, you can simply follow the same steps as described in the** [**code editor**](embedding-ucl-onto-your-ai-agent.md#environment-via-code-editor) **section above.**
{% endhint %}

## **Conclusion**

UCL simplifies the process of embedding AI capabilities into your applications by providing a unified layer for connecting tools and managing multi-tenant workflows. Through its MCP server and Agent Connect component, developers can quickly implement secure, scalable integrations across different customer workspaces while maintaining proper isolation and authentication.

## **Next Steps:**

* Explore [Fastn Docs](https://docs.fastn.ai/)
* Or [request a demo](https://ucl.dev/) for advanced onboarding
