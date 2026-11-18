---
description: "Act!"
hidden: true
---

# Act! CRM

<img src="../../.gitbook/assets/connectors/lg/act-crm.png" alt="Act! CRM logo">

Act! CRM (Act! Premium Cloud and Act! Premium Web) via the Act! Web API. Manage contacts, companies, groups, opportunities, activities, history, notes, products, users, teams, documents and metadata in an Act! database.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [act.com](https://act.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `actCrm` |

## Use it

Add Act! CRM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.actCrm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contact To Group | `addContactToGroup` | Adds a single contact to a group. |
| Add Contact To Groups | `addContactToGroups` | Adds a contact to a list of groups. |
| Add Contact To Single Group | `addContactToSingleGroup` | Adds a contact to a single group, addressed from the contact. |
| Add Contacts To Group | `addContactsToGroup` | Adds a list of contacts to a group. |
| Add CORS Origin | `addCorsOrigin` | Adds an origin to the CORS configuration of the Act! Web API (web.customer.config). |
| Associate Companies With Contact | `associateCompaniesWithContact` | Associates a list of companies with a contact. |
| Associate Companies With Opportunity | `associateCompaniesWithOpportunity` | Associates a list of companies with an opportunity. |
| Associate Company With Contact | `associateCompanyWithContact` | Associates a single company with a contact. |
| Associate Company With Opportunity | `associateCompanyWithOpportunity` | Associates a single company with an opportunity. |
| Associate Contact With Company | `associateContactWithCompany` | Associates a single contact with a company. |
| Associate Contact With History | `associateContactWithHistory` | Associates a contact with a history item if it is not already associated. |
| Associate Contact With Note | `associateContactWithNote` | Associates a contact with a note if it is not already associated. |
| Associate Contact With Opportunity | `associateContactWithOpportunity` | Associates a single contact with an opportunity. |
| Associate Contacts With Company | `associateContactsWithCompany` | Associates a list of contacts with a company. |
| Associate Contacts With Opportunity | `associateContactsWithOpportunity` | Associates a list of contacts with an opportunity. |
| Associate Group With Opportunity | `associateGroupWithOpportunity` | Associates a single group with an opportunity. |
| Associate Groups With Opportunity | `associateGroupsWithOpportunity` | Associates a list of groups with an opportunity. |
| Associate Opportunities With Company | `associateOpportunitiesWithCompany` | Associates a list of opportunities with a company. |
| Associate Opportunities With Contact | `associateOpportunitiesWithContact` | Associates a list of opportunities with a contact. |
| Associate Opportunities With Group | `associateOpportunitiesWithGroup` | Associates a list of opportunities with a group. |
| Associate Opportunity With Company | `associateOpportunityWithCompany` | Associates a single opportunity with a company. |
| Associate Opportunity With Contact | `associateOpportunityWithContact` | Associates a single opportunity with a contact. |
| Associate Opportunity With Group | `associateOpportunityWithGroup` | Associates a single opportunity with a group. |
| Associate Task With Contact | `associateTaskWithContact` | Associates a task with a contact if it is not already associated. |
| Clear All Task Alarms | `clearAllTaskAlarms` | Clears all alarms of the current user. |
| Clear Single Task Alarm | `clearSingleTaskAlarm` | Clears the alarm of a single task, addressed by its 44-character occurrence id or series id. |
| Clear Task | `clearTask` | Clears (completes) a task and records the result to history. |
| Clear Task Alarms | `clearTaskAlarms` | Clears the alarms of the specified activities. |
| Clear Tasks | `clearTasks` | Clears (completes) a list of tasks and records the result to history. |
| Convert Contact To User | `convertContactToUser` | Converts an existing contact into an Act! user (consumes a user licence on Act! Premium Cloud). |
| Convert Opportunity Filter To Criteria | `convertOpportunityFilterToCriteria` | Converts an OData filter into dynamic list criteria JSON for use with Preview Dynamic Opportunity List. |
| Create Activity Series | `createActivitySeries` | Creates a new recurring activity series. |
| Create Calendar Preferences | `createCalendarPreferences` | Creates calendar preferences for the current user. |
| Create Company | `createCompany` | Creates a new company in the Act! database. |
| Create Contact | `createContact` | Creates a new contact in the Act! database. |
| Create Custom Entity Record | `createCustomEntityRecord` | Creates a record in a custom table (custom entity) from a JSON object of field values. |
| Create Custom Table | `createCustomTable` | Creates a custom table (custom entity), optionally linked to parent entities. |
| Create Database | `createDatabase` | Creates a new Act! database on the server. |
| Create Database Backup | `createDatabaseBackup` | Starts a new backup of the database using the supplied database administrator credentials. |
| Create Demo Data | `createDemoData` | Populates the database with Act! demo data. |
| Create Document | `createDocument` | Creates a new history document record; upload its file afterwards with Upload Document Attachment. |
| Create Drop-Down List | `createDropDownList` | Creates a new drop-down list definition. |
| Create Group | `createGroup` | Creates a new group. |
| Create History | `createHistory` | Creates a new history item (a record of a call, meeting, email or other interaction) linked to contacts, companies, groups or opportunities. |
| Create Marketing Automation Email | `createMarketingAutomationEmail` | Records an Act! Marketing Automation email event (send, open, click, bounce) for a campaign and its contacts. |
| Create Note | `createNote` | Creates a new note linked to contacts, companies, groups or opportunities. |
| Create Opportunity | `createOpportunity` | Creates a new opportunity in a sales process stage, linked to contacts, companies or groups. |
| Create Opportunity Process | `createOpportunityProcess` | Creates a new opportunity sales process with its stages. |
| Create Opportunity Product | `createOpportunityProduct` | Adds a product line to an opportunity. |
| Create Process Stage | `createProcessStage` | Creates a new stage in an opportunity sales process. |
| Create Product | `createProduct` | Creates a new product in the product catalogue. |
| Create Record Type Field | `createRecordTypeField` | Creates a custom field on a record type. |
| Create Recurring Task | `createRecurringTask` | Creates a new recurring task series. |
| Create Secondary Contact | `createSecondaryContact` | Creates a secondary contact (an assistant or alternate person) under a contact. |
| Create Task | `createTask` | Creates a new task (call, meeting, to-do or other activity) scheduled with contacts; any recurrence specification is ignored. |
| Create Task For User | `createTaskForUser` | Creates a task scheduled for another Act! user (Schedule For). |
| Create Task Type | `createTaskType` | Creates a custom task type. |
| Create Team | `createTeam` | Creates a new team of Act! users. |
| Create User | `createUser` | Creates a new Act! user (consumes a user licence on Act! Premium Cloud). |
| Create User Preference | `createUserPreference` | Creates or updates a preference of the current user. |
| Create Webhook | `createWebhook` | Registers a webhook that posts notifications to a callback URL when records are created or updated, or when activity alarms sound (Act! Premium Web / on-premise Web API; not available on Act! Premium Cloud). |
| Delete Activity Attachment | `deleteActivityAttachment` | Deletes the attachment of an activity. |
| Delete Activity Series | `deleteActivitySeries` | Deletes a recurring activity series. |
| Delete Company | `deleteCompany` | Deletes a company from the Act! database. |
| Delete Contact | `deleteContact` | Deletes a contact from the Act! database. |
| Delete Contact Note | `deleteContactNote` | Deletes a note that belongs to a contact. |
| Delete Custom Entity Record | `deleteCustomEntityRecord` | Deletes a record of a custom table (custom entity). |
| Delete Custom Table | `deleteCustomTable` | Deletes a custom table (custom entity), including its parent links and data. |
| Delete Database Backup | `deleteDatabaseBackup` | Deletes a database backup file. |
| Delete Demo Data | `deleteDemoData` | Removes the Act! demo data from the database. |
| Delete Document | `deleteDocument` | Deletes a history document. |
| Delete Document Attachment | `deleteDocumentAttachment` | Deletes the file of a history document. |
| Delete Drop-Down List | `deleteDropDownList` | Deletes a drop-down list definition. |
| Delete Group | `deleteGroup` | Deletes a group. |
| Delete History | `deleteHistory` | Deletes a history item. |
| Delete History Attachment | `deleteHistoryAttachment` | Deletes the attachment of a history item. |
| Delete Insight View Definition | `deleteInsightViewDefinition` | Deletes the current user's Insight analytics view definition. |
| Delete MyAct View Definition | `deleteMyActViewDefinition` | Deletes the current user's MyAct analytics view definition. |
| Delete Note | `deleteNote` | Deletes a note. |
| Delete Note Attachment | `deleteNoteAttachment` | Deletes the attachment of a note. |
| Delete Opportunity | `deleteOpportunity` | Deletes an opportunity. |
| Delete Opportunity Process | `deleteOpportunityProcess` | Deletes an opportunity sales process. |
| Delete Opportunity Product | `deleteOpportunityProduct` | Removes a product line from an opportunity. |
| Delete Opportunity Stage | `deleteOpportunityStage` | Deletes an opportunity stage. |
| Delete Phone Number Mask | `deletePhoneNumberMask` | Deletes a phone number format mask. |
| Delete Product | `deleteProduct` | Deletes a product from the product catalogue. |
| Delete Record Type Field | `deleteRecordTypeField` | Deletes a custom field of a record type. |
| Delete Recurring Task | `deleteRecurringTask` | Deletes a recurring task series. |
| Delete Secondary Contact | `deleteSecondaryContact` | Deletes a secondary contact of a contact. |
| Delete Task | `deleteTask` | Deletes a task. |
| Delete Task Type | `deleteTaskType` | Deletes a custom task type. |
| Delete Tasks | `deleteTasks` | Deletes a list of tasks. |
| Delete Team | `deleteTeam` | Deletes a team. |
| Delete User | `deleteUser` | Deletes an Act! user, optionally reassigning its records to another user and removing its contact record. |
| Delete User Preference | `deleteUserPreference` | Deletes a preference of the current user. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook registration. |
| Dissociate Companies From Contact | `dissociateCompaniesFromContact` | Removes the association between a contact and a list of companies. |
| Dissociate Companies From Opportunity | `dissociateCompaniesFromOpportunity` | Removes the association between an opportunity and a list of companies. |
| Dissociate Company From Contact | `dissociateCompanyFromContact` | Removes the association between a contact and a company. |
| Dissociate Company From Opportunity | `dissociateCompanyFromOpportunity` | Removes the association between an opportunity and a company. |
| Dissociate Contact From Company | `dissociateContactFromCompany` | Removes the association between a company and a contact. |
| Dissociate Contact From History | `dissociateContactFromHistory` | Removes a contact from a history item. |
| Dissociate Contact From Note | `dissociateContactFromNote` | Removes a contact from a note. |
| Dissociate Contact From Opportunity | `dissociateContactFromOpportunity` | Removes the association between an opportunity and a contact. |
| Dissociate Contacts From Company | `dissociateContactsFromCompany` | Removes the association between a company and a list of contacts. |
| Dissociate Contacts From Opportunity | `dissociateContactsFromOpportunity` | Removes the association between an opportunity and a list of contacts. |
| Dissociate Group From Opportunity | `dissociateGroupFromOpportunity` | Removes the association between an opportunity and a group. |
| Dissociate Groups From Opportunity | `dissociateGroupsFromOpportunity` | Removes the association between an opportunity and a list of groups. |
| Dissociate Opportunities From Company | `dissociateOpportunitiesFromCompany` | Removes the association between a company and a list of opportunities. |
| Dissociate Opportunities From Contact | `dissociateOpportunitiesFromContact` | Removes the association between a contact and a list of opportunities. |
| Dissociate Opportunities From Group | `dissociateOpportunitiesFromGroup` | Removes the association between a group and a list of opportunities. |
| Dissociate Opportunity From Company | `dissociateOpportunityFromCompany` | Removes the association between a company and an opportunity. |
| Dissociate Opportunity From Contact | `dissociateOpportunityFromContact` | Removes the association between a contact and an opportunity. |
| Dissociate Opportunity From Group | `dissociateOpportunityFromGroup` | Removes the association between a group and an opportunity. |
| Dissociate Task From Contact | `dissociateTaskFromContact` | Removes the association between a contact and a task. |
| Download Activity Attachment | `downloadActivityAttachment` | Downloads the attachment file of an activity. |
| Download Document Attachment | `downloadDocumentAttachment` | Downloads the file of a history document. |
| Download History Attachment | `downloadHistoryAttachment` | Downloads the attachment file of a history item. |
| Download Note Attachment | `downloadNoteAttachment` | Downloads the attachment file of a note. |
| Duplicate Contact | `duplicateContact` | Creates a copy of a contact, optionally copying only the primary fields. |
| Duplicate Contacts | `duplicateContacts` | Creates copies of a list of contacts, optionally copying only the primary fields. |
| Duplicate Task | `duplicateTask` | Creates a copy of a task. |
| Duplicate Tasks | `duplicateTasks` | Creates copies of a list of tasks. |
| Find Contacts By Business Email | `findContactsByBusinessEmail` | Returns contact identifiers for a JSON array of business email addresses. |
| Find Synced Calendar Uids | `findSyncedCalendarUids` | Returns which of the given calendar UIDs are already synchronised, with their external identifiers. |
| Find Synced External Ids | `findSyncedExternalIds` | Returns which of the given external identifiers are already synchronised with Act!. |
| Generate Access Token | `generateAccessToken` | Generates a JWT access token for the Act! Web API. Uses the connection's username and password (HTTP Basic) with the Act-Database-Name header on first connect, and renews the stored token when one exists. Runs automatically when a connection is created and whenever Act! rejects an expired token. |
| Get Activity Counts By User | `getActivityCountsByUser` | Returns activity counts per user for the given users, activity types and date range. |
| Get Activity Details By User | `getActivityDetailsByUser` | Returns the activity details behind the activity count for a single user. |
| Get Activity Series | `getActivitySeries` | Retrieves a recurring activity series by its identifier. |
| Get Actual Vs Predicted Revenue | `getActualVsPredictedRevenue` | Returns actual versus predicted opportunity revenue per period. |
| Get Attachment Upload Status | `getAttachmentUploadStatus` | Returns the upload status of an attachment so clients can wait for an upload to finish. |
| Get Average Time In Stage | `getAverageTimeInStage` | Returns the average time opportunities spend in each stage. |
| Get Calendar Preferences | `getCalendarPreferences` | Returns the current user's calendar preferences. |
| Get Calendar Schedule | `getCalendarSchedule` | Returns the calendar schedule of the current user, optionally filtered with an OData query. |
| Get Campaign Lead Info | `getCampaignLeadInfo` | Returns opportunities created from campaign leads within a date range. |
| Get Campaign Results | `getCampaignResults` | Returns result metrics (opens, clicks, bounces) for marketing campaigns. |
| Get Close Reason Counts | `getCloseReasonCounts` | Summarises how many opportunities were closed for each reason. |
| Get Close Reason Details | `getCloseReasonDetails` | Returns the opportunities closed for a specific reason. |
| Get Company | `getCompany` | Retrieves a company by its identifier. |
| Get Company Access | `getCompanyAccess` | Returns the access level and accessors of a company. |
| Get Contact | `getContact` | Retrieves a contact by its identifier. |
| Get Contact Access | `getContactAccess` | Returns the access level and accessors of a contact. |
| Get Contacts By Ids | `getContactsByIds` | Retrieves several contacts by a comma-separated list of identifiers. |
| Get CORS Origin | `getCorsOrigin` | Retrieves a CORS origin entry from the Act! Web API configuration. |
| Get Current Currency | `getCurrentCurrency` | Returns the currency and culture configured for the database. |
| Get Current User Permissions | `getCurrentUserPermissions` | Returns the permissions of the current user. |
| Get Custom Entity Record | `getCustomEntityRecord` | Retrieves a record of a custom table (custom entity). |
| Get Database Backup | `getDatabaseBackup` | Retrieves information about a database backup file. |
| Get Database Lock State | `getDatabaseLockState` | Returns the maintenance lock state of the database. |
| Get Demo Data Status | `getDemoDataStatus` | Returns whether the database currently contains Act! demo data. |
| Get Document | `getDocument` | Retrieves a history document by its identifier. |
| Get Document History Type | `getDocumentHistoryType` | Retrieves a document history type by name. |
| Get Drop-Down List | `getDropDownList` | Retrieves a drop-down list definition with its items. |
| Get Drop-Down List Item | `getDropDownListItem` | Retrieves an item of a drop-down list. |
| Get Duplicate Checking Preferences | `getDuplicateCheckingPreferences` | Returns the duplicate checking options of a record type. |
| Get Dynamic List Criteria | `getDynamicListCriteria` | Returns the criteria that define a dynamic group or list. |
| Get Dynamic List Metadata | `getDynamicListMetadata` | Returns the fields available for dynamic list criteria. |
| Get E-Marketing History | `getEMarketingHistory` | Returns historical e-marketing activity for a date range. |
| Get Field | `getField` | Retrieves a field definition by its identifier. |
| Get Group | `getGroup` | Retrieves a group by its identifier. |
| Get Group Access | `getGroupAccess` | Returns the access level and accessors of a group. |
| Get History | `getHistory` | Retrieves a history item by its identifier. |
| Get History Type | `getHistoryType` | Retrieves a history type by its identifier. |
| Get Import Field Mapping | `getImportFieldMapping` | Returns the target fields available for mapping the columns of an import file to a record type. |
| Get Import Result | `getImportResult` | Returns the results of an import. |
| Get Insight View Definition | `getInsightViewDefinition` | Returns the current user's Insight analytics view definition. |
| Get KPI Analytics | `getKpiAnalytics` | Returns key performance indicator values for a KPI group within a date range. |
| Get KPI View Definition | `getKpiViewDefinition` | Returns the current user's KPI analytics view definition by name. |
| Get Layout | `getLayout` | Retrieves a layout definition file. |
| Get Metadata Cache Refresh | `getMetadataCacheRefresh` | Refreshes the Act! Web API metadata cache using a GET request. |
| Get My Contact Record | `getMyContactRecord` | Returns the contact record of the current user. |
| Get MyAct View Definition | `getMyActViewDefinition` | Returns the current user's MyAct analytics view definition. |
| Get Note | `getNote` | Retrieves a note by its identifier. |
| Get Opportunities By Ids | `getOpportunitiesByIds` | Retrieves several opportunities by a comma-separated list of identifiers. |
| Get Opportunity | `getOpportunity` | Retrieves an opportunity by its identifier. |
| Get Opportunity Access | `getOpportunityAccess` | Returns the access level and accessors of an opportunity. |
| Get Opportunity Count By Stage | `getOpportunityCountByStage` | Returns the number of opportunities in each stage. |
| Get Opportunity Pipeline Analytics | `getOpportunityPipelineAnalytics` | Returns open opportunities in the pipeline matching the analytics filters. |
| Get Opportunity Pipeline View Settings | `getOpportunityPipelineViewSettings` | Returns the current user's opportunity pipeline analytics view settings. |
| Get Opportunity Process | `getOpportunityProcess` | Retrieves an opportunity sales process with its stages. |
| Get Opportunity Product | `getOpportunityProduct` | Retrieves a product line of an opportunity. |
| Get Opportunity Stage | `getOpportunityStage` | Retrieves an opportunity stage. |
| Get Permission | `getPermission` | Retrieves a permission (feature) by its identifier. |
| Get Product | `getProduct` | Retrieves a product by its identifier. |
| Get Record Type Field | `getRecordTypeField` | Retrieves a field definition of a record type. |
| Get Record Type Pick List | `getRecordTypePickList` | Retrieves a pick list of a record type. |
| Get Recurring Task | `getRecurringTask` | Retrieves a recurring task series. |
| Get Registration Info | `getRegistrationInfo` | Returns the registered Act! serial number and the number of client access licenses. |
| Get Revenue Forecast By Product | `getRevenueForecastByProduct` | Returns forecasted opportunity revenue for the given products. |
| Get Revenue Forecast By Rep | `getRevenueForecastByRep` | Returns forecasted opportunity revenue for the given users. |
| Get Revenue Forecast Details By Product | `getRevenueForecastDetailsByProduct` | Returns the opportunities behind the revenue forecast for one product. |
| Get Revenue Forecast Details By Rep | `getRevenueForecastDetailsByRep` | Returns the opportunities behind the revenue forecast for one user. |
| Get Revenue Vs Cost | `getRevenueVsCost` | Returns periodic opportunity revenue versus cost for the given products. |
| Get Sales By Product | `getSalesByProduct` | Returns opportunity sales totals for the given products. |
| Get Sales By Rep | `getSalesByRep` | Returns opportunity sales totals for the given users. |
| Get Sales Details By Product | `getSalesDetailsByProduct` | Returns the opportunities behind the sales total for one product. |
| Get Sales Details By Rep | `getSalesDetailsByRep` | Returns the opportunities behind the sales total for one user. |
| Get Salutation And Name Preferences | `getSalutationAndNamePreferences` | Returns the salutation and name affix preferences used when parsing contact names. |
| Get Secondary Contact | `getSecondaryContact` | Retrieves a secondary contact of a contact. |
| Get System Info | `getSystemInfo` | Returns version information for Act! and the Act! Web API. |
| Get Task | `getTask` | Retrieves a task (activity occurrence) by its identifier. |
| Get Task Alarm Updates | `getTaskAlarmUpdates` | Returns the current alarm state of a set of tracked activities. |
| Get Task List Analytics | `getTaskListAnalytics` | Returns task list activities for the analytics task list widget within a date range. |
| Get Task Preferences | `getTaskPreferences` | Returns the task preferences. |
| Get Task Type | `getTaskType` | Retrieves a task type by its identifier. |
| Get Tasks By Ids | `getTasksByIds` | Retrieves several tasks by a comma-separated list of identifiers. |
| Get Team | `getTeam` | Retrieves a team by its identifier. |
| Get Team Roster | `getTeamRoster` | Lists the users that belong to a team. |
| Get Top Open Opportunities | `getTopOpenOpportunities` | Returns the top open opportunities matching the analytics filters. |
| Get User | `getUser` | Retrieves an Act! user by its identifier. |
| Get User Permission | `getUserPermission` | Retrieves a single permission of a user. |
| Get Webhook | `getWebhook` | Retrieves a webhook registration. |
| Get Won Vs Lost Metrics | `getWonVsLostMetrics` | Returns opportunity win versus loss metrics for a date range. |
| List Accessors | `listAccessors` | Lists the users and teams that can be granted access to records. |
| List Activity Companies | `listActivityCompanies` | Lists the companies associated with an activity. |
| List Activity History | `listActivityHistory` | Lists the history items associated with an activity. |
| List Activity Series | `listActivitySeries` | Lists recurring activity series, optionally filtered with an OData query. |
| List Campaign Leads | `listCampaignLeads` | Returns contact leads generated by Act! Marketing Automation campaigns. |
| List Companies | `listCompanies` | Lists companies, optionally filtered with an OData query. |
| List Company Contacts | `listCompanyContacts` | Lists the contacts associated with a company. |
| List Company Divisions | `listCompanyDivisions` | Lists the divisions (sub-companies) of a company. |
| List Company Documents | `listCompanyDocuments` | Lists the history documents attached to a company. |
| List Company History | `listCompanyHistory` | Lists the history items of a company. |
| List Company Notes | `listCompanyNotes` | Lists the notes of a company. |
| List Company Opportunities | `listCompanyOpportunities` | Lists the opportunities associated with a company. |
| List Company Tasks | `listCompanyTasks` | Lists the tasks associated with a company. |
| List Company Web Info Links | `listCompanyWebInfoLinks` | Lists the web info hyperlinks configured for companies. |
| List Contact Campaign Results | `listContactCampaignResults` | Lists the marketing campaign results (opens, clicks, bounces) of a contact. |
| List Contact Campaigns | `listContactCampaigns` | Lists the marketing campaigns a contact received. |
| List Contact Companies | `listContactCompanies` | Lists the companies associated with a contact. |
| List Contact Documents | `listContactDocuments` | Lists the history documents attached to a contact. |
| List Contact Geolocations | `listContactGeolocations` | Returns contact counts grouped by geolocation. |
| List Contact Groups | `listContactGroups` | Lists the groups a contact belongs to. |
| List Contact History | `listContactHistory` | Lists the history items of a contact. |
| List Contact Notes | `listContactNotes` | Lists the notes of a contact. |
| List Contact Opportunities | `listContactOpportunities` | Lists the opportunities associated with a contact. |
| List Contact Tasks | `listContactTasks` | Lists the tasks associated with a contact. |
| List Contact Web Info Links | `listContactWebInfoLinks` | Lists the web info hyperlinks configured for contacts. |
| List Contacts | `listContacts` | Lists contacts in the Act! database, with OData query options for filtering, sorting, field selection and paging. |
| List Contacts In Groups | `listContactsInGroups` | Lists the distinct contacts that belong to any of the given groups. |
| List CORS Origins | `listCorsOrigins` | Lists the CORS origins allowed by the Act! Web API configuration. |
| List Currencies | `listCurrencies` | Lists currency symbols from the system regional settings. |
| List Custom Entity Companies | `listCustomEntityCompanies` | Lists the companies associated with a custom entity record. |
| List Custom Entity Contacts | `listCustomEntityContacts` | Lists the contacts associated with a custom entity record. |
| List Custom Entity Groups | `listCustomEntityGroups` | Lists the groups associated with a custom entity record. |
| List Custom Entity Opportunities | `listCustomEntityOpportunities` | Lists the opportunities associated with a custom entity record. |
| List Custom Entity Records | `listCustomEntityRecords` | Lists the records of a custom table (custom entity), optionally filtered with an OData query. |
| List Database Backups | `listDatabaseBackups` | Lists the database backup files. |
| List Document History Types | `listDocumentHistoryTypes` | Lists the history types available for documents. |
| List Documents | `listDocuments` | Lists history documents, optionally filtered with an OData query. |
| List Drop-Down List Items | `listDropDownListItems` | Lists the items of a drop-down list. |
| List Drop-Down Lists | `listDropDownLists` | Lists drop-down list definitions. |
| List Duplicate Checking Fields | `listDuplicateCheckingFields` | Lists the fields that can be used for duplicate checking on a record type. |
| List Dynamic List Operators | `listDynamicListOperators` | Returns the operators available for dynamic list criteria. |
| List Entities | `listEntities` | Lists the entities (record types and custom tables) in the database. |
| List Field Data Types | `listFieldDataTypes` | Lists the field data types available for each Act! record type. |
| List Fields | `listFields` | Lists field definitions across all record types. |
| List Group Contacts | `listGroupContacts` | Lists the contacts that are members of a group. |
| List Group Documents | `listGroupDocuments` | Lists the history documents attached to a group. |
| List Group History | `listGroupHistory` | Lists the history items of a group. |
| List Group Notes | `listGroupNotes` | Lists the notes of a group. |
| List Group Opportunities | `listGroupOpportunities` | Lists the opportunities associated with a group. |
| List Group Tasks | `listGroupTasks` | Lists the tasks associated with a group. |
| List Groups | `listGroups` | Lists groups, optionally filtered with an OData query. |
| List History | `listHistory` | Lists history items, optionally filtered with an OData query. |
| List History Types | `listHistoryTypes` | Lists all history types. |
| List Layouts | `listLayouts` | Lists the layout definition files. |
| List Nearby Contacts | `listNearbyContacts` | Lists contacts located within a radius of a latitude and longitude. |
| List Notes | `listNotes` | Lists notes, optionally filtered with an OData query. |
| List Open Database Sessions | `listOpenDatabaseSessions` | Lists the connections currently open to the database. |
| List Opportunities | `listOpportunities` | Lists opportunities, optionally filtered with an OData query. |
| List Opportunity Companies | `listOpportunityCompanies` | Lists the companies associated with an opportunity. |
| List Opportunity Contacts | `listOpportunityContacts` | Lists the contacts associated with an opportunity. |
| List Opportunity Documents | `listOpportunityDocuments` | Lists the history documents attached to an opportunity. |
| List Opportunity Groups | `listOpportunityGroups` | Lists the groups associated with an opportunity. |
| List Opportunity History | `listOpportunityHistory` | Lists the history items of an opportunity. |
| List Opportunity Notes | `listOpportunityNotes` | Lists the notes of an opportunity. |
| List Opportunity Processes | `listOpportunityProcesses` | Lists opportunity sales processes. |
| List Opportunity Products | `listOpportunityProducts` | Lists the product lines of an opportunity. |
| List Opportunity Stages | `listOpportunityStages` | Lists opportunity stages across all processes. |
| List Opportunity Tasks | `listOpportunityTasks` | Lists the tasks associated with an opportunity. |
| List Permissions | `listPermissions` | Lists all permissions (features). |
| List Phone Number Countries | `listPhoneNumberCountries` | Lists countries that have phone number format masks. |
| List Phone Number Masks | `listPhoneNumberMasks` | Lists phone number format masks. |
| List Process Stages | `listProcessStages` | Lists the stages of an opportunity sales process. |
| List Products | `listProducts` | Lists products, optionally filtered with an OData query. |
| List Record Type Fields | `listRecordTypeFields` | Lists the field definitions of a record type. |
| List Record Type Pick Lists | `listRecordTypePickLists` | Lists the pick lists of a record type. |
| List Recurring Tasks | `listRecurringTasks` | Lists recurring task series, optionally filtered with an OData query. |
| List Secondary Contacts | `listSecondaryContacts` | Lists the secondary contacts of a contact. |
| List Sent Campaigns | `listSentCampaigns` | Returns the marketing campaigns sent within a date range. |
| List Subgroups | `listSubgroups` | Lists the subgroups of a group. |
| List Task Alarms | `listTaskAlarms` | Lists the currently alarmed activities of the current user. |
| List Task Color Palette | `listTaskColorPalette` | Lists the calendar colour palette available for task types. |
| List Task Priorities | `listTaskPriorities` | Lists the available task priorities. |
| List Task Type History Types | `listTaskTypeHistoryTypes` | Lists the history types available for a task type. |
| List Task Type Regarding Options | `listTaskTypeRegardingOptions` | Lists the Regarding drop-down values of a task type. |
| List Task Types | `listTaskTypes` | Lists all task types, such as Call, Meeting and To-do. |
| List Tasks | `listTasks` | Lists tasks, optionally filtered with an OData query. |
| List Teams | `listTeams` | Lists all teams. |
| List User Permissions | `listUserPermissions` | Lists the permissions of a user. |
| List User Preferences | `listUserPreferences` | Lists the current user's preferences, optionally limited to named preferences. |
| List Users | `listUsers` | Lists all Act! users. |
| List Webhooks | `listWebhooks` | Lists webhook registrations, optionally filtered with an OData query. |
| Lock Database | `lockDatabase` | Locks the database, or schedules a pending lock, for maintenance. Other users are disconnected when the lock takes effect. |
| Mark All Snoozed Alarms Read | `markAllSnoozedAlarmsRead` | Marks all active snoozes of the current user as read. |
| Mark Snoozed Alarms Read | `markSnoozedAlarmsRead` | Marks the active snoozes of the specified activities as read. |
| Patch Activity Series | `patchActivitySeries` | Partially updates an existing recurring activity series; only the supplied fields change. |
| Patch Company | `patchCompany` | Partially updates a company; only the supplied fields change. |
| Patch Contact | `patchContact` | Partially updates a contact; only the supplied fields change. |
| Patch Group | `patchGroup` | Partially updates a group; only the supplied fields change. |
| Patch History | `patchHistory` | Partially updates a history item; only the supplied fields change. |
| Patch Note | `patchNote` | Partially updates a note; only the supplied fields change. |
| Patch Opportunity | `patchOpportunity` | Partially updates an opportunity; only the supplied fields change. |
| Patch Opportunity Process | `patchOpportunityProcess` | Partially updates an opportunity sales process. |
| Patch Opportunity Product | `patchOpportunityProduct` | Partially updates a product line of an opportunity. |
| Patch Opportunity Stage | `patchOpportunityStage` | Partially updates an opportunity stage. |
| Patch Product | `patchProduct` | Partially updates a product; only the supplied fields change. |
| Patch Recurring Task | `patchRecurringTask` | Partially updates a recurring task series. |
| Patch Secondary Contact | `patchSecondaryContact` | Partially updates a secondary contact of a contact. |
| Patch Task | `patchTask` | Partially updates a task; only the supplied fields change. |
| Patch Task Type | `patchTaskType` | Partially updates a custom task type. |
| Patch Task Types | `patchTaskTypes` | Partially updates a list of task types in one request, sent as a JSON array. |
| Patch Team | `patchTeam` | Partially updates a team. |
| Patch Webhook | `patchWebhook` | Partially updates a webhook registration. |
| Preview Dynamic Company List | `previewDynamicCompanyList` | Previews the companies that match dynamic list criteria sent as a JSON array. |
| Preview Dynamic Contact List | `previewDynamicContactList` | Previews the contacts that match dynamic contact list criteria sent as a JSON array. |
| Preview Dynamic Group List | `previewDynamicGroupList` | Previews the groups that match dynamic list criteria sent as a JSON array. |
| Preview Dynamic List | `previewDynamicList` | Previews the contacts that match dynamic list criteria sent as a JSON array. |
| Preview Dynamic Opportunity List | `previewDynamicOpportunityList` | Previews the opportunities that match dynamic list criteria sent as a JSON array. |
| Promote Secondary Contact | `promoteSecondaryContact` | Promotes a secondary contact to a primary contact. |
| Query Entity Analytics | `queryEntityAnalytics` | Runs an aggregate analytics query over a field of an entity (contacts, companies, groups or opportunities). |
| Query Entity Analytics Details | `queryEntityAnalyticsDetails` | Returns the records behind one value of an entity analytics query. |
| Refresh Email Integration Cache | `refreshEmailIntegrationCache` | Refreshes the email integration cache of the current user. |
| Refresh Metadata Cache | `refreshMetadataCache` | Refreshes the Act! Web API metadata cache. |
| Remove Contact From Group | `removeContactFromGroup` | Removes a single contact from a group. |
| Remove Contact From Groups | `removeContactFromGroups` | Removes a contact from a list of groups. |
| Remove Contact From Single Group | `removeContactFromSingleGroup` | Removes a contact from a single group, addressed from the contact. |
| Remove Contacts From Group | `removeContactsFromGroup` | Removes a list of contacts from a group. |
| Remove CORS Origin | `removeCorsOrigin` | Removes an origin from the CORS configuration of the Act! Web API (web.customer.config). |
| Reset Webhook Token | `resetWebhookToken` | Updates the current user's webhook registrations with a new Act! access token. |
| Resume Webhook | `resumeWebhook` | Resumes a suspended webhook registration. |
| Run Import | `runImport` | Imports contact records from the uploaded CSV file of an import flow. |
| Save Insight View Definition | `saveInsightViewDefinition` | Creates or updates the current user's Insight analytics view definition. |
| Save KPI View Definition | `saveKpiViewDefinition` | Creates or updates the current user's KPI analytics view definition by name. |
| Save MyAct View Definition | `saveMyActViewDefinition` | Creates or updates the current user's MyAct analytics view definition. |
| Save Opportunity Pipeline View Settings | `saveOpportunityPipelineViewSettings` | Creates or updates the current user's opportunity pipeline analytics view settings. |
| Save User Preference | `saveUserPreference` | Creates or updates a preference of the current user by identifier. |
| Search Opportunity Pipelines | `searchOpportunityPipelines` | Returns opportunities currently being worked that match a custom pipeline filter sent in the request body. |
| Set Contact Hot Lead Subscription | `setContactHotLeadSubscription` | Turns the hot lead subscription of a contact on or off. |
| Set Default Phone Number Mask | `setDefaultPhoneNumberMask` | Makes a phone number format mask the default. |
| Snooze Task Alarms | `snoozeTaskAlarms` | Snoozes the alarms of the specified activities. |
| Start Import | `startImport` | Starts an import flow for an uploaded CSV file with the given column mappings. |
| Suspend Webhook | `suspendWebhook` | Suspends a webhook registration so no notifications are sent. |
| Unclear Task | `unclearTask` | Reverts a cleared task back to open. |
| Unclear Tasks | `unclearTasks` | Reverts a list of cleared tasks back to open. |
| Unlock Database | `unlockDatabase` | Removes the maintenance lock from the database. |
| Update Activity Series | `updateActivitySeries` | Replaces an existing recurring activity series with the supplied values. |
| Update Calendar Preferences | `updateCalendarPreferences` | Updates the current user's calendar preferences. |
| Update Company | `updateCompany` | Replaces an existing company with the supplied values. |
| Update Company Access | `updateCompanyAccess` | Updates the access level and accessors of a company. |
| Update Company Web Info Link | `updateCompanyWebInfoLink` | Updates a web info hyperlink configured for companies. |
| Update Contact | `updateContact` | Replaces an existing contact with the supplied values. |
| Update Contact Access | `updateContactAccess` | Updates the access level and accessors of a contact. |
| Update Contact Web Info Link | `updateContactWebInfoLink` | Updates a web info hyperlink configured for contacts. |
| Update Custom Entity Record | `updateCustomEntityRecord` | Updates a record of a custom table (custom entity) with a JSON object of field values. |
| Update Document | `updateDocument` | Updates an existing history document record. |
| Update Drop-Down List | `updateDropDownList` | Updates a drop-down list definition and its items. |
| Update Duplicate Checking Preferences | `updateDuplicateCheckingPreferences` | Updates the fields used for duplicate checking on a record type. |
| Update Dynamic List Criteria | `updateDynamicListCriteria` | Replaces the criteria that define a dynamic group or list with a JSON array of criteria rows. |
| Update Group | `updateGroup` | Replaces an existing group with the supplied values. |
| Update Group Access | `updateGroupAccess` | Updates the access level and accessors of a group. |
| Update History | `updateHistory` | Replaces an existing history item with the supplied values. |
| Update Note | `updateNote` | Replaces an existing note with the supplied values. |
| Update Opportunity | `updateOpportunity` | Replaces an existing opportunity with the supplied values. |
| Update Opportunity Access | `updateOpportunityAccess` | Updates the access level and accessors of an opportunity. |
| Update Opportunity Process | `updateOpportunityProcess` | Replaces an existing opportunity sales process. |
| Update Opportunity Product | `updateOpportunityProduct` | Replaces a product line of an opportunity. |
| Update Opportunity Stage | `updateOpportunityStage` | Replaces an existing opportunity stage. |
| Update Product | `updateProduct` | Replaces an existing product with the supplied values. |
| Update Record Type Field | `updateRecordTypeField` | Updates a field definition of a record type. |
| Update Recurring Task | `updateRecurringTask` | Replaces a recurring task series. |
| Update Salutation And Name Preferences | `updateSalutationAndNamePreferences` | Updates the salutation and name affix preferences. |
| Update Secondary Contact | `updateSecondaryContact` | Replaces a secondary contact of a contact. |
| Update Task | `updateTask` | Replaces a task with the supplied values; any recurrence specification is ignored. |
| Update Task For User | `updateTaskForUser` | Modifies a task scheduled for another Act! user (Schedule For). |
| Update Task Preferences | `updateTaskPreferences` | Updates the task preferences. |
| Update Task Type | `updateTaskType` | Replaces a custom task type. |
| Update Team | `updateTeam` | Replaces an existing team. |
| Update Webhook | `updateWebhook` | Replaces a webhook registration. |
| Upload Activity Attachment | `uploadActivityAttachment` | Uploads a file as the attachment of an activity (multipart form data). |
| Upload Database Backup | `uploadDatabaseBackup` | Uploads a database backup file as multipart form data. |
| Upload Document Attachment | `uploadDocumentAttachment` | Uploads the file of a history document (multipart form data). |
| Upload History Attachment | `uploadHistoryAttachment` | Uploads a file as the attachment of a history item (multipart form data). |
| Upload Note Attachment | `uploadNoteAttachment` | Uploads a file as the attachment of a note (multipart form data). |
| Upload Template | `uploadTemplate` | Uploads a document template file (multipart form data). |
