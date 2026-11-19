---
description: "Fillout is an online form, survey and scheduling builder."
hidden: true
---

# Fillout

<img src="../../.gitbook/assets/connectors/lg/fillout.png" alt="Fillout logo">

This connector wraps the complete Fillout REST API (https://api.fillout.com/v1/api): listing forms, reading a form's questions, calculations, URL parameters, scheduling and payment fields, reading, filtering, creating and deleting submissions, and registering or removing submission webhooks. Authentication uses a Fillout API key sent as a Bearer token, enabled under Settings &gt; Developer.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [fillout.com](https://fillout.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `fillout` |

## Use it

Add Fillout from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fillout.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Form Submissions</td><td><code>createFormSubmissions</code></td><td>Creates up to ten submissions on a Fillout form in a single call, for backfilling responses collected elsewhere. Each submission lists its answers by question ID and may carry URL parameters, scheduling bookings, payments and a verified login email.</td></tr><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Registers a webhook that posts every new submission of a Fillout form to the given endpoint. Returns the numeric webhook ID needed to remove it again.</td></tr><tr><td>Delete Form Submission</td><td><code>deleteFormSubmission</code></td><td>Permanently deletes a single submission from a Fillout form, including all of its answers.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Removes a Fillout submission webhook so the endpoint stops receiving new responses. Identify it with the webhook ID returned when it was created. The call is idempotent: an unknown webhook ID also returns 200 with an empty object.</td></tr><tr><td>Get Form Metadata</td><td><code>getFormMetadata</code></td><td>Returns a Fillout form's structure: every question with its type, the calculated fields, URL parameters, scheduling and payment fields, and the quiz configuration when quiz mode is on.</td></tr><tr><td>Get Form Submission</td><td><code>getFormSubmission</code></td><td>Returns a single Fillout form submission with every answer, calculation, URL parameter, scheduling booking and payment recorded against it.</td></tr><tr><td>List Form Submissions</td><td><code>listFormSubmissions</code></td><td>Returns submissions for a Fillout form with every answer, calculation, URL parameter, scheduling and payment value, optionally filtered by completion status, date range or a free-text search.</td></tr><tr><td>List Forms</td><td><code>listForms</code></td><td>Returns every form in the connected Fillout workspace with its name and public form ID. Use the returned formId with the form metadata, submission and webhook actions.</td></tr></tbody></table>
