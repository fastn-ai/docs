---
description: "GoSquared is a website analytics and customer engagement platform."
hidden: true
---

# GoSquared

<img src="../../.gitbook/assets/connectors/go-squared.png" alt="GoSquared logo" width="64">

GoSquared is a website analytics and customer engagement platform. This connector covers the GoSquared REST API: real-time Now analytics (concurrents, visitors, pages, sources, geo, engagement and time series), account administration (sites, usage, shared users, blocked visitors, bots and IPs, tagged visitors), webhooks and their triggers, and entry points to the People CRM, Chat, Forms, Ecommerce and Trends products.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [gosquared.com](https://gosquared.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `goSquared` |

## Use it

Add GoSquared from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.goSquared.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Chat Note | `addChatNote` | Leaves an internal note on a GoSquared Chat conversation that is visible to agents but not to the client. Requires an API key with the Write Chat scope. |
| Archive Chat | `archiveChat` | Archives a GoSquared Chat conversation so it no longer appears in the active inbox. Requires an API key with the Write Chat scope. |
| Block IP Address | `blockIpAddress` | Excludes an IP address from a GoSquared site's analytics so that traffic from it is no longer counted. |
| Block Visitor | `blockVisitor` | Excludes a single visitor from a GoSquared site's analytics so their future activity is not counted. |
| Create Site | `createSite` | Adds a new site to the GoSquared account and returns it with the tracking site token to install on that site. |
| Create Smart Group | `createSmartGroup` | Creates a new Smart Group in the GoSquared People CRM from a name and a set of filters on properties or events, for example {key:'property', path:'email', operator:'contains', value:'gosquared'}. Requires an API key with the Write People scope. |
| Create Webhook | `createWebhook` | Registers a webhook on a GoSquared site so GoSquared posts event payloads to the given URL, optionally attaching an initial trigger (for example traffic_spike with a visitor threshold) in the same call. Further triggers can be added with Create Webhook Trigger. Requires an API key with the Write Account scope. |
| Create Webhook Trigger | `createWebhookTrigger` | Adds a trigger to an existing GoSquared webhook so that the chosen event type (chat message, Smart Group entry or exit, traffic spike or dip) is delivered to the webhook URL. Requires an API key with the Write Account scope. |
| Delete Person | `deletePerson` | Permanently deletes a profile and all of its associated data from the GoSquared People CRM by person ID. Optionally blacklists the person's IDs and email so they are never re-created or sent to connected services. This action is irreversible and requires an API key with the Write People scope. |
| Delete Webhook | `deleteWebhook` | Removes a webhook from a GoSquared site, stopping all event delivery to its URL. |

<details>

<summary>See 88 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Webhook Trigger | `deleteWebhookTrigger` | Detaches a trigger from a GoSquared webhook so that its events are no longer delivered. |
| Export Smart Group Feed | `exportSmartGroupFeed` | Requests a CSV export of all pageview activity by the people in a Smart Group over a date range of up to 60 days, and returns a download link that stays valid for 15 minutes. Requires an API key with the Read People scope. |
| Get Blocked Bots Setting | `getBlockedBots` | Returns whether known bots and crawlers are currently excluded from a GoSquared site's analytics. |
| Get Blocked Overview | `getBlocked` | Returns everything currently excluded from a GoSquared site's analytics: the blocked bots, blocked IP addresses and individually blocked visitors. |
| Get Chat | `getChat` | Retrieves a single GoSquared Chat conversation by chat ID, which is the same as the person_id of the client. Requires an API key with the Read Chat scope. |
| Get Chat Feed | `getChatFeed` | Retrieves the combined feed of messages and events (such as archive or agent-join events) for a GoSquared Chat conversation, with optional date range and paging. Requires an API key with the Read Chat scope. |
| Get Chat Message | `getChatMessage` | Retrieves a specific message from a GoSquared Chat conversation by chat ID and message ID. Requires an API key with the Read Chat scope. |
| Get Concurrent Visitors | `getConcurrents` | Returns the live headline counters for a GoSquared site: how many people are online now, how many pages they are viewing, how many are returning visitors and how many are tagged. |
| Get Device | `getDevice` | Retrieves a single tracked device from the GoSquared People CRM by device ID, including platform, browser, user agent, screen size, ISP, location and total visits. Requires an API key with the Read People scope. |
| Get Now Engagement | `getNowEngagement` | Returns real-time engagement metrics for a GoSquared site, showing how actively the current visitors are reading, writing, idling or have the tab in the background. |
| Get Now Geography | `getNowGeo` | Returns the coordinates of the visitors currently on a GoSquared site, one entry per online visitor with latitude, longitude and landing time. |
| Get Now Overview | `getNowOverview` | Returns a combined real-time overview for a GoSquared site: the live visitor counters plus a summary of traffic over the recent reporting range. |
| Get Now Sources | `getNowSources` | Returns where the visitors currently on a GoSquared site came from, grouped into referrers, search engines, social networks and direct traffic. |
| Get Now Sources Section | `getNowSourcesSection` | Returns a single section of the real-time traffic sources for a GoSquared site, for example only the referrers or only the search engines. Pass several section names separated by commas to combine them. |
| Get Now Time | `getNowTime` | Returns the current server time and the reporting time zone GoSquared uses for the site, which is useful when aligning other real-time queries. |
| Get Now Time Series | `getNowTimeSeries` | Returns a time series of recent concurrent-visitor counts for a GoSquared site, suitable for plotting a live traffic chart. |
| Get Online Visitor | `getOnlineVisitor` | Returns the full real-time record for a single visitor currently on a GoSquared site, including their device, location, referrer and browsing activity. |
| Get Person | `getPerson` | Retrieves a single profile from the GoSquared People CRM by person ID, returning every property set on the profile. Requires an API key with the Read People scope. |
| Get Person Feed | `getPersonFeed` | Retrieves the tracked events and session events (pageviews, session starts and ends) for a person in reverse chronological order, with optional search, type and date filters. Requires an API key with the Read People scope. |
| Get Property Type | `getPropertyType` | Retrieves a single People CRM property type by its dot-notation name, for example 'email' or 'last.location.city'. Requires an API key with the Read People scope. |
| Get Site | `getSite` | Returns the settings for a single GoSquared site identified by its site token, including its name, domain, time zone and currency. |
| Get Sites Usage | `getSitesUsage` | Returns the tracked-usage figures for the GoSquared account's sites, showing how much of the plan allowance each site has consumed. |
| Get Smart Group | `getSmartGroup` | Retrieves a single Smart Group from the GoSquared People CRM by its group ID (usually the lower-case name shown in the People dashboard URL). Requires an API key with the Read People scope. |
| Get Token Info | `getTokenInfo` | Returns the scopes granted to the API key used by the connection, such as read_account or read_now, so you can check which GoSquared products the key can access. |
| Get Trends Aggregate | `getTrendsAggregate` | Returns aggregated historical analytics for a GoSquared site over a date range, such as page views, sessions and visitors. Requires an API key that carries the Trends scope; keys without it receive an authorisation error. |
| Get Trends Base Paths | `getTrendsBasePaths` | Retrieves historical metrics grouped by the first URL path segment (path1) for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trends Browsers | `getTrendsBrowsers` | Retrieves historical browser metrics for a GoSquared site over a date range, summarising visits by browser. Requires an API key with the Read Trends scope. |
| Get Trends Campaign Content | `getTrendsCampaignContent` | Retrieves historical UTM campaign content (utm_content) metrics for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trends Campaign Medium | `getTrendsCampaignMedium` | Retrieves historical UTM campaign medium (utm_medium) metrics for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trends Campaign Names | `getTrendsCampaignNames` | Retrieves historical UTM campaign name (utm_campaign) metrics for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trends Campaign Sources | `getTrendsCampaignSources` | Retrieves historical UTM campaign source (utm_source) metrics for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trends Campaign Terms | `getTrendsCampaignTerms` | Retrieves historical UTM campaign term (utm_term) metrics for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trends Countries | `getTrendsCountries` | Retrieves historical visitor metrics broken down by country for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trends Events | `getTrendsEvents` | Retrieves how many times each tracked event was triggered on a GoSquared site over a date range. Event data payloads are not included; use the person feed for those. Requires an API key with the Read Trends scope. |
| Get Trends Languages | `getTrendsLanguages` | Retrieves historical visitor metrics broken down by browser language for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trends Operating Systems | `getTrendsOperatingSystems` | Retrieves historical visitor metrics broken down by operating system for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trends Organisations | `getTrendsOrganisations` | Retrieves historical visitor metrics broken down by organisation (ISP or company network) for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trends Pages | `getTrendsPages` | Retrieves historical page metrics (visits and pageviews per page) for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trends Screen Dimensions | `getTrendsScreenDimensions` | Retrieves historical visitor metrics broken down by screen dimensions for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trends Sources | `getTrendsSources` | Retrieves the historical list of traffic sources that referred visitors to a GoSquared site, grouped into direct, organic, site and social, optionally restricted to one source type. Requires an API key with the Read Trends scope. |
| Get Trends Sources By Type | `getTrendsSourcesByType` | Retrieves the historical list of referring sources of one type (site, social, organic or internal) for a GoSquared site over a date range. Requires an API key with the Read Trends scope. |
| Get Trigger Type | `getTriggerType` | Returns the definition of a single GoSquared webhook trigger type, including the options it accepts when attaching it to a webhook. |
| Get Webhook | `getWebhook` | Returns a single webhook registered on a GoSquared site, including its delivery URL and the triggers attached to it. |
| Get Webhook Trigger | `getWebhookTrigger` | Returns a single trigger attached to a GoSquared webhook, including its type and the options that narrow when it fires. |
| Identify Person | `identifyPerson` | Identifies a visitor as a known person in GoSquared People CRM and sets their profile properties, linking their anonymous browsing history to the person. Sends the same body as Set Person Properties to the identify endpoint used by GoSquared's official tracking libraries (person_id, visitor_id, properties). |
| List Archived Chats | `listArchivedChats` | Lists archived GoSquared Chat conversations for the site, with optional date range and paging. Requires an API key with the Read Chat scope. |
| List Blocked IP Addresses | `listBlockedIps` | Lists the IP addresses excluded from a GoSquared site's analytics, typically used to filter out internal office traffic. |
| List Blocked Visitors | `listBlockedVisitors` | Lists the individual visitors excluded from a GoSquared site's analytics. |
| List Chat Messages | `listChatMessages` | Lists the messages in a GoSquared Chat conversation, with optional date range and paging. Requires an API key with the Read Chat scope. |
| List Chats | `listChats` | Lists active GoSquared Chat conversations for the site, with optional date range and paging. Requires an API key with the Read Chat scope. |
| List Custom Property Types | `listCustomPropertyTypes` | Lists only the custom property types that have been set on profiles in the GoSquared People CRM. Requires an API key with the Read People scope. |
| List Devices | `listDevices` | Lists every device ever tracked in the GoSquared People CRM for the site, paginated. Requires an API key with the Read People scope. |
| List Event Types | `listEventTypes` | Lists the event types that have been tracked in the GoSquared People CRM, ordered by how many times each has been tracked. Requires an API key with the Read People scope. |
| List Now Browsers | `listNowBrowsers` | Breaks down the visitors currently on a GoSquared site by web browser, with a count and share for each browser. |
| List Now Campaigns | `listNowCampaigns` | Lists the marketing campaigns that brought the visitors currently on a GoSquared site, with a count for each campaign. |
| List Now Countries | `listNowCountries` | Breaks down the visitors currently on a GoSquared site by country, with a count for each country. |
| List Now Languages | `listNowLanguages` | Breaks down the visitors currently on a GoSquared site by browser language. |
| List Now Notifications | `listNowNotifications` | Lists the real-time notifications raised for a GoSquared site, such as traffic spikes and milestones. |
| List Now Organisations | `listNowOrganisations` | Lists the organisations that visitors currently on a GoSquared site have been resolved to from their network, with a count for each one. |
| List Now Pages | `listNowPages` | Lists the pages currently being viewed on a GoSquared site, with the number of people on each one. |
| List Now Platforms | `listNowPlatforms` | Breaks down the visitors currently on a GoSquared site by operating system and platform. |
| List Online Visitors | `listOnlineVisitors` | Lists the visitors currently on a GoSquared site, with their location, device, referrer and the page each one is viewing. Supports paging and sorting. |
| List Person Devices | `listPersonDevices` | Lists the devices a specific person has used, newest first, from the GoSquared People CRM. Requires an API key with the Read People scope. |
| List Property Types | `listPropertyTypes` | Lists every property type that exists in the GoSquared People CRM, using dot notation for nested properties such as last.location.coordinates. Requires an API key with the Read People scope. |
| List Shared Users | `listSharedUsers` | Lists the users a GoSquared site has been shared with, together with the access level each one has. |
| List Sites | `listSites` | Lists the GoSquared sites the API key can access, split into sites the account owns and sites shared with it. Each site carries its site token, which other actions use to select a site. |
| List Smart Group People | `listSmartGroupPeople` | Lists the people who currently match a Smart Group in the GoSquared People CRM, with optional search, field selection, sorting and paging. Requires an API key with the Read People scope. |
| List Smart Groups | `listSmartGroups` | Lists all Smart Groups (saved filtered lists of people) in the GoSquared People CRM for the site, including the filters applied to each. Requires an API key with the Read People scope. |
| List Tagged Visitors | `listTaggedVisitors` | Lists the visitors that have been tagged on a GoSquared site so they stand out in the live visitor feed. |
| List Trigger Types | `listTriggerTypes` | Lists the kinds of event a GoSquared webhook trigger can listen for, together with the options each kind accepts. |
| List Webhook Triggers | `listWebhookTriggers` | Lists the triggers attached to a GoSquared webhook. Each trigger decides which kind of event causes GoSquared to post to the webhook URL. |
| List Webhooks | `listWebhooks` | Lists the webhooks registered on a GoSquared site, each with the URL GoSquared posts to and the triggers attached to it. |
| Remove Shared User | `removeSharedUser` | Revokes another user's access to a GoSquared site. |
| Search People | `listPeople` | Searches and filters profiles in the GoSquared People CRM using a free-text query, structured filters on properties or events, field selection, sorting and paging. Requires an API key with the Read People scope. |
| Send Chat Message | `sendChatMessage` | Sends a message into a GoSquared Chat conversation. Messages sent as an agent are attributed to the owner of the API key; sending as a client additionally requires the person's Secure Mode signature. Requires an API key with the Write Chat scope. |
| Send Tracking Ping | `sendTrackingPing` | Tells GoSquared that a visitor is still active, keeping them counted as online in the real-time Now reports. |
| Set Blocked Bots | `setBlockedBots` | Turns bot and crawler filtering on or off for a GoSquared site, controlling whether automated traffic is counted in analytics. |
| Set Person Properties | `setPersonProperties` | Sets profile properties on a person or anonymous visitor in GoSquared People CRM. Supply person_id or visitor_id to say who the properties belong to. |
| Share Site With User | `shareSiteWithUser` | Grants another user access to a GoSquared site at the chosen permission level. GoSquared emails the person an invitation, so use a colleague's real address only when you intend to invite them. |
| Tag Visitor | `tagVisitor` | Tags a visitor on a GoSquared site with a label so they are highlighted whenever they return. |
| Time Out Visitor | `timeOutVisitor` | Tells GoSquared that a visitor has left, removing them immediately from the real-time online visitor count. |
| Track Event | `trackEvent` | Records a custom event against a person or anonymous visitor in GoSquared, such as a signup or a feature being used. The event then appears in that person's activity feed and can drive smart groups and automations. |
| Track Page View | `trackPageView` | Records a page view in GoSquared from the server side, for pages where the JavaScript tracker cannot run. |
| Track Transaction | `trackTransaction` | Records an ecommerce transaction in GoSquared, with its line items, so it appears in revenue reporting and against the buyer's profile. |
| Unarchive Chat | `unarchiveChat` | Restores an archived GoSquared Chat conversation to the active inbox. Requires an API key with the Write Chat scope. |
| Unblock IP Address | `unblockIpAddress` | Removes an IP address from a GoSquared site's block list so that its traffic is counted in analytics again. |
| Unblock Visitor | `unblockVisitor` | Removes a visitor from a GoSquared site's block list so their activity is counted in analytics again. |
| Untag Visitor | `untagVisitor` | Removes the tag from a visitor on a GoSquared site so they are no longer highlighted in the live visitor feed. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Chat Message Received | `chat_message` | Fires when a message is posted in a GoSquared Chat conversation. Payload: the message and the person who sent it. Sample taken from GoSquared's own GET /account/v1/triggerTypes example. |
| Person Entered Smart Group | `entered_smart_group` | Fires when a People CRM profile enters the Smart Group whose ID is given as the trigger value when subscribing. Payload: group, boundary 'enter' and the full person profile. Sample taken from GoSquared's own GET /account/v1/triggerTypes example. |
| Person Exited Smart Group | `exited_smart_group` | Fires when a People CRM profile leaves the Smart Group whose ID is given as the trigger value when subscribing. Payload: group, boundary 'exit' and the full person profile. Sample taken from GoSquared's own GET /account/v1/triggerTypes example. |
| Traffic Dip | `traffic_dip` | Fires when the number of concurrent visitors falls below the threshold given as the trigger value when subscribing. Payload: the alert that fired (triggeredAlert), site details and a snapshot of real-time analytics. Sample taken from GoSquared's own GET /account/v1/triggerTypes example. |
| Traffic Spike | `traffic_spike` | Fires when the number of concurrent visitors rises above the threshold given as the trigger value when subscribing. Payload: the alert that fired (triggeredAlert), site details and a snapshot of real-time analytics. Sample taken from GoSquared's own GET /account/v1/triggerTypes example. |
