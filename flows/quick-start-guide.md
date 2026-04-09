---
description: Build a working flow in under 10 minutes. No prior Fastn experience required.
---

# Quick Start Guide

In this quick start guide, you'll create a flow that listens for an incoming API request and sends a message to a Slack channel. By the end you will have a live, working automation running on Fastn.

### What you'll learn

* How to create a flow with an API request trigger
* How to add and configure your first connector step
* How to map incoming data to outgoing fields
* How to test and deploy your flow

**Estimated time:** 10 minutes

### Prerequisites

* A **Fastn account,** sign up at [fastn.ai](https://fastn.ai/) if you do not have one
* A **Slack workspace** where you can post messages (and permission to install apps)

### Step 1: Create a new flow

1. Click **Flows** in the left-hand menu.
2. Click **+ Create Flows** in the top-right corner.
3. Your new flow opens with a **New API Request** trigger already in place (labeled "Real Time").
4. Give your flow a descriptive name, such as `slacknotification`.

<figure><img src="../.gitbook/assets/part1.gif" alt="Animated demo of creating a new flow by clicking Flows in the menu, then Create Flows, and naming the flow"><figcaption></figcaption></figure>

### Step 2: Add a Slack connector

1. Click the **+** button below the trigger step on the canvas.
2. You see five tabs: **Trigger**, **Connection**, **AI**, **Transformation**, **Control**.
3. Click the **Connection** tab.
4. Click **Connector**.
5. Search for **Slack** and select it.
6. Ensure that you have authorized Slack for&#x20;
7. Choose the **sendMessage** action.

<figure><img src="../.gitbook/assets/part 2 connectors.gif" alt="Animated demo of adding a Slack connector step by selecting Connection tab, choosing Slack, and picking sendMessage"><figcaption></figcaption></figure>

### Step 3: Connect your Slack account

1. In the Slack connector step, click **Connect**.
2. A Slack authorization window opens. Select the workspace you want to connect.
3. Review the permissions and click **Allow**.
4. Once connected, your Slack account appears in the connector step.
5. Additionally, you will see a new Slack app pop up in your workspace as shown below:

<figure><img src="../.gitbook/assets/slack app connector.png" alt="Fastn UCL app in Slack workspace showing MCP Gateway description, key capabilities, and getting started steps"><figcaption></figcaption></figure>

> **Note:** Fastn manages OAuth tokens securely. Your application never sees raw Slack credentials.

### Step 4: Configure the Slack message

1. In the Slack connector step, fill in the required fields:

| Field        | Value                                                                      |
| ------------ | -------------------------------------------------------------------------- |
| `channel ID` | The Slack channel to post to, such as `#general`.                          |
| `text`       | The message body (you map this from the API request data in the next step) |

2. For the `channel` field, enter the name or ID of your target Slack channel which you can access from the your Slack channel details.

<figure><img src="../.gitbook/assets/slack channel id.png" alt="Slack channel details dialog with the Channel ID highlighted at the bottom in a red box"><figcaption></figcaption></figure>

### Step 5: Map request data to the Slack message

This is where the flow connects input to output. You map data from the incoming API request to the Slack message text.

1. Click the `text` field in the Slack connector configuration.
2. Use the data mapper to reference the incoming request. For example:

```
New request received: {{input.message}}
```

3. This maps the `message` field from the incoming API request payload into the Slack message text.

<figure><img src="../.gitbook/assets/data mapping.png" alt="Flow builder with data mapping panel open showing channel ID and message text fields mapped to incoming request data"><figcaption></figcaption></figure>

### Step 6: Test your flow

1. Click the **Test** button in the top-right corner of the flow builder.
2. Enter test input in JSON format:

```json
{
  "message": "Hello from my first Fastn flow!"
}
```

3. Click **Run**.
4. Check your Slack channel — the message "New request received: Hello from my first Fastn flow!" should appear.

<figure><img src="../.gitbook/assets/test success.gif" alt="Animated demo of running a flow test with JSON input and receiving a successful Slack message"><figcaption></figcaption></figure>

> If the test fails, check that your Slack account is connected and that the channel name is correct. The test console displays error details for each step.

### Step 7: Deploy your flow

1. Click the **Deploy** button in the top-right corner.
2. Confirm the deployment.
3. Your flow status changes to **Live**.

Your flow is now live and callable via API. You can find your API key in **Settings → API Keys** and include it as the `x-fastn-api-key` header in production requests.

<figure><img src="../.gitbook/assets/api key.gif" alt="Animated demo of deploying the flow and locating the API key in Settings"><figcaption></figcaption></figure>

### Troubleshooting

| Problem                       | Solution                                                                                           |
| ----------------------------- | -------------------------------------------------------------------------------------------------- |
| Slack message does not appear | Check that your Slack account is connected and the channel name is correct                         |
| Test returns an error         | Check the error details in the test console. Most common cause is a misconfigured field            |
| Flow shows "Changes Pending"  | You have unsaved changes. Click **Save**, then **Deploy** again                                    |
| API request returns 401       | Include the `x-fastn-api-key` header with a valid API key. Generate one in **Settings → API Keys** |
