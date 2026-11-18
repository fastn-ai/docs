---
description: "Noloco is a no-code platform for building internal tools, client portals and business apps on top of your existing data."
hidden: true
---

# Noloco

<img src="../../.gitbook/assets/connectors/noloco.png" alt="Noloco logo" width="64">

Noloco is a no-code platform for building internal tools, client portals and business apps on top of your existing data. This connector covers both of Noloco's GraphQL APIs: the per-app Data API (https://api.portals.noloco.io/data/{appName}) for full CRUD, CSV export and bulk/import operations over every built-in collection (Users, Companies, Files, Roles, Messages, Shared Files, Comments, Onboarding Tasks, Push Subscriptions) plus authentication, notifications and workflow execution; and the Account API (https://api.portals.noloco.io/) for managing projects, data types, data sources, templates, team and billing.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [noloco.io](https://noloco.io) |
| **Authentication** | API key |
| **Slug** | `noloco` |

## Use it

Add Noloco from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.noloco.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Invite | `acceptInvite` | Accept a Noloco portal invitation with the invitation token, set a password and return a session token. The 'profilePicture' Upload argument is not exposed (engine cannot send binary multipart parts). |
| Account: Accept Invite | `acctAcceptInvite` | Accept a Noloco BUILDER-ACCOUNT team invitation (distinct from the portal acceptInvite on the Data API). Requires email, password, confirmPassword, invitationToken, firstName and lastName; returns a session token. |
| Account: Change Plan | `acctChangePlan` | BILLING. Change the Noloco account's subscription plan. planType is one of FREE, STARTER, PRO, BUSINESS, TEAM, ENTERPRISE. Returns a refreshed session payload. |
| Account: Connect Data Source | `acctConnectDataSource` | Connect an external data source to a Noloco project. type is one of AIRTABLE, GOOGLE_SHEETS, POSTGRES, MYSQL, SMART_SUITE, INTERNAL, HUBSPOT, XANO, API; connection is the provider-specific JSON credential/selection object. |
| Account: Create Checkout Session | `acctCreateCheckoutSession` | BILLING. Create a Stripe checkout session URL for a Noloco plan upgrade. interval must be the lowercase enum value 'month' or 'year'. Returns the checkout URL as a string. |
| Account: Create Project | `acctCreateProject` | Create a new Noloco project (portal app) under a team. teamId is the numeric team id; name is optional. Subject to the account plan's project limit. |
| Account: Delete Data Type | `acctDeleteDataType` | DESTRUCTIVE. Delete a data type (table) and its records from a Noloco project. Returns the deleted id. There is no create-data-type mutation on this API, so a deleted table cannot be recreated here. |
| Account: Delete Project | `acctDeleteProject` | DESTRUCTIVE. Permanently delete a Noloco project and everything in it. The name argument is OPTIONAL in the schema — calling this with no name lets the server pick the project, so always pass the project name explicitly. |
| Account: Get Current User | `acctGetCurrentUser` | Return the Noloco account user that owns the Account API key, together with a fresh session token. SENSITIVE: the response contains a live JWT — do not log it. |
| Account: Get Data Source | `acctGetDataSource` | Fetch one external data source of a Noloco project by id. projectId is the project NAME. |

<details>

