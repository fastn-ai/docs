---
description: "LaunchDarkly feature management platform."
hidden: true
---

# LaunchDarkly

<img src="../../.gitbook/assets/connectors/lg/launchdarkly.png" alt="LaunchDarkly logo">

LaunchDarkly feature management platform. Wraps the LaunchDarkly REST API v2: projects, environments, feature flags, segments, metrics, experiments, teams, account members, custom roles, access tokens, webhooks, audit log, code references, contexts, approvals, scheduled changes, workflows and AI Configs.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [launchdarkly.com](https://launchdarkly.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Slug** | `launchdarkly` |

## Use it

Add LaunchDarkly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.launchdarkly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Flag Follower | `putFlagFollower` | Make an account member a follower of a feature flag in one environment, so they are notified of changes. Members with the Reader role can only add themselves. Returns 204 on success. |
| Add Member To Teams | `addMemberToTeams` | Add a single LaunchDarkly account member to one or more teams in a single call. Returns the updated member including their team memberships. |
| Add Multiple Members To Team | `addTeamMembers` | Add several existing account members to a LaunchDarkly team at once by uploading their email addresses as CSV rows. Supply the CSV body as a single string whose first line is the header 'email' followed by one address per line. Addresses that do not belong to a member of your LaunchDarkly account are rejected. |
| Add Restricted AI Models | `postRestrictedModels` | Add AI model config keys to the project's restricted list. Pass global model keys such as DeepSeek.deepseek-chat; a key already in use returns 400 "all specified model config keys are already in use". |
| Apply Approval Request | `postApprovalRequestApply` | Apply an approved approval request, executing its instructions against the target resource. Returns the approval request with status completed. |
| Apply Approval Request For Flag | `postApprovalRequestApplyForFlag` | Apply an approved feature flag approval request, executing its instructions against the flag in that environment. Returns the approval request with status completed. |
| Associate Insights Repositories With Projects | `associateInsightsRepositories` | Associates connected source-code repositories with LaunchDarkly projects so Engineering Insights can attribute pull requests and deployments. Send the full list of repository-to-project mappings. Requires a LaunchDarkly plan that includes Engineering Insights. |
| Complete Warehouse Destination Setup | `postCompleteWarehouseDestinationSetup` | Finish setting up a warehouse Data Export destination after the generated setup script has been run in the warehouse. LaunchDarkly opens a live connection to the warehouse, so this only succeeds against a real, already-provisioned warehouse. kind is snowflake-v2, bigquery, clickhouse, redshift or databricks. |
| Copy Feature Flag Settings | `copyFeatureFlag` | Copy a flag's targeting configuration from a source environment to a target environment within the same project. Use Included Actions or Excluded Actions to copy only part of the configuration. |
| Create Access Token | `createAccessToken` | Create a new LaunchDarkly API access token. The response contains the secret token value exactly once, so store it securely straight away. Choose either a base role, a list of custom role IDs, or an inline policy. |

<details>

<summary>See 393 more actions</summary>

* **Create Adaptive Trigger** `createAdaptiveTrigger`: Creates a LaunchDarkly adaptive trigger that applies flag targeting instructions automatically when the named observability alert fires. Returns the created trigger with its ID.
* **Create Agent Graph** `postAgentGraph`: Create an agent graph. If edges or rootConfigKey is supplied, both must be. Sends the required LD-API-Version: beta header.
* **Create Agent Optimization** `postAgentOptimization`: Create an agent optimization for an AI Config. Requires key, aiConfigKey, maxAttempts and judgeModel.
* **Create Agent Optimization Result** `postAgentOptimizationResult`: Record an agent optimization result. runId must be a UUID; LaunchDarkly returns 400 "can't decode JSON body" for any other format.
* **Create Agent Skill** `postAgentSkill`: Create an agent skill from verbatim SKILL.md markdown. Paid entitlement; without it LaunchDarkly returns 403 "Plan does not allow this operation".
* **Create AI Config** `postAIConfig`: Create a new AI Config in a LaunchDarkly project. Requires key and name; mode is one of agent, completion, judge.
* **Create AI Config Variation** `postAIConfigVariation`: Create a variation of an AI Config: messages, model config, tools, skills or agent instructions.
* **Create AI Model Config** `postModelConfig`: Create a project-level AI model config. Requires key, name and id (the provider's model identifier).
* **Create AI Tool** `postAITool`: Create an AI tool. schema is a JSON Schema describing the tool's parameters for LLM consumption.
* **Create Announcement** `createAnnouncement`: Create an in-app announcement banner that LaunchDarkly shows to everyone in your account between the start and end times you choose.
* **Create Approval Request** `postApprovalRequest`: Create an approval request for a flag-level, AI config or segment change. Resource Id is the LaunchDarkly resource specifier; for a flag it must span every environment with a star, for example proj/my-proj:env/*:flag/my-flag, and LaunchDarkly rejects a single named environment with 400. Flag instructions are limited to addVariation, removeVariation, updateVariation and updateDefaultVariation; environment-scoped changes such as turnFlagOn go through Create Approval Request For Flag instead.
* **Create Approval Request For Flag** `postApprovalRequestForFlag`: Request approval for a change to a feature flag in one environment. Instructions is an array of semantic patch instructions such as [{"kind":"turnFlagOn"}]. Supply Execution Date to schedule the change for a future time, and Operating On Id when the instructions edit or delete an existing scheduled change.
* **Create Big Segment Export** `createBigSegmentExport`: Start an export of a big (unbounded) segment's members to a CSV file. Returns 200 with an empty body; poll Get Big Segment Export with the export id from the segment's _unboundedMetadata or the Location header.
* **Create Big Segment Import** `createBigSegmentImport`: Import member keys into a big (unbounded) segment from CSV content. Supply the CSV text in CSV Content (one key per line). Mode is merge or replace. Returns 204 on success.
* **Create Big Segment Store Integration** `createBigSegmentStoreIntegration`: Beta. Create a persistent store (big segment store) integration for a project/environment. integrationKey is redis or dynamodb. For redis, config requires host and port, and port MUST be sent as a STRING - a numeric port is rejected with 400 "Unable to read JSON".
* **Create Code Reference Extinction** `postExtinction`: Record that a flag's last code reference disappeared from a branch. The LaunchDarkly endpoint accepts a list of extinction events; this action submits the single event described by its inputs. Returns 200 with an empty body.
* **Create Code Reference Repository** `postRepository`: Connect a source repository to LaunchDarkly code references. Type defaults to custom and Default Branch defaults to main. Commit Url Template and Hunk Url Template build the deep links shown next to each code reference.
* **Create Custom Role** `createCustomRole`: Create a custom role in LaunchDarkly from a set of policy statements. Each statement names an effect, the resources it covers and the actions it allows or denies.
* **Create Data Export Destination** `postDestination`: Create a Data Export destination in a project/environment. kind is one of google-pubsub, kinesis, mparticle, segment, azure-event-hubs, snowflake-v2, databricks, bigquery, redshift. config holds the kind-specific fields.
* **Create Environment** `createEnvironment`: Create a new environment inside a LaunchDarkly project. Name, key and color are required. Returns the new environment including its freshly generated SDK key and mobile key.
* **Create Experiment** `createExperiment`: Creates a LaunchDarkly experiment in a project and environment. The iteration object carries the hypothesis, the metrics to analyse, the treatments with their traffic allocation and the flags under test. Returns the created experiment with its draft iteration.
* **Create Experiment Iteration** `createExperimentIteration`: Creates a new draft iteration for an existing LaunchDarkly experiment. Deprecated by LaunchDarkly in favour of the createIteration semantic patch instruction on Patch Experiment, but still live. Returns the created draft iteration.
* **Create Feature Flag** `createFeatureFlag`: Create a feature flag in a project. If no variations are supplied LaunchDarkly creates a boolean flag with true and false variations. Optionally clone an existing flag by supplying its key.
* **Create Flag Copy Approval Request** `postFlagCopyConfigApprovalRequest`: Request approval to copy a feature flag's configuration from a source environment into the target environment named in Environment Key. Source is an object such as {"key":"test","currentVersion":12}. Optionally narrow the copy with Included Actions or Excluded Actions.
* **Create Flag Import Configuration** `createFlagImportConfiguration`: Beta. Create a flag import configuration for a project and integration key. For split, config requires workspaceApiKey, workspaceId, environmentId and ldApiKey. Note the API rejects an "on" field here.
* **Create Flag Link** `createFlagLink`: Attach a link from a feature flag to an external resource such as a Jira ticket or a design doc. Supply Deep Link for a plain URL link, or Integration Key plus Metadata for an integration-backed link. Beta endpoint.
* **Create Flag Trigger** `createTriggerWorkflow`: Create a flag trigger: a unique URL that, when called, performs the given instruction on the flag in that environment. Use generic-trigger as the Integration Key for integrations LaunchDarkly does not name explicitly. The response contains the secret triggerURL.
* **Create Holdout** `postHoldout`: Create a holdout experiment in a project and environment. A holdout withholds a share of traffic from every experiment so their combined impact can be measured. Requires a flag created with Purpose set to holdout.
* **Create Insight Group** `createInsightGroup`: Creates a LaunchDarkly Engineering Insights group over a project, environment and optional set of applications so their delivery scores are tracked together. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Create Insights Deployment Event** `createInsightsDeploymentEvent`: Reports a deployment event to LaunchDarkly Engineering Insights so it can track deployment frequency and lead time for an application version. Returns 201 with no body. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Create Integration Audit Log Subscription** `createSubscription`: Create an audit log subscription for an integration. config carries the integration-specific fields (for msteams and mattermost that is a single url). statements is an array of policy statements scoping which resources the subscription reports on.
* **Create Integration Configuration** `createIntegrationConfiguration`: Beta. Create an integration configuration for an integration key. configValues holds the integration's formVariables (for vercel-native: accessToken and installationId). Returns the created configuration with secrets masked.
* **Create Integration Delivery Configuration** `createIntegrationDeliveryConfiguration`: Beta. Create an integration delivery (featureStore) configuration in a project/environment. Valid integration keys are the ones whose manifest declares the featureStore capability, e.g. cloudflare (accountId, apiToken, namespaceId), fastly (storeId, apiKey), vercel, vercel-native. config carries those fields.
* **Create IP Allowlist Entry** `createIpAllowlistEntry`: Add an IP address or CIDR block to your LaunchDarkly account's IP allowlist. Reserved and private address ranges are rejected. Adding an entry has no effect until session or API token allowlisting is enabled. This endpoint is in beta.
* **Create Layer** `createLayer`: Creates an experiment layer in a LaunchDarkly project so that experiments placed in it never share the same traffic. Returns the created layer.
* **Create Metric** `createMetric`: Create a metric in a LaunchDarkly project so experiments and guarded rollouts can measure it. Custom metrics need an event key; click and pageview metrics need target URLs and, for clicks, a CSS selector.
* **Create Metric Group** `createMetricGroup`: Create a metric group in a LaunchDarkly project so an experiment can analyse several metrics together. Use kind 'funnel' for an ordered sequence of steps, or 'standard' for an unordered set.
* **Create OAuth 2.0 Client** `createOauthClient`: Register a new LaunchDarkly OAuth 2.0 client application so other services can authorize against your LaunchDarkly account. The client secret is returned exactly once in this response, so store it securely straight away.
* **Create Or Update Context Kind** `putContextKind`: Create a context kind in a project, or update an existing one. Archiving a context kind makes it unavailable for targeting.
* **Create Project** `createProject`: Create a new LaunchDarkly project. A project groups feature flags, segments and environments. If no environments are supplied, LaunchDarkly creates the default Test and Production environments.
* **Create Prompt Snippet** `postPromptSnippet`: Create a reusable prompt snippet. Requires key, name and text.
* **Create Relay Proxy Configuration** `postRelayAutoConfig`: Create a Relay Proxy auto-configuration. policy is an array of statements such as [{"effect":"allow","resources":["proj/*:env/*"],"actions":["*"]}]. The full key is returned only in this response.
* **Create Release For Flag** `createReleaseForFlag`: Attach a feature flag to a release pipeline, starting a release. Release Pipeline Key names the pipeline; Release Variation Id optionally pins the variation rolled out in every phase. Returns the release with its phases.
* **Create Release Pipeline** `postReleasePipeline`: Create a release pipeline in a project. Phases is an ordered array, each phase naming the environments a flag rolls out to and its audience configuration, for example [{"name":"Phase 1","audiences":[{"environmentKey":"test","name":"Everyone"}]}]. Set Is Project Default to make it the project's default pipeline.
* **Create Release Policy** `postReleasePolicy`: Create a release policy in a project. Release Method must be progressive-release or guarded-release with the matching config object; immediate-release appears in the schema but LaunchDarkly rejects it with 400 "Invalid release method". Scope narrows the policy to given environmentKeys and/or flagTagKeys. A progressive config needs rolloutContextKindKey and an ordered stages array of {allocation, durationMillis}. Beta endpoint: the LD-API-Version beta header is sent automatically.
* **Create Scheduled Change** `postFlagConfigScheduledChanges`: Schedule a future change to a feature flag in one environment. Execution Date is Unix epoch milliseconds and must be in the future. Instructions is an array of semantic patch instructions such as [{"kind":"turnFlagOn"}]. Set Ignore Conflicts to true to accept instructions that clash with existing scheduled changes.
* **Create SDK Key** `postSdkKey`: Beta. Create an SDK key in an environment. key and name are required; kind is sdk (server-side, the default) or mobile. The secret value is returned in this response.
* **Create Segment** `postSegment`: Create a segment in a project and environment. Set Unbounded to true to create a big segment (requires a paid plan); leave it false for a standard segment.
* **Create Team** `createTeam`: Create a new team in the LaunchDarkly account. Key and name are required. You may seed the team with member IDs, custom role keys and permission grants at creation time.
* **Create View** `createView`: Creates a view in a LaunchDarkly project. The key is lowercased on creation. LaunchDarkly beta endpoint; sends the LD-API-Version: beta header.
* **Create Webhook** `createWebhook`: Register a webhook that posts LaunchDarkly audit log events to a remote URL. Use statements to scope which resources trigger it; omit statements to receive events for every resource. Returns the created webhook including its id and signing secret.
* **Create Workflow** `postWorkflow`: Create a workflow on a feature flag in one environment. Stages is an array of stage objects, each with an optional execution condition and a set of semantic patch action instructions, for example [{"name":"Stage 1","action":{"instructions":[{"kind":"turnFlagOn"}]}}]. Pass Template Key to start from a workflow template, or Dry Run to validate without saving.
* **Create Workflow Template** `createWorkflowTemplate`: Create a reusable workflow template. Either supply Stages directly, or point at an existing workflow with Workflow Id plus Project Key, Environment Key and Flag Key to capture its stages as a template.
* **Delete Access Token** `deleteAccessToken`: Permanently revoke a LaunchDarkly API access token by ID. Any integration still using the secret stops working immediately. Returns an empty body on success.
* **Delete Account Member** `deleteAccountMember`: Permanently remove an account member from your LaunchDarkly account. The member immediately loses all access. The account owner cannot be deleted. Returns an empty body on success.
* **Delete Adaptive Trigger** `deleteAdaptiveTrigger`: Permanently deletes a LaunchDarkly adaptive trigger. The flag and the observability alert are not affected. Returns 204 with no body.
* **Delete Agent Graph** `deleteAgentGraph`: Delete an agent graph by key. Returns 204 No Content. Sends the required LD-API-Version: beta header.
* **Delete Agent Optimization** `deleteAgentOptimization`: Delete an agent optimization by key. Returns 204 No Content.
* **Delete Agent Optimization Run** `deleteAgentOptimizationRun`: Delete one run of an agent optimization by run id. Returns 204 No Content. Sends the required LD-API-Version: beta header.
* **Delete Agent Skill** `deleteAgentSkill`: Delete an agent skill by key. Paid entitlement; without it LaunchDarkly returns 403 "Plan does not allow this operation".
* **Delete AI Config** `deleteAIConfig`: Delete an AI Config by key. Returns 204 No Content on success.
* **Delete AI Config Variation** `deleteAIConfigVariation`: Delete an AI Config variation by key. Returns 204 No Content.
* **Delete AI Model Config** `deleteModelConfig`: Delete a project-level AI model config by key. Returns 204 No Content.
* **Delete AI Tool** `deleteAITool`: Delete an AI tool by key. Returns 204 No Content.
* **Delete Announcement** `deleteAnnouncement`: Permanently delete an in-app announcement by ID. It stops showing to everyone in your LaunchDarkly account immediately. Returns an empty body on success.
* **Delete Application** `deleteApplication`: Beta. Delete an application by its key. Returns 204 with an empty body.
* **Delete Application Version** `deleteApplicationVersion`: Beta. Delete one version of an application. Returns 204 with an empty body.
* **Delete Approval Request** `deleteApprovalRequest`: Delete an approval request by its id. The pending change is discarded and never applied. Returns 204 No Content on success.
* **Delete Approval Request For Flag** `deleteApprovalRequestForFlag`: Delete a feature flag approval request by its id. The pending flag change is discarded. Returns 204 No Content on success.
* **Delete Big Segment Store Integration** `deleteBigSegmentStoreIntegration`: Beta. Delete a persistent store integration by project, environment, integration key and integration id. Returns 204 with an empty body.
* **Delete Code Reference Branch** `deleteBranches`: Queue a task that removes one branch and its code references from a repository. The LaunchDarkly endpoint accepts a list of branch names; this action submits the single branch named in Branch. Returns 200 with an empty body.
* **Delete Code Reference Repository** `deleteRepository`: Delete a code reference repository and every code reference and branch recorded for it. Returns 204 No Content on success.
* **Delete Context Instances** `deleteContextInstances`: Delete all context instances with the given context instance id from an environment. Returns 204 on success.
* **Delete Custom Role** `deleteCustomRole`: Permanently delete a LaunchDarkly custom role by its key. Members and teams that held the role lose the permissions it granted. Returns an empty body on success.
* **Delete Data Export Destination** `deleteDestination`: Delete a Data Export destination by project key, environment key and destination id. Returns 204 with an empty body.
* **Delete Environment** `deleteEnvironment`: Permanently delete an environment from a LaunchDarkly project, including all of its flag targeting configuration. This cannot be undone. Returns 204 No Content on success.
* **Delete Feature Flag** `deleteFeatureFlag`: Permanently delete a feature flag and its targeting configuration in every environment. This cannot be undone; archive the flag instead if you may need it again. Returns 204 No Content on success.
* **Delete Flag Import Configuration** `deleteFlagImportConfiguration`: Beta. Delete a flag import configuration by project key, integration key and integration id. Returns 204 with an empty body.
* **Delete Flag Link** `deleteFlagLink`: Delete a flag link by its id or key. Returns 204 with no content on success. Beta endpoint.
* **Delete Flag Trigger** `deleteTriggerWorkflow`: Delete a flag trigger by id. Returns 204 with no content on success.
* **Delete Insight Group** `deleteInsightGroup`: Permanently deletes a LaunchDarkly Engineering Insights group. The underlying project, environment and applications are not affected. Returns 204 with no body. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Delete Integration Audit Log Subscription** `deleteSubscription`: Delete an audit log subscription by integration key and subscription id. Returns 204 with an empty body.
* **Delete Integration Configuration** `deleteIntegrationConfiguration`: Beta. Delete an integration configuration by its id. Returns 204 with an empty body.
* **Delete Integration Delivery Configuration** `deleteIntegrationDeliveryConfiguration`: Beta. Delete an integration delivery (featureStore) configuration by project, environment, integration key and id. Returns 204 with an empty body.
* **Delete IP Allowlist Entry** `deleteIpAllowlistEntry`: Remove an IP address or CIDR block from your LaunchDarkly account's IP allowlist. If allowlisting is enabled, anyone at that address immediately loses access. This endpoint is in beta.
* **Delete Metric** `deleteMetric`: Permanently delete a LaunchDarkly metric by project and metric key. A metric that is attached to a running experiment cannot be deleted. Returns an empty body on success.
* **Delete Metric Group** `deleteMetricGroup`: Permanently delete a LaunchDarkly metric group by project and metric group key. The metrics themselves are not deleted, only the grouping. Returns an empty body on success.
* **Delete OAuth 2.0 Client** `deleteOauthClient`: Permanently delete a LaunchDarkly OAuth 2.0 client application by its client ID. Any authorization flow that relies on it stops working. Returns an empty body on success.
* **Delete Project** `deleteProject`: Permanently delete a LaunchDarkly project and every environment, feature flag and segment it contains. This cannot be undone. Returns 204 No Content on success.
* **Delete Prompt Snippet** `deletePromptSnippet`: Delete a prompt snippet by key. Returns 204 No Content.
* **Delete Relay Proxy Configuration** `deleteRelayAutoConfig`: Delete a Relay Proxy auto-configuration by id. Returns 204 with an empty body.
* **Delete Release For Flag** `deleteReleaseByFlagKey`: Detach a feature flag from its release pipeline, removing the release. The flag's current targeting is left as it is. Returns 204 No Content on success.
* **Delete Release Pipeline** `deleteReleasePipeline`: Delete a release pipeline from a project. Flags currently released through it stop progressing. Returns 204 No Content on success.
* **Delete Release Policy** `deleteReleasePolicy`: Delete a release policy from a project. Flags previously matched by it fall through to the next policy in rank order. Beta endpoint: the LD-API-Version beta header is sent automatically. Returns 204 No Content on success.
* **Delete Scheduled Change** `deleteFlagConfigScheduledChanges`: Cancel a scheduled change by its id so it never executes. Returns 204 No Content on success.
* **Delete SDK Key** `deleteSdkKeyByKey`: Beta. Delete an SDK key by its user-defined key. Returns 204 with an empty body. The environment's default SDK key cannot be deleted.
* **Delete Segment** `deleteSegment`: Delete a segment from a project and environment. Returns 204 with no content on success.
* **Delete Team** `deleteTeam`: Permanently delete a LaunchDarkly team by its key. Members of the team are not deleted, but they lose any permissions the team granted. Returns an empty body on success.
* **Delete View** `deleteView`: Permanently deletes a LaunchDarkly view. Resources linked to the view are not deleted, only the view itself. Returns 204 with no body. LaunchDarkly beta endpoint; sends the LD-API-Version: beta header.
* **Delete Webhook** `deleteWebhook`: Permanently delete a LaunchDarkly webhook by its id. LaunchDarkly stops posting events to its destination URL. Returns 204 No Content on success.
* **Delete Workflow** `deleteWorkflow`: Delete a workflow from a feature flag. Any stages that have not executed yet are cancelled. Returns 204 No Content on success.
* **Delete Workflow Template** `deleteWorkflowTemplate`: Delete a workflow template by its key. Workflows already created from it are unaffected. Returns 204 No Content on success.
* **Disable Adaptive Trigger** `disableAdaptiveTrigger`: Disables a LaunchDarkly adaptive trigger so that it no longer acts on its flag when the linked observability alert fires. Returns 204 with no body.
* **Enable Adaptive Trigger** `enableAdaptiveTrigger`: Enables a LaunchDarkly adaptive trigger so that it acts on its flag when the linked observability alert fires. Returns 204 with no body.
* **Evaluate Flags For Context Instance** `evaluateContextInstance`: Evaluate every flag in an environment for a single context instance and return the variation each flag serves it. Supply the context instance as a JSON object string, for example {"kind":"user","key":"user-1"}.
* **Find Users** `searchUsers`: Full-text search the legacy users in a LaunchDarkly project and environment by name, email or key, with optional attribute filters. This endpoint is deprecated in favour of the contexts API.
* **Generate Data Export Trust Policy** `postGenerateTrustPolicy`: Generate the AWS IAM trust policy that lets LaunchDarkly Data Export assume a role in your AWS account for a given project and environment.
* **Generate Project Environment Warehouse Destination Key Pair** `postGenerateProjectEnvWarehouseDestinationKeyPair`: Generate an RSA key pair a Snowflake warehouse Data Export destination uses to authenticate, scoped to one project and environment. Returns public_key and public_key_pkcs8.
* **Generate Snowflake Destination Key Pair** `postGenerateWarehouseDestinationKeyPair`: Legacy account-level endpoint that generates a key pair for Snowflake Data Export authentication. LaunchDarkly's own spec declares no parameters and no body, yet the handler always answers 404 "project is not found". Use Generate Project Environment Warehouse Destination Key Pair instead.
* **Generate Warehouse Destination Setup Script** `postGenerateWarehouseDestinationSetupScript`: Generate the SQL/IAM setup script you run in your warehouse before completing a warehouse Data Export destination. kind is snowflake-v2, redshift or clickhouse. Returns script plus the public keys and, for Redshift, the IAM policies.
* **Get Access Token** `getAccessToken`: Fetch the metadata of a single LaunchDarkly API access token by ID, including its role, owner, last-used time and expiry. The secret token value is only returned when the token is first created.
* **Get Account Member** `getAccountMember`: Fetch a single LaunchDarkly account member by their member ID, including their base role, custom roles, team memberships and invitation status.
* **Get Adaptive Trigger** `getAdaptiveTrigger`: Retrieves a single LaunchDarkly adaptive trigger by ID, including the observability alert that fires it, the targeting instructions it applies and whether it is enabled.
* **Get Agent Graph** `getAgentGraph`: Get one agent graph by key, including its root config and edges. Sends the required LD-API-Version: beta header.
* **Get Agent Optimization** `getAgentOptimization`: Get a single agent optimization by key, including its model choices, judges and acceptance statements.
* **Get Agent Skill** `getAgentSkill`: Get one agent skill by key, including its SKILL.md markdown. Paid entitlement; without it LaunchDarkly returns 403 "Plan does not allow this operation".
* **Get AI Config** `getAIConfig`: Get a single AI Config by key from a LaunchDarkly project.
* **Get AI Config Metrics** `getAIConfigMetrics`: Get aggregated AI Config metrics (tokens, generation counts, cost, latency, satisfaction) for a time window in one environment. from/to are milliseconds since epoch, at most 100 days apart.
* **Get AI Config Metrics By Variation** `getAIConfigMetricsByVariation`: Get AI Config metrics broken down per variation for a time window. LaunchDarkly returns a bare JSON array, wrapped here under items.
* **Get AI Config Quick Stats** `getAIConfigQuickStats`: Get AI Config quick stats for one environment: active configs, active experiments, 7-day average satisfaction and month-to-date spend.
* **Get AI Config Targeting** `getAIConfigTargeting`: Show an AI Config's targeting rules across all environments.
* **Get AI Config Variation** `getAIConfigVariation`: Get all versions of one AI Config variation by key. Returns items and totalCount.
* **Get AI Model Config** `getModelConfig`: Get one AI model config by key at a specific version. version is required because LaunchDarkly rejects an empty value for a typed query param; pass the version you want.
* **Get AI Runs Usage** `getAIRunsUsage`: Get AI runs usage for the LaunchDarkly account. Returns a time series of AI run counts, month-to-date at daily granularity.
* **Get AI Tool** `getAITool`: Get a single AI tool by key, including its JSON Schema and custom parameters.
* **Get All Holdouts** `getAllHoldouts`: List the holdout experiments in a project and environment.
* **Get All SDK Versions Usage** `getSdkAllVersions`: Get usage details for all SDK versions in use across the account.
* **Get API Root** `getApiRoot`: Get the LaunchDarkly API root resource, which returns the hypermedia links to every top-level collection the credential can reach. Useful as a cheap connectivity check.
* **Get API Versions** `getApiVersions`: Get LaunchDarkly REST API version information: the list of valid API versions, the latest version, the version this credential currently uses and the current beta version.
* **Get Application** `getApplication`: Beta. Get one application by its key. expand accepts flags.
* **Get Approval Request** `getApprovalRequest`: Get a single approval request by its id, including its review status, the reviews recorded so far, the instructions it will apply and any conflicts.
* **Get Approval Request For Flag** `getApprovalForFlag`: Get one approval request raised against a feature flag in an environment, including its review status, recorded reviews and pending instructions.
* **Get Approval Request Settings** `getApprovalRequestSettings`: Get the approval request settings configured for one resource kind in a project. Resource Kind must be segment or aiconfig; flag is not exposed here, read feature flag approval settings from the environment's own approvalSettings instead. Environment Key and Resource Kind are both required because LaunchDarkly rejects an empty value for either, with 400 "Invalid environment key" and 400 "Invalid resource kind". Beta endpoint: the LD-API-Version beta header is sent automatically.
* **Get Audit Log Entry** `getAuditLogEntry`: Fetch a single LaunchDarkly audit log entry by ID, including who made the change, what was changed and the before and after versions of the resource.
* **Get Audit Log Entry Counts** `getAuditLogEntryCounts`: Return audit log activity counted into evenly spaced time buckets across a date range, so you can chart how much changed and when. After is required. At least one policy statement is required; an empty list is rejected.
* **Get Big Segment Export** `getBigSegmentExport`: Get the status and download link of a big (unbounded) segment export job.
* **Get Big Segment Import** `getBigSegmentImport`: Get the status of a big (unbounded) segment import job, including the mode used and the files processed.
* **Get Big Segment Membership For Context** `getSegmentMembershipForContext`: Check whether a context key is individually included in or excluded from a big (unbounded) segment.
* **Get Big Segment Membership For User** `getSegmentMembershipForUser`: Check whether a user key is individually included in or excluded from a big (unbounded) segment.
* **Get Big Segment Store Integration** `getBigSegmentStoreIntegration`: Beta. Get one persistent store integration. integrationKey is redis or dynamodb.
* **Get Caller Identity** `getCallerIdentity`: Identify the credential making the request. Returns the LaunchDarkly account id, the token kind and name, the member id behind a personal token, and the scopes the token carries. Useful for verifying a connection and for discovering the account id.
* **Get Code Reference Branch** `getBranch`: Get one branch of a code reference repository, including every flag reference found on it. Branch must be URL encoded. Filter the references to one project or flag.
* **Get Code Reference Repository** `getRepository`: Get one code reference repository by name, including its URL templates, default branch, enabled state and known branches.
* **Get Code Reference Statistics For Project** `getStatistics`: Get per-flag code reference counts for a project: for each flag, how many references exist in each connected repository. Narrow the result to one flag with Flag Key.
* **Get Code Reference Statistics Links** `getRootStatistic`: Get the hypermedia links to the code reference statistics for each project in the account. Follow a project link to see which repositories reference its flags.
* **Get Context Attribute Names** `getContextAttributeNames`: List the context attribute names LaunchDarkly has seen in an environment. Filter accepts only a kind filter with the equals operator, for example kind equals "user".
* **Get Context Attribute Values** `getContextAttributeValues`: List the values LaunchDarkly has seen for one context attribute in an environment. Filter accepts only a kind filter with the equals operator.
* **Get Context Instances** `getContextInstances`: Get the context instances that include a given context instance id. The id is the canonical key of a context, for example user-key-123 or a multi-context canonical key.
* **Get Context Kinds** `getContextKindsByProjectKey`: List the context kinds defined in a project. Set Expand to environmentObservations or createdFrom to include extra detail.
* **Get Contexts** `getContexts`: Get the contexts LaunchDarkly has seen in an environment for one context kind and key.
* **Get Contexts Clientside Usage** `getContextsClientsideUsage`: Get client-side contexts usage for the account. Returns a time series of client-side context counts, month-to-date at daily granularity.
* **Get Contexts Serverside Usage** `getContextsServersideUsage`: Get server-side contexts usage for the account. Returns a time series of server-side context counts, month-to-date at daily granularity.
* **Get Contexts Total Usage** `getContextsTotalUsage`: Get total contexts usage across client-side and server-side for the account. Returns a time series, month-to-date at daily granularity.
* **Get Custom Role** `getCustomRole`: Fetch a single LaunchDarkly custom role by its key or ID, including its policy statements, base permissions and what it is assigned to.
* **Get Data Export Destination** `getDestination`: Get a single Data Export destination by project key, environment key and destination id.
* **Get Data Export Events Usage** `getDataExportEventsUsage`: Get Data Export events usage for the account. Returns a time series of exported event counts, month-to-date at daily granularity.
* **Get Deployment Frequency Chart** `getDeploymentFrequencyChart`: Returns the LaunchDarkly Engineering Insights deployment-frequency chart series for a project and environment over a time window. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Get Environment** `getEnvironment`: Get a single environment in a LaunchDarkly project by its key, including the environment SDK key, mobile key, colour, TTL and approval settings.
* **Get Evaluations Usage** `getEvaluationsUsage`: Get flag evaluation usage for one feature flag in one environment. Returns a time series of evaluation counts, defaulting to the last 30 days.
* **Get Events Usage** `getEventsUsage`: Get received or published events usage for the account. Returns a time series of event counts for the last 24 hours by default.
* **Get Experiment** `getExperiment`: Retrieves a single LaunchDarkly experiment by key within a project and environment, including its current iteration, treatments, metrics and analysis configuration.
* **Get Experimentation Events Usage** `getExperimentationEventsUsage`: Get experimentation events usage for the account. Returns a time series of experimentation event counts, month-to-date at daily granularity.
* **Get Experimentation Keys Usage** `getExperimentationKeysUsage`: Get experimentation keys usage for the account. Returns a time series of experimentation key counts, month-to-date at daily granularity.
* **Get Experimentation Settings** `getExperimentationSettings`: Retrieves the experimentation settings for a LaunchDarkly project, listing every randomization unit allowed for experiments in that project and which one is the default.
* **Get Expiring Context Targets For Flag** `getExpiringContextTargets`: List the scheduled removal dates for individual context targets on a feature flag in one environment.
* **Get Expiring Flag Targets For User** `getExpiringFlagsForUser`: Return the scheduled removal dates for a legacy user's individual flag targeting in one environment. This endpoint is deprecated in favour of the contexts API.
* **Get Expiring Targets For Segment** `getExpiringTargetsForSegment`: List the scheduled removal dates for context targets on a segment in one environment.
* **Get Expiring User Targets For Flag** `getExpiringUserTargets`: List the scheduled removal dates for individual user targets on a feature flag in one environment. This is the legacy user-scoped view.
* **Get Expiring User Targets For Segment** `getExpiringUserTargetsForSegment`: List the scheduled removal dates for user targets on a segment in one environment. This is the legacy user-scoped view of expiring targets.
* **Get Feature Flag** `getFeatureFlag`: Get a single feature flag by key, including its variations and its targeting configuration in every environment. Restrict the environments returned with Environment Key.
* **Get Feature Flag Status** `getFeatureFlagStatus`: Get the status of one feature flag in one environment: new, active, inactive or launched, plus when it was last requested.
* **Get Flag Defaults For Project** `getFlagDefaults`: Get the default settings applied to newly created feature flags in a project, including default tags, whether new flags are temporary, the default boolean variations and default client-side availability.
* **Get Flag Followers** `getFlagFollowers`: List the account members following a feature flag in one environment.
* **Get Flag Import Configuration** `getFlagImportConfiguration`: Beta. Get one flag import configuration by project key, integration key (e.g. split) and integration id.
* **Get Flag Setting For User** `getUserFlagSetting`: Return how one feature flag currently evaluates for one legacy user, including the reason and any individual override. This endpoint is deprecated in favour of the contexts API.
* **Get Flag Status Across Environments** `getFeatureFlagStatusAcrossEnvironments`: Get the status of one feature flag in every environment of a project. Set Env to restrict the result to specific environment keys.
* **Get Flag Status Chart** `getFlagStatusChart`: Returns the LaunchDarkly Engineering Insights flag-status chart series, summarising how many flags are in each lifecycle state for a project and environment. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Get Flag Trigger By ID** `getTriggerWorkflowById`: Get one flag trigger by id, including its status, recent trigger bodies and how many times it has fired.
* **Get Followers By Project And Environment** `getFollowersByProjEnv`: List the followers of every feature flag in a project and environment, grouped by flag.
* **Get Holdout** `getHoldout`: Get one holdout experiment by its key. Set Expand to include extra detail such as the linked experiments.
* **Get Holdout By ID** `getHoldoutById`: Get one holdout experiment by its internal id rather than its key.
* **Get Insight Group** `getInsightGroup`: Retrieves a single LaunchDarkly Engineering Insights group by key, optionally with its delivery scores and environment. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Get Insights Deployment** `getInsightsDeployment`: Retrieves a single LaunchDarkly Engineering Insights deployment by ID, including its lead time stages, contributors and optionally its pull requests and flag references. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Get Insights Scores** `getInsightsScores`: Returns the LaunchDarkly Engineering Insights scores for a project and environment, comparing the current period against the previous one. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Get Integration Audit Log Subscription** `getSubscriptionByID`: Get one audit log subscription by integration key and subscription id.
* **Get Integration Configuration** `getIntegrationConfiguration`: Beta. Get one integration configuration by its id. Secret configValues come back masked.
* **Get Integration Delivery Configuration** `getIntegrationDeliveryConfigurationById`: Beta. Get one integration delivery (featureStore) configuration by project, environment, integration key and id.
* **Get IP Allowlist** `getIpAllowlist`: Return your LaunchDarkly account's IP allowlist entries along with whether session and API token allowlisting are enabled. Limit and Offset are required because this endpoint rejects empty numeric values. This endpoint is in beta.
* **Get LaunchDarkly OpenAPI Spec** `getOpenapiSpec`: Downloads the complete OpenAPI 3 specification for the LaunchDarkly REST API as JSON. The document is roughly 3 MB, so use it for tooling and code generation rather than inline inspection.
* **Get Lead Time Chart** `getLeadTimeChart`: Returns the LaunchDarkly Engineering Insights lead-time chart series, broken down by delivery stage or application, over a time window. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Get MAU Clientside Usage** `getMAUClientsideUsage`: Get client-side monthly active user (MAU) usage for the account. Returns a time series, month-to-date at daily granularity.
* **Get MAU SDKs By Type** `getMauSdksByType`: List the SDKs with monthly active users (MAU) for the account, for the last seven days by default.
* **Get MAU Total Usage** `getMAUTotalUsage`: Get total monthly active user (MAU) usage for the account. Replaces the deprecated Get MAU Usage endpoint. Returns a time series, month-to-date at daily granularity.
* **Get MAU Usage (Deprecated)** `getMauUsage`: DEPRECATED by LaunchDarkly - use Get MAU Total Usage instead. Get monthly active user (MAU) usage for the account, rolling 30 days by default.
* **Get MAU Usage By Category (Deprecated)** `getMauUsageByCategory`: DEPRECATED by LaunchDarkly. Get monthly active user (MAU) usage broken down by category, last 30 days by default.
* **Get Metric** `getMetric`: Fetch a single LaunchDarkly metric by project and metric key, including how it is measured and how many experiments and flags use it.
* **Get Metric Group** `getMetricGroup`: Fetch a single LaunchDarkly metric group by project and metric group key, including the ordered list of metrics it contains and the experiments using it.
* **Get Migration Safety Issues** `postMigrationSafetyIssues`: Check whether a set of proposed semantic patch instructions on a migration flag would be unsafe, before applying them. Only works on flags created with Purpose set to migration. LaunchDarkly answers with a JSON array of safety issues, each with issue, causingRuleId, affectedRuleIds and oldSystemAffected; an empty array means the change is safe.
* **Get OAuth 2.0 Client** `getOauthClient`: Fetch a single LaunchDarkly OAuth 2.0 client application by its client ID, including its name, description and redirect URI.
* **Get Observability Errors Usage** `getObservabilityErrorsUsage`: Get observability errors usage for the account. Returns a time series of error counts, month-to-date at daily granularity.
* **Get Observability Logs Usage** `getObservabilityLogsUsage`: Get observability logs usage for the account. Returns a time series of log counts, month-to-date at daily granularity.
* **Get Observability Metrics Usage** `getObservabilityMetricsUsage`: Get observability metrics usage for the account. Returns a time series of metric counts, month-to-date at daily granularity.
* **Get Observability Sessions Usage** `getObservabilitySessionsUsage`: Get observability sessions usage for the account. Returns a time series of session counts, month-to-date at daily granularity.
* **Get Observability Traces Usage** `getObservabilityTracesUsage`: Get observability traces usage for the account. Returns a time series of trace counts, month-to-date at daily granularity.
* **Get Project** `getProject`: Get a single LaunchDarkly project by its key, optionally expanding related resources such as its environments.
* **Get Prompt Snippet** `getPromptSnippet`: Get one prompt snippet by key, including its text.
* **Get Public IP List** `getPublicIpList`: Get the public IP ranges LaunchDarkly sends traffic from, including the outbound addresses used for webhook deliveries. Use these to allowlist LaunchDarkly in a firewall.
* **Get Relay Proxy Configuration** `getRelayProxyConfig`: Get a single Relay Proxy auto-configuration by id.
* **Get Release For Flag** `getReleaseByFlagKey`: Get the release currently attached to a feature flag, including the pipeline it follows, every phase and the status of each phase.
* **Get Release Frequency Chart** `getReleaseFrequencyChart`: Returns the LaunchDarkly Engineering Insights release-frequency chart series, counting flag releases over a time window and optionally grouped by impact. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Get Release Pipeline** `getReleasePipelineByKey`: Get one release pipeline by its key, including every phase, the environments and audiences in each phase, and whether it is the project default.
* **Get Release Policy** `getReleasePolicy`: Get one release policy by its key, including its scope, rank, release method and method configuration. Beta endpoint: the LD-API-Version beta header is sent automatically.
* **Get Scheduled Change** `getFeatureFlagScheduledChange`: Get one scheduled change for a feature flag in an environment by its id, including its execution date, instructions and any conflicts.
* **Get SDK Key** `getSdkKeyByKey`: Beta. Get one SDK key by its user-defined key. sdkKeyKey identifies the key and is distinct from the secret value the SDK uses.
* **Get SDK Versions Usage Details** `getSdkVersionsDetails`: Get SDK versions usage details for the account, including per-version connection detail.
* **Get Segment** `getSegment`: Get a single segment by key, including its included and excluded targets, rules and the flags that reference it.
* **Get Service Connections Usage** `getServiceConnectionsUsage`: Get service connections usage for the account. Returns a time series of service connection counts, month-to-date at daily granularity.
* **Get Stale Flags Chart** `getStaleFlagsChart`: Returns the LaunchDarkly Engineering Insights stale-flags chart series, showing flags that have not changed recently, optionally grouped or filtered by maintainer. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Get Stream Usage** `getStreamUsage`: Get streaming connection usage for client or server SDKs. Returns a time series for the last 30 days by default.
* **Get Stream Usage By SDK Version** `getStreamUsageBySdkVersion`: Get streaming connection usage broken down by SDK version for client or server SDKs. Returns a time series for the last 24 hours by default.
* **Get Stream Usage SDK Versions** `getStreamUsageSdkversion`: List the SDK versions that have opened streaming connections for client or server SDKs.
* **Get Team** `getTeam`: Fetch a single LaunchDarkly team by its key, optionally expanding its members, custom roles, projects and maintainers.
* **Get Team Custom Roles** `getTeamRoles`: Return the custom roles that are assigned to a LaunchDarkly team. Every member of the team inherits the permissions of these roles.
* **Get Team Maintainers** `getTeamMaintainers`: Return the account members who maintain a LaunchDarkly team. Maintainers can edit the team's membership and settings.
* **Get User** `getUser`: Fetch a single legacy user in a LaunchDarkly project and environment by user key. This endpoint is deprecated in favour of the contexts API.
* **Get Vega AI Usage** `getVegaAIUsage`: Get Vega AI usage for the account. Returns a time series of Vega AI usage counts, month-to-date at daily granularity.
* **Get View** `getView`: Retrieves a single LaunchDarkly view by key, including its maintainer, tags and the summary counts of linked flags, segments, metrics and AI Configs. LaunchDarkly beta endpoint; sends the LD-API-Version: beta header.
* **Get Warehouse Export Usage** `getWarehouseExportUsage`: Get warehouse Data Export usage for the account. Returns a time series of warehouse export counts, month-to-date at daily granularity.
* **Get Webhook** `getWebhook`: Get a single LaunchDarkly webhook by its id, including its destination URL, enabled state, signing secret and policy statements.
* **Get Workflow** `getCustomWorkflow`: Get one workflow on a feature flag by its id, including every stage, the conditions guarding each stage and the current execution status.
* **Invite Account Member** `inviteAccountMember`: Invite a new member to your LaunchDarkly account. LaunchDarkly sends an invitation email to the address you supply, so only invite addresses you control. The member starts with the base role you choose plus any custom roles and teams you name.
* **Link Resources To View** `linkViewResources`: Links flags, segments or AI Configs to a LaunchDarkly view by their keys. Returns the number of successes and failures plus the resulting linked resources. LaunchDarkly beta endpoint; sends the LD-API-Version: beta header.
* **List Access Tokens** `listAccessTokens`: Return the LaunchDarkly API access tokens visible to the calling token. Administrators can set Show All to include the personal access tokens of every account member. The secret token values are never returned here.
* **List Account Members** `listAccountMembers`: Return a list of the account members in your LaunchDarkly account, with optional filtering by role, team or last-seen date, sorting and pagination.
* **List Adaptive Triggers** `listAdaptiveTriggers`: Lists the adaptive triggers configured for a flag or AI Config in a LaunchDarkly project and environment. An adaptive trigger changes flag targeting automatically when an observability alert fires. Resource Kind and Resource Key are both required by LaunchDarkly.
* **List Agent Graphs** `listAgentGraphs`: List agent graphs in a project. Sends the required LD-API-Version: beta header.
* **List Agent Optimization Results** `listAgentOptimizationResults`: List the latest agent optimization result per run.
* **List Agent Optimization Results By Run** `listAgentOptimizationResultsByRunId`: List every agent optimization result belonging to one run id.
* **List Agent Optimization Runs** `listAgentOptimizationRuns`: List the runs of an agent optimization.
* **List Agent Optimizations** `listAgentOptimizations`: List agent optimizations in a project.
* **List Agent Skill References** `listAgentSkillReferences`: List the AI Config variations that reference an agent skill. Paid entitlement; without it LaunchDarkly returns 403 "Plan does not allow this operation".
* **List Agent Skill Versions** `listAgentSkillVersions`: List all historical versions of an agent skill. Paid entitlement; without it LaunchDarkly returns 403 "Plan does not allow this operation".
* **List Agent Skills** `listAgentSkills`: List agent skills in a project. Agent skills are a paid LaunchDarkly entitlement; accounts without it get 403 {"code":"forbidden","message":"Plan does not allow this operation"}.
* **List AI Configs** `getAIConfigs`: List all AI Configs in a LaunchDarkly project. Returns items and totalCount.
* **List AI Model Config Versions** `listModelConfigVersions`: List all historical versions of an AI model config.
* **List AI Model Configs** `listModelConfigs`: List AI model configs available to a project, global ones included. LaunchDarkly returns a bare JSON array, wrapped here under items. restricted is required because LaunchDarkly rejects an empty value for a typed query param.
* **List AI Tool References** `listAIToolReferences`: List the AI Config variations that reference a given AI tool.
* **List AI Tool Versions** `listAIToolVersions`: List all historical versions of an AI tool.
* **List AI Tools** `listAITools`: List AI tools in a project. limit and offset are required because LaunchDarkly rejects an empty value for a typed query param.
* **List All Agent Optimization Results** `listAllAgentOptimizationResults`: List all agent optimization results across every version of the optimization.
* **List Announcements** `listAnnouncements`: Return the in-app announcements configured for your LaunchDarkly account, filtered by status. Status, Limit and Offset are all required because this endpoint rejects empty values for them.
* **List Application Versions** `getApplicationVersions`: Beta. List the versions reported for one application. Returns 200 with an empty items array even when the application key does not exist.
* **List Applications** `getApplications`: Beta. List the applications in the account. filter accepts key, name, kind and autoAdded; sort accepts creationDate or name; expand accepts flags. All four are templated into the URL and may be sent empty.
* **List Approval Requests** `getApprovalRequests`: List every approval request in the account. Filter with an expression such as 'notifyMemberIds anyOf ["id"]' or 'reviewStatus equals pending', expand related resources, and page with limit and offset. Returns items, totalCount and hypermedia links.
* **List Approval Requests For Flag** `getApprovalsForFlag`: List every approval request raised against one feature flag in one environment. Returns items and hypermedia links.
* **List Audit Log Entries** `listAuditLogEntries`: List LaunchDarkly audit log entries, newest first. Each entry records who changed what and when, and is the same document LaunchDarkly delivers to webhooks. Filter by time window, free text, resource specifier, member or access token. Limit must be between 1 and 20.
* **List Big Segment Store Integrations** `getBigSegmentStoreIntegrations`: Beta. List every persistent store (big segment store) integration across the account.
* **List Code Reference Branches** `getBranches`: List the branches LaunchDarkly has recorded code references for in one repository, each with its head commit and last sync time.
* **List Code Reference Extinctions** `getExtinctions`: List the recorded extinction events, where a flag's last code reference was removed. Filter by repository, branch, project, flag and a commit-time window. From and To must be used together.
* **List Code Reference Repositories** `getRepositories`: List the source repositories connected to LaunchDarkly code references. Set With Branches or With References For Default Branch to any value to include branch data and code references, and filter to one project or flag.
* **List Custom Roles** `listCustomRoles`: Return a list of all the custom roles defined in your LaunchDarkly account, including each role's policy statements and base permissions.
* **List Data Export Destinations** `getDestinations`: List every Data Export destination across all projects and environments in the account. Returns { items: [...] }.
* **List Dependent Flags** `getDependentFlags`: List the feature flags that have the given flag as a prerequisite, across every environment in the project. Beta endpoint.
* **List Dependent Flags By Environment** `getDependentFlagsByEnv`: List the feature flags that have the given flag as a prerequisite in one environment. Beta endpoint.
* **List Environment SDK Keys** `getSdkKeys`: Beta. List the SDK keys of one environment. filter supports kind equals sdk or mobile; sort is createdAt or -createdAt; limit defaults to 20, maximum 100.
* **List Environments** `listEnvironments`: List every environment in a LaunchDarkly project, with optional filtering, sorting and pagination. Each environment includes its SDK key, mobile key and approval settings.
* **List Experiments Across Environments** `listExperimentsAnyEnv`: Lists every LaunchDarkly experiment in a project across all of its environments. Use it when you do not know which environment an experiment belongs to.
* **List Experiments In Environment** `listExperiments`: Lists all LaunchDarkly experiments in a specific project and environment. Returns each experiment's key, name, methodology, current iteration and lifecycle state. Use it to inventory experiments before reading or patching one.
* **List Feature Flag Statuses** `getFeatureFlagStatuses`: List the status of every feature flag in one environment.
* **List Feature Flags** `listFeatureFlags`: List the feature flags in a project. By default flags exclude their per-environment prerequisites, targets and rules; set Summary to false to include them. Supports tag, environment and expression filters, sorting and pagination.
* **List Flag Import Configurations** `getFlagImportConfigurations`: Beta. List every flag import configuration across the account.
* **List Flag Links** `getFlagLinks`: List the external resource links attached to a feature flag. Beta endpoint.
* **List Flag Settings For User** `listUserFlagSettings`: Return how every feature flag in an environment currently evaluates for one legacy user, including any individual override. This endpoint is deprecated in favour of the contexts API.
* **List Flag Triggers** `getTriggerWorkflows`: List the triggers configured on a feature flag in one environment.
* **List Insight Groups** `listInsightGroups`: Lists the LaunchDarkly Engineering Insights groups, which collect a project, environment and set of applications so their delivery scores can be tracked together. Requires a LaunchDarkly plan that includes Engineering Insights.
* **List Insights Deployments** `listInsightsDeployments`: Lists the deployments LaunchDarkly Engineering Insights has recorded for a project and environment, with duration, status and lead time. Requires a LaunchDarkly plan that includes Engineering Insights.
* **List Insights Flag Events** `listInsightsFlagEvents`: Lists LaunchDarkly Engineering Insights flag events for a project and environment, with the impact size of each flag change. Requires a LaunchDarkly plan that includes Engineering Insights.
* **List Insights Pull Requests** `listInsightsPullRequests`: Lists the pull requests LaunchDarkly Engineering Insights has collected for a project from the connected source-code repositories, optionally with deployments, flag references and lead time. Requires a LaunchDarkly plan that includes Engineering Insights and at least one connected repository.
* **List Insights Repositories** `listInsightsRepositories`: Lists the source-code repositories connected to LaunchDarkly Engineering Insights, optionally expanded with the projects each one is associated with. Requires a LaunchDarkly plan that includes Engineering Insights.
* **List Integration Audit Log Subscriptions** `getSubscriptions`: List all audit log subscriptions for one integration, e.g. msteams, datadog, splunk, slack, elastic. Returns { items: [...], key }.
* **List Integration Configurations** `getAllIntegrationConfigurations`: Beta. List every integration configuration for one integration key. Only integrations that support configurations answer 200; others return 403 "does not allow integration configurations".
* **List Integration Delivery Configurations** `getIntegrationDeliveryConfigurations`: Beta. List every integration delivery (featureStore) configuration across the account.
* **List Integration Delivery Configurations By Environment** `getIntegrationDeliveryConfigurationByEnvironment`: Beta. List the integration delivery (featureStore) configurations in one project and environment.
* **List Layers** `listLayers`: Lists the experiment layers in a LaunchDarkly project. Layers let mutually exclusive experiments share a pool of traffic. Returns each layer's key, name, randomization unit and per-environment reservations.
* **List Metric Groups** `listMetricGroups`: Return the metric groups defined in a LaunchDarkly project. A metric group bundles several metrics so experiments can analyse them together, either as a funnel or as a standard group.
* **List Metrics** `listMetrics`: Return the metrics defined in a LaunchDarkly project, with optional filtering by tag, event kind or numeric type, sorting and pagination.
* **List OAuth 2.0 Clients** `listOauthClients`: Return all the LaunchDarkly OAuth 2.0 client applications registered on your account. Client secrets are not returned here, only on creation.
* **List Project SDK Keys** `getProjectSdkKeys`: Beta. List the SDK keys across every environment of one project. expand supports environmentSummary and viewSummaries.
* **List Projects** `listProjects`: Return a list of all LaunchDarkly projects in the account, with optional filtering, sorting, pagination and expansion of related resources such as environments.
* **List Prompt Snippet References** `listPromptSnippetReferences`: List the AI Config variations that reference a prompt snippet.
* **List Prompt Snippet Versions** `listPromptSnippetVersions`: List all historical versions of a prompt snippet.
* **List Prompt Snippets** `listPromptSnippets`: List prompt snippets in a project.
* **List Relay Proxy Configurations** `getRelayProxyConfigs`: List every Relay Proxy auto-configuration in the account. Returns { items: [...] }; key values are returned obfuscated except immediately after creation.
* **List Release Pipelines** `getAllReleasePipelines`: List the release pipelines defined in a project. Each pipeline is an ordered set of phases that flags roll out through. Filter with expressions such as query:checkout, and page with limit and offset.
* **List Release Policies** `getReleasePolicies`: List the release policies in a project, in rank order. A release policy decides which release method applies to flags matching its scope. Exclude Default is required: LaunchDarkly rejects an empty value with 400 "Query parameter 'excludeDefault' is not a valid boolean." Set it to false to include the built-in default policy. Beta endpoint: the LD-API-Version beta header is sent automatically.
* **List Release Progressions For Pipeline** `getAllReleaseProgressionsForReleasePipeline`: List the flag releases progressing through a release pipeline, with active and completed counts and the phase each release currently sits in. Filter by status active or completed, or by activePhaseId.
* **List Resources Linked To View** `listViewLinkedResources`: Lists the flags, segments or AI Configs currently linked to a LaunchDarkly view, with optional search, filter and sort. LaunchDarkly beta endpoint; sends the LD-API-Version: beta header.
* **List Scheduled Changes** `getFlagConfigScheduledChanges`: List the scheduled changes pending for one feature flag in one environment. Each item carries its execution date and the instructions LaunchDarkly will apply.
* **List Segment Memberships For Context Instance** `getContextInstanceSegmentsMembershipByEnv`: Evaluate which segments in an environment a given context instance belongs to. Supply the context instance as a JSON object string, for example {"kind":"user","key":"user-1"}.
* **List Segments** `getSegments`: List the segments in a project and environment. Supports paging with Limit and Offset, sorting, and filtering by query, tags, includedKeys, excludedKeys, external, unbounded or view.
* **List Tags** `listTags`: List the tags in use across the account for one resource kind, with usage counts. Every parameter is required: unlike LaunchDarkly's other list endpoints this one rejects an EMPTY value for any query parameter with a 400, and the connector cannot omit a parameter conditionally. The optional prefix and point-in-time asOf filters are therefore not exposed.
* **List Teams** `listTeams`: Return a list of all teams in the LaunchDarkly account, with optional filtering, pagination and expansion of related resources such as members, roles, projects and maintainers.
* **List Users** `listUsers`: Return the legacy users that have been seen in a LaunchDarkly project and environment. This endpoint is deprecated in favour of the contexts API and returns nothing for accounts that only use contexts.
* **List Views** `listViews`: Lists the views in a LaunchDarkly project. A view groups flags, segments, metrics and AI Configs so a team can scope what it sees. This is a LaunchDarkly beta endpoint and always sends the LD-API-Version: beta header.
* **List Views Linked To Resource** `listViewsForResource`: Lists every LaunchDarkly view that a given flag, segment or AI Config is linked to. The environmentId query parameter is required when the resource type is segments. LaunchDarkly beta endpoint; sends the LD-API-Version: beta header.
* **List Webhooks** `listWebhooks`: List every webhook configured on the LaunchDarkly account, including its destination URL, enabled state, signing secret and resource policy statements.
* **List Workflow Templates** `getWorkflowTemplates`: List the workflow templates in the account. Set Summary to true to return only names and descriptions, or pass Search to match a substring of a template name or description.
* **List Workflows** `getWorkflows`: List the workflows attached to a feature flag in one environment. Filter by status active, completed or failed, sort by creationDate or stopDate, and page with limit and offset.
* **Patch Experiment** `patchExperiment`: Updates a LaunchDarkly experiment using semantic patch instructions such as updateName, updateDescription, startIteration, stopIteration, archiveExperiment or restoreExperiment. Returns the updated experiment.
* **Patch Holdout** `patchHoldout`: Update a holdout experiment with semantic patch instructions, for example updateName, updateDescription or updateHoldoutAmount.
* **Patch Segment** `patchSegment`: Update a segment with a JSON Patch document. Patch paths such as /name, /description, /tags, /included, /excluded and /rules. Set Dry Run to preview without saving.
* **Remove Flag Follower** `deleteFlagFollower`: Stop an account member following a feature flag in one environment. Members with the Reader role can only remove themselves. Returns 204 on success.
* **Remove Insights Repository From Project** `deleteInsightsRepositoryProject`: Removes the association between a connected source-code repository and a LaunchDarkly project. The repository itself stays connected. Returns 204 with no body. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Remove Restricted AI Models** `deleteRestrictedModels`: Remove AI model config keys from the project's restricted list. Returns 204 No Content.
* **Reorder Release Policies** `postReleasePoliciesOrder`: Set the rank order of a project's release policies. Policy Keys Json is the ordered list of policy KEYS as a JSON array string, for example ["policy-b","policy-a"]; the first entry becomes rank 0. Passing policy ids instead of keys is rejected with 400 "Unknown release policy key at index N". Returns the reordered policies as a JSON array. Beta endpoint: the LD-API-Version beta header is sent automatically.
* **Replace SDK Key Views** `putSdkKeyViews`: Beta. Replace the complete list of views associated with an SDK key; an empty viewKeys array removes them all. Requires the SDK key Views feature to be provisioned on the account - without it LaunchDarkly answers 404 "Resource not found" on every SDK key.
* **Reset Access Token** `resetAccessToken`: Reset a LaunchDarkly API access token so that it gets a brand new secret value, optionally keeping the old value alive until an expiry timestamp. The new secret is returned once in the response. This endpoint is legacy.
* **Reset Environment Mobile Key** `resetEnvironmentMobileKey`: Rotate an environment's mobile SDK key. The old mobile key stops working immediately. Returns the environment with its new mobile key.
* **Reset Environment SDK Key** `resetEnvironmentSdkKey`: Rotate an environment's server-side SDK key. The old key stops working immediately unless an expiry timestamp is supplied. Returns the environment with its new SDK key.
* **Reset Relay Proxy Configuration Key** `resetRelayAutoConfig`: Rotate the key of a Relay Proxy auto-configuration and return the new fullKey. expiry is a Unix millisecond timestamp for when the OLD key stops working; LaunchDarkly requires it to be in the future AND within 720 hours (30 days) from now - 0 or a far-future value is rejected 400.
* **Review Approval Request** `postApprovalRequestReview`: Approve, decline or comment on an approval request. Kind must be approve, decline or comment. Returns the approval request with the new review appended to allReviews.
* **Review Approval Request For Flag** `postApprovalRequestReviewForFlag`: Approve, decline or comment on a feature flag approval request. Kind must be approve, decline or comment. Returns the approval request with the new review appended to allReviews.
* **Search Audit Log Entries** `searchAuditLogEntries`: Search your LaunchDarkly audit log using resource policy statements, so you can narrow results to specific projects, environments, flags or actions. At least one statement is required; an empty list is rejected.
* **Search Context Instances** `searchContextInstances`: Search the context instances LaunchDarkly has seen in an environment. A context instance is a specific combination of contexts that were evaluated together.
* **Search Contexts** `searchContexts`: Search the contexts LaunchDarkly has seen in an environment, using a context filter expression such as kind equals "user".
* **Set Flag Defaults For Project** `setFlagDefaults`: Create or replace the default settings applied to newly created feature flags in a project. All four fields are required; existing defaults are overwritten.
* **Set Flag Setting For User** `setUserFlagSetting`: Pin one legacy user to a specific variation of a feature flag, or clear the override by passing a null setting. This endpoint is deprecated in favour of the contexts API.
* **Trigger Flag Import Job** `triggerFlagImportJob`: Beta. Start an immediate flag import run for an existing flag import configuration. Returns 201 with an empty body.
* **Unlink Resources From View** `unlinkViewResources`: Unlinks flags, segments or AI Configs from a LaunchDarkly view by their keys. The resources themselves are not deleted. LaunchDarkly beta endpoint; sends the LD-API-Version: beta header.
* **Update Access Token** `updateAccessToken`: Apply a single JSON Patch operation to a LaunchDarkly API access token, for example replacing its /name, /description or /role. The secret token value cannot be changed here.
* **Update Account Member** `updateAccountMember`: Apply a single JSON Patch operation to a LaunchDarkly account member, for example replacing their base role at /role or their custom roles at /customRoles.
* **Update Account Members** `updateAccountMembers`: Apply a bulk semantic patch across several LaunchDarkly account members at once, for example replacing the base role of many members or adding them all to a team.
* **Update Adaptive Trigger** `updateAdaptiveTrigger`: Updates the name or the targeting task of an existing LaunchDarkly adaptive trigger. Returns the updated trigger.
* **Update Agent Graph** `patchAgentGraph`: Update an agent graph's name, description, maintainer, root config or edges. Sends the required LD-API-Version: beta header.
* **Update Agent Optimization** `patchAgentOptimization`: Update an agent optimization's attempts, models, judges, acceptance statements or optimization flags.
* **Update Agent Optimization Result** `patchAgentOptimizationResult`: Update an agent optimization result's status, activity, scores, tokens or generated variation.
* **Update Agent Skill** `patchAgentSkill`: Update an agent skill's name, description, markdown, tags or maintainer. Paid entitlement; without it LaunchDarkly returns 403 "Plan does not allow this operation".
* **Update AI Config** `patchAIConfig`: Update an AI Config's name, description, tags, default variation or evaluation metric.
* **Update AI Config Targeting** `patchAIConfigTargeting`: Apply semantic-patch targeting instructions to an AI Config in one environment. instructions is an array of objects such as [{"kind":"updateOffVariation","variationId":"&lt;id&gt;"}].
* **Update AI Config Variation** `patchAIConfigVariation`: Update an AI Config variation: name, messages, model config, tools, skills, publish/archive state.
* **Update AI Model Config** `patchModelConfig`: Update an AI model config's name, costs, params, tags or maintainer. id and provider are immutable.
* **Update AI Tool** `patchAITool`: Update an AI tool's description, JSON Schema, custom parameters, tags or maintainer.
* **Update Announcement** `updateAnnouncement`: Apply a single JSON Patch operation to an in-app announcement, for example replacing its /title, /message, /severity or /endTime.
* **Update Application** `patchApplication`: Beta. Apply one JSON-Patch operation to an application, e.g. replace /description or /maintainerId. value takes the new value directly in its natural JSON type - a plain string, number, boolean or object; do not pre-encode it.
* **Update Application Version** `patchApplicationVersion`: Beta. Apply one JSON-Patch operation to a single version of an application, e.g. replace /supported. value takes the new value directly in its natural JSON type - a plain string, number, boolean or object; do not pre-encode it.
* **Update Approval Request** `patchApprovalRequest`: Update a pending approval request using semantic patch instructions. Supported instruction kinds are addReviewers, which takes notifyMemberIds and notifyTeamKeys, and updateDescription, which takes value. Returns the updated approval request.
* **Update Approval Request Settings** `patchApprovalRequestSettings`: Update the approval request settings for one environment and resource kind in a project. Environment Key and Resource Kind identify which settings to change; the remaining fields are the settings themselves. Beta endpoint: the LD-API-Version beta header is sent automatically.
* **Update Big Segment Context Targets** `updateBigSegmentContextTargets`: Add or remove context keys from a big (unbounded) segment's included and excluded lists. Only works on segments created with Big Segment set to true. Returns 204 on success.
* **Update Big Segment Store Integration** `patchBigSegmentStoreIntegration`: Beta. Apply one JSON-Patch operation to a persistent store integration. value takes the new value directly in its natural JSON type - a plain string, number, boolean or object; do not pre-encode it.
* **Update Big Segment User Targets** `updateBigSegmentTargets`: Add or remove user keys from a big (unbounded) segment's included and excluded lists. Only works on segments created with Big Segment set to true. Returns 204 on success.
* **Update Code Reference Repository** `patchRepository`: Update a code reference repository with a single JSON Patch operation. Patchable paths include /sourceLink, /commitUrlTemplate, /hunkUrlTemplate, /defaultBranch and /enabled.
* **Update Custom Role** `updateCustomRole`: Update a LaunchDarkly custom role with a list of JSON Patch operations, for example replacing /name, /description or the whole /policy array.
* **Update Data Export Destination** `patchDestination`: Apply one JSON-Patch operation to a Data Export destination. value takes the new value directly in its natural JSON type - a plain string, number, boolean or object; do not pre-encode it.
* **Update Environment** `updateEnvironment`: Update an environment with a single JSON Patch operation. Patchable paths include /name, /color, /defaultTtl, /secureMode, /defaultTrackEvents, /requireComments, /confirmChanges, /tags and /critical.
* **Update Experimentation Settings** `updateExperimentationSettings`: Replaces the set of randomization units allowed for experiments in a LaunchDarkly project. Send the complete desired list; units omitted from the list are removed.
* **Update Expiring Context Targets On Flag** `patchExpiringTargets`: Schedule, update or remove expiry dates for individual context targets on a feature flag using semantic patch instructions such as addExpiringTarget, updateExpiringTarget and removeExpiringTarget.
* **Update Expiring Flag Targets For User** `updateExpiringFlagsForUser`: Schedule, change or remove the dates on which a legacy user's individual flag targeting expires, using semantic patch instructions such as addExpiringTarget or removeExpiringTarget. This endpoint is deprecated in favour of the contexts API.
* **Update Expiring Targets For Segment** `patchExpiringTargetsForSegment`: Schedule, update or remove expiry dates for context targets on a segment using semantic patch instructions such as addExpiringTarget, updateExpiringTarget and removeExpiringTarget.
* **Update Expiring User Targets For Segment** `patchExpiringUserTargetsForSegment`: Schedule, update or remove expiry dates for user targets on a segment using semantic patch instructions such as addExpireUserTargetDate, updateExpireUserTargetDate and removeExpireUserTargetDate.
* **Update Expiring User Targets On Flag** `patchExpiringUserTargets`: Schedule, update or remove expiry dates for individual user targets on a feature flag using semantic patch instructions such as addExpireUserTargetDate, updateExpireUserTargetDate and removeExpireUserTargetDate.
* **Update Feature Flag** `updateFeatureFlag`: Update a feature flag with a JSON Patch document. Patch flag-level paths such as /name, /description, /tags, /temporary and /archived, or environment-scoped paths such as /environments/production/on and /environments/production/fallthrough/variation. Set Dry Run to preview the result without saving.
* **Update Flag Approval Request** `patchFlagConfigApprovalRequest`: Update a pending feature flag approval request using semantic patch instructions. Supported instruction kinds are addReviewers, which takes notifyMemberIds and notifyTeamKeys, and updateDescription, which takes value. Returns the updated approval request.
* **Update Flag Defaults For Project** `updateFlagDefaults`: Update a project's feature flag defaults with a single JSON Patch operation. Patchable paths include /tags, /temporary, /booleanDefaults and /defaultClientSideAvailability.
* **Update Flag Import Configuration** `patchFlagImportConfiguration`: Beta. Apply one JSON-Patch operation to a flag import configuration. value takes the new value directly in its natural JSON type - a plain string, number, boolean or object; do not pre-encode it.
* **Update Flag Link** `updateFlagLink`: Update one field of a flag link with a single JSON Patch operation, for example replacing /title or /description. Beta endpoint.
* **Update Flag Setting For Context** `putContextFlagSetting`: Individually target one context with a specific variation of a flag in one environment. Setting must match the flag's variation type; pass null to clear the individual target. Returns 204 on success.
* **Update Flag Trigger** `patchTriggerWorkflow`: Update a flag trigger with semantic patch instructions such as disableTrigger, enableTrigger, cycleTriggerUrl or replaceTriggerActionInstructions.
* **Update Insight Group** `updateInsightGroup`: Updates a LaunchDarkly Engineering Insights group with a single JSON Patch operation, for example replacing /name or /applicationKeys. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Update Insights Deployment** `updateInsightsDeployment`: Updates a LaunchDarkly Engineering Insights deployment with a single JSON Patch operation, for example replacing /status with finished or /archived with true. Requires a LaunchDarkly plan that includes Engineering Insights.
* **Update Integration Audit Log Subscription** `updateSubscription`: Apply one JSON-Patch operation to an audit log subscription. value takes the new value directly in its natural JSON type - a plain string, number, boolean or object; do not pre-encode it.
* **Update Integration Configuration** `updateIntegrationConfiguration`: Beta. Apply one JSON-Patch operation to an integration configuration. value takes the new value directly in its natural JSON type - a plain string, number, boolean or object; do not pre-encode it.
* **Update Integration Delivery Configuration** `patchIntegrationDeliveryConfiguration`: Beta. Apply one JSON-Patch operation to an integration delivery (featureStore) configuration. value takes the new value directly in its natural JSON type - a plain string, number, boolean or object; do not pre-encode it.
* **Update IP Allowlist Configuration** `updateIpAllowlistConfig`: Turn IP allowlisting on or off for browser sessions and for API tokens. Enabling either setting immediately blocks every address that is not on the allowlist, including the one calling this API, so confirm your own address is listed first. This endpoint is in beta.
* **Update IP Allowlist Entry** `updateIpAllowlistEntry`: Change the description of an existing IP allowlist entry. The IP address itself cannot be changed; delete the entry and create a new one instead. This endpoint is in beta.
* **Update Layer** `updateLayer`: Updates a LaunchDarkly experiment layer with semantic patch instructions. The supported instruction is updateExperimentReservation, which sets the percentage of the layer's traffic reserved for a given experiment in a given environment.
* **Update Metric** `updateMetric`: Apply a single JSON Patch operation to a LaunchDarkly metric, for example replacing its /name, /description or /tags.
* **Update Metric Group** `updateMetricGroup`: Apply a single JSON Patch operation to a LaunchDarkly metric group, for example replacing its /name, /description, /tags or the whole /metrics list.
* **Update OAuth 2.0 Client** `updateOauthClient`: Apply a single JSON Patch operation to a LaunchDarkly OAuth 2.0 client, for example replacing its /name, /description or /redirectUri.
* **Update Project** `updateProject`: Update a LaunchDarkly project with a single JSON Patch operation. Choose the operation (add, remove or replace), the JSON Pointer path and the new value. Patchable paths include /name, /tags, /includeInSnippetByDefault and /defaultClientSideAvailability. Returns the updated project.
* **Update Prompt Snippet** `patchPromptSnippet`: Update a prompt snippet's name, description, text, tags or maintainer.
* **Update Relay Proxy Configuration** `patchRelayAutoConfig`: Update a Relay Proxy auto-configuration. Unlike the other integration endpoints this one wraps the JSON-Patch array in an object: { patch: [...], comment }. patch is a real array input.
* **Update Release For Flag** `patchReleaseByFlagKey`: Update a flag's release with a single JSON Patch operation, for example replacing /phases/0/audiences or cancelling the release. Returns the updated release.
* **Update Release Phase Status** `updatePhaseStatus`: Move one phase of a flag's release forward, for example by setting Status to completed. Audiences supplies any extra configuration a phase needs when it is initialized. Returns the updated release.
* **Update Release Pipeline** `putReleasePipeline`: Replace a release pipeline's name, description, phases and tags. Name and Phases are required and overwrite the existing values; the pipeline key cannot be changed.
* **Update Release Policy** `putReleasePolicy`: Replace a release policy's name, scope, release method and method configuration. The policy key cannot be changed. Beta endpoint: the LD-API-Version beta header is sent automatically.
* **Update Scheduled Change** `patchFlagConfigScheduledChange`: Update a scheduled change with semantic patch instructions. The supported kinds are replaceScheduledChangesInstructions, whose value is the new array of actions (only turnFlagOn and turnFlagOff are schedulable), updateScheduledChangesExecutionDate, whose value is the new Unix-millisecond execution date, and deleteScheduledChange. Returns the updated scheduled change.
* **Update SDK Key** `patchSdkKeyByKey`: Beta. Update an SDK key's name, description or expiry. This endpoint takes a plain merge object, not a JSON-Patch array. version applies optimistic locking; send 0 to skip the check.
* **Update Team** `updateTeam`: Update a LaunchDarkly team using semantic patch instructions such as updateName, updateDescription, addMembers, removeMembers, addCustomRoles or removeCustomRoles. Supply one instruction kind and its values.
* **Update Teams** `updateTeams`: Apply a bulk semantic patch across several LaunchDarkly teams at once, for example adding the same members or custom roles to many teams. This endpoint is in beta and the request is sent with the LD-API-Version beta header.
* **Update View** `updateView`: Updates a LaunchDarkly view's name, description, maintainer or tags. Only the supplied fields change. LaunchDarkly beta endpoint; sends the LD-API-Version: beta header.
* **Update Webhook** `updateWebhook`: Update a webhook with a single JSON Patch operation. Patchable paths include /name, /url, /on, /secret, /tags and /statements.
* **Upsert Code Reference Branch** `putBranch`: Create or replace the code references recorded for one branch of a repository. Head is the branch HEAD commit SHA, Sync Time is Unix epoch milliseconds, and References is the array of flag references found on the branch, each with path, hint and hunks. Returns 200 with an empty body.
* **Validate Integration Delivery Configuration** `validateIntegrationDeliveryConfiguration`: Beta. Ask LaunchDarkly to make a test call to the third-party store behind an integration delivery configuration. Returns 200 with { statusCode, timestamp, responseBody } describing the third party's answer. Only integrations whose manifest declares a validation request support this; others return 404 "No validation request in manifest" (cloudflare supports it, fastly and vercel-native do not).

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Access Token Created | `createAccessToken` | A REST API access token was created. Verified present in this account's audit log. Scope with Resource Scope member/*:token/*. |
| Any Change (All Actions) | `*` | Every auditable change on the resources selected by Resource Scope. Use this when you want one trigger for all LaunchDarkly activity rather than a specific action. |
| Context Kind Created | `createContextKind` | A context kind was created in a project. Verified present in this account's audit log. |
| Environment Approval Settings Changed | `updateApprovalSettings` | An environment's approval settings were changed. Verified present in this account's audit log. |
| Environment Created | `createEnvironment` | An environment was created in a project. Verified present in this account's audit log. |
| Environment Deleted | `deleteEnvironment` | An environment was deleted from a project. Verified present in this account's audit log. |
| Environment Mobile Key Reset | `updateMobileKey` | An environment's mobile SDK key was rotated. Verified present in this account's audit log. |
| Environment SDK Key Reset | `updateApiKey` | An environment's server-side SDK key was rotated. Verified present in this account's audit log. |
| Feature Flag Created | `createFlag` | A feature flag was created in a project. Scope with the Resource Scope input, for example proj/my-project:env/*:flag/*. |
| Feature Flag Default Rule Changed | `updateFallthrough` | A feature flag's default (fallthrough) variation was changed in an environment. |

<details>

<summary>See 18 more events</summary>

* **Feature Flag Deleted** `deleteFlag`: A feature flag was permanently deleted from a project.
* **Feature Flag Individual Targets Changed** `updateTargets`: Individual context targets were added to or removed from a feature flag in an environment.
* **Feature Flag Targeting Rules Changed** `updateRules`: A feature flag's targeting rules were changed in an environment.
* **Feature Flag Toggled** `updateOn`: A feature flag was turned on or off in an environment. Scope with Resource Scope to restrict to one environment, for example proj/*:env/production:flag/*.
* **Feature Flag Variations Changed** `updateFlagVariations`: A feature flag's variations were added, removed or edited.
* **Metric Created** `createMetric`: An experimentation metric was created in a project. Verified present in this account's audit log. Scope with Resource Scope proj/*:metric/*.
* **Project Created** `createProject`: A project was created. Scope with Resource Scope proj/*.
* **Project Deleted** `deleteProject`: A project was deleted.
* **Project Flag Defaults Changed** `updateProjectFlagDefaults`: A project's feature flag defaults were changed. Verified present in this account's audit log.
* **Project Renamed** `updateProjectName`: A project was renamed. Verified present in this account's audit log.
* **Resource Renamed** `updateName`: A resource was renamed. LaunchDarkly uses the same updateName action for flags, environments, webhooks and segments; read the kind field of the payload to tell them apart. Verified present in the audit log for environment and webhook renames.
* **Resource Tags Changed** `updateTags`: The tags on a flag or segment were changed.
* **Segment Created** `createSegment`: A context segment was created in a project. Scope with Resource Scope proj/*:env/*:segment/*.
* **Segment Deleted** `deleteSegment`: A context segment was deleted.
* **Segment Excluded Contexts Changed** `updateExcluded`: The contexts explicitly excluded from a segment were changed.
* **Segment Included Contexts Changed** `updateIncluded`: The contexts explicitly included in a segment were changed.
* **Webhook Created** `createWebhook`: A webhook was created on the account. Verified present in this account's audit log. Scope with Resource Scope webhook/*.
* **Webhook Deleted** `deleteWebhook`: A webhook was deleted from the account. Verified present in this account's audit log.

</details>
