---
description: "LeadMaster CRM (leadmaster.com) — lead management, sales and marketing automation."
hidden: true
---

# LeadMaster

LeadMaster CRM (leadmaster.com) — lead management, sales and marketing automation. Wraps the LeadMaster Web API at webapi.leadmaster.com: leads and account records, contacts, opportunities and opportunity products, cases, quotes, callbacks/activities, campaigns, partners, users and workgroups, custom fields and custom forms, plus the webhook subscription API for entity create/update events. Authentication is an access_token query parameter minted from a LeadMaster username, password and company id.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [leadmaster.com](https://leadmaster.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 85 |
| **Events** | 10 |
| **Slug** | `leadMaster` |

## Use it

Add LeadMaster from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.leadMaster.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Partner | `addPartner` | Create a partner record. List Partners and List Partner Reps were already covered, so partners were read-only. LeadMaster publishes no request schema for this endpoint, so the body field names are taken from the List Partners response shape. |
| Attach Custom Form Record | `attachCustomFormRecord` | Attach a new custom-form record instance to a lead. Update Custom Form Record was already shipped but can only write answers into an instance that already exists; without this action a repeatable form could never gain a new instance from the API. FormID and RECDNO are query params because LeadMaster reads them off the query string on POST. |
| Attach File Link | `attachFileLink` | Attach a file to a LeadMaster record by URL. This is the supported upload path through fastn: LeadMaster's multipart endpoint (PostAttachFileAsync) cannot be driven by the fastn executor, which always sends a JSON content type. Note the query parameter is accesstoken, with no underscore. |
| Create Callback Event | `addCallback` | Create a callback event - LeadMaster's activity/calendar record (a scheduled call, meeting or task) against a lead record and contact. Returns a bare string result. |
| Create Case | `addCase` | Open a support case against a LeadMaster lead record. RECDNO is the parent lead, ContactID the person raising it. IsOpen 1 leaves the case open. |
| Create Contact | `addContact` | Create a contact on a LeadMaster lead record. RecordID is the parent lead (RECDNO). Note LeadMaster expects a JSON array at the root here even for a single contact - this action wraps your fields for you and returns the new contactNOField. |
| Create Lead | `addLead` | Create a lead record in LeadMaster. Company is the account name on the record; the person fields create the primary contact alongside it. Optional fields are dropped from the request when left empty. Returns the new RecordID in Result. |
| Create Opportunity | `addOpportunity` | Create an opportunity against a LeadMaster lead record. rECDNOField is the parent lead RecordID. Add line items separately with Create Product / the opportunity product endpoints. |
| Create Product | `addProduct` | Add a product to the LeadMaster catalog so it can be used as an opportunity line item. Carries the access token in the JSON body rather than the query string. |
| Create Quote | `addQuote` | Create a quote on a LeadMaster lead record. RECDNO is the parent lead; refOppID links the quote to an opportunity. |
| Create Webhook Subscription | `addWebhookSubscription` | Register a webhook URL against a LeadMaster entity event and return the new SubscriptionID. The event catalogue is account, contact, opportunity, case and quote, each created and updated. LeadMaster does not publish the literal SubscriptionEvent strings - confirm the accepted format with List Webhook Subscriptions before relying on this. Note the query parameter is accesstoken, with no underscore. |
| Delete Case | `deleteCase` | Delete a LeadMaster support case by CaseID. POST, not DELETE. |
| Delete Contact | `deleteContact` | Delete a LeadMaster contact by ContactID. POST, not DELETE. |
| Delete Lead | `deleteLead` | Delete a LeadMaster lead record by RecordID. Note this is a POST, not a DELETE. Requires the connected user to hold the DeleteLead privilege. |
| Delete Opportunity | `deleteOpportunity` | Delete a LeadMaster opportunity by OppID. POST, not DELETE. |
| Delete Quote | `deleteQuote` | Delete a LeadMaster quote by QuoteID. POST, not DELETE. |
| Get Access Token | `getAccessToken` | Mint a LeadMaster access token from a username, password and company id. Run this first: the returned token is what you paste into the connection's Access Token field, and it is sent as the access_token query parameter on every other action. The response body is a bare JSON string - the token on success, or the literal "Invalid Credentials" with HTTP 401 on failure. |
| Get Case | `getCase` | Fetch one LeadMaster support case by CaseID. Result is an array holding the single case. |
| Get Company Info | `getCompanyInfo` | Return the LeadMaster company (tenant) profile and feature flags for the connected token - company id, database id, company name, branding, and which modules such as opportunity tracking are enabled. |
| Get Contact | `getContact` | Fetch one LeadMaster contact by ContactID. Result is an array holding the single contact. |
| Get Contact By ID (LMWebAPI) | `getContactByIdWeb` | Read a contact through the legacy LMWebAPI controller. Returns the LMWebAPI field shape, which matches Add Contact and Update Contact; the already-shipped Get Contact uses the Automation controller and a different field shape. |
| Get Contact Email History | `getContactEmailHistory` | Return the emails logged against one LeadMaster contact - sender, recipients, subject, body and sent state. Pass EmailID 0 to get the whole history for the contact. |
| Get Contact Note | `getContactNote` | Return the free-text note stored against one LeadMaster contact. The response is a bare JSON string. |
| Get Custom Field Options | `getCustomFieldOptions` | List the allowed picklist responses for one LeadMaster custom field. Depends on List Custom Fields for the questionID. |
| Get Custom Form | `getCustomForm` | Return the field definitions of one LeadMaster custom form - every question with its type, ordering, validation and mapping. Depends on List Custom Forms for the FormID. |
| Get Custom Form Record | `getCustomFormRecord` | Return the stored answers of one custom form instance on one LeadMaster record, as question id and value pairs. Use List Custom Form Records first to find the ChildRecordID. |
| Get Email Template | `getEmailTemplate` | Read one email template by TemplateID, including its subject, format and message body. List Email Templates was already shipped; this fetches a single template without pulling the whole set. |
| Get Lead | `getLead` | Fetch one LeadMaster lead record by its RecordID. Returns the record inside the Automation envelope; Result is an array with a single element. Answers HTTP 200 even on auth failure - check IsSuccess. |
| Get Lead By RECDNO | `getLeadByRecdno` | Read a lead through the legacy LMWebAPI controller, keyed on RECDNO. Returns the LMWebAPI field shape rather than the Automation shape returned by Get Lead, which is what the other LMWebAPI actions (custom forms, sales rep comments, attached files) key on. |
| Get Lead Nurturing Tracks | `getLeadNurturingTracks` | List the lead-nurturing tracks one LeadMaster contact is enrolled in, with status and start date. Use this to tell whether a contact is already in a drip sequence before enrolling them again. |
| Get Login Info | `getLoginInfo` | Return the logon id, full name and edit permissions of the user the connected access token belongs to. Cheapest read on the connector - use it to verify a connection. |
| Get Logon Name | `getLogonName` | Return the logon name of the user the API credential belongs to. A zero-input read, useful as the connection verification call. |
| Get Opportunity | `getOpportunity` | Fetch one LeadMaster opportunity by OppID. Result is an array holding the single opportunity. Use Get Opportunity Products for its line items. |
| Get Opportunity Products | `getOpportunityProducts` | List the product line items attached to one LeadMaster opportunity, with unit price, quantity and line total. |
| Get Quick Action | `getQuickAction` | Return logged activity statistics (LeadMaster quick actions) for a single lead record. |
| Get Quote | `getQuote` | Fetch one LeadMaster quote by QuoteID. Result is an array holding the single quote. |
| Get Reference Table | `getReferenceTable` | Read any LeadMaster reference (lookup) table by name and return its id/value pairs. This is the generic way to resolve picklist values such as lead status, sales stage or industry code before writing them onto a record. |
| Get Sales Rep Comment | `getSalesRepComment` | Read the sales rep comment recorded on a lead. Complements Get Contact Note, which is the contact-level equivalent. |
| Get User Info | `getUserInfo` | Return the full profile and permission flags of the LeadMaster user behind the connected token - name, user type, company id, admin and edit privileges, last access. |
| List Account Managers | `listAccountManagers` | List the LeadMaster account managers (sales reps) available to the connected user. The idField is the EE_REP value used to assign ownership on leads, contacts and opportunities. |
| List Attached Files | `listAttachedFiles` | List the files attached to one LeadMaster record. Note LeadMaster's own multipart upload endpoint is not usable through fastn - use Attach File Link to attach a file by URL instead. |
| List Available Products | `listAvailableProducts` | Search the LeadMaster product catalog that opportunity line items are drawn from. AvailProductID is what you attach to an opportunity. Pass FieldName/FieldValue to filter, e.g. FieldName=ProductName. |
| List Campaigns | `listCampaigns` | List LeadMaster campaigns as id and name only. mkt_Program_IDField is the Mkt_Program_ID value you set on a lead or contact - use this to populate a campaign picker. |
| List Cases | `listCases` | List LeadMaster support cases with page-number pagination. RECDNO is the parent lead record, ContactID the contact the case was raised for. Answers HTTP 200 on auth failure; check IsSuccess. |
| List Contacts | `listContacts` | List LeadMaster contacts with page-number pagination. Contacts hang off a lead record - RECDNO on each contact is the parent lead's RecordID. Answers HTTP 200 on auth failure; check IsSuccess. |
| List Custom Fields | `listCustomFields` | List every custom field defined in the LeadMaster account, with its question id, form id, type, validation, required flag and mapping. questionIDField is the key you pass to Update Custom Field and Get Custom Field Options. |
| List Custom Form Records For Lead | `listCustomFormRecordsForLead` | List the custom-form records attached to one lead. This is the discovery step before Get Custom Form Record, which needs a FormID and ChildRecordID that this action supplies. |
| List Custom Forms | `listCustomForms` | List the custom forms defined in the LeadMaster account. formIDField feeds Get Custom Form, Get Custom Form Record and Attach Custom Form To Record. |
| List Custom Labels | `listCustomLabels` | List how the LeadMaster account has relabelled its standard fields. Each row maps an internal FieldName to the LabelAlias the customer sees - essential for rendering a field mapping UI, because LeadMaster ships generic column names like User_Field_7 that each account renames. |
| List Databases | `listDatabases` | List the LeadMaster databases the connected user can reach. A database id is the parent of workgroups; pass one to List Workgroups. |
| List Email Templates | `listEmailTemplates` | List the email templates defined in the LeadMaster account, with subject and body. templateIDField feeds Get Email Template. |
| List Function Codes | `listFunctionCodes` | List the LeadMaster function codes used to classify a contact's job function. functionCodeField is the FunctionCode value on a contact. |
| List Groups | `listGroups` | List the LeadMaster groups that contacts can be assigned to. |
| List Leads | `listLeads` | List LeadMaster lead records (the master record, keyed by RecordID / RECDNO) with page-number pagination. Optionally project only the columns you need with fieldsList. Note: this endpoint answers HTTP 200 even when the token is rejected - check IsSuccess in the body, not the status code. |
| List Marketing Campaigns | `listMarketingCampaigns` | List full LeadMaster marketing campaign records - sponsor, launch and end dates, budget, projected leads and revenue, audience and list source. Use List Campaigns instead if you only need id and name. |
| List Opportunities | `listOpportunities` | List LeadMaster opportunities with page-number pagination. RECDNO on each opportunity is the parent lead record. Answers HTTP 200 on auth failure; check IsSuccess. |
| List Partner Reps | `listPartnerReps` | List the partner representatives available in the LeadMaster account. idField is the PartnerRepID value you set on a lead. |
| List Partners | `listPartners` | List the partner (channel/reseller) organisations in the LeadMaster account, with their primary and secondary contacts and address. PartnerID links a lead to its partner via MFGPARTNR. |
| List Quick Actions | `listQuickActions` | Return logged activity statistics (LeadMaster quick actions) across the account. Use Get Quick Action for a single lead's activity counts. |
| List Quotes | `listQuotes` | List LeadMaster quotes with page-number pagination. RECDNO is the parent lead record. Answers HTTP 200 on auth failure; check IsSuccess. |
| List Recently Created Leads | `listRecentlyCreatedLeads` | Return leads created within the last N minutes. The companion to List Recently Updated Leads for new-record polling. Note this endpoint carries the access token in the JSON body rather than the query string. |
| List Recently Updated Callback Events | `listRecentlyUpdatedCallbacks` | Return callback events (activities, meetings, tasks) updated within the last N minutes, with limit/offset paging. The delta-sync surface for activities. |
| List Recently Updated Contacts | `listRecentlyUpdatedContacts` | Return contacts updated within the last N minutes, with limit/offset paging. The delta-sync surface for contacts. |
| List Recently Updated Leads | `listRecentlyUpdatedLeads` | Return leads updated within the last N minutes, with limit/offset paging. This is the delta-sync surface for leads - poll it on a schedule to pick up changes. Returns a bare array, surfaced under items. |
| List Recently Updated Opportunities | `listRecentlyUpdatedOpportunities` | Return opportunities updated within the last N minutes, with limit/offset paging. Each row embeds its product line items under ListOpportunitiesProducts. The delta-sync surface for opportunities. |
| List Title Codes | `listTitleCodes` | List the LeadMaster title codes used to classify a contact's seniority. titleCodeField is the TitleCode value on a contact. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | List the webhook subscriptions registered on the connected LeadMaster account. Run this first on a new account: an existing row's SubscriptionEvent value is the authoritative example of the event-string format, which LeadMaster does not document. Note the query parameter is accesstoken, with no underscore. |
| List Workgroups | `listWorkgroups` | List the workgroups inside one LeadMaster database. Depends on List Databases for the databaseid. |
| Log Contact Email | `logContactEmail` | Record an email against a LeadMaster contact's history. Use this to push activity from an external mailbox into the CRM timeline. externalEmailIdField lets you store the sending system's own message id for idempotency. |
| Remove Webhook Subscription | `removeWebhookSubscription` | Unregister a LeadMaster webhook subscription by SubscriptionID. Both parameters travel in the query string even though this is a POST, and the token parameter is accesstoken with no underscore. Returns a bare string. |
| Search Account | `searchAccount` | Look up the account (company) record behind a lead by an exact field match - field is the LeadMaster column, fldVal the value. In LeadMaster the account and the lead record are the same row, keyed by recordIDField; use this when you are resolving a company rather than a person. |
| Search Callback Events | `searchCallbacks` | Return the callback events (activities) booked for one contact between two dates. All four parameters travel in the query string even though this is a POST. |
| Search Opportunities | `searchOpportunities` | Find an opportunity by an exact match on one field - FieldName is the LeadMaster column, FieldValue the value. Returns the opportunity joined with its parent account and contact details. |
| Search Record By Email | `searchRecordByEmail` | Find lead records by email address. This is the dedupe lookup an inbound integration needs before creating a lead; the generic Search Record action requires naming a field explicitly. Body shape mirrors Search Record, which LeadMaster documents as {access_token, Field, FieldVal}, with the field fixed to email. |
| Search Records | `searchRecords` | Find lead records by an exact match on any single field - pass the LeadMaster column name in Field and the value in FieldVal, e.g. Field=Email, FieldVal=jane@acme.com. This is the general-purpose lookup for dedupe before a create. Returns a bare array of full lead records. |
| Update Case | `updateCase` | Update a LeadMaster support case by CaseID - change status, priority, assignee, or close it by setting IsOpen 0 with a CloseReason and DateClosed. |
| Update Contact | `updateContact` | Update a LeadMaster contact by ContactID. Unlike Create Contact this takes a single object, not an array. Empty optional fields are dropped rather than sent blank. |
| Update Custom Field Value | `updateCustomField` | Set one custom field value on one LeadMaster record. All four parameters travel in the query string even though this is a POST - there is no request body. |
| Update Custom Form Record | `updateCustomFormRecord` | Write answers back to a custom form instance on a LeadMaster record. The body is an array of question id and value pairs; RECDNO, FormID and ChildRecordID travel in the query string. |
| Update Lead | `updateLead` | Update an existing LeadMaster lead record by RecordID. Only the fields you supply are sent - empty optional fields are dropped from the request rather than blanking the column. |
| Update Opportunity | `updateOpportunity` | Update an existing opportunity. This was the only write missing from the opportunity object - Add Opportunity, Delete Opportunity and the product line actions were already covered, leaving opportunities effectively create-only. LeadMaster publishes no request schema for this endpoint, so the body field names are taken from the Get Opportunity response shape. Line-item edits go through Add Opportunity Product and Update Opportunity Product. |
| Update Partner | `updatePartner` | Update a partner record by PartnerID. LeadMaster publishes no request schema for this endpoint, so the body field names are taken from the List Partners response shape. |
| Update Product | `updateProduct` | Update a product in the LeadMaster catalog by ProductId. Carries the access token in the JSON body. |
| Update Quote | `updateQuote` | Update a LeadMaster quote by QuoteID. Only the fields you supply are sent. |
| Validate Logon | `validateLogon` | Validate a LeadMaster username, password and legacy API key pair without minting a token. Useful to confirm API access has been enabled on the account before troubleshooting anything else. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Account created | `account.created` | A LeadMaster account (lead master record) was created. UNVERIFIED EVENT ID: LeadMaster documents this catalogue in the LMEntityUpsert endpoint description but publishes no literal SubscriptionEvent strings. Confirm against an existing row from List Webhook Subscriptions before relying on it; the subscription code passes this id straight through, so only this id needs correcting. |
| Account updated | `account.updated` | A LeadMaster account (lead master record) was updated. UNVERIFIED EVENT ID - see Account created. |
| Case created | `case.created` | A support case was opened. UNVERIFIED EVENT ID - see Account created. |
| Case updated | `case.updated` | A support case was updated. UNVERIFIED EVENT ID - see Account created. |
| Contact created | `contact.created` | A contact was created on a LeadMaster record. UNVERIFIED EVENT ID - see Account created. |
| Contact updated | `contact.updated` | A contact was updated. UNVERIFIED EVENT ID - see Account created. |
| Opportunity created | `opportunity.created` | An opportunity was created. UNVERIFIED EVENT ID - see Account created. |
| Opportunity updated | `opportunity.updated` | An opportunity was updated. UNVERIFIED EVENT ID - see Account created. |
| Quote created | `quote.created` | A quote was created. UNVERIFIED EVENT ID - see Account created. |
| Quote updated | `quote.updated` | A quote was updated. UNVERIFIED EVENT ID - see Account created. |
