---
description: "Widgets, embed tokens, share links and setup links."
---

# Widgets and embedding

`lifecycle_hooks` on a widget names the workflows that run as [callbacks](../widget-callbacks.md).

Base URL, authentication and errors are on the [REST API overview](README.md).

## Widgets

### List embed widgets

```http
GET /v1/widgets
```

Your org's own integrations, plus, for a child org, the integrations its DIRECT parent built and offers it (never a grandparent's), marked inheritedFrom: you can run those, cannot edit them, and your own customers do not get them. A customised copy you made of one is yours (customisedFrom), and the copy and its original come back as two rows sharing version.groupId, exactly one version.active. Each widget carries workflowConnectors (read-only, absent when empty): the apps its workflows call per customer that are not in connectorIds, which the hub asks the customer to connect too. Derived on read; it does not count toward connectors_per_widget.

Operation: `listWidgets`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `include` | query | string | No | inherited. One of: `inherited`. |
| `orgId` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `200`: Widget list

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].orgId` | `string` | The workspace that owns this integration. Not the caller's org (whoami.org.id) means it is inherited from the provider: read-only, fork it (forkIntegration) to customise a copy. |
| `data[].forkedFromWidgetId` | `string` | Set on a copy: the provider integration it was forked from. |
| `data[].inheritedFrom` | `object` | Set on your direct parent's integration: { orgId, orgName }. Read-only; not offered to your customers. |
| `data[].customisedFrom` | `object` | Set on your customised copy: { sourceWidgetId, sourceOrgName, sourceName }. |
| `data[].version` | `object` | { groupId, kind: custom \| original, active, originalAvailable } on both rows of a customised integration. |
| `data[].name` | `string` |  |
| `data[].type` | `string` |  |
| `data[].config` | `object` |  |
| `data[].createdAt` | `string` |  |
| `total` | `integer` |  |

### Create an embed widget

```http
POST /v1/widgets
```

Create an embed widget; unified_refs attaches unified catalog entities (their mapped connectors join the manifest; no config template is created). trigger_categories defines named trigger groups (unique slugs) the installer picks from at activation; trigger_refs[].categories tags each template with those slugs (untagged = core, always provisioned). connector_refs[].connectionScope tags a registered SaaS connector with the connection scope activation must pin (registry-validated). Creates a widget in the caller's org (requires widgets.create). Idempotent by name: a live widget with the same name (case-insensitive) is returned with 200 and reused: true instead of a new one. Needs at least one connector: connector_ids, connector_refs or unified_refs. Every 400 is VALIDATION_ERROR in the same envelope as any schema failure: details[] names the field and the rule, and error reads 'Request validation failed: &lt;path>: &lt;message>'. No connector is a path-less issue 'At least one connector or unified entity is required (connector_ids, connector_refs or unified_refs)'; an unknown category is trigger_refs.N.categories; a scope outside the SaaS-connector registry is connector_refs.N.connectionScope.

Operation: `createWidget`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `description` | `string` | No |  |
| `connector_ids` | `string[]` | No |  |
| `connector_refs` | `object[]` | No |  |
| `connector_refs[].connectorId` | `string` | Yes |  |
| `connector_refs[].slug` | `string` | Yes |  |
| `connector_refs[].authMethodId` | `string` | No |  |
| `connector_refs[].authProviderId` | `string` | No |  |
| `connector_refs[].deleteOnDeactivate` | `boolean` | No |  |
| `connector_refs[].hideLogo` | `boolean` | No |  |
| `connector_refs[].optional` | `boolean` | No | The customer may leave this app unconnected and the integration still activates. With every connector optional, connecting any one of them is enough ("connect Gmail or Outlook"). Unset = required. The widget's workflows must handle the app not being connected. |
| `connector_refs[].connectionScope` | `string` | No | SaaS-connector connection scope: activation pins the customer's connection with this scope (400 when the customer has none) and the customer connect flow hides this connector. Must be in the org's saas_connectors registry for this connector. Not the OAuth scopes. |
| `workflow_ids` | `string[]` | No |  |
| `workflow_refs` | `object[]` | No |  |
| `workflow_refs[].workflowId` | `string` | Yes |  |
| `workflow_refs[].slug` | `string` | Yes |  |
| `workflow_refs[].version` | `string` | Yes |  |
| `trigger_ids` | `string[]` | No |  |
| `trigger_refs` | `object[]` | No |  |
| `trigger_refs[].triggerId` | `string` | Yes |  |
| `trigger_refs[].type` | `string` | Yes | One of: `WEBHOOK`, `SCHEDULE`, `APP_EVENT`. |
| `trigger_refs[].endUserEditable` | `boolean` | Yes |  |
| `trigger_refs[].editableFields` | `string[]` | No |  |
| `trigger_refs[].defaultSettings` | `object` | No |  |
| `trigger_refs[].label` | `string` | No |  |
| `trigger_refs[].scheduleOptions` | `object` | No |  |
| `trigger_refs[].scheduleOptions.ratePresets` | `object[]` | No |  |
| `trigger_refs[].scheduleOptions.ratePresets[].value` | `integer` | Yes |  |
| `trigger_refs[].scheduleOptions.ratePresets[].unit` | `string` | Yes | One of: `minutes`, `hours`, `days`. |
| `trigger_refs[].scheduleOptions.cronPresets` | `object[]` | No |  |
| `trigger_refs[].scheduleOptions.cronPresets[].label` | `string` | Yes |  |
| `trigger_refs[].scheduleOptions.cronPresets[].expression` | `string` | Yes |  |
| `trigger_refs[].scheduleOptions.allowCustom` | `boolean` | No |  |
| `trigger_refs[].defaultHeaders` | `object` | No |  |
| `trigger_refs[].allowExtraHeaders` | `boolean` | No |  |
| `trigger_refs[].categories` | `string[]` | No |  |
| `trigger_refs[].activation` | `string` | No | One of: `USER`, `NONE`. |
| `trigger_categories` | `object[]` | No |  |
| `trigger_categories[].slug` | `string` | Yes |  |
| `trigger_categories[].label` | `string` | Yes |  |
| `trigger_categories[].description` | `string` | No |  |
| `trigger_categories_title` | `string` | No | Heading for the activation wizard's sync-type selection step; null uses the built-in 'What do you want to sync?'. |
| `unified_refs` | `object[]` | No |  |
| `unified_refs[].entityId` | `string` | Yes |  |
| `unified_refs[].connectorSlugs` | `string[]` | No |  |
| `unified_refs[].configForm` | `object` | No |  |
| `agent_context` | `string` | No |  |
| `status` | `string` | No | One of: `active`, `draft`, `archived`. |
| `sync_direction` | `string` | No | One of: `inbound`, `outbound`, `bidirectional`. |
| `style_overrides` | `object` | No |  |
| `form_schema` | `object` | No |  |
| `lifecycle_hooks` | `object` | No |  |
| `lifecycle_hooks.onActivation` | `object` | No |  |
| `lifecycle_hooks.onActivation.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onActivation.version` | `string` | No |  |
| `lifecycle_hooks.onActivation.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onActivation.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onActivation.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onDeactivation` | `object` | No |  |
| `lifecycle_hooks.onDeactivation.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onDeactivation.version` | `string` | No |  |
| `lifecycle_hooks.onDeactivation.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onDeactivation.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onDeactivation.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onConfigurationCreated` | `object` | No |  |
| `lifecycle_hooks.onConfigurationCreated.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onConfigurationCreated.version` | `string` | No |  |
| `lifecycle_hooks.onConfigurationCreated.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onConfigurationCreated.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onConfigurationCreated.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onConfigurationChange` | `object` | No |  |
| `lifecycle_hooks.onConfigurationChange.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onConfigurationChange.version` | `string` | No |  |
| `lifecycle_hooks.onConfigurationChange.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onConfigurationChange.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onConfigurationChange.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onConfigurationDelete` | `object` | No |  |
| `lifecycle_hooks.onConfigurationDelete.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onConfigurationDelete.version` | `string` | No |  |
| `lifecycle_hooks.onConfigurationDelete.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onConfigurationDelete.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onConfigurationDelete.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onConnectionDeleted` | `object` | No |  |
| `lifecycle_hooks.onConnectionDeleted.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onConnectionDeleted.version` | `string` | No |  |
| `lifecycle_hooks.onConnectionDeleted.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onConnectionDeleted.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onConnectionDeleted.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onConnectionCreated` | `object` | No |  |
| `lifecycle_hooks.onConnectionCreated.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onConnectionCreated.version` | `string` | No |  |
| `lifecycle_hooks.onConnectionCreated.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onConnectionCreated.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onConnectionCreated.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onSetupLinkCompleted` | `object` | No |  |
| `lifecycle_hooks.onSetupLinkCompleted.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onSetupLinkCompleted.version` | `string` | No |  |
| `lifecycle_hooks.onSetupLinkCompleted.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onSetupLinkCompleted.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onSetupLinkCompleted.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.beforeTriggerCreated` | `object` | No |  |
| `lifecycle_hooks.beforeTriggerCreated.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.beforeTriggerCreated.version` | `string` | No |  |
| `lifecycle_hooks.beforeTriggerCreated.enabled` | `boolean` | No |  |
| `lifecycle_hooks.beforeTriggerCreated.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.beforeTriggerCreated.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onTriggerCreated` | `object` | No |  |
| `lifecycle_hooks.onTriggerCreated.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onTriggerCreated.version` | `string` | No |  |
| `lifecycle_hooks.onTriggerCreated.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onTriggerCreated.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onTriggerCreated.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.beforeTriggerUpdated` | `object` | No |  |
| `lifecycle_hooks.beforeTriggerUpdated.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.beforeTriggerUpdated.version` | `string` | No |  |
| `lifecycle_hooks.beforeTriggerUpdated.enabled` | `boolean` | No |  |
| `lifecycle_hooks.beforeTriggerUpdated.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.beforeTriggerUpdated.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onTriggerUpdated` | `object` | No |  |
| `lifecycle_hooks.onTriggerUpdated.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onTriggerUpdated.version` | `string` | No |  |
| `lifecycle_hooks.onTriggerUpdated.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onTriggerUpdated.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onTriggerUpdated.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.beforeTriggerDeleted` | `object` | No |  |
| `lifecycle_hooks.beforeTriggerDeleted.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.beforeTriggerDeleted.version` | `string` | No |  |
| `lifecycle_hooks.beforeTriggerDeleted.enabled` | `boolean` | No |  |
| `lifecycle_hooks.beforeTriggerDeleted.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.beforeTriggerDeleted.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onTriggerDeleted` | `object` | No |  |
| `lifecycle_hooks.onTriggerDeleted.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onTriggerDeleted.version` | `string` | No |  |
| `lifecycle_hooks.onTriggerDeleted.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onTriggerDeleted.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onTriggerDeleted.runForCustomer` | `boolean` | No |  |
| `activation_mode` | `string` | No | One of: `SINGLE_ACTIVATION`, `MULTI_CONNECTION`. |
| `enabled` | `boolean` | No |  |
| `allowed_end_org_ids` | `string[]` | No |  |

**Responses**

* `201`: Widget created
* `400`: Every 400 is VALIDATION_ERROR in the same envelope as any schema failure: details and issues list every { path, message }, error reads "Request validation failed: &lt;path>: &lt;message>" for the first three, and traceId is set when the request was traced. The rules: no connector (connector_ids, connector_refs and unified_refs all absent or empty) is a path-less issue "At least one connector or unified entity is required (connector_ids, connector_refs or unified_refs)", reported alongside any other failed field; a missing or invalid field (e.g. name, 1-100 characters); trigger_categories: slugs must be unique; trigger_refs.N.categories: every category a ref tags must be in trigger_categories; connector_refs.N.connectionScope: must be in the org's saas_connectors registry for that connector; unified_refs.N.entityId / .connectorSlugs / .configForm: an unknown unified entity, a provider it has no enabled mapping for, or a config form for an unselected provider or with a duplicate key; body: the body is not JSON.
* `403`: quota_exceeded: the widget would list more distinct connectors than connectors_per_widget allows (2 on every plan). An update is refused only when it adds connectors.

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.id` | `string` |  |
| `data.name` | `string` |  |
| `data.type` | `string` |  |
| `data.createdAt` | `string` |  |

