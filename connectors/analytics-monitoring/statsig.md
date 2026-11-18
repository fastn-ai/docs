---
description: "Statsig is a feature flagging, experimentation and product analytics platform."
hidden: true
---

# Statsig

<img src="../../.gitbook/assets/connectors/statsig.png" alt="Statsig logo" width="64">

Statsig is a feature flagging, experimentation and product analytics platform. This connector wraps the Statsig HTTP API (SDK API): evaluate feature gates, dynamic configs, experiments and layers for a user, fetch the full evaluated configuration set for a user, rank contextual bandit variants, and log custom events and custom exposure events for analytics and metric calculation.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [statsig.com](https://statsig.com) |
| **Authentication** | API key |
| **Slug** | `statsig` |

## Use it

Add Statsig from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.statsig.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Feature Gates | `checkFeatureGates` | Evaluates one or more Statsig feature gates for a user and returns whether each gate passes, along with the rule and group that matched. Supply either a single gate name or an array of gate names, not both. With a single gate name the response is one flat result object; with an array it is an object keyed by gate name whose values have that same shape. Statsig automatically logs an exposure event for each evaluation unless exposure logging is disabled in the metadata. |
| Get Dynamic Config Or Experiment | `getDynamicConfigOrExperiment` | Fetches the configuration values a user receives from a dynamic config or an experiment. Statsig determines which of the two the name refers to automatically. An exposure event is logged automatically unless exposure logging is disabled in the metadata. |
| Get ID Lists | `getIdLists` | Returns the ID-list segments the project uses for targeting, each with the storage URL, size and creation time a client needs to download it. An empty object means the project defines no ID lists. |
| Get Layer Parameters | `getLayerParameters` | Fetches the parameter values a user receives from a Statsig layer. Layers let several experiments share a pool of parameters. An exposure event is logged automatically unless exposure logging is disabled in the metadata. A layer name that does not exist in the project returns 404. |
| Get Ranked List For Contextual Bandit | `getRankedListForContextualBandit` | Returns the variants of a Statsig contextual multi-armed bandit (Autotune AI) ranked by predicted performance for a given user context. A config name that is not a contextual bandit, or does not exist, returns 404. |
| Initialize User | `initializeUser` | Returns every feature gate, dynamic config, experiment and layer evaluated for a single user in one call, exactly as a Statsig client SDK receives them on start-up. Configuration names are hashed with the algorithm named in the hash_used field of the response. Use it to hydrate an application with a user's full Statsig state instead of evaluating each configuration separately. |
| Log Custom Events | `logCustomEvents` | Logs one or more custom events to Statsig for analytics and metric calculation. Each event can carry its own user, value, timestamp and metadata, or inherit a shared user supplied at the top level. Statsig accepts the batch asynchronously and answers 202. |
| Log Custom Exposure Events | `logCustomExposureEvents` | Manually logs exposure events for experiments, dynamic configs or feature gates. Use it for analytics-only experiments, for delayed exposure logging, or wherever automatic exposure logging has been disabled. Statsig accepts the batch asynchronously and answers 202. |
| Log Event Via Event Webhook | `logEventViaEventWebhook` | Logs a single event to Statsig through the incoming Event Webhook, the endpoint Statsig exposes for third-party apps and external sources that need to add context to experiments and metrics. It takes one event per call, unlike Log Custom Events which takes a batch. Requires a Server Secret Key. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Custom Event | `custom_event` | Sent for every custom event logged into the project, whatever its name. Statsig puts the customer's own event name in eventName, so this event id is a placeholder for the whole class rather than a literal value found in the payload - filter on eventName inside your workflow. That is also why this connector deliberately sets no event key: a fixed event key would silently drop every custom event whose name is not declared here, so all Statsig deliveries fan out to every bound trigger instead. Setup is manual, in the Statsig console: open Project Settings &gt; Integrations, enable the Generic Webhook integration, paste the fastn trigger URL, select Enable, then use Event Filtering to choose which events are forwarded. Statsig exposes no webhook-registration API, so fastn cannot subscribe on the customer's behalf. Deliveries arrive as a JSON array batch and Statsig does not sign them. This payload schema is modelled from the vendor's documented sample at https://docs.statsig.com/integrations/event_webhook, not from a captured delivery. |
| Dynamic Config Exposure | `statsig::config_exposure` | Sent when Statsig evaluates a dynamic config for a user. The metadata carries the config name, the rule that matched and the evaluation reason. Setup is manual, in the Statsig console: open Project Settings &gt; Integrations, enable the Generic Webhook integration, paste the fastn trigger URL, select Enable, then use Event Filtering to choose which events are forwarded. Statsig exposes no webhook-registration API, so fastn cannot subscribe on the customer's behalf. Deliveries arrive as a JSON array batch and Statsig does not sign them. This payload schema is modelled from the vendor's documented sample at https://docs.statsig.com/integrations/event_webhook, not from a captured delivery. |
| Experiment Exposure | `statsig::experiment_exposure` | Sent when Statsig assigns a user to an experiment group. The metadata carries the experiment name, the assigned group, the rule that matched and the evaluation reason. Setup is manual, in the Statsig console: open Project Settings &gt; Integrations, enable the Generic Webhook integration, paste the fastn trigger URL, select Enable, then use Event Filtering to choose which events are forwarded. Statsig exposes no webhook-registration API, so fastn cannot subscribe on the customer's behalf. Deliveries arrive as a JSON array batch and Statsig does not sign them. This payload schema is modelled from the vendor's documented sample at https://docs.statsig.com/integrations/event_webhook, not from a captured delivery. |
| Feature Gate Exposure | `statsig::gate_exposure` | Sent when Statsig evaluates a feature gate for a user. The metadata carries the gate name, the gate value, the rule that matched and the evaluation reason. Setup is manual, in the Statsig console: open Project Settings &gt; Integrations, enable the Generic Webhook integration, paste the fastn trigger URL, select Enable, then use Event Filtering to choose which events are forwarded. Statsig exposes no webhook-registration API, so fastn cannot subscribe on the customer's behalf. Deliveries arrive as a JSON array batch and Statsig does not sign them. This payload schema is modelled from the vendor's documented sample at https://docs.statsig.com/integrations/event_webhook, not from a captured delivery. |
