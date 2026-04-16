---
description: >-
  This guide walks you through the process of setting up an MCP server from the
  UCL dashboard.
---

# Defining an MCP Server

The Unified Context Layer (UCL) allows you to define your own **MCP (Model Context Protocol) servers** and use them as tools within your workspace.

### Step 1: Access the Define MCP Server Option

* Log in to your UCL account at [**app.ucl.dev**](https://app.ucl.dev).
* Select your workspace.
* From the **Dashboard → Connect page**, click on **Define an MCP Server**.

<figure><img src="../../../.gitbook/assets/Screenshot 2025-10-03 195550.png" alt=""><figcaption></figcaption></figure>

* You will be taken to the **Create New MCP Tool** screen.

### Step 2: Add Tool Details

On this screen, you will provide the basic information for your MCP tool.

#### **Tool Details**

* **Tool Name** → Enter a name for your tool.
* **Description** → Briefly describe your tool.
* **Workspace** → Select the workspace.
* **Images (0/3)** → Optionally upload up to 3 images (e.g., `https://example.com/image.jpg`).
* **Mode** → Choose how the tool will appear:
  * Default
  * Light
  * Dark

<figure><img src="../../../.gitbook/assets/image (636).png" alt=""><figcaption></figcaption></figure>

Click **Next** to continue.

### Step 3: Configure Activation

Set up authentication and activation parameters for your MCP tool.

#### **Available Authentication Modes**

* **OAuth** → Enter OAuth secrets.
* **Basic** → Username/Password authentication.
* **API Key** → Provide an API key.
* **Bearer Token** → Token-based authentication.
* **Custom Input** → Define your own variable names and descriptions (e.g., `Instance ID`).

<figure><img src="../../../.gitbook/assets/image (638).png" alt=""><figcaption></figcaption></figure>

> You can set one of these methods as the **default**.
>
> Example: In _Custom Input_ mode, you may define `instanceId` as a required parameter for connecting.

Click **Next** to proceed.

### Step 4: Configure MCP Server

Provide the server connection details.

#### **Server Configuration**

* **Server URL** → Add the URL of your MCP server

```
 https://your-mcp-server.com
```

* **Headers** → Add any required headers (e.g., `instanceId`).

<figure><img src="../../../.gitbook/assets/image (639).png" alt=""><figcaption></figcaption></figure>

* **Query Parameters** → Add query parameters if needed.
* **Authentication Configuration** → Choose one:
  * No Authentication
  * Basic
  * Bearer
  * JWT Bearer
  * AWS Signature
  * API Key

<figure><img src="../../../.gitbook/assets/image (640).png" alt=""><figcaption></figcaption></figure>

Click **Next** to continue.

### Step 5: Test Connection

You will now see your MCP server details.

```
- Tool Name
- Server URL
- Connection Status: Ready to test connection
```

<figure><img src="../../../.gitbook/assets/image (641).png" alt=""><figcaption></figcaption></figure>

* Click **Test Connection**.
* If successful, you will see a notification: _“Connection Successful. Ready to complete setup.”_

### Step 6: Complete Setup

* Click **Complete Setup**.

<figure><img src="../../../.gitbook/assets/image (643).png" alt=""><figcaption></figcaption></figure>

* Your new MCP server will be added as a tool in your dashboard.

<figure><img src="../../../.gitbook/assets/image (644).png" alt=""><figcaption></figcaption></figure>

> You can now use it within your UCL workspace.
