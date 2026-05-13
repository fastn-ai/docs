---
description: >-
  Organization settings, secrets, environments, domain access control, and OAuth
  Apps.
---

# Configuration

### Settings overview

All configuration lives under **Settings** in the top nav. The Settings page has a left sidebar:

| Section              | What it configures                                   |
| -------------------- | ---------------------------------------------------- |
| **People**           | Users, teams, role assignments, invitations          |
| **General**          | Organization name, timezone, domain & access control |
| **API Keys**         | Test and Live API keys for programmatic access       |
| **Secrets**          | Encrypted values workflows read at runtime           |
| **Environments**     | Deployment environments for workflows                |
| **OAuth Apps**       | Fastn-managed OAuth apps for connector auth          |
| **Billing**          | Plan tier, usage, quotas, customer limits            |
| **Customers**        | Create and manage customers                          |
| **Audit Log**        | Action history across the organization               |
| **ADVANCED → Roles** | System roles, custom roles, permission matrix        |

### General settings

Under **Settings → General**:

#### Organization settings

* **Your Role** — displays your current role (e.g., Admin)
* **Organization Name** — editable
* **Timezone** — dropdown (e.g., Asia/Karachi)

#### Domain & Access Control

* **Email Domain** — set your company domain (e.g., cin7.com). Users signing up with this domain can request to join.
* **Auto-approve domain users** — toggle. When on, domain-matched users are automatically added without manual approval.

### API Keys

Under **Settings → API Keys**:

Two types:

| Type     | Purpose                 |
| -------- | ----------------------- |
| **Test** | Development and testing |
| **Live** | Production use          |

Toggle between Test and Live views. Click **"+ Create API Key"** to generate a new key.

API keys authenticate requests via the `x-fastn-api-key` header.

### Secrets

Under **Settings → Secrets**:

"Encrypted values your workflows can read at runtime."

Secrets store sensitive credentials that workflow code needs — third-party API tokens, database connection strings. Secrets are:

* Encrypted at rest
* Never logged or exposed in error messages
* Accessible in workflow code via the ctx object

### Environments

Under **Settings → Environments**:

"Manage deployment environments for workflows."

Each environment has its own connections, secrets, and configuration. Common setup: development, staging, production.

No default environment is created — you start from scratch with **"Create your first environment."**

### OAuth Apps

Under **Settings → OAuth Apps**:

"OAuth apps fastn manages — use these when building connectors without setting up your own OAuth app."

Fastn maintains OAuth applications for common platforms. When building a connector for a listed platform, you can authenticate without setting up your own OAuth app in the third-party's developer portal.

If the platform isn't listed, you need to create your own OAuth app and configure the credentials in your connector.

### Customers

Under **Settings → Customers**:

"Manage customers under your account."

Create customers with **"Create Customer"**. Each customer gets isolated connections, data, and execution history.

### Audit Log

Under **Settings → Audit Log**:

"Track all actions performed across your organization."

Filters: All Users, All Actions, All Types, date range (From/To).

Columns: TIMESTAMP, USER, ACTION, RESOURCE, OUTCOME.

Actions include: `auth.login`, `credential.token_refresh`, and others.
