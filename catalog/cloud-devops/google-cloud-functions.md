---
description: "Google Cloud Functions runs serverless code on Google Cloud. Create, update, list, get and delete functions, and manage their access policies."
hidden: true
---

# Google Cloud Functions

<img src="../../.gitbook/assets/connectors/lg/google-cloud-functions.png" alt="Google Cloud Functions logo">

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [cloudfunctions.googleapis.com](https://cloudfunctions.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudFunctions` |

## Setup

Your customers sign in to Google Cloud Functions through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Cloud Functions from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Cloud Functions**.
2. Select **Connect** on the Google Cloud Functions card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Cloud Functions and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Cloud Functions's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Abort Function Upgrade</td><td><code>abortFunctionUpgrade</code></td><td>Aborts the 1st gen to 2nd gen upgrade process for the named function, deleting all 2nd gen copy configuration and resources created during the upgrade. Returns a long-running operation.</td></tr><tr><td>Commit Function Upgrade</td><td><code>commitFunctionUpgrade</code></td><td>Finalizes the 1st gen to 2nd gen upgrade, after which it can no longer be rolled back. This is the last step of the multi-step upgrade and deletes all original 1st gen configuration and resources.</td></tr><tr><td>Commit Function Upgrade As Gen2</td><td><code>commitFunctionUpgradeAsGen2</code></td><td>Commits a function upgrade from Cloud Functions 1st gen to 2nd gen. This deletes the 1st gen function, leaving the 2nd gen function active and manageable through the v2 API. Returns a long-running operation.</td></tr><tr><td>Create Function</td><td><code>createFunction</code></td><td>Creates a new Cloud Function in the given project and location. If a function with that name already exists the returned long-running operation fails with ALREADY_EXISTS. Returns a long-running operation.</td></tr><tr><td>Delete Function</td><td><code>deleteFunction</code></td><td>Deletes the function with the given name from the specified project and location. If the function is used by a trigger, that trigger is updated to remove the function. Returns a long-running operation.</td></tr><tr><td>Detach Function</td><td><code>detachFunction</code></td><td>Detaches a 2nd gen Cloud Function so that it becomes a plain Cloud Run function, no longer managed by the Cloud Functions API. Returns a long-running operation.</td></tr><tr><td>Generate Download URL for Function</td><td><code>generateDownloadUrlFunction</code></td><td>Returns a signed Google Cloud Storage URL for downloading the deployed source code of a function. The URL is valid for a limited period and should be used within 30 minutes of generation.</td></tr><tr><td>Generate Upload URL for Function</td><td><code>generateUploadUrlFunction</code></td><td>Returns a signed Google Cloud Storage URL for uploading function source code as a zip archive. Once the upload completes, pass the returned storage source in a Create Function or Update Function request.</td></tr><tr><td>Get Function</td><td><code>getFunction</code></td><td>Returns the Cloud Function with the given name from the requested project and location, including its build configuration, service configuration, event trigger and deployment state.</td></tr><tr><td>Get IAM Policy for Function</td><td><code>getIamPolicyFunction</code></td><td>Gets the access control policy for a Cloud Function. Returns an empty policy if the function exists and has no policy set.</td></tr></tbody></table>

<details>

<summary>View 11 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Operation</td><td><code>getOperation</code></td><td>Gets the latest state of a Cloud Functions long-running operation. Poll this at the interval recommended by the API to learn when a function deployment has finished.</td></tr><tr><td>List Functions</td><td><code>listFunction</code></td><td>Returns the list of Cloud Functions that belong to the requested project and location, with optional filtering, ordering and pagination.</td></tr><tr><td>List Locations</td><td><code>listLocations</code></td><td>Lists information about the supported Cloud Functions locations for a project. Returns the location id, display name and labels for each region where functions can be deployed.</td></tr><tr><td>List Operations</td><td><code>listOperation</code></td><td>Lists the long-running operations in a Cloud Functions location that match the specified filter. Use it to track the progress of function create, update and delete requests.</td></tr><tr><td>List Runtimes</td><td><code>listRuntime</code></td><td>Returns the list of language runtimes supported for the requested project and location, including each runtime's lifecycle stage and deprecation and decommission dates.</td></tr><tr><td>Redirect Function Upgrade Traffic</td><td><code>redirectFunctionUpgradeTraffic</code></td><td>Changes the traffic target of a function from the original 1st gen function to its 2nd gen copy. This is the second step of the multi-step 1st gen to 2nd gen upgrade; afterwards all new traffic is served by the 2nd gen copy.</td></tr><tr><td>Rollback Function Upgrade Traffic</td><td><code>rollbackFunctionUpgradeTraffic</code></td><td>Reverts the traffic target of a function from its 2nd gen copy back to the original 1st gen function. After this operation all new traffic is served by the 1st gen function.</td></tr><tr><td>Set IAM Policy for Function</td><td><code>setIamPolicyFunction</code></td><td>Sets the access control policy on a Cloud Function, replacing any existing policy. Can return NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED errors.</td></tr><tr><td>Setup Function Upgrade Config</td><td><code>setupFunctionUpgradeConfig</code></td><td>Creates a 2nd gen copy of the configuration of the named 1st gen function. This is the first step of the multi-step upgrade; only the 2nd gen configuration is set up and traffic continues to be served by the 1st gen function.</td></tr><tr><td>Test IAM Permissions for Function</td><td><code>testIamPermissionsFunction</code></td><td>Returns the subset of the supplied permissions that the caller holds on a function. If the function does not exist this returns an empty set rather than a NOT_FOUND error, so it is intended for building permission-aware UIs rather than for authorization checks.</td></tr><tr><td>Update Function</td><td><code>updateFunction</code></td><td>Updates an existing Cloud Function. Supply Update Mask to restrict the change to specific fields; if no field mask is provided every field is updated. Returns a long-running operation.</td></tr></tbody></table>

</details>

