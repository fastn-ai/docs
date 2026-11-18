---
description: "Buildkite is a CI/CD platform that runs build pipelines on your own or Buildkite-hosted agents."
hidden: true
---

# Buildkite

<img src="../../.gitbook/assets/connectors/buildkite.png" alt="Buildkite logo" width="64">

Buildkite is a CI/CD platform that runs build pipelines on your own or Buildkite-hosted agents. This connector covers the Buildkite REST API v2: organizations, members, invitations, API and pipeline settings, notification services, repository connections and audit events; pipelines, pipeline schedules, pipeline templates and rules; builds, jobs, job logs, job environment variables, annotations and artifacts; agents; clusters with their queues, agent tokens, agent images, secrets, maintainers, network ranges and cache volumes; teams with their members, pipelines and suites; package registries, registry tokens and packages; Test Engine suites, tests, runs, quarantine and execution tags; plus emojis, rate limits, meta information and access-token management.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [buildkite.com](https://buildkite.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `buildkite` |

## Use it

Add Buildkite from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.buildkite.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Team Member | `createTeamMember` | Adds an existing organization member to a team with the given role. |
| Add Team Pipeline | `createTeamPipeline` | Grants a team access to a pipeline at the given access level. |
| Add Team Suite | `createTeamSuite` | Grants a team access to a Test Engine suite at the given access level. |
| Archive Pipeline | `archivePipeline` | Archives a pipeline. Archived pipelines are hidden from the pipeline list and cannot run new builds, but their build history is retained. |
| Cancel Build | `cancelBuild` | Cancels a build that is scheduled or running, stopping any of its jobs that have not finished. |
| Configure Build Export | `configureBuildExport` | Enables build exports for the organization and sets the destination bucket and storage strategy. Requires a plan that includes build exports. |
| Copy Package | `copyPackage` | Copies a package from one registry to another registry in the same organization. Both registries must use the same package ecosystem. |
| Create Agent Image | `createAgentImage` | Creates a custom hosted agent image for a cluster by layering a Dockerfile on top of the Buildkite-managed base image. The Dockerfile must not contain a FROM instruction. |
| Create Agent Token | `createAgentToken` | Creates an agent token that agents use to register with a cluster. The token secret is returned once, in this response only, so store it immediately. |
| Create Build | `createBuild` | Triggers a new build on a pipeline for the given commit and branch. |

<details>

<summary>See 180 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Build Annotation | `createBuildAnnotation` | Creates an annotation on a build, shown at the top of the build page. Reuse a context value with Append to add to an existing annotation instead of creating another one. |
| Create Cluster | `createCluster` | Creates a cluster to group agent queues, agent tokens and the pipelines permitted to run on them. |
| Create Cluster Maintainer | `createClusterMaintainer` | Grants cluster maintainer permissions to a user or a team. Supply either User UUID or Team UUID, not both. |
| Create Hosted Queue | `createHostedQueue` | Creates a queue in a cluster that runs on Buildkite hosted agents, specifying the machine instance shape jobs run on. To create a queue for your own agents, use Create Self-Hosted Queue instead. |
| Create Job Annotation | `createJobAnnotation` | Creates an annotation scoped to a single job, shown against that job on the build page. |
| Create Notification Service | `createNotificationService` | Creates a notification service that delivers build and job notifications to an external system. OAuth-managed Slack workspace and Linear services must first be connected in the Buildkite interface, but can then be managed through this connector. |
| Create Organization Invitations | `createOrganizationInvitations` | Invites one or more people to join the organization by email, optionally assigning an organization role, an SSO requirement and team memberships. |
| Create Pipeline | `createPipeline` | Creates a pipeline in the organization. Supply the build steps either as a YAML string in Configuration (recommended) or as a Steps array for the legacy visual step format. A pipeline that uses a pipeline template for its steps does not need either. |
| Create Pipeline Schedule | `createPipelineSchedule` | Creates a schedule that automatically triggers builds on a pipeline at a recurring interval. |
| Create Pipeline Template | `createPipelineTemplate` | Creates a pipeline template containing a reusable YAML step configuration that pipelines in the organization can be assigned to. |
| Create Pipeline Webhook | `createPipelineWebhook` | Creates the webhook on the pipeline's connected source-control provider so that pushes to the repository trigger Buildkite builds. The provider connection must already be configured on the organization. |
| Create Portal | `createPortal` | Creates a portal that exposes a single saved GraphQL query or mutation behind a dedicated endpoint, so callers can run it without full GraphQL API access. |
| Create Registry | `createRegistry` | Creates a package registry for a given package ecosystem, which packages can then be published to and installed from. |
| Create Registry Token | `createRegistryToken` | Creates an access token for a package registry, used to authenticate package publishes and installs. The token value is returned once, in this response only. |
| Create Rule | `createRule` | Creates a rule granting one pipeline permission to trigger builds on, or read artifacts from, another pipeline. |
| Create Secret | `createSecret` | Creates a Buildkite secret in a cluster. The value is encrypted at rest and can only be read by builds that satisfy the access policy. |
| Create Self-Hosted Queue | `createSelfHostedQueue` | Creates a queue in a cluster that your own self-hosted Buildkite agents connect to. To create a queue that runs on Buildkite hosted agents, use Create Hosted Queue instead. |
| Create Team | `createTeam` | Creates a team in the organization. Teams control which members can access which pipelines, suites and registries. |
| Create Test Suite | `createTestSuite` | Creates a Test Engine suite that test collectors can upload run data to. |
| Delete Agent Image | `deleteAgentImage` | Deletes a custom hosted agent image from a cluster. Queues currently using the image fall back to the Buildkite-managed base image. |
| Delete Artifact | `deleteArtifact` | Permanently deletes an artifact's stored contents. The artifact record remains but moves to the deleted state. |
| Delete Build Annotation | `deleteBuildAnnotation` | Deletes a build-scoped annotation. |
| Delete Cache Volume | `deleteCacheVolume` | Deletes a hosted agent cache volume identified by its cache tag, clearing the cached data so the next build repopulates it. |
| Delete Cluster | `deleteCluster` | Deletes a cluster along with its queues and agent tokens. Pipelines assigned to the cluster must be moved first. |
| Delete Job Annotation | `deleteJobAnnotation` | Deletes a job-scoped annotation. |
| Delete Job Log | `deleteJobLog` | Permanently deletes a job's log output. The job itself is retained but its log can no longer be read. |
| Delete Notification Service | `deleteNotificationService` | Deletes a notification service and removes its provider configuration. |
| Delete Package | `deletePackage` | Permanently deletes a package from a registry. Consumers that pinned this exact version will no longer be able to install it. |
| Delete Pipeline | `deletePipeline` | Permanently deletes a pipeline and all of its builds. This cannot be undone; consider archiving the pipeline instead. |
| Delete Pipeline GitHub Webhooks | `deletePipelineGitHubWebhooks` | Removes the Buildkite GitHub webhooks from the pipeline's repository so pushes no longer trigger builds. |
| Delete Pipeline Schedule | `deletePipelineSchedule` | Deletes a pipeline build schedule so it stops triggering builds. |
| Delete Pipeline Template | `deletePipelineTemplate` | Deletes a pipeline template. Pipelines currently assigned to the template must be reassigned first. |
| Delete Portal | `deletePortal` | Deletes a portal so its endpoint stops accepting requests. |
| Delete Queue | `deleteQueue` | Deletes a queue from a cluster. A cluster's default queue cannot be deleted until another queue is made the default. |
| Delete Registry | `deleteRegistry` | Deletes a package registry and every package stored in it. This cannot be undone. |
| Delete Registry Token | `deleteRegistryToken` | Deletes a package registry token so it can no longer authenticate publishes or installs. |
| Delete Rule | `deleteRule` | Deletes an organization rule, revoking the cross-pipeline permission it granted. |
| Delete Secret | `deleteSecret` | Deletes a Buildkite secret from a cluster. Builds referencing the secret key will fail until it is recreated. |
| Delete Team | `deleteTeam` | Deletes a team. Its members lose the access the team granted them, but their organization memberships are unaffected. |
| Delete Test Suite | `deleteTestSuite` | Deletes a Test Engine suite along with its collected run and test data. This cannot be undone. |
| Disable Build Export | `disableBuildExport` | Disables build exports for the organization. Returns the full pipeline settings resource. |
| Disable Hosted Agents Terminal Access | `disableHostedAgentsTerminalAccess` | Disables SSH terminal access for Buildkite hosted agents across the organization. Returns the full pipeline settings resource. |
| Disable Notification Service | `disableNotificationService` | Disables a notification service so it stops delivering notifications, without deleting its configuration. Returns the updated notification service. |
| Disable Public Pipeline Creation | `disablePublicPipelineCreation` | Prevents organization members from creating pipelines that are visible outside the organization. Returns the full pipeline settings resource. |
| Download Artifact | `downloadArtifact` | Returns a short-lived, pre-signed URL that the artifact's binary contents can be downloaded from. Buildkite responds with a redirect to storage rather than the file itself. |
| Enable Advanced Queue Metrics | `enableAdvancedQueueMetrics` | Enables advanced queue metrics for the organization's clusters. This is a one-way operation: once enabled it cannot be disabled through the API. Returns the full pipeline settings resource. |
| Enable Hosted Agents Terminal Access | `enableHostedAgentsTerminalAccess` | Enables SSH terminal access for Buildkite hosted agents across the organization and records who enabled it. Returns the full pipeline settings resource. |
| Enable Notification Service | `enableNotificationService` | Enables a notification service and clears any previous disabled or broken state. Returns the updated notification service. |
| Enable Public Pipeline Creation | `enablePublicPipelineCreation` | Allows organization members to create pipelines that are visible outside the organization. Returns the full pipeline settings resource. |
| Enable Teams | `enableTeams` | Turns on the Teams feature for the organization, after which pipeline, suite and registry access is governed by team membership. This cannot be undone through the API. |
| Enable Test | `enableTest` | Removes a test from quarantine so it runs normally again and its failures count against the build. Requires a Pro or Enterprise plan with test state management enabled on the suite. |
| Find Test | `findTest` | Looks up a test by its scope and name so you can recover its UUID when you only know how the test is identified in your test suite. |
| Get Access Token | `getAccessToken` | Retrieves the details of the API access token used by this connection, including the REST API scopes it was granted and its expiry. |
| Get Agent | `getAgent` | Retrieves a single agent by its UUID. Unlike the list action this returns agents in any connection state, including disconnected and lost ones. |
| Get Agent Image | `getAgentImage` | Retrieves a single hosted agent image by its UUID. |
| Get Agent Token | `getAgentToken` | Retrieves a single cluster agent token by its UUID. The token secret itself is only returned when the token is created. |
| Get API Settings | `getApiSettings` | Retrieves the organization's API security settings, mirroring the Security &gt; API settings page in Buildkite. Requires an organization administrator and the read_organization_settings scope. |
| Get Artifact | `getArtifact` | Retrieves the metadata of a single artifact, including its path, size, MIME type, checksums and download URL. |
| Get Audit Event | `getAuditEvent` | Retrieves a single audit log entry by its UUID. Requires the read_audit_events scope and a plan that includes audit logging. |
| Get Build | `getBuild` | Retrieves a single build by its number within a pipeline, including its jobs unless you exclude them. |
| Get Cluster | `getCluster` | Retrieves a single cluster by its UUID, including its default queue and maintainers. |
| Get Cluster Maintainer | `getClusterMaintainer` | Retrieves a single cluster maintainer assignment by its UUID. |
| Get Current User | `getCurrentUser` | Retrieves the Buildkite user account that owns the API access token used by this connection. |
| Get Job | `getJob` | Retrieves a single job by its UUID. Job UUIDs are unique across the organization, so the pipeline and build do not need to be supplied. |
| Get Job Environment Variables | `getJobEnvironmentVariables` | Retrieves the environment variables that were set on a job when it ran, including the BUILDKITE_* variables the agent injected. |
| Get Job Log | `getJobLog` | Retrieves the log output of a job, including its ANSI escape sequences and timestamp markers. |
| Get Meta Information | `getMetaInformation` | Retrieves Buildkite service metadata, including the list of source IP addresses that Buildkite delivers webhooks from. Use these addresses to allowlist Buildkite webhook traffic. |
| Get Notification Service | `getNotificationService` | Retrieves a single notification service by its UUID. |
| Get Organization | `getOrganization` | Retrieves the Buildkite organization configured on this connection. |
| Get Organization Invitation | `getOrganizationInvitation` | Retrieves a single organization invitation by its UUID. Unlike the list action, this returns invitations in any state, including accepted and revoked ones. |
| Get Organization Member | `getOrganizationMember` | Retrieves a single organization member by their user UUID. |
| Get Package | `getPackage` | Retrieves the details of a single package by its UUID, including its version, size and download URL. |
| Get Pipeline | `getPipeline` | Retrieves a single pipeline by its slug, including its YAML configuration, provider settings and build counts. |
| Get Pipeline GitHub Webhooks | `getPipelineGitHubWebhooks` | Retrieves the GitHub webhooks registered on the pipeline's repository, so you can confirm whether GitHub is configured to trigger Buildkite builds. |
| Get Pipeline Schedule | `getPipelineSchedule` | Retrieves a single pipeline build schedule by its UUID. |
| Get Pipeline Settings | `getPipelineSettings` | Retrieves the organization-level pipeline settings, including default branch, default cluster, timeouts, hosted agent terminal access, public pipeline creation, advanced queue metrics and build exports. Requires an organization administrator. |
| Get Pipeline Template | `getPipelineTemplate` | Retrieves a single pipeline template by its UUID. |
| Get Portal | `getPortal` | Retrieves a single portal by its slug, including the GraphQL query it executes. |
| Get Queue | `getQueue` | Retrieves a single cluster queue by its UUID, including its hosted agent instance shape when it is a Buildkite hosted queue. |
| Get Rate Limits | `getRateLimits` | Retrieves the current REST and GraphQL API rate-limit usage for the organization, including the limit, the amount consumed and when the window resets. |
| Get Registry | `getRegistry` | Retrieves a single package registry by its slug. |
| Get Registry Token | `getRegistryToken` | Retrieves a single registry token by its UUID. The token secret is only returned when the token is created. |
| Get Repository Connection | `getRepositoryConnection` | Retrieves a single source-control repository connection by its ID. |
| Get Rule | `getRule` | Retrieves a single organization rule by its UUID. |
| Get Secret | `getSecret` | Retrieves a single cluster secret's metadata by its UUID. The encrypted value is never returned. |
| Get Team | `getTeam` | Retrieves a single team by its UUID, including its privacy setting and member permissions. |
| Get Team Member | `getTeamMember` | Retrieves a single team membership by the member's user UUID. |
| Get Team Pipeline | `getTeamPipeline` | Retrieves a single team pipeline association by the pipeline's UUID. |
| Get Team Suite | `getTeamSuite` | Retrieves a single team suite association by the suite's UUID. |
| Get Test | `getTest` | Retrieves a single test in a Test Engine suite by its UUID. |
| Get Test Run | `getTestRun` | Retrieves a single Test Engine run by its UUID. |
| Get Test Suite | `getTestSuite` | Retrieves a single Test Engine suite by its slug. |
| List Agent Images | `listAgentImages` | Lists the custom hosted agent images defined on a cluster. Each image layers a Dockerfile on top of the Buildkite-managed base image. |
| List Agent Tokens | `listAgentTokens` | Lists the agent tokens belonging to a cluster. Agents present one of these tokens to register with the cluster. |
| List Agents | `listAgents` | Lists the organization's connected and stopping agents. Agents in other connection states are not returned; use Get Agent to look one of those up by ID. |
| List All Builds | `listAllBuilds` | Lists builds across every organization the API access token can reach, newest first. Use the filters to narrow by branch, commit, state, creator or creation time. |
| List Audit Events | `listAuditEvents` | Lists the organization's audit log entries, newest first. Requires the read_audit_events scope and a plan that includes audit logging. |
| List Build Annotations | `listBuildAnnotations` | Lists the annotations attached to a build. By default only build-scoped annotations are returned; use Scope to include job-scoped ones. |
| List Build Artifacts | `listBuildArtifacts` | Lists every artifact uploaded by any job in a build. |
| List Build Jobs | `listBuildJobs` | Lists the jobs in a build, with optional filtering by job state, step key or group key. |
| List Builds For A Pipeline | `listPipelineBuilds` | Lists the builds of a single pipeline, newest first. Use the filters to narrow by branch, commit, state, creator or creation time. |
| List Cache Volumes | `listCacheVolumes` | Lists the hosted agent cache volumes in a cluster, with their tags and current sizes. |
| List Cluster Maintainers | `listClusterMaintainers` | Lists the users and teams granted maintainer permissions on a cluster. Maintainers can manage the cluster's queues, tokens and settings. |
| List Cluster Network Ranges | `listClusterNetworkRanges` | Lists the outbound IP ranges that Buildkite hosted agents in this cluster make network requests from. Use these to allowlist hosted agent traffic in your own systems. |
| List Clusters | `listClusters` | Lists the organization's clusters. A cluster groups agent queues, agent tokens and the pipelines allowed to run on them. |
| List Emojis | `listEmojis` | Lists every emoji available in the organization, including Buildkite's built-in emoji and any custom emoji the organization has uploaded. Emoji names are used in the :emoji: syntax accepted by pipeline, cluster and annotation fields. |
| List Flaky Tests | `listFlakyTests` | Lists the tests in a Test Engine suite that Buildkite has detected as flaky over a given period. Buildkite has deprecated this endpoint in favour of List Tests with the flaky label filter. |
| List Job Annotations | `listJobAnnotations` | Lists the annotations scoped to a single job. |
| List Job Artifacts | `listJobArtifacts` | Lists the artifacts uploaded by a single job. |
| List Muted Tests | `listMutedTests` | Lists the tests currently muted in a Test Engine suite. Use this to configure your test runner to ignore their failures. |
| List Notification Services | `listNotificationServices` | Lists the organization's notification services, oldest first. These are the integrations that deliver build and job notifications to Slack, webhooks, Amazon EventBridge, Datadog and OpenTelemetry. |
| List Organization Builds | `listOrganizationBuilds` | Lists builds across every pipeline in the organization, newest first. Use the filters to narrow by branch, commit, state, creator or creation time. |
| List Organization Invitations | `listOrganizationInvitations` | Lists the organization's pending member invitations, oldest first. Requires the read_organization_invitations scope and permission to invite organization members. |
| List Organization Members | `listOrganizationMembers` | Lists every member of the organization, with their organization role and SSO requirement. |
| List Organizations | `listOrganizations` | Lists every Buildkite organization the API access token can reach. Use this to discover the slug of an organization other than the one configured on this connection. |
| List Packages | `listPackages` | Lists the packages stored in a registry, optionally filtered by package name. |
| List Pipeline Schedules | `listPipelineSchedules` | Lists the build schedules configured on a pipeline, including their cron expressions and the time of the next scheduled build. |
| List Pipeline Templates | `listPipelineTemplates` | Lists the organization's pipeline templates, which define reusable YAML step configurations that pipelines can be locked to. Requires a plan with pipeline templates enabled. |
| List Pipelines | `listPipelines` | Lists the organization's pipelines, optionally filtered by name or repository URL. |
| List Portals | `listPortals` | Lists the organization's portals. A portal exposes a single saved GraphQL query or mutation behind a dedicated, token-authenticated endpoint. |
| List Queues | `listQueues` | Lists the queues in a cluster. Agents register against a queue key, and pipeline steps target a queue through their agent tags. |
| List Registries | `listRegistries` | Lists the organization's package registries across every supported package ecosystem. |
| List Registry Tokens | `listRegistryTokens` | Lists the access tokens issued for a package registry. |
| List Repositories For A Connection | `listConnectionRepositories` | Lists the repositories available through a source-control repository connection, so you can pick one when creating a pipeline. |
| List Repository Connections | `listRepositoryConnections` | Lists the source-control provider connections configured on the organization, such as GitHub or GitLab installations that pipelines can build repositories from. |
| List Rules | `listRules` | Lists the organization's rules, which grant one pipeline permission to trigger builds on, or read artifacts from, another pipeline. |
| List Run Failed Executions | `listRunFailedExecutions` | Lists the individual test executions that failed within a Test Engine run, including their failure reasons and expanded failure output. |
| List Secrets | `listSecrets` | Lists the Buildkite secrets stored in a cluster. Secret values are never returned; only their keys, descriptions and access policies. |
| List Skipped Tests | `listSkippedTests` | Lists the tests currently skipped in a Test Engine suite. Use this to configure your test runner to skip them. Buildkite exposes this listing over PUT rather than GET. |
| List Team Members | `listTeamMembers` | Lists the members of a team and the role each of them holds within it. |
| List Team Pipelines | `listTeamPipelines` | Lists the pipelines a team has access to, with the access level granted for each. |
| List Team Suites | `listTeamSuites` | Lists the Test Engine suites a team has access to, with the access level granted for each. |
| List Teams | `listTeams` | Lists the organization's teams. Requires the organization to have Teams enabled. |
| List Test Runs | `listTestRuns` | Lists the test runs recorded in a Test Engine suite, optionally filtered to the runs belonging to a single build. |
| List Test Suites | `listTestSuites` | Lists the organization's Test Engine suites, which collect test run data uploaded by test collectors. |
| List Tests | `listTests` | Lists the tests recorded in a Test Engine suite, optionally filtered by label. |
| Mute Test | `muteTest` | Quarantines a test by marking it muted, so it still runs but its failures no longer fail the build. Requires a Pro or Enterprise plan with test state management enabled on the suite. |
| Pause Agent | `pauseAgent` | Pauses an agent so no further jobs are dispatched to it, while instructing it to stay running after its current job finishes. Only connected agents can be paused. |
| Pause Queue Dispatch | `pauseQueueDispatch` | Pauses job dispatch to a queue so no further jobs are handed to its agents. Jobs already running continue to completion. |
| Rebuild Build | `rebuildBuild` | Creates a new build that reruns an existing build with the same commit, branch and environment. Returns the new build. |
| Remove Cluster Maintainer | `deleteClusterMaintainer` | Removes cluster maintainer permissions from a user or team. |
| Remove Organization Member | `removeOrganizationMember` | Removes a member from the organization. You cannot remove your own membership. |
| Remove Team Member | `deleteTeamMember` | Removes a member from a team. Their organization membership is unaffected. |
| Remove Team Pipeline | `deleteTeamPipeline` | Removes a team's access to a pipeline. The pipeline itself is not deleted. |
| Remove Team Suite | `deleteTeamSuite` | Removes a team's access to a Test Engine suite. The suite itself is not deleted. |
| Reprioritize Job | `reprioritizeJob` | Changes the dispatch priority of a scheduled job. Higher values are dispatched to agents first. |
| Resume Agent | `resumeAgent` | Resumes a paused agent so Buildkite starts dispatching jobs to it again. |
| Resume Queue Dispatch | `resumeQueueDispatch` | Resumes job dispatch to a paused queue so its agents start receiving jobs again. |
| Retry Failed Jobs | `retryFailedJobs` | Retries the failed jobs in a build. By default every retryable failed job is retried; use States to retry only particular failure types. Buildkite accepts this request asynchronously and returns 202. |
| Retry Job | `retryJob` | Retries a failed or timed-out job, creating a new job execution for the same step. Returns the new job. |
| Revoke Access Token | `revokeAccessToken` | Permanently revokes the API access token used by this connection. This immediately breaks the connection and every other integration using the same token, and the token cannot be restored. Issue a replacement token in Buildkite before running this action. |
| Revoke Agent Token | `revokeAgentToken` | Revokes a cluster agent token. Agents configured with the token can no longer connect, and the token cannot be restored. |
| Revoke Organization Invitation | `revokeOrganizationInvitation` | Revokes a pending organization invitation so the invitee can no longer accept it. Only invitations in the pending state can be revoked. |
| Skip Test | `skipTest` | Quarantines a test by marking it skipped, so test runners configured for quarantine stop executing it. Requires a Pro or Enterprise plan with test state management enabled on the suite. |
| Stop Agent | `stopAgent` | Instructs an agent to disconnect. By default any job the agent is currently running, and that job's build, are canceled; set Force to false to let the current job finish first. |
| Unarchive Pipeline | `unarchivePipeline` | Restores an archived pipeline so it appears in the pipeline list and can run builds again. |
| Unblock Job | `unblockJob` | Unblocks a block step so the build can continue, optionally supplying values for the block step's input fields. |
| Update Agent Token | `updateAgentToken` | Updates a cluster agent token's description, expiry or allowed IP addresses. Only the fields you supply are changed. |
| Update API Settings | `updateApiSettings` | Updates the organization's API security settings. Only the fields you supply are changed. Note that writing an IP allowlist takes effect immediately, so a range that excludes your own address will lock out subsequent API calls. |
| Update Cluster | `updateCluster` | Updates a cluster's name, description, emoji, colour or default queue. Only the fields you supply are changed. |
| Update Execution Tags | `updateExecutionTags` | Bulk-replaces the mutable tags on Test Engine executions. Every tag key must start with the mut. prefix, and all mutable tags on each listed execution are replaced by the set you supply. Send an empty tag map to clear an execution's mutable tags. Rate limited to one request per minute. |
| Update Notification Service | `updateNotificationService` | Updates a notification service. Only the fields you supply are changed; omitted top-level fields and settings are left as they are. The provider of an existing service cannot be changed. |
| Update Organization Member | `updateOrganizationMember` | Updates an organization member's role or SSO requirement. You cannot update your own membership, and at least one of role or SSO mode must be supplied. |
| Update Pipeline | `updatePipeline` | Updates a pipeline. Only the fields you supply are changed, so this is safe to use for partial updates. |
| Update Pipeline GitHub Webhooks | `updatePipelineGitHubWebhooks` | Recreates the GitHub webhooks on the pipeline's repository, replacing any existing Buildkite webhook configuration. Use this to repair a webhook that has drifted or been removed in GitHub. |
| Update Pipeline Schedule | `updatePipelineSchedule` | Updates a pipeline build schedule. Only the fields you supply are changed. |
| Update Pipeline Settings | `updatePipelineSettings` | Updates the organization's default pipeline settings. Only the fields you supply are changed. |
| Update Pipeline Template | `updatePipelineTemplate` | Updates a pipeline template. Only the fields you supply are changed. |
| Update Portal | `updatePortal` | Updates a portal's name, slug, description, GraphQL query, IP allowlist or user-invokable setting. Only the fields you supply are changed. |
| Update Queue | `updateQueue` | Updates a cluster queue's description or retry agent affinity. Only the fields you supply are changed. |
| Update Registry | `updateRegistry` | Updates a package registry's name, description or OIDC policy. When modifying an OIDC policy, send the entire revised policy, not just the changed statements. |
| Update Registry Token | `updateRegistryToken` | Updates the description of a package registry token. |
| Update Secret | `updateSecret` | Updates a cluster secret's description and access policy. The key cannot be changed, and the value must be updated with Update Secret Value instead. |
| Update Secret Value | `updateSecretValue` | Replaces the encrypted value of a cluster secret. To change its description or access policy, use Update Secret instead. |
| Update Team | `updateTeam` | Updates a team's name, description, privacy or member permissions. Only the fields you supply are changed. |
| Update Team Member | `updateTeamMember` | Changes a team member's role between member and maintainer. |
| Update Team Pipeline | `updateTeamPipeline` | Changes the access level a team has to a pipeline. |
| Update Team Suite | `updateTeamSuite` | Changes the access level a team has to a Test Engine suite. |
| Update Test Labels | `updateTestLabels` | Adds labels to, or removes labels from, a test in a Test Engine suite. |
| Update Test Suite | `updateTestSuite` | Updates a Test Engine suite's name, default branch, appearance or OIDC policy. Only the fields you supply are changed. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Agent Blocked | `agent.blocked` | An agent has been blocked because its IP address is no longer in its agent token's allowed IP addresses. |
| Agent Connected | `agent.connected` | An agent has connected to the Buildkite agent API. |
| Agent Disconnected | `agent.disconnected` | An agent has shut down and disconnected from the agent API. |
| Agent Lost | `agent.lost` | An agent has been marked lost because Buildkite stopped receiving its pings. |
| Agent Stopped | `agent.stopped` | An agent has stopped, either gracefully or forcefully. |
| Agent Stopping | `agent.stopping` | An agent has been instructed to stop and is finishing its current job before disconnecting. |
| Agent Token Registration Blocked | `cluster_token.registration_blocked` | An agent registration attempt was rejected because the request IP address is not in the agent token's allowed IP addresses. |
| Build Failing | `build.failing` | A build has entered a failing state because one of its jobs failed, while other jobs are still running. |
| Build Finished | `build.finished` | A build has finished. Check the build state for the outcome, and blocked: true to tell a build waiting on a manual step apart from a completed one. |
| Build Running | `build.running` | A build has started running. |

<details>

<summary>See 8 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Build Scheduled | `build.scheduled` | A build has been scheduled and is waiting for an agent. |
| Build Skipped | `build.skipped` | A build has been skipped, which happens when intermediate build skipping is enabled and a newer build supersedes it. |
| Job Activated | `job.activated` | A block step job has been unblocked through the Buildkite interface or the API. |
| Job Finished | `job.finished` | A job has finished. For a trigger step, the job carries an async field showing whether the triggered build runs asynchronously. |
| Job Promised Exit Status | `job.promised_exit_status` | A running job has declared the exit status it expects to finish with, before it has actually finished. |
| Job Scheduled | `job.scheduled` | A job has been scheduled and is waiting to be dispatched to an agent. |
| Job Started | `job.started` | A command step job has started running on an agent. |
| Ping | `ping` | Sent when the webhook notification service settings are changed, and when the service is first created. Use it to confirm the endpoint is reachable. |

</details>
