---
description: >-
  The orchestrated agent system that builds and maintains connectors — from API
  spec discovery to action creation, webhook setup, testing, and automated
  fixing.
---

# Connector Agent

The Connector Agent is an orchestrator that coordinates 6 sub-agents to handle the full lifecycle of creating and maintaining a connector. Instead of manually discovering an API, writing action handlers, setting up webhooks, and testing each action — the Connector Agent manages the entire process through specialized sub-agents.

### How it works

When you ask the Connector Agent to create a connector for a third-party app, the orchestrator:

1. **Determines the best approach** — Does the app have a machine-readable API spec? If yes, route to Spec Import Builder. If no, route to Manual Action Builder.
2. **Delegates connector creation** — The appropriate builder creates the connector definition with auth, actions, and entity mappings.
3. **Sets up webhooks** — The Event Builder creates webhook events and configures subscribe/unsubscribe lifecycle.
4. **Tests everything** — The Action Tester runs each action against a real test connection.
5. **Fixes failures** — If tests fail, the Action Fixer analyzes the error, consults real API docs, and applies patches.
6. **Hands back** — The orchestrator can pause between steps for user review, then resume when you're ready.

> **Diagram needed:** Flow diagram showing the Connector Agent orchestrator delegating to each sub-agent in sequence: Spec Import / Manual Action → Connector Builder → Event Builder → Action Tester → Action Fixer (if needed) → Done. Show handback points where the user can review.

> **🎬 GIF needed:** The Connector Agent in action — user describes a connector they need, the agent discovers the API spec, creates actions, tests them, and reports results.

### Sub-agents

#### Connector Builder

**What it does:** Creates the connector itself — auth configuration (OAuth2, API Key, Basic Auth, Custom), API actions, and entity definitions with CDM field mappings.

**When the orchestrator calls it:** After an API spec has been imported or after the user describes what actions they need.

**Input:** API spec (from Spec Import Builder) or user descriptions of required actions.

**Output:** A ConnectorDefinition with auth setup, action handlers, entity mappings, and capability declarations.

> **📷 Screenshot needed:** Connector Builder output showing a newly created connector with its actions listed and auth type configured.

***

#### Spec Import Builder

**What it does:** Finds and imports machine-readable API specs. It searches for OpenAPI 3.x, Swagger 2.x, and Postman collection files by probing common documentation URLs, detecting subdomain patterns (api._, docs._, developer.\*), and analyzing page content.

**When the orchestrator calls it:** First step when creating a connector — before building actions, check if the app publishes a spec.

**Input:** The app name or base URL.

**Output:** A parsed API spec with discovered endpoints, entities, auth requirements, and suggested actions.

**How it discovers specs:** The agent uses 20+ URL probe patterns to find documentation, detects spec format (OpenAPI, Swagger, Postman), extracts entity definitions from schemas, and infers entity types and action types from endpoints.

> **📷 Screenshot needed:** Spec Import Builder output showing a discovered OpenAPI spec with the list of extracted endpoints and entities.

***

#### Manual Action Builder

**What it does:** Creates API actions one-by-one from platform API docs when no machine-readable spec exists. Works interactively — the agent reads documentation pages, identifies endpoints, and creates action definitions.

**When the orchestrator calls it:** When Spec Import Builder can't find a machine-readable spec (the app only has human-readable docs or no public documentation).

**Input:** URL to the app's API documentation or user description of available endpoints.

**Output:** Individual action definitions with endpoint URLs, HTTP methods, request/response schemas, and parameter descriptions.

***

#### Event Builder

**What it does:** Creates webhook events for connectors and configures the full subscribe/unsubscribe lifecycle. This includes defining what events the connector can listen for (e.g., `order.created`, `contact.updated`), setting up the webhook registration endpoints, and handling webhook payload parsing.

**When the orchestrator calls it:** After the connector's actions are created — now it's time to add event-driven triggers.

**Input:** The connector definition and information about available webhook events from the API spec or documentation.

**Output:** Webhook event definitions with subscribe/unsubscribe handlers, payload schemas, and HMAC signature verification configuration.

***

#### Action Tester

**What it does:** Executes each connector action against a real test connection and reports pass/fail results. It sends actual API requests using test credentials, validates response schemas, checks HTTP status codes, and verifies data integrity.

**When the orchestrator calls it:** After the Connector Builder and Event Builder have finished creating the connector — testing validates everything works with a real API.

**Input:** The complete connector definition and test credentials for the third-party app.

**Output:** A test report for each action — pass/fail status, response data, latency, and error details for failures.

> **📷 Screenshot needed:** Action Tester results showing a list of actions with pass/fail status, response times, and error details for any failures.

***

#### Action Fixer

**What it does:** Fixes broken actions that failed during testing. It analyzes the error (wrong endpoint, incorrect schema, auth issues, missing parameters), consults the real API documentation, and applies patches to the action definition — including schema corrections and output format adjustments.

**When the orchestrator calls it:** Automatically after Action Tester reports failures. The fix → retest loop continues until all actions pass or the agent determines the issue requires human intervention.

**Input:** The failed action definition, error details from Action Tester, and access to the API documentation.

**Output:** Patched action definition with corrected schemas, endpoints, parameters, or auth configuration.

### The handback pattern

The orchestrator doesn't run all 6 sub-agents in one shot. At key points, it pauses and hands back to the user:

**After spec discovery:** "I found an OpenAPI spec with 45 endpoints. Here are the 12 most relevant actions I'd create. Want me to proceed, or should I adjust the list?"

**After connector creation:** "I've created the connector with 12 actions and 3 webhook events. Review the configuration before I test against the live API."

**After testing:** "10 of 12 actions passed. 2 failed — here's what went wrong. I can attempt to fix them, or you can adjust manually."

**After fixing:** "Both actions now pass. Ready to register the connector."

This handback pattern keeps the user in control while letting the agents handle the heavy lifting.

### When to use the Connector Agent

| Scenario                                         | Approach                                                                                |
| ------------------------------------------------ | --------------------------------------------------------------------------------------- |
| App has a public OpenAPI/Swagger spec            | Connector Agent → Spec Import → Build → Test. Fastest path.                             |
| App has API docs but no spec file                | Connector Agent → Manual Action Builder → Build → Test. More interactive.               |
| App has a proprietary or undocumented API        | Start with Manual Action Builder, provide endpoint details yourself.                    |
| You need to add actions to an existing connector | Connector Agent can extend a connector — add new actions, events, or fix existing ones. |
| A connector action broke after an API update     | Action Tester → Action Fixer loop to diagnose and patch.                                |

### Related pages

* [**Building a Custom Connector**](https://claude.ai/tutorials/developer/building-a-custom-connector.md) — Manual code-based approach using the ConnectorDefinition interface
* [**Workflow Agent**](https://claude.ai/chat/workflow-agent.md) — The equivalent orchestrated system for building workflows
