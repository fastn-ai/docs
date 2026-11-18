---
description: "Adafruit IO is a cloud platform for Internet of Things projects."
hidden: true
---

# Adafruit IO

Adafruit IO is a cloud platform for Internet of Things projects. This connector covers the Adafruit IO HTTP API v2: feeds and feed data, groups, dashboards and blocks, reactive and scheduled actions (triggers), permissions, API tokens, activities, feed webhook receivers, and the time, randomizer, weather and air quality services.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [io.adafruit.com](https://io.adafruit.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 71 |
| **Events** | 0 |
| **Slug** | `adafruitIo` |

## Use it

Add Adafruit IO from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.adafruitIo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Feed To Group | `addFeedToGroup` | Add an existing Feed to a Group. |
| All activities for current user | `deleteActivities` | All activities for current user. Delete all your activities. |
| All activities for current user | `listActivities` | All activities for current user. The Activities endpoint returns information about the user's activities. |
| All blocks for current user | `listBlocks` | All blocks for current user. The Blocks endpoint returns information about the user's blocks. |
| All dashboards for current user | `listDashboards` | All dashboards for current user. The Dashboards endpoint returns information about the user's dashboards. |
| All permissions for current user and type | `listPermissions` | All permissions for current user and type. The Permissions endpoint returns information about the user's permissions. |
| All tokens for current user | `listTokens` | All tokens for current user. The Tokens endpoint returns information about the user's tokens. |
| All triggers for current user | `listTriggers` | All triggers for current user. The Triggers endpoint returns information about the user's triggers. |
| Create a new Block | `createBlock` | Create a new Block. |
| Create a new Dashboard | `createDashboard` | Create a new Dashboard. |
| Create a new Permission | `createPermission` | Create a new Permission. |
| Create a new Token | `createToken` | WARNING: creating a token generates a NEW master Adafruit IO Key and the previous key stops working immediately (verified live 2026-10-20: every call with the old key then returned 401 'invalid API key provided'). Update your fastn connection with the new key returned in the response. Create a new Token. |
| Create a new Trigger | `createTrigger` | Create a new Trigger. |
| Create Feed | `createFeed` | Create a new Feed. |
| Create Feed Data | `createFeedData` | Create new Data. Create new data records on the given feed. **NOTE:** when feed history is on, data `value` size is limited to 1KB, when feed history is turned off data value size is limited to 100KB. |
| Create Feed Data Batch | `createFeedDataBatch` | Adds multiple data points to an Adafruit IO feed in a single request. Each record needs a value and may include a location and timestamp. |
| Create Feed In Group | `createFeedInGroup` | Create a new Feed in a Group. |
| Create Group | `createGroup` | Create a new Group. |
| Create Group Data | `createGroupData` | Create new data for multiple feeds in a group. |
| Create Group Feed Data | `createGroupFeedData` | Create new Data in a feed belonging to a particular group. |
| Create Group Feed Data Batch | `createGroupFeedDataBatch` | Adds multiple data points to a feed that belongs to a specific Adafruit IO group in a single request. |
| Delete an existing Block | `deleteBlock` | Delete an existing Block. |
| Delete an existing Dashboard | `deleteDashboard` | Delete an existing Dashboard. |
| Delete an existing Permission | `deletePermission` | Delete an existing Permission. |
| Delete an existing Token | `deleteToken` | Delete an existing Token. |
| Delete an existing Trigger | `deleteTrigger` | Delete an existing Trigger. |
| Delete Data Point | `deleteDataPoint` | Delete existing Data. |
| Delete Feed | `deleteFeed` | Delete an existing Feed. |
| Delete Group | `deleteGroup` | Delete an existing Group. |
| Get activities by type for current user | `listActivitiesByType` | Get activities by type for current user. The Activities endpoint returns information about the user's activities. |
| Get Current User | `getCurrentUser` | Get information about the current user. |
| Get Data Point | `getDataPoint` | Returns data based on feed key. |
| Get Feed | `getFeed` | Get feed by feed key. Returns feed based on the feed key |
| Get Feed Chart Data | `getFeedChartData` | Chart data for current feed. The Chart API is what we use on io.adafruit.com to populate charts over varying timespans with a consistent number of data points. The maximum number of points returned is 480. This API works by aggregating slices of time into a single value by averaging. All time-based parameters are optional, if none are given it will default to 1 hour at the finest-grained resolution possible. |
| Get Feed Details | `getFeedDetails` | Get detailed feed by feed key. Returns more detailed feed record based on the feed key |
| Get First Data | `getFirstData` | First Data in Queue. Get the oldest data point in the feed. This request sets the queue pointer to the beginning of the feed. |
| Get Group | `getGroup` | Returns Group based on ID. |
| Get Last Data | `getLastData` | Last Data in Queue. Get the most recent data point in the feed. This request sets the queue pointer to the end of the feed. |
| Get Most Recent Data | `getMostRecentData` | Last Data in MQTT CSV format. Get the most recent data point in the feed in an MQTT compatible CSV format: `value,lat,lon,ele` |
| Get Next Data | `getNextData` | Next Data in Queue. Get the next newest data point in the feed. If queue processing hasn't been started, the first data point in the feed will be returned. |
| Get Previous Data | `getPreviousData` | Previous Data in Queue. Get the previously processed data point in the feed. NOTE: this method doesn't move the processing queue pointer. |
| Get Rate Limit Status | `getRateLimitStatus` | Get the user's data rate limit and current activity level.. |
| List Feed Data | `listFeedData` | Get all data for the given feed. |
| List Feeds | `listFeeds` | All feeds for current user. The Feeds endpoint returns information about the user's feeds. The response includes the latest value of each feed, and other metadata about each feed. |
| List Group Feed Data | `listGroupFeedData` | All data for current feed in a specific group. |
| List Group Feeds | `listGroupFeeds` | All feeds for current user in a given group. The Group Feeds endpoint returns information about the user's feeds. The response includes the latest value of each feed, and other metadata about each feed, but only for feeds within the given group. |
| List Groups | `listGroups` | All groups for current user. The Groups endpoint returns information about the user's groups. The response includes the latest value of each feed in the group, and other metadata about the group. |
| Remove Feed From Group | `removeFeedFromGroup` | Remove a Feed from a Group. |
| Replace an existing Block | `replaceBlock` | Replace an existing Block. |
| Replace an existing Dashboard | `replaceDashboard` | Replace an existing Dashboard. |
| Replace an existing Permission | `replacePermission` | Replace an existing Permission. |
| Replace an existing Token | `replaceToken` | Replace an existing Token. |
| Replace an existing Trigger | `replaceTrigger` | Replace an existing Trigger. |
| Replace Data Point | `replaceDataPoint` | Replace existing Data. |
| Replace Feed | `replaceFeed` | Replace an existing Feed. |
| Replace Group | `replaceGroup` | Replace an existing Group. |
| Returns Block based on ID | `getBlock` | Returns Block based on ID. |
| Returns Dashboard based on ID | `getDashboard` | Returns Dashboard based on ID. |
| Returns Permission based on ID | `getPermission` | Returns Permission based on ID. |
| Returns Token based on ID | `getToken` | Returns Token based on ID. |
| Returns Trigger based on ID | `getTrigger` | Returns Trigger based on ID. |
| Send arbitrary data to a feed via webhook URL. | `createRawWebhookFeedData` | Send arbitrary data to a feed via webhook URL.. The raw data webhook receiver accepts POST requests and stores the raw request body on your feed. This is useful when you don't have control of the webhook sender. If feed history is turned on, payloads will be truncated at 1024 bytes. If feed history is turned off, payloads will be truncated at 100KB. Pass any JSON fields next to token; they become the body. |
| Send data to a feed via webhook URL. | `createWebhookFeedData` | Send data to a feed via webhook URL.. |
| Update Data Point | `updateDataPoint` | Update properties of existing Data. |
| Update Feed | `updateFeed` | Update properties of an existing Feed. |
| Update Group | `updateGroup` | Update properties of an existing Group. |
| Update properties of an existing Block | `updateBlock` | Update properties of an existing Block. |
| Update properties of an existing Dashboard | `updateDashboard` | Update properties of an existing Dashboard. |
| Update properties of an existing Permission | `updatePermission` | Update properties of an existing Permission. |
| Update properties of an existing Token | `updateToken` | Update properties of an existing Token. |
| Update properties of an existing Trigger | `updateTrigger` | Update properties of an existing Trigger. |
