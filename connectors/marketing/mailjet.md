---
description: "Send transactional and marketing email and SMS with Mailjet."
hidden: true
---

# Mailjet

Send transactional and marketing email and SMS with Mailjet. Covers the Send API v3.1, contacts and contact lists, campaigns and drafts, templates, segmentation, statistics, sender and domain validation, event webhooks, and account settings.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [mailjet.com](https://mailjet.com) |
| **Authentication** | Basic auth |
| **Actions** | 244 |
| **Events** | 0 |
| **Slug** | `mailjet` |

## Use it

Add Mailjet from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mailjet.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate User | `activateUser` | Activate a Mailjet user account. |
| Archive Workflow | `archiveWorkflow` | Archive a workflow so it no longer appears in the active list. |
| Cancel Campaign Draft Schedule | `deleteCampaignDraftSchedule` | Cancel the scheduled send of a campaign draft. |
| Cancel Newsletter Schedule | `deleteNewsletterSchedule` | Cancel the scheduled send of a newsletter. |
| Check Sender Domain DNS | `checkSenderDomainDns` | Trigger a DNS check to validate the SPF and DKIM records of a sender domain. |
| Check Workflow | `checkWorkflow` | Validate a workflow's configuration and report any errors preventing it from running. |
| Count SMS Messages | `countSms` | Return the number of SMS messages matching the given filters, without returning the messages themselves. |
| Create A/X Test | `createAXTest` | Create a new a/x test in your Mailjet account. |
| Create API Key | `createAPIKey` | Create a new api key in your Mailjet account. |
| Create API Token | `createAPIToken` | Create a new api token in your Mailjet account. |
| Create Batch Job | `createBatchJob` | Create a new batch job in your Mailjet account. |
| Create Campaign Aggregate | `createCampaignAggregate` | Create a new campaign aggregate in your Mailjet account. |
| Create Campaign Draft | `createCampaignDraft` | Create a new campaign draft in your Mailjet account. |
| Create Contact | `createContact` | Create a new contact in your Mailjet account. |
| Create Contact Data | `createContactData` | Create a new contact data in your Mailjet account. |
| Create Contact Export | `createExportContact` | Start an asynchronous export of all contacts on this API key. Returns a job ID; poll it with List Contact Exports to obtain the download URL once the job completes. |
| Create Contact Filter | `createContactFilter` | Create a new contact filter in your Mailjet account. |
| Create Contact History Data | `createContactHistoryData` | Create a new contact history data in your Mailjet account. |
| Create Contact List | `createContactList` | Create a new contact list in your Mailjet account. |
| Create Contact Property | `createContactProperty` | Create a new contact property in your Mailjet account. |
| Create CSV Import | `createCSVImport` | Create a new csv import in your Mailjet account. |
| Create Event Webhook | `createEventWebhook` | Create a new event webhook in your Mailjet account. |
| Create List Recipient | `createListRecipient` | Create a new list recipient in your Mailjet account. |
| Create Meta Sender | `createMetaSender` | Create a new meta sender in your Mailjet account. |
| Create Newsletter | `createNewsletter` | Create a new newsletter in your Mailjet account. |
| Create Newsletter Template | `createNewsletterTemplate` | Create a new newsletter template in your Mailjet account. |
| Create Parse Route | `createParseRoute` | Create a new parse route in your Mailjet account. |
| Create Preset | `createPreset` | Create a new preset in your Mailjet account. |
| Create Sender | `createSender` | Create a new sender in your Mailjet account. |
| Create Template | `createTemplate` | Create a new template in your Mailjet account. |
| Create Widget | `createWidget` | Create a new widget in your Mailjet account. |
| Create Widget Custom Value | `createWidgetCustomValue` | Create a new widget custom value in your Mailjet account. |
| Create Workflow | `createWorkflow` | Create a new workflow in your Mailjet account. |
| Delete A/X Test | `deleteAXTest` | Permanently delete a a/x test by its unique Mailjet ID. |
| Delete API Token | `deleteAPIToken` | Permanently delete a api token by its unique Mailjet ID. |
| Delete Campaign Aggregate | `deleteCampaignAggregate` | Permanently delete a campaign aggregate by its unique Mailjet ID. |
| Delete Contact | `deleteContact` | Permanently delete a contact from this API key's contact database, for GDPR compliance. Contact details are anonymized immediately and all records are removed after 30 days. This cannot be reversed. |
| Delete Contact Data | `deleteContactData` | Permanently delete a contact data by its unique Mailjet ID. |
| Delete Contact Filter | `deleteContactFilter` | Permanently delete a contact filter by its unique Mailjet ID. |
| Delete Contact History Data | `deleteContactHistoryData` | Permanently delete a contact history data by its unique Mailjet ID. |
| Delete Contact List | `deleteContactList` | Permanently delete a contact list by its unique Mailjet ID. |
| Delete Contact Property | `deleteContactProperty` | Permanently delete a contact property by its unique Mailjet ID. |
| Delete Event Webhook | `deleteEventWebhook` | Permanently delete a event webhook by its unique Mailjet ID. |
| Delete List Recipient | `deleteListRecipient` | Permanently delete a list recipient by its unique Mailjet ID. |
| Delete Newsletter Content | `deleteNewsletterContent` | Remove the HTML and text content of a newsletter. |
| Delete Parse Route | `deleteParseRoute` | Permanently delete a parse route by its unique Mailjet ID. |
| Delete Preset | `deletePreset` | Permanently delete a preset by its unique Mailjet ID. |
| Delete Sender | `deleteSender` | Permanently delete a sender by its unique Mailjet ID. |
| Delete Template | `deleteTemplate` | Permanently delete a template by its unique Mailjet ID. |
| Delete Template Preview | `deleteTemplatePreview` | Remove the preview image attached to a template. |
| Delete Template Thumbnail | `deleteTemplateThumbnail` | Remove the thumbnail image attached to a template. |
| Delete Widget | `deleteWidget` | Permanently delete a widget by its unique Mailjet ID. |
| Delete Widget Custom Value | `deleteWidgetCustomValue` | Permanently delete a widget custom value by its unique Mailjet ID. |
| Delete Workflow | `deleteWorkflow` | Permanently delete a workflow by its unique Mailjet ID. |
| Display Template Preview | `displayTemplatePreview` | Retrieve the preview image of a template. |
| Display Template Thumbnail | `displayTemplateThumbnail` | Retrieve the thumbnail image of a template. |
| Export SMS Messages | `exportSms` | Start an asynchronous export of your SMS messages. Returns a job whose status you can poll to obtain the download URL. |
| Get A/X Test | `getAXTest` | Retrieve a single a/x test by its unique Mailjet ID. |
| Get API Key | `getAPIKey` | Retrieve a single api key by its unique Mailjet ID. |
| Get API Key Access | `getAPIKeyAccess` | Retrieve a single api key access by its unique Mailjet ID. |
| Get API Token | `getAPIToken` | Retrieve a single api token by its unique Mailjet ID. |
| Get App Preference | `getAppPreference` | Retrieve a single app preference by its unique Mailjet ID. |
| Get Batch Job | `getBatchJob` | Retrieve a single batch job by its unique Mailjet ID. |
| Get Bounce Statistic | `getBounceStatistic` | Retrieve a single bounce statistic by its unique Mailjet ID. |
| Get Campaign | `getCampaign` | Retrieve a single campaign by its unique Mailjet ID. |
| Get Campaign Aggregate | `getCampaignAggregate` | Retrieve a single campaign aggregate by its unique Mailjet ID. |
| Get Campaign Draft | `getCampaignDraft` | Retrieve a single campaign draft by its unique Mailjet ID. |
| Get Campaign Draft Content | `getCampaignDraftContent` | Retrieve the HTML, text and MJML content of a campaign draft. |
| Get Campaign Draft Schedule | `getCampaignDraftSchedule` | Retrieve the delivery schedule of a campaign draft. |
| Get Campaign Draft Status | `getCampaignDraftStatus` | Retrieve the current sending status of a campaign draft. |
| Get Campaign Graph Statistic | `getCampaignGraphStatistic` | Retrieve a single campaign graph statistic by its unique Mailjet ID. |
| Get Campaign Overview | `getCampaignOverview` | Retrieve a single campaign overview by its ID. The IDType returned by List Campaign Overviews must be supplied alongside the ID. |
| Get Click Statistic | `getClickStatistic` | Retrieve a single click statistic by its unique Mailjet ID. |
| Get Contact | `getContact` | Retrieve a single contact by its unique Mailjet ID. |
| Get Contact Activity | `getContactActivity` | Retrieve a single contact activity by its unique Mailjet ID. |
| Get Contact Data | `getContactData` | Retrieve a single contact data by its unique Mailjet ID. |
| Get Contact Export | `listExportContact` | Retrieve the status of a contact export job and, once it has completed, the URL to download the exported data. |
| Get Contact Filter | `getContactFilter` | Retrieve a single contact filter by its unique Mailjet ID. |
| Get Contact History Data | `getContactHistoryData` | Retrieve a single contact history data by its unique Mailjet ID. |
| Get Contact List | `getContactList` | Retrieve a single contact list by its unique Mailjet ID. |
| Get Contact List Import Job | `getContactListImportJob` | Retrieve the status and result of a contact-import job for a specific contact list. |
| Get Contact List Signup | `getContactListSignup` | Retrieve a single contact list signup by its unique Mailjet ID. |
| Get Contact List Verification | `getContactListVerification` | Retrieve the status and results of a contact list email-verification job. |
| Get Contact Property | `getContactProperty` | Retrieve a single contact property by its unique Mailjet ID. |
| Get Contact Subscriptions | `getContactLists` | Retrieve every contact list a given contact belongs to, with its subscription status. |
| Get CSV Import | `getCSVImport` | Retrieve a single csv import by its unique Mailjet ID. |
| Get Domain Statistic | `getDomainStatistic` | Retrieve a single domain statistic by its unique Mailjet ID. |
| Get Event Webhook | `getEventWebhook` | Retrieve a single event webhook by its unique Mailjet ID. |
| Get List Recipient | `getListRecipient` | Retrieve a single list recipient by its unique Mailjet ID. |
| Get List Statistic | `getListStatistic` | Retrieve a single list statistic by its unique Mailjet ID. |
| Get Manage Many Contacts In List Job | `getManageManyContactsInListJob` | Retrieve the status and result of an asynchronous bulk contact job for a specific contact list. |
| Get Manage Many Contacts Job | `getManageManyContactsJob` | Retrieve the status and result of an asynchronous bulk contact-management job. |
| Get Message | `getMessage` | Retrieve a single message by its unique Mailjet ID. |
| Get Message Information | `getMessageInformation` | Retrieve a single message information by its unique Mailjet ID. |
| Get Message State | `getMessageState` | Retrieve a single message state by its unique Mailjet ID. |
| Get Meta Sender | `getMetaSender` | Retrieve a single meta sender by its unique Mailjet ID. |
| Get Newsletter | `getNewsletter` | Retrieve a single newsletter by its unique Mailjet ID. |
| Get Newsletter Content | `getNewsletterContent` | Retrieve the HTML and text content of a newsletter. |
| Get Newsletter Schedule | `getNewsletterSchedule` | Retrieve the delivery schedule of a newsletter. |
| Get Newsletter Status | `getNewsletterStatus` | Retrieve the current sending status of a newsletter. |
| Get Newsletter Template | `getNewsletterTemplate` | Retrieve a single newsletter template by its unique Mailjet ID. |
| Get Newsletter Template Category | `getNewsletterTemplateCategory` | Retrieve a single newsletter template category by its unique Mailjet ID. |
| Get Open Information | `getOpenInformation` | Retrieve a single open information by its unique Mailjet ID. |
| Get Parse Route | `getParseRoute` | Retrieve a single parse route by its unique Mailjet ID. |
| Get Preference | `getPreference` | Retrieve a single preference by its unique Mailjet ID. |
| Get Preset | `getPreset` | Retrieve a single preset by its unique Mailjet ID. |
| Get Profile | `getProfile` | Retrieve a single profile by its unique Mailjet ID. |
| Get Sender | `getSender` | Retrieve a single sender by its unique Mailjet ID. |
| Get Sender Domain | `getSenderDomain` | Retrieve a single sender domain by its unique Mailjet ID. |
| Get SMS Message | `getSms` | Retrieve a single SMS message by its unique Mailjet message ID. |
| Get Template | `getTemplate` | Retrieve a single template by its unique Mailjet ID. |
| Get Template Content | `getTemplateContent` | Retrieve the HTML, text and MJML content of a template. |
| Get User | `getUser` | Retrieve a single user by its unique Mailjet ID. |
| Get User Agent | `getUserAgent` | Retrieve a single user agent by its unique Mailjet ID. |
| Get Widget | `getWidget` | Retrieve a single widget by its unique Mailjet ID. |
| Get Widget Custom Value | `getWidgetCustomValue` | Retrieve a single widget custom value by its unique Mailjet ID. |
| Get Workflow | `getWorkflow` | Retrieve a single workflow by its unique Mailjet ID. |
| Get Workflow Log | `getWorkflowLog` | Retrieve the execution log of a workflow. |
| Import Contacts Into List | `importContactsIntoList` | Copy all contacts from another contact list into this list. |
| List A/X Tests | `listAXTest` | Retrieve a list of a/x tests from your Mailjet account, with optional filtering, sorting and pagination. |
| List Activity Counters | `listActivityCounter` | Retrieve activity counters. Requires the CounterType filter (for example Message, Campaign or List) together with FromTS and ToTS. The FromTS-to-ToTS window must be narrow enough for the chosen timing resolution, otherwise the API returns 'timestamps are too wide apart'. |
| List API Key Access Entries | `listAPIKeyAccess` | Retrieve a list of api key access entries from your Mailjet account, with optional filtering, sorting and pagination. |
| List API Key Access Grantors | `listAPIKeyAccessGrantor` | List the users who have granted access to this API key. Requires the RealUser or SubAccount filter, and privileged (master-account) access on the Mailjet account. |
| List API Key Totals | `listAPIKeyTotal` | Retrieve a list of api key totals from your Mailjet account, with optional filtering, sorting and pagination. |
| List API Keys | `listAPIKey` | Retrieve a list of api keys from your Mailjet account, with optional filtering, sorting and pagination. |
| List API Metadata | `listAPIMetadataEntry` | Retrieve a list of api metadata from your Mailjet account, with optional filtering, sorting and pagination. |
| List API Tokens | `listAPIToken` | Retrieve a list of api tokens from your Mailjet account, with optional filtering, sorting and pagination. |
| List App Preferences | `listAppPreference` | Retrieve a list of app preferences from your Mailjet account, with optional filtering, sorting and pagination. |
| List Batch Jobs | `listBatchJob` | Retrieve a list of batch jobs from your Mailjet account, with optional filtering, sorting and pagination. |
| List Bounce Statistics | `listBounceStatistic` | Retrieve a list of bounce statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List Campaign Aggregates | `listCampaignAggregate` | Retrieve a list of campaign aggregates from your Mailjet account, with optional filtering, sorting and pagination. |
| List Campaign Drafts | `listCampaignDraft` | Retrieve a list of campaign drafts from your Mailjet account, with optional filtering, sorting and pagination. |
| List Campaign Graph Statistics | `listCampaignGraphStatistic` | Retrieve campaign graph statistics. Requires the IDS filter with one or more campaign IDs, plus at least one of the Open, Click, Unsub or Spam filters. |
| List Campaign Overviews | `listCampaignOverview` | Retrieve a list of campaign overviews from your Mailjet account, with optional filtering, sorting and pagination. |
| List Campaign Statistics | `listCampaignStatistic` | Retrieve a list of campaign statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List Campaigns | `listCampaign` | Retrieve a list of campaigns from your Mailjet account, with optional filtering, sorting and pagination. |
| List Click Statistics | `listClickStatistic` | Retrieve a list of click statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List Contact Activities | `listContactActivity` | Retrieve a list of contact activities from your Mailjet account, with optional filtering, sorting and pagination. |
| List Contact Activity Geo Statistics | `listContactActivityGeoStats` | Retrieve contact activity statistics aggregated by geographic location. |
| List Contact Data Entries | `listContactData` | Retrieve a list of contact data entries from your Mailjet account, with optional filtering, sorting and pagination. |
| List Contact Filters | `listContactFilter` | Retrieve a list of contact filters from your Mailjet account, with optional filtering, sorting and pagination. |
| List Contact History Data Entries | `listContactHistoryData` | Retrieve a list of contact history data entries from your Mailjet account, with optional filtering, sorting and pagination. |
| List Contact List Signups | `listContactListSignup` | Retrieve a list of contact list signups from your Mailjet account, with optional filtering, sorting and pagination. |
| List Contact Lists | `listContactList` | Retrieve a list of contact lists from your Mailjet account, with optional filtering, sorting and pagination. |
| List Contact Properties | `listContactProperty` | Retrieve a list of contact properties from your Mailjet account, with optional filtering, sorting and pagination. |
| List Contact Statistics | `listContactStatistic` | Retrieve a list of contact statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List Contacts | `listContact` | Retrieve a list of contacts from your Mailjet account, with optional filtering, sorting and pagination. |
| List CSV Imports | `listCSVImport` | Retrieve a list of csv imports from your Mailjet account, with optional filtering, sorting and pagination. |
| List Domain Statistics | `listDomainStatistic` | Retrieve a list of domain statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List Event Webhooks | `listEventWebhook` | Retrieve a list of event webhooks from your Mailjet account, with optional filtering, sorting and pagination. |
| List Geo Statistics | `listGeoStatistic` | Retrieve a list of geo statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List Graph Statistics | `listGraphStatistic` | Retrieve a list of graph statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List List Recipient Statistics | `listListRecipientStatistic` | Retrieve a list of list recipient statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List List Recipients | `listListRecipient` | Retrieve a list of list recipients from your Mailjet account, with optional filtering, sorting and pagination. |
| List List Statistics | `listListStatistic` | Retrieve a list of list statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List Message History | `listMessageHistoryEntry` | Retrieve a list of message history from your Mailjet account, with optional filtering, sorting and pagination. |
| List Message Information Entries | `listMessageInformation` | Retrieve a list of message information entries from your Mailjet account, with optional filtering, sorting and pagination. |
| List Message States | `listMessageState` | Retrieve a list of message states from your Mailjet account, with optional filtering, sorting and pagination. |
| List Message Statistics | `listMessageStatistic` | Retrieve a list of message statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List Messages | `listMessage` | Retrieve a list of messages from your Mailjet account, with optional filtering, sorting and pagination. |
| List Meta Senders | `listMetaSender` | Retrieve a list of meta senders from your Mailjet account, with optional filtering, sorting and pagination. |
| List Newsletter Template Categories | `listNewsletterTemplateCategory` | Retrieve a list of newsletter template categories from your Mailjet account, with optional filtering, sorting and pagination. |
| List Newsletter Templates | `listNewsletterTemplate` | Retrieve a list of newsletter templates from your Mailjet account, with optional filtering, sorting and pagination. |
| List Newsletters | `listNewsletter` | Retrieve a list of newsletters from your Mailjet account, with optional filtering, sorting and pagination. |
| List Open Information Entries | `listOpenInformation` | Retrieve a list of open information entries from your Mailjet account, with optional filtering, sorting and pagination. |
| List Open Statistics | `listOpenStatistic` | Retrieve a list of open statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List Parse Routes | `listParseRoute` | Retrieve a list of parse routes from your Mailjet account, with optional filtering, sorting and pagination. |
| List Preferences | `listPreference` | Retrieve a list of preferences from your Mailjet account, with optional filtering, sorting and pagination. |
| List Presets | `listPreset` | Retrieve a list of presets from your Mailjet account, with optional filtering, sorting and pagination. |
| List Profiles | `listProfile` | Retrieve a list of profiles from your Mailjet account, with optional filtering, sorting and pagination. |
| List Return Paths | `listReturnPath` | Retrieve a list of return paths from your Mailjet account, with optional filtering, sorting and pagination. |
| List Sender Domains | `listSenderDomain` | Retrieve a list of sender domains from your Mailjet account, with optional filtering, sorting and pagination. |
| List Sender Statistics | `listSenderStatistic` | Retrieve a list of sender statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List Senders | `listSender` | Retrieve a list of senders from your Mailjet account, with optional filtering, sorting and pagination. |
| List SMS Messages | `listSms` | Retrieve the SMS messages sent from your Mailjet account, with optional date, recipient and status filtering. |
| List Stat Counters | `listStatCounter` | Retrieve statistics counters. Requires either the CounterType filter, or all three of CounterSource, CounterResolution and CounterTiming (for example CounterSource=APIKey, CounterResolution=Lifetime, CounterTiming=Message). Sources other than APIKey also require SourceIDs. |
| List Templates | `listTemplate` | Retrieve a list of templates from your Mailjet account, with optional filtering, sorting and pagination. |
| List Top Links Clicked | `listTopLinkClicked` | Retrieve a list of top links clicked from your Mailjet account, with optional filtering, sorting and pagination. |
| List User Activities | `listUserActivity` | Retrieve activity for a Mailjet user. Requires either the uid or the ts filter; this endpoint does not support pagination parameters. |
| List User Agent Statistics | `listUserAgentStatistic` | Retrieve a list of user agent statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List User Agents | `listUserAgent` | Retrieve a list of user agents from your Mailjet account, with optional filtering, sorting and pagination. |
| List Users | `listUser` | Retrieve a list of users from your Mailjet account, with optional filtering, sorting and pagination. |
| List Widget Custom Values | `listWidgetCustomValue` | Retrieve a list of widget custom values from your Mailjet account, with optional filtering, sorting and pagination. |
| List Widgets | `listWidget` | Retrieve a list of widgets from your Mailjet account, with optional filtering, sorting and pagination. |
| List Workflow Contacts | `listWorkflowContacts` | List the contacts currently enrolled in a workflow. |
| List Workflow Statistics | `listWorkflowStatistic` | Retrieve a list of workflow statistics from your Mailjet account, with optional filtering, sorting and pagination. |
| List Workflows | `listWorkflow` | Retrieve a list of workflows from your Mailjet account, with optional filtering, sorting and pagination. |
| Lock Workflow | `lockWorkflow` | Lock a workflow to prevent further edits. |
| Manage Contact In List | `manageContactInList` | Add, remove or unsubscribe a single contact in a specific contact list. |
| Manage Contact Subscriptions | `manageContactLists` | Add, remove or unsubscribe a single contact across one or more contact lists in a single call. |
| Manage Many Contacts | `manageManyContacts` | Bulk-create or update contacts and their list subscriptions asynchronously. Returns a job to poll for completion. |
| Manage Many Contacts In List | `manageManyContactsInList` | Bulk-add, remove or unsubscribe many contacts in a specific contact list asynchronously. |
| Remove Contact From Workflow | `removeContactFromWorkflow` | Remove a contact from a workflow. |
| Restore Workflow | `restoreWorkflow` | Restore a previously archived workflow. |
| Schedule Campaign Draft | `scheduleCampaignDraft` | Schedule a campaign draft to be sent at a specific date and time. |
| Schedule Newsletter | `scheduleNewsletter` | Schedule a newsletter to be sent at a specific date and time. |
| Send Campaign Draft | `sendCampaignDraft` | Send a campaign draft immediately to its full recipient list. |
| Send Campaign Draft Test | `sendCampaignDraftTest` | Send a test copy of a campaign draft to the specified recipients without sending to the real list. |
| Send Email | `sendEmail` | Send one or more transactional emails through the Mailjet Send API v3.1. The sender address of every message must be a verified sender or belong to a verified domain on your Mailjet account. |
| Send Newsletter | `sendNewsletter` | Send a newsletter immediately to its full recipient list. |
| Send Newsletter Test | `sendNewsletterTest` | Send a test copy of a newsletter to the specified recipients without sending to the real list. |
| Send SMS | `sendSms` | Send a single SMS message through the Mailjet SMS API. Requires an SMS-enabled Mailjet account with credit. |
| Set Campaign Draft Content | `setCampaignDraftContent` | Set the HTML, text and MJML content of a campaign draft. |
| Set Newsletter Content | `setNewsletterContent` | Set the HTML and text content of a newsletter. |
| Set Template Content | `setTemplateContent` | Set the HTML, text and MJML content of a template. |
| Set Template Preview | `setTemplatePreview` | Attach a preview image to a template. |
| Set Template Thumbnail | `setTemplateThumbnail` | Attach a thumbnail image to a template. |
| Start Workflow | `startWorkflow` | Start a workflow so it begins processing contacts. |
| Stop Workflow | `stopWorkflow` | Stop a running workflow so it stops processing contacts. The workflow must be in the Started state. |
| Test Event Webhook | `testEventWebhook` | Send a test event payload to the configured event webhook URL to verify it is reachable. |
| Update A/X Test | `updateAXTest` | Update an existing a/x test. Only the properties you supply are changed. |
| Update API Key | `updateAPIKey` | Update an existing api key. Only the properties you supply are changed. |
| Update API Token | `updateAPIToken` | Update an existing api token. Only the properties you supply are changed. |
| Update Batch Job | `updateBatchJob` | Update an existing batch job. Only the properties you supply are changed. |
| Update Campaign | `updateCampaign` | Update an existing campaign. Only the properties you supply are changed. |
| Update Campaign Aggregate | `updateCampaignAggregate` | Update an existing campaign aggregate. Only the properties you supply are changed. |
| Update Campaign Draft | `updateCampaignDraft` | Update an existing campaign draft. Only the properties you supply are changed. |
| Update Campaign Draft Schedule | `updateCampaignDraftSchedule` | Change the scheduled send date and time of a campaign draft. |
| Update Contact | `updateContact` | Update an existing contact. Only the properties you supply are changed. |
| Update Contact Data | `updateContactData` | Update an existing contact data. Only the properties you supply are changed. |
| Update Contact Filter | `updateContactFilter` | Update an existing contact filter. Only the properties you supply are changed. |
| Update Contact List | `updateContactList` | Update an existing contact list. Only the properties you supply are changed. |
| Update Contact Property | `updateContactProperty` | Update an existing contact property. Only the properties you supply are changed. |
| Update CSV Import | `updateCSVImport` | Update an existing csv import. Only the properties you supply are changed. |
| Update Event Webhook | `updateEventWebhook` | Update an existing event webhook. Only the properties you supply are changed. |
| Update List Recipient | `updateListRecipient` | Update an existing list recipient. Only the properties you supply are changed. |
| Update Meta Sender | `updateMetaSender` | Update an existing meta sender. Only the properties you supply are changed. |
| Update Newsletter | `updateNewsletter` | Update an existing newsletter. Only the properties you supply are changed. |
| Update Newsletter Content | `updateNewsletterContent` | Update the HTML and text content of a newsletter. |
| Update Newsletter Schedule | `updateNewsletterSchedule` | Change the scheduled send date and time of a newsletter. |
| Update Newsletter Template | `updateNewsletterTemplate` | Update an existing newsletter template. Only the properties you supply are changed. |
| Update Parse Route | `updateParseRoute` | Update an existing parse route. Only the properties you supply are changed. |
| Update Preset | `updatePreset` | Update an existing preset. Only the properties you supply are changed. |
| Update Profile | `updateProfile` | Update an existing profile. Only the properties you supply are changed. |
| Update Sender | `updateSender` | Update an existing sender. Only the properties you supply are changed. |
| Update Template | `updateTemplate` | Update an existing template. Only the properties you supply are changed. |
| Update Template Preview | `updateTemplatePreview` | Replace the preview image attached to a template. |
| Update Template Thumbnail | `updateTemplateThumbnail` | Replace the thumbnail image attached to a template. |
| Update User | `updateUser` | Update an existing user. Only the properties you supply are changed. |
| Update Widget | `updateWidget` | Update an existing widget. Only the properties you supply are changed. |
| Update Widget Custom Value | `updateWidgetCustomValue` | Update an existing widget custom value. Only the properties you supply are changed. |
| Update Workflow | `updateWorkflow` | Update an existing workflow. Only the properties you supply are changed. |
| Validate Sender | `validateSender` | Trigger validation of a sender email address or domain and return the validation result. |
| Verify Contact List | `verifyContactList` | Start an email-verification job for the contacts in a contact list. |
