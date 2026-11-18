---
description: "Formcrafts is an online form builder for lead capture, surveys, support requests, payments and registrations."
---

# Formcrafts

Formcrafts is an online form builder for lead capture, surveys, support requests, payments and registrations. This connector wraps the Formcrafts REST API (v2, plus the deprecated v1) to list workspaces, list and inspect forms and their fields, read form responses (submissions), and list and download files uploaded through forms.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [formcrafts.com](https://formcrafts.com) |
| **Authentication** | Basic auth |
| **Actions** | 10 |
| **Events** | 1 |
| **Slug** | `formcrafts` |

## Use it

Add Formcrafts from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.formcrafts.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get File Content | `getFileContent` | Downloads the raw content of one file uploaded through a Formcrafts form, identified by its file id from List Files or from a file_upload answer. The response body is the file itself, served with the file's own content type. Returns 404 with {"error":"File not found"} when the id does not exist. |
| Get Form Details | `getForm` | Retrieves one Formcrafts form by id, including its full field list (field id, type, page, label, description, required flag), its page list, its current response count and its creation and last published dates. Returns 404 with {"error":"Form not found"} when the id does not exist. |
| Get Form Details (API v1, Deprecated) | `getFormV1` | Retrieves one form using the deprecated Formcrafts API v1. Unlike v2, fields are grouped per page as page_title/page_fields and choice fields carry their options inline. Prefer Get Form Details (v2). Returns 404 with {"error":"Form not found"} when the id does not exist. |
| Get Form Responses (API v1, Deprecated) | `getFormResponsesV1` | Lists a form's responses using the deprecated Formcrafts API v1. Each answer is returned as id/label/answer, with an extra answer.value entry for fields whose choices carry a value (for file uploads answer.value holds download links). Prefer List Form Responses (v2). Returns 404 with {"error":"Form not found"} when the id does not exist. |
| Get Organization (Ping) | `getOrganization` | Return the organization the API key belongs to (GET https://api.formcrafts.com/v2). Useful to check that a key works. Docs: https://formcrafts.com/help/developers/api-docs-v2 |
| List Files | `listFiles` | Lists every file uploaded through any form in the Formcrafts organization, with its id, original filename, MIME type, size in bytes and timestamps. Pass the returned file id to Get File Content to download the file. |
| List Form Responses | `listFormResponses` | Lists the submissions (responses) recorded for one Formcrafts form (GET /v2/forms/{id}/responses). Each response carries a test flag, visitor geo/engagement metadata, any workflow results, and one entry per answered field with its field_type, value_type and value. Set partial=true to list only partial (not completed) responses. Returns 404 with {"error":"Form not found"} when the id does not exist. |
| List Forms | `listForms` | Lists every form in the Formcrafts organization, across all workspaces. Returns each form's id, name, owning workspace, enabled flag, creation date and last published date. Use the returned form id with Get Form Details or List Form Responses. |
| List Forms (API v1, Deprecated) | `listFormsV1` | Lists forms using the deprecated Formcrafts API v1, which uses page-number pagination and a different response envelope (type, total, page, hasMore) from v2. Prefer List Forms (v2); this action exists only for callers still on the v1 contract, which also returns formLink and responsesLink URLs. |
| List Workspaces | `listWorkspaces` | Lists every workspace in the Formcrafts organization. Workspaces group forms; use the returned workspace id to identify which workspace a form belongs to. Supports cursor-style pagination on the created_at field via before/after. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Form Response Submitted | `form_response.submitted` | Fires once for every submission of a Formcrafts form. Formcrafts has NO webhook registration API (the REST API is read-only; POST on any collection returns 405 and no /webhooks route exists), so the customer registers this URL by hand, per form. CLICK-PATH: sign in at https://app.formcrafts.com -&gt; open the form -&gt; Workflows tab -&gt; Add action -&gt; Webhook -&gt; paste the fastn trigger URL into Webhook URL -&gt; set Format to JSON (the Form option sends application/x-www-form-urlencoded instead) -&gt; Save -&gt; Publish the form. Repeat for every form that should trigger. IMPORTANT - NO EVENT DISCRIMINATOR: a standard Formcrafts webhook body carries no event-type field, so the customer must use the Custom Webhook option on that same screen and add one literal top-level field to the body, "event": "form_response.submitted", which is the field this config's eventKey reads. Without it the delivery cannot be routed. SIGNATURE: Formcrafts signs the raw body with HMAC-SHA256 and sends it base64-encoded as x-formcrafts-signature: sha256=&lt;base64&gt;; the fastn engine only supports hex and stripe signature formats, so verification is set to NONE here and signature checking is not performed. PAYLOAD SCHEMA BELOW IS MODELLED FROM THE VENDOR'S DOCUMENTED SAMPLE at https://formcrafts.com/help/workflows/webhooks - it was NOT captured from a live delivery, because seeding a form requires a portal password login that was not performed. |
