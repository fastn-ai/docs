---
description: "Google Apps Script API for managing Apps Script projects programmatically."
hidden: true
---

# Google Apps Script

<img src="../../.gitbook/assets/connectors/google-apps-script.png" alt="Google Apps Script logo" width="64">

Google Apps Script API for managing Apps Script projects programmatically. Create projects, read and update project content and manifests, manage versions and deployments, run deployed script functions, and inspect execution processes and metrics.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [script.googleapis.com](https://script.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleAppsScript` |

## Use it

Add Google Apps Script from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleAppsScript.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Deployment | `createDeployment` | Creates a deployment of an Apps Script project from a saved version, making it callable as a web app, executable API or add-on. |
| Create Project | `createProject` | Creates a new, empty Apps Script project with the given title, optionally bound to a parent Google Docs, Sheets, Slides or Forms file. |
| Create Version | `createVersion` | Creates a new immutable version of an Apps Script project, snapshotting its current content so it can be deployed. The version number is assigned by Apps Script. |
| Delete Deployment | `deleteDeployment` | Deletes a deployment of an Apps Script project. Any web app or API endpoint served by that deployment stops responding. |
| Get Deployment | `getDeployment` | Retrieves a single deployment of an Apps Script project, including its configuration and entry points such as the published web app URL. |
| Get Project | `getProject` | Retrieves the metadata of an Apps Script project, including its title, bound parent file, creator and last modification details. |
| Get Project Content | `getProjectContent` | Retrieves the source files of an Apps Script project, including the appsscript manifest. Supply a version number to read a saved version rather than the current head content. |
| Get Project Metrics | `getProjectMetrics` | Retrieves usage statistics for an Apps Script project, returning total executions, failed executions and active users at the requested granularity. |
| Get Version | `getVersion` | Retrieves a single saved version of an Apps Script project by version number, including its description and creation time. |
| List Deployments | `listDeployments` | Lists the deployments of an Apps Script project, including the head deployment, with their configurations and entry points. |

<details>

<summary>See 6 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Script Processes | `listScriptProcesses` | Lists the Apps Script executions of one specific script project, with optional filters on deployment, function, status, type, access level and time window. |
| List User Processes | `listUserProcesses` | Lists the Apps Script executions run by or on behalf of the authenticated user across all their script projects, with optional filters on project, function, status, type, access level and time window. |
| List Versions | `listVersions` | Lists every saved version of an Apps Script project, newest last, with pagination support. |
| Run Script Function | `runScriptFunction` | Runs a function in a deployed Apps Script project and returns the result. The script must be deployed as an executable API and the calling credentials must carry every OAuth scope the script itself uses, otherwise the call is rejected. |
| Update Deployment | `updateDeployment` | Updates an existing deployment of an Apps Script project, for example to point it at a newer saved version. The full deployment configuration replaces the previous one. |
| Update Project Content | `updateProjectContent` | Replaces the entire contents of an Apps Script project with the supplied files. The files array must include the appsscript JSON manifest, and any existing file omitted from the array is deleted. |

</details>
