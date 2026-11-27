---
description: Everything Fastn runs for you, so you don't have to build and maintain it yourself.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Features

Each feature below is something Fastn runs for you, so you don't have to build and maintain it yourself.

| Feature | What Fastn does | What you don't have to build |
| --- | --- | --- |
| **Sign-in and credentials** | The widget runs each app's own OAuth or API-key sign-in. Fastn stores every credential encrypted, scoped to one customer, and renews OAuth tokens. [Learn more](../build/connections/README.md) | An OAuth flow per app, a credential store, and token refresh. |
| **Customer isolation** | Your backend creates a short-lived token for one customer. The widget, API calls and runs see only that customer's connections and data. [Learn more](../tutorials/developer/understanding-tenancy.md) | Customer separation in every integration, and the risk of one customer's data reaching another. |
| **Connector catalog** | Over 1,000 connectors, each with its actions, sign-in methods and webhooks, plus unified APIs that work the same way across every app of a kind, such as every CRM. [Learn more](../build/connectors/the-catalogue.md) | A client for each app's API, and a separate code path per CRM or helpdesk. |
| **Building with AI** | Describe an integration to your AI tool through the Fastn MCP server (every plan), or to the Fastn agent (Scale or Enterprise). It picks the connectors, writes the workflow and tests it. [Learn more](../build/mcp-gateway/README.md) | Hand-written workflows, and developer time for every new integration request. |
| **Fine-tuning for each customer** | Every customer can adjust an integration to fit their own use case, for example its field mappings, filters and sync direction, in the widget or by asking the widget assistant. Changes apply only to that customer. [Learn more](../tutorials/end-user/customizing-your-integrations.md) | Custom builds and forks for individual customers. |
| **Running workflows** | Workflows run on a webhook, a schedule or an app event: for up to 25 seconds while the caller waits, or in the background for long jobs. Fastn handles each app's rate limits, retries temporary failures, and keeps deliveries that still fail in a dead-letter queue, a holding area for failed deliveries. [Learn more](../build/workflows/README.md) | Queues, workers, schedulers, retry logic and rate-limit handling. |
| **Insights and alerts** | Every event, run and app call is logged per customer. Your team sees what needs attention in **Health** and gets alerts by email, Slack, Microsoft Teams or webhook. Customers can review logs and metrics for their own integrations and set their own alerts. [Your alerts](../operate/alerts.md) · [Customers' alerts](../tutorials/end-user/getting-alerted.md) | Logging, dashboards and alerts per integration, and tracing which customer a failure hit. |
| **Maintainer agent** | Watches the apps you use and tells you when a third-party app changes its API. It proposes a fix in **Health → Pending updates** and helps you deploy the update your integrations need. Nothing changes until you accept it. [Learn more](../build/connector-updates.md) | Tracking every vendor's changelog, and fixing breakages after customers report them. |
| **AI agent access** | Fastn Connect gives your AI agents one customer's connected apps as tools. Every call is checked against your policies, logged, and runs with that customer's account. [Learn more](../reference/ai-agents.md) | A separate sign-in and tool layer for your agents, and agents holding raw customer credentials. |
