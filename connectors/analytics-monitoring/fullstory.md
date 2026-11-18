---
description: "Fullstory is a digital experience analytics platform that captures web and mobile sessions."
hidden: true
---

# Fullstory

<img src="../../.gitbook/assets/connectors/lg/fullstory.png" alt="Fullstory logo">

Fullstory is a digital experience analytics platform that captures web and mobile sessions. This connector covers the documented Fullstory Server API v2: users with batch and streaming import, custom server events with batch import, sessions and the Anywhere Activation session endpoints, chart annotations, organization quotas, the beta datasets listing, and the beta extraction rules that pull structured data out of pages, URLs and network requests.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Authentication** | Credentials you enter |
| **Slug** | `fullstory` |

## Use it

Add Fullstory from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.fullstory.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Extraction Rule | `archiveExtractionRule` | Stops an extraction rule capturing data while preserving it for audit history. Permanent deletion is deliberately available only in the Fullstory app. This API is in beta and may change without notice. |
| Create Annotation | `createAnnotation` | Creates an annotation that marks a moment, or a span, on Fullstory's charts so the team can see what happened at that point. |
| Create Batch Events Import Job | `createBatchEventsImportJob` | Queues a batch of custom events for import and returns the job the batch runs under. |
| Create Batch User Import Job | `createBatchUserImportJob` | Queues a batch of users for import and returns the job the batch runs under. Poll the job for status, then fetch the imported users or the errors. |
| Create Event | `createEvent` | Records a custom server event and stitches it into a Fullstory session or user. Supply exactly one form of identification: a session id, or a user identifier together with use_most_recent. |
| Create Extraction Rule | `createExtractionRule` | Creates an extraction rule that pulls a structured value out of page elements, the URL or a network request into a named property. Create always uses selectors: named-element anchoring cannot be introduced through the API. This API is in beta and may change without notice. |
| Create User | `createUser` | Creates a user, or updates the existing one when the uid already belongs to an identified user. There is no need to check first: the call is an upsert. |
| Create User Stream | `createUserStream` | Opens a streaming user-import request and returns the request id used to poll its status. Streaming suits continuous ingestion where a batch job would be too coarse. |
| Create Webhook Endpoint | `createWebhookEndpoint` | Registers a webhook endpoint so Fullstory posts the chosen events to it. The URL must use HTTPS, and the signing secret is what lets the receiver verify a delivery really came from Fullstory. Fullstory system webhooks are a paid feature; on a plan without them every endpoint under /webhooks/v1 answers 403 forbidden. |
| Delete User | `deleteUser` | Deletes a single user, and the data captured for them, by their Fullstory id. Deletion is asynchronous, so the user reports as being deleted until it completes. |

<details>

<summary>See 29 more actions</summary>

