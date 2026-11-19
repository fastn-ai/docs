---
description: "Google Forms is an online form builder. Create and update forms, read responses, set publish settings, and watch for new responses."
hidden: true
---

# Google Forms

<img src="../../.gitbook/assets/connectors/lg/google-forms.png" alt="Google Forms logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [forms.google.com](https://forms.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleForms` |

## Setup

Your customers sign in to Google Forms through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Forms from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleForms.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Update Form</td><td><code>batchUpdateForm</code></td><td>Apply a batch of updates to a form: update Form.info, update FormSettings (e.g. quiz mode), create/move/update/delete an item (question, question group, page break, text, image, video). All requests in the batch either all succeed or none do. Requires forms.body scope.</td></tr><tr><td>Create Form</td><td><code>createForm</code></td><td>Create a new Google Form using only the title (and optionally description/documentTitle) given in info. Items, settings, and other form content cannot be set at creation time and must be added afterwards via Batch Update Form. Requires forms.body scope.</td></tr><tr><td>Create Watch</td><td><code>createWatch</code></td><td>Create a Pub/Sub watch on a form for either SCHEMA (form content/settings changes) or RESPONSES (new submissions) events. The target Pub/Sub topic must already exist, be owned by the calling GCP project, and grant publish privileges to serviceAccount:forms-notifications@system.gserviceaccount.com. A watch expires 7 days after creation unless renewed. Requires forms.body, forms.body.readonly, or forms.responses.readonly scope depending on eventType.</td></tr><tr><td>Delete Watch</td><td><code>deleteWatch</code></td><td>Delete a watch on a form.</td></tr><tr><td>Get Form</td><td><code>getForm</code></td><td>Get a form's full definition: info, settings, items (questions/pages/media), revisionId, responderUri, and linkedSheetId (if responses are linked to a Sheet). Requires forms.body or forms.body.readonly scope (or a Drive scope).</td></tr><tr><td>Get Form Response</td><td><code>getFormResponse</code></td><td>Get a single response to a form, including per-question answers and (for quizzes) grading. Requires forms.responses.readonly scope.</td></tr><tr><td>List Form Responses</td><td><code>listFormResponses</code></td><td>List a form's responses, optionally filtered by submission timestamp. Requires forms.responses.readonly scope.</td></tr><tr><td>List Watches</td><td><code>listWatches</code></td><td>List the Pub/Sub watches owned by the invoking GCP project for a form.</td></tr><tr><td>Renew Watch</td><td><code>renewWatch</code></td><td>Renew an existing watch for another 7 days from now. Takes no request body fields.</td></tr><tr><td>Set Publish Settings</td><td><code>setPublishSettings</code></td><td>Update a form's publish settings: whether it is published/visible and whether it is accepting responses. Setting isAcceptingResponses=true requires isPublished=true (setting both false while the other true is rejected). Requires forms.body, drive, or drive.file scope.</td></tr></tbody></table>

## Events

Google Forms has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
