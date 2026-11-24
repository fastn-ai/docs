# A4 findings: Reference (HTTP API, REST, SDK, code samples, runtime, errors, FAQs, glossary, tutorials index)

Docs repo: /Users/khalid/fastn-code/fastn-docs-katie. Platform checked at origin/main 40cc783e6 (git show/grep, not the working tree). SDK checked at /Users/khalid/fastn-code/fastn-sdk-audit (node 0.5.1, python 0.5.1, latest commit 844d0b7). Nothing committed.

Note: other agents were editing the repo at the same time (e.g. build/agent/README.md is now titled "Build with fastn agent"), so the synonym counts at the end are a snapshot.

### reference/glossary.md
- Status: Fixed (rewritten as the canonical term list)
- Terminology: added a **Not (also seen as)** column; alphabetized. Build with AI -> **fastn agent** (paid plans only); "Agent" disambiguation row folded into fastn agent and Your AI tool; "fastn MCP gateway" -> **fastn Connect** (also seen as fastn MCP gateway); Onboarding "four steps: Connect your product, Choose integrations, Embed the widget, Customers connect and customize" -> setup steps Check your product / Pick your integrations / Set up the widget, going-live items, Get started card n of 7; Integration link text "Choose integrations" -> "Pick your integrations"; "AI Assistant" -> **Widget assistant** (the widget's AI assistant section, Layout → Sections); "AI tools" -> **Your AI tool**. New rows: fastn dashboard, Operator (with note that it differs from the Operator role), fastn Connect, Maintainer agent, Health, Logs, Plans, Your AI tool. Where-to-find paths now use the sidebar (Build → Integrations → tabs, Embed → Widget, Embed → MCP server, Operate → Health/Logs).
- Product accuracy: verified against apps/dashboard/src/lib/rbac.ts (sidebar), pages/ActivityPage.tsx (Logs tabs, Monitoring for owner/admin), pages/onboarding/ob3.tsx (STEP_TITLES, GO_LIVE_TITLES), components/FirstIntegration.tsx (Get started card), lib/integration-glossary.ts (the UI's own definitions: integration = connector, workflow, trigger, connection, widget), components/widget-builder/config.ts and WidgetsPage.tsx (section "AI assistant"), pages/WidgetsPage.tsx (Organization level / User level), pages/WorkflowsPage.tsx (tier limits 15 min / 36 hours), lib/mcp.ts (mcp.fastn.dev/fastn-workspace, mcp.fastn.dev/<org>), lib/credits.ts, packages/db/src/quota.ts, rbac.ts getRoleLabel. "SaaS connector" kept as a docs term but the UI tab is **API connector** on Connect your product (pages/YourProductPage.tsx) and the UI says "connection scopes" (settings/SaasConnectorsTab.tsx).
- Screenshot: none (a table page).
- Follow-up: decide whether docs should rename "SaaS connector" to "API connector" to match the tab; the glossary documents both.

### reference/api.md
- Status: OK
- Terminology: none needed.
- Product accuracy: verified error codes ENV_NOT_PERMITTED, IDENTITY_HEADERS_REQUIRED/CONFLICT, IDENTITY_ORG_NOT_FOUND/MISMATCH, API_KEY_SCOPE_MISMATCH/AMBIGUOUS, EMBED_TOKEN_REQUIRES_END_ORG_ID, ORG_RATE_LIMITED, EXECUTE_RATE_LIMITED, WORKFLOW_NOT_PUBLISHED, "Tenant not found" all exist in services/api; test-key 403 text in services/api/src/server.ts:2514; refresh cap SESSION_MAX_MS 7 days in services/api/src/routes/embed.ts:356; 8-hour token in apps/embed/README.md; Launch 100 / Scale 500 rpm in docs/architecture/08-data-event-flow-overview.md and lib/org-rate-limit.ts; "Copy curl" on UnifiedApiPage.tsx; workflow API tab in WorkflowsPage.tsx.
- Screenshot: workflow editor API tab, route /integrations?tab=workflows then open a published workflow → **API** tab, crop to the generated curl panel (api-workflow-api-tab.webp).
- Follow-up: none.

### reference/rest/README.md
- Status: Needs follow-up
- Terminology: OK.
- Product accuracy: says the reference is generated from release `v1.12.0`; latest platform tag is v1.15.1. I compared all 404 documented operations against the path items in services/api/src/openapi.ts plus services/api/src/openapi-bodies/*: 403 of 404 still exist. One mismatch: docs `PUT /v1/mock/connectors/{connectorSlug}/actions/{actionSlug}/stubs/{stubId}`, platform now `PATCH` (openapi-bodies/api2-misc.ts). About 340 platform operations are not documented; many are dashboard/admin-only, but these look key-callable and are also fastn MCP tools: widget deploy/promote/rollback/promotions/translations/preview-links/activation (`/v1/widgets/{id}/...`), sync jobs (`/v1/sync/jobs...`), connector update proposals and connector changes (maintainer agent), `/v1/environments/guardrails`, `/v1/environments/connections`, `/v1/hub-settings`, `/v1/mock/settings`, `/v1/connections/sandbox-allowance`, `/v1/connections/{id}/access-token`, `/v1/connectors/{id}/webhook-configs`, `/v1/release-reviews...`, `/v1/test-case-drafts...`, `/v1/users/me/invitations...`, `/v1/workflows/{id}/undeploy`, `/v1/workflows/{id}/promotions/{id}/complete`. Full list: /private/tmp/claude-501/-Users-khalid--claude-spares-spare-3s7Aon/8c796db7-ca12-4a43-a127-3fe40e42fab9/scratchpad/new-endpoints.txt
- Screenshot: none.
- Follow-up: regenerate the REST reference and openapi.json from the current spec (not done, per brief).

### reference/rest/workflows.md, installations.md, widgets.md, triggers.md, event-subscriptions.md, connectors.md, connections.md, unified.md, observability.md, environments.md, organization.md
- Status: Needs follow-up (generated; not edited)
- Terminology (comes from OpenAPI summaries/descriptions, fix at the source in services/api/src/openapi*.ts): connections.md:366 heading "List end customers' scoped connections for a registered SaaS connector" (end customers -> customers); widgets.md "end users" in several descriptions (end user -> user at a customer); connectors.md:1365 "hub/marketplace" spec import (marketplace -> integration catalog, if it refers to fastn's catalog); "external system(s)" in triggers.md/workflows.md/observability.md (-> app); `tenant` in field names and `/v1/widgets/insights/tenants` paths is literal API surface and stays.
- Product accuracy: see rest/README.md above (one PUT->PATCH mismatch, spec three releases old).
- Screenshot: none.
- Follow-up: regenerate.

### reference/widget-callbacks.md
- Status: OK
- Terminology: none.
- Product accuracy: blocking time limits match TIMEOUT_MS and BACKGROUND_TIMEOUT_MS (10 s) in services/api/src/lib/hook-dispatcher.ts.
- Screenshot: Embed → Widget → open an integration → **Edit integration** → Callbacks section, crop to the callback pickers (widget-callbacks-edit-integration.webp). Optional.
- Follow-up: none.

### reference/sdk/README.md
- Status: OK
- Product accuracy: package name @fastn-ai/sdk 0.5.1, Python fastn-ai 0.5.1, Node >= 20, default baseUrl https://api.fastn.dev, timeoutMs 60000, retries 2 all match fastn-sdk-audit/node/package.json and node/src/index.ts. All exports used in code (FastnClient, FastnApiError, FastnNetworkError, ToolsClient, ToolError, paginate, parseEvent, signEventBody) exist; every method name used across the SDK pages was found in node/src (loose name check, not a type check).
- Screenshot: none.
- Follow-up: the SDK's source lives in a separate repo (fastn-sdk-audit / fastn-sdk); packages/sdk in the platform is a different, internal `@fastn/sdk` 0.1.0. Worth stating nowhere in docs; just noting for verifiers.

### reference/sdk/end-to-end.md
- Status: Fixed
- Terminology/UI path: "**Widget › Embed › Setup links › Pages to send people back to**" -> "Embed → Widget → **Embed** tab → **Setup links** → **Pages to send people back to** (the panel appears once you pick a customer)".
- Product accuracy: SetupLinksPanel is rendered inside EmbedMethodsPanel only when a customer is selected (components/EmbedMethodsPanel.tsx:617, WidgetsPage.tsx settingsTab "embed"); 24-hour delivery retry window in services/event/src/pipeline/outbound-delivery.ts.
- Screenshot: Embed → Widget (/widgets) → Embed tab with a customer picked, crop to the Setup links panel showing "Pages to send people back to" (widget-embed-setup-links.webp).
- Follow-up: none.

### reference/sdk/customers.md, connecting-apps.md, unified-records.md, calendar-and-crm.md, app-actions.md, events.md, errors-and-options.md, any-operation.md
- Status: OK
- Terminology: `tenantRef` is a literal event field and stays; "HubSpot portal id" is the provider's own term and stays.
- Product accuracy: method names checked against fastn-sdk-audit/node/src (customer.ts, events.ts, catalog.ts, generated/).
- Screenshot: none.
- Follow-up: none.

### reference/sdk/workspace-tools.md
- Status: Fixed
- Terminology: link text "MCP gateway" -> names the endpoint as fastn Connect, the MCP gateway at `mcp.fastn.dev/<workspace>`, linking "fastn MCP server" (ToolsClient's url is that endpoint, node/src/tools.ts:17).
- Product accuracy: removed an internal ticket reference ("platform ticket KAT-8586") from public copy; replaced with "Passing the app's own message through is planned."
- Screenshot: none.
- Follow-up: none.

### reference/code-samples.md
- Status: OK
- Terminology: the "Embed the widget" heading is a task group, not the onboarding step name, so it stays.
- Product accuracy: every linked page exists; examples/ folder exists in this repo (fastn-ai/docs).
- Screenshot: none.

### reference/workflow-runtime.md
- Status: Fixed
- Terminology: connector scope "*per customer* or workspace" -> "**Per customer** or **Platform-wide**" (labels in components/ConnectorManifestEditorPopup.tsx:197-198, ConnectorManifestPanel.tsx:207).
- Product accuracy: fastn.state scopes ORG (default) / INVOCATION in services/workflow/src/sandbox/ctx/state.ts; fastn.diff.compare in ctx/diff.ts; ctx.isRetry/attempt in batch-attempt.ts; editor tabs Test, Connectors, Contract, Diagram, Test cases, Executions, Sync reports, API (WorkflowsPage.tsx:5150-5180).
- Screenshot: workflow editor **Connectors** tab showing the Per customer / Platform-wide badges, route /integrations?tab=workflows → open a workflow → Connectors tab, crop to the tab panel (workflow-connectors-tab.webp).
- Follow-up: none.

### reference/errors.md
- Status: Fixed
- Terminology/style: removed informal "Being straight about the boundary:"; the opening hint said fastn publishes no catalog of error codes while the page lists one, reworded to "Run failures surface as a category plus a message...; API errors carry the codes listed under Error codes"; added the missing blank line and rule before "## Trigger failure states" (it was glued to the previous paragraph).
- Product accuracy: all listed codes found in services/packages (CONN-*, WF-*, AGT-*, API-UNIFIED-*, EVT-*, DB_POOL_EXHAUSTED, legacy names, HTTP_<status>); UI strings AI Diagnosis, Error Details, Was this diagnosis helpful, Dependency Error, Retry Subscription, Status history, Timed out, peakSandboxMB found in apps/dashboard/src.
- Screenshot: Operate → Logs → Executions (/activity/executions), expand a failed run with the Error tab open on AI Diagnosis, crop to the expanded row (logs-execution-error-diagnosis.webp).
- Follow-up: none.

### reference/faqs.md
- Status: Fixed
- Terminology: "[Build with AI](../build/agent/README.md) (or your AI tool)" -> "The [fastn agent](...) (on Scale or Enterprise) or your AI tool". The "customer vs tenant" FAQ is deliberate and stays.
- Product accuracy: sandbox connection answer was wrong ("access is not automatically revoked") -> sandbox connections are deleted after 7 days, allowance 3 on Launch / 20 on Scale (services/api/src/lib/sandbox-connections.ts SANDBOX_CONNECTION_TTL_DAYS = 7; packages/db/src/quota.ts). Verified: customer_connections Launch 3 / Scale 10 / Enterprise unlimited (quota.ts:258-260), Version pins (ConnectorVersionPinsPanel.tsx), Per customer / Platform-wide, "Account level" (ConnectionDetailPage.tsx:384), Increase Instant timeout entitlement.
- Screenshot: none.
- Follow-up: "$50 a month" per extra Scale customer connection not verified in code (pricing likely lives in billing config outside the dashboard); confirm with billing.

### tutorials/README.md
- Status: Fixed
- Terminology: "within their SaaS product" -> "For the operator: the person on your team who sets up and runs fastn for your product"; 'Use "Build with AI"' -> "Use the fastn agent ... Needs a paid plan (Scale or Enterprise)"; fixed "how widget builder works" grammar; removed stray spaces inside link text.
- Product accuracy: role list Owner, Admin, Developer, Operator, Viewer, End User matches rbac.ts getRoleLabel.
- Screenshot: none (hidden index page).

### tutorials/saas-admin/README.md
- Status: Fixed
- Terminology: description "within your SaaS product organization config" -> "for your product: organization config"; "the person responsible" -> "the operator: the person on your team responsible"; onboarding "(Connect your product, Choose integrations, Embed the widget, Customers connect and customize)" -> "setup (Check your product, Pick your integrations, Set up the widget)"; 'the "Build with AI" button' -> "**Build with fastn agent** ... Needs a paid plan"; list punctuation made consistent.
- Screenshot: none.
- Follow-up: the folder name `tutorials/saas-admin/` and SUMMARY's "SaaS Admin" group label still carry the old term (outside my scope; renaming a path needs redirects).

### tutorials/developer/README.md
- Status: Fixed
- Terminology: "dedicated for" -> "for"; link "MCP gateway" -> "fastn MCP server" with a short note that fastn Connect gives AI agents your customers' connected apps.
- Screenshot: none.

## Deprecated synonyms across the whole repo (all .md, excluding reference/glossary.md which lists them on purpose)

Counts strip fenced code, inline code, link targets and HTML tags. Snapshot taken after my edits while other agents were still editing. Terms with zero hits: admin panel, external agent, Settings → API keys, update bot, Growth, Pro, Choose integrations, SaaS connector setup, AI usage, fastn MCP gateway, marketing words, em/en dash.

| Term | Hits | Files (hits) | Note |
| --- | --- | --- | --- |
| Build with AI | 5 | SHOTLIST.md (3), TRACKER.md (1), BACKLOG-docs.md (1) | internal planning files only |
| AI builder | 1 | build/workflows/the-editor.md (1) | -> fastn agent |
| marketplace | 1 | reference/rest/connectors.md (1) | generated, "hub/marketplace" spec import |
| console (not console.*) | 2 | manage/database.md (1), reference/rest/workflows.md (1) | check database.md; rest is generated |
| portal | 9 | tutorials/saas-admin/configuring-a-connector.md (2), manage/billing.md (2), reference/sdk/events.md (2), tutorials/saas-admin/creating-a-workflow-via-ai.md (1), build/connectors/auth-methods.md (1), reference/faqs.md (1) | mostly "provider's developer portal" / "HubSpot portal id" (legit); check billing.md (may mean a billing portal) |
| SaaS admin (prose) | 2 | TRACKER.md (1), SUMMARY.md (1) | SUMMARY group label |
| tenant (prose) | 13 | reference/faqs.md (3), build/agent/worked-example.md (2), SHOTLIST.md (1), operate/customers.md (1), getting-started/concepts.md (1), tutorials/saas-admin/managing-customers.md (1), build/connectors/creating-a-connector.md (1), build/agent/README.md (1), reference/ai-agents.md (1), reference/rest/organization.md (1) | faqs.md is the deliberate "customer vs tenant" FAQ; others -> customer |
| end customer | 1 | reference/rest/connections.md (1) | generated heading |
| end user (prose) | 25 | reference/rest/widgets.md (5), tutorials/saas-admin/roles-and-permissions-setup.md (3), manage/roles.md (2), README.md (1), BACKLOG-docs.md (1), embed/embedding/integration-flow.md (1), getting-started/concepts.md (1), getting-started/onboarding/embed-the-widget.md (1), tutorials/README.md (1), tutorials/saas-admin/README.md (1), tutorials/saas-admin/setting-up-your-organization.md (1), manage/api-keys.md (1), manage/general.md (1), build/workflows/the-editor.md (1), build/workflows/the-tabs.md (1), reference/rest/workflows.md (1), reference/rest/installations.md (1), reference/rest/connections.md (1) | many are the role name **End User** (legit: tutorials/*README, roles pages); the rest -> user / user at a customer |
| MCP gateway | 7 | README.md (2), build/mcp-gateway/README.md (2), getting-started/concepts.md (1), reference/ai-agents.md (1), reference/sdk/workspace-tools.md (1) | fine when it means fastn Connect; wrong if it names the fastn MCP server (mcp.fastn.dev/fastn-workspace) |
| Activity (page name) | 1 | tutorials/end-user/viewing-sync-status-and-history.md (1) | check if it means Operate → Logs (route is /activity, label Logs) or the widget's own activity view |
| API keys and MCP | 2 | SHOTLIST.md (2) | internal file |
| four steps (onboarding) | 1 | build/connectors/the-catalogue.md (1) | onboarding is now 3 setup steps + going-live items |
| Embed the widget (step name) | 10 | getting-started/onboarding/README.md (3), TRACKER.md (1), SUMMARY.md (1), getting-started/onboarding/embed-the-widget.md (1), getting-started/onboarding/customers-connect-and-customize.md (1), tutorials/developer/generating-embed-tokens.md (1), manage/api-keys.md (1), reference/code-samples.md (1) | UI step is "Set up the widget"; code-samples.md is a task heading (OK) |
| Customers connect and customize | 5 | getting-started/onboarding/README.md (2), TRACKER.md (1), SUMMARY.md (1), getting-started/onboarding/customers-connect-and-customize.md (1) | no longer an onboarding step; going-live item is "Your first customer connects" |
| system (say app) | 21 | reference/rest/organization.md (11), tutorials/end-user/viewing-sync-status-and-history.md (2), reference/rest/workflows.md (2), reference/rest/triggers.md (2), embed/widget-builder/style.md (1), tutorials/saas-admin/building-your-widget.md (1), build/connectors/creating-a-connector.md (1), reference/rest/observability.md (1) | organization.md is "system role" (legit API term); others -> app where it means a customer's software |

Biggest cross-page item: SUMMARY.md and getting-started/onboarding/* still describe the old four-step onboarding (Pick your integrations / Embed the widget / Customers connect and customize / Connect your product). The UI is Check your product, Pick your integrations, Set up the widget, then going-live items (ob3.tsx).
