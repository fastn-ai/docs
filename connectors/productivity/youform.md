---
description: "Youform is an online form builder for surveys, quizzes and lead capture."
hidden: true
---

# Youform

<img src="../../.gitbook/assets/connectors/lg/youform.png" alt="Youform logo">

This connector covers the full Youform REST API: reading the authenticated account profile, listing forms, reading a single form by slug, reading complete and partial submissions for a form, creating and deleting per-form submission webhooks, and enabling or disabling a submission refill link.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [youform.com](https://youform.com) |
| **Authentication** | Bearer token |
| **Slug** | `youform` |

## Use it

Add Youform from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.youform.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Form Webhook</td><td><code>createFormWebhook</code></td><td>Registers a webhook on a Youform form so that every new submission is POSTed as JSON to the given URL. Returns the identifier of the created webhook, which Delete Webhook needs.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Removes a previously registered Youform webhook by its identifier, so the form stops POSTing new submissions to that URL.</td></tr><tr><td>Get Form</td><td><code>getForm</code></td><td>Returns a single Youform form identified by its slug, including its published and draft field blocks, design settings, messages, hidden fields and integration configuration.</td></tr><tr><td>Get My Profile</td><td><code>getMyProfile</code></td><td>Returns the profile of the Youform account the API token belongs to, including its numeric identifier, first name, last name and email address. Useful for confirming which account a connection is authenticated as.</td></tr><tr><td>List Fonts</td><td><code>listFonts</code></td><td>Returns the fonts available to forms in the authenticated Youform account, split into custom fonts uploaded to the account and the built-in system fonts.</td></tr><tr><td>List Form Submissions</td><td><code>listFormSubmissions</code></td><td>Returns the submissions of a Youform form as a paginated list. Each submission carries its answers keyed by field block identifier, together with completion state and timestamps. Results are oldest first by default. Filtering by completion state with Is Complete requires a Youform Pro plan; on a free plan omit it and only completed submissions are returned.</td></tr><tr><td>List Form Templates</td><td><code>listFormTemplates</code></td><td>Returns the full Youform form template gallery, each entry carrying its slug, title, marketing description, preview image and category list. Youform returns the complete list as a bare JSON array and ignores any filtering or pagination parameters.</td></tr><tr><td>List Forms</td><td><code>listForms</code></td><td>Returns every form belonging to the authenticated Youform account, as a paginated list of 100 forms per page. Each form carries its slug, name, field blocks, design settings and integration configuration. Use the slug with Get Form and List Form Submissions.</td></tr><tr><td>List Template Categories</td><td><code>listTemplateCategories</code></td><td>Returns the list of category names used to group the Youform form template gallery, such as Application, Booking, Business and Lead generation. Use them to filter the result of List Form Templates client-side.</td></tr><tr><td>List Themes</td><td><code>listThemes</code></td><td>Returns the built-in Youform form themes, each with its name and the background, text, button and button text colours it applies to a form.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Set Submission Refill Link</td><td><code>setSubmissionRefillLink</code></td><td>Enables or disables the refill link for a submission, which lets the respondent reopen and edit their answers. This feature requires a Youform Pro plan; on lower plans Youform returns 403 'Only PRO users can use this feature.'</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Form Submission Received</td><td><code>submission_created</code></td><td>Fires when a new submission is received by the Youform form named in the form_id input. Youform webhooks are registered per form through POST /api/webhooks and removed through DELETE /api/webhooks/{id}; this connector does that automatically. Supply the form's slug (for example 'kyir3qrg', from List Forms) as the form_id input when creating the trigger. Youform's API exposes exactly one webhook event: a new submission. The payload schema below is modelled from Youform's documented submission object, not captured from a live delivery.</td></tr></tbody></table>
