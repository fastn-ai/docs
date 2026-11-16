---
description: "An AI skill that asks about your use case, tells you which fastn pieces fit and which do not, and walks you through the setup. Use it with your AI tool, or use the decision map on this page by hand."
---

# Plan your integration

### What it is

The fastn solution architect is an AI skill. You tell it what your product should do with your customers' apps. It asks the questions it needs, tells you which fastn pieces fit, says plainly what does not fit, and then walks you through the setup one step at a time. You do not need a call with fastn.

It follows a few rules so you can trust the answer:

* It says a thing is **supported** only after it checked your live workspace in the same session. Without that check it says **likely supported, not checked**, and names the check.
* It asks one short question at a time and skips what you already told it.
* It picks the simplest piece that does the job, and says why.
* It never asks for a password, API key or secret in the chat. Credentials go into fastn's own connect screens.
* When fastn does not support something, it says so, offers a workaround if there is one, and helps you write a request to fastn.

### Use it with your AI tool

There are three ways. The first gives the most reliable answers.

#### 1. With the fastn MCP server connected

Connect your AI tool to fastn first. The skill then checks your live workspace: whether a connector exists, which actions and auth methods it has, which events it lists, and which unified APIs cover your apps. Every answer is based on what is really there.

Add fastn as an MCP server at `https://mcp.fastn.dev/fastn-workspace` and sign in. No API key is needed, and you need the **Developer** role or above. The steps for each tool are in [Connect your AI tool (MCP)](../build/mcp-gateway/README.md): [Claude](../build/mcp-gateway/claude.md), [Claude Code](../build/mcp-gateway/claude-code.md), [ChatGPT](../build/mcp-gateway/chatgpt.md), [Cursor](../build/mcp-gateway/cursor.md), [VS Code](../build/mcp-gateway/vscode.md), [Codex](../build/mcp-gateway/codex.md) and others.

Then add the skill to the same tool (next section) and ask your question.

#### 2. Without the MCP server

The skill also works with no connection to fastn. It answers from its own definitions of the fastn pieces and marks every answer **not checked**.

The skill is published in the fastn skills repository on GitHub: TODO-SKILL-REPO-URL. The folder you need is `fastn-solution-architect`.

* **Claude:** download the `fastn-solution-architect` folder from the repository as a zip, then add it as a skill in Claude's settings (see Claude's own help on adding skills).
* **Claude Code:** clone the repository, then copy the `fastn-solution-architect` folder into `~/.claude/skills/` (for all your projects) or into `.claude/skills/` inside one project. Start a new Claude Code session and ask your question.

#### 3. Any other AI tool

Paste this prompt at the start of a chat. It is a short version of the skill.

```
You are a fastn solution architect. fastn lets a SaaS product offer integrations
with the apps its customers use, set up by the customers themselves.

Your job, in order: understand the use case, evaluate it, design the solution,
guide the setup.

Rules:
- Never guess. Say "supported" only after a live check in this session. Otherwise
  say "likely supported, not checked" and name the check.
- Use only facts from https://docs.fastn.ai. Do not invent limits, prices or dates.
- One short question at a time. Skip what the user already answered.
- Prefer the simplest piece that does the job.
- Never ask for a password, API key or secret in the chat.
- If something is not supported, say so, offer a workaround if one exists, and
  help the user write a request to fastn.

Ask only what you still need:
1. What does your product do, and who are your customers?
2. In one sentence, what should happen?
3. Which apps are involved, and which one is yours?
4. Read from the app, write to it, or both?
5. Instant, on a schedule, or when something changes in the app?
6. Who connects: each customer, each user, or one shared account of yours?
7. Where does it show: inside your product, from your backend, or for an AI agent?
8. Is it the same job across similar apps (for example every CRM)?
9. How many customers and records, and how long may a run take?
10. Any constraints: your branding on sign-in screens, data rules, a deadline?

Write a 5 to 8 line summary of the requirement and ask "Is this right?".

Then map each need to a fastn piece:
- Customers connect their own account: connections + the widget or a share link
- Read or write one record in one app: a connector action, from the SDK or MCP
- Same job across every CRM, store or helpdesk: a unified API (check that each
  provider supports the operation)
- When something happens in an app, do something: an app event trigger + a workflow
- Our backend pushes data out to an app: one action call from the SDK; a webhook
  trigger + a workflow when it needs reshaping or retries
- Their system calls us: a webhook trigger + a workflow
- Every night or every hour: a schedule trigger + a workflow
- Tell our product when something happens: webhooks (event subscriptions)
- Move and reshape data between two systems: a workflow
- Customers set it up inside our product: the widget + Connect your product
- An AI agent should do it: the MCP gateway
- Our logo on the sign-in screen: our own OAuth auth provider
- The app is not in the catalog: a custom connector

Answer with: a verdict (fits / fits with gaps / does not fit today), the
requirement summary, a table of need -> piece -> what to set up -> status
(checked / not checked / gap), the gaps with workarounds, what to prepare, and
the order of work. Then guide the setup one step at a time.
```

### No AI tool: the decision map

Use this table by hand. Find the row that sounds like your need, then read the linked page.

