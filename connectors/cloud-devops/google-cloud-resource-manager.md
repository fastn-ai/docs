---
description: "Google Cloud Resource Manager API v3 connector (https://cloudresourcemanager.googleapis.com/v3)."
---

# Google Cloud Resource Manager

Google Cloud Resource Manager API v3 connector (https://cloudresourcemanager.googleapis.com/v3). Programmatically manage the Google Cloud resource hierarchy: create, get, list, search, update, delete, undelete, and move projects and folders; read organizations; manage IAM policies on projects, folders, and organizations; and administer tags (tag keys, tag values, tag bindings, tag holds, effective tags), liens, capabilities, tag binding collections, and long-running operations. OAuth 2.0 (Google) authorization-code auth.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [cloudresourcemanager.googleapis.com](https://cloudresourcemanager.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 62 |
| **Events** | 0 |
| **Slug** | `googleCloudResourceManager` |

## Use it

Add Google Cloud Resource Manager from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudResourceManager.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Folder | `createFolder` | Create a new folder under the specified parent (an organization or another folder). The folder's display name must be unique among its siblings. Returns a long-running Operation. |
| Create Lien | `createLien` | Create a lien that blocks specified operations (such as project deletion) on a resource until the lien is removed. |
| Create Project | `createProject` | Create a new Google Cloud project under the specified parent (an organization or folder). Returns a long-running Operation; poll it with Get Operation until done to obtain the created project. |
| Create Tag Binding | `createTagBinding` | Bind a tag value to a cloud resource. Supply the tag value either by resource name (tagValue) or by namespaced name (tagValueNamespacedName). Returns a long-running Operation. |
| Create Tag Hold | `createTagHold` | Create a tag hold under the specified tag value, recording that a resource is using the tag value and preventing its deletion. Returns a long-running Operation. |
| Create Tag Key | `createTagKey` | Create a new tag key under the specified parent organization or project. The short name must be unique within the tag namespace. Returns a long-running Operation. |
| Create Tag Value | `createTagValue` | Create a new tag value under the specified parent tag key. The short name must be unique within the parent tag key. Returns a long-running Operation. |
| Delete Folder | `deleteFolder` | Mark the specified folder for deletion, moving it to the DELETE_REQUESTED state. The folder must not contain any active projects or sub-folders. Returns a long-running Operation. |
| Delete Lien | `deleteLien` | Delete the specified lien, removing the restriction it enforced. |
| Delete Project | `deleteProject` | Mark the specified project for deletion, moving it to the DELETE_REQUESTED state. The project can be restored with Undelete Project within the recovery window. Returns a long-running Operation. |
| Delete Tag Binding | `deleteTagBinding` | Delete the specified tag binding, detaching a tag value from a resource. Returns a long-running Operation. |
| Delete Tag Hold | `deleteTagHold` | Delete the specified tag hold under a tag value. Returns a long-running Operation. |
| Delete Tag Key | `deleteTagKey` | Delete the specified tag key. The tag key must not have any child tag values. Returns a long-running Operation. |
| Delete Tag Value | `deleteTagValue` | Delete the specified tag value. The tag value must not have any tag holds or tag bindings referencing it. Returns a long-running Operation. |
| Get Effective Tag Binding Collection | `getEffectiveTagBindingCollection` | Retrieve the effective tag binding collection for a resource in a given location, including tags bound directly and inherited from ancestors. |
| Get Folder | `getFolder` | Retrieve the folder identified by the specified folder ID. Returns the folder including its parent, display name, and lifecycle state. |
| Get Folder Capability | `getFolderCapability` | Retrieve a capability (a managed feature toggle) on the specified folder, such as app-management. |
| Get Folder IAM Policy | `getFolderIamPolicy` | Return the IAM access control policy for the specified folder. Requires the resourcemanager.folders.getIamPolicy permission. |
| Get Lien | `getLien` | Retrieve the lien identified by the specified lien ID. |
| Get Namespaced Tag Key | `getNamespacedTagKey` | Retrieve a tag key by its namespaced name, of the form {parentId}/{shortName} (e.g. 42/env for a key under organization 42, or my-project/env for a key under a project). |
| Get Namespaced Tag Value | `getNamespacedTagValue` | Retrieve a tag value by its namespaced name, of the form {parentId}/{tagKeyShortName}/{tagValueShortName} (e.g. 42/env/prod). |
| Get Operation | `getOperation` | Retrieve the latest state of a long-running operation returned by a create, update, delete, undelete, or move action. Poll until done is true. |
| Get Organization | `getOrganization` | Retrieve the organization identified by the specified organization ID. Returns the organization including its display name, directory customer ID, and lifecycle state. |
| Get Organization IAM Policy | `getOrganizationIamPolicy` | Return the IAM access control policy for the specified organization. Requires the resourcemanager.organizations.getIamPolicy permission. |
| Get Project | `getProject` | Retrieve the project identified by the specified project ID or project number. Returns the project including its state, parent, labels, and display name. |
| Get Project IAM Policy | `getProjectIamPolicy` | Return the IAM access control policy for the specified project. Requires the resourcemanager.projects.getIamPolicy permission. |
| Get Tag Binding Collection | `getTagBindingCollection` | Retrieve the tag binding collection for a resource in a given location, listing the tag values bound directly to that resource. |
| Get Tag Key | `getTagKey` | Retrieve the tag key identified by the specified tag key ID. |
| Get Tag Key IAM Policy | `getTagKeyIamPolicy` | Return the IAM access control policy for the specified tag key. |
| Get Tag Value | `getTagValue` | Retrieve the tag value identified by the specified tag value ID. |
| Get Tag Value IAM Policy | `getTagValueIamPolicy` | Return the IAM access control policy for the specified tag value. |
| List Effective Tags | `listEffectiveTags` | List all effective tags on the specified resource, including tags bound directly and tags inherited from ancestors in the resource hierarchy. |
| List Folders | `listFolders` | List the folders that are direct children of the specified parent. Requires the resourcemanager.folders.list permission on the parent. |
| List Liens | `listLiens` | List all liens applied to the specified resource. |
| List Projects | `listProjects` | List the active, non-deleted projects that are direct children of the specified parent. The caller must have the resourcemanager.projects.list permission on the parent. |
| List Tag Bindings | `listTagBindings` | List the tag bindings directly attached to the specified resource. |
| List Tag Holds | `listTagHolds` | List the tag holds under the specified tag value, optionally filtered by holder or origin. |
| List Tag Keys | `listTagKeys` | List every tag key directly under the specified parent organization or project. |
| List Tag Values | `listTagValues` | List every tag value directly under the specified parent tag key. |
| Move Folder | `moveFolder` | Move the specified folder to a new parent (an organization or another folder). Returns a long-running Operation. |
| Move Project | `moveProject` | Move the specified project to a new parent (an organization or folder). Returns a long-running Operation. |
| Search Folders | `searchFolders` | Search across all folders the caller has resourcemanager.folders.get permission on, optionally filtered by a query on fields such as displayName, parent, and state. |
| Search Organizations | `searchOrganizations` | Search the organizations the caller has resourcemanager.organizations.get permission on, optionally filtered by a query on the directory customer ID or domain. |
| Search Projects | `searchProjects` | Search across all projects the caller has resourcemanager.projects.get permission on, optionally filtered by a query on fields such as displayName, parent, id, state, and labels. |
| Set Folder IAM Policy | `setFolderIamPolicy` | Set the IAM access control policy for the specified folder, replacing any existing policy. Requires the resourcemanager.folders.setIamPolicy permission. |
| Set Organization IAM Policy | `setOrganizationIamPolicy` | Set the IAM access control policy for the specified organization, replacing any existing policy. Requires the resourcemanager.organizations.setIamPolicy permission. |
| Set Project IAM Policy | `setProjectIamPolicy` | Set the IAM access control policy for the specified project, replacing any existing policy. Requires the resourcemanager.projects.setIamPolicy permission. |
| Set Tag Key IAM Policy | `setTagKeyIamPolicy` | Set the IAM access control policy for the specified tag key, replacing any existing policy. |
| Set Tag Value IAM Policy | `setTagValueIamPolicy` | Set the IAM access control policy for the specified tag value, replacing any existing policy. |
| Test Folder IAM Permissions | `testFolderIamPermissions` | Return which of the specified permissions the caller holds on the given folder. |
| Test Organization IAM Permissions | `testOrganizationIamPermissions` | Return which of the specified permissions the caller holds on the given organization. |
| Test Project IAM Permissions | `testProjectIamPermissions` | Return which of the specified permissions the caller holds on the given project. |
| Test Tag Key IAM Permissions | `testTagKeyIamPermissions` | Return which of the specified permissions the caller holds on the given tag key. |
| Test Tag Value IAM Permissions | `testTagValueIamPermissions` | Return which of the specified permissions the caller holds on the given tag value. |
| Undelete Folder | `undeleteFolder` | Restore a folder that is in the DELETE_REQUESTED state back to ACTIVE. Returns a long-running Operation. |
| Undelete Project | `undeleteProject` | Restore a project that is in the DELETE_REQUESTED state back to ACTIVE. Returns a long-running Operation. |
| Update Folder | `updateFolder` | Update the display name of the specified folder. The updateMask controls which fields are changed. To change a folder's parent, use Move Folder instead. |
| Update Folder Capability | `updateFolderCapability` | Enable or disable a capability on the specified folder. Returns a long-running Operation. |
| Update Project | `updateProject` | Update the mutable fields (display name and labels) of the specified project. The updateMask controls which fields are changed. To change a project's parent, use Move Project instead. |
| Update Tag Binding Collection | `updateTagBindingCollection` | Replace the tag bindings on a resource in a given location by updating its tag binding collection. Returns a long-running Operation. |
| Update Tag Key | `updateTagKey` | Update the mutable fields (description and allowedValuesRegex) of the specified tag key. The updateMask controls which fields are changed. Returns a long-running Operation. |
| Update Tag Value | `updateTagValue` | Update the description of the specified tag value. The updateMask controls which fields are changed. Returns a long-running Operation. |
