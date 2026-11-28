---
description: "Wikipedia is the free online encyclopedia. Get page HTML, summaries, revisions, media lists and citations in any language."
hidden: true
---

# Wikipedia

<img src="../../.gitbook/assets/connectors/lg/wikipedia-rest.png" alt="Wikipedia logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [wikipedia.org](https://wikipedia.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `wikipediaRest` |

## Setup

Wikipedia needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Wikipedia from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Wikipedia**.
2. Select **Connect** on the Wikipedia card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Wikipedia needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Wikipedia's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Citation</td><td><code>getCitation</code></td><td>Generate citation data from a URL, DOI, PMID, PMCID or ISBN with Citoid (1 request per second for automated use) Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Mobile CSS</td><td><code>getMobileCss</code></td><td>Get the CSS used by the Wikipedia mobile apps Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Mobile HTML Offline Resources</td><td><code>getMobileHtmlOfflineResources</code></td><td>List the CSS and JavaScript URLs needed to show a page's mobile HTML offline Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Mobile JavaScript</td><td><code>getMobileJavascript</code></td><td>Get the JavaScript used by the Wikipedia mobile apps Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Mobile Localized Strings</td><td><code>getMobileI18n</code></td><td>Get localized UI strings for the mobile Page Content Service Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Page HTML</td><td><code>getPageHtml</code></td><td>Get the latest Parsoid HTML of a page. Large articles can be several MB Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Page Lint Errors</td><td><code>getPageLintErrors</code></td><td>Get wikitext lint errors of the latest revision of a page Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Page Media List</td><td><code>getPageMediaList</code></td><td>List the images, videos and audio used on a page Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Page Mobile HTML</td><td><code>getPageMobileHtml</code></td><td>Get page HTML optimized for mobile apps (Page Content Service) Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Page Revision HTML</td><td><code>getPageRevisionHtml</code></td><td>Get the Parsoid HTML of one revision of a page Docs: https://en.wikipedia.org/api/rest_v1/</td></tr></tbody></table>

<details>

<summary>View 19 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Page Revision Info</td><td><code>getPageRevisionInfo</code></td><td>Get metadata for one revision of a page Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Page Revision Lint Errors</td><td><code>getPageRevisionLintErrors</code></td><td>Get wikitext lint errors of one revision of a page Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Page Revision Media List</td><td><code>getPageRevisionMediaList</code></td><td>List the media used on one revision of a page Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Page Revision Mobile HTML</td><td><code>getPageRevisionMobileHtml</code></td><td>Get mobile-optimized HTML of one revision of a page Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Page Summary</td><td><code>getPageSummary</code></td><td>Get a page summary: title, description, plain and HTML extract of the first paragraph, thumbnail, coordinates and URLs (used for link previews) Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Page Title Info</td><td><code>getPageTitleInfo</code></td><td>Get revision metadata for the latest revision of a page: title, page id, revision, timestamp and namespace Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Revision Mobile HTML Offline Resources</td><td><code>getRevisionMobileHtmlOfflineResources</code></td><td>List the offline CSS and JavaScript resources for one revision's mobile HTML Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Talk Page</td><td><code>getTalkPage</code></td><td>Get a talk page parsed into topics and replies Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Get Talk Page Revision</td><td><code>getTalkPageRevision</code></td><td>Get one revision of a talk page parsed into topics and replies Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Transform HTML to Wikitext</td><td><code>transformHtmlToWikitext</code></td><td>Transform HTML to wikitext Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Transform HTML to Wikitext for Page</td><td><code>transformHtmlToWikitextForPage</code></td><td>Transform HTML to wikitext in the context of a page title Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Transform HTML to Wikitext for Revision</td><td><code>transformHtmlToWikitextForRevision</code></td><td>Transform HTML to wikitext in the context of a page revision Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Transform Wikitext to HTML</td><td><code>transformWikitextToHtml</code></td><td>Transform wikitext to HTML Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Transform Wikitext to HTML for Page</td><td><code>transformWikitextToHtmlForPage</code></td><td>Transform wikitext to HTML in the context of a page title Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Transform Wikitext to HTML for Revision</td><td><code>transformWikitextToHtmlForRevision</code></td><td>Transform wikitext to HTML in the context of a page revision Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Transform Wikitext to Lint Errors</td><td><code>transformWikitextToLint</code></td><td>Transform wikitext to lint errors Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Transform Wikitext to Lint Errors for Page</td><td><code>transformWikitextToLintForPage</code></td><td>Transform wikitext to lint errors in the context of a page title Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Transform Wikitext to Lint Errors for Revision</td><td><code>transformWikitextToLintForRevision</code></td><td>Transform wikitext to lint errors in the context of a page revision Docs: https://en.wikipedia.org/api/rest_v1/</td></tr><tr><td>Transform Wikitext to Mobile HTML</td><td><code>transformWikitextToMobileHtml</code></td><td>Transform wikitext to mobile-optimized HTML for a page title Docs: https://en.wikipedia.org/api/rest_v1/</td></tr></tbody></table>

</details>

