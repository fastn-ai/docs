---
description: "Fibery work-management workspace API."
hidden: true
---

# Fibery

Fibery work-management workspace API. Covers the /api/commands command API (entities, collections, schema/databases/fields), documents & rich text, files, views (JSON-RPC), workspace history, webhooks v2, access tokens and the per-space GraphQL API.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [fibery.io](https://fibery.io) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Actions** | 44 |
| **Events** | 5 |
| **Slug** | `fibery` |

## Use it

Add Fibery from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fibery.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Collection Items | `addCollectionItems` | Command fibery.entity/add-collection-items on POST /api/commands. Adds items to a to-many / multi-select field. 'entity' maps each holder entity id to the array of item ids, e.g. {\"&lt;holderId&gt;\":[\"&lt;itemId&gt;\"]}. |
| Batch Commands | `batchCommands` | Command fibery.command/batch on POST /api/commands. Runs several commands of any kind in one atomic transaction. correlationId MUST be a UUID - Fibery rejects any other string - and is echoed back in the webhook delivery for this transaction. |
| Batch Create Or Update Entities | `batchCreateOrUpdateEntities` | Command fibery.entity.batch/create-or-update on POST /api/commands. Upserts many entities of one Database in one call. Every entity must carry a fibery/id. conflictField detects an existing row and CANNOT be a fibery/uuid field (so not fibery/id) - use a text field such as the title. conflictAction is 'skip-create' or 'update-latest'. |
| Create Access Token | `createAccessToken` | POST /api/tokens. Creates a new API token for the current user (max 3 per user). Fibery serves this endpoint only to a browser-cookie session - an API token gets 401 by design. |
| Create Database | `createDatabase` | Sub-command schema.type/create, sent inside a fibery.schema/batch envelope on POST /api/commands. Creates a Database (type). 'name' is 'Space/Database'; 'fields' must include the system fields fibery/id, fibery/public-id, fibery/creation-date, fibery/modification-date. |
| Create Entity | `createEntity` | Command fibery.entity/create on POST /api/commands. Creates one entity in the given Database (type). 'entity' holds the field values, e.g. {\"Project Tracking/Name\":\"Task A\"}. |
| Create Enum | `createEnum` | Sub-command schema.enum/create inside a fibery.schema/batch envelope on POST /api/commands. Creates the enum Database backing a single-select or multi-select Field. Convention: '&lt;Space&gt;/&lt;Field Name&gt;_&lt;Space&gt;/&lt;Database&gt;'. |
| Create Field | `createField` | Sub-command schema.field/create inside a fibery.schema/batch envelope on POST /api/commands. Adds a Field to a Database. Use a primitive fibery/* type, another Database name for a relation, or an enum type for a select. |
| Create Or Update Documents Batch | `createOrUpdateDocumentsBatch` | Command create-or-update-documents on POST /api/documents/commands. Writes several rich-text documents in one call. args is an array of {secret, content}. |
| Create Views | `createViews` | JSON-RPC method create-views on POST /api/views/json-rpc. Creates one or more Views. Each view needs fibery/id, fibery/name, fibery/type (board, table, list, ...) and fibery/container-app pointing at the Space id. |
| Create Webhook | `createWebhook` | POST /api/webhooks/v2. Subscribes a URL to entity changes of one Database. Requires Architect access. Returns the webhook id used to delete it later. |
| Delete Access Token | `deleteAccessToken` | DELETE /api/tokens/{id}. Revokes one of the current user's API tokens. Fibery serves this endpoint only to a browser-cookie session - an API token gets 401 by design. |
| Delete Database | `deleteDatabase` | Sub-command schema.type/delete inside a fibery.schema/batch envelope on POST /api/commands. Deletes a Database; set deleteEntities/deleteRelatedFields to also drop its rows and inbound relation Fields. |
| Delete Entity | `deleteEntity` | Command fibery.entity/delete on POST /api/commands. Permanently deletes one entity by its fibery/id. |
| Delete Field | `deleteField` | Sub-command schema.field/delete inside a fibery.schema/batch envelope on POST /api/commands. Deletes a Field; deleteValues also drops the stored values. |
| Delete Views | `deleteViews` | JSON-RPC method delete-views on POST /api/views/json-rpc. Deletes the Views with the given ids. |
| Delete Webhook | `deleteWebhook` | DELETE /api/webhooks/v2/{id}. Removes a webhook subscription by its numeric id. HTTP 200 means deleted. |
| Download File | `downloadFile` | GET /api/files/{secret}. Downloads the stored file bytes by its fibery/secret. |
| Get Document | `getDocument` | GET /api/documents/{secret}. Reads the content of one rich-text document (a rich-text Field's fibery/secret). format is 'md' or 'html'. |
| Get Documents Batch | `getDocumentsBatch` | Command get-documents on POST /api/documents/commands. Reads several rich-text documents in one call. args is an array of {secret}. |
| Get Schema | `getSchema` | GET /api/schema. Plain REST read of the workspace schema - same payload as the fibery.schema/query command result, without the command envelope. |
| GraphQL Query | `graphqlQuery` | POST /api/graphql/space/{space}. Runs a GraphQL query or mutation against one Space's generated schema. Each Space has its own endpoint and schema. |
| Install Mixins | `installMixins` | Command fibery.app/install-mixins on POST /api/commands. Installs mixins on Databases, e.g. {\"Cricket/Player\":[\"fibery/rank-mixin\"]} to make its entities orderable. |
| List Access Tokens | `listAccessTokens` | GET /api/tokens. Lists the current user's API tokens (max 3). Fibery serves this endpoint only to a browser-cookie session - an API token gets 401 by design. |
| List Users | `listUsers` | GET /api/users. Lists the workspace member email addresses. |
| List Webhooks | `listWebhooks` | GET /api/webhooks/v2. Lists every webhook in the workspace with its url, type, state and latest 50 delivery runs. |
| List Webhooks V1 | `listWebhooksV1` | GET /api/webhooks. Legacy v1 webhook listing, still served by Fibery alongside /api/webhooks/v2. Prefer List Webhooks for new work. |
| Query Entities | `queryEntities` | Command fibery.entity/query on POST /api/commands. Reads entities with q/from, q/select, q/where, q/order-by, q/limit, q/offset. 'params' binds $-placeholders used in q/where (pass {} when unused). |
| Query Schema | `querySchema` | Command fibery.schema/query on POST /api/commands. Returns the full workspace schema: every Database (type) with its Fields and metadata. |
| Query Views | `queryViews` | JSON-RPC method query-views on POST /api/views/json-rpc. Lists Views, optionally filtered by ids, publicIds, isPrivate or container. Pass {} in filter for all Views. |
| Remove Collection Items | `removeCollectionItems` | Command fibery.entity/remove-collection-items on POST /api/commands. Removes specific items from a to-many / multi-select field. |
| Rename Database | `renameDatabase` | Sub-command schema.type/rename inside a fibery.schema/batch envelope on POST /api/commands. Renames a Database. |
| Rename Field | `renameField` | Sub-command schema.field/rename inside a fibery.schema/batch envelope on POST /api/commands. Renames a Field on a Database. |
| Reset Collection Items | `resetCollectionItems` | Command fibery.entity/reset-collection-items on POST /api/commands. Clears every item from a to-many / multi-select field on one entity. |
| Schema Batch | `schemaBatch` | Command fibery.schema/batch on POST /api/commands. Runs several schema.* sub-commands atomically in one transaction - use when a change needs more than one step (e.g. create an enum and the select Field that uses it). |
| Search History | `searchHistory` | POST /api/history/v2/search. Paginated workspace change log. 'where' filters on typeId, action, author, entityId etc; timeframe span is max 1 year; page with sinceItem from nextPage. |
| Set Collection Items | `setCollectionItems` | Command fibery.entity/set-collection-items on POST /api/commands. Replaces the whole contents of a to-many / multi-select field with the given items. |
| Set Field Meta | `setFieldMeta` | Sub-command schema.field/set-meta inside a fibery.schema/batch envelope on POST /api/commands. Sets one meta key on a Field, e.g. key 'fibery/required?' with value true, or key 'fibery/default-value' with value {\"fibery/id\":\"...\"}. |
| Sign File Urls | `signFileUrls` | POST /api/files/sign-urls. Returns temporary public download URLs (valid 60 minutes) for the given file secrets. |
| Update Document | `updateDocument` | PUT /api/documents/{secret}. Replaces the content of one rich-text document. format 'md' or 'html' says how 'content' is interpreted. |
| Update Entity | `updateEntity` | Command fibery.entity/update on POST /api/commands. Updates field values on one entity. 'entity' must include fibery/id plus the fields to change. |
| Update Views | `updateViews` | JSON-RPC method update-views on POST /api/views/json-rpc. Updates one or more Views. Each update is {id, values}. |
| Upload File | `uploadFile` | POST /api/files. Uploads a text file as multipart/form-data and creates the matching fibery/file entity. Returns fibery/id (to attach to an entity) and fibery/secret (to download). Binary uploads are not supported by this engine - use Upload File From Url for those. |
| Upload File From Url | `uploadFileFromUrl` | POST /api/files/from-url. Fibery fetches the given URL itself and stores the result as a file entity. Works for binary content. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Collection items added | `fibery.entity/add-collection-items` | Items were added to a to-many or multi-select Field on an entity in the watched Database. Filter effects[] on effect == 'fibery.entity/add-collection-items'; the effect carries field and items. payloadSchema MODELLED from Fibery's documented sample. |
| Collection items removed | `fibery.entity/remove-collection-items` | Items were removed from a to-many or multi-select Field on an entity in the watched Database. Filter effects[] on effect == 'fibery.entity/remove-collection-items'. payloadSchema MODELLED from Fibery's documented sample. |
| Entity created | `fibery.entity/create` | An entity was created in the watched Database. Set the 'database' input to the Fibery Database name (e.g. 'Project Tracking/Task'); one Fibery webhook per Database delivers EVERY change kind to the same URL, so each delivery's effects[] array must be filtered on effect == 'fibery.entity/create'. payloadSchema is MODELLED from Fibery's documented delivery sample, not captured from a live delivery. |
| Entity deleted | `fibery.entity/delete` | An entity was deleted from the watched Database. Filter effects[] on effect == 'fibery.entity/delete'. payloadSchema MODELLED from Fibery's documented sample. |
| Entity updated | `fibery.entity/update` | Field values changed on an entity in the watched Database. Rich-text Field changes are NOT delivered (vendor limitation). Filter effects[] on effect == 'fibery.entity/update'; each effect carries values and valuesBefore. payloadSchema MODELLED from Fibery's documented sample. |
