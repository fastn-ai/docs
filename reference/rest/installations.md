---
description: "Each customer's setup of a widget, its triggers and its configuration values."
---

# Installations and configs

An installation is one customer's setup of a widget. Creating, changing or deleting one can run the widget's [callbacks](../widget-callbacks.md).

Base URL, authentication and errors are on the [REST API overview](README.md).

## Installations

### List installations

```http
GET /v1/installations
```

Lists installations (a widget, workflow or trigger set up for one customer) visible to the caller, newest first, each with a computed healthStatus. A customer caller only sees its own. 403 when org_id is outside the caller's subtree. Requires widgets.read.

Operation: `listInstallations`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `target_type` | query | string | No | One of: `widget`, `workflow`, `trigger`, `connector_action`, `integration`, `agent`. |
| `target_id` | query | string | No |  |
| `org_id` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |
| `widget_id` | query | string | No |  |

**Responses**

* `200`: { data: [installation] }

### Create an installation

```http
POST /v1/installations
```

Creates an installation of a target for one customer. Unless defer_config is true, the widget's config template is cloned into a per-installation config. 400 when the target, customer, widget, config or a pinned connection is not the caller's; 409 when a binding already exists for target + customer + slug, or the widget allows a single activation per customer. Requires workflows.update.

Operation: `createInstallation`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `target_type` | `string` | Yes | One of: `widget`, `workflow`, `trigger`, `connector_action`, `integration`, `agent`. |
| `target_id` | `string` | Yes |  |
| `target_version` | `string` | No |  |
| `widget_id` | `string` | No |  |
| `source_template_id` | `string` | No |  |
| `label` | `string` | Yes |  |
| `slug` | `string` | No |  |
| `user_id` | `string` | No |  |
| `connections` | `object` | No |  |
| `config_id` | `string` | No |  |
| `config` | `object` | No |  |
| `status` | `string` | No | One of: `draft`, `ready`, `active`, `paused`, `error`, `archived`. |
| `provenance` | `string` | No | One of: `human`, `agent`. |
| `rationale` | `object` | No |  |
| `defer_config` | `boolean` | No |  |
| `selected_trigger_categories` | `string[]` | No |  |
| `org_id` | `string` | Yes | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `201`: Created installation
* `400`: Validation or ownership error
* `409`: Duplicate installation

### Active customer setups whose app triggers have no working subscription, so the...

```http
GET /v1/installations/trigger-health
```

Active customer setups whose app triggers have no working subscription, so the customer's events cannot start the workflow. A setup is checked only for the copies provisioning can make for it: the APP_EVENT template triggers on its own widget, inside its trigger-category selection, activation NONE excluded. Each is reported when the customer has no copy (missing) or the copy's stored subscription status is FAILED or UNSUBSCRIBED, whether the copy is enabled or not (every provisioned copy starts disabled). Copies are matched per setup, not per customer. A template provisioning refused because a sibling setup of the same customer already runs the same workflow on those events is not reported as missing; one refused because a sibling shares the subscription for a different workflow still is. Paused or polling templates and setups with no widget are not reported. Same scope as GET /api/v1/installations; at most 500 setups are read, and `truncated` says when there were more.

Operation: `getInstallationTriggerHealth`

**Responses**

