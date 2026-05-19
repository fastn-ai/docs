---
description: >-
  Build a custom AI agent using the AgentTool interface or the Agent Builder's
  natural language lifecycle.
---

# Creating a Custom AI Agent

**Prerequisites:** [Local Dev Environment Setup](https://claude.ai/chat/local-dev-environment-setup.md). Understanding of LLM tool-use patterns.&#x20;

Fastn includes 15 built-in agents covering:

* Onboarding (SaaS Onboarding, Tenant Onboarding)
* Building (Connector Builder, Workflow Builder, Event Builder, and their orchestrator-managed variants)
* API management (Spec Import Builder, Manual Action Builder)
* Testing (Test Case Agent, Action Tester, Action Fixer)
* Intelligence (Intelligence Brief, Planner Agent)
* Configuration (Configuration Agent).

When you need an agent tailored to your specific use case, you can build one in two ways — via code using the AgentTool interface, or via natural language using the Agent Builder.

### Option A: Building an agent in code

#### The AgentTool interface

Each tool an agent can use implements the AgentTool interface:

```typescript
interface AgentTool {
  name: string;
  description: string;
  inputSchema: object;  // JSON Schema for the tool's input
  handler: (input: any, context: AgentContext) => Promise<any>;
}
```

#### Define your tools

```typescript
const lookupCustomer: AgentTool = {
  name: 'lookup_customer',
  description: 'Look up a customer by email address and return their account details, recent orders, and integration status.',
  inputSchema: {
    type: 'object',
    properties: {
      email: { type: 'string', description: 'Customer email address' }
    },
    required: ['email']
  },
  handler: async (input, context) => {
    const customer = await context.connectors.crm.findByEmail(input.email);
    const orders = await context.connectors.shopify.listOrders({
      customerId: customer.id,
      limit: 5
    });
    return {
      customer,
      recentOrders: orders,
      integrationStatus: customer.integrations
    };
  }
};

const createSupportTicket: AgentTool = {
  name: 'create_support_ticket',
  description: 'Create a support ticket in the helpdesk system for a customer issue.',
  inputSchema: {
    type: 'object',
    properties: {
      customerId: { type: 'string' },
      subject: { type: 'string' },
      description: { type: 'string' },
      priority: { type: 'string', enum: ['low', 'medium', 'high', 'critical'] }
    },
    required: ['customerId', 'subject', 'description']
  },
  handler: async (input, context) => {
    const ticket = await context.connectors.helpdesk.createTicket(input);
    await context.connectors.slack.sendMessage({
      channel: '#support',
      text: `New ticket: ${input.subject} (${input.priority})`
    });
    return ticket;
  }
};
```

#### Create the agent

```typescript
import { createAgent } from '@fastn/agents';

const supportAgent = createAgent({
  name: 'support_agent',
  description: 'Helps support team look up customers, check integration status, and create tickets.',
  model: 'claude-sonnet-4-20250514', // or 'claude-opus-4-20250514', 'claude-haiku'
  tools: [lookupCustomer, createSupportTicket],
  systemPrompt: `You are a support agent for our platform. 
    When a support team member asks about a customer, look them up first.
    If they need to create a ticket, gather the required details before creating it.
    Always confirm actions before executing them.`
});
```

The agent uses Anthropic Claude's tool-use loop (`runAgentTurn`) — the model receives the conversation, decides which tool to call, the handler executes, and the result feeds back to the model.

#### AgentContext

Every tool handler receives an `AgentContext` that provides:

| Property             | What it contains                                               |
| -------------------- | -------------------------------------------------------------- |
| `context.connectors` | Authenticated connector clients scoped to the current customer |
| `context.tenant`     | Customer information (id, name, config)                        |
| `context.user`       | Current user information                                       |
| `context.memory`     | Access to the 4-layer memory system                            |
| `context.session`    | Session ID and conversation history                            |

### Option B: Using the Agent Builder

The Agent Builder lets you create agents via natural language. No code required — describe what you want, and Fastn generates the agent.

#### The build lifecycle

1. **PLANNING** — You describe the agent's goal. The planner agent designs an architecture specification.
2. **PLANNED** — Architecture is ready for review.
3. **GENERATING** — The generator agent produces implementation files in memory.
4. **GENERATED** — Code is ready. The synthesizer merges and validates it.
5. **TESTING** — An ephemeral agent is created for interactive testing.
6. **DEPLOYED** — Full AgentConfig is registered in the platform. (Or **FAILED** if validation fails.)

#### Using the Agent Builder

1. Click **"Build with AI"** on the Connectors or Workflows page — or access the Agent Builder if available under the Home section.
2. Navigate to the Agent Builder section.
3. Describe your agent:

{% code overflow="wrap" %}
```
"Build me an agent that helps our support team look up customer accounts by email, check their integration status across Shopify and Xero, and create support tickets when there's an issue. The agent should always confirm before creating a ticket."
```
{% endcode %}

4. Review the generated architecture and tools.
5. Test the agent interactively — ask it questions and verify it uses the tools correctly.
6. Deploy when satisfied.

> **Screenshot:** Agent Builder interface showing the natural language input and the generated agent architecture.

> **GIF:** Agent Builder flow — entering a description, reviewing the generated tools, testing with a sample conversation, deploying.

### Agent memory

Agents have access to a 4-layer memory system that persists across sessions:

| Layer          | Storage        | Purpose                                       | Key operations                                         |
| -------------- | -------------- | --------------------------------------------- | ------------------------------------------------------ |
| **Episodic**   | pgvector       | Conversation history, decisions, outcomes     | Write episodes, search by similarity, decay importance |
| **Semantic**   | pgvector       | Facts about entities (SaaS, customers, users) | Write/upsert facts, search by subject                  |
| **Procedural** | pgvector       | Learned workflows and success rates           | Write procedures, track success rates                  |
| **Working**    | Redis (4h TTL) | Active session context                        | Store messages, tool calls, temporary facts            |

The Memory Manager assembles context from all 4 layers before each agent turn, with a 2000-token budget. After a session ends, relevant facts are promoted from working memory to semantic memory, and outcomes go to episodic memory.

This means agents learn over time — an agent that successfully resolves a customer issue remembers the resolution pattern and applies it to similar issues in the future.

### Registering and deploying a code-based agent

```typescript
import { registerAgent } from '@fastn/agents';

registerAgent(supportAgent);
```

After registration, the agent is available via:

* The **"Build with AI"** buttons on the Connectors or Workflows pages
* The API at `/api/v1/ai/chat`
* The MCP gateway (if exposed as a tool)

### What you've built

* A custom agent with defined tools (via code or Agent Builder)
* Tool handlers that use connector clients and customer context
* Understanding of the agent memory system
* Knowledge of the Agent Builder lifecycle for no-code agent creation
