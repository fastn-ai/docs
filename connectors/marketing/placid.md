---
description: "Placid is a creative-automation platform that renders images, PDFs and videos from templates you design once and fill with data."
hidden: true
---

# Placid

<img src="../../.gitbook/assets/connectors/lg/placid.png" alt="Placid logo">

Placid is a creative-automation platform that renders images, PDFs and videos from templates you design once and fill with data. This connector covers the Placid REST API v2: template and collection management, custom fonts, and the image, PDF and video generation endpoints with their polling and delete routes.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [placid.app](https://placid.app) |
| **Authentication** | Credentials you enter |
| **Slug** | `placid` |

## Use it

Add Placid from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.placid.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Collection | `createCollection` | Creates a template collection to group Placid templates together - for example one collection per customer of your product. Returns the created collection with its id. |
| Create Image | `createImage` | Renders an image from a Placid template, filling its dynamic layers with your data. The render is queued and returns a polling URL; use Retrieve Image or a success webhook to collect the finished file. Placid charges 1 credit per image for canvases up to 4000 px - switch the project to test mode in the Placid app for free watermarked previews. |
| Create PDF | `createPdf` | Renders a PDF from one or more Placid templates, each template supplying one page and filled with your data. Listing several pages produces a single merged PDF. The render is queued and returns a polling URL. Placid charges 2 credits per PDF page for canvases up to 4000 px - switch the project to test mode in the Placid app for free watermarked previews. |
| Create Template | `createTemplate` | Creates a new Placid template, either blank at the canvas size you give or duplicated from an existing template. The new template has no layers until it is designed in the Placid editor. Returns the created template with its UUID. |
| Create Video | `createVideo` | Renders a video from one or more Placid templates used as clips, each filled with your data and optionally given its own audio track. The render is queued and returns a polling URL. Placid charges 10 credits per 10 seconds of output - switch the project to test mode in the Placid app for free watermarked previews. |
| Delete Collection | `deleteCollection` | Deletes a Placid template collection. The templates inside it are not deleted, only the grouping. |
| Delete Font | `deleteFont` | Permanently deletes a custom font from the Placid project. If any template still references the font, Placid refuses with HTTP 409 and lists the blocking templates; set Force to delete anyway, in which case those templates fall back to the default font on their next render. |
| Delete Image | `deleteImage` | Permanently deletes a generated Placid image. Placid answers HTTP 204 with an empty body on success and HTTP 404 when no image has that id. Once deleted the image cannot be retrieved again. |
| Delete PDF | `deletePdf` | Permanently deletes a generated Placid PDF. Once deleted the file cannot be retrieved again. |
| Delete Template | `deleteTemplate` | Permanently deletes a Placid template. Placid answers HTTP 200 on success. Creatives already generated from the template are not affected. |
| Delete Video | `deleteVideo` | Permanently deletes a generated Placid video. Once deleted the file cannot be retrieved again. |
| Get Collection | `getCollection` | Retrieves a single Placid template collection by its id, including the list of template UUIDs it holds. |
| Get Font | `getFont` | Retrieves a single custom font by its uuid. Placid answers HTTP 404 with "Font not found" when the project has no font with that uuid. |
| Get Template | `getTemplate` | Retrieves a single Placid template by its UUID, including its canvas size, tags, collections and the dynamic layers you fill when generating a creative. |
| List Collections | `listCollections` | Lists the template collections in the Placid project. By default every collection is returned; set Per Page to switch on cursor pagination. |
| List Fonts | `listFonts` | Lists the custom fonts available to the Placid project, 20 per page with cursor pagination. Each font's uuid is the font code you set as fontFamily on a text layer. |
| List Templates | `listTemplates` | Lists the templates in the Placid project the API token belongs to, 20 per page with cursor pagination. Each template carries its UUID, title, tags, thumbnail and the dynamic layers you fill when generating a creative. Optionally filter by collection, title or tag and choose the sort order. |
| Retrieve Image | `getImage` | Retrieves a generated Placid image by its id. Poll this while the status is queued; once it turns finished the image URL is populated. |
| Retrieve PDF | `getPdf` | Retrieves a generated Placid PDF by its id. Poll this while the status is queued; once it turns finished the PDF URL is populated. |
| Retrieve Video | `getVideo` | Retrieves a generated Placid video by its id. Poll this while the status is queued; once it turns finished the video URL is populated. |
| Update Collection | `updateCollection` | Updates a Placid template collection. Template UUIDs replaces the whole membership list, while Add Template UUIDs and Remove Template UUIDs adjust it incrementally. Only the fields you supply change. |
| Update Font | `updateFont` | Renames a custom font in the Placid project. The font file itself cannot be replaced - upload a new font instead. |
| Update Template | `updateTemplate` | Updates a Placid template's title, tags or custom reference data. Only the fields you supply change. The template's design is edited in the Placid editor, not through this endpoint. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Image Render Completed | `image` | Fires when Placid finishes rendering an image. Placid has no webhook-registration API - the callback is set per render: copy this trigger's URL and pass it as the Success Webhook URL input on the Create Image action (the webhook_success field). Placid then POSTs the finished image object to it. Check status in the payload: it is finished on success and error when the render failed. Placid does not sign these deliveries, so there is no signature to verify - compare the passthrough value you sent if you need to authenticate the callback. Payload schema captured from a real Placid render. |
| PDF Render Completed | `pdf` | Fires when Placid finishes rendering a PDF. Placid has no webhook-registration API - the callback is set per render: copy this trigger's URL and pass it as the Success Webhook URL input on the Create PDF action (the webhook_success field). Placid then POSTs the finished PDF object to it. Check status in the payload: it is finished on success and error when the render failed. Placid does not sign these deliveries, so there is no signature to verify - compare the passthrough value you sent if you need to authenticate the callback. Payload schema captured from a real Placid render. |
| Video Render Completed | `video` | Fires when Placid finishes rendering a video. Placid has no webhook-registration API - the callback is set per render: copy this trigger's URL and pass it as the Success Webhook URL input on the Create Video action (the webhook_success field). Placid then POSTs the finished video object to it. Check status in the payload: it is finished on success and error when the render failed. Placid does not sign these deliveries, so there is no signature to verify - compare the passthrough value you sent if you need to authenticate the callback. Payload schema modelled on the image and PDF callbacks, which were captured from real renders, plus Placid's documented video object; no video render was made during this build because Placid charges 10 credits per 10 seconds. |
