---
description: "Linkly URL shortener and click analytics."
hidden: true
---

# Linkly

<img src="../../.gitbook/assets/connectors/lg/linkly.png" alt="Linkly logo">

Linkly URL shortener and click analytics. Create, update, list and delete branded short links; read click analytics and breakdown counters; manage workspaces, workspace members, custom domains and click webhooks.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [linklyhq.com](https://linklyhq.com) |
| **Authentication** | API key |
| **Slug** | `linkly` |

## Use it

Add Linkly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.linkly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Workspace Domain | `addWorkspaceDomain` | Adds a custom branded domain to a Linkly workspace. The domain must already resolve to Linkly via DNS; Linkly validates it at creation time and returns 400 with an explanatory error such as 'Exists but isn't pointing to Linkly.' when it does not. Free workspaces are limited to one domain. |
| Create Link Webhook | `createLinkWebhook` | Subscribes a webhook endpoint to a single short link, so only that link's events are delivered. Linkly sends all four event types (click, link.created, link.updated, link.deleted) and silently ignores any 'events' field. The response 'id' is the endpoint URL itself. |
| Create Workspace | `createWorkspace` | Creates a new Linkly workspace owned by the API key holder and returns its id and name. Note that Linkly exposes no API route to rename or delete a workspace; the only API-side teardown is Remove Workspace User, which removes the workspace once its last member is removed. |
| Create Workspace Webhook | `createWorkspaceWebhook` | Subscribes a webhook endpoint to every link in a workspace. Linkly delivers all four events to it (click, link.created, link.updated, link.deleted); there is no way to subscribe to a subset, and an 'events' field in the request is silently ignored. The response 'id' is the endpoint URL itself. Re-posting the same URL is idempotent. |
| Delete Link | `deleteLink` | Deletes a short link from a workspace by id. Returns 404 with {"error":"Link not found","code":"not_found"} when the link does not exist in that workspace. After deletion the link stops redirecting and disappears from List Links. |
| Delete Link Webhook | `deleteLinkWebhook` | Unsubscribes a webhook endpoint from a single short link. Linkly identifies a webhook by its own URL, so pass the endpoint URL exactly as List Link Webhooks returns it (for example https://example.com/hook); it is percent-encoded into the path automatically. Linkly answers 200 with an empty body whether or not anything matched, so confirm removal with List Link Webhooks. |
| Delete Workspace Domain | `deleteWorkspaceDomain` | Removes a custom branded domain from a Linkly workspace by domain id. Returns 400 with {"error":"Domain not found"} when the id does not belong to the workspace. |
| Delete Workspace Webhook | `deleteWorkspaceWebhook` | Unsubscribes a workspace webhook endpoint. Linkly identifies a webhook by its own URL, so pass the endpoint URL exactly as List Workspace Webhooks returns it (for example https://example.com/hook); it is percent-encoded into the path automatically. Linkly answers 200 with an empty body whether or not anything matched, so confirm removal with List Workspace Webhooks. |
| Get Click Analytics | `getClickAnalytics` | Returns click analytics for a workspace as a time series. Without a pivot Linkly returns {"traffic":[{"t":date,"y":clicks}]}; with pivot=link_id it returns {"data":[{"date","clicks":{link_id:count}}],"links":[...]} so each link can be charted separately. Filter by link, date range, country, platform, referer or ISP, exclude or include bots, count unique visitors only, and choose JSON or CSV output. |
| Get Click Counter | `getClickCounter` | Returns a click breakdown for a workspace grouped by one dimension, as a total plus a list of values with their click counts. Supply start and end: without an explicit window this route reports total 0 even when clicks exist. Linkly accepts only these counter names and answers 400 {"error":"Invalid counter"} for anything else: country, city, region, platform, referer, isp, link_id, utm_source, utm_medium, utm_campaign, utm_term, utm_content. |
| Get Current User | `getCurrentUser` | Returns the Linkly user account that owns the API key, including id, name, email, language and account attribution. Useful as a connection health check because it needs no inputs. |
| Get Link | `getLink` | Retrieves a single short link by id. The workspace_id query parameter is mandatory; omitting it returns 400 with code 'workspace_required'. |
| Get Workspace | `getWorkspace` | Retrieves one Linkly workspace by id, including its plan usage counters, enabled feature flags, configured webhook endpoints, link and domain counts, and onboarding state. |
| List Domains | `listDomains` | Lists custom branded domains for a workspace addressed by the workspace_id query parameter. Linkly returns a bare JSON array here; it is surfaced under 'items'. Omitting workspace_id returns 400 with code 'workspace_required'. |
| List Link Webhooks | `listLinkWebhooks` | Lists the webhook endpoints subscribed to a single short link. Each entry's 'id' is the endpoint URL itself. Linkly returns a bare JSON array here; it is surfaced under 'items'. Link-level and workspace-level subscriptions are independent and can both be present. |
| List Links | `listLinks` | Lists the short links in a workspace with pagination metadata and per-link click counters (today, previous day, thirty days, total, plus human-only variants). Supports a free-text search over link name and destination URL. This is the richer of the two link listings; use List Workspace Links for the plain link records. |
| List Workspace Domains | `listWorkspaceDomains` | Lists the custom branded domains configured on a Linkly workspace, returned under a 'domains' key. Use List Domains for the equivalent flat listing addressed by query parameter. |
| List Workspace Links | `listWorkspaceLinks` | Returns every short link in a workspace as a plain JSON array of link records, without pagination metadata or click counters. Use List Links instead when you need paging, search or click totals. Linkly returns a bare JSON array here; it is surfaced under 'items'. |
| List Workspace Users | `listWorkspaceUsers` | Lists the members of a Linkly workspace. Each row carries the workspace membership id (needed by Remove Workspace User) alongside the underlying user record and that member's monthly report preference. |
| List Workspace Webhooks | `listWorkspaceWebhooks` | Lists the webhook endpoints subscribed at the workspace level. Each entry's 'id' is the endpoint URL itself, which is what Delete Workspace Webhook expects. Linkly returns a bare JSON array here; it is surfaced under 'items'. Every workspace endpoint receives all four Linkly events (click, link.created, link.updated, link.deleted); Get Workspace shows that event list per endpoint. |
| List Workspaces | `listWorkspaces` | Lists every Linkly workspace the API key can access, returning each workspace id and name. Call this first to obtain the workspace_id required by most other Linkly actions. |
| Remove Workspace User | `removeWorkspaceUser` | Removes a member from a Linkly workspace by workspace membership id (the 'id' field from List Workspace Users, not the underlying user id). Removing the last remaining member also removes the workspace itself, which is the only API-side way to tear down a workspace created by Create Workspace. |
| Save Link | `saveLink` | Creates a short link, or updates an existing one when 'id' is supplied. Returns the full link record including its generated short URL in 'full_url'. Fields belonging to paid Linkly features (UTM and Open Graph overrides, link expiry, cloaking, public analytics, tracking pixels, HTML injection, app deep links, custom slugs) are silently ignored on plans where the matching flag in the workspace 'features' map is false; call Get Workspace to see which are enabled. |
| Save Links Bulk | `saveLinksBulk` | Creates or updates many short links in one request. Linkly requires a bare JSON array as the request body here, so pass the array serialized as a string in links_json. Each entry accepts the same fields as Save Link; an entry with 'id' updates that link, one without creates a new link. Returns one result per entry with its index, status and the resulting link record. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Link Clicked | `click` | Fires every time a Linkly short link in the subscribed workspace is visited. The payload carries the full link configuration plus the click's request metadata: geo (country, is_eu_country, city, region, isp), browser_name, platform, referer, user_agent, accept_language, bot_name (null for humans), the resolved destination and any forwarded query params. Payload schema modelled from Linkly's documented sample at linklyhq.com/support/webhooks, not from a captured delivery. |
| Link Created | `link.created` | Fires when a new short link is created in the subscribed workspace, by the API or in the Linkly UI. Payload schema modelled from Linkly's documented sample at linklyhq.com/support/webhooks, not from a captured delivery. |
| Link Deleted | `link.deleted` | Fires when a short link is deleted from the subscribed workspace. Payload schema modelled from Linkly's documented sample at linklyhq.com/support/webhooks, not from a captured delivery. |
| Link Updated | `link.updated` | Fires when an existing short link in the subscribed workspace is modified, including changes made through Save Link or Save Links Bulk. Payload schema modelled from Linkly's documented sample at linklyhq.com/support/webhooks, not from a captured delivery. |
