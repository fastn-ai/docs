---
description: "Bonjoro is a personal video messaging platform for sales follow-up, onboarding and customer appreciation."
hidden: true
---

# Bonjoro

<img src="../../.gitbook/assets/connectors/bonjoro.svg" alt="Bonjoro logo" width="64">

Bonjoro is a personal video messaging platform for sales follow-up, onboarding and customer appreciation. This connector wraps the Bonjoro REST API v2 (https://www.bonjoro.com/api/v2) to manage greets (video message tasks), campaigns, contact profiles, message templates, sender signatures, teams, users, stats and in-app automations.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [bonjoro.com](https://bonjoro.com) |
| **Authentication** | Bearer token |
| **Slug** | `bonjoro` |

## Use it

Add Bonjoro from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bonjoro.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add a media | `createMedia` | Add a media. |
| Add User Device | `addUserDevice` | Registers a mobile device push notification token for the authenticated user. |
| Bulk Create Greets | `bulkCreateGreets` | Creates greets in bulk from a list of contact lines, each with an email address and optional names. |
| Bulk Update Profiles | `bulkUpdateProfiles` | Updates several contact profiles in one request. |
| Check Domain Availability | `checkDomainAvailability` | Checks whether a custom landing page domain is available to add to the team. |
| Check Signature Availability | `checkSignatureAvailability` | Checks whether an email address can be used as a sender signature for a given email transport. |
| Complete Greet | `completeGreet` | Marks a greet as complete and notifies the recipient through the given channels. This delivers the recorded video message to the recipient. |
| Create Automation Action | `createAutomationAction` | Adds an action, such as creating a Bonjoro, to an existing automation trigger. |
| Create Automation Trigger | `createAutomationTrigger` | Adds a trigger of an automation service, such as bonjoro_created, to the team automations. |
| Create Domain | `createDomain` | Adds a custom landing page domain to the team so greet landing pages can be served from it. |

<details>

<summary>See 110 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Feedback | `createFeedback` | Submits product feedback to Bonjoro about a page of the application. |
| Create Greet | `createGreet` | Creates a greet (a video message task) for one or more contact profiles. Creating a greet does not deliver anything; the video is delivered only when the greet is completed. |
| Create Invite | `createInvite` | Invites a person to join the team with a role. Bonjoro emails the invitation to the address given. |
| Create Message Template | `createMessageTemplate` | Creates a new message template pre-filled with the Bonjoro defaults. The request takes no body; use Update Message Template to customise it. |
| Create Profile | `createProfile` | Creates a contact profile from an email address with optional first and last name. |
| Create Recording | `updateRecording` | Starts a multipart video recording and returns its id and S3 upload id. The API reference documents this as PUT /api/v2/recordings, but the live route accepts only POST and requires a recording type. |
| Create Reply | `createReply` | Adds a reply to a greet on behalf of a contact profile or a team member. The greet must already be completed and sent. |
| Create Signature | `createSignature` | Adds a sender signature (from address) to the team. Bonjoro emails a verification link to that address. |
| Create User | `createUser` | Registers a new Bonjoro user account with an email address and password. |
| Delete Automation | `deleteAutomation` | Permanently deletes an automation by its ID. |
| Delete Automation Account | `deleteAutomationAccount` | Disconnects an automation account and deletes its stored credentials. |
| Delete Campaign | `deleteCampaign` | Deletes a campaign by its UUID. |
| Delete Domain | `deleteDomain` | Deletes a custom domain from the team by its ID. |
| Delete Editor Automation | `deleteEditorAutomation` | Deletes an automation from the automation editor. |
| Delete Greet | `deleteGreet` | Deletes a single greet by its ID. |
| Delete Greet Profile | `deleteGreetProfile` | Removes a contact profile from a greet. |
| Delete Greets | `deleteGreets` | Deletes several greets in a single request. |
| Delete Invite | `deleteInvite` | Revokes a pending team invite. The API reference documents the path as /api/v2/{invite_id}, but the live route is /api/v2/invites/{invite_id}. |
| Delete Media | `deleteMedia` | Deletes a media asset owned by the team. |
| Delete Message Template | `deleteMessageTemplate` | Deletes a message template by its ID. |
| Delete Recording | `deleteRecording` | Deletes a video recording by its ID. |
| Delete Signature | `deleteSignature` | Deletes a sender signature by its numeric ID. |
| Get Automation | `getAutomation` | Retrieves a single automation by its ID. |
| Get Automation Account | `getAutomationAccount` | Retrieves a connected automation account by its ID. |
| Get Automation Service | `getAutomationService` | Retrieves one automation service with its triggers, actions and authentication requirements. |
| Get Automation Service Contact Parameters | `getAutomationServiceContactParameters` | Returns the contact filter parameters, such as mailing lists, offered by a connected automation service account. The API reference documents POST, but the live route accepts only GET. |
| Get Campaign | `getCampaign` | Retrieves a single campaign by its UUID (the uuid field returned by List Campaigns, not the numeric id). |
| Get Editor Action | `getEditorAction` | Retrieves one automation editor action, including the parameters it accepts. |
| Get Editor Automation | `getEditorAutomation` | Retrieves one automation as shown in the automation editor. The API requires the automation ID both in the path and as the id query parameter. |
| Get Editor Parameter | `getEditorParameter` | Retrieves the available options of one parameter of an automation editor trigger or action. |
| Get Editor Service | `getEditorService` | Retrieves one automation editor service with the triggers and actions it exposes. |
| Get Greet Upload URL | `getGreetUploadUrl` | Returns a pre-signed S3 URL used to upload the recorded video of a greet. |
| Get Integration | `getIntegration` | Retrieves a connected third-party integration by its ID. |
| Get Link | `getLink` | Retrieves a message template link by its ID. |
| Get Message Template | `getMessageTemplate` | Retrieves a message template by its ID, including its theme, landing page and email settings. |
| Get Pricing | `getPricing` | Returns the Bonjoro plan pricing details available to the account. |
| Get Profile | `getProfile` | Retrieves a contact profile by its ID, including its engagement statistics. |
| Get Profile Attributes | `getAttributes` | Retrieves the attribute values of a contact profile in the context of a specific greet, such as reputation and custom attributes. |
| Get Recording | `getRecording` | Retrieves a video recording by its ID. |
| Get Recording Upload URL | `getRecordingUploadUrl` | Returns a pre-signed URL for uploading one part of a multipart recording upload. |
| Get Result | `getResult` | Retrieves the engagement result of a greet for one contact profile, including the greet and the profile details. |
| Get Result Stats | `getResultStats` | Retrieves lightweight engagement statistics of a greet for one contact profile. |
| Get Tasklist Counts | `getTasklistCounts` | Returns the number of outstanding tasks and replies in the tasklist of the authenticated user. |
| Get Team | `getTeam` | Retrieves a team by its ID. |
| Get Team Link | `getTeamLink` | Retrieves a message template link that belongs to a specific team. |
| Get Team Stats | `getTeamStats` | Retrieves aggregate greet statistics for the whole team, including opens, views, clicks and reactions. |
| Get User | `getUser` | Retrieves a Bonjoro user by ID. |
| Get User Stats | `getUserStats` | Retrieves greet performance statistics for one user of the team. |
| List Attribute Types | `listAttributeTypes` | Lists all contact profile attribute types available in Bonjoro, such as Default, Number, Date, Email, Phone and Company Name. |
| List Automation Accounts | `listAutomationAccounts` | Lists the accounts connected for one automation service, paginated. |
| List Automation Service Contacts | `listAutomationServiceContacts` | Lists the contacts available from a connected account of an automation service. |
| List Automation Services | `listAutomationServices` | Lists all automation services Bonjoro can connect to, with their triggers, actions and authentication requirements. |
| List Automation Triggers | `listAutomationTriggers` | Lists the automation triggers configured for the team, paginated. |
| List Automations | `listAutomations` | Lists the automations configured for the team, paginated. |
| List Campaigns | `listCampaigns` | Lists the campaigns (greet task lists) the authenticated user can access, paginated. |
| List Checklist Items | `listChecklist` | Lists the onboarding checklist items for the authenticated user and whether each one is complete. |
| List Domains | `listDomains` | Lists the custom landing page domains added to the team, paginated. |
| List Editor Actions | `listEditorActions` | Lists the automation editor actions available for a service and a trigger. |
| List Editor Automations | `listEditorAutomations` | Lists the automations as shown in the Bonjoro automation editor, paginated. |
| List Editor Services | `listEditorServices` | Lists the services available in the automation editor, optionally filtered to those offering actions or triggers. |
| List Editor Triggers | `listEditorTriggers` | Lists the triggers a service exposes in the automation editor, including the variables each trigger provides. For the bonjoro service these are the Bonjoro events, such as a Bonjoro being created or interacted with. |
| List Greet Events | `listGreetEvents` | Lists the events recorded on a greet, paginated. |
| List Greet Profiles | `listGreetProfiles` | Lists the contact profiles attached to a greet, paginated. |
| List Greet Result Stats | `listGreetResultStats` | Lists lightweight engagement statistics for sent greets, paginated. |
| List Greet Results | `listGreetResults` | Lists the results of sent greets, including opens, views, clicks and replies, paginated. |
| List Greet Todos | `listGreetTodos` | Lists the open greets still waiting to be recorded, with optional profile, assignee and search filters, paginated. |
| List Greets | `listGreets` | Lists greets (video message tasks) with optional filters by contact profile, assignee, status and search term, paginated. |
| List Industries | `listIndustries` | Lists the valid industry keys and labels used when setting up a team. |
| List Integrations | `listIntegrations` | Lists the third-party integrations connected to the team, paginated. |
| List Invites | `listInvites` | Lists the pending invites of a team, paginated. |
| List Links | `listLinks` | Lists the message template links, which hold the landing page subject, colours and call to action, paginated. |
| List Media | `listMedia` | Lists the media assets such as logos and backgrounds uploaded by the team, paginated. |
| List Message Templates | `listMessageTemplates` | Lists the message templates that define greet email and landing page designs, paginated. |
| List Notifications | `listNotifications` | Lists the in-app notifications of the authenticated user, paginated. |
| List Profile Events | `listEvents` | Lists the timeline events recorded for a contact profile, such as the events that created greets, paginated. |
| List Profiles | `listProfiles` | Lists the contact profiles (greet recipients) known to the team, paginated. |
| List Recordings | `listRecordings` | Lists the video recordings uploaded by the team, paginated. |
| List Replies | `listReplies` | Lists the replies a contact profile has sent on a greet. |
| List Segmented Campaigns | `listSegmentedCampaigns` | Lists campaigns grouped into the segments the authenticated user can and cannot access. |
| List Signatures | `listSignatures` | Lists the sender signatures (from addresses) of the team, with optional email, transport and default filters, paginated. The includes parameter must be sent in array form, which this action does for you. |
| List Stats | `listStats` | Lists greet performance statistics per team member, paginated. |
| List Stock Media | `listStockMedia` | Lists the Bonjoro stock media library used for landing page backgrounds, with an optional tag filter, paginated. |
| List Teams | `listTeams` | Lists the teams the authenticated user belongs to. |
| List Transmissions | `listTransmissions` | Lists the transmission events, such as sent and delivered, of a greet to one recipient profile. The API reference spells the path transmisions, but the live route is /api/v2/transmissions. |
| List User Campaigns | `listUserCampaigns` | Lists the campaigns a specific user belongs to. |
| List User Segmented Campaigns | `listUserSegmentedCampaigns` | Lists the campaigns of a user grouped into public and private segments. |
| List Users | `listUsers` | Lists the users who belong to the same team as the authenticated user, paginated. |
| Mark Notification Read | `markNotificationRead` | Marks an in-app notification of the authenticated user as read. |
| Mark Result Replied | `markResultReplied` | Marks the result of a greet for a contact profile as replied, or clears that flag. |
| Resend Invite | `resendInvite` | Resends the invitation email for a pending team invite. The API reference documents the path as /api/v2/{invite_id}/resend, but the live route is /api/v2/invites/{invite_id}/resend. |
| Rollup Greets | `rollupGreets` | Rolls up and deletes the greets of a given type in a campaign, returning how many were removed. |
| Test Automation Account | `testAutomationAccount` | Tests that the stored credentials of a connected automation account still work. |
| Update Automation | `updateAutomation` | Updates the name or the enabled status of an automation. |
| Update Automation Action | `updateAutomationAction` | Assigns a connected automation account to an automation action. |
| Update Automation Trigger | `updateAutomationTrigger` | Assigns a connected automation account to an automation trigger. |
| Update Campaign | `updateCampaign` | Updates a campaign name, type, goal, privacy and member users. |
| Update Demo Message Template | `updateDemoMessageTemplate` | Updates the landing page and theme of the onboarding demo message template. |
| Update Editor Automation | `updateEditorAutomation` | Updates an automation in the automation editor: its trigger, its action, whether it is enabled and its editor state. |
| Update Greet Assignee | `updateGreetAssignee` | Changes the team member assigned to record a greet. |
| Update Greet Metadata | `updateGreetMetadata` | Updates the metadata of a greet after its video upload, such as the message template used. The video and thumbnail files themselves are uploaded to the pre-signed URL returned by Get Greet Upload URL. |
| Update Greet Profile | `updateGreetProfile` | Updates the contact details and the event message of a contact profile inside a greet. |
| Update Greets | `updateGreets` | Updates the assignee and/or the campaign of several greets at once. |
| Update Message Template | `updateMessageTemplate` | Updates a message template name, sharing setting, theme colours, landing page and email template. |
| Update My Bio | `updateMyBio` | Updates the bio of the authenticated user. The API reference documents POST /api/v2/me, but that route does not exist; the live route is POST /api/v2/users/me. |
| Update Profile | `updateProfile` | Updates the email address and names of a contact profile. |
| Update Team | `updateTeam` | Updates the landing page subdomain used for the greet landing pages of a team. |
| Update User Bio | `updateUserBio` | Updates the bio shown on the greet landing pages of a team member. |
| Update User Onboarding | `updateUserOnboarding` | Updates the onboarding details of a user and their team, such as industry, company name, timezone and default sender signature. The API applies the change to the authenticated user and their team regardless of the user ID in the path. |
| Verify Domain | `verifyDomain` | Runs DNS verification for a custom domain and returns whether it is now verified. |
| Verify Signature | `verifySignature` | Sends the verification email again for a sender signature so its owner can confirm it. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Bonjoro Created | `bonjoro_created` | A Bonjoro task is created for a contact. Bonjoro has no webhook registration API (help.bonjoro.com/en/articles/1891432-webhooks-integration says webhooks are still on their timeline for a direct integration), so delivery is set up by the customer in Zapier: create a Zap with the Bonjoro trigger Bonjoro Created, add a Webhooks by Zapier POST action pointing at the fastn trigger URL, and add a literal field event = bonjoro_created to the POST body so this connector can route the event. The payload fields below are the variables Bonjoro exposes for this trigger (GET /api/v2/automation/editor/triggers?service=bonjoro); the exact JSON shape is composed by the customer in the Zap. |
| Bonjoro Interaction | `bonjoro_interacted` | A recipient interacts with a sent Bonjoro: opens it, watches it, clicks the call to action, reacts, thanks or replies. Delivery is set up by the customer in Zapier exactly as for Bonjoro Created (Bonjoro trigger Bonjoro Interaction, or the individual Zapier triggers Bonjoro Sent, Email Opened, Watched, Call to Action Clicked, Reply, Reaction, Shared, Reassigned, Dismissed and Bounced), with a literal field event = bonjoro_interacted added to the POST body. The payload fields below are the variables Bonjoro exposes for this trigger; the exact JSON shape is composed by the customer in the Zap. |
