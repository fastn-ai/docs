---
description: "Make (formerly Integromat) is a visual workflow automation and iPaaS platform."
hidden: true
---

# Make

<img src="../../.gitbook/assets/connectors/make.png" alt="Make logo" width="64">

Make (formerly Integromat) is a visual workflow automation and iPaaS platform. This connector covers the Make Public API v2: scenarios, scenario folders, scenario labels, organizations, teams, connections, data stores and records, hooks (custom webhooks), templates, users, notifications, keys (keychain), and custom (SDK) apps. Base URL is zone-specific (e.g. https://eu1.make.com/api/v2) and authenticates with a per-user API token.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [make.com](https://make.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `make` |

## Use it

Add Make from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.make.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Organization Invitation | `acceptOrganizationInvitation` | Accepts a pending invitation to join an organization using its invitation hash. |
| Add Scenario Build Variables | `addScenarioBuildVariables` | Adds new buildtime variables to a scenario, given an array of name/value pairs. |
| Check Scenario Module Data | `checkScenarioModuleData` | Checks whether stored data (e.g. a data structure sample or static IML variable) exists for a given module within a scenario. |
| Clone Data Structure | `cloneDataStructure` | Clones a data structure to the same or a different team. |
| Clone Scenario | `cloneScenario` | Creates a copy of a scenario, optionally in a different team or organization, with remapped connections and webhooks. |
| Clone SDK App | `cloneSdkApp` | Clones a custom app to a new app name and version. |
| Clone SDK App To Next Major Version | `cloneMajorSdkApp` | Clones a custom app to the next major version under the same app name. Requires the account's app-development feature to be enabled. |
| Count Trashed Scenarios | `countTrashedScenarios` | Returns the number of scenarios currently in the trash for a given team, awaiting permanent deletion. |
| Create API Token | `createApiToken` | Creates a new API token for the authenticated user with the given scopes. |
| Create Connection | `createConnection` | Creates a new app connection in a team from the given account type and credential data. |

<details>

<summary>See 151 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Data Store | `createDataStore` | Creates a new data store backed by a data structure, with a maximum size limit. |
| Create Data Store Record | `createDataStoreRecord` | Creates a new record in a data store, optionally with a custom key (auto-generated if omitted). |
| Create Data Structure | `createDataStructure` | Creates a new data structure (a named field schema) that can be used to define a data store or scenario data. |
| Create Hook | `createHook` | Creates a new custom webhook that generates a URL external services can POST to in order to trigger a scenario. |
| Create Key | `createKey` | Creates a new key in a team's keychain, storing reusable credential material such as an API key, certificate, or proxy configuration. |
| Create Organization Variable | `createOrganizationVariable` | Creates a new custom variable at the organization level, available to every scenario in the organization. |
| Create Scenario | `createScenario` | Creates a new scenario in a team from a blueprint (a serialized JSON automation flow) and a scheduling configuration. |
| Create Scenario Folder | `createScenarioFolder` | Creates a new scenario folder in a team, optionally nested under a parent folder. |
| Create Scenario Label | `createScenarioLabel` | Creates a new colour-coded scenario label in a team. Label names must be unique within the team. |
| Create SDK App | `createSdkApp` | Creates a new custom (SDK) app for building a private or public Make integration. |
| Create SDK App Function | `createSdkAppFunction` | Creates a new custom IML function in a custom app. |
| Create Team | `createTeam` | Creates a new team within an organization, optionally with an operations limit. |
| Create Team Variable | `createTeamVariable` | Creates a new custom variable at the team level, available to every scenario in the team. |
| Create Template | `createTemplate` | Creates a new private scenario template from a blueprint and scheduling configuration. |
| Delete API Token | `deleteApiToken` | Deletes the authenticated user's API token with the specified creation timestamp. |
| Delete Connection | `deleteConnection` | Deletes a connection, given its ID. |
| Delete Data Store Records | `deleteDataStoreRecords` | Deletes specified records, or all records, from a data store. |
| Delete Data Stores | `deleteDataStores` | Deletes one or more data stores by ID, or every data store in a team. |
| Delete Data Structure | `deleteDataStructure` | Deletes a data structure, given its ID. |
| Delete Hook | `deleteHook` | Deletes a hook. Requires confirmation if it is currently assigned to a scenario. |
| Delete Hook Incomings | `deleteHookIncomings` | Deletes items from the processing queue of a hook, either by ID or all at once. |
| Delete Key | `deleteKey` | Removes a key from a team's keychain. |
| Delete Notifications | `deleteNotifications` | Deletes notifications with the given IDs. |
| Delete Organization | `deleteOrganization` | Permanently removes an organization and every team within it. This is irreversible. |
| Delete Organization Variable | `deleteOrganizationVariable` | Removes a custom variable from the organization. |
| Delete Scenario | `deleteScenario` | Moves a scenario to the trash. Trashed scenarios can be restored within a retention window using Restore Scenario. |
| Delete Scenario Folder | `deleteScenarioFolder` | Deletes a scenario folder. Scenarios inside move to the parent folder or become uncategorized at the top level. |
| Delete SDK App | `deleteSdkApp` | Deletes a version of a custom (SDK) app. |
| Delete SDK App Function | `deleteSdkAppFunction` | Deletes a custom IML function from an app. |
| Delete Team | `deleteTeam` | Permanently deletes a team and all its data, including scenarios, connections, and data stores. |
| Delete Team Variable | `deleteTeamVariable` | Removes a custom variable from a team. |
| Delete Template | `deleteTemplate` | Deletes a template, given its ID. |
| Disable Hook | `disableHook` | Disables a hook so it stops receiving and queueing requests. |
| Enable Hook | `enableHook` | Enables a previously disabled hook so it can receive requests again. |
| Get Connection | `getConnection` | Retrieves details of a specific connection, given its ID. |
| Get Connection Access List | `getConnectionAccessList` | Returns the access control list for a connection, showing which principals have been granted a role on it. Requires the locked connections feature to be enabled for the organization. |
| Get Connection Editable Data Schema | `getConnectionEditableSchema` | Gets the list of connection parameters that can be updated with Update Connection Data. |
| Get Current User | `getCurrentUser` | Retrieves profile data about the currently authenticated Make user, including id, name, email, language, timezone, enabled features, and team memberships. |
| Get Current User Authorization | `getCurrentUserAuthorization` | Returns current authorization information for the authenticated user, including granted scopes and the authentication method used. |
| Get Data Store | `getDataStore` | Retrieves details of a data store, given its ID. |
| Get Data Structure | `getDataStructure` | Retrieves a data structure, given its ID. |
| Get Hook | `getHook` | Retrieves details of a specific hook, given its ID. |
| Get Hook Incoming | `getHookIncoming` | Retrieves detail of a single queued incoming webhook request. |
| Get Hook Incomings Stats | `getHookIncomingsStats` | Gets processing queue statistics for a hook, including item count and queue limits. |
| Get Hook Log | `getHookLog` | Retrieves a single hook execution log, with request headers and payload detail. |
| Get Key | `getKey` | Gets details of a specific key in a team's keychain. |
| Get Key Access List | `getKeyAccessList` | Returns the access control list for a key, showing which principals have been granted a role on it. Requires the locked connections feature to be enabled for the organization. |
| Get Notification | `getNotification` | Retrieves details and full content of a specific notification. |
| Get Onboarding Survey Status | `getOnboardingSurveyStatus` | Returns whether the authenticated user has a pending onboarding survey to complete. |
| Get Organization | `getOrganization` | Retrieves detailed information about a specific organization, given its ID. |
| Get Organization Feature Controls | `getOrganizationFeatureControls` | Retrieves the feature control (feature flag) settings configured for an organization. |
| Get Organization Invitation | `getOrganizationInvitation` | Retrieves details of a pending organization invitation from its invitation hash. |
| Get Organization Subscription | `getOrganizationSubscription` | Retrieves details of an organization's active subscription plan. |
| Get Organization Universal Discount | `getOrganizationUniversalDiscount` | Returns the organization's current universal discount, whether active or dormant. |
| Get Organization Usage | `getOrganizationUsage` | Retrieves the last 30 days of centicredit, operations, and data transfer usage for an organization. |
| Get Organization Variable History | `getOrganizationVariableHistory` | Retrieves the update history of a custom organization variable. |
| Get Scenario | `getScenario` | Retrieves the full details of a scenario, given its ID. |
| Get Scenario Blueprint | `getScenarioBlueprint` | Retrieves the blueprint (the full automation flow definition) of a scenario, optionally a specific version or the unsaved draft. |
| Get Scenario Execution | `getScenarioExecution` | Retrieves comprehensive details of a specific scenario execution, including status, timing, and per-module outputs. |
| Get Scenario Execution Log | `getScenarioExecutionLog` | Retrieves a single execution log entry for a scenario, given the scenario and execution IDs. |
| Get Scenario Interface | `getScenarioInterface` | Retrieves the declared input and output interface specification of a scenario, used when the scenario is invoked as a callable sub-flow or app. |
| Get Scenario Triggers | `getScenarioTriggers` | Retrieves the trigger properties (start module configuration) of a scenario, given its ID. |
| Get Scenario Usage | `getScenarioUsage` | Retrieves the last 30 days of operations, data transfer, and consumption usage metrics for a scenario. |
| Get SDK App | `getSdkApp` | Retrieves details of a specific custom (SDK) app version. |
| Get SDK App Common Data | `getSdkAppCommon` | Gets the app's client ID, client secret, and other shared configuration data. |
| Get SDK App Events Log | `getSdkAppEventsLog` | Retrieves the events log for a custom app, tracking changes and lifecycle events. |
| Get SDK App Function | `getSdkAppFunction` | Retrieves details of a specific custom IML function. |
| Get SDK App Function Code | `getSdkAppFunctionCode` | Retrieves the IML source code of a custom function. |
| Get SDK App Readme | `getSdkAppReadme` | Retrieves the markdown documentation (README) for a custom app. |
| Get SDK App Review | `getSdkAppReview` | Retrieves the current review status of a custom app submitted for the Make app directory. |
| Get Team | `getTeam` | Returns information about a specific team, given its ID. |
| Get Team Feature Controls | `getTeamFeatureControls` | Retrieves the feature control settings for the organization that owns the given team. |
| Get Team LLM Configuration | `getTeamLlmConfiguration` | Retrieves a team's AI/LLM configuration, including AI mapping and toolkit account settings. |
| Get Team Usage | `getTeamUsage` | Retrieves the last 30 days of operations, transfer, and centicredit usage for a team. |
| Get Team Variable History | `getTeamVariableHistory` | Retrieves the update history of a custom team variable. |
| Get Template | `getTemplate` | Retrieves details of a template, given its ID. |
| Get Template Blueprint | `getTemplateBlueprint` | Retrieves the automation flow blueprint of a template. |
| Get User By Permission | `getUserByPermission` | Retrieves users holding a specific permission on a team or organization. |
| Get User Organization Invitations | `getUserOrganizationInvitations` | Retrieves pending organization invitations for the currently authenticated user. |
| Invite Organization User | `inviteOrganizationUser` | Invites a new or existing user to join the organization by email, assigning an organization role and optional team memberships. Sends a real invitation email to the recipient. |
| List API Tokens | `listApiTokens` | Gets the API tokens of the currently authenticated user. |
| List Connections | `listConnections` | Retrieves a collection of all connections for a team, sorted by name. |
| List Data Store Records | `listDataStoreRecords` | Retrieves a collection of all records stored in a data store. |
| List Data Stores | `listDataStores` | Retrieves a collection of all data stores for a team. |
| List Data Structures | `listDataStructures` | Retrieves a collection of all data structures (record schemas) for a team. |
| List Hook Incomings | `listHookIncomings` | Retrieves the queue of incoming webhook requests waiting to be processed for a hook. |
| List Hook Logs | `listHookLogs` | Retrieves a list of execution logs for a hook, optionally filtered by time range. |
| List Hooks | `listHooks` | Retrieves a collection of all hooks (custom webhooks and mailhooks) for a team. |
| List Key Types | `listKeyTypes` | Retrieves the available key types that can be stored in a team's keychain. |
| List Keys | `listKeys` | Gets the list of keys in a team's custom keychain. |
| List Notifications | `listNotifications` | Retrieves a collection of all notifications for the authenticated user, sorted by ID descending. |
| List Organization Apps | `listOrganizationApps` | Lists the third-party apps that users in the organization have connected. |
| List Organization Payment Method Types | `getOrganizationPaymentMethodTypes` | Returns the payment method types available for an organization's subscription (e.g. card, bank transfer). |
| List Organization Payment Methods | `listOrganizationPaymentMethods` | Returns the payment methods on file for an organization's subscription. |
| List Organization Variables | `listOrganizationVariables` | Lists the custom and system-defined variables configured at the organization level. |
| List Organizations | `listOrganizations` | Retrieves a collection of all organizations in which the authenticated user has membership. |
| List Scenario Blueprint Versions | `listScenarioBlueprintVersions` | Retrieves a collection of blueprint versions for a scenario saved in the last 60 days. |
| List Scenario Build Variables | `listScenarioBuildVariables` | Retrieves the buildtime variables (name/value pairs used at scenario save time) configured on a scenario. |
| List Scenario Consumptions | `listScenarioConsumptions` | Retrieves a list of scenarios and their current centicredit, operations, and data transfer consumption for the active reset period. |
| List Scenario Folders | `listScenarioFolders` | Retrieves the direct scenario folder children for a team or organization, optionally including nested descendants. |
| List Scenario Labels | `listScenarioLabels` | Retrieves the colour-coded labels owned by a team, sorted by name. |
| List Scenario Logs | `listScenarioLogs` | Retrieves a collection of execution logs for a scenario, with optional filters by time range, status, duration, operations, transfer, and credits. |
| List Scenario Module Logs | `listScenarioModuleLogs` | Retrieves the operation logs of a specific module within a scenario. |
| List Scenarios | `listScenarios` | Retrieves a collection of all scenarios for a given team or organization, with optional filtering by folder, label, name, and active status. |
| List SDK App Functions | `listSdkAppFunctions` | Lists the custom IML functions defined in a custom app. |
| List SDK Apps | `listSdkApps` | Retrieves a collection of all custom (SDK) apps available to the authenticated user. |
| List Team Variables | `listTeamVariables` | Retrieves the custom and system variables configured at the team level. |
| List Teams | `listTeams` | Retrieves the list of teams in an organization. |
| List Templates | `listTemplates` | Retrieves a collection of all scenario templates for a team. |
| List Users | `listUsers` | Retrieves a collection of all users for a team or organization. |
| Mark All Notifications Read | `markAllNotificationsRead` | Marks all of the authenticated user's notifications as read. |
| Move Scenarios To Folder | `moveScenariosToFolder` | Moves the given scenarios into a target folder, or uncategorizes them by passing a null target folder. |
| Ping Hook | `pingHook` | Checks whether a hook is active and returns its status, including address, attachment state, and learning mode. |
| Publish Template | `publishTemplate` | Publishes a private template, making it visible to the team. |
| Rename Connection | `renameConnection` | Updates the display name of a connection. |
| Reorder Scenario Folders | `reorderScenarioFolders` | Sets the manual display order of sibling scenario folders within one parent folder. |
| Replace Data Store Record | `replaceDataStoreRecord` | Replaces a data store record entirely with new values, given its key. |
| Replay Scenario Execution | `replayScenarioExecution` | Reruns one or more previous scenario executions using their original trigger data. |
| Request SDK App Review | `requestSdkAppReview` | Submits a custom app for Make's review process ahead of public listing. |
| Request Template Approval | `requestTemplateApproval` | Requests approval to make a published template publicly available in the Make template gallery. |
| Restore Scenario | `restoreScenario` | Restores a trashed scenario back to active status before its retention window expires. |
| Run Scenario | `runScenario` | Executes a scenario immediately (on-demand run), optionally passing input data to its interface and requesting a synchronous response. |
| Set Hook Data | `setHookData` | Configures hook-specific settings, such as whether to capture the HTTP method, headers, or a stringified body. |
| Set SDK App Base Configuration | `setSdkAppBase` | Sets the base HTTP configuration (base URL, default headers, request/response templates) shared by every module in a custom app. |
| Set SDK App Common Data | `setSdkAppCommon` | Sets the app's shared configuration data, such as OAuth client credentials, available to every module in the app. |
| Set SDK App Function Code | `setSdkAppFunctionCode` | Sets the IML source code of a custom function. |
| Set SDK App Readme | `setSdkAppReadme` | Sets the markdown documentation (README) for a custom app. Sends Content-Type: text/markdown, which this endpoint requires - application/json is rejected with HTTP 400 'Invalid content-type'. |
| Start Hook Learning | `startHookLearning` | Puts a hook into learning mode so its next incoming request is used to infer the payload data structure. |
| Start Scenario | `startScenario` | Activates a scenario so it starts running on its configured schedule or trigger. |
| Stop Hook Learning | `stopHookLearning` | Stops the payload-structure learning process on a hook. |
| Stop Scenario | `stopScenario` | Deactivates a scenario, stopping it from running on its configured schedule or trigger. |
| Stop Scenario Execution | `stopScenarioExecution` | Stops a currently running scenario execution, optionally forcing immediate termination. |
| Test Connection | `testConnection` | Verifies whether a connection's stored credentials are still valid by communicating with the connected app's API. |
| Update Connection Data | `updateConnectionData` | Replaces a connection's stored credential data with new values, per the connection's editable data schema. |
| Update Data Store | `updateDataStore` | Updates a data store's name, data structure, or maximum size. |
| Update Data Store Record | `updateDataStoreRecord` | Partially updates a data store record, given its key. Fields not provided remain unchanged. |
| Update Data Structure | `updateDataStructure` | Updates a data structure's name, strictness, or field spec. All structure fields to keep must be resent. |
| Update Hook | `updateHook` | Renames a hook. |
| Update Key | `updateKey` | Updates a key's name or its stored connection parameters. |
| Update Organization | `updateOrganization` | Updates an organization's name, timezone, or country. |
| Update Organization Variable | `updateOrganizationVariable` | Updates the value or type of an existing organization-level custom variable. |
| Update Scenario | `updateScenario` | Updates a scenario's blueprint, scheduling, name, folder, or description by passing new values in the request body. |
| Update Scenario Folder | `updateScenarioFolder` | Renames a scenario folder or moves it under a different parent folder. |
| Update Scenario Interface | `updateScenarioInterface` | Updates the declared input and output interface specification of a scenario used when the scenario is invoked as a callable sub-flow or app. |
| Update SDK App | `updateSdkApp` | Updates a custom (SDK) app's label, description, theme, or other top-level properties. |
| Update Team | `updateTeam` | Updates a team's name or operations limit. |
| Update Team LLM Configuration | `updateTeamLlmConfiguration` | Updates a team's AI/LLM configuration settings, such as the default model or toolkit account mapping. |
| Update Team Variable | `updateTeamVariable` | Updates the value or type of an existing team-level custom variable. |
| Update Template | `updateTemplate` | Updates a template's name, blueprint, or scheduling. |
| Update User | `updateUser` | Updates a user's profile information such as display name, language, timezone, locale, or country. |
| Verify Connection Scope | `verifyConnectionScope` | Checks whether a connection has been granted a given scope. |

</details>
