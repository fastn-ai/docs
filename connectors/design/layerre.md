---
description: "Layerre design-automation API."
---

# Layerre

Layerre design-automation API. Import a Canva design as a reusable template, edit its layers, and render image/PDF variants at scale (single, bulk, and combined multi-page PDFs). Also analyzes a public Canva share URL for its colors, fonts and images.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [layerre.com](https://layerre.com) |
| **Authentication** | API key |
| **Actions** | 17 |
| **Events** | 0 |
| **Slug** | `layerre` |

## Use it

Add Layerre from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.layerre.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Analyze Canva Design | `analyzeCanvaDesign` | Inspect a public Canva share URL without importing it, returning the design's colour palette, the fonts it uses with their weights and styles, and its images. Useful for previewing or brand-checking a design before committing a render to create a template. NOTE: the image URLs returned are pre-signed and fetchable without an API key. |
| Create Layer | `createLayer` | Add a new layer to a template. Supply properties.text to create a text layer or properties.img_url to create an image layer. Position it with x/y and size it with properties.width/height. Returns the created layer including the layer id you need for variant overrides. |
| Create Template From Canva URL | `createTemplate` | Import a public Canva design into Layerre as a reusable template. Layerre fetches the share URL and extracts layers, fonts, images and dimensions. The URL must be on canva.com or canva.link and must be shared as 'Anyone with the link'. Counts as one render against the account's quota. Returns 201 with the new template and its layer ids. |
| Create Variant | `createVariant` | Render one image or PDF from a template, optionally overriding individual layers. Each override names a layer_id (from Get Template) plus the properties to change, such as text or img_url; layers you omit keep their template defaults. Consumes one render from the account quota. Returns the saved variant with a downloadable URL. |
| Create Variants In Bulk | `createVariantsBulk` | Render many variants from one template in a single request, all sharing one export_type. Each item carries its own overrides, size and page_number. Set combine_pdf true (Plus plans and above, PDF export only) to merge every item into one multi-page PDF in a single render pass. Consumes one render per item. |
| Delete Layer | `deleteLayer` | Soft-delete one layer from a template. Returns 204 with an empty body on success and 404 'Template not found for user.' when the template or layer id does not belong to the account. The layer stops appearing in later renders. |
| Delete Template | `deleteTemplate` | Soft-delete a Layerre template by id. Returns 204 with an empty body on success and 404 with 'Template not found for user.' if the id does not belong to the account. The template's variants become unreachable through the API. |
| Delete Variant | `deleteVariant` | Soft-delete one rendered variant. Returns 204 with an empty body on success and 404 'Template not found for user.' when the ids do not belong to the account. WARNING: deleting the record does not necessarily invalidate any pre-signed download URL already handed out for that file. |
| Get API Health | `getApiHealth` | Service health probe for the Layerre API. Returns the status string, a human-readable message and the running API version. Undocumented but live; useful as a cheap liveness check that consumes no render quota. |
| Get Layer | `getLayer` | Get one layer of a template by id, with all of its properties. Refreshes the layer's signed image URL if it has expired. NOTE: for image layers the response contains a time-limited pre-signed storage URL that grants direct read access without an API key. |
| Get Template | `getTemplate` | Get one Layerre template by id, including every layer with its full properties (text, fonts, geometry, image URLs). Refreshes the signed image URLs on all image layers. NOTE: the response embeds time-limited pre-signed storage URLs that grant direct read access to the template's images without any API key. |
| Get Variant | `getVariant` | Get one rendered variant by id and obtain a fresh download URL for it, regenerating the signed URL if it has expired. NOTE: the download URL returned is pre-signed and can be fetched by anyone who has it, with no API key. |
| List Template Tags | `listTemplateTags` | List every distinct tag used across the account's templates together with how many templates carry each one, sorted by count descending then alphabetically. Use it to populate a tag picker before calling List Templates with a tag filter. |
| List Template Variants | `listTemplateVariants` | List every variant rendered from a template, with pagination via skip and limit. Refreshes the signed download URL on each variant. NOTE: the returned download URLs are pre-signed and readable without an API key until they expire. |
| List Templates | `listTemplates` | List all templates for the authenticated Layerre account, sorted by last modified, with variant counts. Supports pagination (skip/limit), filtering by tag, and case-insensitive name search via q. Set include_layers=true to embed each template's layers (slower). |
| Update Layer | `updateLayer` | Update a single layer on a template: change its text, swap its img_url, or adjust any styling or geometry property. Edits the template itself, so every later variant inherits the change. Returns the updated layer. |
| Update Template | `updateTemplate` | Update a template's metadata (name, width, height, background colour, per-page backgrounds, tags) and/or replace layer properties in bulk. Only the fields you send are changed. Returns the updated template. |
