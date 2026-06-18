# How Embedding Works

Fastn is embedded into your product as an iframe. Your application renders the Fastn widget, and your customers use it to connect their apps and configure integrations without leaving your product.

### How the pieces fit together

There are three parts:

**Your backend** generates a short-lived embed token by calling the Fastn token endpoint with your API key. The token scopes the widget to a specific customer.

**Your frontend** renders the Fastn iframe, passing the token in the URL. The iframe loads the widget your customers interact with.

**The Fastn platform** validates the token, serves the widget, and handles the integration work — authentication with third-party apps, data sync, and workflow execution.

```
Your backend ──(API key)──> Fastn token endpoint ──> short-lived token
     │
     └──> token ──> Your frontend ──> Fastn iframe (with token) ──> Widget
```

### The iframe is the current integration path

The Embed tab in the Widget Builder lists a React SDK, but it is marked "coming soon." Today, the supported method is the iframe. This guide documents the iframe path.

When the React SDK ships, it will wrap this same flow — your backend will still generate the token, and the SDK will render the iframe for you. The token generation pattern you build now will carry over.

### What you'll set up

1. A server-side function that generates an embed token on each request (never hardcode tokens — they expire in 15 minutes).
2. A frontend component that renders the Fastn iframe with the token.
3. A decision about how connections are scoped — shared across the customer's organization, or isolated per individual user (see [Tenancy](https://claude.ai/fastn/tutorials/developer/tenancy)).

### Why generate tokens server-side

The token is minted from your API key. Your API key must never be exposed in client-side code. The token also expires after 15 minutes, so it can't be generated once and reused — each page load needs a fresh token. Both of these require a backend step.

A common failure is hardcoding a token into the frontend during testing. It works for the first 15 minutes, then the iframe renders blank with no obvious error. Generating the token server-side per request avoids this entirely.

### Next

Start with the [Quickstart](https://claude.ai/fastn/tutorials/developer/quickstart) to get a working embed, then read [Generating Embed Tokens](https://claude.ai/fastn/tutorials/developer/generating-embed-tokens) for the full token details.
