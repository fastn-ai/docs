---
description: Start a workflow for the right customer whenever something happens in your product.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Start an integration from your product's events

When something happens in your product, such as a new order, an integration should run for that customer, for example adding the order to their HubSpot. Your backend sends the event to a webhook trigger, signed for that customer, and fastn runs the workflow with that customer's setup.

<figure><img src="../.gitbook/assets/diagrams/run-for-a-customer.svg" alt="Running an integration for one customer: your backend calls fastn with x-org-id, fastn loads that customer's setup, calls their apps, and returns the result or an execution id."><figcaption><p>The signed x-org-id tells fastn whose setup to use.</p></figcaption></figure>

### Before you start

* A published workflow that takes the event as its input. See [Test and release](../build/workflows/lifecycle.md).
* An API key with **Verify caller identity (HMAC)** set to **Monitor only** or **Enforce**, and its identity secret. See [API keys](../manage/api-keys.md#identity-hash).
* A customer that has connected the apps the workflow uses.

### 1. Create the webhook trigger

1. Open **Integrations → Triggers** and click **Add trigger → Webhook**.
2. Enter a name, and add a route with your workflow as its **Workflow**.
3. Under **Advanced options**, set **Authentication** to API key.
4. Click **Create trigger**, then copy its URL from the row menu (**Copy URL**).

You can also ask the fastn agent to create it: *"Add a webhook trigger that runs the add-order-to-HubSpot workflow."*

### 2. Send the event from your backend

Name the customer and the user in `x-org-id` and `x-user-id`, and sign them with your identity secret:

```javascript
const crypto = require("crypto");

async function sendOrderEvent({ customerId, userId, order }) {
  const hmac = crypto.createHmac("sha256", process.env.FASTN_IDENTITY_SECRET)
    .update(`${customerId}\n${userId}`)
    .digest("hex");

  await fetch(process.env.FASTN_ORDER_WEBHOOK_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": process.env.FASTN_API_KEY,
      "x-org-id": customerId,
      "x-user-id": userId,
      "x-identity-hmac": hmac,
    },
    body: JSON.stringify(order),
  });
}
```

The JSON body arrives in the workflow as `ctx.input`.

{% hint style="warning" %}
`x-org-id` names the customer only when the key's identity verification is **Monitor only** or **Enforce**, or the call carries `x-identity-hmac`. Without that, the headers are only passed through to the workflow and do not name the customer.
{% endhint %}

### 3. Check it ran

**You should see:** the event in **Operate → Logs → Events** and the run in **Operate → Logs → Executions**.

If a delivery fails, fastn retries it with the trigger's **Max attempts** and **Backoff strategy**. Deliveries that run out of retries wait in the dead-letter queue, shown on **Health**.

### Related

* [Using a webhook trigger](../operate/triggers/using-a-webhook-trigger.md): every header and response
* [Webhook triggers](../build/triggers/webhooks.md): routes, retries, deduplication and execution mode
* [Run an integration for one customer](run-for-a-customer.md): call a workflow directly and read its result
