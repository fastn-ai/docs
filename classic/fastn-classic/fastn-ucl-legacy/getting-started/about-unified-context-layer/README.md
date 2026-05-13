---
description: >-
  A unified layer that simplifies integration by handling routing, context, and
  multitenancy; securely and at scale.
---

# About Unified Context Layer

## What is it?

Unified Context Layer (UCL) is a secure, scalable integration layer that connects AI agents to real-world tools and data, so they can go beyond suggestions and take action.

<figure><img src="../../../../../.gitbook/assets/Frame 6.png" alt="Diagram showing UCL as a secure integration layer connecting AI agents to external tools and data"><figcaption></figcaption></figure>

Think of it as a universal remote control for AI agents, letting them interact with real-world tools and services while maintaining security and proper access controls. UCL brings the protocol to life with a fully managed server that handles authentication, routing, multitenancy, and context management out of the box.

### **Why do SaaS companies need UCL?**

SaaS platforms serve many customers, and each customer often uses a different mix of tools, CRMs, ticketing systems, and messaging apps. To make AI agents truly effective inside a SaaS product, they need to connect to each customer’s unique stack securely and in real time.

UCL handles this complexity out of the box. It enables you to support custom integrations for every customer while managing authentication, routing, and user isolation. So, whether one customer uses **Salesforce** and **Slack** and another uses **HubSpot** and **Microsoft Teams**, their AI agents can still act intelligently within the right context and without requiring any code changes.

<figure><img src="../../../../../.gitbook/assets/image (304).png" alt="Diagram showing UCL routing requests to different tools per customer, such as Salesforce, Slack, HubSpot, and Microsoft Teams"><figcaption></figcaption></figure>

### **Why do enterprise companies need UCL?**

Enterprises need more than just secure integrations. They need smart, permission-aware agents that understand how different teams and departments work, that is also completely owned and controlled by enterprises. For example, marketing might need access to content tools, while IT needs infrastructure access, each with the right boundaries.

UCL enables this with contextual permissions, team-based access to tools, and isolated execution per workspace. This allows AI agents to run across different departments with just the right level of access and visibility. Each team’s agent stays secure and focused, even when operating across a shared environment.

**Imagine this,**\
You are building a task reminder feature for your SaaS product. Your customers use different tools to receive notifications:

* **Customer A** prefers **Slack.**
* **Customer B** relies on **Microsoft Teams.**
* **Customer C** wants reminders via **Gmail.**

**The Challenge with MCP:**\
Using Model Context Protocol (MCP) alone, you can standardize how agents describe actions, but you’re still responsible for building the infrastructure to execute them.\
Each customer, tool, or environment requires a separate setup:

* Custom logic for routing
* Manual integration for each tool
* Repeated work for every user

This quickly becomes brittle, time-consuming, and hard to scale in production.

**How UCL Solves This:**\
The Unified Context Layer (UCL) accepts MCP-formatted commands and connects with multiple everyday apps like Slack, Notion, Jira, and more. Each workspace can have multiple users, each with access to different tools based on the enabled actions (e.g, sending a message or assigning a task).

UCL does the heavy-lifting;

* Detects the user and user context.
* Routes the command to the correct tool, like Slack, Teams, or Notion.
* Manages authentication, retries, and logging in the background.

You don’t need to write separate logic for each user or app. UCL ensures the right action happens in the right context.

**Result:**

* Reduced development and maintenance effort
* Scalable, multi-user support out of the box
* More reliable and flexible integrations

A user interacts with an AI assistant to trigger an intent (e.g., sending a task reminder). The assistant securely connects to UCL to retrieve the user-specific context. UCL server processes the request, selects the right tool based on user settings, and executes the action (like sending a message via Slack, Teams, or Gmail). Finally, the result is sent back to the assistant, which delivers the response to the user.

<figure><img src="../../../../../.gitbook/assets/image (433).png" alt="Flowchart showing a user intent routed through UCL to the correct tool such as Slack, Teams, or Gmail"><figcaption></figcaption></figure>

_Visual overview of how UCL components interact:_

