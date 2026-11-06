---
description: "What a widget callback workflow receives in ctx.input, what it can return, and when each callback fires."
---

# Widget callbacks

A callback runs one of your workflows when something happens to a customer's setup of a widget. You pick the workflows in [Edit integration](../embed/widget-builder/edit-integration.md#callbacks), or set `lifecycle_hooks` when you create or update a widget through the [REST API](rest/widgets.md).

```json
{
  "lifecycle_hooks": {
    "onActivation": { "workflowId": "wf_123", "mode": "blocking", "runForCustomer": true },
    "onConnectionCreated": { "workflowId": "wf_456", "mode": "background" }
  }
}
```

| Field | Type | Meaning |
| --- | --- | --- |
| `workflowId` | string | The workflow to run. Required. |
| `mode` | `blocking` or `background` | How it runs. `blocking` when left out. |
| `enabled` | boolean | Set `false` to silence the callback and keep the workflow selected. On when left out. |
| `runForCustomer` | boolean | Lets this callback run a workflow the customer has not installed. Off when left out. `onSetupLinkCompleted`, `onConnectionCreated` and `onConnectionDeleted` do not need it. |

Most callbacks run under the customer's org, whoever acted: the widget, a share link, the dashboard or an API key. The exception is updating or deleting a config through `/v1/configs`, which runs `onConfigurationChange` or `onConfigurationDelete` under the caller's org. A workflow you use only as a callback is not installed for the customer, so it needs `runForCustomer: true`. Without it the run is refused, and a blocking callback then stops the customer's action.

## What the workflow receives

The payload arrives as `ctx.input`. `event`, `endOrgId` and `widgetId` are always present. The other fields depend on the event.

