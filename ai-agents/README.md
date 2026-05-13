---
description: >-
  Fastn's 15 AI agents — what each one does, how they work together, and how
  orchestrated agents coordinate sub-agents for complex tasks.
hidden: true
---

# AI Agents

Fastn uses AI agents powered by Anthropic Claude throughout the platform. Agents handle onboarding, connector building, workflow creation, API discovery, testing, configuration, and integration planning — tasks that would otherwise require manual setup or engineering time.

There are 15 agents total. Some are standalone — they handle a single task end to end. Others are **orchestrated** — a parent agent coordinates multiple sub-agents that each handle one part of a complex workflow, with handback support so the orchestrator can resume control between steps.

### How agents are organized

#### Orchestrated agents

These are multi-agent systems where a parent orchestrator manages sub-agents:

[**Connector Agent**](https://claude.ai/chat/connector-agent.md) — Builds and maintains connectors. The orchestrator coordinates 6 sub-agents: Connector Builder, Spec Import Builder, Manual Action Builder, Event Builder, Action Tester, and Action Fixer. Together they handle everything from discovering an API spec to creating actions, setting up webhooks, testing against real connections, and fixing failures.

[**Workflow Agent**](https://claude.ai/chat/workflow-agent.md) — Builds and validates workflows. The orchestrator coordinates 3 sub-agents: Planner Agent, Workflow Builder, and Test Case Agent. Together they analyze requirements, produce a build plan, create the workflow, generate test cases, and validate the result.

#### Standalone agents

These agents operate independently for a specific purpose:

[**SaaS Onboarding**](https://claude.ai/chat/saas-onboarding.md) — Guides SaaS companies through initial platform setup: connectors, integration packs, widget configuration, and go-live readiness.

[**Tenant Onboarding**](https://claude.ai/chat/tenant-onboarding.md) — Helps end customers connect their tools, map fields, configure syncs, and set up automations through the embedded widget experience.

[**Intelligence Brief**](https://claude.ai/chat/intelligence-brief.md) — A multi-agent graph that researches companies using public information and produces integration strategy briefs with recommended connectors and workflow patterns.

[**Configuration Agent**](https://claude.ai/chat/configuration-agent.md) — Probes live APIs to gather sample data, helps users define filter conditions and targets, and manages complex configuration scenarios.

### Agent architecture (common to all agents)

Every agent — standalone or orchestrated — shares the same underlying architecture:

**Tool-use loop** — Agents use Anthropic Claude's tool-use pattern. The model receives the conversation, decides which tool to call, the tool handler executes, and the result feeds back to the model. This loop continues until the task is complete.

**AgentContext** — Every tool handler receives context scoped to the current tenant and user, including authenticated connector clients, configuration, and memory access.

**4-layer memory** — Agents maintain context across sessions through episodic memory (conversation history), semantic memory (facts about entities), procedural memory (learned workflows with success rates), and working memory (active session context with a 4-hour TTL in Redis).

**Orchestrator pattern** — For orchestrated agents, the parent agent decides which sub-agent to invoke, passes context, and handles handback when the sub-agent completes or needs intervention. This allows complex multi-step tasks to be broken into specialized pieces while maintaining coordination.

> **🖼️ Diagram needed:** Visual showing the orchestrator pattern — parent agent at the top, sub-agents branching below, arrows showing task delegation and handback flow. Use the Connector Agent as the example with its 6 sub-agents.

> **🖼️ Diagram needed:** The 4-layer memory system — Episodic (pgvector), Semantic (pgvector), Procedural (pgvector), Working (Redis 4h TTL). Show how memory assembles context before each agent turn and promotes facts after session ends.
