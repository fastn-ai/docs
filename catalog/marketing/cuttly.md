---
description: "Cutt.ly shortens links. Create and edit short links, add tags, run split tests and read link statistics."
hidden: true
---

# Cutt.ly

<img src="../../.gitbook/assets/connectors/lg/cuttly.png" alt="Cutt.ly logo">

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [cutt.ly](https://cutt.ly) |
| **Authentication** | API key |
| **Slug** | `cuttly` |

## Setup

Your customers enter their API key for Cutt.ly when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Cutt.ly from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Cutt.ly**.
2. Select **Connect** on the Cutt.ly card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Cutt.ly's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Tag To Link</td><td><code>addTagToLink</code></td><td>Add a TAG to an existing Cutt.ly short link you own, for grouping links in Cuttly Campaigns and aggregated analytics. Returns status 1 when saved, 2 if it could not be saved, or 3 if the link does not exist or you do not own it.</td></tr><tr><td>Change Link Alias</td><td><code>changeLinkAlias</code></td><td>Rename an existing Cutt.ly short link to a new alias, changing the short URL itself. The new alias must not already be taken, otherwise the API returns a 'Provided alias is unavailable' error. Returns status 1 when saved, 2 if it could not be saved, or 3 if the link does not exist or you do not own it.</td></tr><tr><td>Change Link Destination</td><td><code>changeLinkDestination</code></td><td>Repoint an existing Cutt.ly short link at a different destination URL, keeping the same short link. Returns status 1 when saved, 2 if it could not be saved, 3 if the link does not exist or you do not own it, or 4 if the new destination URL failed validation.</td></tr><tr><td>Change Link Title</td><td><code>changeLinkTitle</code></td><td>Change the stored title of an existing Cutt.ly short link. The title is what appears alongside the link in the Cutt.ly dashboard and in analytics responses. Returns status 1 when saved, 2 if it could not be saved, or 3 if the link does not exist or you do not own it.</td></tr><tr><td>Configure Split Test</td><td><code>configureSplitTest</code></td><td>Configure an A/B or A/B/C split test on a Cutt.ly short link, splitting incoming traffic between the link's own destination and one or two variation URLs. Pass abtest 1 for an A/B test, 2 for an A/B/C test, or 0 to remove the test. The B and C percentages must each be 0-100 and together must not exceed 100. Returns status 1 when saved, or 3 if the link does not exist or you do not own it.</td></tr><tr><td>Delete Link</td><td><code>deleteLink</code></td><td>Permanently delete a Cutt.ly short link you own, together with its click statistics. The short URL stops resolving immediately and this cannot be undone. Returns status 1 when the link was deleted, 2 if it could not be saved, or 3 if the link does not exist or you do not own it.</td></tr><tr><td>Get Link Statistics</td><td><code>getLinkStatistics</code></td><td>Retrieve click analytics for one Cutt.ly short link: total clicks, creation date, page title, destination URL, per-network social shares (facebook, twitter, pinterest, instagram, linkedin), and click breakdowns by device and referrer. stats.status is 1 when the link was found. Fields such as bots require a higher subscription plan and are returned as the string 'Insufficient subscription level' on lower plans.</td></tr><tr><td>Get Link Statistics For Date Range</td><td><code>getLinkStatisticsForDateRange</code></td><td>Retrieve click analytics for a Cutt.ly short link restricted to a date window. Supply date_from, date_to, or both. Requires a Team subscription plan or higher; lower plans receive a 401 'Insufficient subscription level' response. Dates must be formatted YYYY-MM-DD or the API returns an incorrect-date-format error.</td></tr><tr><td>Set Link Expiration</td><td><code>setLinkExpiration</code></td><td>Set an expiration rule on a Cutt.ly short link, either by calendar date or after a number of clicks, and optionally send visitors to a fallback URL once it expires. Pass expireCond 0 to remove an existing expiration rule. Returns status 1 when saved, or 3 if the link does not exist or you do not own it.</td></tr><tr><td>Set Link Password</td><td><code>setLinkPassword</code></td><td>Protect a Cutt.ly short link with a password, so visitors must enter it before being redirected. Send an empty password to remove the protection. Returns status 1 when saved, 2 if it could not be saved, or 3 if the link does not exist or you do not own it.</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Set Mobile Redirect</td><td><code>setMobileRedirect</code></td><td>Set an operating-system-specific redirect on a Cutt.ly short link, so visitors on Android, iOS or Windows Mobile are sent to a different destination than desktop visitors. The mobile parameter is case sensitive. Omit destination to remove the redirect already configured for that option. Returns status 1 when saved, 3 if the link does not exist or you do not own it, or 4 if the destination URL failed validation.</td></tr><tr><td>Set Unique Click Counting</td><td><code>setUniqueClickCounting</code></td><td>Configure unique-click counting for a Cutt.ly short link. Send 0 to stop counting unique clicks, 1 to enable it (Single plan), or a window of 15 to 1440 minutes over which repeat clicks from the same visitor are collapsed into one (Team plans). Values outside 15-1440 return 'Unique time must be between 15 - 1440 minutes'; using a window without the required plan returns 'Insufficient subscription level'.</td></tr><tr><td>Shorten URL</td><td><code>shortenUrl</code></td><td>Shorten a long URL into a Cutt.ly short link. Optionally set a custom alias, use your own approved branded domain, skip page-title lookup, or make the click stats public. Returns url.status (7 = shortened OK, 1 = the link is already shortened, 2 = invalid link, 3/4/5 = validation failure, 6 = blocked domain, 8 = monthly link limit reached) plus shortLink, fullLink, title and date when status is 7.</td></tr></tbody></table>

</details>

