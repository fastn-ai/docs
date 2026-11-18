---
description: "Wikipedia's REST API (Wikimedia REST v1) for any language edition: page summaries, HTML and mobile HTML, revision metadata, media lists, talk pages, lint…"
hidden: true
---

# Wikipedia

Wikipedia's REST API (Wikimedia REST v1) for any language edition: page summaries, HTML and mobile HTML, revision metadata, media lists, talk pages, lint errors, wikitext/HTML transforms, citation generation (Citoid) and mobile app resources. No API key needed; Wikimedia asks for a descriptive User-Agent.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [wikipedia.org](https://wikipedia.org) |
| **Authentication** | No authentication |
| **Actions** | 29 |
| **Events** | 0 |
| **Slug** | `wikipediaRest` |

## Use it

Add Wikipedia from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.wikipediaRest.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Citation | `getCitation` | Generate citation data from a URL, DOI, PMID, PMCID or ISBN with Citoid (1 request per second for automated use) (GET /api/rest_v1/data/citation/{format}/{query}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Mobile CSS | `getMobileCss` | Get the CSS used by the Wikipedia mobile apps (GET /api/rest_v1/data/css/mobile/{type}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Mobile HTML Offline Resources | `getMobileHtmlOfflineResources` | List the CSS and JavaScript URLs needed to show a page's mobile HTML offline (GET /api/rest_v1/page/mobile-html-offline-resources/{title}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Mobile JavaScript | `getMobileJavascript` | Get the JavaScript used by the Wikipedia mobile apps (GET /api/rest_v1/data/javascript/mobile/{type}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Mobile Localized Strings | `getMobileI18n` | Get localized UI strings for the mobile Page Content Service (GET /api/rest_v1/data/i18n/{type}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Page HTML | `getPageHtml` | Get the latest Parsoid HTML of a page. Large articles can be several MB (GET /api/rest_v1/page/html/{title}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Page Lint Errors | `getPageLintErrors` | Get wikitext lint errors of the latest revision of a page (GET /api/rest_v1/page/lint/{title}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Page Media List | `getPageMediaList` | List the images, videos and audio used on a page (GET /api/rest_v1/page/media-list/{title}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Page Mobile HTML | `getPageMobileHtml` | Get page HTML optimized for mobile apps (Page Content Service) (GET /api/rest_v1/page/mobile-html/{title}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Page Revision HTML | `getPageRevisionHtml` | Get the Parsoid HTML of one revision of a page (GET /api/rest_v1/page/html/{title}/{revision}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Page Revision Info | `getPageRevisionInfo` | Get metadata for one revision of a page (GET /api/rest_v1/page/title/{title}/{revision}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Page Revision Lint Errors | `getPageRevisionLintErrors` | Get wikitext lint errors of one revision of a page (GET /api/rest_v1/page/lint/{title}/{revision}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Page Revision Media List | `getPageRevisionMediaList` | List the media used on one revision of a page (GET /api/rest_v1/page/media-list/{title}/{revision}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Page Revision Mobile HTML | `getPageRevisionMobileHtml` | Get mobile-optimized HTML of one revision of a page (GET /api/rest_v1/page/mobile-html/{title}/{revision}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Page Summary | `getPageSummary` | Get a page summary: title, description, plain and HTML extract of the first paragraph, thumbnail, coordinates and URLs (used for link previews) (GET /api/rest_v1/page/summary/{title}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Page Title Info | `getPageTitleInfo` | Get revision metadata for the latest revision of a page: title, page id, revision, timestamp and namespace (GET /api/rest_v1/page/title/{title}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Revision Mobile HTML Offline Resources | `getRevisionMobileHtmlOfflineResources` | List the offline CSS and JavaScript resources for one revision's mobile HTML (GET /api/rest_v1/page/mobile-html-offline-resources/{title}/{revision}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Talk Page | `getTalkPage` | Get a talk page parsed into topics and replies (GET /api/rest_v1/page/talk/{title}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Get Talk Page Revision | `getTalkPageRevision` | Get one revision of a talk page parsed into topics and replies (GET /api/rest_v1/page/talk/{title}/{revision}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Transform HTML to Wikitext | `transformHtmlToWikitext` | Transform HTML to wikitext (POST /api/rest_v1/transform/html/to/wikitext). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Transform HTML to Wikitext for Page | `transformHtmlToWikitextForPage` | Transform HTML to wikitext in the context of a page title (POST /api/rest_v1/transform/html/to/wikitext/{title}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Transform HTML to Wikitext for Revision | `transformHtmlToWikitextForRevision` | Transform HTML to wikitext in the context of a page revision (POST /api/rest_v1/transform/html/to/wikitext/{title}/{revision}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Transform Wikitext to HTML | `transformWikitextToHtml` | Transform wikitext to HTML (POST /api/rest_v1/transform/wikitext/to/html). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Transform Wikitext to HTML for Page | `transformWikitextToHtmlForPage` | Transform wikitext to HTML in the context of a page title (POST /api/rest_v1/transform/wikitext/to/html/{title}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Transform Wikitext to HTML for Revision | `transformWikitextToHtmlForRevision` | Transform wikitext to HTML in the context of a page revision (POST /api/rest_v1/transform/wikitext/to/html/{title}/{revision}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Transform Wikitext to Lint Errors | `transformWikitextToLint` | Transform wikitext to lint errors (POST /api/rest_v1/transform/wikitext/to/lint). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Transform Wikitext to Lint Errors for Page | `transformWikitextToLintForPage` | Transform wikitext to lint errors in the context of a page title (POST /api/rest_v1/transform/wikitext/to/lint/{title}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Transform Wikitext to Lint Errors for Revision | `transformWikitextToLintForRevision` | Transform wikitext to lint errors in the context of a page revision (POST /api/rest_v1/transform/wikitext/to/lint/{title}/{revision}). Docs: https://en.wikipedia.org/api/rest_v1/ |
| Transform Wikitext to Mobile HTML | `transformWikitextToMobileHtml` | Transform wikitext to mobile-optimized HTML for a page title (POST /api/rest_v1/transform/wikitext/to/mobile-html/{title}). Docs: https://en.wikipedia.org/api/rest_v1/ |
