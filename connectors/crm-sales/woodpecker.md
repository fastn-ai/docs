---
description: "Woodpecker is a cold email and LinkedIn outreach platform for sales teams and agencies."
hidden: true
---

# Woodpecker

<img src="../../.gitbook/assets/connectors/lg/woodpecker.png" alt="Woodpecker logo">

Woodpecker is a cold email and LinkedIn outreach platform for sales teams and agencies. This connector covers the full Woodpecker public REST API: campaigns and campaign steps, Bounce Shield, prospects and campaign prospect management, the blacklist, inbox messages and replies, mailboxes and Microsoft Graph credentials, manual tasks, Lead Finder search and enrichment, LinkedIn profile collection, purchased domains and mailboxes, predefined reports, users, the agency (multi-client) API, and webhook subscriptions.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [woodpecker.co](https://woodpecker.co) |
| **Authentication** | Credentials you enter |
| **Slug** | `woodpecker` |

## Use it

Add Woodpecker from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.woodpecker.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Campaign Step | `addCampaignStep` | Appends a new EMAIL or LINKEDIN step to the end of a campaign, directly after the given parent step. The parent step must be the last step and must not have processed any prospects. Only campaigns in DRAFT or EDITED status can be updated. |
| Add Mailboxes In Bulk | `addMailboxesInBulk` | Connects one or more mailboxes using SMTP and IMAP credentials, with optional sending limits, tracking domains and footers. Up to 200 mailboxes per request. Processing is asynchronous - track it with Get Mailbox Batch Status. |
| Add Microsoft Mailboxes In Bulk | `addMicrosoftMailboxesInBulk` | Connects one or more Microsoft mailboxes using Microsoft Graph app-only authentication. The credential identifier may be omitted only when the account has exactly one valid Microsoft Graph credential. |
| Add Prospects To Campaign | `addProspectsToCampaign` | Enrols one or more prospects in a campaign, creating them in the global prospect list when they do not exist yet. Prospects whose global status is not ACTIVE are rejected unless the force option is enabled. Up to 20 000 prospects per request. |
| Add Prospects To Database | `addProspectsToDatabase` | Adds one or more prospects to the global prospect list without enrolling them in a campaign. Prospects that already exist are left unchanged - use Update Prospects In Database to overwrite their data. Up to 20 000 prospects per request. |
| Blacklist Agency Domains | `blacklistAgencyDomains` | Adds domains to the agency-wide blacklist so no client campaign contacts prospects on them. Up to 500 domains per request. Requires the Agency add-on. |
| Blacklist Agency Emails | `blacklistAgencyEmails` | Adds email addresses to the agency-wide blacklist so no client campaign contacts them. Up to 500 addresses per request. Requires the Agency add-on. |
| Blacklist Domains | `blacklistDomains` | Adds domains to the account blacklist so prospects on those domains are no longer contacted. Up to 500 domains per request. Existing prospects keep their status until the campaign next processes them. |
| Blacklist Emails | `blacklistEmails` | Adds email addresses to the account blacklist so those prospects are no longer contacted. Up to 500 addresses per request. |
| Check Domain Availability | `checkDomainAvailability` | Checks a specific list of domain names against a provider and returns each one's availability and price. Use it when the exact domain names are already known. |
| Clear Bounce Shield Threshold | `clearBounceShieldThreshold` | Removes the Bounce Shield Monitor bounce rate threshold from a campaign, disabling automatic pausing for it. |
| Collect LinkedIn Profiles From Posts | `collectLinkedinProfilesFromPosts` | Collects the LinkedIn profiles of people who reacted to or commented on the given posts and saves them to a new list in Woodpecker. Processing is asynchronous and consumes account credits - 0.1 credit per collected reaction profile and 0.3 per comment profile. |
| Connect Company LinkedIn Account | `connectCompanyLinkedinAccount` | Creates a LinkedIn account slot inside a client company and returns its identifier together with an authorization URL the user must open to finish connecting. The link is valid for 48 hours and an available LinkedIn slot is required. Requires the Agency add-on. |
| Create Campaign | `createCampaign` | Creates an email, LinkedIn or multichannel campaign. The sequence starts with a START step followed by 1 to 16 EMAIL or LINKEDIN steps chained through the followup property. The campaign is created in DRAFT status and is not started. |
| Create Companies | `createCompanies` | Creates client accounts under the agency, each with its own prospect database, campaigns and team access. Up to 10 per request, all created or none. Each new client account is billed periodically while it is active. Requires the Agency add-on. |
| Create Company API Key | `createCompanyApiKey` | Generates a new API key for a client company and returns it. The key authenticates requests made on behalf of that company. Requires the Agency add-on. |
| Create Microsoft Graph Credential | `createMicrosoftGraphCredential` | Saves a Microsoft Graph app-only credential used to connect Microsoft mailboxes. Woodpecker verifies that the tenant, client identifier and secret can obtain a Graph access token before storing it, and the secret is encrypted and never returned. |
| Delete Campaign | `deleteCampaign` | Permanently deletes a campaign in any status. Campaigns that are part of a workflow cannot be deleted, and a deleted campaign cannot be restored. |
| Delete Campaign Step | `deleteCampaignStep` | Deletes an EMAIL or LINKEDIN step from a campaign. The step must not have processed any prospects and must not be the first step after START. Deleted steps cannot be restored. |
| Delete Company Prospects | `deleteCompanyProspects` | Removes prospects from a client company's database and returns the deletion request identifier and the number removed. This is irreversible. Requires the Agency add-on. |
| Delete Domain | `deleteDomain` | Requests deletion of a purchased domain. The domain must belong to the account and be ready, and deleting it also deletes every mailbox attached to it. This cannot be undone. |
| Delete Domain Mailbox | `deleteDomainMailbox` | Requests deletion of a mailbox from a purchased domain. The mailbox must belong to the domain and have the PAID status. This cannot be undone. |
| Delete Microsoft Graph Credential | `deleteMicrosoftGraphCredential` | Deletes a Microsoft Graph app-only credential. Woodpecker refuses the deletion while the credential is still used by an active Microsoft mailbox. |
| Delete Prospects | `deleteProspects` | Deletes prospects from the account. Without campaign identifiers the prospects are removed globally, which also removes them from every campaign. With campaign identifiers they are only removed from those campaigns and stay in the global database. |
| Enrich Collected LinkedIn Profiles | `enrichCollectedLinkedinProfiles` | Starts an asynchronous job that enriches every profile in a collected LinkedIn list with contact and company data. Each successfully enriched profile costs 1.5 account credits. |
| Generate Campaign Statistics Report | `generateCampaignStatisticsReport` | Requests generation of the campaign-level statistics report for a date range and returns a hash. Pass the hash to Get Report to fetch the results once they are ready. Data can be generated for the last 30 days. |
| Generate LinkedIn Connection Link | `generateLinkedinConnectionLink` | Generates a fresh authorization URL for an existing LinkedIn account in a client company, so the user can connect or reconnect it. The link is valid for 48 hours. Requires the Agency add-on. |
| Generate Open Rate Report | `generateOpenRateReport` | Requests generation of the open rate report, broken down by campaign, day, mailbox, path, step and version, and returns a hash. Pass the hash to Get Report to fetch the results. Data can be generated for the last 30 days. |
| Generate Sent Messages Report | `generateSentMessagesReport` | Requests generation of the sent messages report, broken down by campaign, day, path, step and version, and returns a hash. Pass the hash to Get Report to fetch the results. Data can be generated for the last 30 days. |
| Generate Step Statistics Report | `generateStepStatisticsReport` | Requests generation of the step-level statistics report, grouped by campaign, step and A/B version, and returns a hash. Pass the hash to Get Report to fetch the results. Data can be generated for the last 30 days. |
| Get Agency Deliverability Statistics | `getAgencyDeliverabilityStatistics` | Retrieves per-client campaign performance for a date range - emails sent, delivered, opened, replied to and bounced - with a comparison against the preceding period of the same length. Clients with no activity in the period are omitted. Requires the Agency add-on. |
| Get Bounce Shield Threshold | `getBounceShieldThreshold` | Retrieves the Bounce Shield Monitor bounce rate threshold configured for a campaign, as a percentage, or null when no threshold is set. |
| Get Campaign | `getCampaign` | Retrieves the full structure of a campaign, including its settings, attached mailboxes and LinkedIn accounts, and every step with its delivery times and content versions. Use it to obtain step and version identifiers needed by the update actions. |
| Get Campaign Statistics | `getCampaignStatistics` | Retrieves delivery, open, reply, bounce and opt-out statistics for a single campaign, together with the content of its email steps. |
| Get Current Account | `getCurrentAccount` | Retrieves the Woodpecker user and company that the API key belongs to. Use it to verify the credential and to obtain the account (firm) identifier. |
| Get Domain | `getDomain` | Retrieves one purchased domain with its owner data, forwarding and redirect settings, readiness status and mailbox summary. The domain lookup is case-insensitive. |
| Get Domain Mailbox | `getDomainMailbox` | Retrieves one mailbox under a purchased domain, including its credentials and IMAP and SMTP settings. Domain and mailbox lookups are case-insensitive. |
| Get Domain Owner | `getDomainOwner` | Retrieves the domain owner details saved for the account. These details are required before any domain can be ordered. |
| Get Lead Enrichment | `getLeadEnrichment` | Retrieves one lead enrichment batch by its identifier, with the processing state of each lead in it. |
| Get LinkedIn Collection Job | `getLinkedinCollectionJob` | Retrieves a single LinkedIn profile collection job by its identifier, with its current status and progress. Polling does not consume credits. |
| Get LinkedIn Enrichment Status | `getLinkedinEnrichmentStatus` | Retrieves the processing state and result summary of a LinkedIn profile enrichment job. |
| Get Mailbox | `getMailbox` | Retrieves the configuration of a single connected email account, including its connection settings, sending limits and warm-up state. |
| Get Mailbox Batch Status | `getMailboxBatchStatus` | Retrieves the progress and per-mailbox outcome of a bulk mailbox connection batch, including any connection errors. |
| Get Prospect Enrichment | `getProspectEnrichment` | Retrieves the status details of a single prospect enrichment batch by its identifier. |
| Get Prospect Responses | `getProspectResponses` | Retrieves every reply received from a single prospect, sorted by delivery date ascending, optionally narrowed to specific campaigns. |
| Get Prospects In Campaign | `getProspectsInCampaign` | Retrieves a paginated list of prospects enrolled in the given campaigns, each with their campaign status, campaign details and interest level in that campaign. A prospect enrolled in several requested campaigns is returned once per campaign. |
| Get Report | `getReport` | Retrieves a generated report by its hash. Generation takes a moment, so poll the status field until it reaches READY. |
| Invite Guests To Company | `inviteGuestsToCompany` | Invites guests to a client company, or resends invitations to guests who have not accepted yet. This sends real invitation emails. Up to 10 guests per request, all invited or none. Requires the Agency add-on. |
| List Agency Blacklisted Domains | `listAgencyBlacklistedDomains` | Retrieves the domains blacklisted across the whole agency. The domain filter can be used to check whether specific domains are on the list. Requires the Agency add-on. |
| List Agency Blacklisted Emails | `listAgencyBlacklistedEmails` | Retrieves the email addresses blacklisted across the whole agency. The email filter can be used to check whether specific addresses are on the list. Requires the Agency add-on. |
| List Blacklisted Domains | `listBlacklistedDomains` | Retrieves the account's blacklisted domains in alphabetical order. The domain filter can be used to check whether specific domains are on the list. |
| List Blacklisted Emails | `listBlacklistedEmails` | Retrieves the account's blacklisted email addresses. The email filter can be used to check whether specific addresses are on the list. |
| List Campaigns | `listCampaigns` | Retrieves all campaigns in the account with their basic settings, optionally filtered by status or by a list of campaign identifiers. |
| List Companies | `listCompanies` | Retrieves the client companies managed by the agency, with their identifier, name, owner, active state, running campaign count and connected account count. Requires the Agency add-on. |
| List Company API Keys | `listCompanyApiKeys` | Retrieves the API keys of a client company that were created by the requesting user. Requires the Agency add-on. |
| List Company Email Accounts | `listCompanyEmailAccounts` | Retrieves the email accounts linked to a client company, including type, provider, from name, IMAP identifier, error status and the number of campaigns running from each. Requires the Agency add-on. |
| List Company Users | `listCompanyUsers` | Retrieves the users of a client company, with their identifier, name, email, roles and guest permissions. Requires the Agency add-on. |
| List Domain Mailboxes | `listDomainMailboxes` | Retrieves the active mailboxes belonging to a purchased domain, with their basic information. Credentials and connection settings come from Get Domain Mailbox. |
| List Domain Providers | `listDomainProviders` | Retrieves the providers available for domain and mailbox orders, with the mailbox price for each in the account currency. |
| List Domains | `listDomains` | Retrieves the domains purchased through Woodpecker for the account, with their status, expiry date and mailbox count. |
| List Inbox Messages | `listInboxMessages` | Retrieves messages from the Woodpecker inbox, newest first, with cursor-based pagination. Results can be narrowed by mailbox, campaign, prospect status, interest level, read state or search phrases. |
| List Lead Enrichments | `listLeadEnrichments` | Retrieves lead enrichment batches requested for the account, with their per-lead processing state. Defaults to the last 24 hours unless a cutoff date is given. |
| List Lead Search Criteria | `listLeadSearchCriteria` | Retrieves the Lead Finder search criteria currently available to the account, grouped into freetext criteria you supply values for and enumerated criteria whose allowed values must be fetched separately. Use it instead of hardcoding criterion names. |
| List Lead Search Criterion Values | `listLeadSearchCriterionValues` | Retrieves the allowed values of an enumerated Lead Finder criterion such as COUNTRY or INDUSTRY, with filtering and pagination so the values can drive a searchable dropdown. |
| List LinkedIn Accounts | `listLinkedinAccounts` | Retrieves the LinkedIn accounts connected to the Woodpecker account with their session status, user information and subscription level. |
| List LinkedIn Collection Jobs | `listLinkedinCollectionJobs` | Retrieves LinkedIn profile collection jobs for the account, newest first, in fixed pages of 100. Use it to monitor collection progress and to find collector and list identifiers. Polling does not consume credits. |
| List Mailboxes | `listMailboxes` | Retrieves every email account connected to the Woodpecker account, with its SMTP and IMAP settings, connection errors, sending limits, warm-up state and freeze dates. Use it to obtain the SMTP identifiers required when creating campaigns. |
| List Manual Tasks | `listManualTasks` | Retrieves the manual tasks created by the campaigns in the account. |
| List Microsoft Graph Credentials | `listMicrosoftGraphCredentials` | Retrieves the Microsoft Graph app-only credentials saved for the account. Client secrets are never returned. Use it to find the credential identifier needed when connecting Microsoft mailboxes in bulk. |
| List Prospect Enrichments | `listProspectEnrichments` | Retrieves recent prospect enrichment statuses for the account, optionally filtered to specific prospect email addresses. Send no emails to get the most recent statuses. |
| List Prospects | `listProspects` | Retrieves a paginated list of prospects in the account together with their snippet data, global status and contact dates. Results can be filtered by identifier, status, contact history, interest level and activity. |
| List Users | `listUsers` | Retrieves the confirmed, active users of the Woodpecker account together with their roles. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | Retrieves every webhook subscription on the account, regardless of which user created it. Each entry pairs a target URL with an event. |
| Make Campaign Editable | `makeCampaignEditable` | Switches a campaign into EDITED status so that its settings, steps and content can be changed. Running campaigns must be made editable before any update action is accepted. |
| Order Domain Mailboxes | `orderDomainMailboxes` | Orders additional mailboxes for domains already purchased in Woodpecker. This creates billable assets paid from the account's prepaid funds. |
| Order Domains | `orderDomains` | Orders domains together with mailboxes preconfigured for cold emailing. This creates billable assets paid from the account's prepaid funds, and domain owner details must be saved first. Processing is asynchronous. |
| Pause Campaign | `pauseCampaign` | Pauses a running campaign. Queued prospects stop being contacted until the campaign is run again. |
| Queue Lead Enrichments | `queueLeadEnrichments` | Queues up to 50 Lead Finder search results for asynchronous enrichment and returns the batch identifier used to poll progress. Enriching a lead and finding an email costs 1.5 account credits, charged only when data is found. |
| Queue Prospect Enrichments | `queueProspectEnrichments` | Queues prospects that already exist in the global prospect database for asynchronous enrichment, matching them by email address. It updates matching prospects and never creates new ones. Successfully enriching a prospect costs 1.5 account credits. |
| Remove Agency Blacklisted Domains | `removeAgencyBlacklistedDomains` | Removes domains from the agency-wide blacklist. Up to 500 domains per request. Requires the Agency add-on. |
| Remove Agency Blacklisted Emails | `removeAgencyBlacklistedEmails` | Removes email addresses from the agency-wide blacklist. Up to 500 addresses per request. Requires the Agency add-on. |
| Remove Blacklisted Domains | `removeBlacklistedDomains` | Removes domains from the account blacklist. Up to 500 domains per request. Prospects already marked BLACKLISTED keep that status. |
| Remove Blacklisted Emails | `removeBlacklistedEmails` | Removes email addresses from the account blacklist. Up to 500 addresses per request. Prospects already marked BLACKLISTED keep that status. |
| Reply To Inbox Message | `replyToInboxMessage` | Sends a reply to a message received in the Woodpecker inbox, through the mailbox that received it or another connected SMTP mailbox. This delivers a real email to the recipient and marks the original message as read. |
| Run Campaign | `runCampaign` | Starts or resumes a campaign so that Woodpecker begins contacting its prospects. This sends real email and LinkedIn messages to everyone enrolled in the campaign. |
| Save Domain Owner | `saveDomainOwner` | Creates or replaces the domain owner details used to register purchased domains. The request replaces the saved record, so the complete owner object must be supplied. |
| Search Domain Availability | `searchDomainAvailability` | Searches a provider for available domain suggestions matching a phrase, returning the proposals with their prices. |
| Search Leads | `searchLeads` | Searches Lead Finder for people matching the given criteria and returns a compact result set for selecting leads to enrich. This consumes one account credit per lead returned. |
| Search Prospects | `searchProspects` | Searches prospects by field values such as email, company, tags or any snippet. Multiple criteria of different types are combined with AND, and criteria of the same type with OR. All fields except email and organization_id use a broad substring match. |
| Set Bounce Shield Threshold | `setBounceShieldThreshold` | Sets or replaces the Bounce Shield Monitor bounce rate threshold for a campaign. Woodpecker pauses the campaign automatically once its bounce rate reaches this percentage. |
| Set Domain Email Forwarding | `setDomainEmailForwarding` | Sets the address that all email sent to mailboxes under a purchased domain is forwarded to. The domain must already be ready for use. |
| Set Domain Redirect URL | `setDomainRedirectUrl` | Sets the URL visitors are redirected to when they open a purchased domain. The domain must already be ready for use. |
| Stop Campaign | `stopCampaign` | Stops a campaign. Unlike pausing, a stopped campaign restarts its sequence for prospects when it is run again. |
| Subscribe To Webhook | `subscribeWebhook` | Subscribes a target URL to a Woodpecker event so that matching events are delivered to it as an array of objects. The same event can be subscribed up to five times per account, each with a distinct target URL. |
| Unsubscribe From Webhook | `unsubscribeWebhook` | Removes a webhook subscription so the target URL stops receiving that event. The target URL and event pair identifies the subscription. |
| Update Campaign Settings | `updateCampaignSettings` | Updates campaign-wide settings such as the name, attached mailboxes, timezone and sending limits. Supports partial updates. Only campaigns in DRAFT or EDITED status can be updated. |
| Update Campaign Step | `updateCampaignStep` | Replaces the delivery time windows of an EMAIL step. The whole delivery time object is overwritten, so days left out of the request stop sending. Only campaigns in DRAFT or EDITED status can be updated. |
| Update Campaign Step Version | `updateCampaignStepVersion` | Updates the content of a single A/B version of a campaign step - the subject line, message body, signature setting and open tracking for EMAIL steps, or the message and InMail subject for LINKEDIN steps. Supports partial updates. |
| Update Company Guest Permissions | `updateCompanyGuestPermissions` | Changes the permissions of guests who already belong to a client company. Requires the Agency add-on. |
| Update Domain Mailbox Profile Picture | `updateDomainMailboxProfilePicture` | Sets or replaces the profile picture of a mailbox under a purchased domain, so recipients recognise the sender. Currently supported for Google mailboxes. |
| Update Mailbox | `updateMailbox` | Updates the signature footer of a connected SMTP mailbox. The footer is the only property this endpoint can change. |
| Update Microsoft Graph Credential | `updateMicrosoftGraphCredential` | Renames a Microsoft Graph app-only credential or rotates its client secret. Rotating the secret requires both the new secret and its expiry date in the same request. |
| Update Prospects In Campaign | `updateProspectsInCampaign` | Updates prospects already enrolled in a campaign - their campaign status, interest level, earliest sending date, tags and snippet data. Prospects that are not enrolled yet are added. Omitted fields are left unchanged. |
| Update Prospects In Database | `updateProspectsInDatabase` | Updates the status and snippet data of prospects in the global prospect list, matching them by email address. Prospects that do not yet exist are created. Omitted fields are left unchanged. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Campaign Completed | `campaign_completed` | Fires when a campaign status changes to COMPLETED, 24 hours after the last prospect was contacted. |
| Campaign Email Sent | `campaign_sent` | Fires when a campaign email is sent to a prospect. The payload carries the prospect data and the content of the sent message. |
| Campaign Paused By Bounce Shield | `campaign_paused_by_bounce_shield` | Fires when Bounce Shield automatically pauses a running campaign because its bounce rate exceeded the configured threshold. |
| Email Opened | `email_opened` | Fires when a prospect opens a tracked email. |
| Follow-Up Scheduled After Autoreply | `followup_after_autoreply` | Fires when a follow-up is scheduled after an autoresponse was received. |
| Link Clicked | `link_clicked` | Fires when a prospect clicks a tracked link inside an email. |
| LinkedIn Account Connected | `linkedin_automation_account_connected` | Fires when a LinkedIn account is successfully connected to Woodpecker. |
| LinkedIn Account Disconnected | `linkedin_automation_account_disconnected` | Fires when a LinkedIn account is disconnected from Woodpecker. |
| LinkedIn Connection Request Accepted | `linkedin_automation_connection_request_accepted` | Fires when a prospect accepts a LinkedIn connection request sent through Woodpecker automation. |
| LinkedIn Direct Message Sent | `linkedin_automation_direct_message_sent` | Fires when a LinkedIn direct message is sent through Woodpecker automation. |
| LinkedIn Prospect Replied | `linkedin_automation_prospect_replied` | Fires when a prospect replies in a LinkedIn conversation tracked by automation, including direct messages, InMail and replies to connection requests. |
| Manual Task Completed | `task_done` | Fires when a manual task is marked as done. |
| Manual Task Created | `task_created` | Fires when a manual task is created for a prospect. |
| Manual Task Ignored | `task_ignored` | Fires when a manual task is marked as ignored. |
| Prospect Autoreplied | `prospect_autoreplied` | Fires when an autoreply is detected or a prospect's status is manually set to AUTOREPLIED. |
| Prospect Blacklisted | `prospect_blacklisted` | Fires when a prospect's status is updated to BLACKLISTED. |
| Prospect Bounced | `prospect_bounced` | Fires when a bounce is detected or a prospect's status is manually set to BOUNCED. |
| Prospect Marked Interested | `prospect_interested` | Fires when a prospect's interest level is set to INTERESTED. |
| Prospect Marked Invalid | `prospect_invalid` | Fires when a prospect's email address is marked INVALID by the built-in validation or manually. |
| Prospect Marked Maybe Later | `prospect_maybe_later` | Fires when a prospect's interest level is set to MAYBE_LATER. |
| Prospect Marked Not Interested | `prospect_not_interested` | Fires when a prospect's interest level is set to NOT_INTERESTED. |
| Prospect Non-Responsive | `prospect_non_responsive` | Fires when a prospect's campaign status changes to NON_RESPONSIVE. |
| Prospect Opted Out | `prospect_opt_out` | Fires when a prospect unsubscribes or their status is manually set to OPT_OUT. |
| Prospect Replied | `prospect_replied` | Fires when a prospect's reply is detected or their status is manually set to RESPONDED. |
| Prospect Saved | `prospect_saved` | Fires when a prospect is added to the database or an existing prospect is updated. |
| Secondary Response Received | `secondary_replied` | Fires when a secondary response is detected - a further reply after the first one. |
