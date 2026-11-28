---
description: "AltText.ai writes alt text for images with AI. Create alt text from image links, uploads or CSV files, scrape page images, and manage your image library."
hidden: true
---

# AltText.ai

<img src="../../.gitbook/assets/connectors/lg/alt-text-ai.png" alt="AltText.ai logo">

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [alttext.ai](https://alttext.ai) |
| **Authentication** | API key |
| **Slug** | `altTextAi` |

## Setup

Your customers enter their API key for AltText.ai when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AltText.ai from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AltText.ai**.
2. Select **Connect** on the AltText.ai card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AltText.ai's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Bulk Create Images From CSV</td><td><code>bulkCreateImages</code></td><td>Upload a CSV of image URLs to AltText.ai and queue alt text generation for every valid row, up to 100000 rows. Pass the CSV text itself in csv_content (a url header line followed by one image URL per line). Valid rows are processed in the background and consume one credit each; invalid rows are returned in row_errors as [rowNumber, message] pairs. Optionally supply an email address to receive the results of the bulk upload.</td></tr><tr><td>Create Image From Base64 Upload</td><td><code>createImageFromBase64</code></td><td>Upload a local image as base64-encoded data to AltText.ai and generate alt text for it. Use this when the image is not reachable at a public URL; otherwise use Create Image From URL. The raw field must be RFC 4648 base64 with no line feeds, and must not be combined with a url. Uploads are always processed synchronously, so the async option is not supported. The image file is analysed and then discarded, never stored. Consumes one credit per image. Supported formats JPEG, PNG, GIF, WEBP, BMP, maximum 16 MB, minimum 50x50 pixels.</td></tr><tr><td>Create Image From URL</td><td><code>createImageFromUrl</code></td><td>Add a publicly accessible image URL to the AltText.ai library and generate alt text for it. Consumes one credit per new image (extra languages cost one translation credit each); re-sending a URL already in the library returns the existing record free of charge. Supported formats JPEG, PNG, GIF, WEBP, BMP, maximum 16 MB, minimum 50x50 pixels. Rate limited to 4 calls per second. Use Create Image From Base64 instead when the image is not reachable by URL.</td></tr><tr><td>Delete Image</td><td><code>deleteImage</code></td><td>Permanently delete an image and its generated alt text from the AltText.ai library by asset ID. The deleted image record is returned in the response. Credits already spent on the image are not refunded.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Retrieve the AltText.ai account settings, including the credit usage for the current billing period (usage / usage_limit), the webhook notification URL, the notification email, the default language and the alt-text formatting defaults. Use this before generating alt text to check how many credits remain.</td></tr><tr><td>Get Image</td><td><code>getImage</code></td><td>Retrieve a single image from the AltText.ai library by its asset ID, returning the generated alt text in every language, tags, custom metadata and any generation errors. Use this to poll for the result of an image created with async set to true.</td></tr><tr><td>List Images</td><td><code>listImages</code></td><td>List the images in the AltText.ai library together with their generated alt text, tags and metadata. Supports pagination with page and limit (maximum 100 per page) and an optional exact-match url filter.</td></tr><tr><td>Scrape Page Images</td><td><code>scrapePageImages</code></td><td>Crawl a web page URL, or parse a raw HTML document, and queue alt text generation for every img element found. The response lists the scraped image elements with their src, existing alt, width and height, plus a skip_reason for any that were not queued; the generated alt text itself arrives asynchronously, so poll Get Image or List Images for the results. The crawler does not execute JavaScript and must download and parse the page within 3 seconds. Each queued image consumes one credit.</td></tr><tr><td>Search Images</td><td><code>searchImages</code></td><td>Search the AltText.ai image library. The query type is detected automatically: a query starting with http:// or https:// searches by URL substring, otherwise an exact asset ID match is tried first and the query then falls back to a full-text search of alt text supporting the operators &amp; (AND), | or OR, and - or ! (exclude). Supports pagination with page and limit.</td></tr><tr><td>Update Account</td><td><code>updateAccount</code></td><td>Update the AltText.ai account settings that are editable through the API: the account name, the webhook notification URL that image events are POSTed to, and the notification email address. Other settings such as whitelabel, ending_period and no_quotes can only be changed on the AltText.ai website. On a validation failure the API returns 4xx with the offending field listed under errors.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Update Image</td><td><code>updateImage</code></td><td>Update an existing AltText.ai image: replace its alt text, rename its asset ID or replace its custom metadata. The image URL cannot be changed. Use the lang and overwrite query parameters to control which language the alt text is written to and whether existing alt text in that language is replaced.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Image Deleted</td><td><code>deleted</code></td><td>Sent when images are deleted from the AltText.ai library. AltText.ai delivers webhooks to the single account-level notification URL, which this connector sets through Update Account when the trigger is enabled. AltText.ai does not sign webhook deliveries.</td></tr><tr><td>Image Uploaded</td><td><code>uploaded</code></td><td>Sent when new images are added to the AltText.ai library and their alt text has been generated, including images queued asynchronously by Create Image From URL with async true, Bulk Create Images From CSV and Scrape Page Images. AltText.ai delivers webhooks to the single account-level notification URL, which this connector sets through Update Account when the trigger is enabled. AltText.ai does not sign webhook deliveries.</td></tr></tbody></table>
