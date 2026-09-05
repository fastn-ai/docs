---
description: An overview of how tenancy works per user and org level in Fastn
---

# Understanding Tenancy

Fastn supports two ways to scope connections within the same embed: org-level (shared) and user-level (per individual). Choosing correctly determines who can see and use which connections.

### The distinction

**Org-level (shared)** — One connection serves the entire customer organization. Anyone in that organization uses the same connection. Use this for shared systems of record.

**User-level (per individual)** — Each user has their own connection, isolated from other users in the same organization. Use this for resources tied to one person's identity.

{% hint style="info" %}
This is **not** an "internal vs external user" distinction, and it is **not** about who can edit. It is strictly shared-vs-personal, based on who owns the connected resource.
{% endhint %}

### How to decide

Ask who owns the resource being connected:

| Resource type                         | Scope      | Examples                                                           |
| ------------------------------------- | ---------- | ------------------------------------------------------------------ |
| Shared systems of record              | Org-level  | CRM, project management, data warehouse, shared messaging channels |
| Personal identity, inbox, or calendar | User-level | A person's email, personal calendar, individual account            |

A shared Salesforce instance that the whole company uses is org-level. An individual sales rep's email inbox is user-level. Most customers need both in the same embed — a shared CRM connection plus each rep's own email.

### How it's set in the embed

The tenancy choice is encoded in the iframe URL and the identity the token is minted with.

**User-level (per individual):**

```
https://live.gcp.fastn.ai/api/v1/embed/iframe?tenant-id=<endOrgId>&token=<token>
```

The `tenant-id` parameter is present. Combined with the `userEmail` and `userName` in the token body, connections are isolated to that individual user.

**Org-level (shared):**

```
https://live.gcp.fastn.ai/api/v1/embed/iframe?token=<token>
```

No `tenant-id` parameter. Connections are shared across the organization.

### Persona examples

These illustrate the typical mix of shared and personal connections per buyer persona:

| Persona                            | Org-level (shared) | User-level (personal)         |
| ---------------------------------- | ------------------ | ----------------------------- |
| Integration Backlog Owner (VP Eng) | Jira, Slack        | Google Calendar               |
| Product Manager                    | Ad account, CRM    | Slack alerts                  |
| CRO                                | Salesforce         | Each rep's email              |
| Head of Solution Engineering       | Snowflake, CRM     | Each tester's sandbox account |
| Head of Customer Success           | Usage-data system  | Each CSM's calendar / email   |

The through-line: shared systems of record map to org-level; personal identity, inbox, or calendar maps to user-level. Most customers need both, which is why both flavors exist.
