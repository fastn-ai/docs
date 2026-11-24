---
description: >-
  Tutorials for developers embedding fastn in their product: embed tokens, API
  keys, customer identifiers, connection scope, deployment and MCP.
hidden: true
---

# Developer tutorials

This section is for developers embedding fastn into their own product. Your customers use the embedded widget to connect their apps and configure integrations; your job is to render that widget inside your application and generate the tokens that scope it to each customer.

You don't run fastn locally or build the integration infrastructure yourself. fastn runs as a hosted platform. You embed its widget as an iframe, generate a short-lived token from your backend, and decide how connections are scoped to your customers.

### In this section

[**How Embedding Works**](how-embedding-works.md) - The embedding model: how the iframe, the token, and your backend fit together.

[**Embedding Quickstart**](embedding-quickstart.md) - Generate a token, render the iframe, and see a working connection.

[**Generating Embed Tokens**](generating-embed-tokens.md) - The token endpoint, the server-side pattern, and token lifecycle.

[**Authentication & API Keys**](authentication-and-api-keys.md) - Test vs live keys and the headers each requires.

[**Finding Your Org Identifier**](finding-your-org-identifier.md) - Locating the customer identifier your token request needs.

[**Understanding Tenancy**](understanding-tenancy.md) - The two ways connections can be scoped, and how to choose.

[**Deployment**](deployment.md) - Environment variables and deploy-time considerations.

[**fastn MCP server**](../../build/mcp-gateway/README.md) - Connect your AI tool, such as Claude or Cursor, to build and manage integrations; fastn Connect gives AI agents your customers' connected apps as tools.

[**Troubleshooting**](troubleshooting.md) - Common errors and their causes.
