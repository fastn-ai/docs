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

The `x-user-id` and `x-identity-hmac` headers are optional.
