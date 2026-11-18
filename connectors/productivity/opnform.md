---
description: "OpnForm is an open-source form builder."
hidden: true
---

# OpnForm

<img src="../../.gitbook/assets/connectors/lg/opnform.png" alt="OpnForm logo">

OpnForm is an open-source form builder. This connector wraps the OpnForm Cloud REST API (https://api.opnform.com) covering forms, form submissions, form integrations (including outgoing webhooks), workspaces, workspace users and invites, form templates, public form viewing and answering, AI form generation and platform content endpoints.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [opnform.com](https://opnform.com) |
| **Authentication** | Bearer token |
| **Slug** | `opnform` |

## Use it

Add OpnForm from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.opnform.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Workspace User | `addWorkspaceUser` | Adds a person to a workspace by email. If the email already has an OpnForm account they are added immediately; otherwise an invitation email is sent. Inviting users requires a Pro plan; on Free the API answers 403 'A Pro plan is required to invite users.' Requires the 'workspace-users-write' token ability. |
| Cancel Workspace Invite | `cancelWorkspaceInvite` | Cancels a pending workspace invitation so the invited email can no longer join. Requires the 'workspace-users-write' token ability. |
| Create Form | `createForm` | Creates a new OpnForm form in a workspace. All appearance fields (visibility, language, theme, presentation_style, width, size, border_radius, dark_mode, color, uppercase_labels, no_branding, transparent_background) are required by the API alongside the title and the 'properties' array that defines the form fields. Returns { message, form, users_first_form }. Requires the 'forms-write' token ability. |
| Create Form Integration | `createFormIntegration` | Adds an integration to a form so that each new submission triggers it. Use integration_id 'webhook' with data { webhook_url } to receive submission payloads over HTTP. Slack, Discord, Telegram and the advanced email integration require a Pro workspace; HubSpot, Salesforce, Airtable and Google Sheets require Business. Requires the 'manage-integrations' token ability. |
| Create Form Payment Intent | `createFormPaymentIntent` | Creates the Stripe payment intent a respondent needs before submitting a form that contains a payment block. Answers 400 'Form does not have a payment block.' on forms without one. No money moves until the respondent confirms the intent in Stripe. |
| Create Form Template | `createTemplate` | Creates a reusable form template from a form definition. The slug must be unique across all OpnForm templates. Set publicly_listed to true to offer it in the public template gallery. |
| Create Signed Storage URL | `createSignedStorageUrl` | Issues a pre-signed S3 upload URL for a file that will be attached to a form submission. PUT the file bytes to the returned 'url' with the returned headers, then send the returned 'uuid' as the answer to the form's file field. Returns { uuid, bucket, key, url, headers }. |
| Create Workspace | `createWorkspace` | Creates a new OpnForm workspace owned by the authenticated user, who becomes its admin. Returns { message, workspace_id, workspace }. Multiple workspaces require a Pro plan; on Free the API answers 403 'You have reached the workspace limit for Free plan.' Requires the 'workspaces-write' token ability. |
| Delete Form | `deleteForm` | Permanently deletes an OpnForm form and all of its submissions. Returns a confirmation message. Requires the 'forms-write' token ability. |
| Delete Form Integration | `deleteFormIntegration` | Removes an integration from a form, stopping it from running on future submissions. Requires the 'manage-integrations' token ability. |

<details>

<summary>See 42 more actions</summary>

* **Delete Form Submission** `deleteFormSubmission`: Permanently deletes a single submission from a form. Returns a confirmation message. Requires the 'forms-write' token ability.
* **Delete Form Template** `deleteTemplate`: Permanently deletes a form template you own. Forms already created from it are unaffected.
* **Delete Workspace** `deleteWorkspace`: Permanently deletes a workspace together with every form and submission it contains. Only a workspace admin may do this, and the call is irreversible. Returns { message, workspace_id }. Requires the 'workspaces-write' token ability.
* **Export Form Submissions** `exportFormSubmissions`: Exports form submissions as CSV. 'columns' selects which field ids appear in the export (map of field id to true/false); 'submissionIds' optionally limits the export to specific submissions. Small exports return the CSV synchronously; large ones return a job id to poll. Requires the 'forms-read' token ability.
* **Generate Form Fields With AI** `generateFormFieldsWithAi`: Generates additional form fields from a plain-language prompt, to append to a form you are already editing. Returns an AI completion id to poll with Get AI Form Completion.
* **Generate Form With AI** `generateFormWithAi`: Starts an AI generation of a complete form from a plain-language prompt and returns an AI completion id to poll with Get AI Form Completion. The prompt is capped at 4000 characters on Free and 10000 with the Pro 'ai.form_generation' feature.
* **Get AI Form Completion** `getAiFormCompletion`: Polls an AI form generation started by Generate Form With AI or Generate Form Fields With AI, returning its status and, once finished, the generated form definition.
* **Get Feature Flags** `getFeatureFlags`: Returns the OpnForm instance's feature flags - whether it is self-hosted, whether billing, AI features, custom domains, storage and each third-party service are enabled. Use it to discover what the instance supports before calling a feature-specific endpoint.
* **Get Form** `getForm`: Retrieves a single OpnForm form by its numeric id or slug, including its complete field definition, appearance settings, submission settings and share URL. Requires the 'forms-read' token ability.
* **Get Form Asset** `getFormAsset`: Resolves a form asset (a logo or cover image uploaded through Upload Form Asset) by its stored file name and returns the file. Answers 400 with { type, message, file_name } when the asset does not exist.
* **Get Form Stripe Account** `getFormStripeAccount`: Returns the Stripe Connect account details behind a form's payment field, so a front end can initialise Stripe Elements. Only meaningful on forms that contain a 'payment' block with a connected Stripe account.
* **Get Form Template** `getTemplate`: Retrieves a single form template by its slug, including the complete form definition, the questions it answers and its related templates.
* **Get Public Form** `getPublicForm`: Fetches a published form by its public slug exactly as a respondent's browser would, returning the fields, theme and submission settings needed to render it. Works without a token; draft forms are not returned.
* **Get Public Form Submission** `getPublicFormSubmission`: Fetches one submission of a public form by id, as used by the 'edit your answer' link on forms with editable submissions enabled. Returns respondent-supplied personal data.
* **Import Form** `importForm`: Imports a form from another form builder and returns an OpnForm form definition ready to be saved with Create Form. Supported sources are typeform, tally, fillout and google_forms; google_forms additionally requires an authenticated user and a connected Google OAuth provider id. Rate limited to 10 requests per minute.
* **Leave Workspace** `leaveWorkspace`: Removes the authenticated user from a workspace they are a member of. This is irreversible without a new invitation, and the last remaining admin cannot leave. Requires the 'workspace-users-write' token ability.
* **List All Forms** `listForms`: Lists every form across all workspaces the authenticated user belongs to. Returns the full form definition for each form, including its slug, share URL, visibility, theme and field properties. Requires the 'forms-read' token ability.
* **List Changelog Entries** `listChangelogEntries`: Returns OpnForm's published product changelog entries. The array is empty when the instance has no changelog feed configured.
* **List Fonts** `listFonts`: Returns the font family names a form's font_family setting accepts, in the order OpnForm offers them in its editor.
* **List Form Integration Events** `listFormIntegrationEvents`: Lists the delivery/run history of a single form integration, newest first - useful for debugging why a webhook or notification did not arrive. Requires the 'manage-integrations' token ability.
* **List Form Integrations** `listFormIntegrations`: Lists the integrations configured on a form (webhook, email, Slack, Discord, Telegram, Google Sheets, Zapier, Make, n8n and others), including each integration's status, settings and logic. Requires the 'manage-integrations' token ability.
* **List Form Submissions** `listFormSubmissions`: Lists the submissions of a form, newest first and paginated. Optionally full-text searches submission values and filters by completion status. Returns { data, links, meta }. Submission data is respondent-supplied personal data. Requires the 'forms-read' token ability.
* **List Form Templates** `listTemplates`: Lists OpnForm's publicly listed form templates, newest first, each with its slug, name, description, image and full form definition ready to be cloned. Note that the /templates routes are not covered by API-token authentication, so this always returns the public gallery; the 'onlymy' filter the web app uses has no effect with a token and is therefore not exposed here.
* **List Plans** `listPlans`: Returns OpnForm's subscription tiers (free, pro, business and higher) with their monthly and yearly prices, plus the feature matrix describing which tier each capability requires.
* **List Public Form Users** `listPublicFormUsers`: Returns the workspace members that a public form's user-picker field can offer as options. Used by forms containing an 'assign to a user' style field.
* **List Sitemap URLs** `listSitemapUrls`: Returns every public OpnForm page path that belongs in a sitemap - mainly the public template gallery - as a list of { loc } entries.
* **List Workspace Forms** `listWorkspaceForms`: Lists the forms belonging to a single OpnForm workspace, paginated. Returns a 'data' array of form objects plus 'links' and 'meta' pagination envelopes. Requires the 'forms-read' token ability.
* **List Workspace Invites** `listWorkspaceInvites`: Lists the pending user invitations for a workspace, with the invited email, role and invitation status. Requires the 'workspace-users-read' token ability.
* **List Workspace Users** `listWorkspaceUsers`: Lists the members of a workspace with their id, name, email, avatar and workspace role (admin, user or readonly). Requires the 'workspace-users-read' token ability.
* **List Workspaces** `listWorkspaces`: Lists every OpnForm workspace the authenticated user belongs to, including the workspace name, icon, plan tier, custom domains, member count and the caller's role in each workspace. Requires the 'workspaces-read' token ability.
* **Record Public Form View** `recordPublicFormView`: Registers a view of a public form, incrementing its views_count - the same call the public form page makes when it loads. Use it when embedding an OpnForm form in your own front end so analytics stay accurate.
* **Remove Workspace User** `removeWorkspaceUser`: Removes a member from a workspace, revoking their access to its forms and submissions. The member's own account is not deleted. Requires the 'workspace-users-write' token ability.
* **Resend Workspace Invite** `resendWorkspaceInvite`: Sends the invitation email again for a pending workspace invite. Requires the 'workspace-users-write' token ability.
* **Submit Form Answer** `submitForm`: Submits an answer to a public OpnForm form, exactly as a respondent would. The answer keys are the form's field ids (see the 'properties' array returned by Get Form); pass them as additional top-level inputs alongside formId. Triggers every active integration on the form, including notification emails and webhooks. Returns { type, message, submission_id, is_first_submission }. No token ability is needed - this is the public submission endpoint.
* **Update Form** `updateForm`: Replaces an existing form's definition. The API validates the whole payload, so send every required field (title, visibility, language, theme, presentation_style, width, size, border_radius, dark_mode, color, uppercase_labels, no_branding, transparent_background, properties) even when changing only one value - fetch the current form with Get Form first and merge. Returns { message, form }. Requires the 'forms-write' token ability.
* **Update Form Integration** `updateFormIntegration`: Updates an existing form integration in place - for example to change a webhook URL or to pause it by setting status to 'inactive'. The whole integration payload must be sent. Requires the 'manage-integrations' token ability.
* **Update Form Submission** `updateFormSubmission`: Overwrites the answers stored on an existing submission. The answer keys are the form's field ids; pass them as additional top-level inputs alongside formId and submission_id. Returns { message, data }. Submission content is respondent personal data. Requires the 'forms-write' token ability.
* **Update Form Template** `updateTemplate`: Replaces an existing form template you own. Every required field must be sent, as with Create Form Template.
* **Update Workspace** `updateWorkspace`: Renames a workspace and sets its icon emoji. Both values are replaced: sending no emoji clears the current icon. Returns { message, workspace }. Requires the 'workspaces-write' token ability.
* **Update Workspace User Role** `updateWorkspaceUserRole`: Changes an existing workspace member's role between admin, user and readonly. Requires the 'workspace-users-write' token ability.
* **Upload File** `uploadFile`: Uploads a text file to OpnForm's temporary storage as a multipart form-data 'file' part, returning the stored path to use as the answer to a form's file field. Supply the file name and its text content. For binary files (images, PDFs) use Create Signed Storage URL instead and PUT the bytes to S3 directly.
* **Upload Form Asset** `uploadFormAsset`: Promotes a file already placed in OpnForm's temporary storage into permanent asset storage, returning the public asset URL to use as a form's logo_picture or cover_picture. Upload the file first with Upload File (or Create Signed Storage URL), then pass its uuid here - either the bare uuid, or 'name_{uuid}.{ext}' to keep a readable file name. Returns { message, url }.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| New Form Submission | `form.submission` | Fires each time a submission is saved on the subscribed OpnForm form. OpnForm's outgoing webhook carries no event-type discriminator and no signature header, so this is the only event type this webhook can deliver. The payload contains respondent-supplied personal data. |
