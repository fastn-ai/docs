---
description: "Azure Resource Manager (ARM) control-plane API at https://management.azure.com."
---

# Azure Resource Manager

Azure Resource Manager (ARM) control-plane API at https://management.azure.com. List and manage subscriptions, tenants, locations, resource groups, generic resources, ARM template deployments and deployment operations, resource providers and resource types, subscription tag names and values, resource tags at any scope, and read role assignments, role definitions and effective permissions. Every ARM request requires an api-version query parameter, exposed on each action with the current stable default. Connect with Microsoft Entra ID OAuth 2.0; the signed-in user needs Azure RBAC rights on the target scope.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [management.azure.com](https://management.azure.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 71 |
| **Events** | 0 |
| **Slug** | `azureResourceManager` |

## Use it

Add Azure Resource Manager from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.azureResourceManager.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Calculate Template Hash | `calculateTemplateHash` | Computes the canonical hash of an ARM template, which is a quick way to tell whether two templates are functionally identical. |
| Cancel Deployment | `cancelDeployment` | Cancels a resource group deployment that is still running. Resources already provisioned by the deployment are left in place. |
| Cancel Subscription Deployment | `cancelDeploymentAtSubscriptionScope` | Cancels a running subscription-scope deployment. Resources already provisioned are left in place. |
| Check Resource Name | `checkResourceName` | Checks whether a proposed resource name is allowed, and whether it is reserved or contains a word Azure disallows for that resource type. |
| Check Zone Peers | `checkZonePeers` | Compares the physical availability zone mapping of one subscription against other subscriptions, so that zone-redundant workloads can be pinned to the same physical zones across subscriptions. Note: Azure returns 404 InvalidResourceType unless the subscription is enabled for availability zone peering. |
| Create Or Update Deployment | `createOrUpdateDeployment` | Starts an ARM template deployment into a resource group. Supply the template inline or by link, together with its parameters, and choose Incremental or Complete mode. The deployment runs asynchronously. |
| Create Or Update Resource | `createOrUpdateResource` | Creates or replaces a top-level Azure resource of any type. The properties object carries the resource-type-specific payload, and the api-version must be the one published by that resource's own provider. |
| Create Or Update Resource Group | `createOrUpdateResourceGroup` | Creates a resource group, or replaces an existing one with the supplied location and tags. The location cannot be changed once the group exists. |
| Create Or Update Subscription Deployment | `createOrUpdateDeploymentAtSubscriptionScope` | Starts an ARM template deployment at subscription scope, which is how resource groups and subscription-level resources are created from a template. A location is required because the deployment metadata is stored regionally. |
| Create Tag Name | `createTagName` | Registers a predefined tag name in a subscription so it can be offered when tagging resources. |
| Create Tag Value | `createTagValue` | Registers a predefined value for an existing tag name in a subscription. |
| Delete Deployment | `deleteDeployment` | Deletes the deployment history record for a resource group deployment. The resources the deployment created are not affected. |
| Delete Resource | `deleteResource` | Deletes a top-level Azure resource. The api-version must be the one published by that resource's own provider, and deletion may run asynchronously. |
| Delete Resource Group | `deleteResourceGroup` | Deletes a resource group and every resource inside it. This is irreversible and runs asynchronously, returning 202 Accepted with a status URL. |
| Delete Resource Group Tags | `deleteResourceGroupTags` | Removes every tag from a resource group. |
| Delete Subscription Deployment | `deleteDeploymentAtSubscriptionScope` | Deletes the deployment history record for a subscription-scope deployment. The resources it created are not affected. |
| Delete Subscription Tags | `deleteSubscriptionTags` | Removes every tag from a subscription. |
| Delete Tag Name | `deleteTagName` | Removes a predefined tag name from a subscription. The name must have no registered values and must not be in use on any resource. |
| Delete Tag Value | `deleteTagValue` | Removes a predefined value from a tag name in a subscription. The value must not be in use on any resource. |
| Export Deployment Template | `exportDeploymentTemplate` | Retrieves the ARM template that was used for a past resource group deployment. |
| Export Resource Group Template | `exportResourceGroupTemplate` | Generates an ARM template that describes the current contents of a resource group, which can then be redeployed elsewhere. |
| Export Subscription Deployment Template | `exportDeploymentTemplateAtSubscriptionScope` | Retrieves the ARM template that was used for a past subscription-scope deployment. |
| Get Deployment | `getDeployment` | Retrieves one ARM template deployment in a resource group, including its provisioning state, outputs and the resources it created. |
| Get Deployment Operation | `getDeploymentOperation` | Retrieves one operation from a resource group deployment, including its status code, status message and the resource it targeted. |
| Get Provider Permissions | `getProviderPermissions` | Retrieves the permissions a resource provider holds in a subscription, which explains what the provider's own service principals may do on the customer's behalf. |
| Get Resource | `getResource` | Retrieves a single top-level Azure resource by provider namespace, resource type and name. The api-version must be the one published by that resource's own provider, not the Microsoft.Resources version. |
| Get Resource Group | `getResourceGroup` | Retrieves a single resource group by name, including its location, tags and provisioning state. |
| Get Resource Group Tags | `getResourceGroupTags` | Retrieves the tags applied to a resource group through the Microsoft.Resources tags resource. |
| Get Resource Provider | `getResourceProvider` | Retrieves one Azure resource provider for a subscription, including its registration state and the resource types and API versions it offers. |
| Get Resource Provider At Tenant Scope | `getResourceProviderAtTenantScope` | Retrieves one Azure resource provider at tenant scope, including the resource types and API versions it offers. |
| Get Role Assignment | `getRoleAssignment` | Retrieves one Azure RBAC role assignment defined at subscription scope, by its assignment name (a GUID). |
| Get Role Definition | `getRoleDefinition` | Retrieves one Azure RBAC role definition at subscription scope by its role definition ID, including the actions it allows and denies. |
| Get Subscription | `getSubscription` | Retrieves the details of one Azure subscription, including its display name, state, tenant and subscription policies. |
| Get Subscription Deployment | `getDeploymentAtSubscriptionScope` | Retrieves one ARM template deployment made at subscription scope, including its provisioning state and outputs. |
| Get Subscription Deployment Operation | `getDeploymentOperationAtSubscriptionScope` | Retrieves one operation from a subscription-scope deployment, including its status code and the resource it targeted. |
| Get Subscription Tags | `getSubscriptionTags` | Retrieves the tags applied to a subscription itself, as opposed to the predefined tag names registered inside it. |
| List Deployment Operations | `listDeploymentOperations` | Lists the individual operations that made up a resource group deployment, which is the quickest way to find which resource caused a deployment to fail. |
| List Deployments At Tenant Scope | `listDeploymentsAtTenantScope` | Lists the ARM template deployments made at tenant scope, which are the deployments that create subscriptions or tenant-level resources. |
| List Deployments In Resource Group | `listDeploymentsByResourceGroup` | Lists the ARM template deployments recorded against a resource group, newest first, with their provisioning state and timestamps. |
| List Deployments In Subscription | `listDeploymentsAtSubscriptionScope` | Lists the ARM template deployments made at subscription scope, which are the deployments that create resource groups or subscription-level resources. |
| List Effective Permissions For Resource Group | `listPermissionsForResourceGroup` | Lists the effective permissions the signed-in identity holds on a resource group, flattened into the actions it may and may not perform. |
| List Provider Resource Types | `listProviderResourceTypes` | Lists the resource types offered by one resource provider, with the regions and API versions each type supports. Use it to discover the correct api-version for a resource-type-specific call. |
| List Resource Groups | `listResourceGroups` | Lists the resource groups in a subscription with their locations, tags and provisioning state. |
| List Resource Manager Operations | `listResourceManagerOperations` | Lists the operations exposed by the Microsoft.Resources provider, which is useful for discovering the exact operation names used in Azure role definitions. |
| List Resource Providers | `listResourceProviders` | Lists the Azure resource providers available to a subscription and their registration state. |
| List Resource Providers At Tenant Scope | `listResourceProvidersAtTenantScope` | Lists every Azure resource provider at tenant scope, independent of any one subscription. |
| List Resources In Resource Group | `listResourcesByResourceGroup` | Lists the resources inside one resource group, optionally narrowed by an OData filter on resource type, name or tag. |
| List Resources In Subscription | `listResources` | Lists every resource in a subscription, optionally narrowed by an OData filter on resource type, name, location or tag. |
| List Role Assignments For Resource | `listRoleAssignmentsForResource` | Lists the Azure RBAC role assignments that apply to a single resource. |
| List Role Assignments In Resource Group | `listRoleAssignmentsForResourceGroup` | Lists the Azure RBAC role assignments that apply to a resource group. |
| List Role Assignments In Subscription | `listRoleAssignmentsForSubscription` | Lists the Azure RBAC role assignments in a subscription, each linking a principal to a role definition at a scope. |
| List Role Definitions | `listRoleDefinitions` | Lists the Azure RBAC role definitions available at subscription scope, both built-in roles and custom roles, with the permissions each grants. |
| List Subscription Deployment Operations | `listDeploymentOperationsAtSubscriptionScope` | Lists the individual operations that made up a subscription-scope deployment. |
| List Subscription Locations | `listSubscriptionLocations` | Lists the Azure regions available to a subscription, with their display names, geography and physical coordinates. |
| List Subscriptions | `listSubscriptions` | Lists every Azure subscription the signed-in identity can access, with its display name, state and tenant. Use it first to obtain the subscription ID that most other actions require. |
| List Tag Names | `listTagNames` | Lists the predefined tag names registered in a subscription, together with the values recorded for each and how many resources use them. |
| List Tenants | `listTenants` | Lists the Microsoft Entra ID tenants the signed-in identity can access. |
| Move Resources | `moveResources` | Moves resources from one resource group to another, optionally across subscriptions. The move runs asynchronously and every resource in the request must move together. |
| Preview Deployment Changes | `whatIfDeployment` | Runs a what-if analysis for a resource group deployment, returning the resources the template would create, modify, delete or leave unchanged without applying anything. |
| Preview Subscription Deployment Changes | `whatIfDeploymentAtSubscriptionScope` | Runs a what-if analysis for a subscription-scope deployment, returning the resources and resource groups the template would create, modify or delete without applying anything. |
| Register Resource Provider | `registerResourceProvider` | Registers a resource provider with a subscription so its resource types can be deployed there. |
| Replace Resource Group Tags | `replaceResourceGroupTags` | Replaces the entire set of tags on a resource group. Any tag not present in the request is removed. |
| Replace Subscription Tags | `replaceSubscriptionTags` | Replaces the entire set of tags on a subscription. Any tag not present in the request is removed, so use Update Subscription Tags for a partial change. |
| Unregister Resource Provider | `unregisterResourceProvider` | Unregisters a resource provider from a subscription. Unregistration fails while resources of that provider still exist in the subscription. |
| Update Resource | `updateResource` | Partially updates a top-level Azure resource, most commonly to change its tags. Only the fields you supply are sent, and the api-version must be the one published by that resource's own provider. |
| Update Resource Group | `updateResourceGroup` | Updates the tags, name or managing resource of an existing resource group. Only the properties you supply are changed; the location cannot be updated. |
| Update Resource Group Tags | `updateResourceGroupTags` | Selectively changes the tags on a resource group, merging, replacing or deleting the supplied tags according to the chosen operation. |
| Update Subscription Tags | `updateSubscriptionTags` | Selectively changes the tags on a subscription. The operation chooses whether the supplied tags are merged in, used to replace the whole set, or deleted. |
| Validate Deployment | `validateDeployment` | Validates an ARM template and its parameters against a resource group without deploying anything, reporting any template or parameter errors. |
| Validate Move Resources | `validateMoveResources` | Validates a resource move without performing it, reporting whether every resource could be moved to the target resource group. Returns 204 No Content when the move would succeed and 409 Conflict with details when it would not. |
| Validate Subscription Deployment | `validateDeploymentAtSubscriptionScope` | Validates a subscription-scope ARM template and its parameters without deploying anything. |
