---
description: >-
  Built-in connector list, 6 auth methods, Create Connector dialog fields,
  connections, and capability registry.
---

# Connectors

Connectors are pre-built integrations with third-party systems. Each connector handles authentication with its system and exposes that system's actions (reading and writing data, triggering events) so workflows and the widget can use them.

### Finding connectors

Go to **Integrations → Connectors**. Connectors appear as cards with an app icon, a description, and a badge indicating who created them.

| Badge    | Meaning          |
| -------- | ---------------- |
| MANAGED  | Created by Fastn |
| PERSONAL | Created by you   |

Top-right actions on the Connectors page:

| Button          | Purpose                                              |
| --------------- | ---------------------------------------------------- |
| Import          | Import a connector definition                        |
| + Create        | Create a connector manually                          |
| ✦ Build with AI | Describe a connector and have the AI agents build it |

Each connector card shows either **Connect** (if not yet authenticated) or **+ Add Connection** (if a connection already exists).

### Available connectors

The platform has 40+ connectors. Verified examples include:

**CRM & Sales:** Salesforce, HubSpot, Dynamics 365 CRM (Dataverse)

**E-commerce & Inventory:** Shopify, BigCommerce, BigCommerce B2B Edition, Cin7 Core, Brightpearl, Akeneo PIM

**Accounting & Finance:** QuickBooks Online, Dynamics 365 Finance & Operations

**Communication:** Slack, Mailgun

**Project & Knowledge:** Jira, Confluence, Linear, ClickUp, Notion, Miro

**Developer & Data:** GitHub, ServiceNow, Typesense, Azure Synapse Analytics, Azure Service Bus, Azure Data Lake, WebDAV

**Storage:** Dropbox, OneDrive, SharePoint, Cloudinary, Google Drive

**Google Workspace:** Gmail, Google Calendar, Google Drive, Google Docs, Google Sheets

**Databases:** Supabase, Supabase Management

**Marketing:** Klaviyo

**Other:** Shopify, HP Workforce Experience, Fireflies, Gamma API

> The connector list changes over time. Check **Integrations → Connectors** for the current set.

#### Connectors with "MCP" in the name

Some connectors are named with "MCP" (e.g., "Fathom MCP", "Gamma MCP"). These are individual connectors for those products. They are not related to the [MCP Gateway](https://claude.ai/fastn/reference/mcp-gateway) feature, which exposes your integrations as tools to AI agents.

#### The two Supabase connectors

There are two distinct Supabase connectors:

| Connector           | Scope                                                           |
| ------------------- | --------------------------------------------------------------- |
| Supabase            | Data plane — PostgREST CRUD, Storage, Auth Admin                |
| Supabase Management | Management API — edge functions, SQL/DDL, project configuration |

Use **Supabase** for reading and writing data. Use **Supabase Management** for managing the project itself.

### Authentication types

Connectors authenticate with their systems using one of several methods, depending on what the system supports:

* **OAuth** — The connector redirects the user to the system's authorization screen. For common platforms, Fastn manages the OAuth app (see **Settings → OAuth Apps**); for others, you supply your own OAuth credentials.
* **API Key** — The user provides an API key for the system.

When a connector is used during an AI-built integration, the authentication form appears inline in the chat — the user provides credentials without leaving the flow.

### Connections

A **connector** is the integration definition (e.g., "Salesforce"). A **connection** is an authenticated instance of that connector for a specific account. One connector can have multiple connections (e.g., two different Slack workspaces).

Connections are managed under **Integrations → Connections**.
