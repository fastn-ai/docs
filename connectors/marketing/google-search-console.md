---
description: "Connect Google Search Console to your product with fastn."
hidden: true
---

# Google Search Console

<img src="../../.gitbook/assets/connectors/lg/google-search-console.png" alt="Google Search Console logo">

Google Search Console API — manage verified sites and sitemaps, query Search Analytics performance data, inspect URL indexing status, and run the Mobile-Friendly Test.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [searchconsole.googleapis.com](https://searchconsole.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleSearchConsole` |

## Use it

Add Google Search Console from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleSearchConsole.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Site</td><td><code>addSite</code></td><td>Adds a site to the authenticated user's set of Search Console properties. The property still has to be verified separately before its data becomes available.</td></tr><tr><td>Delete Site</td><td><code>deleteSite</code></td><td>Removes a site from the authenticated user's set of Search Console properties. This does not affect Google's crawling or indexing of the site.</td></tr><tr><td>Delete Sitemap</td><td><code>deleteSitemap</code></td><td>Removes a sitemap from the Sitemaps report of a Search Console property. This does not stop Google from crawling the sitemap or the URLs it previously discovered.</td></tr><tr><td>Get Site</td><td><code>getSite</code></td><td>Retrieves information about a single Search Console property, including the authenticated user's permission level for it.</td></tr><tr><td>Get Sitemap</td><td><code>getSitemap</code></td><td>Retrieves the processing status, error and warning counts, and content type breakdown for a single sitemap submitted to a Search Console property.</td></tr><tr><td>Inspect URL</td><td><code>inspectUrl</code></td><td>Runs the URL Inspection tool for a single URL within a Search Console property, returning its Google Index status, canonical URL, crawl details, mobile usability, rich results, and AMP status.</td></tr><tr><td>List Sitemaps</td><td><code>listSitemaps</code></td><td>Lists the sitemaps submitted for a Search Console property, or the sitemaps contained in a given sitemap index file, with their processing status, error counts, and content type breakdown.</td></tr><tr><td>List Sites</td><td><code>listSites</code></td><td>Lists every Search Console property the authenticated user has access to, along with their permission level.</td></tr><tr><td>Query Search Analytics</td><td><code>querySearchAnalytics</code></td><td>Queries Search Analytics performance data for a Search Console property over a date range, returning clicks, impressions, click-through rate, and average position grouped by the requested dimensions.</td></tr><tr><td>Query Search Analytics With Filters</td><td><code>querySearchAnalyticsWithFilters</code></td><td>Queries Search Analytics performance data for a Search Console property and restricts the results with a single dimension filter, for example only rows whose query contains a keyword or whose country equals a given code.</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Run Mobile Friendly Test</td><td><code>runMobileFriendlyTest</code></td><td>Runs the Mobile-Friendly Test against any public URL and returns the mobile-friendliness verdict, any usability issues found, and optionally a screenshot of the rendered page. The URL does not have to belong to a Search Console property.</td></tr><tr><td>Submit Sitemap</td><td><code>submitSitemap</code></td><td>Submits a sitemap for a Search Console property so that Google discovers the URLs it contains. Returns an empty body on success.</td></tr></tbody></table>

</details>
