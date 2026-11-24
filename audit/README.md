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

## Open decisions

* **"operator" vs the Operator role.** Settings → Roles has a built-in role named **Operator**. The docs also say "operator" for the person on your team who sets up integrations, about 46 times. The glossary notes the difference for now.
* **Demo data for screenshots.** Customers, connections, workflows, logs and the fastn agent are shown in their empty state, or not at all. Shots with data need a test customer and a sample workflow in a demo org.

## Follow-ups outside the docs

* Product copy says both "maintenance agent" (6 places) and "maintainer agent" (9). Billing says "sandbox tenant". Connections labels say "system" ("Connect a system", "Search systems").
* The code-editing-off banner still says "the AI builder".
* The Long tier timeout is 36 h in the UI and 48 h in the backend.
* ChatGPT and Lovable setup steps in the dashboard disagree with their docs pages. Check them in the live tools.
* Regenerate the REST reference from v1.15.1 and add the new routes (widget deploy, promote and translations, sync jobs, connector update proposals, environment guardrails).

## Competitor takeaways worth doing next

* Keep the core nouns. Customer, connector, connection, workflow and trigger match Prismatic and Workato.
* Add a "Which MCP do I need?" box wherever fastn Connect and the fastn MCP server both appear.
* Publish an architecture reference page covering the whole flow: API key → embed token → widget → connection → run → MCP (Merge has one).
* Add a hosted widget demo and a "Where to start, by task" index (Paragon and Prismatic have these).
* Add "For agents" notes to quickstart steps, with a prompt developers can copy (Nango does this).