### Which of your customers have the widget embedded in their product

```http
GET /v1/widgets/embed-status
```

One entry per customer of the partner (its direct children, whatever their org type), each with whether the widget is embedded in that customer's product. A sighting is recorded when that customer's embed session (a customer-scoped embed token; not a share link or any scoped setup/connect link) lists its widgets from a page whose host is known, from the request Origin or, on the iframe path, the frame's Referer. A widget URL opened in a tab of its own is not counted. Only the partner's own widgets are recorded. status is active when last seen within activeWindowDays, inactive when seen before that, never when not seen (with widgetId, when that widget was not seen). host is the partner page it was last seen on. widgets lists each widget that customer's hub served, with its own first and last sighting. lastSeenAt is coarse: at most one write per customer every few minutes. At most 2000 customers, most recently seen first then never-seen by name; truncated is true when there were more. For each SaaS partner to track its own customers: requires widgets.read and an account-tier role (owner, admin, developer) acting as the partner. A customer-scoped session (embed token, customer-pinned or customer-scoped API key) and operator, viewer and end_user are refused.

Operation: `getWidgetEmbedStatus`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `widgetId` | query | string | No | Only customers whose hub served this widget |

**Responses**

* `200`: data: { activeWindowDays, truncated, customers: [{ orgId, name, status: active \| inactive \| never, firstSeenAt, lastSeenAt, host, widgets: [{ widgetId, firstSeenAt, lastSeenAt }] }] }
* `400`: widgetId empty or longer than 100 characters, or no organisation selected
* `403`: A customer-scoped session, or a role below account tier

### Widget/workflow summary

```http
GET /v1/widgets/insights
```

