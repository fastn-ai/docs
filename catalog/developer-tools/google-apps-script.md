---
description: "Google Apps Script runs scripts across Google Workspace. Create and update script projects, and manage their versions, deployments and metrics."
hidden: true
---

# Google Apps Script

<img src="../../.gitbook/assets/connectors/lg/google-apps-script.png" alt="Google Apps Script logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [script.googleapis.com](https://script.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleAppsScript` |

## Setup

Your customers sign in to Google Apps Script through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Apps Script from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Apps Script**.
2. Select **Connect** on the Google Apps Script card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Apps Script and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Apps Script's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Deployment</td><td><code>createDeployment</code></td><td>Creates a deployment of an Apps Script project from a saved version, making it callable as a web app, executable API or add-on.</td></tr><tr><td>Create Project</td><td><code>createProject</code></td><td>Creates a new, empty Apps Script project with the given title, optionally bound to a parent Google Docs, Sheets, Slides or Forms file.</td></tr><tr><td>Create Version</td><td><code>createVersion</code></td><td>Creates a new immutable version of an Apps Script project, snapshotting its current content so it can be deployed. The version number is assigned by Apps Script.</td></tr><tr><td>Delete Deployment</td><td><code>deleteDeployment</code></td><td>Deletes a deployment of an Apps Script project. Any web app or API endpoint served by that deployment stops responding.</td></tr><tr><td>Get Deployment</td><td><code>getDeployment</code></td><td>Retrieves a single deployment of an Apps Script project, including its configuration and entry points such as the published web app URL.</td></tr><tr><td>Get Project</td><td><code>getProject</code></td><td>Retrieves the metadata of an Apps Script project, including its title, bound parent file, creator and last modification details.</td></tr><tr><td>Get Project Content</td><td><code>getProjectContent</code></td><td>Retrieves the source files of an Apps Script project, including the appsscript manifest. Supply a version number to read a saved version rather than the current head content.</td></tr><tr><td>Get Project Metrics</td><td><code>getProjectMetrics</code></td><td>Retrieves usage statistics for an Apps Script project, returning total executions, failed executions and active users at the requested granularity.</td></tr><tr><td>Get Version</td><td><code>getVersion</code></td><td>Retrieves a single saved version of an Apps Script project by version number, including its description and creation time.</td></tr><tr><td>List Deployments</td><td><code>listDeployments</code></td><td>Lists the deployments of an Apps Script project, including the head deployment, with their configurations and entry points.</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Script Processes</td><td><code>listScriptProcesses</code></td><td>Lists the Apps Script executions of one specific script project, with optional filters on deployment, function, status, type, access level and time window.</td></tr><tr><td>List User Processes</td><td><code>listUserProcesses</code></td><td>Lists the Apps Script executions run by or on behalf of the authenticated user across all their script projects, with optional filters on project, function, status, type, access level and time window.</td></tr><tr><td>List Versions</td><td><code>listVersions</code></td><td>Lists every saved version of an Apps Script project, newest last, with pagination support.</td></tr><tr><td>Run Script Function</td><td><code>runScriptFunction</code></td><td>Runs a function in a deployed Apps Script project and returns the result. The script must be deployed as an executable API and the calling credentials must carry every OAuth scope the script itself uses, otherwise the call is rejected.</td></tr><tr><td>Update Deployment</td><td><code>updateDeployment</code></td><td>Updates an existing deployment of an Apps Script project, for example to point it at a newer saved version. The full deployment configuration replaces the previous one.</td></tr><tr><td>Update Project Content</td><td><code>updateProjectContent</code></td><td>Replaces the entire contents of an Apps Script project with the supplied files. The files array must include the appsscript JSON manifest, and any existing file omitted from the array is deleted.</td></tr></tbody></table>

</details>

