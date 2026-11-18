---
description: "CabinPanda is a data collection platform for building online forms, surveys and popups."
hidden: true
---

# CabinPanda

CabinPanda is a data collection platform for building online forms, surveys and popups. This connector covers the CabinPanda REST API: forms (list, get, create, update, rename, duplicate, delete, fields), submissions (list, get, delete, public submit), form types and templates, webhooks (create, update, enable/disable, delete, activities, test and redelivery), workspaces, notifications, API tokens and the current user.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [cabinpanda.com](https://cabinpanda.com) |
| **Authentication** | Bearer token |
| **Actions** | 28 |
| **Events** | 1 |
| **Slug** | `cabinpanda` |

## Use it

Add CabinPanda from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cabinpanda.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Form | `createForm` | Creates a new form from a design template and form type, optionally with a name and notification receivers. The template's default fields and settings are applied; use Update Form afterwards to change fields, messages and other settings. Returns the created form including its key. |
| Create Webhook | `createWebhook` | Creates a webhook on a form that delivers each new submission to the given URL. New webhooks are created disabled; call Set Webhook Status to enable delivery. The team id comes from Get Current User. |
| Delete Form | `deleteForm` | Permanently deletes a form by key together with its submissions and webhooks. This cannot be undone. |
| Delete Submission | `deleteSubmission` | Permanently deletes a single form submission by its numeric id (the 'id' value from List Form Submissions). |
| Delete Webhook | `deleteWebhook` | Deletes a webhook from a form so it no longer receives submissions. |
| Duplicate Form | `duplicateForm` | Creates a copy of an existing form by key, including its fields and settings. Returns the new form with its own key. |
| Get Current User | `getCurrentUser` | Returns the profile of the user who owns the API token, including their team, current workspace and the plan features available to the account. |
| Get Form | `getForm` | Returns the full details of a single form by its key, including its settings, template and the list of fields with their keys, types and options. |
| Get Form Submission | `getFormSubmission` | Returns a single submission of a form by the submission's uid, including all submitted field values and files. |
| List API Tokens | `listApiTokens` | Lists the personal API tokens of the current user with their names, creation and expiry dates. Token values are never returned. |
| List Field Types | `listFieldTypes` | Lists the available form field types (short answer, long answer, email, name, dropdown, file and so on) with their numeric ids and the attributes each type accepts, including validation rules and defaults. Field type ids are required when defining fields in Update Form. |
| List Form Fields | `listFormFields` | Returns the field keys and labels of a form. Field keys are needed to build the 'fields' map when submitting a form. |
| List Form Submissions | `listFormSubmissions` | Lists the submissions received by a form, newest first, with pagination. Each submission includes its id, uid and the submitted field values. |
| List Form Templates | `listFormTemplates` | Lists all form design templates available to the workspace, with their ids (used by Create Form), form type and style variables. The list is not paginated. |
| List Form Types | `listFormTypes` | Lists the available form types (regular, backendless, popup, conversational) with the ids used by Create Form and Update Form. |
| List Forms | `listForms` | Lists all forms in the current workspace, with pagination. Each form includes its key (used by every other form action), name, template id and detail settings. |
| List Forms By Type | `listFormsByType` | Lists the workspace's forms of a given form type (see List Form Types), with pagination. |
| List Notifications | `listNotifications` | Returns the current user's in-app notifications and platform announcements. |
| List Webhook Activities | `listWebhookActivities` | Returns the delivery log of a webhook: each activity holds the submission id, the JSON request payload that was sent and the endpoint's response. |
| List Webhooks | `listWebhooks` | Lists the webhooks configured on a form, including each webhook's id, target URL, HTTP method type, secret, SSL verification flag and enabled status. |
| List Workspaces | `listWorkspaces` | Lists the workspaces the current user belongs to, with their owner and team. |
| Redeliver Webhook Activity | `redeliverWebhookActivity` | Re-sends a previous webhook delivery (an activity from List Webhook Activities) to the webhook's URL, for example after the endpoint was down. |
| Rename Form | `renameForm` | Renames a form by key without creating a new revision. Returns the updated form. |
| Send Webhook Test Request | `sendWebhookTestRequest` | Sends a sample submission payload to a webhook's URL to verify the endpoint accepts deliveries. Returns the payload that was sent and the endpoint's response. |
| Set Webhook Status | `setWebhookStatus` | Enables or disables delivery for a webhook. Newly created webhooks are disabled until enabled with this action. |
| Submit Form | `submitForm` | Submits a response to a form through the public submit endpoint. Pass the form key and a map of field key to value (field keys come from List Form Fields). Returns the uid of the new submission and triggers the form's notifications, integrations and webhooks. |
| Update Form | `updateForm` | Replaces the definition of a form by key: its name, design template, settings ('detail') and fields, creating a new revision and optionally publishing it. This is a full replacement, so send the complete settings, template id and field list you want to keep (read them with Get Form first); omitted settings are reset to defaults, an omitted template clears the design and an omitted field list clears the fields. |
| Update Webhook | `updateWebhook` | Replaces the settings of a form webhook: URL, delivery method, secret and SSL verification. This is a full replacement, so send every value you want to keep; an omitted secret is cleared and an omitted ssl flag resets to 1. Returns the updated webhook. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Form Submission Received | `TEAM_WEBHOOK_CALLED` | Fired when a respondent submits the form the webhook is attached to. CabinPanda POSTs a JSON body with the workspace, the form (key and name) and the submitted values (field_label, field_key, value). The 'event' field is always TEAM_WEBHOOK_CALLED and 'event_key' is a unique delivery id. Payload captured from a real CabinPanda delivery. |
