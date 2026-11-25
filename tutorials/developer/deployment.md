---
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

# Deployment

When you deploy the application you've embedded fastn into, the main consideration is how environment variables and secrets bind on your deploy target. Getting this wrong is a common cause of a working local build that fails in production.

### Environment variables: runtime vs build time

Your embedded integration needs `FASTN_API_KEY`, your `fsk_` API key, available to the server-side function that generates embed tokens.

The customer id you send as `x-org-id` is not an environment variable. Read it from the signed-in user's session on each request; see [Find your org identifier](finding-your-org-identifier.md). A fixed `FASTN_ORG_ID` is only for a local test with one customer.

On some hosts, environment variables set in a CI pipeline are not automatically available to the deployed runtime. They bind at deploy time on the hosting target, not from the pipeline's own secrets. If the token function reads an undefined API key in production, token generation fails and the embed renders blank.

### Checklist for deploying

1. Set `FASTN_API_KEY` directly on the hosting target (not only in CI).
2. Use a `fsk_live_` key in production (and drop the `X-fastn-Test-Mode` header; see [Authentication](authentication-and-api-keys.md)).
3. Redeploy after changing environment variables, if your host binds them at deploy time.
4. Paste secret values raw, with no surrounding quotes or brackets.
5. Confirm the token endpoint is reachable from your deployed backend.

### Verifying after deploy

Load the embedded page in production and confirm that the widget renders and that a fresh token is generated on each load. If the widget is blank, check that the environment variables are bound on the runtime, not only present in CI. See [Troubleshooting](troubleshooting.md).
