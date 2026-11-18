---
description: "Manage and deliver structured content with Contentful."
---

# Contentful

Manage and deliver structured content with Contentful. Covers the Content Management API (spaces, environments, content types, entries, assets, locales, webhooks, roles, API keys, uploads, tags, and content releases) and the Content Delivery API for reading published content.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [contentful.com](https://contentful.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 207 |
| **Events** | 0 |
| **Slug** | `contentful` |

## Use it

Add Contentful from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.contentful.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Asset | `archiveAsset` | Archives a media asset, hiding it from normal listings without deleting it. An asset must be unpublished before it can be archived. |
| Archive Entry | `archiveEntry` | Archives an entry, hiding it from normal listings without deleting it. An entry must be unpublished before it can be archived. |
| Archive Release | `archiveRelease` | Archives a release, disabling further publish, unpublish, and scheduling actions on it. Requires the release's current version for optimistic concurrency control. |
| Bulk Publish | `createBulkPublish` | Publish many entries/assets in one bulk action. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Bulk Unpublish | `createBulkUnpublish` | Unpublish many entries/assets. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Bulk Validate | `createBulkValidate` | Validate many entries/assets for publishing. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Cancel Scheduled Action | `cancelScheduledAction` | Cancel (delete) a scheduled action. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Complete Workflow | `completeWorkflow` | Complete a workflow. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create API Key | `createApiKey` | Creates a new Content Delivery API key for a space, along with a matching Preview API key. |
| Create Asset | `createAsset` | Creates a new media asset from a source file URL. The asset must be processed and published before it is usable. |
| Create Asset Key | `createAssetKey` | Create a key for signing embargoed asset URLs. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create Content Type | `createContentType` | Creates a new content type model in a space environment, defining its display name and field schema. |
| Create Entry | `createEntry` | Creates a new entry of the given content type. Field values are keyed by field ID, and each field value is keyed by locale code. |
| Create Entry Comment | `createEntryComment` | Comment on an entry. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create Entry Task | `createEntryTask` | Create a task on an entry. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create Environment | `createEnvironment` | Creates a new environment in a Contentful space, optionally cloned from a source environment. |
| Create Locale | `createLocale` | Adds a new locale to a space environment. |
| Create or Update Environment Alias | `updateEnvironmentAlias` | Point an environment alias at a target environment. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create or Update UI Extension | `updateExtension` | Create (with id) or update a UI extension. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create Organization Invitation | `createOrganizationInvitation` | Invite a person to the organization by email (sends an email). Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create Personal Access Token | `createPersonalAccessToken` | Create a personal access token (the token value is returned once). Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create Release | `createRelease` | Creates a content release: a named, orderable batch of entries and assets that can be validated and published together. |
| Create Role | `createRole` | Creates a custom role defining what space members assigned to it can see and do. |
| Create Scheduled Action | `createScheduledAction` | Schedule publish/unpublish of an entry, asset or release. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create Space | `createSpace` | Creates a new Contentful space under the given organization. |
| Create Space Membership | `createSpaceMembership` | Add an organization user to the space. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create Tag | `createTag` | Creates a new tag with the given ID in a space environment, which can then be applied to entries and assets. |
| Create Team | `createTeam` | Create a team. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create Team Membership | `createTeamMembership` | Add an organization member to a team. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create Team Space Membership | `createTeamSpaceMembership` | Give a team access to the space. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create UI Extension | `createExtension` | Create a UI extension. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create Upload | `createUpload` | Uploads a file's raw content to the Uploads API, returning an upload ID that can be referenced when creating an asset. Text content round-trips correctly; binary files should be uploaded out of band and referenced by external URL on Create Asset instead, since generic passthrough tooling cannot guarantee byte-exact binary transport. |
| Create Webhook | `createWebhook` | Creates a webhook definition that notifies an external URL when selected content events occur in the space. |
| Create Workflow | `createWorkflow` | Start a workflow on an entry. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Create Workflow Definition | `createWorkflowDefinition` | Create a workflow definition. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Delete API Key | `deleteApiKey` | Permanently deletes a Content Delivery API key from a space. |
| Delete Asset | `deleteAsset` | Permanently deletes an unpublished media asset. This action cannot be undone. |
| Delete Content Type | `deleteContentType` | Permanently deletes an unpublished content type. This action cannot be undone. |
| Delete Entry | `deleteEntry` | Permanently deletes an unpublished entry. This action cannot be undone. |
| Delete Entry Comment | `deleteEntryComment` | Delete a comment. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Delete Entry Task | `deleteEntryTask` | Delete a task. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Delete Environment | `deleteEnvironment` | Permanently deletes an environment and all of its content. This action cannot be undone. |
| Delete Environment Alias | `deleteEnvironmentAlias` | Delete an environment alias (not master). Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Delete Locale | `deleteLocale` | Permanently removes a locale from a space environment. |
| Delete Organization Membership | `deleteOrganizationMembership` | Remove a user from the organization. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Delete Release | `deleteRelease` | Permanently deletes a content release. This does not affect the publish state of the entities it referenced. |
| Delete Role | `deleteRole` | Permanently deletes a custom role from a space. |
| Delete Space | `deleteSpace` | Permanently deletes a Contentful space and all of its content. This action cannot be undone. |
| Delete Space Membership | `deleteSpaceMembership` | Remove a user from the space. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Delete Tag | `deleteTag` | Permanently deletes a tag from a space environment. Requires the tag's current version for optimistic concurrency control. |
| Delete Team | `deleteTeam` | Delete a team. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Delete Team Membership | `deleteTeamMembership` | Remove a user from a team. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Delete Team Space Membership | `deleteTeamSpaceMembership` | Remove a team from the space. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Delete UI Extension | `deleteExtension` | Delete a UI extension. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Delete Webhook | `deleteWebhook` | Permanently deletes a webhook definition from a space. |
| Delete Webhook Signing Secret | `deleteWebhookSigningSecret` | Remove the webhook signing secret. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Delete Workflow | `deleteWorkflow` | Delete a workflow. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Delete Workflow Definition | `deleteWorkflowDefinition` | Delete a workflow definition. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Aggregated Usage | `getAggregatedUsage` | Aggregated usage of one metric for the organization (Usage API). Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get API Key | `getApiKey` | Retrieves a single Content Delivery API key by ID. |
| Get App Installation | `getAppInstallation` | Get the installation of one app. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Asset | `getAsset` | Retrieves a single media asset by ID. |
| Get Asset Bandwidth Usage Detailed | `getAssetBandwidthUsageDetailed` | Detailed asset bandwidth usage for the organization. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Bulk Action | `getBulkAction` | Get the status of a bulk action. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Content Type | `getContentType` | Retrieves a single content type model and its field definitions. |
| Get Content Type Snapshot | `getContentTypeSnapshot` | Get one snapshot of a content type. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Current User | `getCurrentUser` | Get the user that owns the access token. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Delivery Asset | `cdaGetAsset` | Retrieves a single published media asset via the Content Delivery API. |
| Get Delivery Content Type | `cdaGetContentType` | Retrieves a single content type model via the Content Delivery API. |
| Get Delivery Entry | `cdaGetEntry` | Retrieves a single published entry via the Content Delivery API. |
| Get Delivery Space | `cdaGetSpace` | Retrieves space metadata via the Content Delivery API, using a space-scoped delivery access token. |
| Get Editor Interface | `getEditorInterface` | Retrieves the editor interface configuration (field widget assignments) for a content type. |
| Get Entry | `getEntry` | Retrieves a single entry by ID, including its field values and system metadata. |
| Get Entry Comment | `getEntryComment` | Get one comment. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Entry References | `getEntryReferences` | Get an entry with all linked entries/assets resolved. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Entry Snapshot | `getEntrySnapshot` | Get one snapshot of an entry. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Entry Task | `getEntryTask` | Get one task. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Environment | `getEnvironment` | Retrieves a single environment from a Contentful space. |
| Get Environment Alias | `getEnvironmentAlias` | Get an environment alias (e.g. master). Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Locale | `getLocale` | Retrieves a single locale configured for a space environment. |
| Get Organization Invitation | `getOrganizationInvitation` | Get one organization invitation. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Organization Membership | `getOrganizationMembership` | Get one organization membership. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Organization Space Membership | `getOrganizationSpaceMembership` | Get one space membership at organization level. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Organization User | `getOrganizationUser` | Get one user of an organization. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Personal Access Token | `getPersonalAccessToken` | Get one personal access token. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Preview API Key | `getPreviewApiKey` | Retrieves a single Content Preview API key by ID. |
| Get Release | `getRelease` | Retrieves a single content release by ID. |
| Get Release Action | `getReleaseAction` | Retrieves the status and outcome of an asynchronous release action (validate, publish, or unpublish). |
| Get Role | `getRole` | Retrieves a single role by ID, including its feature permissions and content policies. |
| Get Scheduled Action | `getScheduledAction` | Get one scheduled action. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Space | `getSpace` | Retrieves a single Contentful space by its ID. |
| Get Space Member | `getSpaceMember` | Get one space member. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Space Membership | `getSpaceMembership` | Get one space membership. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Space User | `getSpaceUser` | Get one user of a space. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Tag | `getTag` | Retrieves a single tag by ID. |
| Get Team | `getTeam` | Get one team. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Team Membership | `getTeamMembership` | Get one team membership. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Team Space Membership | `getTeamSpaceMembership` | Get one team space membership. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get UI Config | `getUiConfig` | Get the shared UI config (saved views) of the environment. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get UI Extension | `getExtension` | Get a UI extension. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Upload | `getUpload` | Retrieves metadata for a previously created file upload, including its expiration time. |
| Get User UI Config | `getUserUiConfig` | Get the current user UI config. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Webhook | `getWebhook` | Retrieves a single webhook definition by ID. |
| Get Webhook Call Details | `getWebhookCallDetails` | Retrieves the full request and response detail for a single webhook delivery attempt. |
| Get Webhook Health | `getWebhookHealth` | Retrieves the recent call success rate for a webhook, indicating whether deliveries are succeeding. |
| Get Webhook Signing Secret | `getWebhookSigningSecret` | Get the (redacted) webhook signing secret. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Workflow | `getWorkflow` | Get a workflow. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Get Workflow Definition | `getWorkflowDefinition` | Get a workflow definition. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Install or Update App | `upsertAppInstallation` | Install an app or update its parameters. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List API Keys | `listApiKeys` | Lists the Content Delivery / Preview API keys issued for a space. |
| List App Installations | `listAppInstallations` | List apps installed in the environment. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Assets | `listAssets` | Lists the media assets in a space environment. |
| List Content Type Snapshots | `listContentTypeSnapshots` | List snapshots of a content type. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Content Types | `listContentTypes` | Lists the content type models defined in a space environment. |
| List Delivery Assets | `cdaListAssets` | Lists published media assets via the Content Delivery API. |
| List Delivery Content Types | `cdaListContentTypes` | Lists content type models visible to the Content Delivery API in a space environment. |
| List Delivery Entries | `cdaListEntries` | Lists published entries via the Content Delivery API, optionally filtered by content type. |
| List Delivery Locales | `cdaListLocales` | Lists the locales available through the Content Delivery API for a space environment. |
| List Delivery Tags | `cdaListTags` | Lists the tags visible through the Content Delivery API for a space environment. |
| List Editor Interfaces | `listEditorInterfaces` | List editor interfaces of all content types. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Eligible Licenses | `listEligibleLicenses` | List licenses the space is eligible for. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Entries | `listEntries` | Lists entries in a space environment, optionally filtered by content type. |
| List Entry Comments | `listEntryComments` | List comments on an entry. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Entry Snapshots | `listEntrySnapshots` | List snapshots (published versions) of an entry. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Entry Tasks | `listEntryTasks` | List tasks on an entry. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Environment Aliases | `listEnvironmentAliases` | List environment aliases of a space. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Environments | `listEnvironments` | Lists every environment defined in a Contentful space. |
| List Locales | `listLocales` | Lists the locales configured for a space environment. |
| List Organization Access Tokens | `listOrganizationAccessTokens` | List personal access tokens across the organization (org admin). Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Organization Memberships | `listOrganizationMemberships` | List organization memberships. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Organization Periodic Usage | `listOrganizationUsage` | DEPRECATED by Contentful (sunset 2027-02-28; use Get Aggregated Usage). Get API usage for the organization. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Organization Roles | `listOrganizationRoles` | List space roles across the organization. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Organization Space Memberships | `listOrganizationSpaceMemberships` | List space memberships across all spaces of an organization. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Organization Spaces | `listOrganizationSpaces` | List spaces in an organization (org admin/owner). Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Organization Team Memberships | `listOrganizationTeamMemberships` | List all team memberships of an organization. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Organization Team Space Memberships | `listOrganizationTeamSpaceMemberships` | List team space memberships across an organization. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Organization Users | `listOrganizationUsers` | List users in an organization. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Organizations | `listOrganizations` | List organizations the token user belongs to. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Personal Access Tokens | `listPersonalAccessTokens` | List personal access tokens of the current user. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Preview API Keys | `listPreviewApiKeys` | List Content Preview API keys. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Published Assets | `listPublishedAssets` | List published assets through the CMA. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Published Content Types | `listPublishedContentTypes` | List activated content types. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Published Entries | `listPublishedEntries` | List published entries through the CMA. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Release Actions | `listReleaseActions` | Lists release actions (validate, publish, unpublish attempts) across all releases in a space environment. |
| List Release Assets | `listReleaseAssets` | List assets pinned in a release (release v2 / timeline). Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Release Entries | `listReleaseEntries` | List entries pinned in a release (release v2 / timeline). Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Releases | `listReleases` | Lists content releases (batched sets of entries and assets scheduled to publish together) in a space environment. |
| List Roles | `listRoles` | Lists the custom roles defined for a space. |
| List Scheduled Actions | `listScheduledActions` | List scheduled actions (environment.sys.id is required by the API). Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Space Add-ons | `listSpaceAddOns` | List add-ons allocated to the space. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Space Members | `listSpaceMembers` | List space members (users with effective access). Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Space Memberships | `listSpaceMemberships` | List space memberships. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Space Periodic Usage | `listSpaceUsage` | DEPRECATED by Contentful (sunset 2027-02-28; use Get Aggregated Usage). Get API usage per space. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Space Teams | `listSpaceTeams` | List teams with access to the space. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Space Users | `listSpaceUsers` | List users of a space. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Spaces | `listSpaces` | Lists every Contentful space the authenticated Content Management API token can access. |
| List Tags | `listTags` | Lists the tags defined in a space environment. |
| List Team Memberships | `listTeamMemberships` | List memberships of one team. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Team Space Memberships | `listTeamSpaceMemberships` | List team space memberships. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Teams | `listTeams` | List teams of an organization. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List UI Extensions | `listExtensions` | List UI extensions. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Webhook Call Details | `listWebhookCallDetails` | Lists recent delivery attempts (calls) made for a webhook, most recent first. |
| List Webhooks | `listWebhooks` | Lists the webhook definitions configured on a space. |
| List Workflow Definitions | `listWorkflowDefinitions` | List workflow definitions. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Workflows | `listWorkflows` | List workflows. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| List Workflows Changelog | `listWorkflowsChangelog` | Workflow change history for an entity. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Patch Entry | `patchEntry` | Apply a JSON Patch to an entry. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Process Asset | `processAsset` | Processes a newly created asset's source file for a given locale, generating the final Contentful-hosted file. Required before the asset can be published. |
| Publish Asset | `publishAsset` | Publishes a processed asset, making it available through the Content Delivery API. |
| Publish Content Type | `publishContentType` | Publishes a content type so entries of that type can be created and published. |
| Publish Entry | `publishEntry` | Publishes an entry, making it available through the Content Delivery API. |
| Publish Release | `publishRelease` | Asynchronously publishes every entity in a release. Poll Get Release Action for completion status. |
| Revoke Personal Access Token | `revokePersonalAccessToken` | Revoke a personal access token. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Sync Space | `cdaSync` | Performs an initial or incremental sync of all published content in a space environment via the Content Delivery API. Pass a previously returned sync token to continue an existing sync. |
| Unarchive Asset | `unarchiveAsset` | Unarchives a previously archived media asset, restoring it to normal listings. |
| Unarchive Entry | `unarchiveEntry` | Unarchives a previously archived entry, restoring it to normal listings. |
| Unarchive Release | `unarchiveRelease` | Unarchives a release, re-enabling publish, unpublish, and scheduling actions on it. Requires the release's current version for optimistic concurrency control. |
| Uninstall App | `deleteAppInstallation` | Uninstall an app. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Unpublish Asset | `unpublishAsset` | Unpublishes a media asset, removing it from the Content Delivery API while keeping it in the space. |
| Unpublish Content Type | `unpublishContentType` | Unpublishes a content type. Entries of this type can no longer be created or published until it is republished. |
| Unpublish Entry | `unpublishEntry` | Unpublishes an entry, removing it from the Content Delivery API while keeping it in the space. |
| Unpublish Release | `unpublishRelease` | Asynchronously unpublishes every entity in a release. Poll Get Release Action for completion status. |
| Update API Key | `updateApiKey` | Updates the name, description, or environment scope of an existing API key. Requires the key's current version for optimistic concurrency control. |
| Update Asset | `updateAsset` | Replaces the field values of an existing media asset. Requires the asset's current version for optimistic concurrency control. |
| Update Content Type | `updateContentType` | Updates the name, description, or field schema of an existing content type. Requires the content type's current version for optimistic concurrency control. |
| Update Editor Interface | `updateEditorInterface` | Assigns the editor widget used for each field of a content type in the Contentful web app. |
| Update Entry | `updateEntry` | Replaces the field values of an existing entry. Requires the entry's current version for optimistic concurrency control. |
| Update Entry Comment | `updateEntryComment` | Update a comment. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Update Entry Task | `updateEntryTask` | Update a task. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Update Environment | `updateEnvironment` | Renames an existing environment. Requires the environment's current version for optimistic concurrency control. |
| Update Locale | `updateLocale` | Updates the settings of an existing locale. Requires the locale's current version for optimistic concurrency control. |
| Update Organization Membership | `updateOrganizationMembership` | Change the role of an organization membership. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Update Release | `updateRelease` | Updates the title or entity list of an existing release. Requires the release's current version for optimistic concurrency control. |
| Update Role | `updateRole` | Updates the permissions and policies of an existing role. Requires the role's current version for optimistic concurrency control. |
| Update Scheduled Action | `updateScheduledAction` | Update a scheduled action. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Update Space | `updateSpace` | Renames an existing Contentful space. Requires the space's current version for optimistic concurrency control. |
| Update Space Membership | `updateSpaceMembership` | Update roles/admin flag of a space membership. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Update Tag | `updateTag` | Renames an existing tag. Requires the tag's current version for optimistic concurrency control. |
| Update Team | `updateTeam` | Update a team. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Update Team Space Membership | `updateTeamSpaceMembership` | Update a team space membership. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Update UI Config | `updateUiConfig` | Update the shared UI config. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Update User UI Config | `updateUserUiConfig` | Update the current user UI config. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Update Webhook | `updateWebhook` | Updates the configuration of an existing webhook definition. Requires the webhook's current version for optimistic concurrency control. |
| Update Workflow | `updateWorkflow` | Move a workflow to another step. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Update Workflow Definition | `updateWorkflowDefinition` | Update a workflow definition. Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Upsert Webhook Signing Secret | `upsertWebhookSigningSecret` | Set the webhook signing secret (64 chars). Docs: https://www.contentful.com/developers/docs/references/content-management-api/ |
| Validate Release | `validateRelease` | Asynchronously validates that every entity in a release can be published. Only one validation can run per release at a time; poll Get Release Action for the result. |
