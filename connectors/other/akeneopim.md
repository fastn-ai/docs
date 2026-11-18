---
description: "Akeneo PIM REST API connector — products, product models, families, attributes, categories, channels, locales, reference entities, assets, catalogs, jobs, and…"
hidden: true
---

# Akeneo PIM

<img src="../../.gitbook/assets/connectors/akeneopim.png" alt="Akeneo PIM logo" width="64">

Akeneo PIM REST API connector — products, product models, families, attributes, categories, channels, locales, reference entities, assets, catalogs, jobs, and webhooks. Full CRUD per resource.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [akeneo.com](https://akeneo.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `akeneopim` |

## Use it

Add Akeneo PIM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.akeneopim.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Approve Modelization Suggestion | `approveModelizationSuggestion` | Data Architect Agent: approve a modelization suggestion by UUID, optionally overriding attribute code, type, labels, group, scopable and localizable. All body fields are optional overrides. |
| Bulk Upsert Assets | `bulkUpsertAssets` | Create or update several assets of a given asset family in one PATCH call. Body is a top-level JSON array (Content-Type application/json) — one asset object per element. Returns HTTP 200 with a per-line result array. |
| Bulk Upsert Association Types | `bulkUpsertAssociationTypes` | Update/create several association types at once. Body is newline-delimited JSON (one association type object per line), sent with the Akeneo collection content type. |
| Bulk Upsert Attribute Groups | `bulkUpsertAttributeGroups` | Create or update several attribute groups at once (NDJSON bulk PATCH). Body is newline-delimited JSON objects, one group per line. |
| Bulk Upsert Attribute Options | `bulkUpsertAttributeOptions` | Create or update several options of a given attribute at once (NDJSON bulk PATCH). Body is newline-delimited JSON objects, one option per line. |
| Bulk Upsert Attributes | `bulkUpsertAttributes` | Create or update several attributes at once (NDJSON bulk PATCH). Body is newline-delimited JSON objects, one attribute per line. Returns one status line per submitted attribute. |
| Bulk Upsert Categories | `bulkUpsertCategories` | Create or update several categories in one request using NDJSON (one JSON category object per line). Content-Type application/vnd.akeneo.collection+json. Returns a line-by-line status report. |
| Bulk Upsert Channels | `bulkUpsertChannels` | Create or update several channels in one request using NDJSON (one JSON channel object per line). Content-Type application/vnd.akeneo.collection+json. Returns a line-by-line status report. |
| Bulk Upsert Families | `bulkUpsertFamilies` | Update/create several families in one call (NDJSON bulk). Provide 'items' as newline-delimited JSON objects, one family per line. Uses Content-Type application/vnd.akeneo.collection+json. Returns one status line per submitted family. |
| Bulk Upsert Family Variants | `bulkUpsertFamilyVariants` | Update/create several family variants for a given family in one call (NDJSON bulk). Provide 'items' as newline-delimited JSON objects, one variant per line. Uses Content-Type application/vnd.akeneo.collection+json. |

<details>

<summary>See 141 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Upsert Product Models | `bulkUpsertProductModels` | Update/create several product models at once. Body is newline-delimited JSON (one product model object per line), sent with the Akeneo collection content type. Each object must include code and family_variant. |
| Bulk Upsert Products (UUID) | `bulkUpsertProductsUuid` | Update or create several products in one call via the UUID collection endpoint. Body is newline-delimited JSON (one product object per line) sent as application/vnd.akeneo.collection+json. Returns one HTTP-status line per submitted product. |
| Create Asset Media File | `createAssetMediaFile` | Upload a new media file for an asset (multipart/form-data). The binary file is sent in the 'file' part. Note: fastn cannot emit binary multipart bodies, so this action is expected to be classified as blocked in the verify phase. |
| Create Association Type | `createAssociationType` | Create a new association type. code is required. is_quantified marks quantified associations; is_two_way marks bidirectional associations. |
| Create Attribute | `createAttribute` | Create a new catalog attribute. Required: code, type, group. Many optional fields apply only to specific attribute types. |
| Create Attribute Group | `createAttributeGroup` | Create a new attribute group. Required: code. |
| Create Attribute Option | `createAttributeOption` | Create a new option for a given attribute. Required: attribute_code (path) and code (body). |
| Create Catalog | `createCatalog` | Create a new catalog. Requires a name; optionally managed currencies and locales. Returns the created catalog (201). |
| Create Category | `createCategory` | Create a new category. Required: code. Optional: parent, labels, channel_requirements, values, validations. Returns 201 with an empty body and a Location header. |
| Create Category Media File | `createCategoryMediaFile` | Upload a media file and associate it with a category attribute value. multipart/form-data with a 'category' JSON string field and a binary 'file' field. NOTE: fastn cannot emit binary multipart, so live execution is expected to be blocked. |
| Create Channel | `createChannel` | Create a new channel. Required: code, locales, currencies, category_tree. Optional: conversion_units, labels. Returns 201 with an empty body. |
| Create Extension | `createExtension` | Create a new UI extension (JSON variant). 'name', 'position' and 'type' are required. Optionally provide description, version, configuration, status and credentials. |
| Create Family | `createFamily` | Create a new family. Body is a single JSON object with code, attributes, attribute_requirements, labels, etc. Returns 201 with a Location header and empty body. |
| Create Family Variant | `createFamilyVariant` | Create a new family variant for a given family. Body is a single JSON object with code, variant_attribute_sets (levels/axes/attributes), and labels. Returns 201 with empty body. |
| Create Modelization Suggestion | `createModelizationSuggestion` | Data Architect Agent: create a modelization (attribute) suggestion. 'source' and 'description' are required. Optionally provide code, type and additional_comments. |
| Create Product | `createProduct` | Create a new product (POST /products). The identifier is required. Optionally set enabled state, family, categories, groups, parent product model, attribute values and associations. Returns 201 with no body on success (Location header points to the created resource). |
| Create Product (UUID) | `createProductUuid` | Create a new product on the UUID endpoint. Optionally pass a UUID; otherwise Akeneo generates one. Returns 201 with a Location header and empty body on success. |
| Create product media file | `createMediaFile` | Upload a new product media file (multipart/form-data). The binary file plus an optional JSON 'product' or 'product_model' descriptor that links the media to a product attribute value. NOTE: fastn cannot emit binary multipart bodies, so this action is expected to be classified as blocked during verification. |
| Create Product Model | `createProductModel` | Create a new product model. code is required for create. family_variant identifies the family variant; parent links to a parent product model for sub product models. |
| Create Reference Entity Media File | `createReferenceEntityMediaFile` | Upload a new media file for a reference entity or record image attribute (multipart/form-data). The media file code is returned in the Location/Asset-media-file-code response header. NOTE: fastn cannot emit binary multipart bodies, so live execution is expected to be blocked. |
| Decline Modelization Suggestion | `declineModelizationSuggestion` | Data Architect Agent: decline a modelization suggestion by UUID, optionally providing a reject reason. |
| Delete Asset | `deleteAsset` | Delete an asset of a given asset family by code. Returns 204 No Content on success. |
| Delete Asset Attribute Option | `deleteAssetAttributeOption` | Delete an attribute option for a given attribute of a given asset family. Returns 204 No Content on success. |
| Delete Catalog | `deleteCatalog` | Delete a catalog by its id (UUID path param). Returns 204 No Content on success. |
| Delete Catalog Product Mapping Schema | `deleteCatalogProductMappingSchema` | Delete the product mapping schema linked to a catalog. Returns 204 No Content on success. Requires an App token with catalogs scope. |
| Delete Extension | `deleteExtension` | Delete a UI extension by its UUID. |
| Delete Family | `deleteFamily` | Delete a family by its code. Returns 204 with empty body on success. |
| Delete Product | `deleteProduct` | Delete a product by its identifier (code). DELETE /products/{code}. Returns 204 with no body on success. |
| Delete Product By UUID | `deleteProductUuid` | Delete a product by its UUID. Returns 204 No Content on success. |
| Delete Product Model | `deleteProductModel` | Delete a product model by its code. |
| Download Asset Media File | `downloadAssetMediaFile` | Download the binary media file associated to an asset by its code. Returns the raw file content. |
| Download Category Media File | `downloadCategoryMediaFile` | Download a category media file by its file_path identifier. Returns the binary file content. |
| Download product media file | `downloadMediaFile` | Download the binary content of a product media file by its code. Returns the raw file bytes. |
| Duplicate Catalog | `duplicateCatalog` | Duplicate an existing catalog by id. Optionally override name, currencies, locales, skip checks, and replace mapping locales. Returns the new catalog (201). |
| Get API overview | `getApiOverview` | Get the list of all available API endpoints (the API root/overview): host, authentication endpoint, and the routes map. |
| Get Asset | `getAsset` | Get a single asset of a given asset family by code. |
| Get Asset Attribute | `getAssetAttribute` | Get a single attribute of a given asset family by code. |
| Get Asset Attribute Option | `getAssetAttributeOption` | Get an attribute option for a given attribute of a given asset family by code. |
| Get Asset Family | `getAssetFamily` | Get a single asset family by its code. |
| Get Association Type | `getAssociationType` | Get a single association type by its code. |
| Get Attribute | `getAttribute` | Get a single catalog attribute by its code. Optionally include table select options. |
| Get Attribute Group | `getAttributeGroup` | Get a single attribute group by its code. |
| Get Attribute Option | `getAttributeOption` | Get a single option of a given attribute by attribute code and option code. |
| Get Catalog | `getCatalog` | Get a single catalog by its id (UUID path param). Returns the catalog object. |
| Get Catalog Product | `getCatalogProduct` | Get a single product related to a catalog by its UUID. Returns the full product object. |
| Get Catalog Product Mapping Schema | `getCatalogProductMappingSchema` | Get the product mapping schema related to a catalog. Returns the JSON Schema describing the catalog's product mapping targets. |
| Get Category | `getCategory` | Get a single category by its code. Optional query params with_position and with_enriched_attributes. Returns the category object. |
| Get Channel | `getChannel` | Get a single channel by its code. Returns the channel object. |
| Get Currency | `getCurrency` | Get a single currency by its code. Returns the currency object. |
| Get Family | `getFamily` | Get a single family by its code. Returns the family object. |
| Get Family Variant | `getFamilyVariant` | Get a single family variant by family code and variant code. Returns the variant object. |
| Get Locale | `getLocale` | Get a single locale by its code. Returns the locale object. |
| Get Modelization Suggestion | `getModelizationSuggestion` | Data Architect Agent: get a single modelization suggestion by its UUID. |
| Get Product | `getProduct` | Get a single product by its identifier (code). Optional query flags return quality scores, completenesses, attribute-option labels, asset share links and workflow execution statuses. Returns the full product object. |
| Get Product By UUID | `getProductUuid` | Get a single product by its UUID. Optional query flags return attribute option labels, asset share links, quality scores, completenesses, root parent and workflow execution statuses. |
| Get Product Draft | `getProductDraft` | Get the working-copy draft of a product by its identifier (GET /products/{code}/draft). Returns the draft product object with its pending changes. |
| Get Product Draft By UUID | `getProductDraftUuid` | Get the working-copy draft of a product identified by UUID. Returns the product representation reflecting unpublished draft changes. |
| Get product media file | `getMediaFile` | Get the metadata of a single product media file by its code (original filename, mime type, size, extension, download link). |
| Get Product Model | `getProductModel` | Get a single product model by its code. |
| Get Product Model Draft | `getProductModelDraft` | Get the working-copy draft of a product model by its code. |
| Get Reference Entity | `getReferenceEntity` | Get a single reference entity by its code. |
| Get Reference Entity Attribute | `getReferenceEntityAttribute` | Get a single attribute of a given reference entity by attribute code. |
| Get Reference Entity Attribute Option | `getReferenceEntityAttributeOption` | Get a single attribute option for a given attribute of a given reference entity. |
| Get Reference Entity Media File | `getReferenceEntityMediaFile` | Download the binary media file associated to a reference entity or record by its media file code. Returns the raw file content. |
| Get Reference Entity Record | `getReferenceEntityRecord` | Get a single record of a given reference entity by record code. |
| Get Rule Definition | `getRuleDefinition` | Get a single rule definition by its code, including conditions, actions and triggers. |
| Get system information | `getSystemInformation` | Get system information about the PIM instance: its version and edition. |
| Get user channels permissions | `getUserChannelsPermissions` | Get a user's channels permissions (canView/canEdit per channel code) by the user's UUID. |
| Get user locales permissions | `getUserLocalesPermissions` | Get a user's locales permissions (canView/canEdit per locale code) by the user's UUID. |
| Get Workflow | `getWorkflow` | Get a single workflow by its UUID, including its steps configuration. |
| Launch export job | `launchExportJob` | Launch an export job by its job profile code. Optionally run in dry-run mode. Returns the job execution id. |
| Launch import job | `launchImportJob` | Launch an import job by its job profile code. Optionally override the import mode and run in dry-run mode. Returns the job execution id. |
| List All Reference Entity Records | `listAllReferenceEntityRecords` | Get all records across all reference entities. Optionally filter by reference_entity, search, channel, locales. Supports search_after pagination. |
| List Asset Attribute Options | `listAssetAttributeOptions` | Get the list of options of a given attribute for a given asset family. Returns a plain array. |
| List Asset Attributes | `listAssetAttributes` | Get the list of attributes of a given asset family. Returns a plain array (not paginated). |
| List Asset Families | `listAssetFamilies` | Get the list of asset families. Supports search_after cursor pagination. |
| List Assets | `listAssets` | Get the list of assets of a given asset family. Supports asset filters via search, channel/locale value filtering, and search_after cursor pagination. |
| List Association Types | `listAssociationTypes` | Get the paginated list of association types. |
| List Attribute Groups | `listAttributeGroups` | List attribute groups with optional search filter and pagination. Returns a paginated HAL list. |
| List Attribute Options | `listAttributeOptions` | List the options of a given attribute (select/multiselect attribute). Returns a paginated HAL list. |
| List Attributes | `listAttributes` | List catalog attributes with optional search filter and pagination. Returns a paginated HAL list of attributes. |
| List Catalog Mapped Model Variants | `listCatalogMappedModelVariants` | Get the list of mapped variants of a given model related to a catalog. Supports search_after, limit, and updated_before/after filters. |
| List Catalog Mapped Models | `listCatalogMappedModels` | Get the list of mapped models related to a catalog. Supports search_after pagination, limit, and updated_before/after date filters. |
| List Catalog Mapped Products | `listCatalogMappedProducts` | Get the list of mapped flattened or simple products related to a catalog. Supports search_after, limit, and updated_before/after filters. |
| List Catalog Product UUIDs | `listCatalogProductUuids` | Get the list of product uuids related to a catalog. Supports search_after, limit, with_count, and updated_before/after filters. |
| List Catalog Products | `listCatalogProducts` | Get the list of products related to a catalog. Supports search_after, limit, and updated_before/after filters. |
| List Catalogs | `listCatalogs` | Get the list of owned catalogs. Paginated with page/limit. Returns HAL-wrapped catalog items. |
| List Categories | `listCategories` | Get the list of categories. Supports search filter, pagination (page/limit), with_count, with_position, with_enriched_attributes. Returns paginated HAL list of categories. |
| List Channels | `listChannels` | Get a list of channels. Supports pagination (page/limit) and with_count. Returns paginated HAL list of channels. |
| List Currencies | `listCurrencies` | Get a list of currencies. Supports search filter, pagination (page/limit) and with_count. Returns paginated HAL list of currencies. |
| List Extensions | `listExtensions` | List all UI extensions registered in the PIM. Returns an array of extension objects. |
| List Families | `listFamilies` | Get list of families. Supports search filter, page/limit pagination, and with_count. Returns a paginated HAL collection under _embedded.items. |
| List Family Variants | `listFamilyVariants` | Get list of family variants for a given family. Supports page/limit pagination and with_count. Returns a paginated HAL collection under _embedded.items. |
| List Locales | `listLocales` | Get a list of locales. Supports search filter, pagination (page/limit) and with_count. Returns paginated HAL list of locales. |
| List measurement families | `listMeasurementFamilies` | Get the list of all measurement families (each with code, labels, standard unit and its units with conversion operations). Returns a JSON array, not paginated. |
| List Modelization Suggestions | `listModelizationSuggestions` | Data Architect Agent: get the list of modelization suggestions. Supports filtering by codes, status, source and author plus pagination. |
| List product media files | `listMediaFiles` | Get a paginated list of product media files (their metadata: code, original filename, mime type, size, extension). Supports page/limit/with_count query params. |
| List Product Models | `listProductModels` | Get the paginated list of product models. Supports search, scope, locales, attributes filters and page/search_after pagination. |
| List Products | `listProducts` | List products with optional search filters, pagination, locale/scope filtering. Returns paginated product list. |
| List Products By UUID | `listProductsUuid` | List products keyed by UUID. Supports search filters, pagination (page/search_after), scope/locale/attribute filtering and optional quality/completeness data. Returns a paginated HAL collection under _embedded.items. |
| List Reference Entities | `listReferenceEntities` | Get the list of reference entities. Supports search_after cursor pagination. Returns a HAL collection under _embedded.items. |
| List Reference Entity Attribute Options | `listReferenceEntityAttributeOptions` | Get the list of attribute options for a given attribute of a given reference entity. Returns a JSON array. |
| List Reference Entity Attributes | `listReferenceEntityAttributes` | Get the list of all attributes of a given reference entity. Returns a JSON array of attribute objects. |
| List Reference Entity Records | `listReferenceEntityRecords` | Get the list of records of a specific reference entity. Optionally filter by search, channel, locales. Supports search_after pagination. |
| List Rule Definitions | `listRuleDefinitions` | Get the list of rule definitions. Supports filtering by codes, type, execution_type and enabled. Returns paginated items with code, type, triggers and action_types. |
| List Workflow Step Assignees | `listWorkflowStepAssignees` | Get the list of assignees for a given workflow step, identified by the step UUID. Returns paginated assignee users. |
| List Workflow Tasks | `listWorkflowTasks` | Get the list of workflow tasks. Requires a stringified JSON 'search' filter. Returns paginated tasks with status, product, due date and pending attributes. |
| List Workflows | `listWorkflows` | Get the list of workflows in the PIM. Returns paginated items each with uuid, code, labels and enabled flag. |
| Search Products (UUID) | `searchProductsUuid` | Search products via POST on the UUID endpoint, passing the filter and value-selection options in the JSON body. Pagination options (page/search_after/limit/with_count) are query params. Returns a paginated HAL collection under _embedded.items. |
| Start Workflow Executions | `startWorkflowExecutions` | Start several workflow executions in one call (max 100). Pass an array of execution items, each referencing a workflow (by uuid) and a product (by uuid). |
| Submit Product Model Proposal | `submitProductModelProposal` | Submit a product model draft for approval (proposal). Sends an empty JSON object body; the product model is identified by code in the path. |
| Submit Product Proposal | `submitProductProposal` | Submit a product's draft for approval (POST /products/{code}/proposal). The request body is an empty JSON object. Returns 201 with no body on success. |
| Submit Product Proposal By UUID | `submitProductProposalUuid` | Submit the draft of a product (identified by UUID) for approval, creating a proposal. The request body is an empty JSON object. Returns 201 on success. |
| Update Catalog | `updateCatalog` | Update a catalog by id (PATCH). Send name and/or managed currencies/locales. Returns the updated catalog. |
| Update Extension | `updateExtension` | Update an existing UI extension by UUID (PATCH, JSON variant). All body fields are optional; provide the fields you want to change. |
| Update Extension With File Upload | `updateExtensionFile` | Update a UI extension with a file upload (multipart/form-data) by UUID — used for sdk_script type extensions to upload a built JavaScript file. NOTE: fastn cannot emit binary multipart bodies; verify phase will classify this as blocked. |
| Update Workflow Task Status | `updateWorkflowTask` | Update a workflow task's status by UUID: approve, reject, or complete a review task. 'status' is required. When rejecting a review task, also provide 'send_back_to_step_uuid'; when completing, provide 'pending_attributes'. |
| Upsert Asset | `upsertAsset` | Create or update a single asset of a given asset family (PATCH upsert). |
| Upsert Asset Attribute | `upsertAssetAttribute` | Create or update an attribute of a given asset family (PATCH upsert). The attribute type is immutable once created. |
| Upsert Asset Attribute Option | `upsertAssetAttributeOption` | Create or update an attribute option for a given attribute of a given asset family (PATCH upsert). |
| Upsert Asset Family | `upsertAssetFamily` | Create or update an asset family (PATCH upsert). If the asset family with the given code exists it is updated, otherwise it is created. |
| Upsert Association Type | `upsertAssociationType` | Update or create an association type identified by code in the path (PATCH = upsert). |
| Upsert Attribute | `upsertAttribute` | Create or update a single attribute by code (PATCH upsert). Only the code is templated; pass any additional fields documented in the input contract. |
| Upsert Attribute Group | `upsertAttributeGroup` | Create or update a single attribute group by code (PATCH upsert). |
| Upsert Attribute Option | `upsertAttributeOption` | Create or update a single attribute option by attribute code and option code (PATCH upsert). |
| Upsert Catalog Product Mapping Schema | `upsertCatalogProductMappingSchema` | Create or update (PUT) the product mapping schema related to a catalog. Body is a JSON Schema; $schema and properties are required. |
| Upsert Category | `upsertCategory` | Create or update a single category by code (PATCH upsert). Provide the code in the path; body fields are merged. Returns 201/204 with an empty body. |
| Upsert Channel | `upsertChannel` | Create or update a single channel by code (PATCH upsert). Returns 201/204 with an empty body. |
| Upsert Family | `upsertFamily` | Update or create a single family by code (Akeneo PATCH upsert). Body is a single JSON object. Returns 201 (created) or 204 (updated) with empty body. |
| Upsert Family Variant | `upsertFamilyVariant` | Update or create a single family variant by family code and variant code (Akeneo PATCH upsert). Body is a single JSON object. Returns 201 (created) or 204 (updated) with empty body. |
| Upsert measurement families | `upsertMeasurementFamilies` | Update or create several measurement families at once. Body is a JSON array of measurement family objects (each requires code, standard_unit_code, units). Returns an array of per-line status objects. |
| Upsert Product | `upsertProduct` | Update or create a product by identifier (PATCH /products/{code} = upsert). Sends a partial JSON object; only the supplied fields are modified. Use add_categories / remove_categories for incremental category edits. Returns 204 (updated) or 201 (created) with no body. |
| Upsert Product By UUID | `upsertProductUuid` | Update or create a single product identified by UUID (PATCH is an upsert in Akeneo). Provide only the fields to change. add_categories/remove_categories let you incrementally adjust categories. Returns 204 on success. |
| Upsert Product Model | `upsertProductModel` | Update or create a product model identified by code in the path (PATCH = upsert). Only code is templated; pass values/categories/associations as needed. add_categories/remove_categories adjust categories incrementally. |
| Upsert Products (bulk) | `upsertProductsBulk` | Update or create up to 100 products at once (PATCH /products collection, NDJSON). The 'items' input is a newline-delimited list of product JSON objects (one per line), each with at least an 'identifier'. Content-Type is application/vnd.akeneo.collection+json. Returns one status line per product. |
| Upsert Reference Entity | `upsertReferenceEntity` | Create or update a reference entity (PATCH upsert) identified by its code. Returns 201 (created) or 204 (updated) with an empty body. |
| Upsert Reference Entity Attribute | `upsertReferenceEntityAttribute` | Create or update an attribute of a given reference entity (PATCH upsert). type is required on creation. Returns 201/204 with empty body. |
| Upsert Reference Entity Attribute Option | `upsertReferenceEntityAttributeOption` | Create or update an attribute option for a given attribute of a given reference entity (PATCH upsert). Returns 201/204 with empty body. |
| Upsert Reference Entity Record | `upsertReferenceEntityRecord` | Create or update a single record of a given reference entity (PATCH upsert) identified by record code. Returns 201/204 with empty body. |
| Upsert Reference Entity Records (Bulk) | `upsertReferenceEntityRecords` | Create or update several records of a reference entity in one call. The request body is a JSON array of record objects (each requires code and values). Returns a JSON array of per-record results. |
| Upsert Rule Definition | `upsertRuleDefinition` | Create or update (PUT) a rule definition identified by its code. 'type' and 'actions' are required. Optionally provide conditions, labels, priority, enabled, execution_type, triggers and reference_entity_identifier (required for record rules). |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Product Created | `product.created` | Fired when a product is created in the PIM. The payload event carries the product UUID and identifier. |
| Product Model Created | `product_model.created` | Fired when a product model is created in the PIM. The payload event carries the product model resource (code, family_variant, values). |
| Product Model Removed | `product_model.removed` | Fired when a product model is deleted in the PIM. The payload event carries the removed product model's code. |
| Product Model Updated | `product_model.updated` | Fired when a product model is updated in the PIM. The payload event carries the updated product model resource. |
| Product Removed | `product.removed` | Fired when a product is deleted in the PIM. The payload event carries the removed product's uuid and identifier. |
| Product Updated | `product.updated` | Fired when a product is updated in the PIM. The payload event carries the updated product resource. |