| Field | Type | Sent on |
| --- | --- | --- |
| `event` | string | Every callback. The callback's name. |
| `endOrgId` | string | Every callback. The customer's fastn id. |
| `widgetId` | string | Every callback. |
| `externalRef` | string or null | Every callback. Your own id for the customer, or `null` if it has none. |
| `installationId` | string | Everything except `onConfigurationDelete`. `onConfigurationCreated` has it only when the config is pinned to an installation. |
| `connections` | object | Any callback with an `installationId`, when the installation has connections. Maps app slug to connection id. |
| `config` | object or null | `onActivation`, `onDeactivation`, `onSetupLinkCompleted`, `onConfigurationCreated` and `onConfigurationChange`. The configuration values in effect. |
| `previousConfig` | object or null | `onConfigurationChange` and `onConfigurationDelete`. The values before the change. On a first activation that supplies values, `onConfigurationChange` sends `{}`. |
| `metadata` | object | Only when there is some: what you passed to the [embed token](../embed/embedding/token-api.md) for `onActivation`, `onDeactivation` and `onConfigurationChange` from an embed session, or the setup link's metadata for `onSetupLinkCompleted` and `onConnectionCreated`. |
| `source` | string | `setup_link` on `onSetupLinkCompleted` and `onConnectionCreated`. |
| `connectionId`, `connectorSlug` | string | `onConnectionCreated` and `onConnectionDeleted`. The account added or removed, and its app. |
| `installationDeleted` | boolean | `true` on a background `onDeactivation` caused by deleting the installation. The installation no longer exists when the workflow runs, so do not read it back. |
| `templateTriggerId` | string | The trigger events. The widget's template trigger this instance came from. |
| `triggerData` | object | The trigger events. See [Trigger events](#trigger-events). |

The same customer and installation are also on the request as `x-end-org-id` and `x-installation-id`, so they are on `ctx.headers`. A background `onDeactivation` for a deleted installation has no `x-installation-id`.

### Example: `onActivation`

```json
{
  "event": "onActivation",
  "endOrgId": "org_acme",
  "widgetId": "wgt_abc123",
  "installationId": "ins_123",
  "config": { "syncDirection": "bidirectional" },
  "connections": { "hubspot": "conn_456" },
  "externalRef": "acme-001",
  "metadata": { "plan": "pro" }
}
```

### Example: `onConnectionCreated`

```json
{
  "event": "onConnectionCreated",
  "endOrgId": "org_acme",
  "widgetId": "wgt_abc123",
  "installationId": "ins_123",
  "connectionId": "conn_789",
  "connectorSlug": "googleCalendar",
  "source": "setup_link",
  "connections": { "googleCalendar": "conn_456" },
  "externalRef": "acme-001",
  "metadata": { "campaign": "second-calendar" }
}
```

`connections` is what the installation has pinned. The new account is `connectionId`, and it may not be in `connections`.

### Example: `onTriggerCreated`

```json
{
  "event": "onTriggerCreated",
  "endOrgId": "org_acme",
  "widgetId": "wgt_abc123",
  "installationId": "ins_123",
  "templateTriggerId": "trg_template",
  "triggerData": { "id": "trg_789", "name": "Nightly sync" },
  "connections": { "hubspot": "conn_456" },
  "externalRef": "acme-001"
}
```

## When each callback fires

| Callback | Fires when | Modes | Time limit when blocking |
| --- | --- | --- | --- |
| `onActivation` | An installation is created as active, or changes to active | Blocking or background | 5 seconds |
| `onDeactivation` | An active installation changes to inactive, or is deleted | Blocking or background | 5 seconds |
| `onConfigurationCreated` | A customer's config is created for this widget | Blocking or background | 2 seconds |
| `onConfigurationChange` | An installation's configuration changes, a config pinned to an installation is updated, or an active installation is created with values | Blocking or background | 2 seconds |
| `onConfigurationDelete` | A config for this widget is deleted by a caller acting for a customer. Deleting one with no customer in context runs no callback. | Blocking or background | 2 seconds |
| `onSetupLinkCompleted` | A setup link creates the customer's first setup of this widget | Background only | |
| `onConnectionCreated` | A later setup link adds another account, or signs a pinned account in again | Background only | |
| `onConnectionDeleted` | The customer removes an account an active setup uses | Background only | |
| `beforeTriggerCreated` | Before a trigger instance is created | Blocking or background | 5 seconds |
| `onTriggerCreated` | After a trigger instance is created | Blocking or background | 5 seconds |
| `beforeTriggerUpdated` | Before a trigger instance is updated | Blocking or background | 5 seconds |
| `onTriggerUpdated` | After a trigger instance is updated | Blocking or background | 2 seconds |
| `beforeTriggerDeleted` | Before a customer deletes a trigger instance | Blocking or background | 5 seconds |
| `onTriggerDeleted` | After a trigger instance is deleted | Blocking or background | 2 seconds |

Deleting an installation also deletes its triggers. That runs `onTriggerDeleted` for each one and never `beforeTriggerDeleted`.

## What the workflow can return

A blocking callback's return value decides what happens next.

| Field | Used by | Effect |
| --- | --- | --- |
| `accept` | Blocking `onActivation`, `onDeactivation`, the configuration events and the `before*` events | `false` stops the action. Left out, the action goes ahead. |
| `reason` | The same | The message returned to the caller when `accept` is `false`. |
| `modifiedConfig` | `onConfigurationCreated`, `onConfigurationChange` | Replaces the configuration that gets saved. On the first activation it is not applied. |
| `modifiedSettings` | `beforeTriggerCreated`, `beforeTriggerUpdated` | Replaces the trigger settings. Settings that do not validate are ignored. |

```json
{ "accept": false, "reason": "This plan does not include HubSpot." }
```

A refusal returns `422` to whoever asked, with `error` set to your `reason` and `hook` set to everything the workflow returned. `onActivation` refusing a new installation also removes the installation it had just created.

{% hint style="warning" %}
**A blocking callback fails closed.** If the workflow times out, cannot be reached, returns a non-2xx status or returns something other than JSON, fastn treats that as `accept: false` and the customer's action fails. Keep blocking callbacks fast, and use background for anything slow.
{% endhint %}

{% hint style="info" %}
**Use the Instant tier for a blocking callback.** Only an Instant workflow returns its value inline. A Standard or Long workflow answers `202` before it has run, so its return value never arrives and the action goes ahead.
{% endhint %}

`onTriggerCreated`, `onTriggerUpdated` and `onTriggerDeleted` run after the fact, so their return value is ignored in either mode.

A background callback's return value is always ignored. If fastn cannot deliver one within 10 seconds, it writes `widget.hook.delivery_failed` to the [audit log](../manage/audit-log.md), since the workflow never ran and left no execution of its own.

## Trigger events

`triggerData` differs by event.

| Event | `triggerData` |
| --- | --- |
| `beforeTriggerCreated` | `type`, `templateName`, `settings`, `defaultSettings` |
| `onTriggerCreated` | The created trigger, as the [triggers API](rest/triggers.md) returns it |
| `beforeTriggerUpdated` | `triggerId`, `type`, `settings`, `headers` |
| `onTriggerUpdated` | The updated trigger, as the triggers API returns it |
| `beforeTriggerDeleted`, `onTriggerDeleted` | The snapshot below |

The snapshot is taken before the delete, so you can clean up anything registered with a third party:

| Field | Meaning |
| --- | --- |
| `triggerId`, `type`, `name`, `status` | The trigger. `type` is `WEBHOOK`, `SCHEDULE` or `APP_EVENT`. |
| `cron`, `rate`, `timezone`, `startsAt` | Its schedule, for a schedule trigger. |
| `triggerUrl`, `webhookUrl` | Its public URL. For an app event trigger, `webhookUrl` is the URL registered with the third-party app. |
| `routes` | Its route bindings. |
| `connectorId`, `connectorName`, `events`, `accountId` | The app and events, for an app event trigger. |
| `additionalConfig`, `subscriptionResponse`, `subscriptionStatus` | Its extra settings and subscription state. |
| `reason` | On `onTriggerDeleted` only, when the delete came from something else: `installation_deleted` or `category_deselected`. |

If the trigger's record cannot be read, the snapshot is only `triggerId`, `type` and `webhookUrl: null`.
