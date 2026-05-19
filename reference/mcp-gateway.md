---
description: >-
  Native tools, dynamic tools, per-tenant availability, and the MCP resource
  protocol.
---

# MCP Gateway

The MCP Gateway exposes Fastn capabilities as tools for AI assistants via the Model Context Protocol.

### Native tools

Six built-in tools are always available regardless of which connectors a tenant has connected:

| Tool                           | Description                                     | Input                                                       |
| ------------------------------ | ----------------------------------------------- | ----------------------------------------------------------- |
| `fastn_list_integrations`      | List all active integrations for a tenant       | `{ tenant_id: string }`                                     |
| `fastn_get_integration_status` | Get detailed status of a specific integration   | `{ tenant_id: string, integration_id: string }`             |
| `fastn_create_flow`            | Create a new automation flow from specification | `{ tenant_id: string, spec: FlowSpec }`                     |
| `fastn_get_event_history`      | Retrieve recent events for a tenant             | `{ tenant_id: string, limit?: number, since?: datetime }`   |
| `fastn_get_usage_summary`      | Get quota usage summary                         | `{ tenant_id: string }`                                     |
| `fastn_search_entities`        | Search CDM entities across integrations         | `{ tenant_id: string, entity_type: string, query: object }` |

### Dynamic tools

Auto-generated from active connector capabilities. Each connector action becomes an MCP tool.

#### Generation rules

* Tool name: `{connector}_{action}` (e.g., `slack_send_message`, `shopify_list_orders`)
* Tool description: derived from the action's description field
* Input schema: derived from the action's inputSchema
* Only generated for connectors the tenant has active

#### Example dynamic tools

A tenant with Slack and Shopify connected gets:

```
slack_send_message
slack_list_channels
slack_list_users
shopify_list_orders
shopify_get_customer
shopify_list_products
shopify_get_order
```

A different tenant with only Slack gets:

```
slack_send_message
slack_list_channels
slack_list_users
```

No Shopify tools — they haven't connected Shopify.

### Per-tenant availability

Tool visibility is scoped per tenant:

1. AI assistant invokes an MCP tool
2. Gateway identifies the tenant from the request context
3. Gateway checks the tenant's active integrations
4. Only tools for connected connectors are exposed
5. Tool executes using the tenant's stored credentials
6. Response returns to the AI assistant

This ensures tenants only see tools for apps they've connected, and all API calls use the correct tenant credentials.

### Resource protocol

The MCP gateway implements the MCP resource protocol for read-only data access:

| Resource       | Description                                     |
| -------------- | ----------------------------------------------- |
| `integrations` | List of active integrations and their status    |
| `entities`     | CDM entities available across connected systems |
| `events`       | Recent event history                            |
| `usage`        | Quota usage data                                |

Resources provide data without executing actions — useful for AI assistants that need to answer questions about state without triggering workflows.

### MCP server URL

```
https://mcp.ucl.dev/mcp/?id={PROJECT_ID}&api_key={API_KEY}&space_id={PROJECT_ID}
```
