---
description: >-
  Tutorials for building on Fastn's platform from local dev setup, custom
  connectors, TypeScript workflows, deployment, AI agents, to MCP integration.
---

# Developer

This section is dedicated for developers embedding Fastn into their own product. Your customers use the embedded widget to connect their apps and configure integrations; your job is to render that widget inside your application and generate the tokens that scope it to each customer.

You don't run Fastn locally or build the integration infrastructure yourself. Fastn runs as a hosted platform. You embed its widget as an iframe, generate a short-lived token from your backend, and decide how connections are scoped to your customers.

### In this section

[**How Embedding Works**](how-embedding-works.md) — The embedding model: how the iframe, the token, and your backend fit together.

[**Embedding Quickstart**](embedding-quickstart.md) — Generate a token, render the iframe, and see a working connection.

[**Generating Embed Tokens**](generating-embed-tokens.md) — The token endpoint, the server-side pattern, and token lifecycle.

[**Authentication & API Keys**](authentication-and-api-keys.md) — Test vs live keys and the headers each requires.

[**Finding Your Org Identifier**](finding-your-org-identifier.md) — Locating the `endOrgId` your token and iframe calls need.

[**Understanding Tenancy**](understanding-tenancy.md) — The two ways connections can be scoped, and how to choose.

[**Deployment**](deployment.md) — Environment variables and deploy-time considerations.

[**MCP Gateway Integration**](mcp-gateway-integration.md) — Exposing integrations as tools for AI agents.

[**Troubleshooting**](troubleshooting.md) — Common errors and their causes.
