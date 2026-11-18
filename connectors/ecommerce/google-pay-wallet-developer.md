---
description: "Google Pay & Wallet Developer MCP server (https://paydeveloper.googleapis.com/mcp), Google's hosted remote Model Context Protocol server for Google Pay and…"
hidden: true
---

# Google Pay & Wallet Developer

Google Pay & Wallet Developer MCP server (https://paydeveloper.googleapis.com/mcp), Google's hosted remote Model Context Protocol server for Google Pay and Google Wallet developers. Its tools are discovered live from the server and include search_documentation, list_merchants, list_google_pay_integrations, create_merchant, update_merchant, query_merchant_performance, query_merchant_error_metrics, list_principals, set_principal_role, delete_principal, list_pass_issuers, list_pass_classes and validate_pass_jwt. The server accepts OAuth 2.0 only (no API keys); this connector requests the scopes paydeveloper.merchant (manage Google Pay merchant data), paydeveloper.issuer.readonly (read Google Wallet issuer data) and wallet.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [paydeveloper.googleapis.com](https://paydeveloper.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 0 |
| **Events** | 0 |
| **Slug** | `googlePayWalletDeveloper` |

## Use it

Add Google Pay & Wallet Developer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googlePayWalletDeveloper.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).
