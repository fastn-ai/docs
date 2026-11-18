---
description: "EnforcedFlow intelligent lead routing and advanced round-robin distribution."
---

# EnforcedFlow

EnforcedFlow intelligent lead routing and advanced round-robin distribution. Manage round-robin groups, inspect their routing field configuration, list and upsert the agents in a group, and request the next agent the round-robin should assign work to, with MultiSelect, AI-classified, weighted and timezone-aware filtering.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [enforcedflow.com](https://enforcedflow.com) |
| **Authentication** | API key |
| **Actions** | 9 |
| **Events** | 0 |
| **Slug** | `enforcedFlow` |

## Use it

Add EnforcedFlow from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.enforcedFlow.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Human In The Loop Task | `createHumanInTheLoopTask` | Create an EnforcedFlow Human in the Loop review task so a person can approve, reject or edit generated content before an automation continues. Returns the task and its review URL. EnforcedFlow does not notify anyone itself: your own workflow is responsible for delivering the review URL to the reviewer. EnforcedFlow exposes no delete route for tasks, so every task created here is permanent. |
| Get Authenticated Account | `getAuthenticatedAccount` | Return the EnforcedFlow account that the configured Provider Key belongs to, as a name and email pair. Use this to verify a connection is live and to identify which EnforcedFlow account the key authenticates as. |
| Get Group Routing Fields | `getGroupRoutingFields` | Return the routing field configuration of one advanced round-robin group: each field's machine name, label, evaluator type, AI instructions and selectable options, plus the list of agent metadata field names. Use it to discover which criteria keys Get Next Agent will accept for the group. |
| Get Human In The Loop Task | `getHumanInTheLoopTask` | Retrieve one EnforcedFlow Human in the Loop review task by id, including its current review status and the content as the reviewer left it. Poll this after creating a task to detect when a human has approved, rejected or edited it, since EnforcedFlow sends no webhook of its own. |
| Get Next Agent | `getNextAgent` | Select the next agent from an advanced round-robin group, applying the supplied routing criteria. MultiSelect fields take an array of option labels and match case-insensitively; AISelect fields take raw text that GPT-4o-mini classifies against the configured options; weight and timezone evaluators are applied automatically. Empty criteria match any agent. Returns the chosen agent and an agent_found flag. This advances the group's round-robin pointer, so do not run it against a live production group unless you intend the assignment. |
| List Group Agents | `listGroupAgents` | List every agent belonging to one advanced round-robin group, with the agent id, display name, custom metadata, active flag and field evaluator values. Optionally filter to only active or only inactive agents. |
| List Round Robin Groups | `listRoundRobinGroups` | Retrieve every EnforcedFlow advanced round-robin group the Provider Key can access, including each group's id, name and the routing field configuration used to filter agents. Use this first to discover the groupId required by every other EnforcedFlow action. |
| Upsert Group Agent | `upsertGroupAgent` | Create a new agent in an advanced round-robin group, or update the first existing agent matching the filter. The filter matches on agent id first, then on name and active with AND logic, then on JSON containment of each meta key; an empty filter always creates. Returns the agent and a created flag. EnforcedFlow exposes no delete route for agents, so an agent created here can only be retired by setting active to false. |
| Upsert Group Agent Via Post | `upsertGroupAgentViaPost` | Undocumented POST form of the agent upsert route, accepted by EnforcedFlow alongside PUT on the same path and with the same filter and data body. Provided for callers and proxies that cannot issue PUT. Prefer Upsert Group Agent unless PUT is unavailable. EnforcedFlow exposes no delete route for agents, so an agent created here can only be retired by setting active to false. |
