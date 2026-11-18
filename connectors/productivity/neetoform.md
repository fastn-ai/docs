---
description: "NeetoForm is a form builder from the neeto suite."
hidden: true
---

# NeetoForm

<img src="../../.gitbook/assets/connectors/lg/neetoform.png" alt="NeetoForm logo">

NeetoForm is a form builder from the neeto suite. This connector wraps the NeetoForm external REST API (v2, plus the deprecated v1) so you can list and create forms, read form submissions with their answers and submitter user-agent details, and manage workspace team members. Authentication is a workspace API key sent in the X-Api-Key header against your workspace subdomain host.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [neetoform.com](https://neetoform.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `neetoform` |

## Use it

Add NeetoForm from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.neetoform.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Team Members | `addTeamMembers` | Invite one or more people to the NeetoForm workspace (v2 API). The call is all-or-nothing: if any address is malformed or the role does not exist in the workspace, nobody is added and the error names the offending values. An email that already belongs to the workspace is reactivated rather than duplicated and its role is overwritten. WARNING: unless send_invitation_email is set to the string "false", NeetoForm emails an invitation to every address listed. Returns a confirmation message only, so follow with List Team Members to read the new member ids. |
| Add Team Members (v1 Legacy) | `addTeamMembersV1` | Invite one or more people to the workspace using NeetoForm's legacy v1 API. Behaves exactly like Add Team Members (v2) but answers HTTP 200 instead of 201. WARNING: unless send_invitation_email is set to the string "false", NeetoForm emails an invitation to every address listed. NeetoForm marks v1 deprecated in its own docs - prefer the v2 action. |
| Create Form | `createForm` | Create a new form in the NeetoForm workspace (v2 API). The new form is created as an unpublished draft with no questions; its questions, design and publish state can only be edited in the NeetoForm web app. Returns the created form including its id and public attempt URL. NOTE: NeetoForm's external API has no delete-form or update-form endpoint, so a form created here can only be removed from the NeetoForm web app. |
| Get Form | `getForm` | Show one form with its questions, in the order they appear on the form (GET /api/external/v2/forms/{form_id}). |
| Get Team Member | `getTeamMember` | Fetch one active NeetoForm workspace team member by id (v2 API), returning their email, first and last name, time zone, profile image URL, active flag and organization role. Answers 404 with {"error":"User does not exist."} when the id is unknown or the member has been removed. |
| List Form Submissions | `listFormSubmissions` | List the completed submissions of one NeetoForm form (v2 API). Each submission carries its id, submitted timestamp, the answers as a responses array (question label, field kind, slug and value) and the submitter's user-agent details including IP address, browser and operating system. Get form_id from List Forms. Omit both paging inputs to return every submission. |
| List Form Submissions (v1 Legacy) | `listFormSubmissionsV1` | List the completed submissions of one form using NeetoForm's legacy v1 API. NeetoForm marks v1 deprecated in its own docs - prefer List Form Submissions (v2), which returns the identical payload. Kept for workspaces still pinned to v1. |
| List Forms | `listForms` | List all forms in the workspace, oldest first by default (order=desc for newest first). Filter by status or title search. Without page_number every matching form is returned. |
| List Forms (v1 Legacy) | `listFormsV1` | List every form in the workspace using NeetoForm's legacy v1 API. NeetoForm marks v1 deprecated in its own docs - prefer List Forms (v2), which returns the identical payload. Kept for workspaces still pinned to v1. |
| List Team Members | `listTeamMembers` | List the active team members of the NeetoForm workspace (v2 API), with each member's id, email, first and last name, time zone, profile image URL, active flag and organization role, plus pagination metadata. Use the returned id with Get Team Member, Update Team Member or Remove Team Member. |
| List Team Members (v1 Legacy) | `listTeamMembersV1` | List the active workspace team members using NeetoForm's legacy v1 API, which spells the collection team_members with an underscore. NeetoForm marks v1 deprecated in its own docs - prefer List Team Members (v2), which returns the identical payload. |
| Remove Team Member | `removeTeamMember` | Deactivate and remove one NeetoForm workspace team member by id (v2 API). Their forms and submissions are left intact. Returns 204 with no body on success, so confirm with Get Team Member, which then answers 404 {"error":"User does not exist."}. DANGER: NeetoForm refuses 422 only for the LAST Admin of the workspace; any other member, including the account whose API key you are using, can be removed and cannot be restored through the API. |
| Remove Team Member (v1 Legacy) | `removeTeamMemberV1` | Deactivate and remove one workspace team member by id using NeetoForm's legacy v1 API. Unlike the v2 route it answers HTTP 200 with {"message":"Team member has been removed"}. This per-id route is live but absent from NeetoForm's published v1 spec, which documents a collection-level DELETE by email that does not actually exist. DANGER: only the LAST Admin is protected, so any other member - including the account owning your API key - can be removed and cannot be restored through the API. Note: the v1 docs describe DELETE /team_members with an emails body, but that route returns 404 live; the per-id route is what the API serves. |
| Update Team Member | `updateTeamMember` | Update one NeetoForm workspace team member by id (v2 API). Only the fields you pass are changed. Returns the full updated team member, so the response itself confirms the new values. Changing organization_role changes what that person may do in the workspace, so avoid pointing it at the workspace's only Admin. |
| Update Team Member (v1 Legacy) | `updateTeamMemberV1` | Update one workspace team member by id using NeetoForm's legacy v1 API. Only the fields you pass are changed and the full updated member is returned. NeetoForm marks v1 deprecated in its own docs - prefer Update Team Member (v2). Note that v1 has no get-by-id route, so read the member back with List Team Members (v1 Legacy) or Get Team Member (v2). |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Form Submitted | `form_submitted` | Fires the moment someone completes and submits a NeetoForm form. REGISTRATION IS MANUAL - NeetoForm exposes no webhook-registration API, so the customer pastes the fastn trigger URL into NeetoForm themselves: open the NeetoForm workspace, go to Admin Panel &gt; Webhooks &gt; Add New Webhook, paste the fastn trigger URL as the endpoint (it must accept POST), choose the form-submission event, and click Save Changes. Deliveries and their HTTP responses are inspectable under Admin Panel &gt; Webhooks by clicking the endpoint URL; a failed delivery is retried after 5 minutes and then at widening intervals for up to 6 hours. SIGNATURE: NeetoForm's Add New Webhook screen offers an optional Secret. If one is set, every delivery carries header x-neeto-webhook-signature whose value is 'sha256=' followed by the hex HMAC-SHA256 of the raw JSON body (HTML-escaped) keyed by that secret. fastn cannot currently hold a per-webhook secret for an APP-type config, so this config is set to NONE verification - LEAVE THE SECRET FIELD BLANK IN NEETOFORM, or the signature will go unchecked. EVENT ID: NeetoForm's payload carries no event-type discriminator (only webhook.source = 'NeetoForm') and the vendor publishes no machine-readable event list, so 'form_submitted' is a fastn-side identifier for the single event NeetoForm documents, not a vendor slug. PAYLOAD SCHEMA IS MODELLED from NeetoForm's published sample payload (help.neetoform.com/articles/sample-payload-for-webhook), not captured from a live delivery. The answers object is keyed by each question's field code from its advanced properties, so its keys differ from form to form. |
