---
description: "Fillout is an online form, survey and scheduling builder."
hidden: true
---

# Fillout

<img src="../../.gitbook/assets/connectors/fillout.png" alt="Fillout logo" width="64">

Fillout is an online form, survey and scheduling builder. This connector wraps the complete Fillout REST API (https://api.fillout.com/v1/api): listing forms, reading a form's questions, calculations, URL parameters, scheduling and payment fields, reading, filtering, creating and deleting submissions, and registering or removing submission webhooks. Authentication uses a Fillout API key sent as a Bearer token, enabled under Settings &gt; Developer.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [fillout.com](https://fillout.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `fillout` |

## Use it

Add Fillout from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fillout.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Form Submissions | `createFormSubmissions` | Creates up to ten submissions on a Fillout form in a single call, for backfilling responses collected elsewhere. Each submission lists its answers by question ID and may carry URL parameters, scheduling bookings, payments and a verified login email. |
| Create Webhook | `createWebhook` | Registers a webhook that posts every new submission of a Fillout form to the given endpoint. Returns the numeric webhook ID needed to remove it again. |
| Delete Form Submission | `deleteFormSubmission` | Permanently deletes a single submission from a Fillout form, including all of its answers. |
| Delete Webhook | `deleteWebhook` | Removes a Fillout submission webhook so the endpoint stops receiving new responses. Identify it with the webhook ID returned when it was created. The call is idempotent: an unknown webhook ID also returns 200 with an empty object. |
| Get Form Metadata | `getFormMetadata` | Returns a Fillout form's structure: every question with its type, the calculated fields, URL parameters, scheduling and payment fields, and the quiz configuration when quiz mode is on. |
| Get Form Submission | `getFormSubmission` | Returns a single Fillout form submission with every answer, calculation, URL parameter, scheduling booking and payment recorded against it. |
| List Form Submissions | `listFormSubmissions` | Returns submissions for a Fillout form with every answer, calculation, URL parameter, scheduling and payment value, optionally filtered by completion status, date range or a free-text search. |
| List Forms | `listForms` | Returns every form in the connected Fillout workspace with its name and public form ID. Use the returned formId with the form metadata, submission and webhook actions. |
