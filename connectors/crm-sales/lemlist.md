---
description: "Lemlist sales engagement and cold outreach automation."
---

# Lemlist

Lemlist sales engagement and cold outreach automation. Manage campaigns, leads, sequences, schedules, activities, unsubscribes, contacts, companies, tasks, inbox, people database, enrichment, lemwarm, and webhooks.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [lemlist.com](https://lemlist.com) |
| **Authentication** | Basic auth |
| **Actions** | 122 |
| **Events** | 0 |
| **Slug** | `lemlist` |

## Use it

Add Lemlist from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.lemlist.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add and Update Company | `upsertCompany` | Create a new company or update an existing one (matched by domain/linkedinUrl/companyId). Only non-empty fields applied. |
| Add and Update Contact | `upsertContact` | Create a new contact or update an existing one (matched by email/linkedinUrl/contactId). Only non-empty fields are applied. |
| Add Contacts to List | `addContactsToList` | Add existing CRM contacts to a static contact list (up to 1,000 per request). |
| Add Lead Variables | `addLeadVariables` | Add NEW custom variables to a lead. Body keys are new variable names with values. Cannot reuse existing variable names. |
| Add Step to Sequence | `addStepToSequence` | Create a step or condition within a campaign sequence. type is required; other fields depend on step type (see docs). email needs subject+message; linkedinSend/whatsappMessage/sms need message. |
| Add Unsubscribe Email or Domain | `addUnsubscribe` | Legacy: add an email address or domain to your unsubscribe list. Prefer Unsubscribe Variable. |
| Add Webhook | `addWebhook` | Create a webhook receiving real-time POST callbacks for selected events. Omit type to subscribe to all events. |
| Associate Schedule with Campaign | `associateScheduleWithCampaign` | Associate an existing schedule with a campaign. |
| Attach Labels to Conversations | `attachLabelsToConversations` | Attach one or more labels to one or more conversations for a contact. |
| Bulk Enrich Data | `bulkEnrichData` | Batch enrichment for up to 500 entities. Provide a pre-stringified JSON array of enrichment requests in 'body'. Route is under /v2/enrichments/bulk. |
| Bulk Unsubscribe Variables | `bulkUnsubscribeVariables` | Unsubscribe up to 10,000 variables in a single request. Provide a JSON array of variable values as a string in 'body'. |
| Connect Email Account | `connectEmailAccount` | Connect a custom SMTP/IMAP email account as a campaign sender. Gmail SMTP/IMAP not allowed (use OAuth). |
| Create Campaign | `createCampaign` | Create a new campaign with an auto-generated empty sequence and default schedule. Returns campaign, sequence and schedule ids. |
| Create Company Note | `createCompanyNote` | Create a new note attached to a specific company. |
| Create Contact List | `createContactList` | Create a new static contact list. Only static lists can be created via API. |
| Create Draft | `createDraft` | Create a draft for a contact (source set to api). draftOwner required. content max 30KB; channel one of email/linkedin/whatsapp/sms. |
| Create Label | `createLabel` | Create a new inbox label available to the team. |
| Create Lead in Campaign | `createLeadInCampaign` | Create a new lead and add it to a campaign. Provide email plus any lead fields. |
| Create Schedule | `createSchedule` | Create a new schedule with timing and timezone settings. |
| Create Task | `createTask` | Create a manual task (opportunity) associated with a contact/company or lead. Must be assigned to a team member with a due date. |
| Delete Activity Recording & Transcript | `deleteActivityRecordingTranscript` | Permanently delete the call recording and transcript attached to an activity. |
| Delete Company | `deleteCompany` | Delete a lemlist company. Use force=true to detach attached contacts before deletion. |
| Delete Contact | `deleteContact` | Permanently delete a contact from the Lemlist CRM by its contact id or email address. Returns 404 with code CONTACT_NOT_FOUND when no matching contact exists. |
| Delete Draft | `deleteDraft` | Soft-delete a draft. draftOwner required. |
| Delete Lead from Campaign | `deleteLead` | Remove a lead from a campaign (action=remove). Without action=remove the API unsubscribes the lead instead. |
| Delete Lead Variables | `deleteLeadVariables` | Erase the values of custom variables on a lead (does not delete the variables themselves). |
| Delete Schedule | `deleteSchedule` | Delete a specific schedule. |
| Delete Sequence Step | `deleteSequenceStep` | Delete a specific step from a sequence. |
| Delete Unsubscribe Email | `deleteUnsubscribeEmail` | Legacy: remove an email address from your unsubscribe list. Prefer Re-subscribe Variable. |
| Delete Webhook | `deleteWebhook` | Delete a specific webhook by id. |
| Disconnect Email Account | `disconnectEmailAccount` | Permanently disconnect an SMTP/IMAP email account from your team. |
| Duplicate Campaign | `duplicateCampaign` | Create a full copy of a campaign (sequences, schedules, templates) in draft state. Optional custom name. |
| Enrich Data | `enrichData` | Enrich data (find email/phone/LinkedIn) from inputs. Asynchronous, consumes credits. Provide at least one identifier and one enrichment flag. |
| Enrich Lead | `enrichLead` | Enrich an existing lead in lemlist with additional data (asynchronous, consumes credits). |
| Export Campaign Leads | `exportCampaignLeads` | Export leads from a campaign filtered by state, as CSV or JSON. |
| Export Contact List | `exportContactList` | Export contacts or companies from a CRM list as a CSV file. |
| Export Unsubscribed Contacts | `exportUnsubscribedContacts` | Export all contacts with their subscription status to a CSV file. |
| Export Unsubscribed Variables | `exportUnsubscribedVariables` | Export all unsubscribed variables to a CSV file. |
| Export Unsubscribes | `exportUnsubscribes` | Legacy: export all unsubscribed emails and domains to CSV. |
| Get Batch Campaign Stats | `getBatchCampaignStats` | Retrieve performance statistics for multiple campaigns in one request. Route is under /v2/. |
| Get Campaign | `getCampaign` | Retrieve detailed information about a specific campaign by id. |
| Get Campaign Export Status | `getCampaignExportStatus` | Check the status of an asynchronous campaign export by exportId. Statuses expire after 2 hours. |
| Get Campaign Leads | `getCampaignLeads` | Retrieve leads from a campaign, optionally filtered by state. Sorted newest first. |
| Get Campaign Reports | `getCampaignReports` | Retrieve aggregated reports/statistics for one or multiple campaigns (comma-separated campaignIds). |
| Get Campaign Schedules | `getCampaignSchedules` | Retrieve all schedules associated with a specific campaign. |
| Get Campaign Sequences | `getCampaignSequences` | Retrieve all sequences and their steps for a specific campaign. |
| Get Campaign Stats | `getCampaignStats` | Retrieve performance statistics for a specific campaign. Route is under /v2/. |
| Get Campaign Statutes | `getCampaignStatutes` | Retrieve validation statutes for a campaign (errors blocking launch, warnings, info). |
| Get Company Notes | `getCompanyNotes` | Retrieve all notes associated with a specific company. |
| Get Contact | `getContact` | Retrieve a specific contact by id or email address. |
| Get Contact Lists | `getContactLists` | Retrieve all static and dynamic contact lists, with optional name filtering. |
| Get Contact Messages | `getContactMessages` | Retrieve all messages exchanged with a specific contact. |
| Get Contact Subscription Status | `getContactSubscriptionStatus` | Check whether a contact is unsubscribed (do-not-contact). |
| Get CRM Filters | `getCrmFilters` | Retrieve available CRM filters for your team's connected CRM services. Beta-only. |
| Get Database Filters | `getDatabaseFilters` | Retrieve available filters for searching the people and companies database. |
| Get Draft | `getDraft` | Retrieve a single draft with full content. draftOwner required. |
| Get Enrichment Result | `getEnrichmentResult` | Retrieve the results of a completed enrichment request by its id. |
| Get Label | `getLabel` | Get info of a specific inbox label. |
| Get Lead by Email | `getLeadByEmail` | Retrieve a specific lead by email address. version=v2 is required. |
| Get Lead by Email or ID | `getLeadByEmailOrId` | Retrieve a lead by email or id (query params). If both given, email wins. |
| Get lemwarm Settings | `getLemwarmSettings` | Retrieve lemwarm email deliverability settings for a specific user mailbox. |
| Get Many Activities | `getManyActivities` | Retrieve the history of campaign activities/steps, optionally filtered by type, campaign, and date range. |
| Get Many Campaigns | `getManyCampaigns` | Retrieve a paginated list of all campaigns in your team. version=v2 is required. |
| Get Many Companies | `getManyCompanies` | Retrieve companies from your CRM. Use idsOrDomains to fetch specific companies (max 100) or omit for a paginated list. |
| Get Many Contacts | `getManyContacts` | Retrieve contacts by ids/emails, or search by name, email, contact list, or campaign membership. |
| Get Many Inboxes | `getManyInboxes` | Retrieve all inbox conversations for your team. |
| Get Many Labels | `getManyLabels` | List all inbox labels available to your team. |
| Get Many Schedules | `getManySchedules` | Retrieve all schedules for your team (paginated). |
| Get Many Tasks | `getManyTasks` | Retrieve all pending tasks assigned to your team members. Done tasks are excluded. |
| Get Many Unsubscribes | `getManyUnsubscribes` | Legacy: retrieve a list of all unsubscribed emails and domains. Prefer List Unsubscribed Variables. |
| Get Many Webhooks | `getManyWebhooks` | Retrieve all webhooks configured for your team. |
| Get Schedule | `getSchedule` | Retrieve details of a specific schedule by id. |
| Get Signal Agent Signals | `getSignals` | Retrieve paginated signals detected by your Signal Agents, with filtering and sorting. |
| Get Team | `getTeam` | Retrieve details about the current team (id, users, plan, beta features). |
| Get Team Credits | `getTeamCredits` | Retrieve the remaining credits balance for your team account. |
| Get Team CRM Users | `getTeamCrmUsers` | Retrieve all connected CRM services and users in your team. Beta-only. |
| Get Team Senders | `getTeamSenders` | Retrieve all team members (senders) and their associated campaigns/channels. |
| Get Unsubscribe by Email | `getUnsubscribeByEmail` | Legacy: retrieve unsubscribe information for a specific email address. |
| Get Unsubscribed Variable | `getUnsubscribedVariable` | Retrieve a specific unsubscribed variable by its value. |
| Get User | `getUser` | Retrieve all information for a specific user by their id. |
| Get User Channels | `getUserChannels` | Retrieve the connected channels (email, LinkedIn, WhatsApp) and availability for the authenticated user (API key). |
| Ignore Tasks | `ignoreTasks` | Mark one or more tasks as ignored. |
| Import Leads from CRM | `importLeadsFromCrm` | Import leads from your connected CRM into a campaign. Beta-only endpoint. |
| Launch Lead | `launchLead` | Manually launch (review) a single lead in its campaign. Requires emailPro plan or higher. |
| List Drafts | `listDrafts` | List all non-deleted drafts for a contact. draftOwner (userId or login email) is required. |
| List Fields | `listFields` | List all available fields for contacts and companies, grouped by entity. Discover field names before upserting. |
| List Unsubscribed Variables | `listUnsubscribedVariables` | Retrieve a paginated list of all unsubscribed variables (emails, domains, LinkedIn URLs, phone numbers). |
| List Watchlists | `getManyWatchlists` | Retrieve the signal watchlists configured for the team, paginated. Each watchlist defines the accounts or people whose buying signals Lemlist tracks. |
| Mark Lead as Interested | `markLeadAsInterested` | Mark a lead as interested across all campaigns. |
| Mark Lead as Interested in Campaign | `markLeadAsInterestedInCampaign` | Mark a lead as interested in a specific campaign. |
| Mark Lead as Not Interested | `markLeadAsNotInterested` | Mark a lead as not interested across all campaigns. |
| Mark Lead as Not Interested in Campaign | `markLeadAsNotInterestedInCampaign` | Mark a lead as not interested in a specific campaign. |
| Pause Campaign | `pauseCampaign` | Pause a running campaign. No-op if the campaign is not running. |
| Pause Lead | `pauseLead` | Pause a lead in all campaigns, or a specific campaign via campaignId query param. |
| Pause lemwarm | `pauseLemwarm` | Pause lemwarm email deliverability improvement for a specific user mailbox. |
| Re-subscribe Contact | `resubscribeContact` | Re-subscribe a contact, removing the do-not-contact flag. |
| Re-subscribe Variable | `resubscribeVariable` | Re-subscribe a variable, removing it from the unsubscribe list. LEAD/ABUSE source variables cannot be re-subscribed (409). |
| Remove Contacts from List | `removeContactsFromList` | Remove contacts from a static contact list (POST with action=remove). Only affects membership, not the contacts. |
| Remove Labels from Conversation | `removeLabelsFromConversation` | Remove one or more labels from a conversation for a contact. |
| Resume Paused Lead | `resumePausedLead` | Resume a paused lead in all campaigns, or a specific campaign via campaignId query param. |
| Search Companies Database | `searchCompaniesDatabase` | Search the companies database using filters, keywords, and pagination. |
| Search People Database | `searchPeopleDatabase` | Search the people database (450M+ B2B contacts) using filters, keywords, and pagination. |
| Send Inbox Email | `sendInboxEmail` | Send an email to a contact through the lemlist inbox. |
| Send Inbox LinkedIn Message | `sendInboxLinkedinMessage` | Send a LinkedIn message to a contact through the lemlist inbox. |
| Send SMS Message | `sendSmsMessage` | Send an SMS message to a contact or lead through the lemlist inbox from a phone number provisioned on your team. Returns ok and the resolved contactId. |
| Send WhatsApp Message | `sendWhatsappMessage` | Send a WhatsApp message to a contact through the lemlist inbox. |
| Set Export Email Notification | `setExportEmailNotification` | Configure an email address to be notified with the download link when a campaign export completes. |
| Start Campaign | `startCampaign` | Start or resume a paused campaign. No-op if already running. |
| Start Campaign Stats Export | `startCampaignExport` | Initiate an asynchronous export of campaign statistics to CSV. Returns an exportId to poll. |
| Start lemwarm | `startLemwarm` | Start lemwarm email deliverability improvement for a specific user mailbox. |
| Test Email Account | `testEmailAccount` | Test the SMTP and IMAP connection of an email account. |
| Unsubscribe Contact | `unsubscribeContact` | Mark a contact as unsubscribed (do-not-contact). |
| Unsubscribe Lead from Campaign | `unsubscribeLeadFromCampaign` | Unsubscribe a lead from a campaign by email (no action=remove). |
| Unsubscribe Variable | `unsubscribeVariable` | Unsubscribe a single variable. Idempotent; returns the existing record if already unsubscribed. |
| Update Campaign | `updateCampaign` | Update settings/configuration of an existing campaign. Only provided fields are changed (partial update). |
| Update Draft | `updateDraft` | Partially update an existing draft. draftOwner required. |
| Update Lead in Campaign | `updateLeadInCampaign` | Update an existing lead's default fields in a campaign. Only provided fields are changed. |
| Update Lead Variables | `updateLeadVariables` | Update the VALUES of existing custom variables on a lead. Body keys are variable names with new values. |
| Update lemwarm Settings | `updateLemwarmSettings` | Update lemwarm email deliverability settings for a specific user mailbox. |
| Update Schedule | `updateSchedule` | Update an existing schedule's parameters. Only provided fields are changed. |
| Update Sequence Step | `updateSequenceStep` | Update an existing step in a sequence. type must be included (cannot be changed). Only provided fields updated. |
| Update Task | `updateTask` | Update an existing task (title, message, priority, assignee) or mark it complete. The task id is required. The due date cannot be changed through this endpoint - create a new task instead. |
