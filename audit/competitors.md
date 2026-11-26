# Competitor docs benchmark for docs.fastn.ai

Researched 2026-11-24 from each vendor's live docs and their `llms.txt` indexes. Quoted terms are as they appear in those docs. Where a cell says "none", that vendor's docs had no first-class term for the concept. fastn's column reflects the target vocabulary given in the brief, with notes where the live docs (this repo) disagree with it.

Sources (index pages used for navigation):
- Paragon: https://docs.useparagon.com/llms.txt
- Merge: https://docs.merge.dev/llms.txt
- Nango (docs moved to nango.dev/docs): https://nango.dev/docs/llms.txt
- Prismatic: https://prismatic.io/docs/llms.txt
- Ampersand (docs moved to docs.ampersand.ai): https://docs.ampersand.ai/llms.txt
- Composio: https://docs.composio.dev/llms.txt
- Pipedream Connect: https://pipedream.com/docs/llms.txt (Connect section)
- Arcade: https://docs.arcade.dev/llms.txt and https://docs.arcade.dev/en/home
- Workato Embedded: https://docs.workato.com/oem.html and https://docs.workato.com/oem/oem-api/managed-users
- fastn: https://docs.fastn.ai/ plus this repo's `SUMMARY.md`, `reference/glossary.md`, `getting-started/quickstart.md`

---

## 1. Terminology matrix

The matrix is split in two so it stays readable. Table A covers the embedded iPaaS and unified API vendors, and Table B covers the agent auth and tool vendors. fastn appears in both.

### Table A: embedded iPaaS and unified API vendors

