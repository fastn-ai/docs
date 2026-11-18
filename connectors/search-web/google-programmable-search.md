---
description: "Google Programmable Search (Custom Search JSON API) — run web and image queries against a Programmable Search Engine and read the ranked results with their…"
hidden: true
---

# Google Programmable Search

<img src="../../.gitbook/assets/connectors/google-programmable-search.png" alt="Google Programmable Search logo" width="64">

Google Programmable Search (Custom Search JSON API) — run web and image queries against a Programmable Search Engine and read the ranked results with their titles, snippets and links.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [programmablesearchengine.google.com](https://programmablesearchengine.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleProgrammableSearch` |

## Use it

Add Google Programmable Search from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleProgrammableSearch.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Search | `search` | Runs a query against a Programmable Search Engine and returns ranked results with title, snippet, display link and full link. |
| Search Site Restricted | `searchSiteRestricted` | Same as Search but against an engine configured to cover only specific sites; it has no daily query limit. |
