# A3 findings: Operate, For your customers, Settings

Docs repo: /Users/khalid/fastn-code/fastn-docs-katie. Verified against fastn-platform origin/main (2287b9e20; later main 40cc783e6 only touched widget-builder files). Sources: apps/dashboard/src (lib/rbac.ts, App.tsx, pages/*), packages/embed/src/ui/i18n/en.ts, packages/rbac/src/engine.ts, packages/core/src/alerts.ts, services/api/src/routes/billing.ts. Nothing committed.

Cross-cutting facts confirmed:
- Operate rail: Health (/health), Customers (/customers), Connections (/connections), Logs (/activity).
- Logs tab strip: Events, Executions, Sync reports, plus Monitoring (Owner/Admin, entitlement activity.monitoring, shown locked when off). Traces is NOT on the strip (ActivityPage.tsx filters it out); /activity/traces still answers. Tab routes are paths (/activity/events etc.), not ?tab=.
- Health tabs: Needs attention (default), Overview, Pending updates, Alerts (Alerts dropped by canUseAlerts).
- Settings menu (rbac.ts SETTINGS_PAGES): People, General, Billing, Roles, Audit log (Owner/Admin); Environments, Secrets, Configs, Database, Trash (Developer+); Workflow tags (min role developer). /settings redirects to /settings/people.
- Brief discrepancy: the brief's canonical Logs tab list includes Traces; the product does not show it as a tab.

---

### operate/overview.md
- Status: Fixed
- Terminology: "Activity" -> "Logs" (3 places, prose and links).
- Product accuracy: rail items and Health flow match rbac.ts / HealthPage.tsx.
- Screenshot: none (lifecycle SVG already there).
- Follow-up: none.

### operate/health.md
- Status: Fixed
- Terminology: "[Activity](README.md)" -> "[Logs](README.md)".
- Product accuracy: tabs, Needs attention row kinds, empty state, Overview filters/tiles/strips/panels all match HealthPage.tsx, ReportingPage.tsx, reporting/ReportingPipeline.tsx and embed en.ts (insights.*). Added the failing-workflow row's **Runs** and **Fix with fastn agent** buttons (HealthPage.tsx WorkflowRow).
- Screenshot: /health (Needs attention tab, with at least one Update, Broken and Failing row), crop to the header + list. health-needs-attention.webp. Second: /health?tab=overview with All customers, Today, crop tiles + Right now + period strip. health-overview.webp.
- Follow-up: none.

### build/connector-updates.md (Pending updates)
- Status: OK
- Terminology: none needed.
- Product accuracy: header sub, empty state, "Show N already handled", status pills (lib/pending-update-story.ts), verification labels, Not tested yet, Notify affected organizations all match ConnectorUpdatesPage.tsx.
- Screenshot: /health?tab=updates with one proposal expanded (patch + verification label visible), crop to the row. pending-updates-expanded.webp.
- Follow-up: the working copy in /Users/khalid/fastn-code/fastn-docs (not katie) shows this file modified; I only edited the katie repo.

### operate/alerts.md
- Status: OK
- Terminology: none needed.
- Product accuracy: empty state, Turn on failure alerts, Custom alert, New alert, autosave/Untitled alert/Paused/No recipients, four Alert when options, window options, Watch, Deliver to, Firing history, Sync failure notifications all match embed en.ts (alerts.*); metric labels/units/descriptions match packages/core/src/alerts.ts.
- Screenshot: /health?tab=alerts, empty state (No alerts yet with both buttons) and Notification channels strip. alerts-empty.webp. Existing widget images unchanged.
- Follow-up: none.

### operate/customers.md
- Status: Fixed
- Terminology: "beside Health, Connections and Activity" -> "... and Logs".
- Product accuracy: columns, statuses, View connections, Create customer, External ID match pages/admin/TenantsPage.tsx. Added the **All tiers** filter and the plan cap note ("Your plan allows 3 customers, N in use", hard-cap refusal) from TenantsPage.tsx customerCapNote (live on Launch per coordinator).
- Screenshot: existing customers.jpg; re-shoot /customers in Docs-test with the cap note visible, crop header + table. customers-list.webp.
- Follow-up: none.

### tutorials/saas-admin/managing-customers.md
- Status: Fixed
- Terminology: H1 "Managing Customers" -> "Manage customers" (matches sidebar); "Activity → Executions/Events" -> "Operate → Logs → Executions/Events"; "isolated environment" -> "isolated space" (avoids clash with workflow environments).
- Product accuracy: create form fields now named as in TenantsPage.tsx (Customer Name, Slug, Admin Email, Tier, External ID; submit **Create Customer**). Limits override flow matches AccountBillingView.tsx ("Pick a customer to override. Overrides win over the plan default."). "Tenant not found" 404 confirmed in services/api/src/routes/embed.ts.
- Screenshot: /customers with the Create customer panel open, crop to the form. customers-create.webp.
- Follow-up: none.

### build/connections/README.md
- Status: Fixed
- Terminology: kept "app" per style rule (see follow-up).
- Product accuracy: views, status chips incl. Needs action, columns match pages/ConnectionsPage.tsx. Fixed: Customers-view search placeholder is "Search by customer, connector or name"; empty states differ per view ("No customer connections yet" + explanation); row ⋯ menu also has **Set as default** (active, not already default).
- Screenshot: /connections Customers view with a mix of statuses, crop toolbar + table. connections-customers.webp.
- Follow-up: UI copy uses "system": "Connect a system and its authenticated link appears here.", button "Connect a system", picker title "Connect a system", "Search systems", "Loading systems...", "No system matches that" (ConnectionsPage.tsx lines ~717-1100). Docs no longer quote these labels; recommend a platform copy change to "app".

### build/connections/creating-a-connection.md
- Status: Fixed
- Terminology: removed bolded labels that do not exist in the UI ("Connect an app", "Search apps", "Loading apps...") rather than quoting "system".
- Product accuracy: Authorise, Auth Method, Auth provider, Change provider, scope copy, "Nothing is stored here until you come back", stored-encrypted note confirmed in components/ConnectModal.tsx, lib/connect-audience.ts, embed en.ts.
- Screenshot: /connections → New connection, OAuth form for a connector with scopes, crop to dialog. connections-new-oauth.webp.
- Follow-up: same "system" copy issue as above; "Authorise" (UK) on the button vs US spelling elsewhere in the UI.

### build/connections/inside-a-connection.md
- Status: Fixed
- Terminology: "Authorised/authorised" -> "Authorized/authorized" (UI spelling); "[Activity]" -> "[Logs]".
- Product accuracy (pages/ConnectionDetailPage.tsx): added Back to connections, key-based auth note, Scope alternative "Limited to this workspace.", conditional **Connection scope** and **Usable in** rows; fixed a dangling "asks for confirmation first:" (now quotes "This cannot be undone.").
- Screenshot: /integrations/connections/<id> for an expired OAuth connection, crop header + Connection + Token and activity cards. connection-detail.webp.
- Follow-up: none.

### build/connections/statuses.md
- Status: Fixed
- Terminology: "Authorised" -> "Authorized".
- Product accuracy: status meanings now use the detail page's own one-liners (ConnectionDetailPage.tsx lines 338-346).
- Screenshot: none.
- Follow-up: none.

### build/connections/auth-types.md
- Status: OK
- Product accuracy: labels match lib/auth-method-label.ts.
- Screenshot: none.

### operate/README.md (Logs)
- Status: Fixed
- Terminology: "Cancelled" -> "Canceled" (UI label).
- Product accuracy: was "four tabs" including Traces. Now: three tabs (Events, Executions, Sync reports), Monitoring for Owner/Admin and locked on plans without it, Traces only by URL. Table reordered.
- Screenshot: /activity/events, crop to the tab strip + header (shows Monitoring locked on Launch). logs-tabs.webp.
- Follow-up: brief's canonical Logs tab list should drop Traces.

### operate/events.md
- Status: Fixed
- Terminology: "Activity → Events" -> "Operate → Logs → Events · /activity/events".
- Product accuracy (pages/EventsPage.tsx): added `Skipped` status, Test/Live environment options, named the **Auto refresh** toggle.
- Screenshot: /activity/events with rows and one expanded detail panel. logs-events.webp.
- Follow-up: the empty-state quote says "connected apps"; the UI says "connected systems" (EventsPage.tsx line ~356, also page sub). Recommend UI copy change.

### operate/executions.md
- Status: Fixed
- Terminology: path -> "Operate → Logs → Executions"; "Cancelled" -> "Canceled" (EXEC_LABEL).
- Product accuracy (pages/ExecutionsPage.tsx): added **Skipped** status (fastn.skip). Filters, tiers, Triggered by values, rows per page 10/20/50, Runs/Logs switch, Enable payload searching, detail tabs all confirmed.
- Screenshot: /activity/executions with a failed run expanded on the Error tab (AI Diagnosis). logs-execution-error.webp.
- Follow-up: status pills show raw values (via label map); not verified whether the Skipped status is also a filter pill (it is not in STATUS_FILTERS).

### operate/traces.md
- Status: Fixed
- Terminology: "Activity strip" -> "Operate → Logs strip".
- Product accuracy: filters and empty state match pages/TracesPage.tsx.
- Screenshot: none (page intentionally hidden).

### operate/sync-reports.md
- Status: Fixed
- Terminology: path -> "Operate → Logs → Sync reports"; "Build with AI" -> "the fastn agent".
- Product accuracy: matches components/SyncReportsTable.tsx.
- Screenshot: /activity/sync-reports with one report expanded on Changes. logs-sync-report.webp.

### operate/triggers/README.md
- Status: OK
- Screenshot: none.

### operate/triggers/using-a-webhook-trigger.md
- Status: Fixed
- Terminology: "Build with AI" -> "the fastn agent".
- Product accuracy: URL shape webhooks.fastn.dev/<env>/triggers/... (packages/core/src/trigger-webhook-url.ts); Monitor only / Enforce (ApiKeysTab.tsx).
- Screenshot: none.

### operate/troubleshooting.md
- Status: Fixed
- Terminology: "Build with AI" -> "the fastn agent" (2 places).
- Product accuracy: statuses, row menu, alerts names, Trash quote confirmed.
- Screenshot: none.

### tutorials/developer/troubleshooting.md
- Status: OK
- Product accuracy: 8 h token TTL (routes/embed.ts TOKEN_TTL_MS), test-mode 403 message (server.ts), IDENTITY_* codes, "Verify caller identity (HMAC)" label all confirmed.
- Screenshot: none.

### tutorials/end-user/README.md
- Status: Fixed
- Terminology: link titles to sentence case matching SUMMARY (Connect apps, Customize an integration, Extend a pre-built integration, Get alerted, Connect Claude and other AI clients, View sync status and history).
- Screenshot: none.

### tutorials/end-user/connecting-apps-via-widget.md
- Status: Fixed
- Terminology: H1 "Connecting Apps via Widget" -> "Connect apps"; cross-link titles.
- Product accuracy: all widget strings (Search integrations, status lines, Manage, New installation, Delete connection/installation, Ask the assistant, Generate MCP URL) present in embed en.ts.
- Screenshot: widget hub (/widgets/hub preview in Docs-test) list with mixed statuses, crop widget only. widget-integrations-list.webp.

### tutorials/end-user/customizing-your-integrations.md
- Status: Fixed
- Terminology: H1 -> "Customize an integration"; first-run button named **Build with fastn agent** (components/SyncConfigModal.tsx) and said it is shown only to the provider's team (canRunAgent = operator+), instead of "needs an operator role".
- Product accuracy: dialog title, Entity pairs, tabs, filter operators (components/sync-config/state.ts), Save changes tooltip, Discard changes? confirmed.
- Screenshot: Integration Configuration dialog on Field mappings with a locked required row, crop to dialog. widget-config-mappings.webp.
- Follow-up: packages/embed/src/ui/ConfigEditor.tsx is a second editor with a different operator set (equals, not equals, contains, greater than, less than, exists). Confirm which editor the embedded widget shows customers; the page documents SyncConfigModal.

### tutorials/end-user/extending-a-prebuilt-integration.md
- Status: Fixed
- Terminology: H1 -> "Extend a pre-built integration"; "**Build with AI** button" -> "**Build with fastn agent** button".
- Product accuracy: build-gate message confirmed (services/agent build-gate.ts).
- Screenshot: none.

### tutorials/end-user/getting-alerted.md
- Status: Fixed
- Terminology: H1 -> "Get alerted"; cross-link titles.
- Product accuracy: matches embed en.ts alerts.* and core alerts.ts metrics.
- Screenshot: existing widget images are fine; no new ones.

### tutorials/end-user/viewing-sync-status-and-history.md
- Status: Fixed
- Terminology: H1 -> "View sync status and history"; cross-link titles.
- Product accuracy: Insights panels, connection states, categories, workflow tabs present in embed en.ts.
- Screenshot: widget ⋯ → Insights, 7 days, crop to panels row. widget-insights.webp.

### tutorials/end-user/connecting-claude.md
- Status: OK
- Product accuracy: 10-minute single-use link (en.ts mcp.validity), error copy confirmed.
- Screenshot: widget ⋯ → Generate MCP URL dialog with the URL masked. widget-mcp-url.webp.

### manage/README.md
- Status: Fixed
- Terminology: "moved to **Embed → MCP server**" -> "moved to **Embed → API keys** and **Embed → MCP server**".
- Product accuracy: menu order and role table match SETTINGS_PAGES.
- Screenshot: Settings menu open in the rail as Owner, crop to the menu. settings-menu.webp.
- Follow-up: Environments (manage/environments.md) is a live Settings page but not in my list; owner should verify.

### manage/people.md
- Status: OK (pages/admin/AdminUsersPage.tsx, InviteUserSlideOver.tsx).
- Screenshot: existing settings-people.jpg; re-shoot /settings/people in Docs-test. settings-people.webp.

### manage/roles.md
- Status: OK. Counts 44/44/36/21/6/35 and matrix verified against packages/rbac/src/engine.ts and PermissionsPage.tsx RESOURCES.
- Screenshot: existing settings-roles.jpg; re-shoot /settings/roles with Operator selected. settings-roles.webp.

### tutorials/saas-admin/roles-and-permissions-setup.md
- Status: Fixed
- Terminology: H1 "Roles & Permissions Setup" -> "Set up roles and permissions".
- Product accuracy: "Save" steps -> **Role Name** field and **Create Role** button (PermissionsPage.tsx). Audit filters/columns match AuditPage.tsx.
- Screenshot: none (roles.md covers it).

### manage/general.md
- Status: Fixed
- Product accuracy: Your product card copy was wrong. Now "Not connected yet. Required to go live." / "API docs found, not connected yet. Required to go live." / "{product} is connected to fastn." and button **Connect {product}** (components/FirstIntegration.tsx YourProductCard). Other fields match GeneralTab.tsx.
- Screenshot: /settings/general, crop Organization + Joining by email domain cards. settings-general.webp.

### manage/billing.md
- Status: Fixed
- Product accuracy: plan card line corrected to what AccountBillingView.tsx renders ("Billing 12 customer connections · renews <date>" or "... customers", "ends" once cancelled); reworded the garbled onboarding-credits sentence. All other labels confirmed (AccountBillingView.tsx, AIUsageSlideOver.tsx, TenantBillingView.tsx, routes/billing.ts quota labels). Limits table not re-derived row by row; plan numbers in packages/db/src/quota.ts comments agree on Launch 3 customers / 3 customer connections, Scale 10 included.
- Screenshot: /settings/billing on Launch, crop plan card + Credits. settings-billing.webp.
- Follow-up: the onboarding-credits overspend rule ("taken off the next month's credits") was in the original; not verified in code.

### manage/audit-log.md
- Status: OK (pages/admin/AuditPage.tsx).
- Screenshot: /settings/audit with filters set, crop table. settings-audit.webp.

### manage/secrets.md
- Status: OK (pages/settings/SecretsTab.tsx).
- Screenshot: /settings/secrets Create Secret panel. settings-secrets-create.webp.

### manage/configs.md
- Status: OK (pages/settings/StaticConfigsTab.tsx).
- Screenshot: none.

### manage/database.md
- Status: OK (pages/settings/DatabaseTab.tsx).
- Screenshot: /settings/database as Owner, crop the Shared/Your own choice. settings-database.webp.

### manage/workflow-tags.md
- Status: Fixed
- Terminology: "Uncategorised" -> "Uncategorized" (UI label, components/WorkflowCategories.tsx, lib/workflow-categories.ts).
- Screenshot: none (separate PR already reshot it).

### manage/trash.md
- Status: OK (pages/TrashPage.tsx).
- Screenshot: none.

### manage/profile.md
- Status: OK (pages/ProfilePage.tsx).
- Screenshot: none.
