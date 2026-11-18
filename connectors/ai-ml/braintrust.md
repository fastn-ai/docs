---
description: "Braintrust is an AI evaluation and observability platform for building, evaluating and monitoring LLM applications."
hidden: true
---

# Braintrust

<img src="../../.gitbook/assets/connectors/braintrust.png" alt="Braintrust logo" width="64">

Braintrust is an AI evaluation and observability platform for building, evaluating and monitoring LLM applications. This connector covers the Braintrust REST API v1: projects, experiments, datasets and dataset snapshots, project logs, prompts, functions and agents, views, span iframes, project scores and tags, groups, roles, ACLs, users, organizations, API keys, service tokens, AI secrets, environment variables, MCP servers, project and organization automations, environments, evals and the AI proxy.

| | |
| --- | --- |
| **Category** | [AI and ML](README.md) |
| **Website** | [braintrust.dev](https://braintrust.dev) |
| **Authentication** | Bearer token |
| **Slug** | `braintrust` |

## Use it

Add Braintrust from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.braintrust.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Update ACLs | `aclBatchUpdate` | Adds and removes ACLs in one idempotent batch: adding ACLs that already exist and removing ACLs that do not exist have no effect. |
| Create ACL | `postAcl` | Creates an ACL granting a permission or a role to a user or group on an object. Supply exactly one of user_id or group_id and exactly one of permission or role_id. If an identical ACL already exists it is returned unmodified. |
| Create Agent | `postAgent` | Creates a new agent, a project-scoped durable object identifying an AI agent or service that emits traces. If an agent with the same name already exists in the project, Braintrust returns it unmodified. |
| Create AI Secret | `postAiSecret` | Create a new AI provider secret (e.g. an OpenAI key stored in Braintrust). If an ai_secret with the same name already exists it is returned unmodified. Returns the ai_secret object (secret value is never returned, only preview_secret). |
| Create Dataset | `postDataset` | Creates a new dataset in a project. If a dataset with the same name already exists in the project, Braintrust returns it unmodified. |
| Create Dataset Snapshot | `postDatasetSnapshot` | Create a named version snapshot of a dataset at a given transaction id (xact_id, as returned by dataset fetch rows). If a snapshot with the same name exists it is returned unmodified. Requires a paid plan: free orgs get 403 "Version snapshots are not available on your current plan". |
| Create Environment | `createEnvironment` | Create a new deployment environment (e.g. staging, production) in the organization. Requires Pro or Enterprise plan: free orgs get 403 "Upgrade to Pro or Enterprise to create environments". Note this endpoint lives at /environment (not under /v1). |
| Create Environment Variable | `postEnvVar` | Create a new env_var scoped to an organization, project or function. If an env_var with the same name already exists on that object it is returned unmodified. Returns the env_var object (value is never returned, only preview_secret). |
| Create Experiment | `postExperiment` | Creates a new experiment in a project. If an experiment with the same name already exists in the project, Braintrust returns it unmodified unless ensure_new is true. |
| Create Function | `postFunction` | Creates a function (prompt, code, global, graph or remote-eval backed scorer, task, tool or other function type) in a project. If a function with the same slug already exists, a new version is appended and returned. |

<details>

<summary>See 151 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Group | `postGroup` | Creates a new user group. If a group with the same name already exists, Braintrust returns it unmodified. |
| Create MCP Server | `postMcpServer` | Register a new MCP server in a project. If an mcp_server with the same name already exists in the project it is returned unmodified. Returns the mcp_server object. |
| Create Or Replace Agent | `putAgent` | Creates an agent, or replaces the existing agent with the same name in the project using the provided fields. |
| Create Or Replace AI Secret | `putAiSecret` | Create or replace an AI secret by name. If an ai_secret with the same name exists it is replaced with the provided fields (secret value is kept intact when omitted). Returns the ai_secret object. |
| Create Or Replace Dataset Snapshot | `putDatasetSnapshot` | Create or replace a dataset version snapshot by name. Requires a paid plan: free orgs get 403 "Version snapshots are not available on your current plan". |
| Create Or Replace Environment Variable | `putEnvVar` | Create or replace an env_var on an organization, project or function. If an env_var with the same name exists on that object it is replaced with the provided fields. Returns the env_var object. |
| Create Or Replace Function | `putFunction` | Creates a function, or appends a new version when a function with the same slug already exists in the project. Returns the resulting function version. |
| Create Or Replace Group | `putGroup` | Creates a group, or replaces the existing group with the same name using the provided fields. |
| Create Or Replace MCP Server | `putMcpServer` | Create or replace an MCP server in a project by name. If an mcp_server with the same name exists it is replaced with the provided fields. Returns the mcp_server object. |
| Create Or Replace Org Automation | `putOrgAutomation` | Creates an organization automation, or replaces the existing automation with the same name using the provided fields. |
| Create Or Replace Project Automation | `putProjectAutomation` | Creates a project automation, or replaces the existing automation with the same name in the project using the provided fields. |
| Create Or Replace Project Group | `putProjectGroup` | Creates a project group, or replaces the existing project group with the same name using the provided fields. |
| Create Or Replace Project Score | `putProjectScore` | Creates a project score definition, or replaces the existing score with the same name in the project using the provided fields. |
| Create Or Replace Project Tag | `putProjectTag` | Creates a project tag, or replaces the existing tag with the same name in the project using the provided fields. |
| Create Or Replace Prompt | `putPrompt` | Creates a prompt, or appends a new version when a prompt with the same slug already exists in the project. Returns the resulting prompt version. |
| Create Or Replace Role | `putRole` | Creates a role, or replaces the existing role with the same name using the provided fields. |
| Create Or Replace Service Token | `putServiceToken` | Creates a service token, or replaces the existing token with the same name. Requires a service token with organization-owner permissions; the raw token is returned once in the key field. |
| Create Or Replace Span IFrame | `putSpanIframe` | Creates a span iframe, or replaces the existing iframe with the same name in the project using the provided fields. |
| Create Or Replace View | `putView` | Creates a saved view, or replaces the existing view with the same name on the object using the provided fields. |
| Create Org Automation | `postOrgAutomation` | Creates an organization-level automation, currently a data retention policy for project logs, experiments or datasets. If an automation with the same name already exists, Braintrust returns it unmodified. |
| Create Project | `postProject` | Creates a new project. If a project with the same name already exists, Braintrust returns the existing project unmodified. |
| Create Project Automation | `postProjectAutomation` | Creates a project automation rule. Supported event types: logs (trigger a webhook or Slack action when rows match a BTQL filter), btql_export, async_query, retention (Enterprise plan), environment_update, windowed, topic and topic_digest. If an automation with the same name already exists in the project, Braintrust returns it unmodified. |
| Create Project Group | `postProjectGroup` | Creates a new project group, a collection of projects that can inherit access from project-group ACLs. If a project group with the same name already exists, Braintrust returns it unmodified. |
| Create Project Score | `postProjectScore` | Creates a human-review score definition in a project (slider, categorical, weighted, minimum, maximum, online or free-form). If a score with the same name already exists in the project, Braintrust returns it unmodified. |
| Create Project Tag | `postProjectTag` | Creates a tag definition in a project with an optional description and UI color. If a tag with the same name already exists in the project, Braintrust returns it unmodified. |
| Create Prompt | `postPrompt` | Creates a new prompt in a project. If a prompt with the same slug already exists in the project, a new version of that prompt is appended and returned. |
| Create Role | `postRole` | Creates a new role, a collection of permissions that can be granted through ACLs. If a role with the same name already exists, Braintrust returns it unmodified. |
| Create Service Token | `postServiceToken` | Creates a service token for a service account. The raw token is returned once in the key field. This endpoint must be called with a service token that has organization-owner permissions; user API keys are rejected. |
| Create Span IFrame | `postSpanIframe` | Creates a span iframe: a custom URL embedded in the trace viewer for a project, optionally receiving span data via postMessage. If an iframe with the same name already exists, Braintrust returns it unmodified. |
| Create View | `postView` | Creates a saved view (filters, columns and chart options) on a Braintrust object such as a project's logs or experiments. If a view with the same name already exists on the object, Braintrust returns it unmodified. |
| Cross-Object Insert | `postCrossObjectInsert` | Insert log events and feedback into multiple experiments, datasets and project logs in one call. Each of experiment / dataset / project_logs is a map from object id to {events: [...], feedback: [...]}. Returns the inserted row ids per object. |
| Delete ACL | `deleteAclId` | Deletes an ACL by its id and returns the deleted ACL object. |
| Delete Agent | `deleteAgentId` | Deletes an agent by its id and returns the deleted agent object. |
| Delete AI Secret | `deleteAiSecretId` | Delete an AI secret by its id. Returns the deleted ai_secret object. |
| Delete AI Secret By Name | `deleteAiSecret` | Delete a single AI secret by its name (sent in the JSON body). Returns the deleted ai_secret object. |
| Delete API Key | `deleteApiKeyId` | Permanently revokes an API key by its id and returns the deleted key's metadata. |
| Delete Dataset | `deleteDatasetId` | Deletes a dataset by its id and returns the deleted dataset object. |
| Delete Dataset Snapshot | `deleteDatasetSnapshotId` | Delete a dataset_snapshot by its id. Returns the deleted snapshot object. |
| Delete Environment | `deleteEnvironment` | Delete a deployment environment by its id. Endpoint lives at /environment/{id} (not under /v1). |
| Delete Environment Variable | `deleteEnvVarId` | Delete an env_var by its id. Returns the deleted env_var object. |
| Delete Experiment | `deleteExperimentId` | Deletes an experiment by its id and returns the deleted experiment object. |
| Delete Function | `deleteFunctionId` | Deletes a function by its id and returns the deleted function object. |
| Delete Group | `deleteGroupId` | Deletes a user group by its id and returns the deleted group object. |
| Delete MCP Server | `deleteMcpServerId` | Delete an mcp_server by its id. Returns the deleted mcp_server object. |
| Delete Org Automation | `deleteOrgAutomationId` | Deletes an organization automation by its id and returns the deleted automation object. |
| Delete Project | `deleteProjectId` | Deletes a project by its id and returns the deleted project object. |
| Delete Project Automation | `deleteProjectAutomationId` | Deletes a project automation by its id and returns the deleted automation object. |
| Delete Project Group | `deleteProjectGroupId` | Deletes a project group by its id and returns the deleted project group object. |
| Delete Project Score | `deleteProjectScoreId` | Deletes a project score definition by its id and returns the deleted object. |
| Delete Project Tag | `deleteProjectTagId` | Deletes a project tag definition by its id and returns the deleted object. |
| Delete Prompt | `deletePromptId` | Deletes a prompt by its id and returns the deleted prompt object. |
| Delete Role | `deleteRoleId` | Deletes a role by its id and returns the deleted role object. |
| Delete Service Token | `deleteServiceTokenId` | Permanently revokes a service token by its id and returns the deleted token's metadata. |
| Delete Single ACL | `deleteAcl` | Deletes a single ACL identified by its contents (object, user or group, and permission or role) rather than by id. |
| Delete Span IFrame | `deleteSpanIframeId` | Deletes a span iframe by its id and returns the deleted object. |
| Delete View | `deleteViewId` | Deletes a saved view by its id. The owning object's type and id are required in the body. Returns the deleted view object. |
| Fetch Dataset Events | `postDatasetIdFetch` | Fetches the records in a dataset with the query parameters in the request body (POST form). Results are paginated from latest to earliest; pass the returned cursor to fetch the next page. |
| Fetch Dataset Events (GET Form) | `getDatasetIdFetch` | Fetches the records in a dataset with the query parameters in the URL (GET form). |
| Fetch Experiment Events | `postExperimentIdFetch` | Fetches the events in an experiment with the query parameters in the request body (POST form). Results are paginated from latest to earliest; pass the returned cursor to fetch the next page. |
| Fetch Experiment Events (GET Form) | `getExperimentIdFetch` | Fetches the events in an experiment with the query parameters in the URL (GET form). |
| Fetch Project Logs | `postProjectLogsIdFetch` | Fetches the events in a project's logs with the query parameters in the request body (POST form). Results are paginated from latest to earliest; pass the returned cursor to fetch the next page. |
| Fetch Project Logs (GET Form) | `getProjectLogsIdFetch` | Fetches the events in a project's logs with the query parameters in the URL (GET form). Equivalent to the POST form without cursor support. |
| Get ACL | `getAclId` | Retrieves an ACL by its id. |
| Get Agent | `getAgentId` | Retrieves an agent by its id. |
| Get AI Secret | `getAiSecretId` | Get an AI secret object by its id. The secret value is never returned (only preview_secret). |
| Get API Key | `getApiKeyId` | Retrieves an API key's metadata (name, owner, expiry) by its id. The secret is never returned. |
| Get Dataset | `getDatasetId` | Retrieves a dataset by its id. |
| Get Dataset Snapshot | `getDatasetSnapshotId` | Get a dataset_snapshot object by its id. |
| Get Environment | `getEnvironment` | Get a deployment environment by its id. Endpoint lives at /environment/{id} (not under /v1). |
| Get Environment Variable | `getEnvVarId` | Get an env_var object by its id. The value is never returned (only preview_secret). |
| Get Experiment | `getExperimentId` | Retrieves an experiment by its id. |
| Get Function | `getFunctionId` | Retrieves a function by its id. |
| Get Group | `getGroupId` | Retrieves a user group by its id. |
| Get MCP Server | `getMcpServerId` | Get an mcp_server object by its id. |
| Get Org Automation | `getOrgAutomationId` | Retrieves an organization automation by its id. |
| Get Organization | `getOrganizationId` | Retrieves an organization by its id. |
| Get Project | `getProjectId` | Retrieves a project by its id. |
| Get Project Automation | `getProjectAutomationId` | Retrieves a project automation by its id. |
| Get Project Group | `getProjectGroupId` | Retrieves a project group by its id. |
| Get Project Score | `getProjectScoreId` | Retrieves a project score definition by its id. |
| Get Project Tag | `getProjectTagId` | Retrieves a project tag definition by its id. |
| Get Prompt | `getPromptId` | Retrieves a prompt by its id. |
| Get Role | `getRoleId` | Retrieves a role by its id. |
| Get Service Token | `getServiceTokenId` | Retrieves a service token's metadata by its id. The secret is never returned. |
| Get Span IFrame | `getSpanIframeId` | Retrieves a span iframe by its id. |
| Get User | `getUserId` | Retrieves a user by its id. |
| Get View | `getViewId` | Retrieves a saved view by its id. The owning object's type and id must be supplied as well. |
| Hello World | `getIndex` | Default API root endpoint. Replies with the plain-text string "Hello, World!" (returned as a raw string, not JSON). Useful as a reachability check; authorization is not required by the vendor. |
| Insert Dataset Events | `postDatasetIdInsert` | Inserts a set of records into a dataset. Returns the ids of the inserted rows, aligned one-to-one with the supplied events. |
| Insert Experiment Events | `postExperimentIdInsert` | Inserts a set of evaluation events (rows) into an experiment. Returns the ids of the inserted rows, aligned one-to-one with the supplied events. |
| Insert Project Logs Events | `postProjectLogsIdInsert` | Inserts a set of log events (spans) into a project's logs. Returns the ids of the inserted rows, aligned one-to-one with the supplied events. |
| Invoke Function | `postFunctionIdInvoke` | Invokes a function (scorer, task, tool or prompt) with an input and returns its result. Prompt-backed functions call the configured LLM and need a configured AI provider secret; code functions run in Braintrust's sandbox. Set stream to false for a JSON result. |
| Launch Eval | `evalLaunch` | Launch an evaluation (API equivalent of the SDK Eval function): runs a task function over a dataset (by dataset_id or inline data rows) and scores the outputs with scorer functions, creating a new experiment in the project. Task and scores reference functions by function_id / slug / global_function. Returns experiment name, URL, aggregate scores and metrics. NOTE: the vendor omits the Content-Type header on this endpoint, so the response arrives as a JSON string; parse it with JSON.parse. May consume model credits if the task or scorers call LLMs. |
| List ACLs | `getAcl` | Lists the ACLs on a specific object, most recently created first, with cursor pagination and optional filters by user, group, permission or role. |
| List Agents | `getAgent` | Lists agents, most recently created first, with cursor pagination and filters by agent name, id or organization. |
| List AI Secrets | `getAiSecret` | List all AI secrets in the organization, most recently created first. Supports cursor pagination and filtering by name, type, id or organization. Secret values are never returned (only preview_secret). |
| List API Keys | `getApiKey` | Lists the organization's API keys (metadata only, never the secret), most recently created first, with cursor pagination and filters by key name or organization. New keys are created in the Braintrust UI under Settings &gt; API keys. |
| List Dataset Snapshots | `getDatasetSnapshot` | List all dataset version snapshots, most recently created first. Supports cursor pagination and filtering by name, id, dataset or organization. |
| List Datasets | `getDataset` | Lists datasets, most recently created first, with cursor pagination and filters by dataset name, project name, project id, id or organization. |
| List Environment Variables | `getEnvVar` | List env_vars scoped to one object (organization, project or function), most recently created first. The API requires both object_type and object_id; optional filters are env_var_name and ids. Values are never returned (only preview_secret). No limit or cursor pagination on this endpoint. |
| List Environments | `listEnvironments` | List all deployment environments in the organization, most recently created first. Filters: ids, name, org_name. Endpoint lives at /environment (not under /v1). |
| List Experiments | `getExperiment` | Lists experiments, most recently created first, with cursor pagination and filters by experiment name, project name, project id, id or organization. |
| List Functions | `getFunction` | Lists functions, most recently created first, with cursor pagination and filters by function name, slug, version, environment, project or organization. |
| List Groups | `getGroup` | Lists user groups, most recently created first, with cursor pagination and filters by group name, id or organization. |
| List MCP Servers | `getMcpServer` | List all MCP servers, most recently created first. Supports cursor pagination and filtering by name, id, project or organization. |
| List Org Automations | `getOrgAutomation` | Lists organization automations, most recently created first, with cursor pagination and filters by name or organization. |
| List Organization ACLs | `aclListOrg` | Lists all ACLs in the organization for a given object (requires read_acls permission at the organization level), with cursor pagination and optional filters by user, group, permission or role. |
| List Organizations | `getOrganization` | Lists the organizations the API key belongs to, most recently created first, with cursor pagination and optional filtering by id or name. |
| List Project Automations | `getProjectAutomation` | Lists project automations, most recently created first, with cursor pagination and filters by automation name, project or organization. |
| List Project Groups | `getProjectGroup` | Lists project groups, most recently created first, with cursor pagination and filters by name, id or organization. |
| List Project Scores | `getProjectScore` | Lists project score definitions, most recently created first, with cursor pagination and filters by score name, score type, project or organization. |
| List Project Tags | `getProjectTag` | Lists project tag definitions, most recently created first, with cursor pagination and filters by tag name, project or organization. |
| List Projects | `getProject` | Lists all projects, sorted by creation date with the most recently created first. Supports cursor pagination and filtering by name, id or organization. |
| List Prompts | `getPrompt` | Lists prompts, most recently created first, with cursor pagination and filters by prompt name, slug, version, environment, project or organization. |
| List Roles | `getRole` | Lists roles, most recently created first, including Braintrust system roles, with cursor pagination and filters by role name, id or organization. |
| List Service Tokens | `getServiceToken` | Lists the organization's service tokens (metadata only), most recently created first, with cursor pagination and filters by token name or organization. |
| List Span IFrames | `getSpanIframe` | Lists span iframes, most recently created first, with cursor pagination and filters by name, project or organization. |
| List Users | `getUser` | Lists users in the organization, most recently created first, with cursor pagination and filters by given name, family name, email or organization. |
| List Views | `getView` | Lists the saved views on an object, most recently created first, with cursor pagination and filters by view name or view type. |
| Log Feedback For Dataset Events | `postDatasetIdFeedback` | Logs feedback (comments, tags, metadata) for a set of existing dataset records, identified by their row ids. |
| Log Feedback For Experiment Events | `postExperimentIdFeedback` | Logs feedback (scores, expected values, comments, tags) for a set of existing experiment events, identified by their row ids. |
| Log Feedback For Project Logs Events | `postProjectLogsIdFeedback` | Logs feedback (scores, expected values, comments, tags) for a set of existing project log events, identified by their row ids. |
| Modify Organization Membership | `patchOrganizationMembers` | Invites users (by id or email) to the organization, optionally adding them to groups and sending invite emails, creates service accounts, or removes users from the organization. |
| Proxy Any OpenAI Request | `proxyOpenAiRequest` | Catch-all POST through the Braintrust AI proxy: any path not matched by chat/completions, completions, auto or embeddings (e.g. responses, moderations, images/generations) is forwarded to the OpenAI-compatible API with the given path. All fields other than path are sent as the JSON body. Requires an AI provider key configured in the org; otherwise the gateway returns 404 "No provider found". |
| Proxy Auto | `proxyAuto` | Send a request through the Braintrust AI proxy and let it route to chat/completions or completions automatically based on the model. Pass messages for chat models or prompt for completion models. Requires an AI provider key configured in the org; otherwise the gateway returns 404 "No provider found for '&lt;model&gt;'". Leave stream false. |
| Proxy Chat Completions | `proxyChatCompletions` | Send an OpenAI-compatible chat/completions request through the Braintrust AI proxy to any configured provider model, converting formats as needed. Responses are cached when temperature=0 or seed is set. Requires an AI provider key configured in the org (Settings &gt; AI Providers); otherwise the gateway returns 404 "No provider found for '&lt;model&gt;'". Leave stream false. |
| Proxy Completions | `proxyCompletions` | Send an OpenAI-compatible legacy completions (prompt) request through the Braintrust AI proxy. Cached when temperature=0 or seed is set. Requires an AI provider key configured in the org; otherwise the gateway returns 401 "no provider credentials available". Leave stream false. |
| Proxy Embeddings | `proxyEmbeddings` | Send an OpenAI-compatible embeddings request through the Braintrust AI proxy (cached automatically). Requires an AI provider key configured in the org; otherwise the gateway returns 401 "no provider credentials available". |
| Summarize Dataset | `getDatasetIdSummarize` | Summarizes a dataset: project and dataset names and URLs, and optionally a data summary with the total number of records. |
| Summarize Experiment | `getExperimentIdSummarize` | Summarizes an experiment: project and experiment names and URLs, and optionally its scores and metrics compared against a baseline experiment. |
| Update Agent | `patchAgentId` | Partially updates an agent's name, description or metadata. Object-type fields are deep-merged. |
| Update AI Secret | `patchAiSecretId` | Partially update an AI secret by id. Only the fields provided (name, type, metadata, secret) are changed; omitted fields keep their values. Returns the updated ai_secret object. |
| Update Dataset | `patchDatasetId` | Partially updates a dataset. Only the supplied fields change; object-type fields are deep-merged. Fields cannot be removed or set to null. |
| Update Dataset Snapshot | `patchDatasetSnapshotId` | Partially update a dataset_snapshot by id (name, description). Returns the updated snapshot object. |
| Update Environment | `updateEnvironment` | Partially update a deployment environment by id (name, slug, description). Endpoint lives at /environment/{id} (not under /v1). |
| Update Environment Variable | `patchEnvVarId` | Partially update an env_var by id. The API requires name in the payload; value, metadata and secret_type are optional. Object-type fields are deep-merged. Returns the updated env_var object. |
| Update Experiment | `patchExperimentId` | Partially updates an experiment. Only the supplied fields change; object-type fields are deep-merged. Fields cannot be removed or set to null. |
| Update Function | `patchFunctionId` | Partially updates a function's name, description, prompt data, function data or tags. Object-type fields are deep-merged. |
| Update Group | `patchGroupId` | Partially updates a group: rename it, change its description, and add or remove member users and inherited groups. |
| Update MCP Server | `patchMcpServerId` | Partially update an mcp_server by id (name, url, description). Omitted fields keep their values. Returns the updated mcp_server object. |
| Update Org Automation | `patchOrgAutomationId` | Partially updates an organization automation's name, description or retention config. Object-type fields are deep-merged. |
| Update Organization | `patchOrganizationId` | Partially updates an organization's name, data-plane URLs or image rendering mode. Only the supplied fields change. |
| Update Project | `patchProjectId` | Partially updates a project. Only the supplied fields change; object-type fields are deep-merged with existing content. Fields cannot be removed or set to null. |
| Update Project Automation | `patchProjectAutomationId` | Partially updates a project automation's name, description or config. When config is supplied it must include the full discriminated config (event_type plus that type's required fields); Braintrust deep-merges object-type fields. |
| Update Project Group | `patchProjectGroupId` | Partially updates a project group: rename it, change its description, and add or remove member projects. |
| Update Project Score | `patchProjectScoreId` | Partially updates a project score definition's name, description, type, categories or config. Object-type fields are deep-merged. |
| Update Project Tag | `patchProjectTagId` | Partially updates a project tag's name, description or color. |
| Update Prompt | `patchPromptId` | Partially updates a prompt. Only the supplied fields change; object-type fields such as prompt_data are deep-merged. Fields cannot be removed or set to null. |
| Update Role | `patchRoleId` | Partially updates a role: rename it, change its description, and add or remove member permissions and inherited roles. |
| Update Span IFrame | `patchSpanIframeId` | Partially updates a span iframe's name, URL, description or postMessage setting. |
| Update View | `patchViewId` | Partially updates a saved view's name, description, starred flag, view data or options. The owning object's type and id are required in the body. Object-type fields are deep-merged. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Environment updated | `environment_update` | Fires immediately when a prompt or dataset is assigned to / removed from a deployment environment (e.g. production). Registered via a project automation of event_type 'environment_update'; optional environmentFilter input limits it to given environment slugs. Payload shape per Braintrust docs (Webhook payloads &gt; Environment alerts). Note: creating environments requires a Pro/Enterprise plan. |
| Log alert triggered | `logs` | Fires when project log rows match the alert's BTQL filter (batched; at most once per intervalSeconds). Registered via a Braintrust project automation of event_type 'logs' with a webhook action. Payload shape per Braintrust docs (Webhook payloads &gt; Log alerts). |
| Time window alert state change | `windowed` | Fires when a scheduled BTQL calculation over a time window crosses (or recovers from) a threshold. Registered via a project automation of event_type 'windowed'. details.transition is one of scheduled, firing, recovery, renotify, evaluation_failed, evaluation_recovered. Payload shape per Braintrust docs (Webhook payloads &gt; Time window alerts). |