| Concept | fastn (current) | Paragon | Merge | Prismatic | Ampersand | Workato Embedded |
|---|---|---|---|---|---|---|
| The SaaS company's customer (org) | customer (the API says "end org"; the repo also uses "tenant" about 54 times) | no org noun. "Connected User", keyed by the JWT `sub`, which is "a user or their company" | "end user" plus `end_user_organization_name` | "Customer" ("The organization's customer (not Prismatic's)"). The SaaS company itself is "Organization" | "group" ("a company, team, or workspace within your app") | "Customer" (API resource `managed_users`) |
| The person at the customer | user (org-level vs user-level connection) | "Connected User" / "your users" | "end user" (`end_user_origin_id`, `end_user_email_address`). Agent Handler: "Registered User" | "Customer User" | "consumer" ("an individual end user that installs an integration") | "collaborators" / "members" of a customer |
| App definition | connector | "Integration" / "Integration Providers"; "Custom Integrations" | "Integration" (Unified); "Connector" (Agent Handler) | "Connector" / "Component" (stated synonyms) | "Provider" + "Provider app" (your OAuth app) | "connector" ("Shared connectors"; "Adapters" in the API) |
| Stored credential / account link | connection | no first-class noun: "your users' app accounts", "credential", "Multi-Account Authorization" | "Linked Account" (+ "account token") | "Connection" ("Credentials ... a connector uses to authenticate") | "Connection" ("a SaaS credential that Ampersand stores"); "Installation" = integration per customer | "Connection" |
| Logic that runs | workflow | "Workflows"; "ActionKit" actions; "Managed Sync" | none user-authored; Merge-run "syncs" | "Integration" made of "Flows"; deployed per customer as an "Instance" | "read / write / subscribe actions" in `amp.yaml`; each run is an "Operation" | "Recipe" |
| Embedded UI | widget | "Connect Portal" ("Headless Connect Portal") | "Merge Link" (plus "Magic Link") | "Marketplace" + "Config Wizard"; "Embedded Workflow Builder"; "Solis" headless SDK | "Prebuilt UI components" (`InstallIntegration`); "Headless UI library" | "Iframes" ("Workato Fully Embedded"); "Connection widget" |
| Per-customer config | setup / config | "User Settings" (integration-level and workflow-level); "Field Mapping"; "Multi-Configuration" | "Field Mapping"; "Scopes" | "Config variables" collected by the "Config Wizard" | "Config" ("A customer's preference for which objects and fields...") | "Environment properties"; "Lookup tables" |
| Dashboard | fastn dashboard | "Paragon dashboard" | "Merge dashboard" | the Prismatic app ("Organization") | "Ampersand Dashboard" | "Admin console" |
| Backend auth key | API key (`fsk_test_` / `fsk_live_`) | "Signing Key" (one per environment; signs the user JWT) | "API key" / "Production Access key" | "signing key" (embedded); refresh token for the GraphQL API | "API key" (`X-Api-Key`) or a registered JWT key pair | "API client" tokens |
| Frontend short-lived token | embed token (`emb_`, 8 h) | "Paragon User Token" (a JWT you sign) | "link token" (30 min) -> "public token" -> "account token" | embedded "JWT" signed by you | "JWT" | "JWT direct linking" |
| Unified / common model API | unified API | "Managed Sync" + "Synced Objects" (normalized) | "Unified API", "Common Models", "Categories" | none | "Build your own unified API" | none |
| Triggers / events | trigger (webhook, schedule, app event) | "Triggering Workflows": "App Events", "Request Trigger", "Integration Trigger", "Scheduler Trigger" | "Webhooks" (`sync_completed`) | "Trigger" ("webhook, schedule, or app event") | "Subscribe actions"; "Destinations"; "Notifications" | recipe trigger |
| Logs / observability | Logs (Operate: Activity, Events, Traces, Executions) | "Monitoring", "Event Logs", "Task History", "Event Destinations" | Agent Handler "tool call logs"; "audit trail" | "Instance Executions", "Alert Monitors" | "Operations" / "operation logs" | jobs; "Audit log streaming" |
| MCP / agent tool access | fastn Connect (MCP gateway) | "ActionKit", "Paragon MCP Server" | "Merge Agent Handler" ("Tool Packs", "Security Gateway") | "MCP flow server", "Agentic flows" | "Ampersand AI SDK" | "Enterprise MCP" |
| AI builder | fastn agent (repo also says "Build with AI", "Agent", "AI builder") | "Building with Agents" (Agent Skills for your IDE) | none | "Build with Code and AI"; customer-facing "AI copilot" | "Start with AI"; "builder MCP server" | Agent Studio (platform-wide, not Embedded) |

### Table B: agent auth and tool vendors

| Concept | fastn (current) | Nango | Composio | Pipedream Connect | Arcade |
|---|---|---|---|---|---|
| The SaaS company's customer (org) | customer | "tenant" ("whose connected accounts an agent can use"); the old "end user" is deprecated with a migration guide | none (only "user"); "B2B agents" page | none (only "external user") | none (only "user"); "User Sources" for SSO |
| The person at the customer | user | "end user" (`end_user_id` tag) | "user" (`userId`: "An identifier from your application...") | "external user" (`external_user_id`) / "end user" | "user" (`user_id`, often an email) |
| App definition | connector | "Integration" (instance of a "Provider") | "Toolkit" + "Auth Config" (the auth blueprint); legacy "app" | "App" | "MCP Server" (renamed from "toolkit"); "Auth Provider" |
| Stored credential / account link | connection | "Connection" | "Connected Account" (renamed from "connection") | "Connected account" | none as a noun: the user "authorizes" a scope |
| Logic that runs | workflow | "Functions" (syncs, tools; "actions" deprecated) | "Tool" (renamed from "action") | "Actions", "Triggers" ("components"); "Workflows" | "Tool" |
| Embedded UI | widget | "Connect UI" (or "headless auth") | "Connect Link" (hosted page) | "Connect Link"; Client SDK (`connect-react`) | hosted authorization URL ("Secure and Brand the Auth Flow") |
| Per-customer config | setup / config | "Connection tags, config, and metadata" | session config | "App Overrides"; configured props | "Contextual Access" |
| Dashboard | fastn dashboard | "Nango dashboard" / "Environment Settings" | Composio dashboard | Pipedream project UI | "Arcade Dashboard" |
| Backend auth key | API key | "Environment API key" (legacy "secret key") | "Composio API Key" (project) + "Organization API Key" | "OAuth client" (client ID and secret) | "API key" (per project) |
| Frontend short-lived token | embed token | "connect session" -> "session token" | none (hosted Connect Link) | "Connect token" (4 h, single use) | none (authorization URL) |
| Unified / common model API | unified API | "Unified APIs with functions" (build your own) | none | none | none |
| Triggers / events | trigger | "Triggers" (webhook processing, "Webhook functions") | "Trigger" | "Triggers" ("Deploying Triggers") | none |
| Logs / observability | Logs | "Logs" tab, "Function logging", "Observability", "Audit trail" | Troubleshooting | usage records | "Tool Executions", "Audit Logs" (OpenTelemetry) |
| MCP / agent tool access | fastn Connect | "Agent sessions", "Toolsets & tools", "Meta tools" | "Sessions" (`session.mcp.url`), "Single-toolkit MCP" | "MCP Servers" (Pipedream MCP) | "MCP Gateways", "Arcade Engine" |
| AI builder | fastn agent | "Coding agent setup", "Management MCP", "Docs MCP server" | "Agent plugins", "Set up a coding agent" | "Develop with Pipedream MCP" | "Agent Plugin"; gateways "Create via AI" |

Key citations for the matrix:
- Paragon Connected User and signing key: https://docs.useparagon.com/getting-started/installing-the-connect-sdk.md ; User Settings: https://docs.useparagon.com/connect-portal/workflow-user-settings/workflow-user-settings.md
- Merge tokens and Linked Account: https://docs.merge.dev/merge-unified/merge-link.md ; Agent Handler concepts: https://docs.merge.dev/merge-agent-handler/how-it-works.md
- Prismatic terminology block: https://prismatic.io/docs/llms.txt (section "Terminology")
- Ampersand terminology: https://docs.ampersand.ai/terminology
- Nango tenant: https://nango.dev/docs/guides/agent-sessions/tenant.md ; end-user migration: https://nango.dev/docs/guides/platform/migrations/migrate-from-end-user.md ; Connect UI: https://nango.dev/docs/guides/auth/customize-connect-ui
- Composio glossary (with legacy renames): https://docs.composio.dev/docs/glossary
- Pipedream Connect tokens: https://pipedream.com/docs/connect/managed-auth/tokens
- Arcade glossary: https://docs.arcade.dev/en/resources/glossary
- Workato Embedded customers: https://docs.workato.com/oem/oem-api/managed-users

---

## 2. Docs IA comparison

| Vendor | Top-level nav | Quickstart shape | Architecture diagram | Try-it / sandbox | Samples repo | API reference style | Per-audience paths | Right-side outline / AI-readable docs |
|---|---|---|---|---|---|---|---|---|
| **fastn** (GitBook) | Getting Started, Tutorials (SaaS Admin / Developer / End User), Build, Embed, Operate, Manage, Reference, Classic | 8 steps, "about twenty minutes" (the home page says a "five-minute trial"), UI-first via Build with AI | Yes: the "Build once, extend per customer, use everywhere" figure on the home page | Workflow Test tab (Live / Partial Mock / Fully Mock), all inside the product | none linked | Hand-written markdown (`reference/api.md`); no OpenAPI-rendered reference | Yes: three audience cards on home + Tutorials by role | GitBook outline; `llms.txt` returns 200 |
| **Paragon** | Platform, Managed Sync, Workflows, Integrations, API Reference, Guides, Release Notes | 3 steps: Installing the SDK -> Adding Integrations -> Displaying the Connect Portal | Only for on-prem ("Infrastructure Architecture") | "Hosted Demo Environment", "AI Agent Playground", "Paragon User Token Generator" | "Quickstart Sample App" | OpenAPI specs + per-endpoint pages | By product (Sync / ActionKit / Workflows), not by role | `.md` per page, `llms.txt`, "Install the Paragon Skill" |
| **Merge** | Unified API, Agent Handler, Gateway, Merge for Workforce (product tabs) | "Make your first Merge API call in under 10 minutes": create a test Linked Account in 4 dashboard steps, then call the API | Yes: "Architecture Reference" (Merge Link, Unified API, webhooks, your backend) | "Sandboxes", test Linked Accounts, Postman collections | GitHub org + SDKs in 6 languages | Per-category API reference + Postman | By product | `.md` per page, `llms.txt`, docs MCP server |
| **Nango** | Getting started, Guides (Agent sessions, Auth, Tools, Triggers, Syncs, Platform), Reference (Frontend, Backend HTTP API, SDKs), API catalog | 5 numbered steps, each with a collapsible "For agents" block | none | Dashboard "Playground" tab | Example functions; API catalog | OpenAPI-driven HTTP API + SDKs in 7 languages | Human vs coding-agent (per step) | `llms.txt`, "Docs MCP server", "Management MCP" |
| **Prismatic** | Evaluate, Getting Started Guides, Core Concepts, Integration Use-Cases, Developer Resources, Connectors, Platform | Get-started track with 4 product paths (Build Integrations, Embed a Marketplace, Embed a Workflow Builder, Connect AI Agents) and tutorials per path | One "responsibilities" image only | "API Explorer" (GraphQL) | https://github.com/prismatic-io/examples | GraphQL API + interactive explorer | Yes: "Where to start, by task" list in `llms.txt` and by product path | `.md` per page, `llms.txt` with a Terminology block |
| **Ampersand** | Getting started, Actions, UI and libraries, Destinations, Notifications, Reference, CLI, API, Provider guides, Customer guides, Troubleshooting | 7 steps around a fictional app ("MailMonkey" + Salesforce): org, provider app, destination, `amp.yaml`, deploy, embed | Yes, on the overview (your app, managed runtime, shared `amp.yaml`, per-customer field maps) | Starter project | Starter project + sample `amp.yaml` on GitHub | OpenAPI (platform, read, write, search) | "Customer guides" written for the SaaS's own customers | `llms.txt`; "Use with your coding agent" |
| **Composio** | Choose your path (Platform vs For You), Build an application, Provider guides, Session SDK reference, API Reference v3.1 / v3.0 | Framework tabs (OpenAI Agents, Claude Agent SDK, Vercel AI SDK), 3 steps each, then "What just happened?" | none | none (CLI login) | "Examples" section | REST v3.1, versioned, with legacy v3.0 kept | "Platform" (builders) vs "For You" (end users) | `llms.txt`; "Notes for AI Code Generators" with an old-to-new term table |
| **Pipedream Connect** | Overview, Managed Auth, Pre Built Tools, MCP Servers, Webhooks, API Reference | 5 CLI steps (`pd init connect`) that scaffold a runnable Next.js demo | none in the text | "SDK Playground", "MCP Chat Demo" | Demo apps via the CLI | Per-endpoint reference grouped by resource (Tokens, Accounts, Actions, Triggers...) | By capability | `llms.txt` |
| **Arcade** | Get Started, Build, Operate, Resources, References | 6 steps, with Python / TypeScript / Java tabs and a full example file | "Platform architecture" page under Operate | none in docs | "Examples" and "Sample applications" on home | API reference + CLI cheat sheet | Yes: home "Choose your path": Build agents and tools vs Deploy and operate | Notes that the docs are formatted for AI agents; `llms.txt` |
| **Workato Embedded** | Management layer (Admin console, Teams...) and Deployment layer (Iframes, Embedded platform APIs, implementation guides) | No public quickstart; access needs an Embedded account | none public | none | none | Per-resource REST pages | Partner admin vs developer, implicitly | none found |

Observations:
- Every agent-era vendor (Nango, Composio, Merge, Paragon, Prismatic, Arcade, Ampersand) now ships `llms.txt`, per-page `.md`, and either a docs MCP server or a "for coding agents" path. fastn has `llms.txt` but no visible "for coding agents" path on the quickstart.
- Merge and Ampersand show the clearest architecture picture. Paragon, Nango, Composio and Pipedream skip diagrams on the quickstart. fastn's home diagram is an asset worth keeping.
- The best quickstarts are code-first and finish with something running in under 10 minutes (Merge, Pipedream, Composio). fastn's is UI-first and has 8 steps, which suits the dashboard persona but leaves developers without a fast path. The "twenty minutes" vs "five-minute trial" mismatch should be fixed.

---

## 3. Where fastn diverges, and what to do per term

| fastn term | Industry norm | Divergence | Recommendation |
|---|---|---|---|
| **customer** (the SaaS's customer org) | Prismatic and Workato say "Customer". Ampersand says "group", Nango says "tenant", and Merge/Pipedream/Composio/Arcade only have a user-level "end user" / "user" | fastn matches the two most similar embedded-iPaaS products, so the term is fine. The problem is internal: the repo also says "tenant" (about 54 uses), "end user" (about 36) and "end org" (API) | **Keep**. Add an "also called tenant / end org in the API" note in the Glossary, and replace "tenant" with "customer" in prose except where it names an API field |
| **user** (person at the customer) | "end user" (Merge, Nango, Pipedream), "Connected User" (Paragon), "Customer User" (Prismatic), "consumer" (Ampersand) | "user" alone is ambiguous: it can also mean a fastn dashboard user | **Keep but qualify**. Use "customer user" on first mention per page (as Prismatic does), with "also called end user" in the Glossary |
| **connector** | Prismatic, Workato and Merge Agent Handler say "connector". Paragon, Merge Unified and Nango say "integration"; Composio says "toolkit"; Pipedream says "app" | fastn is in the iPaaS majority | **Keep**. Add "also called integration, app or toolkit elsewhere" to the Glossary |
| **connection** | "Connection" (Nango, Prismatic, Ampersand, Workato); "connected account" (Composio, Pipedream); "Linked Account" (Merge) | fastn uses the most common term. Composio's rename from "connection" to "connected account" shows that agent-focused readers find "account" clearer | **Keep**, and add "also called connected account or linked account". On widget and customer-facing pages, say "connected account" in prose, since customers think in accounts |
| **workflow** | Paragon "Workflow", Prismatic "Flow", Workato "Recipe"; tool-centric vendors say "tool" / "action" | Fine | **Keep**. Where a workflow is exposed through fastn Connect, say once that "each workflow appears to the agent as a tool" |
| **widget** | "Connect Portal" (Paragon), "Merge Link", "Connect UI" (Nango), "Marketplace" (Prismatic), "Connect Link" (Composio, Pipedream), "Prebuilt UI components" (Ampersand) | No competitor says "widget", and to developers it sounds like a small or optional piece. fastn's widget is also more than an auth popup (it covers configuration, an AI assistant and sync history), closer to Prismatic's Marketplace | **Keep but add a note**. A product rename is not a docs decision. Define it once as "the embedded integrations portal (similar to a Connect Portal or Marketplace)" and use "widget" consistently after that |
| **setup / config** | "User Settings" (Paragon), "Config Wizard" + "config variables" (Prismatic), "Config" (Ampersand) | "setup" vs "config" vs "Configs" (Manage page) is used loosely | **Rename in docs to one term**: "configuration" for the per-customer values and "setup" only for the customer-facing flow that collects them. Add an "also called user settings or config wizard" note |
| **fastn dashboard** | "<Vendor> dashboard" everywhere | Matches | **Keep** |
| **API key** | "API key" (Merge, Ampersand, Composio, Arcade, Nango) | Matches | **Keep** |
| **embed token** | "link token" (Merge), "Connect token" (Pipedream), "session token" (Nango), "User Token" JWT (Paragon, Prismatic, Ampersand) | Descriptive and fine. The difference is that fastn mints it with an API call, while Paragon and Prismatic have you sign a JWT. Spell that out | **Keep**. Add a one-line comparison: "like Merge's link token or Pipedream's Connect token" |
| **unified API** | Merge "Unified API" + "Common Models"; Paragon "Managed Sync"; Nango and Ampersand "build your own unified API" | Matches, but fastn has no name for the shared schema | **Keep**, and name the schema objects (for example "unified models") so readers coming from Merge recognize them |
| **trigger** | Prismatic and Paragon use the same three kinds (webhook, schedule, app event) | Exact match with Prismatic | **Keep** |
| **Logs** | "Monitoring" / "Event Logs" (Paragon), "Executions" (Prismatic), "Operations" (Ampersand), "Observability" + "Audit trail" (Nango) | The brief says "Logs", but the nav calls the section "Operate" with Activity, Events, Traces and Executions and has no page called Logs | **Rename in docs**: use "Operate" as the section and "monitoring" in prose, and drop "Logs" as a product noun unless the UI has it |
| **fastn Connect / fastn MCP server** | "Agent Handler" (Merge), "MCP Gateways" (Arcade), "Agent sessions" (Nango), "Sessions" (Composio), "Paragon MCP Server" | Two separate MCP things (the builder MCP and the gateway) are easy to confuse. Ampersand and Nango name theirs "builder MCP" / "Management MCP" vs runtime access, and the repo Glossary lists "MCP Gateway" with a Control Plane and a Data Plane | **Keep both names**, but always pair each with a role: "fastn Connect (MCP gateway for your AI agents)" vs "fastn MCP server (for building in your AI tool)". Add a "which MCP do I need?" box |
| **fastn agent** | "Building with Agents" (Paragon), "Coding agent setup" (Nango), "Start with AI" (Ampersand), "AI copilot" (Prismatic, for customers) | Internally inconsistent: the repo uses "Build with AI", "Agent", "fastn agent", "AI builder", "the agents" and "maintainer agent" | **Rename in docs to one name** that matches the UI label (the sidebar says "Build with AI"). Keep "maintainer agent" as a separate, explicitly different thing |

Overall: fastn's core nouns (customer, connector, connection, workflow, trigger) match the embedded-iPaaS norm set by Prismatic and Workato, so no core rename is needed. The real problem is internal drift (tenant, end user, end org; agent, Build with AI, AI builder; Logs vs Operate). Fixing that matters more than matching any one competitor.

---

## 4. Things competitors do that fastn should copy

1. **A canonical terminology block that defines "you" vs "your customer"**. Prismatic opens with "Organization: The B2B SaaS company using Prismatic" and "Customer: The organization's customer (not Prismatic's)". This removes the three-party ambiguity in one line. https://prismatic.io/docs/llms.txt
2. **An "old name -> new name" table**. Composio's glossary records each rename (connection -> connected account, action -> tool, workbench -> sandbox), and Nango has a migration page for dropping "end user". fastn has a Classic section and V1 terms such as UCL and flows, and readers need this map. https://docs.composio.dev/docs/glossary , https://nango.dev/docs/guides/platform/migrations/migrate-from-end-user.md
3. **An architecture reference page that shows the token flow end to end**. Merge's page shows how Merge Link, the account token, webhooks and your backend fit together, plus the production switch. fastn should do the same for API key -> embed token -> widget -> connection -> workflow run -> fastn Connect. https://docs.merge.dev/merge-unified/architecture-reference.md
4. **A hosted demo you can use without writing code**. Paragon's Hosted Demo Environment takes a Project ID, signing key and user ID, then renders the real Connect Portal. fastn could host a demo page that takes an embed token and renders the widget. https://docs.useparagon.com/demo.md
5. **A collapsible "For agents" block on each quickstart step**. Nango's quickstart gives every step a version for coding agents, and Composio adds a "Help me add Composio to this project" prompt. This fits fastn's "Connect your AI tool" story. https://nango.dev/docs/getting-started/quickstart
6. **A runnable sample scaffolded from the CLI**. Pipedream's `pd init connect` produces a Next.js app with managed auth working at localhost:3000. A `fastn-examples` repo with an embed-the-widget Next.js starter would cover the missing developer fast path. https://pipedream.com/docs/connect/quickstart
7. **Show the token lifecycle numbers in one place**. Merge says link tokens default to 30 minutes, and Pipedream says Connect tokens have "a 4-hour expiry, and can only be used once". fastn's 8-hour `emb_` token should get the same treatment on the embed token page: lifetime, single or multi use, scope. https://docs.merge.dev/merge-unified/merge-link.md , https://pipedream.com/docs/connect/managed-auth/tokens
8. **A "Where to start, by task" index**. Prismatic maps tasks ("Per-customer configuration", "Embedding a marketplace", "Exposing integrations to an AI agent") straight to pages. fastn's three audience cards could grow into this. https://prismatic.io/docs/llms.txt
9. **Docs written for the SaaS's own customers**. Ampersand's "Customer guides" are per-provider setup pages a SaaS can link from its own UI. fastn's End User tutorials could expand into per-connector "how your customer connects X" pages. https://docs.ampersand.ai/llms.txt
10. **A "Choose your path" split on home between building and operating**. Arcade's home separates "Build agents & tools" from "Deploy & operate Arcade" and has a matching Operate quickstart. fastn already has Build / Embed / Operate rails, and an Operate quickstart (first alert, first trace) would complete it. https://docs.arcade.dev/en/home

---

## Summary of key recommendations

1. Keep fastn's core nouns: customer, connector, connection, workflow, trigger, API key, embed token, unified API. They match the Prismatic and Workato embedded-iPaaS norm.
2. Fix internal drift first: the repo uses "tenant" (about 54 times), "end user" (about 36) and "end org" for "customer". Standardize on "customer" in prose.
3. Use "customer user" for the person at the customer on first mention, so it is not confused with fastn dashboard users.
4. Pick one name for the AI builder (the UI says "Build with AI") and keep "maintainer agent" visibly separate.
5. Always pair fastn Connect and the fastn MCP server with their role, and add a "which MCP do I need?" box.
6. Keep "widget", but define it once as the embedded integrations portal (like Paragon's Connect Portal or Prismatic's Marketplace).
7. On customer-facing pages, say "connected account" in prose and keep "connection" as the object name.
8. Use one term for per-customer settings ("configuration") and keep "setup" for the flow that collects them.
9. Use "Operate" / "monitoring" rather than "Logs", since the nav has no Logs page.
10. Add an "also called" column to the Glossary covering the competitor synonyms in section 1, plus an old-to-new names table for Classic / UCL terms.
11. Publish a Merge-style architecture reference with the full key -> embed token -> widget -> connection -> run -> MCP flow.
12. Give developers a code-first fast path: a runnable starter repo (Pipedream style) and an "under 10 minutes" embed quickstart.
13. Add "For agents" blocks to quickstart steps (Nango style) and a copyable "set up fastn in this project" prompt.
14. Fix the "five-minute trial" (home) vs "about twenty minutes" (quickstart) mismatch.
15. Consider a hosted widget demo page and a "Where to start, by task" index, modeled on Paragon and Prismatic.
