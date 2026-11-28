---
description: "EnforcedFlow routes leads with round-robin assignment. Read round-robin groups and agents, get the next agent and create review tasks."
hidden: true
---

# EnforcedFlow

<img src="../../.gitbook/assets/connectors/lg/enforced-flow.png" alt="EnforcedFlow logo">

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [enforcedflow.com](https://enforcedflow.com) |
| **Authentication** | API key |
| **Slug** | `enforcedFlow` |

## Setup

Your customers enter their API key for EnforcedFlow when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect EnforcedFlow from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **EnforcedFlow**.
2. Select **Connect** on the EnforcedFlow card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use EnforcedFlow's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Human In The Loop Task</td><td><code>createHumanInTheLoopTask</code></td><td>Create an EnforcedFlow Human in the Loop review task so a person can approve, reject or edit generated content before an automation continues. Returns the task and its review URL. EnforcedFlow does not notify anyone itself: your own workflow is responsible for delivering the review URL to the reviewer. EnforcedFlow exposes no delete route for tasks, so every task created here is permanent.</td></tr><tr><td>Get Authenticated Account</td><td><code>getAuthenticatedAccount</code></td><td>Return the EnforcedFlow account that the configured Provider Key belongs to, as a name and email pair. Use this to verify a connection is live and to identify which EnforcedFlow account the key authenticates as.</td></tr><tr><td>Get Group Routing Fields</td><td><code>getGroupRoutingFields</code></td><td>Return the routing field configuration of one advanced round-robin group: each field's machine name, label, evaluator type, AI instructions and selectable options, plus the list of agent metadata field names. Use it to discover which criteria keys Get Next Agent will accept for the group.</td></tr><tr><td>Get Human In The Loop Task</td><td><code>getHumanInTheLoopTask</code></td><td>Retrieve one EnforcedFlow Human in the Loop review task by id, including its current review status and the content as the reviewer left it. Poll this after creating a task to detect when a human has approved, rejected or edited it, since EnforcedFlow sends no webhook of its own.</td></tr><tr><td>Get Next Agent</td><td><code>getNextAgent</code></td><td>Select the next agent from an advanced round-robin group, applying the supplied routing criteria. MultiSelect fields take an array of option labels and match case-insensitively; AISelect fields take raw text that GPT-4o-mini classifies against the configured options; weight and timezone evaluators are applied automatically. Empty criteria match any agent. Returns the chosen agent and an agent_found flag. This advances the group's round-robin pointer, so do not run it against a live production group unless you intend the assignment.</td></tr><tr><td>List Group Agents</td><td><code>listGroupAgents</code></td><td>List every agent belonging to one advanced round-robin group, with the agent id, display name, custom metadata, active flag and field evaluator values. Optionally filter to only active or only inactive agents.</td></tr><tr><td>List Round Robin Groups</td><td><code>listRoundRobinGroups</code></td><td>Retrieve every EnforcedFlow advanced round-robin group the Provider Key can access, including each group's id, name and the routing field configuration used to filter agents. Use this first to discover the groupId required by every other EnforcedFlow action.</td></tr><tr><td>Upsert Group Agent</td><td><code>upsertGroupAgent</code></td><td>Create a new agent in an advanced round-robin group, or update the first existing agent matching the filter. The filter matches on agent id first, then on name and active with AND logic, then on JSON containment of each meta key; an empty filter always creates. Returns the agent and a created flag. EnforcedFlow exposes no delete route for agents, so an agent created here can only be retired by setting active to false.</td></tr><tr><td>Upsert Group Agent Via Post</td><td><code>upsertGroupAgentViaPost</code></td><td>Undocumented POST form of the agent upsert route, accepted by EnforcedFlow alongside PUT on the same path and with the same filter and data body. Provided for callers and proxies that cannot issue PUT. Prefer Upsert Group Agent unless PUT is unavailable. EnforcedFlow exposes no delete route for agents, so an agent created here can only be retired by setting active to false.</td></tr></tbody></table>

