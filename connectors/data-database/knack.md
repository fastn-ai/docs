---
description: "Knack is a no-code platform for online databases and business apps. Create, read, update and delete records, and read objects and app schema."
hidden: true
---

# Knack

<img src="../../.gitbook/assets/connectors/lg/knack.png" alt="Knack logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [knack.com](https://knack.com) |
| **Authentication** | Application ID and API key |
| **Slug** | `knack` |

## Setup

Your customers enter their application id and api key for Knack when they connect. Nothing else needs setting up.

## Use it

Add Knack from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.knack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Record</td><td><code>createRecord</code></td><td>Creates a record in a Knack object. Knack objects are defined per application, so the field values are supplied as a JSON object keyed by field key, for example {"field_23":"Acme Ltd"}. Use List Object Fields to discover the field keys and types for the object.</td></tr><tr><td>Create User Session</td><td><code>createUserSession</code></td><td>Authenticates an app user with their email and password and returns a user token. Pass that token to the view-based record actions to read or write through views on pages protected by a login.</td></tr><tr><td>Create View Record</td><td><code>createViewRecord</code></td><td>Creates a record through a form view, so the view's record rules, submit rules and connected-record defaults are applied. Field values are supplied as a JSON object keyed by Knack field key.</td></tr><tr><td>Delete Record</td><td><code>deleteRecord</code></td><td>Permanently deletes a record from a Knack object by its record ID. This cannot be undone.</td></tr><tr><td>Delete View Record</td><td><code>deleteViewRecord</code></td><td>Permanently deletes a record through a view that has a delete action, applying that view's permissions. This cannot be undone.</td></tr><tr><td>Download Asset</td><td><code>downloadAsset</code></td><td>Downloads a file or image asset attached to a record. The asset ID and file name come from the file or image field's raw value on the record.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Retrieves the Knack account that owns the connected application, including its plan, billing status, product entitlements and the applications it contains.</td></tr><tr><td>Get Application Schema</td><td><code>getApplicationSchema</code></td><td>Retrieves the complete schema of the connected Knack application, including every object, field, scene and view together with account, design and settings metadata. Use it to discover scene and view keys for the view-based record actions.</td></tr><tr><td>Get Object</td><td><code>getObject</code></td><td>Retrieves the full definition of a single Knack object, including its inflections, identifier field, connections and every field it contains.</td></tr><tr><td>Get Record</td><td><code>getRecord</code></td><td>Retrieves a single record from a Knack object by its record ID, returning every field value on the record.</td></tr></tbody></table>

<details>

<summary>View 7 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get View Record</td><td><code>getViewRecord</code></td><td>Retrieves a single record through a view on a page, returning only the fields that view exposes. Views on pages protected by a login require a user token.</td></tr><tr><td>List Object Fields</td><td><code>listObjectFields</code></td><td>Lists every field defined on a Knack object, returning each field's key, label, type and whether it is required. Use the field keys when building record payloads.</td></tr><tr><td>List Objects</td><td><code>listObjects</code></td><td>Lists every object (table) defined in the connected Knack application, returning each object's name and key. Use the returned object key to address records with the object-based record actions.</td></tr><tr><td>List Records</td><td><code>listRecords</code></td><td>Retrieves records from a Knack object with optional filtering, sorting, pagination and value formatting. Records are returned with both raw and HTML-formatted field values.</td></tr><tr><td>List View Records</td><td><code>listViewRecords</code></td><td>Retrieves the records a specific view on a page returns, honouring that view's own source, filters and record rules. Views on pages protected by a login require a user token, which Create User Session returns.</td></tr><tr><td>Update Record</td><td><code>updateRecord</code></td><td>Updates an existing record in a Knack object. Only the field keys present in the supplied JSON object are changed; every other field on the record is left untouched.</td></tr><tr><td>Update View Record</td><td><code>updateViewRecord</code></td><td>Updates a record through a form or inline-edit view, so the view's record and submit rules are applied. Only the field keys present in the supplied JSON object are changed.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Record Created</td><td><code>record.created</code></td><td>Fires when a record is created in a Knack object. Knack has no public webhook-registration API, so this is registered by hand in the Knack Builder: open Flows, click Create Flow, choose the trigger Record Created and pick the object, add the step Send Webhook (under HTTP / Outgoing Webhook), paste the fastn trigger URL as the destination, set the method to POST, and in the payload builder add two literal fields alongside your record fields - event set to record.created and applicationId set to your Knack Application ID - then save and turn the Flow on. Both literal fields are required: fastn routes on event and matches the connection on applicationId, and the Flow payload is composed by the builder so Knack sends neither by itself.</td></tr><tr><td>Record Deleted</td><td><code>record.deleted</code></td><td>Fires when a record is deleted from a Knack object. Knack has no public webhook-registration API, so this is registered by hand in the Knack Builder: open Flows, click Create Flow, choose the trigger Record Deleted and pick the object, add the step Send Webhook (under HTTP / Outgoing Webhook), paste the fastn trigger URL as the destination, set the method to POST, and in the payload builder add two literal fields alongside your record fields - event set to record.deleted and applicationId set to your Knack Application ID - then save and turn the Flow on. Both literal fields are required: fastn routes on event and matches the connection on applicationId, and the Flow payload is composed by the builder so Knack sends neither by itself.</td></tr><tr><td>Record Updated</td><td><code>record.updated</code></td><td>Fires when a record is updated in a Knack object. Knack has no public webhook-registration API, so this is registered by hand in the Knack Builder: open Flows, click Create Flow, choose the trigger Record Updated and pick the object, add the step Send Webhook (under HTTP / Outgoing Webhook), paste the fastn trigger URL as the destination, set the method to POST, and in the payload builder add two literal fields alongside your record fields - event set to record.updated and applicationId set to your Knack Application ID - then save and turn the Flow on. Both literal fields are required: fastn routes on event and matches the connection on applicationId, and the Flow payload is composed by the builder so Knack sends neither by itself.</td></tr></tbody></table>
