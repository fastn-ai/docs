---
description: Call a webhook trigger from your backend once it exists, with an example curl.
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

# Call a webhook trigger

At the end, your backend sends a request to a webhook trigger's URL and the trigger runs the workflows it is routed to.

### Before you start

* **A webhook trigger.** Build it in the dashboard, or have your AI tool build it through the [Fastn MCP server](../../build/mcp-gateway/README.md) or the [Fastn agent](../../build/agent/README.md). See [Webhook triggers](../../build/triggers/webhooks.md).
* **A Fastn API key** (`fsk_…`), if the trigger's authentication is API key, which is the default. See [API keys](../../manage/api-keys.md).

### Steps

1. **Copy the URL.** Go to **Build → Integrations → Triggers**, open the **Webhooks** tab, and select **Copy URL** or **Copy as cURL** in the trigger's row menu · [Open in Fastn](https://app.fastn.dev/integrations?tab=triggers).

   **You should see:** a URL of the form `https://webhooks.fastn.dev/prod/triggers/<ORG_ID>/webhooks/<WEBHOOK_ID>`. The first ID in the URL is your organization's ID.

2. **Send the request.** Call the URL from your backend with a request like this one:

   ```bash
   curl --location 'https://webhooks.fastn.dev/prod/triggers/<ORG_ID>/webhooks/<WEBHOOK_ID>' \
   --header 'Content-Type: application/json' \
   --header 'x-api-key: <YOUR_API_KEY>' \
   --data '{
   }'
   ```

   The API key is needed only when the trigger's authentication is API key. A trigger with no authentication accepts the call without it. You can send the `fsk_` key in any of these headers:

   * **`x-api-key`:** As in the example.
   * **`Authorization: Bearer fsk_…`:** The way the [platform API](../../reference/api.md#authentication) takes it.
   * **`x-fastn-access-key`:** The older header, still accepted.

   **You should see:** a `webhook` event for your call in **Operate → Logs → Events** · [Open in Fastn](https://app.fastn.dev/activity/events). To see what the workflow did with it, open [Executions](../executions.md).

### Name the customer the call is for

On a trigger whose authentication is API key, your backend can name the customer, and the person at the customer, that the call is for. Send the optional `x-org-id` and `x-user-id` headers, proven with `x-identity-hmac` (computed as in [Verify caller identity](../../manage/identity-verification.md)).

* **When the headers name the customer:** Only when your API key's identity verification is set to Monitor only or Enforce, or when the call carries `x-identity-hmac`.
* **Enforce:** A key set to Enforce refuses the call unless the headers come with a valid hash.
* **Otherwise:** On any other call, and on a trigger with no authentication, those headers are passed to the workflow as ordinary headers.

### What's next

* [Start an integration from your product's events](../../how-to/events-from-your-product.md): send a webhook from your product each time something happens there.
* [Events](../events.md): read, filter and replay the events your triggers receive.
