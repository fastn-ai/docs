---
description: "PhantomBuster is a cloud automation platform for lead generation and data extraction (Phantoms)."
hidden: true
---

# PhantomBuster

<img src="../../.gitbook/assets/connectors/lg/phantombuster.png" alt="PhantomBuster logo">

PhantomBuster is a cloud automation platform for lead generation and data extraction (Phantoms). This connector covers the PhantomBuster API v2 and the legacy v1 endpoints: agents (create, launch, schedule, stop, output, delete), containers and their output and result objects, scripts and branches, organization settings, resources, usage exports and agent groups, the current user, org storage for leads, lead lists, lead objects and company objects, identities, CRM access and contacts, AI completions and advice, ICPs, buyer personas, scoring definitions, SERP search, IP location and captcha solving.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [phantombuster.com](https://phantombuster.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `phantombuster` |

## Use it

Add PhantomBuster from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.phantombuster.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Abort Agent (v1) | `abortAgentV1` | Aborts all running instances of an agent through the legacy v1 API, optionally as a soft abort. |
| Attach To Container | `attachToContainer` | Attaches to a running container and streams its output in real time as NDJSON (start, heartbeat, log, summary and error messages). The response is the stream text once the connection closes. |
| Create Branch | `createBranch` | Creates a new script branch in the current organization. |
| Delete Agent | `deleteAgent` | Deletes an agent by ID. |
| Delete Branch | `deleteBranch` | Deletes a script branch by ID. |
| Delete Lead List | `deleteLeadList` | Deletes a lead list by ID. |
| Delete Lead Objects | `deleteLeadObjects` | Deletes one or more lead objects, selected by type and slug or by lead object ID. |
| Delete Leads | `deleteLeads` | Deletes leads from the organization's storage by their IDs. |
| Delete Script | `deleteScript` | Deletes a script by ID, optionally scoped to a branch and environment. |
| Export Agent Usage | `exportAgentUsage` | Exports a CSV file of agent usage for the current organization over the given number of days (up to six months). |

<details>

<summary>See 68 more actions</summary>

* **Export Container Usage** `exportContainerUsage`: Exports a CSV file of container usage for the current organization over the given number of days (up to six months), optionally limited to one agent.
* **Generate Identity Token** `generateIdentityToken`: Generates an identity token that lets an identity be saved with Save Identity With Token. Requires a validated email address on the account.
* **Get Agent** `getAgent`: Gets an agent (Phantom) by its ID, optionally including its manifest, agent object, script code, slave agents and sub-slave agents.
* **Get Agent (v1)** `getAgentV1`: Gets an agent record through the legacy v1 API, optionally including its script record.
* **Get Agent Groups** `getAgentGroups`: Gets the agent groups of the current organization and their order, as shown on the dashboard. The API returns a bare array, exposed here as items.
* **Get Agent Output** `getAgentOutput`: Gets the console output, status, progress and runtime events of the most recent container of an agent. Designed for incremental polling: pass the previous output position, container ID, status and runtime event index to receive only new data.
* **Get Agent Output (v1)** `getAgentOutputV1`: Gets an agent's console output, status, progress and messages through the legacy v1 API, either for a tracked container or for the most recent run, with incremental output positions.
* **Get AI Advice** `getAiAdvice`: Gets a recommendation from PhantomBuster's AI assistant for a conversation of assistant and user messages, with optional model and temperature. Consumes the organization's AI credits.
* **Get AI Completion** `getAiCompletion`: Generates a chat completion from PhantomBuster's AI for a list of system, assistant and user messages, with optional model, temperature and a JSON schema for structured output. Consumes the organization's AI credits.
* **Get Branch Diff** `getBranchDiff`: Gets, for every script on a branch, the length difference between its staging and release versions together with their visibility and access lists. The API returns a bare array, exposed here as items.
* **Get Container** `getContainer`: Gets a container (agent run) by ID with its status, launch and end details, optionally including its result object, console output, runtime events and the IDs of the newer and older containers.
* **Get Container Output** `getContainerOutput`: Gets the console output of a container, as JSON (default) or as plain text.
* **Get Container Result Object** `getContainerResultObject`: Gets the result object that an agent's script saved for a container with buster.setResultObject.
* **Get CRM Access** `getCrmAccess`: Gets the organization's connected CRM access (CRM name, account ID and access token) used to fetch CRM resources. Returns an error when no CRM integration is connected.
* **Get CRM Resources** `getCrmResources`: Gets resources from the organization's connected CRM: account info, contact lists or contact properties. Returns an error when no CRM integration is connected.
* **Get Current User** `getCurrentUser`: Gets the current user's profile and organization details. When called with an API key a new session is created and its ID is returned; pass detailedOrgId to include the detailed organization record.
* **Get IP Location** `getIpLocation`: Retrieves the country of an IP address.
* **Get Lead List** `getLeadList`: Gets a lead list by ID with its filter, tags and configuration.
* **Get Organization** `getOrganization`: Gets the current organization with its plan, resource limits, billing details and time zone, optionally including its global object, proxies, CRM integrations and custom prompts.
* **Get Organization Resources** `getOrganizationResources`: Gets the current organization's resource usage (execution time, emails, captchas, AI and SERP credits, storage, agent count) together with its plan limits and the next reset times.
* **Get Scoring Definition** `getScoringDefinition`: Fetches a lead scoring definition by ID with its name, lead scorer agent and the scoring rules and signals it evaluates.
* **Get Script** `getScript`: Gets a script by ID with its description, visibility, access list, categories, branches and optionally its code, for a given branch and environment.
* **Get Script By Name (v1)** `getScriptByNameV1`: Gets a script record by its file name through the legacy v1 API, as JSON metadata with contents or as raw text.
* **Get Script Code** `getScriptCode`: Gets the source code of a script by name, optionally from another organization, branch or environment.
* **Get User (v1)** `getUserV1`: Gets the account email, remaining execution time, emails, captchas and storage, and the list of agents through the legacy v1 API.
* **Launch Agent** `launchAgent`: Adds an agent to the launch queue and returns the ID of the container created for the run. Supports a launch argument or single-use bonus argument, saving the argument as the default, marking the launch as manual, limiting concurrent instances, container metadata and a persisted volume key. Launching consumes the organization's execution time.
* **Launch Agent (v1)** `launchAgentV1`: Adds an agent to the launch queue through the legacy v1 API. The output mode selects the response: a JSON container ID, the result object, the result object with console output, an event stream or raw output. Launching consumes execution time.
* **Launch Agent Synchronously** `launchAgentSync`: Launches an agent and streams its execution status as NDJSON until it ends: a start message with the container ID, heartbeats, optional log lines, the execution summary and any errors. The response is the stream text. Launching consumes the organization's execution time.
* **List Agent Containers (v1)** `listAgentContainersV1`: Lists the ended containers of an agent through the legacy v1 API, ordered by date, with launch and end details and exit codes.
* **List Agents** `listAgents`: Lists all agents (Phantoms) of the current organization, optionally filtered by input types, output types or agent IDs, with optional agent slot factor and argument included. The API returns a bare array, exposed here as items.
* **List Branches** `listBranches`: Lists the script branches of the current organization. The API returns a bare array, exposed here as items.
* **List Buyer Personas** `listBuyerPersonas`: Lists the buyer personas defined for the organization with their ICP, lead list and sourcing and monitoring agents. The API returns a bare array, exposed here as items.
* **List Containers** `listContainers`: Lists the containers (runs) of an agent, newest first, with optional limit, end-date cutoff, finalized-only mode and runtime events.
* **List Deleted Agents** `listDeletedAgents`: Lists all deleted agents of the current organization with their deletion time and the user who deleted them. The API returns a bare array, exposed here as items.
* **List Ideal Customer Profiles** `listIdealCustomerProfiles`: Lists the ideal customer profiles (ICPs) defined for the organization. The API returns a bare array, exposed here as items.
* **List Lead Lists** `listLeadLists`: Lists all lead lists of the organization with their filters, tags and configuration. The API returns a bare array, exposed here as items.
* **List Leads By List** `listLeadsByList`: Fetches the leads that belong to a lead list, with pagination options, optional lead object types and the lead's company.
* **List Running Containers** `listRunningContainers`: Lists the containers currently running in the organization with their agent, launch type and script.
* **List Scripts** `listScripts`: Lists the scripts of the current organization, or of another organization such as phantombuster for the public Phantom store, optionally filtered by branch, module type or script IDs. The API returns a bare array, exposed here as items.
* **Release Branch** `releaseBranch`: Releases the staging version of the given scripts on a branch to the release environment.
* **Save Agent** `saveAgent`: Creates a new agent (Phantom) from a script, or updates an existing agent when an ID is provided: name, script, branch and environment, execution time limit, file management, parallelism and retries, launch type and schedule, notifications, proxy settings, default argument, agent object, expiry and metadata. Only the fields sent are changed.
* **Save Agent Groups** `saveAgentGroups`: Replaces the organization's agent groups and their order. Each entry is either an agent ID string or a group object with id, name and the ordered agent IDs it contains.
* **Save Company Object** `saveCompanyObject`: Saves a company object (a typed data record about a LinkedIn company) with its LinkedIn company ID, type, slug and properties.
* **Save Company Objects** `saveCompanyObjects`: Saves up to 20 company objects in one call. The request body is a JSON array of company objects, each with linkedinCompanyId, type, slug and properties. The API returns a bare array of per-object results, exposed here as items.
* **Save CRM Contact** `saveCrmContact`: Creates or updates a contact in the organization's connected CRM (HubSpot) from a LinkedIn profile URL, name and optional email, phone, job title and company. Requires a connected CRM integration.
* **Save Identity** `saveIdentity`: Saves a LinkedIn or Google identity (a connected social account profile) for the current user, with its profile ID, name, profile URL, picture, headline and subscription titles.
* **Save Identity Event** `saveIdentityEvent`: Records an event for an identity, such as an action performed by a connected LinkedIn account, with its type, data and optional timestamp.
* **Save Identity With Token** `saveIdentityWithToken`: Saves an identity on behalf of an organization using an identity token generated with Generate Identity Token, including the profile details and the active session credentials.
* **Save Lead** `saveLead`: Creates or updates a lead in the organization's storage, identified by its LinkedIn profile URL, with contact details, company, LinkedIn profile, job, education, CRM and AI properties.
* **Save Lead List** `saveLeadList`: Creates a dynamic lead list defined by a filter, or updates an existing list when an ID is provided, with name, description and tags.
* **Save Lead Object** `saveLeadObject`: Saves a lead object (a typed data record produced by an agent, such as a post or message) with its type, slug, properties and the agent that produced it, optionally linked to a lead by ID, slug or URN.
* **Save Lead Objects** `saveLeadObjects`: Saves lead objects in bulk with a shared type, slug, properties and agent, optionally linked to a lead. The API returns a bare array of results, exposed here as items.
* **Save Leads** `saveLeads`: Creates or updates many leads in the organization's storage in one call. Each lead uses the same fields as Save Lead and is identified by its LinkedIn profile URL. The API returns a bare array of per-lead results, exposed here as items.
* **Save Script** `saveScript`: Creates a new script or updates an existing one when an ID is provided, with its name, branch, JavaScript code, markdown description and manifest. Prefix the name with lib- to define a module.
* **Save Script (v1)** `saveScriptV1`: Updates an existing script or creates a new one by file name through the legacy v1 API, sending the script text as a form-encoded body. The new script ID is returned in data when a script is created.
* **Schedule Agent Launch** `scheduleAgentLaunch`: Schedules an agent to launch before the given number of minutes elapses, optionally with a launch argument that can be saved as the default.
* **Search Company Objects** `searchCompanyObjects`: Searches company objects in the organization's storage with a filter (global search, field filters, or and/or combinations) and pagination options.
* **Search Identities** `searchIdentities`: Searches the identities (connected LinkedIn or Google accounts) of the organization by ID, session cookie, profile ID or type. The API returns a bare array, exposed here as items.
* **Search Lead Objects** `searchLeadObjects`: Searches lead objects in the organization's storage with a filter (global search, field filters, or and/or combinations) and pagination options, returning the matching objects and their linked leads.
* **Search SERP** `searchSerp`: Performs a web search through PhantomBuster's Bright Data SERP integration and returns the search engine results. Consumes the organization's SERP credits.
* **Solve hCaptcha** `solveHcaptcha`: Solves an hCaptcha challenge for a page URL and site key and returns the response token. The API answers 200 even when solving fails and puts the error in the body. Consumes the organization's captcha credits.
* **Solve reCAPTCHA** `solveRecaptcha`: Solves a reCAPTCHA v2 or v3 challenge for a page URL and site key and returns the response token; v3 also takes a minimum score and page action, and both support reCAPTCHA Enterprise. The API answers 200 even when solving fails and puts the error in the body. Consumes captcha credits.
* **Stop Agent** `stopAgent`: Stops the running containers of an agent, with options for a soft abort, cascading to slave agents, cancelling a pending scheduled launch and switching the agent to manual launch.
* **Unschedule All Agents** `unscheduleAllAgents`: Disables automatic launches for every agent in the current organization.
* **Update Current User** `updateCurrentUser`: Updates the current user's profile: name, phone, company, job, newsletter and pixel tracking consent, enabled experiments, developer mode, onboarding answers and custom prompt. Only the fields sent are changed.
* **Update Organization** `updateOrganization`: Updates the current organization's name, display name, time zone, company and billing details, global object, proxies, invoice information, CRM integration options and custom prompt. PhantomBuster only allows web or MCP sessions to call this endpoint; API-key calls are rejected.
* **Update Script Access List** `updateScriptAccessList`: Adds an organization or user to, or removes one from, the access list of a script branch.
* **Update Script Visibility** `updateScriptVisibility`: Updates the visibility of a script branch: private, semi public, public, semi open source or open source.

</details>
