---
description: "Jotform online form builder API."
hidden: true
---

# Jotform

<img src="../../.gitbook/assets/connectors/jotform.png" alt="Jotform logo" width="64">

Jotform online form builder API. Manage forms, questions, properties, submissions, reports, folders, webhooks, and account/user data. Auth via APIKEY header.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [jotform.com](https://jotform.com) |
| **Authentication** | API key |
| **Slug** | `jotform` |

## Use it

Add Jotform from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.jotform.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Form Questions | `addFormQuestions` | Adds or updates several questions on a form in one request (documented PUT /form/{id}/questions). Pass a questions object keyed by question id; each value carries the question's type, text, order, name and any other question property. Only the properties supplied are sent. |
| Add Label Resources | `addLabelResources` | Attaches resources (forms, workflows, sheets, portals) to a label. |
| Clone Form | `cloneForm` | Clone an existing form into a new copy. Returns the new form details. |
| Create Form | `createForm` | Creates a new form. Pass form properties (title required) and optionally an array of questions and email settings; the body is sent as JSON to the documented PUT /user/forms endpoint and only supplied fields are sent. |
| Create Form Question | `createFormQuestion` | Adds a new question (field) to a form. type, text, name and order are all required and sent as question[...] fields. Use Add Form Questions to add several at once or to set extra properties. |
| Create Form Submission | `createFormSubmission` | Submit data to a form programmatically. Form-urlencoded with submission[qid] keys mapping question ids to answer values. Use submission[qid_subfield] for composite fields. |
| Create Form Submission (Full) | `createFormSubmissionFull` | Creates ONE form submission carrying every answer in a single call. Pass `submission` as a JSON ARRAY holding a single object keyed by question id, e.g. [{"1":"jane@example.com","2":"ACME"}]. The array form is required: a bare object creates a SEPARATE one-answer submission per key. Returns { responseCode, message, content: [ { submissionID, URL } ] }. |
| Create Form Webhook | `createFormWebhook` | Register a webhook URL on a form. Jotform will POST submission data to this URL on every new submission. Form-urlencoded with webhookURL. |
| Create Label | `createLabel` | Creates a new label. Labels group forms, workflows, sheets and portals. |
| Create Report | `createReport` | Creates a new report for a form (csv, excel, grid, table or calendar). title, list_type and fields are required; pass fields=all to include every field. |

<details>

<summary>See 37 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Form | `deleteForm` | Delete a form (moves it to trash). Returns the deleted form's properties. |
| Delete Form Question | `deleteFormQuestion` | Delete a question (field) from a form by its question id. |
| Delete Form Webhook | `deleteFormWebhook` | Delete a webhook from a form by its webhook id (the index key returned by Get Form Webhooks). |
| Delete Label | `deleteLabel` | Deletes a label by ID. Resources attached to the label are not deleted. |
| Delete Report | `deleteReport` | Delete a report by its report id. |
| Delete Submission | `deleteSubmission` | Delete a submission by its submission id. |
| Edit Form Question | `editFormQuestion` | Edits an existing question on a form. text, order and required are all sent, so pass the current value for any you do not want to change (see Get Form Question). Use Add Form Questions for partial JSON updates. |
| Edit Submission | `editSubmission` | Update the answers of an existing submission. Form-urlencoded with submission[qid] keys. |
| Edit Submission (Full) | `editSubmissionFull` | Updates MANY answers on an existing submission in a single call. Pass `formBody` as a pre-encoded application/x-www-form-urlencoded string, e.g. submission[7]=ACME%20TOOL&submission[15]=CHICAGO. Returns { responseCode, message, content }. |
| Get Form | `getForm` | Get the basic details of a single form: title, status, creation date, submission count, and last submission. |
| Get Form Files | `getFormFiles` | List all files uploaded to a form's submissions. |
| Get Form Properties | `getFormProperties` | Get all configuration properties of a form (theme, fonts, layout, settings). |
| Get Form Property | `getFormProperty` | Get a single configuration property of a form by its property key. |
| Get Form Question | `getFormQuestion` | Get the properties of a single question on a form by its question id. |
| Get Form Questions | `getFormQuestions` | Get all questions (fields) of a form, keyed by question id, with type, text, order, and field-specific properties. |
| Get Form Reports | `getFormReports` | List all reports created from a specific form. |
| Get Form Submissions | `getFormSubmissions` | List submissions for a specific form. Supports pagination, filtering, and ordering. |
| Get Form Webhooks | `getFormWebhooks` | List all webhook URLs registered on a form. Returns a map of webhook index to URL. |
| Get Label | `getLabel` | Retrieves a label by ID. |
| Get Label Resources | `getLabelResources` | Lists the resources (forms, workflows, sheets, portals) attached to a label, with paging. |
| Get Report | `getReport` | Get the details of a single report by its report id. |
| Get Submission | `getSubmission` | Get the details and answers of a single submission by its submission id. |
| Get Subusers | `getSubusers` | List sub-users of the account and the forms/folders shared with each. |
| Get Usage | `getUsage` | Get monthly usage stats for the user: number of API requests, submissions, SSL submissions, payments, and uploads. |
| Get User | `getUser` | Get account details for the authenticated Jotform user (name, email, account type, usage limits). FREE read — use for connection validation. |
| Get User Forms | `getUserForms` | List all forms owned by the user. Supports pagination (offset, limit), filtering, and ordering. |
| Get User History | `getUserHistory` | Get the user's activity history (account activity log), newest first. Filter by action type and by a preset date range (date). Jotform does not apply the documented startDate, endDate and sortBy parameters on this endpoint, so they are not offered. |
| Get User Invoices | `getUserInvoices` | Lists the account's billing invoices. |
| Get User Reports | `getUserReports` | List all reports created across the user's forms (Excel, CSV, grid, calendar, etc.). |
| Get User Setting | `getUserSetting` | Retrieves a single account setting by key (e.g. username, name, email, website, time_zone, language). |
| Get User Settings | `getUserSettings` | Get the user's account settings (email, time zone, language, security settings, etc.). |
| Get User Submissions | `getUserSubmissions` | List all submissions across all of the user's forms. Supports pagination, filtering, and ordering. |
| List User Labels | `getUserFolders` | Lists the account's labels (Jotform's replacement for folders), including nested sublabels. Labels group forms, workflows, sheets and portals. |
| Remove Label Resources | `removeLabelResources` | Detaches resources (forms, workflows, sheets, portals) from a label. |
| Set Form Properties | `setFormProperties` | Updates configuration properties of a form. Pass a properties object with only the keys to change (title, thanktext, activeRedirect, thankurl, formWidth, ...); sent as JSON to the documented PUT /form/{id}/properties endpoint. |
| Update Label | `updateLabel` | Updates a label's name and/or color. Only the fields supplied are sent (JSON PUT). |
| Update User Settings | `updateUserSettings` | Update the user's account settings. Pass only the fields you want to change (name, website, time_zone, language); omitted fields are left untouched. Form-urlencoded. |

</details>
