---
description: >-
  Tutorials for building on Fastn's platform from local dev setup, custom
  connectors, TypeScript workflows, deployment, AI agents, to MCP integration.
hidden: true
---

# Developer

This section is dedicated for developers embedding Fastn into their own product. Your customers use the embedded widget to connect their apps and configure integrations; your job is to render that widget inside your application and generate the tokens that scope it to each customer.

You don't run Fastn locally or build the integration infrastructure yourself. Fastn runs as a hosted platform. You embed its widget as an iframe, generate a short-lived token from your backend, and decide how connections are scoped to your customers.

### In this section

[**Embedding Fastn**](https://claude.ai/fastn/tutorials/developer/embedding-fastn) — The embedding model: how the iframe, the token, and your backend fit together.

[**Quickstart**](https://claude.ai/fastn/tutorials/developer/quickstart) — Generate a token, render the iframe, and see a working connection.

[**Generating Embed Tokens**](https://claude.ai/fastn/tutorials/developer/generating-embed-tokens) — The token endpoint, the server-side pattern, and token lifecycle.

[**Authentication & API Keys**](https://claude.ai/fastn/tutorials/developer/authentication-and-api-keys) — Test vs live keys and the headers each requires.

[**Finding Your Org Identifier**](https://claude.ai/fastn/tutorials/developer/finding-your-org-identifier) — Locating the `endOrgId` your token and iframe calls need.

[**Tenancy: Org-level vs User-level**](https://claude.ai/fastn/tutorials/developer/tenancy) — The two ways connections can be scoped, and how to choose.

[**Connectors vs Raw REST**](https://claude.ai/fastn/tutorials/developer/connectors-vs-raw-rest) — When to use a first-party connector instead of calling an API directly.

[**Deployment**](https://claude.ai/fastn/tutorials/developer/deployment) — Environment variables and deploy-time considerations.

[**MCP Gateway Integration**](https://claude.ai/fastn/tutorials/developer/mcp-gateway-integration) — Exposing integrations as tools for AI agents.

[**Troubleshooting**](https://claude.ai/fastn/tutorials/developer/troubleshooting) — Common errors and their causes.

### Prerequisites

* A Fastn account with a published widget (see [Building Your Widget](https://claude.ai/fastn/tutorials/saas-admin/building-your-widget))
* An API key (see [Authentication & API Keys](https://claude.ai/fastn/tutorials/developer/authentication-and-api-keys))
* A backend you can run a token-generation function on
