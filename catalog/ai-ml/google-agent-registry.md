---
description: "Google Agent Registry is a catalog of AI agents and tools in Google Cloud. List agents and MCP servers, and create and manage services."
hidden: true
---

# Google Agent Registry

<img src="../../.gitbook/assets/connectors/lg/google-agent-registry.png" alt="Google Agent Registry logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [agentregistry.googleapis.com](https://agentregistry.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleAgentRegistry` |

## Setup

Your customers sign in to Google Agent Registry through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Agent Registry from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleAgentRegistry.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Service</td><td><code>createService</code></td><td>Registers a service (an agent, MCP server or plain endpoint) in Agent Registry. Supply interfaces plus exactly one spec. Safe demo: endpointSpec {"type": "NO_SPEC"} with interfaces [{"url": "https://example.com/api", "protocolBinding": "HTTP_JSON"}] registers a catalog entry only and calls nothing; remove it with Delete Service. Returns a long-running operation; poll it with Get Operation. Requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-write.</td></tr><tr><td>Delete Service</td><td><code>deleteService</code></td><td>Deletes a user-registered Agent Registry service (use it to clean up the service made by Create Service). Returns a long-running operation; poll it with Get Operation. Requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-write.</td></tr><tr><td>Get Operation</td><td><code>getOperation</code></td><td>Gets the status of an Agent Registry long-running operation, such as the one returned by Create Service or Delete Service. Returns done, and either the result in response or the failure in error. Requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-only (or agentregistry.read-write).</td></tr><tr><td>Get Service</td><td><code>getService</code></td><td>Gets one user-registered Agent Registry service by ID, including its spec (agent, MCP server or endpoint), interfaces and the resulting registry resource. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-only (or agentregistry.read-write).</td></tr><tr><td>List Agents</td><td><code>listAgents</code></td><td>Lists the AI agents in Agent Registry for a project and location, with their display names, descriptions, versions, protocols (connection details), skills and attributes, often taken from each agent's A2A Agent Card. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-only (or agentregistry.read-write).</td></tr><tr><td>List MCP Servers</td><td><code>listMcpServers</code></td><td>Lists the MCP (Model Context Protocol) servers in Agent Registry for a project and location, with their display names, interfaces (URLs and protocol bindings) and tools. Use location 'global' to see Google and Google Cloud remote MCP servers that are registered automatically. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-only (or agentregistry.read-write).</td></tr><tr><td>List Services</td><td><code>listServices</code></td><td>Lists the user-registered services (agents, MCP servers and endpoints registered manually) in Agent Registry for a project and location. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-only (or agentregistry.read-write).</td></tr></tbody></table>

## Events

Google Agent Registry has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
