---
description: "Formcrafts is an online form builder. List workspaces and forms, read form details and responses, and download uploaded files."
hidden: true
---

# Formcrafts

<img src="../../.gitbook/assets/connectors/lg/formcrafts.png" alt="Formcrafts logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [formcrafts.com](https://formcrafts.com) |
| **Authentication** | Username and password |
| **Slug** | `formcrafts` |

## Setup

Your customers enter their username and password for Formcrafts when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Formcrafts from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Formcrafts**.
2. Select **Connect** on the Formcrafts card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Formcrafts's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get File Content</td><td><code>getFileContent</code></td><td>Downloads the raw content of one file uploaded through a Formcrafts form, identified by its file id from List Files or from a file_upload answer. The response body is the file itself, served with the file's own content type.</td></tr><tr><td>Get Form Details</td><td><code>getForm</code></td><td>Retrieves one Formcrafts form by id, including its full field list (field id, type, page, label, description, required flag), its page list, its current response count and its creation and last published dates.</td></tr><tr><td>Get Form Details (API v1, Deprecated)</td><td><code>getFormV1</code></td><td>Retrieves one form using the deprecated Formcrafts API v1. Unlike v2, fields are grouped per page as page_title/page_fields and choice fields carry their options inline. Prefer Get Form Details (v2).</td></tr><tr><td>Get Form Responses (API v1, Deprecated)</td><td><code>getFormResponsesV1</code></td><td>Lists a form's responses using the deprecated Formcrafts API v1. Each answer is returned as id/label/answer, with an extra answer.value entry for fields whose choices carry a value (for file uploads answer.value holds download links). Prefer List Form Responses (v2).</td></tr><tr><td>Get Organization (Ping)</td><td><code>getOrganization</code></td><td>Return the organization the API key belongs to (GET https://api.formcrafts.com/v2). Useful to check that a key works. Docs: https://formcrafts.com/help/developers/api-docs-v2</td></tr><tr><td>List Files</td><td><code>listFiles</code></td><td>Lists every file uploaded through any form in the Formcrafts organization, with its id, original filename, MIME type, size in bytes and timestamps. Pass the returned file id to Get File Content to download the file.</td></tr><tr><td>List Form Responses</td><td><code>listFormResponses</code></td><td>Lists the submissions (responses) recorded for one Formcrafts form Each response carries a test flag, visitor geo/engagement metadata, any workflow results, and one entry per answered field with its field_type, value_type and value. Set partial=true to list only partial (not completed) responses.</td></tr><tr><td>List Forms</td><td><code>listForms</code></td><td>Lists every form in the Formcrafts organization, across all workspaces. Returns each form's id, name, owning workspace, enabled flag, creation date and last published date. Use the returned form id with Get Form Details or List Form Responses.</td></tr><tr><td>List Forms (API v1, Deprecated)</td><td><code>listFormsV1</code></td><td>Lists forms using the deprecated Formcrafts API v1, which uses page-number pagination and a different response envelope (type, total, page, hasMore) from v2. Prefer List Forms (v2); this action exists only for callers still on the v1 contract, which also returns formLink and responsesLink URLs.</td></tr><tr><td>List Workspaces</td><td><code>listWorkspaces</code></td><td>Lists every workspace in the Formcrafts organization. Workspaces group forms; use the returned workspace id to identify which workspace a form belongs to. Supports cursor-style pagination on the created_at field via before/after.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Form Response Submitted</td><td><code>form_response.submitted</code></td><td>Fires once for every submission of a Formcrafts form. Formcrafts has NO webhook registration API (the REST API is read-only; POST on any collection CLICK-PATH: sign in at https://app.formcrafts.com -&gt; open the form -&gt; Workflows tab -&gt; Add action -&gt; Webhook -&gt; paste the Fastn trigger URL into Webhook URL -&gt; set Format to JSON (the Form option sends application/x-www-form-urlencoded instead) -&gt; Save -&gt; Publish the form. Repeat for every form that should trigger. IMPORTANT - NO EVENT DISCRIMINATOR: a standard Formcrafts webhook body carries no event-type field, so the customer must use the Custom Webhook option on that same screen and add one literal top-level field to the body, "event": "form_response.submitted", which is the field this config's eventKey reads. Without it the delivery cannot be routed. SIGNATURE: Formcrafts signs the raw body with HMAC-SHA256 and sends it base64-encoded as x-formcrafts-signature: sha256=&lt;base64&gt;; the Fastn engine only supports hex and stripe signature formats, so verification is set to NONE here and signature checking is not performed.</td></tr></tbody></table>
