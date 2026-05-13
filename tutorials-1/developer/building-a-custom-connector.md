---
description: >-
  Implement the ConnectorDefinition interface to integrate a third-party app
  that Fastn doesn't support out of the box.
---

# Building a Custom Connector

**Prerequisites:** [Local Dev Environment Setup](https://claude.ai/chat/local-dev-environment-setup.md). Familiarity with TypeScript and REST APIs.

Fastn ships with built-in connectors for Shopify, Stripe, Xero, QuickBooks, Slack, GitHub, and others. When you need to integrate an app that isn't in the library, you build a custom connector using the `ConnectorDefinition` interface.

### The ConnectorDefinition interface

Every connector, built-in or custom implements the same interface:

```typescript
import { ConnectorDefinition } from '@fastn/connectors';

const myConnector: ConnectorDefinition = {
  name: 'my-app',
  displayName: 'My App',
  description: 'Integration with My App API',
  
  auth: {
    type: 'oauth2', // or 'api_key', 'basic', 'bearer_token', 'custom', 'none'
    // auth-specific configuration
  },

  actions: {
    // what the connector can do
  },

  triggers: {
    // what events the connector can listen for
  },

  entities: {
    // what data types the connector works with
  }
};
```

{% hint style="info" %}
⚠️ **VERIFY:** This interface structure is derived from PRD Section 3.2. Confirm the exact import path and property names against the `@fastn/connectors` package source code.
{% endhint %}

### Step 1: Scaffold the connector

Create a new file in the connectors directory:

```bash
# From the project root
mkdir -p packages/connectors/src/my-app
touch packages/connectors/src/my-app/index.ts
```

{% hint style="info" %}
⚠️ **VERIFY:** Confirm the directory structure for custom connectors in the monorepo.
{% endhint %}

### Step 2: Define authentication

Choose the auth method that matches the third-party app. Fastn supports 6 auth types:

#### No Auth

```typescript
auth: {
  type: 'none',
  // No authentication required — for public APIs
}
```

#### Basic Auth

```typescript
auth: {
  type: 'basic',
  // Username and password provided per-customer via credentials
}
```

#### Bearer Token

```typescript
auth: {
  type: 'bearer_token',
  // Token provided per-customer via credentials
  // Sent as: Authorization: Bearer {token}
}
```

#### API Key

```typescript
auth: {
  type: 'api_key',
  headerName: 'X-API-Key',
  // The actual key value is provided per-customer via credentials
}
```

#### OAuth 2.0

```typescript
auth: {
  type: 'oauth2',
  authorizationUrl: 'https://myapp.com/oauth/authorize',
  tokenUrl: 'https://myapp.com/oauth/token',
  scopes: ['read', 'write'],
  clientId: process.env.MYAPP_CLIENT_ID,
  clientSecret: process.env.MYAPP_CLIENT_SECRET,
}
```

#### Custom

```typescript
auth: {
  type: 'custom',
  handler: async (credentials) => {
    // Custom auth logic — e.g., generate a session token,
    // call a proprietary auth endpoint, etc.
    return { headers: { 'Authorization': `Bearer ${token}` } };
  }
}
```

### Step 3: Define actions

Actions are the operations your connector can perform. Each action maps to an API call on the third-party app:

```typescript
actions: {
  listContacts: {
    name: 'List Contacts',
    description: 'Fetch all contacts from My App',
    entity: 'contact',
    type: 'read',
    handler: async (ctx, params) => {
      const response = await ctx.http.get('https://api.myapp.com/contacts', {
        headers: ctx.auth.headers,
        params: { limit: params.limit || 100 }
      });
      return response.data;
    },
    inputSchema: {
      type: 'object',
      properties: {
        limit: { type: 'number', description: 'Max records to return' }
      }
    },
    outputSchema: {
      type: 'array',
      items: { $ref: '#/entities/contact' }
    }
  },

  createContact: {
    name: 'Create Contact',
    description: 'Create a new contact in My App',
    entity: 'contact',
    type: 'create',
    handler: async (ctx, params) => {
      const response = await ctx.http.post('https://api.myapp.com/contacts', {
        headers: ctx.auth.headers,
        body: params
      });
      return response.data;
    },
    inputSchema: {
      type: 'object',
      properties: {
        email: { type: 'string', required: true },
        firstName: { type: 'string' },
        lastName: { type: 'string' },
        company: { type: 'string' }
      }
    }
  }
}
```

The `ctx` object provides:

* `ctx.auth` — resolved credentials for the current customer
* `ctx.http` — HTTP client with retry and error handling built in
* `ctx.tenant` — the current customer context
* `ctx.logger` — structured logging

{% hint style="info" %}
⚠️ **VERIFY:** Confirm the `ctx` object properties and the HTTP client interface from the `@fastn/connectors` package.
{% endhint %}

### Step 4: Define entities

Entities describe the data types your connector works with. They map to CDM entities for cross-connector normalization:

```typescript
entities: {
  contact: {
    name: 'Contact',
    cdmMapping: 'CDMContact', // maps to Fastn's universal Contact entity
    fields: {
      id: { type: 'string', cdmField: 'id' },
      email: { type: 'string', cdmField: 'email' },
      first_name: { type: 'string', cdmField: 'firstName' },
      last_name: { type: 'string', cdmField: 'lastName' },
      org: { type: 'string', cdmField: 'company' }
    }
  }
}
```

The `cdmField` property tells Fastn how to map your connector's native field names to the CDM. This enables automatic data normalization — a contact from your connector can be seamlessly synced to HubSpot, Salesforce, or any other connector that supports `CDMContact`.

### Step 5: Define triggers (optional)

Triggers let your connector listen for events from the third-party app:

```typescript
triggers: {
  contactCreated: {
    name: 'Contact Created',
    description: 'Fires when a new contact is created',
    entity: 'contact',
    type: 'webhook', // or 'poll'
    handler: async (ctx, webhookPayload) => {
      // Transform the webhook payload to normalized event format
      return {
        entity: 'contact',
        action: 'created',
        data: webhookPayload.contact
      };
    }
  }
}
```

For apps that don't support webhooks, use the `poll` type. Fastn's Synthetic Event Engine handles the polling, change detection (SHA-256 record hashing), and deduplication automatically.

### Step 6: Register the connector

Register your connector so the platform discovers it:

```typescript
import { ConnectorRegistry } from '@fastn/connectors';
import { myConnector } from './my-app';

ConnectorRegistry.register(myConnector);
```

After registration, your connector appears in:

* The Connectors section of the dashboard
* The step picker when building flows (Connection → Connector)
* The capability registry for MCP tool generation

{% hint style="info" %}
⚠️ **VERIFY:** Confirm the registration mechanism — is it `ConnectorRegistry.register()` or does it use a config file / auto-discovery pattern?
{% endhint %}

### Step 7: Test the connector

With the local dev environment running:

1. Open the dashboard at `http://localhost:5173`.
2. Go to **Connectors** — your custom connector should appear in the list.
3. Click **Connect** and authenticate with your test account on the third-party app.
4. Create a simple flow using your connector's actions.
5. Test the flow and verify the data comes through correctly.

Alternatively, test programmatically:

```bash
# Test the list action via the API
curl -X POST http://localhost:3001/api/v1/connectors/my-app/actions/listContacts \
  -H "Content-Type: application/json" \
  -d '{"limit": 10}'
```

> **Screenshot needed:** Custom connector appearing in the Connectors list in the local dashboard.

> **Screenshot needed:** A flow using the custom connector's action in a step, with test output showing data from the third-party app.

### Capability declaration

For advanced use cases, declare your connector's capabilities explicitly. This enables the MCP gateway to auto-generate tools from your connector:

```typescript
capabilities: {
  entities: ['contact', 'deal'],
  actions: {
    contact: ['create', 'read', 'update', 'delete', 'list'],
    deal: ['create', 'read', 'list']
  },
  events: {
    contact: ['created', 'updated', 'deleted'],
    deal: ['created']
  }
}
```

The capability registry also tracks field coverage — how completely your connector maps to the CDM. Higher coverage means better cross-connector interoperability.

### What you've built

* A custom connector implementing the ConnectorDefinition interface
* Authentication configuration (OAuth2, API Key, Basic Auth, or Custom)
* Actions with input/output schemas and handler functions
* Entity definitions mapped to CDM fields
* Triggers for webhook or poll-based event detection
* Registration with the ConnectorRegistry
