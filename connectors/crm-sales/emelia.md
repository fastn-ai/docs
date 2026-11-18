---
description: "Emelia cold-email and LinkedIn outreach platform."
hidden: true
---

# Emelia

<img src="../../.gitbook/assets/connectors/emelia.png" alt="Emelia logo" width="64">

Emelia cold-email and LinkedIn outreach platform. Manage multichannel campaigns, contact lists and contacts, email providers and warmup, webhooks, LinkedIn scrappers, and the Email Finder / Phone Finder / Email Verifier tools through the Emelia REST API at https://api.emelia.io.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [emelia.io](https://emelia.io) |
| **Authentication** | API key |
| **Slug** | `emelia` |

## Use it

Add Emelia from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.emelia.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add a Contact to a List | `addAContactToAList` | Adds a single contact to an Emelia contact list from a flat JSON object: one key per field. Unrecognised keys automatically create a new custom variable on the account. If the list is used by campaigns, the contact is added to those campaigns too. Set Update If Exists to overwrite an existing duplicate instead of ignoring it. |
| Add a New Email Provider | `addANewEmailProvider` | Connects a new sending email provider (Google, Office 365, Exchange, generic SMTP or Google IMAP) to the Emelia account so campaigns can send from it. |
| Add a Webhook to a Scrapper | `addAWebhookToAScrapper` | Attaches a webhook URL to a LinkedIn scrapper. Emelia POSTs the event data as a JSON body to that URL when the scrapper finishes or errors. |
| Add Contact to a LinkedIn Campaign | `addContactToALinkedInCampaign` | Adds a contact to a legacy LinkedIn-only campaign, identified by their LinkedIn profile URL. |
| Add Contact to a Multichannel Campaign | `addContactToACampaign` | Adds a contact directly to a multichannel (email + LinkedIn) campaign. The contact starts receiving the campaign steps once the campaign is running. |
| Add Contact to an Email Campaign | `addContactToAnEmailCampaign` | Adds a contact to a legacy email-only campaign. |
| Add Contact to Blacklist | `addContactToBlacklist` | Blacklists an email address or a whole domain so Emelia never contacts it again from this account. |
| Add Contacts in Bulk | `addContactsInBulk` | Adds up to 100 contacts to a list in one call. Each row is the same flat contact object as Add a Contact to a List. Rows are processed independently: a failing row is reported in results with its index and error and does not block the others. |
| Add Contacts to a LinkedIn List | `addContactsToALinkedInList` | Adds a contact to a LEGACY LinkedIn contact list. The API resolves the LinkedIn profile URL against LinkedIn and rejects any URL that is not a real, reachable profile with "Invalid linkedin profile". |
| Add Contacts to a Multichannel List | `addContactsToAList` | Adds a contact to a multichannel contact list. Both a LinkedIn profile URL and an email address are required on the contact. |

<details>

