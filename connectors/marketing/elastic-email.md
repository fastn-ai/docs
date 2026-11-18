---
description: "Elastic Email is an email delivery and marketing platform."
hidden: true
---

# Elastic Email

Elastic Email is an email delivery and marketing platform. This connector wraps the complete Elastic Email v4 REST API: sending transactional and bulk email, contacts, lists, segments, templates, campaigns, files, inbound routes, domains, email verification, statistics, suppressions, sub-accounts, API key and SMTP credential management, activity events and webhooks.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [elasticemail.com](https://elasticemail.com) |
| **Authentication** | API key |
| **Actions** | 112 |
| **Events** | 0 |
| **Slug** | `elasticEmail` |

## Use it

Add Elastic Email from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.elasticEmail.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Bounce | `addBounce` | Adds an email address to the Elastic Email bounce suppression list so that it is excluded from future sends. The API accepts a JSON array of addresses; this action adds one address per call. Requires the ModifySuppressions access level. |
| Add Complaint | `addComplaint` | Adds an email address to the Elastic Email complaint suppression list so that it is excluded from future sends. The API accepts a JSON array of addresses; this action adds one address per call. Requires the ModifySuppressions access level. |
| Add Contact | `addContact` | Adds a contact to the Elastic Email account and, optionally, to one or more contact lists. The API accepts a JSON array of contacts; this action adds exactly one contact per call. Custom fields and consent data can be set afterwards with Update Contact. Requires the ModifyContacts access level. |
| Add Contacts To List | `addContactsToList` | Adds existing Elastic Email contacts to a named contact list, selected either by an explicit list of email addresses or by a segment rule. Provide either Emails or Rule, not both. Requires the ModifyContacts access level. |
| Add Domain | `addDomain` | Adds a sending domain to the Elastic Email account so that its DNS records can be verified. Requires the ModifySettings access level. |
| Add Unsubscribe | `addUnsubscribe` | Adds an email address to the Elastic Email unsubscribe suppression list so that it is excluded from future sends. The API accepts a JSON array of addresses; this action adds one address per call. Requires the ModifySuppressions access level. |
| Create API Key | `createApiKey` | Creates a new Elastic Email API key with an explicit permission set, optional expiry and optional IP restrictions. The secret token is returned once in this response and cannot be retrieved later. Permissions not included in the account's billing plan are rejected. Requires the Security access level. |
| Create Campaign | `createCampaign` | Adds a new email campaign to Elastic Email for processing. Provide the campaign name, the recipient lists or segments, and one or more content blocks (multiple content blocks create an A/X split campaign). Requires the ModifyCampaigns access level. |
| Create Inbound Route | `createInboundRoute` | Creates an inbound email route in Elastic Email that matches incoming mail on the recipient address or subject and then forwards it to an email address, posts it to an HTTP endpoint, or stops processing. Requires the ModifySettings access level. |
| Create List | `createList` | Creates a new contact list in Elastic Email and optionally seeds it with existing contacts. Leave Emails empty to add every contact in the account. Requires the ModifyContacts access level. |
| Create Segment | `createSegment` | Creates a new contact segment in Elastic Email from a SQL-like rule. Requires the ModifyContacts access level. |
| Create SMTP Credential | `createSmtpCredential` | Creates a new SMTP credential for the Elastic Email account. The name must be a valid email address and the generated password is returned once in this response. Requires the Security access level. |
| Create Sub-Account | `createSubAccount` | Creates a sub-account under the Elastic Email account, optionally sending it an activation email and applying per-account sending limits. Sub-accounts are a reseller feature and are not available on the free plan. Requires the ModifySubAccounts access level. |
| Create Template | `createTemplate` | Creates a new email template in Elastic Email with one or more body parts, for example an HTML part and a plain-text part. Requires the ModifyTemplates access level. |
| Create Webhook | `createWebhook` | Registers a webhook on the Elastic Email account so that delivery events such as sent, opened, clicked, unsubscribed, abuse report and error are posted to your URL. Requires the ModifySettings access level. |
| Delete API Key | `deleteApiKey` | Deletes an Elastic Email API key by name, immediately revoking it. Requires the Security access level. |
| Delete Campaign | `deleteCampaign` | Deletes an Elastic Email campaign by name. Returns an empty body on success. Requires the ModifyCampaigns access level. |
| Delete Contact | `deleteContact` | Deletes a single contact from the Elastic Email account by email address. Requires the ModifyContacts access level. |
| Delete Contacts In Bulk | `deleteContactsBulk` | Deletes many Elastic Email contacts at once, selected either by an explicit list of email addresses or by a segment rule. Provide either Emails or Rule, not both. Requires the ModifyContacts access level. |
| Delete Domain | `deleteDomain` | Removes a sending domain from the Elastic Email account. Requires the ModifySettings access level. |
| Delete Email Verification File | `deleteVerificationFile` | Deletes a bulk email verification file and its results from Elastic Email. Requires the VerifyEmails access level. |
| Delete Email Verification Result | `deleteVerificationResult` | Deletes the stored Elastic Email verification result for a single email address. Requires the VerifyEmails access level. |
| Delete File | `deleteFile` | Deletes a file from the Elastic Email account by file name. Requires the ModifyFiles access level. |
| Delete Inbound Route | `deleteInboundRoute` | Deletes an Elastic Email inbound route by its public id. Requires the ModifySettings access level. |
| Delete List | `deleteList` | Deletes an Elastic Email contact list by name. The contacts themselves are not deleted. Requires the ModifyContacts access level. |
| Delete Segment | `deleteSegment` | Deletes an Elastic Email contact segment by name. The contacts it matched are not deleted. Requires the ModifyContacts access level. |
| Delete SMTP Credential | `deleteSmtpCredential` | Deletes an Elastic Email SMTP credential by name, immediately revoking it. Requires the Security access level. |
| Delete Sub-Account | `deleteSubAccount` | Deletes an Elastic Email sub-account by its email address. Requires the ModifySubAccounts access level. |
| Delete Suppression | `deleteSuppression` | Removes an email address from the Elastic Email suppression list so that it can receive mail again. Requires the ModifySuppressions access level. |
| Delete Template | `deleteTemplate` | Deletes an Elastic Email template by name. Requires the ModifyTemplates access level. |
| Delete Webhook | `deleteWebhook` | Deletes an Elastic Email webhook by its public id, stopping all event notifications to that URL. Requires the ModifySettings access level. |
| Download Email Verification File Result | `downloadVerificationFileResult` | Downloads the completed results of a bulk email verification in Elastic Email as a file. Requires the ViewVerifyEmails access level. |
| Download File | `downloadFile` | Downloads the raw content of a file stored in the Elastic Email account, by file name. The response is the file itself rather than JSON. Requires the ViewFiles access level. |
| Export Channel Events | `exportChannelEvents` | Starts an export of the Elastic Email activity log for a single channel and returns the export id and link. Use Get Channel Events Export Status to poll it. Requires the Export access level. |
| Export Contacts | `exportContacts` | Starts an export of Elastic Email contacts to a downloadable file, selected either by an explicit list of email addresses or by a segment rule. Returns the export id and download link. Use Get Contacts Export Status to poll the export. Requires the Export access level. |
| Export Events | `exportEvents` | Starts an export of the account-wide Elastic Email activity log to a downloadable file and returns the export id and link. Use Get Events Export Status to poll it. Requires the Export access level. |
| Get Account Statistics | `getAccountStatistics` | Returns aggregated sending statistics for the whole Elastic Email account over a date range, including delivered, bounced, opened, clicked, unsubscribed and complaint counts. Requires the ViewReports access level. |
| Get API Key | `getApiKey` | Loads a single Elastic Email API key by name, with its permissions and expiry. The secret token is not returned. Requires the Security access level. |
| Get Campaign | `getCampaign` | Loads a single Elastic Email campaign by its name, including its content blocks, recipient lists and segments, and delivery options. Requires the ViewCampaigns access level. |
| Get Campaign Statistics | `getCampaignStatistics` | Returns delivery and engagement statistics for a single Elastic Email campaign, identified by campaign name. Requires the ViewReports access level. |
| Get Channel Events Export Status | `getChannelEventsExportStatus` | Checks the status of a channel activity-log export previously started with Export Channel Events. Requires the Export access level. |
| Get Channel Statistics | `getChannelStatistics` | Returns delivery and engagement statistics for a single Elastic Email sending channel, identified by channel name. Requires the ViewReports access level. |
| Get Contact | `getContact` | Loads a single contact from Elastic Email by email address, including status, custom fields, consent data and activity counters. Requires the ViewContacts access level. |
| Get Contacts Export Status | `getContactsExportStatus` | Checks the status of a contacts export previously started with Export Contacts. Requires the Export access level. |
| Get Domain | `getDomain` | Loads a single Elastic Email sending domain with its full DNS verification state. Requires the ViewSettings access level. |
| Get Email Status | `getEmailStatus` | Returns the delivery status of an Elastic Email send transaction, with optional per-recipient breakdowns of failed, sent, delivered, pending, opened, clicked, abuse-reported and unsubscribed addresses. Requires the ViewReports access level. |
| Get Email Verification File Result | `getVerificationFileResult` | Returns the per-address results of a bulk email verification file in Elastic Email. Requires the ViewVerifyEmails access level. |
| Get Email Verification Result | `getVerificationResult` | Returns the stored Elastic Email verification result for a single email address that was verified earlier. Requires the ViewVerifyEmails access level. |
| Get Events Export Status | `getEventsExportStatus` | Checks the status of an activity-log export previously started with Export Events. Requires the Export access level. |
| Get File Info | `getFileInfo` | Returns the metadata of a file stored in the Elastic Email account without downloading its content. Requires the ViewFiles access level. |
| Get Inbound Route | `getInboundRoute` | Loads a single Elastic Email inbound route by its public id. Requires the ViewSettings access level. |
| Get List | `getList` | Loads a single Elastic Email contact list by name. Requires the ViewContacts access level. |
| Get Restricted Domain Details | `getRestrictedDomainDetails` | Returns the limited public verification details of a domain, usable when the caller does not own the domain in this Elastic Email account. Requires the ViewSettings access level. |
| Get Segment | `getSegment` | Loads a single Elastic Email contact segment by name, including its rule. Requires the ViewContacts access level. |
| Get SMTP Credential | `getSmtpCredential` | Loads a single Elastic Email SMTP credential by name. The secret password is not returned. Requires the Security access level. |
| Get Sub-Account | `getSubAccount` | Loads a single Elastic Email sub-account by its email address, with credits, reputation and sending settings. Requires the ViewSubAccounts access level. |
| Get Suppression | `getSuppression` | Loads the suppression record for a single email address in Elastic Email, showing why and when it was suppressed. Requires the ViewSuppressions access level. |
| Get Template | `getTemplate` | Loads a single Elastic Email template by name, including all of its body parts. Requires the ViewTemplates access level. |
| Get Webhook | `getWebhook` | Loads a single Elastic Email webhook by its public id, including its URL and event subscriptions. Requires the ViewSettings access level. |
| Import Bounces | `importBounces` | Imports a file of bounced email addresses into the Elastic Email bounce suppression list. Elastic Email accepts this endpoint only as a multipart/form-data file upload, which the fastn HTTP executor cannot produce; use Add Bounce for individual addresses instead. Requires the ModifySuppressions access level. |
| Import Complaints | `importComplaints` | Imports a file of complaint email addresses into the Elastic Email complaint suppression list. Elastic Email accepts this endpoint only as a multipart/form-data file upload, which the fastn HTTP executor cannot produce; use Add Complaint for individual addresses instead. Requires the ModifySuppressions access level. |
| Import Contacts | `importContacts` | Imports contacts into Elastic Email from CSV text sent as a multipart file upload (header row must include an email column), optionally adding them to a named existing list. Requires the ModifyContacts access level. |
| Import Unsubscribes | `importUnsubscribes` | Imports a file of unsubscribed email addresses into the Elastic Email unsubscribe suppression list. Elastic Email accepts this endpoint only as a multipart/form-data file upload, which the fastn HTTP executor cannot produce; use Add Unsubscribe for individual addresses instead. Requires the ModifySuppressions access level. |
| List API Keys | `listApiKeys` | Returns the API keys defined on the Elastic Email account or on one of its sub-accounts, with their permissions, creation date and expiry. The secret token itself is never returned. Requires the Security access level. |
| List Bounces | `listBounces` | Returns the email addresses suppressed in Elastic Email because delivery to them bounced, optionally filtered by a search fragment. Requires the ViewSuppressions access level. |
| List Campaign Statistics | `listCampaignStatistics` | Returns per-campaign delivery and engagement statistics for every campaign in the Elastic Email account. Requires the ViewReports access level. |
| List Campaigns | `listCampaigns` | Returns a list of the email campaigns in your Elastic Email account, optionally filtered by a name fragment and paged. Limited to 1000 results. Requires the ViewCampaigns access level. |
| List Channel Events | `listChannelEvents` | Returns the email activity log for a single Elastic Email channel over a date range. Requires the ViewReports access level. |
| List Channel Statistics | `listChannelStatistics` | Returns per-channel delivery and engagement statistics for every sending channel in the Elastic Email account. Requires the ViewReports access level. |
| List Complaints | `listComplaints` | Returns the email addresses suppressed in Elastic Email because the recipient reported a message as spam, optionally filtered by a search fragment. Requires the ViewSuppressions access level. |
| List Contacts | `listContacts` | Returns a paged list of all contacts in the Elastic Email account, including their status, custom fields, consent data and activity counters. Requires the ViewContacts access level. |
| List Contacts In List | `listContactsInList` | Returns a paged list of the contacts that belong to a named Elastic Email contact list. Requires the ViewContacts access level. |
| List Domains | `listDomains` | Returns every sending domain configured in the Elastic Email account together with its SPF, DKIM, MX, DMARC and link-tracking verification state. Requires the ViewSettings access level. |
| List Email Verification Files | `listVerificationFiles` | Returns the bulk email verification files uploaded to the Elastic Email account, with their processing status and address counts. Requires the ViewVerifyEmails access level. |
| List Email Verification Results | `listVerificationResults` | Returns the results of the single-address email verifications performed on the Elastic Email account. Requires the ViewVerifyEmails access level. |
| List Events | `listEvents` | Returns the account-wide email activity log from Elastic Email over a date range, with one row per submission, delivery, bounce, open, click, unsubscribe or complaint. Requires the ViewReports access level. |
| List Files | `listFiles` | Returns a paged list of the files stored in the Elastic Email account that can be attached to emails and campaigns. Requires the ViewFiles access level. |
| List Inbound Routes | `listInboundRoutes` | Returns all inbound email routes configured in the Elastic Email account, in the order they are evaluated against incoming mail. Requires the ViewSettings access level. |
| List Lists | `listLists` | Returns a paged list of the contact lists in the Elastic Email account. Requires the ViewContacts access level. |
| List Segments | `listSegments` | Returns a paged list of the contact segments in the Elastic Email account, including the rule that defines each segment. Requires the ViewContacts access level. |
| List SMTP Credentials | `listSmtpCredentials` | Returns the SMTP credentials defined on the Elastic Email account or one of its sub-accounts. The secret password is never returned. Requires the Security access level. |
| List Sub-Accounts | `listSubAccounts` | Returns the sub-accounts belonging to the Elastic Email account, with their credit balance, reputation and sending settings. Sub-accounts are a reseller feature and are not available on the free plan. Requires the ViewSubAccounts access level. |
| List Suppressions | `listSuppressions` | Returns every suppressed email address in the Elastic Email account, covering bounces, complaints and unsubscribes in a single list. Requires the ViewSuppressions access level. |
| List Templates | `listTemplates` | Returns a paged list of the email templates in the Elastic Email account, filtered by template scope and optionally by template type. Requires the ViewTemplates access level. |
| List Transaction Events | `listTransactionEvents` | Returns the activity events belonging to a single Elastic Email send transaction, such as delivery, opens and clicks for that send. Requires the ViewReports access level. |
| List Unsubscribes | `listUnsubscribes` | Returns the email addresses suppressed in Elastic Email because the recipient unsubscribed, optionally filtered by a search fragment. Requires the ViewSuppressions access level. |
| List Webhooks | `listWebhooks` | Returns the webhooks registered on the Elastic Email account, with the notification URL and which delivery events each one subscribes to. Requires the ViewSettings access level. |
| Pause Campaign | `pauseCampaign` | Pauses an Elastic Email campaign that is currently sending, by campaign name. Requires the ModifyCampaigns access level. |
| Remove Contacts From List | `removeContactsFromList` | Removes contacts from a named Elastic Email contact list, selected either by an explicit list of email addresses or by a segment rule. Provide either Emails or Rule, not both. The contacts themselves are not deleted. Requires the ModifyContacts access level. |
| Send Bulk Email | `sendBulkEmail` | Sends an email through Elastic Email to a list of recipients, delivering a separate copy to each so recipients never see one another. Per-recipient merge fields can personalise the body. Requires the SendHttp access level. |
| Send Email With Merge File | `sendMergeFileEmail` | Sends an email through Elastic Email to every row of an uploaded CSV merge file, using the file's columns as merge fields. The first column must be named email. Requires the SendHttp access level. |
| Send Transactional Email | `sendTransactionalEmail` | Sends a single transactional email through Elastic Email to To, CC and BCC recipients who all see each other's addresses in the To and CC fields. Use Send Bulk Email instead when each recipient must receive a separate copy. Requires the SendHttp access level. |
| Set Default Sender | `setDefaultSender` | Marks an email address as the default sender address for the Elastic Email account. Requires the ModifySettings access level. |
| Set Inbound Routes Order | `setInboundRoutesOrder` | Changes the position of one inbound route in the Elastic Email evaluation order. The API accepts a JSON array of route/order pairs; this action reorders exactly one route per call, where sort order 1 means the route is evaluated first. Requires the ModifySettings access level. |
| Start Email Verification File | `startVerificationFile` | Starts verifying the addresses in a previously uploaded Elastic Email bulk verification file. Requires the VerifyEmails access level. |
| Update API Key | `updateApiKey` | Updates the name, permissions, expiry and IP restrictions of an existing Elastic Email API key. Permissions not included in the account's billing plan are rejected with HTTP 400. Requires the Security access level. |
| Update Campaign | `updateCampaign` | Updates an existing Elastic Email campaign identified by its current name. Send the full campaign definition; fields that are omitted are cleared by the API. Requires the ModifyCampaigns access level. |
| Update Contact | `updateContact` | Updates the first name, last name and custom fields of an existing Elastic Email contact, identified by email address. Requires the ModifyContacts access level. |
| Update Domain | `updateDomain` | Updates the certificate status, VERP setting and custom bounces domain of an Elastic Email sending domain. Requires the ModifySettings access level. |
| Update Inbound Route | `updateInboundRoute` | Updates an existing Elastic Email inbound route, replacing its name, filter and action. Requires the ModifySettings access level. |
| Update List | `updateList` | Renames an Elastic Email contact list and updates whether contacts may unsubscribe from it. Requires the ModifyContacts access level. |
| Update Segment | `updateSegment` | Updates the name and rule of an existing Elastic Email contact segment. Requires the ModifyContacts access level. |
| Update SMTP Credential | `updateSmtpCredential` | Updates the name, expiry and IP restrictions of an existing Elastic Email SMTP credential. Requires the Security access level. |
| Update Sub-Account Credits | `updateSubAccountCredits` | Adds or subtracts email credits from an Elastic Email sub-account's credit pool, with an optional note recorded in the credit history. Requires the ModifySubAccounts access level. |
| Update Sub-Account Email Settings | `updateSubAccountEmailSettings` | Updates the sending limits and options of an Elastic Email sub-account, such as its daily send limit, maximum contacts and IP pool. Requires the ModifySubAccounts access level. |
| Update Template | `updateTemplate` | Updates an existing Elastic Email template, replacing its name, subject, scope and body parts. Requires the ModifyTemplates access level. |
| Update Webhook | `updateWebhook` | Updates an existing Elastic Email webhook, changing its name, notification URL, event subscriptions or enabled state. Requires the ModifySettings access level. |
| Upload Email Verification File | `uploadVerificationFile` | Uploads CSV text (header row with an email column) to Elastic Email as a multipart file for bulk verification. The upload alone does not start verification. Requires the VerifyEmails access level. |
| Upload File | `uploadFile` | Uploads a file to the Elastic Email account so it can be attached to emails and campaigns by name. The file content is supplied as a Base64 string. Requires the ModifyFiles access level. |
| Verify Domain | `verifyDomain` | Triggers DNS verification for an Elastic Email sending domain and sets the link-tracking protocol to use for it. The request body is a single tracking-type value. Requires the ModifySettings access level. |
| Verify Email Address | `verifyEmailAddress` | Runs an Elastic Email verification on a single email address and returns whether it is valid, risky, unknown or invalid, together with the reason and a predicted deliverability score. Requires the VerifyEmails access level. |
| View Email | `viewEmail` | Returns the rendered subject, sender and body of a previously sent Elastic Email message, identified by its message id. Requires the ViewReports access level. |
