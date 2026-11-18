---
description: "Hightouch Composable CDP and data activation platform."
hidden: true
---

# Hightouch

<img src="../../.gitbook/assets/connectors/hightouch.png" alt="Hightouch logo" width="64">

Hightouch Composable CDP and data activation platform. Manage sources, models, destinations, syncs, sync runs, audiences, event contracts, Decision Engine flows and messages, identity resolution (IDR), and sync sequences through the Hightouch Management REST API.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [hightouch.com](https://hightouch.com) |
| **Authentication** | Bearer token |
| **Slug** | `hightouch` |

## Use it

Add Hightouch from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hightouch.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Decision Engine Message | `createMessage` | Create a new message within a Decision Engine flow for a given channel. |
| Create Destination | `createDestination` | Create a new destination in Hightouch. The configuration schema depends on the destination type (e.g. salesforce, hubspot). |
| Create Event Contract | `createEventContract` | Create a new event contract in Hightouch to validate incoming events against defined schemas. |
| Create Model | `createModel` | Create a new model in Hightouch on a given source. Provide exactly one query definition (raw, custom, table, visual, or dbt) matching the queryType. Columns are introspected lazily (skipColumnQuery) so creation does not block on the source warehouse. |
| Create Source | `createSource` | Create a new data source in Hightouch. The configuration schema depends on the source type (e.g. snowflake, postgres). |
| Create Sync | `createSync` | Create a new sync in Hightouch that connects a model to a destination on a schedule. The configuration schema depends on the destination type. |
| Get Campaign Send Status | `getSendStatus` | Get the delivery status of a specific campaign send by campaign ID and send ID. |
| Get Decision Engine Flow | `getFlow` | Retrieve a single Decision Engine flow by its ID. |
| Get Decision Engine Message | `getMessage` | Retrieve a single Decision Engine message by flow ID and message ID. |
| Get Destination | `getDestination` | Retrieve a single Hightouch destination by its numeric ID. |

<details>

<summary>See 29 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Event Contract | `getEventContract` | Retrieve a single event contract by its ID, including its event definitions and event sources. |
| Get IDR Reprocess Status | `getReprocessStatus` | Get the status of an IDR reprocessing request by graph ID and request ID. |
| Get Model | `getModel` | Retrieve a single Hightouch model by its numeric ID, including its query definition. |
| Get Source | `getSource` | Retrieve a single Hightouch data source by its numeric ID. |
| Get Sync | `getSync` | Retrieve a single Hightouch sync by its numeric ID, including status and schedule. |
| Get Sync Sequence Run | `getSyncSequenceRun` | Get the status of a Hightouch sync sequence run by its run ID, including per-sync run statuses. |
| List Decision Engine Flows | `listFlows` | List all Decision Engine flows in the Hightouch workspace with optional name filter and pagination. |
| List Decision Engine Messages | `listMessages` | List all messages within a Decision Engine flow, with optional pagination. |
| List Destinations | `listDestinations` | List all destinations in the Hightouch workspace, optionally filtered by name or slug with pagination. |
| List Event Contracts | `listEventContracts` | List all event contracts in the Hightouch workspace with optional name filter and pagination. |
| List IDR Runs | `listIdrRuns` | List Identity Resolution (IDR) runs for a given identity graph, with status and stats per run. |
| List Models | `listModels` | List all models in the Hightouch workspace, optionally filtered by name, slug, or tags with pagination. |
| List Sources | `listSources` | List all data sources in the Hightouch workspace, optionally filtered by name or slug with pagination. |
| List Sync Runs | `listSyncRuns` | List the run history for a given Hightouch sync, including row counts and status per run. |
| List Syncs | `listSyncs` | List all syncs in the Hightouch workspace, optionally filtered by slug or model with pagination. |
| Queue Identifiers For Reprocessing | `queueForReprocessing` | Queue identifier values for reprocessing in a Hightouch identity graph, optionally adding them to the blocklist. |
| Trigger Campaign Send | `triggerCampaign` | Trigger an API campaign send in Hightouch to a list of recipients, with optional shared personalization properties. |
| Trigger Decision Engine Flow Run | `runFlow` | Trigger a run of a Decision Engine flow by its ID, enqueuing message decisions. |
| Trigger Identity Graph Run | `triggerIdGraphRun` | Trigger an identity graph run by graph ID, incrementally or as a full rerun. |
| Trigger IDR Run | `triggerIdrRun` | Trigger an Identity Resolution (IDR) run for a given identity graph, incrementally or as a full rerun. |
| Trigger Sync | `triggerSync` | Trigger a new run of a Hightouch sync by its numeric ID, with optional full-resync options. |
| Trigger Sync By ID or Slug | `triggerSyncByIdOrSlug` | Trigger a Hightouch sync run identified by sync ID or slug in the request body, with optional full-resync options. |
| Trigger Sync Sequence | `triggerSyncSequence` | Trigger a run of a Hightouch sync sequence by its ID. |
| Update Decision Engine Message | `updateMessage` | Update an existing Decision Engine message by flow ID and message ID. Only the provided fields are changed. |
| Update Destination | `updateDestination` | Update an existing Hightouch destination's name or configuration by its numeric ID. |
| Update Event Contract | `updateEventContract` | Update an existing event contract by its ID. Only the provided fields are changed. |
| Update Model | `updateModel` | Update an existing Hightouch model by its numeric ID. Only the provided fields are changed. |
| Update Source | `updateSource` | Update an existing Hightouch data source's name or configuration by its numeric ID. |
| Update Sync | `updateSync` | Update an existing Hightouch sync by its numeric ID. Only the provided fields are changed. |

</details>
