---
description: "Rebrandly is a branded link management platform for creating, organizing, and analyzing custom short links, QR codes, tags, and scripts across domains and…"
---

# Rebrandly

Rebrandly is a branded link management platform for creating, organizing, and analyzing custom short links, QR codes, tags, and scripts across domains and workspaces.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [rebrandly.com](https://rebrandly.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 32 |
| **Events** | 0 |
| **Slug** | `rebrandly` |

## Use it

Add Rebrandly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rebrandly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Attach Script to Link | `attachScriptToLink` | Attaches an existing custom script to a branded short link, so the script runs on redirect. Not included on the free plan. |
| Attach Tag to Link | `attachTagToLink` | Attaches an existing tag to a branded short link. |
| Bulk Delete Links | `bulkDeleteLinks` | Deletes multiple branded short links in a single request, up to 25 link IDs at a time. |
| Count Domains | `countDomains` | Returns the number of branded domains matching the given filters, without returning the domain records themselves. |
| Count Links | `countLinks` | Returns the number of branded short links matching the given filters, without returning the link records themselves. |
| Count Scripts | `countScripts` | Returns the total number of custom scripts in a workspace. |
| Count Tags | `countTags` | Returns the total number of tags in a workspace. |
| Create Express Link | `createExpressLink` | Quickly creates a branded short link using a single GET request with query-string parameters instead of a JSON body. Useful for one-off link creation from a browser or simple integration. Counts against the account's per-cycle link quota, same as Create Link. |
| Create Link | `createLink` | Creates a new branded short link pointing to a destination URL, optionally with a custom slashtag, title, and branded domain. Counts against the account's per-cycle link quota. |
| Create Script | `createScript` | Creates a new custom JavaScript script that can be attached to branded short links to run tracking or redirect code. Counts against the account's script quota, which is 0 on the Free plan. |
| Create Tag | `createTag` | Creates a new tag that can be attached to branded short links for categorization. Counts against the account's tag quota. |
| Delete Link | `deleteLink` | Permanently deletes a single branded short link by its unique ID. This does not free up the account's per-cycle link quota - deleted links still count toward the cycle total. |
| Delete Script | `deleteScript` | Permanently deletes a custom script by its unique ID. Not included on the free plan. |
| Delete Tag | `deleteTag` | Permanently deletes a tag by its unique ID. The tag is also removed from any links it was attached to. |
| Detach Script from Link | `detachScriptFromLink` | Removes a custom script from a branded short link. The script itself is not deleted. Not included on the free plan. |
| Detach Tag from Link | `detachTagFromLink` | Removes a tag from a branded short link. The tag itself is not deleted. |
| Get Account | `getAccount` | Retrieves details about the authenticated Rebrandly account, including the account holder's name, email, and subscription plan limits (links, domains, workspaces, teammates, tags, and scripts used vs. max). |
| Get Account Click Statistics | `getAccountClicks` | Retrieves a time-series of click counts across the whole account, grouped by hour, day, or month. Requires the account's 'metrics.advanced' feature flag; accounts without it (including the free plan) receive a 403. |
| Get Domain | `getDomain` | Retrieves details for a single branded domain by its unique ID. |
| Get Link | `getLink` | Retrieves full details for a single branded short link by its unique ID, including its destination, status, tags, and click count. |
| Get Script | `getScript` | Retrieves details for a single custom script by its unique ID. Not included on the free plan. |
| Get Tag | `getTag` | Retrieves details for a single tag by its unique ID. |
| List Domains | `listDomains` | Lists the branded domains available in a workspace, including Rebrandly's own shared domains (e.g. rebrand.ly) and any custom domains the account owns. Supports filtering by active status and pagination. |
| List Link Scripts | `listLinkScripts` | Lists the custom scripts currently attached to a specific branded short link. |
| List Link Tags | `listLinkTags` | Lists the tags currently attached to a specific branded short link. |
| List Links | `listLinks` | Lists branded short links, with optional filters by domain, slashtag, creator, and creation date range, plus sorting and pagination. |
| List Scripts | `listScripts` | Lists the custom JavaScript tracking/redirect scripts defined in a workspace. Scripts can be attached to branded short links to run custom code on redirect. Not included on the free plan (0 script quota). |
| List Tags | `listTags` | Lists the tags defined in a workspace, used to categorize and organize branded short links. |
| List Workspaces | `listWorkspaces` | Lists the workspaces the authenticated account belongs to, including the account's own workspace and any shared workspaces, with role and subscription details for each. |
| Update Link | `updateLink` | Updates the destination URL and/or title of an existing branded short link. The link's domain and slashtag cannot be changed after creation; create a new link instead. |
| Update Script | `updateScript` | Updates the name and/or JavaScript value of an existing script. Not included on the free plan. |
| Update Tag | `updateTag` | Updates the name and/or color of an existing tag. |
