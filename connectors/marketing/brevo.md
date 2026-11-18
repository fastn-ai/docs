---
description: "Brevo (formerly Sendinblue) marketing platform: contacts, email and SMS campaigns, transactional email/SMS, CRM (companies, deals, tasks, notes, pipelines),…"
hidden: true
---

# Brevo

<img src="../../.gitbook/assets/connectors/lg/brevo.png" alt="Brevo logo">

Brevo (formerly Sendinblue) marketing platform: contacts, email and SMS campaigns, transactional email/SMS, CRM (companies, deals, tasks, notes, pipelines), ecommerce, senders, domains, and webhooks.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [brevo.com](https://brevo.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `brevo` |

## Use it

Add Brevo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.brevo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Ecommerce | `activateEcommerce` | Activate the Ecommerce application on your Brevo account. |
| Add Blocked Domain | `addBlockedDomain` | Add a domain to the transactional email block list. |
| Add Contacts to List | `addContactsToList` | Add existing contacts to a list by email or contact ID. |
| Authenticate Domain | `authenticateDomain` | Authenticate a sender domain once the required DNS records are set. |
| Create Categories Batch | `createCategoriesBatch` | Create or update multiple ecommerce categories in a batch. |
| Create Company | `createCompany` | Create a new CRM company. |
| Create Contact | `createContact` | Create a new contact in Brevo. |
| Create Contact Attribute | `createContactAttribute` | Create a new contact attribute in a given category. |
| Create Coupon Collection | `createCouponCollection` | Create a new coupon collection. |
| Create Coupons | `createCoupons` | Add coupon codes to an existing coupon collection. |

<details>

<summary>See 133 more actions</summary>

* **Create Deal** `createDeal`: Create a new CRM deal.
* **Create Domain** `createDomain`: Create a new sender domain. Returns the DNS records to configure.
* **Create Email Campaign** `createEmailCampaign`: Create a new classic or trigger email campaign.
* **Create Email Template** `createEmailTemplate`: Create a new transactional email template.
* **Create Folder** `createFolder`: Create a new contact folder.
* **Create List** `createList`: Create a new contact list inside a folder.
* **Create Note** `createNote`: Create a new CRM note linked to contacts, deals, or companies.
* **Create or Update Category** `createCategory`: Create or update an ecommerce product category.
* **Create or Update Order** `createOrder`: Create or update an ecommerce order with its status and products.
* **Create or Update Orders Batch** `createOrdersBatch`: Create or update multiple ecommerce orders in a single batch.
* **Create or Update Product** `createProduct`: Create or update an ecommerce product.
* **Create Products Batch** `createProductsBatch`: Create or update multiple ecommerce products in a batch.
* **Create Sender** `createSender`: Create a new email sender. Triggers a validation email.
* **Create SMS Campaign** `createSmsCampaign`: Create a new SMS campaign.
* **Create Task** `createTask`: Create a new CRM task.
* **Create Webhook** `createWebhook`: Create a webhook to receive event notifications at a target URL.
* **Create WhatsApp Campaign** `createWhatsappCampaign`: Create a new WhatsApp campaign from an approved template.
* **Delete Blocked Domain** `deleteBlockedDomain`: Remove a domain from the transactional email block list.
* **Delete Company** `deleteCompany`: Delete a CRM company by ID.
* **Delete Contact** `deleteContact`: Delete a contact by email address or contact ID.
* **Delete Contact Attribute** `deleteContactAttribute`: Delete a contact attribute by category and name.
* **Delete Deal** `deleteDeal`: Delete a CRM deal by ID.
* **Delete Domain** `deleteDomain`: Delete a sender domain by name.
* **Delete Email Campaign** `deleteEmailCampaign`: Delete an email campaign by ID.
* **Delete Email Template** `deleteEmailTemplate`: Delete a transactional email template by ID.
* **Delete Folder** `deleteFolder`: Delete a contact folder and all lists inside it.
* **Delete Hardbounces** `deleteHardbounces`: Delete hardbounces over a date range, optionally for a specific contact.
* **Delete List** `deleteList`: Delete a contact list by ID.
* **Delete Note** `deleteNote`: Delete a CRM note by ID.
* **Delete Scheduled Email** `deleteScheduledEmail`: Delete scheduled transactional emails by batchId or messageId before they are sent.
* **Delete Sender** `deleteSender`: Delete an email sender by ID.
* **Delete SMS Campaign** `deleteSmsCampaign`: Delete an SMS campaign by ID.
* **Delete Task** `deleteTask`: Delete a CRM task by ID.
* **Delete Webhook** `deleteWebhook`: Delete a webhook by ID.
* **Delete WhatsApp Campaign** `deleteWhatsappCampaign`: Delete a WhatsApp campaign by ID.
* **Export Contacts** `exportContacts`: Export contacts to a file. Returns a process ID; the file is delivered via notifyUrl.
* **Export Email Campaign Recipients** `exportEmailCampaignRecipients`: Export the recipients of an email campaign to a file (delivered via notifyUrl).
* **Export Webhook Events** `exportWebhookEvents`: Export webhook event history to a CSV file; Brevo sends the file link to the Notify URL. Enterprise feature: Brevo must activate it on the account.
* **Get Account** `getAccount`: Get your Brevo account details including company, plan, and credit information.
* **Get All Pipelines** `getPipelines`: Get details of all CRM pipelines and their stages.
* **Get Category** `getCategory`: Get an ecommerce category by ID.
* **Get Company** `getCompany`: Get a CRM company by ID.
* **Get Company Attributes** `getCompanyAttributes`: Get the list of CRM company attributes.
* **Get Contact** `getContact`: Get details of a contact by email address or contact ID.
* **Get Contacts in List** `getContactsInList`: Get all contacts belonging to a specific list.
* **Get Coupon Collection** `getCouponCollection`: Get a coupon collection by ID.
* **Get CRM Attributes** `getCrmAttributes`: Get all CRM attributes for contacts, companies, and deals.
* **Get Deal** `getDeal`: Get a CRM deal by ID.
* **Get Deal Attributes** `getDealAttributes`: Get the list of CRM deal attributes.
* **Get Domain Configuration** `getDomainConfiguration`: Get the DNS configuration and authentication status of a sender domain.
* **Get Email Campaign** `getEmailCampaign`: Get details and statistics of an email campaign by ID.
* **Get Email Template** `getEmailTemplate`: Get a transactional email template by ID.
* **Get Folder** `getFolder`: Get details of a contact folder by ID.
* **Get Inbound Event** `getInboundEvent`: Get details of a single inbound parsed email event by UUID.
* **Get List** `getList`: Get details of a contact list by ID.
* **Get Lists in Folder** `getFolderLists`: Get all the lists inside a specific folder.
* **Get Note** `getNote`: Get a CRM note by ID.
* **Get Pipeline** `getPipeline`: Get details of a specific CRM pipeline by ID.
* **Get Product** `getProduct`: Get an ecommerce product by ID.
* **Get SMS Aggregated Report** `getSmsAggregatedReport`: Get a global aggregated report of transactional SMS activity.
* **Get SMS Campaign** `getSmsCampaign`: Get an SMS campaign by ID.
* **Get SMS Events** `getSmsEvents`: Get all events for transactional SMS.
* **Get SMS Report** `getSmsReport`: Returns a day-by-day report of transactional SMS activity. The endpoint does not accept paging parameters; limit the span with Days or a date range instead.
* **Get Task** `getTask`: Get a CRM task by ID.
* **Get Task Types** `getTaskTypes`: Get the list of CRM task types.
* **Get Transactional Email Aggregated Report** `getTransactionalEmailAggregatedReport`: Get a global aggregated report of transactional email activity over a period.
* **Get Transactional Email Events** `getTransactionalEmailEvents`: Get all events for transactional emails (delivered, opened, clicked, bounced, etc.).
* **Get Transactional Email Report** `getTransactionalEmailReport`: Get an aggregated day-by-day report of transactional email activity.
* **Get Webhook** `getWebhook`: Get details of a webhook by ID.
* **Get WhatsApp Account Info** `getWhatsappAccountInfo`: Get your WhatsApp API account information: business verification, phone number status and quality, and sending limit.
* **Get WhatsApp Campaign** `getWhatsappCampaign`: Get a WhatsApp campaign by ID.
* **Import Contacts** `importContacts`: Import contacts in bulk from a file URL, inline JSON, or CSV body.
* **Link or Unlink Company** `linkUnlinkCompany`: Link or unlink a company with contacts and deals.
* **Link or Unlink Deal** `linkUnlinkDeal`: Link or unlink a deal with contacts and companies.
* **List Blocked Contacts** `listBlockedContacts`: Get the list of blocked or unsubscribed transactional contacts.
* **List Blocked Domains** `listBlockedDomains`: Get the list of blocked domains for transactional email.
* **List Categories** `listCategories`: Get all ecommerce product categories with pagination.
* **List Companies** `listCompanies`: Get all CRM companies with filtering and pagination.
* **List Contact Attributes** `listContactAttributes`: Get the list of all contact attributes defined in your account.
* **List Contacts** `listContacts`: Get all contacts in your Brevo account with pagination.
* **List Coupon Collections** `listCouponCollections`: Get all coupon collections with pagination.
* **List CRM Files** `listCrmFiles`: Get all CRM files linked to contacts, deals, or companies.
* **List Deals** `listDeals`: Get all CRM deals, with filters by deal name, owner, stage, pipeline, linked company or contact, and created or modified date, plus paging and sorting.
* **List Domains** `listDomains`: Get the list of all sender domains and their authentication status.
* **List Email Campaigns** `listEmailCampaigns`: Get all email campaigns with filtering and pagination.
* **List Email Templates** `listEmailTemplates`: Get the list of transactional email templates.
* **List Folders** `listFolders`: Get all contact folders with pagination.
* **List Inbound Events** `listInboundEvents`: Get the list of inbound parsed email events.
* **List Lists** `listLists`: Get all contact lists with pagination.
* **List Notes** `listNotes`: Get all CRM notes with optional entity filters.
* **List Orders** `listOrders`: Get all ecommerce orders, with paging, sorting and filters by created or modified date.
* **List Products** `listProducts`: Get all ecommerce products with pagination.
* **List Segments** `listSegments`: Get all contact segments with pagination.
* **List Senders** `listSenders`: Get the list of all email senders.
* **List SMS Campaigns** `listSmsCampaigns`: Get all SMS campaigns with filtering and pagination.
* **List Tasks** `listTasks`: Get all CRM tasks, with filters by task type, status, due date, assignee, and linked contacts, deals or companies, plus paging and sorting.
* **List Transactional Emails** `listTransactionalEmails`: Lists transactional emails that were sent. Brevo requires at least one of Email, Message ID or Template ID to be supplied; a call with only dates or paging returns 400 missing_parameter.
* **List Webhooks** `listWebhooks`: Get all webhooks of a given type.
* **List WhatsApp Campaigns** `listWhatsappCampaigns`: Get all WhatsApp campaigns with pagination.
* **List WhatsApp Templates** `listWhatsappTemplates`: Get all WhatsApp message templates, with paging, sorting, and filters by creation date and source.
* **Remove Contacts from List** `removeContactsFromList`: Remove contacts from a list by email or contact ID.
* **Send Double Opt-In Confirmation** `sendDoubleOptinConfirmation`: Send a double opt-in confirmation email to a contact.
* **Send Email Campaign Now** `sendEmailCampaignNow`: Send an email campaign immediately.
* **Send Email Campaign Report** `sendEmailCampaignReport`: Email an existing email campaign report to specified recipients.
* **Send Email Campaign Test** `sendEmailCampaignTest`: Send a test of an email campaign to specific email addresses.
* **Send SMS Campaign Now** `sendSmsCampaignNow`: Send an SMS campaign immediately.
* **Send SMS Campaign Report** `sendSmsCampaignReport`: Email an SMS campaign report to specified recipients.
* **Send SMS Campaign Test** `sendSmsCampaignTest`: Send a test of an SMS campaign to specific phone numbers.
* **Send Test Template** `sendTestTemplate`: Send a test of a transactional email template to specific addresses.
* **Send Transactional Email** `sendTransactionalEmail`: Send a transactional email via SMTP, with content or a template.
* **Send Transactional SMS** `sendTransactionalSms`: Send a transactional SMS message.
* **Track Event** `trackEvent`: Track a custom marketing automation event for a contact.
* **Unblock Contact** `unblockContact`: Unblock or resubscribe a transactional contact by email.
* **Update Company** `updateCompany`: Update an existing CRM company.
* **Update Contact** `updateContact`: Update an existing contact identified by email or contact ID.
* **Update Contact Attribute** `updateContactAttribute`: Update an existing contact attribute.
* **Update Contacts in Batch** `updateContactsBatch`: Update multiple contacts at once.
* **Update Coupon Collection** `updateCouponCollection`: Update a coupon collection's default coupon.
* **Update Deal** `updateDeal`: Update an existing CRM deal.
* **Update Email Campaign** `updateEmailCampaign`: Update an existing email campaign.
* **Update Email Campaign Status** `updateEmailCampaignStatus`: Change the status of an email campaign (suspend, archive, schedule, send).
* **Update Email Template** `updateEmailTemplate`: Update a transactional email template.
* **Update Folder** `updateFolder`: Update the name of a contact folder.
* **Update List** `updateList`: Update a contact list's name or move it to another folder.
* **Update Note** `updateNote`: Update an existing CRM note.
* **Update Sender** `updateSender`: Update an existing email sender.
* **Update SMS Campaign** `updateSmsCampaign`: Update an existing SMS campaign.
* **Update SMS Campaign Status** `updateSmsCampaignStatus`: Change the status of an SMS campaign.
* **Update Task** `updateTask`: Update an existing CRM task.
* **Update Webhook** `updateWebhook`: Update an existing webhook's URL, description, or events.
* **Update WhatsApp Campaign** `updateWhatsappCampaign`: Update a WhatsApp campaign: name, status (scheduled or suspended), new send time, or recipients (lists and segments).
* **Upload Email Campaign Image** `uploadEmailCampaignImage`: Upload an image to the Brevo image gallery for email campaigns, from a public image URL.
* **Validate Sender** `validateSender`: Validate a sender using the OTP code sent to the sender email.

</details>
