---
description: "Google Search Console reports how sites perform in Google Search. Manage sites and sitemaps, and inspect URL indexing."
hidden: true
---

# Google Search Console

<img src="../../.gitbook/assets/connectors/lg/google-search-console.png" alt="Google Search Console logo">

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [searchconsole.googleapis.com](https://searchconsole.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleSearchConsole` |

## Setup

Your customers sign in to Google Search Console through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Search Console from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Search Console**.
2. Select **Connect** on the Google Search Console card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Search Console and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Search Console's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Site</td><td><code>addSite</code></td><td>Adds a site to the authenticated user's set of Search Console properties. The property still has to be verified separately before its data becomes available.</td></tr><tr><td>Delete Site</td><td><code>deleteSite</code></td><td>Removes a site from the authenticated user's set of Search Console properties. This does not affect Google's crawling or indexing of the site.</td></tr><tr><td>Delete Sitemap</td><td><code>deleteSitemap</code></td><td>Removes a sitemap from the Sitemaps report of a Search Console property. This does not stop Google from crawling the sitemap or the URLs it previously discovered.</td></tr><tr><td>Get Site</td><td><code>getSite</code></td><td>Retrieves information about a single Search Console property, including the authenticated user's permission level for it.</td></tr><tr><td>Get Sitemap</td><td><code>getSitemap</code></td><td>Retrieves the processing status, error and warning counts, and content type breakdown for a single sitemap submitted to a Search Console property.</td></tr><tr><td>Inspect URL</td><td><code>inspectUrl</code></td><td>Runs the URL Inspection tool for a single URL within a Search Console property, returning its Google Index status, canonical URL, crawl details, mobile usability, rich results, and AMP status.</td></tr><tr><td>List Sitemaps</td><td><code>listSitemaps</code></td><td>Lists the sitemaps submitted for a Search Console property, or the sitemaps contained in a given sitemap index file, with their processing status, error counts, and content type breakdown.</td></tr><tr><td>List Sites</td><td><code>listSites</code></td><td>Lists every Search Console property the authenticated user has access to, along with their permission level.</td></tr><tr><td>Query Search Analytics</td><td><code>querySearchAnalytics</code></td><td>Queries Search Analytics performance data for a Search Console property over a date range, returning clicks, impressions, click-through rate, and average position grouped by the requested dimensions.</td></tr><tr><td>Query Search Analytics With Filters</td><td><code>querySearchAnalyticsWithFilters</code></td><td>Queries Search Analytics performance data for a Search Console property and restricts the results with a single dimension filter, for example only rows whose query contains a keyword or whose country equals a given code.</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Run Mobile Friendly Test</td><td><code>runMobileFriendlyTest</code></td><td>Runs the Mobile-Friendly Test against any public URL and returns the mobile-friendliness verdict, any usability issues found, and optionally a screenshot of the rendered page. The URL does not have to belong to a Search Console property.</td></tr><tr><td>Submit Sitemap</td><td><code>submitSitemap</code></td><td>Submits a sitemap for a Search Console property so that Google discovers the URLs it contains. Returns an empty body on success.</td></tr></tbody></table>

</details>

