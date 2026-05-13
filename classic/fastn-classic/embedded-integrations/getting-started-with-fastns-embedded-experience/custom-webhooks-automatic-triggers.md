---
description: >-
  In Fastn, webhooks enable event-driven automation, so your workflows respond
  instantly to external changes without the need for constant checking or manual
  input.
---

# Custom Webhooks: Automatic Triggers

## What are Webhooks?

**Webhooks** are a way for applications to communicate with each other in real time. When something happens in one system, like a new order being placed or a form being submitted, it can send a message, known as a **webhook event**, to Fastn. This message can then automatically trigger a **flow** you've set up.

## Creating a Custom Webhook in Fastn

You can create a custom webhook tailored to your use case by following these steps:

### Registering a New Webhook

From the left side menu, navigate to the **Triggers** page and then click on **Add Webhook**.

<figure><img src="../../../../.gitbook/assets/image (339).png" alt=""><figcaption></figcaption></figure>

1. **Enter a Descriptive Name**\
   Provide a clear and meaningful name for your webhook to easily identify it later.
2. **Select an Event Model**\
   Choose the event model(s) that should apply to incoming input events for this webhook.
3. **Set a Webhook ID (Optional)**\
   Enter a unique identifier for the webhook if you want extra customization or tracking.
4. **Register the Webhook**\
   Click the **Register** button to complete the webhook setup and activate it.

## Routes

Routes provide you with a webhook URL that can be linked to a specific route. Each time this webhook URL is triggered externally, the route runs its assigned flow automatically.

Once you’ve registered your webhook, you can configure routes to define how incoming data should be processed.

<figure><img src="../../../../.gitbook/assets/image (340).png" alt=""><figcaption></figcaption></figure>

To add a new route, simply click on **“Add Route.”**

<figure><img src="../../../../.gitbook/assets/image (341).png" alt=""><figcaption></figcaption></figure>

1. **Provide a Name for the Route**\
   Give your route a clear, descriptive name to easily identify it later.
2. **Select the Destination API**\
   Choose the API endpoint where you want incoming data to be routed.
3. **Add Pattern Filters**\
   Pattern filters are conditions applied to incoming data that let you selectively process or route events based on specific criteria.

To configure a Pattern Filter, follow these steps:

1. **Open the Pattern Filters section** in your flow or widget settings.
2. **Add a key** — this is the parameter you want to filter by (e.g., `type`).
3. **Select an operator** — such as `Equals`, Prefix, or Suffix.
4. **Enter a value** — for example, `user`.

<figure><img src="../../../../.gitbook/assets/image (343).png" alt=""><figcaption></figcaption></figure>

5. **Add Headers:** After setting up patterns and filters to define how data is processed, you can further customize the outgoing HTTP request by adding headers.

{% hint style="info" %}
Headers allow you to include additional information or instructions for the destination receiving the webhook payload, such as authentication tokens, content types, or custom metadata.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (344).png" alt=""><figcaption></figcaption></figure>

### **How to Add Headers**

1. Click **Add** in the **Headers** section.
2. Enter the **key** for the header — for example, `Content-Type`.
3. Enter the **value** for the header — for example, `application/json`.
4. Add additional headers as needed—for example, a user token or API key.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeseaaxvgvXemv7gUAt7hHmdn9yYuOjgyZC2w8pHGjPZj_LgwvdS8kVqucG8fTeSncgg36sIUma3yaCiefS_bqAsl7L33r9nCTE3Q6Z8L1ehq_ncHr-AxVRfuLtvm5u6bxTPrvwag?key=aWFNWdC9I0x6b7wkwYQbDg" alt=""><figcaption></figcaption></figure>

6. **Batch Window:** Define the size of each batch to be processed. This controls how many events are grouped together before processing, optimizing performance and resource usage.
7. **Add Description:** After adding headers, it’s helpful to include a description for your webhook route. This provides context and clarifies the purpose or functionality of the route for future reference.

<figure><img src="../../../../.gitbook/assets/image (345).png" alt=""><figcaption></figcaption></figure>

6. **Save and Continue:** Click **Configure** to save your route settings, then click **Next** to proceed.

## Triggers

Once you’ve registered your webhook and configured its routes on Fastn.ai, you can optionally set up **triggers** to automate when your webhook and its associated workflows run.

Triggers enable you to schedule automatic executions based on your preferred timing or intervals—no manual intervention needed.

<figure><img src="../../../../.gitbook/assets/image (346).png" alt=""><figcaption></figcaption></figure>

Follow these steps to configure a trigger for your webhook:

1. **Enable Scheduling**\
   Click the **“Enable Schedule”** toggle to activate the scheduling feature.
2. **Select a Scheduling Option**\
   Choose between **Time-based** (specific times/dates) or **Rate-based** (fixed intervals) scheduling according to your needs.
3. **Choose the Destination API**\
   Select the API endpoint where the webhook payload should be sent when triggered.
4. **Save Your Trigger**\
   Click **Save** to confirm and activate your trigger settings.
