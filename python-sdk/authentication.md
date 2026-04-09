---
description: >-
  Manage OAuth connections to external services, check connection status, and
  configure custom auth providers.
---

# Authentication

The auth namespace manages OAuth connections between your end users and external services. Access it through `fastn.auth`.

{% hint style="info" %}
This page covers the **auth namespace** for managing end-user connections. For developer authentication (API keys and OAuth login), see [Configuration](configuration.md).
{% endhint %}

## `auth.connect()`

Initiate an OAuth flow for an end user to connect an external service.

```python
result = fastn.auth.connect(
    connector="slack",
    tenant_id="acme-corp",
    redirect_url="https://myapp.com/callback",
)

print(result["auth_url"])       # URL to redirect the user to
print(result["connection_id"])  # Connection ID to track this connection
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `connector` | `str` | Yes | Connector name (e.g., `"slack"`, `"github"`) |
| `tenant_id` | `str` | Yes | Tenant identifier for multi-tenant scoping |
| `redirect_url` | `str` | Yes | URL to redirect the user after authorization |

**Returns:** `dict` with:

| Field | Type | Description |
|-------|------|-------------|
| `connection_id` | `str` | Unique connection identifier |
| `auth_url` | `str` | OAuth authorization URL to redirect the user to |
| `status` | `str` | Connection status (initially `"pending"`) |
| `expires_in` | `int` | Seconds until the authorization link expires |

## `auth.status()`

Check the status of an existing connection. You can look up by `connection_id` or by `connector` + `tenant_id`.

```python
# Look up by connection ID
status = fastn.auth.status(connection_id="conn_abc")

# Look up by connector and tenant
status = fastn.auth.status(connector="slack", tenant_id="acme-corp")

print(status["status"])  # e.g., "active", "pending", "expired"
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection_id` | `str` or `None` | No | Connection ID to check |
| `connector` | `str` or `None` | No | Connector name (use with `tenant_id`) |
| `tenant_id` | `str` or `None` | No | Tenant ID (use with `connector`) |

Provide either `connection_id` **or** `connector` + `tenant_id`.

**Returns:** `dict` with:

| Field | Type | Description |
|-------|------|-------------|
| `connection_id` | `str` | Connection identifier |
| `connector` | `str` | Connector name |
| `status` | `str` | Connection status |
| `tenant_id` | `str` | Tenant identifier |
| `created_at` | `str` | Creation timestamp |

## `auth.configure_custom()`

Register a custom authentication provider by specifying an OpenID Connect userinfo endpoint.

```python
result = fastn.auth.configure_custom(
    userinfo_url="https://auth.myapp.com/.well-known/openid-configuration",
)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `userinfo_url` | `str` | Yes | OpenID Connect userinfo endpoint URL |

**Returns:** `dict` — Configuration result.

## OAuth device flow

The SDK uses OAuth 2.1 device authorization (RFC 8628) for developer authentication via `fastn login`. The following dataclasses and functions are available in `fastn.oauth`:

### DeviceCodeResponse

| Field | Type | Description |
|-------|------|-------------|
| `device_code` | `str` | Device code for polling |
| `user_code` | `str` | Code the user enters in the browser |
| `verification_uri` | `str` | URL the user visits |
| `verification_uri_complete` | `str` | URL with code pre-filled |
| `expires_in` | `int` | Seconds until expiration |
| `interval` | `int` | Polling interval in seconds |

### TokenResponse

| Field | Type | Description |
|-------|------|-------------|
| `access_token` | `str` | JWT access token |
| `refresh_token` | `str` | JWT refresh token |
| `expires_in` | `int` | Token lifetime in seconds |
| `token_type` | `str` | Token type (e.g., `"Bearer"`) |

### OAuth functions

| Function | Description |
|----------|-------------|
| `request_device_code()` | Request a device code from Keycloak for browser-based login |
| `poll_for_token(device_code, interval, expires_in)` | Poll the token endpoint until the user authorizes |
| `refresh_access_token(refresh_token)` | Refresh an expired access token |
| `fetch_userinfo(access_token)` | Fetch user profile from Keycloak (falls back to JWT decoding) |
| `is_token_expired(token_expiry)` | Check if a token is expired (with 30-second safety buffer) |
| `compute_token_expiry(expires_in)` | Compute ISO-8601 expiry timestamp from seconds |

## HTTP headers

Every API request includes these authentication headers:

| Header | Value | When |
|--------|-------|------|
| `x-fastn-api-key` | Your API key | API key authentication |
| `Authorization` | `Bearer <token>` | OAuth token authentication |
| `x-fastn-space-id` | Project ID | Always |
| `x-fastn-space-tenantid` | Tenant ID | Always |
| `realm` | `fastn` | Always |
| `stage` | `LIVE` (or configured stage) | Always |

## Async usage

All auth methods have async equivalents:

```python
async with AsyncFastnClient() as fastn:
    result = await fastn.auth.connect(
        connector="slack",
        tenant_id="acme-corp",
        redirect_url="https://myapp.com/callback",
    )
    status = await fastn.auth.status(connection_id=result["connection_id"])
```
