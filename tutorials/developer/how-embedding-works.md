---
---

# How Embedding Works

fastn is embedded into your product as an iframe. Your application renders the fastn widget, and your customers use it to connect their apps and configure integrations without leaving your product.

### How the pieces fit together

There are three parts:

**Your backend** generates a short-lived embed token by calling the fastn token endpoint with your API key. The token scopes the widget to a specific customer.

**Your frontend** renders the fastn iframe, passing the token in the URL. The iframe loads the widget your customers interact with.

**The fastn platform** validates the token, serves the widget, and handles the integration work - authentication with third-party apps, data sync, and workflow execution.

```
Your backend ──(API key)──> fastn token endpoint ──> short-lived token
     │
     └──> token ──> Your frontend ──> fastn iframe (with token) ──> Widget
```

### Iframe or SDK

The Embed tab in the widget builder offers two methods today: **Iframe** and **SDK**. Only **A2A** is marked coming soon. The SDK comes in four variants (Connect card, React component, Script tag and Build your own UI); see [SDK](../../embed/embedding/sdk.md).

This guide documents the iframe path. The SDK wraps the same flow: your backend still generates the token, and the SDK renders the iframe for you, so the token generation pattern you build here carries over.

### What you'll set up

1. A server-side function that generates an embed token on each request (never hardcode tokens: they expire in 8 hours).
2. A frontend component that renders the fastn iframe with the token.
3. A user id for each person at your customer, sent when you mint the token, so each person's session is scoped to them (see [Tenancy](understanding-tenancy.md)).

### Why generate tokens server-side

The token is minted from your API key. Your API key must never be exposed in client-side code. The token also expires after 8 hours, so it can't be generated once and reused; each page load needs a fresh token. Both of these require a backend step.

A common failure is hardcoding a token into the frontend during testing. It works for the first 8 hours, then the iframe renders blank with no obvious error. Generating the token server-side per request avoids this entirely.

### Next

Start with the [Quickstart](embedding-quickstart.md) to get a working embed, then read [Generating Embed Tokens](generating-embed-tokens.md) for the full token details.
