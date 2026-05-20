---
description: >-
  This approach provides clear separation and control while optimizing resource
  usage.
---

# Multitenancy

Multitenancy is a foundational concept within UCL that enables secure, scalable, and efficient management of multiple customers or teams within a single platform instance.

### **Core Concepts**

Multitenancy means that a single deployment of the UCL platform can serve multiple distinct tenants \[users], such as different customers, departments, or user groups. Each user operates in an isolated environment with their data, credentials, tools, and access policies. This ensures privacy and security, preventing any cross-tenant data exposure.

<figure><img src="../../../../../.gitbook/assets/Fastn-GIF3.gif" alt="Animated demo of UCL multitenancy showing isolated tenant environments within a shared platform instance"><figcaption></figcaption></figure>

## How Multitenancy Works in UCL: A Simple Case Study

Imagine Sarah, June, and Emily all work at the same company and share the same Space ID in your app, but each manages different tools and integrations as shown in the video:

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F3iSr2Tx8FvvuoLPncziH%2Fuploads%2FUzHKreiCSdf3gNSPGT4a%2FMulti%20tenantcy.mp4?alt=media&token=d4682d52-9829-441a-b8f6-831340260a48" %}

### **1. User Context Keeps Everything Organized**

Each user operates within their own **user context** \[tenant ID], even though they share the same Space ID. For example, when Sarah logs in and accesses integrations, UCL recognizes her user identity and:

* Displays only **Sarah's selected tools** (e.g., Slack, HubSpot, Salesforce).
* Uses only her data and configurations when performing actions.

Similarly, June and Emily see and interact only with their own tools and configurations, even if some tools overlap in the space.

### **2. Different Users, Different Tools and Toolkits**

Within a shared Fastn workspace (same space ID), all users have access to the same set of available tools, like Slack, Gmail, or Notion. However, each user or tenant can connect these tools with their credentials and enable only the actions they need.

For example:

* Sarah might connect Slack and enable message posting actions.
* June might use the same Slack tool, but might not have "send message" Action enabled.
* Emily might connect Notion and only enable read-only access for documentation.

This setup ensures everyone shares the same tool infrastructure but operates independently, with secure separation of credentials, access, and actions.

### **3. Seamless Isolation, Zero Mix-Ups**

Despite all users operating in the same app and sharing the same Space ID, UCL keeps its tools, data, and actions strictly isolated:

* Sarah cannot see or affect June's integrations.
* June cannot send messages using Emily's Gmail setup.
* Each user's data and configurations remain private and secure.

### **4. Platform Handles Complexity Automatically**

All of this complexity is managed transparently by UCL. It reads the tenant ID on every request and automatically:

* Routes requests to the correct toolkits per user/tenant
* Applies the appropriate permissions and roles
* Keeps all user data and actions isolated and secure

This lets you focus on building features instead of managing multi-tenant logic.

## **Key Benefits of Multitenancy**

UCL's multitenancy architecture delivers several critical advantages that enhance both operational efficiency and user experience:

* **Security:** User isolation prevents unauthorized data sharing or accidental exposure across teams.
* **Simplicity:** Teams manage their own integrations and tasks independently without interference.
* **Scalability:** A single UCL deployment can grow to support thousands of users without performance loss.
* **Cost Efficiency:** Shared infrastructure reduces overhead compared to maintaining separate instances for each user.
* **Centralized Management:** IT administrators can oversee multiple users from a unified dashboard while respecting tenant boundaries.

## **Architecture**

The multitenant architecture of UCL consists of a centralized server that handles requests for all users. Each user's data, configuration, and authentication tokens are stored separately within secure workspaces. Tools and actions are dynamically mapped based on user context, allowing seamless routing of operations. The architecture supports horizontal scaling to meet increasing demand while preserving user isolation and performance consistency.

<figure><img src="../../../../../.gitbook/assets/image (321).png" alt="UCL multitenant architecture diagram showing request routing from API, SDK, or MCP client through Fastn UCL to tenant-isolated apps with Slack and Teams notifications"><figcaption></figcaption></figure>
