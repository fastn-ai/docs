---
description: "Sanity is a headless content operating system."
hidden: true
---

# Sanity

<img src="../../.gitbook/assets/connectors/sanity.png" alt="Sanity logo" width="64">

Sanity is a headless content operating system. Query and mutate content in the Content Lake with GROQ, manage documents, drafts, versions and Content Releases, upload assets, and administer projects, datasets, members, roles, tokens and webhooks through the Sanity Management API.

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [sanity.io](https://sanity.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `sanity` |

## Use it

Add Sanity from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sanity.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Access Request | `acceptAccessRequest` | Permissions `sanity.{resourceType}.members.invite`. |
| Accept Invite | `acceptInvite` | Accepts an invite using its token. Attempting to accept an invite that is already accepted or revoked will result in a Bad Request error. Once the invite has been accepted, the user will have access to the resource with the role assigned as part of the invitation. &gt; **Access is propagated internally and may take a up to a few minutes to &gt; be fully available across all systems.** ### Unavailable resources If the underlying resource is unavailable then a Bad Request error will be returned. A common example of an unavailable resource is a project that is blocked or archived. ### Member quota Some resources have a limit on the number of members. If accepting an invite would go over this limit, then a Payment Required error is returned. ### Authorization This endpoint requires an authenticated user session. |
| Add Role To Organization Member | `addRoleToOrganizationMember` | Add a role to a member in an organization. |
| Add Role To Project Member | `addRoleToProjectMember` | Add a role to a user in a project. |
| Add Role To User | `addRoleToUser` | Add a role to a user. Requires permission - `sanity.{resourceType}.members.update`. |
| Apply Organization Default Role | `applyOrganizationDefaultRole` | Add default role to all resource users. Limited to Organization. Requires permission - `sanity.organization.members.update`. |
| Archive Content Release | `archiveContentRelease` | Archives a content release, removing it from the active releases. Its documents stay in retention and remain reachable through the History API. |
| Assign Tag To Dataset | `assignTagToDataset` | Assigns a tag to a dataset. |
| Check My Access Permissions | `checkMyAccessPermissions` | Checks whether the current user holds one permission on the given resource. Returns an object mapping the requested permission to true or false. Check one permission per call. |
| Check Studio Host Availability | `checkStudioHostAvailability` | Check if a studio host is available. |

<details>

<summary>See 218 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Copy Dataset | `copyDataset` | Copies a dataset to a new dataset. This is a feature available to Business and Enterprise customers. |
| Create Access Permission | `createAccessPermission` | Creates a custom permission on a resource. &lt;br /&gt; &lt;br /&gt; Requires permission: `sanity.{resourceType}.roles.create` &lt;br /&gt; Requires feature: `advancedRolesManagement` &lt;br /&gt; &lt;br /&gt; See Example. It creates a permission to allow a user to read legal documents in project `c7ja4siy` and dataset `production`. |
| Create Access Request | `createAccessRequest` | Creates a new request for the given project/organization. Requires an authenticated user. |
| Create Access Role | `createAccessRole` | Requires permission: - `sanity.{resourceType}.roles.create` Requires feature: - `advancedRolesManagement`. |
| Create Application | `createApplication` | Create an application in the registry. Requires the `sanity.sdk.applications.deploy` grant. |
| Create Attribute Definition | `createAttributeDefinition` | Create a new Sanity (API-managed) attribute definition for an organization. This endpoint **only creates Sanity definitions**. SAML definitions are automatically created during SSO authentication and cannot be created through this API. **Important restrictions:** - **Cannot create Sanity definition when SAML definition exists**: If a SAML definition already exists for the key, this endpoint returns 403 Forbidden. Sanity definitions for SAML attributes are automatically created when you set the first Sanity value for that attribute. - **Existing Sanity definitions**: If a Sanity definition with the same key already exists, it returns the existing definition with `alreadyExists: true`. - **Type validation**: If a definition exists with a different type, returns 409 Conflict. ### Permissions Requires `sanity.organization.manage` permission. |
| Create Content Release | `createContentRelease` | Creates a content release, a named bundle of document versions that can be published together. The release ID must not have been used by a previously published or archived release. |
| Create CORS Origin | `createCORSOrigin` | Adds a new CORS origin for a project. |
| Create Dataset | `createDataset` | Creates a new dataset in the project. |
| Create Document | `createDocument` | Creates a new document in a dataset. Fails if a document with the same ID already exists. If _id is omitted a random ID is generated; if _id ends with a dot it is used as a prefix for a generated ID. |
| Create Document Draft | `createDocumentDraft` | Creates a draft or release version of a document through the Actions API. The document _id must be prefixed with drafts. or versions.&lt;release&gt;. and the remainder must equal the published ID. |
| Create Document If Not Exists | `createDocumentIfNotExists` | Creates a document only if no document with that ID exists. If one already exists the mutation succeeds without changing anything. The document must include an _id. |
| Create Document Version | `createDocumentVersion` | Creates a version of a document inside a content release. Either supply the complete version document, or supply a version ID together with the ID of an existing document to copy from. |
| Create Embeddings Index | `createEmbeddingsIndex` | Create a new embeddings index for an existing dataset in a Sanity project. |
| Create Invite | `createInvite` | Creates an invite for the specified resource. The invitee will receive an email with a link to accept the invite. Each invitee can only receive one invite per resource and role. Attempting to create an invite using a non-existent role, or a role that cannot be granted to users will result in a Bad Request error. ### Unavailable resources If the underlying resource is unavailable then a Bad Request error will be returned. A common example of an unavailable resource is a project that is blocked or archived. ### Authorization This endpoint requires an authenticated user session with the following permissions: - `sanity.{resourceType}.members.invite` Additionally, only administrators can invite other administrators. |
| Create Media Library Signing Key | `createMediaLibrarySigningKey` | Create a new signing key. |
| Create Or Replace Document | `createOrReplaceDocument` | Creates a document, or completely replaces it if a document with the same ID already exists. The document must include an _id. Any field not present in the supplied document is removed. |
| Create Project | `createProject` | Creates a new Sanity project. |
| Create Project Grant | `createProjectGrant` | Create a grant for in a project. Supply an ID from a permission resource to create a grant linked to that resource. This grant can then be assigned to a user. |
| Create Project Role | `createProjectRole` | Create a role in a project. |
| Create Project Tag | `createProjectTag` | Creates a new tag for the project. Datasets cannot be assigned at tag creation. Use the PUT endpoint to assign datasets to the tag. |
| Create Project Token | `createProjectToken` | Creates a new token for the project. |
| Create Project User Application | `createProjectUserApplication` | Create a user application for a project. |
| Create Robot Token | `createRobotToken` | Creates a robot with the specified role grants and returns its secret token. Only the specified resource and its children resources can be specified in the role grants. The robot will not have access to other resources. ### Secret token The secret token is returned only once and cannot be retrieved again. If it is compromised, the token holder can replace it through the self-service rotate endpoint. If it is lost, create a replacement robot and delete this one. ### Email notifications For project robots, an email notification is sent to all project administrators by default when a robot is created. This can be disabled by setting `sendNotification=false`, but only for projects created within the last 5 minutes. ### Authorization This endpoint requires an authenticated user session with the following permissions: - `sanity.{resourceType}.tokens.create`. |
| Create Schedule | `createSchedule` | Creates a schedule that publishes or unpublishes a set of documents at a future time. The schedule name, execution time, action and documents are all sent in the request body. |
| Create User Application | `createUserApplication` | Create a user application. Either a project ID or an organization ID must be supplied. |
| Create User Application Data | `createUserApplicationData` | Create user application data. |
| Create Webhook | `createWebhook` | Create a webhook. |
| Decline Access Request | `declineAccessRequest` | Permissions `sanity.{resourceType}.members.invite`. |
| Delete Access Permission | `deleteAccessPermission` | Deletes a specific permission for a resource. Can only be used with custom permissions. Requires permission - `sanity.{resourceType}.roles.delete` Requires feature: - `advancedRolesManagement`. |
| Delete Access Role | `deleteAccessRole` | Requires permission: - `sanity.{resourceType}.roles.delete` for resource scoped roles (e.g. project admin) Requires feature: - `advancedRolesManagement` Cannot delete a role that is assigned to a user. The role needs to be removed from users first. |
| Delete All Project User Applications | `deleteAllProjectUserApplications` | Deletes all user applications for a project. Requires a service token. |
| Delete Application | `deleteApplication` | Soft-delete an application and all its deployments. Requires the `sanity.sdk.applications.delete` grant. Singletons with active installations cannot be deleted. |
| Delete Attribute Definition | `deleteAttributeDefinition` | Delete an attribute definition by key. Important restrictions: - **Cannot delete if SAML source exists**: If the attribute has a SAML definition (sources includes 'saml'), deletion is forbidden (403). This applies even if you want to delete only the API-managed part. - **Cannot delete if in use**: If any user has values for this attribute (API-managed or SAML), deletion fails (409). - **API-managed only**: Only attributes with `sources: ['sanity']` can be deleted, and only when no users have values. Note: API-managed definitions are often automatically cleaned up when you delete user attribute values (if a SAML definition exists for the same key). Use this endpoint only for cleaning up unused API-managed-only definitions. ### Permissions Requires `sanity.organization.manage` permission. |
| Delete Content Release | `deleteContentRelease` | Deletes a published or archived content release, removing the release system document from the dataset. |
| Delete CORS Origin | `deleteCORSOrigin` | Deletes a specific CORS origin for a project. |
| Delete Dataset | `deleteDataset` | Deletes a specific dataset by name. |
| Delete Document | `deleteDocument` | Deletes a document by ID. The mutation succeeds even if the document does not exist. Drafts and versions of the document are not deleted; use Delete Document And Versions for that. |
| Delete Document And Versions | `deleteDocumentAndVersions` | Deletes a published document through the Actions API, optionally along with named drafts or release versions of it. |
| Delete Documents By Query | `deleteDocumentsByQuery` | Deletes every document matched by a GROQ query. A single query can delete at most 10000 documents; paginate by _id for larger sets. |
| Delete Embeddings Index | `deleteEmbeddingsIndex` | Delete a specific embeddings index for an existing database in a Sanity project. |
| Delete Installation Config | `deleteInstallationConfig` | Soft-delete a configuration snapshot. The record is removed from history immediately, but its content stays in storage so applications still resolving this config keep working; the content is purged once newer configs supersede it. Requires a session token with `sanity.sdk.applications.deploy` grant. |
| Delete Media Library Signing Key | `deleteMediaLibrarySigningKey` | Delete a signing key. |
| Delete Project | `deleteProject` | Deletes a specific project by ID. |
| Delete Project Role | `deleteProjectRole` | Delete a role in a project. |
| Delete Project Tag | `deleteProjectTag` | Deletes a tag by identifier. The tag must not be assigned to any datasets. |
| Delete Project Token | `deleteProjectToken` | Deletes a token for the project. |
| Delete Project User Application | `deleteProjectUserApplication` | Delete a user application for a project. |
| Delete Robot Token | `deleteRobotToken` | Permanently revokes the robot's active token and deletes the robot. After this operation succeeds, the token can no longer authenticate. ### Authorization This endpoint requires an authenticated session with the following permissions: - `sanity.{resourceType}.tokens.delete`. |
| Delete User Application | `deleteUserApplication` | Delete a user application. |
| Delete User Application Data | `deleteUserApplicationData` | Delete user application data. |
| Delete User Attributes | `deleteUserAttributes` | Delete attribute values for a user using attribute keys. This removes Sanity (API-managed) attribute values. If a SAML value exists for the same attribute key, it will become the active value and will be visible in the response (with `activeSource: 'saml'`). **Automatic Definition Cleanup:** When you delete Sanity attribute values, the system automatically cleans up Sanity definitions if: 1. No users have Sanity values for that attribute anymore, AND 2. A SAML definition exists for the same key In this case, the sources will automatically revert from `['saml', 'sanity']` to `['saml']`. Sanity-only definitions (`sources: ['sanity']`) are never automatically cleaned up when values are deleted. They must be manually deleted via the DELETE /attribute-definitions/{key} endpoint. ### Permissions Requires `sanity.organization.manage` permission. |
| Delete Video Subtitle | `deleteVideoSubtitle` | Deletes the specified subtitle and its associated track from the video provider. |
| Delete Webhook | `deleteWebhook` | Delete a webhook. |
| Deploy Application | `deployApplication` | Deploy a new version to an existing application. The new deployment becomes active, superseding the previous one. Requires the `sanity.sdk.applications.deploy` grant. Multipart form-data. `interfaces`, `access`, and `workspaces` are JSON parts (send each with `Content-Type: application/json`). Sanity-hosted apps include a `tarball`; external studios omit it. Field parts must precede the `tarball` part. |
| Deploy Installation Config | `deployInstallationConfig` | Push a configuration snapshot to an installed singleton. Creates a new config record and deactivates any previous active config. Requires a session token with `sanity.sdk.applications.deploy` grant. Field parts must precede the `tarball` part. |
| Deploy Project User Application | `deployProjectUserApplication` | Deploys a build of a user application. The endpoint accepts only a multipart upload of the built studio bundle (it answers 406 'the request is not multipart' for a JSON body), so deployments must be made with the Sanity CLI rather than through this action. The action is kept for endpoint coverage and for the deployment metadata it takes. |
| Deploy Studio Legacy Route | `deployStudioLegacyRoute` | Legacy deploy route used by Sanity CLI. This route should be considered deprecated, and is kept for Sanity CLI compatibility. The call is made against the project host, so the project is taken from the connection. The project must already have an assigned studio hostname; otherwise the API answers 400 'Project does not have an assigned studio hostname'. |
| Deploy User Application | `deployUserApplication` | Deploys a build of a user application. The endpoint accepts only a multipart upload of the built studio bundle (it answers 406 'the request is not multipart' for a JSON body), so deployments must be made with the Sanity CLI rather than through this action. The action is kept for endpoint coverage and for the deployment metadata it takes. |
| Discard Document Draft | `discardDocumentDraft` | Deletes the draft version of a document, discarding unpublished changes. Sanity marks this action deprecated in favour of Discard Document Version, which behaves the same for drafts. The Actions API rejects versionId here; this action takes draftId. |
| Discard Document Version | `discardDocumentVersion` | Discards a draft or release version of a document, removing it without touching the published document. |
| Dispatch Document Actions | `dispatchDocumentActions` | Dispatches one or more raw actions to the Actions API in a single transaction. Use the dedicated actions for common operations; use this when you need several actions applied atomically. Document, version and release actions cannot be mixed in one call. |
| Edit Content Release | `editContentRelease` | Updates the metadata of an existing, unpublished content release. The patch may only address paths under metadata. |
| Edit Document Version | `editDocumentVersion` | Applies a patch to a draft or release version of a document. If the version does not exist it is created from the current published document and then patched. |
| Export Activity Log As CSV | `exportActivityLogAsCSV` | Returns a CSV export of activity log events matching the supplied filters. CSV headers are sorted alphabetically. Metadata keys appear as dynamic `metadata.&lt;key&gt;` columns when present in the returned events. |
| Export Dataset | `exportDataset` | The Export API allows you to export all the non-deleted documents in a dataset, including drafts and asset documents. By default, this endpoint returns all the documents a user can access as an NDJSON stream. The documents will be in the state they were when the request was made and will not be affected by any changes in the dataset that happened after the request was made. In most cases, you probably want to use the CLI tool's export functionality or the JavaScript npm package. Those have built-in features such as asset downloads and an option for including drafts. ### Cursor mode for large datasets For datasets with many documents (typically tens of thousands), you can experience that network or other instabilities cause the export stream to time out or be interrupted. In these cases, you can send a request a nextCursor query parameter set to an empty string. This will cause the export to run for 30 seconds and end with an object with a nextCursor key and value. T |
| Generate Document Content | `generateDocumentContent` | Sends an instruction request to Generate for a specific dataset. Examples and implementation details can be found in the [Generate documentation](https://www.sanity.io/docs/generate). |
| Generate Video Subtitles | `generateVideoSubtitles` | Triggers AI-powered subtitle generation for the specified video. Returns immediately with a processing status; the subtitle will be updated via webhook when generation completes. |
| Get Access Permission | `getAccessPermission` | Gets a permission for a resource by name. Requires permission - `sanity.{resourceType}.roles.read`. |
| Get Access Role | `getAccessRole` | Requires permission - `sanity.{resourceType}.roles.read`. |
| Get Application | `getApplication` | Retrieve a single application by ID, regardless of deployment state. Supports optional includes for the active deployment summary (activeDeployment), its children (interfaces, workspaces, access) and application config (config.studio, config.mfManifest). |
| Get Application Resource Access | `getApplicationResourceAccess` | Retrieve the Sanity resources an application accesses, resolved from the active deployment. Returns null for singletons. |
| Get Dataset ACL | `getDatasetACL` | Get the access control list for a dataset. |
| Get Dataset Backup | `getDatasetBackup` | This endpoint is primarily designed for use through the Sanity CLI `sanity backup download` command, which handles paging, downloading all files, and constructing a tarball in the format expected by `sanity dataset import`. |
| Get Dataset Embeddings Settings | `getDatasetEmbeddingsSettings` | Returns the settings for the embeddings index for a dataset. |
| Get Document Revision | `getDocumentRevision` | Returns a document as it was at a point in the past. This endpoint behaves the same as the `/doc` endpoint. It applies the current access control to every revision of the document. Note: Current Access Control means if you're able to access the document today, you'll be able to access all the previous revisions of the document. |
| Get Documents By ID | `getDocumentsByID` | This endpoint cuts through any caching/indexing middleware that may involve delayed processing. It is designed for use cases where you want to be very sure to get the absolute latest possible version of a document as it is known to the backend. It can only fetch documents by id and it is less scalable/performant than the other query-mechanisms, so should be used sparingly. |
| Get Embeddings Index | `getEmbeddingsIndex` | Retrieve a specific embeddings index for an existing database in a Sanity project. |
| Get Installation | `getInstallation` | Retrieve a single active installation and its singleton's title and slug. Use `include` to embed the active config, access rows, or interfaces. |
| Get Installation Resource Access | `getInstallationResourceAccess` | Retrieve the installation-scoped resource access declarations. Returns an empty array until the install flow writes these rows (SDK-1811). |
| Get Invite By Token | `getInviteByToken` | Retrieves an invite using its token. ### Authorization This endpoint does not require authentication. |
| Get Job Status | `getJobStatus` | Get the status of a job. |
| Get Media Library Signing Key | `getMediaLibrarySigningKey` | Get a specific signing key. |
| Get My User Attributes | `getMyUserAttributes` | Retrieve your own attributes within an organization. This endpoint returns all attributes for the current authenticated user, including both SAML and Sanity values. Each attribute includes: - **values**: Object showing values from all sources (e.g., `{saml: "US", sanity: "UK"}`) - **activeSource**: Which source is currently in effect ('saml' or 'sanity') - **activeValue**: The actual value being used in access control When an attribute exists in both SAML and Sanity sources, the `values` object will contain both, and `activeSource` will be 'sanity' since Sanity values take precedence. ### Permissions No special permission required - users can always read their own attributes. |
| Get Organization Member Roles | `getOrganizationMemberRoles` | Get the roles of a specific member in an organization. |
| Get Project | `getProject` | Returns the details of a specific project by ID. |
| Get Project Member Roles | `getProjectMemberRoles` | Get the role of a specific user in a project. |
| Get Project Role | `getProjectRole` | Get a role in a project. |
| Get Project User | `getProjectUser` | Returns a list of details for the user. |
| Get Project User Application | `getProjectUserApplication` | Get a user application by id. |
| Get Resource User | `getResourceUser` | Get the users for a single user of a resource. Requires permission - `sanity.{resourceType}.members.read`. |
| Get Robot Token | `getRobotToken` | Retrieves a robot using its unique identifier. It's not possible to retrieve a robot token. ### Authorization This endpoint requires an authenticated user session with the following permissions: - `sanity.{resourceType}.tokens.read`. |
| Get Schedule | `getSchedule` | Get schedule by ID. |
| Get Studio Auto Update Version Status | `getStudioAutoUpdateVersionStatus` | Returns the auto-updating version status for a studio based on the X-App-Host header. |
| Get User Application | `getUserApplication` | Get a user application by id. |
| Get User Attributes | `getUserAttributes` | Retrieve attributes for a user within an organization. This endpoint returns all attributes for a user, including both SAML and Sanity values. Each attribute includes: - **values**: Object showing values from all sources (e.g., `{saml: "US", sanity: "UK"}`) - **activeSource**: Which source is currently in effect ('saml' or 'sanity') - **activeValue**: The actual value being used in access control When an attribute exists in both SAML and Sanity sources, the `values` object will contain both, and `activeSource` will be 'sanity' since Sanity values take precedence. ### Permissions - To read your own attributes: No special permission required - To read other users' attributes: Requires `sanity.organization.manage` permission - This only applies for organizations you have permissions for. |
| Get Video Playback Info | `getVideoPlaybackInfo` | Get video playback information. |
| Get Video Playback URL | `getVideoPlaybackURL` | Redirect to video playback URL. |
| Get Video Rendition URL | `getVideoRenditionURL` | Returns a redirect to the rendition (downloadable MP4) for the specified video. |
| Get Webhook | `getWebhook` | Get a webhook by ID. |
| Import Content Release | `importContentRelease` | Imports a release system document into a dataset. Used when moving releases between datasets, for example during a dataset import. |
| Insert Into Document Array | `insertIntoDocumentArray` | Inserts items into an array field on a document. Supply exactly one of Insert Before, Insert After or Replace to say where the items go; the API returns 400 if none or more than one is given. |
| Install Application | `installApplication` | Install a singleton application for an organization. Requires a service token. Creates an installation record linking the organization to the singleton. |
| Leave Resource | `leaveResource` | This removes the currently authenticated user from the given resource. If the resourceType is `organization`, this will also remove the user from all projects owned by the organization. This is a specific route which does not require resource permissions, since users should be able to remove themselves from resources without requiring an administrator to intervene for them. |
| Link Media Library Asset | `linkMediaLibraryAsset` | Creates a linked Media Library asset in your dataset. To support features like preview, Media Library assets need to be linked to a local asset document. Pair with mutate to attach linked Media Library assets to documents. |
| List Access Permissions | `listAccessPermissions` | Gets the available permissions within the scope of a resource. These permissions can be applied to roles and are used to determine user/robot access to resources. &lt;br /&gt; &lt;br /&gt; Requires permission: `sanity.{resourceType}.roles.read`. |
| List Access Requests | `listAccessRequests` | Permissions `sanity.{resourceType}.members.read`. |
| List Access Roles | `listAccessRoles` | Requires permission - `sanity.{resourceType}.roles.read`. |
| List Activity Log Events | `listActivityLogEvents` | Returns activity log events matching the supplied filters. Requests only return events for organizations and projects that the authenticated user can access. |
| List Application Deployments | `listApplicationDeployments` | Retrieve the deployment history for an application. Returns all non-deleted deployments with nested children (interfaces, workspaces, access), ordered by creation date descending. |
| List Application Interfaces | `listApplicationInterfaces` | Retrieve interfaces of a specific type for an application, resolved from the active deployment. |
| List Application Workspaces | `listApplicationWorkspaces` | Retrieve workspaces for a studio application, resolved from the active deployment. Returns null for non-studio applications. |
| List Applications | `listApplications` | List all org-owned applications for an organization, regardless of deployment state. Supports cursor-based pagination and optional includes for the active deployment summary (activeDeployment), its children (interfaces, workspaces, access) and application config (config.studio, config.mfManifest). |
| List Asset References | `listAssetReferences` | Get references to an asset document from other documents and datasets. At this time, this does not support draft or version documents. Note: this endpoint is currently only available on version `vX` of the API. |
| List Attribute Definitions | `listAttributeDefinitions` | Retrieve a paginated list of attribute definitions for an organization. Definitions are grouped by key and show all sources where that key is defined. ### Permissions Requires `sanity.organization.manage` permission. |
| List Content Releases | `listContentReleases` | Lists every content release in a dataset with its state and metadata, using the releases::all() GROQ function. |
| List CORS Origins | `listCORSOrigins` | Returns a list of all CORS origins for a specific project. |
| List Dataset Backups | `listDatasetBackups` | List backups. |
| List Dataset Grants | `listDatasetGrants` | Get all grants for a dataset. |
| List Dataset Tags | `listDatasetTags` | Returns a list of tags for the dataset. |
| List Dataset Transactions | `listDatasetTransactions` | Returns an NDJSON (Newline Delimited JSON) containing transactions for all documents. **Using with `limit` is highly recommended.**. The endpoint answers with newline-delimited JSON, which is returned as a stored file reference rather than parsed JSON. Download it with the file reference to read the records. |
| List Datasets | `listDatasets` | Returns a list of all datasets for the project. |
| List Document Transactions | `listDocumentTransactions` | Returns an NDJSON (Newline Delimited JSON) containing transactions for the given document ids. The endpoint answers with newline-delimited JSON, which is returned as a stored file reference rather than parsed JSON. Download it with the file reference to read the records. |
| List Embeddings Indexes | `listEmbeddingsIndexes` | Retrieve a list of all embeddings indexes for the specified dataset. |
| List Installation Configs | `listInstallationConfigs` | Retrieve the configuration history for an installed singleton. Returns config snapshot metadata ordered by creation date descending. |
| List Installation Interfaces | `listInstallationInterfaces` | Retrieve a singleton's interfaces of a specific type, addressed by an installation id and resolved from the singleton's active deployment. |
| List Installations | `listInstallations` | List an organization's active singleton installations. Each item carries the installation and its singleton's title and slug; use `include` to embed the active config, access rows, or interfaces. Supports cursor-based pagination. |
| List Media Library Signing Keys | `listMediaLibrarySigningKeys` | List all signing keys. |
| List My Access Permissions | `listMyAccessPermissions` | Gets current user permissions within scope of a resource. These permissions can be applied to roles and are used to determine user/robot access to resources. |
| List My Access Requests | `listMyAccessRequests` | Requires an authenticated user. |
| List My Invites | `listMyInvites` | Retrieves a list of invites for the current user, using the email. |
| List Organization Grants | `listOrganizationGrants` | Get all grants for the current user in an organization. |
| List Organization Members | `listOrganizationMembers` | Get a list of all members and their roles in an organization. |
| List Permission Resource Schemas | `listPermissionResourceSchemas` | List all permission resources in a project. |
| List Project Features | `listProjectFeatures` | Returns a list of active features for the project. |
| List Project Grants | `listProjectGrants` | List all grants for users in a project. |
| List Project Members | `listProjectMembers` | List all users and their roles in a project. |
| List Project Permissions | `listProjectPermissions` | Returns a list of permissions for the project. |
| List Project Roles | `listProjectRoles` | List all roles in a project. |
| List Project Tokens | `listProjectTokens` | Returns a list of tokens for the project. This endpoint does not reveal the actual token, only details about the token. |
| List Project User Application Deployments | `listProjectUserApplicationDeployments` | Get deployments for a user application. The response is paginated shape but the actual data is not paginated at this point. |
| List Project User Applications | `listProjectUserApplications` | Retrieves user applications for the given project or organization. Returns an array of applications by default, or a single application when filtering by `appHost` or `default`. For studio applications queried via organization route, fetches all projects within the organization. |
| List Projects | `listProjects` | Returns a list of all projects you are a member of. |
| List Release Documents | `listReleaseDocuments` | Lists every document version that belongs to a content release. The query runs with the raw perspective because release versions are hidden from the default perspective. |
| List Resource Invites | `listResourceInvites` | Retrieves a list of invites for the specified resource. Only pending invites are retrieved by default; use the optional Status filter to list accepted or revoked invites instead (one status per call). By default, only invites for the specified resource are returned; set Include Children to include invites for child resources (organization resources only). Requires the `sanity.{resourceType}.members.read` permission. |
| List Resource Users | `listResourceUsers` | Retrieve a list of all users of a resource along with their assigned roles. When the resourceType is `organization`, this endpoint will return users of projects owned by the organization. Requires permission - `sanity.{resourceType}.members.read`. |
| List Robot Tokens | `listRobotTokens` | Retrieves a list of robots that have access to the specified resource. ### Access to children resources By default, this endpoint returns robots that have at least one role on the specified resource. Use the optional `includeChildren` parameter to include robots that have a role on children resources as well. This only applies to `organization` resources. ### Authorization This endpoint requires an authenticated user session with the following permissions: - `sanity.{resourceType}.tokens.read`. |
| List Schedules | `listSchedules` | List schedules. |
| List Studio Workspaces | `listStudioWorkspaces` | Returns a flattened view of user applications with their workspaces. Each workspace becomes a separate entry in the response, allowing easy access to schema descriptors. |
| List User Application Deployments | `listUserApplicationDeployments` | Get deployments for a user application. The response is paginated shape but the actual data is not paginated at this point. |
| List User Application Workspaces | `listUserApplicationWorkspaces` | Returns a flattened view of workspaces for a specific user application. Each workspace becomes a separate entry in the response, allowing easy access to schema descriptors. |
| List User Applications | `listUserApplications` | Retrieves user applications for the given project or organization. Returns an array of applications by default, or a single application when filtering by `appHost` or `default`. For studio applications queried via organization route, fetches all projects within the organization. Either a project ID or an organization ID must be supplied. |
| List Webhook Delivery Attempts | `listWebhookDeliveryAttempts` | List webhook attempts. |
| List Webhook Messages | `listWebhookMessages` | List webhook messages. |
| List Webhooks | `listWebhooks` | List all webhooks. |
| Mutate Documents | `mutateDocuments` | Applies a transaction of raw mutations (create, createOrReplace, createIfNotExists, patch, delete) to a dataset. Use the dedicated document actions for common cases; use this when you need several mutations applied atomically. |
| Mutate Media Library Assets | `mutateMediaLibraryAssets` | You can use this endpoint to create, update, or delete documents in the Media Library. This uses the same mutation syntax as Content Lake's [Mutation API](https://www.sanity.io/docs/http-reference/mutation). |
| Patch Document | `patchDocument` | Applies a patch to a single document by ID. Operations are applied in the order set, setIfMissing, unset, inc, dec, insert. Supply only the operations you need; omitted operations are not sent. |
| Patch Document With AI | `patchDocumentWithAI` | A schema-aware patch API that validates the provided paths and values against the target schema. This operation does not use an LLM and will only use regular Sanity billing for API requests. |
| Patch Documents By Query | `patchDocumentsByQuery` | Applies the same patch to every document matched by a GROQ query. The query can match at most 10000 documents in one transaction. |
| Prompt Language Model | `promptLanguageModel` | Prompt the LLM for a response. Does not interact with documents beyond fetching content as context when requested. Use for tasks that don't require manipulating documents, such as generating details that you may want to use with other Agent Actions. |
| Publish Content Release | `publishContentRelease` | Publishes every document version in a content release. For large releases the effect can take a short while to become fully visible. |
| Publish Document | `publishDocument` | Publishes a draft or release version of a document, making its content the published document. |
| Publish Document Immediately | `publishDocuments` | Publishes a document immediately through the Scheduling API, outside of any schedule. One document is published per call. |
| Query Documents | `queryDocuments` | Runs a GROQ query against a dataset in the Content Lake and returns the result. Use this for any read that is not a plain fetch by document ID. |
| Query Embeddings Index | `queryEmbeddingsIndex` | Query an embeddings index to retrieve documents that are closely related to the input query. |
| Query Media Library | `queryMediaLibrary` | Use GROQ to query the Media Library. See the [GROQ documentation](https://www.sanity.io/docs/groq) for more information on writing GROQ queries. |
| Quickstart Deploy Studio | `quickstartDeployStudio` | Quickstart deploy route used by Quickstart. This route is used for a specific experiment and should not be used without prior approval. The call is made against the project host, so the project is taken from the connection. The project must already have an assigned studio hostname; otherwise the API answers 400 'Project does not have an assigned studio hostname'. |
| Register Project User Application Config | `registerProjectUserApplicationConfig` | Register a configuration for a user application under the provided key. Only updates when the config value is different from the current value. Note: The supported keys depends on the type of the user application. **Studio Config Keys** - `live-manifest`: See [Studio Manifest](#/components/schemas/StudioManifest). The live-manifest payload is only accepted once its schema descriptors have been synchronised to the project with sanity schema deploy; otherwise the API answers 400 'live-manifest contains unsynchronized descriptors'. |
| Register User Application Config | `registerUserApplicationConfig` | Register a configuration for a user application under the provided key. Only updates when the config value is different from the current value. Note: The supported keys depends on the type of the user application. **Studio Config Keys** - `live-manifest`: See [Studio Manifest](#/components/schemas/StudioManifest). The live-manifest payload is only accepted once its schema descriptors have been synchronised to the project with sanity schema deploy; otherwise the API answers 400 'live-manifest contains unsynchronized descriptors'. |
| Remove Role From Organization Member | `removeRoleFromOrganizationMember` | Remove a role from a member in an organization. |
| Remove Role From Project Member | `removeRoleFromProjectMember` | Remove a role from a user in a project. |
| Remove Role From User | `removeRoleFromUser` | You cannot remove the last role from a user. You must have at least one role assigned to a user. Requires permission - `sanity.{resourceType}.members.update`. |
| Remove Tag From Dataset | `removeTagFromDataset` | Removes a tag from a dataset. |
| Remove User From Resource | `removeUserFromResource` | This removes all roles. If the resourceType is `organization`, this will also remove the user from all projects owned by the organization. Requires permission - `sanity.{resourceType}.members.delete`. |
| Replace Document Draft | `replaceDocumentDraft` | Replaces the draft version of a document with the supplied content. Deprecated by Sanity in favour of Replace Document Version. |
| Replace Document Version | `replaceDocumentVersion` | Replaces an existing draft or release version of a document with the supplied content. |
| Replace User Roles | `replaceUserRoles` | Replace the role set for a user on a resource. The supplied `roleNames` become the user's complete role set: missing roles are added, extra roles are removed. The list must contain at least one role: at least one role must remain assigned at all times. Roles are assigned before extras are revoked so the user never momentarily drops to zero roles. A single composite `members.role.replace` activity event is emitted per call (no per-role events). Requires permission - `sanity.{resourceType}.members.update`. |
| Resolve Application By Host | `resolveApplicationByHost` | This route is used for internal services to resolve an application by host name. |
| Resolve Project By Application | `resolveProjectByApplication` | This route is moved from populus, and we have updated services that use it to route to this URL. https://github.com/sanity-io/populus/blob/b460c53cc020a9ca6971c03c45d93bd960196b82/src/controllers/internal/resolve/projects.js Some changes were implemented -- for example, returning a single entity rather than an array. |
| Revoke Current Robot Token | `revokeCurrentRobotToken` | Revokes the robot token supplied in the `Authorization` header and deletes its associated robot. No resource or robot identifier is required. For a robot token the operation is idempotent: once the first call has deleted the robot, cleared its roles and invalidated its sessions, a subsequent call is still `204`. This endpoint is rate limited. See the `429` response for details. |
| Revoke Invite | `revokeInvite` | Revokes an invite. Attempting to revoke an invite that has already been accepted or revoked will result in a Bad Request error. ### Authorization This endpoint requires an authenticated user session with the following permissions: - `sanity.{resourceType}.members.invite`. |
| Rotate Current Robot Token | `rotateCurrentRobotToken` | Replaces the robot token supplied in the `Authorization` header while preserving the robot, its roles, and the token's expiration. No resource or robot identifier is required. There is no overlap period. After this operation succeeds, the previous token is revoked and clients must use the new token. The new secret is returned only in this response and cannot be retrieved again. Rotation replaces exactly the token that authenticated the request. This endpoint is rate limited. See the `429` response for details. |
| Run Parameterized Query | `runParameterizedQuery` | Runs a GROQ query against a dataset using the POST endpoint, which supports queries longer than 11 KB and named query parameters. Use this instead of Query Documents when the query is long or takes parameters. |
| Run Schedule Now | `runScheduleNow` | Run schedule. |
| Schedule Content Release | `scheduleContentRelease` | Schedules a content release to publish at a future time. The release is locked from further edits until the scheduled time. |
| Search Media Library Assets | `searchMediaLibraryAssets` | Search for assets and references. |
| Send Content Agent Message | `sendContentAgentMessage` | Send a message to the agent and receive a streaming response. This endpoint manages conversation threads and persists message history. |
| Send Content Agent Prompt | `sendContentAgentPrompt` | Stateless one-shot prompt endpoint. No thread management or message persistence. Ideal for simple, single-turn interactions. |
| Set Dataset Backup Settings | `setDatasetBackupSettings` | Enable or disable backups. |
| Set Document Fields | `setDocumentFields` | Overwrites the given fields on a document, leaving every other field untouched. Field paths may be nested, for example meta.slug. |
| Transform Document With AI | `transformDocumentWithAI` | Transforms a source document into a new document. Examples and implementation details can be found in the [Transform documentation](https://www.sanity.io/docs/compute-and-ai/transform). |
| Translate Document With AI | `translateDocumentWithAI` | Translates a source document into a new document. |
| Unarchive Content Release | `unarchiveContentRelease` | Restores an archived content release and all of its documents to the state they were in before archiving. |
| Uninstall Application | `uninstallApplication` | Uninstall a singleton from an organization. Sets `uninstalledAt` and preserves the record for audit history. Requires a service token. |
| Unpublish Document | `unpublishDocument` | Removes a document from the published perspective while keeping its draft. The document must currently be published. |
| Unpublish Document Immediately | `unpublishDocuments` | Unpublishes a document immediately through the Scheduling API, outside of any schedule. One document is unpublished per call. |
| Unpublish Document Version | `unpublishDocumentVersion` | Marks a release version so that publishing the release removes the corresponding published document. |
| Unschedule Content Release | `unscheduleContentRelease` | Cancels the scheduled publication of a content release and unlocks it for further edits. |
| Unset Document Fields | `unsetDocumentFields` | Removes the given fields from a document. Field paths may address array members, for example tags[0]. |
| Update Access Permission | `updateAccessPermission` | Updates a permission for a resource. Requires permission - `sanity.{resourceType}.roles.update` Requires feature: - `advancedRolesManagement`. |
| Update Access Role | `updateAccessRole` | Requires permission: - `sanity.{resourceType}.roles.update` Requires feature: - `advancedRolesManagement` Replaces existing object values including permissions. |
| Update Application | `updateApplication` | Update an application's mutable properties. Requires the `sanity.sdk.applications.deploy` grant. |
| Update Dataset | `updateDataset` | Updates a specific dataset in the project. |
| Update Dataset Embeddings Settings | `updateDatasetEmbeddingsSettings` | Updates the settings for the embeddings index for a dataset. |
| Update Project | `updateProject` | Updates a specific project by ID. |
| Update Project Role | `updateProjectRole` | Update a role in a project. |
| Update Project Tag | `updateProjectTag` | Updates a tag by identifier. |
| Update Project User Application | `updateProjectUserApplication` | Update a user application for a project. |
| Update Robot Token | `updateRobotToken` | Updates the expiry date for a robot token. ### Authorization This endpoint requires an authenticated user session with the following permissions: - `sanity.{resourceType}.tokens.create`. |
| Update Schedule | `updateSchedule` | Updates a schedule. The name, description, execution time, documents and state are all sent in the request body. Set State to cancelled to cancel a scheduled publish. |
| Update User Application | `updateUserApplication` | Update a user application. |
| Update User Attributes | `updateUserAttributes` | Set or update attribute values for a user using attribute keys. When you set a value for an attribute key that also exists in SAML, your Sanity value will take precedence and shadow the SAML value. The SAML value remains in the system and is visible in the `values` object. If the attribute key doesn't have a Sanity definition yet, one will be created automatically. This endpoint returns at most the first 50 attributes after the update, prioritizing attributes with values. ### Permissions Requires `sanity.organization.manage` permission. |
| Update Webhook | `updateWebhook` | Update a webhook. |
| Upload File Asset | `uploadFileAsset` | Upload an file asset to Content Lake. This uploads an file and creates a linked `sanity.fileAsset` document containing the file metadata. |
| Upload Image Asset | `uploadImageAsset` | Upload an image asset to Content Lake. This uploads an image and creates a linked `sanity.imageAsset` document containing the image metadata. |
| Upload Media Library Asset | `uploadMediaLibraryAsset` | Upload an asset to the media library. |
| Upload Video Subtitle | `uploadVideoSubtitle` | Uploads a VTT or SRT subtitle file for the specified video. The subtitle file content is sent as the raw request body (not JSON). Metadata is passed via query parameters. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Document Created | `created` | Fires when a document is created in the selected dataset. Registered against the Sanity webhook rule 'on: create'. The payload of a Sanity webhook is defined by the GROQ projection on the webhook, not by a fixed vendor contract. fastn registers the projection shown here, so these fields are the ones actually delivered for triggers created through fastn. Sanity signs each delivery with a sanity-webhook-signature header of the form t=&lt;timestamp&gt;,v1=&lt;signature&gt;, where the signature is a base64url HMAC-SHA256 over &lt;timestamp&gt;.&lt;rawBody&gt;. The platform's HMAC verification only supports hex and stripe signature formats, so this scheme cannot be expressed as a verification config and is left unset; set a secret on the webhook and verify downstream if you need origin verification. |
| Document Deleted | `deleted` | Fires when a document is deleted in the selected dataset. Registered against the Sanity webhook rule 'on: delete'. The payload of a Sanity webhook is defined by the GROQ projection on the webhook, not by a fixed vendor contract. fastn registers the projection shown here, so these fields are the ones actually delivered for triggers created through fastn. Sanity signs each delivery with a sanity-webhook-signature header of the form t=&lt;timestamp&gt;,v1=&lt;signature&gt;, where the signature is a base64url HMAC-SHA256 over &lt;timestamp&gt;.&lt;rawBody&gt;. The platform's HMAC verification only supports hex and stripe signature formats, so this scheme cannot be expressed as a verification config and is left unset; set a secret on the webhook and verify downstream if you need origin verification. |
| Document Updated | `updated` | Fires when a document is updated in the selected dataset. Registered against the Sanity webhook rule 'on: update'. The payload of a Sanity webhook is defined by the GROQ projection on the webhook, not by a fixed vendor contract. fastn registers the projection shown here, so these fields are the ones actually delivered for triggers created through fastn. Sanity signs each delivery with a sanity-webhook-signature header of the form t=&lt;timestamp&gt;,v1=&lt;signature&gt;, where the signature is a base64url HMAC-SHA256 over &lt;timestamp&gt;.&lt;rawBody&gt;. The platform's HMAC verification only supports hex and stripe signature formats, so this scheme cannot be expressed as a verification config and is left unset; set a secret on the webhook and verify downstream if you need origin verification. |
