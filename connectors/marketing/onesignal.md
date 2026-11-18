---
description: "OneSignal customer engagement platform — send push notifications, emails, SMS, and Live Activities; manage users, subscriptions, aliases, segments, templates,…"
hidden: true
---

# OneSignal

OneSignal customer engagement platform — send push notifications, emails, SMS, and Live Activities; manage users, subscriptions, aliases, segments, templates, custom events, outcomes, apps, and API keys via the OneSignal REST API.

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Website** | [onesignal.com](https://onesignal.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 44 |
| **Events** | 0 |
| **Slug** | `onesignal` |

## Use it

Add OneSignal from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.onesignal.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Message | `cancelNotification` | Cancel a scheduled message that has not yet been delivered, by its notification ID. |
| Copy Template To App | `copyTemplateToApp` | Copy an existing template into another OneSignal app. |
| Create Alias | `createAlias` | Add or update identity aliases for a user identified by an existing alias label and value. |
| Create Alias By Subscription | `createAliasBySubscription` | Add or update identity aliases for the user that owns a given subscription ID. |
| Create API Key | `createApiKey` | Create a new REST API key (auth token) for the OneSignal app. Requires an Organization-level API key. |
| Create App | `createApp` | Create a new OneSignal app. Requires an Organization-level API key. |
| Create Custom Events | `createCustomEvents` | Send custom events for users to trigger OneSignal journeys and message automations. |
| Create Message | `createNotification` | Send a push notification, email, or SMS through OneSignal. Target by segments, aliases, subscription IDs, or filters, and compose content, buttons, media, and scheduling options. |
| Create Segment | `createSegment` | Create a segment in the OneSignal app using targeting filters. |
| Create Subscription | `createSubscription` | Create a new subscription (push, email, or SMS channel) for a user identified by an alias label and value. |
| Create Template | `createTemplate` | Create a reusable message template in the OneSignal app. |
| Create User | `createUser` | Create a user in the OneSignal app with identity aliases, custom properties, and subscriptions (push, email, or SMS). |
| Delete Alias | `deleteAlias` | Delete a specific identity alias from a user. |
| Delete API Key | `deleteApiKey` | Delete an API key (auth token) from the OneSignal app. Requires an Organization-level API key. |
| Delete Segment | `deleteSegment` | Delete a segment from the OneSignal app by its segment ID. |
| Delete Subscription | `deleteSubscription` | Delete a subscription by its subscription ID. |
| Delete Template | `deleteTemplate` | Delete a message template from the OneSignal app by its template ID. |
| Delete User | `deleteUser` | Delete a user (and their aliases) identified by an alias label and value. |
| Export Message Events CSV | `exportNotificationEvents` | Generate a CSV export of aggregated events (sent, delivered, clicked, etc.) for a specific message. |
| Export Subscriptions CSV | `exportSubscriptionsCsv` | Generate a compressed CSV export of all subscription (device) records for the app, with optional extra fields and segment filters. |
| List Apps | `getApps` | Retrieve all OneSignal apps in your organization. Returns an array of apps. Requires an Organization-level API key. |
| Rotate API Key | `rotateApiKey` | Rotate an existing API key, invalidating the old token and issuing a new one. Requires an Organization-level API key. |
| Start Live Activity | `startLiveActivity` | Start an iOS Live Activity for users, associating an activity ID with push-to-start tokens. |
| Transfer Subscription | `transferSubscription` | Transfer ownership of a subscription to another user identified by an alias in the identity object. |
| Unsubscribe Email With Token | `unsubscribeEmail` | Unsubscribe an email recipient using the unsubscribe token from a message, honoring one-click unsubscribe. |
| Update API Key | `updateApiKey` | Update the name, scopes, or IP allowlist of an existing API key. Requires an Organization-level API key. |
| Update App | `updateApp` | Update the configuration of an existing OneSignal app. Requires an Organization-level API key. |
| Update Live Activity | `updateLiveActivity` | Send an update or end event to an active iOS Live Activity by its activity ID. |
| Update Subscription | `updateSubscription` | Update the attributes of an existing subscription by its subscription ID. |
| Update Subscription By Token | `updateSubscriptionByToken` | Update a subscription identified by its channel token (e.g. email address or phone number) and token type. |
| Update Template | `updateTemplate` | Update an existing message template by its template ID. |
| Update User | `updateUser` | Update a user's properties, tags, or session deltas identified by an alias label and value. |
| View Aliases | `getAliases` | Retrieve all identity aliases for a user identified by an alias label and value. |
| View Aliases By Subscription | `getAliasesBySubscription` | Retrieve the identity aliases of the user that owns a given subscription ID. |
| View API Keys | `viewApiKeys` | Retrieve all REST API keys (auth tokens) for the OneSignal app. Requires an Organization-level API key. |
| View App | `getApp` | Retrieve the configuration and details of a single OneSignal app by its App ID. |
| View Message | `getNotification` | View the details and delivery stats of a single message by its notification ID. |
| View Message History | `getNotificationHistory` | Request the recipient-level history (sent or clicked events) for a message. Results are emailed as a CSV download link. |
| View Messages | `getNotifications` | View a list of messages (notifications) sent from your OneSignal app, with pagination. |
| View Outcomes | `getOutcomes` | Retrieve aggregated outcome data (e.g. custom conversions, purchases) for the app over a time range. |
| View Segments | `getSegments` | Retrieve all segments configured in the OneSignal app. |
| View Template | `viewTemplate` | Retrieve the details of a single template by its template ID. |
| View Templates | `viewTemplates` | Retrieve all message templates in the OneSignal app, with pagination. |
| View User | `getUser` | Retrieve a user by an alias label and value (e.g. external_id), including their identity, properties, and subscriptions. |
