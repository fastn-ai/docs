---
description: "Copper CRM Developer API v1 — leads, people, companies, opportunities, projects, tasks, activities, pipelines, custom fields, connect fields, related items,…"
hidden: true
---

# Copper

<img src="../../.gitbook/assets/connectors/lg/copper.png" alt="Copper logo">

Copper CRM Developer API v1 — leads, people, companies, opportunities, projects, tasks, activities, pipelines, custom fields, connect fields, related items, files, and webhook subscriptions. Base: https://api.copper.com/developer_api/v1

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [copper.com](https://copper.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `copper` |

## Use it

Add Copper from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.copper.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Create Activities | `bulkCreateActivities` | Create multiple activities in one call (POST /activities/bulk_create). Bulk API rate limit: 3 req/s. |
| Bulk Create Companies | `bulkCreateCompanies` | Create multiple companies in one call (POST /companies/bulk_create). Bulk API rate limit: 3 req/s. |
| Bulk Create Leads | `bulkCreateLeads` | Create multiple leads in one call (POST /leads/bulk_create). Bulk API rate limit: 3 req/s. |
| Bulk Create Opportunities | `bulkCreateOpportunities` | Create multiple opportunities in one call (POST /opportunities/bulk_create). Bulk API rate limit: 3 req/s. |
| Bulk Create People | `bulkCreatePeople` | Create multiple people in one call (POST /people/bulk_create). Bulk API rate limit: 3 req/s. |
| Bulk Update Companies | `bulkUpdateCompanies` | Update multiple companies in one call (POST /companies/bulk_update). Each company object must include its id. |
| Bulk Update Leads | `bulkUpdateLeads` | Update up to 10 leads in one call (POST /leads/bulk_update). Each lead object must include its id. |
| Bulk Update People | `bulkUpdatePeople` | Update multiple people in one call (POST /people/bulk_update). Each person object must include its id. |
| Convert Lead | `convertLead` | Convert a lead into a Person, optionally creating/attaching a Company and an Opportunity. |
| Create Activity | `createActivity` | Log a new activity (e.g. note, phone call) on a record. type.category is 'user'; type.id 0 = note, or a user activity type id from listActivityTypes. |
| Create Company | `createCompany` | Create a new company. email_domain is a unique key for Companies. |
| Create Connection | `createConnection` | Create a connect-field connection between two records (POST /related_links). |
| Create Custom Activity Type | `createCustomActivityType` | Create a custom activity type. |
| Create Custom Field Definition | `createCustomFieldDefinition` | Create a custom field definition. Requires an admin API key. |
| Create Lead | `createLead` | Create a new lead. Requires the Leads feature to be enabled on the account. |
| Create Opportunity | `createOpportunity` | Create a new opportunity. Requires name and primary_contact_id (a Person ID). |
| Create Person | `createPerson` | Create a new person. Email address must be unique across People. |
| Create Project | `createProject` | Create a new project. |
| Create Task | `createTask` | Create a new task, optionally related to a record via related_resource. |
| Create Webhook | `createWebhook` | Create a webhook subscription (POST /webhooks). Copper POSTs notifications with the IDs of changed records to the target URL. |
| Delete Activity | `deleteActivity` | Delete an activity by ID. |
| Delete Company | `deleteCompany` | Delete a company by ID. |
| Delete Connection | `deleteConnection` | Delete a connect-field connection by ID (DELETE /related_links/{id}). |
| Delete Custom Field Definition | `deleteCustomFieldDefinition` | Delete a custom field definition by ID. Requires an admin API key. |
| Delete File | `deleteFile` | Delete a file attached to an entity record. |
| Delete Lead | `deleteLead` | Delete a lead by ID. |
| Delete Opportunity | `deleteOpportunity` | Delete an opportunity by ID. |
| Delete Person | `deletePerson` | Delete a person by ID. |
| Delete Project | `deleteProject` | Delete a project by ID. |
| Delete Task | `deleteTask` | Delete a task by ID. |
| Delete Webhook | `deleteWebhook` | Delete (unsubscribe) a webhook subscription by ID. |
| Fetch Person by Email | `fetchPersonByEmail` | Fetch a person by email address (POST /people/fetch_by_email). Email is a unique key for People. |
| Get Account | `getAccount` | Fetch details of the Copper account associated with the API key. |
| Get Activity | `getActivity` | Fetch an activity by ID. |
| Get API User | `getApiUser` | Fetch the Copper user record that owns the API token (GET /users/me). |
| Get Company | `getCompany` | Fetch a company by ID. |
| Get Custom Activity Type | `getCustomActivityType` | Fetch a custom activity type by ID. |
| Get Custom Field Definition | `getCustomFieldDefinition` | Fetch a custom field definition by ID. |
| Get Field Layout | `getFieldLayout` | List the field layout for an entity type (GET /field_layouts/by_entity/{entity}). For opportunities you MUST also pass pipeline_id. |
| Get File Metadata | `getFileMetadata` | Get metadata of a specific file attached to an entity record. |
| Get Lead | `getLead` | Fetch a lead by ID. Requires the Leads feature to be enabled on the account. |
| Get Opportunity | `getOpportunity` | Fetch an opportunity by ID. |
| Get Person | `getPerson` | Fetch a person by ID. |
| Get Project | `getProject` | Fetch a project by ID. |
| Get Signed S3 URL | `getSignedS3Url` | Step 1 of file upload: get a signed S3 upload URL + form fields for an entity record. POST the file to the returned url as multipart form-data (fields from body + the file), then call relateFileToEntity with the returned key. |
| Get Task | `getTask` | Fetch a task by ID. |
| Get User | `getUser` | Fetch a Copper user by ID. |
| Get Webhook | `getWebhook` | Fetch a webhook subscription by ID. |
| List Activity Types | `listActivityTypes` | List activity types, grouped into user and system categories. |
| List Company Activities | `listCompanyActivities` | View activities on a company (POST /companies/{id}/activities). |
| List Connections | `listConnections` | List connect-field connections on an entity (GET /related_links). |
| List Contact Types | `listContactTypes` | List contact types (used by people and companies). |
| List Custom Activity Types | `listCustomActivityTypes` | List custom activity types. |
| List Custom Field Definitions | `listCustomFieldDefinitions` | List all custom field definitions. |
| List Customer Sources | `listCustomerSources` | List customer sources (used by leads and opportunities). |
| List Files | `listFiles` | List files attached to an entity record (GET /{entity}/{id}/files). |
| List Lead Activities | `listLeadActivities` | View activities on a lead (POST /leads/{id}/activities). Optionally filter by activity types. |
| List Lead Statuses | `listLeadStatuses` | List lead statuses configured on the account. Requires the Leads feature to be enabled. |
| List Loss Reasons | `listLossReasons` | List opportunity loss reasons. |
| List Person Activities | `listPersonActivities` | View activities on a person (POST /people/{id}/activities). |
| List Pipeline Stages | `listPipelineStages` | List all pipeline stages across pipelines. |
| List Pipelines | `listPipelines` | List opportunity pipelines with their stages. |
| List Related Records | `listRelatedRecords` | View all records related to an entity (GET /{entity}/{id}/related). |
| List Related Records By Type | `listRelatedRecordsByType` | View records of one type related to an entity (GET /{entity}/{id}/related/{relatedType}). |
| List Stages In Pipeline | `listStagesInPipeline` | List the stages of one pipeline (GET /pipeline_stages/pipeline/{id}). |
| List Tags | `listTags` | List all tags defined on the account. |
| List Users | `listUsers` | List users on the Copper account (POST /users/search) with pagination. |
| List Webhooks | `listWebhooks` | List all webhook subscriptions. |
| Relate File To Entity | `relateFileToEntity` | Step 3 of file upload: attach an uploaded S3 object to an entity record (POST /{entity}/{id}/files with file_name + key from getSignedS3Url). |
| Relate Record | `relateRecord` | Relate an existing record to an entity (POST /{entity}/{id}/related). Both records must already exist. |
| Search Activities | `searchActivities` | List/search activities (POST /activities/search). Filter by parent record, activity types, and activity date range. |
| Search Companies | `searchCompanies` | List/search companies (POST /companies/search) with filters, sorting and pagination. |
| Search Leads | `searchLeads` | List/search leads (POST /leads/search) with filters, sorting and pagination. Response header X-PW-TOTAL carries total match count. |
| Search Opportunities | `searchOpportunities` | List/search opportunities (POST /opportunities/search) with filters, sorting and pagination. |
| Search People | `searchPeople` | List/search people (POST /people/search) with filters, sorting and pagination. |
| Search Projects | `searchProjects` | List/search projects (POST /projects/search) with filters, sorting and pagination. |
| Search Tasks | `searchTasks` | List/search tasks (POST /tasks/search) with filters, sorting and pagination. |
| Unrelate Record | `unrelateRecord` | Remove a relationship between a record and an entity (DELETE /{entity}/{id}/related). Neither record is deleted. |
| Update Activity | `updateActivity` | Update an existing user activity (details and/or activity_date). |
| Update Company | `updateCompany` | Update an existing company (partial update — only provided fields are sent). |
| Update Custom Activity Type | `updateCustomActivityType` | Update a custom activity type (name, icon_type, is_disabled). |
| Update Custom Field Definition | `updateCustomFieldDefinition` | Update a custom field definition (partial update — only provided fields are sent). |
| Update Lead | `updateLead` | Update an existing lead (partial update — only provided fields are sent). |
| Update Opportunity | `updateOpportunity` | Update an existing opportunity (partial update - only provided fields are sent). Copper ignores company_id on update: to change the company use Unrelate Record then Relate Record (Related Items). |
| Update Person | `updatePerson` | Update an existing person (partial update - only provided fields are sent). Copper ignores company_id on update: to move the person to another company use Unrelate Record then Relate Record (Related Items). |
| Update Project | `updateProject` | Update an existing project (partial update — only provided fields are sent). |
| Update Task | `updateTask` | Update an existing task (partial update — only provided fields are sent). |
| Update Webhook | `updateWebhook` | Update a webhook subscription (target, secret, headers, custom_field_computed_values). |
| Upsert Lead | `upsertLead` | Atomically create or update a lead matched by a field (PUT /leads/upsert). match.field_name can be a standard field (e.g. email) or 'custom' with field_value {custom_field_definition_id, value}. 422 when 2+ records match. |
