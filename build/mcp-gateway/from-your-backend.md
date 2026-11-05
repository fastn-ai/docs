---
description: Connect a backend service to the MCP gateway with OAuth (authorization code, refresh token, or client credentials).
---

# From your backend

AI clients such as Claude and Cursor walk through the OAuth browser flow for you. A backend service talks to the same authorization server directly: register a client, obtain a token, then call the [MCP gateway](README.md) with that token in the `Authorization` header.

## Authorization server

The gateway's protected-resource metadata points at **connect.fastn.dev** as the authorization server. Its OAuth metadata advertises:

| Endpoint | Path |
| -------- | ---- |
| Authorize | `/oauth/authorize` |
| Token | `/oauth/token` |
| Dynamic client registration | `/oauth/register` |

| Capability | Value |
| ---------- | ----- |
| Grant types | `authorization_code`, `refresh_token`, `client_credentials` |
| PKCE | `S256` |
| Scope | `mcp` |
| Bearer delivery | `Authorization` header only |

Full URLs:

* `https://connect.fastn.dev/oauth/authorize`
* `https://connect.fastn.dev/oauth/token`
* `https://connect.fastn.dev/oauth/register`

## Obtain a token

Pick the grant that matches how your service runs:

* **Authorization code + PKCE (`S256`)** — a user or operator signs in once; your backend stores the refresh token and renews access tokens as needed. Use this when a person must consent for the workspace.
* **Client credentials** — a non-interactive service authenticates as itself. Use this for scheduled jobs and server-to-server callers that should not open a browser.

Register the client at `/oauth/register` (dynamic client registration) unless you already have client credentials from your Fastn workspace.

Request scope `mcp` on the authorize or token call.

## Call the gateway

Send the access token as a Bearer token in the `Authorization` header only — query-string and other header forms are not supported:

```http
Authorization: Bearer <access_token>
```

Point the MCP client or HTTP caller at your workspace gateway URL (see [MCP gateway](README.md)). A missing or invalid token returns **401**; see [Troubleshooting](../../operate/troubleshooting.md#mcp-gateway-returns-401).

{% hint style="info" %}
For interactive AI tools (Claude, Cursor, VS Code, and the others in this section), prefer the per-tool guides — they handle OAuth in the client UI. This page is for backends and scripts that speak OAuth themselves.
{% endhint %}

<!-- TODO(eng): confirm client_credentials access-token lifetime and which org/workspace the token is bound to. Also confirm whether a `ucl_` access key is the "workspace key" expected by the SDK (see reference/sdk/workspace-tools.md), or whether backends should use OAuth only. -->
