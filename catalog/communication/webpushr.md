---
description: "Webpushr sends web push notifications. Send pushes to all subscribers, segments or single subscribers, and read subscriber counts and analytics."
hidden: true
---

# Webpushr

<img src="../../.gitbook/assets/connectors/lg/webpushr.png" alt="Webpushr logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [webpushr.com](https://webpushr.com) |
| **Authentication** | API key |
| **Slug** | `webpushr` |

## Setup

Your customers enter their API key for Webpushr when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Webpushr from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Webpushr**.
2. Select **Connect** on the Webpushr card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Webpushr's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Authenticate API Credentials</td><td><code>authenticate</code></td><td>Validates the stored Webpushr REST API Key and Auth Token against the Webpushr API. Returns status 'success' with the description 'You are authorized' when the credentials are valid. Use it to verify a connection before sending notifications.</td></tr><tr><td>Get Dashboard Analytics</td><td><code>getDashboardAnalytics</code></td><td>Returns the Webpushr dashboard analytics for the site: a 31-day subscriber growth series, total and active subscriber counts, and the opt-in rate. The browsers, devices, os and subscribers_logs fields are returned by Webpushr as pre-rendered HTML fragments rather than structured data. This endpoint is not in the published Webpushr REST API reference but is live on api.webpushr.com.</td></tr><tr><td>Get Push Notification Status</td><td><code>getPushNotificationStatus</code></td><td>Returns the delivery report for a single Webpushr campaign: its status plus attempt, send, failure, delivery, click and close counts. Pass the campaign ID returned by any of the Send Push actions.</td></tr><tr><td>Get Subscriber Count</td><td><code>getSubscriberCount</code></td><td>Returns the lifetime and currently active web push subscriber counts for the site the API key belongs to. Useful as a safety check before sending a broadcast campaign.</td></tr><tr><td>List Segments</td><td><code>listSegments</code></td><td>Lists every subscriber segment defined for the site, each with its ID, title, type and current subscriber total, plus the site-wide active subscriber count. Use the returned segment IDs with Send Push To Segments. This endpoint is not in the published Webpushr REST API reference but is live on api.webpushr.com.</td></tr><tr><td>Send Push To All Subscribers</td><td><code>sendPushToAllSubscribers</code></td><td>Creates a web push campaign that is delivered to every active subscriber of the site. Returns the created campaign ID, which can be passed to Get Push Notification Status. Set send_at to schedule the campaign for a future UTC time instead of sending immediately.</td></tr><tr><td>Send Push To Custom Attribute</td><td><code>sendPushToCustomAttribute</code></td><td>Creates a web push campaign delivered to subscribers tagged with the given custom attribute key/value pairs, for example an email attribute. When several pairs are supplied, subscribers matching any one of them receive the notification (OR logic). Returns the created campaign ID.</td></tr><tr><td>Send Push To Segments</td><td><code>sendPushToSegments</code></td><td>Creates a web push campaign delivered only to subscribers in one or more Webpushr segments. Segment IDs come from List Segments. Returns the created campaign ID for use with Get Push Notification Status.</td></tr><tr><td>Send Push To Subscriber ID</td><td><code>sendPushToSubscriberId</code></td><td>Sends a web push notification to one specific Webpushr subscriber, identified by its numeric subscriber ID (sid). The sid is obtained from the Webpushr console or the webpushr JavaScript fetch-id method. This endpoint does not support the large hero image parameter.</td></tr></tbody></table>

