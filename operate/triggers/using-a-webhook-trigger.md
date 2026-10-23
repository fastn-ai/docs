---
description: Call a webhook trigger from your backend once it exists, with an example curl.
---

# Using a webhook trigger

Once the webhook trigger is built through the UI or through the agent it can be triggered as shown by the example curl below.

```bash
curl --location 'https://webhooks.fastn.dev/prod/triggers/<WORKSPACE_ID>/webhooks/<WEBHOOK_ID>' \
--header 'Content-Type: application/json' \
--header 'x-api-key: <YOUR_API_KEY>' \
--header 'x-org-id: <ORG_ID>' \
--header 'x-user-id: <USER_ID>' \
--header 'x-identity-hmac: <IDENTITY_HASH>' \
--data '{
}'
```

## Getting a result back

The webhook doesn't return the workflow's result. It replies `202 Accepted` as soon as it receives the event, before the workflow runs. If your product needs an answer, such as the ID of a ticket the workflow opened, have the workflow call your product back.

1. Put your own ID for the record in the webhook body, such as `findingId`. The workflow reads it from [`ctx.input`](../../reference/workflow-runtime.md).
2. The workflow does the work, such as creating a ticket, and saves both IDs in `fastn.state`. If the same event arrives twice, it finds the saved ticket instead of opening a second one ([Idempotent event sync](../../build/patterns.md#idempotent-event-sync)).
3. The workflow calls your product through your [connector](../../build/connectors/README.md) with both IDs. Your product finds the record by its own ID.

```javascript
const { findingId, title } = ctx.input;
const key = `finding-ticket:${findingId}`;

let link = await fastn.state.get(key);
if (!link) {
  const ticket = await fastn.connector.jira.createIssue({ summary: title });
  link = { ticketId: ticket.id };
  await fastn.state.set(key, link);
}

await fastn.connector.yourproduct.updateFinding({ findingId, ticketId: link.ticketId });
return { success: true, findingId, ticketId: link.ticketId };
```

The connector and action names are examples. Your connector needs an action for the callback, such as "update finding". If another workflow needs the saved IDs later, use a `fastn.db` table instead ([Backfill without disturbing the live sync](../../build/patterns.md#backfill-without-disturbing-the-live-sync)).
