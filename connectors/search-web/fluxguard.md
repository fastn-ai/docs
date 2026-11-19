---
description: "Fluxguard is an AI-powered website change monitoring service."
hidden: true
---

# Fluxguard

<img src="../../.gitbook/assets/connectors/lg/fluxguard.png" alt="Fluxguard logo">

This connector covers the Fluxguard REST API: account details, adding pages to monitor, initiating crawls, reading page and session data, site and page deletion, site categories, and webhook endpoints that receive change notifications with links to captured HTML, screenshots and diffs.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [fluxguard.com](https://fluxguard.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `fluxguard` |

## Use it

Add Fluxguard from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fluxguard.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Page</td><td><code>addPage</code></td><td>Adds a new page URL to Fluxguard monitoring. When no site and session are given, a new site and session are created for the page and the optional category and nickname settings apply; when siteId and sessionId are given the page is added to that existing session. Returns the site, session and page identifiers.</td></tr><tr><td>Create Category</td><td><code>createCategory</code></td><td>Creates a new site category with the given name. Sites can be placed in categories when they are added with Add Page. Returns the new category's ID and creation time.</td></tr><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Registers a webhook endpoint URL that Fluxguard will POST change notifications to whenever a monitored page changes. Returns the ID of the new webhook; the signing secret is available from List Webhooks.</td></tr><tr><td>Delete Category</td><td><code>deleteCategory</code></td><td>Deletes a category by its ID. Responds with HTTP 204 and no body. This route is not listed in the public API guide but is live on the Fluxguard API.</td></tr><tr><td>Delete Page</td><td><code>deletePage</code></td><td>Deletes a single monitored page, identified by its site, session and page IDs, together with all of its captured versions. Responds with HTTP 204 and no body.</td></tr><tr><td>Delete Site</td><td><code>deleteSite</code></td><td>Deletes a monitored site by its ID, together with all of its sessions, pages and captured versions. Responds with HTTP 204 and no body.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Removes a registered webhook endpoint by its ID so Fluxguard stops sending change notifications to it. Responds with HTTP 204 and no body.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Retrieves your Fluxguard organization's account attributes, including plan, remaining credits, status, notification gap, site count and the configured change flags.</td></tr><tr><td>Get Page</td><td><code>getPage</code></td><td>Retrieves the monitoring data for a single page identified by its site, session and page IDs, including its URL, path and captured version information.</td></tr><tr><td>Get Sample Webhook</td><td><code>getSampleWebhook</code></td><td>Returns a sample webhook payload built from your account's data (or generic sample data on a new account) so you can see exactly what Fluxguard sends when a page change is detected.</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Session</td><td><code>getSession</code></td><td>Retrieves a monitoring session identified by its site and session IDs, including its settings and pages. When the session does not exist Fluxguard responds with HTTP 200 and an error field.</td></tr><tr><td>Initiate Crawl</td><td><code>initiateCrawl</code></td><td>Starts a crawl of every page in a monitoring session, identified by its site and session IDs. Each crawl consumes account credits and produces a new captured version of the pages.</td></tr><tr><td>List Categories</td><td><code>listCategories</code></td><td>Returns all site and page categories in your Fluxguard organization as an object keyed by category ID, with each category's name, type and timestamps.</td></tr><tr><td>List Webhooks</td><td><code>listWebhooks</code></td><td>Lists every webhook endpoint registered on your Fluxguard organization, with each webhook's URL, signing secret, API version and creation time.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Page Changed</td><td><code>page.changed</code></td><td>Fired whenever Fluxguard detects a change on a monitored page. Fluxguard delivers a JSON array of change objects (one per changed page) with the captured version, AI flag and summaries, and links to captured HTML, screenshots, text and diff files under fileBaseUrl. Fluxguard has a single webhook event type; every registered endpoint receives all change activity for the organization. Payload modelled from Fluxguard's documented webhook body and its GET /account/webhook/sample endpoint.</td></tr></tbody></table>
