---
description: "Manage Google Cloud Functions (2nd gen) through the Cloud Functions API v2: create, update, list, get and delete functions, generate signed upload and…"
hidden: true
---

# Google Cloud Functions

<img src="../../.gitbook/assets/connectors/lg/google-cloud-functions.png" alt="Google Cloud Functions logo">

Manage Google Cloud Functions (2nd gen) through the Cloud Functions API v2: create, update, list, get and delete functions, generate signed upload and download URLs, manage IAM policies, list supported runtimes and locations, run the 1st-gen to 2nd-gen upgrade workflow, and poll long-running operations.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [cloudfunctions.googleapis.com](https://cloudfunctions.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudFunctions` |

## Use it

Add Google Cloud Functions from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudFunctions.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Abort Function Upgrade | `abortFunctionUpgrade` | Aborts the 1st gen to 2nd gen upgrade process for the named function, deleting all 2nd gen copy configuration and resources created during the upgrade. Returns a long-running operation. |
| Commit Function Upgrade | `commitFunctionUpgrade` | Finalizes the 1st gen to 2nd gen upgrade, after which it can no longer be rolled back. This is the last step of the multi-step upgrade and deletes all original 1st gen configuration and resources. |
| Commit Function Upgrade As Gen2 | `commitFunctionUpgradeAsGen2` | Commits a function upgrade from Cloud Functions 1st gen to 2nd gen. This deletes the 1st gen function, leaving the 2nd gen function active and manageable through the v2 API. Returns a long-running operation. |
| Create Function | `createFunction` | Creates a new Cloud Function in the given project and location. If a function with that name already exists the returned long-running operation fails with ALREADY_EXISTS. Returns a long-running operation. |
| Delete Function | `deleteFunction` | Deletes the function with the given name from the specified project and location. If the function is used by a trigger, that trigger is updated to remove the function. Returns a long-running operation. |
| Detach Function | `detachFunction` | Detaches a 2nd gen Cloud Function so that it becomes a plain Cloud Run function, no longer managed by the Cloud Functions API. Returns a long-running operation. |
| Generate Download URL for Function | `generateDownloadUrlFunction` | Returns a signed Google Cloud Storage URL for downloading the deployed source code of a function. The URL is valid for a limited period and should be used within 30 minutes of generation. |
| Generate Upload URL for Function | `generateUploadUrlFunction` | Returns a signed Google Cloud Storage URL for uploading function source code as a zip archive. Once the upload completes, pass the returned storage source in a Create Function or Update Function request. |
| Get Function | `getFunction` | Returns the Cloud Function with the given name from the requested project and location, including its build configuration, service configuration, event trigger and deployment state. |
| Get IAM Policy for Function | `getIamPolicyFunction` | Gets the access control policy for a Cloud Function. Returns an empty policy if the function exists and has no policy set. |

<details>

<summary>See 11 more actions</summary>

* **Get Operation** `getOperation`: Gets the latest state of a Cloud Functions long-running operation. Poll this at the interval recommended by the API to learn when a function deployment has finished.
* **List Functions** `listFunction`: Returns the list of Cloud Functions that belong to the requested project and location, with optional filtering, ordering and pagination.
* **List Locations** `listLocations`: Lists information about the supported Cloud Functions locations for a project. Returns the location id, display name and labels for each region where functions can be deployed.
* **List Operations** `listOperation`: Lists the long-running operations in a Cloud Functions location that match the specified filter. Use it to track the progress of function create, update and delete requests.
* **List Runtimes** `listRuntime`: Returns the list of language runtimes supported for the requested project and location, including each runtime's lifecycle stage and deprecation and decommission dates.
* **Redirect Function Upgrade Traffic** `redirectFunctionUpgradeTraffic`: Changes the traffic target of a function from the original 1st gen function to its 2nd gen copy. This is the second step of the multi-step 1st gen to 2nd gen upgrade; afterwards all new traffic is served by the 2nd gen copy.
* **Rollback Function Upgrade Traffic** `rollbackFunctionUpgradeTraffic`: Reverts the traffic target of a function from its 2nd gen copy back to the original 1st gen function. After this operation all new traffic is served by the 1st gen function.
* **Set IAM Policy for Function** `setIamPolicyFunction`: Sets the access control policy on a Cloud Function, replacing any existing policy. Can return NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED errors.
* **Setup Function Upgrade Config** `setupFunctionUpgradeConfig`: Creates a 2nd gen copy of the configuration of the named 1st gen function. This is the first step of the multi-step upgrade; only the 2nd gen configuration is set up and traffic continues to be served by the 1st gen function.
* **Test IAM Permissions for Function** `testIamPermissionsFunction`: Returns the subset of the supplied permissions that the caller holds on a function. If the function does not exist this returns an empty set rather than a NOT_FOUND error, so it is intended for building permission-aware UIs rather than for authorization checks.
* **Update Function** `updateFunction`: Updates an existing Cloud Function. Supply Update Mask to restrict the change to specific fields; if no field mask is provided every field is updated. Returns a long-running operation.

</details>
