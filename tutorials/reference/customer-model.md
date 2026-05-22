---
description: >-
  The customer hierarchy, isolation model, customer management, and data
  residency.
---

# Customer model

In Fastn, your end users are called **Customers** (alternatively called "Tenants"). Every entity in the system i.e. connections, workflows, execution logs, configurations is scoped to a specific customer.

### Hierarchy

```
Platform (Fastn)
└── Organization (Your SaaS Company)
    ├── Customer A (Your end user)
    ├── Customer B (Your end user)
    └── Customer C (Your end user)
```

### Roles

| Role          | Permissions | Scope                                         |
| ------------- | ----------- | --------------------------------------------- |
| **Owner**     | 39          | Full access within organization and customers |
| **Admin**     | 39          | Full access within organization and customers |
| **Developer** | 34          | Build connectors, workflows, agents           |
| **Operator**  | 18          | Operational access                            |
| **Viewer**    | 7           | Read-only access                              |
| **End User**  | 9           | Customer-facing widget access                 |

Roles are managed under **Settings → ADVANCED → Roles**. Custom roles can be created or duplicated from system roles.

### Customer isolation

Isolation is enforced at the database level:

* **Row-Level Security (RLS)** policies on customer-scoped database tables
* PostgreSQL session variables (`app.tenant_id`, `app.role`) set per request
* Every query automatically filters by the customer's ID
* No customer can read, write, or reference another customer's data

### Customer management

Customers are managed under **Settings → Customers**.

| Action           | How                                                  |
| ---------------- | ---------------------------------------------------- |
| Create           | Click **"Create Customer"**                          |
| View             | Customer list with IDs                               |
| Customize limits | **Settings → Billing → "Customize Customer Limits"** |

### Data residency

Customers can be configured for regional data residency:

| Region   | Description                   |
| -------- | ----------------------------- |
| **US**   | Data stored in United States  |
| **EU**   | Data stored in European Union |
| **APAC** | Data stored in Asia-Pacific   |

### SaaS partner signup

SaaS partners register through a validation pipeline:

1. Email validation (domain check against \~40 personal provider blocklist)
2. Duplicate check (existing domain lookup)
3. LLM classification (industry, tech stack, integration needs)
4. Outcome: approved, provisional, manual\_review, or rejected

Each partner gets an organization with the **Free** plan by default.
