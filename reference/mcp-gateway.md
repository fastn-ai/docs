---
description: >-
  Native tools, dynamic tools, per-tenant availability, and the MCP resource
  protocol.
---

# MCP Gateway

The MCP Gateway exposes Fastn's capabilities as tools that AI assistants and agents can call over the Model Context Protocol (MCP). It is found under **Widgets → Widget Builder → Embed → MCP**, with two planes: a Control Plane for managing your workspace and a Data Plane for per-customer agent access.

### The two planes

| Plane         | Server               | For                                                            |
| ------------- | -------------------- | -------------------------------------------------------------- |
| Control Plane | Admin MCP Server     | Managing your Fastn workspace via an AI tool (Claude, Cursor)  |
| Data Plane    | Customer MCP Gateway | An agent acting inside a specific customer's connected systems |

### Control Plane — Admin MCP Server

For developers and AI tools (Claude, Cursor) to manage connectors, actions, auth, webhooks, and connections.

* **Server URL:** `https://live.gcp.fastn.ai/mcp/admin`
* **Authentication:** Your API key, passed as a query parameter (`?api_key=fsk_live_...`)
* **Tools available:** 37

Example configuration for an MCP client (Claude, Cursor):

```json
{
  "mcpServers": {
    "fastn-admin": {
      "url": "https://live.gcp.fastn.ai/mcp/admin?api_key=fsk_live_..."
    }
  }
}
```

Use this when you want to manage your Fastn setup through an AI tool — for example, asking Claude to list your connectors or configure an action.

### Data Plane — Customer MCP Gateway

A per-customer MCP endpoint. This is the path for AI agents in your product that need to act inside a specific customer's connected systems.

* **Gateway URL:** `https://live.gcp.fastn.ai/mcp/gateway?customer_id=CUSTOMER_ID`
* **Authentication:** Your API key, passed as a query parameter
* **Tool exposure:** Configurable per customer — "All connectors" or "Selected only"

Example configuration:

```json
{
  "mcpServers": {
    "fastn": {
      "url": "https://live.gcp.fastn.ai/mcp/gateway?customer_id=CUSTOMER_ID&api_key=fsk_live_..."
    }
  }
}
```

#### Configuring tools

In the Data Plane view, you select a customer and configure which tools are exposed to agents acting on that customer's behalf:

* **All connectors** — every connector the customer has connected is available as a tool.
* **Selected only** — you choose which connectors are exposed.

Until tools are configured, the gateway shows "No tools configured. Click Configure to enable connectors."

> **VERIFY:** Confirm whether `customer_id` in the gateway URL is the same identifier as `endOrgId` used in the embed token flow, and confirm the production authentication method (query parameter vs header).

### Which plane to use

| Goal                                                    | Plane                         |
| ------------------------------------------------------- | ----------------------------- |
| Manage your own Fastn workspace through an AI tool      | Control Plane (Admin MCP)     |
| Let your product's AI agent act in a customer's systems | Data Plane (Customer Gateway) |
