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
Once the webhook trigger is built, in the dashboard, with the fastn agent or with your AI tool, call it with a request like the one below. The first ID in the URL is your organization's ID.

```bash
curl --location 'https://webhooks.fastn.dev/prod/triggers/<ORG_ID>/webhooks/<WEBHOOK_ID>' \
--header 'Content-Type: application/json' \
--header 'x-api-key: <YOUR_API_KEY>' \
--data '{
}'
```

The `x-api-key` header is needed only when the trigger's auth is set to API key. A trigger with no auth accepts the call without it.

The key is your `fsk_` key, in `x-api-key`, as `Authorization: Bearer fsk_…` (the way the [platform API](../../reference/api.md#authentication) takes it), or in the older `x-fastn-access-key`.

On a trigger whose auth is API key, your backend can also name the customer and the person at the customer the call is for with the optional `x-org-id` and `x-user-id` headers, proven with `x-identity-hmac` (computed as in [Verify caller identity](../../manage/identity-verification.md)). These headers name the customer only when your API key's identity verification is set to Monitor only or Enforce, or when the call carries `x-identity-hmac`. A key set to Enforce refuses the call unless they come with a valid hash. Otherwise, and on a trigger with no auth, those headers are passed through to the workflow as ordinary headers.
