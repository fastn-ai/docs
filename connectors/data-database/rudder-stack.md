---
description: "RudderStack is a warehouse-native customer data platform."
hidden: true
---

# RudderStack

<img src="../../.gitbook/assets/connectors/lg/rudder-stack.png" alt="RudderStack logo">

RudderStack is a warehouse-native customer data platform. This connector covers the RudderStack Management (Config Plane) API: workspace details, event stream sources and their write keys, destinations with their transformation links, source-to-destination connections, cloud accounts, JavaScript transformations and shared libraries with versioning, publishing and test runs, the data catalog of events, properties, categories and custom types, tracking plans with their events and source connections, observed event schemas, Reverse ETL sources, connections and syncs, Profiles runs, data graphs, audit logs, user suppression and data regulation requests, and source/destination connectivity tests.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [rudderstack.com](https://rudderstack.com) |
| **Authentication** | Basic auth, Credentials you enter |
| **Slug** | `rudderStack` |

## Use it

Add RudderStack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.rudderStack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Alias User Identity | `aliasUserIdentity` | Merge two identifiers for the same person, for example linking an anonymous visitor to the account they just signed up with. This action uses the Source Write Key connection, not the Workspace Access Token connection. |
| Associate User With Group | `associateUserWithGroup` | Associate a user with a group such as a company, account or workspace, and record traits about that group. This action uses the Source Write Key connection, not the Workspace Access Token connection. |
| Connect Tracking Plan To Source | `connectTrackingPlanToSource` | Connect a tracking plan to a source so the source's events are validated against the plan, and set how violations are handled. |
| Connect Transformation To Destination | `connectTransformationToDestination` | Attach a transformation to a destination so that events are transformed before delivery. A destination can have only one transformation at a time, so this replaces any transformation already connected. The transformation must be published first. |
| Create Account | `createAccount` | Store a cloud or warehouse credential in the workspace so that Reverse ETL sources and destinations can use it. The secret is write-only and is never returned. |
| Create Catalog Category | `createCatalogCategory` | Create a category for grouping related event definitions in the data catalog. |
| Create Catalog Event | `createCatalogEvent` | Add an event definition to the data catalog so it can be referenced by tracking plans and used to validate incoming events. |
| Create Catalog Property | `createCatalogProperty` | Add a property definition to the data catalog so it can be attached to events in a tracking plan and used to validate incoming payloads. |
| Create Connection | `createConnection` | Connect a source to a destination so that events collected by the source are routed to the destination. |
| Create Data Regulation | `createDataRegulation` | Submit a user suppression or suppression-and-delete request so RudderStack stops forwarding events for the given users and optionally deletes their existing data. This is an Enterprise data governance feature. |

<details>

<summary>See 111 more actions</summary>

* **Create Destination** `createDestination`: Create a new destination in the workspace. The configuration keys required depend on the destination type; consult the RudderStack setup guide for that destination.
* **Create Event Stream Source** `createEventStreamSource`: Create an SDK event stream source and claim it under a caller-owned external ID. RudderStack returns the write key that the SDK uses to send events.
* **Create Reverse ETL Connection** `createReverseEtlConnection`: Create a Reverse ETL connection that syncs rows from a warehouse source to a destination on a schedule. RudderStack detects the flow from the destination definition: JSON Mapper destinations such as webhooks additionally require mappings and restrict identifier targets to user_id and anonymous_id. A destination cannot be shared between Reverse ETL sources and event stream sources.
* **Create Reverse ETL Source** `createReverseEtlSource`: Create a Reverse ETL source that reads rows from a warehouse table or a SQL model, so they can be synced out to a destination.
* **Create Source** `createSource`: Create a new event stream source in the workspace. RudderStack generates and returns a write key that SDKs and the HTTP event API use to send events to this source.
* **Create Tracking Plan** `createTrackingPlan`: Create an empty tracking plan. Add event schemas to it with Add Events To Tracking Plan, then connect it to a source to start validating events.
* **Create Transformation** `createTransformation`: Create a transformation that reshapes, filters or enriches events before they reach a destination. Publish it before connecting it to a destination.
* **Create Transformation Library** `createTransformationLibrary`: Create a shared code library that transformations can import, so common helper functions can be written once and reused.
* **Delete Account** `deleteAccount`: Delete a stored cloud or warehouse credential. Sources and destinations still using the credential will stop working.
* **Delete Catalog Category** `deleteCatalogCategory`: Delete a data catalog category. Events filed under it become uncategorised.
* **Delete Catalog Event** `deleteCatalogEvent`: Remove an event definition from the data catalog. Tracking plans that reference the event must be updated separately.
* **Delete Catalog Property** `deleteCatalogProperty`: Remove a property definition from the data catalog. Tracking plans that reference the property must be updated separately.
* **Delete Connection** `deleteConnection`: Delete a source to destination connection so that events from the source stop reaching the destination. This also removes Reverse ETL connections, which are returned by List Connections alongside event stream connections.
* **Delete Destination** `deleteDestination`: Delete a destination. Deleting a destination also removes every connection that routes events to it.
* **Delete Event Stream Source** `deleteEventStreamSource`: Delete an event stream source created through the event stream sources API.
* **Delete Reverse ETL Connection** `deleteReverseEtlConnection`: Delete a Reverse ETL connection so it stops syncing rows to the destination. RudderStack resolves the underlying warehouse source for this call, so it returns 404 "Source does not exist" when the source's warehouse credential is not reachable; Delete Connection against the same connection ID removes it in that case.
* **Delete Reverse ETL Source** `deleteReverseEtlSource`: Delete a Reverse ETL source. Connections that sync from it stop working.
* **Delete Source** `deleteSource`: Delete an event stream source. Deleting a source stops event collection for it and removes its connections to destinations.
* **Delete Tracking Plan** `deleteTrackingPlan`: Delete a tracking plan. Sources connected to it stop validating their events.
* **Delete Transformation** `deleteTransformation`: Delete a transformation. Destinations that currently use it stop transforming events.
* **Delete Transformation Library** `deleteTransformationLibrary`: Delete a transformation library. Transformations that import it stop working until the import is removed.
* **Disconnect Tracking Plan From Source** `disconnectTrackingPlanFromSource`: Disconnect a tracking plan from a source so the source's events are no longer validated against it.
* **Disconnect Transformation From Destination** `disconnectTransformationFromDestination`: Detach the transformation currently connected to a destination so that events are delivered untransformed.
* **Get Account** `getAccount`: Retrieve a single stored credential by its identifier. Only non-secret metadata is returned.
* **Get Catalog Category** `getCatalogCategory`: Retrieve a single data catalog category by its identifier.
* **Get Catalog Event** `getCatalogEvent`: Retrieve a single event definition from the data catalog by its identifier.
* **Get Catalog Property** `getCatalogProperty`: Retrieve a single property definition from the data catalog by its identifier.
* **Get Connection** `getConnection`: Retrieve a single source to destination connection by its identifier.
* **Get Destination** `getDestination`: Retrieve a single destination by its identifier, including its full configuration.
* **Get Destination Transformation** `getDestinationTransformation`: Retrieve the transformation currently connected to a destination. Returns a 404 when no transformation is connected.
* **Get Event Schema** `getEventSchema`: Retrieve a single observed event schema by its identifier.
* **Get Event Schema Version** `getEventSchemaVersion`: Retrieve one specific observed version of an event schema.
* **Get Profiles Run Status** `getProfilesRunStatus`: Check the status of a Profiles run that was previously started.
* **Get Reverse ETL Connection** `getReverseEtlConnection`: Retrieve a single Reverse ETL connection by its identifier, including its schedule, sync behaviour and field mappings.
* **Get Reverse ETL Source** `getReverseEtlSource`: Retrieve a single Reverse ETL source by its identifier, including its SQL or table configuration.
* **Get Reverse ETL Source Preview Result** `getReverseEtlSourcePreviewResult`: Fetch the result of a previously submitted Reverse ETL source preview. Poll this until the status is completed or failed.
* **Get Reverse ETL Sync** `getReverseEtlSync`: Retrieve a single Reverse ETL sync run, including its status, timings and any error.
* **Get Source** `getSource`: Retrieve a single event stream source by its identifier, including its write key and configuration.
* **Get Tracking Plan** `getTrackingPlan`: Retrieve a single tracking plan by its identifier, optionally rebuilding the JSON schemas of its events.
* **Get Tracking Plan Event** `getTrackingPlanEvent`: Retrieve one event schema from a tracking plan, including the JSON Schema rules its payload is validated against. The event must already have been added to the plan; a catalog event that is not in the plan returns a 404.
* **Get Transformation** `getTransformation`: Retrieve a single transformation by its identifier, including its current code and version.
* **Get Transformation Library** `getTransformationLibrary`: Retrieve a single transformation library by its identifier, including its current code and import handle.
* **Get Transformation Library Version** `getTransformationLibraryVersion`: Retrieve one specific saved version of a transformation library, including the exact code that version contains.
* **Get Transformation Version** `getTransformationVersion`: Retrieve one specific saved version of a transformation, including the exact code that version contains.
* **Get Workspace** `getWorkspace`: Retrieve the RudderStack workspace that the supplied access token belongs to, including its name, data residency region, environment and data plane URL.
* **Identify User** `identifyUser`: Associate a user with their identifier and record what you know about them as traits. This action uses the Source Write Key connection, not the Workspace Access Token connection.
* **List Accounts** `listAccounts`: List the stored cloud and warehouse credentials in the workspace. Only non-secret metadata is returned; secrets are never read back.
* **List Audit Logs** `listAuditLogs`: List the audit log entries for a workspace, showing who changed which RudderStack resource and when. This endpoint requires an Organization Access Token rather than a workspace token, and the AUDIT_LOGS feature must be enabled on the organisation's plan.
* **List Catalog Categories** `listCatalogCategories`: List the categories used to group event definitions in the data catalog.
* **List Catalog Custom Types** `listCatalogCustomTypes`: List the reusable custom property types defined in the data catalog. Custom types are an add-on feature and this action returns a 403 when it is not enabled for the account.
* **List Catalog Events** `listCatalogEvents`: List the event definitions in the data catalog, which describe the events the workspace expects to receive.
* **List Catalog Properties** `listCatalogProperties`: List the property definitions in the data catalog, which describe the properties and traits events may carry.
* **List Connections** `listConnections`: List every source to destination connection in the workspace.
* **List Data Graphs** `listDataGraphs`: List the data graphs defined in the workspace, which describe how warehouse tables relate to each other for Profiles. Data graphs are an add-on feature and this action returns a 403 when it is not enabled for the account.
* **List Data Regulations** `listDataRegulations`: List the user suppression and deletion requests submitted for the workspace. This is an Enterprise data governance feature and returns a 403 when the organisation is not entitled to it.
* **List Destinations** `listDestinations`: List every destination in the workspace, including each destination's type, configuration and connected transformation.
* **List Event Schema Versions** `listEventSchemaVersions`: List the versions of an observed event schema, showing how the payload shape has changed over time.
* **List Event Schemas** `listEventSchemas`: List the event payload shapes RudderStack has actually observed arriving in the workspace, which is the basis for auditing real traffic against a tracking plan.
* **List Event Stream Sources** `listEventStreamSources`: List every event stream source created through the event stream sources API, including each source's external ID and linked tracking plan.
* **List Reverse ETL Connections** `listReverseEtlConnections`: List the Reverse ETL connections in the workspace, each of which syncs a warehouse source to a destination on a schedule.
* **List Reverse ETL Sources** `listReverseEtlSources`: List the Reverse ETL sources in the workspace, which read rows out of a warehouse table or SQL model.
* **List Reverse ETL Syncs** `listReverseEtlSyncs`: List the sync runs of a Reverse ETL connection, so their status and row counts can be monitored.
* **List Sources** `listSources`: List every event stream source in the workspace, including each source's write key, type and enabled state.
* **List Tracking Plan Events** `listTrackingPlanEvents`: List the event schemas contained in a tracking plan.
* **List Tracking Plan Sources** `listTrackingPlanSources`: List the sources a tracking plan is connected to, so you can see which pipelines it validates.
* **List Tracking Plans** `listTrackingPlans`: List the tracking plans in the workspace. A tracking plan is the schema contract a source's events are validated against.
* **List Transformation Libraries** `listTransformationLibraries`: List every shared code library in the workspace that transformations can import.
* **List Transformation Library Versions** `listTransformationLibraryVersions`: List every saved version of a transformation library, so an earlier revision of the code can be inspected.
* **List Transformation Versions** `listTransformationVersions`: List every saved version of a transformation, so an earlier revision of the code can be inspected.
* **List Transformations** `listTransformations`: List every transformation in the workspace, including its current code, language and imported libraries.
* **Publish Transformations** `publishTransformations`: Publish one or more transformation and library versions in a single call, optionally running each transformation's test suite first. Publishing makes a version the one that runs in the pipeline.
* **Record Page View** `recordPageView`: Record that a user viewed a web page, along with properties such as the page name, URL and referrer. This action uses the Source Write Key connection, not the Workspace Access Token connection.
* **Record Screen View** `recordScreenView`: Record that a user viewed a screen in a mobile app, along with properties describing it. This is the mobile equivalent of a page view. This action uses the Source Write Key connection, not the Workspace Access Token connection.
* **Remove Event From Tracking Plan** `removeEventFromTrackingPlan`: Remove one event schema from a tracking plan. The underlying data catalog event definition is not deleted. The event must currently be in the plan.
* **Run Transformation Tests** `runTransformationTests`: Run the supplied test suites against transformation versions without publishing them, to check that the code produces the expected output.
* **Send Event Batch** `sendEventBatch`: Send several events of any type in one request. Use this to reduce the number of calls when replaying or backfilling events. This action uses the Source Write Key connection, not the Workspace Access Token connection.
* **Set Account External ID** `setAccountExternalId`: Claim an existing stored credential under a caller-owned external ID so it can be looked up without storing the RudderStack identifier.
* **Set Catalog Category External ID** `setCatalogCategoryExternalId`: Claim an existing data catalog category under a caller-owned external ID so it can be looked up without storing the RudderStack identifier.
* **Set Catalog Event External ID** `setCatalogEventExternalId`: Claim an existing catalog event under a caller-owned external ID so it can be looked up without storing the RudderStack identifier.
* **Set Catalog Property External ID** `setCatalogPropertyExternalId`: Claim an existing catalog property under a caller-owned external ID so it can be looked up without storing the RudderStack identifier.
* **Set Destination External ID** `setDestinationExternalId`: Claim an existing destination under a caller-owned external ID so it can be looked up without storing the RudderStack identifier.
* **Set Event Stream Source External ID** `setEventStreamSourceExternalId`: Claim an existing event stream source under a caller-owned external ID so it can be looked up without storing the RudderStack identifier.
* **Set Reverse ETL Connection External ID** `setReverseEtlConnectionExternalId`: Claim an existing Reverse ETL connection under a caller-owned external ID so it can be looked up without storing the RudderStack identifier.
* **Set Reverse ETL Source External ID** `setReverseEtlSourceExternalId`: Claim an existing Reverse ETL source under a caller-owned external ID so it can be looked up without storing the RudderStack identifier.
* **Set Tracking Plan External ID** `setTrackingPlanExternalId`: Claim an existing tracking plan under a caller-owned external ID so it can be looked up without storing the RudderStack identifier.
* **Set Transformation External ID** `setTransformationExternalId`: Claim an existing transformation under a caller-owned external ID so it can be looked up without storing the RudderStack identifier.
* **Set Transformation Library External ID** `setTransformationLibraryExternalId`: Claim an existing transformation library under a caller-owned external ID so it can be looked up without storing the RudderStack identifier.
* **Start Profiles Run** `startProfilesRun`: Trigger a Profiles project to run immediately, rebuilding the identity graph and feature tables in the warehouse.
* **Start Reverse ETL Sync** `startReverseEtlSync`: Trigger a Reverse ETL connection to sync immediately instead of waiting for its next scheduled run. Returns a 409 when a sync is already running for the connection.
* **Stop Reverse ETL Sync** `stopReverseEtlSync`: Stop the sync run currently in progress for a Reverse ETL connection.
* **Submit Reverse ETL Source Preview** `submitReverseEtlSourcePreview`: Run a SQL query against a stored warehouse credential to preview the rows a Reverse ETL source would produce. The query runs asynchronously; poll Get Reverse ETL Source Preview Result with the returned identifier. The credential must point at a reachable warehouse, otherwise RudderStack rejects the request before running the query.
* **Test Destination Connectivity** `testDestinationConnectivity`: Push a test event to a single destination and return the transformed payload and the destination's response, so credentials and mappings can be verified without sending real traffic.
* **Test Source Connectivity** `testSourceConnectivity`: Push a test event through a source and every destination connected to it, returning what each destination received and how it responded. The source must be connected to at least one destination.
* **Track Event** `trackEvent`: Record an action a user performed, along with any properties describing it. This is the core RudderStack event type for user behaviour. This action uses the Source Write Key connection, not the Workspace Access Token connection.
* **Update Account** `updateAccount`: Update a stored credential. This is a full replace: every field must be supplied, because a missing field is treated as an instruction to clear it. The account definition cannot be changed.
* **Update Catalog Category** `updateCatalogCategory`: Rename a data catalog category.
* **Update Catalog Event** `updateCatalogEvent`: Update an event definition in the data catalog. Send the full desired state: fields omitted from the request are reset rather than left unchanged.
* **Update Catalog Property** `updateCatalogProperty`: Update a property definition in the data catalog. Send the full desired state: fields omitted from the request are reset rather than left unchanged.
* **Update Connection** `updateConnection`: Enable or disable an existing source to destination connection.
* **Update Destination** `updateDestination`: Update an existing destination. Send the full desired state: fields omitted from the request are reset rather than left unchanged.
* **Update Event Stream Source** `updateEventStreamSource`: Update the name or enabled state of an event stream source created through the event stream sources API.
* **Update Reverse ETL Connection** `updateReverseEtlConnection`: Update the mutable parts of a Reverse ETL connection: its schedule, enabled state, mappings, identifiers, constants and sync settings. The source, destination and event configuration are immutable and are rejected if sent.
* **Update Reverse ETL Source** `updateReverseEtlSource`: Update a Reverse ETL source's name, credential or SQL and table configuration. Send the full desired state.
* **Update Source** `updateSource`: Update an existing event stream source. Send the full desired state: fields omitted from the request are reset rather than left unchanged.
* **Update Tracking Plan** `updateTrackingPlan`: Update a tracking plan's name or description. Event schemas are managed separately with the tracking plan event actions.
* **Update Tracking Plan Source Connection** `updateTrackingPlanSourceConnection`: Change how a source handles tracking plan violations, without disconnecting the plan.
* **Update Transformation** `updateTransformation`: Update a transformation's name, description or code, creating a new version. Publish the new version for it to take effect in the pipeline.
* **Update Transformation Library** `updateTransformationLibrary`: Update a transformation library's name, description or code, creating a new version. Publish the new version for transformations to pick it up.
* **Upsert Tracking Plan Event With Identifiers** `upsertTrackingPlanEventWithIdentifiers`: Add or replace one event in a tracking plan by referencing data catalog entries that already exist, supplying only the event ID and property IDs. Use this when the catalog is managed separately from the plan.
* **Upsert Tracking Plan Event With Properties** `upsertTrackingPlanEventWithProperties`: Add or replace one event in a tracking plan by describing its properties directly. RudderStack creates or reuses the matching data catalog entries and builds the validation schema from them. Changes are queued and typically apply within a few minutes.
* **Upsert Tracking Plan Event With Rules** `upsertTrackingPlanEventWithRules`: Add or replace one event in a tracking plan by supplying a raw JSON Schema for its payload. RudderStack has announced that this endpoint will be deprecated; prefer Upsert Tracking Plan Event With Properties for new work.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Alias | `alias` | Two identifiers for the same person were merged. RudderStack delivers the full event payload with type set to alias and the retired identifier in previousId. |
| Group | `group` | A user was associated with a group such as a company or account. RudderStack delivers the full event payload with type set to group and the group identifier in groupId. |
| Identify | `identify` | A user was identified or their traits changed. RudderStack delivers the full event payload with type set to identify and the known traits in traits. |
| Page | `page` | A web page was viewed. RudderStack delivers the full event payload with type set to page and the page details in properties. |
| Screen | `screen` | A mobile app screen was viewed. RudderStack delivers the full event payload with type set to screen. |
| Track | `track` | A user performed an action. RudderStack delivers the full event payload with type set to track and the action name in event. |