Run and record counts come from pre-aggregated counts, so any window up to 365 days answers in milliseconds. Every window is whole calendar days in `tz`: a preset of N days is today plus the N-1 days before it; `from`/`to` are exactly those days.

Operation: `getWidgetInsights`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `range` | query | string | No | One of: `1d`, `7d`, `14d`, `30d`, `90d`. |
| `days` | query | integer | No | Custom length in days, ending today. Overrides range. |
| `from` | query | string | No | Start of a calendar window (YYYY-MM-DD, inclusive). Must be sent with `to`; overrides range/days. |
| `to` | query | string | No | End of the window (YYYY-MM-DD, inclusive of the whole day). Must be sent with `from`. |
| `tz` | query | string | No | IANA zone the window's days are in; UTC when omitted or unrecognised. |
| `orgId` | query | string | No | The customer: the id you gave it at creation (orgId), or fastn's id. Replaces orgId. |

**Responses**

* `200`: runsToday, recordsProcessed, needsAttention, connector summary, failedRuns, per-workflow lastRunStatus with dead-workflow signal. `window` is the exact { from, to } the numbers cover; `historyFrom` is the earliest instant counts are held from (null: none yet), a window starting earlier is answered for its covered part only.
* `400`: Invalid range/days, a half-specified or inverted from..to, or a span over 365 days

### Widget insights, right now: runs processing and queued and trigger deliveries due...

```http
GET /v1/widgets/insights/live
```

Widget insights, right now: runs processing and queued and trigger deliveries due another retry, in the insights panel's scope. Not windowed; read from the in-flight rows. Scoped like getWidgetInsights: the caller's org, narrowed to one customer for an end_user or by orgId. range is still validated (400 on an unknown value) but does not change the answer.

Operation: `getLiveWidgetInsights`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `orgId` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |
| `range` | query | string | No | One of: `1d`, `7d`, `14d`, `30d`, `90d`. |

**Responses**

* `200`: data: processing, queued, oldestProcessingSeconds, oldestQueuedSeconds, stuck (queued runs waiting over stuckAfterSeconds), retrying, per-workflow and per-customer counts, and the longest-running / longest-waiting runs and oldest retrying deliveries. `degraded` names any read that failed.
* `400`: Invalid range
* `403`: orgId is outside the caller's customer scope

### Partner reporting: the same operational metrics as /widgets/insights, totalled across...

```http
GET /v1/widgets/insights/tenants
```

Partner reporting: the same operational metrics as /widgets/insights, totalled across every customer of the calling account plus one row per customer. Workflows labelled Internal or Staging are left out of every number. Totals span all customers and ignore ?q; only the table is filtered. Refused for a customer-scoped session (an embed token or customer-pinned API key), whose 'customers' would be its own siblings, and for roles below developer. Account-wide reporting across the caller's customers: totals, chart series, failure categories, per-workflow and per-connector rows, and a sorted, paged per-customer table. Refused (403) for customer-scoped sessions and roles below the account tier.

Operation: `getTenantInsights`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `range` | query | string | No | One of: `1d`, `7d`, `14d`, `30d`, `90d`. |
| `days` | query | integer | No | Custom lookback window, overrides range. |
| `sort` | query | string | No | One of: `failed`, `runs`, `records`, `name`, `activity`. |
| `dir` | query | string | No | One of: `asc`, `desc`. |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No |  |
| `q` | query | string | No | Filter the table by customer name. |
| `tz` | query | string | No | IANA zone for the chart buckets and for resolving from/to; UTC when omitted or unrecognised. |
| `from` | query | string | No | Start of a real calendar window (YYYY-MM-DD, inclusive). Must be sent with `to`; overrides range/days. Unlike the widget panel's custom range this is a window, not a lookback length. |
| `to` | query | string | No | End of the window (YYYY-MM-DD, inclusive of the whole day). Must be sent with `from`. |
| `health` | query | string | No | Filter the customer list to one verdict. Never affects totals. One of: `healthy`, `needs_attention`, `idle`, `never_connected`. |
| `customer` | query | string | No | Narrow EVERY number, totals, charts, workflows, connectors, to one of the caller's own customers (404 otherwise). |

**Responses**

