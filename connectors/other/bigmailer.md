---
description: "BigMailer email marketing platform."
---

# BigMailer

BigMailer email marketing platform. Manage brands, contacts, lists, fields, segments, templates, senders, message types, suppression lists, users and bulk/RSS/transactional campaigns via the BigMailer v1 REST API.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [bigmailer.io](https://bigmailer.io) |
| **Authentication** | API key |
| **Actions** | 81 |
| **Events** | 0 |
| **Slug** | `bigmailer` |

## Use it

Add BigMailer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bigmailer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Bounce Domain | `createBounceDomain` | Add a bounce (MAIL FROM) subdomain under a BigMailer sending identity. |
| Create Brand | `createBrand` | Create a new brand in your BigMailer account. Returns the new brand id. Note: the BigMailer API has no delete-brand route, so brands can only be removed from the web app. |
| Create Brand Property | `createBrandProperty` | Create a brand property whose value is substituted for its merge tag in templates. |
| Create Bulk Campaign | `createBulkCampaign` | Create a bulk campaign in a BigMailer brand. The campaign stays a draft unless ready is true, in which case BigMailer queues it for sending to every contact in the selected lists. |
| Create Contact | `createContact` | Create a contact in a BigMailer brand with optional field values and list memberships. |
| Create Field | `createField` | Create a custom contact field in a BigMailer brand. |
| Create List | `createList` | Create a contact list in a BigMailer brand. |
| Create Message Type | `createMessageType` | Create a message type in a BigMailer brand so contacts can subscribe or unsubscribe per category. |
| Create Or Update Contact | `upsertContact` | Create a contact, or update it if a contact with the same email already exists in the brand. |
| Create RSS Campaign | `createRssCampaign` | Create an RSS campaign in a BigMailer brand that mails new feed items on a schedule. The campaign stays a draft unless ready is true. |
| Create Segment | `createSegment` | Create a contact segment in a BigMailer brand from a set of conditions. |
| Create Sender | `createSender` | Add a sending identity (a domain or a single email address) to a BigMailer brand. The response carries the DNS records that must be published before the sender can be verified. |
| Create Template | `createTemplate` | Create an email or page template in a BigMailer brand. |
| Create Transactional Campaign | `createTransactionalCampaign` | Create a transactional campaign in a BigMailer brand. Creating it sends nothing; use Send Transactional Email to deliver it to one recipient. |
| Create User | `createUser` | Invite a user to your BigMailer account with a given role. BigMailer emails an invitation to the address supplied. |
| Delete Brand Property | `deleteBrandProperty` | Delete a brand property from a BigMailer brand. |
| Delete Contact | `deleteContact` | Delete a contact from a BigMailer brand by contact id or email address. |
| Delete Field | `deleteField` | Delete a custom contact field from a BigMailer brand. |
| Delete List | `deleteList` | Delete a contact list from a BigMailer brand. Contacts in the list are not deleted. |
| Delete Message Type | `deleteMessageType` | Delete a message type from a BigMailer brand. |
| Delete Segment | `deleteSegment` | Delete a contact segment from a BigMailer brand. |
| Delete Sender | `deleteSender` | Delete a sending identity from a BigMailer brand. |
| Delete Template | `deleteTemplate` | Delete a template from a BigMailer brand. |
| Delete User | `deleteUser` | Remove a user from your BigMailer account. |
| Get Brand | `getBrand` | Retrieve a single BigMailer brand by id, including sending defaults, bounce settings, contact counts and engagement. |
| Get Brand Property | `getBrandProperty` | Retrieve a single brand property from a BigMailer brand. |
| Get Bulk Campaign | `getBulkCampaign` | Retrieve a bulk campaign from a BigMailer brand, including its content, targeting and delivery statistics. |
| Get Campaign Suppression List | `getSuppressionList` | Retrieve a campaign suppression list from a BigMailer brand, including the uploaded file name and size. |
| Get Connection | `getConnection` | Retrieve a single BigMailer sending connection by id. |
| Get Contact | `getContact` | Retrieve a contact from a BigMailer brand by contact id or by email address. |
| Get Contact Batch Status | `getContactBatch` | Get the processing status and per-row results of a contact batch upload. |
| Get Current Account | `getMe` | Retrieve the BigMailer account associated with the API key, returning the account email and company name. |
| Get Field | `getField` | Retrieve a single custom contact field from a BigMailer brand. |
| Get List | `getList` | Retrieve a single contact list in a BigMailer brand, including its contact count and engagement. |
| Get Message Type | `getMessageType` | Retrieve a single message type from a BigMailer brand. |
| Get RSS Campaign | `getRssCampaign` | Retrieve an RSS campaign from a BigMailer brand, including its feed URL, schedule and content. |
| Get RSS Update Campaign | `getRssUpdateCampaign` | Retrieve a single update send generated by a parent RSS campaign, including its delivery statistics. |
| Get Segment | `getSegment` | Retrieve a single contact segment from a BigMailer brand, including its conditions. |
| Get Sender | `getSender` | Retrieve a sending identity from a BigMailer brand, including the DNS records required for sender and bounce-domain verification. |
| Get Template | `getTemplate` | Retrieve a single template from a BigMailer brand, including its HTML body. |
| Get Test Campaign | `getTestCampaign` | Retrieve a previously sent test campaign from a BigMailer brand, including its recipients and status. |
| Get Transactional Campaign | `getTransactionalCampaign` | Retrieve a transactional campaign from a BigMailer brand, including its content and delivery statistics. |
| Get User | `getUser` | Retrieve a single BigMailer account user by id. |
| List Brand Properties | `listBrandProperties` | List the brand properties (merge tags substituted into templates) defined in a BigMailer brand. |
| List Brands | `listBrands` | List the brands in your BigMailer account, with cursor pagination. |
| List Bulk Campaigns | `listBulkCampaigns` | List the bulk (one-off broadcast) campaigns in a BigMailer brand. |
| List Campaign Suppression Lists | `listSuppressionLists` | List the campaign suppression lists uploaded to a BigMailer brand. |
| List Connections | `listConnections` | List the sending connections (e.g. dedicated SMTP/SES connections) configured in your BigMailer account. |
| List Contacts | `listContacts` | List contacts in a BigMailer brand, optionally filtered to a list, with cursor pagination. |
| List Fields | `listFields` | List the custom contact fields defined in a BigMailer brand. |
| List Lists | `listLists` | List the contact lists in a BigMailer brand. |
| List Message Types | `listMessageTypes` | List the message types (subscription categories) in a BigMailer brand. |
| List RSS Campaigns | `listRssCampaigns` | List the RSS-driven recurring campaigns in a BigMailer brand. |
| List RSS Update Campaigns | `listRssUpdateCampaigns` | List the individual update sends generated by a parent RSS campaign. |
| List Segments | `listSegments` | List the contact segments defined in a BigMailer brand. |
| List Senders | `listSenders` | List the verified sending identities (domains and email addresses) in a BigMailer brand. |
| List Templates | `listTemplates` | List the email and page templates in a BigMailer brand. |
| List Test Campaigns | `listTestCampaigns` | List the test campaigns previously sent from a BigMailer brand. |
| List Transactional Campaigns | `listTransactionalCampaigns` | List the transactional campaigns (reusable one-to-one email templates) in a BigMailer brand. |
| List Users | `listUsers` | List the users in your BigMailer account with their roles and activation state. |
| Pause RSS Campaign | `pauseRssCampaign` | Pause an active RSS campaign so BigMailer stops mailing new feed items. |
| Send Test Campaign | `sendTestCampaign` | Send a test email to the listed recipients from a BigMailer brand. This delivers real email immediately. |
| Send Transactional Email | `sendTransactionalCampaign` | Send a transactional campaign to a single recipient. This delivers a real email and consumes sending volume. |
| Unpause RSS Campaign | `unpauseRssCampaign` | Resume a paused RSS campaign so BigMailer starts mailing new feed items again. |
| Update Brand | `updateBrand` | Update a BigMailer brand. Only the fields you supply are changed. |
| Update Brand Property | `updateBrandProperty` | Update a brand property in a BigMailer brand. Only the fields you supply are changed. |
| Update Bulk Campaign | `updateBulkCampaign` | Update a draft bulk campaign in a BigMailer brand. Setting ready to true queues the campaign for sending. |
| Update Contact | `updateContact` | Update a contact in a BigMailer brand. Parameters not supplied are left unchanged; the *_op inputs control whether supplied arrays are added, removed or replaced. |
| Update Field | `updateField` | Update a custom contact field in a BigMailer brand. The field type cannot be changed. |
| Update List | `updateList` | Rename a contact list in a BigMailer brand. |
| Update Message Type | `updateMessageType` | Rename a message type in a BigMailer brand. |
| Update RSS Campaign | `updateRssCampaign` | Update an RSS campaign in a BigMailer brand. Setting ready to true activates it. |
| Update Segment | `updateSegment` | Update a contact segment in a BigMailer brand. Only the fields you supply are changed. |
| Update Sender | `updateSender` | Change whether a BigMailer sending identity is shared with all brands or limited to the current brand. |
| Update Template | `updateTemplate` | Update a template in a BigMailer brand. Only the fields you supply are changed. |
| Update Transactional Campaign | `updateTransactionalCampaign` | Update a transactional campaign in a BigMailer brand. Only the fields you supply are changed. |
| Update User | `updateUser` | Update a BigMailer account user's email, role or allowed brands. |
| Upload Campaign Suppression List | `createSuppressionList` | Upload a CSV of email addresses as a campaign suppression list. Pass the raw CSV text in csv; contacts are not added to the brand, the addresses are only excluded from campaigns that reference the list. |
| Upload Contact Batch | `createContactBatch` | Upload a batch of up to 1,000 contacts to be created or updated asynchronously. Returns a batch id whose progress is polled with Get Contact Batch Status. |
| Verify Bounce Domain | `verifyBounceDomain` | Ask BigMailer to re-check the DNS records for a sender's bounce domain. Publish the records under bounce_dns_records from Get Sender first. |
| Verify Sender | `verifySender` | Ask BigMailer to re-check the DNS records for a sending identity. Publish the records under dns_records from Get Sender first; the response reports whether verification succeeded. |
