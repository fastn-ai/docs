# Docs audit tracker (unpublished)

Full pass over every page in SUMMARY.md, started 24 Nov 2026: terminology, accuracy against the product (fastn-platform main), and screenshots from the demo org. Status: [ ] to do, [~] in progress, [x] done. Terminology rules live in reference/glossary.md.

## Workstreams

- [x] Terminology and accuracy audit of all 158 pages (4 batches; findings in audit/)
- [x] Competitor benchmark of docs structure and terms
- [x] Glossary as the one canonical term list
- [x] Sweep leftover deprecated terms across all pages
- [~] Screenshots from the live dashboard, dark mode, .webp: 25 captured, placed on 23 pages; populated views (customers, connections, workflows, logs, fastn agent) wait on demo data
- [x] Link check (0 broken), dash check (0)
- [ ] PR

## Pages

| # | Section | Page | File | Audit | Screenshot | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Get started | Welcome to fastn | `README.md` | [x] OK | [ ] | |
| 2 | Get started | Quickstart: your first integration | `getting-started/quickstart.md` | [x] OK | [x] | connect-your-ai-tool.webp |
| 3 | Get started | Authentication | `tutorials/developer/authentication-and-api-keys.md` | [x] OK | [ ] | |
| 4 | Get started | Core concepts | `getting-started/concepts.md` | [x] Fixed | [ ] | |
| 5 | Get started | Platform tour | `getting-started/platform-tour.md` | [x] Fixed | [x] | home-launch-plan.webp |
| 6 | Get started | Set up fastn | `getting-started/onboarding/README.md` | [x] Fixed | [x] | get-started-checklist.webp |
| 7 | Get started | Pick your integrations | `getting-started/onboarding/choose-integrations.md` | [x] Fixed | [ ] | |
| 8 | Get started | Set up and add the widget | `getting-started/onboarding/embed-the-widget.md` | [x] Fixed | [ ] | |
| 9 | Get started | Your first customer connects | `getting-started/onboarding/customers-connect-and-customize.md` | [x] Fixed | [ ] | |
| 10 | Get started | Connect your product | `getting-started/onboarding/connect-your-product.md` | [x] Fixed | [ ] | |
| 11 | Get started | Set up your organization | `tutorials/saas-admin/setting-up-your-organization.md` | [x] Fixed | [ ] | |
| 12 | How-to guides | How-to guides | `how-to/README.md` | [x] OK | [ ] | |
| 13 | How-to guides | Read and write a customer's CRM records | `how-to/crm-records.md` | [x] Fixed | [ ] | |
| 14 | How-to guides | Run an integration for one customer | `how-to/run-for-a-customer.md` | [x] OK | [ ] | |
| 15 | How-to guides | Start an integration from your product's events | `how-to/events-from-your-product.md` | [x] Fixed | [ ] | |
| 16 | Build | Overview | `build/README.md` | [x] Fixed | [ ] | |
| 17 | Build | Build with fastn agent | `build/agent/README.md` | [x] Fixed | [ ] | |
| 18 | Build | Create a workflow with AI | `tutorials/saas-admin/creating-a-workflow-via-ai.md` | [x] Fixed | [ ] | |
| 19 | Build | Approval mode | `build/agent/approval-mode.md` | [x] OK | [ ] | |
| 20 | Build | Worked example | `build/agent/worked-example.md` | [x] Fixed | [ ] | |
| 21 | Build | Build from your AI tool | `build/building-from-your-ai-agent.md` | [x] Fixed | [x] | mcp-server.webp |
| 22 | Build | fastn MCP server | `build/mcp-gateway/README.md` | [x] Fixed | [x] | connect-your-ai-tool.webp |
| 23 | Build | Claude | `build/mcp-gateway/claude.md` | [x] Fixed | [ ] | |
| 24 | Build | Claude Code | `build/mcp-gateway/claude-code.md` | [x] Fixed | [ ] | |
| 25 | Build | ChatGPT | `build/mcp-gateway/chatgpt.md` | [~] Follow-up | [ ] | |
| 26 | Build | Cursor | `build/mcp-gateway/cursor.md` | [x] Fixed | [ ] | |
| 27 | Build | VS Code | `build/mcp-gateway/vscode.md` | [x] Fixed | [ ] | |
| 28 | Build | Codex | `build/mcp-gateway/codex.md` | [x] Fixed | [ ] | |
| 29 | Build | Antigravity | `build/mcp-gateway/antigravity.md` | [x] Fixed | [ ] | |
| 30 | Build | Devin | `build/mcp-gateway/devin.md` | [x] Fixed | [ ] | |
| 31 | Build | Cline | `build/mcp-gateway/cline.md` | [x] Fixed | [ ] | |
| 32 | Build | Lovable | `build/mcp-gateway/lovable.md` | [~] Follow-up | [ ] | |
| 33 | Build | Bolt | `build/mcp-gateway/bolt.md` | [x] Fixed | [ ] | |
| 34 | Build | fastn for AI agents | `reference/ai-agents.md` | [x] Fixed | [ ] | |
| 35 | Build | Connect your product | `manage/saas-connectors.md` | [x] OK | [x] | connect-your-product.webp |
| 36 | Build | Webhooks | `manage/saas-webhooks.md` | [x] OK | [ ] | |
| 37 | Build | Integrations | `build/integrations.md` | [x] Fixed | [x] | create-integration-menu.webp |
| 38 | Build | Connectors | `build/connectors/README.md` | [x] Fixed | [ ] | |
| 39 | Build | Configure a connector | `tutorials/saas-admin/configuring-a-connector.md` | [x] Fixed | [ ] | |
| 40 | Build | The catalog | `build/connectors/the-catalogue.md` | [x] Fixed | [x] | connectors-catalog.webp |
| 41 | Build | Creating a connector | `build/connectors/creating-a-connector.md` | [x] Fixed | [x] | create-connector-menu.webp |
| 42 | Build | Inside a connector | `build/connectors/inside-a-connector.md` | [x] OK | [x] | connector-detail-overview.webp |
| 43 | Build | Auth methods and providers | `build/connectors/auth-methods.md` | [x] OK | [x] | connector-detail-auth.webp |
| 44 | Build | Actions | `build/connectors/action-detail.md` | [x] Fixed | [x] | action-editor.webp |
| 45 | Build | Webhook config | `build/connectors/webhook-config.md` | [x] OK | [ ] | |
| 46 | Build | Editing, publishing and deleting | `build/connectors/editing-and-deleting.md` | [x] OK | [ ] | |
| 47 | Build | Importing and exporting | `build/connectors/importing-and-exporting.md` | [x] OK | [ ] | |
| 48 | Build | Connect an app | `build/connectors/connect-an-app.md` | [x] Fixed | [ ] | |
| 49 | Build | Unified APIs | `build/unified-apis/README.md` | [x] Fixed | [x] | unified-apis.webp |
| 50 | Build | Set up and use | `build/unified-apis/setup-and-usage.md` | [x] Fixed | [ ] | |
| 51 | Build | Inside a category | `build/unified-apis/inside-a-category.md` | [x] OK | [ ] | |
| 52 | Build | Unified vs direct | `build/unified-apis/unified-vs-direct.md` | [x] OK | [ ] | |
| 53 | Build | Workflows | `build/workflows/README.md` | [x] Fixed | [ ] | |
| 54 | Build | The editor | `build/workflows/the-editor.md` | [x] Fixed | [ ] | |
| 55 | Build | Write a workflow in code | `tutorials/saas-admin/configuring-a-workflow-in-code.md` | [x] Fixed | [ ] | |
| 56 | Build | Triggers | `build/triggers/README.md` | [x] OK | [ ] | |
| 57 | Build | Set up triggers | `tutorials/saas-admin/setting-up-triggers.md` | [x] Fixed | [ ] | |
| 58 | Build | Webhook triggers | `build/triggers/webhooks.md` | [x] Fixed | [ ] | |
| 59 | Build | Schedule triggers | `build/triggers/schedulers.md` | [x] Fixed | [ ] | |
| 60 | Build | App event triggers | `build/triggers/app-events.md` | [x] OK | [ ] | |
| 61 | Build | Test and release | `build/workflows/lifecycle.md` | [x] Fixed | [ ] | |
| 62 | Build | Test a workflow | `build/workflows/the-tabs.md` | [x] Fixed | [ ] | |
| 63 | Build | Environments and GitHub | `manage/environments.md` | [x] OK | [x] | settings-environments.webp |
| 64 | Build | Deployment checklist | `tutorials/developer/deployment.md` | [x] OK | [ ] | |
| 65 | Build | Common patterns | `build/patterns.md` | [x] Fixed | [ ] | |
| 66 | Embed | Overview | `embed/README.md` | [x] Fixed | [ ] | |
| 67 | Embed | Widget | `embed/widget-builder/README.md` | [x] OK | [x] | widget-builder.webp |
| 68 | Embed | Build your widget | `tutorials/saas-admin/building-your-widget.md` | [x] Fixed | [ ] | |
| 69 | Embed | Edit integration | `embed/widget-builder/edit-integration.md` | [x] OK | [ ] | |
| 70 | Embed | Layout | `embed/widget-builder/layout.md` | [x] Fixed | [ ] | |
| 71 | Embed | Style | `embed/widget-builder/style.md` | [x] Fixed | [ ] | |
| 72 | Embed | Features | `embed/widget-builder/features.md` | [x] Fixed | [ ] | |
| 73 | Embed | Embed in your product | `embed/embedding/README.md` | [x] Fixed | [x] | widget-embed-tab.webp |
| 74 | Embed | How embedding works | `tutorials/developer/how-embedding-works.md` | [x] Fixed | [ ] | |
| 75 | Embed | Embedding quickstart | `tutorials/developer/embedding-quickstart.md` | [x] Fixed | [ ] | |
| 76 | Embed | Iframe | `embed/embedding/iframe.md` | [x] Fixed | [ ] | |
| 77 | Embed | SDK | `embed/embedding/sdk.md` | [x] OK | [ ] | |
| 78 | Embed | Token API | `embed/embedding/token-api.md` | [x] Fixed | [ ] | |
| 79 | Embed | Generate embed tokens | `tutorials/developer/generating-embed-tokens.md` | [x] Fixed | [ ] | |
| 80 | Embed | Integration flow | `embed/embedding/integration-flow.md` | [x] Fixed | [ ] | |
| 81 | Embed | Customers and tenancy | `tutorials/developer/understanding-tenancy.md` | [x] Fixed | [ ] | |
| 82 | Embed | Customer MCP URL | `embed/embedding/customer-mcp-url.md` | [x] Fixed | [ ] | |
| 83 | Embed | Go-live checklist | `embed/embedding/production-checklist.md` | [x] Fixed | [ ] | |
| 84 | Embed | API keys | `manage/api-keys.md` | [x] Fixed | [x] | api-keys.webp |
| 85 | Embed | Find your org identifier | `tutorials/developer/finding-your-org-identifier.md` | [x] Fixed | [ ] | |
| 86 | Operate | Overview | `operate/overview.md` | [x] Fixed | [ ] | |
| 87 | Operate | Health | `operate/health.md` | [x] Fixed | [x] | health-needs-attention.webp |
| 88 | Operate | Pending updates | `build/connector-updates.md` | [x] OK | [ ] | |
| 89 | Operate | Alerts | `operate/alerts.md` | [x] OK | [ ] | |
| 90 | Operate | Customers | `operate/customers.md` | [x] Fixed | [ ] | |
| 91 | Operate | Manage customers | `tutorials/saas-admin/managing-customers.md` | [x] Fixed | [ ] | |
| 92 | Operate | Connections | `build/connections/README.md` | [x] Fixed | [x] | connections-customers-empty.webp |
| 93 | Operate | Create a connection | `build/connections/creating-a-connection.md` | [x] Fixed | [ ] | |
| 94 | Operate | Inside a connection | `build/connections/inside-a-connection.md` | [x] Fixed | [ ] | |
| 95 | Operate | Statuses | `build/connections/statuses.md` | [x] Fixed | [ ] | |
| 96 | Operate | Auth types | `build/connections/auth-types.md` | [x] OK | [ ] | |
| 97 | Operate | Logs | `operate/README.md` | [x] Fixed | [x] | logs-events-empty.webp |
| 98 | Operate | Events | `operate/events.md` | [x] Fixed | [ ] | |
| 99 | Operate | Executions | `operate/executions.md` | [x] Fixed | [ ] | |
| 100 | Operate | Traces | `operate/traces.md` | [x] Fixed | [ ] | |
| 101 | Operate | Sync reports | `operate/sync-reports.md` | [x] Fixed | [ ] | |
| 102 | Operate | Triggers | `operate/triggers/README.md` | [x] OK | [ ] | |
| 103 | Operate | Using a webhook trigger | `operate/triggers/using-a-webhook-trigger.md` | [x] Fixed | [ ] | |
| 104 | Operate | Troubleshooting | `operate/troubleshooting.md` | [x] Fixed | [ ] | |
| 105 | Operate | Developer troubleshooting | `tutorials/developer/troubleshooting.md` | [x] OK | [ ] | |
| 106 | For your customers | Using integrations in the widget | `tutorials/end-user/README.md` | [x] Fixed | [ ] | |
| 107 | For your customers | Connect apps | `tutorials/end-user/connecting-apps-via-widget.md` | [x] Fixed | [ ] | |
| 108 | For your customers | Customize an integration | `tutorials/end-user/customizing-your-integrations.md` | [x] Fixed | [ ] | |
| 109 | For your customers | Extend a pre-built integration | `tutorials/end-user/extending-a-prebuilt-integration.md` | [x] Fixed | [ ] | |
| 110 | For your customers | Get alerted | `tutorials/end-user/getting-alerted.md` | [x] Fixed | [ ] | |
| 111 | For your customers | View sync status and history | `tutorials/end-user/viewing-sync-status-and-history.md` | [x] Fixed | [ ] | |
| 112 | For your customers | Connect Claude and other AI clients | `tutorials/end-user/connecting-claude.md` | [x] OK | [ ] | |
| 113 | Settings | Settings | `manage/README.md` | [x] Fixed | [ ] | |
| 114 | Settings | People | `manage/people.md` | [x] OK | [ ] | |
| 115 | Settings | Roles | `manage/roles.md` | [x] OK | [x] | settings-roles.webp |
| 116 | Settings | Set up roles and permissions | `tutorials/saas-admin/roles-and-permissions-setup.md` | [x] Fixed | [ ] | |
| 117 | Settings | General | `manage/general.md` | [x] Fixed | [ ] | |
| 118 | Settings | Billing and limits | `manage/billing.md` | [x] Fixed | [x] | settings-billing.webp |
| 119 | Settings | Audit log | `manage/audit-log.md` | [x] OK | [ ] | |
| 120 | Settings | Secrets | `manage/secrets.md` | [x] OK | [x] | settings-secrets.webp |
| 121 | Settings | Configs | `manage/configs.md` | [x] OK | [ ] | |
| 122 | Settings | Database | `manage/database.md` | [x] OK | [ ] | |
| 123 | Settings | Workflow tags | `manage/workflow-tags.md` | [x] Fixed | [ ] | |
| 124 | Settings | Trash | `manage/trash.md` | [x] OK | [ ] | |
| 125 | Settings | Your profile | `manage/profile.md` | [x] OK | [ ] | |
| 126 | Reference | HTTP API | `reference/api.md` | [x] OK | [ ] | |
| 127 | Reference | REST API reference | `reference/rest/README.md` | [~] Follow-up | [ ] | |
| 128 | Reference | Workflows | `reference/rest/workflows.md` | [~] Generated | n/a | Regenerate from OpenAPI v1.15.1 (platform team) |
| 129 | Reference | Installations and configs | `reference/rest/installations.md` | [~] Generated | n/a | Regenerate from OpenAPI v1.15.1 (platform team) |
| 130 | Reference | Widgets and embedding | `reference/rest/widgets.md` | [~] Generated | n/a | Regenerate from OpenAPI v1.15.1 (platform team) |
| 131 | Reference | Triggers and events | `reference/rest/triggers.md` | [~] Generated | n/a | Regenerate from OpenAPI v1.15.1 (platform team) |
| 132 | Reference | Event subscriptions | `reference/rest/event-subscriptions.md` | [~] Generated | n/a | Regenerate from OpenAPI v1.15.1 (platform team) |
| 133 | Reference | Connectors | `reference/rest/connectors.md` | [~] Generated | n/a | Regenerate from OpenAPI v1.15.1 (platform team) |
| 134 | Reference | Connections | `reference/rest/connections.md` | [~] Generated | n/a | Regenerate from OpenAPI v1.15.1 (platform team) |
| 135 | Reference | Unified API | `reference/rest/unified.md` | [~] Generated | n/a | Regenerate from OpenAPI v1.15.1 (platform team) |
| 136 | Reference | Alerts and observability | `reference/rest/observability.md` | [~] Generated | n/a | Regenerate from OpenAPI v1.15.1 (platform team) |
| 137 | Reference | Environments and secrets | `reference/rest/environments.md` | [~] Generated | n/a | Regenerate from OpenAPI v1.15.1 (platform team) |
| 138 | Reference | Organization and access | `reference/rest/organization.md` | [~] Generated | n/a | Regenerate from OpenAPI v1.15.1 (platform team) |
| 139 | Reference | Widget callbacks | `reference/widget-callbacks.md` | [x] OK | [ ] | |
| 140 | Reference | SDK | `reference/sdk/README.md` | [x] OK | [ ] | |
| 141 | Reference | Build an integration, end to end | `reference/sdk/end-to-end.md` | [x] Fixed | [ ] | |
| 142 | Reference | Customers | `reference/sdk/customers.md` | [x] OK | [ ] | Matches @fastn-ai/sdk 0.5.1 |
| 143 | Reference | Connecting apps | `reference/sdk/connecting-apps.md` | [x] OK | [ ] | Matches @fastn-ai/sdk 0.5.1 |
| 144 | Reference | Unified records | `reference/sdk/unified-records.md` | [x] OK | [ ] | Matches @fastn-ai/sdk 0.5.1 |
| 145 | Reference | Calendar and CRM | `reference/sdk/calendar-and-crm.md` | [x] OK | [ ] | Matches @fastn-ai/sdk 0.5.1 |
| 146 | Reference | Direct app actions | `reference/sdk/app-actions.md` | [x] OK | [ ] | Matches @fastn-ai/sdk 0.5.1 |
| 147 | Reference | Events | `reference/sdk/events.md` | [x] OK | [ ] | Matches @fastn-ai/sdk 0.5.1 |
| 148 | Reference | Errors, retries and options | `reference/sdk/errors-and-options.md` | [x] OK | [ ] | Matches @fastn-ai/sdk 0.5.1 |
| 149 | Reference | Workspace tools | `reference/sdk/workspace-tools.md` | [x] Fixed | [ ] | |
| 150 | Reference | Any other operation | `reference/sdk/any-operation.md` | [x] OK | [ ] | Matches @fastn-ai/sdk 0.5.1 |
| 151 | Reference | Code samples | `reference/code-samples.md` | [x] OK | [ ] | |
| 152 | Reference | Workflow runtime API | `reference/workflow-runtime.md` | [x] Fixed | [ ] | |
| 153 | Reference | Errors and failure states | `reference/errors.md` | [x] Fixed | [ ] | |
| 154 | Reference | FAQs | `reference/faqs.md` | [x] Fixed | [ ] | |
| 155 | Reference | Glossary | `reference/glossary.md` | [x] Fixed | [ ] | |
| 156 | Reference | Tutorials | `tutorials/README.md` | [x] Fixed | [ ] | |
| 157 | Reference | Dashboard tutorials | `tutorials/saas-admin/README.md` | [x] Fixed | [ ] | |
| 158 | Reference | Developer | `tutorials/developer/README.md` | [x] Fixed | [ ] | |
