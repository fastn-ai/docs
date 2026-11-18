---
description: "Keap (formerly Infusionsoft) CRM, sales, and marketing automation platform."
---

# Keap

Keap (formerly Infusionsoft) CRM, sales, and marketing automation platform. Contacts, companies, opportunities, orders, subscriptions, products, tasks, appointments, notes, emails, tags, campaigns, automations, affiliates, files, users, and REST Hook webhooks over the Keap v1 + v2 REST API.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [keap.com](https://keap.com) |
| **Authentication** | API key |
| **Actions** | 206 |
| **Events** | 0 |
| **Slug** | `keap` |

## Use it

Add Keap from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.keap.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Achieve an Automation Goal | `achieveAutomationGoal` | Achieve an automation goal for a contact. Use integration+call_name OR automation_id+goal_id. |
| Add Contacts to Automation Sequence | `addContactsToAutomationSequence` | Add contacts to an automation sequence |
| Add Contacts to Campaign Sequence | `addContactsToCampaignSequence` | Add contacts to a campaign sequence |
| Add Tag to Company | `addTagToCompany` | Add a tag to a company |
| Adjust Product Inventory | `adjustProductInventory` | Increase/decrease a product's inventory |
| Apply Tag to Contacts | `applyTagToContacts` | Apply a tag to contacts (v2) |
| Apply Tags to a Contact | `applyTagsToContact` | Apply one or more tags to a contact (v1) |
| Batch Add Email Records | `batchAddEmails` | Create a set of email records (max 1000) |
| Batch Remove Email Records | `batchRemoveEmails` | Delete a set of email records |
| Cancel a Subscription | `cancelSubscription` | Deactivate/cancel a subscription |
| Create a Company | `createCompany` | Create a Company (company_name required) |
| Create a Contact | `createContact` | Create a Contact. Provide duplicate_option (Email/EmailAndName/EmailAndNameAndCompany) to upsert on a match; at minimum supply an email address or given_name/family_name. |
| Create a Contact Credit Card | `createContactCreditCard` | Add a credit card to a contact (v1) |
| Create a Contact Custom Field | `createContactCustomField` | Create a Contact custom field |
| Create a Contact Custom Field Group | `createContactCustomFieldGroup` | Create a Contact custom field group |
| Create a Contact Email Record | `createContactEmail` | Record a sent/received email for a contact (v1) |
| Create a Contact Link type | `createContactLinkType` | Create a Contact Link type |
| Create a Contact Note | `createContactNote` | Create a note for a contact. Provide title or type, and user_id. |
| Create a File | `createFile` | Create a file. Provide file_name, file_data (Base64), is_public, and optionally contact_id. |
| Create a Hook Subscription | `createHook` | Create a REST Hook (webhook) subscription for an event key + target URL |
| Create a Lead Source | `createLeadSource` | Create a lead source (name required) |
| Create a Product | `createProduct` | Create a product (name, price, short_description required). price in smallest currency unit (cents). |
| Create a Product Category | `createProductCategory` | Create a product category (name required) |
| Create a Referral | `createReferral` | Create a referral (contact_id required) |
| Create a Subscription | `createSubscription` | Create a subscription (contact_id, subscription_plan_id required) |
| Create a Task | `createTask` | Create a Task (assigned_to_user_id required) |
| Create a User | `createUser` | Create/invite a user (v1). email + given_name required. |
| Create an Affiliate | `createAffiliate` | Create an affiliate (code + contact_id required) |
| Create an Affiliate Link | `createAffiliateRedirect` | Create an affiliate redirect link (code, name, website_address required) |
| Create an Appointment | `createAppointment` | Create an appointment (v1). title, start_date, end_date required. |
| Create an Appointment Custom Field | `createAppointmentCustomField` | Create an appointment custom field (v1) |
| Create an Email Record | `createEmailRecord` | Create an email record (sent_to_address required) |
| Create an Opportunity | `createOpportunity` | Create an Opportunity (opportunity_title required; stage_id + contact_id recommended) |
| Create an Opportunity Stage | `createOpportunityStage` | Create an opportunity stage |
| Create an Order | `createOrder` | Create an order (contact_id, order_time, order_title, order_type required; include order_items) |
| Create an Order Item | `createOrderItem` | Add an item to an order (order_id, quantity required) |
| Create an Order Payment | `createOrderPayment` | Record/charge a payment on an order (order_id, payment_amount, apply_to_commissions required) |
| Create Automation Category | `createAutomationCategory` | Create an automation category |
| Create Product Subscription Plan | `createProductSubscriptionPlan` | Create a subscription plan on a product (product_id, cycle_type, plan_price required) |
| Create Tag | `createTag` | Create a tag (category.id required) |
| Create Tag Category | `createTagCategory` | Create a tag category (unique name) |
| Delete a Company | `deleteCompany` | Delete a Company |
| Delete a Contact | `deleteContact` | Delete a Contact |
| Delete a Contact Custom Field | `deleteContactCustomField` | Delete a Contact custom field |
| Delete a Contact Link type | `deleteContactLinkType` | Delete a Contact Link type |
| Delete a File | `deleteFile` | Delete a file |
| Delete a Hook Subscription | `deleteHook` | Delete a REST Hook subscription |
| Delete a Lead Source | `deleteLeadSource` | Delete a lead source |
| Delete a Note | `deleteContactNote` | Delete a Note |
| Delete a Product | `deleteProduct` | Delete a product |
| Delete a Product Category | `deleteProductCategory` | Delete a product category |
| Delete a Task | `deleteTask` | Delete a Task |
| Delete an Affiliate | `deleteAffiliate` | Delete an affiliate |
| Delete an Affiliate Link | `deleteAffiliateRedirect` | Delete an affiliate redirect link |
| Delete an Appointment | `deleteAppointment` | Delete an appointment (v1) |
| Delete an Email Record | `deleteEmail` | Delete an email record |
| Delete an Opportunity | `deleteOpportunity` | Delete an Opportunity |
| Delete an Opportunity Stage | `deleteOpportunityStage` | Delete an opportunity stage |
| Delete an Order | `deleteOrder` | Delete an order |
| Delete an Order Item | `deleteOrderItem` | Delete an order item |
| Delete Automation Categories | `deleteAutomationCategories` | Delete automation categories by ids |
| Delete Tag | `deleteTag` | Delete a tag |
| Delete Tag Category | `deleteTagCategory` | Delete a tag category |
| Get Application Configuration | `getApplicationConfiguration` | Get Application Configuration |
| Get Application Status | `isApplicationEnabled` | Get Application Status |
| Get Contact Option types | `getContactOptionTypes` | Get Contact Option types |
| Get Country | `getCountry` | Get Country |
| Get User Email Signature | `getUserSignature` | Get a user's email signature |
| Insert UTMs for a Contact | `insertContactUtm` | Insert UTM parameters for a contact (v1) |
| Invoice a Subscription | `invoiceSubscription` | Generate an invoice for a subscription |
| Link Contacts | `linkContacts` | Link two Contacts by a link type |
| List a Country's Provinces | `listProvinces` | List a Country's Provinces |
| List Affiliate Links | `listAffiliateRedirects` | List affiliate redirect links |
| List Affiliate Payments | `listAffiliatePayments` | List an affiliate's payments |
| List Affiliate Summaries | `listAffiliateSummaries` | List affiliate summaries |
| List Affiliates | `listAffiliates` | List affiliates |
| List All Notes | `listNotes` | List all notes across contacts |
| List Applied Tags | `listContactTags` | List tags applied to a contact |
| List Applied Tags (v1) | `listContactAppliedTags` | List tags applied to a contact (v1) |
| List Appointments | `listAppointments` | List appointments (v1). Provide since/until date-times. |
| List Automation Categories | `listAutomationCategories` | List automation categories |
| List Automation Ids | `listAutomationIds` | List automation IDs |
| List Automations | `listAutomations` | List automations |
| List Campaign Goals | `getCampaignGoals` | List goals for a campaign |
| List Campaign Sequences | `getCampaignSequences` | List sequences for a campaign |
| List Campaigns | `listCampaigns` | List campaigns |
| List Companies | `listCompanies` | List Companies |
| List Company Applied Tags | `listCompanyTags` | List tags applied to a company |
| List Contact Custom Field Groups | `listContactCustomFieldGroups` | List Contact custom field groups |
| List Contact Email Records | `listContactEmails` | List email records for a contact (v1) |
| List Contact Link types | `listContactLinkTypes` | List Contact Link types |
| List Contact Notes | `listContactNotes` | List notes for a contact |
| List Contacts | `listContacts` | List Contacts |
| List Countries | `listCountries` | List Countries |
| List Email Address Statuses | `listEmailAddresses` | List email address opt-in statuses |
| List Emails | `listEmails` | List email records |
| List Files | `listFiles` | List files |
| List Hook Event Types | `listHookEventTypes` | List available REST Hook event keys |
| List Hook Subscriptions | `listHooks` | List stored REST Hook subscriptions |
| List Lead Sources | `listLeadSources` | List lead sources |
| List Linked Contacts | `listContactLinks` | List a contact's links |
| List Merchant accounts | `listMerchants` | List Merchant accounts |
| List Opportunities | `listOpportunities` | List Opportunities |
| List Opportunity Stage Moves | `listOpportunityStageMoves` | List opportunity stage moves |
| List Opportunity Stages | `listOpportunityStages` | List opportunity stages (pipeline) |
| List Order Payments | `listOrderPayments` | List payments on an order |
| List Orders | `listOrders` | List orders |
| List Payment Methods | `listPaymentMethods` | List payment methods |
| List Product Categories | `listProductCategories` | List product categories |
| List Product Subscription Plans | `listProductSubscriptionPlans` | List a product's subscription plans |
| List Products | `listProducts` | List products |
| List Referrals | `listReferrals` | List referrals |
| List Sales Payments | `listSalesPayments` | List sales payments |
| List Shipping methods | `listShippingMethods` | List Shipping methods |
| List Subscriptions | `listSubscriptions` | List subscriptions |
| List Tag Categories | `listTagCategories` | List tag categories |
| List Tagged Companies | `listTagCompanies` | List companies with a tag |
| List Tagged Contacts | `listTagContacts` | List contacts with a tag |
| List Tags | `listTags` | Retrieves a list of tags defined in the Keap application. Returns the tags and a next_page_token for paging. |
| List Tasks | `listTasks` | List Tasks |
| List Transactions | `listTransactions` | List sales transactions |
| List User Groups | `listUserGroups` | List user groups |
| List Users | `listUsers` | List users |
| List Webforms with filter | `listWebforms` | List Webforms with filter |
| Merge two Contacts | `mergeContacts` | Merge two Contacts |
| Remove Contacts from Campaign Sequence | `removeContactsFromCampaignSequence` | Remove contacts from a campaign sequence |
| Remove Tag from Company | `removeTagFromCompany` | Remove a tag from a company |
| Remove Tag from Contacts | `removeTagFromContacts` | Remove a tag from contacts (v2) |
| Remove Tags from a Contact | `removeTagsFromContact` | Remove applied tags from a contact (v1) |
| Replace an Appointment | `updateAppointment` | Replace an appointment (v1 PUT). title/start_date/end_date required. |
| Retrieve a Campaign | `getCampaign` | Retrieve a campaign |
| Retrieve a Company | `getCompany` | Retrieve a Company |
| Retrieve a Contact | `getContact` | Retrieve a Contact |
| Retrieve a Contact Custom Field Group | `getContactCustomFieldGroup` | Retrieve a Contact custom field group |
| Retrieve a File | `getFile` | Retrieve a file's metadata |
| Retrieve a File's Data | `getFileData` | Retrieve a file's binary data |
| Retrieve a Hook Subscription | `getHook` | Retrieve a REST Hook subscription |
| Retrieve a Lead Source | `getLeadSource` | Retrieve a lead source |
| Retrieve a Note | `getContactNote` | Retrieve a Note |
| Retrieve a Product | `getProduct` | Retrieve a product |
| Retrieve a Product Category | `getProductCategory` | Retrieve a product category |
| Retrieve a Subscription | `getSubscription` | Retrieve a subscription |
| Retrieve a Tag | `getTag` | Retrieve a tag |
| Retrieve a Tag Category | `getTagCategory` | Retrieve a tag category |
| Retrieve a Task | `getTask` | Retrieve a Task. NOTE: Keap's GET /crm/rest/v2/tasks/{id} returns 404 "Unable to find this Task" even for ids returned by GET /crm/rest/v2/tasks. Use getTaskById instead; the unified CRM task mapping is bound to getTaskById. |
| Retrieve a Task by Id | `getTaskById` | Retrieve a single Task by id. Keap's GET /crm/rest/v2/tasks/{id} returns 404 for tasks that GET /crm/rest/v2/tasks returns, and the v1 /tasks/{id} resource is not reachable either, so this action uses the v2 collection endpoint with filter=id==&lt;id&gt;. |
| Retrieve a User | `getUser` | Retrieve a user |
| Retrieve a User Group | `getUserGroup` | Retrieve a user group |
| Retrieve account profile | `getAccountProfile` | Retrieve account profile |
| Retrieve Affiliate Commission Total | `getAffiliateCommissionTotal` | Retrieve affiliate commission earned and ledger URL |
| Retrieve Affiliate Commissions | `getAffiliateCommissions` | Retrieve an affiliate's commissions |
| Retrieve Affiliate Model | `getAffiliateModel` | Retrieve affiliate custom-field model |
| Retrieve Affiliate Referrals | `listAffiliateReferrals` | List an affiliate's referrals |
| Retrieve an Affiliate | `getAffiliate` | Retrieve an affiliate |
| Retrieve an Affiliate Link | `getAffiliateRedirect` | Retrieve an affiliate redirect link |
| Retrieve an Appointment | `getAppointment` | Retrieve an appointment (v1) |
| Retrieve an Automation | `getAutomation` | Retrieve an automation |
| Retrieve an Email | `getEmail` | Retrieve an email record |
| Retrieve an Email Address status | `getEmailAddressStatus` | Retrieve opt-in status of an email address |
| Retrieve an Email Template | `getEmailTemplate` | Retrieve an email template |
| Retrieve an Opportunity | `getOpportunity` | Retrieve an Opportunity |
| Retrieve an Opportunity Stage | `getOpportunityStage` | Retrieve an opportunity stage |
| Retrieve an Opportunity Stage Move | `getOpportunityStageMove` | Retrieve an opportunity stage move |
| Retrieve an Order | `getOrder` | Retrieve an order |
| Retrieve an Order Item | `getOrderItem` | Retrieve an order item |
| Retrieve Appointment Model | `getAppointmentModel` | Retrieve appointment custom-field model (v1) |
| Retrieve Business Profile | `getBusinessProfile` | Retrieve Business Profile |
| Retrieve Company Model | `getCompanyModel` | Retrieve company custom-field model |
| Retrieve Contact Credit Cards | `listContactCreditCards` | List a contact's stored credit cards (v1) |
| Retrieve Contact Model | `getContactModel` | Retrieve Contact Model (custom fields definition) |
| Retrieve Lead Score of a Contact | `getContactLeadScore` | Retrieve lead score of a contact |
| Retrieve Note Model | `getNoteModel` | Retrieve note custom-field model |
| Retrieve Note Templates | `listNoteTemplates` | Retrieve note templates |
| Retrieve Task Model | `getTaskModel` | Retrieve task custom-field model |
| Retrieve User Info | `getUserInfo` | Retrieve the authenticated user's info |
| Send an Email | `sendEmail` | Send an email to contacts (contacts, subject, user_id required) |
| Send Email from Template | `sendEmailTemplate` | Send an email based on a template (contact_ids, template_id, user_id required) |
| Unlink Contacts | `unlinkContacts` | Delete a link between two Contacts |
| Unpublish an Automation | `unpublishAutomation` | Unpublish an automation |
| Update a Company | `updateCompany` | Update a Company |
| Update a Contact | `updateContact` | Update a Contact |
| Update a Contact Link type | `updateContactLinkType` | Update a Contact Link type |
| Update a File | `updateFile` | Update a file's metadata/content |
| Update a Hook Subscription | `updateHook` | Update a REST Hook subscription |
| Update a Lead Source | `updateLeadSource` | Update a lead source |
| Update a Note | `updateContactNote` | Update a Note |
| Update a Product | `updateProduct` | Update a product |
| Update a Product Category | `updateProductCategory` | Update a product category |
| Update a Subscription | `updateSubscription` | Update a subscription |
| Update a Tag | `updateTag` | Update a tag |
| Update a Tag Category | `updateTagCategory` | Update a tag category |
| Update a Task | `updateTask` | Update a Task |
| Update a User | `updateUser` | Update a user |
| Update an Affiliate | `updateAffiliate` | Update an affiliate |
| Update an Affiliate Link | `updateAffiliateRedirect` | Update an affiliate redirect link |
| Update an Appointment | `patchAppointment` | Partially update an appointment (v1 PATCH) |
| Update an Email Address opt-in status | `updateEmailAddressStatus` | Update opt-in status of an email address |
| Update an Opportunity | `updateOpportunity` | Update an Opportunity |
| Update an Opportunity Stage | `updateOpportunityStage` | Update an opportunity stage |
| Update an Order | `updateOrder` | Update an order |
| Update an Order Item | `updateOrderItem` | Update an order item |
| Update Automation Category | `updateAutomationCategory` | Update an automation category |
| Update Business Profile | `updateBusinessProfile` | Update Business Profile |
| Updates an account profile | `updateAccountProfile` | Updates an account profile |
| Verify a Hook Subscription | `verifyHook` | Verify a REST Hook subscription (immediate) |
| Verify a Hook Subscription (Delayed) | `verifyHookDelayed` | Verify a REST Hook subscription using the delayed X-Hook-Secret handshake |
