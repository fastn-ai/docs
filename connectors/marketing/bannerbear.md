---
description: "Bannerbear is an API for automatically generating images, videos, screenshots, animated GIFs, movies and PDFs at scale for marketing automation, ad creative,…"
---

# Bannerbear

Bannerbear is an API for automatically generating images, videos, screenshots, animated GIFs, movies and PDFs at scale for marketing automation, ad creative, and dynamic content workflows. Covers Templates, Video Templates, Template Sets, Images, Videos, Collections, Animated GIFs, Screenshots, Movies, Sessions, Webhooks, Projects, PDF utilities, Diagnoses, Fonts and Effects.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [bannerbear.com](https://bannerbear.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 44 |
| **Events** | 0 |
| **Slug** | `bannerbear` |

## Use it

Add Bannerbear from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bannerbear.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Authorization | `checkAuthorization` | Verify the API key is valid and see which project it is scoped to. Free, read-only, no credits consumed. |
| Create Animated GIF | `createAnimatedGif` | Generate an animated GIF from a sequence of per-frame modifications on a template (max 30 frames). Consumes API credits. |
| Create Collection | `createCollection` | Render one image per template in a template set, in a single call. Consumes 1 API credit per template in the set. |
| Create Diagnosis | `createDiagnosis` | Run a diagnostic report on a previously generated image, e.g. to check whether any external image_url modifications failed to load. Free. |
| Create Image | `createImage` | Generate an image from a template. Consumes 1 API credit (3x if render_pdf is set). Returns immediately with status 'pending' unless the template is simple enough to render synchronously. |
| Create Movie | `createMovie` | Compose multiple video/image clips into a single movie with transitions and an optional soundtrack. Consumes API credits proportional to output length. |
| Create Project | `createProject` | Create a new project in the account. Per Bannerbear docs this requires a Master API Key (not a Project API Key) - with a Project key it is expected to return an auth/tier error, which still proves the route is real. |
| Create Screenshot | `createScreenshot` | Take a screenshot of a website URL. Consumes 1 API credit. |
| Create Session | `createSession` | Create a secure, embeddable template editor session URL (expires after 2 hours). Free - does not render anything. |
| Create Signed Base | `createSignedBase` | Create a signed-URL base for a template, enabling on-the-fly image generation via a signed GET URL (no API call needed to render). Free. |
| Create Template | `createTemplate` | Create a new blank template of a given size. Free - defines a design canvas, does not render anything. Layers must then be added via the Bannerbear editor UI or a session URL. |
| Create Template Set | `createTemplateSet` | Group existing templates into a template set so a single Collection call can render all of them together. Free - references existing templates, does not render anything. |
| Create Video | `createVideo` | Render a video from a video template (Overlay, Transcribe or Multi Overlay build pack). Consumes API credits proportional to output length - can be significantly more expensive than an image. |
| Create Video Template | `createVideoTemplate` | Create a video template from an existing parent image template. Free - defines a render recipe, does not render anything itself. |
| Create Webhook | `createWebhook` | Register a project-level webhook that fires for a given event type across the whole project (distinct from the static per-project webhook signing key). Free. |
| Delete Template | `deleteTemplate` | Permanently delete a template. Free. |
| Delete Webhook | `deleteWebhook` | Unregister a project-level webhook. Free. |
| Duplicate Template | `duplicateTemplate` | Duplicate an existing template, including its layers. Free. |
| Get Account | `getAccount` | Retrieve account-level status: plan name, API usage and quota. Per Bannerbear docs this requires a Master API Key (not a Project API Key) - with a Project key it is expected to return an auth/tier error, which still proves the route is real. |
| Get Animated GIF | `getAnimatedGif` | Retrieve a single animated GIF by UID. Free, read-only. |
| Get Collection | `getCollection` | Retrieve a single collection by UID. Free, read-only. |
| Get Diagnosis | `getDiagnosis` | Retrieve a single diagnosis report by UID. Free, read-only. |
| Get Image | `getImage` | Retrieve a single image by UID, including its render status and final image_url once complete. Free, read-only. |
| Get Movie | `getMovie` | Retrieve a single movie by UID. Free, read-only. |
| Get PDF Join | `getPdfJoin` | Retrieve a single PDF join operation by UID. Free, read-only. |
| Get PDF Rasterize | `getPdfRasterize` | Retrieve a single PDF rasterize operation by UID. Free, read-only. |
| Get Project | `getProject` | Retrieve a single project by UID. Per Bannerbear docs this requires a Master API Key. |
| Get Screenshot | `getScreenshot` | Retrieve a single screenshot by UID. Free, read-only. |
| Get Session | `getSession` | Retrieve a single editor session by UID. Free, read-only. |
| Get Template | `getTemplate` | Retrieve a single template by UID. Free, read-only. |
| Get Template Set | `getTemplateSet` | Retrieve a single template set by UID. Free, read-only. |
| Get Video | `getVideo` | Retrieve a single video by UID, including render progress and final video_url once complete. Free, read-only. |
| Get Video Template | `getVideoTemplate` | Retrieve a single video template by UID. Free, read-only. |
| Get Webhook | `getWebhook` | Retrieve a single registered webhook by UID. Free, read-only. |
| Hydrate Project | `hydrateProject` | Copy templates from another project into this one. Per Bannerbear docs this requires a Master API Key. |
| Import Templates | `importTemplates` | Import one or more templates from Bannerbear's public template library into this project by Publication ID. Free. |
| Join PDFs | `joinPdfs` | Join multiple PDF files into a single PDF. Consumes API credits (shared with the image/video/screenshot quota). |
| List Animated GIFs | `listAnimatedGifs` | List all animated GIFs in the project. Free, read-only. |
| List Collections | `listCollections` | List all collections in the project. Free, read-only. |
| List Effects | `listEffects` | List all image effect names available for the 'effect' modification field. Free, read-only. |
| List Fonts | `listFonts` | List all fonts available for use in templates, grouped by category. Free, read-only. |
| List Images | `listImages` | List all generated images in the project. Free, read-only. |
| List Movies | `listMovies` | List all movies in the project. Free, read-only. |
| List Projects | `listProjects` | List all projects in the account. Per Bannerbear docs this requires a Master API Key. |
