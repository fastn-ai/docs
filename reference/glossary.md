---
description: >-
  Alphabetized definitions of every term used across the Fastn platform and
  documentation.
---

# Glossary

| Term                        | Definition                                                                                                                                                           | Where to find it                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **Connector**               | A pre-built integration with a third-party system (Salesforce, Slack, Shopify, etc.). Handles authentication and exposes that system's actions.                      | Integrations → Connectors             |
| **Connection**              | An authenticated instance of a connector for a specific account. One connector can have multiple connections (e.g., two Slack workspaces).                           | Operate → Connections                 |
| **Workflow**                | An automation that moves and transforms data between systems. Built by AI agents from a plain-language description; the generated code can be inspected.             | Integrations → Workflows              |
| **Trigger**                 | What starts a workflow. Three types: Webhook, Scheduler, App Event.                                                                                                  | Integrations → Triggers               |
| **Customer**                | One company using your product. The API calls it an end org. Each customer's connections and data are isolated.                                                                    | Operate → Customers                   |
| **Widget**                  | The embedded interface your customers use to connect apps and manage integrations inside your product.                                                               | Embed → Widget                        |
| **Build with AI**           | fastn's builder: describe an integration and it picks the connectors, drafts the workflow and shows the diff. Opened from the Build with AI sidebar row, the Home prompt, or a connector. | Build → Build with AI                                            |
| **Agent**                   | Not a page. fastn's builder is **Build with AI** (**fastn agent** on Home's switch); Claude, Cursor and other MCP clients are **your AI tool**.                             | Build with AI; Embed → API keys and MCP                           |
| **AI Assistant**            | A toggleable widget section that lets your customers describe an automation and have it built inside the widget.                                                     | Widget sections                       |
| **MCP Gateway**             | The endpoint that exposes integrations as tools for AI agents, over the Model Context Protocol. Has a Control Plane (Admin MCP) and a Data Plane (Customer Gateway). | Widgets → Embed → MCP                 |
| **Embed token**             | A short-lived token (8-hour expiry, `emb_` prefix) generated from your backend that scopes an embedded widget to a specific customer.                             | Generated via the embed token API     |
| **API key**                 | A credential in `fsk_` format (`fsk_test_` or `fsk_live_`) used to authenticate backend API calls, including generating embed tokens.                                | Settings → API Keys                   |
| **Execution tier**          | A workflow's runtime mode: Instant (synchronous, up to 30s), Standard (async, up to 15min), or Long (async, up to 36h).                                                             | Workflow editor → Configuration       |
| **Dead Letter Queue (DLQ)** | An option on webhook triggers that captures failed events for later inspection or replay.                                                                            | Triggers → Webhook → Advanced options |
| **Org-level / User-level**  | The two ways a connection can be scoped: shared across a customer's whole organization (org-level) or isolated to an individual user (user-level).                   | Set via the embed iframe URL          |
