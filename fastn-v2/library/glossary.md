---
description: >-
  Definitions of key Fastn terms including connectors, flows, tenants, MCP, UCL,
  workspaces, and AI agent components.
---

# Glossary

### API (Application Programming Interface)

A set of protocols and tools for building and interacting with software applications. Fastn provides APIs to manage integrations, users, and workflows.

### CLI (Command Line Interface)

A text-based interface to interact with Fastn, allowing developers to run commands, trigger actions, and manage integrations via terminal.

### Connect Portal

A customizable UI that allows end users to connect third-party applications to your platform securely.

### Embed Fastn UCL (Unified Context Layer)

Fastn's core orchestration engine that unifies integrations under a single JSON API or SDK call, supporting multi-tenant environments with secure routing and execution.

### Integration Hub

A centralized platform within Fastn where users can connect, manage, and monitor all their integrations and AI-driven workflows.

### Multitenancy

An architecture where a single instance of Fastn serves multiple tenants (customers), ensuring complete data isolation and secure execution for each tenant.

### Orchestration Layer

The unified layer that manages communication, execution, and routing between AI agents and connected apps or services in Fastn.

### Policy Control

Rules and permissions that govern what actions AI agents or users can perform within the Fastn platform.

### SDK (Software Development Kit)

A set of tools, libraries, and documentation provided by Fastn to help developers embed and extend Fastn functionality within their applications.

### Server-Sent Events (SSE)

A communication protocol supported by Fastn for real-time streaming of updates from the server to the client.

### Workflow

A sequence of automated tasks or actions designed in Fastn to synchronize, transform, or route data across multiple applications.

### **Agent Connect UI**

A plug-and-play embeddable interface (React component) provided by Fastn UCL that allows users to interact with connected tools and actions directly in your app interface.

### **AI Agent**

A component in Fastn Flows that maintains context, interprets user input, and interacts with external systems via enabled actions. It leverages the MCP layer and OpenAI models to perform reasoning or task execution.

### **AI Action**

A flow step where AI performs a task using the input from previous steps. These can include summarization, classification, or generating commands for connected tools.

### **Connector**

A prebuilt integration with third-party apps (e.g., Notion, Jira, Slack). Connectors handle OAuth, token management, and expose available actions that can be executed in flows or via agents.

### **Workspace**

A logical grouping within Fastn UCL that contains connectors, actions, and environment configurations for a specific app, tenant, or team. Each workspace has a unique Space ID and supports isolation.

### **Tenant ID**

An identifier used to distinguish individual tenants (customers or users) within a single workspace. Enables Fastn UCL to provide secure multitenancy and ensure context-aware execution of actions.

### **MCP (Model Context Protocol)**

An open protocol that standardizes how AI agents describe actions and interact with external tools. Fastn UCL builds on top of MCP to make it production-ready by adding infrastructure, security, and multitenant context handling.

### **MCP Server URL**

The endpoint that agents use to send and receive structured action commands. Fastn provides a preconfigured MCP server (via `NEXT_PUBLIC_FASTN_MCP_SERVER_URL`) for routing, authentication, and context.

### **Action**

A predefined operation exposed by a connector (e.g., "Get Tasks" in Notion or "Send Message" in Slack). Actions are selectable per connector and executable through agents or flows.

### **Environment File (.env)**

A local configuration file in your codebase that stores sensitive variables such as your OpenAI key and Fastn MCP server URL.

### **Flow**

A no-code/low-code visual automation built inside Fastn that sequences steps like triggers, connectors, AI agents, and logic to perform a complete task.

### **Flow Types**

Different kinds of flows tailored to use cases like scheduled execution, webhook-based flows, or agent-driven flows.

### **Trigger**

The starting point of a flow. It defines the condition or event that initiates the flow, such as a time-based schedule, webhook, or external command.

### **Variables & States**

Used within flows to store and pass data between steps. Variables are static, while states are updated dynamically during flow execution.

### **Multitenancy**

The architecture in Fastn UCL that allows multiple tenants to securely share the same infrastructure while maintaining strict separation of data, context, and configuration.

### **Space ID**

A unique identifier for each Fastn UCL workspace, embedded within the MCP Server URL and used for scoping connector access and tenant isolation.

### **Agent Instruction**

The natural language prompt or command that the AI Agent interprets to select the appropriate action and execute it via Fastn UCL.

### **Connected Status**

Indicates a successful OAuth or API connection to a third-party app. Once a connector shows "Connected" in the UI, its actions can be selected and used.

### **Codespaces (GitHub)**

A browser-based cloud development environment that allows users to run Fastn UCL integration projects without needing to install dependencies locally.

### **Activation Flow**

A flow that runs once when a connector widget is first enabled for a tenant. Initializes webhooks, templates, or database tables for that tenant.

### **Configuration Flow**

A flow that defines what settings appear in your widget's UI — dropdowns, file pickers, text fields. After building one, you must link it in Settings → Configurations. Without this linking step, your widget shows no configuration options.

### **Connector**

A step added from the Connection tab in the flow builder. Connects your flow to external apps like Slack, HubSpot, or Salesforce. Not to be confused with the Connectors section in the left-hand menu, which manages authenticated app connections and credentials.

### **Custom Code**

A step under the Control tab in the flow builder. Lets you write JavaScript or C# for operations other components can't handle — null checks, string formatting, custom logic.

### **Deploy**

Publishes your flow so it's callable via API or webhook. The Deploy button is in the top-right of the flow builder. Deployed flows show status "Live." Flows with unpublished changes show "Changes Pending."

### **Fixed vs Dynamic**

Two ways to set a field value in a component step. Fixed values are hardcoded at design time (e.g., channel = "#alerts"). Dynamic values are mapped from a previous step's output and change per execution.

### **Logger**

A step under the Control tab in the flow builder. Logs data at any point in your flow so you can inspect what's passing between steps. Useful during development — remove before production.

### **Loop**

A step under the Control tab. Processes data iteratively by running the steps inside it once per item in a collection.

### **Refresh vs Rerun**

Two actions in the Logs section. Refresh reloads the log list to show new entries — it does not re-execute anything. Rerun re-executes a previous flow with the same input, creating a new log entry.

### **Secrets**

Encrypted project-level values such as API keys and tokens. Managed under Settings → Secrets. Never exposed in logs or flow output.

### **Selection Flow**

A flow that fetches and returns a list of options to populate dropdowns in a Configuration Flow. For example, a Selection Flow might call an API to retrieve Slack channels, which the Configuration Flow then displays as a dropdown.

### **State**

A key-value store that persists data across loop iterations within a single flow execution. Use State when you need a counter or accumulator inside a Loop — regular variables don't update mid-loop.

### **Switch**

A step under the Control tab. Routes your flow to different branches based on conditions. If no cases match, the flow skips all branches silently — always add a default case.

### **Tenant**

An end-user in a multi-tenant setup. Each tenant has isolated connectors, data, and execution logs. Identified by the x-fastn-space-tenantid header. Managed under Settings → Tenants.

### **Test**

The button in the top-right of the flow builder. Runs your flow with test input without deploying it. Use this to verify your flow works before clicking Deploy.

### **Trigger**

The starting point of a flow. Added from the Trigger tab in the flow builder. The default trigger type is "New API Request" (labeled "Real Time"). Webhooks and schedules are managed separately under the Triggers section in the left-hand menu.
