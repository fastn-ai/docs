---
description: "Google Tag Manager API v2 — manage accounts, containers, workspaces, tags, triggers, variables, templates, clients, transformations, zones, folders,…"
hidden: true
---

# Google Tag Manager

<img src="../../.gitbook/assets/connectors/lg/google-tag-manager.png" alt="Google Tag Manager logo">

Google Tag Manager API v2 — manage accounts, containers, workspaces, tags, triggers, variables, templates, clients, transformations, zones, folders, environments, container versions, and user permissions.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [tagmanager.googleapis.com](https://tagmanager.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleTagManager` |

## Use it

Add Google Tag Manager from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleTagManager.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Update Workspace | `bulkUpdateWorkspace` | Applies a batch of entity changes to a workspace in a single call. Each change names one entity kind together with the change status to record for it. |
| Combine Containers | `combineContainers` | Merges a source container into a destination container, moving the source container's configuration across. The destination container is identified by the path and the source by the container id parameter. |
| Create Client | `createClient` | Creates a client in a Google Tag Manager server-side workspace. Clients claim incoming requests and turn them into events that server-side tags can act on. |
| Create Container | `createContainer` | Creates a new container in a Google Tag Manager account. The usage context determines the platform the container targets, such as web, server, or a mobile app. |
| Create Environment | `createEnvironment` | Creates a user-defined environment in a Google Tag Manager container, which lets a specific container version be served to a preview or staging site. |
| Create Folder | `createFolder` | Creates a folder in a Google Tag Manager workspace for organising tags, triggers, and variables. |
| Create Google Tag Config | `createGtagConfig` | Creates a Google tag configuration in a Google Tag Manager workspace, holding shared settings applied to a Google tag destination. |
| Create Tag | `createTag` | Creates a tag in a Google Tag Manager workspace. The tag type determines which parameters are required, for example an html tag needs a html parameter and a Google Analytics event tag needs measurement and event parameters. |
| Create Template | `createTemplate` | Creates a custom template in a Google Tag Manager workspace from a template definition, which declares the template's fields, permissions, and sandboxed JavaScript. |
| Create Transformation | `createTransformation` | Creates a transformation in a Google Tag Manager server-side workspace, which rewrites or redacts event data before tags receive it. |

<details>

<summary>See 96 more actions</summary>

* **Create Trigger** `createTrigger`: Creates a trigger in a Google Tag Manager workspace. The trigger type determines which conditions and timing options apply, for example a pageview trigger uses filters while a timer trigger uses interval and limit.
* **Create User Permission** `createUserPermission`: Grants a user access to a Google Tag Manager account, setting their account-level role and optionally per-container permissions.
* **Create Variable** `createVariable`: Creates a user-defined variable in a Google Tag Manager workspace. The variable type determines the required parameters, for example a data layer variable of type v needs a name parameter naming the data layer key.
* **Create Workspace** `createWorkspace`: Creates a new workspace in a Google Tag Manager container so that changes can be drafted independently of other in-progress work.
* **Create Workspace Version** `createWorkspaceVersion`: Freezes the current state of a workspace into a new container version, which can then be published. Fails if the workspace still has unresolved merge conflicts.
* **Create Zone** `createZone`: Creates a zone in a Google Tag Manager workspace, delegating part of the container to one or more child containers under the given boundary conditions.
* **Delete Client** `deleteClient`: Deletes a client from a Google Tag Manager server-side workspace.
* **Delete Container** `deleteContainer`: Permanently deletes a Google Tag Manager container together with all of its workspaces, versions, tags, triggers, and variables.
* **Delete Container Version** `deleteContainerVersion`: Marks a container version as deleted. Deleted versions remain recoverable with Undelete Container Version.
* **Delete Environment** `deleteEnvironment`: Deletes a user-defined environment from a Google Tag Manager container. The built-in live and latest environments cannot be deleted.
* **Delete Folder** `deleteFolder`: Deletes a folder from a Google Tag Manager workspace. The tags, triggers, and variables inside it are not deleted, only ungrouped.
* **Delete Google Tag Config** `deleteGtagConfig`: Deletes a Google tag configuration from a Google Tag Manager workspace.
* **Delete Tag** `deleteTag`: Deletes a tag from a Google Tag Manager workspace. The deletion takes effect live only once a new container version is created and published.
* **Delete Template** `deleteTemplate`: Deletes a custom template from a Google Tag Manager workspace. Tags and variables built on the template will no longer resolve.
* **Delete Transformation** `deleteTransformation`: Deletes a transformation from a Google Tag Manager server-side workspace.
* **Delete Trigger** `deleteTrigger`: Deletes a trigger from a Google Tag Manager workspace. The deletion takes effect live only once a new container version is created and published.
* **Delete User Permission** `deleteUserPermission`: Revokes a user's access to a Google Tag Manager account by removing their user permission record.
* **Delete Variable** `deleteVariable`: Deletes a user-defined variable from a Google Tag Manager workspace. Tags still referencing the variable will fail to resolve it.
* **Delete Workspace** `deleteWorkspace`: Deletes a workspace from a Google Tag Manager container, discarding any unpublished changes it contains.
* **Delete Zone** `deleteZone`: Deletes a zone from a Google Tag Manager workspace, removing the delegation to its child containers.
* **Disable Built-In Variable** `deleteBuiltInVariable`: Disables a built-in variable in a workspace so that it is no longer available to tags and triggers.
* **Enable Built-In Variable** `createBuiltInVariable`: Enables one or more built-in variables in a workspace so that they can be referenced by tags and triggers.
* **Get Account** `getAccount`: Retrieves a single Google Tag Manager account by its account identifier.
* **Get Client** `getClient`: Retrieves a single client from a Google Tag Manager server-side workspace, including its priority and configuration parameters.
* **Get Container** `getContainer`: Retrieves a single Google Tag Manager container, including its public container id, usage context, and associated domains.
* **Get Container Snippet** `getContainerSnippet`: Returns the tagging snippet HTML for a container, which is the code that must be installed on the site or app for the container to run.
* **Get Container Version** `getContainerVersion`: Retrieves a full container version, including every tag, trigger, variable, client, zone, transformation, and built-in variable it contains.
* **Get Destination** `getDestination`: Retrieves a single Google tag destination linked to a Google Tag Manager container.
* **Get Environment** `getEnvironment`: Retrieves a single environment in a Google Tag Manager container, including its authorization code and the container version it points at.
* **Get Folder** `getFolder`: Retrieves a single folder from a Google Tag Manager workspace.
* **Get Google Tag Config** `getGtagConfig`: Retrieves a single Google tag configuration from a Google Tag Manager workspace.
* **Get Latest Version Header** `getLatestVersionHeader`: Retrieves the header of the most recently created container version, without returning the full version payload.
* **Get Live Container Version** `getLiveContainerVersion`: Retrieves the container version that is currently published and serving live traffic, including all of its tags, triggers, and variables.
* **Get Tag** `getTag`: Retrieves a single tag from a Google Tag Manager workspace, including its full parameter list and trigger assignments.
* **Get Template** `getTemplate`: Retrieves a single custom template from a Google Tag Manager workspace, including its full template definition.
* **Get Transformation** `getTransformation`: Retrieves a single transformation from a Google Tag Manager server-side workspace, including its configuration parameters.
* **Get Trigger** `getTrigger`: Retrieves a single trigger from a Google Tag Manager workspace, including its full condition set and timing options.
* **Get User Permission** `getUserPermission`: Retrieves a single user's account-level and container-level permissions on a Google Tag Manager account.
* **Get Variable** `getVariable`: Retrieves a single user-defined variable from a Google Tag Manager workspace, including its configuration parameters and format value settings.
* **Get Workspace** `getWorkspace`: Retrieves a single workspace in a Google Tag Manager container.
* **Get Workspace Status** `getWorkspaceStatus`: Returns the status of a workspace, listing every entity changed in it since the last sync and any merge conflicts against the base container version.
* **Get Zone** `getZone`: Retrieves a single zone from a Google Tag Manager workspace, including its boundary conditions, delegated child containers, and tag type restrictions.
* **Import Template From Gallery** `importTemplateFromGallery`: Imports a custom template from the Community Template Gallery into a Google Tag Manager workspace, identified by its GitHub owner, repository, and commit SHA.
* **Link Destination** `linkDestination`: Links a Google tag destination, such as a Google Ads or Analytics property, to a Google Tag Manager container.
* **List Accounts** `listAccounts`: Lists all Google Tag Manager accounts that the authenticated user has access to.
* **List Built-In Variables** `listBuiltInVariables`: Lists the built-in variables that are currently enabled in a workspace. Built-in variables are pre-created, non-customizable variables such as Page URL and Click Element.
* **List Clients** `listClients`: Lists all clients in a Google Tag Manager server-side workspace. Clients receive and claim incoming requests before tags run.
* **List Containers** `listContainers`: Lists all containers in a Google Tag Manager account.
* **List Destinations** `listDestinations`: Lists the Google tag destinations linked to a Google Tag Manager container.
* **List Environments** `listEnvironments`: Lists all environments in a Google Tag Manager container, including the built-in live and latest environments and any user-defined ones.
* **List Folder Entities** `listFolderEntities`: Lists the tags, triggers, and variables that belong to a folder in a Google Tag Manager workspace.
* **List Folders** `listFolders`: Lists all folders in a Google Tag Manager workspace. Folders are used to organise tags, triggers, and variables.
* **List Google Tag Configs** `listGtagConfigs`: Lists the Google tag configurations in a Google Tag Manager workspace, which hold the shared settings applied to Google tag destinations.
* **List Tags** `listTags`: Lists all tags in a Google Tag Manager workspace, including their type, parameters, and firing triggers.
* **List Templates** `listTemplates`: Lists all custom templates in a Google Tag Manager workspace. Custom templates define reusable tag and variable types written in sandboxed JavaScript.
* **List Transformations** `listTransformations`: Lists all transformations in a Google Tag Manager server-side workspace. Transformations modify event data before it reaches tags.
* **List Triggers** `listTriggers`: Lists all triggers in a Google Tag Manager workspace, including their event type and firing conditions.
* **List User Permissions** `listUserPermissions`: Lists all users who have access to a Google Tag Manager account, along with their account-level and container-level permissions.
* **List Variables** `listVariables`: Lists all user-defined variables in a Google Tag Manager workspace, including their type and configuration parameters.
* **List Version Headers** `listVersionHeaders`: Lists lightweight headers for every container version, giving each version's id, name, and entity counts without returning the full version payload.
* **List Workspaces** `listWorkspaces`: Lists all workspaces in a Google Tag Manager container. A workspace holds in-progress changes that have not yet been published.
* **List Zones** `listZones`: Lists all zones in a Google Tag Manager workspace. Zones delegate part of a container to another container, which is how Tag Manager 360 supports delegated tagging.
* **Lookup Container** `lookupContainer`: Finds a Google Tag Manager container by its Google tag id or destination id, without needing to know which account it belongs to. Supply exactly one of the two identifiers.
* **Move Entities To Folder** `moveEntitiesToFolder`: Moves the given tags, triggers, and variables into a folder in a Google Tag Manager workspace.
* **Move Tag ID** `moveTagId`: Moves a Google tag id out of a container into a new or existing container, optionally copying that tag's settings, users, and terms of service acceptance.
* **Publish Container Version** `publishContainerVersion`: Publishes a container version, making it the live version served to visitors. This immediately changes what runs on every site or app using the container.
* **Quick Preview Workspace** `quickPreviewWorkspace`: Creates a temporary preview version of a workspace so its unpublished changes can be tested without creating a permanent container version.
* **Reauthorize Environment** `reauthorizeEnvironment`: Regenerates the authorization code for an environment, which invalidates the previous code and requires the environment's tagging snippet to be reinstalled.
* **Resolve Workspace Conflict** `resolveWorkspaceConflict`: Resolves a merge conflict in a workspace by supplying the entity value that should win. Send exactly one entity, matching the kind of the conflicting entity.
* **Revert Built-In Variable** `revertBuiltInVariable`: Discards the workspace's unpublished change to a built-in variable, restoring it to the state in the base container version.
* **Revert Client** `revertClient`: Discards the workspace's unpublished changes to a client, restoring it to the state in the base container version.
* **Revert Folder** `revertFolder`: Discards the workspace's unpublished changes to a folder, restoring it to the state in the base container version.
* **Revert Tag** `revertTag`: Discards the workspace's unpublished changes to a tag, restoring it to the state in the base container version.
* **Revert Template** `revertTemplate`: Discards the workspace's unpublished changes to a custom template, restoring it to the state in the base container version.
* **Revert Transformation** `revertTransformation`: Discards the workspace's unpublished changes to a transformation, restoring it to the state in the base container version.
* **Revert Trigger** `revertTrigger`: Discards the workspace's unpublished changes to a trigger, restoring it to the state in the base container version.
* **Revert Variable** `revertVariable`: Discards the workspace's unpublished changes to a user-defined variable, restoring it to the state in the base container version.
* **Revert Zone** `revertZone`: Discards the workspace's unpublished changes to a zone, restoring it to the state in the base container version.
* **Set Latest Container Version** `setLatestContainerVersion`: Marks a container version as the latest version of the container, without publishing it live.
* **Sync Workspace** `syncWorkspace`: Syncs a workspace to the latest container version by pulling in changes made elsewhere. Entities that changed in both places are returned as merge conflicts to resolve.
* **Undelete Container Version** `undeleteContainerVersion`: Restores a container version that was previously marked as deleted.
* **Update Account** `updateAccount`: Updates a Google Tag Manager account's display name and data sharing setting. Supply the account's current fingerprint to guard against concurrent modification.
* **Update Client** `updateClient`: Updates a client in a Google Tag Manager server-side workspace. The supplied fields replace the existing ones, so send the complete parameter list. Supply the client's current fingerprint to guard against concurrent modification.
* **Update Container** `updateContainer`: Updates a Google Tag Manager container's name, domains, usage context, and notes. Supply the container's current fingerprint to guard against concurrent modification.
* **Update Container Version** `updateContainerVersion`: Updates the name and description of an existing container version. Supply the version's current fingerprint to guard against concurrent modification.
* **Update Environment** `updateEnvironment`: Updates a user-defined environment in a Google Tag Manager container. Supply the environment's current fingerprint to guard against concurrent modification.
* **Update Folder** `updateFolder`: Updates a folder's name and notes in a Google Tag Manager workspace. Supply the folder's current fingerprint to guard against concurrent modification.
* **Update Google Tag Config** `updateGtagConfig`: Updates a Google tag configuration in a Google Tag Manager workspace. The supplied parameters replace the existing ones. Supply the configuration's current fingerprint to guard against concurrent modification.
* **Update Tag** `updateTag`: Updates a tag in a Google Tag Manager workspace. The supplied fields replace the existing ones, so send the complete parameter and trigger lists. Supply the tag's current fingerprint to guard against concurrent modification.
* **Update Template** `updateTemplate`: Updates a custom template in a Google Tag Manager workspace. The supplied template definition replaces the existing one. Supply the template's current fingerprint to guard against concurrent modification.
* **Update Transformation** `updateTransformation`: Updates a transformation in a Google Tag Manager server-side workspace. The supplied fields replace the existing ones. Supply the transformation's current fingerprint to guard against concurrent modification.
* **Update Trigger** `updateTrigger`: Updates a trigger in a Google Tag Manager workspace. The supplied fields replace the existing ones, so send the complete filter list. Supply the trigger's current fingerprint to guard against concurrent modification.
* **Update User Permission** `updateUserPermission`: Changes a user's account-level and container-level permissions on a Google Tag Manager account. The container access list replaces the existing one.
* **Update Variable** `updateVariable`: Updates a user-defined variable in a Google Tag Manager workspace. The supplied fields replace the existing ones, so send the complete parameter list. Supply the variable's current fingerprint to guard against concurrent modification.
* **Update Workspace** `updateWorkspace`: Updates a workspace's name and description. Supply the workspace's current fingerprint to guard against concurrent modification.
* **Update Zone** `updateZone`: Updates a zone in a Google Tag Manager workspace. The supplied fields replace the existing ones, so send the complete child container and boundary configuration. Supply the zone's current fingerprint to guard against concurrent modification.

</details>
