---
description: "Simplescraper turns any website into structured data and APIs."
hidden: true
---

# Simplescraper

<img src="../../.gitbook/assets/connectors/lg/simplescraper.png" alt="Simplescraper logo">

Simplescraper turns any website into structured data and APIs. This connector covers the full Simplescraper Extract API v1: create, list, read and update scrape recipes, run them on demand or in bulk, manage the batch (crawler) URL list, read run results and run history, extract markdown, HTML, screenshots and structured data from a single URL, run AI-powered Smart Extract, capture page screenshots, and discover every URL on a site from its sitemap.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [simplescraper.io](https://simplescraper.io) |
| **Authentication** | Bearer token |
| **Slug** | `simplescraper` |

## Use it

Add Simplescraper from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.simplescraper.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Capture Screenshot | `captureScreenshot` | Captures a screenshot of any web page with full control over image format, viewport, pixel density and page-load waiting. Choose output 'url' for a hosted image link (recommended, kept for 30 days), 'base64' for an encoded image string, or 'binary' for raw image bytes. Costs one credit per request. |
| Create Recipe | `createRecipe` | Creates a new scrape recipe from a name, a target URL and a list of named CSS selectors. Returns the new recipe ID and the stored recipe, including a generated UID for each selector. A maximum of 100 selectors is allowed. |
| Extract Page | `extractPage` | Extracts content from a single URL and returns it immediately, with no job queue or polling. Request any combination of markdown, raw HTML, a screenshot and structured data from CSS selectors. With no extraction flags set, only page metadata is returned. Consumes scrape credits. |
| Extract URLs | `extractUrls` | Discovers every page URL on a website by finding and parsing its sitemap, including nested sitemap indexes. Useful as a first step before batch scraping. This endpoint does not consume scrape credits. |
| Get Latest Recipe Results | `getLatestRecipeResults` | Retrieves the most recent scrape results already stored for a recipe, without starting a new run and without consuming credits. Supports cursor pagination and ordering by row index or scrape timestamp. |
| Get Recipe | `getRecipe` | Retrieves the full details of a single scrape recipe, including its name, source URL, host, creation and last-run dates, and the CSS selectors that define what it extracts. |
| Get Recipe Results History | `getRecipeResultsHistory` | Lists the most recent scrape runs for a recipe, newest first, with the results ID, completion date, status and number of pages scraped for each. Capped at the 50 most recent runs. A recipe with no completed runs returns an empty list. |
| Get Results | `getResults` | Retrieves the data and progress of a specific scrape run by its results ID. Poll this action after an asynchronous run until the status reads 'completed'. Supports cursor pagination and ordering by row index or scrape timestamp. |
| Get Smart Extract Result | `getSmartExtractResult` | Polls a Smart Extract task by its extract UID and returns the extracted data and generated selectors once it finishes. A status of 'success' or 'completed' means the extraction is done, 'running' means it is still processing, and 'error' means it failed. |
| List Recipes | `listRecipes` | Lists the scrape recipes in your Simplescraper account, with optional keyword search, host filtering, sorting and pagination. Returns the total number of matching recipes and a page of recipe summaries. |

<details>

<summary>See 4 more actions</summary>

* **Run Recipe** `runRecipe`: Runs a saved scrape recipe and returns the extracted data. Optionally override the source URL, scrape the recipe's crawler URL list, supply a list of URLs to scrape in one call, or request a markdown version of each page. Runs that exceed 90 seconds, and any run using the urls list, return a results ID with status 'running' that can be polled with Get Results. Consumes scrape credits.
* **Smart Extract** `smartExtract`: Uses AI to extract named data points from any page and returns both the data and reusable CSS selectors, without writing selectors yourself. Describe the fields you want as a comma-separated schema. Extractions taking longer than two minutes return a running status and an extract ID to poll with Get Smart Extract Result. Consumes scrape credits.
* **Update Batch URLs** `updateBatchUrls`: Adds to or replaces the batch (crawler) URL list of a scrape recipe, so the recipe can scrape many pages in one run. Returns a summary of new, existing and invalid URLs. A recipe can hold at most 5000 batch URLs. Run the recipe with the crawler option enabled to scrape this list.
* **Update Recipe** `updateRecipe`: Updates an existing scrape recipe. Any combination of name, source URL and selectors can be changed. Use update mode 'merge' to update selectors that share a name and add the new ones, or 'replace' to swap the selector list entirely.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Scrape Completed | `scrape.completed` | Fires after each URL in a scrape recipe finishes and its results are saved; a recipe scraping several pages sends one delivery per page. Registration is manual and per recipe, in the Simplescraper dashboard: open https://simplescraper.io/dashboard, select the recipe, open the Integrations tab, paste the fastn trigger URL into the webhook field and press Enter to save, then run the recipe. Simplescraper has no webhook registration API, so fastn cannot subscribe on the customer's behalf. The delivery is a POST with Content-Type application/json whose body is a bare JSON array of scraped rows; it carries no event-type discriminator and no signature, so this connector declares a single event and does not set an event key. The payload schema below is modelled from Simplescraper's documented sample at https://simplescraper.io/docs/sending-data-to-webhook, not from a captured delivery. |
