---
description: "AltText.ai generates alt text for images using AI computer-vision models, so images can be made accessible and SEO-friendly without a human copywriter."
---

# AltText.ai

AltText.ai generates alt text for images using AI computer-vision models, so images can be made accessible and SEO-friendly without a human copywriter. This connector wraps the full AltText.ai REST API v1: account settings, the image library (create by public URL or base64 upload, read, update, delete, list, search), bulk CSV creation and web-page scraping, plus image webhook events.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [alttext.ai](https://alttext.ai) |
| **Authentication** | Credentials you enter |
| **Actions** | 11 |
| **Events** | 2 |
| **Slug** | `altTextAi` |

## Use it

Add AltText.ai from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.altTextAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Create Images From CSV | `bulkCreateImages` | Upload a CSV of image URLs to AltText.ai and queue alt text generation for every valid row, up to 100000 rows. Pass the CSV text itself in csv_content (a url header line followed by one image URL per line). Valid rows are processed in the background and consume one credit each; invalid rows are returned in row_errors as [rowNumber, message] pairs. Optionally supply an email address to receive the results of the bulk upload. |
| Create Image From Base64 Upload | `createImageFromBase64` | Upload a local image as base64-encoded data to AltText.ai and generate alt text for it. Use this when the image is not reachable at a public URL; otherwise use Create Image From URL. The raw field must be RFC 4648 base64 with no line feeds, and must not be combined with a url. Uploads are always processed synchronously, so the async option is not supported. The image file is analysed and then discarded, never stored. Consumes one credit per image. Supported formats JPEG, PNG, GIF, WEBP, BMP, maximum 16 MB, minimum 50x50 pixels. |
| Create Image From URL | `createImageFromUrl` | Add a publicly accessible image URL to the AltText.ai library and generate alt text for it. Consumes one credit per new image (extra languages cost one translation credit each); re-sending a URL already in the library returns the existing record free of charge. Supported formats JPEG, PNG, GIF, WEBP, BMP, maximum 16 MB, minimum 50x50 pixels. Rate limited to 4 calls per second. Use Create Image From Base64 instead when the image is not reachable by URL. |
| Delete Image | `deleteImage` | Permanently delete an image and its generated alt text from the AltText.ai library by asset ID. The deleted image record is returned in the response. Returns 404 when no image has that asset ID. Credits already spent on the image are not refunded. |
| Get Account | `getAccount` | Retrieve the AltText.ai account settings, including the credit usage for the current billing period (usage / usage_limit), the webhook notification URL, the notification email, the default language and the alt-text formatting defaults. Use this before generating alt text to check how many credits remain. |
| Get Image | `getImage` | Retrieve a single image from the AltText.ai library by its asset ID, returning the generated alt text in every language, tags, custom metadata and any generation errors. Use this to poll for the result of an image created with async set to true. Returns 404 when no image has that asset ID. |
| List Images | `listImages` | List the images in the AltText.ai library together with their generated alt text, tags and metadata. Supports pagination with page and limit (maximum 100 per page) and an optional exact-match url filter. |
| Scrape Page Images | `scrapePageImages` | Crawl a web page URL, or parse a raw HTML document, and queue alt text generation for every img element found. The response lists the scraped image elements with their src, existing alt, width and height, plus a skip_reason for any that were not queued; the generated alt text itself arrives asynchronously, so poll Get Image or List Images for the results. The crawler does not execute JavaScript and must download and parse the page within 3 seconds. Each queued image consumes one credit. |
| Search Images | `searchImages` | Search the AltText.ai image library. The query type is detected automatically: a query starting with http:// or https:// searches by URL substring, otherwise an exact asset ID match is tried first and the query then falls back to a full-text search of alt text supporting the operators & (AND), \| or OR, and - or ! (exclude). Supports pagination with page and limit. |
| Update Account | `updateAccount` | Update the AltText.ai account settings that are editable through the API: the account name, the webhook notification URL that image events are POSTed to, and the notification email address. Other settings such as whitelabel, ending_period and no_quotes can only be changed on the AltText.ai website. On a validation failure the API returns 4xx with the offending field listed under errors. |
| Update Image | `updateImage` | Update an existing AltText.ai image: replace its alt text, rename its asset ID or replace its custom metadata. The image URL cannot be changed. Use the lang and overwrite query parameters to control which language the alt text is written to and whether existing alt text in that language is replaced. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Image Deleted | `deleted` | Sent when images are deleted from the AltText.ai library. AltText.ai delivers webhooks to the single account-level notification URL, which this connector sets through Update Account when the trigger is enabled. AltText.ai does not sign webhook deliveries. Payload schema is modelled from the vendor's published OpenAPI webhook definition (https://alttext.ai/openapi.yml, schema_ver 1.0.1); no live delivery was captured. |
| Image Uploaded | `uploaded` | Sent when new images are added to the AltText.ai library and their alt text has been generated, including images queued asynchronously by Create Image From URL with async true, Bulk Create Images From CSV and Scrape Page Images. AltText.ai delivers webhooks to the single account-level notification URL, which this connector sets through Update Account when the trigger is enabled. AltText.ai does not sign webhook deliveries. Payload schema is modelled from the vendor's published OpenAPI webhook definition (https://alttext.ai/openapi.yml, schema_ver 1.0.1); no live delivery was captured. |
