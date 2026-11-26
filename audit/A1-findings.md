# A1 audit findings (Get started, How-to guides, Embed)

Verified against fastn-platform origin/main 2287b9e20 (local checkout is behind; every check used `git grep ... origin/main` / `git show origin/main:`), plus the coordinator's live check of app.fastn.dev (24 Nov). Docs repo: /Users/khalid/fastn-code/fastn-docs-katie. Nothing committed.

### README.md
- Status: OK
- Terminology: none needed (fastn Connect = MCP gateway, fastn agent, maintainer agent all correct).
- Product accuracy: 25 s / 36 h tiers (WorkflowsPage.tsx tier copy), alert channels email/Slack/Teams/webhook (components/alerts/AlertsManager.tsx, AlertAppConnect.tsx), Health → Pending updates (HealthPage.tsx tabs), Connect your AI tool (App.tsx top bar) all match.
- Screenshot: none (the SVG overview already carries the page).
- Follow-up: none.

### getting-started/quickstart.md
- Status: OK
- Terminology: OK.
- Product accuracy: Home prompt "What should your customers be able to do?" (CommandCenter.tsx), Create integration → Build with fastn agent / Build in your AI tool (CreateIntegrationMenu.tsx), Approval mode chip Auto/Manual (OrchestratorPage.tsx, embed i18n en.ts), Test tab "Use contract", "Fully Mock", "Run Fully Mock" (WorkflowsPage.tsx 5243-5303), WORKFLOW_NOT_PUBLISHED, Health → Alerts "Turn on failure alerts" (AlertsManager.tsx) all match.
- Screenshot: /integrations?tab=workflows, a workflow open on the Test tab with mode set to Fully Mock after a run; crop to the right-hand Test panel (input, mode selector, output). quickstart-fully-mock-run.webp
- Follow-up: none.

### tutorials/developer/authentication-and-api-keys.md
- Status: OK
- Terminology: OK.
- Product accuracy: 8 h token / 7 day session cap (services/api/src/routes/embed.ts TOKEN_TTL_MS, SESSION_MAX_MS), Search keys, All/Live/Test pills, Mode column, Create key, "Create an API key", Test mode card copy (pages/settings/ApiKeysTab.tsx, lib/api-key-modes.ts), 403 test-key message (services/api/src/server.ts), header table (services/event/src/lib/fastn-key.ts, routes/webhook-trigger.ts), customer MCP URL 10 min (routes/embed.ts MCP_CONNECT_CODE_TTL_MS) all match.
- Screenshot: /api-keys, Create key dialog open with Test mode selected; crop to the Mode cards. auth-api-key-mode-cards.webp
- Follow-up: none.

