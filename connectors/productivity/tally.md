---
description: "Tally is an online form builder."
hidden: true
---

# Tally

<img src="../../.gitbook/assets/connectors/lg/tally.png" alt="Tally logo">

Tally is an online form builder. This connector wraps the complete Tally REST API (https://api.tally.so): forms and their blocks, questions, submissions, per-form analytics (metrics, visits, submissions, dimensions, drop-off), workspaces and folders, organization users and invites, and webhook subscriptions with their delivery events. Authentication uses a Tally API key sent as a Bearer token, created under Settings &gt; API keys.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [tally.so](https://tally.so) |
| **Authentication** | Bearer token |
| **Slug** | `tally` |

## Use it

Add Tally from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tally.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Organization Invite | `cancelOrganizationInvite` | Cancels a pending invitation to join workspaces in a Tally organization. Only the user who created the invite can cancel it. Returns 204 No Content with an empty body on success. |
| Create Form | `createForm` | Creates a new Tally form from a list of blocks, optionally based on a template and placed in a specific workspace or folder. Returns the form metadata including the new form ID. |
| Create Organization Invites | `createOrganizationInvites` | Invites one or more people by email to join specific workspaces in a Tally organization. People who already have a Tally account are added to the workspaces directly, everyone else receives an invitation email. Requires a Tally Pro subscription and returns 204 No Content with an empty body on success. |
| Create Webhook | `createWebhook` | Creates a webhook that delivers Tally form events to an HTTPS endpoint, optionally signing each delivery and adding custom request headers. |
| Create Workspace | `createWorkspace` | Creates a new Tally workspace and adds the authenticated user as a member. Requires a Tally Pro subscription; accounts on the Free plan receive an authorization error. |
| Create Workspace Folder | `createWorkspaceFolder` | Creates a folder in a Tally workspace, optionally nested under an existing folder. Requires a Tally Pro subscription; accounts on the Free plan receive an authorization error. |
| Delete Form | `deleteForm` | Deletes a Tally form by its ID and moves it to the trash, from where it can be restored in the Tally dashboard. Returns 204 No Content with an empty body on success. |
| Delete Form Submission | `deleteFormSubmission` | Permanently deletes a single submission from a Tally form, including all of its answers. Returns 204 No Content with an empty body on success. |
| Delete Webhook | `deleteWebhook` | Deletes a Tally webhook. If it is the last webhook on its form, the form's webhooks integration is marked deleted as well. Returns 204 No Content with an empty body on success. |
| Delete Workspace | `deleteWorkspace` | Deletes a Tally workspace and moves it and all of its forms to the trash, from where they can be restored in the Tally dashboard. Returns 204 No Content with an empty body on success. |
| Delete Workspace Folder | `deleteWorkspaceFolder` | Deletes a folder and every folder nested inside it, moving any forms they contain to the trash. Requires a Tally Pro subscription; accounts on the Free plan receive an authorization error. Returns 204 No Content with an empty body on success. |
| Get Current User | `getCurrentUser` | Returns the profile of the Tally user that owns the API key, including the organization the user belongs to and the active subscription plan. Optionally updates the user's stored timezone. |
| Get Form | `getForm` | Returns a single Tally form by its ID, including all of its blocks and its settings. |
| Get Form Dimensions | `getFormDimensions` | Returns visitor breakdowns for a Tally form by traffic source, browser, operating system, device, country and city over the chosen period. |
| Get Form Drop-Off | `getFormDropOff` | Returns per-question drop-off statistics for a Tally form, showing how many respondents viewed, answered and abandoned each question over the chosen period. |
| Get Form Metrics | `getFormMetrics` | Returns aggregate analytics for a Tally form over a chosen period, including visits, starts, completions, unique respondents and completion rate. |
| Get Form Submission | `getFormSubmission` | Returns a single Tally form submission with all of its answers and the questions they belong to. |
| Get Form Submission Analytics | `getFormSubmissionAnalytics` | Returns a time series of completed and partial submission counts for a Tally form over the chosen period. |
| Get Form Visits | `getFormVisits` | Returns a time series of visit counts for a Tally form over the chosen period, bucketed at the interval the API selects for that period. |
| Get Workspace | `getWorkspace` | Returns a single Tally workspace by its ID, including its members and pending invites. |
| List Form Questions | `listFormQuestions` | Returns every question in a Tally form with its answer fields and response count. Use it to map question IDs to titles when reading submissions. |
| List Form Submissions | `listFormSubmissions` | Returns a paginated list of submissions for a Tally form together with the form's questions, optionally filtered by completion status, date range or a cursor submission. |
| List Forms | `listForms` | Returns a paginated list of the forms the authenticated user can access, optionally restricted to specific workspaces. |
| List Organization Invites | `listOrganizationInvites` | Returns every pending invitation to join workspaces in a Tally organization. |
| List Organization Users | `listOrganizationUsers` | Returns every user that belongs to a Tally organization. The organization ID is available on the Get Current User response. |
| List Webhook Events | `listWebhookEvents` | Returns a paginated list of delivery attempts for a Tally webhook, including the payload sent, the delivery status, the response status code and the retry count. |
| List Webhooks | `listWebhooks` | Returns a paginated list of every webhook configured across the forms and workspaces the authenticated user can access. |
| List Workspace Folders | `listWorkspaceFolders` | Returns the folders in a Tally workspace. Requires a Tally Pro subscription; accounts on the Free plan receive an authorization error. |
| List Workspaces | `listWorkspaces` | Returns a paginated list of the workspaces the authenticated user is a member of, each with its members, pending invites and folders. |
| Remove Organization User | `removeOrganizationUser` | Removes a user from a Tally organization. Only the organization creator can remove other members; any user may remove themselves. Returns 204 No Content with an empty body on success. |
| Retry Webhook Event | `retryWebhookEvent` | Redelivers a Tally webhook event that previously failed, posting the same payload to the webhook's configured endpoint again. Returns 204 No Content with an empty body once the retry is queued; read the outcome back with List Webhook Events. |
| Update Form | `updateForm` | Updates a Tally form's name, publication status, blocks or settings. Only the fields supplied are changed; supplying blocks replaces the form's entire block list. |
| Update Form Blocks | `updateFormBlocks` | Replaces the block list of a Tally form, and optionally its settings, in a single call. Send the complete block list because any block omitted is removed from the form. |
| Update Webhook | `updateWebhook` | Updates an existing Tally webhook. The form, endpoint URL, event types and enabled flag must all be supplied, so read the webhook first and send back every value you want to keep. Returns 204 No Content with an empty body on success. |
| Update Workspace | `updateWorkspace` | Renames a Tally workspace. Returns 204 No Content with an empty body on success; read the workspace back with Get Workspace to confirm the new name. |
| Update Workspace Folder | `updateWorkspaceFolder` | Renames a folder in a Tally workspace. Requires a Tally Pro subscription; accounts on the Free plan receive an authorization error. Returns 204 No Content with an empty body on success. |
