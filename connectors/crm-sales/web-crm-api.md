---
description: "webCRM via the webCRM REST API (api.webcrm.com)."
---

# webCRM

webCRM via the webCRM REST API (api.webcrm.com). Manage organisations, persons, B2C persons, opportunities, deliveries, activities, events, meetings, support cases, products, quotation lines, documents, users, price groups, VAT and account settings, and register per-entity webhooks (hooks) for create, update and delete events. Access tokens are minted from the webCRM API token and renewed automatically.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [webcrm.com](https://webcrm.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 334 |
| **Events** | 42 |
| **Slug** | `webCrmApi` |

## Use it

Add webCRM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.webCrmApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Delivery to Opportunity | `convertDeliveryToOpportunity` | Converts the delivery with the specified ID into an opportunity at the given pipeline level in webCRM and returns the new opportunity ID. |
| Convert Opportunity to Delivery | `convertOpportunityToDelivery` | Converts the opportunity with the specified ID into a delivery in webCRM and returns the new delivery ID. |
| Create Activity | `createActivity` | Adds a new activity to webCRM and returns the assigned ID. |
| Create Activity Hook | `createActivityHook` | Registers a webhook that webCRM calls at the target URL when an activity is created, updated or deleted, and returns the assigned hook ID. Send 0 as the ID for a new hook. |
| Create Activity Linked Data Item | `createActivityLinkedDataItem` | Creates a linked data item for activities in webCRM and returns the assigned ID. Send 0 as the ID for a new item. |
| Create Activity Note | `createActivityNote` | Adds a new note to an activity in webCRM. |
| Create B2C Person | `createB2CPerson` | Adds a new b2c person to webCRM and returns the assigned ID. Send 0 as PersonB2CId. |
| Create B2C Person Hook | `createB2CPersonHook` | Registers a webhook that webCRM calls at the target URL when a b2c person is created, updated or deleted, and returns the assigned hook ID. Send 0 as the ID for a new hook. |
| Create B2C Person Linked Data Item | `createB2CPersonLinkedDataItem` | Creates a linked data item for b2c persons in webCRM and returns the assigned ID. Send 0 as the ID for a new item. |
| Create Delivery | `createDelivery` | Adds a new delivery to webCRM and returns the assigned ID. |
| Create Delivery Hook | `createDeliveryHook` | Registers a webhook that webCRM calls at the target URL when a delivery is created, updated or deleted, and returns the assigned hook ID. Send 0 as the ID for a new hook. |
| Create Delivery Linked Data Item | `createDeliveryLinkedDataItem` | Creates a linked data item for deliveries in webCRM and returns the assigned ID. Send 0 as the ID for a new item. |
| Create Document | `createDocument` | Adds a new document record to webCRM and returns the assigned ID. The file content is sent Base64-encoded in the File field. |
| Create Document Hook | `createDocumentHook` | Registers a webhook that webCRM calls at the target URL when a document is created or updated, and returns the assigned hook ID. Send 0 as the ID for a new hook. webCRM does not support the Delete event type for documents. |
| Create Event | `createEvent` | Adds a new calendar event to webCRM and returns the assigned ID. webCRM has no delete endpoint for events. |
| Create Event Hook | `createEventHook` | Registers a webhook that webCRM calls at the target URL when an event is created or updated, and returns the assigned hook ID. Send 0 as the ID for a new hook. webCRM does not support the Delete event type for events. |
| Create Event Linked Data Item | `createEventLinkedDataItem` | Creates a linked data item for events in webCRM and returns the assigned ID. Send 0 as the ID for a new item. |
| Create Meeting | `createMeeting` | Creates a new calendar meeting in webCRM for the given user. Set Send Invitations to true only if attendees should receive invitation emails. |
| Create Meeting Hook | `createMeetingHook` | Registers a webhook that webCRM calls at the target URL when a meeting is created, updated or deleted, and returns the assigned hook ID. Send 0 as the ID for a new hook. |
| Create Opportunity | `createOpportunity` | Adds a new opportunity to webCRM and returns the assigned ID. Send 0 as the opportunity ID. Requires an API user with write access to opportunities. |
| Create Opportunity Hook | `createOpportunityHook` | Registers a webhook that webCRM calls at the target URL when an opportunity is created, updated or deleted, and returns the assigned hook ID. Send 0 as the ID for a new hook. |
| Create Opportunity Linked Data Item | `createOpportunityLinkedDataItem` | Creates a linked data item for opportunities in webCRM and returns the assigned ID. Send 0 as the ID for a new item. |
| Create Organisation | `createOrganisation` | Adds a new organisation to webCRM and returns the assigned ID. |
| Create Organisation Hook | `createOrganisationHook` | Registers a webhook that webCRM calls at the target URL when an organisation is created, updated or deleted, and returns the assigned hook ID. Send 0 as the ID for a new hook. |
| Create Organisation Linked Data Item | `createOrganisationLinkedDataItem` | Creates a linked data item for organisations in webCRM and returns the assigned ID. Send 0 as the ID for a new item. |
| Create Person | `createPerson` | Adds a new person to webCRM and returns the assigned ID. Send 0 as PersonId and set PersonOrganisationId to the organisation the person belongs to. |
| Create Person Hook | `createPersonHook` | Registers a webhook that webCRM calls at the target URL when a person is created, updated or deleted, and returns the assigned hook ID. Send 0 as the ID for a new hook. |
| Create Person Linked Data Item | `createPersonLinkedDataItem` | Creates a linked data item for persons in webCRM and returns the assigned ID. Send 0 as the ID for a new item. |
| Create Price Group | `createPriceGroup` | Adds a new price group to webCRM and returns the assigned ID. |
| Create Product | `createProduct` | Adds a new product to webCRM and returns the assigned ID. |
| Create Product Hook | `createProductHook` | Registers a webhook that webCRM calls at the target URL when a product is created, updated or deleted, and returns the assigned hook ID. Send 0 as the ID for a new hook. |
| Create Product Linked Data Item | `createProductLinkedDataItem` | Creates a linked data item for products in webCRM and returns the assigned ID. Send 0 as the ID for a new item. |
| Create Punch Card | `createPunchCard` | Adds a new punch card (prepaid time or service card) to an organisation in webCRM and returns the assigned ID. webCRM has no delete endpoint for punch cards; deactivate a card instead. |
| Create Punch Entry | `createPunchEntry` | Adds a new punch entry (time registration) to a punch card in webCRM and returns the assigned ID. |
| Create Quotation Line | `createQuotationLine` | Adds a new quotation line to an opportunity in webCRM and returns the assigned ID. |
| Create Quotation Line Hook | `createQuotationLineHook` | Registers a webhook that webCRM calls at the target URL when a quotation line is created, updated or deleted, and returns the assigned hook ID. Send 0 as the ID for a new hook. |
| Create Quotation Line Linked Data Item | `createQuotationLineLinkedDataItem` | Creates a quotation line linked data item (catalogue item) in webCRM and returns the assigned ID. Send 0 as the ID for a new item. |
| Create Relation | `createRelation` | Adds a new relation (a link between persons and/or organisations) to webCRM and returns the assigned ID. Send 0 as RelationId for a new relation. |
| Create Relation Hook | `createRelationHook` | Registers a webhook that webCRM calls at the target URL when a relation is created, updated or deleted, and returns the assigned hook ID. Send 0 as the ID for a new hook. |
| Create Support Case | `createSupportCase` | Adds a new support case to webCRM and returns the assigned ID. Send 0 as SupportCaseId for a new case. |
| Create Support Case Email | `createSupportCaseEmail` | Adds an email record to a support case in webCRM and returns the assigned ID. |
| Create Support Case Hook | `createSupportCaseHook` | Registers a webhook that webCRM calls at the target URL when a support case is created, updated or deleted, and returns the assigned hook ID. Send 0 as the ID for a new hook. |
| Create Support Case Linked Data Item | `createSupportCaseLinkedDataItem` | Creates a linked data item for support cases in webCRM and returns the assigned ID. Send 0 as the ID for a new item. |
| Create User | `createUser` | Adds a new user to webCRM and returns the assigned ID. Creating a user can send an invitation email to the address given. |
| Create User Hook | `createUserHook` | Registers a webhook that webCRM calls at the target URL when a user is created, updated or deleted, and returns the assigned hook ID. Send 0 as the ID for a new hook. |
| Delete Activity Hook | `deleteActivityHook` | Deletes the activity webhook with the specified ID from webCRM. |
| Delete Activity Linked Data Item | `deleteActivityLinkedDataItem` | Deletes the activity linked data item with the specified ID from webCRM. |
| Delete All Activity Linked Data Items | `deleteAllActivityLinkedDataItems` | Deletes every linked data item for activities in webCRM. This cannot be undone. |
| Delete All B2C Person Linked Data Items | `deleteAllB2CPersonLinkedDataItems` | Deletes every linked data item for b2c persons in webCRM. This cannot be undone. |
| Delete All Delivery Linked Data Items | `deleteAllDeliveryLinkedDataItems` | Deletes every linked data item for deliveries in webCRM. This cannot be undone. |
| Delete All Event Linked Data Items | `deleteAllEventLinkedDataItems` | Deletes every linked data item for events in webCRM. This cannot be undone. |
| Delete All Opportunity Linked Data Items | `deleteAllOpportunityLinkedDataItems` | Deletes every linked data item for opportunities in webCRM. This cannot be undone. |
| Delete All Organisation Linked Data Items | `deleteAllOrganisationLinkedDataItems` | Deletes every linked data item for organisations in webCRM. This cannot be undone. |
| Delete All Person Linked Data Items | `deleteAllPersonLinkedDataItems` | Deletes every linked data item for persons in webCRM. This cannot be undone. |
| Delete All Product Linked Data Items | `deleteAllProductLinkedDataItems` | Deletes every linked data item for products in webCRM. This cannot be undone. |
| Delete All Quotation Line Linked Data Items | `deleteAllQuotationLineLinkedDataItems` | Deletes every quotation line linked data item (catalogue item) in webCRM. This cannot be undone. |
| Delete All Support Case Linked Data Items | `deleteAllSupportCaseLinkedDataItems` | Deletes every linked data item for support cases in webCRM. This cannot be undone. |
| Delete B2C Person Hook | `deleteB2CPersonHook` | Deletes the b2c person webhook with the specified ID from webCRM. |
| Delete B2C Person Linked Data Item | `deleteB2CPersonLinkedDataItem` | Deletes the b2c person linked data item with the specified ID from webCRM. |
| Delete Delivery Hook | `deleteDeliveryHook` | Deletes the delivery webhook with the specified ID from webCRM. |
| Delete Delivery Linked Data Item | `deleteDeliveryLinkedDataItem` | Deletes the delivery linked data item with the specified ID from webCRM. |
| Delete Document | `deleteDocument` | Deletes the document with the specified ID from webCRM. |
| Delete Document Hook | `deleteDocumentHook` | Deletes the document webhook with the specified ID from webCRM. |
| Delete Event Hook | `deleteEventHook` | Deletes the event webhook with the specified ID from webCRM. |
| Delete Event Linked Data Item | `deleteEventLinkedDataItem` | Deletes the event linked data item with the specified ID from webCRM. |
| Delete Meeting | `deleteMeeting` | Deletes a meeting, or one occurrence of a recurring meeting when Start Time is given, in webCRM. |
| Delete Meeting Hook | `deleteMeetingHook` | Deletes the meeting webhook with the specified ID from webCRM. |
| Delete Newest Activity Note | `deleteNewestActivityNote` | Removes the newest note from an activity in webCRM. |
| Delete Opportunity Hook | `deleteOpportunityHook` | Deletes the opportunity webhook with the specified ID from webCRM. |
| Delete Opportunity Linked Data Item | `deleteOpportunityLinkedDataItem` | Deletes the opportunity linked data item with the specified ID from webCRM. |
| Delete Organisation Hook | `deleteOrganisationHook` | Deletes the organisation webhook with the specified ID from webCRM. |
| Delete Organisation Linked Data Item | `deleteOrganisationLinkedDataItem` | Deletes the organisation linked data item with the specified ID from webCRM. |
| Delete Person Hook | `deletePersonHook` | Deletes the person webhook with the specified ID from webCRM. |
| Delete Person Linked Data Item | `deletePersonLinkedDataItem` | Deletes the person linked data item with the specified ID from webCRM. |
| Delete Product | `deleteProduct` | Deletes the product with the specified ID from webCRM. |
| Delete Product Hook | `deleteProductHook` | Deletes the product webhook with the specified ID from webCRM. |
| Delete Product Linked Data Item | `deleteProductLinkedDataItem` | Deletes the product linked data item with the specified ID from webCRM. |
| Delete Punch Entry | `deletePunchEntry` | Deletes the punch entry with the specified ID from webCRM. |
| Delete Quotation Line | `deleteQuotationLine` | Deletes the quotation line with the specified ID from webCRM. |
| Delete Quotation Line Hook | `deleteQuotationLineHook` | Deletes the quotation line webhook with the specified ID from webCRM. |
| Delete Quotation Line Linked Data Item | `deleteQuotationLineLinkedDataItem` | Deletes the quotation line linked data item (catalogue item) with the specified ID from webCRM. |
| Delete Relation Hook | `deleteRelationHook` | Deletes the relation webhook with the specified ID from webCRM. |
| Delete Support Case Hook | `deleteSupportCaseHook` | Deletes the support case webhook with the specified ID from webCRM. |
| Delete Support Case Linked Data Item | `deleteSupportCaseLinkedDataItem` | Deletes the support case linked data item with the specified ID from webCRM. |
| Delete User Hook | `deleteUserHook` | Deletes the user webhook with the specified ID from webCRM. |
| Download Document | `downloadDocument` | Downloads the file attached to the document with the specified ID in webCRM. The response is the raw file (application/octet-stream). |
| Exchange API Token for Access Token | `apiLogin` | Exchanges the connection's webCRM API token for a one-hour access token and a refresh token. The connector runs this automatically whenever webCRM rejects the current access token, so you rarely need to call it yourself. |
| Get Activity | `getActivity` | Returns the activity with the specified ID from webCRM. |
| Get Activity Hook | `getActivityHook` | Returns the activity webhook with the specified ID from webCRM. |
| Get Activity Linked Data Item | `getActivityLinkedDataItem` | Returns the activity linked data item with the specified ID from webCRM. |
| Get Activity Linked Data Setup | `getActivityLinkedDataSetup` | Returns the linked data setup (field labels and configuration) for activities in webCRM. |
| Get Authenticated User Info | `getAuthenticatedUserInfo` | Returns the user name, system ID and system name of the webCRM user the current access token belongs to. |
| Get B2C Person | `getB2CPerson` | Returns the b2c person with the specified ID from webCRM. |
| Get B2C Person Hook | `getB2CPersonHook` | Returns the b2c person webhook with the specified ID from webCRM. |
| Get B2C Person Linked Data Item | `getB2CPersonLinkedDataItem` | Returns the b2c person linked data item with the specified ID from webCRM. |
| Get B2C Person Linked Data Setup | `getB2CPersonLinkedDataSetup` | Returns the linked data setup (field labels and configuration) for b2c persons in webCRM. |
| Get Budget | `getBudget` | Returns the budget with the specified ID from webCRM, including its monthly revenue and gross margin targets. |
| Get Data Field Settings | `getDataFieldSettings` | Returns which optional data fields are enabled for each entity type in the webCRM account. |
| Get Delivery | `getDelivery` | Returns the delivery with the specified ID from webCRM. |
| Get Delivery Hook | `getDeliveryHook` | Returns the delivery webhook with the specified ID from webCRM. |
| Get Delivery Linked Data Item | `getDeliveryLinkedDataItem` | Returns the delivery linked data item with the specified ID from webCRM. |
| Get Delivery Linked Data Setup | `getDeliveryLinkedDataSetup` | Returns the linked data setup (field labels and configuration) for deliveries in webCRM. |
| Get Document | `getDocument` | Returns the document with the specified ID from webCRM. |
| Get Document Hook | `getDocumentHook` | Returns the document webhook with the specified ID from webCRM. |
| Get Event | `getEvent` | Returns the event with the specified ID from webCRM. |
| Get Event Hook | `getEventHook` | Returns the event webhook with the specified ID from webCRM. |
| Get Event Linked Data Item | `getEventLinkedDataItem` | Returns the event linked data item with the specified ID from webCRM. |
| Get Event Linked Data Setup | `getEventLinkedDataSetup` | Returns the linked data setup (field labels and configuration) for events in webCRM. |
| Get Feature Settings | `getFeatureSettings` | Returns the features enabled on the webCRM account. |
| Get Meeting | `getMeeting` | Returns the meeting with the specified ID from webCRM. For a recurring meeting, pass Start Time to get a specific occurrence. |
| Get Meeting Hook | `getMeetingHook` | Returns the meeting webhook with the specified ID from webCRM. |
| Get Milestone | `getMilestone` | Returns the delivery milestone with the specified ID from webCRM, including planned and actual hours and revenue. |
| Get Opportunity | `getOpportunity` | Returns the opportunity with the specified ID from webCRM. |
| Get Opportunity Hook | `getOpportunityHook` | Returns the opportunity webhook with the specified ID from webCRM. |
| Get Opportunity Linked Data Item | `getOpportunityLinkedDataItem` | Returns the opportunity linked data item with the specified ID from webCRM. |
| Get Opportunity Linked Data Setup | `getOpportunityLinkedDataSetup` | Returns the linked data setup (field labels and configuration) for opportunities in webCRM. |
| Get Organisation | `getOrganisation` | Returns the organisation with the specified ID from webCRM. |
| Get Organisation Hook | `getOrganisationHook` | Returns the organisation webhook with the specified ID from webCRM. |
| Get Organisation Linked Data Item | `getOrganisationLinkedDataItem` | Returns the organisation linked data item with the specified ID from webCRM. |
| Get Organisation Linked Data Setup | `getOrganisationLinkedDataSetup` | Returns the linked data setup (field labels and configuration) for organisations in webCRM. |
| Get Overview | `getOverview` | Returns the overview (saved report definition) with the specified ID from webCRM. |
| Get Person | `getPerson` | Returns the person with the specified ID from webCRM. |
| Get Person Hook | `getPersonHook` | Returns the person webhook with the specified ID from webCRM. |
| Get Person Linked Data Item | `getPersonLinkedDataItem` | Returns the person linked data item with the specified ID from webCRM. |
| Get Person Linked Data Setup | `getPersonLinkedDataSetup` | Returns the linked data setup (field labels and configuration) for persons in webCRM. |
| Get Price Group | `getPriceGroup` | Returns the price group with the specified ID from webCRM. |
| Get Product | `getProduct` | Returns the product with the specified ID from webCRM. |
| Get Product Hook | `getProductHook` | Returns the product webhook with the specified ID from webCRM. |
| Get Product Linked Data Item | `getProductLinkedDataItem` | Returns the product linked data item with the specified ID from webCRM. |
| Get Product Linked Data Setup | `getProductLinkedDataSetup` | Returns the linked data setup (field labels and configuration) for products in webCRM. |
| Get Punch Card | `getPunchCard` | Returns the punch card with the specified ID from webCRM, including its current balance. |
| Get Punch Entry | `getPunchEntry` | Returns the punch entry with the specified ID from webCRM. |
| Get Quotation Line | `getQuotationLine` | Returns the quotation line with the specified ID from webCRM. |
| Get Quotation Line Hook | `getQuotationLineHook` | Returns the quotation line webhook with the specified ID from webCRM. |
| Get Quotation Line Linked Data Item | `getQuotationLineLinkedDataItem` | Returns the quotation line linked data item (catalogue item) with the specified ID from webCRM. |
| Get Quotation Line Linked Data Item Prices | `getQuotationLineLinkedDataItemPrices` | Returns the prices of a quotation line linked data item (catalogue item) in webCRM, per price group and currency. Results are paginated: use Page and Size to walk through them. |
| Get Quotation Line Linked Data Setup | `getQuotationLineLinkedDataSetup` | Returns the quotation line linked data setup (labels, visible columns, pricing and layout configuration) in webCRM. |
| Get Relation | `getRelation` | Returns the relation with the specified ID from webCRM. |
| Get Relation Hook | `getRelationHook` | Returns the relation webhook with the specified ID from webCRM. |
| Get Revenue | `getRevenue` | Returns the revenue (opportunity revenue split by month) with the specified ID from webCRM. |
| Get Support Case | `getSupportCase` | Returns the support case with the specified ID from webCRM. |
| Get Support Case Email | `getSupportCaseEmail` | Returns the support case email with the specified ID from webCRM. |
| Get Support Case Hook | `getSupportCaseHook` | Returns the support case webhook with the specified ID from webCRM. |
| Get Support Case Linked Data Item | `getSupportCaseLinkedDataItem` | Returns the support case linked data item with the specified ID from webCRM. |
| Get Support Case Linked Data Setup | `getSupportCaseLinkedDataSetup` | Returns the linked data setup (field labels and configuration) for support cases in webCRM. |
| Get System Settings | `getSystemSettings` | Returns the system settings of the webCRM account, including locale formats, enabled features and enabled data fields. |
| Get Time Expense | `getTimeExpense` | Returns the time or expense registration with the specified ID from webCRM. |
| Get User | `getUser` | Returns the user with the specified ID from webCRM. Sensitive fields such as password and ticket are returned censored. |
| Get User Access Settings | `getUserAccessSettings` | Returns the access settings of the current webCRM user. |
| Get User Hook | `getUserHook` | Returns the user webhook with the specified ID from webCRM. |
| List Active Campaigns | `listActiveCampaigns` | Returns all active marketing campaigns from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Active Support Cases | `listActiveSupportCases` | Returns all support cases webCRM considers active. Results are paginated: use Page and Size to walk through them. |
| List Active Users | `listActiveUsers` | Returns all active users from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Activities | `listActivities` | Returns all activities from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Activities by Creation Date Range | `listActivitiesByCreationDateRange` | Returns all activities created in the given date range (startDate &lt;= created date &lt; endDate) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Activities by Organisation | `listActivitiesByOrganisation` | Returns all activities that belong to the given organisation from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Activities by Responsible | `listActivitiesByResponsible` | Returns all activities assigned to the given responsible user from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Activities by Status | `listActivitiesByStatus` | Returns all activities with the given status from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Activity Hooks | `listActivityHooks` | Returns the activity webhooks registered by the current API user in webCRM. |
| List Activity Linked Data Items | `listActivityLinkedDataItems` | Returns all linked data items for activities from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Activity Notes | `listActivityNotes` | Returns the notes of an activity from webCRM. Results are paginated: use Page and Size to walk through them. |
| List B2C Person Hooks | `listB2CPersonHooks` | Returns the b2c person webhooks registered by the current API user in webCRM. |
| List B2C Person Linked Data Items | `listB2CPersonLinkedDataItems` | Returns all linked data items for b2c persons from webCRM. Results are paginated: use Page and Size to walk through them. |
| List B2C Person Products | `listB2CPersonProducts` | Returns all products of the B2C person with the specified ID from webCRM. |
| List B2C Person Relations | `listB2CPersonRelations` | Returns all relations of the B2C person with the specified ID from webCRM. |
| List B2C Persons | `listB2CPersons` | Returns all b2c persons from webCRM. Results are paginated: use Page and Size to walk through them. |
| List B2C Persons by Organisation | `listB2CPersonsByOrganisation` | Returns the b2c persons that belong to the given organisation from webCRM. |
| List Budgets | `listBudgets` | Returns all budgets from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Currency Exchange Rates | `listCurrencyExchangeRates` | Returns the currency exchange rates configured in the webCRM account. |
| List Deliveries | `listDeliveries` | Returns all deliveries from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Deliveries by Creation Date Range | `listDeliveriesByCreationDateRange` | Returns all deliveries created in the given date range (startDate &lt;= created date &lt; endDate) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Deliveries by Organisation | `listDeliveriesByOrganisation` | Returns all deliveries that belong to the given organisation from webCRM. Results are paginated where supported. |
| List Deliveries by Responsible | `listDeliveriesByResponsible` | Returns all deliveries assigned to the given responsible user from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Deliveries by Secondary Responsible | `listDeliveriesBySecondaryResponsible` | Returns all deliveries where the given user is the second responsible user, from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Deliveries by Status | `listDeliveriesByStatus` | Returns all deliveries with the given status from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Delivery Hooks | `listDeliveryHooks` | Returns the delivery webhooks registered by the current API user in webCRM. |
| List Delivery Linked Data Items | `listDeliveryLinkedDataItems` | Returns all linked data items for deliveries from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Delivery Quotation Lines | `listDeliveryQuotationLines` | Returns all quotation lines of the delivery with the specified ID from webCRM. |
| List Document Hooks | `listDocumentHooks` | Returns the document webhooks registered by the current API user in webCRM. |
| List Documents | `listDocuments` | Returns all documents from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Documents by Entity | `listDocumentsByEntity` | Returns all documents attached to the given entity in webCRM. Results are paginated: use Page and Size to walk through them. |
| List Event Hooks | `listEventHooks` | Returns the event webhooks registered by the current API user in webCRM. |
| List Event Linked Data Items | `listEventLinkedDataItems` | Returns all linked data items for events from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Events | `listEvents` | Returns all events from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Events by Creation Date Range | `listEventsByCreationDateRange` | Returns all events created in the given date range (startDate &lt;= created date &lt; endDate) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Events by Organisation | `listEventsByOrganisation` | Returns all events that belong to the given organisation from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Events by Responsible | `listEventsByResponsible` | Returns all events assigned to the given responsible user from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Events by Status | `listEventsByStatus` | Returns all events with the given status from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Fields Metadata | `listFieldsMetadata` | Returns metadata (labels, display types, lengths and dropdown values) for every field of every entity type in webCRM. |
| List Fields Metadata by Entity Types | `listFieldsMetadataByEntityTypes` | Returns field metadata (labels, display types, lengths and dropdown values) for the given entity type in webCRM. |
| List Meeting Hooks | `listMeetingHooks` | Returns the meeting webhooks registered by the current API user in webCRM. |
| List Meetings | `listMeetings` | Returns the meetings of a user within the given time window from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Meetings by Organisation | `listMeetingsByOrganisation` | Returns the meetings connected to an organisation within the given time window from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Meetings by Update Time | `listMeetingsByUpdateTime` | Returns the meetings updated within the given time window from webCRM, optionally for a specific user. Results are paginated: use Page and Size to walk through them. |
| List Meetings by Users | `listMeetingsByUsers` | Returns the meetings of the given users within a time window from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Milestones | `listMilestones` | Returns all delivery milestones from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Opportunities | `listOpportunities` | Returns all opportunities from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Opportunities by Creation Date Range | `listOpportunitiesByCreationDateRange` | Returns all opportunities created in the given date range (start date inclusive, end date exclusive) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Opportunities by Organisation | `listOpportunitiesByOrganisation` | Returns all opportunities that belong to the given organisation from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Opportunities by Pipeline Level | `listOpportunitiesByPipelineLevel` | Returns all opportunities at the given pipeline level from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Opportunities by Responsible | `listOpportunitiesByResponsible` | Returns all opportunities whose primary responsible user is the given user from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Opportunities by Secondary Responsible | `listOpportunitiesBySecondaryResponsible` | Returns all opportunities whose secondary responsible user is the given user from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Opportunity Hooks | `listOpportunityHooks` | Returns the opportunity webhooks registered by the current API user in webCRM. |
| List Opportunity Linked Data Items | `listOpportunityLinkedDataItems` | Returns all linked data items for opportunities from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Opportunity Quotation Lines | `listOpportunityQuotationLines` | Returns all quotation lines of the opportunity with the specified ID from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Opportunity Revenues | `listOpportunityRevenues` | Returns all revenue entries of the opportunity with the specified ID from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Organisation Events | `listOrganisationEvents` | Returns all events of the organisation with the specified ID from webCRM. |
| List Organisation Hooks | `listOrganisationHooks` | Returns the organisation webhooks registered by the current API user in webCRM. |
| List Organisation Linked Data Items | `listOrganisationLinkedDataItems` | Returns all linked data items for organisations from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Organisation Persons | `listOrganisationPersons` | Returns all persons of the organisation with the specified ID from webCRM. |
| List Organisation Products | `listOrganisationProducts` | Returns all products of the organisation with the specified ID from webCRM. |
| List Organisation Relations | `listOrganisationRelations` | Returns all relations of the organisation with the specified ID from webCRM. |
| List Organisation Revenues | `listOrganisationRevenues` | Returns all revenues of the organisation with the specified ID from webCRM. |
| List Organisation Support Cases | `listOrganisationSupportCases` | Returns all support cases of the organisation with the specified ID from webCRM. |
| List Organisations | `listOrganisations` | Returns all organisations from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Organisations by Creation Date Range | `listOrganisationsByCreationDateRange` | Returns all organisations created in the given date range (startDate &lt;= created date &lt; endDate) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Organisations by Update Date Range | `listOrganisationsByUpdateDateRange` | Returns all organisations updated in the given date range (startDate &lt;= updated date &lt; endDate) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Overviews | `listOverviews` | Returns all overviews (saved report definitions) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Overviews by Data Type | `listOverviewsByDataType` | Returns the overviews (saved report definitions) of the given data type from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Person Hooks | `listPersonHooks` | Returns the person webhooks registered by the current API user in webCRM. |
| List Person Linked Data Items | `listPersonLinkedDataItems` | Returns all linked data items for persons from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Person Relations | `listPersonRelations` | Returns all relations of the person with the specified ID from webCRM. |
| List Persons | `listPersons` | Returns all persons from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Persons by Organisation | `listPersonsByOrganisation` | Returns all persons that belong to the given organisation from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Persons by Update Date Range | `listPersonsByUpdateDateRange` | Returns all persons updated in the given date range (startDate &lt;= updated date &lt; endDate) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Pipelines | `listPipelines` | Returns all opportunity pipeline levels configured in webCRM. |
| List Price Group Own Prices | `listPriceGroupOwnPrices` | Returns only the prices configured for exactly this price group (group 0 is the default group) in webCRM, excluding inherited prices. |
| List Price Group Prices | `listPriceGroupPrices` | Returns all prices configured for the price group with the specified ID in webCRM, including prices inherited from its base group. |
| List Price Groups | `listPriceGroups` | Returns all price groups from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Product Hooks | `listProductHooks` | Returns the product webhooks registered by the current API user in webCRM. |
| List Product Linked Data Items | `listProductLinkedDataItems` | Returns all linked data items for products from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Products | `listProducts` | Returns all products from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Products by Organisation | `listProductsByOrganisation` | Returns all products of the given organisation from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Punch Cards | `listPunchCards` | Returns all punch cards (prepaid time or service cards) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Punch Entries | `listPunchEntries` | Returns all punch entries (time registrations on punch cards) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Punch Entries by Punch Card | `listPunchEntriesByPunchCard` | Returns all punch entries of the given punch card from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Quotation Line Hooks | `listQuotationLineHooks` | Returns the quotation line webhooks registered by the current API user in webCRM. |
| List Quotation Line Linked Data Items | `listQuotationLineLinkedDataItems` | Returns all linked data items (catalogue items) for quotation lines from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Quotation Lines | `listQuotationLines` | Returns all quotation lines from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Relation Hooks | `listRelationHooks` | Returns the relation webhooks registered by the current API user in webCRM. |
| List Relations | `listRelations` | Returns all relations (links between persons and/or organisations) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Revenues | `listRevenues` | Returns all revenues (opportunity revenue split by month) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Support Case Emails | `listSupportCaseEmails` | Returns all support case emails from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Support Case Emails by Support Case | `listSupportCaseEmailsBySupportCase` | Returns all emails that belong to the given support case in webCRM. Results are paginated: use Page and Size to walk through them. |
| List Support Case Hooks | `listSupportCaseHooks` | Returns the support case webhooks registered by the current API user in webCRM. |
| List Support Case Linked Data Items | `listSupportCaseLinkedDataItems` | Returns all linked data items for support cases from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Support Cases | `listSupportCases` | Returns all support cases from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Support Cases by Channel | `listSupportCasesByChannel` | Returns all support cases received through the given channel from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Support Cases by Creation Date Range | `listSupportCasesByCreationDateRange` | Returns all support cases created in the given date range (startDate &lt;= created date &lt; endDate) from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Support Cases by Organisation | `listSupportCasesByOrganisation` | Returns all support cases that belong to the given organisation from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Support Cases by Responsible | `listSupportCasesByResponsible` | Returns all support cases assigned to the given responsible user from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Support Cases by Status | `listSupportCasesByStatus` | Returns all support cases with the given status from webCRM. Results are paginated: use Page and Size to walk through them. |
| List Time Expenses | `listTimeExpenses` | Returns all time and expense registrations from webCRM. Results are paginated: use Page and Size to walk through them. |
| List User Activities | `listUserActivities` | Returns all activities of the user with the specified ID from webCRM. Results are paginated: use Page and Size to walk through them. |
| List User Events | `listUserEvents` | Returns all events of the user with the specified ID from webCRM. Results are paginated: use Page and Size to walk through them. |
| List User Hooks | `listUserHooks` | Returns the user webhooks registered by the current API user in webCRM. |
| List Users | `listUsers` | Returns all users from webCRM. Results are paginated: use Page and Size to walk through them. |
| List VAT Codes | `listVATCodes` | Returns all VAT codes configured in webCRM. |
| List VAT Groups | `listVATGroups` | Returns all VAT groups configured in webCRM. |
| List VAT Values | `listVATValues` | Returns all non-zero VAT values (the VAT percentage table) configured in webCRM. |
| Log In With Publish Code | `logInWithPublishCode` | Exchanges a webCRM publish code, login name and password for an access token. webCRM reports failed logins in the IsError and Error fields. |
| Log In With User Credentials | `logInWithUserCredentials` | Exchanges a webCRM database code, user name and password for an access token. Most integrations should use the API token exchange instead. webCRM reports failed logins in the IsError and Error fields. |
| Manage Quotation Line Linked Data Item Prices | `manageQuotationLineLinkedDataItemPrices` | Creates, updates or deletes prices of quotation line linked data items in webCRM. Send a price ID of 0 to create a price; a non-zero ID with a value updates it; a non-zero ID without a value deletes it so future lines use the auto-calculated price. |
| Merge Persons | `mergePersons` | Merges the person with the specified ID into the destination person in webCRM. The source person is removed after the merge, so this cannot be undone. |
| Move Activity to Organisation | `moveActivityToOrganisation` | Moves the activity to another organisation in webCRM. |
| Move Delivery to Organisation | `moveDeliveryToOrganisation` | Moves the delivery to another organisation in webCRM. |
| Move Opportunity to Organisation | `moveOpportunityToOrganisation` | Moves the opportunity with the specified ID to another organisation in webCRM. |
| Move Person to Organisation | `movePersonToOrganisation` | Moves the person to another organisation in webCRM. |
| Refresh API Access Token | `refreshAPIAccessToken` | Refreshes an access token that was issued from an API token, using the refresh token returned by the token exchange. webCRM reports failures in the IsError and Error fields. |
| Refresh CRM Access Token | `refreshCRMAccessToken` | Refreshes an access token that was issued from a CRM login, using the refresh token returned by that login. webCRM reports failures in the IsError and Error fields. |
| Replace VAT Codes | `replaceVATCodes` | Saves the submitted list as the complete set of VAT codes in webCRM, overriding all existing codes. Sending an empty list removes every code. |
| Replace VAT Groups | `replaceVATGroups` | Saves the submitted list as the complete set of VAT groups in webCRM, overriding all existing groups. Sending an empty list removes every group. |
| Replace VAT Values | `replaceVATValues` | Saves the submitted list as the complete VAT percentage table in webCRM, overriding all existing values. Sending an empty list removes every value. |
| Run Overview Report | `runOverviewReport` | Runs the overview (saved report) with the specified ID in webCRM and returns its result rows. Results are paginated: use Page and Size to walk through them. |
| Run Query | `runQuery` | Runs a read-only webCRM query script and returns the result rows. Results are paginated: use Page and Size to walk through them. |
| Search Persons | `searchPersons` | Returns all persons whose full name matches the given text in webCRM. |
| Update Activity | `updateActivity` | Updates the activity with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update Activity Hook | `updateActivityHook` | Updates the activity webhook with the specified ID in webCRM. |
| Update Activity Linked Data Item | `updateActivityLinkedDataItem` | Updates the activity linked data item with the specified ID in webCRM. |
| Update B2C Person | `updateB2CPerson` | Updates the b2c person with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update B2C Person Hook | `updateB2CPersonHook` | Updates the b2c person webhook with the specified ID in webCRM. |
| Update B2C Person Linked Data Item | `updateB2CPersonLinkedDataItem` | Updates the b2c person linked data item with the specified ID in webCRM. |
| Update Delivery | `updateDelivery` | Updates the delivery with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update Delivery Hook | `updateDeliveryHook` | Updates the delivery webhook with the specified ID in webCRM. |
| Update Delivery Linked Data Item | `updateDeliveryLinkedDataItem` | Updates the delivery linked data item with the specified ID in webCRM. |
| Update Document | `updateDocument` | Updates the document with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update Document Hook | `updateDocumentHook` | Updates the document webhook with the specified ID in webCRM. |
| Update Event | `updateEvent` | Updates the event with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update Event Hook | `updateEventHook` | Updates the event webhook with the specified ID in webCRM. |
| Update Event Linked Data Item | `updateEventLinkedDataItem` | Updates the event linked data item with the specified ID in webCRM. |
| Update Meeting | `updateMeeting` | Updates an existing calendar meeting in webCRM. Use Send Updates to control whether attendees are notified. |
| Update Meeting Connections | `updateMeetingConnections` | Replaces the activities and opportunities connected to a meeting in webCRM. |
| Update Meeting Hook | `updateMeetingHook` | Updates the meeting webhook with the specified ID in webCRM. |
| Update Opportunity | `updateOpportunity` | Updates the opportunity with the specified ID in webCRM. webCRM replaces the record, so send every field you want to keep. Requires an API user with write access to opportunities. |
| Update Opportunity Hook | `updateOpportunityHook` | Updates the opportunity webhook with the specified ID in webCRM. |
| Update Opportunity Linked Data Item | `updateOpportunityLinkedDataItem` | Updates the opportunity linked data item with the specified ID in webCRM. |
| Update Organisation | `updateOrganisation` | Updates the organisation with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update Organisation Hook | `updateOrganisationHook` | Updates the organisation webhook with the specified ID in webCRM. |
| Update Organisation Linked Data Item | `updateOrganisationLinkedDataItem` | Updates the organisation linked data item with the specified ID in webCRM. |
| Update Person | `updatePerson` | Updates the person with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update Person Hook | `updatePersonHook` | Updates the person webhook with the specified ID in webCRM. |
| Update Person Linked Data Item | `updatePersonLinkedDataItem` | Updates the person linked data item with the specified ID in webCRM. |
| Update Price Group | `updatePriceGroup` | Updates the price group with the specified ID in webCRM. The price group ID in the body must match the ID in the path. |
| Update Product | `updateProduct` | Updates the product with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update Product Hook | `updateProductHook` | Updates the product webhook with the specified ID in webCRM. |
| Update Product Linked Data Item | `updateProductLinkedDataItem` | Updates the product linked data item with the specified ID in webCRM. |
| Update Punch Card | `updatePunchCard` | Updates the punch card with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update Punch Entry | `updatePunchEntry` | Updates the punch entry with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update Quotation Line | `updateQuotationLine` | Updates the quotation line with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update Quotation Line Hook | `updateQuotationLineHook` | Updates the quotation line webhook with the specified ID in webCRM. |
| Update Quotation Line Linked Data Item | `updateQuotationLineLinkedDataItem` | Updates the quotation line linked data item (catalogue item) with the specified ID in webCRM. |
| Update Relation | `updateRelation` | Updates the relation with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update Relation Hook | `updateRelationHook` | Updates the relation webhook with the specified ID in webCRM. |
| Update Support Case | `updateSupportCase` | Updates the support case with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update Support Case Hook | `updateSupportCaseHook` | Updates the support case webhook with the specified ID in webCRM. |
| Update Support Case Linked Data Item | `updateSupportCaseLinkedDataItem` | Updates the support case linked data item with the specified ID in webCRM. |
| Update User | `updateUser` | Updates the user with the specified ID in webCRM. Send the fields you want to store on the record. |
| Update User Hook | `updateUserHook` | Updates the user webhook with the specified ID in webCRM. |
| Upsert Activities | `upsertActivities` | Updates or inserts the submitted activities in webCRM. Returns assigned IDs for inserted activities and error messages if insert/update fails. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert B2C Persons | `upsertB2CPersons` | Updates or inserts the submitted b2c persons in webCRM. Records with a PersonB2CId of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Deliveries | `upsertDeliveries` | Updates or inserts the submitted deliveries in webCRM. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Documents | `upsertDocuments` | Updates or inserts the submitted documents in webCRM. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Events | `upsertEvents` | Updates or inserts the submitted events in webCRM. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Opportunities | `upsertOpportunities` | Updates or inserts the submitted opportunities in webCRM. Records with an ID of 0 are inserted and others are updated. Returns one string per record with the assigned ID or an error message; webCRM answers HTTP 200 even when individual records fail, so check each returned string. |
| Upsert Organisations | `upsertOrganisations` | Updates or inserts the submitted organisations in webCRM. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Persons | `upsertPersons` | Updates or inserts the submitted persons in webCRM. Records with a PersonId of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Price Groups | `upsertPriceGroups` | Updates or inserts the submitted price groups in webCRM. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Products | `upsertProducts` | Updates or inserts the submitted products in webCRM. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Punch Cards | `upsertPunchCards` | Updates or inserts the submitted punch cards in webCRM. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Punch Entries | `upsertPunchEntries` | Updates or inserts the submitted punch entries in webCRM. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Quotation Lines | `upsertQuotationLines` | Updates or inserts the submitted quotation lines in webCRM. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Relations | `upsertRelations` | Updates or inserts the submitted relations in webCRM. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Support Cases | `upsertSupportCases` | Updates or inserts the submitted support cases in webCRM. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |
| Upsert Users | `upsertUsers` | Updates or inserts the submitted users in webCRM. Records with an ID of 0 are inserted and others are updated. webCRM answers HTTP 200 even when individual records fail, so check each returned string for an error message. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Activity Created | `activityCreated` | Fires when an activity is created in webCRM (Activities/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Activity Deleted | `activityDeleted` | Fires when an activity is deleted in webCRM (Activities/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Activity Updated | `activityUpdated` | Fires when an activity is updated in webCRM (Activities/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| B2C Person Created | `b2cPersonCreated` | Fires when a B2C person is created in webCRM (PersonsB2C/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| B2C Person Deleted | `b2cPersonDeleted` | Fires when a B2C person is deleted in webCRM (PersonsB2C/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| B2C Person Updated | `b2cPersonUpdated` | Fires when a B2C person is updated in webCRM (PersonsB2C/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Delivery Created | `deliveryCreated` | Fires when a delivery is created in webCRM (Deliveries/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Delivery Deleted | `deliveryDeleted` | Fires when a delivery is deleted in webCRM (Deliveries/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Delivery Updated | `deliveryUpdated` | Fires when a delivery is updated in webCRM (Deliveries/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Document Created | `documentCreated` | Fires when a document is created in webCRM (Documents/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Document Deleted | `documentDeleted` | Fires when a document is deleted in webCRM (Documents/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Document Updated | `documentUpdated` | Fires when a document is updated in webCRM (Documents/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Event Created | `eventCreated` | Fires when an event is created in webCRM (Events/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Event Deleted | `eventDeleted` | Fires when an event is deleted in webCRM (Events/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Event Updated | `eventUpdated` | Fires when an event is updated in webCRM (Events/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Meeting Created | `meetingCreated` | Fires when a meeting is created in webCRM (Meetings/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Meeting Deleted | `meetingDeleted` | Fires when a meeting is deleted in webCRM (Meetings/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Meeting Updated | `meetingUpdated` | Fires when a meeting is updated in webCRM (Meetings/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Opportunity Created | `opportunityCreated` | Fires when an opportunity is created in webCRM (Opportunities/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Opportunity Deleted | `opportunityDeleted` | Fires when an opportunity is deleted in webCRM (Opportunities/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Opportunity Updated | `opportunityUpdated` | Fires when an opportunity is updated in webCRM (Opportunities/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Organisation Created | `organisationCreated` | Fires when an organisation is created in webCRM (Organisations/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Organisation Deleted | `organisationDeleted` | Fires when an organisation is deleted in webCRM (Organisations/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Organisation Updated | `organisationUpdated` | Fires when an organisation is updated in webCRM (Organisations/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Person Created | `personCreated` | Fires when a person is created in webCRM (Persons/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Person Deleted | `personDeleted` | Fires when a person is deleted in webCRM (Persons/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Person Updated | `personUpdated` | Fires when a person is updated in webCRM (Persons/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Product Created | `productCreated` | Fires when a product is created in webCRM (Products/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Product Deleted | `productDeleted` | Fires when a product is deleted in webCRM (Products/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Product Updated | `productUpdated` | Fires when a product is updated in webCRM (Products/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Quotation Line Created | `quotationLineCreated` | Fires when a quotation line is created in webCRM (QuotationLines/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Quotation Line Deleted | `quotationLineDeleted` | Fires when a quotation line is deleted in webCRM (QuotationLines/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Quotation Line Updated | `quotationLineUpdated` | Fires when a quotation line is updated in webCRM (QuotationLines/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Relation Created | `relationCreated` | Fires when a relation is created in webCRM (Relations/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Relation Deleted | `relationDeleted` | Fires when a relation is deleted in webCRM (Relations/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Relation Updated | `relationUpdated` | Fires when a relation is updated in webCRM (Relations/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Support Case Created | `supportCaseCreated` | Fires when a support case is created in webCRM (SupportCases/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Support Case Deleted | `supportCaseDeleted` | Fires when a support case is deleted in webCRM (SupportCases/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| Support Case Updated | `supportCaseUpdated` | Fires when a support case is updated in webCRM (SupportCases/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| User Created | `userCreated` | Fires when a user is created in webCRM (Users/Hooks with EventType Create). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| User Deleted | `userDeleted` | Fires when a user is deleted in webCRM (Users/Hooks with EventType Delete). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
| User Updated | `userUpdated` | Fires when a user is updated in webCRM (Users/Hooks with EventType Update). webCRM does not publish the delivery payload, so the schema stays open until a real delivery is captured. |