* `200`: Trigger health

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.truncated` | `boolean` |  |
| `data.issues` | `object[]` |  |
| `data.issues[].installationId` | `string` |  |
| `data.issues[].installationLabel` | `string` |  |
| `data.issues[].templateTriggerId` | `string` |  |
| `data.issues[].triggerName` | `string` |  |
| `data.issues[].connectorName` | `string` |  |
| `data.issues[].triggerId` | `string` | The customer's copy, when there is one |
| `data.issues[].subscriptionStatus` | `string` |  |
| `data.issues[].problem` | `string` | One of: `missing`, `failed`, `unsubscribed`. |
| `data.issues[].orgId` | `string` | The customer this belongs to, under the id you gave it (its external ref); the account itself when it belongs to no customer. |
| `data.issues[].orgName` | `string` |  |

### Get an installation

```http
GET /v1/installations/{id}
```

Reads one installation. 404 when it is outside the caller's scope. Requires widgets.read.

Operation: `getInstallation`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Installation
* `404`: Not found

### Update an installation

```http
PUT /v1/installations/{id}
```

Updates an installation. Changing selected_trigger_categories provisions newly covered trigger instances and deletes uncovered ones. 400 when nothing applicable was sent or a referenced widget, config or connection is not the caller's; 409 on a duplicate label for the widget. Requires workflows.update.

Operation: `updateInstallation`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `target_version` | `string` | No |  |
| `widget_id` | `string` | No |  |
| `label` | `string` | No |  |
| `slug` | `string` | No |  |
| `connections` | `object` | No |  |
| `config_id` | `string` | No |  |
| `config` | `object` | No |  |
| `status` | `string` | No | One of: `draft`, `ready`, `active`, `paused`, `error`, `archived`. |
| `health_status` | `string` | No |  |
| `rationale` | `object` | No |  |
| `selected_trigger_categories` | `string[]` | No |  |

**Responses**

* `200`: Updated installation
* `400`: Validation or ownership error
* `404`: Not found
* `409`: Duplicate label

### Delete an installation

```http
DELETE /v1/installations/{id}
```

Deletes an installation and its trigger instances. Deleting an active one fires the widget's onDeactivation hook first, which can veto. Requires workflows.update.

Operation: `deleteInstallation`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted
* `404`: Not found

### Save the customer's answers to the widget's settings form (form_schema)

```http
PUT /v1/installations/{id}/form-values
```

Save the customer's answers to the widget's settings form (form_schema). Validated against that schema, stored as the installation's inline config.formValues (so workflows read them via fastn.config.getByWorkflow), and gated on the widget's onConfigurationChange hook. Requires widgets.update.

Operation: `updateInstallationFormValues`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `formValues` | `object` | Yes |  |

**Responses**

* `200`: Updated installation
* `400`: Malformed body, or the widget has no settings form
* `404`: Installation not found or out of scope
* `422`: Answers fail the form's rules ({ fieldErrors: { key: message } }), or an onConfigurationChange hook vetoed the change

### Get an installation's resolved config

```http
GET /v1/installations/{id}/resolved-config
```

The configuration the runtime sees for this installation: the config template (config_id) with the installation's inline overrides deep-merged on top. Requires widgets.read.

Operation: `getInstallationResolvedConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Merged config
* `404`: Not found

### List the widget's template triggers plus the trigger instances materialized for this...

```http
GET /v1/installations/{id}/triggers
```

List the widget's template triggers plus the trigger instances materialized for this installation (with live trigger state). Templates carry their categories tags and are never filtered by the installation's selected_trigger_categories, templates outside the selection stay available for manual creation. The installation's trigger templates (from its widget) and the live trigger instances made from them. Requires events.read.

