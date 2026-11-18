---
description: "Manage Google Analytics 4 configuration through the Google Analytics Admin API v1beta: accounts, account summaries, properties, data streams, measurement…"
hidden: true
---

# Google Analytics Admin

<img src="../../.gitbook/assets/connectors/lg/google-analytics-admin.png" alt="Google Analytics Admin logo">

Manage Google Analytics 4 configuration through the Google Analytics Admin API v1beta: accounts, account summaries, properties, data streams, measurement protocol secrets, custom dimensions and metrics, key events, conversion events, Google Ads links, Firebase links, data retention and data sharing settings, change history search, and data access reporting.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [analyticsadmin.googleapis.com](https://analyticsadmin.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleAnalyticsAdmin` |

## Use it

Add Google Analytics Admin from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleAnalyticsAdmin.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Acknowledge User Data Collection for Property | `acknowledgeUserDataCollectionProperty` | Acknowledges the terms of user data collection for a property. This acknowledgement must be completed, either in the Google Analytics UI or through this action, before measurement protocol secrets can be created. |
| Archive Property Custom Dimension | `archivePropertyCustomDimension` | Archives a custom dimension on a property. Returns an empty object on success. |
| Archive Property Custom Metric | `archivePropertyCustomMetric` | Archives a custom metric on a property. Returns an empty object on success. |
| Ask Analytics Advisor | `chatWithProperty` | Asks a natural-language question about a GA4 property's data (e.g. "How many active users did we have last week?") through the Google Analytics Data API v1alpha properties.chat (Analytics Advisor) and returns the AI answer as text/table blocks. Read-only. Google scope: analytics.chatbot.read. Pre-release (v1alpha) Google AI feature; answers may be inaccurate and chat activity may be used by Google to improve the product. Pass the returned sessionId to ask follow-up questions. Returns sessionId, blocks[] and optional propertyQuota. |
| Create Access Binding | `createAccessBinding` | Grants a user roles on a Google Analytics account or GA4 property by creating an access binding via the Analytics Admin API v1alpha accessBindings.create. The user must have a Google account; Google may email them that access was granted. Google scope: analytics.manage.users. The caller needs administrator rights. Remove it with Delete Access Binding. Returns the created binding (name, user, roles). |
| Create Property | `createProperty` | Creates a Google Analytics 4 property with the specified attributes. Set Parent to the resource name of the owning account, for example accounts/123. |
| Create Property Conversion Event | `createPropertyConversionEvent` | Creates a conversion event on a property with the specified attributes. Deprecated by Google in favour of Create Property Key Event. |
| Create Property Custom Dimension | `createPropertyCustomDimension` | Creates a custom dimension on a property. Google warns that this method must not be used to collect data on individual users; sending user IDs in custom dimensions violates the Google Analytics Terms of Service. |
| Create Property Custom Metric | `createPropertyCustomMetric` | Creates a custom metric on a property. Restricted Metric Type is required when the measurement unit is CURRENCY. |
| Create Property Data Stream | `createPropertyDataStream` | Creates a data stream on a property. Populate Web Stream Data, Android App Stream Data or iOS App Stream Data to match the chosen stream Type. |
| Create Property Data Stream Measurement Protocol Secret | `createPropertyDataStreamMeasurementProtocolSecret` | Creates a measurement protocol secret on a data stream. The property must have acknowledged user data collection before secrets can be created. |
| Create Property Firebase Link | `createPropertyFirebaseLink` | Creates a Firebase link on a property, connecting it to a Firebase project. A property can have at most one Firebase link. |
| Create Property Google Ads Link | `createPropertyGoogleAdsLink` | Creates a Google Ads link on a property, connecting it to the given Google Ads customer account. |
| Create Property Key Event | `createPropertyKeyEvent` | Creates a key event on a property, marking the given event name as a key event with the chosen counting method. |
| Delete Access Binding | `deleteAccessBinding` | Revokes a user's access by deleting an access binding on a Google Analytics account or GA4 property via the Analytics Admin API v1alpha accessBindings.delete. Google scope: analytics.manage.users. Never target the connected owner's own binding. Returns an empty body on success. |
| Delete Account | `deleteAccount` | Marks the target Google Analytics account as soft-deleted (trashed). There is no API method to restore a soft-deleted account; use the Trash Can UI. If it is not restored before the expiration time, the account and all its child resources are permanently purged. |
| Delete Property | `deleteProperty` | Marks the target property as soft-deleted (trashed) and returns it. There is no API method to restore a soft-deleted property; use the Trash Can UI. If it is not restored before the expiration time, the property and all its child resources are permanently purged. |
| Delete Property Conversion Event | `deletePropertyConversionEvent` | Deletes a conversion event on a property. Deprecated by Google in favour of Delete Property Key Event. Returns an empty object on success. |
| Delete Property Data Stream | `deletePropertyDataStream` | Deletes a data stream on a property. Returns an empty object on success. |
| Delete Property Data Stream Measurement Protocol Secret | `deletePropertyDataStreamMeasurementProtocolSecret` | Deletes the target measurement protocol secret from a data stream. Returns an empty object on success. |
| Delete Property Firebase Link | `deletePropertyFirebaseLink` | Deletes a Firebase link on a property. Returns an empty object on success. |
| Delete Property Google Ads Link | `deletePropertyGoogleAdsLink` | Deletes a Google Ads link on a property. Returns an empty object on success. |
| Delete Property Key Event | `deletePropertyKeyEvent` | Deletes a key event on a property. Returns an empty object on success. |
| Get Access Binding | `getAccessBinding` | Gets one user access binding on a Google Analytics account or GA4 property via the Analytics Admin API v1alpha accessBindings.get. Read-only. Google scope: analytics.manage.users.readonly (or analytics.manage.users). Returns the binding's name, user email and roles[]. |
| Get Account | `getAccount` | Looks up a single Google Analytics account and returns its display name, region code and creation time. |
| Get Data Retention Settings for Property | `getDataRetentionSettingsProperty` | Returns the singleton data retention settings for a property, including the event-level and user-level retention durations. |
| Get Data Sharing Settings for Account | `getDataSharingSettingsAccount` | Gets the singleton data sharing settings on a Google Analytics account, showing which data sharing options are enabled. |
| Get Property | `getProperty` | Looks up a single Google Analytics 4 property and returns its display name, parent account, property type, industry category, currency, time zone and service level. |
| Get Property Conversion Event | `getPropertyConversionEvent` | Retrieves a single conversion event on a property. Deprecated by Google in favour of Get Property Key Event. |
| Get Property Custom Dimension | `getPropertyCustomDimension` | Looks up a single custom dimension on a property and returns its display name, parameter name and scope. |
| Get Property Custom Metric | `getPropertyCustomMetric` | Looks up a single custom metric on a property and returns its display name, parameter name, scope and measurement unit. |
| Get Property Data Stream | `getPropertyDataStream` | Looks up a single data stream on a property and returns its type, display name and stream-specific configuration. |
| Get Property Data Stream Measurement Protocol Secret | `getPropertyDataStreamMeasurementProtocolSecret` | Looks up a single measurement protocol secret on a data stream and returns its display name and secret value. |
| Get Property Key Event | `getPropertyKeyEvent` | Retrieves a single key event on a property, including its counting method and default value. |
| List Access Bindings | `listAccessBindings` | Lists the user access bindings (who has which role) on a Google Analytics account or GA4 property via the Analytics Admin API v1alpha accessBindings.list. Read-only and safe. Google scope: analytics.manage.users.readonly (or analytics.manage.users). The caller needs administrator rights on the account/property. Returns accessBindings[] (name, user, roles[]) and nextPageToken. |
| List Account Summaries | `listAccountSummary` | Returns summaries of all Google Analytics accounts accessible by the caller, each with the summaries of its child properties. This is the quickest way to discover every property you can reach. |
| List Accounts | `listAccount` | Returns all Google Analytics accounts accessible by the caller. Soft-deleted (trashed) accounts are excluded by default. To list every property you can reach, use List Account Summaries instead. |
| List Properties | `listProperty` | Returns child properties under the specified parent account. Properties the caller cannot access are excluded, and soft-deleted (trashed) properties are excluded by default. The Filter input is required by the API and must name a parent or ancestor, for example parent:accounts/123. |
| List Property Conversion Events | `listPropertyConversionEvent` | Returns the conversion events configured on a property, or an empty list if none exist. Deprecated by Google in favour of List Property Key Events. |
| List Property Custom Dimensions | `listPropertyCustomDimension` | Lists the custom dimensions configured on a property. |
| List Property Custom Metrics | `listPropertyCustomMetric` | Lists the custom metrics configured on a property. |
| List Property Data Stream Measurement Protocol Secrets | `listPropertyDataStreamMeasurementProtocolSecret` | Returns the measurement protocol secrets configured on a data stream. |
| List Property Data Streams | `listPropertyDataStream` | Lists the data streams configured on a property, covering web, Android app and iOS app streams. |
| List Property Firebase Links | `listPropertyFirebaseLink` | Lists the Firebase links on a property. A property can have at most one Firebase link. |
| List Property Google Ads Links | `listPropertyGoogleAdsLink` | Lists the Google Ads links configured on a property. |
| List Property Key Events | `listPropertyKeyEvent` | Returns the key events configured on a property, or an empty list if none exist. |
| Provision Account Ticket | `provisionAccountTicketAccount` | Requests a ticket for creating a Google Analytics account. The returned ticket id is passed in the Terms of Service acceptance link that the user must complete before the account exists. |
| Run Access Report for Account | `runAccessReportAccount` | Returns a customized report of data access records scoped to an account, showing each time a user read Google Analytics reporting data. Access records are retained for up to 2 years. |
| Run Access Report for Property | `runAccessReportProperty` | Returns a customized report of data access records for a property, showing each time a user read Google Analytics reporting data. Access records are retained for up to 2 years. Dimensions unrelated to quota can only be requested on Google Analytics 360 properties. |
| Search Change History Events for Account | `searchChangeHistoryEventsAccount` | Searches all changes made to an account or its child resources, filtered by time, actor, action type and resource type. Only returns the subset of changes supported by the API; the Analytics UI may show additional changes. |
| Update Account | `updateAccount` | Updates a Google Analytics account. Update Mask is required and must list the snake_case fields to change, for example display_name. |
| Update Data Retention Settings for Property | `updateDataRetentionSettingsProperty` | Updates the singleton data retention settings for a property. Update Mask is required and must list the snake_case field names to change, for example event_data_retention. |
| Update Property | `updateProperty` | Updates a Google Analytics 4 property. Update Mask is required and must list the snake_case field names to change, for example display_name,time_zone. |
| Update Property Conversion Event | `updatePropertyConversionEvent` | Updates a conversion event on a property. Deprecated by Google in favour of Update Property Key Event. Update Mask is required and must list the snake_case fields to change. |
| Update Property Custom Dimension | `updatePropertyCustomDimension` | Updates a custom dimension on a property. Update Mask is required and must list the fields to change; use '*' to replace the entire entity. |
| Update Property Custom Metric | `updatePropertyCustomMetric` | Updates a custom metric on a property. Update Mask is required and must list the fields to change; use '*' to replace the entire entity. |
| Update Property Data Stream | `updatePropertyDataStream` | Updates a data stream on a property. Update Mask is required and must list the fields to change; use '*' to replace the entire entity. |
| Update Property Data Stream Measurement Protocol Secret | `updatePropertyDataStreamMeasurementProtocolSecret` | Updates a measurement protocol secret on a data stream. Update Mask is required and must list the fields to change. |
| Update Property Google Ads Link | `updatePropertyGoogleAdsLink` | Updates a Google Ads link on a property. Update Mask is required and must list the snake_case field names to change, for example ads_personalization_enabled. |
| Update Property Key Event | `updatePropertyKeyEvent` | Updates a key event on a property. Update Mask is required and must list the snake_case fields to change. |
