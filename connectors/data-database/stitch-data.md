---
description: "Stitch is a cloud ETL service that replicates data from SaaS applications and databases into a data warehouse."
hidden: true
---

# Stitch

Stitch is a cloud ETL service that replicates data from SaaS applications and databases into a data warehouse. This connector covers the documented Stitch Connect API v4 - sources and source types, destinations and destination types, connection checks, streams, stream schemas and field selection, replication jobs, extraction and load history, and Import API access tokens - together with the Notification API v1 for custom email recipients and post-load webhooks, the partner-only account and session endpoints, and the Import API v2 for pushing records into Stitch.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Authentication** | Credentials you enter |
| **Slug** | `stitchData` |

## Use it

Add Stitch from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.stitchData.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Custom Email Notification Recipient | `createCustomEmailNotificationRecipient` | Adds an email address to the list of recipients Stitch sends account notifications to. |
| Create Destination | `createDestination` | Creates a new destination warehouse on the Stitch account. |
| Create Ephemeral Session | `createEphemeralSession` | Creates a short-lived single-use session token that logs a user straight into the Stitch app. This endpoint is available only to Stitch Partners. |
| Create Import API Token | `createImportApiToken` | Generates a new Import API access token for an Import API source. The token value is returned once and cannot be retrieved again. |
| Create Post-Load Hook Notification | `createHookNotification` | Registers a post-load webhook so Stitch posts a notification to the supplied URL each time the given destination finishes loading data. |
| Create Source | `createSource` | Creates a new data source on the Stitch account. Stitch returns the source together with a report card listing the configuration steps still outstanding. |
| Create Stitch Account | `createAccount` | Creates a new Stitch client account. This endpoint is available only to Stitch Partners and requires partner credentials in the request body rather than an access token. |
| Delete Custom Email Notification Recipient | `deleteCustomEmailNotificationRecipient` | Permanently removes an email address from the account notification recipient list. |
| Delete Destination | `deleteDestination` | Deletes a destination from the Stitch account. |
| Delete Post-Load Hook Notification | `deleteHookNotification` | Permanently deletes a post-load webhook so Stitch stops calling it. |
| Delete Source | `deleteSource` | Deletes a source. Stitch stops replicating it and stamps the record with a deletion timestamp. |
| Disable Custom Email Notification Recipient | `disableCustomEmailNotificationRecipient` | Disables a custom notification recipient so Stitch stops emailing them, without removing the record. |
| Disable Post-Load Hook Notification | `disableHookNotification` | Disables a post-load webhook so Stitch stops delivering notifications to it. |
| Enable Custom Email Notification Recipient | `enableCustomEmailNotificationRecipient` | Re-enables a disabled custom notification recipient so Stitch resumes emailing them. |
| Enable Post-Load Hook Notification | `enableHookNotification` | Re-enables a disabled post-load webhook so Stitch resumes delivering notifications to it. |
| Get Destination Type | `getDestinationType` | Retrieves a single destination type and the form properties required to configure it. |
| Get Extraction Job Logs | `getExtractionLogs` | Retrieves the log output of a single extraction job. Job names come from List Extractions. |
| Get Import API Status | `getImportApiStatus` | Reports whether the Stitch Import API is currently available. Use it as a health check before pushing records. |
| Get Source | `getSource` | Retrieves a single source and its current configuration state by identifier. |
| Get Source Last Connection Check | `getSourceLastConnectionCheck` | Retrieves the result of the most recent connection check Stitch ran against a source, including the outcome of each individual check step. |
| Get Source Type | `getSourceType` | Retrieves a single source type and the form properties required to configure it. |
| Get Stream Schema | `getStreamSchema` | Retrieves the JSON schema and field-level metadata for a single stream, which is what field selection is applied against. |
| List Custom Email Notification Recipients | `listCustomEmailNotificationRecipients` | Retrieves every additional email address Stitch sends account notifications to. |
| List Destination Types | `listDestinationTypes` | Retrieves every destination type Stitch can load data into, including the form properties each type requires. |
| List Destinations | `listDestinations` | Retrieves every destination configured on the Stitch client account. |
| List Extractions | `listExtractions` | Retrieves the most recent extraction job for every source on the account, ordered by source identifier. Results are paginated 100 records to a page. |
| List Import API Tokens | `listImportApiTokens` | Retrieves the identifiers of the Import API access tokens issued for a source. Token values themselves are never returned. |
| List Loads | `listLoads` | Retrieves the most recent load attempt for every stream on the account, ordered by stream name. Results are paginated 100 records to a page. |
| List Post-Load Hook Notifications | `listHookNotifications` | Retrieves every post-load webhook Stitch calls when a destination finishes loading data. |
| List Source Types | `listSourceTypes` | Retrieves every source type Stitch supports, including the form properties each type requires. |
| List Sources | `listSources` | Retrieves every source configured on the Stitch client account, including deleted ones. |
| List Streams | `listStreams` | Retrieves every stream, meaning table or endpoint, that a source exposes for replication. |
| Pause Source | `pauseSource` | Pauses a source so Stitch stops scheduling replication jobs for it. Any timestamp value pauses the source immediately. |
| Push Import API Batch With Schema | `pushImportApiBatch` | Pushes a batch of records together with an explicit JSON schema, which lets Stitch type the destination columns precisely. Requires an Import API access token created for an Import API source, not a Connect API token. |
| Push Import API Records | `pushImportApiRecords` | Pushes a batch of upsert records into a Stitch Import API source, which loads them into the destination table. Requires an Import API access token created for an Import API source, not a Connect API token. |
| Revoke Import API Token | `revokeImportApiToken` | Revokes an Import API access token so it can no longer push data into Stitch. |
| Start Replication Job | `startReplicationJob` | Starts a replication job for a source immediately instead of waiting for its next scheduled run. |
| Stop Replication Job | `stopReplicationJob` | Stops the replication job currently running for a source. |
| Unpause Source | `unpauseSource` | Resumes a paused source so Stitch schedules replication jobs for it again. |
| Update Destination | `updateDestination` | Updates the connection properties of an existing destination. |
| Update Source | `updateSource` | Updates the display name, destination or connection properties of an existing source. |
| Update Streams Metadata | `updateStreamsMetadata` | Selects streams and fields for replication and sets their replication method. This is the endpoint that drives field selection on a source. |
| Validate Import API Records | `validateImportApiRecords` | Validates a batch of Import API records against Stitch's structural rules without persisting anything. Requires an Import API access token created for an Import API source, not a Connect API token. |
