---
description: >-
  Tutorials for building on Fastn's platform from local dev setup, custom
  connectors, TypeScript workflows, deployment, AI agents, to MCP integration.
---

# Developer

These tutorials are for engineers building on top of Fastn's platform. You'll work with the CLI, write TypeScript, build custom connectors, deploy workflows to cloud infrastructure, and integrate AI agents via the MCP gateway.

### Tutorials in this section

[**Local Dev Environment Setup** ](local-dev-environment-setup.md)— Clone the repo, run the full platform stack locally with Docker Compose, and use the Fastn CLI for development.

[**Building a Custom Connector** ](building-a-custom-connector.md)— Implement the ConnectorDefinition interface to integrate an app that Fastn doesn't support out of the box.

[**Writing a Workflow (TypeScript)**](writing-a-workflow-via-typescript-dsl.md) — Write workflows as async functions using the code editor — ctx object, execution tiers, testing, and deployment patterns.

[**Deploying to Lambda / Cloud Run** ](deploying-to-lamba-cloud-run.md)— Deploy your workflows to AWS Lambda or GCP Cloud Run using the Fastn CLI and Pulumi infrastructure.

[**Creating a Custom AI Agent**](creating-a-custom-ai-agent.md) — Build a custom agent using the AgentTool interface or the Agent Builder's natural language lifecycle.

[**MCP Gateway Integration** ](mcp-gateway-integration.md)— Connect AI assistants to Fastn's MCP server — native tools, dynamic tools, and per-customer scoping.

If you're integrating Fastn into an existing AI product, skip to [MCP Gateway Integration](mcp-gateway-integration.md) directly.
