---
description: "Kibana is the management and visualization layer for the Elastic Stack."
hidden: true
---

# Kibana

<img src="../../.gitbook/assets/connectors/kibana.png" alt="Kibana logo" width="64">

Kibana is the management and visualization layer for the Elastic Stack. This connector covers the Kibana REST API on Elastic Cloud: spaces, data views and their fields and runtime fields, saved objects, dashboards, alerting rules and rule types with enable/disable/mute/snooze, action connectors and connector types (including webhook connectors used to deliver alerts), maintenance windows, Fleet agent policies, package policies, agents, enrollment keys, outputs, proxies, server hosts and integration packages, Logstash pipelines, streams, security roles, task manager health, Kibana features and status. Authenticates with an Elasticsearch API key sent as 'Authorization: ApiKey &lt;key&gt;' plus the mandatory kbn-xsrf header.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [elastic.co](https://elastic.co) |
| **Authentication** | Credentials you enter |
| **Slug** | `kibana` |

## Use it

Add Kibana from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.kibana.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add a Case Comment or Alert | `addCaseCommentDefaultSpace` | Attach a user comment or an alert to a case. Set type to user with comment text, or to alert with alertId, index and rule. Requires all privileges for the Cases feature. |
| Add a Conversation Attachment | `postAgentBuilderConversationsConversationIdAttachments` | Attach content to an Agent Builder conversation so the agent can use it as context. The shape of data depends on type: a text attachment takes {"content": "..."}. Supply origin instead of data to attach a saved object by reference. |
| Archive a Maintenance Window | `archiveMaintenanceWindow` | Archive an alerting maintenance window so that it stops suppressing rule actions, without deleting it. |
| Authorize Package Transforms | `postFleetEpmPackagesPkgnamePkgversionTransformsAuthorize` | Reauthorize the Elasticsearch transforms installed by an integration package so they run with the caller's secondary authorization. |
| Bulk Change Agent Privilege Level | `postFleetAgentsBulkPrivilegeLevelChange` | Change the privilege level of multiple Elastic Agents to unprivileged. Required privileges: fleet-agents-all. |
| Bulk Create Workflows | `postWorkflows` | Create up to 500 workflows in one request. The response splits the outcome into created and failed lists, so partial success is reported rather than failing the whole batch. |
| Bulk Delete Package Policies | `postFleetPackagePoliciesDelete` | Delete several Fleet package policies by ID in one request. Required privileges: fleet-agent-policies-all and integrations-all. |
| Bulk Delete Workflows | `deleteWorkflows` | Delete up to 1000 workflows by id in one request. By default they are soft-deleted; set force to true to remove them permanently. |
| Bulk Get Agent Policies | `postFleetAgentPoliciesBulkGet` | Get several agent policies by id in one request. Requires the fleet-agent-policies-read, fleet-agents-read or fleet-setup privilege. |
| Bulk Get Package Assets | `postFleetEpmBulkAssets` | Retrieve several Kibana saved-object assets belonging to integration packages by ID and type. Required privileges: integrations-read, fleet-setup or fleet-all. |

<details>

<summary>See 381 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Get Package Policies | `postFleetPackagePoliciesBulkGet` | Get several Fleet package policies by ID in one request. |
| Bulk Install Packages | `postFleetEpmPackagesBulk` | Install several integration packages from the Elastic Package Registry in one request. Required privileges: integrations-all and fleet-agent-policies-all. |
| Bulk Reassign Agents | `postFleetAgentsBulkReassign` | Reassign multiple Elastic Agents to a different Fleet agent policy. Required privilege: fleet-agents-all. |
| Bulk Remove OpAMP Collectors | `postFleetAgentsBulkRemoveCollectors` | Remove multiple OpAMP collectors from the Fleet agents list and mark them unenrolled. API keys are not invalidated, so collectors can reconnect on their own. Required privileges: fleet-agents-all. |
| Bulk Request Diagnostics from Agents | `postFleetAgentsBulkRequestDiagnostics` | Request diagnostics bundles from multiple Elastic Agents in one call. Required privileges: fleet-agents-read. |
| Bulk Revoke or Delete Enrollment API Keys | `postFleetEnrollmentApiKeysBulkDelete` | Revoke or delete several enrollment API keys at once, selected by id list or by a KQL query. Requires the fleet-agents-all privilege. |
| Bulk Rollback Agents | `postFleetAgentsBulkRollback` | Roll multiple Elastic Agents back to their previous version. Required privileges: fleet-agents-all. |
| Bulk Rollback Packages | `postFleetEpmPackagesBulkRollback` | Roll several integration packages back to their previous versions. Returns a task ID to poll with Get Bulk Rollback Packages Details. Required privileges: integrations-all and fleet-agent-policies-all. |
| Bulk Set Package Namespace Customization | `postFleetEpmPackagesBulkNamespaceCustomization` | Enable or disable namespace-level index template customization for a list of integration packages in one call. Required privileges: integrations-all and fleet-agent-policies-all. |
| Bulk Unenroll Agents | `postFleetAgentsBulkUnenroll` | Unenroll multiple Elastic Agents from Fleet, optionally revoking their enrollment API keys. Required privileges: fleet-agents-all. |
| Bulk Uninstall Packages | `postFleetEpmPackagesBulkUninstall` | Uninstall several integration packages in one operation. Returns a task ID to poll with Get Bulk Uninstall Packages Details. Required privileges: integrations-all and fleet-agent-policies-all. |
| Bulk Update Agent Tags | `postFleetAgentsBulkUpdateAgentTags` | Add or remove tags across multiple Elastic Agents in one request. Required privileges: fleet-agents-all. |
| Bulk Update Entities | `putSecurityEntityStoreEntitiesBulk` | Update several Security Entity Store records in one request. Required privileges: securitySolution. |
| Bulk Update Stream Attachments | `bulkStreamAttachments` | Link and unlink several stream attachments in one request. Mixed attachment types are supported. Requires the manage_stream privilege. |
| Bulk Upgrade Agentless Policies (Deprecated) | `postFleetAgentlessPoliciesUpgrade` | Deprecated alias of Bulk Upgrade Managed Integrations. Use POST /api/fleet/managed_integrations/_upgrade instead. |
| Bulk Upgrade Agents | `postFleetAgentsBulkUpgrade` | Upgrade multiple Elastic Agents to a newer version, with optional rollout window and source URI. Required privileges: fleet-agents-all. |
| Bulk Upgrade Managed Integrations | `postFleetManagedIntegrationsUpgrade` | Upgrade several Fleet managed integrations to their installed package version. Always returns 200 with a per-policy result array; a missing ID, or one that is not a managed integration, is reported as a per-item failure without failing the batch. Policies already at the installed version report success without being re-persisted. |
| Bulk Upgrade Packages | `postFleetEpmPackagesBulkUpgrade` | Upgrade several integration packages to their latest versions, optionally upgrading their package policies too. Returns a task ID to poll with Get Bulk Upgrade Packages Details. Required privileges: integrations-all and fleet-agent-policies-all. |
| Call the Agent Builder MCP Server | `postAgentBuilderMcp` | Send a Model Context Protocol JSON-RPC request to Kibana's built-in MCP server, for example method "tools/list" to enumerate the Agent Builder tools or "tools/call" to run one. The endpoint requires an Accept header that allows both application/json and text/event-stream, which this action sends for you. |
| Cancel a Workflow Execution | `postWorkflowsExecutionsExecutionidCancel` | Request cancellation of a single running workflow execution. Returns an empty 200 body. |
| Cancel All Executions of a Workflow | `postWorkflowsWorkflowWorkflowidExecutionsCancel` | Request cancellation of every active execution of one workflow. Returns an empty 200 body. |
| Cancel an Agent Action | `postFleetAgentsActionsActionidCancel` | Cancel a pending Fleet agent action by its action ID. Required privileges: fleet-agents-all. |
| Change Agent Privilege Level | `postFleetAgentsAgentidPrivilegeLevelChange` | Change a single Elastic Agent's privilege level to unprivileged, optionally naming the local account it should run as. Required privileges: fleet-agents-all. |
| Chat With an Agent | `postAgentBuilderConverse` | Send a message to an Agent Builder agent and wait for the complete reply. Omit conversation_id to start a new conversation; supply it to continue one. Returns the answer together with the model and token usage of the round. |
| Chat With an Agent (Streaming) | `postAgentBuilderConverseAsync` | Same as Chat With an Agent, but the reply is streamed back as Server-Sent Events (conversation_id_set, then reasoning, tool-call and message-chunk events) instead of one JSON body. Useful for token-by-token UIs. |
| Chat With the Observability AI Assistant | `observabilityAiAssistantChatComplete` | Send a conversation to the Observability AI Assistant and stream the completion back. The reply is an OpenAI-style Server-Sent Event stream of chat.completion.chunk objects terminated by "data: [DONE]", not a single JSON body. |
| Check Fleet Permissions | `getFleetCheckPermissions` | Check whether the current credential has the privileges required to use Fleet, optionally including Fleet Server setup privileges. |
| Check Fleet Server Health | `postFleetHealthCheck` | Check the health of a Fleet Server instance by the ID of its Fleet Server host entry. Required privileges: fleet-settings-all. |
| Clone a Workflow | `postWorkflowsWorkflowIdClone` | Create a copy of an existing workflow. The copy keeps the source's enabled state, description and tags, has " Copy" appended to its name, and gets a new id derived from it (for example my-workflow becomes my-workflow-copy). |
| Copy an Agent Policy | `postFleetAgentPoliciesByAgentpolicyidCopy` | Duplicate an existing agent policy, including its package policies, under a new name. Requires the fleet-agent-policies-all privilege. |
| Create a Case | `createCaseDefaultSpace` | Create a Kibana case. Requires all privileges for the Cases feature in the Management, Observability or Security section, matching the case owner. |
| Create a Case Template | `createCaseTemplateDefaultSpace` | Create a case template. The definition is a YAML string holding the case defaults (name, severity, category, tags, assignees, connector, settings) plus a fields array of inline field definitions or $ref entries into the owner's field library. Limits: 200 templates per owner per space, 200 fields per definition, 30000 characters per definition. Requires all privileges for the Cases feature. |
| Create a Cloud Connector | `postFleetCloudConnectors` | Create a Fleet cloud connector holding the credentials an agentless integration uses to reach AWS, Azure or GCP. Required privileges: fleet-agent-policies-all or integrations-all. |
| Create a Connector with an ID | `postActionsConnectorId` | Create a Kibana action connector at a specific identifier. Config and secrets are type-specific: see the documentation for the chosen connector_type_id, for example .index, .webhook, .slack or .email. |
| Create a Custom Integration | `postFleetEpmCustomIntegrations` | Create a new custom integration package with user-defined data streams. Required privileges: integrations-all and fleet-agent-policies-all. |
| Create a Dashboard | `createDashboard` | Create a dashboard in the current space. Only the title is mandatory; panels, filters, tags and display options can be supplied to build a fully configured dashboard. |
| Create a Fleet Server Host | `postFleetFleetServerHosts` | Register a new Fleet Server host that Elastic Agents check in to. Requires the fleet-settings-all privilege. |
| Create a Fleet Service Token | `postFleetServiceTokens` | Create an Elasticsearch service account token used to enroll a Fleet Server instance. Required privileges: fleet-agents-all. |
| Create a Links Library Item | `postLinks` | Create a links panel in the Kibana library and return its ID, full state and metadata. Each entry is either a dashboardLink pointing at a dashboard saved-object ID or an externalLink pointing at a URL. |
| Create a Maintenance Window | `createMaintenanceWindow` | Create an alerting maintenance window. While it is active, rules that match its scope keep running but their actions are suppressed. |
| Create a Managed Integration | `postFleetManagedIntegrations` | Create a Fleet managed (agentless) integration. Fleet provisions and runs the integration for you, so no agent policy is required. |
| Create a Markdown Library Item | `postMarkdowns` | Create a markdown panel in the Kibana library. The content supports GitHub-flavored Markdown. |
| Create a Package Policy | `postFleetPackagePolicies` | Create a package policy (an integration instance) and attach it to one or more Fleet agent policies. Required privileges: fleet-agent-policies-all and integrations-all. |
| Create a Proxy | `postFleetProxies` | Create a Fleet proxy that agents, outputs and download sources can route their traffic through. Requires the fleet-settings-all privilege. |
| Create a Rule with an ID | `postAlertingRuleId` | Create an alerting rule at a specific identifier. The params object is specific to the chosen rule_type_id. |
| Create a Runtime Field | `createRuntimeFieldDefault` | Add a runtime field to a data view. Runtime fields are computed at query time with a Painless script and need no reindexing; without a script the field falls back to the matching value in _source. |
| Create a Space | `postSpacesSpace` | Create a new Kibana space. The space ID becomes part of the Kibana URL and cannot be changed afterwards. |
| Create a Tag | `postTags` | Create a Kibana saved-object tag and return it with its generated ID. |
| Create a Visualization | `createVisualization` | Create a saved visualization. The body shape depends on the chart type: metric, legacy_metric, gauge, pie, waffle, treemap, mosaic, xy, data_table, heatmap, region_map or tag_cloud. Each type takes a data_source plus its own chart fields (metrics for metric charts, layers for xy, region for region_map, tag_by for tag_cloud). |
| Create a Workflow | `postWorkflowsWorkflow` | Create a new workflow in the current Kibana space from a YAML definition. The YAML must contain at least a name, a triggers list and a steps list. |
| Create Action Connector | `createConnector` | Create an action connector that alerting rules and cases can send notifications to. For a webhook destination use connector_type_id ".webhook" with config.url and config.method, which is how a rule delivers events to an external HTTPS endpoint. |
| Create Alerting Rule | `createRule` | Create an alerting rule that runs on a schedule and fires its configured actions when the rule conditions are met. Point an action at a webhook action connector to deliver events to an external endpoint. Each action must carry a frequency object; the API rejects actions without one. |
| Create an Agent Action | `postFleetAgentsAgentidActions` | Create a new Fleet action targeting a single Elastic Agent, such as a settings change. Required privileges: fleet-agents-all. |
| Create an Agent Binary Download Source | `postFleetAgentDownloadSources` | Create a new agent binary download source, the location Elastic Agents fetch their binaries from. Requires the fleet-settings-all privilege. |
| Create an Agent Builder Agent | `postAgentBuilderAgents` | Create a custom Agent Builder agent with its own instructions, tools, skills and connectors. The id, name, description and configuration are required. |
| Create an Agent Builder Conversation | `postAgentBuilderConversations` | Create an empty Agent Builder conversation against an agent. Every field is optional: the agent defaults to the Elastic AI Agent, the title to "New conversation" and access to private. |
| Create an Agent Builder Skill | `postAgentBuilderSkills` | Create a user-defined Agent Builder skill: a named block of Markdown instructions, optionally bound to specific tools, that agents can load on demand. |
| Create an Agent Builder Tool | `postAgentBuilderTools` | Register a new tool that Agent Builder agents can call. The configuration depends on the type; an esql tool takes {"query": "&lt;ES\|QL&gt;", "params": {...}}, and Kibana derives the tool's parameter schema from the query. |
| Create an Agent Policy | `postFleetAgentPolicies` | Create a new Fleet agent policy. Requires the fleet-agent-policies-all privilege. |
| Create an Agentless Policy (Deprecated) | `postFleetAgentlessPolicies` | Deprecated alias of Create a Managed Integration. Use POST /api/fleet/managed_integrations instead. |
| Create an Enrollment API Key | `postFleetEnrollmentApiKeys` | Create an enrollment API key that Elastic Agents use to enroll into a given agent policy. Requires the fleet-agents-all privilege. |
| Create an Entity | `postSecurityEntityStoreEntitiesEntitytype` | Create an entity record of the given type in the Security Entity Store. The store must be installed first. Required privileges: securitySolution. |
| Create an Output | `postFleetOutputs` | Create a Fleet output that agent policies ship data to. The type field selects the shape: elasticsearch, remote_elasticsearch, logstash, kafka or otlp. Requires the fleet-settings-all privilege. |
| Create Data View | `createDataView` | Create a data view so Kibana can explore a set of Elasticsearch indices. The title is the index pattern; set timeFieldName to enable time-based views. |
| Create or Update a Logstash Pipeline | `putLogstashPipeline` | Create a Logstash pipeline in Kibana's Logstash Central Management, or replace it if the id already exists. |
| Create or Update a Runtime Field | `createUpdateRuntimeFieldDefault` | Create a runtime field on a data view, replacing the existing definition when a field of that name is already present. |
| Create or Update a Security Role | `putSecurityRole` | Create a Kibana security role, or replace it if it already exists. The elasticsearch block carries cluster and index privileges; the kibana block grants feature privileges per space. |
| Create or Update a Stream | `putStream` | Create or update a stream definition, together with the dashboards and rules attached to it. The stream object must carry a type of wired, classic or query, and the matching block: ingest.wired for wired, ingest for classic, query for query. Classic streams can only be updated here, not created. Requires the manage_stream privilege. |
| Create or Update Roles | `postSecurityRoles` | Create or update several Kibana roles in one request. Roles is a map of role name to role definition, each with elasticsearch and kibana privilege blocks. |
| Delete a Backfill by ID | `deleteAlertingRulesBackfillId` | Cancel and delete an alerting rule backfill by its identifier. |
| Delete a Case Comment | `deleteCaseCommentDefaultSpace` | Remove one comment or alert attachment from a case. Requires all privileges for the Cases feature. |
| Delete a Case Template | `deleteCaseTemplateDefaultSpace` | Delete a case template by its identifier. Requires all privileges for the Cases feature. |
| Delete a Cloud Connector | `deleteFleetCloudConnectorsCloudconnectorid` | Delete a Fleet cloud connector by ID. Use Force to delete one that package policies still reference. Required privileges: fleet-agent-policies-all or integrations-all. |
| Delete a Conversation Attachment | `deleteAgentBuilderConversationsConversationIdAttachmentsAttachmentId` | Remove an attachment from a conversation. By default it is soft-deleted and can be restored; set permanent to true to erase it, which only works for attachments no conversation round references. |
| Delete a Dashboard | `deleteDashboard` | Delete a dashboard by id. Panels saved inside the dashboard go with it; saved objects it only references are left in place. |
| Delete a Fleet Agent | `deleteFleetAgentsAgentid` | Delete an enrolled Elastic Agent record from Fleet by its agent ID. Required privileges: fleet-agents-all. |
| Delete a Fleet Server Host | `deleteFleetFleetServerHostsByItemid` | Delete a Fleet Server host by id. Requires the fleet-settings-all privilege. |
| Delete a Links Library Item | `deleteLinksId` | Permanently delete a links library item by its ID. |
| Delete a Logstash Pipeline | `deleteLogstashPipeline` | Delete a Logstash pipeline from Kibana's Logstash Central Management. |
| Delete a Maintenance Window | `deleteMaintenanceWindow` | Permanently delete an alerting maintenance window by id. |
| Delete a Managed Integration | `deleteFleetManagedIntegrationsPolicyid` | Delete a Fleet managed (agentless) integration by its policy ID. |
| Delete a Markdown Library Item | `deleteMarkdownsId` | Permanently delete a markdown library item by its ID. |
| Delete a Package | `deleteFleetEpmPackagesPkgname` | Uninstall an integration package and remove all of its assets. Required privileges: integrations-all and fleet-agent-policies-all. |
| Delete a Package Policy | `deleteFleetPackagePoliciesPackagepolicyid` | Delete one Fleet package policy by ID. Required privileges: fleet-agent-policies-all and integrations-all. |
| Delete a Package Version | `deleteFleetEpmPackagesByPkgnameByPkgversion` | Uninstall a specific version of an integration package and remove all of its assets. Requires the integrations-all and fleet-agent-policies-all privileges. |
| Delete a Proxy | `deleteFleetProxiesByItemid` | Delete a Fleet proxy by id. Requires the fleet-settings-all privilege. |
| Delete a Runtime Field | `deleteRuntimeFieldDefault` | Remove a runtime field from a data view. |
| Delete a Security Role | `deleteSecurityRole` | Delete a Kibana security role by name. Users who only had this role lose the access it granted. |
| Delete a Snooze Schedule from a Rule | `deleteAlertingRuleRuleidSnoozeScheduleScheduleid` | Remove one snooze schedule from an alerting rule so its actions fire again. |
| Delete a Space | `deleteSpacesSpaceId` | Delete a Kibana space and every saved object inside it. This cannot be undone and the reserved Default space cannot be deleted. |
| Delete a Stream | `deleteStream` | Delete a stream definition and the data stream behind it. Requires the manage_stream privilege. |
| Delete a Tag | `deleteTagsId` | Permanently delete a Kibana saved-object tag by ID. The tag is also removed from every object that referenced it. |
| Delete a Visualization | `deleteVisualization` | Permanently delete a saved visualization by its ID. |
| Delete a Workflow | `deleteWorkflowsWorkflowId` | Delete a single workflow. By default the workflow is soft-deleted and can be restored; set force to true to remove it permanently. |
| Delete Action Connector | `deleteConnector` | Delete an action connector by id. You cannot delete a connector that is still referenced by a rule; remove the rule action first. Returns 204 No Content on success. |
| Delete Alerting Rule | `deleteRule` | Delete an alerting rule by id. This permanently removes the rule and stops it running. Returns 204 No Content on success. |
| Delete All Case Comments | `deleteCaseCommentsDefaultSpace` | Remove every comment and alert attachment from a case. Requires all privileges for the Cases feature. |
| Delete an Agent Binary Download Source | `deleteFleetAgentDownloadSourcesBySourceid` | Delete an agent binary download source by id. Requires the fleet-settings-all privilege. |
| Delete an Agent Builder Agent | `deleteAgentBuilderAgentsId` | Delete a custom Agent Builder agent by id. Built-in agents such as elastic-ai-agent cannot be deleted. |
| Delete an Agent Builder Conversation | `deleteAgentBuilderConversationsConversationId` | Permanently delete one Agent Builder conversation and its rounds. |
| Delete an Agent Builder Skill | `deleteAgentBuilderSkillsSkillid` | Delete a user-defined Agent Builder skill. If any agent still uses it the call is refused unless force is true, which first removes the skill from those agents. |
| Delete an Agent Builder Tool | `deleteAgentBuilderToolsToolid` | Delete a user-created Agent Builder tool. If any agent still uses it the call is refused unless force is true, which first removes the tool from those agents. |
| Delete an Agent Policy | `postFleetAgentPoliciesDelete` | Delete an agent policy by id. The id goes in the request body, not the path. Requires the fleet-agent-policies-all privilege. |
| Delete an Agentless Policy (Deprecated) | `deleteFleetAgentlessPoliciesPolicyid` | Deprecated alias of Delete a Managed Integration. Use DELETE /api/fleet/managed_integrations/{policyId} instead. |
| Delete an Entity | `deleteSecurityEntityStoreEntities` | Delete one entity record from the Security Entity Store. It disappears from the latest index immediately. Required privileges: securitySolution. |
| Delete an Output | `deleteFleetOutputsByOutputid` | Delete a Fleet output by id. Preconfigured outputs and outputs still referenced by an agent policy cannot be deleted. Requires the fleet-settings-all privilege. |
| Delete an Uploaded Agent File | `deleteFleetAgentsFilesFileid` | Delete a diagnostics or log file that an Elastic Agent uploaded to Fleet. Required privileges: fleet-agents-all. |
| Delete Cases | `deleteCaseDefaultSpace` | Delete one or more Kibana cases. The ids query parameter must be a JSON array string, for example ["e58e77e3-...","b2e0e1a4-..."]. Requires read or all privileges plus the delete sub-feature privilege for the Cases feature matching the case owner. |
| Delete Data Stream Assets for a Package | `deleteFleetEpmPackagesPkgnamePkgversionDatastreamAssets` | Delete the data stream assets that an integration package created for a given package policy. Required privileges: integrations-all and fleet-agent-policies-all. |
| Delete Data View | `deleteDataView` | Delete a data view by id. This removes only the Kibana saved object; the underlying Elasticsearch indices are untouched. Returns 200 with an empty body on success. |
| Delete Kibana Assets for a Package | `deleteFleetEpmPackagesPkgnamePkgversionKibanaAssets` | Delete the Kibana assets such as dashboards and visualizations that an integration package version installed. Required privileges: integrations-all and fleet-agent-policies-all. |
| Disable an Alerting Rule | `disableRule` | Disable an alerting rule so that it stops running. The rule definition is kept. |
| Disable an Entity Resolution Rule | `putSecurityEntityStoreResolutionRuleDisable` | Turn off one managed entity resolution rule in this space. Required privileges: securitySolution and securitySolution-entity-analytics. |
| Disable Wired Streams | `disableStreams` | Turn off wired streams and delete every existing wired stream definition. The data already written into wired streams is not deleted. Requires the manage_stream privilege. |
| Download a Kubernetes Agent Manifest | `getFleetKubernetesDownload` | Download the Kubernetes manifest for deploying Elastic Agent as a YAML file. Required privileges: fleet-agent-policies-read or fleet-setup. |
| Download an Agent Policy | `getFleetAgentPoliciesByAgentpolicyidDownload` | Download the agent policy as YAML, optionally formatted for a standalone agent or for Kubernetes. The response body is raw YAML text, not JSON. Requires the fleet-agent-policies-read or fleet-setup privilege. |
| Dry Run a Package Policy Upgrade | `postFleetPackagePoliciesUpgradeDryrun` | Preview the changes that upgrading the named Fleet package policies would make, without applying them. Required privileges: fleet-agent-policies-read and integrations-read. |
| Enable an Alerting Rule | `enableRule` | Enable an alerting rule so that it starts running on its schedule. |
| Enable an Entity Resolution Rule | `putSecurityEntityStoreResolutionRuleEnable` | Turn on one managed entity resolution rule in this space. Required privileges: securitySolution and securitySolution-entity-analytics. |
| Enable Wired Streams | `enableStreams` | Turn on wired streams for this project, creating the root stream and the Elasticsearch assets behind it. Requires the manage_stream privilege. |
| Execute an Agent Builder Tool | `postAgentBuilderToolsExecute` | Run one Agent Builder tool directly, without going through an agent, and return its results. Useful for testing a tool definition. |
| Export Saved Objects | `postSavedObjectsExport` | Export saved objects as an NDJSON stream so they can be imported into another Kibana. Supply either types or objects. Treat the output as opaque; editing it risks data loss, and exports cannot be imported into an older Kibana. |
| Export Stream Content | `exportStreamContent` | Export a content pack describing a stream's structure: its routing, mappings and processing. Significant-event queries are not included. The response is a binary content-pack archive. Requires the manage_stream privilege. |
| Export Workflows | `postWorkflowsExport` | Export one or more workflows as portable YAML entries together with an export manifest, so they can be re-imported with Bulk Create Workflows. |
| Find Alerting Rules | `findRules` | Search the alerting rules in the space, with paging, sorting and an optional KQL filter. Returns each rule with its schedule, parameters, actions and execution status. |
| Find Case Activity | `findCaseActivityDefaultSpace` | Search the user-action history of a case, showing who changed what and when. Requires read privileges for the Cases feature. |
| Find Case Comments | `findCaseCommentsDefaultSpace` | Search the comments and alert attachments of a case, with paging and sorting. Requires read privileges for the Cases feature. |
| Find Case Connectors | `findCaseConnectorsDefaultSpace` | List the action connectors that cases can be pushed to, such as Jira, ServiceNow or Swimlane. Requires read privileges for the Actions and Connectors feature. |
| Find Maintenance Windows | `findMaintenanceWindows` | List the maintenance windows configured for alerting, with paging. During a maintenance window matching rules keep running but their actions are suppressed. |
| Find Rule Backfills | `postAlertingRulesBackfillFind` | Search the scheduled and completed backfills of alerting rules, with paging, date filters and sorting. |
| Fork a Stream | `forkStream` | Fork a wired stream, creating a child stream that receives the documents matching a routing condition. Requires the manage_stream privilege. |
| Generate a Logstash API Key | `postFleetLogstashApiKeys` | Generate an Elasticsearch API key for Logstash to use with a Fleet Logstash output. Required privileges: fleet-settings-all. |
| Get a Backfill by ID | `getAlertingRulesBackfillId` | Get one alerting rule backfill by its identifier, including its schedule and status. |
| Get a Case Comment | `getCaseCommentDefaultSpace` | Get one comment or alert attachment of a case by its identifier. Requires read privileges for the Cases feature. |
| Get a Case Template | `getCaseTemplateDefaultSpace` | Get one case template by its identifier. Requires read privileges for the Cases feature. |
| Get a Cloud Connector | `getFleetCloudConnectorsCloudconnectorid` | Get one Fleet cloud connector by its ID. Required privileges: fleet-agent-policies-read or integrations-read. |
| Get a Dashboard | `getDashboard` | Get a single dashboard by id, including its panels, options and saved references. |
| Get a Decrypted Uninstall Token | `getFleetUninstallTokensUninstalltokenid` | Get one Fleet uninstall token, decrypted, by its ID. Required privileges: fleet-agents-all. |
| Get a Fleet Agent | `getFleetAgentsAgentid` | Get a single enrolled Elastic Agent by its agent ID, optionally including CPU and memory metrics. Required privileges: fleet-agents-read. |
| Get a Fleet Server Host | `getFleetFleetServerHostsByItemid` | Get a single Fleet Server host by id. Requires the fleet-settings-read privilege. |
| Get a Full Agent Policy | `getFleetAgentPoliciesByAgentpolicyidFull` | Get the fully resolved agent policy, with every input, output and secret reference expanded exactly as an Elastic Agent receives it. Requires the fleet-agent-policies-read privilege. |
| Get a Kubernetes Agent Manifest | `getFleetKubernetes` | Get the Kubernetes manifest for deploying Elastic Agent, optionally pre-filled with a Fleet Server URL and enrollment token. Required privileges: fleet-agent-policies-read or fleet-setup. |
| Get a Limited Package List | `getFleetEpmPackagesLimited` | List the integration packages that cannot be uninstalled, such as elastic_agent and fleet_server. Required privileges: integrations-read, fleet-setup or fleet-all. |
| Get a Links Library Item | `getLinksId` | Get the complete state of a links library item by its ID. |
| Get a Logstash Pipeline | `getLogstashPipeline` | Get a single Logstash pipeline managed through Kibana by its id, including its configuration and settings. |
| Get a Maintenance Window | `getMaintenanceWindow` | Get a single alerting maintenance window by id, including its schedule and scope. |
| Get a Managed Integration | `getFleetManagedIntegrationsPolicyid` | Get one Fleet managed (agentless) integration by its policy ID. |
| Get a Markdown Library Item | `getMarkdownsId` | Get the complete state of a markdown library item by its ID. |
| Get a Package | `getFleetEpmPackagesPkgname` | Get information about an integration package by name, returning the latest installed or available version. |
| Get a Package File | `getFleetEpmPackagesPkgnamePkgversionFilepath` | Get the contents of one file inside an integration package, such as its readme or manifest. The file path may contain slashes; Kibana decodes the encoded path. Required privileges: integrations-read, fleet-setup or fleet-all. |
| Get a Package Policy | `getFleetPackagePoliciesPackagepolicyid` | Get one Fleet package policy by its ID. |
| Get a Package Version | `getFleetEpmPackagesByPkgnameByPkgversion` | Get the full details of one version of an integration package, including its data streams, policy templates, variables and assets. |
| Get a Proxy | `getFleetProxiesByItemid` | Get a single Fleet proxy by id. Requires the fleet-settings-read privilege. |
| Get a Resolution Group | `getSecurityEntityStoreResolutionGroup` | Get the entity resolution group an entity belongs to, listing every entity linked to it. Required privileges: securitySolution and securitySolution-entity-analytics. |
| Get a Runtime Field | `getRuntimeFieldDefault` | Get a single runtime field of a data view by name. |
| Get a Security Role | `getSecurityRole` | Get a single Kibana security role by name. |
| Get a Stream | `getStream` | Get the definition of a single stream by name, including its ingest configuration and dashboards. |
| Get a Tag | `getTagsId` | Get one Kibana saved-object tag by its ID. |
| Get a Visualization | `getVisualization` | Get the complete state of a saved visualization by its ID. |
| Get a Workflow | `getWorkflowsWorkflowId` | Retrieve a single workflow by id, including its YAML source, its parsed definition and its validation state. |
| Get a Workflow Execution | `getWorkflowsExecutionsExecutionid` | Retrieve one workflow execution by id, with its status, timings, the workflow definition it ran and the per-step results. Input and output payloads are omitted unless requested. |
| Get a Workflow Step Execution | `getWorkflowsExecutionsExecutionidStepStepexecutionid` | Retrieve one step execution of a workflow execution, with its status, timings, scope stack and ordering indexes. |
| Get Agent Access Control | `getAgentBuilderAgentsIdAccessControl` | Read the sharing settings of an Agent Builder agent: whether it is private or public, who it is shared with, and whether the caller may change that. |
| Get Agent Setup Info | `getFleetAgentsSetup` | Get the current Fleet agent setup status, including whether Fleet is ready to enroll agents and which requirements or optional features are missing. Required privileges: fleet-agents-read, fleet-agent-policies-read, fleet-settings-read or fleet-setup. |
| Get Agent Tags | `getFleetAgentsTags` | List every tag used across enrolled Elastic Agents, optionally filtered with a KQL query. Required privileges: fleet-agents-read. |
| Get Agent Token Consumption | `postAgentBuilderAgentsAgentIdConsumption` | List the conversations held with one agent together with their token usage, round counts, LLM call counts and any high-token warnings. Uses search_after cursor pagination. |
| Get Agent Uploads | `getFleetAgentsAgentidUploads` | List the diagnostics and log files that a single Elastic Agent has uploaded to Fleet. Required privileges: fleet-agents-read. |
| Get Agents by Action IDs | `postFleetAgents` | Retrieve the Elastic Agents associated with a set of Fleet action IDs. Required privileges: fleet-agents-read. |
| Get Alerting Framework Health | `getAlertingHealth` | Get the health of the Kibana alerting framework: whether it is sufficiently secure, whether a permanent encryption key is configured, and the status of rule execution and alert decryption. |
| Get Alerts Attached to a Case | `getCaseAlertsDefaultSpace` | List the alerts attached to a case. Requires read privileges for the Cases feature. |
| Get an A2A Agent Card | `getAgentBuilderA2aAgentidjson` | Return the Agent2Agent (A2A) agent card for an Agent Builder agent: the metadata another A2A client needs to discover and call it, including its endpoint URL, provider, protocol version, capabilities and skills. |
| Get an Agent Binary Download Source | `getFleetAgentDownloadSourcesBySourceid` | Get a single agent binary download source by id. Requires the fleet-agent-policies-read or fleet-settings-read privilege. |
| Get an Agent Builder Agent | `getAgentBuilderAgentsId` | Retrieve one Agent Builder agent by id, with its full configuration, access control and the caller's permissions on it. |
| Get an Agent Builder Conversation | `getAgentBuilderConversationsConversationId` | Retrieve one Agent Builder conversation by id, including every round of the exchange and the events recorded during it. |
| Get an Agent Builder Skill | `getAgentBuilderSkillsSkillid` | Retrieve one Agent Builder skill by id, including its full Markdown instructions and the tools it references. |
| Get an Agent Builder Tool | `getAgentBuilderToolsToolid` | Retrieve one Agent Builder tool by id, with its configuration, derived parameter schema and confirmation policy. |
| Get an Agent Policy | `getFleetAgentPoliciesByAgentpolicyid` | Get a single agent policy by id. Requires the fleet-agent-policies-read, fleet-agents-read or fleet-setup privilege. |
| Get an Agent's Effective Config | `getFleetAgentsAgentidEffectiveConfig` | Get the effective configuration currently applied to a single Elastic Agent. Required privileges: fleet-agents-read. |
| Get an Agentless Policy (Deprecated) | `getFleetAgentlessPoliciesPolicyid` | Deprecated alias of Get a Managed Integration. Use GET /api/fleet/managed_integrations/{policyId} instead. |
| Get an Alerting Rule | `getRule` | Get a single alerting rule by id, including its schedule, parameters, actions and last execution status. |
| Get an Enrollment API Key | `getFleetEnrollmentApiKeysByKeyid` | Get a single enrollment API key by id. Requires the fleet-agents-all or fleet-setup privilege. |
| Get an Inputs Template | `getFleetEpmTemplatesPkgnamePkgversionInputs` | Get the inputs template for an integration package version, used to pre-populate package policy forms. Required privileges: integrations-read, fleet-setup or fleet-all. |
| Get an Output | `getFleetOutputsByOutputid` | Get a single Fleet output by id. The returned shape depends on the output type: elasticsearch, remote_elasticsearch, logstash, kafka or otlp. Requires the fleet-settings-read or fleet-agent-policies-read privilege. |
| Get an Uploaded Agent File | `getFleetAgentsFilesFileidFilename` | Download a file that an Elastic Agent uploaded to Fleet, such as a diagnostics bundle. The response is the raw file content. Required privileges: fleet-agents-read. |
| Get Applicable Case Fields | `getApplicableFieldsDefaultSpace` | List the case fields that apply to an owning application, including the global library fields. Requires read privileges for the Cases feature. |
| Get Applicable Fields for a Case | `getCaseApplicableFieldsDefaultSpace` | List the case fields that apply to one specific case, including its owner's global fields. Requires read privileges for the Cases feature. |
| Get Auto Upgrade Agent Status | `getFleetAgentPoliciesByAgentpolicyidAutoUpgradeAgentsStatus` | Get the auto-upgrade status of the agents assigned to an agent policy, broken down by the agent version they are currently on. Requires the fleet-agents-read privilege. |
| Get Available Agent Versions | `getFleetAgentsAvailableVersions` | Get a list of Elastic Agent versions available for upgrade in Fleet. Required privilege: fleet-agents-read. |
| Get Bulk Rollback Packages Details | `getFleetEpmPackagesBulkRollbackTaskid` | Get the status and per-package results of a bulk package rollback task. Required privileges: integrations-all and fleet-agent-policies-all. |
| Get Bulk Uninstall Packages Details | `getFleetEpmPackagesBulkUninstallTaskid` | Get the status and per-package results of a bulk package uninstall task. Required privileges: integrations-all and fleet-agent-policies-all. |
| Get Bulk Upgrade Packages Details | `getFleetEpmPackagesBulkUpgradeTaskid` | Get the status and per-package results of a bulk package upgrade task. Required privileges: integrations-all and fleet-agent-policies-all. |
| Get Case Configuration | `getCaseConfigurationDefaultSpace` | Get the case settings for each owning application, including the default connector, closure behaviour, custom fields, templates and observable types. Requires read privileges for the Cases feature. |
| Get Case Information | `getCaseDefaultSpace` | Get one Kibana case by ID. Comments are not included; use Find Case Comments for those. Requires read privileges for the Cases feature matching the case owner. |
| Get Case Reporters | `getCaseReportersDefaultSpace` | List the users who have opened cases, so they can be offered as a reporter filter. Requires read privileges for the Cases feature. |
| Get Case Tags | `getCaseTagsDefaultSpace` | List every tag used on cases, so tags can be offered as a filter. Requires read privileges for the Cases feature. |
| Get Cases for an Alert | `getCasesByAlertDefaultSpace` | List the cases an alert has been attached to. Requires read privileges for the Cases feature. |
| Get Child Workflow Executions | `getWorkflowsExecutionsExecutionidChildren` | List the child executions spawned by a workflow execution, for example by foreach fan-out or by a step that calls another workflow. The response body is a bare JSON array. |
| Get Cloud Connector Usage | `getFleetCloudConnectorsCloudconnectoridUsage` | List the package policies that use a given Fleet cloud connector. Required privileges: fleet-agent-policies-read or integrations-read. |
| Get Connector Information | `getActionsConnectorId` | Get one Kibana action connector by its ID, including its type, configuration and whether any secrets are missing. |
| Get Data View | `getDataView` | Get a single data view by id, including its index pattern, time field, field formats and runtime field definitions. |
| Get Entity Store Status | `getSecurityEntityStoreStatus` | Get the overall Entity Store status and the status of each entity engine, optionally with component-level health. Required privileges: securitySolution. |
| Get Executions of a Workflow | `getWorkflowsWorkflowWorkflowidExecutions` | List the executions of one workflow, filterable by status, execution type, who ran it and start or finish time. Array filters take one repeated parameter per value in Kibana, so one value per filter can be sent per request. |
| Get Fleet Agent Status Summary | `getFleetAgentStatus` | Get a count of Elastic Agents by status - online, error, inactive, offline, updating, unenrolled and more. |
| Get Fleet Settings | `getFleetSettings` | Get the global Fleet settings for the space, including the configured Fleet Server hosts and prerelease integration options. |
| Get Fleet Space Settings | `getFleetSpaceSettings` | Get the Fleet settings that apply to the current Kibana space, such as the namespace prefixes that are allowed in it. |
| Get Incoming Agent Data | `getFleetAgentStatusData` | Show which data streams the named Elastic Agents are actively sending data to, optionally with a preview of the ingested documents. Required privileges: fleet-agents-read. |
| Get Installed Packages | `getFleetEpmPackagesInstalled` | List the integration packages currently installed on this deployment, with paging. Requires the integrations-read, fleet-setup or fleet-all privilege. |
| Get Integration Data Streams | `getFleetEpmDataStreams` | List the data streams contributed by installed integration packages, optionally filtered by type or by whether they currently hold data. |
| Get Kibana Status | `getStatus` | Get the overall health of the Kibana instance and the status of each of its plugins, along with version and build information. |
| Get Outputs for Agent Policies | `postFleetAgentPoliciesOutputs` | Get the data and monitoring outputs that several agent policies resolve to, in one request. Requires the fleet-agent-policies-read and fleet-settings-read privileges. |
| Get Outputs for an Agent Policy | `getFleetAgentPoliciesByAgentpolicyidOutputs` | Get the data output and monitoring output that a single agent policy resolves to. Requires the fleet-agent-policies-read and fleet-settings-read privileges. |
| Get Package Dependencies | `getFleetEpmPackagesPkgnamePkgversionDependencies` | List the packages that a given integration package version depends on. Required privileges: integrations-read, fleet-setup or fleet-all. |
| Get Package Stats | `getFleetEpmPackagesByPkgnameStats` | Get usage statistics for an integration package, namely how many agent policies and package policies reference it. Requires the integrations-read, fleet-setup or fleet-all privilege. |
| Get Packages | `getFleetEpmPackages` | List the integration packages available in the Elastic Package Registry. Narrow the result with the category filter, since the unfiltered catalogue is very large. Requires the integrations-read, fleet-setup or fleet-all privilege. |
| Get Space | `getSpace` | Get a single Kibana space by its identifier, including its name, colour and the features disabled within it. |
| Get Step Executions of a Workflow | `getWorkflowsWorkflowWorkflowidExecutionsSteps` | List the individual step executions across all runs of one workflow, optionally narrowed to a single step or a time window. |
| Get Stream Ingest Settings | `getStreamIngest` | Get the ingest settings of an ingest stream, including its processing steps, lifecycle, failure store and index settings. Requires the read_stream privilege. |
| Get Stream Query Settings | `getStreamQueries` | Get the ES\|QL query and field descriptions that define a query stream. Requires the read_stream privilege. |
| Get Task Manager Health | `getTaskManagerHealth` | Get the health of the Kibana task manager, which runs alerting rules and other background work. Reports configuration, workload and runtime statistics. |
| Get the Connector OAuth Callback Script | `getActionsConnectorOauthCallbackScript` | Get the JavaScript that Kibana serves to the OAuth callback popup for action connectors. |
| Get the Default Data View | `getDefaultDataViewDefault` | Get the identifier of the default data view for the current Kibana space. |
| Get the Elasticsearch Query for a Rule | `getAlertingRuleIdQueryInspector` | Show the Elasticsearch query an alerting rule runs, and optionally run it and include the response. |
| Get the External Resume Form | `getWorkflowsExecutionsExecutionidStepsStepidResumeExternalForm` | Return the HTML form that a human reviewer fills in to supply input to a paused workflow step. Authorised by the resume token rather than the API key. |
| Get the Latest Output Health | `getFleetOutputsByOutputidHealth` | Get the most recent health status reported for a Fleet output. Requires the fleet-settings-read privilege. |
| Get the Package Verification Key ID | `getFleetEpmVerificationKeyId` | Get the id of the GPG key Fleet uses to verify integration package signatures. |
| Get the Workflow JSON Schema | `getWorkflowsSchema` | Return the JSON Schema that workflow YAML definitions are validated against, for use in editors and generators. |
| Get Workflow Aggregations | `getWorkflowsAggs` | Return the distinct values and document counts of a workflow field, for building filter pickers. Kibana expects one repeated fields parameter per field, so one field can be aggregated per request. |
| Get Workflow Connectors | `getWorkflowsConnectors` | Return every Kibana action connector type that workflow steps can call, with the configured instances, licence requirements and sub-actions of each type. |
| Get Workflow Execution Logs | `getWorkflowsExecutionsExecutionidLogs` | Return the paginated engine log entries written during a workflow execution, optionally narrowed to a single step execution. |
| Get Workflow Statistics | `getWorkflowsStats` | Return summary statistics for the current space: how many workflows are enabled and disabled, and a per-day count of completed, failed and cancelled executions. |
| Get Workflows by IDs | `postWorkflowsMget` | Retrieve up to 500 workflows by their identifiers in a single request, optionally limiting the returned fields. The response body is a bare JSON array of workflow documents. |
| Handle a Connector OAuth Callback | `getActionsConnectorOauthCallback` | Complete the OAuth 2.0 authorization code flow for a Kibana action connector by exchanging the authorization code for access and refresh tokens. The identity provider normally calls this endpoint in the browser. Required privilege: actions:oauth. |
| Initiate Fleet Agent Setup | `postFleetAgentsSetup` | Initialize the Fleet agent subsystem. Elastic Agents call this to trigger Fleet setup; it is idempotent and safe to call repeatedly. Required privileges: fleet-agents-all or fleet-setup. |
| Initiate Fleet Setup | `postFleetSetup` | Initialize Fleet and create the Elasticsearch resources it needs. Idempotent and safe to call repeatedly. Required privileges: fleet-setup. |
| Install a Package from the Registry | `postFleetEpmPackagesPkgname` | Install the latest version of an integration package from the Elastic Package Registry. Required privileges: integrations-all and fleet-agent-policies-all. |
| Install a Package Version | `postFleetEpmPackagesByPkgnameByPkgversion` | Install a specific version of an integration package from the Elastic Package Registry, creating all of its Elasticsearch and Kibana assets. Requires the integrations-all and fleet-agent-policies-all privileges. |
| Install Alert Rule Assets for a Package | `postFleetEpmPackagesPkgnamePkgversionRuleAssets` | Install the Kibana alert rule assets shipped with an integration package version. Required privileges: integrations-all and fleet-agent-policies-all. |
| Install Kibana Assets for a Package | `postFleetEpmPackagesPkgnamePkgversionKibanaAssets` | Install the Kibana assets such as dashboards and visualizations shipped with an integration package version, optionally into specific spaces. Required privileges: integrations-all and fleet-agent-policies-all. |
| Install the Entity Store | `postSecurityEntityStoreInstall` | Install the Security Entity Store and create engines for the given entity types. The log extraction settings are shared by all engines: supply them once at install, or omit them to keep the defaults or the existing configuration. Required privileges: securitySolution. |
| Link a Stream Attachment | `putStreamAttachment` | Attach a dashboard, alerting rule or SLO to a stream. Linking an attachment that is already linked is a no-op. Requires the manage_stream privilege. |
| Link Entities | `postSecurityEntityStoreResolutionLink` | Link one or more entities to a target entity, forming a resolution group. The change becomes visible on the next index refresh. Required privileges: securitySolution and securitySolution-entity-analytics. |
| List Action Connector Types | `listConnectorTypes` | List the action connector types available on this deployment, with whether each is enabled and the minimum licence it requires. Optionally filter to the types usable by a given feature. |
| List Action Connectors | `listConnectors` | List all action connectors configured in the space. Action connectors define where an alerting rule sends its notifications, for example a webhook, email or Slack destination. |
| List Agent Action Statuses | `getFleetAgentsActionStatus` | List the status of recent Fleet agent actions, including how many agents completed, failed or are still in progress. Required privileges: fleet-agents-read. |
| List Agent Builder Agents | `getAgentBuilderAgents` | List every Agent Builder agent available in the current Kibana space, including the built-in Elastic AI Agent, with each agent's configuration, access control and the caller's permissions on it. |
| List Agent Builder Conversations | `getAgentBuilderConversations` | List the Agent Builder conversations visible to the caller, newest first, optionally narrowed to one agent or to pinned conversations. |
| List Agent Builder Skills | `getAgentBuilderSkills` | List the Agent Builder skills available in the space: the built-in Elastic playbooks plus any user-created skills, and optionally skills contributed by installed plugins. |
| List Agent Builder Tools | `getAgentBuilderTools` | List every tool in the Agent Builder tool registry: the built-in platform tools plus any user-created ESQL or index-search tools, with their descriptions, tags and confirmation policy. |
| List Agentless Policies (Deprecated) | `getFleetAgentlessPolicies` | Deprecated alias of List Managed Integrations. Use GET /api/fleet/managed_integrations instead. Lists Fleet managed (agentless) integrations. |
| List Case Templates | `getCaseTemplatesDefaultSpace` | List the case templates defined for an owning application. Requires read privileges for the Cases feature. |
| List Cloud Connectors | `getFleetCloudConnectors` | List the Fleet cloud connectors that hold cloud provider credentials for agentless integrations. Note: on Kibana 9.6.0 Serverless the Kuery filter is rejected by Fleet itself ("This type cloud_connectors is not allowed"), so leave it empty and filter client-side. Required privileges: fleet-agent-policies-read or integrations-read. |
| List Conversation Attachments | `getAgentBuilderConversationsConversationIdAttachments` | List the attachments on an Agent Builder conversation together with the total token estimate they contribute to the context window. |
| List Dashboards | `listDashboards` | List the dashboards in the current space, with paging. |
| List Data Views | `listDataViews` | List all data views in the space. A data view tells Kibana which Elasticsearch indices to explore and which field is the time field. |
| List Entity Resolution Rules | `getSecurityEntityStoreResolutionRules` | List the managed entity resolution rules and whether each is enabled in this space. Required privileges: securitySolution and securitySolution-entity-analytics. |
| List Entity Store Entities | `getSecurityEntityStoreEntities` | List entity records from the Security Entity Store. Use page and per_page for page-based paging, or filter, size and searchAfter for cursor-based paging; the two modes cannot be combined. Required privileges: securitySolution. |
| List Features | `listFeatures` | List the Kibana features available on this deployment, with the privileges each feature exposes. Useful for building space and role definitions. |
| List Fleet Agent Download Sources | `listFleetAgentDownloadSources` | List the agent binary download sources that Fleet offers to Elastic Agents for upgrades. |
| List Fleet Agent Policies | `listFleetAgentPolicies` | List the Fleet agent policies, which define what integrations the Elastic Agents enrolled in them run. |
| List Fleet Agents | `listFleetAgents` | List the Elastic Agents enrolled in Fleet, with their status, version and the policy they run. |
| List Fleet Data Streams | `getFleetDataStreams` | List all Fleet-managed data streams with their package, namespace, size and last activity. Required privileges: fleet-agents-all, fleet-agent-policies-all and fleet-settings-all. |
| List Fleet Enrollment API Keys | `listFleetEnrollmentApiKeys` | List the Fleet enrollment API keys that Elastic Agents use to enrol into an agent policy. |
| List Fleet Outputs | `listFleetOutputs` | List the Fleet outputs, which define where Elastic Agents ship their data. |
| List Fleet Package Policies | `listFleetPackagePolicies` | List the Fleet package policies, which are the integration instances attached to agent policies. |
| List Fleet Proxies | `listFleetProxies` | List the Fleet proxies that agents and outputs can route their traffic through. |
| List Fleet Server Hosts | `listFleetServerHosts` | List the Fleet Server hosts that Elastic Agents connect to. |
| List Fleet Uninstall Tokens | `listFleetUninstallTokens` | List the Fleet uninstall tokens, which are required to remove a tamper-protected Elastic Agent from a host. |
| List Integration Categories | `listFleetPackageCategories` | List the categories that Elastic integration packages are grouped into, with the number of packages in each. |
| List Links Library Items | `getLinks` | Return a paginated list of links panels saved in the Kibana library, with optional text search and tag include/exclude filters. Use Get a Links Library Item by ID for the full state. |
| List Logstash Pipelines | `listLogstashPipelines` | List the Logstash pipelines managed through Kibana's Logstash Central Management, with their descriptions and last-modified times. |
| List Managed Integrations | `getFleetManagedIntegrations` | List Fleet managed (agentless) integrations, with paging, sorting and KQL filtering on name, namespace and package.name. |
| List Markdown Library Items | `getMarkdowns` | Return a paginated list of markdown panels saved in the Kibana library, with optional text search and tag include/exclude filters. |
| List Rule Types | `listRuleTypes` | List the alerting rule types available on this deployment, with their action groups, action variables and the authorized consumers. Use the returned id as rule_type_id when creating a rule. |
| List Security Roles | `listSecurityRoles` | List the Kibana security roles, including their Elasticsearch cluster and index privileges and their Kibana feature privileges. |
| List Spaces | `listSpaces` | List all Kibana spaces. Spaces partition saved objects, dashboards and rules so different teams can work in isolation. |
| List Stale Conversation Attachments | `getAgentBuilderConversationsConversationIdAttachmentsStale` | Report, for every by-reference attachment on a conversation, whether the saved object it points at has changed since the attachment was resolved. The response lists each attachment with an is_stale flag rather than only the stale ones. |
| List Stream Attachments | `listStreamAttachments` | List the dashboards, alerting rules and SLOs attached to a stream that the current user can see in this space. Requires the read_stream privilege. |
| List Streams | `listStreams` | List the streams known to Kibana, including classic streams backed by existing data streams and wired streams. |
| Migrate a Single Agent | `postFleetAgentsAgentidMigrate` | Migrate one Elastic Agent to another cluster by re-enrolling it against a new Fleet Server URI and enrollment token. Required privileges: fleet-agents-all. |
| Migrate Multiple Agents | `postFleetAgentsBulkMigrate` | Bulk migrate Elastic Agents to another cluster by enrolling them against a new Fleet Server URI and enrollment token. Required privilege: fleet-agents-all. |
| Mute a Single Alert | `muteRuleAlert` | Mute one specific alert of an alerting rule, leaving the rule's other alerts untouched. |
| Mute All Alerts of a Rule | `muteAllRuleAlerts` | Mute every alert of an alerting rule. The rule keeps running and keeps detecting, but none of its actions fire. |
| Mute an Alert | `postAlertingRuleRuleIdAlertAlertIdMute` | Mute one alert of an alerting rule so that its actions stop firing while the alert stays active. |
| Preview a Managed Integrations Upgrade | `postFleetManagedIntegrationsUpgradeDryrun` | Preview upgrading several Fleet managed integrations without applying anything. Each result carries the current and proposed versions and any migration errors, plus the migrated policy when the dry run is clean. |
| Preview an Agentless Policy Upgrade (Deprecated) | `postFleetAgentlessPoliciesUpgradeDryrun` | Deprecated alias of Preview a Managed Integrations Upgrade. Use POST /api/fleet/managed_integrations/_upgrade/dryrun instead. |
| Preview Data View Reference Swap | `previewSwapDataViewsDefault` | List the saved objects that a data view reference swap would change, without applying anything. |
| Push a Case to a Connector | `pushCaseDefaultSpace` | Push a case to an external incident-management system through one of its connectors, creating or updating the incident there. Requires all privileges for the Cases and Actions features. |
| Query Roles | `postSecurityRoleQuery` | Search Kibana roles with a text query, paging and sorting, optionally including reserved roles. |
| Reassign an Agent | `postFleetAgentsAgentidReassign` | Reassign a single Elastic Agent to a different Fleet agent policy. Required privileges: fleet-agents-all. |
| Remove an OpAMP Collector | `postFleetAgentsAgentidRemoveCollector` | Remove one OpAMP collector from the Fleet agents list and mark it unenrolled. API keys are not invalidated, so the collector can reconnect on its own. Required privileges: fleet-agents-all. |
| Rename a Conversation Attachment | `patchAgentBuilderConversationsConversationIdAttachmentsAttachmentId` | Change only the description (display name) of a conversation attachment, leaving its content and version history untouched. |
| Request Agent Diagnostics | `postFleetAgentsAgentidRequestDiagnostics` | Request a diagnostics bundle from one Elastic Agent. Required privileges: fleet-agents-read. |
| Restore a Conversation Attachment | `postAgentBuilderConversationsConversationIdAttachmentsAttachmentIdRestore` | Bring a soft-deleted conversation attachment back into use so the agent can see it again. |
| Resume a Workflow Execution | `postWorkflowsExecutionsExecutionidResume` | Supply input to a workflow execution that is paused waiting for it, so the execution continues. The execution must be in status waiting_for_input; otherwise Kibana answers 409 naming the current status. |
| Resume a Workflow Step From an External Link | `getWorkflowsExecutionsExecutionidStepsStepidResumeExternal` | Resume a paused workflow step from the one-time link Kibana emails to a human reviewer. Authentication is the token issued when the step paused, not the API key, and the response is an HTML confirmation page. |
| Resync Streams | `resyncStreams` | Resync every stream so that the Elasticsearch assets backing them are brought up to date with their definitions. Requires the manage_stream privilege. |
| Review a Pending Package Policy Upgrade | `postFleetEpmPackagesPkgnameReviewUpgrade` | Accept, decline or reset a pending package policy upgrade for an integration package that contains deprecations. Required privileges: integrations-all and fleet-agent-policies-all. |
| Revoke or Delete an Enrollment API Key | `deleteFleetEnrollmentApiKeysByKeyid` | Revoke an enrollment API key by id, or remove its document entirely with forceDelete. Requires the fleet-agents-all privilege. |
| Rollback a Package to its Previous Version | `postFleetEpmPackagesPkgnameRollback` | Roll an integration package back to the version installed before its last upgrade. Required privileges: integrations-all and fleet-agent-policies-all. |
| Rollback an Agent | `postFleetAgentsAgentidRollback` | Roll one Elastic Agent back to the version it ran before its last upgrade. Required privileges: fleet-agents-all. |
| Rotate an Uninstall Token | `postFleetUninstallTokensAgentpolicyidRotate` | Rotate the uninstall token of a Fleet agent policy. Only applies to policies with tamper protection enabled. Required privileges: fleet-agents-all. |
| Rotate the Fleet Message Signing Key Pair | `postFleetMessageSigningServiceRotateKeyPair` | Rotate the key pair Fleet uses to sign messages sent to Elastic Agents. This is irreversible and requires every enrolled agent to be re-enrolled afterwards, so the call only proceeds when Acknowledge is true. Required privileges: fleet-agents-all, fleet-agent-policies-all and fleet-settings-all. |
| Run a Connector | `postActionsConnectorIdExecute` | Run a Kibana action connector to test it against the third-party system it talks to. The params object is specific to the connector type, for example documents for .index or message for .slack. Anything the connector really sends is sent for real, so test with harmless values. |
| Run a Workflow | `postWorkflowsWorkflowIdRun` | Execute an enabled workflow as a production run and return the identifier of the new execution. Disabled workflows are rejected with 400 "Workflow is disabled. Enable it to run it." |
| Schedule a Rule Backfill | `postAlertingRulesBackfillSchedule` | Schedule a manual backfill so that one or more alerting rules re-run over a past time range. The Kibana endpoint takes a top-level JSON array, so pass the array as a JSON string in Backfills, for example [{"rule_id":"...","ranges":[{"start":"2026-09-15T00:00:00.000Z","end":"2026-09-15T01:00:00.000Z"}]}]. |
| Schedule a Snooze for a Rule | `postAlertingRuleIdSnoozeSchedule` | Add a snooze schedule to an alerting rule. The rule keeps running but its actions do not fire during the snooze, which can be a single window or a recurring one. |
| Search Cases | `findCasesDefaultSpace` | Search Kibana cases with paging, sorting and filters on owner, status, severity, tags, category, assignees, reporters and free text. Requires read privileges for the Cases feature. |
| Search Tags | `getTags` | Return a paginated list of Kibana saved-object tags, optionally filtered by a search query over name and description. |
| Search Visualizations | `searchVisualizations` | Return a paginated list of saved visualizations, with optional text search and tag include/exclude filters. |
| Search Workflow Executions | `getWorkflowsWorkflowExecutions` | Search executions across every workflow in the space with a KQL query and filters on status, type, who ran it and start or finish time. Array filters take one repeated parameter per value in Kibana, so one value per filter can be sent per request. |
| Search Workflows | `getWorkflows` | Return a paginated list of the workflows in the current Kibana space, with optional free-text search and filters on enabled state, creator, tags and managed status. |
| Send an A2A Task to an Agent | `postAgentBuilderA2aAgentid` | Send an Agent2Agent (A2A) JSON-RPC request to an Agent Builder agent, for example method "message/send" with a user message. Returns the JSON-RPC envelope with the agent's reply, its taskId and contextId. |
| Set a Conversation Attachment Origin | `putAgentBuilderConversationsConversationIdAttachmentsAttachmentIdOrigin` | Point a conversation attachment at a saved object, so it is tracked by reference to that visualization or dashboard rather than as a standalone copy. |
| Set Case Configuration | `setCaseConfigurationDefaultSpace` | Create the case settings for an owning application, including its default connector, closure behaviour, custom fields, templates and observable types. Requires all privileges for the Cases feature. |
| Set the Default Data View | `setDefaultDataViewDefault` | Set the default data view for the current Kibana space. Kibana does not check that the identifier exists; pass null to clear the default. |
| Snooze an Alert | `postAlertingRuleRuleIdAlertAlertIdSnooze` | Snooze one alert of an alerting rule until a given time, or until one of the supplied conditions is met. |
| Start Entity Store Engines | `putSecurityEntityStoreStart` | Resume data processing on previously stopped Entity Store engines. Required privileges: securitySolution. |
| Start OAuth Authorization for a Connector | `getActionsConnectorConnectoridOauthStart` | Begin the OAuth 2.0 authorization code flow for a Kibana action connector. Kibana replies with a redirect to the identity provider's consent screen, so this is meant to be opened in a browser. Required privilege: actions:oauth. |
| Stop Entity Store Engines | `putSecurityEntityStoreStop` | Pause data processing on running Entity Store engines. Required privileges: securitySolution. |
| Submit External Input for a Paused Workflow Step | `postWorkflowsExecutionsExecutionidStepsStepidResumeExternal` | Submit the reviewer's form data to a paused workflow step so the execution continues. The body is the free-form input the step declared, and the response is an HTML confirmation page. Authorised by the resume token rather than the API key. |
| Swap Data View References | `swapDataViewsDefault` | Repoint every saved object that references one data view at another. Misuse can break many saved objects at once, so preview the change first with Preview Data View Reference Swap. |
| Sync Machine Learning Saved Objects | `mlSync` | Synchronize the Kibana saved objects for machine learning jobs and trained models in the current space. Kibana runs this automatically at start-up and periodically thereafter. Requires all privileges for the Machine Learning feature. |
| Test a Workflow | `postWorkflowsTest` | Run a workflow as a test execution, either an existing workflow by id or an ad-hoc YAML definition. Unlike Run a Workflow this also works while the workflow is disabled, and the execution is flagged as a test run. |
| Test a Workflow Step | `postWorkflowsStepTest` | Execute a single step of a workflow in isolation against a supplied context, and return the identifier of the resulting test execution. |
| Unarchive a Maintenance Window | `unarchiveMaintenanceWindow` | Bring an archived alerting maintenance window back into use. |
| Unenroll an Agent | `postFleetAgentsAgentidUnenroll` | Unenroll one Elastic Agent from Fleet, optionally forcing a hosted agent and revoking its API keys. Required privileges: fleet-agents-all. |
| Uninstall the Entity Store | `postSecurityEntityStoreUninstall` | Uninstall the Security Entity Store, removing the engines and their resources for the given entity types. Required privileges: securitySolution. |
| Unlink a Stream Attachment | `deleteStreamAttachment` | Detach a dashboard, alerting rule or SLO from a stream. Unlinking something that is not linked is a no-op. Requires the manage_stream privilege. |
| Unlink Entities | `postSecurityEntityStoreResolutionUnlink` | Remove one or more entities from their resolution group. The change becomes visible on the next index refresh. Required privileges: securitySolution and securitySolution-entity-analytics. |
| Unmute a Single Alert | `unmuteRuleAlert` | Unmute one specific alert of an alerting rule so that its actions fire again. |
| Unmute All Alerts of a Rule | `unmuteAllRuleAlerts` | Unmute every alert of an alerting rule so that its actions fire again. |
| Unmute an Alert | `postAlertingRuleRuleIdAlertAlertIdUnmute` | Unmute one alert of an alerting rule so its actions fire again. |
| Unsnooze an Alert | `postAlertingRuleRuleIdAlertAlertIdUnsnooze` | End the snooze on one alert of an alerting rule immediately. |
| Update a Case Comment | `updateCaseCommentDefaultSpace` | Replace the text of an existing case comment, or the details of an attached alert. The comment id and its current version are required. Requires all privileges for the Cases feature. |
| Update a Case Template | `updateCaseTemplateDefaultSpace` | Fully replace a case template's YAML definition. Requires all privileges for the Cases feature. |
| Update a Cloud Connector | `putFleetCloudConnectorsCloudconnectorid` | Update a Fleet cloud connector's name, account type or credentials. Required privileges: fleet-agent-policies-all or integrations-all. |
| Update a Connector | `putActionsConnectorId` | Update a Kibana action connector. The connector type cannot be changed; config and secrets are type-specific. |
| Update a Conversation Attachment | `putAgentBuilderConversationsConversationIdAttachmentsAttachmentId` | Replace the content of a conversation attachment, creating a new version of it. The data shape is validated per attachment type; a text attachment takes {"content": "..."}. |
| Update a Custom Integration | `putFleetEpmCustomIntegrationsPkgname` | Update the readme and categories of an existing custom integration package. Required privileges: fleet-settings-all and integrations-all. |
| Update a Dashboard | `updateDashboard` | Replace an existing dashboard by id. The whole dashboard definition is written, so send every attribute that should be kept. |
| Update a Data View | `updateDataViewDefault` | Update an existing data view. Only the properties supplied inside data_view are changed; everything else is left as stored. |
| Update a Fleet Server Host | `putFleetFleetServerHostsByItemid` | Update a Fleet Server host by id. Only the fields you supply are changed. Requires the fleet-settings-all privilege. |
| Update a Maintenance Window | `updateMaintenanceWindow` | Update an alerting maintenance window. Only the fields you send are changed. |
| Update a Managed Integration | `putFleetManagedIntegrationsPolicyid` | Update a Fleet managed (agentless) integration. This is a full replace: every optional field you omit is cleared or reset to its default. The package name is immutable. |
| Update a Managed Workflow | `putWorkflowsManagedWorkflowId` | Partially update a workflow that is managed by an Elastic package or solution. Same body as Update a Workflow, but routed through the managed-workflow endpoint. |
| Update a Package Policy | `putFleetPackagePoliciesPackagepolicyid` | Update a Fleet package policy by ID. Fields you omit are left unchanged. Required privileges: fleet-agent-policies-all and integrations-all. |
| Update a Proxy | `putFleetProxiesByItemid` | Update a Fleet proxy by id. Only the fields you supply are changed. Requires the fleet-settings-all privilege. |
| Update a Rule API Key | `updateRuleApiKey` | Regenerate the API key that an alerting rule runs under, so that it uses the privileges of the calling user from now on. |
| Update a Runtime Field | `updateRuntimeFieldDefault` | Update an existing runtime field of a data view. Only type and script can be changed. |
| Update a Space | `putSpacesSpaceId` | Update an existing Kibana space. The space ID cannot be changed. This is a full replace, so send every field you want to keep. |
| Update a Workflow | `putWorkflowsWorkflowId` | Partially update a workflow. Only the properties you send are changed, so this is the route used to enable or disable a workflow or to replace its YAML. |
| Update Agent Access Control | `putAgentBuilderAgentsIdAccessControl` | Replace the list of users an Agent Builder agent is shared with. The supplied list replaces the stored one; send an empty list to unshare the agent. |
| Update an Agent Binary Download Source | `putFleetAgentDownloadSourcesBySourceid` | Update an agent binary download source by id. Name and host are always required, so send the full desired state. Requires the fleet-settings-all privilege. |
| Update an Agent Builder Agent | `putAgentBuilderAgentsId` | Update an existing Agent Builder agent. Only the properties you send are changed; the agent id itself cannot be changed. |
| Update an Agent Builder Skill | `putAgentBuilderSkillsSkillid` | Update a user-defined Agent Builder skill. Only the properties you send are changed. Elastic-supplied read-only skills cannot be updated. |
| Update an Agent Builder Tool | `putAgentBuilderToolsToolid` | Update a user-created Agent Builder tool. Only the properties you send are changed; the tool's id and type cannot be changed. Built-in tools are read-only. |
| Update an Agent by ID | `putFleetAgentsAgentid` | Update the tags or user-provided metadata of a single enrolled Elastic Agent. Fields you omit are left unchanged. Required privileges: fleet-agents-all. |
| Update an Agent Policy | `putFleetAgentPoliciesByAgentpolicyid` | Update an agent policy by id. Name and namespace are always required, so send the full desired state. Requires the fleet-agent-policies-all privilege. |
| Update an Agentless Policy (Deprecated) | `putFleetAgentlessPoliciesPolicyid` | Deprecated alias of Update a Managed Integration. Use PUT /api/fleet/managed_integrations/{policyId} instead. Full-replace semantics: omitted optional fields are cleared. |
| Update an Alerting Rule | `updateRule` | Update an alerting rule. The rule type and consumer cannot be changed; name, tags, schedule, params, actions and throttle settings can. Every action entry needs its own frequency object. |
| Update an Entity | `putSecurityEntityStoreEntitiesEntitytype` | Update an entity record in the Security Entity Store. Only unprotected fields change unless Force is true. Required privileges: securitySolution. |
| Update an Output | `putFleetOutputsByOutputid` | Update a Fleet output by id. Only the fields you supply are changed; the type field selects which shape applies. Requires the fleet-settings-all privilege. |
| Update Case Configuration | `updateCaseConfigurationDefaultSpace` | Update the case settings of one owning application. The current version is required for optimistic concurrency. Requires all privileges for the Cases feature. |
| Update Cases | `updateCaseDefaultSpace` | Update one or more Kibana cases. Each entry needs the case id and its current version for optimistic concurrency. Requires all privileges for the Cases feature matching the case owner. |
| Update Conversation Access Control | `putAgentBuilderConversationsConversationIdAccessControl` | Set who may read and continue an Agent Builder conversation. The entries list replaces the stored one; send an empty list to unshare. Entries must be empty when the mode is public. |
| Update Data View Field Metadata | `updateFieldsMetadataDefault` | Set custom labels, custom descriptions and format overrides for individual fields of a data view. |
| Update Fleet Settings | `putFleetSettings` | Update the global Fleet settings, such as whether prerelease integrations are offered and whether unenrolled agents are deleted automatically. Only the fields you supply are changed. Requires the fleet-settings-all privilege. |
| Update Fleet Space Settings | `putFleetSpaceSettings` | Create or update the Fleet settings for the current Kibana space, for example the namespace prefixes integrations in this space may use. Requires the fleet-settings-all privilege. |
| Update Machine Learning Job Spaces | `mlUpdateJobsSpaces` | Add machine learning jobs to, or remove them from, the given Kibana spaces. |
| Update Package Settings | `putFleetEpmPackagesPkgname` | Update settings for an integration package, such as whether its package policies are kept up to date automatically and which namespaces may customize its index templates. Required privileges: integrations-all and fleet-agent-policies-all. |
| Update Package Version Settings | `putFleetEpmPackagesPkgnamePkgversion` | Update settings for one specific version of an integration package. Required privileges: integrations-all and fleet-agent-policies-all. |
| Update Stream Ingest Settings | `putStreamIngest` | Replace the ingest settings of an ingest stream. The whole ingest block is sent, so include every setting you want to keep. Requires the manage_stream privilege. |
| Update Stream Query Settings | `putStreamQueries` | Replace the ES\|QL query that defines a query stream, and optionally its field descriptions. Requires the manage_stream privilege. |
| Update the Entity Store | `putSecurityEntityStore` | Change the shared log-extraction configuration of an installed Security Entity Store. Required privileges: securitySolution. |
| Update Trained Model Spaces | `mlUpdateTrainedModelsSpaces` | Add machine learning trained models to, or remove them from, the given Kibana spaces. |
| Upgrade an Agent | `postFleetAgentsAgentidUpgrade` | Upgrade one Elastic Agent to a newer version. Required privileges: fleet-agents-all. |
| Upgrade Package Policies | `postFleetPackagePoliciesUpgrade` | Upgrade the named Fleet package policies to the latest version of their integration package. Required privileges: fleet-agent-policies-all and integrations-all. |
| Upsert a Links Library Item | `putLinksId` | Replace the full state of a links library item, or create it at the given ID. Partial updates are not supported: read the item first, change what you need and send the whole object back. |
| Upsert a Markdown Library Item | `putMarkdownsId` | Replace the full state of a markdown library item, or create it at the given ID. Partial updates are not supported. |
| Upsert a Tag | `putTagsId` | Update a Kibana saved-object tag, or create it at the given ID when it does not exist. |
| Upsert a Visualization | `upsertVisualization` | Replace the full state of a saved visualization, or create it at the given ID. Partial updates are not supported. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Alert Active | `alert.active` | Fired by a Kibana alerting rule each time its conditions are met (the rule's default action group, for example 'query matched' on an Elasticsearch query rule). fastn subscribes by creating a .webhook action connector pointing at the fastn trigger URL and an alerting rule bound to it. NOTE: the Kibana webhook body is composed by the rule's action params, so the payload shape below is the body this subscription configures, not a fixed vendor contract. |
| Alert Recovered | `alert.recovered` | Fired by a Kibana alerting rule when a previously active alert returns to normal (the 'recovered' action group). fastn subscribes by adding a second action on the same rule bound to the recovered group. NOTE: the payload is composed by the rule's action params, so the shape below is what this subscription configures rather than a fixed vendor contract. |
