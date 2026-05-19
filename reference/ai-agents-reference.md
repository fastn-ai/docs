---
description: >-
  All 15 platform agents listed with tools, AgentTool interface, Agent Builder
  lifecycle states, and the 4-layer memory system.
---

# AI Agents Reference

### Platform agents

#### Orchestrated agents

| Orchestrator        | Sub-agents                                                                                                | Entry point                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Connector Agent** | Connector Builder, Spec Import Builder, Manual Action Builder, Event Builder, Action Tester, Action Fixer | **"Build with AI"** on Connectors page                    |
| **Workflow Agent**  | Planner Agent, Workflow Builder, Test Case Agent                                                          | **"Build with AI"** on Workflows page (orchestrator mode) |

#### Standalone agents

| Agent                           | Purpose                                                              | Entry point                             |
| ------------------------------- | -------------------------------------------------------------------- | --------------------------------------- |
| **SaaS Onboarding**             | Guide SaaS companies through platform setup                          | **Home** → Setup Assistants             |
| **Tenant Onboarding**           | Guide customers through widget-based integration setup               | Embedded widget                         |
| **Intelligence Brief**          | Research companies, produce integration strategy briefs              | Part of SaaS Onboarding (Research step) |
| **Configuration Agent**         | Probe live APIs, define filter conditions and targets                | During integration building             |
| **Standalone Workflow Builder** | Build + validate workflows only (no planner/config/connector agents) | **"Build with AI"** on Workflows page   |

### AgentTool interface

```typescript
interface AgentTool {
  name: string;
  description: string;
  inputSchema: JSONSchema;
  handler: (input: any, context: AgentContext) => Promise<any>;
}
```

### AgentContext

| Property     | Type             | Description                                                |
| ------------ | ---------------- | ---------------------------------------------------------- |
| `connectors` | ConnectorClients | Authenticated connector clients scoped to current customer |
| `tenant`     | CustomerContext  | Customer info: id, name, config                            |
| `user`       | UserContext      | Current user info: id, email, role                         |
| `memory`     | MemoryManager    | Access to all 4 memory layers                              |
| `session`    | SessionContext   | Session ID, conversation history                           |
| `config`     | object           | Configuration values                                       |
| `logger`     | Logger           | Structured logging                                         |

### Agent Builder lifecycle

| State        | Description                                              |
| ------------ | -------------------------------------------------------- |
| `PLANNING`   | User describes agent goal. Planner designs architecture. |
| `PLANNED`    | Architecture specification ready for review.             |
| `GENERATING` | Generator produces implementation files in memory.       |
| `GENERATED`  | Code ready. Synthesizer merges and validates.            |
| `TESTING`    | Ephemeral agent created for interactive testing.         |
| `DEPLOYED`   | Full AgentConfig registered in the platform.             |
| `FAILED`     | Validation or generation failed.                         |

### 4-layer memory system

| Layer          | Storage             | Purpose                                       | TTL                    |
| -------------- | ------------------- | --------------------------------------------- | ---------------------- |
| **Episodic**   | pgvector (1536-dim) | Conversation history, decisions, outcomes     | Permanent (with decay) |
| **Semantic**   | pgvector (1536-dim) | Facts about entities (SaaS, customers, users) | Permanent              |
| **Procedural** | pgvector (1536-dim) | Learned workflows and success rates           | Permanent              |
| **Working**    | Redis               | Active session context                        | 4 hours                |

#### Memory Manager

* **Context assembly**: Parallel retrieval from all 4 layers, priority-based token budgeting (2000 tokens max)
* **Session promotion**: Facts → semantic memory, outcomes → episodic memory, working memory → cleared
* **Search**: Cosine similarity with access-count reinforcement for episodic, incremental success rate for procedural
