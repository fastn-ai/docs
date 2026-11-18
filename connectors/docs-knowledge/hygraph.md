---
description: "Hygraph headless CMS."
---

# Hygraph

Hygraph headless CMS. GraphQL Management API for schema management (models, fields, enumerations, components, stages, locales, taxonomies), webhooks, and permanent auth tokens, plus Content API access. Auth via a Permanent Auth Token (Bearer).

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [hygraph.com](https://hygraph.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 31 |
| **Events** | 0 |
| **Slug** | `hygraph` |

## Use it

Add Hygraph from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hygraph.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Component | `createComponent` | Create a reusable component definition in an environment. Runs as an asynchronous schema migration. Provide variables.data with environmentId, apiId, apiIdPlural, and displayName. |
| Create Component Field | `createComponentField` | Add a component field (single or list) to a model or component. Runs as an asynchronous schema migration. Provide variables.data with parentId, apiId, displayName, isList, visibility, isRequired, and the component ID. |
| Create Enumerable Field | `createEnumerableField` | Add an enumeration-backed field to a model or component. Runs as an asynchronous schema migration. Provide variables.data with modelId (or parentId), enumerationId, type ENUMERATION, apiId, displayName, and the required boolean flags. |
| Create Enumeration | `createEnumeration` | Create a new enumeration (a set of allowed values) in an environment. Runs as an asynchronous schema migration. Provide variables.data with environmentId, apiId, displayName, and a values array of { apiId, displayName }. |
| Create Locale | `createLocale` | Create a new locale in an environment for localized content. Runs as an asynchronous schema migration. Provide variables.data with environmentId, apiId (e.g. 'fr'), and displayName. |
| Create Model | `createModel` | Create a new content model in the given environment. Schema changes run as an asynchronous migration; the response returns the migration id and status. Provide variables.data with environmentId, apiId, apiIdPlural, and displayName. |
| Create Permanent Auth Token | `createPermanentAuthToken` | Create a new Permanent Auth Token (PAT) for an environment. Provide variables.data with environmentId and name; optionally managementPermissionIds to grant management permissions. Returns the created token including its secret value. |
| Create Relational Field | `createRelationalField` | Add a relation or asset-reference field to a model. Runs as an asynchronous schema migration. Provide variables.data with modelId, type (RELATION or ASSET), apiId, displayName, isList, and reverseSide (the related modelId and optional reverse field). |
| Create Simple Field | `createSimpleField` | Add a scalar field (STRING, INT, FLOAT, BOOLEAN, DATETIME, DATE, JSON, RICHTEXT, LOCATION, COLOR, ID) to a model or component. Runs as an asynchronous schema migration. Provide variables.data with modelId (or parentId for a component), apiId, type, displayName, and the required boolean flags. |
| Create Stage | `createStage` | Create a new content stage in an environment. Runs as an asynchronous schema migration. Provide variables.data with environmentId, apiId, displayName, and colorPaletteId. Note: free plans are limited to two stages (Draft, Published). |
| Create Taxonomy | `createTaxonomy` | Create a new taxonomy in an environment. Runs as an asynchronous schema migration. Provide variables.data with environmentId, apiId, and displayName. |
| Create Webhook | `createWebhook` | Register a webhook that fires on content events. Provide variables.data with environmentId, name, url, isActive, includePayload, models (array of model IDs, empty for all), stages (array of stage IDs), triggerType CONTENT_MODEL, and triggerActions (CREATE, UPDATE, DELETE, PUBLISH, UNPUBLISH, TRANSITION_STEP). |
| Delete Component | `deleteComponent` | Delete a component definition by ID. Runs as an asynchronous schema migration. Provide variables.data.id. |
| Delete Enumeration | `deleteEnumeration` | Delete an enumeration by ID. Runs as an asynchronous schema migration. Provide variables.data.id. |
| Delete Field | `deleteField` | Delete a field from a model or component by field ID. Runs as an asynchronous schema migration. Provide variables.data.id. |
| Delete Locale | `deleteLocale` | Delete a locale by ID. Runs as an asynchronous schema migration. Provide variables.data.id and optionally force. |
| Delete Model | `deleteModel` | Delete a content model by ID. Runs as an asynchronous schema migration. Provide variables.data.id. |
| Delete Permanent Auth Token | `deletePermanentAuthToken` | Delete a Permanent Auth Token by ID. Provide variables.data.id. Returns the deleted token ID. |
| Delete Stage | `deleteStage` | Delete a content stage by ID. Runs as an asynchronous schema migration. Provide variables.data.id and optionally force. |
| Delete Taxonomy | `deleteTaxonomy` | Delete a taxonomy by ID. Runs as an asynchronous schema migration. Provide variables.data.id. |
| Delete Webhook | `deleteWebhook` | Delete a webhook by ID. Provide variables.data.webhookId. Returns the deleted webhook ID. |
| Get Content Model | `getContentModel` | Retrieve the full content model for a project environment: all models, stages, locales, enumerations, and components with their IDs and API IDs. Use these IDs when creating fields, webhooks, or other schema resources. Requires the project ID and environment name. |
| Get Meta Info | `getMetaInfo` | Retrieve Hygraph Management API meta information, including the server version. |
| Get Viewer | `getViewer` | Retrieve the authenticated viewer and a project's metadata, including its name, description, and environments (id, name, display name, endpoint). Requires the project ID. |
| Retrigger Webhook | `retriggerWebhook` | Retrigger a previously delivered webhook event by its log ID. Provide variables.data with the webhookId and the logId of the delivery to replay. Returns the new log ID. |
| Run Content GraphQL | `runContentGraphql` | Execute any GraphQL query or mutation against the Hygraph Content API for the connected project and environment. Use this to query or mutate content entries whose types are specific to the project schema. Pass the query string and an optional variables object. |
| Run Management GraphQL | `runManagementGraphql` | Execute any GraphQL query or mutation against the Hygraph Management API. Generic passthrough for management operations not covered by a dedicated action (roles, workflows, extensions, apps, integrations, remote sources, content views, members, environments). Pass the query string and an optional variables object. |
| Update Enumeration | `updateEnumeration` | Update an enumeration: rename it or add, update, or remove its values. Runs as an asynchronous schema migration. Provide variables.data with the enumeration id and any of valuesToCreate, valuesToUpdate, or valuesToDelete. |
| Update Model | `updateModel` | Update an existing content model's API IDs, display name, or description. Runs as an asynchronous schema migration. Provide variables.data with the model id and the fields to change. |
| Update Simple Field | `updateSimpleField` | Update an existing scalar field's properties (display name, description, required/unique/list flags, etc.). Runs as an asynchronous schema migration. Provide variables.data with the field id. |
| Update Webhook | `updateWebhook` | Update an existing webhook's configuration (URL, active state, trigger actions, scoped models/stages, etc.). Provide variables.data with the webhookId and the fields to change. |
