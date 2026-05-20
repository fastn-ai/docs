---
description: >-
  Set up a connector with OAuth or API key auth, configure its capabilities,
  test actions, and manage tenant-level credentials.
---

# Configuring a Connector

**Prerequisites:** [Your First Integration](../../getting-started/your-first-integration.md).

### Two ways to create a connector

#### Manual setup

1. Go to **Integrations → Connectors**.
2. Click **+ Create**.
3. Fill in the Create Connector dialog:

| Field            | What to enter                                                        |
| ---------------- | -------------------------------------------------------------------- |
| **Name**         | Display name (e.g., "Salesforce")                                    |
| **Slug**         | URL-safe identifier, auto-generated from name (e.g., "salesforce")   |
| **Description**  | What the connector does (e.g., "CRM integration")                    |
| **Domain**       | The app's domain (e.g., "salesforce.com")                            |
| **Visibility**   | Private (only you) or shared                                         |
| **Icon URL**     | URL to the app's icon/logo                                           |
| **Auth Methods** | Select one or more from the dropdown, click **"+ Add"** for multiple |

4. Click **Create**.

> **Screenshot:** Create Connector dialog with all fields filled in.

#### Building with AI

1. Go to **Integrations → Connectors**.
2. Click **Build with AI**.
3. The **Connector Agent** page opens.
4. Describe what you want (e.g., "HubSpot CRM") or click a quick-start prompt.
5. The agent researches the API, discovers the spec, builds actions and events, and tests them.

> **Screenshot:** Connector Agent page with the chat input and quick-start prompts.

> &#x20;**GIF needed:** Using Build with AI — entering a connector name, watching the agent discover the API and build actions.

### Authentication methods

Six auth methods are available when creating a connector:

| Method           | How it works                                                             | Example apps                          |
| ---------------- | ------------------------------------------------------------------------ | ------------------------------------- |
| **No Auth**      | No authentication required. For public APIs.                             | Public data feeds                     |
| **Basic Auth**   | Username and password sent as Base64 in Authorization header.            | Legacy APIs, internal systems         |
| **Bearer Token** | Token sent in Authorization header as `Bearer {token}`.                  | Many modern APIs                      |
| **API Key**      | Key sent in a custom header (e.g., `X-API-Key`).                         | Stripe, SendGrid, OpenAI              |
| **OAuth 2.0**    | User authorizes via the app's login screen. Fastn manages token refresh. | Slack, Shopify, HubSpot, Xero, Google |
| **Custom**       | A custom handler manages auth. For proprietary systems.                  | Internal tools, custom APIs           |

You can add multiple auth methods to one connector (click **"+ Add"** in the Auth Methods section). One method is set as default.

> **Screenshot:** Auth Methods dropdown showing all 6 options.

#### Using Fastn-managed OAuth apps

For supported platforms, Fastn manages OAuth on your behalf (see **Settings → OAuth Apps**). This means you can authenticate without creating your own OAuth application in the third-party's developer portal.

If the platform isn't listed under OAuth Apps, you'll need to:

1. Create an OAuth application in the third-party's developer portal
2. Copy the Client ID and Client Secret
3. Configure them in your connector's auth settings

### Adding a connection

A connector defines the integration. A **connection** is an authenticated instance — your credentials or your customer's credentials.

1. On the Connectors page, find your connector card.
2. Click **Connect** (first connection) or **+ Add Connection** (additional connections).
3. Complete the auth flow:
   * **OAuth 2.0:** Popup opens with the app's login screen. Authorize and you're redirected back.
   * **API Key / Bearer Token:** Paste the key/token and save.
   * **Basic Auth:** Enter username and password.
4. The connection appears under **Integrations → Connections**.

> **GIF:** Adding a connection — clicking Connect on a connector card, completing OAuth, seeing the connected state.

#### Connections vs connectors

|                   | Connector                                                 | Connection                                        |
| ----------------- | --------------------------------------------------------- | ------------------------------------------------- |
| **What it is**    | The integration definition (auth config, actions, events) | An authenticated instance with stored credentials |
| **How many**      | One per app                                               | Many — one per user/customer who connects         |
| **Where managed** | Integrations → Connectors                                 | Integrations → Connections                        |
| **Created by**    | You (manual or AI)                                        | You (for testing) or your customers (via widget)  |

#### Connector card states

On the Connectors page, each connector card shows:

| Element                     | Meaning                                    |
| --------------------------- | ------------------------------------------ |
| **PERSONAL** badge          | Created by you, not shared                 |
| **Connect** button (purple) | No connection yet — click to authenticate  |
| **+ Add Connection** button | Already connected — add another connection |
| **Created by: You**         | Shows who created the connector            |

### Connector visibility

| Visibility  | Who can see it                                   |
| ----------- | ------------------------------------------------ |
| **Private** | Only you and your organization                   |
| **Public**  | Available to other organizations (if applicable) |

Set visibility in the Create Connector dialog or edit it later from the connector's settings.

### What you've learned

* Two ways to create connectors: manual (+ Create) and AI (Build with AI)
* All 6 auth methods and when to use each
* How Fastn-managed OAuth apps simplify authentication
* The difference between connectors and connections
* Connector card states and visibility settings
