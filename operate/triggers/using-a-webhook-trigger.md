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

The key value comes from **Settings → API keys** (prefix `fsk_`). See [API keys](../../manage/api-keys.md).

<!-- TODO(eng): operate/triggers uses `x-api-key` while build/triggers/webhooks.md documents `x-api-key` (default) and still accepts `x-fastn-access-key`. Confirm whether the `x-api-key` alias is live in prod, and whether docs should standardize on one header name. -->

On a trigger whose auth is API key, your backend can also name the customer and end user the call is for with the optional `x-org-id` and `x-user-id` headers, proven with `x-identity-hmac`. These headers name the customer only when your API key's identity verification is set to optional or required, or when the call carries `x-identity-hmac`. Otherwise, and on a trigger with no auth, those headers are passed through to the workflow as ordinary headers.