<figure><img src="../../../../../.gitbook/assets/image (434).png" alt="Architecture overview of UCL components: AI assistant, UCL server, context management, and tool execution"><figcaption></figcaption></figure>

## **How UCL Works?**

**1. Understands AI Commands**\
Accepts MCP-formatted commands from AI agents or user interfaces.

**2. Detects Context**\
Identifies the correct user, and workspace context for each command.

**3. Connects to Apps**\
Uses pre-configured tools to link with the appropriate app or tool.

**4. Executes Securely**\
Performs the action with built-in routing, authentication, and user-based access.

### **Why This Approach Works**

UCL enables intelligent routing without the need for hardcoded logic or manual segmentation. You benefit from:

* Simplified integration logic
* Centralized context and configuration
* Consistent data isolation and security
* Faster scalability across varied customer environments

This allows your team to deliver flexible, secure, and tailored experiences to every customer, without reinventing your workflow for each use case.

## How does UCL complement MCP?

UCL transcends MCP's basic protocol by providing a complete, production-ready platform that handles complex enterprise requirements out of the box. While MCP offers the foundational protocol for AI-tool interactions, UCL delivers a fully managed solution with built-in multitenancy, security, and monitoring capabilities.

The key differentiator is that UCL removes the burden of infrastructure management and security implementation from developers, allowing them to focus on building AI features while UCL handles the complexities of integration, authentication, and user isolation.

| Feature / Aspect           | **Model Context Protocol (MCP)**                                         | **UCL (Unified Context Layer)**                                      |
| -------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| **Definition**             | The open protocol that standardizes how AI interacts with tools and data | Fully managed platform that implements MCP in a scalable, secure way |
| **Purpose**                | Enable AI agents to securely access external systems                     | Make MCP practical for real-world SaaS applications and teams        |
| **Hosting**                | Self-hosted / DIY                                                        | Fully hosted and maintained by UCL                                   |
| **Security Model**         | Protocol-level definitions (e.g., tokens, scopes)                        | Enforced through secure APIs, workspace isolation, and user tokens   |
| **Multitenancy**           | Not provided out of the box                                              | Built-in, with true per-user isolation and routing                   |
| **Integration Management** | Requires custom implementation                                           | Centralized dashboard, observability, and configuration              |
| **Developer Effort**       | High; needs setup, infrastructure, and glue code                         | Low; ready-to-use with UCL SDKs and tools                            |
| **Use Case Fit**           | Good for experimentation or single-user systems                          | Ideal for SaaS teams needing scalable, white-labeled AI integration  |
| **Extensibility**          | Open protocol; customizable                                              | Supports custom tools + full API access                              |
| **Standard Compliance**    | Protocol-only                                                            | Full MCP-compliant implementation                                    |

## Why is UCL the game-changer?

UCL extends the Model Context Protocol (MCP) into a robust, production-ready platform that addresses the practical demands of SaaS integration at scale. It enables AI systems to operate securely, contextually, and reliably across multiple environments.

#### **Embedding: Seamless Integration Within Your Product**

UCL enables deep, native integration with apps directly within your SaaS product. Without requiring end users to manage external configurations, the integration logic remains fully embedded, delivering a unified experience while UCL handles the complexity in the background.

#### **Multitenancy: Native Support for Scaled, Isolated Environments**

UCL is architected for true multitenancy. Each customer (tenant) operates within an isolated environment, with separate credentials and data contexts. This eliminates the need for multiple deployment instances and ensures consistent, secure operation as your customer base scales.

#### **Monitoring: Centralized Observability and Operational Insight**

UCL provides comprehensive visibility into all integration activity across users. Built-in monitoring and logging tools allow your team to track usage patterns, identify issues proactively, and maintain high system reliability, without the need for additional infrastructure.

#### **Security: Built-In Isolation and Access Control**

Security is fundamental to UCL’s architecture. User data and execution contexts are strictly isolated, and access is governed by fine-grained, role-based controls. Every request is authenticated and validated, ensuring that actions taken through AI agents remain secure and compliant with organizational policies.
