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

Your customers sign in to Google Agent Registry through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Agent Registry from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Agent Registry**.
2. Select **Connect** on the Google Agent Registry card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Agent Registry and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Agent Registry's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Service</td><td><code>createService</code></td><td>Registers a service (an agent, MCP server or plain endpoint) in Agent Registry. Supply interfaces plus exactly one spec. Safe demo: endpointSpec {"type": "NO_SPEC"} with interfaces [{"url": "https://example.com/api", "protocolBinding": "HTTP_JSON"}] registers a catalog entry only and calls nothing; remove it with Delete Service. Returns a long-running operation; poll it with Get Operation. Requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-write.</td></tr><tr><td>Delete Service</td><td><code>deleteService</code></td><td>Deletes a user-registered Agent Registry service (use it to clean up the service made by Create Service). Returns a long-running operation; poll it with Get Operation. Requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-write.</td></tr><tr><td>Get Operation</td><td><code>getOperation</code></td><td>Gets the status of an Agent Registry long-running operation, such as the one returned by Create Service or Delete Service. Returns done, and either the result in response or the failure in error. Requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-only (or agentregistry.read-write).</td></tr><tr><td>Get Service</td><td><code>getService</code></td><td>Gets one user-registered Agent Registry service by ID, including its spec (agent, MCP server or endpoint), interfaces and the resulting registry resource. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-only (or agentregistry.read-write).</td></tr><tr><td>List Agents</td><td><code>listAgents</code></td><td>Lists the AI agents in Agent Registry for a project and location, with their display names, descriptions, versions, protocols (connection details), skills and attributes, often taken from each agent's A2A Agent Card. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-only (or agentregistry.read-write).</td></tr><tr><td>List MCP Servers</td><td><code>listMcpServers</code></td><td>Lists the MCP (Model Context Protocol) servers in Agent Registry for a project and location, with their display names, interfaces (URLs and protocol bindings) and tools. Use location 'global' to see Google and Google Cloud remote MCP servers that are registered automatically. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-only (or agentregistry.read-write).</td></tr><tr><td>List Services</td><td><code>listServices</code></td><td>Lists the user-registered services (agents, MCP servers and endpoints registered manually) in Agent Registry for a project and location. Read-only; requires the Google OAuth scope https://www.googleapis.com/auth/agentregistry.read-only (or agentregistry.read-write).</td></tr></tbody></table>