* `200`: Every runs object (totals, each customer, `own`) is { total, succeeded, failed, running }: `running` is runs created in the window, started and not ended yet (read live), and `succeeded` = total - failed - running, the runs that completed. totals (runs, records, connections, needsAttention across all customers in scope, and `byHealth`: customers per verdict, each equal to that `?health=` list's length; `timing`: start-to-end time of runs finished in the window, p50/p90/p95 as bucket bounds, slowest, average and average queue wait; `retries`: trigger deliveries that exhausted every retry, by customer, the partner's own counted separately, with the top errors; and `recovered` / `ownRecovered`: deliveries that failed and then succeeded on an automatic retry, by when they succeeded, with `avgRetries` (failed attempts before success, over queue retries), `avgRecoverMs` (mean time from first runnable, or from going to the DLQ, to success; null when known for none), `recoveredFrom` (when recording began, or the retention cut-off) and `byCustomer[].recovered`; all absent when the read failed (`retryRecoveries` in `degraded`) or the window ended before recording began; `sentToDlq` / `ownSentToDlq`: deliveries that went to the DLQ in the window, including ones a replay has since cleared (`exhausted` is only those still there), with `sentToDlqFrom` (when that record became complete; a window starting earlier counts only deliveries still in the DLQ then) and `byCustomer[].sentToDlq`, absent when that read failed (`sentToDlq` in `degraded`); `alerts`: alert firings in the window for the partner's and its customers' rules, test sends and outage notices excluded, as `fired`, `undelivered` (a channel did not accept it), `ruleCount`, `historyFrom` (set when the window reaches past the 90 days firings are kept) and `rules` (the busiest 200, each with its owner, firings, undelivered and last fired); `events` (null when that read failed): `received` events of triggers in scope, split into `processedFirstAttempt`, `recovered` (failed first, then a retry or replay succeeded), `notProcessed` (failed or never ran, nothing since succeeded) and `inProgress`; `received` counts only events routed to a workflow; `unattributed`, events on the partner's own triggers, which a one-customer view cannot split by customer (0 otherwise); `heldFrom`, the earliest hour the outcome counts has filled (null when none yet); `replays` { replayed, succeeded, failed }: events replayed from the executions page, as an event replay, or delivered by a DLQ replay or automatic DLQ retry (not told apart), and of those the ones now processed and the ones still not; a DLQ replay or retry that fails is not counted, null while no hour in the window has them computed; and `replaysPartial`, true while some hours do not), `timingFrom`, a page of per-customer rows with a health verdict, and connectionsTruncated. Plus the chart data the widget's Insights panel renders: `series` (zero-filled runs, failed runs and records buckets, `timing`, per chart bucket, finished runs and p50/p90/p95 read off that bucket's own timing sums (bounds, like `totals.timing`); `finished` is null for a bucket that ended before `timingFrom`, meaning unknown, and a percentile is null where nothing finished, and `prevRuns`, the same days one window-length earlier, for the trend delta), `failureCategories` (failing runs by kind, with the DISTINCT customers each reaches, `byCustomer` and the most frequent error `examples`), `workflows` (per workflow: runs, succeeded, failed, running, avg duration, records, latest run) and `connectors` (per connector: customers connected, healthy, broken, actions, failed actions). `window` is the exact { from, to } covered; `historyFrom` the earliest instant counts are held from; `customer` echoes the filter. A null `connections` on a row or in totals means the read was unavailable or cut short, unknown, never zero; `degraded` names which read (`alerts` when the alert counts failed or the window is wholly older than the firings kept).
* `400`: Invalid range/days/sort/dir/limit/offset/health, a half-specified or inverted from..to, a span over 365 days, or no organisation in scope
* `403`: Customer-scoped session, or a role that cannot read other organisations' reporting
* `404`: `customer` is not one of the caller's own customers

### Partner reporting, right now: runs processing and queued (with the oldest age of...

```http
GET /v1/widgets/insights/tenants/live
```

Partner reporting, right now: runs processing and queued (with the oldest age of each), and trigger deliveries due another retry, across every customer or one. Not windowed; read from the in-flight rows. In-flight snapshot across the caller's customers (or one, via customer): runs processing and queued and trigger deliveries awaiting retry. Refused (403) for customer-scoped sessions and roles below the account tier.

Operation: `getLiveTenantInsights`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `customer` | query | string | No | Narrow to one of the caller's own customers (404 otherwise). |

**Responses**

* `200`: processing, queued, oldestProcessingSeconds, oldestQueuedSeconds, stuck (queued runs waiting over stuckAfterSeconds), retrying, byWorkflow and byCustomer counts, the longest-running/longest-waiting runs (`processingRuns`, `queuedRuns`, at most 50 each) and the oldest retrying deliveries (`retryingDeliveries`, at most 50). `degraded` names any read that failed, those counts are then unknown, not zero.
* `403`: Customer-scoped session, or a role that cannot read other organisations' reporting
* `404`: `customer` is not one of the caller's own customers

### Get widget

```http
GET /v1/widgets/{id}
```

Returns one widget. An end_user gets only a widget its catalog lists (enabled and allowed for its customer); a child org's team can also read its direct parent's widget, returned with inheritedFrom. 404 when out of scope. workflowConnectors (read-only, absent when empty) lists the apps the widget's workflows call per customer (MULTI_TENANT manifest entries) that are not in connectorIds: the hub asks the customer to connect them too. It is derived on read, never stored, and does not count toward connectors_per_widget. connectorRefs[].optional marks an app the customer may leave unconnected; with every app optional, any one is enough.

Operation: `getWidget`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `include` | query | string | No | inherited. One of: `inherited`. |

**Responses**

* `200`: Widget
* `404`: Not found

### Update widget

```http
PUT /v1/widgets/{id}
```

Update widget. Shrinking trigger_categories while trigger_refs still tag a removed slug is rejected (400). connector_refs[].connectionScope (SaaS-connector activation pinning) is validated against the org's saas_connectors registry. Partial update; omitted fields keep their stored value, and an omitted unified_refs[].configForm keeps the stored form. The integration's How it works doc is changed with updateWidgetDocs, not here. Allowed when the caller is owner/admin/developer in the widget's owning workspace; 403 WIDGET_NOT_IN_ACCOUNT otherwise (an inherited widget must be forked first). Every 400 is VALIDATION_ERROR in the same envelope as any schema failure, details[] naming the field and the rule: id for a malformed id in the URL, and the path-less 'At least one connector or unified entity is required (connector_ids, connector_refs or unified_refs)' when the update would leave no connector and no unified entity. Only fields the request sent are named; a stored value that breaks a rule is reported on the sent field that kept it, with the message saying it is stored.

Operation: `updateWidget`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `connector_ids` | `string[]` | No |  |
| `connector_refs` | `object[]` | No |  |
| `connector_refs[].connectorId` | `string` | Yes |  |
| `connector_refs[].slug` | `string` | Yes |  |
| `connector_refs[].authMethodId` | `string` | No |  |
| `connector_refs[].authProviderId` | `string` | No |  |
| `connector_refs[].deleteOnDeactivate` | `boolean` | No |  |
| `connector_refs[].hideLogo` | `boolean` | No |  |
| `connector_refs[].optional` | `boolean` | No | The customer may leave this app unconnected and the integration still activates. With every connector optional, connecting any one of them is enough ("connect Gmail or Outlook"). Unset = required. The widget's workflows must handle the app not being connected. |
| `connector_refs[].connectionScope` | `string` | No | SaaS-connector connection scope: activation pins the customer's connection with this scope (400 when the customer has none) and the customer connect flow hides this connector. Must be in the org's saas_connectors registry for this connector. Not the OAuth scopes. |
| `workflow_ids` | `string[]` | No |  |
| `workflow_refs` | `object[]` | No |  |
| `workflow_refs[].workflowId` | `string` | Yes |  |
| `workflow_refs[].slug` | `string` | Yes |  |
| `workflow_refs[].version` | `string` | Yes |  |
| `trigger_ids` | `string[]` | No |  |
| `trigger_refs` | `object[]` | No |  |
| `trigger_refs[].triggerId` | `string` | Yes |  |
| `trigger_refs[].type` | `string` | Yes | One of: `WEBHOOK`, `SCHEDULE`, `APP_EVENT`. |
| `trigger_refs[].endUserEditable` | `boolean` | Yes |  |
| `trigger_refs[].editableFields` | `string[]` | No |  |
| `trigger_refs[].defaultSettings` | `object` | No |  |
| `trigger_refs[].label` | `string` | No |  |
| `trigger_refs[].scheduleOptions` | `object` | No |  |
| `trigger_refs[].scheduleOptions.ratePresets` | `object[]` | No |  |
| `trigger_refs[].scheduleOptions.ratePresets[].value` | `integer` | Yes |  |
| `trigger_refs[].scheduleOptions.ratePresets[].unit` | `string` | Yes | One of: `minutes`, `hours`, `days`. |
| `trigger_refs[].scheduleOptions.cronPresets` | `object[]` | No |  |
| `trigger_refs[].scheduleOptions.cronPresets[].label` | `string` | Yes |  |
| `trigger_refs[].scheduleOptions.cronPresets[].expression` | `string` | Yes |  |
| `trigger_refs[].scheduleOptions.allowCustom` | `boolean` | No |  |
| `trigger_refs[].defaultHeaders` | `object` | No |  |
| `trigger_refs[].allowExtraHeaders` | `boolean` | No |  |
| `trigger_refs[].categories` | `string[]` | No |  |
| `trigger_refs[].activation` | `string` | No | One of: `USER`, `NONE`. |
| `trigger_categories` | `object[]` | No |  |
| `trigger_categories[].slug` | `string` | Yes |  |
| `trigger_categories[].label` | `string` | Yes |  |
| `trigger_categories[].description` | `string` | No |  |
| `trigger_categories_title` | `string` | No | Heading for the activation wizard's sync-type selection step; null uses the built-in 'What do you want to sync?'. |
| `unified_refs` | `object[]` | No |  |
| `unified_refs[].entityId` | `string` | Yes |  |
| `unified_refs[].connectorSlugs` | `string[]` | No |  |
| `unified_refs[].configForm` | `object` | No |  |
| `agent_context` | `string` | No |  |
| `status` | `string` | No | One of: `active`, `draft`, `archived`. |
| `sync_direction` | `string` | No | One of: `inbound`, `outbound`, `bidirectional`. |
| `style_overrides` | `object` | No |  |
| `form_schema` | `object` | No |  |
| `lifecycle_hooks` | `object` | No |  |
| `lifecycle_hooks.onActivation` | `object` | No |  |
| `lifecycle_hooks.onActivation.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onActivation.version` | `string` | No |  |
| `lifecycle_hooks.onActivation.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onActivation.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onActivation.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onDeactivation` | `object` | No |  |
| `lifecycle_hooks.onDeactivation.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onDeactivation.version` | `string` | No |  |
| `lifecycle_hooks.onDeactivation.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onDeactivation.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onDeactivation.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onConfigurationCreated` | `object` | No |  |
| `lifecycle_hooks.onConfigurationCreated.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onConfigurationCreated.version` | `string` | No |  |
| `lifecycle_hooks.onConfigurationCreated.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onConfigurationCreated.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onConfigurationCreated.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onConfigurationChange` | `object` | No |  |
| `lifecycle_hooks.onConfigurationChange.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onConfigurationChange.version` | `string` | No |  |
| `lifecycle_hooks.onConfigurationChange.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onConfigurationChange.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onConfigurationChange.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onConfigurationDelete` | `object` | No |  |
| `lifecycle_hooks.onConfigurationDelete.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onConfigurationDelete.version` | `string` | No |  |
| `lifecycle_hooks.onConfigurationDelete.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onConfigurationDelete.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onConfigurationDelete.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onConnectionDeleted` | `object` | No |  |
| `lifecycle_hooks.onConnectionDeleted.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onConnectionDeleted.version` | `string` | No |  |
| `lifecycle_hooks.onConnectionDeleted.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onConnectionDeleted.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onConnectionDeleted.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onConnectionCreated` | `object` | No |  |
| `lifecycle_hooks.onConnectionCreated.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onConnectionCreated.version` | `string` | No |  |
| `lifecycle_hooks.onConnectionCreated.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onConnectionCreated.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onConnectionCreated.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onSetupLinkCompleted` | `object` | No |  |
| `lifecycle_hooks.onSetupLinkCompleted.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onSetupLinkCompleted.version` | `string` | No |  |
| `lifecycle_hooks.onSetupLinkCompleted.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onSetupLinkCompleted.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onSetupLinkCompleted.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.beforeTriggerCreated` | `object` | No |  |
| `lifecycle_hooks.beforeTriggerCreated.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.beforeTriggerCreated.version` | `string` | No |  |
| `lifecycle_hooks.beforeTriggerCreated.enabled` | `boolean` | No |  |
| `lifecycle_hooks.beforeTriggerCreated.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.beforeTriggerCreated.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onTriggerCreated` | `object` | No |  |
| `lifecycle_hooks.onTriggerCreated.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onTriggerCreated.version` | `string` | No |  |
| `lifecycle_hooks.onTriggerCreated.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onTriggerCreated.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onTriggerCreated.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.beforeTriggerUpdated` | `object` | No |  |
| `lifecycle_hooks.beforeTriggerUpdated.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.beforeTriggerUpdated.version` | `string` | No |  |
| `lifecycle_hooks.beforeTriggerUpdated.enabled` | `boolean` | No |  |
| `lifecycle_hooks.beforeTriggerUpdated.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.beforeTriggerUpdated.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onTriggerUpdated` | `object` | No |  |
| `lifecycle_hooks.onTriggerUpdated.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onTriggerUpdated.version` | `string` | No |  |
| `lifecycle_hooks.onTriggerUpdated.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onTriggerUpdated.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onTriggerUpdated.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.beforeTriggerDeleted` | `object` | No |  |
| `lifecycle_hooks.beforeTriggerDeleted.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.beforeTriggerDeleted.version` | `string` | No |  |
| `lifecycle_hooks.beforeTriggerDeleted.enabled` | `boolean` | No |  |
| `lifecycle_hooks.beforeTriggerDeleted.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.beforeTriggerDeleted.runForCustomer` | `boolean` | No |  |
| `lifecycle_hooks.onTriggerDeleted` | `object` | No |  |
| `lifecycle_hooks.onTriggerDeleted.workflowId` | `string` | Yes |  |
| `lifecycle_hooks.onTriggerDeleted.version` | `string` | No |  |
| `lifecycle_hooks.onTriggerDeleted.enabled` | `boolean` | No |  |
| `lifecycle_hooks.onTriggerDeleted.mode` | `string` | No | One of: `blocking`, `background`. |
| `lifecycle_hooks.onTriggerDeleted.runForCustomer` | `boolean` | No |  |
| `activation_mode` | `string` | No | One of: `SINGLE_ACTIVATION`, `MULTI_CONNECTION`. |
| `enabled` | `boolean` | No |  |
| `allowed_end_org_ids` | `string[]` | No |  |

**Responses**

* `200`: Updated
* `400`: Every 400 is VALIDATION_ERROR in the same envelope as any schema failure: details and issues list every { path, message }, error reads "Request validation failed: &lt;path>: &lt;message>" for the first three, and traceId is set when the request was traced. Only fields this request sent are named: a rule broken by a stored value names the sent field that kept or exposed it, and the message says the value is stored. id: the id in the URL is malformed; an update that would leave no connector and no unified entity is the same path-less issue as on create, "At least one connector or unified entity is required (connector_ids, connector_refs or unified_refs)"; a field that fails the schema; trigger_categories: slugs must be unique, or the new catalog drops a category a stored trigger ref still tags; trigger_refs.N.categories (trigger_ids.N for an ids-only update carrying a stored ref): every category a ref tags must be in the resulting trigger_categories; connector_refs.N.connectionScope (connector_ids.N for an ids-only update keeping a stored scope): must be in the org's saas_connectors registry for that connector; unified_refs.N.entityId / .connectorSlugs / .configForm: as on create; body: not JSON, or no field to update.
* `403`: quota_exceeded: the widget would list more distinct connectors than connectors_per_widget allows (2 on every plan). An update is refused only when it adds connectors.

### Delete widget

```http
DELETE /v1/widgets/{id}
```

Hard-deletes the widget. Customers running it who have their own customised copy are moved onto that copy first, and every remaining installation of it is archived. Allowed for owner/admin/developer of the widget's owning workspace; 403 WIDGET_NOT_IN_ACCOUNT otherwise.

Operation: `deleteWidget`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted

### Choose which version of a customised integration your org runs

```http
PUT /v1/widgets/{id}/active-version
```

{id} is the ORIGINAL widget. activeWidgetId is either the original itself or your org's live fork of it. In the customer catalog (GET /widgets as an end user) the pair is returned as two rows sharing version.groupId, exactly one with version.active = true. Exactly one version runs: switching pauses the customer's active setups on the version it leaves, resumes the ones an earlier switch paused on the version it returns to, and where that version has no setup yet recreates the paused ones on it with the same connections, label and answers (data.carried). A setup cannot be created or resumed on the inactive version (409 VERSION_INACTIVE). Ask the customer before switching. Accepts ?orgId= for a partner previewing a customer.

Operation: `setWidgetActiveVersion`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `orgId` | query | string | No | The customer: the id you gave it at creation (orgId), or fastn's id. Replaces orgId. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `activeWidgetId` | `string` | Yes |  |

**Responses**

* `200`: data: { sourceWidgetId, activeWidgetId, kind: custom \| original, paused, resumed, carried, failed }
* `400`: VERSION_NOT_IN_GROUP
* `404`: VERSION_NO_FORK
* `409`: VERSION_PAUSE_FAILED: a setup on the current version could not be paused, so nothing was switched

### Read an integration's How it works doc

```http
GET /v1/widgets/{id}/docs
```

The one customer-facing How it works document for an integration (widget): what it does, every sync it runs, how it works, what the customer can configure, what they need first, recipes and troubleshooting. It is shown in the hub on the integration's card and detail view. markdown is the owner's own text when set (source: override, written with updateWidgetDocs), otherwise the AI-generated doc (source: generated), otherwise null. The generated doc is written from the integration's real contract (its apps, every live workflow's own help article and behaviour, its triggers and its config template) and never contains code, ids or internal mechanics. When the generated doc is missing or out of date, reading it starts a background generation and answers pending: true, so poll until pending is false. stale: true means a newer doc is on its way. visibleToEndUsers says whether customers (end users in the embed) can see it: they only can when it is true, the owner's team always can. An end_user caller gets 404 while it is false. Requires widgets.read.

Operation: `getWidgetDocs`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `orgId` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |
| `include` | query | string | No | Also resolve a widget the caller's direct parent offers it, as GET /api/v1/widgets/{id} does One of: `inherited`. |

**Responses**

* `200`: data: { widgetId, markdown (string or null), source (override, generated or null), generatedAt (string or null), stale, pending, visibleToEndUsers }
* `404`: Widget not found or not visible to the caller, or the caller is an end_user and the owner has not made the doc visible to customers

### Update an integration's How it works doc

```http
PUT /v1/widgets/{id}/docs
```

The one way to change an integration's customer-facing How it works doc. markdown replaces the AI-generated doc with your own text for everyone who reads it (the whole document, in Markdown, written for the customer: no ids, code or internal details). resetToGenerated: true drops your own text and goes back to the generated doc, which is kept (it is never deleted, and there is no way to delete the doc). visibleToEndUsers shows or hides the doc from your customers (end users in the embed): turn it on only when the owner agrees. Send at least one field. markdown and resetToGenerated cannot be combined. Answers the doc as it now reads, same shape as getWidgetDocs. Allowed for owner, admin or developer of the widget's owning workspace. Requires widgets.update.

Operation: `updateWidgetDocs`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `markdown` | `string` | No | Your own text for the integration's How it works doc, the whole document in Markdown. It replaces the AI-generated doc for everyone who reads it, including your customers when visibleToEndUsers is true. Write for the customer: what the integration does, every sync it runs, how it works, what they can configure. No ids, code or internal details. |
| `visibleToEndUsers` | `boolean` | No | Whether your customers (end users in the embed) can read the doc. Off by default. Your own team always can. Turn it on only when the owner agrees. |
| `resetToGenerated` | `boolean` | No | true drops your own text and goes back to the AI-generated doc. The generated doc itself is kept. Cannot be combined with markdown. Always `True`. |

**Responses**

* `200`: data: { widgetId, markdown, source, generatedAt, stale, pending, visibleToEndUsers }
* `400`: Empty body, markdown and resetToGenerated together, empty or over 50,000 characters of markdown, or an unknown field
* `403`: WIDGET_NOT_IN_ACCOUNT: the caller cannot change this widget (an inherited widget must be forked first)
* `404`: Widget not found

### Fork an inherited widget and its config template into your own org

```http
POST /v1/widgets/{id}/fork
```

Copies only the widget row and its config template; the copy keeps pointing at the parent's workflows, triggers and connectors. Use forkIntegration to copy those too.

Operation: `forkWidget`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `orgId` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |

**Responses**

* `200`: Already forked (reused: true)
* `201`: Widget, plus forkedConfigId
* `400`: FORK_NO_PARENT / FORK_OWN_RESOURCE
* `403`: FORK_NOT_CHILD
* `404`: Not found

### Regenerate an integration's How it works doc

```http
POST /v1/widgets/{id}/generate-docs
```

Starts a fresh AI generation of the integration's customer-facing How it works doc, even when nothing it depends on changed. Asynchronous: it answers 202 at once, so poll getWidgetDocs until pending is false. The doc also regenerates on its own when the integration, one of its workflows, its triggers or its config template change. When a workflow's own help article is missing, that is written first and the integration doc waits for it, so a generation can take a few minutes. Your own text (set with updateWidgetDocs) still wins over the generated doc until you reset it. Allowed for owner, admin or developer of the widget's owning workspace. Requires widgets.update.

Operation: `generateWidgetDocs`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `202`: data: { widgetId, generating: true }
* `403`: WIDGET_NOT_IN_ACCOUNT: the caller cannot change this widget (an inherited widget must be forked first)
* `404`: Widget not found

### Load select options for a widget's unified config field by executing the snippet...

```http
POST /v1/widgets/{widgetId}/unified-config/options
```

Load select options for a widget's unified config field by executing the snippet stored on the widget (never client-supplied code); params become ctx.input for cascading selects. Runs the options snippet stored on the widget's unified config field in the workflow sandbox and returns the options, filtered by query and paged by offset/limit. An end_user may not name another customer or installation (403).

Operation: `loadUnifiedConfigFieldOptions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `widgetId` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `entityId` | `string` | Yes |  |
| `connectorSlug` | `string` | Yes |  |
| `fieldKey` | `string` | Yes |  |
| `params` | `object` | No |  |
| `installationId` | `string` | No |  |
| `offset` | `integer` | No | Default: `0`. |
| `limit` | `integer` | No | Page size, at most the server's option ceiling (UNIFIED_CONFIG_MAX_OPTIONS). Defaults to the whole result set. Default: `5000`. |
| `query` | `string` | No | Case-insensitive substring filter over label then value, applied server-side to what the snippet returned. |
| `orgId` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `200`: { options: [{value, label}], pageInfo: { hasNextPage, offset, limit, endCursor, total, truncated, truncatedAt, returnedCount, droppedOptions }, durationMs }. truncated means the snippet returned more than the platform ceiling (UNIFIED_CONFIG_MAX_OPTIONS, default 5000) and the surplus is not reachable by paging or query, total is then a floor.
* `400`: Unknown field (UNIFIED_CONFIG_UNKNOWN_FIELD)
* `403`: end_user supplied orgId/installationId
* `404`: Widget not found
* `422`: The snippet itself failed, threw, timed out, or returned something other than an array of options (UNIFIED_OPTIONS_FAILED). Carries the reason; a 5xx here would be replaced by the edge's own error page.
* `502`: The workflow sandbox never answered (UNIFIED_OPTIONS_FAILED)

## Embed

### Create a one-time Claude (MCP) connect URL

```http
POST /v1/embed/mcp-connect-codes
```

Returns mcp.&lt;zone>/fastn-workspace/c/&lt;mcpc_code>, which works once and for 10 minutes. Pasted into an MCP client, it connects that client to Fastn Workspace as the customer; redeeming it creates a Claude connection (listed by GET /api/v1/embed/share-links?kind=mcp, disconnected by DELETE /api/v1/embed/share-links/{id}). From an embed token the customer and user are the token's and the body is ignored; from a dashboard session (owner/admin/developer) orgId names one of the caller's own customers. Capability-scoped link tokens are refused.

Operation: `createMcpConnectCode`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `orgId` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `201`: Connect URL
* `400`: orgId missing (dashboard caller)
* `403`: Not a customer session, or role not allowed
* `404`: Customer is not the caller's
* `429`: EMBED_RATE_LIMITED
* `503`: EMBED_MCP_CONNECT_UNAVAILABLE: no MCP host configured

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.url` | `string` |  |
| `data.expiresAt` | `string` |  |

### List embed share links

```http
GET /v1/embed/share-links
```

The org's share links (newest 200), including revoked ones. kind=mcp lists Claude MCP connections instead of share links. Requires connectors.read.

Operation: `listEmbedShareLinks`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `orgId` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |
| `kind` | query | string | No | One of: `share`, `mcp`. |

**Responses**

* `200`: { data: [link] }

### Create an embed share link

```http
POST /v1/embed/share-links
```

Creates a durable, revocable link that opens one customer's embedded hub without a token in the URL; each load mints an end_user session for orgId. Optional metadata (partner only, at most 4KB) is handed back in the widget's installation lifecycle hooks for sessions opened from the link. Requires connectors.read.

Operation: `createEmbedShareLink`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `label` | `string` | No |  |
| `expiresInDays` | `integer` | No |  |
| `metadata` | `object` | No |  |
| `orgId` | `string` | Yes | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `201`: { data: { id, orgId, label, expiresAt, metadata? } }
* `400`: Validation error
* `403`: metadata sent by a caller that is not the customer's partner (code EMBED_PARTNER_ONLY_FIELD)

### Revoke an embed share link

```http
DELETE /v1/embed/share-links/{id}
```

Revokes a share link and ends every session it already minted. The row is kept for audit. 404 when the link is not the org's or is already revoked. Requires connectors.read.

Operation: `revokeEmbedShareLink`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: { id, revoked: true, sessionsKilled } }
* `404`: Not found or already revoked