Operation: `getInstallationTriggers`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: { templates: TriggerRef[], instances: [{ triggerId, templateTriggerId, type, createdAt, trigger }] } }. trigger carries live state plus accountId (APP_EVENT routing account; for an activation NONE trigger the customer's external ref, or its id) and orgId (the value a partner sends as x-org-id).
* `404`: Installation not found or out of scope

### Create one trigger instance from a widget template trigger (one instance per template...

```http
POST /v1/installations/{id}/triggers
```

Create one trigger instance from a widget template trigger (one instance per template per installation). The created trigger is partner-org-owned, stamped with org_id + installation_id, and its route bindings carry installationId plus x-installation-id / x-org-id headers. APP_EVENT templates subscribe with the end user's connection pinned on the installation. Fires the widget's beforeTriggerCreated (can veto/mutate settings) or onTriggerCreated hook per its lifecycle_hooks config. Materializes a trigger instance on this installation from one of its widget's template triggers, owned by the partner org with the customer as customer. 404 when the template is not attached to the widget. Requires events.create.

Operation: `createInstallationTrigger`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `templateTriggerId` | `string` | Yes |  |
| `settings` | `object` | No |  |
| `settings.name` | `string` | No |  |
| `settings.cron` | `object` | No |  |
| `settings.cron.expression` | `string` | Yes |  |
| `settings.rate` | `object` | No |  |
| `settings.rate.value` | `integer` | Yes |  |
| `settings.rate.unit` | `string` | Yes | One of: `minutes`, `hours`, `days`. |
| `settings.timezone` | `string` | No |  |
| `settings.startsAt` | `string` | No |  |
| `headers` | `object` | No |  |

**Responses**

* `201`: { data: { instance, trigger, subscription } }
* `404`: Installation or template not found
* `409`: An instance already exists for this template
* `422`: Hook veto, non-editable field, preset mismatch, extra headers not allowed, or missing APP_EVENT connection

### Update a trigger instance within the template's editableFields (preset membership...

```http
PUT /v1/installations/{id}/triggers/{triggerId}
```

Update a trigger instance within the template's editableFields (preset membership enforced unless allowCustom). Fires onTriggerUpdated. Edits a trigger instance's settings (name, cron or rate, timezone, startsAt) and extra headers. Extra headers are honoured only when the template sets allowExtraHeaders. Requires events.update.

Operation: `updateInstallationTrigger`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `triggerId` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `settings` | `object` | No |  |
| `settings.name` | `string` | No |  |
| `settings.cron` | `object` | No |  |
| `settings.cron.expression` | `string` | Yes |  |
| `settings.rate` | `object` | No |  |
| `settings.rate.value` | `integer` | Yes |  |
| `settings.rate.unit` | `string` | Yes | One of: `minutes`, `hours`, `days`. |
| `settings.timezone` | `string` | No |  |
| `settings.startsAt` | `string` | No |  |
| `headers` | `object` | No |  |

**Responses**

* `200`: Updated trigger
* `404`: Installation or instance not found
* `422`: Not editable, non-editable field, or preset mismatch

### Delete one trigger instance (unregisters schedules / third-party subscriptions via the...

```http
DELETE /v1/installations/{id}/triggers/{triggerId}
```

Delete one trigger instance (unregisters schedules / third-party subscriptions via the event service). Fires onTriggerDeleted. Deletes a trigger instance from this installation. Requires events.delete.

Operation: `deleteInstallationTrigger`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `triggerId` | path | string | Yes |  |

**Responses**

* `200`: { data: { deleted: true, triggerId } }
* `404`: Installation or instance not found

### Merge per-customer unified config values into an installation's inline config...

```http
PUT /v1/installations/{id}/unified-values
```

Merge per-customer unified config values into an installation's inline config (end_user-callable; scoped by org_id or org_id) Writes per-connector unified-API field values into the installation's inline config (connectorSlug -> fieldKey -> value). Requires unified.execute.

Operation: `updateInstallationUnifiedValues`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `unifiedValues` | `object` | Yes |  |

**Responses**

* `200`: Merged inline config
* `400`: Malformed unifiedValues
* `404`: Installation not found or out of scope

## Configs

### List configs

```http
GET /v1/configs
```

Lists integration configs (field mappings, conditions, defaults, matching) in the caller's scope. With widget_id, an embed customer also gets the template its ancestor workspace defined for that widget. Requires widgets.read.

Operation: `listConfigs`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `widget_id` | query | string | No |  |
| `org_id` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `200`: { data: [config] }

### Create a config

```http
POST /v1/configs
```

Creates a config. Either send config, or fork_from_widget_id to clone that widget's template server side. installation_id pins the new config onto that installation in the same call. 403 when org_id is outside the caller's customer scope. Requires widgets.create.

Operation: `createConfig`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `widget_id` | `string` | No |  |
| `template_config_id` | `string` | No |  |
| `fork_from_widget_id` | `string` | No |  |
| `installation_id` | `string` | No |  |
| `config` | `object` | No |  |
| `config.entities` | `object[]` | No |  |
| `config.entities[].id` | `string` | No |  |
| `config.entities[].configuration` | `object` | No |  |
| `config.directions` | `object[]` | No |  |
| `config.directions[].id` | `string` | No |  |
| `config.directions[].configuration` | `object` | No |  |
| `config.matching` | `object` | No |  |
| `config.targets` | `object[]` | No |  |
| `config.unified` | `object[]` | No |  |
| `config.unifiedValues` | `object` | No |  |
| `plan` | `object` | No |  |
| `org_id` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `201`: Created config
* `400`: Validation error, empty config, or a widget/template/installation that is not the caller's
* `403`: org_id out of scope
* `404`: installation not found

### Get a config

```http
GET /v1/configs/{id}
```

Reads one config. 404 when it is outside the caller's scope. Requires widgets.read.

Operation: `getConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Config id (cfg_*). |

**Responses**

* `200`: Config
* `404`: Not found

### Update a config

```http
PUT /v1/configs/{id}
```

Replaces the fields sent. Send baseUpdatedAt (the updatedAt you loaded) to get 409 CONFIG_CONFLICT instead of overwriting a newer save. To edit one row of an array-typed configuration prefer the /entries endpoints. Requires widgets.update.

Operation: `updateConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Config id (cfg_*). |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `widget_id` | `string` | No |  |
| `template_config_id` | `string` | No |  |
| `config` | `object` | No |  |
| `config.entities` | `object[]` | No |  |
| `config.entities[].id` | `string` | No |  |
| `config.entities[].configuration` | `object` | No |  |
| `config.directions` | `object[]` | No |  |
| `config.directions[].id` | `string` | No |  |
| `config.directions[].configuration` | `object` | No |  |
| `config.matching` | `object` | No |  |
| `config.targets` | `object[]` | No |  |
| `config.unified` | `object[]` | No |  |
| `config.unifiedValues` | `object` | No |  |
| `plan` | `object` | No |  |
| `baseUpdatedAt` | `string` | No |  |
| `org_id` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `200`: Updated config
* `400`: Validation error or nothing to update
* `404`: Not found
* `409`: CONFIG_CONFLICT: the config changed since baseUpdatedAt

### Delete a config

```http
DELETE /v1/configs/{id}
```

Deletes a config. 409 when an installation references it unless force=true. The widget's onConfigurationDelete hook runs first and can veto. Requires widgets.delete.

Operation: `deleteConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Config id (cfg_*). |
| `force` | query | boolean | No | Delete even when installations reference it. |

**Responses**

* `200`: { data: { deleted: true } }
* `404`: Not found
* `409`: Referenced by an installation

### Set configuration decisions

```http
PATCH /v1/configs/{id}/decisions
```

Sets the value of named decision fields (connector-declared defaults or AI-proposed configurationDecisions) and/or merges keys into matching. 400 DECISION_FIELDS_NOT_FOUND when no named field exists; a partial match answers 200 with the misses in unmatched. Requires widgets.update.

Operation: `updateConfigDecisions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Config id (cfg_*). |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `decisions` | `object[]` | No |  |
| `decisions[].field` | `string` | Yes |  |
| `decisions[].value` | `any` | No |  |
| `matching` | `object` | No | Keys merged over the config's matching strategy. |

**Responses**

* `200`: Updated config, plus unmatched when some fields were not found
* `400`: Neither decisions nor matching, or no field matched
* `404`: Not found

### List the rows of an array-typed configuration

```http
GET /v1/configs/{id}/entries
```

A config can declare a list, one row per thing the customer is setting up, where each row carries its own id. These endpoints address one row at a time; they are the v2 equivalent of v1's customer-configuration operations. Prefer them over PUT /configs/{id} for row edits: that rewrites the whole config, so two rows saved concurrently lose one of the two writes. Each write here is a compare-and-swap and retries against the new state rather than overwriting it.

Operation: `listConfigEntries`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Config id (cfg_*) |
| `entityId` | query | string | No | Which entity's list. Optional when the config declares exactly one; required when it declares several, since guessing would write the row into the wrong entity. |
| `connectorId` | query | string | No | Return only this connector's rows. One config commonly serves several connectors and each row names its own, so a screen about one connector filters here rather than fetching every row and sifting. Matches the v2 connector id, the v2 slug, or the raw connectorId on the row: a row written by v2 puts the v2 id in connectorId, while a row migrated from v1 keeps the v1 id there (_knexa_...) and carries v2ConnectorId / v2ConnectorSlug alongside, so matching connectorId alone would return nothing for every migrated row. Rows naming no connector at all are excluded from a filtered result, since returning them under every filter would show one row on several connectors' screens. |

**Responses**

* `200`: Rows, plus the entity they came from
* `400`: No array-typed configuration, or several and none named
* `404`: Config not found, or the named entity holds no rows

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `meta` | `object` |  |
| `meta.entityId` | `string` |  |
| `meta.entities` | `string[]` | Every entity in this config that holds rows. |
| `meta.total` | `integer` | Rows returned, always equal to data.length, filtered or not. |
| `meta.totalUnfiltered` | `integer` | Rows before the connectorId filter, present only when it narrowed the list. Tells 'filtered out' apart from 'this config is empty'. |
| `meta.multiConfig` | `boolean` | Whether this entity may hold more than one configuration record, v1's enableMultiConfigs, carried onto the entity by migration. False means the widget has exactly one configuration: render a single form, not a rows editor. Do not infer this from the configuration's shape; a single-config entity's configuration is also an array, with one element. |
| `meta.connectorId` | `string` | Echoed when the list was filtered. |

### Create a configuration row

```http
POST /v1/configs/{id}/entries
```

Omit id to have one assigned (cfe_*). A duplicate id is rejected rather than merged. A connectorId given on the body or as a query param is stamped onto the row unless values sets one, so a row created while filtered to a connector comes back under that same filter instead of being missing from the list that created it.

Operation: `createConfigEntry`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `entityId` | `string` | No |  |
| `id` | `string` | No |  |
| `connectorId` | `string` | No |  |
| `values` | `object` | No |  |

**Responses**

* `201`: Row created
* `400`: No array-typed configuration; several and none named; or a missing connectorId on a multi-config entity, whose records are keyed by (id, connectorId)
* `404`: Config not found
* `409`: A row with that id already exists; the entity holds a single configuration and already has one; or the config was modified concurrently past the retry budget

### Get one configuration row

```http
GET /v1/configs/{id}/entries/{entryId}
```

Reads one row of an array-typed configuration by its id. 404 when the config or the row does not exist. Requires widgets.read.

Operation: `getConfigEntry`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `entryId` | path | string | Yes |  |
| `entityId` | query | string | No |  |
| `connectorId` | query | string | No | Scope assertion, not a filter: the row must belong to this connector or the call answers 404, so a caller working within one connector cannot reach another's row by id. Matches the v2 id, the v2 slug, or the raw connectorId. 404 rather than 403, from that scoped view the row is genuinely absent, and saying otherwise leaks that it exists elsewhere. |

**Responses**

* `200`: The row
* `404`: Config or row not found, or the row belongs to a different connector

### Replace one configuration row

```http
PUT /v1/configs/{id}/entries/{entryId}
```

Replaces the row, as v1's update did, send the row you want, not a patch. The row keeps its id and its position in the list. An id in the body cannot rename the addressed row.

Operation: `updateConfigEntry`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `entryId` | path | string | Yes |  |
| `connectorId` | query | string | No | Scope assertion: the row must belong to this connector or the call answers 404. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `entityId` | `string` | No |  |
| `id` | `string` | No |  |
| `connectorId` | `string` | No |  |
| `values` | `object` | No |  |

**Responses**

* `200`: Row replaced
* `404`: Config or row not found
* `409`: Modified concurrently past the retry budget

### Delete one configuration row

```http
DELETE /v1/configs/{id}/entries/{entryId}
```

Removes one row of an array-typed configuration. 404 when the config or the row does not exist. Requires widgets.update.

Operation: `deleteConfigEntry`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `entryId` | path | string | Yes |  |
| `entityId` | query | string | No |  |
| `connectorId` | query | string | No | Scope assertion: the row must belong to this connector or the call answers 404. |

**Responses**

* `200`: Row deleted
* `404`: Config or row not found
* `409`: Modified concurrently past the retry budget

### Fork an inherited config template into your own org

```http
POST /v1/configs/{id}/fork
```

Creates a new template owned by your org. Pass widgetId to attach it to one of your own widgets.

Operation: `forkConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `orgId` | query | string | No | The customer: the id you gave it at creation (orgId), or fastn's id. Replaces orgId. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `widgetId` | `string` | No |  |

**Responses**

* `200`: Already forked
* `201`: data: { id, ... }
* `400`: FORK_CONFIG_NOT_TEMPLATE / FORK_CONFIG_WIDGET

### Fetch dynamic options for a configuration form field

```http
POST /v1/configs/{id}/options
```

Executes the field's optionsSource.flowId workflow (matched by workflow id or slug within the config's catalog lineage) with the caller's current form values and the config's customer context (x-org-id + x-installation-id are stamped server-side; a caller-supplied installationId pin wins over the derivation and supplies the customer). The field is identified by its dot-path id (e.g. mapdata1.channels).

Operation: `getConfigFieldOptions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Config id (cfg_*) |
| `fieldId` | query | string | Yes | Dot-path field id, e.g. mapdata1.channels |
| `side` | query | string | No | Mapping-mode fields only: which of the field's two flows to execute, source lists the items being mapped, destination lists the choices. Defaults to destination. One of: `source`, `destination`. |
| `installationId` | query | string | No | Pin the options flow to a specific installation. The flow runs as that installation's customer (its connections map selects the connection), which must be within the caller's customer scope. Wins over the server-side derivation from the config. Rejected for end_user callers. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `object` | No |  |
| `offset` | `integer` | No | Default: `0`. |
| `limit` | `integer` | No | Default: `10`. |
| `cursor` | `string` | No |  |
| `query` | `string` | No |  |

**Responses**

* `200`: Normalized options page
* `400`: Field has no dynamic options source, or missing fieldId
* `403`: end_user supplied installationId, or the pinned installation's customer is outside the caller's scope
* `404`: Config, field, options flow, or pinned installation not found
* `502`: Options workflow failed or returned an unrecognized shape
* `504`: Options workflow timed out

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.options` | `object[]` |  |
| `data.options[].value` | `string` |  |
| `data.options[].label` | `string` |  |
| `data.pageInfo` | `object` |  |
| `data.pageInfo.hasNextPage` | `boolean` | An explicit value from the flow wins; otherwise a CURSOR field has more when it returned a new cursor, and an OFFSET field when total exceeds the advanced offset (falling back to a full page). |
| `data.pageInfo.offset` | `integer` | The offset to send for the NEXT page, already advanced. Held steady on an empty page so paging cannot run off the end. Meaningless for CURSOR fields. |
| `data.pageInfo.limit` | `integer` |  |
| `data.pageInfo.endCursor` | `string` | Cursor for the next page. Read from the flow's pageInfo.endCursor or a flat cursor/curser/nextCursor/next_cursor. Null when the list is exhausted. |
| `data.pageInfo.total` | `integer` | Provider total when the flow reports one, the authoritative end-of-list signal for offset paging. |

### Upgrade a config clone from its template

```http
POST /v1/configs/{id}/upgrade
```

Moves this per-installation clone to its template's latest version. The template supplies the structure; the customer's choices are kept wherever the new version has the same item: mappings (by id, else target field), filter values (by field), setup answers (by decision id, else field), configuration-form values (by field key), custom properties, matching and unifiedValues. Customer-added mappings and filters are kept; template items the clone lacked are added. The response's merge object counts what was kept and added, and merge.lost names what goes: whole sections (with how many mappings, filters, answers and form values the customer had in each), mappings that yield to a template mapping into the same field, answers to questions no longer asked, and form values for fields no longer present. With { dryRun: true } nothing is written: the response is the same report, for confirming the upgrade before it runs. 400 when the config is not a clone. Requires widgets.update.

Operation: `upgradeConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Config id (cfg_*). |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `dryRun` | `boolean` | No | Report what the upgrade would keep, add and lose without writing anything. |

**Responses**

* `200`: Upgraded config with a merge report, or alreadyUpToDate: true
* `400`: Not a clone
* `404`: Config or its template not found

### List workflows that use a config

```http
GET /v1/configs/{id}/workflows
```

Workflows in the caller's org whose config_id is this config. Requires workflows.read.

Operation: `listConfigWorkflows`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Config id (cfg_*). |

**Responses**

* `200`: { data: [{ id, slug, name, description, execution_tier, enabled, created_at, updated_at }] }

## Config drafts

### Create a config draft for review

```http
POST /v1/config-drafts
```

Stores a finished configuration proposal (verbatim) for the user to review and returns a reviewUrl that opens the review page without signing in for 20 minutes. The draft expires after 24h. Poll getConfigDraft until status is approved, then use its configId. 503 while the store is unavailable. Requires widgets.create.

Operation: `createConfigDraft`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `proposal` | `object` | Yes |  |
| `plan` | `object` | No |  |
| `widget_id` | `string` | No |  |

**Responses**

* `201`: { data: { draftId, reviewUrl, status: "pending" } }
* `400`: Validation error
* `503`: No description.

### Propose a configuration from probes

```http
POST /v1/config-drafts/propose
```

Takes rough per-direction mappings plus the probe ids already run (POST /probes), and builds the enriched proposal server side: corrects field names against the probed fields, adds required target fields and option lists. Stores it as a draft and returns its reviewUrl like createConfigDraft. Requires widgets.create.

Operation: `proposeConfiguration`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `directions` | `object[]` | Yes |  |
| `directions[].integrationScope` | `string` | Yes |  |
| `directions[].sourceProbeId` | `string` | No |  |
| `directions[].targetProbeId` | `string` | No |  |
| `directions[].sourceConnectorSlug` | `string` | No |  |
| `directions[].sourceActionSlug` | `string` | No |  |
| `directions[].targetConnectorSlug` | `string` | No |  |
| `directions[].targetActionSlug` | `string` | No |  |
| `directions[].requiredTargetFields` | `string[]` | No |  |
| `directions[].mappings` | `object[]` | Yes |  |
| `directions[].mappings[].id` | `string` | No |  |
| `directions[].mappings[].sourceEntity` | `string` | No |  |
| `directions[].mappings[].sourceField` | `string` | Yes |  |
| `directions[].mappings[].sourceLabel` | `string` | No |  |
| `directions[].mappings[].targetEntity` | `string` | No |  |
| `directions[].mappings[].targetField` | `string` | Yes |  |
| `directions[].mappings[].targetLabel` | `string` | No |  |
| `directions[].mappings[].confidence` | `string` | No | One of: `high`, `medium`, `low`. |
| `directions[].mappings[].reason` | `string` | No |  |
| `directions[].mappings[].required` | `boolean` | No |  |
| `directions[].mappings[].condition` | `object` | No |  |
| `directions[].mappings[].valueMappings` | `object[]` | No |  |
| `directions[].mappings[].syncDirection` | `string` | No | One of: `inbound`, `outbound`, `bidirectional`. |
| `directions[].mappings[].unmappedDefault` | `any` | No |  |
| `directions[].mappings[].default` | `any` | No |  |
| `directions[].conditions` | `object` | No |  |
| `directions[].conditions.sourceConnector` | `string` | No |  |
| `directions[].conditions.sourceEntity` | `string` | No |  |
| `directions[].conditions.targetConnector` | `string` | No |  |
| `directions[].conditions.targetEntity` | `string` | No |  |
| `directions[].conditions.suggestedConditions` | `object[]` | No |  |
| `directions[].conditions.suggestedConditions[].field` | `string` | Yes |  |
| `directions[].conditions.suggestedConditions[].operator` | `string` | Yes |  |
| `directions[].conditions.suggestedConditions[].value` | `string` | Yes |  |
| `directions[].conditions.suggestedConditions[].reason` | `string` | No |  |
| `matchingStrategy` | `object` | No |  |
| `settings` | `object` | No |  |
| `plan` | `object` | No |  |
| `widget_id` | `string` | No |  |

**Responses**

* `201`: { data: { draftId, reviewUrl, status, warnings? } }; warnings names probes that were not found
* `400`: Validation error
* `503`: No description.

### Get a config draft

```http
GET /v1/config-drafts/{id}
```

Poll target after creating a draft. Until the user approves it only status is returned, with an instruction not to act on it; once approved, configId names the saved config. ?include=proposal returns the body (the review page uses it). 404 when expired or not the caller's org. Requires widgets.read.

Operation: `getConfigDraft`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Draft id (cdr_*). |
| `include` | query | string | No | One of: `proposal`. |

**Responses**

* `200`: { data: { draftId, status, configId?, ... } }
* `404`: Not found or expired

### Approve a config draft

```http
POST /v1/config-drafts/{id}/approve
```

Called by the review page when the user approves: saves the (possibly edited) configuration as a config and marks the draft approved. Approving again returns the same configId. Requires widgets.create.

Operation: `approveConfigDraft`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Draft id (cdr_*). |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `config` | `object` | Yes |  |
| `plan` | `object` | No |  |

**Responses**

* `200`: Already approved (reused: true)
* `201`: { data: { configId, status: "approved" } }
* `404`: Not found or expired
