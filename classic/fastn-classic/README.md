---
description: >-
  V1 is in maintenance mode. It will be supported until sunset. New features are
  only available in V2.
---

# Fastn Classic

This section contains documentation for **Fastn V1** — the original embedded integration platform. V1 is currently in **maintenance mode**: active bugs are addressed, but no new features will be added. All new development is happening in [Fastn V2](https://claude.ai/README.md).

If you are starting a new project, use V2.

### What is V1?

Fastn V1 is a UI-driven embedded integration platform that lets SaaS companies give their customers pre-built connectors and automation flows. You configure connectors, build flows using a visual step editor, and embed an integration widget into your product.

V1 does not include the Canonical Data Model, TypeScript DSL, AI agents, or the MCP Gateway. These are V2-only capabilities.

### V1 vs V2 at a Glance

|                    | V1 (Legacy)                | V2                                                  |
| ------------------ | -------------------------- | --------------------------------------------------- |
| Workflow authoring | Visual step editor         | TypeScript DSL + visual canvas                      |
| Connector building | UI-only                    | Code-first (`ConnectorDefinition`)                  |
| AI agents          | Not available              | 7 platform agents + custom Agent Builder            |
| Data model         | Connector-specific schemas | Canonical Data Model (CDM)                          |
| Auth               | OAuth2, API Key            | OAuth2, API Key, SSO (Keycloak)                     |
| Multi-tenancy      | Single-tier                | Three-tier (Platform Admin / SaaS Admin / End User) |
| Status             | **Maintenance only**       | **Active development**                              |

### Support Timeline

V1 will be supported until the official sunset date is announced. When sunset is confirmed, this section will be archived and a migration guide will be published.

If you are on V1 and want to understand what moving to V2 involves, see the [Migration Guide](https://claude.ai/resources/migration-guide.md).

{% hint style="info" %}
⚠️ No new features will be added to V1. If a capability you need is not in V1, it will not be backported. Check the V2 docs to see if it is available there. \{% endhint %\}
{% endhint %}

### Known Limitations in V1

These gaps are documented and will not be fixed. They are resolved in V2.

**Sync & Scheduling**

* Scheduled sync cadence (daily / weekly / monthly / quarterly) is not available for folder-based file connectors. Only manual and event-based modes exist.
* Scheduler triggers can occasionally fail to pick up jobs, causing missed data runs.

**Connector & Flow Building**

* OAuth setup for custom connectors requires steps that are not fully surfaced in the UI. Expect to need support assistance the first time.
* Step-level test harness is not available. You cannot test a single connector step in isolation — you have to run the full flow.
* Copy-paste of flow steps can fail intermittently and requires a page reload to recover.
* Simple conditional logic (null checks, default values) requires multiple flow steps. There is no shorthand.

**Configuration Discoverability**

* Configuration dependencies — for example, linking a flow to a widget action — are not surfaced in the UI. You have to know to go to **Settings → Configurations** to find them.
* Some setup options are hidden behind toggles that are not labelled clearly. If something is not working, check for a collapsed or inactive toggle before raising a support ticket.

**Logs & Debugging**

* Execution logs show run time and return value only. Data passed between steps is not visible. You cannot inspect intermediate state without adding explicit output steps to your flow.
* Log search does not consistently return results when filtering by partial tenant ID. Use the full ID where possible.

**Editor Stability**

* The SQL and custom code editors do not retain unsaved state if you lose focus or navigate away. Save frequently.

### Finding V1 Documentation

Use the navigation under this **Legacy** section. The structure covers:

* **Getting Started** — account setup, first connector, first flow
* **Embedded Integrations** — connectors, flows, widget embedding
* **Tutorials & Resources** — step-by-step walkthroughs

{% hint style="info" %}
⚠️ **You are reading legacy documentation.** Features, UI labels, and configuration steps described here apply to V1 only. Do not mix V1 and V2 concepts  the architectures are fundamentally different. If you are unsure which version you are on, check your dashboard URL or contact your Fastn account manager.
{% endhint %}
