---
description: >-
  Alphabetized definitions of every term used across the Fastn platform and
  documentation.
---

# Glossary

| Term                        | Definition                                                                                                                                                           | Where to find it                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **Connector**               | A pre-built integration with a third-party system (Salesforce, Slack, Shopify, etc.). Handles authentication and exposes that system's actions.                      | Integrations → Connectors             |
| **Connection**              | An authenticated instance of a connector for a specific account. One connector can have multiple connections (e.g., two Slack workspaces).                           | Integrations → Connections            |
| **Workflow**                | An automation that moves and transforms data between systems. Built by AI agents from a plain-language description; the generated code can be inspected.             | Integrations → Workflows              |
| **Trigger**                 | What starts a workflow. Three types: Webhook, Scheduler, App Event.                                                                                                  | Integrations → Triggers               |
| **Customer**                | An end user organization of your SaaS product. Each customer's connections and data are isolated.                                                                    | Settings → Customers                  |
| **Widget**                  | The embedded interface your customers use to connect apps and manage integrations inside your product.                                                               | Widgets → Widget Builder              |
| **Setup Assistant**         | The AI-guided onboarding wizard that configures a new SaaS partner's integration platform (Use cases → Connectors → Workflows → Embed → Live).                       | Home page                             |
| **Build with AI**           | The label for the AI integration/workflow builder.                                                                                                                   | Workflows tab; embedded widget        |
| **Agent**                   | The Integrations sub-tab where you describe an integration and the AI agents build it.                                                                               | Integrations → Agent                  |
| **AI Assistant**            | A toggleable widget section that lets your customers describe an automation and have it built inside the widget.                                                     | Widget sections                       |
| **MCP Gateway**             | The endpoint that exposes integrations as tools for AI agents, over the Model Context Protocol. Has a Control Plane (Admin MCP) and a Data Plane (Customer Gateway). | Widgets → Embed → MCP                 |
| **Embed token**             | A short-lived token (15-minute expiry, `emb_` prefix) generated from your backend that scopes an embedded widget to a specific customer.                             | Generated via the embed token API     |
| **API key**                 | A credential in `fsk_` format (`fsk_test_` or `fsk_live_`) used to authenticate backend API calls, including generating embed tokens.                                | Settings → API Keys                   |
| **Execution tier**          | A workflow's runtime mode: Instant (synchronous, ≤60s), Standard (async, ≤15min), or Long (async, ≤6hr).                                                             | Workflow editor → Configuration       |
| **Dead Letter Queue (DLQ)** | An option on webhook triggers that captures failed events for later inspection or replay.                                                                            | Triggers → Webhook → Advanced options |
| **Org-level / User-level**  | The two ways a connection can be scoped: shared across a customer's whole organization (org-level) or isolated to an individual user (user-level).                   | Set via the embed iframe URL          |
