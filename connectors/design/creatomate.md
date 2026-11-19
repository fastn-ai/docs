---
description: "Creatomate is a media automation platform for generating videos, images and GIFs from reusable templates or raw RenderScript."
hidden: true
---

# Creatomate

<img src="../../.gitbook/assets/connectors/lg/creatomate.png" alt="Creatomate logo">

Creatomate is a media automation platform for generating videos, images and GIFs from reusable templates or raw RenderScript. This connector covers the Creatomate REST API: creating and tracking renders, full template CRUD, and reading data feeds.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [creatomate.com](https://creatomate.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `creatomate` |

## Use it

Add Creatomate from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.creatomate.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Render</td><td><code>createRender</code></td><td>Queues a video, image or GIF render. Supply either a Template ID with Modifications, or a raw RenderScript document using the Elements field and the output settings alongside it. WARNING - this spends render credits and queues real work unless Dry Run is set to true; with Dry Run the request only validates and returns the effective RenderScript at no cost. A second warning: Output Format defaults to jpg, so a video render without it silently produces a still image. Returns 202 with the queued render; poll Get Render or supply Webhook URL for completion.</td></tr><tr><td>Create Renders Batch</td><td><code>createRendersBatch</code></td><td>Queues one or more renders through the v1 endpoint, which always returns an array. Unlike Create Render it accepts Tags, which renders EVERY template in the project carrying those tags - one paid render per matching template - and Transcripts for supplying your own subtitle timings. WARNING - this endpoint has NO dry-run mode: it was verified live that a dry_run flag is silently ignored here and the render is queued and charged anyway. Every call spends render credits. Verify which templates a tag matches with List Templates first, and use Create Render with Dry Run when you only want to validate.</td></tr><tr><td>Create Template</td><td><code>createTemplate</code></td><td>Creates a new template in the Creatomate project from a RenderScript document. Creating a template costs no render credits. The RenderScript root must set output_format explicitly - it defaults to jpg, so a video template without it produces a still image. Returns the created template including its id.</td></tr><tr><td>Delete Template</td><td><code>deleteTemplate</code></td><td>Soft-deletes a Creatomate template. The template is removed from the project but stays recoverable for 30 days through Creatomate support. Automations and scheduled renders that reference the template id stop working immediately. Returns HTTP 204 with an empty body on success, and 404 with the hint 'No template was found with that ID.' for an unknown id.</td></tr><tr><td>Get Feed</td><td><code>getFeed</code></td><td>Retrieves a single Creatomate data feed by its id, including its configuration. Note that an unknown feed id is answered with HTTP 400 and the hint 'No feed was found with that ID.' rather than a 404.</td></tr><tr><td>Get Feed Sample</td><td><code>getFeedSample</code></td><td>Returns the most recent rows of a Creatomate data feed, so you can inspect the column names and values that drive bulk generation before wiring them into template modifications. An unknown feed id is answered with HTTP 400 and the hint 'No feed was found with that ID.'</td></tr><tr><td>Get Render</td><td><code>getRender</code></td><td>Retrieves the status and result of a single render by its id. Once the status is succeeded the response carries the output file URL, which stays hosted for 30 days after the render was created; when the status is failed, read the error message. For tracking many renders at once prefer a webhook over polling, because the API allows only 30 requests per 10 seconds per account.</td></tr><tr><td>Get Template</td><td><code>getTemplate</code></td><td>Retrieves a single Creatomate template by its id, including the full RenderScript source document that the list endpoint omits. Returns a 404 with the hint 'No template was found with that ID.' when the id does not exist in the project.</td></tr><tr><td>List Feeds</td><td><code>listFeeds</code></td><td>Returns every data feed configured in the Creatomate project. Feeds are spreadsheet or API data sources that drive bulk generation, where each row becomes one render. Feeds are created and configured in the Creatomate dashboard, not through the API.</td></tr><tr><td>List Templates</td><td><code>listTemplates</code></td><td>Returns every template in the Creatomate project the API key belongs to, as a compact list. The RenderScript source is never included in this list response - use Get Template to retrieve a single template with its source. Optionally filter the list to templates carrying specific tags.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Update Template</td><td><code>updateTemplate</code></td><td>Partially updates a Creatomate template. Only the fields you supply are changed - name, tags and the RenderScript source can each be updated independently. Replacing the source of a template that automations already use can break those automations, because modifications match on element names.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Render Failed</td><td><code>failed</code></td><td>Fires when a Creatomate render fails. The payload is the render record with status 'failed' and an error_message explaining the cause. Creatomate has no webhook-registration API, so the fastn trigger URL must be registered by hand, in either of two places: (1) per render - pass the trigger URL as the Webhook URL input on the Create Render or Create Renders Batch action; or (2) as a project default - in the Creatomate dashboard go to Project Settings &gt; Webhooks and paste the trigger URL into the default webhook URL field, then save. Creatomate does not sign its webhook requests, so no signature verification is possible.</td></tr><tr><td>Render Succeeded</td><td><code>succeeded</code></td><td>Fires when a Creatomate render finishes successfully. The payload is the full render record and 'url' points at the finished file, which stays hosted for 30 days. Creatomate has no webhook-registration API, so the fastn trigger URL must be registered by hand, in either of two places: (1) per render - pass the trigger URL as the Webhook URL input on the Create Render or Create Renders Batch action; or (2) as a project default - in the Creatomate dashboard go to Project Settings &gt; Webhooks and paste the trigger URL into the default webhook URL field, then save. Creatomate does not sign its webhook requests, so no signature verification is possible.</td></tr></tbody></table>
