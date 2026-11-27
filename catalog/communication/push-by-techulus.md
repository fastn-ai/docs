---
description: "Push by Techulus sends push notifications to your devices. Send notifications to devices or groups, and invite or remove team members."
hidden: true
---

# Push by Techulus

<img src="../../.gitbook/assets/connectors/lg/push-by-techulus.png" alt="Push by Techulus logo">

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [push.techulus.com](https://push.techulus.com) |
| **Authentication** | API key |
| **Slug** | `pushByTechulus` |

## Setup

Your customers enter their API key for Push by Techulus when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Push by Techulus from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Push by Techulus**.
2. Select **Connect** on the Push by Techulus card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Push by Techulus's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Invite Team Member</td><td><code>inviteTeamMember</code></td><td>Invites a user to one of your Push teams by email. Once the invitee accepts, every notification sent with that team's API key also reaches their devices. Requires the account API key, not a team API key. This endpoint is part of the beta Management API.</td></tr><tr><td>Remove Team Member</td><td><code>removeTeamMember</code></td><td>Removes a member from one of your Push teams, or revokes a pending invite, by email address. Their devices stop receiving notifications sent with that team's API key. Requires the account API key, not a team API key. This endpoint is part of the beta Management API.</td></tr><tr><td>Send Notification</td><td><code>sendNotification</code></td><td>Sends a push notification synchronously to every device on the connected account, or to every member's devices when a team API key is connected. The response reports delivery per device. Use Send Notification Async instead when more than 10 devices are targeted.</td></tr><tr><td>Send Notification Async</td><td><code>sendNotificationAsync</code></td><td>Queues a push notification for every device on the connected account, or for every member's devices when a team API key is connected, and returns as soon as it is accepted. Recommended over Send Notification whenever more than 10 devices are targeted, because delivery happens in the background.</td></tr><tr><td>Send Notification To Group</td><td><code>sendNotificationToGroup</code></td><td>Sends a push notification to every device in one device group on the connected account. Device groups are created in the Push console or mobile app; this request requires an account API key rather than a team API key.</td></tr><tr><td>Send Notification Via Get</td><td><code>sendNotificationViaGet</code></td><td>Sends a push notification with a single GET request, passing the notification fields as query parameters and the connected API key in the URL path. This is the variant Push recommends for webhook sources that can only issue a GET.</td></tr><tr><td>Send Notification Via Key Path</td><td><code>sendNotificationViaKeyPath</code></td><td>Sends a push notification using the API-key-in-URL variant of the Push API, where the connected API key is placed in the request path instead of a header. Behaves identically to Send Notification and exists for clients that cannot set custom headers.</td></tr></tbody></table>

