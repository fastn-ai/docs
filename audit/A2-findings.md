# A2 findings: Build section (50 pages)

Docs repo: /Users/khalid/fastn-code/fastn-docs-katie. Verified against fastn-platform origin/main (40cc783e6, 25 Nov 2026). Key sources: apps/dashboard/src/lib/rbac.ts (sidebar), components/CreateIntegrationMenu.tsx, components/BuildWithAgentMenuItem.tsx, pages/ConnectorsPage.tsx (Create connector menu ~L9985), pages/IntegrationsPage.tsx (tabs), pages/orchestrator/* and packages/embed/src/ui/i18n/en.ts (agent copy), lib/mcp.ts + components/ConnectMcpPanel.tsx + pages/settings/McpServerTab.tsx (MCP server), pages/YourProductPage.tsx + settings/SaasConnectorsTab.tsx + your-product/* (Connect your product), pages/WorkflowsPage.tsx, services/workflow/src/sandbox/isolate.ts (runtime).

Totals: OK 14, Fixed 34, Needs follow-up 2.

SUMMARY.md (Build section only): "Build with AI" -> "Build with fastn agent"; "Create a workflow with AI" -> "Create a workflow with the fastn agent".

### build/README.md
- Status: Fixed
- Terminology: tab "Build with AI" -> "fastn agent"; "fastn's builder" -> "The fastn agent"; "Build with AI" in prose -> "the fastn agent"; link texts "Building from your AI agent" -> "Build from your AI tool", "MCP gateway" -> "fastn MCP server".
- Product accuracy: "All Build pages" said Build with AI "has its own sidebar item" (false: rbac.ts has no row, comment L261) and listed Connections and Pending updates as Build pages (they are under Operate). Rewrote the section to match the sidebar (Connect your product, Integrations) and the SUMMARY order; removed the Connections and Pending updates content-refs, added Connect your product, Integrations, Test and release.
- Screenshot: none (diagram already present).
- Follow-up: none.

### build/agent/README.md
- Status: Fixed
- Terminology: H1 "Build with AI" -> "Build with fastn agent"; warning hint now says "Building with the fastn agent". "START FROM AN EXAMPLE" -> "Start from an example" (en.ts `assistant.examples`).
- Product accuracy: all labels checked in en.ts and orchestrator files (Build an integration, emptyBody quote, Sessions, No sessions yet..., Search sessions, Collapse sessions sidebar, the 4 starter cards, Write a message…, Attach a file, Build progress, phases Use cases/Connectors/Workflows/Widget, Complete, Worked, Show details, Download document, Other…, By agent, context meter `19k / 1000k` format). Credits badge Owner/Admin only (App.tsx AI_USAGE_ROLES). Added that the agent also needs the "fastn agent" module switched on (use-can-build-with-ai.ts checks the aiBuilder.integrations entitlement besides the Operator role).
- Screenshot: /agent, new session empty state (hero, 4 example cards, composer with approval chip); crop to centre pane plus Sessions rail. agent-empty-state.webp. Second: /agent/<thread> mid-build with Build progress rail expanded; crop chat plus right rail. agent-build-progress.webp.
- Follow-up: none.

### tutorials/saas-admin/creating-a-workflow-via-ai.md
- Status: Fixed
- Terminology: description, H1 and intro "Build with AI" -> "the fastn agent"; "See [Build with AI]" -> "See [Build with fastn agent]".
- Product accuracy: "Add Filters" -> "Add filters" (en.ts `assistant.addFilters`). Verified WE'VE SET THIS UP FOR YOU, Record Matching Strategy, + Add Mapping, Change, Looks good, turn on, Feedback (optional)..., Revise, Approve, Diagram sub-tabs Flow/Sequence/Docs (WorkflowVisualization.tsx), Save workflow, Publish & Deploy, widget "Workflow Diagram" (BuilderControls.tsx).
- Screenshot: /agent thread at the field-mapping review card (WE'VE SET THIS UP FOR YOU banner, rows, Looks good, turn on); crop to the card. agent-field-mapping-review.webp.
- Follow-up: none.

### build/agent/approval-mode.md
- Status: OK
- Terminology: none needed.
- Product accuracy: Auto is the default for a new session (OrchestratorPage.tsx `pendingAutoAccept` starts true); Manual/Auto hints, Accept/Always allow/Reject, 50,000-byte cap (ToolApprovalCard.tsx L235), secrets redacted. en.ts strings are lowercase ("view raw input", "note to agent (optional)"); docs show them uppercase, presumably the rendered CSS. Left as is.
- Screenshot: /agent thread in Manual mode with a pending tool approval card; crop to the card. agent-approval-card.webp.
- Follow-up: none.

### build/agent/worked-example.md
- Status: Fixed
- Terminology: link text "Lifecycle" -> "Test and release".
- Product accuracy: matches the approval-card and build-progress copy above. Plan and field-mapping content is agent output, so it can't be checked against code.
- Screenshot: none (approval-mode and agent README shots cover it).
- Follow-up: none.

### build/building-from-your-ai-agent.md
- Status: Fixed
- Terminology: H1 "Building from your AI agent" -> "Build from your AI tool" (matches SUMMARY); "your agent" -> "your AI tool" throughout; "MCP gateway" -> "fastn MCP server"; "Build with AI" -> "the in-app fastn agent"; added "uses no fastn AI credits".
- Product accuracy: workflow tabs Test cases and Executions exist (WorkflowsPage.tsx L5171-5173); Embed → Widget OK.
- Screenshot: none.
- Follow-up: none.

### build/mcp-gateway/README.md
- Status: Fixed
- Terminology: description rewritten for the fastn MCP server; "Your agent" -> "Your AI tool"; "fastn MCP gateway (fastn Connect)" -> "fastn Connect (the MCP gateway)"; "How your agent connects" -> "How your AI tool connects"; "such as Build with AI" -> "such as the fastn agent".
- Product accuracy: dialog title, subtitle, Recommended/Other, MCP server URL row confirmed (ConnectMcpModal.tsx, ConnectMcpPanel.tsx). Developer+ role confirmed (CONNECT_MCP_MIN_ROLE = developer). Added the auth method shown on the page: "OAuth 2.0 with dynamic client registration", leave Client ID/Secret empty (mcp.ts MCP_AUTH_TYPE/HINT). Added a GitHub Copilot paragraph, because the page has a GitHub Copilot tile (mcp.ts id "copilot") and the docs had no page for it. A2A "soon" confirmed (EmbedMethodsPanel.tsx L446).
- Screenshot: /mcp-server with no tile selected (Recommended Claude card, Other grid, MCP server URL and Authentication rows); full pane. mcp-server-page.webp.
- Follow-up: the client table rows for ChatGPT and Lovable match the dashboard tile steps (mcp.ts) but not the dedicated pages (see chatgpt.md, lovable.md). One side needs a live recheck.

### build/mcp-gateway/claude.md
- Status: Fixed
- Terminology: "same steps as every agent: see Building from your AI agent" -> "every AI tool: see Build from your AI tool"; "fastn's MCP page" -> "fastn's **MCP server** page".
- Product accuracy: Add to Claude, second Claude tile, Add for the whole organization match mcp.ts. Third-party Claude UI not verifiable from the repo.
- Screenshot: none (existing images).
- Follow-up: none.

### build/mcp-gateway/claude-code.md
- Status: Fixed
- Terminology: link text as above. Figcaption "under **Connect AI tools**" -> "under **Other** on the fastn **MCP server** page" (no "Connect AI tools" group exists; ConnectMcpPanel uses Recommended / Other).
- Product accuracy: command and Desktop mcp-remote config match mcp.ts.
- Screenshot: none (existing).
- Follow-up: none.

### build/mcp-gateway/chatgpt.md
- Status: Needs follow-up
- Terminology: link text as above.
- Product accuracy: the page walks through ChatGPT **Plugins** → **Add** → **Add custom MCP server** → **Create as a plugin**. The dashboard tile (mcp.ts L541-549) and the MCP README table say Settings → Apps & Connectors → Advanced settings → Developer mode, then Add custom connector. Not changed. Can't tell from the repo which is current.
- Screenshot: none (existing).
- Follow-up: recheck ChatGPT live; update either mcp.ts tile steps (platform) or this page plus the README row.

### build/mcp-gateway/cursor.md
- Status: Fixed
- Terminology: link text.
- Product accuracy: Add to Cursor, ~/.cursor/mcp.json, project .cursor/mcp.json match mcp.ts.
- Screenshot: none (existing).
- Follow-up: none.

### build/mcp-gateway/vscode.md
- Status: Fixed
- Terminology: link text.
- Product accuracy: Install in VS Code, `code --add-mcp`, `servers` key match mcp.ts.
- Screenshot: none (existing).
- Follow-up: none.

### build/mcp-gateway/codex.md
- Status: Fixed
- Terminology: link text.
- Product accuracy: command and TOML match mcp.ts.
- Screenshot: none.
- Follow-up: none.

### build/mcp-gateway/antigravity.md
- Status: Fixed
- Terminology: link text.
- Product accuracy: serverUrl, path, View raw config, .agents/mcp_config.json match mcp.ts note.
- Screenshot: none (existing).
- Follow-up: none.

### build/mcp-gateway/devin.md
- Status: Fixed
- Terminology: link text. (Alt text quotes Devin's own "marketplace" labels; left.)
- Product accuracy: steps and CLI command match mcp.ts.
- Screenshot: none (existing).
- Follow-up: none.

### build/mcp-gateway/cline.md
- Status: Fixed
- Terminology: link text.
- Product accuracy: streamableHttp and 405 note match mcp.ts.
- Screenshot: none (existing).
- Follow-up: none.

### build/mcp-gateway/lovable.md
- Status: Needs follow-up
- Terminology: link text.
- Product accuracy: the page says **Connectors** → **Add custom** → **MCP server**. The dashboard tile (mcp.ts L554-562) and the README row say Connectors → **Chat connectors** tab → **New MCP server**. Not changed.
- Screenshot: none (existing).
- Follow-up: recheck Lovable live and align mcp.ts or this page plus the README row.

### build/mcp-gateway/bolt.md
- Status: Fixed
- Terminology: link text.
- Product accuracy: matches mcp.ts (Connectors (MCP), custom MCP server). The Fastn Workspace tool-picker explanation agrees with mcp.ts withFastnWorkspace.
- Screenshot: none (existing).
- Follow-up: none.

### reference/ai-agents.md
- Status: Fixed
- Terminology: "Product MCP gateway" -> "fastn MCP server"; "against the product gateway" / "A gateway client" -> fastn MCP server; added a line saying how fastn Connect differs; "you, the SaaS company" -> "you, the company whose product embeds fastn".
- Product accuracy: tier ceilings 25s/2 min, 15 min, 36 h confirmed (WorkflowsPage.tsx L1806, L4601-4653, entitlements/modules.ts L71). Confirmed `fastn.connectors` works at run time (isolate.ts L757-761) and clarified "Both work, at save time and at run time".
- Screenshot: none (page is for machines by design).
- Follow-up: none.

### manage/saas-connectors.md
- Status: OK
- Terminology: OK.
- Product accuracy: subtitle, empty state, panel title, Select your product's connector…, helper texts, 50-char scope limit, Add connector, tabs API connector / Webhooks, role gates all match YourProductPage.tsx, SaasConnectorsTab.tsx, rbac.ts.
- Screenshot: /your-product, API connector tab with the Connect your product panel open; crop to the panel. connect-your-product-panel.webp.
- Follow-up: none.

### manage/saas-webhooks.md
- Status: OK
- Terminology: OK.
- Product accuracy: Add webhook, Endpoint URL, All customers, Send test, Deliveries, Pause, Rotate secret, Resend, Payload schema, + Connector schema, Default, Editing, Add field, Value from, Event path, JSON Schema, Use example, the "Only these…" fields and Every connector all found in ProductWebhooks.tsx / PayloadSchemaEditor.tsx. Retry timing and signing come from the event service and were not re-derived.
- Screenshot: none (existing add-form image).
- Follow-up: none.

### build/integrations.md
- Status: Fixed
- Terminology: "[Build with AI]" -> "[the fastn agent]".
- Product accuracy: Create integration menu items and notes match CreateIntegrationMenu.tsx exactly. Tabs match IntegrationsPage.tsx (Action reviews is a platform_admin strip tab, correctly omitted).
- Screenshot: /integrations?tab=connectors with the Create integration menu open; crop to the header and menu. integrations-create-menu.webp.
- Follow-up: none.

### build/connectors/README.md
- Status: Fixed
- Terminology: "**Build with AI**" -> "the fastn agent"; "The catalog" link text -> "The catalogue" (sidebar title).
- Product accuracy: Create connector menu (From scratch, Build with fastn agent, Build in your AI tool, Import from file; Import fallback) matches ConnectorsPage.tsx L9985-10017. Intro quote and badges confirmed.
- Screenshot: /integrations?tab=connectors with the Create connector menu open; crop to the header and menu. connectors-create-menu.webp.
- Follow-up: none.

### tutorials/saas-admin/configuring-a-connector.md
- Status: Fixed
- Terminology: H1 "Configuring a Connector" -> "Configure a connector" (sentence case, matches SUMMARY). Menu items "Build with AI" / "Build from Claude or any MCP client" -> "Build with fastn agent" / "Build in your AI tool"; section renamed; added the paid-plan note and the Launch copy.
- Product accuracy: as connectors README.
- Screenshot: none (connectors-create-menu.webp covers it).
- Follow-up: none.

### build/connectors/the-catalogue.md
- Status: Fixed
- Terminology: Create connector menu item names corrected (as above), with links to the agent and MCP server pages.
- Product accuracy: filters, empty-state copy, Managed by Fastn, page guide (Page guide · N steps, New to Connectors?, Not now, Show me, the 4 step titles, Take me there) verified in ConnectorsPage.tsx, PageGuideModal.tsx, page-guides.ts. Live count is "All connectors 1030" (coordinator check); the page has no hard-coded count.
- Screenshot: /integrations?tab=connectors default state (categories column, filters, cards); crop to the top half. connectors-catalogue.webp.
- Follow-up: none.

### build/connectors/creating-a-connector.md
- Status: Fixed
- Terminology: "Build with AI also reads it" -> "The fastn agent also reads it".
- Product accuracy: Request connector first field label is **Which system?** in the UI (RequestConnectorModal.tsx L310); docs said "Which app?". Docs now follow the UI.
- Screenshot: Create connector → From scratch dialog, empty state; crop to the dialog. connector-create-dialog.webp.
- Follow-up: platform copy: "Which system?" goes against the "app, not system" rule; suggest the UI change it to "Which app?" and then revert the docs.

### build/connectors/inside-a-connector.md
- Status: OK
- Terminology: OK.
- Product accuracy: tab names, tile and Details copy, Versions, Connections, Version pins copy all found in ConnectorsPage.tsx. "Auto-versioned on update" is server data (not in UI code).
- Screenshot: /integrations/connectors/hubspot Overview tab; crop to the header, tabs and tiles. connector-detail-overview.webp.
- Follow-up: none.

### build/connectors/auth-methods.md
- Status: OK
- Terminology: OK.
- Product accuracy: Manage providers / Add provider / View providers, Create Provider, New Auth Provider, + Detailed, + Group, Response Type, Token Grant Type, URL Variables, Use this app, Change provider confirmed. The UI reads "Community", a dash and "read-only", with a long dash; the docs' hyphen follows the style rule.
- Screenshot: none (existing images).
- Follow-up: none.

### build/connectors/action-detail.md
- Status: Fixed
- Terminology: three "Build with AI" -> "the fastn agent" (and "your AI tool" where it reads descriptions).
- Product accuracy: tab names, Stored action setting help text, Mocks copy, run panel strings, version tooltip, Propose update all found.
- Screenshot: /integrations/connectors/<slug>/<action> with the Run panel open in mock mode; crop to the editor. action-editor-run.webp.
- Follow-up: none.

### build/connectors/webhook-config.md
- Status: OK
- Terminology: OK.
- Product accuracy: all form labels and copy found in ConnectorsPage.tsx. The UI's "None", a dash and "accept all requests" with a long dash; docs use a hyphen.
- Screenshot: none.
- Follow-up: none.

### build/connectors/editing-and-deleting.md
- Status: OK
- Terminology: OK.
- Product accuracy: Credential verification copy, Save changes, Create Action, Restore Version, Delete Connector options all found.
- Screenshot: none.
- Follow-up: none.

### build/connectors/importing-and-exporting.md
- Status: OK
- Terminology: OK.
- Product accuracy: the Replace existing connector? dialog copy matches ConnectorsPage.tsx L4037-4042. Export Selected found.
- Screenshot: none.
- Follow-up: none.

### build/connectors/connect-an-app.md
- Status: Fixed
- Terminology: none.
- Product accuracy: "You will authorise in a new window" -> "You will authorize in a new window" (en.ts `account.oauthTitle`); button "Authorise" -> "Authorize" (en.ts `account.authorize`).
- Screenshot: Connect dialog for an OAuth connector (e.g. HubSpot); crop to the dialog. connect-dialog-oauth.webp.
- Follow-up: none.

### build/unified-apis/README.md
- Status: Fixed
- Terminology: OK.
- Product accuracy: added **Scheduling** to the example categories (the live check shows 6 categories). Subtitle quote matches UnifiedApiPage.tsx L937.
- Screenshot: none (existing image; reshoot so it shows all 6 categories). unified-apis.webp.
- Follow-up: the existing unified-apis.jpg shows 5 categories; reshoot.

### build/unified-apis/setup-and-usage.md
- Status: Fixed
- Terminology: title-case headings -> sentence case; "Log in" -> "Sign in"; "SaaS application" -> "your product"; API key step now points to **Embed → API keys**; the x-org-id paragraph now says "customer ID".
- Product accuracy: Copy curl, operations and paths match lib/unified-op-curl.ts (`/v1/unified/<cat>/<entity>`, `/search`, `page_size=50`, Bearer YOUR_FASTN_API_KEY).
- Screenshot: none (existing).
- Follow-up: none.

### build/unified-apis/inside-a-category.md
- Status: OK
- Terminology: OK.
- Product accuracy: paths and operations match unified-op-curl.ts; Copy curl and All providers confirmed.
- Screenshot: /integrations?tab=unified&surface=crm, one entity block with providers and API rows; crop to that block. unified-category-crm.webp.
- Follow-up: none.

### build/unified-apis/unified-vs-direct.md
- Status: OK
- Terminology / accuracy: OK.
- Screenshot: none.
- Follow-up: none.

### build/workflows/README.md
- Status: Fixed
- Terminology: "In this section" link texts now use the sidebar titles (Write a workflow in code, Test a workflow, Test and release).
- Product accuracy: status tooltips (workflow-row-status.ts), Search workflows, tier pills, Connect GitHub, Create workflow confirmed.
- Screenshot: /integrations?tab=workflows list with at least one Live and one Unpublished row; crop to the header and the first rows. workflows-list.webp.
- Follow-up: none.

### build/workflows/the-editor.md
- Status: Fixed
- Terminology: "Build with AI" -> "the fastn agent (or your AI tool)" in 3 places.
- Product accuracy: tier limits, retry fields, Publish & Deploy, Discard dialog, Reset to generated, End user / Technical all confirmed. The quoted code-editing-off banner matches WorkflowsPage.tsx L5140 word for word, "AI builder" included.
- Screenshot: workflow editor drawer on an existing workflow, Test tab; crop to the full drawer. workflow-editor.webp.
- Follow-up: the platform banner says "the AI builder". Suggest the UI change it to "the fastn agent", then update the quote here.

### tutorials/saas-admin/configuring-a-workflow-in-code.md
- Status: Fixed
- Terminology: H1 "Configuring a Workflow in Code" -> "Write a workflow in code"; Build with AI -> fastn agent / your AI tool; "Lifecycle" link -> "Test and release".
- Product accuracy: placeholders "e.g. Sync Contacts" and "sync-contacts", Create Workflow, Draft saved confirmed.
- Screenshot: none (workflow-editor.webp covers it).
- Follow-up: none.

### build/triggers/README.md
- Status: OK
- Terminology: OK.
- Product accuracy: sub-tabs, status filter, detail-panel sections, Trigger Now, "which is the limit of" text confirmed.
- Screenshot: /integrations?tab=triggers&trigger=scheduler with a row's detail panel open; crop to the panel. trigger-detail-panel.webp.
- Follow-up: none.

### tutorials/saas-admin/setting-up-triggers.md
- Status: Fixed
- Terminology: H1 "Setting Up Triggers" -> "Set up triggers".
- Product accuracy: Add a trigger, What should start the workflow?, Advanced options, Add route confirmed.
- Screenshot: Add trigger picker (Webhook / Schedule / App event); crop to the dialog. add-trigger-picker.webp.
- Follow-up: none.

### build/triggers/webhooks.md
- Status: Fixed
- Terminology: "Can Build with AI do this for me?" -> "Can the fastn agent do this for me?", plus 3 more renames; added that your AI tool can do the same over the fastn MCP server.
- Product accuracy: Webhook ID, Deduplication key, Create trigger, None (public), API Key (x-api-key), Copy as cURL confirmed.
- Screenshot: none.
- Follow-up: none.

### build/triggers/schedulers.md
- Status: Fixed
- Terminology: none.
- Product accuracy: "Delay (minutes)" -> **Delay** (minutes): the UI label is "Delay" with a "minutes" hint (CreateScheduledEventForm.tsx L749). Other labels confirmed.
- Screenshot: none.
- Follow-up: none.

### build/triggers/app-events.md
- Status: OK
- Terminology: OK.
- Product accuracy: Copy ingest URL, Retry Subscription, no-connection message, Search events..., Not Subscribed confirmed.
- Screenshot: none.
- Follow-up: none.

### build/workflows/lifecycle.md
- Status: Fixed
- Terminology: Build with AI -> the fastn agent or your AI tool; "The tabs" link -> "Test a workflow".
- Product accuracy: toasts, Publish a snapshot first, Provided by your provider, Requires review confirmed.
- Screenshot: workflow editor Publish & Deploy section with an environment 1 behind; crop to that section. publish-deploy.webp.
- Follow-up: the H1 is "Lifecycle" but the sidebar title is "Test and release". Consider renaming the H1 (left as is).

### build/workflows/the-tabs.md
- Status: Fixed
- Terminology: Build with AI -> the fastn agent (or your AI tool); "Activity → Executions" -> "Operate → Logs → Executions".
- Product accuracy: the warning said the runtime does not provide plural `fastn.connectors`, so a plural call fails. That is wrong: isolate.ts L757-761 aliases `connectors: connector`. Replaced it with a note that both forms work and that dynamic `fastn.connectors[slug]` needs manual wiring. Tab list matches WorkflowsPage.tsx L5153-5175.
- Screenshot: workflow editor, Test cases tab with grouped cases; crop to the tab. workflow-test-cases.webp.
- Follow-up: the H1 "The tabs" doesn't match the sidebar title "Test a workflow". "Smart features" (docs section name) not found in the dashboard code; it is likely generated by a service, so check it live.

### manage/environments.md
- Status: OK
- Terminology: OK.
- Product accuracy: intro quote, Create Environment, Protected, No repository connected, Awaiting review, Mirror all workflows / Sync to GitHub, Require review before publishing confirmed.
- Screenshot: /settings/environments with the GitHub panel unconnected and the table; full pane. settings-environments.webp.
- Follow-up: none.

### tutorials/developer/deployment.md
- Status: OK
- Terminology: OK (no product UI).
- Product accuracy: nothing UI-specific to verify.
- Screenshot: none.
- Follow-up: none.

### build/patterns.md
- Status: Fixed
- Terminology: "[Build with AI]" -> "[the fastn agent] or [your AI tool]".
- Product accuracy: retry defaults match the-editor.md.
- Screenshot: none.
- Follow-up: none.

## Cross-page notes (outside A2)
- Other pages still link "Build with AI" / "Building from your AI agent" link texts? Not checked outside my set; a repo-wide grep for "Build with AI" is recommended.
- dashboard copy uses "system" in Request connector ("Which system?") and "AI builder" in the code-editing banner: platform follow-ups.