| The need sounds like | Use | Read |
| --- | --- | --- |
| "Customers connect their own account" | Connections, plus the widget or a share link | [Connections](../build/connections/README.md), [Widget](../embed/widget-builder/README.md) |
| "Read or write one record in one app" | A connector action, called from the SDK or an AI tool | [Actions](../build/connectors/action-detail.md), [Direct app actions](../reference/sdk/app-actions.md) |
| "Same job across every CRM, store or helpdesk" | A unified API | [Unified APIs](../build/unified-apis/README.md), [Unified vs direct](../build/unified-apis/unified-vs-direct.md) |
| "When something happens in the app, do something" | An app event trigger and a workflow | [App event triggers](../build/triggers/app-events.md) |
| "Our backend pushes data out to an app" | One action call from the SDK, or a webhook trigger and a workflow when the data needs reshaping or retries | [Direct app actions](../reference/sdk/app-actions.md), [Webhook triggers](../build/triggers/webhooks.md) |
| "Their system will call us" | A webhook trigger and a workflow | [Webhook triggers](../build/triggers/webhooks.md) |
| "Every night or every hour" | A schedule trigger and a workflow | [Schedule triggers](../build/triggers/schedulers.md) |
| "Tell our product when something happens" | Webhooks to your product (event subscriptions) | [Webhooks](../manage/saas-webhooks.md), [Events in the SDK](../reference/sdk/events.md) |
| "Move and reshape data between two systems" | A workflow, with your product connected at one end | [Workflows](../build/workflows/README.md), [Common patterns](../build/patterns.md) |
| "Our customers set it up themselves in our app" | The widget, and your product connected | [Embed in your product](../embed/embedding/README.md), [Connect your product](../manage/saas-connectors.md) |
| "An AI agent should do this" | The MCP gateway | [Connect your AI tool (MCP)](../build/mcp-gateway/README.md) |
| "Our customer's own AI client should do this" | A customer MCP URL | [Customer MCP URL](../embed/embedding/customer-mcp-url.md) |
| "We need our logo on the sign-in screen" | Your own OAuth auth provider | [Auth methods and providers](../build/connectors/auth-methods.md) |
| "Build before we have credentials" | Mocks on actions | [Actions: mocks](../build/connectors/action-detail.md#mocks) |
| "The app is not in the catalog" | A connector you create | [Creating a connector](../build/connectors/creating-a-connector.md) |

When two rows fit, pick the one with less to build.

### The pieces

* **Customers**: each of your customers, with their connections and data kept apart from every other customer's. See [Customers](../operate/customers.md) and [Customers and tenancy](../tutorials/developer/understanding-tenancy.md).
* **Connectors and actions**: one app's definition and the operations you can call on it. See [Connectors](../build/connectors/README.md) and [The catalogue](../build/connectors/the-catalogue.md).
* **Auth methods and providers**: how a customer signs in to an app, and the OAuth app behind it. See [Auth methods and providers](../build/connectors/auth-methods.md).
* **Connections**: one customer's authorized link to one app. See [Connections](../build/connections/README.md).
* **Connect your product**: your own product as a connector, so integrations can reach it. See [Connect your product](../manage/saas-connectors.md).
* **Workflows**: the JavaScript code that moves and reshapes data. See [Workflows](../build/workflows/README.md).
* **Triggers**: what starts a workflow: a webhook, a schedule or an app event. See [Triggers](../build/triggers/README.md).
* **Webhooks to your product**: fastn calls your product with a signed request when something happens for a customer. See [Webhooks](../manage/saas-webhooks.md).
* **Unified APIs**: one endpoint per business object, served by whichever app each customer connected. See [Unified APIs](../build/unified-apis/README.md).
* **Widget and embedding**: the screens your customers use inside your product to connect and manage integrations. See [Widget](../embed/widget-builder/README.md) and [Embed in your product](../embed/embedding/README.md).
* **SDK and REST API**: the platform API for your backend. See [SDK](../reference/sdk/README.md) and [HTTP API](../reference/api.md).
* **Build with AI**: fastn's own builder in the dashboard. See [Build with AI](../build/agent/README.md).
* **Environments**: where each published version runs, with an optional review gate. See [Environments and GitHub](../manage/environments.md).
* **Operate**: health, alerts, events, executions and traces for each customer. See [Overview](../operate/overview.md) and [Alerts](../operate/alerts.md).
* **Settings and roles**: who can build and who can only operate. See [Roles](../manage/roles.md).
* **MCP gateway**: your integrations as tools for an AI client. See [Connect your AI tool (MCP)](../build/mcp-gateway/README.md).

### When fastn does not support something

The skill tells you plainly, offers a workaround if there is one (for example a connector you create, a webhook trigger instead of an app event, or a schedule instead of an event), and writes the request with you:

* **Need**: one sentence.
* **App and piece**: which app, and which action, event or auth method.
* **Why it matters**: what it blocks.
* **Urgency**: blocking now, needed by a date, or nice to have.

Send it to fastn from the dashboard: **Help (?)** → **Contact support**.

### Talk to a person

If you would rather talk it through, or the skill could not answer after a real attempt, contact the fastn team the same way: **Help (?)** → **Contact support**. Include the requirement summary and the verdict the skill gave you, so the conversation starts where the chat ended.

### Try it

Ask the skill one of these to start:

* "When a deal closes in our customers' CRM, we want to create an invoice in our product. Can fastn do this?"
* "Our customers use different CRMs. We want to read their contacts the same way for all of them. Which fastn pieces do we need?"
* "We want our customers' own AI assistant to create tasks in their project management tool. How do we set that up with fastn?"
