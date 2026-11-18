---
description: "E2B provides secure cloud sandboxes (isolated Linux VMs) for AI agents and code execution."
hidden: true
---

# E2B

<img src="../../.gitbook/assets/connectors/e2b.png" alt="E2B logo" width="64">

E2B provides secure cloud sandboxes (isolated Linux VMs) for AI agents and code execution. This connector covers the full E2B public API: sandbox lifecycle (create, list, get, connect, pause, resume, fork, timeout, refresh, network, kill), sandbox logs and metrics, snapshots, templates and builds, tags, volumes, team metrics, project secrets, the in-sandbox envd API (health, stats, environment, file download and upload, filesystem operations, process control) and sandbox lifecycle events with webhook management.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [e2b.dev](https://e2b.dev) |
| **Authentication** | API key |
| **Slug** | `e2b` |

## Use it

Add E2B from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.e2b.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Assign Template Tags | `assignTemplateTags` | Assigns one or more tags to a template build given as name:tag. |
| Check Sandbox Health | `checkSandboxHealth` | Checks that the envd service inside a running sandbox is healthy (204 No Content when healthy). |
| Close Process Stdin | `closeProcessStdin` | Closes stdin of a running sandbox process to signal end of input (non-PTY processes only). |
| Connect To Sandbox | `connectToSandbox` | Returns sandbox details and extends its time to live; a paused sandbox is resumed. |
| Create Filesystem Watcher | `createFilesystemWatcher` | Creates a non-streaming filesystem watcher on a sandbox path; poll it with Get Watcher Events and remove it with Remove Filesystem Watcher. |
| Create Sandbox | `createSandbox` | Creates a new sandbox from a template with the given timeout, network, metadata, environment variables and volume mounts. Returns the sandbox id and, for secure sandboxes, the envd access token used by the sandbox-level actions. Running sandboxes consume compute. |
| Create Secret | `createSecret` | Creates a project secret by storing a runtime marker as its first version; the response carries metadata only. |
| Create Snapshot | `createSnapshot` | Creates a persistent snapshot template from the sandbox current state; snapshots can be used to create new sandboxes and outlive the sandbox. |
| Create Template | `createTemplate` | Creates a new template (v3) with an optional name, tags, CPU and memory. Returns the template id and initial build id; use Start Build to build it. |
| Create Volume | `createVolume` | Creates a team volume and returns its id and content access token. |

<details>

<summary>See 60 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Webhook | `createWebhook` | Registers a webhook that receives sandbox lifecycle events for the project at the given HTTPS URL, signed with the provided secret (at least 32 characters). |
| Delete Secret | `deleteSecret` | Revokes a secret and schedules its versions for cleanup. Returns no content on success. |
| Delete Template | `deleteTemplate` | Deletes a template by id. Returns no content on success. |
| Delete Template Tags | `deleteTemplateTags` | Deletes one or more tags from a template. Returns no content on success. |
| Delete Volume | `deleteVolume` | Deletes a team volume by id. Returns no content on success. |
| Delete Webhook | `deleteWebhook` | Unregisters a sandbox lifecycle webhook by id. |
| Download Sandbox File | `downloadSandboxFile` | Downloads a file from a running sandbox by path (relative paths resolve to the user home directory). Returns the raw file content. |
| Fork Sandbox | `forkSandbox` | Checkpoints a running sandbox and creates one or more new sandboxes from that snapshot. Returns one result per requested fork. |
| Get Build Logs | `getBuildLogs` | Returns structured template build logs with cursor, direction, level and source filters. |
| Get Build Status | `getBuildStatus` | Returns the status and logs of a template build, with log offset, limit and level filters. |
| Get Build Upload Link | `getBuildUploadLink` | Returns an upload URL for a tar file of build layer files identified by its hash, or whether it is already cached. |
| Get Sandbox | `getSandbox` | Returns a sandbox by id, including state, resources, network configuration, lifecycle policy and (for secure sandboxes) the envd access token. |
| Get Sandbox Environment Variables | `getSandboxEnvironmentVariables` | Returns the environment variables set inside a running sandbox (envd /envs) as a name-to-value map. |
| Get Sandbox Lifecycle Events | `getSandboxLifecycleEvents` | Lists the lifecycle events of one sandbox with offset, limit, order and a single event-type filter. Events are retained for 7 days. |
| Get Sandbox Logs | `getSandboxLogs` | Returns structured sandbox logs with cursor, direction, level and search filters. |
| Get Sandbox Logs (Legacy) | `getSandboxLogsLegacy` | Returns sandbox logs from a start timestamp. Legacy endpoint; prefer Get Sandbox Logs. |
| Get Sandbox Metrics | `getSandboxMetrics` | Returns CPU, memory and disk metrics of a sandbox over an optional Unix-timestamp interval. |
| Get Sandbox Resource Stats | `getSandboxResourceStats` | Returns live CPU, memory and disk usage from inside a running sandbox (envd /metrics). |
| Get Secret | `getSecret` | Returns the metadata of one secret by id or name; never the value. |
| Get Team Metrics | `getTeamMetrics` | Returns concurrent-sandbox and sandbox-start-rate metrics of a team over an optional Unix-timestamp interval. |
| Get Team Metrics Max | `getTeamMetricsMax` | Returns the maximum value of a team metric (concurrent_sandboxes or sandbox_start_rate) in the given interval. |
| Get Template | `getTemplate` | Returns a template with all of its builds, with cursor pagination. |
| Get Template By Alias | `getTemplateByAlias` | Checks whether a template with the given alias exists and returns its id and visibility. |
| Get Volume | `getVolume` | Returns a team volume by id, including its content access token. |
| Get Watcher Events | `getWatcherEvents` | Returns the filesystem events collected by a watcher since the last call. |
| Get Webhook | `getWebhook` | Returns the configuration of a sandbox lifecycle webhook by id. |
| Kill Sandbox | `killSandbox` | Kills (terminates) a sandbox by id. Returns no content on success. |
| List Running Sandboxes (Legacy) | `listRunningSandboxes` | Lists all running sandboxes of the team, optionally filtered by metadata. Legacy endpoint; prefer List Sandboxes. |
| List Sandbox Directory | `listSandboxDirectory` | Lists the entries of a directory inside a running sandbox, optionally recursing to the given depth. |
| List Sandbox Lifecycle Events | `listSandboxLifecycleEvents` | Lists the latest sandbox lifecycle events (created, updated, paused, resumed, checkpointed, killed) for all sandboxes of the project, with offset, limit, order and a single event-type filter. Events are retained for 7 days. |
| List Sandbox Metrics | `listSandboxMetrics` | Returns the latest resource metrics for the given sandbox ids (comma-separated). |
| List Sandbox Processes | `listSandboxProcesses` | Lists the processes started through envd in a running sandbox. |
| List Sandboxes | `listSandboxes` | Lists the team sandboxes with metadata, state, order, startedAfter and template filters and cursor pagination. |
| List Secrets | `listSecrets` | Lists the project secrets (metadata only, never values) with cursor pagination. |
| List Snapshots | `listSnapshots` | Lists the team snapshots with optional sandbox id and name filters and cursor pagination. |
| List Teams | `listTeams` | Lists the teams of the authenticated user with their API keys. This endpoint requires a personal access token (Bearer, from the E2B dashboard) supplied as input rather than the team API key. |
| List Template Tags | `listTemplateTags` | Lists the tags of a template with their build ids. |
| List Templates | `listTemplates` | Lists the team templates (v2) with cursor pagination. |
| List Templates (Legacy) | `listTemplatesLegacy` | Lists the team templates. Legacy endpoint; prefer List Templates. |
| List Volumes | `listVolumes` | Lists the team volumes. |
| List Webhooks | `listWebhooks` | Lists the sandbox lifecycle webhooks registered for the project. |
| Make Sandbox Directory | `makeSandboxDirectory` | Creates a directory (and parents) inside a running sandbox. |
| Move Sandbox Path | `moveSandboxPath` | Moves or renames a file or directory inside a running sandbox. |
| Pause Sandbox | `pauseSandbox` | Pauses a running sandbox, capturing a full memory snapshot by default (memory=false persists only the filesystem). Returns no content on success. |
| Refresh Sandbox | `refreshSandbox` | Extends the time to live of a sandbox by the given duration in seconds (max 3600). Returns no content on success. |
| Remove Filesystem Watcher | `removeFilesystemWatcher` | Removes a filesystem watcher created with Create Filesystem Watcher. Returns an empty object on success. |
| Remove Sandbox Path | `removeSandboxPath` | Removes a file or directory inside a running sandbox. Returns an empty object on success. |
| Resume Sandbox | `resumeSandbox` | Resumes a paused sandbox with a new timeout, optionally from disk state only. |
| Send Process Input | `sendProcessInput` | Sends stdin or PTY input (base64-encoded bytes) to a running sandbox process selected by pid or tag. |
| Send Process Signal | `sendProcessSignal` | Sends SIGTERM or SIGKILL to a running sandbox process selected by pid or tag. |
| Set Sandbox Timeout | `setSandboxTimeout` | Sets the sandbox time to live to the given number of seconds from now, overwriting the previous TTL. Returns no content on success. |
| Start Build | `startBuild` | Starts a template build (v2) from a base image or template with build steps, optional registry credentials, start and ready commands. Returns no content on success (202). |
| Stat Sandbox Path | `statSandboxPath` | Returns the entry information (type, size, permissions, owner, modified time, metadata) of a path inside a running sandbox. |
| Update Process | `updateProcess` | Updates a running sandbox process, e.g. resizes its PTY. |
| Update Sandbox Network | `updateSandboxNetwork` | Replaces the egress network configuration (allow/deny lists, SOCKS5 proxy, per-domain rules, internet access) of a running sandbox. Omitted fields are cleared. Returns no content on success. |
| Update Secret | `updateSecret` | Appends a new version to a secret with a new runtime marker and optional metadata. |
| Update Template | `updateTemplate` | Updates whether a template is public or team-only (v2). |
| Update Template (Legacy) | `updateTemplateLegacy` | Updates whether a template is public. Legacy endpoint; prefer Update Template. |
| Update Webhook | `updateWebhook` | Updates a sandbox lifecycle webhook; provided fields replace the previous configuration. |
| Upload Sandbox File | `uploadSandboxFile` | Writes text content to a file in a running sandbox at the given path, creating parent directories and overwriting an existing file. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Sandbox checkpointed | `sandbox.lifecycle.checkpointed` | A snapshot/fork checkpoint of the sandbox was taken. Captured live 2026-09-15. |
| Sandbox created | `sandbox.lifecycle.created` | A sandbox was created. Payload modelled from the vendor's lifecycle event record returned by GET /events/sandboxes (captured live on 2026-09-15); webhook delivery body has the same shape (id, type, version, timestamp, sandboxId, sandboxTemplateId, sandboxBuildId, sandboxTeamId, sandboxExecutionId, eventCategory, eventLabel, eventData). |
| Sandbox killed | `sandbox.lifecycle.killed` | A sandbox was killed (explicit kill or timeout). eventData carries execution stats and kill_reason. Captured live from GET /events/sandboxes on 2026-09-15. |
| Sandbox paused | `sandbox.lifecycle.paused` | A sandbox was paused. Captured live 2026-09-15. |
| Sandbox resumed | `sandbox.lifecycle.resumed` | A paused sandbox was resumed. Captured live 2026-09-15. |
| Sandbox updated | `sandbox.lifecycle.updated` | Sandbox timeout or network config changed (eventData.set_timeout or eventData.network_egress). Captured live 2026-09-15. |
