---
description: >-
  Built-in connector list, 6 auth methods, Create Connector dialog fields,
  connections, and capability registry.
---

# Connectors

### Built-in connectors

| Connector      | Category      | Auth type |
| -------------- | ------------- | --------- |
| **Shopify**    | E-commerce    | OAuth 2.0 |
| **Stripe**     | Payments      | API Key   |
| **Xero**       | Accounting    | OAuth 2.0 |
| **QuickBooks** | Accounting    | OAuth 2.0 |
| **Cin7 Core**  | Inventory     | API Key   |
| **Cin7 Omni**  | Fulfillment   | API Key   |
| **GitHub**     | Development   | OAuth 2.0 |
| **Slack**      | Communication | OAuth 2.0 |
| **HubSpot**    | CRM           | OAuth 2.0 |
| **Email**      | Communication | Custom    |
| **HTTP**       | Generic       | Custom    |
| **OpenAI**     | AI/ML         | API Key   |

### Auth methods (6 types)

| Method           | Description                                                                        |
| ---------------- | ---------------------------------------------------------------------------------- |
| **No Auth**      | No authentication required. For public APIs.                                       |
| **Basic Auth**   | Username/password pair encoded as Base64 in Authorization header.                  |
| **Bearer Token** | Token sent in Authorization header as `Bearer {token}`.                            |
| **API Key**      | Key sent in a configurable header (e.g., `X-API-Key`).                             |
| **OAuth 2.0**    | User authorizes via app's login screen. Fastn manages token refresh automatically. |
| **Custom**       | Custom handler for proprietary auth flows.                                         |

Multiple auth methods can be added to one connector. One is set as default.

#### Fastn-managed OAuth Apps

For supported platforms, Fastn manages OAuth on your behalf (**Settings → OAuth Apps**). You can authenticate connectors without creating your own OAuth application in the third-party's developer portal.

### Create Connector dialog

Fields when clicking **+ Create** on the Connectors page:

| Field            | Required | Description                                      |
| ---------------- | -------- | ------------------------------------------------ |
| **Name**         | Yes      | Display name (e.g., "Salesforce")                |
| **Slug**         | Auto     | URL-safe identifier, auto-generated from name    |
| **Description**  | No       | What the connector does                          |
| **Domain**       | No       | The app's domain (e.g., "salesforce.com")        |
| **Visibility**   | Yes      | Private or Public                                |
| **Icon URL**     | No       | URL to the app's icon/logo                       |
| **Auth Methods** | Yes      | Select from dropdown, click "+ Add" for multiple |

### Connections

A **connection** is an authenticated instance of a connector with stored credentials.

|               | Connector                                      | Connection                              |
| ------------- | ---------------------------------------------- | --------------------------------------- |
| What it is    | Integration definition (auth, actions, events) | Authenticated instance with credentials |
| How many      | One per app                                    | Many — per user/customer                |
| Where managed | Integrations → Connectors                      | Integrations → Connections              |
| Created by    | You (manual or AI)                             | You or your customers (via widget)      |

#### Connector card states

| Element              | Meaning                               |
| -------------------- | ------------------------------------- |
| **PERSONAL** badge   | Created by you, not shared            |
| **Connect** button   | No connection — click to authenticate |
| **+ Add Connection** | Already connected — add another       |
| **Created by: You**  | Shows creator                         |

### Build with AI

Click **"Build with AI"** on the Connectors page to open the **Connector Agent**. Describe what you want to connect and the agent:

1. Researches the API
2. Discovers the spec (OpenAPI/Swagger/Postman)
3. Builds actions and events
4. Tests against real connections
5. Fixes failures automatically

### Capability registry

Each connector declares capabilities:

* **Entities** — data types it works with (contacts, orders, products)
* **Actions** — operations per entity (create, read, update, delete, list)
* **Events** — webhook events per entity (created, updated, deleted)

Used for connector matching, field coverage analysis, and MCP dynamic tool generation.