### getting-started/concepts.md
- Status: Fixed
- Terminology: "Build with AI" -> "the fastn agent" (lifecycle step 1, and the "Build with AI" section renamed "The fastn agent", now stating paid plans and AI credits, with the AI-tool alternative). "The MCP gateway" section -> "The fastn MCP server and fastn Connect", distinguishing mcp.fastn.dev/fastn-workspace (build) from fastn Connect (agents use customers' apps); link text "MCP gateway" -> "fastn MCP server".
- Product accuracy: tier ranges/defaults match the UI (WorkflowsPage.tsx tierLimits and tierDefaults: 25 s, 2 min, 15 min defaults; Long max 36 h). "Requires review", Per customer / Platform-wide badges (ConnectorManifestPanel.tsx), "Account level" and "Pass this to the API to act as this customer." (ConnectionDetailPage.tsx) match.
- Screenshot: none.
- Follow-up: backend allows Long runs up to 48 h (packages/http/src/contracts/workflow.ts MAX_TIMEOUT_MS) while the UI and docs say 36 h; product should pick one.

### getting-started/platform-tour.md
- Status: Fixed
- Terminology: "Build with AI opens at /agent" -> "the fastn agent opens at /agent"; Integrations "See [MCP gateway]" -> fastn MCP server, reworded as connecting your AI tool to the fastn MCP server. Alerts row "What should page us" -> neutral wording.
- Product accuracy: Operate rows reordered to the sidebar order Health, Customers, Connections, Logs (lib/rbac.ts). Logs tabs: added Monitoring (ActivityPage.tsx, owner/admin, entitlement "activity.monitoring", locked when off); removed Traces from the tab list and the sidebar row because ActivityPage.tsx filters it off the strip (confirmed in the live check), with a note that /activity/traces exists. Home on Launch: added "Ask the fastn agent a question" (CommandCenter.tsx), and the setup banner "Your setup isn't finished." with Continue setup (components/FirstIntegration.tsx). Help menu, Report a bug, search action, Create connector menu, Customers statuses, My organization, widget footer all verified.
- Screenshot: / (Home) on a Launch org with setup unfinished; crop to the banner, heading and paid-plan note. platform-tour-home-launch.webp. And /health on the Needs attention tab; crop to tab strip plus first rows. platform-tour-health.webp
- Follow-up: the live check lists the top bar as search, help, theme, Connect your AI tool, credits; the code renders BugReportButton too. Confirm whether Report a bug is gated before removing it from the table.

### getting-started/onboarding/README.md
- Status: Fixed
- Terminology: "ask fastn's agent questions (the prompt on Home, or /agent)" -> "ask the fastn agent questions at /agent ... on Launch, Home links to it as Ask the fastn agent a question".
- Product accuracy: credits 15/10/5 setup, 20 build (packages/core/src/index.ts ONBOARDING_STEP_CREDITS + SETUP_GRANT_STEP), setup/go-live items and order (SETUP_STEPS, GO_LIVE_ITEMS), "Here's what we found", Looks right/Edit (onboarding/ProductScreens.tsx), I'll add it / My developer / My AI tool (WidgetStepScreen.tsx) match.
- Screenshot: /onboarding on the plan screen (setup steps and going-live list); crop to the list. onboarding-plan.webp
- Follow-up: the Launch credit dates (1 Dec / 25 Nov 2026) are not in the dashboard code; verify with billing (another agent owns manage/billing.md).

### getting-started/onboarding/choose-integrations.md
- Status: Fixed
- Terminology: "fastn's agent (Build with AI)" -> "the fastn agent, or your AI tool"; table rows "Build with AI" -> "fastn agent", "Your AI tools" -> "Your AI tool"; test-case and code-editing lines no longer say Build with AI; related link text -> "Build with the fastn agent".
- Product accuracy: the "Scope: shared or per user" section was wrong. In WidgetsPage.tsx (create mode, ~line 967) Scope only sets sync_direction (org = bidirectional, user = inbound) and agent_context; it does not separate connections (embed/widget-builder/README.md already said so). Rewrote the section to match and dropped the Scope column from the use-case table. Badges You offer it / You don't offer it / Needs work / In fastn / Not in fastn yet / Do it later verified (onboarding/IntegrationScreens.tsx, integration-build.ts, BuildScreens.tsx).
- Screenshot: /onboarding on step 2 (Pick your integrations) with a few apps picked; crop to two or three rows showing both badges. onboarding-pick-integrations.webp
- Follow-up: product owner should confirm the intended meaning of Scope; if per-user connections are planned, the UI caption "Per-customer connections" for User level is also misleading.

### getting-started/onboarding/embed-the-widget.md
- Status: Fixed
- Terminology: "the AI your customers use" -> "the widget assistant your customers use".
- Product accuracy: "**Make it match**" is not a UI label; replaced with the real controls "Customize it in <your AI tool>", "Or change it in the widget builder" and "Who adds it to <product>?" (WidgetStepScreen.tsx). Removed the "User level Scope" row and the Organization-level Scope claim (see choose-integrations). Embed backend preset, Every customer, Verify caller identity (HMAC), preset list (lib/api-key-presets.ts), Preview the widget / Open the widget builder / Send to your developer / Widget found (onboarding/FinishScreens.tsx), Copy URL, Allowed Origins, webhook host (services/event/src/lib/webhook-url.ts) verified.
- Screenshot: /onboarding/live/widget (Add the widget to <product>); crop to the button row and step 1. onboarding-add-widget.webp
- Follow-up: the register-customer example uses `"tier": "pro"` (a customer tier, not a fastn plan); consider another tier name to avoid confusion with retired plan names.

### getting-started/onboarding/customers-connect-and-customize.md
- Status: Fixed
- Terminology: "AI assistant" -> "widget assistant" (table and bullets); related link text "Managing customers" -> "Manage customers".
- Product accuracy: Ask the assistant (embed i18n hub.askAssistant), "No configuration found for this widget." (config.notFoundForWidget), Customize customer limits (AccountBillingView.tsx), Try it as your first customer (FinishScreens.tsx), Add another connection, Pending admin activation verified.
- Screenshot: /onboarding on "Try it as your first customer" with at least one event listed; crop to the event list. onboarding-first-customer.webp
- Follow-up: none.

### getting-started/onboarding/connect-your-product.md
- Status: Fixed
- Terminology: "SaaS connector" -> "product connector" (prose, table row, step 3; matches the UI's "Add another product connector"); "Build with AI" -> "fastn agent"; "Your AI tools" -> "Your AI tool"; link texts "SaaS connectors" -> "Connect your product", "Building from your AI agent" -> "Build from your AI tool" (SUMMARY titles), "Build with AI" -> "Build with the fastn agent".
- Product accuracy: Live tested, Publish to live (ConnectorsPage.tsx), Add another product connector / Add connector / Connect your product panel (settings/SaasConnectorsTab.tsx), Start small and "Upgrade to use the fastn agent" (onboarding/BuildScreens.tsx) verified.
- Screenshot: /your-product with one product connector registered; crop to the card list and the Add another product connector button. connect-your-product.webp
- Follow-up: none.

### tutorials/saas-admin/setting-up-your-organization.md
- Status: Fixed
- Terminology: H1 "Setting Up Your Organization" -> "Set up your organization"; Developer row "uses Build with AI" -> "can use the fastn agent (paid plans)".
- Product accuracy: General tab cards and fields (settings/GeneralTab.tsx), Invite someone, Create custom role (admin/PermissionsPage.tsx), Customers subtitle (admin/TenantsPage.tsx), See plans / Request plan change (AccountBillingView.tsx), Launch 500 events/day, 1,000 API calls/day and Scale 10 customer connections (packages/db/src/quota.ts) verified.
- Screenshot: /settings/billing on Launch; crop to the plan header and Limits card. org-billing-limits.webp
- Follow-up: per-role permission counts (44/44/36/21/6/35) were not re-counted against the Roles screen; spot-check on /settings/roles.

### how-to/README.md
- Status: OK
- Terminology: OK. Product accuracy: links only.
- Screenshot: none. Follow-up: none.

### how-to/crm-records.md
- Status: Fixed
- Terminology: example note "Signed up for the Pro plan" -> "Signed up for the annual plan" (avoids the retired plan name).
- Product accuracy: Copy curl on Unified APIs (UnifiedApiPage.tsx) verified. SDK methods `fastn.customer()`, `crm.contacts.find/create/list`, `crm.notes.add` exist in the node SDK (fastn-sdk-audit/node/src/index.ts, domain.ts).
- Screenshot: /integrations?tab=unified with the CRM category open; crop to a row with Copy curl. unified-copy-curl.webp
- Follow-up: the published package name `@fastn-ai/sdk` is not in the platform repo (packages/sdk is `@fastn/sdk`, a different connector SDK); confirm against the fastn-sdk repo's published name.

### how-to/run-for-a-customer.md
- Status: OK
- Product accuracy: workflow API tab (WorkflowsPage.tsx), X-Execution-Id (packages/http), IDENTITY_ORG_NOT_FOUND, IDENTITY_HEADERS_REQUIRED, test-key 403 verified.
- Screenshot: /integrations?tab=workflows, a workflow on the API tab; crop to the workflow id and ready curl. workflow-api-tab.webp
- Follow-up: none.

### how-to/events-from-your-product.md
- Status: Fixed
- Terminology: OK.
- Product accuracy: "dead-letter queue, shown on Health" was wrong; DLQ is counted on the trigger row as "Dead-lettered" (TriggersPage.tsx) and replayed in Logs → Monitoring (entitlement description in lib/entitlements/modules.ts). Add trigger, Advanced options, Create trigger, Max attempts, Backoff strategy, Monitor only verified.
- Screenshot: /integrations?tab=triggers with the Add trigger → Webhook form open and Advanced options expanded; crop to the form. webhook-trigger-form.webp
- Follow-up: none.

### embed/README.md
- Status: Fixed
- Terminology: link text "Embedding in production" -> "Go-live checklist" (SUMMARY title).
- Product accuracy: preview widths, View as admin, Preview language, Saved configs / Custom pages, Use for customers, Review draft, Reset widget to defaults?, Unsaved changes / Live badge (WidgetsPage.tsx, lib/widget-draft.ts) verified.
- Screenshot: /widgets on the Layout tab with the preview at Tablet; full page minus browser chrome. widget-builder-overview.webp
- Follow-up: none.

### embed/widget-builder/README.md
- Status: OK
- Product accuracy: Add Integrations, Apps/Unified, Select connectors, Scope captions (WidgetsPage.tsx 2000-2060), Edit Integration verified. Its Scope description is the correct one.
- Screenshot: /widgets with the Add Integrations dialog open on Apps; crop to the dialog. widget-add-integrations.webp
- Follow-up: none.

### tutorials/saas-admin/building-your-widget.md
- Status: Fixed
- Terminology: H1 "Building Your Widget" -> "Build your widget"; AI assistant section described as "The widget assistant"; link text "Embedding fastn" -> "Embedding quickstart".
- Product accuracy: Tokens has no "Compact mode" (removed; BuilderControls.tsx General group has Allowed Origins and Show 'Powered by fastn', whose hiding is Enterprise white-label). Features has no "Coming soon" group and no "Role based access": rewrote to Available now (Catalog connectors, Workflow Diagram, Generate MCP URL, App page layout, Installations layout) and Customer access (Widget filter, Access check; instant-tier workflows). Embed sub-tabs Iframe/SDK/A2A, SDK variants, User dropdown, Embed Code, Shareable links (EmbedMethodsPanel.tsx) verified.
- Screenshot: /widgets on the Features tab; crop to the left panel. widget-features-tab.webp
- Follow-up: none.

### embed/widget-builder/edit-integration.md
- Status: OK
- Product accuracy: every label checked in WidgetsPage.tsx (1452-1860), ConnectorSettingsInline.tsx, LifecycleHooksPanel.tsx, WidgetLocalizationEditor.tsx. Minor casing only (UI "Auth provider", "Override only what differs..."; docs use the section-style caps).
- Screenshot: one existing image (widget-callbacks.jpg) is in place; optionally reshoot as /widgets, pencil on an integration, Edit Integration scrolled to Callbacks. widget-edit-integration-callbacks.webp
- Follow-up: none.

### embed/widget-builder/layout.md
- Status: Fixed
- Terminology: AI assistant row now "The widget assistant: an Ask the assistant launcher...".
- Product accuracy: defaults Integrations / Connect your favorite tools, three sections (components/widget-builder/config.ts, packages/embed theme.ts) verified.
- Screenshot: none (building-your-widget covers it).
- Follow-up: none.

### embed/widget-builder/style.md
- Status: Fixed
- Terminology: OK.
- Product accuracy: removed Compact mode row; noted that hiding Powered by fastn is Enterprise white-label. Fonts, size 11-18, weights, spacing, Square/Rounded/Soft/Pill, radius 0-20, surface tokens (BuilderControls.tsx, config.ts) verified.
- Screenshot: /widgets on Style → Tokens; crop to Allowed Origins and Powered by fastn. widget-style-tokens.webp
- Follow-up: none.

### embed/widget-builder/features.md
- Status: Fixed
- Product accuracy: replaced the "Coming soon" table (Widget filter "filter by category", Role based access) with the real controls: App page layout, Installations layout, and the Customer access group (Widget filter, Access check workflows) from BuilderControls.tsx FeaturesControls.
- Screenshot: same as building-your-widget (widget-features-tab.webp); do not shoot twice.
- Follow-up: none.

### embed/embedding/README.md
- Status: Fixed
- Terminology: H1 "Embedding the widget" -> "Embed in your product" (SUMMARY title).
- Product accuracy: No customers yet card (UI uses a long dash; docs keep a hyphen per style rule), Create a customer, Pick a customer above first., New links and expiry options, Never used (EmbedMethodsPanel.tsx) verified.
- Screenshot: /widgets on the Embed tab, Iframe sub-tab, a test customer picked; crop to the Shareable links card. widget-embed-share-links.webp
- Follow-up: none.

### tutorials/developer/how-embedding-works.md
- Status: Fixed
- Terminology: H1 -> "How embedding works"; links "Tenancy" -> "Customers and tenancy", "Quickstart" -> "Embedding quickstart", "Generating Embed Tokens" -> "Generate embed tokens"; first line now mentions the SDK.
- Product accuracy: OK. Screenshot: none. Follow-up: none.

### tutorials/developer/embedding-quickstart.md
- Status: Fixed
- Terminology: H1 -> "Embedding quickstart"; link texts "Generating Embed Tokens" -> "Generate embed tokens", "Managing customers" -> "Manage customers".
- Product accuracy: Create customer and External ID (admin/TenantsPage.tsx), token call and response shape verified.
- Screenshot: /customers with the Create customer panel open; crop to the panel. customers-create.webp
- Follow-up: none.

### embed/embedding/iframe.md
- Status: Fixed
- Product accuracy: placeholder host `YOUR_FASTN_HOST` -> `api.fastn.dev`, matching every other page.
- Screenshot: none. Follow-up: none.

### embed/embedding/sdk.md
- Status: OK
- Product accuracy: `@fastn-ai/embed` with ./react, ./headless, ./headless/react exports (packages/embed/package.json), FastnConnectCard, createFastnEmbed, script bundle path (lib/embed-snippets.ts) verified.
- Screenshot: /widgets Embed tab → SDK sub-tab, React component variant; crop to the snippet. widget-embed-sdk.webp
- Follow-up: script tag still uses `YOUR_FASTN_HOST`; the dashboard renders `${apiBase}/v1/embed/assets/...` and packages/embed/README.md shows `https://api.fastn.dev/v1/...` (no /api). Confirm the public URL before filling it in.

### embed/embedding/token-api.md
- Status: Fixed
- Terminology: H1 "Tokens" -> "Token API" (SUMMARY title).
- Product accuracy: all error codes and fields exist in services/api/src (embed.ts, identity-hmac); 8 h, 7 days, 24 h refresh grace verified.
- Screenshot: none. Follow-up: none.

### tutorials/developer/generating-embed-tokens.md
- Status: Fixed
- Terminology: H1 -> "Generate embed tokens"; link texts -> "Find your org identifier", "Customers and tenancy".
- Product accuracy: error table codes verified in services/api/src (EMBED_TOKEN_REUSED, EMBED_SESSION_EXPIRED, TENANT_SLUG_TAKEN, API_KEY_SCOPE_AMBIGUOUS, etc.).
- Screenshot: none. Follow-up: none.

### embed/embedding/integration-flow.md
- Status: Fixed
- Terminology: headings to sentence case ("Pre-requisites" -> "Prerequisites", "Creating an API key" -> "Create an API key", "API Reference" -> "API reference", "Create a Customer Organization" -> "Create a customer organization", "Generate Embed Token" -> "Generate embed token"; anchors unchanged); "No end user exists yet" -> "No user exists yet"; "[Tokens]" -> "[Token API]".
- Product accuracy: Create key dialog fields now use the UI labels Permissions, Customers it can reach, Allowed IP addresses, Rate limit, Expires, Verify caller identity (HMAC) (ApiKeysTab.tsx).
- Screenshot: none (api-key-identity-secret.webp already present).
- Follow-up: anchor `#pre-requisites` changed to `#prerequisites`; no inbound links found.

### tutorials/developer/understanding-tenancy.md
- Status: Fixed
- Terminology: H1 "Understanding Tenancy" -> "Customers and tenancy"; link texts -> "Find your org identifier", "Generate embed tokens".
- Product accuracy: OK. Screenshot: none. Follow-up: none.

### embed/embedding/customer-mcp-url.md
- Status: Fixed
- Terminology: "the Fastn Workspace tools" -> "the fastn MCP server's workspace tools".
- Product accuracy: 10 min TTL, error codes, MCP card on the Embed tab (EmbedMethodsPanel.tsx 871) verified.
- Screenshot: /widgets Embed tab with a customer picked; crop to the MCP card after Generate. widget-embed-mcp-card.webp
- Follow-up: none.

### embed/embedding/production-checklist.md
- Status: Fixed
- Terminology: H1 "Embedding in production" -> "Go-live checklist"; "Embed > Widget > Embed" -> arrows; "[Tokens]" -> "[Token API]".
- Product accuracy: live.gcp.fastn.ai retired (services/api/src/lib/request-domain.ts) verified.
- Screenshot: none. Follow-up: none.

### manage/api-keys.md
- Status: Fixed
- Terminology: link text "Embedding the widget" -> "Embed in your product".
- Product accuracy: columns Name/Key/Mode/Scope/Last used, Rotate, Identity verification, Revoke, Delete, Identity/Access/Limits sections, Only the ones I pick, Required for keys used in an embed session., Resource scope, expiry options, Rotate the secret, "API keys per customer" limit (QuotaEditor.tsx) verified. Example host `YOUR_FASTN_HOST` -> `api.fastn.dev`.
- Screenshot: existing create-api-key.jpg; reshoot as /api-keys with the keys table (one Live, one Test key); crop to table. api-keys-list.webp
- Follow-up: none.

### tutorials/developer/finding-your-org-identifier.md
- Status: Fixed
- Terminology: H1 -> "Find your org identifier"; links -> "Manage customers", "Generate embed tokens".
- Product accuracy: /customers/:customerId route (App.tsx) verified.
- Screenshot: /customers/<id> for the Docs-test test customer; crop to the header and address bar. customer-detail-id.webp
- Follow-up: none.

## Cross-page issues (not edited; outside A1)
- SUMMARY.md still titles build/agent/README.md "Build with AI"; it should be "Build with the fastn agent" (A1 link texts now use that).
- build/building-from-your-ai-agent.md H1 is "Building from your AI agent" while SUMMARY says "Build from your AI tool".
- Logs → Traces is off the tab strip (ActivityPage.tsx); any page that lists Traces as a Logs tab (operate/traces.md, operate/README.md, the brief) should say so.
- Workflow Long tier: UI 36 h vs backend 48 h.
