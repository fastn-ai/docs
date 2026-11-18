---
description: "Push by Techulus sends push notifications to your iOS, Android, desktop and web devices from any script, webhook or automation."
hidden: true
---

# Push by Techulus

<img src="../../.gitbook/assets/connectors/push-by-techulus.png" alt="Push by Techulus logo" width="64">

Push by Techulus sends push notifications to your iOS, Android, desktop and web devices from any script, webhook or automation. This connector covers the full Push API: synchronous and asynchronous notifications to every device on an account or team, notifications to a specific device group, webhook-style notifications with the API key in the URL, and the beta Management API for inviting and removing team members.

| | |
| --- | --- |
| **Category** | [Communication](README.md) |
| **Website** | [push.techulus.com](https://push.techulus.com) |
| **Authentication** | API key |
| **Slug** | `pushByTechulus` |

## Use it

Add Push by Techulus from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pushByTechulus.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Invite Team Member | `inviteTeamMember` | Invites a user to one of your Push teams by email. Once the invitee accepts, every notification sent with that team's API key also reaches their devices. Requires the account API key, not a team API key. This endpoint is part of the beta Management API. |
| Remove Team Member | `removeTeamMember` | Removes a member from one of your Push teams, or revokes a pending invite, by email address. Their devices stop receiving notifications sent with that team's API key. Requires the account API key, not a team API key. This endpoint is part of the beta Management API. |
| Send Notification | `sendNotification` | Sends a push notification synchronously to every device on the connected account, or to every member's devices when a team API key is connected. The response reports delivery per device. Use Send Notification Async instead when more than 10 devices are targeted. |
| Send Notification Async | `sendNotificationAsync` | Queues a push notification for every device on the connected account, or for every member's devices when a team API key is connected, and returns as soon as it is accepted. Recommended over Send Notification whenever more than 10 devices are targeted, because delivery happens in the background. |
| Send Notification To Group | `sendNotificationToGroup` | Sends a push notification to every device in one device group on the connected account. Device groups are created in the Push console or mobile app; this request requires an account API key rather than a team API key. |
| Send Notification Via Get | `sendNotificationViaGet` | Sends a push notification with a single GET request, passing the notification fields as query parameters and the connected API key in the URL path. This is the variant Push recommends for webhook sources that can only issue a GET. |
| Send Notification Via Key Path | `sendNotificationViaKeyPath` | Sends a push notification using the API-key-in-URL variant of the Push API, where the connected API key is placed in the request path instead of a header. Behaves identically to Send Notification and exists for clients that cannot set custom headers. |
