---
description: "Knack is a no-code platform for building online databases and business apps."
hidden: true
---

# Knack

<img src="../../.gitbook/assets/connectors/knack.png" alt="Knack logo" width="64">

Knack is a no-code platform for building online databases and business apps. This connector covers the Knack REST API: application schema discovery, object-based record create, read, update and delete with filtering, sorting and pagination, view-based record operations for pages protected by logins, end-user session tokens, and asset downloads.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [knack.com](https://knack.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `knack` |

## Use it

Add Knack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.knack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Record | `createRecord` | Creates a record in a Knack object. Knack objects are defined per application, so the field values are supplied as a JSON object keyed by field key, for example {"field_23":"Acme Ltd"}. Use List Object Fields to discover the field keys and types for the object. |
| Create User Session | `createUserSession` | Authenticates an app user with their email and password and returns a user token. Pass that token to the view-based record actions to read or write through views on pages protected by a login. |
| Create View Record | `createViewRecord` | Creates a record through a form view, so the view's record rules, submit rules and connected-record defaults are applied. Field values are supplied as a JSON object keyed by Knack field key. |
| Delete Record | `deleteRecord` | Permanently deletes a record from a Knack object by its record ID. This cannot be undone. |
| Delete View Record | `deleteViewRecord` | Permanently deletes a record through a view that has a delete action, applying that view's permissions. This cannot be undone. |
| Download Asset | `downloadAsset` | Downloads a file or image asset attached to a record. The asset ID and file name come from the file or image field's raw value on the record. |
| Get Account | `getAccount` | Retrieves the Knack account that owns the connected application, including its plan, billing status, product entitlements and the applications it contains. |
| Get Application Schema | `getApplicationSchema` | Retrieves the complete schema of the connected Knack application, including every object, field, scene and view together with account, design and settings metadata. Use it to discover scene and view keys for the view-based record actions. |
| Get Object | `getObject` | Retrieves the full definition of a single Knack object, including its inflections, identifier field, connections and every field it contains. |
| Get Record | `getRecord` | Retrieves a single record from a Knack object by its record ID, returning every field value on the record. |

<details>

<summary>See 7 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get View Record | `getViewRecord` | Retrieves a single record through a view on a page, returning only the fields that view exposes. Views on pages protected by a login require a user token. |
| List Object Fields | `listObjectFields` | Lists every field defined on a Knack object, returning each field's key, label, type and whether it is required. Use the field keys when building record payloads. |
| List Objects | `listObjects` | Lists every object (table) defined in the connected Knack application, returning each object's name and key. Use the returned object key to address records with the object-based record actions. |
| List Records | `listRecords` | Retrieves records from a Knack object with optional filtering, sorting, pagination and value formatting. Records are returned with both raw and HTML-formatted field values. |
| List View Records | `listViewRecords` | Retrieves the records a specific view on a page returns, honouring that view's own source, filters and record rules. Views on pages protected by a login require a user token, which Create User Session returns. |
| Update Record | `updateRecord` | Updates an existing record in a Knack object. Only the field keys present in the supplied JSON object are changed; every other field on the record is left untouched. |
| Update View Record | `updateViewRecord` | Updates a record through a form or inline-edit view, so the view's record and submit rules are applied. Only the field keys present in the supplied JSON object are changed. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Record Created | `record.created` | Fires when a record is created in a Knack object. Knack has no public webhook-registration API, so this is registered by hand in the Knack Builder: open Flows, click Create Flow, choose the trigger Record Created and pick the object, add the step Send Webhook (under HTTP / Outgoing Webhook), paste the fastn trigger URL as the destination, set the method to POST, and in the payload builder add two literal fields alongside your record fields - event set to record.created and applicationId set to your Knack Application ID - then save and turn the Flow on. Both literal fields are required: fastn routes on event and matches the connection on applicationId, and the Flow payload is composed by the builder so Knack sends neither by itself. The schema below is the recommended payload shape, modelled on the Knack record body returned by the REST API rather than captured from a Flow delivery. |
| Record Deleted | `record.deleted` | Fires when a record is deleted from a Knack object. Knack has no public webhook-registration API, so this is registered by hand in the Knack Builder: open Flows, click Create Flow, choose the trigger Record Deleted and pick the object, add the step Send Webhook (under HTTP / Outgoing Webhook), paste the fastn trigger URL as the destination, set the method to POST, and in the payload builder add two literal fields alongside your record fields - event set to record.deleted and applicationId set to your Knack Application ID - then save and turn the Flow on. Both literal fields are required: fastn routes on event and matches the connection on applicationId, and the Flow payload is composed by the builder so Knack sends neither by itself. The schema below is the recommended payload shape, modelled on the Knack record body returned by the REST API rather than captured from a Flow delivery. |
| Record Updated | `record.updated` | Fires when a record is updated in a Knack object. Knack has no public webhook-registration API, so this is registered by hand in the Knack Builder: open Flows, click Create Flow, choose the trigger Record Updated and pick the object, add the step Send Webhook (under HTTP / Outgoing Webhook), paste the fastn trigger URL as the destination, set the method to POST, and in the payload builder add two literal fields alongside your record fields - event set to record.updated and applicationId set to your Knack Application ID - then save and turn the Flow on. Both literal fields are required: fastn routes on event and matches the connection on applicationId, and the Flow payload is composed by the builder so Knack sends neither by itself. The schema below is the recommended payload shape, modelled on the Knack record body returned by the REST API rather than captured from a Flow delivery. |