* **Delete User By UID** `deleteUserByUid`: Deletes a single user, and the data captured for them, by the application-specific identifier you gave them.
* **Delete Webhook Endpoint** `deleteWebhookEndpoint`: Deletes a webhook endpoint so Fullstory stops delivering events to it. Fullstory system webhooks are a paid feature; on a plan without them every endpoint under /webhooks/v1 answers 403 forbidden.
* **Generate Session Context** `generateSessionContext`: Returns the session's events lightly transformed and structured for consumption by a large language model you control. This endpoint belongs to Fullstory Anywhere: Activation. On a plan without that entitlement it answers 403 permission_denied.
* **Generate Session Summary** `generateSessionSummary`: Generates an AI summary of a session using a stored prompt profile. This endpoint belongs to Fullstory Anywhere: Activation. On a plan without that entitlement it answers 403 permission_denied.
* **Get Batch Events Import Errors** `getBatchEventsImportErrors`: Retrieves the error code and message for every event a batch import job failed to create.
* **Get Batch Events Import Status** `getBatchEventsImportStatus`: Retrieves the status and counts of a queued batch events import job.
* **Get Batch Imported Events** `getBatchEventsImports`: Retrieves the events that a completed batch import job created.
* **Get Batch Imported Users** `getBatchUserImports`: Retrieves the users that a completed batch import job created, together with their Fullstory ids.
* **Get Batch User Import Errors** `getBatchUserImportErrors`: Retrieves the error code and message for every user a batch import job failed to create.
* **Get Batch User Import Status** `getBatchUserImportStatus`: Retrieves the status and counts of a queued batch user import job.
* **Get Extraction Rule** `getExtractionRule`: Retrieves a single extraction rule by identifier. This API is in beta and may change without notice.
* **Get Organization Quotas** `getQuotas`: Retrieves the organization's usage and limits for the current billing cycle, covering captured sessions and server events.
* **Get Session Events** `getSessionEvents`: Retrieves the raw captured events of a session, untransformed, for custom processing. This endpoint belongs to Fullstory Anywhere: Activation. On a plan without that entitlement it answers 403 permission_denied.
* **Get User** `getUser`: Retrieves a single user by the identifier Fullstory assigned them.
* **Get User Stream Status** `getCreateUserStreamStatus`: Retrieves the status of a streaming user-import request opened with Create User Stream.
* **Get Webhook Endpoint** `getWebhookEndpoint`: Retrieves a single webhook endpoint by identifier. Fullstory system webhooks are a paid feature; on a plan without them every endpoint under /webhooks/v1 answers 403 forbidden.
* **Get Webhook Sample Data** `getWebhookSampleData`: Retrieves a sample payload for an event type, useful for building and testing a receiver before real deliveries start. Fullstory system webhooks are a paid feature; on a plan without them every endpoint under /webhooks/v1 answers 403 forbidden.
* **List Datasets** `listDatasets`: Retrieves the datasets these credentials can read. This API is in beta and may change without notice.
* **List Extraction Rules** `listExtractionRules`: Retrieves the extraction rules for one scope, together with how much of that scope's rule budget is in use. This API is in beta and may change without notice.
* **List Sessions** `listSessions`: Retrieves the sessions belonging to a single user. Exactly one of uid, email or session_uid must be supplied, otherwise the request is rejected.
* **List Users** `listUsers`: Retrieves the users matching the supplied filter criteria, a page at a time.
* **List Webhook Endpoints** `listWebhookEndpoints`: Retrieves the configured webhook endpoints, a page at a time. Fullstory system webhooks are a paid feature; on a plan without them every endpoint under /webhooks/v1 answers 403 forbidden.
* **List Webhook Event Subcategories** `listWebhookEventSubcategories`: Retrieves the subcategories available for an event type that requires one, such as the particular alert an alert event should be limited to. Fullstory system webhooks are a paid feature; on a plan without them every endpoint under /webhooks/v1 answers 403 forbidden.
* **List Webhook Event Types** `listWebhookEventTypes`: Retrieves every webhook event type available to the organization. An event type flagged as having subcategories requires one to be supplied when an endpoint subscribes to it. Fullstory system webhooks are a paid feature; on a plan without them every endpoint under /webhooks/v1 answers 403 forbidden.
* **Replace Extraction Rule** `replaceExtractionRule`: Replaces an extraction rule in full. Supply the complete rule; anything omitted is cleared. This API is in beta and may change without notice.
* **Unarchive Extraction Rule** `unarchiveExtractionRule`: Restores an archived extraction rule so it resumes capturing. Fails when restoring the rule would exceed the active rule limit for its scope. This API is in beta and may change without notice.
* **Update Extraction Rule** `updateExtractionRule`: Updates part of an extraction rule, leaving everything else untouched. Supply at least one of name, description, source or mappings. This API is in beta and may change without notice.
* **Update User** `updateUser`: Updates the details of an existing user identified by their Fullstory id.
* **Update Webhook Endpoint** `updateWebhookEndpoint`: Changes a webhook endpoint's destination URL, subscribed events, signing secret or enabled state. Fullstory system webhooks are a paid feature; on a plan without them every endpoint under /webhooks/v1 answers 403 forbidden.

</details>
