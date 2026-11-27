---
description: "Simplescraper turns websites into structured data. Extract pages and URLs, capture screenshots and manage scraping recipes and results."
hidden: true
---

# Simplescraper

<img src="../../.gitbook/assets/connectors/lg/simplescraper.png" alt="Simplescraper logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [simplescraper.io](https://simplescraper.io) |
| **Authentication** | Access token |
| **Slug** | `simplescraper` |

## Setup

Your customers enter their access token for Simplescraper when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Simplescraper from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Simplescraper**.
2. Select **Connect** on the Simplescraper card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Simplescraper's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Capture Screenshot</td><td><code>captureScreenshot</code></td><td>Captures a screenshot of any web page with full control over image format, viewport, pixel density and page-load waiting. Choose output 'url' for a hosted image link (recommended, kept for 30 days), 'base64' for an encoded image string, or 'binary' for raw image bytes. Costs one credit per request.</td></tr><tr><td>Create Recipe</td><td><code>createRecipe</code></td><td>Creates a new scrape recipe from a name, a target URL and a list of named CSS selectors. Returns the new recipe ID and the stored recipe, including a generated UID for each selector. A maximum of 100 selectors is allowed.</td></tr><tr><td>Extract Page</td><td><code>extractPage</code></td><td>Extracts content from a single URL and returns it immediately, with no job queue or polling. Request any combination of markdown, raw HTML, a screenshot and structured data from CSS selectors. With no extraction flags set, only page metadata is returned. Consumes scrape credits.</td></tr><tr><td>Extract URLs</td><td><code>extractUrls</code></td><td>Discovers every page URL on a website by finding and parsing its sitemap, including nested sitemap indexes. Useful as a first step before batch scraping. This endpoint does not consume scrape credits.</td></tr><tr><td>Get Latest Recipe Results</td><td><code>getLatestRecipeResults</code></td><td>Retrieves the most recent scrape results already stored for a recipe, without starting a new run and without consuming credits. Supports cursor pagination and ordering by row index or scrape timestamp.</td></tr><tr><td>Get Recipe</td><td><code>getRecipe</code></td><td>Retrieves the full details of a single scrape recipe, including its name, source URL, host, creation and last-run dates, and the CSS selectors that define what it extracts.</td></tr><tr><td>Get Recipe Results History</td><td><code>getRecipeResultsHistory</code></td><td>Lists the most recent scrape runs for a recipe, newest first, with the results ID, completion date, status and number of pages scraped for each. Capped at the 50 most recent runs. A recipe with no completed runs returns an empty list.</td></tr><tr><td>Get Results</td><td><code>getResults</code></td><td>Retrieves the data and progress of a specific scrape run by its results ID. Poll this action after an asynchronous run until the status reads 'completed'. Supports cursor pagination and ordering by row index or scrape timestamp.</td></tr><tr><td>Get Smart Extract Result</td><td><code>getSmartExtractResult</code></td><td>Polls a Smart Extract task by its extract UID and returns the extracted data and generated selectors once it finishes. A status of 'success' or 'completed' means the extraction is done, 'running' means it is still processing, and 'error' means it failed.</td></tr><tr><td>List Recipes</td><td><code>listRecipes</code></td><td>Lists the scrape recipes in your Simplescraper account, with optional keyword search, host filtering, sorting and pagination. Returns the total number of matching recipes and a page of recipe summaries.</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Run Recipe</td><td><code>runRecipe</code></td><td>Runs a saved scrape recipe and returns the extracted data. Optionally override the source URL, scrape the recipe's crawler URL list, supply a list of URLs to scrape in one call, or request a markdown version of each page. Runs that exceed 90 seconds, and any run using the urls list, return a results ID with status 'running' that can be polled with Get Results. Consumes scrape credits.</td></tr><tr><td>Smart Extract</td><td><code>smartExtract</code></td><td>Uses AI to extract named data points from any page and returns both the data and reusable CSS selectors, without writing selectors yourself. Describe the fields you want as a comma-separated schema. Extractions taking longer than two minutes return a running status and an extract ID to poll with Get Smart Extract Result. Consumes scrape credits.</td></tr><tr><td>Update Batch URLs</td><td><code>updateBatchUrls</code></td><td>Adds to or replaces the batch (crawler) URL list of a scrape recipe, so the recipe can scrape many pages in one run. Returns a summary of new, existing and invalid URLs. A recipe can hold at most 5000 batch URLs. Run the recipe with the crawler option enabled to scrape this list.</td></tr><tr><td>Update Recipe</td><td><code>updateRecipe</code></td><td>Updates an existing scrape recipe. Any combination of name, source URL and selectors can be changed. Use update mode 'merge' to update selectors that share a name and add the new ones, or 'replace' to swap the selector list entirely.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Scrape Completed</td><td><code>scrape.completed</code></td><td>Fires after each URL in a scrape recipe finishes and its results are saved; a recipe scraping several pages sends one delivery per page. Registration is manual and per recipe, in the Simplescraper dashboard: open https://simplescraper.io/dashboard, select the recipe, open the Integrations tab, paste the Fastn trigger URL into the webhook field and press Enter to save, then run the recipe. Simplescraper has no webhook registration API, so Fastn cannot subscribe on the customer's behalf. The delivery is a POST with Content-Type application/json whose body is a bare JSON array of scraped rows; it carries no event-type discriminator and no signature, so this connector declares a single event and does not set an event key.</td></tr></tbody></table>
