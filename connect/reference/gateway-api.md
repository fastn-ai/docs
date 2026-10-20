---
description: >-
  Reference for the Fastn Connect MCP endpoint: methods, authentication,
  request headers, tool naming, the per-user auth response, and status codes.
---

# Gateway API reference

**What this page answers**

* Which MCP methods does the gateway support?
* How does a caller authenticate?
* Which headers does a multi-tenant agent send?
* What does a "connect your account" response look like?
* What do the HTTP status codes mean?

### Endpoint

```
POST https://mcp.fastn.dev/<org>[/<workspace>]
```

Standard MCP (JSON-RPC 2.0) over Streamable HTTP. The gateway implements `initialize`, `tools/list` and `tools/call`. Every [URL form](gateway-urls.md) speaks the same protocol. Send `Accept: application/json, text/event-stream`.

### Authentication

| Method | How | For |
| --- | --- | --- |
| **OAuth (sign-in)** | The client discovers the authorisation server from `https://mcp.fastn.dev/.well-known/oauth-protected-resource`, the person signs in at `connect.fastn.dev` and consents, and the client receives a token. Standard MCP authorisation: dynamic client registration and PKCE. | People using Claude, ChatGPT, Cursor and so on. |
| **Access key** | `Authorization: Bearer ucl_<key>`. Shown once at creation, stored only as a hash. | Agents, scripts, clients without OAuth. |
| **OAuth client credentials** | `POST https://connect.fastn.dev/oauth/token` with `grant_type=client_credentials`, `client_id`, `client_secret`; then `Authorization: Bearer <access_token>`. | Services. |
| **mTLS** | A client certificate, in addition to a bearer credential, when the organisation requires it. | Enterprise. |

An unauthenticated request gets `401` with a `WWW-Authenticate: Bearer resource_metadata="..."` header pointing at the protected-resource document, which is how MCP clients start sign-in.

Create keys and OAuth clients on [Agents](../agents/README.md).

### Request headers

| Header | Required | Meaning |
| --- | --- | --- |
| `Authorization` | Yes | `Bearer <access key or token>`. |
| `X-Org-Id` | Multi-tenant keys | The end-org (your customer) the call is for. |
| `X-User-Id` | Multi-tenant keys, for per-user apps | The end user to act as. Required on every call if the key has **Require an end user**. |
| `X-Identity-Hmac` | When the key enforces identity verification | Hex HMAC-SHA256 of `<org id>\n<user id>` with the key's verification secret. |
| `X-Connection-Id` | No | Picks one account when the identity has several for the same app. |

Single-org keys and signed-in people do not send `X-Org-Id` or `X-User-Id`. See [Multi-tenant agents](../agents/multi-tenant.md).

### Tool names

Tools are namespaced `<connector>__<tool>`, for example `slack__send_message`. With **Smart** loading or a **Search-first** key, the client also gets two gateway tools:

* `search_tools`: find tools across every app in the workspace.
* `run_tool`: run a tool found by search.

### When an account is not connected

On an app where each person signs in, a call from someone who has not connected returns a tool result (not a protocol error) with `isError: true`:

```json
{
  "isError": true,
  "content": [
    {
      "type": "text",
      "text": "Authorization required: the Slack account isn't connected.\n\nhttps://connect.fastn.dev/...\n\n[Connect Slack](https://connect.fastn.dev/...)\n\nOpen the link to authorize your Slack account, then run the tool again."
    }
  ],
  "structuredContent": {
    "authRequired": true,
    "authorizeUrl": "https://connect.fastn.dev/..."
  }
}
```

If a stored credential was rejected, `structuredContent.reason` is `credential_rejected` and the text asks the user to reconnect. An agent should show the link to its user and retry after they connect.

### Status codes

| Code | Meaning | What to do |
| --- | --- | --- |
| `400` | A required header is missing or invalid, for example no `X-User-Id` on a key with **Require an end user**, or `X-User-Id: default`. | Send the header the message names. |
| `401` | Missing, invalid, expired or revoked credential; a token used on a URL it was not issued for; or a bad or missing `X-Identity-Hmac` on a key that enforces identity verification. | Clients re-run sign-in. For keys, check the key, URL and identity hash. |
| `402` | The organisation's monthly plan quota is used up. | Upgrade, or wait for the month to reset. |
| `403` | The caller may not make this call. The message says why, for example: the key's IP rules block the client; the `X-Org-Id` is not in the key's allowed orgs; the URL's org does not match the key's org; the organisation requires a client certificate (mTLS); agent access is turned off for the organisation; or a single-app token was used for another app. | Fix the cause named in the message. |
| `404` | Not an MCP path, or the organisation or workspace does not exist. | Copy the URL from Home. |
| `429` | Rate limit, concurrency or the daily or weekly ceiling. Includes `Retry-After`. | Back off and retry after the given seconds. |

A call refused by a policy is reported as a failed tool result, and shows as **policy** in Monitor and **Refused** in Audit.

### Per-call identity override

On connectors that can run as either the organisation's account or the user's own, a call can pass a reserved `_identity` argument of `"org"` or `"user"` to choose. The gateway strips it before the call reaches the app. A connector pinned to one mode (for example, one shared account, or per-user only) rejects a conflicting override with `403`.
