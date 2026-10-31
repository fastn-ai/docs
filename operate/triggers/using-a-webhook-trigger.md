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

The API key goes in `x-api-key`, as above, or in `x-fastn-access-key`: your `fsk_` key either way. A webhook URL does not read `Authorization`, so a bearer token here is answered `401`, even though `Authorization: Bearer` is how the [platform API](../../reference/api.md#authentication) takes the same key.

`x-org-id`, `x-user-id` and `x-identity-hmac` say which of your customers, and which user, the event is for. `x-org-id` is your id for the customer (or fastn's), `x-user-id` is optional, and the hash is computed as in [API keys](../../manage/api-keys.md#identity-hash). A key with **Verify caller identity (HMAC)** set to Enforce refuses the call unless they come with a valid hash. With a key that has no identity verification, `x-org-id` and `x-user-id` sent without `x-identity-hmac` reach the workflow as ordinary headers, and do not name the customer.
