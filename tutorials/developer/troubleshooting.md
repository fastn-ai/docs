---
---

# Troubleshooting

Common errors when embedding fastn, with their causes and fixes.

### Blank embed / iframe renders nothing

**Most likely cause:** an expired or hardcoded token.

Embed tokens expire after 8 hours. If a token is hardcoded into your frontend or cached and reused, it works until it expires, then the iframe loads blank with no obvious error.

**Fix:** Generate a fresh token from your backend on each page load. Never hardcode or cache tokens. See [Generating Embed Tokens](generating-embed-tokens.md).

**Also check:** In production, confirm `FASTN_API_KEY` is bound on the runtime, not just present in CI. An undefined API key means token generation fails silently. See [Deployment](deployment.md).

### 404 on the token request

**Most likely cause:** the wrong customer identifier.

For `endOrgId`, use fastn's customer id, or the External ID shown on the customer (your own id if you set one when creating the customer; otherwise it defaults to the slug). An id that matches neither returns 404 `Tenant not found`.

### Requests fail with a test key

**Most likely cause:** the missing test-mode header.

Requests made with a `fsk_test_` key require the header `X-fastn-Test-Mode: true`. Without it, requests fail with 403 `Test API keys require X-fastn-Test-Mode: true header`.

**Fix:** Add `X-fastn-Test-Mode: true` for test keys. Remove it for live keys. See [Authentication & API Keys](authentication-and-api-keys.md).

### "Failed to fetch" in the widget

**Most likely cause:** a tenancy or token mismatch.

This can appear when the iframe URL's tenancy shape doesn't match how the token was minted - for example, a single-tenant embed where the `tenant-id` and token identity don't line up.

**Fix:** Confirm the iframe URL matches your intended tenancy (see [Tenancy](understanding-tenancy.md)), and that the token was generated with the correct `endOrgId` and identity fields. Confirm the backend token pattern is being used rather than a hardcoded token.



### Empty response token

**Most likely cause:** reading the token from the wrong place in the response.

The token is nested under `data` in the response - `response.data.token`, not `response.token`.

**Fix:** Read `json.data.token`. See [Generating Embed Tokens](generating-embed-tokens.md).
