# Troubleshooting

Common errors when embedding Fastn, with their causes and fixes.

### Blank embed / iframe renders nothing

**Most likely cause:** an expired or hardcoded token.

Embed tokens expire after 15 minutes. If a token is hardcoded into your frontend or cached and reused, it works until it expires, then the iframe loads blank with no obvious error.

**Fix:** Generate a fresh token from your backend on each page load. Never hardcode or cache tokens. See [Generating Embed Tokens](generating-embed-tokens.md).

**Also check:** In production, confirm `FASTN_API_KEY` is bound on the runtime, not just present in CI. An undefined API key means token generation fails silently. See [Deployment](deployment.md).

### 404 on the token request

**Most likely cause:** the wrong org identifier.

`endOrgId` must be the customer's internal UUID. The customer slug and the External ID both return 404.

### Requests fail with a test key

**Most likely cause:** the missing test-mode header.

Requests made with a `fsk_test_` key require the header `X-fastn-Test-Mode: true`. Without it, requests fail in ways the error message doesn't make obvious.

**Fix:** Add `X-fastn-Test-Mode: true` for test keys. Remove it for live keys. See [Authentication & API Keys](https://claude.ai/fastn/tutorials/developer/authentication-and-api-keys).

### "Failed to fetch" in the widget

**Most likely cause:** a tenancy or token mismatch.

This can appear when the iframe URL's tenancy shape doesn't match how the token was minted — for example, a single-tenant embed where the `tenant-id` and token identity don't line up.

**Fix:** Confirm the iframe URL matches your intended tenancy (see [Tenancy](understanding-tenancy.md)), and that the token was generated with the correct `endOrgId` and identity fields. Confirm the backend token pattern is being used rather than a hardcoded token.



### Empty response token

**Most likely cause:** reading the token from the wrong place in the response.

The token is nested under `data` in the response — `response.data.token`, not `response.token`.

**Fix:** Read `json.data.token`. See [Generating Embed Tokens](generating-embed-tokens.md).
