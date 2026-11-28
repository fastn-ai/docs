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

Your customers sign in to Google Forms through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Forms from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Forms**.
2. Select **Connect** on the Google Forms card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Forms and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Forms's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Update Form</td><td><code>batchUpdateForm</code></td><td>Apply a batch of updates to a form: update Form.info, update FormSettings (e.g. quiz mode), create/move/update/delete an item (question, question group, page break, text, image, video). All requests in the batch either all succeed or none do. Requires forms.body scope.</td></tr><tr><td>Create Form</td><td><code>createForm</code></td><td>Create a new Google Form using only the title (and optionally description/documentTitle) given in info. Items, settings, and other form content cannot be set at creation time and must be added afterwards via Batch Update Form. Requires forms.body scope.</td></tr><tr><td>Create Watch</td><td><code>createWatch</code></td><td>Create a Pub/Sub watch on a form for either SCHEMA (form content/settings changes) or RESPONSES (new submissions) events. The target Pub/Sub topic must already exist, be owned by the calling GCP project, and grant publish privileges to serviceAccount:forms-notifications@system.gserviceaccount.com. A watch expires 7 days after creation unless renewed. Requires forms.body, forms.body.readonly, or forms.responses.readonly scope depending on eventType.</td></tr><tr><td>Delete Watch</td><td><code>deleteWatch</code></td><td>Delete a watch on a form.</td></tr><tr><td>Get Form</td><td><code>getForm</code></td><td>Get a form's full definition: info, settings, items (questions/pages/media), revisionId, responderUri, and linkedSheetId (if responses are linked to a Sheet). Requires forms.body or forms.body.readonly scope (or a Drive scope).</td></tr><tr><td>Get Form Response</td><td><code>getFormResponse</code></td><td>Get a single response to a form, including per-question answers and (for quizzes) grading. Requires forms.responses.readonly scope.</td></tr><tr><td>List Form Responses</td><td><code>listFormResponses</code></td><td>List a form's responses, optionally filtered by submission timestamp. Requires forms.responses.readonly scope.</td></tr><tr><td>List Watches</td><td><code>listWatches</code></td><td>List the Pub/Sub watches owned by the invoking GCP project for a form.</td></tr><tr><td>Renew Watch</td><td><code>renewWatch</code></td><td>Renew an existing watch for another 7 days from now. Takes no request body fields.</td></tr><tr><td>Set Publish Settings</td><td><code>setPublishSettings</code></td><td>Update a form's publish settings: whether it is published/visible and whether it is accepting responses. Setting isAcceptingResponses=true requires isPublished=true (setting both false while the other true is rejected). Requires forms.body, drive, or drive.file scope.</td></tr></tbody></table>

