---
description: "Typeform is an online form and survey builder. Create and delete forms, read and delete responses, and manage themes, images, workspaces and webhooks."
hidden: true
---

# Typeform

<img src="../../.gitbook/assets/connectors/lg/typeform.png" alt="Typeform logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [typeform.com](https://typeform.com) |
| **Authentication** | Access token, OAuth 2.0 |
| **Slug** | `typeform` |

## Setup

Your customers sign in to Typeform through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Typeform from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Typeform**.
2. Select **Connect** on the Typeform card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Typeform offers more than one sign-in method. Choose one in **Auth Method**, then:

   * For a key or credential method, fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

     <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

   * For OAuth 2.0, keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Typeform and approve access in the window that opens.

     <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Typeform's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Image</td><td><code>addImage</code></td><td>Add an image to your account, either base64-encoded (image) or by URL. Required: file_name plus one of image or url.</td></tr><tr><td>Add Workspace Members</td><td><code>addWorkspaceMembers</code></td><td>Add members to a workspace via JSON Patch add operations on /members.</td></tr><tr><td>Create Form</td><td><code>createForm</code></td><td>Create a new form. Only the title is required; pass optional fields/settings/theme/workspace/logic/hidden/screens/variables to fully build out the form.</td></tr><tr><td>Create Or Update Webhook</td><td><code>createOrUpdateWebhook</code></td><td>Create or update a webhook on a form by tag (PUT). Required: form_id, tag, url, enabled.</td></tr><tr><td>Create Theme</td><td><code>createTheme</code></td><td>Create a new theme. Required: name, font, and colors (answer, background, button, question).</td></tr><tr><td>Create Workspace</td><td><code>createWorkspace</code></td><td>Create a new workspace. Required: name.</td></tr><tr><td>Delete Form</td><td><code>deleteForm</code></td><td>Delete a form and all of its responses by form ID.</td></tr><tr><td>Delete Image</td><td><code>deleteImage</code></td><td>Delete an image by ID.</td></tr><tr><td>Delete Responses</td><td><code>deleteResponses</code></td><td>Delete responses from a form by their response/token IDs.</td></tr><tr><td>Delete Theme</td><td><code>deleteTheme</code></td><td>Delete a theme by ID.</td></tr></tbody></table>

<details>

<summary>View 20 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Delete a webhook from a form by its tag.</td></tr><tr><td>Delete Workspace</td><td><code>deleteWorkspace</code></td><td>Delete a workspace by ID.</td></tr><tr><td>Get Form</td><td><code>getForm</code></td><td>Retrieve a single form by its unique ID, including all fields, logic, settings, theme and workspace references.</td></tr><tr><td>Get Form Messages</td><td><code>getFormMessages</code></td><td>Retrieve the customizable on-screen messages (button labels, errors, etc.) for a form.</td></tr><tr><td>Get Image</td><td><code>getImage</code></td><td>Retrieve metadata for a single image by ID.</td></tr><tr><td>Get Insights Summary</td><td><code>getInsightsSummary</code></td><td>Retrieve aggregate insights/metrics summary for a form (views, starts, submissions, completion and drop-off rates per question).</td></tr><tr><td>Get Theme</td><td><code>getTheme</code></td><td>Retrieve a single theme by its ID.</td></tr><tr><td>Get Webhook</td><td><code>getWebhook</code></td><td>Retrieve a single webhook for a form by its tag.</td></tr><tr><td>Get Workspace</td><td><code>getWorkspace</code></td><td>Retrieve a single workspace by ID, including its members.</td></tr><tr><td>List Forms</td><td><code>listForms</code></td><td>Retrieve a list of forms in your account. FREE read endpoint - credit-safe validation. Supports pagination and search.</td></tr><tr><td>List Images</td><td><code>listImages</code></td><td>Retrieve all images in your account.</td></tr><tr><td>List Responses</td><td><code>listResponses</code></td><td>Retrieve responses (submissions) for a form, with full answers, metadata, hidden fields and calculated scores. Supports filtering and pagination.</td></tr><tr><td>List Themes</td><td><code>listThemes</code></td><td>Retrieve all themes in your account, with pagination.</td></tr><tr><td>List Webhooks</td><td><code>listWebhooks</code></td><td>Retrieve all webhooks configured for a form.</td></tr><tr><td>List Workspaces</td><td><code>listWorkspaces</code></td><td>Retrieve all workspaces in your account, with pagination and search.</td></tr><tr><td>Patch Form</td><td><code>patchForm</code></td><td>Partially update a form using JSON Patch operations (PATCH). Pass an array of {op, path, value} operations in the operations field.</td></tr><tr><td>Update Form</td><td><code>updateForm</code></td><td>Fully replace a form definition (PUT). Send the complete form object; any field omitted is removed. Use Patch Form for partial updates.</td></tr><tr><td>Update Form Messages</td><td><code>updateFormMessages</code></td><td>Replace the customizable on-screen messages for a form. Pass a messages object of message keys to strings.</td></tr><tr><td>Update Theme</td><td><code>updateTheme</code></td><td>Update an existing theme by ID. Replaces name, font, and colors.</td></tr><tr><td>Update Workspace</td><td><code>updateWorkspace</code></td><td>Update a workspace using JSON Patch operations (e.g. rename). Pass an array of {op, path, value} operations.</td></tr></tbody></table>

</details>

