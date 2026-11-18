---
description: "GenerateBanners.com automates visual marketing: manage image templates, browse the public template library and Google Fonts catalogue, and render on-brand…"
hidden: true
---

# GenerateBanners.com

<img src="../../.gitbook/assets/connectors/generate-banners.png" alt="GenerateBanners.com logo" width="64">

GenerateBanners.com automates visual marketing: manage image templates, browse the public template library and Google Fonts catalogue, and render on-brand banner images (Open Graph images, social cards, ad creatives) from a template plus variable values. Wraps the https://api.generatebanners.com/api/v1 REST API.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [generatebanners.com](https://generatebanners.com) |
| **Authentication** | API key |
| **Slug** | `generateBanners` |

## Use it

Add GenerateBanners.com from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.generateBanners.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check API Availability | `checkApiAvailability` | Pings the root of the GenerateBanners.com API and returns the plain-text string OK when the service is reachable. Needs no credentials, so it distinguishes a service outage from an authentication problem. Free - consumes no render credits. |
| Create Template | `createTemplate` | Creates a new image template in your GenerateBanners.com workspace from a name, canvas size and optional layer structure. The server derives the template's render variables from the layers you supply. Free - consumes no render credits. Use Delete Template to remove it again. |
| Delete Template | `deleteTemplate` | Permanently deletes an image template from your GenerateBanners.com workspace. This cannot be undone. Note that signed URLs already issued for the template keep serving their cached image afterwards, so deleting a template does not revoke public links. Returns HTTP 204 with an empty body, so confirm the deletion with List Templates. Free - consumes no render credits. |
| Download Signed Image | `downloadSignedImage` | Fetches the rendered image bytes behind a short signed URL previously issued by Get Template Signed URL. Pass only the short code from the end of that URL. SECURITY: this endpoint needs no credentials, so anyone holding the code can retrieve the image. Free - the credit was already charged when the signed URL was issued. |
| Get Account Identity | `getAccountIdentity` | Returns the identity the current credentials authenticate as: the public API key in use and the id of the GenerateBanners.com workspace it belongs to. Useful as a connection health check. SECURITY: the response echoes your own public API key, so treat its output as credential-bearing. Free - consumes no render credits. |
| Get Credit Usage | `getCreditUsage` | Returns the current billing period's render-credit usage and the plan allowance, so you can check the remaining quota before running a batch of renders. Each render or signed-URL call consumes one credit. Free - consumes no render credits. |
| Get Library Template | `getLibraryTemplate` | Returns one ready-made design from the shared GenerateBanners.com library, including its full layer structure. Feed that structure straight into Create Template to copy the design into your own workspace. Free - consumes no render credits. |
| Get Template | `getTemplate` | Returns the full metadata of one image template: its dimensions, category, layer structure and the complete list of variable names that can be overridden when rendering it. Free - consumes no render credits. |
| Get Template Signed URL | `getTemplateSignedUrl` | Returns a short, HMAC-signed public image URL for a template rendered with the supplied variable values. The returned URL can be embedded directly in a web page or email without exposing your secret API key. WARNING: the returned URL is publicly reachable by anyone who has it. Consumes 1 render credit per call. |
| List Available Fonts | `listAvailableFonts` | Lists every font family that can be used on a text layer, covering the full Google Fonts catalogue plus any custom fonts uploaded to your workspace. Use a returned fontFamily value as the font property of a text layer. The API answers with a bare JSON array, currently about 1966 entries, exposed here under the items key. Free - consumes no render credits. |

<details>

<summary>See 4 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Library Templates | `listLibraryTemplates` | Lists the ready-made templates in the shared GenerateBanners.com starter library, grouped by category such as Blog, Podcast or Product, with each design's dimensions and render variables. Use a library id with Get Library Template to inspect its layer structure before copying it into your own workspace. Free - consumes no render credits. |
| List Templates | `listTemplates` | Lists the metadata of all image templates in your GenerateBanners.com workspace, including each template's id, name, category, pixel dimensions and the variables it exposes for rendering. Supports page/limit pagination. Free - consumes no render credits. |
| Render Template Image | `renderTemplateImage` | Renders a template into a finished image and returns the image bytes directly (JPEG by default). Pass one extra top-level property per template variable you want to override. Consumes 1 render credit per call and is rate-limited to 100 renders per 15 minutes per API key. To embed the image on a page instead of downloading it, use Get Template Signed URL. |
| Update Template | `updateTemplate` | Updates an existing image template in place: rename it, resize the canvas, replace its layer structure or variables, or toggle public sharing. Only the fields you supply are changed. Returns HTTP 204 with an empty body, so confirm the change with Get Template. Free - consumes no render credits. |

</details>
