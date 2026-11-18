---
description: "ClickHouse Cloud Management API for administering organizations, services, API keys, members, invitations, usage/cost, private endpoints, and backups on…"
hidden: true
---

# ClickHouse Cloud

<img src="../../.gitbook/assets/connectors/lg/clickhousecloud.png" alt="ClickHouse Cloud logo">

ClickHouse Cloud Management API for administering organizations, services, API keys, members, invitations, usage/cost, private endpoints, and backups on api.clickhouse.cloud.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [clickhouse.com](https://clickhouse.com) |
| **Authentication** | Basic auth |
| **Slug** | `clickhousecloud` |

## Use it

Add ClickHouse Cloud from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.clickhousecloud.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Attach UDF To Service | `attachUdf` | Attaches a user-defined function (UDF) version to a service, replacing the current version when necessary. When version is omitted, the latest ready version is attached. Beta endpoint. |
| ClickStack: Create Alert | `clickstackCreateAlert` | Creates a new ClickStack alert on a dashboard tile or a saved search, with a threshold, evaluation interval, and notification channel. Beta endpoint. |
| ClickStack: Create Dashboard | `clickstackCreateDashboard` | Creates a new ClickStack observability dashboard with a name and a list of chart tiles. Beta endpoint. |
| ClickStack: Create Role | `clickstackCreateRole` | Creates a new custom ClickStack team role with CASL permissions. Beta endpoint. |
| ClickStack: Create Saved Search | `clickstackCreateSavedSearch` | Creates a new saved log/trace search against a ClickStack source. Beta endpoint. |
| ClickStack: Create Source | `clickstackCreateSource` | Creates a new ClickStack data source. This generic action models a log source, the most common kind; trace, metric, session, and PromQL sources use additional kind-specific fields not exposed here. Beta endpoint. |
| ClickStack: Create Webhook | `clickstackCreateWebhook` | Creates a new ClickStack alert-notification webhook (Slack, incident.io, or generic) for the team on a service. Beta endpoint. |
| ClickStack: Delete Alert | `clickstackDeleteAlert` | Deletes a ClickStack alert. Beta endpoint. |
| ClickStack: Delete Dashboard | `clickstackDeleteDashboard` | Deletes a ClickStack dashboard. Beta endpoint. |
| ClickStack: Delete Role | `clickstackDeleteRole` | Deletes a custom ClickStack team role. Predefined roles, the team default role, and roles assigned to users cannot be deleted. Beta endpoint. |

<details>

<summary>See 135 more actions</summary>

* **ClickStack: Delete Saved Search** `clickstackDeleteSavedSearch`: Deletes a saved search and any alerts attached to it. Beta endpoint.
* **ClickStack: Delete Source** `clickstackDeleteSource`: Deletes a ClickStack data source. Beta endpoint.
* **ClickStack: Delete Webhook** `clickstackDeleteWebhook`: Deletes a ClickStack webhook. Blocked with a 409 while any alert still references it. Beta endpoint.
* **ClickStack: Get Alert** `clickstackGetAlert`: Returns a single ClickStack alert by ID. Beta endpoint.
* **ClickStack: Get Dashboard** `clickstackGetDashboard`: Returns a single ClickStack dashboard by ID. Beta endpoint.
* **ClickStack: Get Role** `clickstackGetRole`: Returns a single ClickStack team role by ID. Beta endpoint.
* **ClickStack: Get Saved Search** `clickstackGetSavedSearch`: Returns a single saved search by ID. Beta endpoint.
* **ClickStack: Get Source** `clickstackGetSource`: Returns a single ClickStack data source by ID. Beta endpoint.
* **ClickStack: List Alerts** `clickstackListAlerts`: Returns the ClickStack alerts configured for the team on a service, paginated. Beta endpoint.
* **ClickStack: List Dashboards** `clickstackListDashboards`: Returns every ClickStack observability dashboard for the team on a ClickHouse service. Beta endpoint.
* **ClickStack: List Roles** `clickstackListRoles`: Returns every role for the team on a service, including predefined roles. Beta endpoint.
* **ClickStack: List Saved Searches** `clickstackListSavedSearches`: Returns the saved log/trace searches for the team on a service, paginated. Beta endpoint.
* **ClickStack: List Sources** `clickstackListSources`: Returns every ClickStack data source (log, trace, metric, session, or PromQL) configured for the team on a service. Beta endpoint.
* **ClickStack: List Webhooks** `clickstackListWebhooks`: Returns the ClickStack alert-notification webhooks configured for the team on a service, paginated. Beta endpoint.
* **ClickStack: Update Alert** `clickstackUpdateAlert`: Updates an existing ClickStack alert's threshold, interval, schedule, or notification channel. Beta endpoint.
* **ClickStack: Update Dashboard** `clickstackUpdateDashboard`: Fully replaces an existing ClickStack dashboard. Concurrent updates to the same dashboard are not protected by optimistic concurrency. Beta endpoint.
* **ClickStack: Update Role** `clickstackUpdateRole`: Updates a custom ClickStack role's name, description, and permissions. Predefined roles cannot be modified. Beta endpoint.
* **ClickStack: Update Saved Search** `clickstackUpdateSavedSearch`: Fully replaces an existing saved search. Every optional field omitted from the request is cleared. Beta endpoint.
* **ClickStack: Update Source** `clickstackUpdateSource`: Fully replaces an existing ClickStack data source. This generic action models a log source's fields; other kinds have additional fields not exposed here. Beta endpoint.
* **ClickStack: Update Webhook** `clickstackUpdateWebhook`: Fully replaces an existing ClickStack webhook. The description and body fields are a full replace: omitting them clears them. Beta endpoint.
* **ClickStack: Validate Dashboard** `clickstackValidateDashboard`: Validates a dashboard body against the same schema and tile rules used by dashboard creation, without ever persisting it. Beta endpoint.
* **Create API Key** `createApiKey`: Creates a new ClickHouse Cloud API key for the organization, returning the generated key ID and secret (shown only once).
* **Create Backup Bucket** `createBackupBucket`: Configures a customer-owned external bucket (AWS S3 currently modelled) to hold a service's backups instead of ClickHouse-managed storage. Requires an ADMIN-role API key. Beta endpoint.
* **Create BYOC Infrastructure** `createByocInfrastructure`: Creates a new Bring-Your-Own-Cloud (BYOC) infrastructure in the organization for hosting ClickHouse services inside the customer's own cloud account.
* **Create ClickPipe** `createClickPipe`: Creates a new ClickPipe data-ingestion pipeline on a service. This generic action models the two simplest source types, Kafka-family and object storage (S3/GCS/Azure Blob/etc.); the other supported source types (Kinesis, Pub/Sub, Postgres, MySQL, MongoDB, BigQuery CDC) each need different vendor-specific credential fields not exposed here and should be created from the ClickHouse Cloud console for now.
* **Create Invitation** `createInvitation`: Invites a user to join the organization by email, optionally assigning specific role IDs to them.
* **Create Postgres Read Replica** `createPostgresReadReplica`: Initiates creation of a new read replica for a managed PostgreSQL service. Beta endpoint.
* **Create Postgres Service** `createPostgresService`: Creates a new managed PostgreSQL service in the organization and returns it. The service starts asynchronously. Beta endpoint.
* **Create Private Endpoint** `createPrivateEndpoint`: Registers a new private endpoint and associates it with the service and organization.
* **Create Reverse Private Endpoint** `createReversePrivateEndpoint`: Creates a new reverse private endpoint on a service, allowing ClickPipes to reach a data source inside a customer's private VPC.
* **Create Role** `createRole`: Creates a new custom RBAC role for the organization with the given name, assigned actors, and access policies.
* **Create Service** `createService`: Creates a new ClickHouse service in the organization and returns its initial state and access password. The service starts asynchronously.
* **Create UDF** `createUdf`: Registers a new user-defined function (UDF) from a previously uploaded source archive, assigning it a name, runtime, arguments, and return type. Beta endpoint.
* **Create UDF Upload URL** `createUdfUploadUrl`: Creates an organization-scoped presigned application/zip upload URL for a UDF source archive. The returned upload ID may only be used for one create or version attempt. Beta endpoint.
* **Create UDF Version** `createUdfVersion`: Consumes a new uploaded source archive, assigns the next version number to an existing UDF, and starts its build. Beta endpoint.
* **Delete API Key** `deleteApiKey`: Permanently deletes a ClickHouse Cloud API key. A key cannot delete itself; use a different key or the console to remove the active credential.
* **Delete Backup Bucket** `deleteBackupBucket`: Removes the customer-owned external backup bucket configuration, reverting the service to ClickHouse-managed backup storage. Requires an ADMIN-role API key. Beta endpoint.
* **Delete BYOC Infrastructure** `deleteByocInfrastructure`: Removes a Bring-Your-Own-Cloud (BYOC) infrastructure from the organization.
* **Delete ClickPipe** `deleteClickPipe`: Deletes a ClickPipe data-ingestion pipeline from a service.
* **Delete Invitation** `deleteInvitation`: Deletes a single pending organization invitation, revoking the invite before it is accepted.
* **Delete Postgres Service** `deletePostgresService`: Deletes a managed PostgreSQL service that belongs to the organization. Beta endpoint.
* **Delete Reverse Private Endpoint** `deleteReversePrivateEndpoint`: Deletes a reverse private endpoint from a service.
* **Delete Role** `deleteRole`: Deletes an existing custom role and all its associated policies. System roles cannot be deleted.
* **Delete Service** `deleteService`: Deletes a ClickHouse service. The service must be in stopped state; it is deleted asynchronously after this call.
* **Delete Service Autoscaling Schedule** `deleteScalingSchedule`: Deletes the time-based autoscaling schedule for a service, restoring the base scaling configuration first if an entry was active. Beta endpoint.
* **Delete Service Query Endpoint** `deleteServiceQueryEndpoint`: Removes the service query API endpoint, disabling SQL query execution against the service over HTTP.
* **Delete Service Upgrade Window** `deleteUpgradeWindow`: Deletes the maintenance upgrade window for a primary service, restoring default upgrade scheduling.
* **Delete UDF** `deleteUdf`: Deletes every version of a user-defined function (UDF) and detaches it from all services. Removal from services completes asynchronously. Beta endpoint.
* **Delete UDF Version** `deleteUdfVersion`: Deletes a single version of a user-defined function (UDF). The UDF must not be attached to any services. Beta endpoint.
* **Detach UDF From Service** `detachUdf`: Detaches a user-defined function (UDF) from a service. Beta endpoint.
* **Discover ClickPipe Source Schema** `discoverClickPipeSchema`: Infers the field names and ClickHouse data types of a ClickPipe source (Kafka, Kinesis, Pub/Sub, or object storage) without creating a pipe.
* **Discover Prometheus Scrape Targets** `discoverPrometheusTargets`: Returns one Prometheus HTTP service-discovery scrape target per service in the organization the caller can view. Beta endpoint.
* **Get Active Prepaid Balances** `getActiveBalances`: Returns the organization's active prepaid credit balances, each with its own balance ID and remaining credits, plus the total remaining credits across all active balances.
* **Get API Key** `getApiKey`: Returns the details of a single ClickHouse Cloud API key by ID.
* **Get Backup** `getBackup`: Returns the details of a single service backup by ID.
* **Get Backup Bucket** `getBackupBucket`: Returns the customer-owned external storage bucket configured to hold a service's backups (AWS S3, GCP GCS, or Azure Blob).
* **Get Backup Configuration** `getBackupConfiguration`: Returns the automated backup schedule configuration for a ClickHouse service.
* **Get CDC ClickPipes Scaling** `getCdcClickPipesScaling`: Returns the shared CPU and memory scaling settings for database CDC ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery) on a service.
* **Get ClickHouse Setting** `getClickhouseSetting`: Returns the current effective value of one named ClickHouse server setting for a service. Beta endpoint.
* **Get ClickHouse Settings Schema** `getClickhouseSettingsSchema`: Returns the schema of every configurable ClickHouse server setting for a service, including types, valid values, descriptions, and warnings. Beta endpoint.
* **Get ClickPipe** `getClickPipe`: Returns the details of a single ClickPipe on a service.
* **Get ClickPipe Settings** `getClickPipeSettings`: Returns the advanced ingestion-tuning settings for a ClickPipe.
* **Get Invitation** `getInvitation`: Returns details for a single organization invitation by ID.
* **Get Organization** `getOrganization`: Returns the details of a single ClickHouse Cloud organization. The authenticating API key must belong to the organization.
* **Get Organization Activity** `getOrganizationActivity`: Returns the details of a single organization audit-log activity by ID.
* **Get Organization Member** `getMember`: Returns details for a single organization member by user ID.
* **Get Organization Metrics** `getOrganizationMetrics`: Returns Prometheus-format metrics (text exposition format) for every service in the organization the caller can view.
* **Get Organization PostgreSQL Metrics** `getOrganizationPostgresMetrics`: Returns Prometheus-format metrics for all managed PostgreSQL services in the organization (up to 100 services). Beta endpoint.
* **Get Organization Quota** `getOrganizationQuota`: Returns a single organization resource quota identified by its quota code, including its current usage. Responds with a not-found error when the quota code is unknown or does not apply to the organization.
* **Get Postgres CA Certificates** `getPostgresCaCertificates`: Downloads the CA certificates needed to establish a verified TLS connection to a managed PostgreSQL service. Beta endpoint.
* **Get Postgres Metrics** `getPostgresMetrics`: Returns bucketed time-series metrics (CPU, memory, disk, network, connections, cache hit ratio, throughput, transactions, and more) for a managed PostgreSQL service over a requested window. Beta endpoint.
* **Get Postgres Service** `getPostgresService`: Returns the details of a single managed PostgreSQL service. Beta endpoint.
* **Get Postgres Service Configuration** `getPostgresConfig`: Returns the PostgreSQL server and PgBouncer configuration for a managed PostgreSQL service. Beta endpoint.
* **Get Postgres Slow Query Pattern** `getPostgresSlowQueryPattern`: Returns aggregate metrics for a single slow query pattern on a managed PostgreSQL service, together with its most recent individual executions. Beta endpoint.
* **Get PostgreSQL Service Metrics** `getPostgresServiceMetrics`: Returns Prometheus-format metrics for a single managed PostgreSQL service. Beta endpoint.
* **Get Private Endpoint Config For Region** `getPrivateEndpointConfigForRegion`: Deprecated by ClickHouse: returns the private endpoint configuration for a cloud provider region within the organization. Superseded by the AWS PrivateLink allow-list process.
* **Get Reverse Private Endpoint** `getReversePrivateEndpoint`: Returns the details of a single reverse private endpoint on a service.
* **Get Role** `getRole`: Returns the details, actors, and policies for a single RBAC role.
* **Get Service** `getService`: Returns the details of a single ClickHouse service belonging to the organization.
* **Get Service Autoscaling Schedule** `getScalingSchedule`: Returns the time-based autoscaling schedule configured for a service. Requires the scheduled autoscaling feature to be enabled for the organization. Beta endpoint.
* **Get Service Metrics** `getServiceMetrics`: Returns Prometheus-format metrics (text exposition format) for a single ClickHouse service.
* **Get Service Private Endpoint Config** `getServicePrivateEndpointConfig`: Returns the information required to set up a private (PrivateLink/Private Service Connect) endpoint to a ClickHouse service.
* **Get Service Query Endpoint** `getServiceQueryEndpoint`: Returns the configuration of the service query API endpoint, which allows executing SQL queries against the service via HTTP.
* **Get Service Upgrade Window** `getUpgradeWindow`: Returns the configured maintenance upgrade window for a service.
* **Get UDF** `getUdf`: Returns the latest version of a single user-defined function (UDF) by name. Beta endpoint.
* **Get UDF Attachment** `getUdfAttachment`: Returns the current attachment of a user-defined function (UDF) to one service. Beta endpoint.
* **Get Usage Cost** `getUsageCost`: Returns the grand total and a list of daily, per-entity usage cost records for an organization over a queried period of up to 31 days, evaluated in UTC.
* **List API Keys** `listApiKeys`: Returns a list of all ClickHouse Cloud API keys configured for the organization.
* **List ClickHouse Settings** `listClickhouseSettings`: Returns the ClickHouse server settings that have been explicitly configured for a service. Beta endpoint.
* **List ClickPipes** `listClickPipes`: Returns every ClickPipe (data ingestion pipeline) configured on a ClickHouse service.
* **List Invitations** `listInvitations`: Returns a list of all pending organization invitations.
* **List Organization Activities** `listOrganizationActivities`: Returns the audit-log activity feed for the organization, optionally filtered to a date range.
* **List Organization Members** `listMembers`: Returns a list of all members belonging to the organization.
* **List Organization Quotas** `listOrganizationQuotas`: Returns the resource quotas enforced for the organization together with their current usage where available. Quotas that do not apply to the organization are omitted.
* **List Organizations** `listOrganizations`: Retrieves the list of ClickHouse Cloud organizations that the authenticated API key can access.
* **List Postgres Server Logs** `listPostgresLogs`: Returns PostgreSQL server log entries for a managed PostgreSQL service within a given time window, most recent first by default. Beta endpoint.
* **List Postgres Services** `listPostgresServices`: Returns every managed PostgreSQL service in the organization. Beta endpoint.
* **List Postgres Slow Query Patterns** `listPostgresSlowQueryPatterns`: Returns aggregate metrics for the slowest query patterns observed on a managed PostgreSQL service during a given time window. Beta endpoint.
* **List Reverse Private Endpoints** `listReversePrivateEndpoints`: Returns the reverse private endpoints configured for a service, used by ClickPipes to reach sources in a customer's private network.
* **List Roles** `listRoles`: Returns all system and custom roles available for the organization, each with its assigned actors and policies.
* **List Service Backups** `listServiceBackups`: Returns all backups for a ClickHouse service, most recent first.
* **List Services** `listServices`: Returns a list of all ClickHouse services in the organization.
* **List UDF Attachments** `listUdfAttachments`: Returns the current service attachments for a user-defined function (UDF), at most one attachment per service. Beta endpoint.
* **List UDF Versions** `listUdfVersions`: Returns all versions of a user-defined function (UDF). Beta endpoint.
* **List UDFs** `listUdfs`: Returns the latest version of every user-defined function (UDF) in the organization. Beta endpoint.
* **Remove Organization Member** `removeMember`: Removes a user from the organization.
* **Replace Postgres Service Configuration** `replacePostgresConfig`: Replaces the entire PostgreSQL server and PgBouncer configuration for a managed PostgreSQL service. Beta endpoint.
* **Reset ClickHouse Setting** `resetClickhouseSetting`: Removes a previously configured ClickHouse server setting, reverting it to the platform default. Beta endpoint.
* **Restore Postgres Service** `restorePostgresService`: Restores a managed PostgreSQL database from continuous backup into a new service, optionally at a specific point in time. Beta endpoint.
* **Set Service Autoscaling Schedule** `upsertScalingSchedule`: Creates or fully replaces the time-based autoscaling schedule for a service. Passing an empty entries array clears the schedule. Beta endpoint.
* **Set Service Upgrade Window** `setUpgradeWindow`: Creates or fully replaces the maintenance upgrade window for a primary service. The window lasts 6 hours from the given start hour.
* **Update API Key** `updateApiKey`: Updates properties of an existing ClickHouse Cloud API key such as its name, state, expiry, or assigned roles.
* **Update Backup Bucket** `updateBackupBucket`: Updates the customer-owned external backup bucket configuration for a service (AWS S3 currently modelled). Requires an ADMIN-role API key. Beta endpoint.
* **Update Backup Configuration** `updateBackupConfiguration`: Updates the automated backup schedule for a service: how often backups run, how long they are retained, and the daily start time. Requires an ADMIN-role API key.
* **Update BYOC Infrastructure** `updateByocInfrastructure`: Updates the configuration of an existing Bring-Your-Own-Cloud (BYOC) infrastructure and returns the modified infrastructure.
* **Update CDC ClickPipes Scaling** `updateCdcClickPipesScaling`: Updates the shared CPU and memory scaling settings for database CDC ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery) on a service. Changes may take a few minutes to propagate.
* **Update ClickHouse Settings** `updateClickhouseSettings`: Updates one or more ClickHouse server settings for a service, given as a JSON object of setting names to values. Beta endpoint.
* **Update ClickPipe** `updateClickPipe`: Updates a ClickPipe's mutable fields, such as its name and destination field mappings. Most source connection fields are immutable after creation.
* **Update ClickPipe Scaling** `updateClickPipeScaling`: Changes replica count, CPU, and memory scaling for a Kafka, Kinesis, or object storage ClickPipe. Database CDC pipes use Update CDC ClickPipes Scaling instead.
* **Update ClickPipe Settings** `updateClickPipeSettings`: Updates advanced ingestion-tuning settings for a ClickPipe, such as insert wait time, polling interval, and batch sizing.
* **Update ClickPipe State** `updateClickPipeState`: Starts, stops, or resyncs a ClickPipe. Resync is only available for Postgres and MySQL CDC pipes.
* **Update Organization** `updateOrganization`: Updates organization details such as name, private endpoints, and whether crash-report core-dump collection is enabled for services. Requires an ADMIN-role API key.
* **Update Organization Member** `updateMember`: Updates the roles assigned to an organization member.
* **Update Postgres Service** `updatePostgresService`: Updates a managed PostgreSQL service's name, size, high-availability type, or tags. Changing the name also updates the service's host name and certificates. Beta endpoint.
* **Update Postgres Service Configuration** `updatePostgresConfig`: Partially updates the PostgreSQL server and PgBouncer configuration for a managed PostgreSQL service. Beta endpoint.
* **Update Postgres Service State** `updatePostgresServiceState`: Initiates a restart, a read-replica promotion, or a primary/standby switchover for a managed PostgreSQL service. Beta endpoint.
* **Update Postgres Superuser Password** `updatePostgresPassword`: Sets a new password for a managed PostgreSQL service's superuser account. If omitted, a new password is generated and returned once. Beta endpoint.
* **Update Reverse Private Endpoint** `updateReversePrivateEndpoint`: Updates the mutable fields of an existing reverse private endpoint. The DNS mapping list is a full replacement; pass an empty array to clear it.
* **Update Role** `updateRole`: Updates the name, actors, or policies of an existing custom role. System roles cannot be updated; only fields provided are changed.
* **Update Service** `updateService`: Updates basic details of a service such as its name, IP access list, release channel, or whether core-dump collection is enabled.
* **Update Service Password** `updateServicePassword`: Sets a new default-user password for the service. If no hash is supplied, a new password is generated and returned once in the response.
* **Update Service Replica Scaling** `updateServiceReplicaScaling`: Updates per-replica autoscaling memory limits and mode (vertical or horizontal) for a production service.
* **Update Service State** `updateServiceState`: Starts, stops, or wakes a ClickHouse service.
* **Update Service Total Memory Scaling** `updateServiceScaling`: Updates the deprecated total-memory autoscaling limits and idle-mode behavior for a production service. Prefer Update Service Replica Scaling for new integrations.
* **Upsert Service Query Endpoint** `upsertServiceQueryEndpoint`: Creates or replaces the service query API endpoint, which allows executing SQL queries against the service over HTTP.

</details>
