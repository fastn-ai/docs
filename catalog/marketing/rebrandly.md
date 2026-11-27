---
description: "Rebrandly manages branded short links. Create links, attach tags and scripts, and count links, domains and tags."
hidden: true
---

# Rebrandly

<img src="../../.gitbook/assets/connectors/lg/rebrandly.png" alt="Rebrandly logo">

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [rebrandly.com](https://rebrandly.com) |
| **Authentication** | API key |
| **Slug** | `rebrandly` |

## Setup

Your customers enter their API key for Rebrandly when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Rebrandly from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Rebrandly**.
2. Select **Connect** on the Rebrandly card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Rebrandly's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Attach Script to Link</td><td><code>attachScriptToLink</code></td><td>Attaches an existing custom script to a branded short link, so the script runs on redirect. Not included on the free plan.</td></tr><tr><td>Attach Tag to Link</td><td><code>attachTagToLink</code></td><td>Attaches an existing tag to a branded short link.</td></tr><tr><td>Bulk Delete Links</td><td><code>bulkDeleteLinks</code></td><td>Deletes multiple branded short links in a single request, up to 25 link IDs at a time.</td></tr><tr><td>Count Domains</td><td><code>countDomains</code></td><td>Returns the number of branded domains matching the given filters, without returning the domain records themselves.</td></tr><tr><td>Count Links</td><td><code>countLinks</code></td><td>Returns the number of branded short links matching the given filters, without returning the link records themselves.</td></tr><tr><td>Count Scripts</td><td><code>countScripts</code></td><td>Returns the total number of custom scripts in a workspace.</td></tr><tr><td>Count Tags</td><td><code>countTags</code></td><td>Returns the total number of tags in a workspace.</td></tr><tr><td>Create Express Link</td><td><code>createExpressLink</code></td><td>Quickly creates a branded short link using a single GET request with query-string parameters instead of a JSON body. Useful for one-off link creation from a browser or simple integration. Counts against the account's per-cycle link quota, same as Create Link.</td></tr><tr><td>Create Link</td><td><code>createLink</code></td><td>Creates a new branded short link pointing to a destination URL, optionally with a custom slashtag, title, and branded domain. Counts against the account's per-cycle link quota.</td></tr><tr><td>Create Script</td><td><code>createScript</code></td><td>Creates a new custom JavaScript script that can be attached to branded short links to run tracking or redirect code. Counts against the account's script quota, which is 0 on the Free plan.</td></tr></tbody></table>

<details>

<summary>View 22 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Tag</td><td><code>createTag</code></td><td>Creates a new tag that can be attached to branded short links for categorization. Counts against the account's tag quota.</td></tr><tr><td>Delete Link</td><td><code>deleteLink</code></td><td>Permanently deletes a single branded short link by its unique ID. This does not free up the account's per-cycle link quota - deleted links still count toward the cycle total.</td></tr><tr><td>Delete Script</td><td><code>deleteScript</code></td><td>Permanently deletes a custom script by its unique ID. Not included on the free plan.</td></tr><tr><td>Delete Tag</td><td><code>deleteTag</code></td><td>Permanently deletes a tag by its unique ID. The tag is also removed from any links it was attached to.</td></tr><tr><td>Detach Script from Link</td><td><code>detachScriptFromLink</code></td><td>Removes a custom script from a branded short link. The script itself is not deleted. Not included on the free plan.</td></tr><tr><td>Detach Tag from Link</td><td><code>detachTagFromLink</code></td><td>Removes a tag from a branded short link. The tag itself is not deleted.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Retrieves details about the authenticated Rebrandly account, including the account holder's name, email, and subscription plan limits (links, domains, workspaces, teammates, tags, and scripts used vs. max).</td></tr><tr><td>Get Account Click Statistics</td><td><code>getAccountClicks</code></td><td>Retrieves a time-series of click counts across the whole account, grouped by hour, day, or month. Requires the account's 'metrics.advanced' feature flag; accounts without it (including the free plan) receive a 403.</td></tr><tr><td>Get Domain</td><td><code>getDomain</code></td><td>Retrieves details for a single branded domain by its unique ID.</td></tr><tr><td>Get Link</td><td><code>getLink</code></td><td>Retrieves full details for a single branded short link by its unique ID, including its destination, status, tags, and click count.</td></tr><tr><td>Get Script</td><td><code>getScript</code></td><td>Retrieves details for a single custom script by its unique ID. Not included on the free plan.</td></tr><tr><td>Get Tag</td><td><code>getTag</code></td><td>Retrieves details for a single tag by its unique ID.</td></tr><tr><td>List Domains</td><td><code>listDomains</code></td><td>Lists the branded domains available in a workspace, including Rebrandly's own shared domains (e.g. rebrand.ly) and any custom domains the account owns. Supports filtering by active status and pagination.</td></tr><tr><td>List Link Scripts</td><td><code>listLinkScripts</code></td><td>Lists the custom scripts currently attached to a specific branded short link.</td></tr><tr><td>List Link Tags</td><td><code>listLinkTags</code></td><td>Lists the tags currently attached to a specific branded short link.</td></tr><tr><td>List Links</td><td><code>listLinks</code></td><td>Lists branded short links, with optional filters by domain, slashtag, creator, and creation date range, plus sorting and pagination.</td></tr><tr><td>List Scripts</td><td><code>listScripts</code></td><td>Lists the custom JavaScript tracking/redirect scripts defined in a workspace. Scripts can be attached to branded short links to run custom code on redirect. Not included on the free plan (0 script quota).</td></tr><tr><td>List Tags</td><td><code>listTags</code></td><td>Lists the tags defined in a workspace, used to categorize and organize branded short links.</td></tr><tr><td>List Workspaces</td><td><code>listWorkspaces</code></td><td>Lists the workspaces the authenticated account belongs to, including the account's own workspace and any shared workspaces, with role and subscription details for each.</td></tr><tr><td>Update Link</td><td><code>updateLink</code></td><td>Updates the destination URL and/or title of an existing branded short link. The link's domain and slashtag cannot be changed after creation; create a new link instead.</td></tr><tr><td>Update Script</td><td><code>updateScript</code></td><td>Updates the name and/or JavaScript value of an existing script. Not included on the free plan.</td></tr><tr><td>Update Tag</td><td><code>updateTag</code></td><td>Updates the name and/or color of an existing tag.</td></tr></tbody></table>

</details>

