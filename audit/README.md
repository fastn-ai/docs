# Docs audit, 24 Nov 2026 (unpublished)

This pass covered all 158 pages in SUMMARY.md, checked against fastn-platform main and the live dashboard. Page-by-page status is in [TRACKER.md](../TRACKER.md).

## Files here

| File | What it holds |
| --- | --- |
| [A1-findings.md](A1-findings.md) | Get started, How-to guides, Embed (35 pages) |
| [A2-findings.md](A2-findings.md) | Build (50 pages) |
| [A3-findings.md](A3-findings.md) | Operate, For your customers, Settings (40 pages) |
| [A4-findings.md](A4-findings.md) | Reference, the glossary, and a repo-wide count of old terms (33 pages) |
| [competitors.md](competitors.md) | Terminology and docs structure compared with Paragon, Merge, Nango, Prismatic, Ampersand, Composio, Pipedream Connect, Workato Embedded and Arcade |
| [undocumented-endpoints.txt](undocumented-endpoints.txt) | Platform operations missing from the REST reference (generated from v1.12.0; latest is v1.15.1) |

## Result

* 96 pages fixed, 48 already correct, 3 need a check in a live third-party tool, and 11 generated REST pages need regeneration.
* [reference/glossary.md](../reference/glossary.md) is the one canonical term list, with the old names each term replaces.
* 25 screenshots taken from the live dashboard in dark mode, saved in `.gitbook/assets/screens/` and placed on 23 pages.

## Terminology decisions applied

| Use | Instead of |
| --- | --- |
| fastn agent, **Build with fastn agent** | Build with AI, AI builder |
| fastn MCP server (`mcp.fastn.dev/fastn-workspace`) | MCP gateway, for the address your AI tool connects to |
| fastn Connect, the MCP gateway | fastn MCP gateway |
| Operate → Logs (Events, Executions, Sync reports, Monitoring) | Activity; Traces as a tab |
| Pick your integrations, Set up and add the widget, Your first customer connects | Choose integrations, Embed the widget, Customers connect and customize |
| customer | tenant, end customer (identifiers such as `tenantRef` stay) |
| Scale or Enterprise | Growth, Pro |

## Round 2 (same day)

* **"operator":** in prose the person is now **your team**. **Operator** only names the built-in role. The diagrams were regenerated to match.
* **Demo data:** a test customer, Northwind Traders, is in the personal demo org. 9 more screenshots cover the customer list, create and detail pages, the new-workflow editor, Health Alerts and Pending updates, Logs Executions and Sync reports, and Settings General. Personal names and emails were replaced on screen before capture.
* **ChatGPT, Lovable, GitHub Copilot:** checked against OpenAI's and Lovable's current docs. The docs pages were right and the dashboard's setup copy is out of date. A GitHub Copilot page was added.
* **REST reference:** regenerated from v1.15.1: 470 operations (was 404) and a new Sync jobs page. The generator allowlist change (`scripts/docs-rest-reference`) belongs to the platform team; until it lands there, the next regeneration drops the new operations.
* **Architecture:** a new [Architecture](../getting-started/architecture.md) page with a diagram of every part, four request flows and a "Which MCP do I need?" table. The same box is on the fastn MCP server and Core concepts pages.

## Still open (outside the docs)

* **Product copy, for the platform team:**
  * "maintenance agent" vs "maintainer agent".
  * "sandbox tenant" on Billing.
  * "system" labels on Connections ("Connect a system", "Search systems").
  * "the AI builder" in the code-editing banner.
  * "Which system?" on Request connector.
  * Long tier 36 h in the UI vs 48 h in the backend.
  * The ChatGPT and Lovable setup steps in `apps/dashboard/src/lib/mcp.ts` and `pages/onboarding/ai-tools.ts`.
* **Screenshots that need a paid plan or real runs:** the fastn agent, a populated workflows list, and events and executions with data. The demo org is on Launch with code editing off, so it can't build or run a workflow.
* **Hosted widget demo:** there is no public demo environment to link yet.
