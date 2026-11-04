---
description: >-
  Set up a connector with OAuth or API key auth, configure its capabilities,
  test actions, and manage each customer's connections.
---

# Configuring a Connector

**Prerequisites:** [Your First Integration](../../getting-started/quickstart.md).

### Ways to create a connector

Go to **Integrations → Connectors** and open the **Create connector** menu (top right). It offers **From scratch**, **Build with AI**, **Build from Claude or any MCP client** and **Import from file**. This tutorial covers the first two.

#### From scratch

1. Choose **Create connector → From scratch**.
2. Fill in the **Create a connector** dialog. It has three sections:

| Section | Fields |
| ------- | ------ |
| **Identity** | **Name** (display name, e.g. "Salesforce"), **Slug** (derived from the name; you can edit it), **Description** (what the connector does) |
| **Connection** | **Protocol** (REST by default), **Visibility**, **Domain** (the app's domain, e.g. "salesforce.com"), **Icon URL** (URL to the app's icon) |
| **Authentication** | One block per auth method. Click **Add method** to offer more than one. |

**Visibility** is `Private` when you create a connector: *Only your organization can see it.* Publishing a connector to the customer catalog is done by a platform admin.

3. Click **Create connector**.

For every field and protocol, see [Creating a connector](../../build/connectors/creating-a-connector.md).

#### Build with AI

1. Choose **Create connector → Build with AI**. This opens [Build with AI](../../build/agent/README.md).
2. Describe what you want (e.g., "HubSpot CRM"), and give it the vendor's API docs if you have them.
3. Build with AI researches the API, builds the actions and auth method, and tests them.

### Authentication methods

Seven auth methods are available when creating a connector:

| Method           | How it works                                                             | Example apps                          |
| ---------------- | ------------------------------------------------------------------------ | ------------------------------------- |
| **No Auth**      | No authentication required. For public APIs.                             | Public data feeds                     |
| **Basic Auth**   | Username and password sent as Base64 in Authorization header.            | Legacy APIs, internal systems         |
| **Digest Auth**  | Username and password, using HTTP digest authentication.                 | APIs that require digest auth         |
| **Bearer Token** | Token sent in Authorization header as `Bearer {token}`.                  | Many modern APIs                      |
| **API Key**      | Key sent in a custom header (e.g., `X-API-Key`).                         | Stripe, SendGrid, OpenAI              |
| **OAuth 2.0**    | User authorizes via the app's login screen. fastn manages token refresh. | Slack, Shopify, HubSpot, Xero, Google |
| **Custom**       | Starts with an empty Configuration: you define every field the user enters when connecting, for example an account subdomain plus a token. | Internal tools, custom APIs |

You can add multiple auth methods to one connector (click **Add method** in the Authentication section). One method is set as default.

#### Using fastn-managed OAuth apps

For supported platforms, fastn provides the OAuth app on your behalf. You can see it on the connector's **Auth** tab under **View providers** (or **Manage providers**). This means you can authenticate without creating your own OAuth application in the third-party's developer portal.

If the connector has no OAuth app you can use, you'll need to:

1. Create an OAuth application in the third-party's developer portal
2. Copy the Client ID and Client Secret
3. Add them as a provider on the connector's **Auth** tab (**Add provider** or **Manage providers**). See [Auth methods and providers](../../build/connectors/auth-methods.md).

### Adding a connection

A connector defines the integration. A **connection** is an authenticated instance - your credentials or your customer's credentials.

1. On the Connectors page, find your connector card.
2. Click **Connect** (first connection) or **Add another connection** (additional connections).
3. Complete the auth flow:
   * **OAuth 2.0:** Popup opens with the app's login screen. Authorize and you're redirected back.
   * **API Key / Bearer Token:** Paste the key/token and save.
   * **Basic Auth:** Enter username and password.
4. The connection appears under **Operate → Connections**.

> **GIF:** Adding a connection - clicking Connect on a connector card, completing OAuth, seeing the connected state.

#### Connections vs connectors

|                   | Connector                                                 | Connection                                        |
| ----------------- | --------------------------------------------------------- | ------------------------------------------------- |
| **What it is**    | The integration definition (auth config, actions, events) | An authenticated instance with stored credentials |
| **How many**      | One per app                                               | Many - one per user/customer who connects         |
| **Where managed** | Integrations → Connectors                                 | Operate → Connections                             |
| **Created by**    | You (manual or AI)                                        | You (for testing) or your customers (via widget)  |

#### Connector card states

On the Connectors page, each connector card shows:

| Element                     | Meaning                                    |
| --------------------------- | ------------------------------------------ |
| **managed** or **Custom** badge | Maintained by fastn, or created in your workspace. Once the connector has an active connection the badge reads **Connected**; if it has connections but none is active, **Inactive**. |
| **OAuth 2.0** chip          | The connector offers an OAuth 2.0 method   |
| **Managed by** ...          | Who maintains it: *Managed by Fastn*, or *Managed by* your organization's name |
| **Connect** button          | No connection yet - click to authenticate  |
| **Add another connection** button | Already connected - add another connection |

### Connector visibility

| Visibility  | Who can see it                                   |
| ----------- | ------------------------------------------------ |
| **Private** | Only your organization can see it.               |
| **Public**  | Customers under your organization can use it when Catalog connectors is on. Other organizations never see it. Only a platform admin can make a connector public. |

New connectors are always created as `Private`.

### What you've learned

* Ways to create connectors: **From scratch** and **Build with AI**, both from the **Create connector** menu
* All 7 auth methods and when to use each
* How fastn-managed OAuth apps simplify authentication
* The difference between connectors and connections
* Connector card states and visibility settings
