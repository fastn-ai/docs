---
description: "Google Search Console API — manage verified sites and sitemaps, query Search Analytics performance data, inspect URL indexing status, and run the…"
hidden: true
---

# Google Search Console

<img src="../../.gitbook/assets/connectors/google-search-console.png" alt="Google Search Console logo" width="64">

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

| Action | Slug | What it does |
| --- | --- | --- |
| Add Site | `addSite` | Adds a site to the authenticated user's set of Search Console properties. The property still has to be verified separately before its data becomes available. |
| Delete Site | `deleteSite` | Removes a site from the authenticated user's set of Search Console properties. This does not affect Google's crawling or indexing of the site. |
| Delete Sitemap | `deleteSitemap` | Removes a sitemap from the Sitemaps report of a Search Console property. This does not stop Google from crawling the sitemap or the URLs it previously discovered. |
| Get Site | `getSite` | Retrieves information about a single Search Console property, including the authenticated user's permission level for it. |
| Get Sitemap | `getSitemap` | Retrieves the processing status, error and warning counts, and content type breakdown for a single sitemap submitted to a Search Console property. |
| Inspect URL | `inspectUrl` | Runs the URL Inspection tool for a single URL within a Search Console property, returning its Google Index status, canonical URL, crawl details, mobile usability, rich results, and AMP status. |
| List Sitemaps | `listSitemaps` | Lists the sitemaps submitted for a Search Console property, or the sitemaps contained in a given sitemap index file, with their processing status, error counts, and content type breakdown. |
| List Sites | `listSites` | Lists every Search Console property the authenticated user has access to, along with their permission level. |
| Query Search Analytics | `querySearchAnalytics` | Queries Search Analytics performance data for a Search Console property over a date range, returning clicks, impressions, click-through rate, and average position grouped by the requested dimensions. |
| Query Search Analytics With Filters | `querySearchAnalyticsWithFilters` | Queries Search Analytics performance data for a Search Console property and restricts the results with a single dimension filter, for example only rows whose query contains a keyword or whose country equals a given code. |

<details>

<summary>See 2 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Run Mobile Friendly Test | `runMobileFriendlyTest` | Runs the Mobile-Friendly Test against any public URL and returns the mobile-friendliness verdict, any usability issues found, and optionally a screenshot of the rendered page. The URL does not have to belong to a Search Console property. |
| Submit Sitemap | `submitSitemap` | Submits a sitemap for a Search Console property so that Google discovers the URLs it contains. Returns an empty body on success. |

</details>
