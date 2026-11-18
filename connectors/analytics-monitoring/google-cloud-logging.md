---
description: "Google Cloud Logging API v2 for writing, reading and managing logs across projects, organizations, folders and billing accounts."
hidden: true
---

# Google Cloud Logging

<img src="../../.gitbook/assets/connectors/lg/google-cloud-logging.png" alt="Google Cloud Logging logo">

Google Cloud Logging API v2 for writing, reading and managing logs across projects, organizations, folders and billing accounts. Write and list log entries, manage log buckets, views, links, sinks, exclusions, log scopes, saved queries and log-based metrics, and configure CMEK and default logging settings.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [logging.googleapis.com](https://logging.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudLogging` |

## Use it

Add Google Cloud Logging from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudLogging.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Operation | `cancelOperation` | Requests cancellation of a Cloud Logging long-running operation. Cancellation is best-effort, so poll the operation afterwards to see whether it stopped. |
| Copy Log Entries | `copyLogEntries` | Copies log entries out of a log bucket to a Cloud Storage bucket. This starts a long-running operation; poll the returned operation to follow progress. |
| Create Bucket Link | `createLink` | Creates a linked BigQuery dataset on a log bucket so the bucket's data can be queried in BigQuery. The bucket must have Log Analytics enabled. Returns a long-running operation. |
| Create Log Bucket | `createBucket` | Creates a log bucket that can be used to store log entries. Once created, the bucket's location cannot be changed. Use Create Log Bucket Async when the bucket needs customer-managed encryption. |
| Create Log Bucket Async | `createBucketAsync` | Creates a log bucket asynchronously and returns a long-running operation. Use this rather than Create Log Bucket when the bucket needs customer-managed encryption, since CMEK settings can only be applied this way. |
| Create Log Exclusion | `createExclusion` | Creates a log exclusion on a project, organization, folder or billing account. Matching entries are dropped at ingestion, so they are neither stored nor billed, though they are still counted by log-based metrics. |
| Create Log Metric | `createMetric` | Creates a log-based metric on a project. A counter metric counts entries matching the filter; a distribution metric additionally extracts a numeric value from each entry, which requires a value extractor and bucket options. |
| Create Log Scope | `createLogScope` | Creates a log scope naming the projects and log views that Logs Explorer should search together. Organizations and folders cannot be listed as resource names inside a scope. |
| Create Log Sink | `createSink` | Creates a log sink that exports matching entries to Cloud Storage, BigQuery, Pub/Sub or another log bucket. The response carries a writerIdentity that must be granted write access on the destination before the sink can export anything. |
| Create Log View | `createView` | Creates a log view on a log bucket. The view's filter decides which of the bucket's entries callers granted access to the view can read. A bucket may hold at most 30 views. |

<details>

<summary>See 54 more actions</summary>

* **Create Saved Query** `createSavedQuery`: Saves a Logs Explorer or Log Analytics query so it can be reused. Supply exactly one of loggingQuery or opsAnalyticsQuery, and choose PRIVATE or SHARED visibility.
* **Delete Bucket Link** `deleteLink`: Deletes a linked BigQuery dataset from a log bucket. Returns a long-running operation; the bucket's own data is unaffected.
* **Delete Log** `deleteLog`: Permanently deletes every entry in a log. The log itself reappears if new entries are written to it afterwards. Entries written shortly before the call may not be removed.
* **Delete Log Bucket** `deleteBucket`: Deletes a log bucket. The bucket moves to the DELETE_REQUESTED state and is permanently removed after seven days, during which Undelete Log Bucket can restore it. A locked bucket cannot be deleted.
* **Delete Log Exclusion** `deleteExclusion`: Deletes a log exclusion. Entries that were being dropped by it start being ingested and billed again.
* **Delete Log Metric** `deleteMetric`: Deletes a log-based metric. The metric stops producing data points and any Cloud Monitoring alerts built on it stop firing.
* **Delete Log Scope** `deleteLogScope`: Deletes a log scope. The projects and log views it referenced are unaffected; only the saved grouping is removed.
* **Delete Log Sink** `deleteSink`: Deletes a log sink and stops exporting entries to its destination. Data already written to the destination is left in place.
* **Delete Log View** `deleteView`: Deletes a log view from a log bucket. The bucket's entries are unaffected, but callers whose access came only through this view lose it.
* **Delete Saved Query** `deleteSavedQuery`: Deletes a saved query. Log entries and views the query referenced are unaffected.
* **Get Bucket Link** `getLink`: Retrieves a single linked BigQuery dataset on a log bucket, including its lifecycle state and the BigQuery dataset it exposes.
* **Get CMEK Settings** `getCmekSettings`: Retrieves the customer-managed encryption key settings the Log Router uses for a resource, including the service account that must be granted access to the key.
* **Get Location** `getLocation`: Retrieves metadata about a single Cloud Logging location within a project, organization, folder or billing account.
* **Get Log Bucket** `getBucket`: Retrieves a single log bucket, including its retention period, lock state, analytics setting and CMEK configuration.
* **Get Log Exclusion** `getExclusion`: Retrieves a single log exclusion, including the filter that decides which entries it drops and whether it is currently enabled.
* **Get Log Metric** `getMetric`: Retrieves a single log-based metric, including its filter, label extractors and Cloud Monitoring descriptor.
* **Get Log Scope** `getLogScope`: Retrieves a single log scope, listing the projects and log views that Logs Explorer searches when the scope is selected.
* **Get Log Sink** `getSink`: Retrieves a single log sink, including its destination, filter and the writer identity that must be granted access on the destination.
* **Get Log View** `getView`: Retrieves a single log view on a log bucket, including the filter that restricts which entries the view exposes.
* **Get Log View IAM Policy** `getViewIamPolicy`: Retrieves the IAM access control policy attached to a log view, listing the principals granted each role. Billing account views do not support IAM policies.
* **Get Logging Settings** `getSettings`: Retrieves the default Cloud Logging settings for a resource, including the storage location and default sink behaviour applied to newly created projects and folders beneath it.
* **Get Operation** `getOperation`: Retrieves the current state of a Cloud Logging long-running operation. Poll this after starting an asynchronous bucket create, link create or log entry copy.
* **Get Saved Query** `getSavedQuery`: Retrieves a single saved query, returning either its Logs Explorer filter or its Log Analytics SQL text depending on the query type.
* **List Bucket Links** `listLinks`: Lists the linked BigQuery datasets on a log bucket. A link exposes the bucket's analytics data as a BigQuery dataset that can be queried directly.
* **List Locations** `listLocations`: Lists the Cloud Logging locations available to a project, organization, folder or billing account. Most Logging resources live in the 'global' location.
* **List Log Buckets** `listBuckets`: Lists the log buckets in a location, including the built-in _Default and _Required buckets. Pass '-' as the location id to list buckets across every location.
* **List Log Entries** `listLogEntries`: Searches log entries across one or more projects, organizations, folders, billing accounts or log views. Entries that have not yet been ingested are not returned, and the filter uses the Logging query language.
* **List Log Exclusions** `listExclusions`: Lists the log exclusions on a project, organization, folder or billing account. Exclusions drop matching entries at ingestion so they are neither stored nor billed.
* **List Log Metrics** `listMetrics`: Lists the log-based metrics defined on a project. Log-based metrics count or extract values from log entries matching a filter, and are only supported at project scope.
* **List Log Scopes** `listLogScopes`: Lists the log scopes in a location. A log scope names a set of projects and log views that Logs Explorer searches together. Log scopes are only available in the global location.
* **List Log Sinks** `listSinks`: Lists the log sinks on a project, organization, folder or billing account. Sinks route matching entries to Cloud Storage, BigQuery, Pub/Sub or another log bucket.
* **List Log Views** `listViews`: Lists the log views defined on a log bucket. Views restrict which entries in the bucket a caller can see, and are the unit IAM policies are attached to.
* **List Logs** `listLogs`: Lists the names of the logs that have entries in a project, organization, folder or billing account. Only logs that have data are returned.
* **List Logs In View** `listViewLogs`: Lists the names of the logs that have entries visible through a specific log view. Only logs with data are returned.
* **List Monitored Resource Descriptors** `listMonitoredResourceDescriptors`: Lists the monitored resource types Cloud Logging understands, with the labels each type expects. Use this to discover the correct resource type and labels before writing log entries.
* **List Operations** `listOperations`: Lists the Cloud Logging long-running operations in a location, such as bucket creations, link creations and log entry copies. Cloud Logging requires the filter to name a request type, for example 'request_type=CopyLogEntries'; calling this without a filter returns 400 INVALID_ARGUMENT.
* **List Recent Queries** `listRecentQueries`: Lists the queries the calling user has run recently in Logs Explorer or Log Analytics. Pass '-' as the location id to list across every location.
* **List Saved Queries** `listSavedQueries`: Lists the saved Logs Explorer and Log Analytics queries in a location. Pass '-' as the location id to list saved queries across every location.
* **Replace Log Sink** `updateSink`: Replaces a log sink with the supplied values. Without an updateMask this is a full replacement, so any writable field you omit is cleared. Use Update Log Sink to change only selected fields.
* **Set Log View IAM Policy** `setViewIamPolicy`: Replaces the IAM access control policy on a log view, which is how per-view read access is granted. The policy sent replaces the existing one entirely, so read it first and modify the result.
* **Tail Log Entries** `tailLogEntries`: Streams newly arriving log entries from one or more parent resources (POST /v2/entries:tail). Google exposes this bidirectional streaming method over HTTP/JSON as a JSON array of requests, so this action sends a one-element array and returns the array of TailLogEntriesResponse messages received before the stream closes (often [] if nothing arrives within the buffer window). Use List Log Entries for history. Docs: https://cloud.google.com/logging/docs/reference/v2/rest/v2/entries/tail
* **Test Log View IAM Permissions** `testViewIamPermissions`: Returns which of the supplied IAM permissions the caller actually holds on a log view. This is designed for building permission-aware user interfaces and never errors on a missing permission.
* **Undelete Log Bucket** `undeleteBucket`: Restores a log bucket that is in the DELETE_REQUESTED state. This works only within the seven-day grace period before the bucket is permanently removed.
* **Update CMEK Settings** `updateCmekSettings`: Sets the customer-managed encryption key the Log Router uses for an organization. The Log Router service account must already hold the CryptoKey Encrypter/Decrypter role on the key, and this is only configurable at organization scope.
* **Update Log Bucket** `patchBucket`: Updates a log bucket. Only the fields named in updateMask are changed. A locked bucket cannot have its retention period changed, and CMEK settings must be changed with Update Log Bucket Async.
* **Update Log Bucket Async** `updateBucketAsync`: Updates a log bucket asynchronously and returns a long-running operation. Use this rather than Update Log Bucket when changing customer-managed encryption settings, which cannot be changed synchronously.
* **Update Log Exclusion** `patchExclusion`: Updates a log exclusion. Only the fields named in updateMask are changed, so pausing an exclusion is a patch of disabled alone.
* **Update Log Metric** `updateMetric`: Creates or replaces a log-based metric. This is a full replacement, so send every writable field you want to keep. If no metric with this name exists it is created.
* **Update Log Scope** `patchLogScope`: Updates a log scope. Only the fields named in updateMask are changed, and the resource names list is replaced wholesale rather than merged.
* **Update Log Sink** `patchSink`: Updates selected fields of a log sink. Only the fields named in updateMask are changed, so disabling a sink is a patch of disabled alone.
* **Update Log View** `patchView`: Updates a log view. Only the fields named in updateMask are changed. Changing the filter takes several minutes to take effect.
* **Update Logging Settings** `updateSettings`: Updates the default Cloud Logging settings for an organization or folder, which govern the storage location, CMEK key and _Default sink behaviour of newly created containers beneath it. Only the fields named in updateMask are changed.
* **Update Saved Query** `patchSavedQuery`: Updates a saved query. Only the fields named in updateMask are changed, and a query cannot be switched between the Logging and Ops Analytics types.
* **Write Log Entries** `writeLogEntries`: Writes log entries to Cloud Logging. Each entry needs a log name and a monitored resource, either set on the entry itself or supplied once as the request-level defaults. Use dryRun to validate entries without persisting them.

</details>