### Generate scoped embed token

```http
POST /v1/embed/token
```

Issues a short-lived (8 hour) token scoped to a customer and end_user role. Requires connectors.read permission. Partner backends may send an EMPTY body together with the identity headers (x-org-id + x-user-id, proven with x-identity-hmac when the API key's identity-verification mode requires it), the customer and user then come from the headers. Without identity headers, orgId is required unless allowOrgLevel is true.

Operation: `createEmbedToken`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `x-org-id` | header | string | No | The customer the request acts for: the id you gave the customer when you created it (its external ref), or its fastn id. API-key calls only; the customer must belong to the key's account. When the key's identity-verification mode is not off, must be proven with x-identity-hmac. |
| `x-user-id` | header | string | No | End-user identifier the partner's backend authorized for this request. May accompany x-org-id or stand alone; covered by x-identity-hmac when the key enforces identity verification. |
| `x-identity-hmac` | header | string | No | Hex HMAC-SHA256 of "{x-org-id}\n{x-user-id}" (the header values exactly as sent, newline-joined; an absent header is the empty string) signed with the API key's identity-verification secret. Required when the key's idv mode is 'required' (missing/invalid = 401); logged-only under 'optional'; ignored when 'off'. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `allowOrgLevel` | `boolean` | No |  |
| `createIfMissing` | `boolean` | No |  |
| `customerName` | `string` | No |  |
| `userId` | `string` | No |  |
| `userEmail` | `string` | No |  |
| `userName` | `string` | No |  |
| `roleOverride` | `string` | No |  |
| `role` | `string` | No | One of: `end_user`. Default: `"end_user"`. |
| `metadata` | `object` | No |  |
| `orgId` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `200`: Embed token issued
* `400`: EMBED_TOKEN_REQUIRES_END_ORG_ID / IDENTITY_ORG_MISMATCH / IDENTITY_USER_MISMATCH
* `401`: Missing or invalid x-identity-hmac on a key whose identity-verification mode is required (IDENTITY_HMAC_INVALID)
* `403`: Customer does not belong to caller's account
* `404`: Customer not found

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.token` | `string` |  |
| `data.userId` | `string` |  |
| `data.role` | `string` |  |
| `data.tierId` | `string` |  |
| `data.expiresAt` | `string` |  |
| `data.expiresIn` | `integer` | Seconds until expiry |
| `data.orgId` | `string` | The customer this belongs to, under the id you gave it (its external ref); the account itself when it belongs to no customer. |

### Refresh an embed token (silent re-auth)

```http
POST /v1/embed/token/refresh
```

Rotates the session: the presented token is retired and a replacement issued with a fresh 8 hour TTL. Also accepts a token that expired less than 24 hours ago, so an idle embed session can silently re-establish; such a token still cannot authenticate any other request. Rotation cannot extend the session past its absolute lifetime (7 days from first issue), and the final token is clamped to that ceiling. Replaying an already-rotated token revokes the whole chain, but concurrent refreshes of the same token within a short race window are idempotent and all receive the same successor, so a parallel mount can never revoke a live session. Unauthenticated by design: the token in the body is the credential, and requiring a live one to reach this route would be circular.

Operation: `refreshEmbedToken`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `token` | `string` | Yes |  |

**Responses**

* `200`: New token issued
* `401`: Refused. `code` distinguishes why: EMBED_TOKEN_INVALID (unknown, or expired beyond the grace window), EMBED_SESSION_EXPIRED (past the absolute session lifetime, mint a new token), EMBED_TOKEN_REUSED (an already-rotated token was replayed; the whole chain is revoked), EMBED_SESSION_REVOKED (the chain was revoked by an earlier reuse).
* `403`: Token is not refreshable (scoped-link tokens have a hard expiry)
* `429`: Too many refreshes for this token (code EMBED_RATE_LIMITED). This route is public, so it is throttled here rather than by the gateway.

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.token` | `string` |  |
| `data.role` | `string` |  |
| `data.expiresAt` | `string` |  |
| `data.expiresIn` | `integer` |  |
| `data.orgId` | `string` | The customer this belongs to, under the id you gave it (its external ref); the account itself when it belongs to no customer. |

### Validate an embed token

```http
POST /v1/embed/token/validate
```

Resolves a token to its (non-secret) session context. Accepts a token inside the refresh grace window and reports it with expired:true and remainingMs:0, that grants strictly less than POST /embed/token/refresh would give the same caller, and stops a widget mounting with no identity at all. Validating never authenticates: every other path rejects an expired token outright.

Operation: `validateEmbedToken`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `token` | `string` | Yes |  |
| `orgId` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `200`: Token valid
* `400`: The orgId in the body names a different customer than the token carries (code EMBED_TENANT_MISMATCH). The error text names only the customer the caller asked for, never the one the token belongs to.
* `401`: Invalid or expired token

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.valid` | `boolean` |  |
| `data.orgId` | `string` | The customer this belongs to, under the id you gave it (its external ref); the account itself when it belongs to no customer. |
| `data.role` | `string` |  |
| `data.expiresAt` | `string` |  |
| `data.remainingMs` | `integer` | Remaining ACCESS in ms, never negative. 0 when the token resolved on the refresh grace alone. |
| `data.expired` | `boolean` | True when the token is past expiry and resolved only via the refresh grace: it carries identity but authenticates nothing, so the caller must refresh before using it. |
| `data.refreshable` | `boolean` | False for scoped-link tokens, whose expiry is hard. |
| `data.sessionExpiresAt` | `string` | Absolute end of the session; refresh cannot extend past this. |

## Setup links

### Create a setup link for widget installation

```http
POST /v1/setup-links
```

Generates a single-use URL where an customer customer can install a widget (connect accounts + configure) without logging in. Lifetime defaults to SETUP_LINK_DEFAULT_TTL_MINUTES (15) and can be set per link with expiresInMinutes up to SETUP_LINK_MAX_TTL_MINUTES (7 days). After the setup is completed the link token stays usable only SETUP_LINK_AFTER_COMPLETE_MINUTES (60) so the wizard can finish. The caller must be the partner org (passing orgId or externalRef) or the customer itself (omit both or set useCallerOrg: true). With externalRef + createIfMissing the customer is created on first use (needs customers.create). When the widget opts in to the onSetupLinkCompleted hook, completing the link fires it in background mode with source "setup_link" and the link metadata.

Operation: `createSetupLink`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `widgetId` | `string` | Yes |  |
| `useCallerOrg` | `boolean` | No |  |
| `label` | `string` | No |  |
| `connectionName` | `string` | Yes |  |
| `externalRef` | `string` | No |  |
| `createIfMissing` | `boolean` | No |  |
| `expiresInMinutes` | `integer` | No |  |
| `allowAdditionalConnection` | `boolean` | No |  |
| `metadata` | `object` | No |  |
| `redirectUrl` | `string` | No |  |
| `orgId` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `201`: Setup link created
* `400`: Invalid orgId, could not resolve partner org, or expiresInMinutes over the maximum (code SETUP_LINK_TTL_TOO_LONG)
* `404`: Widget not found, or no customer has externalRef (code TENANT_NOT_FOUND)
* `409`: createIfMissing could not create the customer (code TENANT_SLUG_TAKEN)
* `503`: No description.

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.setupId` | `string` | Setup link ID (stp_*) |
| `data.setupUrl` | `string` | URL to share with the customer |
| `data.status` | `string` | One of: `pending`. |
| `data.expiresAt` | `string` |  |
| `data.metadata` | `object` |  |
| `data.redirectUrl` | `string` |  |
| `data.allowAdditionalConnection` | `boolean` |  |
| `data.orgId` | `string` | The customer this belongs to, under the id you gave it (its external ref); the account itself when it belongs to no customer. |

### Get setup link status and context

```http
GET /v1/setup-links/{id}
```

Returns the current status of a setup link, plus widget details and config template for rendering the setup wizard.

Operation: `getSetupLink`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Setup link ID (stp_*) |

**Responses**

* `200`: Setup link details
* `404`: Setup link not found or expired
* `410`: Setup link was cancelled (code SETUP_LINK_REVOKED)
* `503`: No description.

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.setupId` | `string` |  |
| `data.status` | `string` | One of: `pending`, `complete`, `revoked`. |
| `data.widgetId` | `string` |  |
| `data.label` | `string` |  |
| `data.installationId` | `string` |  |
| `data.expiresAt` | `string` |  |
| `data.redirectUrl` | `string` |  |
| `data.metadata` | `object` | Only returned to the partner, never to the customer's link token. |
| `data.allowAdditionalConnection` | `boolean` | Present (true) when the link offers a new account per app. |
| `data.widget` | `object` |  |
| `data.widget.id` | `string` |  |
| `data.widget.name` | `string` |  |
| `data.widget.slug` | `string` |  |
| `data.widget.connectorRefs` | `object[]` |  |
| `data.widget.connectorIds` | `string[]` |  |
| `data.widget.unifiedRefs` | `object[]` |  |
| `data.configTemplate` | `object` |  |
| `data.configTemplate.id` | `string` |  |
| `data.configTemplate.config` | `object` |  |
| `data.orgId` | `string` | The customer this belongs to, under the id you gave it (its external ref); the account itself when it belongs to no customer. |

### Cancel a setup link

```http
DELETE /v1/setup-links/{id}
```

Cancels a setup link that has not been used yet and ends its link token at once. Only the partner org that created it can cancel it. Requires workflows.update.

Operation: `cancelSetupLink`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Setup link ID (stp_*) |

**Responses**

* `200`: Cancelled
* `404`: Setup link not found or expired
* `409`: Setup link was already used (code SETUP_LINK_COMPLETED)
* `503`: No description.

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.setupId` | `string` |  |
| `data.status` | `string` | One of: `revoked`. |

### Complete setup and create installation

```http
POST /v1/setup-links/{id}/complete
```

Marks the setup link as complete and creates (or reuses) a widget installation for the customer. The link is single-use and cannot be completed again. Must be called before the 15-minute expiry.

Operation: `completeSetupLink`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Setup link ID (stp_*) |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connections` | `object` | No |  |
| `config` | `object` | No |  |

**Responses**

* `200`: Already completed (idempotent)
* `201`: Installation created
* `404`: Setup link not found or expired
* `410`: Setup link has expired
* `503`: No description.

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.installationId` | `string` |  |
| `data.status` | `string` | One of: `complete`. |
| `data.reused` | `boolean` |  |

### Setup link status (public)

```http
GET /v1/setup-links/{id}/status
```

Whether a setup link can still be used, so the setup page can say why it does not open. Needs no session and returns no link data beyond its state and expiry.

Operation: `getSetupLinkStatus`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | stp_ id |

**Responses**

* `200`: { data: { status: pending \| complete \| revoked \| expired, expiresAt } }
* `404`: { error: not_found }
