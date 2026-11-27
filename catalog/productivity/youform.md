---
description: "Youform is an online form builder. List forms, templates and themes, read form submissions, and create and delete form webhooks."
hidden: true
---

# Youform

<img src="../../.gitbook/assets/connectors/lg/youform.png" alt="Youform logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [youform.com](https://youform.com) |
| **Authentication** | Access token |
| **Slug** | `youform` |

## Setup

Your customers enter their access token for Youform when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Youform from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Youform**.
2. Select **Connect** on the Youform card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Youform's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Form Webhook</td><td><code>createFormWebhook</code></td><td>Registers a webhook on a Youform form so that every new submission is POSTed as JSON to the given URL. Returns the identifier of the created webhook, which Delete Webhook needs.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Removes a previously registered Youform webhook by its identifier, so the form stops POSTing new submissions to that URL.</td></tr><tr><td>Get Form</td><td><code>getForm</code></td><td>Returns a single Youform form identified by its slug, including its published and draft field blocks, design settings, messages, hidden fields and integration configuration.</td></tr><tr><td>Get My Profile</td><td><code>getMyProfile</code></td><td>Returns the profile of the Youform account the API token belongs to, including its numeric identifier, first name, last name and email address. Useful for confirming which account a connection is authenticated as.</td></tr><tr><td>List Fonts</td><td><code>listFonts</code></td><td>Returns the fonts available to forms in the authenticated Youform account, split into custom fonts uploaded to the account and the built-in system fonts.</td></tr><tr><td>List Form Submissions</td><td><code>listFormSubmissions</code></td><td>Returns the submissions of a Youform form as a paginated list. Each submission carries its answers keyed by field block identifier, together with completion state and timestamps. Results are oldest first by default. Filtering by completion state with Is Complete requires a Youform Pro plan; on a free plan omit it and only completed submissions are returned.</td></tr><tr><td>List Form Templates</td><td><code>listFormTemplates</code></td><td>Returns the full Youform form template gallery, each entry carrying its slug, title, marketing description, preview image and category list. Youform returns the complete list as a bare JSON array and ignores any filtering or pagination parameters.</td></tr><tr><td>List Forms</td><td><code>listForms</code></td><td>Returns every form belonging to the authenticated Youform account, as a paginated list of 100 forms per page. Each form carries its slug, name, field blocks, design settings and integration configuration. Use the slug with Get Form and List Form Submissions.</td></tr><tr><td>List Template Categories</td><td><code>listTemplateCategories</code></td><td>Returns the list of category names used to group the Youform form template gallery, such as Application, Booking, Business and Lead generation. Use them to filter the result of List Form Templates client-side.</td></tr><tr><td>List Themes</td><td><code>listThemes</code></td><td>Returns the built-in Youform form themes, each with its name and the background, text, button and button text colours it applies to a form.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Set Submission Refill Link</td><td><code>setSubmissionRefillLink</code></td><td>Enables or disables the refill link for a submission, which lets the respondent reopen and edit their answers. This feature requires a Youform Pro plan; on lower plans Youform'</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Form Submission Received</td><td><code>submission_created</code></td><td>Fires when a new submission is received by the Youform form named in the form_id input. Youform webhooks are registered per form through and removed through; this connector does that automatically. Supply the form's slug (for example 'kyir3qrg', from List Forms) as the form_id input when creating the trigger. Youform's API exposes exactly one webhook event: a new submission.</td></tr></tbody></table>
