---
description: "LiveSession is a product-analytics and session-replay platform."
hidden: true
---

# LiveSession

LiveSession is a product-analytics and session-replay platform. This connector covers the full LiveSession REST API: session search with visitor, device, geolocation and engagement detail; website management; alert rules and their notification providers; and webhook endpoint management, together with the session-event webhook surface.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [livesession.io](https://livesession.io) |
| **Authentication** | Credentials you enter |
| **Actions** | 10 |
| **Events** | 5 |
| **Slug** | `livesession` |

## Use it

Add LiveSession from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.livesession.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Alert | `createAlert` | Creates an alert rule that fires on the chosen session events and notifies either a Slack channel or a webhook endpoint. Supply Slack Channel ID when the provider is slack, or Webhook ID when it is webhooks. Requires the alerts:write scope. |
| Create Webhook | `createWebhook` | Registers a webhook endpoint for a website and returns its identifier. Registering the endpoint alone does not deliver anything: wire the returned Webhook ID to an alert with Create Alert to choose which session events are pushed to it. Requires the webhooks:write scope. |
| Delete Alert | `deleteAlert` | Permanently deletes an alert rule so it stops firing. Requires the alerts:write scope. |
| Delete Webhook | `deleteWebhook` | Permanently removes a webhook endpoint so LiveSession stops delivering to it. Requires the webhooks:write scope. |
| Get Sessions | `getSessions` | Lists recorded sessions with their visitor, device, geolocation, engagement and page-view detail, paginated. Filter by identified email, visitor identifier or a date window. Requires the users.sessions:read scope. |
| List Alerts | `listAlerts` | Lists every alert rule on the account, with the events that trigger it and where it sends notifications. Requires the alerts:read scope. |
| List Webhooks | `listWebhooks` | Lists the webhook endpoints registered on the account, with the website each belongs to and whether it is enabled. Requires the webhooks:read scope. |
| List Websites | `listWebsites` | Lists the websites tracked by the LiveSession account, with each site's identifier and hostname. Requires the websites:read scope. |
| Update Alert | `updateAlert` | Updates an existing alert rule. Only the fields you supply are sent, so omitted fields keep their current values. Requires the alerts:write scope. |
| Update Webhook | `updateWebhook` | Updates a registered webhook endpoint's URL, website or payload version. The API requires the version both as a query parameter and in the request body; the connector sends it in both places from the single Version input. Requires the webhooks:write scope. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Custom Event | `Custom` | Fires when a custom event your site tracks through the LiveSession browser SDK is captured, carrying the event name, value and occurrence count. Registering the endpoint alone delivers nothing: an alert must route this event kind to it, which the subscription code does from the Website ID and Event Kind inputs. Verify the base64 LiveSession-Signature header downstream. |
| Error Click | `ErrorClick` | Fires when a click produces a visible error during a session, carrying the error message shown. Registering the endpoint alone delivers nothing: an alert must route this event kind to it, which the subscription code does from the Website ID and Event Kind inputs. Verify the base64 LiveSession-Signature header downstream. |
| JavaScript Error | `JSError` | Fires when a JavaScript error is captured during a session. Delivery is two-step in LiveSession: a webhook endpoint is registered against one website, then an alert routes an event kind to that endpoint. The subscription code does both, so supply the Website ID and Event Kind inputs when subscribing. Signature verification is not configured here because LiveSession signs with a base64-encoded HMAC-SHA256 in the LiveSession-Signature header, which the fastn engine cannot express; verify it downstream with the endpoint's secret. |
| Network Error | `NetError` | Fires when a failed network request is captured during a session, carrying the method, URL and HTTP status that failed. Registering the endpoint alone delivers nothing: an alert must route this event kind to it, which the subscription code does from the Website ID and Event Kind inputs. Verify the base64 LiveSession-Signature header downstream. |
| Rage Click | `RageClick` | Fires when a visitor clicks repeatedly in frustration on the same element. Registering the endpoint alone delivers nothing: an alert must route this event kind to it, which the subscription code does from the Website ID and Event Kind inputs. Verify the base64 LiveSession-Signature header downstream. |
