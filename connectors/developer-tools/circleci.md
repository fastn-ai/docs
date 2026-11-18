---
description: "CircleCI is a continuous integration and delivery platform for building, testing and deploying software."
hidden: true
---

# CircleCI

<img src="../../.gitbook/assets/connectors/lg/circleci.png" alt="CircleCI logo">

CircleCI is a continuous integration and delivery platform for building, testing and deploying software. This connector covers the CircleCI API v2: projects, pipelines, workflows, jobs, contexts, environment variables, checkout keys, schedules, triggers, insights, deploys, policies, OIDC claims, usage exports and outbound webhooks.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [circleci.com](https://circleci.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `circleci` |

## Use it

Add CircleCI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.circleci.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Context Environment Variable | `addEnvironmentVariableToContext` | Create or update an environment variable within a context. Returns information about the environment variable, not including its value. |
| Approve Pending Approval Job | `approvePendingApprovalJobById` | Approves a pending approval job in a workflow. |
| Cancel Job by ID | `cancelJobByJobID` | Cancel job with a given job ID. |
| Cancel Job by Number | `cancelJobByJobNumber` | Cancel job with a given job number. |
| Cancel Workflow | `cancelWorkflow` | Cancels a running workflow. |
| Continue Pipeline | `continuePipeline` | Continue a pipeline from the setup phase. For information on using pipeline parameters with dynamic configuration, see the [Pipeline values and parameters](https://circleci.com/docs/pipeline-variables/#pipeline-parameters-and-dynamic-configuration) docs. |
| Create Checkout Key | `createCheckoutKey` | Not available to projects that use GitLab or GitHub App. Creates a new checkout key. This API request is only usable with a user API token. Please ensure that you have authorized your account with GitHub before creating user keys. This is necessary to give CircleCI the permission to create a user key associated with your GitHub user account. You can find this page by visiting Project Settings &gt; Checkout SSH Keys Checkout keys are only available on projects backed by a version control repository. A standalone CircleCI project returns 400 "This API is not supported for this project.". |
| Create Context | `createContext` | Creates a new context in the specified organization. |
| Create Context Restriction | `createContextRestriction` | Creates project or expression restriction on a context. |
| Create Organization | `createOrganization` | Create a new organization. For VCS providers (GitHub/Bitbucket), this validates access and syncs org data. For standalone orgs, this creates a new CircleCI organization. |

<details>

<summary>See 104 more actions</summary>

* **Create Organization Group** `createOrganizationGroup`: Create a new group under the organization. Currently only supported for standalone organizations.
* **Create OTLP Exporter** `createOtelExporter`: [__EXPERIMENTAL__] Creates a new OTLP exporter configuration for the given organization. A maximum of 5 exporter configurations are allowed per organization.
* **Create Pipeline Definition** `createPipelineDefinition`: Create a pipeline definition for a given project. Currently only supported for pipeline definitions where `config_source.provider` is `github_app` or `github_server`. [Share feedback](https://circleci.canny.io/cloud-feature-requests/p/project-administration-apis) about our Project Administration APIs.
* **Create Policy Bundle** `createPolicyBundle`: This endpoint replaces the current policy bundle with the provided policy bundle Policy management requires a CircleCI paid plan; organizations on the free plan receive 403 "Forbidden: plan does not have sufficient permissions".
* **Create Project** `createProject`: Create a new project. Works for all organization types.
* **Create Project Environment Variable** `createEnvVar`: Creates a new environment variable.
* **Create Schedule** `createSchedule`: Creates a schedule and returns the created schedule. Available only on organizations of type `bitbucket` and `github`, and for the latter will exclusively create schedule triggers associated with the GitHub OAuth pipeline definition. For projects of type `circleci`, or to create schedule triggers for GitHub App pipeline definitions, use the [Create trigger](https://circleci.com/docs/api/v2/index.html#tag/Trigger/operation/createTrigger) endpoint. Scheduled pipelines are only available on projects backed by a version control repository. A standalone CircleCI project returns 400 "Scheduled pipelines is not supported for standalone projects".
* **Create Trigger** `createTrigger`: Create a trigger for a given pipeline definition. Currently only supported for pipeline definitions where `config_source.provider` is `github_oauth`, `github_app`, `github_server`, or `schedule`. [Share feedback](https://circleci.canny.io/cloud-feature-requests/p/project-administration-apis) about our Project Administration APIs. The API also requires checkout_ref, which the published specification omits; a request without it returns 400 "Checkout_ref must be provided.".
* **Create URL Orb Allow List Entry** `createURLOrbAllowListEntry`: Create a new URL Orb allow-list entry
* **Create Usage Export** `createUsageExport`: Submits a request to create a usage export for an organization.
* **Create Webhook** `createWebhook`: Creates an outbound webhook for the given scope.
* **Delete Checkout Key** `deleteCheckoutKey`: Deletes the checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.
* **Delete Context** `deleteContext`: Delete a context by its ID. Will also delete all environment variables inside the context.
* **Delete Context Environment Variable** `deleteEnvironmentVariableFromContext`: Delete an environment variable from a context.
* **Delete Context Restriction** `deleteContextRestriction`: Deletes a project, expression or group restriction from a context.
* **Delete Organization** `deleteOrganization`: Delete an organization. This action will delete all projects including all build data for the organization.
* **Delete Organization Group** `deleteGroup`: Delete a group in an organization. This will remove all members from the group as well, and the subsequent role grants tied to the group. Currently only supported for standalone organizations.
* **Delete Organization OIDC Claims** `deleteOrgClaims`: Deletes org-level custom claims of OIDC identity tokens
* **Delete OTLP Exporter** `deleteOtelExporter`: [__EXPERIMENTAL__] Deletes an OTLP exporter configuration by ID.
* **Delete Pipeline Definition** `deletePipelineDefinition`: Delete pipeline definition. Currently only supported for pipeline definitions where `config_source.provider` is `github_app`, `github_server`, or `bitbucket_dc`. [Share feedback](https://circleci.canny.io/cloud-feature-requests/p/project-administration-apis) about our Project Administration APIs.
* **Delete Project** `deleteProjectBySlug`: Deletes a project by project slug
* **Delete Project Environment Variable** `deleteEnvVar`: Deletes the environment variable named :name.
* **Delete Project OIDC Claims** `deleteProjectClaims`: Deletes project-level custom claims of OIDC identity tokens
* **Delete Schedule** `deleteScheduleById`: Deletes a schedule by ID. Available only on schedules associated with GitHub OAuth or Bitbucket Cloud pipeline definitions.
* **Delete Trigger** `deleteTrigger`: Delete a trigger. Currently only supported for triggers where `event_source.provider` is `github_oauth`, `github_app`, `github_server`, `bitbucket_dc`, `webhook`, or `schedule`. [Share feedback](https://circleci.canny.io/cloud-feature-requests/p/project-administration-apis) about our Project Administration APIs.
* **Delete URL Orb Allow List Entry** `removeURLOrbAllowListEntry`: Remove an entry from the org's URL orb allow-list
* **Delete Webhook** `deleteWebhook`: Deletes an existing outbound webhook by its unique ID.
* **Get Checkout Key** `getCheckoutKey`: Returns an individual checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.
* **Get Context** `getContext`: Returns basic information about a context.
* **Get Current User** `getCurrentUser`: Provides information about the user that is currently signed in.
* **Get Deploy Component** `getComponent`: Get the details of a component by ID.
* **Get Deploy Environment** `getEnvironment`: Allows getting an environment for a given environment ID.
* **Get Job** `getJob`: Gets a job's metadata by its unique ID, including its name, job number, type, status, and associated resource IDs.
* **Get Job Details by Number** `getJobDetailsByNumber`: Return the full detail of a single job identified by its project slug and job number, including its executor, parallelism, timing and parent workflow. This route is live on the API v2 host but is not listed in the current CircleCI API v2 reference index; Get Job returns the same record by job ID.
* **Get Job Timeseries** `getJobTimeseries`: Get timeseries data for all jobs within a workflow. Hourly granularity data is only retained for 48 hours while daily granularity data is retained for 90 days.
* **Get Organization** `getOrganization`: Retrieve an organization by slug or ID
* **Get Organization Group** `getGroup`: Get details for a group in an organization. Currently only supported for standalone organizations.
* **Get Organization Insights Summary** `getOrgSummaryData`: Gets aggregated summary metrics with trends for the entire org. Also gets aggregated metrics and trends for each project belonging to the org.
* **Get Organization OIDC Claims** `getOrgClaims`: Fetches org-level custom claims of OIDC identity tokens
* **Get Pipeline by ID** `getPipelineById`: Returns a pipeline by the pipeline ID.
* **Get Pipeline by Number** `getPipelineByNumber`: Returns a pipeline by the pipeline number.
* **Get Pipeline Configuration** `getPipelineConfigById`: Returns a pipeline's configuration by ID.
* **Get Pipeline Definition** `getPipelineDefinition`: Get details for a pipeline definition. Currently only supported for pipeline definitions where `config_source.provider` is `github_app`, `github_server`, `github_oauth`, `bitbucket_dc`, `bitbucket_oauth` or `gitlab`. [Share feedback](https://circleci.canny.io/cloud-feature-requests/p/project-administration-apis) about our Project Administration APIs.
* **Get Pipeline Values** `getPipelineValuesById`: Returns a map of pipeline values by pipeline ID. For more information see the [pipeline values reference page](https://circleci.com/docs/variables/#pipeline-values).
* **Get Policy Bundle** `getPolicyBundle`: This endpoint will retrieve a policy bundle Policy management requires a CircleCI paid plan; organizations on the free plan receive 403 "Forbidden: plan does not have sufficient permissions".
* **Get Policy Bundle for Decision Log** `getDecisionLogPolicyBundle`: This endpoint will retrieve a policy bundle for a given decision log ID Policy management requires a CircleCI paid plan; organizations on the free plan receive 403 "Forbidden: plan does not have sufficient permissions".
* **Get Policy Decision Log** `getDecisionLog`: This endpoint will retrieve a decision for a given decision log ID Policy management requires a CircleCI paid plan; organizations on the free plan receive 403 "Forbidden: plan does not have sufficient permissions".
* **Get Policy Decision Settings** `getDecisionSettings`: This endpoint retrieves the current decision settings (eg enable/disable policy evaluation) Policy management requires a CircleCI paid plan; organizations on the free plan receive 403 "Forbidden: plan does not have sufficient permissions".
* **Get Policy Document** `getPolicyDocument`: This endpoint will retrieve a policy document. Policy management requires a CircleCI paid plan; organizations on the free plan receive 403 "Forbidden: plan does not have sufficient permissions".
* **Get Project** `getProjectBySlug`: Retrieves a project by project slug.
* **Get Project Environment Variable** `getEnvVar`: Returns the masked value of environment variable :name.
* **Get Project Insights Summary** `getProjectWorkflowsPageData`: Get summary metrics and trends for a project at workflow and branch level. Workflow runs going back at most 90 days are included in the aggregation window. Trends are only supported upto last 30 days. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting. Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI. This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI. For precise credit reporting, always use the Plan Overview page in the CircleCI UI.
* **Get Project OIDC Claims** `getProjectClaims`: Fetches project-level custom claims of OIDC identity tokens
* **Get Project Settings** `getProjectSettings`: Returns a list of the advanced settings for a CircleCI project, whether enabled (true) or not (false).
* **Get Schedule** `getScheduleById`: Get a schedule by id.
* **Get Trigger** `getTrigger`: Get details for a trigger. Currently only supported for triggers where `event_source.provider` is `github_oauth`, `github_app`, `github_server`, `bitbucket_dc`, `webhook`, or `schedule`. [Share feedback](https://circleci.canny.io/cloud-feature-requests/p/project-administration-apis) about our Project Administration APIs.
* **Get Usage Export** `getUsageExport`: Gets a usage export for an organization.
* **Get User** `getUser`: Provides information about the user with the given ID.
* **Get Webhook** `getWebhookById`: Get an outbound webhook by id.
* **Get Workflow** `getWorkflowById`: Returns summary fields of a workflow by ID.
* **Get Workflow Summary Metrics** `getWorkflowSummary`: Get the metrics and trends for a particular workflow on a single branch or all branches
* **Get Workflow Test Metrics** `getProjectWorkflowTestMetrics`: Get test metrics for a project's workflows. Currently tests metrics are calculated based on 10 most recent workflow runs.
* **List Checkout Keys** `listCheckoutKeys`: Returns a sequence of checkout keys for `:project`.
* **List Collaborations** `getCollaborations`: Provides the set of organizations of which a user is a member or a collaborator. The set of organizations that a user can collaborate on is composed of: * Organizations that the current user belongs to across VCS types (e.g. BitBucket, GitHub) * The parent organization of repository that the user can collaborate on, but is not necessarily a member of * The organization of the current user's account
* **List Context Environment Variables** `listEnvironmentVariablesFromContext`: List information about environment variables in a context, not including their values.
* **List Context Restrictions** `getContextRestrictions`: Gets a list of project and expression restrictions associated with a context.
* **List Contexts** `listContexts`: List all contexts for an owner. Supply either owner-id or owner-slug; a call with neither returns 400 "must specify either owner-slug or owner-id".
* **List Deploy Component Versions** `listComponentVersions`: List the versions for a component.
* **List Deploy Components** `listComponents`: Allows for listing of components for a given organization ID.
* **List Deploy Environments** `listEnvironments`: Allows listing environments for a given organization ID.
* **List Flaky Tests** `getFlakyTests`: Get a list of flaky tests for a given project. Flaky tests are branch agnostic. A flaky test is a test that passed and failed in the same commit.
* **List Insights Branches** `getAllInsightsBranches`: Get a list of all branches for a specified project. The list will only contain branches currently available within Insights. The maximum number of branches returned by this endpoint is 5,000.
* **List Job Artifacts** `listJobArtifacts`: Return the artifacts produced by a completed job. Artifacts are only retained for the configured storage period and an in-progress job returns an empty list. This route is live on the API v2 host but is not listed in the current CircleCI API v2 reference index.
* **List Job Test Metadata** `getJobTestMetadata`: Return the test metadata collected for a completed job. The job must have used the store_test_results step, otherwise the list is empty. This route is live on the API v2 host but is not listed in the current CircleCI API v2 reference index.
* **List My Project Pipelines** `listMyPipelines`: Returns a sequence of all pipelines for this project triggered by the user.
* **List Organization Groups** `getOrganizationGroups`: Get all the groups in an organization.
* **List Organization Pipelines** `listPipelines`: Returns all pipelines for the most recently built projects (max 250) you follow in an organization.
* **List OTLP Exporters** `listOtelExporters`: [__EXPERIMENTAL__] Returns a list of OTLP exporter configurations for the given organization.
* **List Pipeline Definition Triggers** `listPipelineDefinitionTriggers`: List all triggers for a given pipeline definition. Currently only supported for pipeline definitions where `config_source.provider` is `github_oauth`, `github_app`, `github_server`, `bitbucket_dc`, or `schedule`. [Share feedback](https://circleci.canny.io/cloud-feature-requests/p/project-administration-apis) about our Project Administration APIs.
* **List Pipeline Definitions** `listPipelineDefinitions`: List all pipeline definitions for a given project. [Share feedback](https://circleci.canny.io/cloud-feature-requests/p/project-administration-apis) about our Project Administration APIs.
* **List Pipeline Workflows** `listWorkflowsByPipelineId`: Returns a paginated list of workflows by pipeline ID.
* **List Policy Decision Logs** `getDecisionLogs`: This endpoint will return a list of decision audit logs that were made using this owner's policies. Policy management requires a CircleCI paid plan; organizations on the free plan receive 403 "Forbidden: plan does not have sufficient permissions".
* **List Project Environment Variables** `listEnvVars`: Returns four 'x' characters, in addition to the last four ASCII characters of the value, consistent with the display of environment variable values on the CircleCI website.
* **List Project Pipelines** `listPipelinesForProject`: Returns all pipelines for this project.
* **List Project Schedules** `listSchedulesForProject`: For a given project, returns all schedules associated with GitHub OAuth or Bitbucket Cloud pipeline definitions. Does not return schedule triggers associated with GitHub App pipelines. To fetch schedule triggers associated with GitHub App pipelines, use the [List pipeline definition triggers](https://circleci.com/docs/api/v2/index.html#tag/Trigger/operation/listPipelineDefinitionTriggers] endpoint. Scheduled pipelines are only available on projects backed by a version control repository.
* **List URL Orb Allow List Entries** `listURLOrbAllowListEntries`: List the entries in the org's URL Orb allow-list
* **List Webhooks** `getWebhooks`: Get a list of outbound webhooks that match the given scope-type and scope-id.
* **List Workflow Job Metrics** `getProjectWorkflowJobMetrics`: Get summary metrics for a project workflow's jobs. Job runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting. Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI. This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI. For precise credit reporting, always use the Plan Overview page in the CircleCI UI.
* **List Workflow Jobs** `listWorkflowJobs`: Returns a sequence of jobs for a workflow.
* **List Workflow Metrics** `getProjectWorkflowMetrics`: Get summary metrics for a project's workflows. Workflow runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting. Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI. This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI. For precise credit reporting, always use the Plan Overview page in the CircleCI UI.
* **List Workflow Runs** `getProjectWorkflowRuns`: Get recent runs of a workflow. Runs going back at most 90 days are returned. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting. Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI. This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI. For precise credit reporting, always use the Plan Overview page in the CircleCI UI.
* **Make Policy Decision** `makeDecision`: This endpoint will evaluate input data (config+metadata) against owner's stored policies and return a decision. Policy management requires a CircleCI paid plan; organizations on the free plan receive 403 "Forbidden: plan does not have sufficient permissions".
* **Rerun Workflow** `rerunWorkflow`: Reruns a workflow.
* **Roll Back Project** `rollbackProject`: Performs a rollback operation by triggering a rollback pipeline. A rollback targets a component and environment that already exist under the project's Deploys, which are created by pipeline runs that publish deploy markers. Calling it for a component or environment the project has never deployed returns 500 "Internal server error." from CircleCI.
* **Trigger Pipeline (Legacy)** `triggerPipeline`: **[This endpoint is superseded by the [new Trigger Pipeline API](#tag/Pipeline/operation/triggerPipelineRun), which supports all organization and pipeline types except GitLab.]** Triggers a new pipeline on the project. Does not support triggering pipelines integrated with GitLab or GitHub App. This is the legacy trigger endpoint and only works on projects backed by a GitHub OAuth or Bitbucket Cloud repository. Use Trigger Pipeline Run for GitLab, GitHub App and standalone CircleCI projects.
* **Trigger Pipeline Run** `triggerPipelineRun`: Trigger a pipeline given a pipeline definition ID. Currently only supported for pipeline definitions where `config_source.provider` is `github_app`, `github_server`, `github_oauth`, `bitbucket_dc`, or `bitbucket_oauth`. The slash-separated project slug is shown in Project Settings &gt; Overview. Depending on the organization type, the project slug may have a human-readable format (`vcs_type/org_name/project_name`) or be an opaque string (e.g. `circleci/43G3lM5RtfFE7v5sa4nWAU/44n9wujWcTnVZ2b5S8Fnat`).
* **Update Organization OIDC Claims** `patchOrgClaims`: Creates/Updates org-level custom claims of OIDC identity tokens
* **Update Pipeline Definition** `updatePipelineDefinition`: Update pipeline definition. Currently only supported for pipeline definitions where `config_source.provider` is `github_app`, `github_server`, or `bitbucket_dc`. [Share feedback](https://circleci.canny.io/cloud-feature-requests/p/project-administration-apis) about our Project Administration APIs.
* **Update Policy Decision Settings** `setDecisionSettings`: This endpoint allows modifying decision settings (eg enable/disable policy evaluation) Policy management requires a CircleCI paid plan; organizations on the free plan receive 403 "Forbidden: plan does not have sufficient permissions".
* **Update Project OIDC Claims** `patchProjectClaims`: Creates/Updates project-level custom claims of OIDC identity tokens
* **Update Project Settings** `patchProjectSettings`: Updates one or more of the advanced settings for a CircleCI project.
* **Update Schedule** `updateSchedule`: Updates a schedule and returns the updated schedule. Available only on schedules associated with GitHub OAuth or Bitbucket Cloud pipeline definitions. To update schedule triggers for GitHub App pipeline definitions, use the [Update trigger](https://circleci.com/docs/api/v2/index.html#tag/Trigger/operation/updateTrigger) endpoint.
* **Update Trigger** `updateTrigger`: Update a trigger. Currently only supported for triggers where `event_source.provider` is `github_oauth`, `github_app`, `github_server`, `bitbucket_dc`, `webhook`, or `schedule`. [Share feedback](https://circleci.canny.io/cloud-feature-requests/p/project-administration-apis) about our Project Administration APIs.
* **Update Webhook** `updateWebhook`: Updates an existing outbound webhook by its unique ID.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Job Completed | `job-completed` | Fires when an individual job reaches a terminal state (success, failed, canceled or unauthorized). CircleCI registers outbound webhooks per project, so the projectId input must be set to the project UUID from Project Settings &gt; Overview. The delivered payload names the event in its type field. |
| Workflow Completed | `workflow-completed` | Fires when a workflow reaches a terminal state (success, failed, error, canceled or unauthorized). CircleCI registers outbound webhooks per project, so the projectId input must be set to the project UUID from Project Settings &gt; Overview. The delivered payload names the event in its type field. |
