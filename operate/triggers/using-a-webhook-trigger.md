---
description: Call a webhook trigger from your backend once it exists, with an example curl.
---

# Using a webhook trigger

Once the webhook trigger is built, in the dashboard, with Build with AI or with your AI tool, it can be called as shown by the example curl below. The first ID in the URL is your organization's ID.

```bash
curl --location 'https://webhooks.fastn.dev/prod/triggers/<ORG_ID>/webhooks/<WEBHOOK_ID>' \
--header 'Content-Type: application/json' \
--header 'x-api-key: <YOUR_API_KEY>' \
--data '{
}'
```

The `x-api-key` header is needed only when the trigger's auth is set to API key. A trigger with no auth accepts the call without it.

On a trigger whose auth is API key, your backend can also name the customer and end user the call is for with the optional `x-org-id` and `x-user-id` headers, proven with `x-identity-hmac`. These headers name the customer only when your API key's identity verification is set to optional or required, or when the call carries `x-identity-hmac`. Otherwise, and on a trigger with no auth, those headers are passed through to the workflow as ordinary headers.
