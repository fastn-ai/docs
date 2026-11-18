---
description: "Orshot generates images, PDFs and videos from reusable templates."
hidden: true
---

# Orshot

<img src="../../.gitbook/assets/connectors/lg/orshot.png" alt="Orshot logo">

Orshot generates images, PDFs and videos from reusable templates. This connector wraps the Orshot v1 REST API: studio and library (utility) template rendering, signed render URLs, async render jobs, brand assets (images, videos, audio, colors, fonts), template folders, sharing and versions, AI video generation, social publishing and analytics, workflows, and workspace profile and logs.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [orshot.com](https://orshot.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Slug** | `orshot` |

## Use it

Add Orshot from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.orshot.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Brand Color | `addBrandColor` | Save a brand color to the workspace so it can be reused in templates. Accepts a solid CSS color or a gradient string, with optional tags. |
| Bulk Create Studio Templates | `bulkCreateStudioTemplates` | Create several studio templates in one request from a JSON array of template definitions. Requires an Enterprise-plan workspace; other plans receive a 403 naming the templateCreation feature. |
| Cancel Render Job | `cancelRenderJob` | Cancel an asynchronous render job that has not started yet. A render already in progress completes and is billed normally, and a canceled job fires no webhook. |
| Create Signed Render URL | `createSignedRenderUrl` | Generate a signed, shareable render URL for a template so the image can be rendered publicly without exposing the API key. Only templates whose renderType is images can be signed. Creating the URL costs nothing; every access to it triggers a render that consumes a render credit. |
| Create Studio Template | `createStudioTemplate` | Create a studio template programmatically with a canvas size and optional page structure. Requires an Enterprise-plan workspace; other plans receive a 403 naming the templateCreation feature. |
| Create Template Folder | `createTemplateFolder` | Create a folder for grouping studio templates. Template folders require a paid plan; free workspaces receive a 403 with the code folders_paid_plan_required. |
| Create Workflow | `createWorkflow` | Create a bulk-generation workflow from an ordered list of steps. Workflows are an Enterprise API feature; other plans receive a 403 naming the workflows feature. |
| Delete Brand Audio | `deleteBrandAudio` | Permanently remove a stored brand audio file from the workspace. |
| Delete Brand Color | `deleteBrandColor` | Permanently remove a saved brand color from the workspace. Templates already rendered are unaffected. |
| Delete Brand Image | `deleteBrandImage` | Permanently remove a stored brand image from the workspace. |

<details>

<summary>See 79 more actions</summary>

* **Delete Brand Video** `deleteBrandVideo`: Permanently remove a stored brand video from the workspace.
* **Delete Custom Font** `deleteCustomFont`: Permanently remove an uploaded custom font from the workspace. Templates still referencing it fall back to a default font.
* **Delete Studio Template** `deleteStudioTemplate`: Permanently delete a studio template from the workspace. Images already rendered from it remain available at their stored URLs.
* **Delete Template Folder** `deleteTemplateFolder`: Delete a template folder from the workspace. Templates inside it are not deleted, only moved out of the folder. Template folders require a paid plan.
* **Delete Template Version** `deleteTemplateVersion`: Remove one version from a studio template's timeline. The live template is unchanged. Requires an Enterprise-plan workspace.
* **Delete Workflow** `deleteWorkflow`: Permanently delete a workflow from the workspace. Its past runs stop being reachable. Workflows are an Enterprise API feature.
* **Discard Social Post** `discardSocialPost`: Delete a draft social post or cancel one that is scheduled. Posts already published to a platform are not retracted.
* **Duplicate Studio Template** `duplicateStudioTemplate`: Copy an existing studio template into a new one, optionally into a different workspace and under a new name. Requires an Enterprise-plan workspace.
* **Duplicate Template Version** `duplicateTemplateVersion`: Create a brand new studio template from an earlier version, leaving the live template untouched. Requires an Enterprise-plan workspace.
* **Estimate AI Video Credits** `estimateAiVideoCredits`: Price an AI video before generating it. Send the same body you would send to Generate AI Video and receive the AI credit cost, with nothing generated and no credits spent.
* **Generate AI Video** `generateAiVideo`: Generate a short AI video from a prompt, animate a still image, or make a photo speak. Billed in AI credits per second of output, so call Estimate AI Video Credits first. Returns a job to poll unless sync is true.
* **Generate Studio Template Variants** `generateStudioTemplateVariants`: Use AI to produce several size variants of an existing studio template in one call. Requires an Enterprise-plan workspace.
* **Get Daily Social Analytics** `getDailySocialAnalytics`: Read day-by-day social metrics across the connected accounts, with a per-platform breakdown.
* **Get Library Template** `getLibraryTemplate`: Retrieve one Orshot library (utility) template by its slug, for example website-screenshot or tweet-image. Undocumented in the OpenAPI spec but live on the v1 API.
* **Get Library Template By Render Type** `getLibraryTemplateByRenderType`: Retrieve one Orshot library (utility) template scoped to a render type, for example images and website-screenshot. Undocumented in the OpenAPI spec but live on the v1 API.
* **Get Profile And Workspaces** `getProfileAndWorkspaces`: Retrieve the Orshot profile behind the API key together with its workspaces, current plan, render-credit balance and AI-credit balance. Use this to check remaining credits before running a render.
* **Get Render Job** `getRenderJob`: Poll one asynchronous render job by id until its finished flag turns true, then read its result or its error. A job id belonging to another workspace answers 404.
* **Get Social Analytics Overview** `getSocialAnalyticsOverview`: Read cross-account social analytics for the workspace: totals, per-post metrics and follower counts over a date range.
* **Get Social Post** `getSocialPost`: Read one social post, including its per-account delivery status and the live URLs of anything already published.
* **Get Social Post Analytics** `getSocialPostAnalytics`: Read one social post's full metrics together with its day-by-day timeline.
* **Get Social Posting Insights** `getSocialPostingInsights`: Read the best times to post, posting frequency and engagement decay computed from the workspace's own posting history.
* **Get Studio Template** `getStudioTemplate`: Retrieve one studio template of the workspace by its numeric id, including its canvas size, pages and layer modifications.
* **Get Studio Template (Short Path)** `getStudioTemplateShortPath`: Retrieve one studio template through the short alias path /v1/studio/{templateId}. This route is undocumented, is live on the v1 API and returns the same template as Get Studio Template.
* **Get Template Sharing** `getTemplateSharing`: Read the public sharing state of a studio template, including its share links and view statistics.
* **Get Template Version** `getTemplateVersion`: Read one version of a studio template, optionally including its full design snapshot. Requires an Enterprise-plan workspace.
* **Get Workflow** `getWorkflow`: Read one workflow with its full step definition. Workflows are an Enterprise API feature.
* **Get Workflow Run** `getWorkflowRun`: Fetch one execution of an Orshot workflow by run id, including its per-step status and output. Requires an Enterprise plan: on any lower plan every /v1/workflows route answers 403 enterprise_required.
* **Get Workflow Sharing** `getWorkflowSharing`: Read the public sharing settings of an Orshot workflow, including whether it is publicly shared and its share link. Requires an Enterprise plan: on any lower plan every /v1/workflows route answers 403 enterprise_required.
* **Get Workspace** `getWorkspace`: Retrieve the details of the Orshot workspace the API key belongs to, including its title, slug and settings.
* **List AI Presets** `listAiPresets`: List the role and look presets available for AI video generation, each with a preview clip, together with the current AI credit rate card.
* **List Brand Audio** `listBrandAudio`: List the brand audio files stored in the workspace, optionally filtered to a single tag.
* **List Brand Colors** `listBrandColors`: List the brand colors saved in the workspace, optionally filtered to a single tag.
* **List Brand Images** `listBrandImages`: List the brand images stored in the workspace, optionally filtered to a single tag.
* **List Brand Videos** `listBrandVideos`: List the brand videos stored in the workspace, optionally filtered to a single tag.
* **List Custom Fonts** `listCustomFonts`: List the custom fonts uploaded to the workspace, optionally filtered to a single tag.
* **List Library Template Modifications** `listLibraryTemplateModifications`: List the modification keys a library (utility) template accepts, with each key's type, description and example values. Use this before calling Render From Library Template. Undocumented in the OpenAPI spec but live on the v1 API.
* **List Library Templates** `listLibraryTemplates`: List every Orshot library (utility) template, such as Website Screenshot, Tweet Screenshot and Dynamic Image Resizer, with its slug, title, description and render type. Undocumented in the OpenAPI spec but live on the v1 API.
* **List Library Templates By Render Type** `listLibraryTemplatesByRenderType`: List the Orshot library (utility) templates that produce a given render type. Only images is populated today; pdfs and videos return a not-found message. Undocumented in the OpenAPI spec but live on the v1 API.
* **List Plans** `listPlans`: List the Orshot subscription plans with their monthly and annual prices, render-credit allowances and feature limits. Undocumented in the OpenAPI spec but live on the v1 API.
* **List Render Jobs** `listRenderJobs`: List the workspace's asynchronous render jobs, newest first, optionally filtered by status and paged with a cursor. Job records are removed seven days after creation; the rendered files are unaffected.
* **List Social Accounts** `listSocialAccounts`: List the social media accounts connected to the workspace, which are the accounts Publish To Social can target.
* **List Social Analytics Accounts** `listSocialAnalyticsAccounts`: Read follower counts, growth and daily follower history for each connected social account.
* **List Social Posts** `listSocialPosts`: List the social posts of the workspace, newest first, filtered by status, platform or account and paged with a cursor.
* **List Studio Templates** `listStudioTemplates`: List the studio templates that belong to the workspace, with pagination, free-text search and tag filtering.
* **List Studio Templates (Short Path)** `listStudioTemplatesShortPath`: List the workspace's studio templates through the short unpaginated path documented in the Orshot agent auth guide. Prefer List Studio Templates, which supports pagination, search and tags. This route answers 403 with an explanatory body while the workspace has no studio templates.
* **List Template Folders** `listTemplateFolders`: List the template folders that organise the studio templates of the workspace.
* **List Template Versions** `listTemplateVersions`: Read the version timeline of a studio template, showing what each version changed and whether the current plan may restore it. Requires an Enterprise-plan workspace.
* **List Workflow Runs** `listWorkflowRuns`: List the execution history of one Orshot workflow, newest first. Requires an Enterprise plan: on any lower plan every /v1/workflows route answers 403 enterprise_required.
* **List Workflows** `listWorkflows`: List the bulk-generation workflows in the workspace, filtered by status and paged with limit and offset. Workflows are an Enterprise API feature.
* **List Workspace Logs** `listWorkspaceLogs`: List the render and API request logs of the workspace, newest first, with cursor pagination and optional filters by status, request source, template, output format and date range.
* **Move Studio Template To Folder** `moveStudioTemplateToFolder`: Move a studio template into a template folder, or out of its current folder. Template folders require a paid plan.
* **Name Current Template Version** `nameCurrentTemplateVersion`: Save the template exactly as it stands under a label. Named versions are never pruned from the timeline. Requires an Enterprise-plan workspace.
* **Publish Held Social Post** `publishHeldSocialPost`: Send a draft or scheduled social post to its platforms immediately. This publishes publicly visible content, so use it only on a post you intend to go live now.
* **Publish To Social** `publishToSocial`: Publish an image or video to connected social accounts, or save it as a draft or a scheduled post. Set status to draft or scheduled to avoid posting immediately.
* **Rename Template Folder** `renameTemplateFolder`: Change the display name of a template folder. Template folders require a paid plan.
* **Rename Template Version** `renameTemplateVersion`: Give a template version a name, or rename one that already has a label. Requires an Enterprise-plan workspace.
* **Render From Library Template** `renderFromLibraryTemplate`: Render an image or PDF from an Orshot library (utility) template such as website-screenshot or tweet-image. Each render consumes one render credit per image or PDF page. Call List Library Template Modifications first to learn the modification keys the chosen template accepts.
* **Render From Signed URL** `renderFromSignedUrl`: Render an image through the public GET form of the render endpoint using the signature produced by Create Signed Render URL. Pass every query parameter that appears in the signed URL, including each modification key, exactly as issued - changing any value invalidates the signature. Each call consumes one render credit and returns the image bytes.
* **Render From Studio Template** `renderFromStudioTemplate`: Render an image, PDF or video from a template designed in Orshot Studio, optionally publishing the result to connected social accounts. Set response.mode to async to receive a render job instead of waiting. Each render consumes render credits: one per image, per PDF page or per video second.
* **Restore Template Version** `restoreTemplateVersion`: Put an earlier design back on the live studio template, recorded as a new step on its timeline so nothing is lost. Requires an Enterprise-plan workspace.
* **Run Workflow** `runWorkflow`: Execute an Orshot workflow now, passing its input variables in the body. Each render step the workflow performs consumes render credits. Requires an Enterprise plan: on any lower plan every /v1/workflows route answers 403 enterprise_required.
* **Search Brand Assets** `searchBrandAssets`: Search across every brand asset type in the workspace at once - images, colors, fonts, videos and audio - and receive the matches grouped by type with a total per group.
* **Update Brand Audio Tags** `updateBrandAudioTags`: Replace the tags on a stored brand audio file. The tags array you send becomes the complete tag list for that file.
* **Update Brand Color Tags** `updateBrandColorTags`: Replace the tags on a saved brand color. The tags array you send becomes the complete tag list for that color.
* **Update Brand Image Tags** `updateBrandImageTags`: Replace the tags on a stored brand image. The tags array you send becomes the complete tag list for that image.
* **Update Brand Video Tags** `updateBrandVideoTags`: Replace the tags on a stored brand video. The tags array you send becomes the complete tag list for that video.
* **Update Custom Font Tags** `updateCustomFontTags`: Replace the tags on an uploaded custom font. The tags array you send becomes the complete tag list for that font.
* **Update Profile** `updateProfile`: Update the display name, work role and work URL on the Orshot profile that owns the API key. Only the fields you supply are changed.
* **Update Social Post** `updateSocialPost`: Edit a draft or scheduled social post before it goes out, changing its copy, media, target accounts, status or schedule.
* **Update Studio Template** `updateStudioTemplate`: Change a studio template's name, description, tags, canvas dimensions or complete page structure. Requires an Enterprise-plan workspace.
* **Update Studio Template Modifications** `updateStudioTemplateModifications`: Change the text, images, videos, styles and spoken narration held in a studio template's layers without replacing the whole design. Requires an Enterprise-plan workspace.
* **Update Template Sharing** `updateTemplateSharing`: Turn public sharing on or off for a studio template and choose whether visitors may duplicate it into their own workspace.
* **Update Workflow** `updateWorkflow`: Change a workflow's steps, status, name, description or metadata. Workflows are an Enterprise API feature.
* **Update Workflow Sharing** `updateWorkflowSharing`: Turn public sharing of an Orshot workflow on or off, and choose whether a copier also receives the workflow's template. Requires an Enterprise plan: on any lower plan every /v1/workflows route answers 403 enterprise_required.
* **Update Workspace** `updateWorkspace`: Rename the Orshot workspace or change its slug. Changing the slug alters every workspace-scoped public URL, so supply it only when you intend that.
* **Upload Brand Audio** `uploadBrandAudio`: Store an audio file in the workspace brand library. Supply the file as a publicly reachable URL; Orshot downloads it server-side. The docs describe a multipart upload, but the endpoint also accepts this JSON form.
* **Upload Brand Image** `uploadBrandImage`: Store an image in the workspace brand library so templates can reference it. The file may be supplied as a public URL or as a base64 data string.
* **Upload Brand Video** `uploadBrandVideo`: Store a video in the workspace brand library. Supply the file as a publicly reachable URL; Orshot downloads it server-side. The docs describe a multipart upload, but the endpoint also accepts this JSON form.
* **Upload Custom Font** `uploadCustomFont`: Upload a custom font to the workspace so templates can use it. Supply the font as a publicly reachable URL pointing directly at a font file. The docs describe a multipart upload, but the endpoint also accepts this JSON form.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Render Job Finished | `render_job.finished` | Fires when an asynchronous Orshot render job reaches a terminal status (succeeded or failed). Orshot has NO webhook subscription registry - there is no /v1/webhooks or /v1/events route (both return 404 route_not_found). Registration is PER REQUEST: copy this trigger's fastn webhook URL and pass it as the top-level `webhook_url` field of the render request that should notify you - either POST /v1/studio/render with response.mode set to "async" (action: Render From Studio Template), or POST /v1/ai/video (action: Generate AI Video). Optionally also pass a top-level `metadata` string, which Orshot echoes back inside job.metadata so you can correlate the delivery with your own record. The URL must be publicly reachable over http(s); private and loopback addresses are rejected at create time. Orshot attempts delivery 3 times (immediately, +30s, +2m) with a 10-second timeout each and treats any 2xx as an acknowledgement. Jobs you cancel do NOT fire; every other terminal status does. Webhooks are a convenience only - polling Get Render Job remains the vendor's source of truth. |
