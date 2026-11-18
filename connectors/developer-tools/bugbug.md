---
description: "BugBug browser test automation."
hidden: true
---

# BugBug

<img src="../../.gitbook/assets/connectors/lg/bugbug.png" alt="BugBug logo">

BugBug browser test automation. Public API v2: tests, suites, test runs, suite runs, steps, groups, components, folders, variables, profiles, projects, project settings, backups, visual regression reference screenshots, and YAML/ZIP import-export.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [bugbug.io](https://bugbug.io) |
| **Authentication** | API key |
| **Slug** | `bugbug` |

## Use it

Add BugBug from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bugbug.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check API Status And Token | `getApiStatus` | Health check that also confirms the API token authenticates. Returns {status, authenticated}. |
| Check Project Import | `checkProjectImport` | Dry-run of a whole-project import: inspects a project export ZIP and reports what it contains, without changing anything. The ZIP is sent as a multipart file part named 'file'. |
| Check Test Import | `checkTestImport` | Dry-run of a test import: validates the YAML and reports what would be created, updated or conflict, without changing anything. |
| Create Component | `createComponent` | Creates a reusable component (a shared step group). WARNING: the v2 API has no delete route for components - neither /components/{id}/ nor /groups/{id}/ accepts the component id - so a component created here can only be removed from the BugBug web app. |
| Create Folder | `createFolder` | Creates a folder for organising tests and components. Undocumented but live v2 route. kind is required by the API; "test" is the verified value (the API rejects "tests" with invalidChoice). |
| Create Group | `createGroup` | Creates a step group inside a test. testId is required. Set isComponent=true to make the group a reusable component. |
| Create Step | `createStep` | Creates a step inside a group. type selects the step shape (goto, click, type, change, assert, execute, scroll, ...) and each type adds its own fields, e.g. goto needs url. |
| Create Suite | `createSuite` | Creates a test suite. runProfileId is required. Optionally pass the list of test UUIDs and before-all/after-all hooks. |
| Create Test | `createTest` | Creates a new, empty test in the project. Returns the created test with its UUID. Add steps afterwards with Create Step. |
| Create Variable | `createVariable` | Undocumented but live v2 route. NOTE: the API exposes no DELETE for variables - a variable created here can only be removed in the BugBug web app. |

<details>

<summary>See 71 more actions</summary>

* **Create Visual Regression Reference Screenshot** `createReferenceScreenshot`: Stores a reference screenshot for a visual-regression step. The API requires a real multipart image upload in the 'screenshot' part (a URL string is rejected with "The submitted data was not a file"), so imageContent must carry the raw image bytes.
* **Delete Folder** `deleteFolder`: Permanently removes a folder. Undocumented but live v2 route. Returns 204 with no body.
* **Delete Group** `deleteGroup`: Permanently removes a step group and the steps inside it. Returns 204 with no body. NOTE: this does NOT delete components - a component created by Create Component is not addressable here (its id returns 404 "Group Not found") and the v2 API exposes no delete route for components at all.
* **Delete Step** `deleteStep`: Permanently removes one step from its test. Returns 204 with no body.
* **Delete Suite** `deleteSuite`: Permanently removes a suite. The tests it contained are not deleted. Returns 204 with no body.
* **Delete Test** `deleteTest`: Permanently removes a test and its steps. Returns 204 with no body. Irreversible.
* **Delete Visual Regression Reference Screenshot** `deleteReferenceScreenshot`: Permanently removes a stored visual-regression reference screenshot. Returns 204 with no body.
* **Download Project Backup** `downloadProjectBackup`: Downloads one stored project backup archive by its id.
* **Download Test Run Debug Artifact** `getTestRunDebugArtifact`: Downloads one debug artifact of a test run by artifact type: chrome_debug_logs, cloud_logs, container_stats, dom_snapshot, logs, logs_partial or network_logs.
* **Export Project** `exportProject`: Exports the whole project (tests, suites, components, settings) as a ZIP archive containing bugbug-export.json and per-test YAML files.
* **Export Test** `exportTest`: Exports a single test in BugBug YAML format (fmt=yaml) or as a ZIP archive (fmt=zip).
* **Get Component Usage** `getComponentUsage`: Returns how many tests use a component and their ids. IMPORTANT: id here is the component RELATION id that appears in a test's groups[] (the entry whose isComponent is true), not the component id returned by Create Component or List Components - that one 404s.
* **Get Folder** `getFolder`: Returns one folder by UUID. Undocumented but live v2 route.
* **Get Group** `getGroup`: Returns a single step group by UUID with its steps.
* **Get Run Profile** `getProfile`: Returns a single run profile by UUID.
* **Get Settings For Token Project** `getSettings`: Returns the run settings (browser size, language, timeouts, selector methods, incognito mode) of the project the API token belongs to.
* **Get Settings Of Project By Id** `getProjectSettingsById`: Returns the run settings of a specific project, addressed by its UUID.
* **Get Step** `getStep`: Returns a single test step by UUID, with its type-specific fields and waiting conditions.
* **Get Suite** `getSuite`: Returns a single test suite by UUID with its tests, before-all/after-all hooks, retry and parallel settings.
* **Get Suite Run** `getSuiteRun`: Returns full details of one suite run, including the individual test runs it contains.
* **Get Suite Run JUnit Report** `getSuiteRunJunitReport`: Returns the JUnit XML report for a whole suite run, for CI pipelines.
* **Get Suite Run Screenshots** `getSuiteRunScreenshots`: Returns the screenshots captured across all test runs of a suite run.
* **Get Suite Run Status** `getSuiteRunStatus`: Lightweight polling endpoint returning only the current status of a suite run.
* **Get Test** `getTest`: Returns a single test by its UUID, including its groups, notes, screen size type and web app URL.
* **Get Test Run** `getTestRun`: Returns full details of one test run, including step results, timings and failure reason.
* **Get Test Run JUnit Report** `getTestRunJunitReport`: Returns the JUnit XML report for a test run, for CI pipelines.
* **Get Test Run Logs** `getTestRunLogs`: Returns the execution logs recorded for a test run.
* **Get Test Run Screenshots** `getTestRunScreenshots`: Returns the screenshots captured during a test run, per step.
* **Get Test Run Status** `getTestRunStatus`: Lightweight polling endpoint returning only the current status of a test run.
* **Get Variable** `getVariable`: Returns one project variable. The path identifier is the variable KEY (not a UUID) - a UUID 404s. Undocumented but live v2 route.
* **Get Visual Regression Reference Screenshot** `getReferenceScreenshot`: Returns one visual-regression reference screenshot record by its UUID.
* **Get YAML Schema** `getYamlSchema`: Returns the JSON Schema (v1) that describes the BugBug YAML test format used by export and import.
* **Import Test From YAML** `importTest`: Imports a test from a BugBug YAML document, creating or updating it. Pass the YAML text in fileContent and a filename. Returns 201 with status=created, or 200 with status=conflict when a test with that slug already exists.
* **Insert Component Into Test** `insertComponentIntoTest`: Inserts a reusable component into a test at an optional position. Prefer componentId; the legacy groupId field is still accepted.
* **List Cloud Runner IP Addresses** `listRunnerIps`: Returns the outbound IP addresses BugBug cloud runners use, for allow-listing in a firewall.
* **List Components** `listComponents`: Returns the paginated list of reusable components (shared step groups) in the project.
* **List Folders** `listFolders`: Returns the folders used to organise tests and components. Undocumented but live v2 route.
* **List Groups** `listGroups`: Returns the paginated list of step groups in the project (components are groups with isComponent=true).
* **List Organizations** `listOrganizations`: Returns the organizations the API token can see. Undocumented but live v2 route.
* **List Project Backups** `listProjectBackups`: Returns the automatic backup schedule of a project and the list of stored backups.
* **List Project Settings** `listProjectSettings`: Returns the run settings via the projects collection route (/projects/settings/). Equivalent payload to Get Settings For Token Project.
* **List Projects** `listProjects`: Returns the projects the API token can access, with their organization.
* **List Run Profiles** `listProfiles`: Returns the paginated list of run profiles (named sets of run variables/settings) in the project.
* **List Suite Run Debug Artifacts** `listSuiteRunDebugArtifacts`: Lists the debug artifacts available across the test runs of a suite run.
* **List Suite Runs** `listSuiteRuns`: Returns the paginated list of suite runs, filterable by suiteId, status and start time window.
* **List Suites** `listSuites`: Returns the paginated list of test suites in the project, each with its tests, before-all/after-all hooks and run profile.
* **List Test Run Debug Artifacts** `listTestRunDebugArtifacts`: Lists the debug artifacts available for a test run (logs, network logs, DOM snapshots, container stats).
* **List Test Runs** `listTestRuns`: Returns the paginated list of single-test runs, filterable by testId, status and start time window.
* **List Tests** `listTests`: Returns the paginated list of tests in the project. Optional filters: folderId, noFolder, latestRun, ordering, query, page, page_size.
* **List Variables** `listVariables`: Returns the project variables plus BugBug's built-in variables (randomNumber, randomName, ...). Undocumented but live v2 route. Returns a bare JSON array.
* **List Visual Regression Reference Screenshots** `listReferenceScreenshots`: Lists the stored visual-regression reference screenshots for one step. step_id is required by the API.
* **Move Step Within Test** `updateStepPosition`: Moves a step to a different group or index inside a test.
* **Replace Group** `replaceGroup`: Full PUT replacement of a step group's name, active flag, component flag and folder.
* **Replace Step** `replaceStep`: Full PUT replacement of a step. Send the complete object including type and the type's required fields; omitted fields are reset.
* **Replace Suite** `replaceSuite`: Full PUT replacement of a suite. Every field you omit is reset to its default, so send the whole object. runProfileId is required.
* **Replace Visual Regression Reference Screenshot** `replaceReferenceScreenshot`: Full PUT replacement of a stored reference screenshot. The API requires a real multipart image upload in the 'screenshot' part.
* **Resolve Visual Regression Difference** `resolveVisualRegression`: Resolves a visual-regression difference on a step run, either by accepting the new screenshot as the reference or by raising the allowed max difference.
* **Run Project Import** `runProjectImport`: WARNING - starts the actual project import for a previously validated uploadId and creates a project from it. Returns 202 with the resulting projectId.
* **Start Suite Run** `startSuiteRun`: WARNING - this starts real cloud browser runs for every test in the suite and consumes plan run minutes. Optionally override the base URL and run variables.
* **Start Test Run** `startTestRun`: WARNING - this starts a real cloud browser run of the given test against whatever site that test targets, and consumes plan run minutes. Returns the created test run. Poll Get Test Run Status for progress.
* **Stop Suite Run** `stopSuiteRun`: Stops a suite run that is queued or running, along with its pending test runs.
* **Stop Test Run** `stopTestRun`: Stops a test run that is queued or running, freeing the remaining run minutes.
* **Unlink Component From Test** `unlinkComponentFromTest`: Removes the link between a test and a component instance. groupId is the component relation id inside the test.
* **Update Folder** `updateFolder`: Renames a folder. Undocumented but live v2 route (PATCH only - the API exposes no PUT for folders).
* **Update Group** `updateGroup`: Partially updates a step group, for example renaming it or promoting it to a component.
* **Update Step** `updateStep`: Partially updates a step - rename it, disable it, change its URL or selector, adjust sleep and timeouts.
* **Update Suite** `updateSuite`: Partially updates a suite: rename it, change retry/parallel settings, or swap its test list.
* **Update Test** `updateTest`: Partially updates a test's name, notes, screen size type or folder. Only the fields you send are changed.
* **Update Variable** `updateVariable`: Updates a project variable's value or description. The path identifier is the variable KEY (not a UUID). Undocumented but live v2 route (PATCH only; the API exposes no DELETE for variables).
* **Update Visual Regression Reference Screenshot** `updateReferenceScreenshot`: Partially updates a stored reference screenshot. The only mutable field is the image itself and the API still requires the multipart 'screenshot' file part - an empty PATCH returns 400 "No file was submitted".
* **Validate Project Import** `validateProjectImport`: Uploads and validates a project export ZIP and returns an uploadId. Pass that uploadId to Run Project Import to actually perform the import.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Schedule finished | `scheduleFinished` | Fires when a scheduled run ends, with per-result suite and test lists (each truncated to 10 items). REGISTRATION IS UI-ONLY. |
| Schedule started | `scheduleStarted` | Fires when a scheduled run starts. REGISTRATION IS UI-ONLY. |
| Suite finished | `suiteFinished` | Fires when a suite run ends, with per-result test lists (each list truncated to 10 items, flagged by the matching *Truncated field). REGISTRATION IS UI-ONLY. |
| Suite started | `suiteStarted` | Fires when a suite run starts. REGISTRATION IS UI-ONLY. |
| Test finished | `testFinished` | Fires when a test run ends (passed, failed or BugBug internal error). REGISTRATION IS UI-ONLY. |
| Test started | `testStarted` | Fires when a test run starts. REGISTRATION IS UI-ONLY - BugBug has no alerts API (/v2/alerts/ and /v2/notifications/ both 404). Payload shape is author-defined; the schema below is the recommended body. |
