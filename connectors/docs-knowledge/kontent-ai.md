---
description: "Kontent.ai headless CMS Management API v2 connector."
hidden: true
---

# Kontent.ai

<img src="../../.gitbook/assets/connectors/lg/kontent-ai.png" alt="Kontent.ai logo">

Kontent.ai headless CMS Management API v2 connector. Manage content items, language variants, content types, snippets, taxonomy groups, assets, asset folders and renditions, languages, collections, spaces, workflows, webhooks, roles, and users in a Kontent.ai environment.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [kontent.ai](https://kontent.ai) |
| **Authentication** | Credentials you enter |
| **Slug** | `kontentAi` |

## Use it

Add Kontent.ai from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.kontentAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Web Spotlight | `activateWebSpotlight` | Activates Web Spotlight in the environment using the specified root content type. |
| Add Asset | `addAsset` | Creates a new asset from a previously uploaded file reference. |
| Add Asset Folders | `addAssetFolders` | Creates one or more asset folders, optionally nested. |
| Add Asset Rendition | `addAssetRendition` | Creates a new rendition of an image asset using the specified transformation. |
| Add Content Item | `addContentItem` | Creates a new content item of the specified content type. Element values are set separately using Upsert Language Variant. |
| Add Content Type | `addContentType` | Creates a new content type with the specified elements and content groups. |
| Add Content Type Snippet | `addContentTypeSnippet` | Creates a new content type snippet with the specified elements. |
| Add Custom App | `addCustomApp` | Creates a new custom app in the environment. |
| Add Language | `addLanguage` | Creates a new language in the environment. |
| Add Space | `addSpace` | Creates a new space in the environment. |
| Add Taxonomy Group | `addTaxonomyGroup` | Creates a new taxonomy group with the specified terms. |
| Add Webhook | `addWebhook` | Creates a new webhook that sends notifications to the specified URL when the configured events occur. |
| Add Workflow | `addWorkflow` | Creates a new workflow with the specified steps and scopes. |
| Bulk Get Items With Variants | `bulkGetItemsWithVariants` | Retrieves a batch of language variants together with their content items, identified by item and language pairs. |
| Cancel Scheduled Publishing Of Language Variant | `cancelScheduledPublishingOfLanguageVariant` | Cancels a previously scheduled publishing of a language variant. |
| Cancel Scheduled Unpublishing Of Language Variant | `cancelScheduledUnpublishingOfLanguageVariant` | Cancels a previously scheduled unpublishing of a language variant. |
| Change Live Preview Configuration | `changeLivePreviewConfiguration` | Updates the live preview configuration of the environment. |
| Change Project User Roles | `changeProjectUserRoles` | Changes the roles assigned to a user in the environment. |
| Change Workflow Of Language Variant | `changeWorkflowOfLanguageVariant` | Moves a language variant to a specific step of a specific workflow. |
| Change Workflow Step Of Language Variant | `changeWorkflowStepOfLanguageVariant` | Moves a language variant to a specific workflow step. |
| Check Environment Validation | `checkEnvironmentValidation` | Retrieves the status of an asynchronous environment validation task. |
| Check Web Spotlight Status | `checkWebSpotlightStatus` | Retrieves the current Web Spotlight status of the environment. |
| Clone Environment | `cloneEnvironment` | Creates a new environment by cloning the current one. Requires the Manage environments permission. |
| Create New Version Of Language Variant | `createNewVersionOfLanguageVariant` | Creates a new draft version of a published language variant so it can be edited. |
| Deactivate Web Spotlight | `deactivateWebSpotlight` | Deactivates Web Spotlight in the environment. |
| Delete Asset | `deleteAsset` | Deletes an asset from the environment. |
| Delete Content Item | `deleteContentItem` | Deletes a content item and all of its language variants. |
| Delete Content Type | `deleteContentType` | Deletes a content type. The content type must not be used by any content items. |
| Delete Content Type Snippet | `deleteContentTypeSnippet` | Deletes a content type snippet. The snippet must not be used by any content type. |
| Delete Custom App | `deleteCustomApp` | Deletes a custom app from the environment. |
| Delete Environment | `deleteEnvironment` | Permanently deletes the environment identified by the connection. This operation is irreversible and removes all content in the environment. |
| Delete Language Variant | `deleteLanguageVariant` | Deletes a specific language variant of a content item. The content item itself is not deleted. |
| Delete Space | `deleteSpace` | Deletes a space from the environment. |
| Delete Taxonomy Group | `deleteTaxonomyGroup` | Deletes a taxonomy group. The taxonomy group must not be used by any content type. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook from the environment. |
| Delete Workflow | `deleteWorkflow` | Deletes a workflow. The default workflow cannot be deleted. |
| Disable Webhook | `disableWebhook` | Disables a webhook so it stops sending notifications. |
| Enable Webhook | `enableWebhook` | Enables a webhook so it starts sending notifications. |
| Filter Items With Variants | `filterItemsWithVariants` | Retrieves content items together with their language variants, filtered and ordered by the specified criteria. |
| Get Custom App | `getCustomApp` | Retrieves a single custom app by its internal ID or codename. |
| Get Environment Cloning State | `getEnvironmentCloningState` | Retrieves the current cloning state of the environment. |
| Get Environment Information | `getEnvironmentInformation` | Retrieves basic information about the current Kontent.ai environment, including its ID, project name, environment name, and whether it is the production environment. |
| Get Live Preview Configuration | `getLivePreviewConfiguration` | Retrieves the live preview configuration of the environment. |
| Get Preview Configuration | `getPreviewConfiguration` | Retrieves the preview configuration of the environment, including space domains and preview URL patterns. |
| Get Taxonomy Group | `getTaxonomyGroup` | Retrieves a single taxonomy group by its internal ID, codename, or external ID. |
| Get Webhook | `getWebhook` | Retrieves a single webhook by its internal ID. |
| Invite Project User | `inviteProjectUser` | Invites a user to the environment and assigns them the specified roles. |
| List Asset Folders | `listAssetFolders` | Retrieves the full tree of asset folders in the environment. |
| List Asset Renditions | `listAssetRenditions` | Retrieves all renditions of a specific asset. |
| List Assets | `listAssets` | Retrieves a list of all assets in the environment. |
| List Collections | `listCollections` | Retrieves a list of all collections in the environment. |
| List Content Items | `listContentItems` | Retrieves a list of all content items in the environment. |
| List Content Type Snippets | `listContentTypeSnippets` | Retrieves a list of all content type snippets in the environment. |
| List Content Types | `listContentTypes` | Retrieves a list of all content types in the environment. |
| List Custom Apps | `listCustomApps` | Retrieves a list of all custom apps in the environment. |
| List Environment Validation Issues | `listEnvironmentValidationIssues` | Retrieves the list of issues found by a completed environment validation task. |
| List Language Variants By Collection | `listLanguageVariantsByCollection` | Retrieves all language variants of content items that belong to a specific collection. |
| List Language Variants By Space | `listLanguageVariantsBySpace` | Retrieves all language variants of content items that belong to a specific space. |
| List Language Variants Of Content Type | `listLanguageVariantsOfContentType` | Retrieves all language variants that are based on a specific content type. |
| List Language Variants Of Content Type With Components | `listLanguageVariantsOfContentTypeWithComponents` | Retrieves all language variants that use a specific content type, including variants where the type is used as a component inside rich text. |
| List Language Variants Of Item | `listLanguageVariantsOfItem` | Retrieves all language variants of a specific content item. |
| List Languages | `listLanguages` | Retrieves a list of all languages in the environment. |
| List Roles | `listRoles` | Retrieves a list of all roles defined in the environment. |
| List Spaces | `listSpaces` | Retrieves a list of all spaces in the environment. |
| List Taxonomy Groups | `listTaxonomyGroups` | Retrieves a list of all taxonomy groups in the environment. |
| List Webhooks | `listWebhooks` | Retrieves a list of all webhooks configured in the environment. |
| List Workflow Steps | `listWorkflowSteps` | Retrieves the steps of the default workflow in the environment. |
| List Workflows | `listWorkflows` | Retrieves a list of all workflows in the environment, including their steps and scopes. |
| Mark Environment As Production | `markEnvironmentAsProduction` | Marks the current environment as the production environment. Requires the Manage environments permission. |
| Modify Asset Folders | `modifyAssetFolders` | Modifies the asset folder tree using a list of operations, such as adding, renaming, or removing folders. |
| Modify Asset Rendition | `modifyAssetRendition` | Updates the transformation of an existing asset rendition. |
| Modify Content Type | `modifyContentType` | Modifies a content type using a list of operations, such as adding, removing, or replacing elements and properties. |
| Modify Content Type Snippet | `modifyContentTypeSnippet` | Modifies a content type snippet using a list of operations, such as adding, removing, or replacing elements. |
| Modify Custom App | `modifyCustomApp` | Modifies a custom app using a list of operations, such as replacing its name, source URL, or allowed roles. |
| Modify Environment | `modifyEnvironment` | Renames the current environment. Requires the Manage environments permission. |
| Modify Language | `modifyLanguage` | Modifies a language using a list of operations, such as replacing its name, codename, activity, or fallback language. |
| Modify Preview Configuration | `modifyPreviewConfiguration` | Replaces the preview configuration of the environment with the space domains and preview URL patterns provided. |
| Modify Space | `modifySpace` | Modifies a space using a list of operations, such as replacing its name, codename, collections, or Web Spotlight root item. |
| Modify Taxonomy Group | `modifyTaxonomyGroup` | Modifies a taxonomy group using a list of operations, such as adding, removing, or replacing terms. |
| Publish Language Variant | `publishLanguageVariant` | Publishes a language variant immediately, or schedules it to be published at a specific time. |
| Set Collections | `setCollections` | Modifies the collections in the environment using a list of operations, such as adding, renaming, moving, or removing collections. |
| Start Environment Validation | `startEnvironmentValidation` | Starts an asynchronous validation of the environment and returns the ID of the validation task. |
| Unpublish Language Variant | `unpublishLanguageVariant` | Unpublishes and archives a language variant immediately, or schedules it to be unpublished at a specific time. |
| Update Content Item | `updateContentItem` | Updates the name, codename, or collection of an existing content item. |
| Update Workflow | `updateWorkflow` | Updates an existing workflow, replacing its steps and scopes with the values provided. |
| Upload Binary File | `uploadBinaryFile` | Uploads a binary file and returns a file reference that can be used to create an asset. Send the raw file content as the request body. |
| Upsert Asset | `upsertAsset` | Updates an existing asset, or creates it when referenced by an external ID that does not exist yet. |
| Upsert Content Item By External ID | `upsertContentItemByExternalId` | Creates a content item with the given external ID, or updates it if an item with that external ID already exists. |
| Upsert Language Variant | `upsertLanguageVariant` | Creates or updates a language variant of a content item with the specified element values. |
| Validate Environment | `validateEnvironment` | Runs a synchronous validation of the environment and returns any content type and language variant issues. |
| View Asset | `viewAsset` | Retrieves a single asset by its internal ID or external ID. |
| View Asset Rendition | `viewAssetRendition` | Retrieves a single rendition of an asset. |
| View Content Item | `viewContentItem` | Retrieves a single content item by its internal ID, codename, or external ID. |
| View Content Type | `viewContentType` | Retrieves a single content type by its internal ID, codename, or external ID. |
| View Content Type Snippet | `viewContentTypeSnippet` | Retrieves a single content type snippet by its internal ID, codename, or external ID. |
| View Language | `viewLanguage` | Retrieves a single language by its internal ID, codename, or external ID. |
| View Language Variant | `viewLanguageVariant` | Retrieves a specific language variant of a content item. |
| View Role | `viewRole` | Retrieves a single role by its internal ID or codename. |
| View Space | `viewSpace` | Retrieves a single space by its internal ID or codename. |
