---
description: "Youform is an online form builder for surveys, quizzes and lead capture."
hidden: true
---

# Youform

<img src="../../.gitbook/assets/connectors/lg/youform.png" alt="Youform logo">

Youform is an online form builder for surveys, quizzes and lead capture. This connector covers the full Youform REST API: reading the authenticated account profile, listing forms, reading a single form by slug, reading complete and partial submissions for a form, creating and deleting per-form submission webhooks, and enabling or disabling a submission refill link.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [youform.com](https://youform.com) |
| **Authentication** | Bearer token |
| **Slug** | `youform` |

## Use it

Add Youform from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.youform.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Form Webhook | `createFormWebhook` | Registers a webhook on a Youform form so that every new submission is POSTed as JSON to the given URL. Returns the identifier of the created webhook, which Delete Webhook needs. |
| Delete Webhook | `deleteWebhook` | Removes a previously registered Youform webhook by its identifier, so the form stops POSTing new submissions to that URL. |
| Get Form | `getForm` | Returns a single Youform form identified by its slug, including its published and draft field blocks, design settings, messages, hidden fields and integration configuration. |
| Get My Profile | `getMyProfile` | Returns the profile of the Youform account the API token belongs to, including its numeric identifier, first name, last name and email address. Useful for confirming which account a connection is authenticated as. |
| List Fonts | `listFonts` | Returns the fonts available to forms in the authenticated Youform account, split into custom fonts uploaded to the account and the built-in system fonts. |
| List Form Submissions | `listFormSubmissions` | Returns the submissions of a Youform form as a paginated list. Each submission carries its answers keyed by field block identifier, together with completion state and timestamps. Results are oldest first by default. Filtering by completion state with Is Complete requires a Youform Pro plan; on a free plan omit it and only completed submissions are returned. |
| List Form Templates | `listFormTemplates` | Returns the full Youform form template gallery, each entry carrying its slug, title, marketing description, preview image and category list. Youform returns the complete list as a bare JSON array and ignores any filtering or pagination parameters. |
| List Forms | `listForms` | Returns every form belonging to the authenticated Youform account, as a paginated list of 100 forms per page. Each form carries its slug, name, field blocks, design settings and integration configuration. Use the slug with Get Form and List Form Submissions. |
| List Template Categories | `listTemplateCategories` | Returns the list of category names used to group the Youform form template gallery, such as Application, Booking, Business and Lead generation. Use them to filter the result of List Form Templates client-side. |
| List Themes | `listThemes` | Returns the built-in Youform form themes, each with its name and the background, text, button and button text colours it applies to a form. |

<details>

<summary>See 1 more action</summary>

* **Set Submission Refill Link** `setSubmissionRefillLink`: Enables or disables the refill link for a submission, which lets the respondent reopen and edit their answers. This feature requires a Youform Pro plan; on lower plans Youform returns 403 'Only PRO users can use this feature.'

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Form Submission Received | `submission_created` | Fires when a new submission is received by the Youform form named in the form_id input. Youform webhooks are registered per form through POST /api/webhooks and removed through DELETE /api/webhooks/{id}; this connector does that automatically. Supply the form's slug (for example 'kyir3qrg', from List Forms) as the form_id input when creating the trigger. Youform's API exposes exactly one webhook event: a new submission. The payload schema below is modelled from Youform's documented submission object, not captured from a live delivery. |
