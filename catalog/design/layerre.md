---
description: "Layerre is a design automation tool. Import a Canva design as a template, edit its layers and create image variants."
hidden: true
---

# Layerre

<img src="../../.gitbook/assets/connectors/lg/layerre.png" alt="Layerre logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [layerre.com](https://layerre.com) |
| **Authentication** | API key |
| **Slug** | `layerre` |

## Setup

Your customers enter their API key for Layerre when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Layerre from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Layerre**.
2. Select **Connect** on the Layerre card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Layerre's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Analyze Canva Design</td><td><code>analyzeCanvaDesign</code></td><td>Inspect a public Canva share URL without importing it, returning the design's colour palette, the fonts it uses with their weights and styles, and its images. Useful for previewing or brand-checking a design before committing a render to create a template. NOTE: the image URLs returned are pre-signed and fetchable without an API key.</td></tr><tr><td>Create Layer</td><td><code>createLayer</code></td><td>Add a new layer to a template. Supply properties.text to create a text layer or properties.img_url to create an image layer. Position it with x/y and size it with properties.width/height. Returns the created layer including the layer id you need for variant overrides.</td></tr><tr><td>Create Template From Canva URL</td><td><code>createTemplate</code></td><td>Import a public Canva design into Layerre as a reusable template. Layerre fetches the share URL and extracts layers, fonts, images and dimensions. The URL must be on canva.com or canva.link and must be shared as 'Anyone with the link'. Counts as one render against the account's quota.</td></tr><tr><td>Create Variant</td><td><code>createVariant</code></td><td>Render one image or PDF from a template, optionally overriding individual layers. Each override names a layer_id (from Get Template) plus the properties to change, such as text or img_url; layers you omit keep their template defaults. Consumes one render from the account quota. Returns the saved variant with a downloadable URL.</td></tr><tr><td>Create Variants In Bulk</td><td><code>createVariantsBulk</code></td><td>Render many variants from one template in a single request, all sharing one export_type. Each item carries its own overrides, size and page_number. Set combine_pdf true (Plus plans and above, PDF export only) to merge every item into one multi-page PDF in a single render pass. Consumes one render per item.</td></tr><tr><td>Delete Layer</td><td><code>deleteLayer</code></td><td>Soft-delete one layer from a template.' when the template or layer id does not belong to the account. The layer stops appearing in later renders.</td></tr><tr><td>Delete Template</td><td><code>deleteTemplate</code></td><td>Soft-delete a Layerre template by id.' if the id does not belong to the account. The template's variants become unreachable through the API.</td></tr><tr><td>Delete Variant</td><td><code>deleteVariant</code></td><td>Soft-delete one rendered variant.' when the ids do not belong to the account. WARNING: deleting the record does not necessarily invalidate any pre-signed download URL already handed out for that file.</td></tr><tr><td>Get API Health</td><td><code>getApiHealth</code></td><td>Service health probe for the Layerre API. Returns the status string, a human-readable message and the running API version. Undocumented but live; useful as a cheap liveness check that consumes no render quota.</td></tr><tr><td>Get Layer</td><td><code>getLayer</code></td><td>Get one layer of a template by id, with all of its properties. Refreshes the layer's signed image URL if it has expired. NOTE: for image layers the response contains a time-limited pre-signed storage URL that grants direct read access without an API key.</td></tr></tbody></table>

<details>

<summary>View 7 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Template</td><td><code>getTemplate</code></td><td>Get one Layerre template by id, including every layer with its full properties (text, fonts, geometry, image URLs). Refreshes the signed image URLs on all image layers. NOTE: the response embeds time-limited pre-signed storage URLs that grant direct read access to the template's images without any API key.</td></tr><tr><td>Get Variant</td><td><code>getVariant</code></td><td>Get one rendered variant by id and obtain a fresh download URL for it, regenerating the signed URL if it has expired. NOTE: the download URL returned is pre-signed and can be fetched by anyone who has it, with no API key.</td></tr><tr><td>List Template Tags</td><td><code>listTemplateTags</code></td><td>List every distinct tag used across the account's templates together with how many templates carry each one, sorted by count descending then alphabetically. Use it to populate a tag picker before calling List Templates with a tag filter.</td></tr><tr><td>List Template Variants</td><td><code>listTemplateVariants</code></td><td>List every variant rendered from a template, with pagination via skip and limit. Refreshes the signed download URL on each variant. NOTE: the returned download URLs are pre-signed and readable without an API key until they expire.</td></tr><tr><td>List Templates</td><td><code>listTemplates</code></td><td>List all templates for the authenticated Layerre account, sorted by last modified, with variant counts. Supports pagination (skip/limit), filtering by tag, and case-insensitive name search via q. Set include_layers=true to embed each template's layers (slower).</td></tr><tr><td>Update Layer</td><td><code>updateLayer</code></td><td>Update a single layer on a template: change its text, swap its img_url, or adjust any styling or geometry property. Edits the template itself, so every later variant inherits the change. Returns the updated layer.</td></tr><tr><td>Update Template</td><td><code>updateTemplate</code></td><td>Update a template's metadata (name, width, height, background colour, per-page backgrounds, tags) and/or replace layer properties in bulk. Only the fields you send are changed. Returns the updated template.</td></tr></tbody></table>

</details>

