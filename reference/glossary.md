---
description: >-
  Alphabetized definitions of every term used across the fastn platform and
  documentation.
---

# Glossary

| Term                        | Definition                                                                                                                                                           | Where to find it                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **Connector**               | One app's definition in fastn: its actions, auth methods and webhooks. fastn maintains a catalog of them, and you can create your own. It holds no credentials. | Integrations → Connectors             |
| **Connection**              | One signed-in account on a connector, holding its credential. One connector can have many connections (for example, two Slack workspaces). | Operate → Connections                 |
| **SaaS connector** | Your product's connector, registered with its connection scopes. | [Build → Connect your product](../manage/saas-connectors.md) |
| **Connection scope** | One capability of your API, such as `billing`. Each customer holds one connection per connection scope. | [Build → Connect your product](../manage/saas-connectors.md) |
| **App** | Any other software a customer uses, such as a CRM, Jira or Slack. | [Integrations → Connectors](../build/connectors/the-catalogue.md) |
| **Workflow**                | The code that runs: a JavaScript module that moves and transforms data between apps. Usually written by Build with AI or your AI tool from a plain-language description; the code can be inspected. | Integrations → Workflows              |
| **Integration** | A connector, a connection, its triggers (app event, schedule or webhook) and the workflow logic around them, doing a job between your product and a customer's app. | [Onboarding → Choose integrations](../getting-started/onboarding/choose-integrations.md) |
| **Trigger**                 | What starts a workflow. Three types: Webhook, Schedule, App event.                                                                                                  | Integrations → Triggers               |
| **Customer**                | One of your customers: a company using your product. The API names it with `x-org-id` or `orgId`. Each customer's connections and data are isolated.                                                                    | Operate → Customers                   |
| **Organization** | In the dashboard, your organization: you, the SaaS company. Each of your customers is also stored as an organization under yours; you register it through the UI or the [Create a Customer Organization](../embed/embedding/integration-flow.md#create-a-customer-organization) API. API calls identify a customer by fastn's customer id or by your external reference for it (the `orgId` you set, which defaults to the customer's slug if you set none), sent as `x-org-id` or `orgId`. | Operate → Customers |
| **User** | A person at one of your customers who uses the embedded integrations. Each is identified by a user id you choose, sent as the `x-user-id` header. Sending a user id is optional. | The `x-user-id` header |
| **Identity hash** | Also written Identity-hmac, or the `x-identity-hmac` header. An HMAC-SHA256 of the org ID and user ID (newline-joined), signed with your identity-verification secret. It proves that your backend authorized that specific org and user pair. | [API keys → Identity hash](../manage/api-keys.md#identity-hash) |
| **Widget**                  | The embedded interface your customers use to connect apps and manage integrations inside your product.                                                               | Embed → Widget                        |
| **Onboarding**              | The guided setup at `/onboarding`, in four steps: Connect your product, Choose integrations, Embed the widget, Customers connect and customize. | [Onboarding](../getting-started/onboarding/README.md) |
| **Build with AI**           | fastn's builder: describe an integration and it picks the connectors, drafts the workflow and shows the diff. Opened from the Build with AI sidebar row, the Home prompt, or a connector. | Build → Build with AI                                            |
| **Agent**                   | Not a page. fastn's builder is **Build with AI** (called **fastn agent** in onboarding); Claude, Cursor and other MCP clients are **your AI tool**.                             | Build with AI; Embed → API keys and MCP                           |
| **AI tools** | Claude, ChatGPT, Gemini, Cursor and similar, connected to fastn through its MCP server. They use no AI credits. | [MCP gateway](../build/mcp-gateway/README.md) |
| **AI credits** | What fastn's agent (Build with AI) uses. Your plan includes a monthly allowance, and finishing onboarding adds 50 on top of it. | [Onboarding](../getting-started/onboarding/README.md) |
| **AI Assistant**            | A toggleable widget section that lets your customers describe an integration and have it built inside the widget.                                                       | Widget sections                       |
| **MCP Gateway**             | The endpoint that exposes integrations as tools for AI agents, over the Model Context Protocol. Has a Control Plane (Admin MCP) and a Data Plane (Customer Gateway). | Embed → API keys and MCP → MCP server (`/access?tab=mcp`) |
| **Embed token**             | A short-lived token (8-hour expiry, `emb_` prefix) generated from your backend that scopes an embedded widget to a specific customer.                             | Generated via the embed token API     |
| **API key**                 | A credential in `fsk_` format (`fsk_test_` or `fsk_live_`) used to authenticate backend API calls, including generating embed tokens.                                | Embed → API keys and MCP → API keys (`/access?tab=api-keys`) |
| **Execution tier**          | A workflow's runtime mode: Instant (synchronous, up to 25s, or 2 min where fastn has turned on the longer Instant timeout), Standard (async, up to 15min), or Long (async, up to 36 hours).                                                             | Workflow editor → Configuration       |
| **Dead Letter Queue (DLQ)** | An option on webhook triggers that captures failed events for later inspection or replay.                                                                            | Triggers → Webhook → Advanced options |
| **Organization level / User level**  | The two ways an integration's connections can be scoped: shared across a customer's whole organization (Organization level) or kept to each user at the customer (User level).                   | Set per integration in the widget (**Scope**) |