<summary>See 121 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Account: Get Data Type | `acctGetDataType` | Fetch one data type (table) of a Noloco project from the Account API, including its field definitions. projectId is the project NAME; id is the numeric data type id. |
| Account: Get Project | `acctGetProject` | Fetch one Noloco project by its project NAME (the projectId argument takes the name, not the numeric id) from the Account API. Returns the project plus its data types and media files. |
| Account: Get Template | `acctGetTemplate` | Fetch one Noloco app template by its numeric id. |
| Account: Invite User | `acctInviteUser` | Invite a collaborator to the Noloco account team by email. Sends a real invitation email. Returns the invitation createdAt and the invited public user. |
| Account: List Airtable Bases | `acctListAirtableBases` | List the Airtable bases the Noloco account has authorised, with id, name and permission level. Returns an empty array when no Airtable account is linked. |
| Account: List Data Sources | `acctListDataSources` | List the external data sources (Airtable, Google Sheets, Postgres, ...) connected to a Noloco project. projectId is the project NAME. |
| Account: List Projects | `acctListProjects` | List every Noloco project on the account, via the undocumented Account API (api.portals.noloco.io). Returns a count and the project id, name, createdAt and live flag. Uses the Account API key, not the app API key. |
| Account: List Templates | `acctListTemplates` | List the Noloco app templates available to the account, with id, name, description and category. |
| Account: Login | `acctLogin` | Log in to a Noloco builder account with email and password and return a session token plus the user. Unauthenticated operation — it does not use the Account API key. |
| Account: Publish Project | `acctPublishProject` | Publish a Noloco project so its portal goes live. Takes the project name and returns the project with its live flag. |
| Account: Recover Password | `acctRecoverPassword` | Start a Noloco account password recovery: sends a reset email to the given address and echoes the email back. |
| Account: Register | `acctRegister` | Create a new Noloco builder account. All five arguments are required. Returns a session token and the new user. There is no delete-account mutation on this API. |
| Account: Reset Password | `acctResetPassword` | Complete a Noloco account password reset using the emailed resetToken. Requires email, resetToken, password and confirmPassword; returns a fresh session token. |
| Account: Update Data Source | `acctUpdateDataSource` | Update an existing external data source on a Noloco project. All six arguments are required by the schema: id, projectName, externalId, display, connection (JSON) and type. |
| Account: Update Data Type | `acctUpdateDataType` | Re-sync/refresh one data type of a Noloco project. The schema takes exactly two arguments: projectName and the data type id. |
| Account: Update Project | `acctUpdateProject` | Patch one path inside a Noloco project's document. name is the project name, path is the JSON path segments to write (e.g. [\"settings\",\"title\"]) and value is the JSON value to set there. |
| Account: Update Team | `acctUpdateTeam` | Rename a Noloco team. id is the numeric team id and name is the new team name. Returns the team with its plan type, interval and status. |
| Account: Upload Media | `acctUploadMedia` | Upload a media file to a Noloco project's asset library. ENGINE GAP: the file argument is GraphQL Upload!, which requires a binary multipart part that the fastn engine cannot send; only the projectName variable and the operation map can be produced. |
| Account: Verify Email | `acctVerifyEmail` | Verify a Noloco account email address with the token from the verification email. Returns a boolean. |
| Bulk Update Comments | `bulkUpdateComments` | Update many comments in the Noloco app in a single call. |
| Bulk Update Companies | `bulkUpdateCompanies` | Update many company records in the Noloco app's Companies collection in a single call. |
| Bulk Update Files | `bulkUpdateFiles` | Update many file records in the Noloco app's Files collection in a single call. |
| Bulk Update Messages | `bulkUpdateMessages` | Update many message records in the Noloco app's Messages collection in a single call. |
| Bulk Update Onboarding Tasks | `bulkUpdateOnboardingTasks` | Update many onboarding tasks in the Noloco app in a single call, addressed by record id. |
| Bulk Update Push Subscriptions | `bulkUpdatePushSubscriptions` | Update many push-notification subscriptions in the Noloco app in a single call. |
| Bulk Update Roles | `bulkUpdateRoles` | Update many roles in the Noloco app in a single call. |
| Bulk Update Shared Files | `bulkUpdateSharedFiles` | Update many Shared Files records in the Noloco app in a single call. |
| Bulk Update Users | `bulkUpdateUsers` | Update many user records in one call. Each entry must carry the record id plus the fields to change. |
| Check Comment Notification Subscription | `hasCommentNotificationSubscription` | Return whether the authenticated Noloco user is subscribed to comment notifications on a specific record. |
| Create Comment | `createComment` | Create a comment on a user or company record in the Noloco app. The 'attachments' Upload argument is not exposed (engine cannot send binary multipart parts); link existing files with Attachment File IDs. |
| Create Company | `createCompany` | Create a company record in the Noloco app's Companies collection and optionally link users, messages, shared files and comments to it. |
| Create File | `createFile` | Create a file record in the Noloco app's Files collection from an already-hosted URL and its metadata. |
| Create Message | `createMessage` | Create a message record in the Noloco app's Messages collection. The GraphQL 'attachment' Upload argument is not exposed because the engine cannot send binary multipart parts; link an existing file with Attachment File ID instead. |
| Create Onboarding Task | `createOnboardingTask` | Create an onboarding task in the Noloco app, targeted at users or companies. |
| Create Push Subscription | `createPushSubscription` | Register a Web Push subscription (endpoint plus p256dh and auth keys) so the Noloco app can deliver browser notifications to that device. |
| Create Role | `createRole` | Create a role in the Noloco app, optionally granting internal, data-admin, builder or MCP access and assigning users to it. |
| Create Shared File | `createSharedFile` | Create a shared-file or folder entry in the Noloco app's Shared Files collection. The 'file' Upload argument is not exposed (engine cannot send binary multipart parts); reference an existing Files record with File ID. |
| Create User | `createUser` | Create a user record in the Noloco app's Users collection without sending an invitation email. Use Invite User instead when the person should receive an email invite. |
| Deactivate User | `deactivateUser` | Deactivate a Noloco portal user so they can no longer sign in, without deleting their record. |
| Delete Comment | `deleteComment` | Delete a comment from the Noloco app and return the deleted record. |
| Delete Company | `deleteCompany` | Delete a company record from the Noloco app's Companies collection and return the deleted record. |
| Delete File | `deleteFile` | Delete a file record from the Noloco app's Files collection and return the deleted record. |
| Delete Message | `deleteMessage` | Delete a message record from the Noloco app's Messages collection and return the deleted record. |
| Delete Onboarding Task | `deleteOnboardingTask` | Delete an onboarding task from the Noloco app and return the deleted record. |
| Delete Push Subscription | `deletePushSubscription` | Delete a push-notification subscription from the Noloco app and return the deleted record. |
| Delete Role | `deleteRole` | Delete a role from the Noloco app and return the deleted record. |
| Delete Shared File | `deleteSharedFile` | Delete a record from the Noloco app's Shared Files collection and return the deleted record. |
| Delete User | `deleteUser` | Permanently delete a user record from the Noloco app's Users collection. Returns the deleted record. Consider Deactivate User instead if you only want to block access. |
| Export Comments To CSV | `exportCommentsCsv` | Export the Noloco app's Comments collection as a base64-encoded CSV. |
| Export Companies To CSV | `exportCompaniesCsv` | Export the Noloco app's Companies collection as a base64-encoded CSV. |
| Export Files To CSV | `exportFilesCsv` | Export the Noloco app's Files collection as a base64-encoded CSV, using the same filter, sort and pagination arguments as List Files. |
| Export Messages To CSV | `exportMessagesCsv` | Export the Noloco app's Messages collection as a base64-encoded CSV. |
| Export Onboarding Tasks To CSV | `exportOnboardingTasksCsv` | Export the Noloco app's onboarding tasks as a base64-encoded CSV. |
| Export Push Subscriptions To CSV | `exportPushSubscriptionsCsv` | Export the Noloco app's push-notification subscriptions as a base64-encoded CSV. |
| Export Roles To CSV | `exportRolesCsv` | Export the Noloco app's Roles collection as a base64-encoded CSV. |
| Export Shared Files To CSV | `exportSharedFilesCsv` | Export the Noloco app's Shared Files collection as a base64-encoded CSV. |
| Export Users To CSV | `exportUsersCsv` | Export the Noloco app's Users collection as a base64-encoded CSV file, honouring the same filter, sort and pagination arguments as List Users. |
| Generate OTP Backup Codes | `generateOtpBackupCodes` | Generate a fresh set of two-factor backup codes for the authenticated Noloco user. Generating new codes invalidates any previous set. |
| Generate OTP Secret | `generateOtp` | Start two-factor enrolment for the authenticated Noloco user and return the otpauth:// URL and base32 secret to show as a QR code. |
| Get API Info | `getInfo` | Health/identity probe for the Noloco Data API. Returns a short info string for the connected app and is the cheapest way to verify the App API key and app name are correct. |
| Get Billing Plan | `getBillingPlan` | Return the Noloco billing plan attached to the app's team: plan type, status, interval, trial and period dates, and Stripe customer/subscription identifiers. |
| Get Comment | `getComment` | Fetch a single comment from the Noloco app's Comments collection by id or uuid. |
| Get Company | `getCompany` | Fetch a single company record from the Noloco app's Companies collection by id or uuid. |
| Get Current User | `getCurrentUser` | Return the authenticated principal for the Noloco Data API connection, including the user record the API key belongs to and its session token. |
| Get Demo User | `getDemoUser` | Return the Noloco app's demo user session, used by preview/demo links. Returns null when the app has no demo user configured. |
| Get File | `getFile` | Fetch a single file record from the Noloco app's Files collection by id or uuid. |
| Get Ghost User Session | `getGhostUser` | Impersonate ("ghost") a portal user and return an auth payload with a session token scoped to that user, for support and debugging. |
| Get Invitation | `getInvitation` | Look up a pending Noloco portal invitation by its invitation token and return the invited person's email and name. |
| Get Message | `getMessage` | Fetch a single message from the Noloco app's Messages collection by id or uuid. |
| Get Onboarding Task | `getOnboardingTask` | Fetch a single onboarding task from the Noloco app by id or uuid. |
| Get Project Version Info | `getProjectVersionInfo` | Return the currently published version number of the Noloco app and when it was last updated. |
| Get Push Subscription | `getPushSubscription` | Fetch a single browser push-notification subscription from the Noloco app by id or uuid. |
| Get Role | `getRole` | Fetch a single role from the Noloco app's Roles collection by id, uuid, name or reference id. |
| Get Shared File | `getSharedFile` | Fetch a single record from the Noloco app's Shared Files collection by id or uuid. |
| Get User | `getUser` | Fetch a single Noloco user record from the app's Users collection by internal id, uuid or email address. Supply exactly one identifier. Returns null when no user matches. |
| Import Comments From File | `importComments` | Bulk-import comments from an uploaded spreadsheet. The required GraphQL 'file' argument is an Upload scalar needing a binary multipart part, which the fastn engine cannot currently send. |
| Import Companies From File | `importCompanies` | Bulk-import records into the Companies collection from an uploaded spreadsheet. The required GraphQL 'file' argument is an Upload scalar needing a binary multipart part, which the fastn engine cannot currently send. |
| Import Files From File | `importFiles` | Bulk-import records into the Files collection from an uploaded spreadsheet. The required GraphQL 'file' argument is an Upload scalar needing a binary multipart part, which the fastn engine cannot currently send. |
| Import Messages From File | `importMessages` | Bulk-import messages from an uploaded spreadsheet. The required GraphQL 'file' argument is an Upload scalar needing a binary multipart part, which the fastn engine cannot currently send. |
| Import Onboarding Tasks From File | `importOnboardingTasks` | Bulk-import onboarding tasks from an uploaded spreadsheet. The required GraphQL 'file' argument is an Upload scalar needing a binary multipart part, which the fastn engine cannot currently send. |
| Import Push Subscriptions From File | `importPushSubscriptions` | Bulk-import push subscriptions from an uploaded spreadsheet. The required GraphQL 'file' argument is an Upload scalar needing a binary multipart part, which the fastn engine cannot currently send. |
| Import Roles From File | `importRoles` | Bulk-import roles from an uploaded spreadsheet. The required GraphQL 'file' argument is an Upload scalar needing a binary multipart part, which the fastn engine cannot currently send. |
| Import Shared Files From File | `importSharedFiles` | Bulk-import Shared Files records from an uploaded spreadsheet. The required GraphQL 'file' argument is an Upload scalar needing a binary multipart part, which the fastn engine cannot currently send. |
| Import Users From File | `importUsers` | Bulk-import users into the Noloco app from an uploaded CSV/XLSX file, mapping spreadsheet columns to user fields. NOTE: the required GraphQL 'file' argument is an Upload scalar that must travel as a binary multipart part, which the fastn engine cannot currently send, so this action can be configured but not driven end to end. |
| Invite User | `inviteUser` | Create a Noloco portal user and email them an invitation to set their password. This sends a real email. The 'profilePicture' Upload argument is not exposed (engine cannot send binary multipart parts). |
| List Comments | `listComments` | List records in the Noloco app's Comments collection with cursor pagination, filtering and sorting. |
| List Companies | `listCompanies` | List records in the Noloco app's Companies collection with cursor pagination, filtering and sorting. |
| List Files | `listFiles` | List records in the Noloco app's Files collection with cursor pagination, filtering and sorting. |
| List Messages | `listMessages` | List records in the Noloco app's Messages collection with cursor pagination, filtering and sorting. |
| List Notifications | `listNotifications` | List in-app notifications for the authenticated Noloco user, optionally limited to read or unread and to a time window. |
| List Onboarding Tasks | `listOnboardingTasks` | List the Noloco app's onboarding tasks with cursor pagination, filtering and sorting. |
| List Push Subscriptions | `listPushSubscriptions` | List the browser push-notification subscriptions registered in the Noloco app, with cursor pagination, filtering and sorting. |
| List Roles | `listRoles` | List the roles defined in the Noloco app with cursor pagination, filtering and sorting. |
| List Shared Files | `listSharedFiles` | List records in the Noloco app's Shared Files collection with cursor pagination, filtering and sorting. |
| List Users | `listUsers` | List users from the Noloco app's Users collection with cursor pagination, filtering and sorting. Returns totalCount, edges[].node and pageInfo cursors. |
| List Users Table | `listUsersTable` | Table view of the Users collection (userTable). Same filtering, sorting and cursor pagination as List Users, but resolved through the app's table permissions rather than the raw collection. |
| Log In Portal User | `loginUser` | Authenticate a Noloco portal user with email and password and return a session token, plus a flag indicating whether two-factor authentication is still required. |
| Mark Notifications Read | `readNotifications` | Mark the given in-app notifications as read for the authenticated Noloco user. |
| Mark Notifications Unread | `unreadNotifications` | Mark the given in-app notifications as unread for the authenticated Noloco user. |
| Reactivate User | `reactivateUser` | Reactivate a previously deactivated Noloco portal user so they can sign in again. |
| Register Portal User | `registerUser` | Self-service sign-up: create a Noloco portal user with a password and return an auth payload containing a session token. The 'profilePicture' Upload argument is not exposed (engine cannot send binary multipart parts). |
| Remove Two-Factor Auth | `removeTwoFactorAuth` | Disable two-factor authentication for a Noloco portal user, either by confirming a current OTP token or, as an admin, by naming the user id. |
| Reset Password | `resetPassword` | Set a new password for a Noloco portal user using the reset token from a password-recovery email, and return a session token. |
| Run Workflow | `runWorkflow` | Run a Noloco workflow against a specific record and return the workflow execution id. Use this to trigger the app's automations (emails, record updates, outbound webhooks) from outside Noloco. |
| Send Magic Link | `magicLinkLogin` | Email a passwordless magic sign-in link to a Noloco portal user. This sends a real email to the address supplied. |
| Send Password Recovery Email | `recoverPassword` | Trigger a password-reset email for a Noloco portal user. This sends a real email to the address supplied. |
| Set Comment Notification Subscription | `modifyCommentNotificationSubscription` | Subscribe or unsubscribe the authenticated Noloco user from comment notifications on a specific record. |
| Test Workflow | `testWorkflow` | Execute a Noloco workflow in test mode against a record and return the full execution result, including success flag, failure reason and step trace. |
| Update Comment | `updateComment` | Update an existing comment in the Noloco app. The 'attachments' Upload argument is not exposed (engine cannot send binary multipart parts). |
| Update Company | `updateCompany` | Update an existing company record in the Noloco app's Companies collection. |
| Update File | `updateFile` | Update the metadata of an existing file record in the Noloco app's Files collection. |
| Update Message | `updateMessage` | Update an existing message record in the Noloco app's Messages collection. The 'attachment' Upload argument is not exposed (engine cannot send binary multipart parts). |
| Update Notification Preference | `updateNotificationPreference` | Set how the authenticated Noloco user is notified about comments: on replies, on mentions only, or never. |
| Update Onboarding Task | `updateOnboardingTask` | Update an existing onboarding task in the Noloco app. |
| Update Push Subscription | `updatePushSubscription` | Update an existing Web Push subscription registered in the Noloco app. |
| Update Role | `updateRole` | Update an existing role in the Noloco app, including its permission flags and assigned users. |
| Update Shared File | `updateSharedFile` | Update an existing entry in the Noloco app's Shared Files collection. The 'file' Upload argument is not exposed (engine cannot send binary multipart parts). |
| Update User | `updateUser` | Update an existing user record in the Noloco app's Users collection. Only the fields you supply are changed. |
| Upsert Onboarding Tasks | `updateOnboardingTasks` | Replace or upsert the Noloco app's whole onboarding task list in one call, using full OnboardingTaskInput objects rather than per-record ids. |
| Verify OTP Backup Code | `verifyOtpBackupCode` | Complete two-factor authentication using one of the user's one-time backup codes instead of an authenticator app code. |
| Verify OTP Code | `verifyOtp` | Complete two-factor authentication by submitting the six-digit authenticator code, returning a fully authenticated session token. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Field Changed | `record.fieldChanged` | Fires when a chosen field on a record changes. Registered by hand: Noloco Studio &gt; Workflows &gt; New Workflow &gt; table &gt; Trigger = 'Field changed' &gt; pick the field &gt; Add action &gt; 'Trigger a Webhook' &gt; paste the fastn webhook URL &gt; Save &gt; Publish. Payload schema MODELLED, not captured live. |
| On-Demand Workflow Run | `workflow.onDemand` | Fires from an action button or from this connector's Run Workflow action. Registered by hand: Noloco Studio &gt; Workflows &gt; New Workflow &gt; table &gt; Trigger = 'On demand' &gt; Add action &gt; 'Trigger a Webhook' &gt; paste the fastn webhook URL &gt; Save &gt; Publish. Payload schema MODELLED, not captured live. |
| Record Created | `record.created` | Fires when a record is created in a Noloco table. Noloco has NO webhook-registration API (verified by full introspection of the Data API and field-probing of the account API), so this is registered BY HAND. CLICK-PATH: Noloco Studio (https://portals.noloco.io) &gt; Workflows in the left sidebar &gt; New Workflow &gt; choose the table &gt; Trigger = 'Record created' &gt; Add action &gt; 'Trigger a Webhook' &gt; paste the fastn webhook URL (must start with https) &gt; Save &gt; Publish the app. Noloco's outbound body is the record payload only, carries no event-type field and is not editable, so create ONE Noloco workflow per fastn webhook URL. Payload schema is MODELLED from the Noloco record shape, not captured from a live delivery. |
| Record Updated | `record.updated` | Fires when a record is updated. Registered by hand: Noloco Studio &gt; Workflows &gt; New Workflow &gt; table &gt; Trigger = 'Record updated' &gt; Add action &gt; 'Trigger a Webhook' &gt; paste the fastn webhook URL &gt; Save &gt; Publish. One Noloco workflow per fastn webhook URL. Payload schema MODELLED, not captured live. |
| Scheduled Workflow Run | `workflow.scheduled` | Fires on a time-based schedule. Registered by hand: Noloco Studio &gt; Workflows &gt; New Workflow &gt; table &gt; Trigger = 'Scheduled' &gt; set the schedule &gt; Add action &gt; 'Trigger a Webhook' &gt; paste the fastn webhook URL &gt; Save &gt; Publish. Payload schema MODELLED, not captured live. |