<summary>See 102 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contacts to an Email List | `addContactsToAnEmailList` | Adds a contact to a LEGACY email contact list. Legacy email lists are a separate collection from the Lists endpoints: an id from List All Lists is rejected with "This contacts list doesn't exists". Legacy lists can only be created in the Emelia web app. |
| Archive a Campaign | `archiveACampaign` | Archives a multichannel campaign. Its status becomes ARCHIVED and it stops being returned by List Multichannel Campaigns, while its contacts, activities and statistics are kept. The campaign must not be RUNNING: pause it first. |
| Create a LinkedIn Campaign | `createALinkedInCampaign` | Creates an empty legacy LinkedIn-only campaign with the given name. |
| Create a List | `createAList` | Creates an empty contact list and returns its id. Add contacts afterwards with Add a Contact to a List or Add Contacts in Bulk. |
| Create a Multichannel Campaign | `createACampaign` | Creates an empty multichannel (email + LinkedIn) campaign. The name must be unused on the account. Add steps, identities and recipients before starting it. |
| Create a New LinkedIn Authentication | `createANewLinkedInAuthentication` | Registers a LinkedIn authentication configuration from session cookies so LinkedIn scrappers and campaigns can act as that account. There is no API route to delete an authentication once created. |
| Create a New LinkedIn Scrapper | `createANewLinkedInScrapper` | Creates a LinkedIn scrapper that extracts profiles from a LinkedIn search, group or event URL using the given authentication configurations. |
| Create a Webhook | `createAWebhook` | Registers a webhook URL that Emelia calls when the selected campaign events occur. Use ALL_CAMPAIGNS as the campaign id to watch every campaign of the account. |
| Create Account API Key | `createAPIKey` | SECURITY WARNING: undocumented endpoint that mints a new live Emelia API key for the account. It takes no input and cannot be undone except with Delete Account API Key. Never call it from an automated flow. |
| Create an Email Campaign | `createAnEmailCampaign` | Creates an empty legacy email-only campaign and returns its full configuration. |
| Create Tag | `createTag` | Undocumented endpoint that creates a tag used to label campaigns and contact lists. Color is required and must be one of the named colours Emelia accepts; a hex value is rejected with "Invalid tag color". |
| Delete a Campaign | `deleteACampaign` | Permanently deletes a multichannel campaign. Its contacts and contact lists are kept and stay available for other campaigns. The campaign must not be RUNNING: pause it first. |
| Delete a Contact | `deleteAContact` | Deletes a contact and its company data from a list. List counters stay in sync and the removal propagates to campaigns using that list. Find the contact id with the email or linkedinUrl lookup of List Contacts of a List. |
| Delete a LinkedIn Campaign | `deleteALinkedInCampaign` | Undocumented endpoint that permanently deletes a legacy LinkedIn campaign. This is the only way to remove a campaign created with Create a LinkedIn Campaign. |
| Delete a LinkedIn Scrapper | `deleteALinkedInScrapper` | Permanently deletes a LinkedIn scrapper and the data it collected. |
| Delete a List | `deleteAList` | Permanently deletes a contact list and every contact it holds. |
| Delete a Webhook | `deleteAWebhook` | Deletes an existing webhook by the campaign it watches and its URL. |
| Delete Account API Key | `deleteAPIKey` | Undocumented endpoint that revokes one of the account API keys, identified by the key value itself. Revoking the key the connection authenticates with breaks every other action. |
| Delete an Email Campaign | `deleteAnEmailCampaign` | Undocumented endpoint that permanently deletes a legacy email campaign. This is the only way to remove a campaign created with Create an Email Campaign. |
| Delete Contact from a LinkedIn Campaign | `deleteContactFromALinkedInCampaign` | Removes a contact from a legacy LinkedIn campaign, identified by their LinkedIn profile URL. |
| Delete Contact from an Email Campaign | `deleteContactFromAnEmailCampaign` | Removes a contact from a legacy email campaign, identified by their email address. |
| Delete Custom Tracking Domain | `deleteCustomDomain` | Undocumented endpoint that removes a custom link-tracking domain from the account. Its not-found body refers to an Email Provider, which is a vendor-side message bug, not a wrong route. |
| Delete Email Provider | `deleteEmailProvider` | Undocumented endpoint that disconnects a sending email provider from the account. It answers 200 success even for an id that does not exist, so confirm the removal with List Email Providers. |
| Delete Tag | `deleteTag` | Undocumented endpoint that permanently deletes a tag and removes it from every campaign and list carrying it. |
| Disable Warmup for an Email Provider | `disableWarmupForAnEmailProvider` | Turns the deliverability warmup off for one connected email provider. |
| Download Scrapper Data | `downloadScrapperData` | Downloads the profiles collected by a LinkedIn scrapper, filtered by whether an email was found. |
| Duplicate a Campaign | `duplicateACampaign` | Creates a new draft multichannel campaign from an existing one, copying only the parts you select. The new name must be free on the account. |
| Enable Warmup for an Email Provider | `enableWarmupForAnEmailProvider` | Turns the deliverability warmup on for one connected email provider. |
| Export Lists | `exportLists` | Exports one contact list as a CSV file, or several lists as a ZIP archive holding one CSV per list. The response body is the raw file content, not JSON: a single-list export returns CSV text. |
| Find Email of a Single Contact | `findEmailOfASingleContact` | Submits an Email Finder job for one person at one company and returns a job id. Poll Get the Result of a Find Email Job for the outcome. Consumes Email Finder credits. |
| Find Phone Number of a Single Contact | `findPhoneNumberOfASingleContact` | Submits a Phone Finder job for one LinkedIn profile and returns a job id. Poll Get the Result of a Find Phone Job for the outcome. Consumes Phone Finder credits. |
| Get a Contact | `getAContact` | Returns a single contact of a list with all of its fields and custom variables. |
| Get Account API Keys | `getAPIKeys` | SECURITY WARNING: this undocumented endpoint returns the Emelia account own API keys in cleartext, so every caller of this action receives a live credential. Use it only for key-rotation audits, never in a flow whose output is logged or shared. |
| Get API Service Health | `getServiceHealth` | Undocumented health probe that returns the Emelia API status and its database connectivity. It answers without authentication, so it is safe to poll for availability. |
| Get Email Campaign Activities | `getEmailCampaignActivities` | Returns the paginated activity feed of a legacy email campaign, optionally filtered by contact, version, activity type or a free-text query. |
| Get Email Campaign Details | `getEmailCampaignDetails` | Returns the full configuration of a legacy email campaign, including its steps, schedule and recipients. |
| Get Email Campaign Statistics | `getEmailCampaignStatistics` | Returns the global and per-step statistics of a legacy email campaign over an optional date range, optionally filtered by sending provider. |
| Get LinkedIn Campaign Activities | `getLinkedInCampaignActivities` | Returns the paginated activity feed of a legacy LinkedIn campaign, optionally filtered by contact, version, activity type or a free-text query. |
| Get LinkedIn Campaign Statistics | `getLinkedInCampaignStatistics` | Returns the global and per-step statistics of a legacy LinkedIn campaign over an optional date range, optionally filtered by LinkedIn account. |
| Get List Details | `getListDetails` | Returns one contact list with its name, source, status and contact, email, phone and LinkedIn counters. |
| Get Multichannel Campaign Activities | `getCampaignActivities` | Returns the paginated activity feed of a multichannel campaign, optionally filtered by contact, sequence version, activity type or a free-text query. |
| Get Multichannel Campaign Details | `getCampaignDetails` | Returns the full configuration of a multichannel campaign, including its steps, identities, settings, attached contact lists and excluded lists. |
| Get Multichannel Campaign Statistics | `getCampaignStatistics` | Returns the global and per-step statistics of a multichannel campaign over an optional date range. |
| Get Pending Manual Tasks for a Campaign | `getPendingManualTasksForACampaign` | Returns the manual tasks of a multichannel campaign that are still pending, optionally limited to one sequence step. |
| Get the Result of a Find Email Job | `getTheResultOfAFindEmailJob` | Returns the status and result of an Email Finder job previously submitted with Find Email of a Single Contact. |
| Get the Result of a Find Phone Job | `getTheResultOfAFindPhoneJob` | Returns the status and result of a Phone Finder job previously submitted with Find Phone Number of a Single Contact. |
| Get the Result of a Verify Email Job | `getTheResultOfAVerifyEmailJob` | Returns the status and verdict of an Email Verifier job previously submitted with Verify Email of a Single Contact. |
| List All LinkedIn Authentications | `listAllAuthesAuthenticationConfigurations` | Returns every LinkedIn authentication configuration registered on the account, for use by scrappers and LinkedIn campaigns. |
| List All LinkedIn Scrappers | `listAllLinkedInScrappers` | Returns the LinkedIn scrappers of the account with their status and progress, one page at a time. |
| List All Lists | `listAllLists` | Returns the contact lists of the account. Without Page and Limit it returns a plain array; with pagination parameters it returns a paginated envelope with totals. |
| List Blacklisted Contacts | `listBlacklistedContacts` | Undocumented endpoint that returns every email address and domain on the account blacklist. |
| List Contacts of a List | `listContactsOfAList` | Paginated listing of the contacts of a list. To check whether one specific contact exists before updating or deleting it, use the Email or LinkedIn URL lookup instead: it returns the exact match only. |
| List Custom Tracking Domains | `listCustomDomains` | Undocumented endpoint that returns the custom link-tracking domains configured on the account. |
| List Email Campaign Contacts | `listEmailCampaignContacts` | Returns the contacts of a legacy email campaign one page at a time, optionally filtered by the events they triggered or a free-text query. |
| List Email Campaigns | `listEmailCampaigns` | Returns every legacy email-only campaign of the account with its id, name and status. |
| List Email Finder Jobs | `listFindEmailJobs` | Undocumented endpoint that returns a paginated history of every Email Finder job submitted on the account. |
| List Email Providers | `listEmailProviders` | Returns every sending email provider connected to the account, with credentials masked. Filter to disconnected to find providers that need reconnecting. |
| List Email Verifier Jobs | `listVerifyEmailJobs` | Undocumented endpoint that returns a paginated history of every Email Verifier job submitted on the account. |
| List Legacy Campaigns | `listLegacyCampaigns` | Undocumented endpoint that returns a paginated list of the legacy campaigns of the account across all channels, with a total count. |
| List LinkedIn Authentications (Alias Route) | `listLinkedinAuthesAlias` | Undocumented alias of List All LinkedIn Authentications, served under the LinkedIn campaign prefix. Returns the same authentication configurations. |
| List LinkedIn Campaign Contacts | `listLinkedInCampaignContacts` | Returns the contacts of a legacy LinkedIn campaign one page at a time, optionally filtered by the events they triggered or a free-text query. |
| List LinkedIn Campaigns | `listLinkedInCampaigns` | Returns every legacy LinkedIn-only campaign of the account with its id, name and status. |
| List Multichannel Campaigns | `listCampaigns` | Returns every non-archived multichannel campaign of the account with its id, name and status. |
| List Phone Finder Jobs | `listFindPhoneJobs` | Undocumented endpoint that returns a paginated history of every Phone Finder job submitted on the account. |
| List Tags | `listTags` | Undocumented endpoint that returns every tag defined on the account, used to label campaigns and contact lists. |
| List User Webhooks | `listUserWebhooks` | Returns every webhook registered on the account, with the campaign it watches, its URL and the events it listens for. |
| List Warmups for All Providers | `listWarmupsForAllProviders` | Returns the deliverability warmup status of every email provider on the account, ten results per page. |
| Pause a Campaign | `pauseACampaign` | Pauses a running multichannel campaign and cancels every action already scheduled. Pausing is required before renaming a campaign or changing its settings, identities or steps. |
| Pause a LinkedIn Scrapper | `pauseALinkedInScrapper` | Pauses a running LinkedIn scrapper. Resume it later with Resume a LinkedIn Scrapper. |
| Pause an Email Campaign | `pauseAnEmailCampaign` | Pauses a running legacy email campaign and cancels the emails already scheduled. |
| Remove a Webhook from a Scrapper | `removeAWebhookFromAScrapper` | Detaches a webhook URL from a LinkedIn scrapper so it stops receiving that scrapper events. |
| Remove Contact from Blacklist | `removeContactFromBlacklist` | Removes an email address or a whole domain from the account blacklist so campaigns can contact it again. |
| Rename a Campaign | `renameACampaign` | Changes the name of a multichannel campaign. The campaign must not be RUNNING: pause it first. |
| Rename a LinkedIn Scrapper | `renameALinkedInScrapper` | Changes the display name of a LinkedIn scrapper. |
| Rename a List | `renameAList` | Changes the name of a contact list. |
| Reply to an Emelia Reply | `replyToAnEmeliaReply` | Sends a real reply email into an existing Emelia conversation thread from one of your connected providers. This delivers a message to a real recipient inbox, so use it only against addresses you control. |
| Resume a LinkedIn Scrapper | `resumeALinkedInScrapper` | Resumes a paused LinkedIn scrapper so it continues collecting profiles. |
| Schedule a Campaign Start | `scheduleACampaignStart` | Plans the automatic start of a multichannel campaign at a future date, or cancels a plan already registered. The campaign must already pass every Start a Campaign check. |
| Send a Test Email | `sendATestEmail` | Sends one step of a campaign as a test email to an address you choose. This delivers a real email, so use it only against a mailbox you control. |
| Set a Manual Task Status | `setAManualTaskStatus` | Marks a pending manual task of a multichannel campaign as completed or failed for one contact. |
| Set Custom Field to a LinkedIn Contact | `setCustomFieldToALinkedInContact` | Sets one custom variable on a contact of a legacy LinkedIn campaign, identified by their LinkedIn profile URL. |
| Set Custom Field to a Multichannel Contact | `setCustomFieldToAContact` | Sets one custom variable on a contact of a multichannel campaign, identified by email or LinkedIn profile URL. |
| Set Custom Field to an Email Contact | `setCustomFieldToAnEmailContact` | Sets one custom variable on a contact of a legacy email campaign, identified by their email address. |
| Split a LinkedIn Scrapper | `splitALinkedInScrapper` | Splits a LinkedIn scrapper into several smaller scrapping jobs so they run across the attached authentications. |
| Start a Campaign | `startACampaign` | Starts a multichannel campaign and schedules its first actions, which sends real messages to its recipients. The campaign needs at least one identity, at least one recipient (15,000 maximum), a valid sequence and connected identity accounts. |
| Start an Email Campaign | `startAnEmailCampaign` | Starts a legacy email campaign, which begins delivering real emails to its recipients. |
| Start Enrichment for a Scrapper | `startEnrichmentForAScrapper` | Starts email enrichment on the profiles collected by a LinkedIn scrapper. Consumes enrichment credits. |
| Test a Webhook | `testAWebhook` | Sends a sample event payload to an existing webhook so you can confirm your endpoint receives and parses it. |
| Update a Contact | `updateAContact` | Updates a contact from a flat JSON object: one key per field. Only the contact id is needed, the list is derived from it. Unrecognised keys create new custom variables. |
| Update Campaign Contact Lists | `updateCampaignContactLists` | Replaces the whole contact-list selection of a multichannel campaign. Send every list id you want attached, not only the new ones, plus any lists to exclude. |
| Update Campaign Identities | `updateCampaignIdentities` | Replaces the identities of a multichannel campaign. An identity is a sender: a name plus the email provider and/or LinkedIn account it sends from. Each identity needs a name and at least one account. |
| Update Campaign Providers Settings | `updateCampaignProvidersSettings` | Chooses which email providers a legacy email campaign sends through, either a single provider or a rotation across several. |
| Update Campaign Settings | `updateCampaignSettings` | Updates the general settings of a multichannel campaign: daily cadence, sending window, tracking, and the events that stop the sequence for a contact. The settings you send are merged into the current ones. |
| Update Email Campaign Global Settings | `updateEmailCampaignGlobalSettings` | Replaces the schedule and sending settings of a legacy email campaign: daily volume, intervals, sending window, tracking and stop events. |
| Update Email Campaign Name | `updateEmailCampaignName` | Changes the name of a legacy email campaign. |
| Update Email Campaign Steps | `updateEmailCampaignSteps` | Replaces the full sequence of a legacy email campaign. Send every step you want kept, not only the new ones. Each version requires an options.schedule array: one entry per sending day with day, start and end. |
| Update Email Provider | `updateEmailProvider` | Undocumented endpoint that updates the settings of a connected sending email provider, such as its sender name, signature or SMTP and IMAP details. |
| Update LinkedIn Campaign Global Settings | `updateLinkedInCampaignGlobalSettings` | Replaces the schedule and targeting settings of a legacy LinkedIn campaign: daily contacts, sending window and profile exclusions. |
| Update LinkedIn Campaign Name | `updateLinkedInCampaignName` | Changes the name of a legacy LinkedIn campaign. |
| Update LinkedIn Campaign Steps | `updateLinkedInCampaignSteps` | Replaces the full sequence of a legacy LinkedIn campaign. Send every step you want kept, not only the new ones. |
| Update Tag | `updateTag` | Undocumented endpoint that renames or recolours an existing tag. |
| Verify Email of a Single Contact | `verifyEmailOfASingleContact` | Submits an Email Verifier job for one address and returns a job id. Poll Get the Result of a Verify Email Job for the verdict. Consumes verification credits. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Contact Unsubscribed | `UNSUBSCRIBED` | A contact unsubscribed from the campaign. |
| Email Bounced | `BOUNCED` | An email to a contact bounced. |
| Email Opened | `OPENED` | A contact opened a tracked email. |
| Email Replied | `MAIL_REPLIED` | A contact replied to an email of a multichannel campaign. |
| Email Sent | `MAIL_SENT` | An email step was sent to a contact of a multichannel campaign. |
| Link Clicked | `CLICKED` | A contact clicked a tracked link in an email. |
| LinkedIn Invitation Accepted | `ACCEPTED` | A contact accepted the LinkedIn connection invitation. |
| LinkedIn Invitation Sent | `INVITED` | A LinkedIn connection invitation was sent to a contact. LinkedIn-only campaigns (campaignType linkedin). |
| LinkedIn Message Sent | `MESSAGE_SENT` | A LinkedIn message step was sent to a contact. |
| LinkedIn Post Liked | `LIKED` | The campaign liked a contact LinkedIn post. |

<details>

<summary>See 4 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| LinkedIn Profile Visited | `VISITED` | The campaign visited a contact LinkedIn profile. |
| LinkedIn Replied | `LINKEDIN_REPLIED` | A contact replied to a LinkedIn message of a multichannel campaign. |
| Replied (Legacy Campaigns) | `REPLIED` | A contact replied. Emitted by legacy email campaigns (campaignType email) and legacy LinkedIn campaigns (campaignType linkedin). |
| Sent (Legacy Email Campaigns) | `SENT` | An email was sent. Emitted by legacy email campaigns (campaignType email). |

</details>
