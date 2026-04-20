---
description: >-
  Build a working webhook-to-Slack flow in under 10 minutes. No prior Fastn
  experience required.
---

# Build your first flow

In this tutorial you create a flow that listens for an incoming webhook and posts a message to a Slack channel. By the end you have a live, working automation running on Fastn.

**What you learn:**

* How to create a flow with a webhook trigger
* How to add and configure a Slack connector step
* How to map incoming data to outgoing fields
* How to test in DRAFT mode and deploy to LIVE

**Estimated time:** 10 minutes

## Prerequisites

Before you start, make sure you have:

* A **Fastn account** — sign up at [fastn.ai](https://fastn.ai) if you do not have one
* A **Slack workspace** where you can post messages (and permission to install apps)
* A tool for sending HTTP requests, such as `curl`, Postman, or any REST client

## Step 1: Create a new flow

1. Log in to your Fastn workspace and select your project.
2. Click **Flows** in the left-hand menu to open the Flows section.
3. Click **Create Flow** in the top-right corner.
4. Select **On Webhook Event** as the trigger type.

Fastn creates a new flow with a webhook trigger already in place. The flow canvas appears with the trigger step as the starting point.

{% hint style="info" %}
Each webhook flow gets a unique webhook URL. You use this URL later to send data into the flow.
{% endhint %}

5. Give your flow a descriptive name, such as `webhook-to-slack`.

<!-- TODO: Add screenshot of the Create Flow dialog with trigger type selection -->

## Step 2: Add a Slack connector

Next, add a step that sends a message to Slack.

1. Click the **+** button after the webhook trigger step on the canvas.
2. Select **Connector** from the list of available components.
3. In the connector selection panel, search for **Slack**.
4. Select **Slack** from the results.

<!-- TODO: Add screenshot of the connector search showing Slack -->

5. Choose the **sendMessage** endpoint from the list of available actions.

<!-- TODO: Add screenshot of the Slack endpoint selection -->

## Step 3: Connect your Slack account

Before Fastn can post messages, it needs access to your Slack workspace.

1. Click **Connect** in the Slack connector step.
2. A Slack authorization window opens. Select the workspace you want to connect.
3. Review the permissions and click **Allow**.
4. Once connected, your Slack account appears in the connector step.

{% hint style="info" %}
Fastn manages OAuth tokens securely in a SOC 2 certified vault. Your application never sees raw Slack credentials.
{% endhint %}

## Step 4: Configure the Slack message

Now configure what the Slack message looks like.

1. In the Slack connector step, fill in the required fields:

| Field | Value |
|-------|-------|
| `channel` | The Slack channel to post to, such as `#general` or a channel ID |
| `text` | The message body (you map this from webhook data in the next step) |

2. For the `channel` field, enter the name or ID of your target Slack channel.

## Step 5: Map webhook data to the Slack message

This is where the flow connects input to output. You map data from the incoming webhook payload to the Slack message text.

1. Click the `text` field in the Slack connector configuration.
2. Use the data mapper to reference the webhook input. For example:

```
New webhook received: {{input.message}}
```

This maps the `message` field from the incoming webhook payload into the Slack message text.

{% hint style="info" %}
You can reference any field from the incoming webhook payload using the pattern `{{input.<fieldName>}}`. To reference outputs from other steps, use `{{steps.<stepName>.output.<field>}}`. See [Data Mapping in Flows](flow-setup-essentials/designing-a-flow/data-mapping-in-flows.md) for the complete mapping reference.
{% endhint %}

3. Click **Save** to save the connector configuration.

<!-- TODO: Add screenshot of the data mapping configuration -->

## Step 6: Test your flow

Before deploying, verify that everything works using the built-in Debugger.

1. Click the **Test** button in the top-right corner of the flow canvas.
2. The Debugger opens and provides a test webhook URL.
3. Send a test request using `curl`:

```bash
curl -X POST <your-test-webhook-url> \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello from my first Fastn flow!"}'
```

4. Check the Debugger console for the execution result. You should see each step complete with a green checkmark.
5. Open your Slack channel — the message "New webhook received: Hello from my first Fastn flow!" should appear.

<!-- TODO: Add screenshot of the Debugger showing successful test run -->

{% hint style="warning" %}
If the test fails, check that your Slack account is connected and that the channel name is correct. The Debugger console displays error details for each step.
{% endhint %}

## Step 7: Deploy to LIVE

Once your test passes, deploy the flow so it runs on real webhook events.

1. Click the **Deploy** button in the top-right corner.
2. Select **LIVE** as the deployment stage.
3. Add an optional comment, such as "Initial deployment".
4. Click **Confirm**.

Your flow is now live. Fastn provides a production webhook URL that you can use from any external system.

<!-- TODO: Add screenshot of the Deploy dialog -->

## Step 8: Send a real webhook

Now test the live flow with a real request.

1. Copy the production webhook URL from the flow settings.
2. Send a request:

```bash
curl -X POST <your-production-webhook-url> \
  -H "Content-Type: application/json" \
  -H "x-fastn-api-key: <your-api-key>" \
  -d '{"message": "Production webhook is working!"}'
```

3. Check your Slack channel for the new message.

{% hint style="info" %}
You can find your API key in the project settings under **Generate API Key**. Include it as the `x-fastn-api-key` header in all production requests. See [Flow Settings](flow-setup-essentials/flow-settings/README.md) for authentication configuration details.
{% endhint %}

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Slack message does not appear | Verify your Slack account is connected and the channel name is correct. Check the Debugger console for error details. |
| Webhook URL returns 401 | Confirm you included the `x-fastn-api-key` header with a valid API key in your request. |
| Test passes but LIVE fails | Make sure you deployed the flow to the **LIVE** stage. DRAFT and LIVE have separate webhook URLs. |
| JSON parse error | Ensure your `curl` request includes `-H "Content-Type: application/json"` and the body is valid JSON. |

## What you built

You now have a working automation that:

* Listens for incoming webhooks
* Extracts data from the request payload
* Posts a formatted message to Slack
* Runs in production with a single API key for authentication

## Next steps

Now that you have built your first flow, explore these topics to go further:

* **[Flow Setup Essentials](flow-setup-essentials/README.md)** — learn about all five trigger types and flow components
* **[Designing a Flow](flow-setup-essentials/designing-a-flow/README.md)** — add switches, loops, variables, and custom code to your flows
* **[Connecting Apps](flow-setup-essentials/connecting-apps/README.md)** — connect to 250+ apps including Jira, GitHub, Salesforce, and more
* **[Data Mapping in Flows](flow-setup-essentials/designing-a-flow/data-mapping-in-flows.md)** — master the full data mapping syntax
* **[Flow Settings](flow-setup-essentials/flow-settings/README.md)** — configure validation, multi-tenancy, error handling, and async execution
