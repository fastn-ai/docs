---
description: "Typeform Create, Responses, Webhooks, and Insights APIs."
hidden: true
---

# Typeform

<img src="../../.gitbook/assets/connectors/lg/typeform.png" alt="Typeform logo">

Typeform Create, Responses, Webhooks, and Insights APIs. Manage forms, responses, themes, images, workspaces, webhooks, and insights via the api.typeform.com REST API.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [typeform.com](https://typeform.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Slug** | `typeform` |

## Use it

Add Typeform from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.typeform.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Image | `addImage` | Add an image to your account, either base64-encoded (image) or by URL. Required: file_name plus one of image or url. |
| Add Workspace Members | `addWorkspaceMembers` | Add members to a workspace via JSON Patch add operations on /members. |
| Create Form | `createForm` | Create a new form. Only the title is required; pass optional fields/settings/theme/workspace/logic/hidden/screens/variables to fully build out the form. |
| Create Or Update Webhook | `createOrUpdateWebhook` | Create or update a webhook on a form by tag (PUT). Required: form_id, tag, url, enabled. |
| Create Theme | `createTheme` | Create a new theme. Required: name, font, and colors (answer, background, button, question). |
| Create Workspace | `createWorkspace` | Create a new workspace. Required: name. |
| Delete Form | `deleteForm` | Delete a form and all of its responses by form ID. Returns 204 No Content. |
| Delete Image | `deleteImage` | Delete an image by ID. Returns 204 No Content. |
| Delete Responses | `deleteResponses` | Delete responses from a form by their response/token IDs. Returns 200/204. |
| Delete Theme | `deleteTheme` | Delete a theme by ID. Returns 204 No Content. |

<details>

<summary>See 20 more actions</summary>

* **Delete Webhook** `deleteWebhook`: Delete a webhook from a form by its tag. Returns 204 No Content.
* **Delete Workspace** `deleteWorkspace`: Delete a workspace by ID. Returns 204 No Content.
* **Get Form** `getForm`: Retrieve a single form by its unique ID, including all fields, logic, settings, theme and workspace references.
* **Get Form Messages** `getFormMessages`: Retrieve the customizable on-screen messages (button labels, errors, etc.) for a form.
* **Get Image** `getImage`: Retrieve metadata for a single image by ID.
* **Get Insights Summary** `getInsightsSummary`: Retrieve aggregate insights/metrics summary for a form (views, starts, submissions, completion and drop-off rates per question).
* **Get Theme** `getTheme`: Retrieve a single theme by its ID.
* **Get Webhook** `getWebhook`: Retrieve a single webhook for a form by its tag.
* **Get Workspace** `getWorkspace`: Retrieve a single workspace by ID, including its members.
* **List Forms** `listForms`: Retrieve a list of forms in your account. FREE read endpoint - credit-safe validation. Supports pagination and search.
* **List Images** `listImages`: Retrieve all images in your account.
* **List Responses** `listResponses`: Retrieve responses (submissions) for a form, with full answers, metadata, hidden fields and calculated scores. Supports filtering and pagination.
* **List Themes** `listThemes`: Retrieve all themes in your account, with pagination.
* **List Webhooks** `listWebhooks`: Retrieve all webhooks configured for a form.
* **List Workspaces** `listWorkspaces`: Retrieve all workspaces in your account, with pagination and search.
* **Patch Form** `patchForm`: Partially update a form using JSON Patch operations (PATCH). Pass an array of {op, path, value} operations in the operations field.
* **Update Form** `updateForm`: Fully replace a form definition (PUT). Send the complete form object; any field omitted is removed. Use Patch Form for partial updates.
* **Update Form Messages** `updateFormMessages`: Replace the customizable on-screen messages for a form. Pass a messages object of message keys to strings.
* **Update Theme** `updateTheme`: Update an existing theme by ID. Replaces name, font, and colors.
* **Update Workspace** `updateWorkspace`: Update a workspace using JSON Patch operations (e.g. rename). Pass an array of {op, path, value} operations.

</details>
