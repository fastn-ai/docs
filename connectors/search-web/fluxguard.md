---
description: "Fluxguard is an AI-powered website change monitoring service."
---

# Fluxguard

Fluxguard is an AI-powered website change monitoring service. This connector covers the Fluxguard REST API: account details, adding pages to monitor, initiating crawls, reading page and session data, site and page deletion, site categories, and webhook endpoints that receive change notifications with links to captured HTML, screenshots and diffs.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [fluxguard.com](https://fluxguard.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 14 |
| **Events** | 1 |
| **Slug** | `fluxguard` |

## Use it

Add Fluxguard from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fluxguard.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Page | `addPage` | Adds a new page URL to Fluxguard monitoring. When no site and session are given, a new site and session are created for the page and the optional category and nickname settings apply; when siteId and sessionId are given the page is added to that existing session. Returns the site, session and page identifiers. |
| Create Category | `createCategory` | Creates a new site category with the given name. Sites can be placed in categories when they are added with Add Page. Returns the new category's ID and creation time. |
| Create Webhook | `createWebhook` | Registers a webhook endpoint URL that Fluxguard will POST change notifications to whenever a monitored page changes. Returns the ID of the new webhook; the signing secret is available from List Webhooks. |
| Delete Category | `deleteCategory` | Deletes a category by its ID. Responds with HTTP 204 and no body. This route is not listed in the public API guide but is live on the Fluxguard API. |
| Delete Page | `deletePage` | Deletes a single monitored page, identified by its site, session and page IDs, together with all of its captured versions. Responds with HTTP 204 and no body. |
| Delete Site | `deleteSite` | Deletes a monitored site by its ID, together with all of its sessions, pages and captured versions. Responds with HTTP 204 and no body. |
| Delete Webhook | `deleteWebhook` | Removes a registered webhook endpoint by its ID so Fluxguard stops sending change notifications to it. Responds with HTTP 204 and no body. |
| Get Account | `getAccount` | Retrieves your Fluxguard organization's account attributes, including plan, remaining credits, status, notification gap, site count and the configured change flags. |
| Get Page | `getPage` | Retrieves the monitoring data for a single page identified by its site, session and page IDs, including its URL, path and captured version information. |
| Get Sample Webhook | `getSampleWebhook` | Returns a sample webhook payload built from your account's data (or generic sample data on a new account) so you can see exactly what Fluxguard sends when a page change is detected. |
| Get Session | `getSession` | Retrieves a monitoring session identified by its site and session IDs, including its settings and pages. When the session does not exist Fluxguard responds with HTTP 200 and an error field. |
| Initiate Crawl | `initiateCrawl` | Starts a crawl of every page in a monitoring session, identified by its site and session IDs. Each crawl consumes account credits and produces a new captured version of the pages. |
| List Categories | `listCategories` | Returns all site and page categories in your Fluxguard organization as an object keyed by category ID, with each category's name, type and timestamps. |
| List Webhooks | `listWebhooks` | Lists every webhook endpoint registered on your Fluxguard organization, with each webhook's URL, signing secret, API version and creation time. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Page Changed | `page.changed` | Fired whenever Fluxguard detects a change on a monitored page. Fluxguard delivers a JSON array of change objects (one per changed page) with the captured version, AI flag and summaries, and links to captured HTML, screenshots, text and diff files under fileBaseUrl. Fluxguard has a single webhook event type; every registered endpoint receives all change activity for the organization. Payload modelled from Fluxguard's documented webhook body and its GET /account/webhook/sample endpoint. |
