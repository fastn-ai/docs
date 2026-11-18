---
description: "Memberspot is a German online course and membership platform."
hidden: true
---

# Memberspot

<img src="../../.gitbook/assets/connectors/memberspot.png" alt="Memberspot logo" width="64">

Memberspot is a German online course and membership platform. This connector covers the full Memberspot public API: member lookup and listing, granting and revoking offer access by email or user id, order state management, custom user properties, chapter access, course progress reporting, offers and exam results.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [memberspot.de](https://memberspot.de) |
| **Authentication** | API key |
| **Slug** | `memberspot` |

## Use it

Add Memberspot from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.memberspot.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Login Token | `createLoginToken` | Creates a single sign-on token for the given user with which that user can be signed in to Memberspot automatically. The token expires after one hour. |
| Delete Users By Email | `deleteUsersByEmail` | Permanently deletes one or more users from the school, identified by email address. This cannot be undone. Use Delete Users By Email (POST) instead if your HTTP client cannot send a body with DELETE. |
| Delete Users By Email (POST) | `deleteUsersByEmailPost` | Permanently deletes one or more users from the school by email address, using POST instead of DELETE for clients that cannot send a body with a DELETE request. This cannot be undone. |
| Delete Users By UID | `deleteUsersByUid` | Permanently deletes one or more users from the school, identified by Memberspot user id. This cannot be undone. Use Delete Users By UID (POST) instead if your HTTP client cannot send a body with DELETE. |
| Delete Users By UID (POST) | `deleteUsersByUidPost` | Permanently deletes one or more users from the school by Memberspot user id, using POST instead of DELETE for clients that cannot send a body with a DELETE request. This cannot be undone. |
| Find User By Email | `findUserByEmail` | Returns the user with the given email address, including course progress and custom properties, or null when no such user exists in the school. |
| Find User By UID | `findUserByUid` | Returns the user with the given Memberspot user id, including course progress and custom properties, or null when no such user exists in the school. |
| Get School | `getSchool` | Returns the Memberspot school that the configured API key belongs to, including its school id and name. Use this to verify credentials and to obtain the school id. |
| Get User Course Progress By Email | `getUserCourseProgressByEmail` | Returns the user's progress in one specific course, identified by email address and course id. |
| Get User Course Progress By UID | `getUserCourseProgressByUid` | Returns the user's progress in one specific course, identified by Memberspot user id and course id. |

<details>

<summary>See 20 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Grant Chapter Access By Email | `grantChapterAccessByEmail` | Grants a user access to a single chapter of a course, identified by email address. Use this to unlock individual lessons without granting a whole offer. |
| Grant Chapter Access By UID | `grantChapterAccessByUid` | Grants a user access to a single chapter of a course, identified by Memberspot user id. |
| Grant User Offer By Email | `grantUserOfferByEmail` | Grants a user access to an offer, identified by email address. If no user with that email exists in the school, Memberspot creates one using the supplied first and last name. |
| Grant User Offer By UID | `grantUserOfferByUid` | Grants an existing user access to an offer, identified by Memberspot user id. |
| List Custom User Properties | `listCustomUserProperties` | Lists every custom user property defined for the school. The returned property ids are required when setting custom property values on a user. |
| List Exam Results | `listExamResults` | Returns a paginated list of every user who has taken the given exam, with their individual runs, last run, last successful run and overall pass state. |
| List Offers | `listOffers` | Returns every offer available in the school, including the ids of the courses each offer unlocks. Offer ids are required by the grant-access and offer-state actions. |
| List User Course Progress By Email | `listUserCourseProgressByEmail` | Returns a paginated list of the user's progress across all courses, identified by email address. |
| List User Course Progress By UID | `listUserCourseProgressByUid` | Returns a paginated list of the user's progress across all courses, identified by Memberspot user id. |
| List Users | `listUsers` | Returns a paginated page of users in the school. Optionally filter by offer, by course, or by active state. Use the returned nextPage value as lastLoadedId to fetch the following page. |
| Set Custom User Properties By Email | `setCustomUserProperties` | Sets the values of several custom user properties at once for the user with the given email address. Property ids come from List Custom User Properties. |
| Set Custom User Properties By UID | `setCustomUserPropertiesByUid` | Sets the values of several custom user properties at once for the user with the given Memberspot user id. |
| Set Offer Expiry | `setOfferExpires` | Sets or clears the expiration date of a user's access to a specific offer. Omit Expires At to remove an existing expiry so the access no longer lapses. |
| Set Offer State By Email | `setOfferState` | Activates or deactivates a user's access to a specific offer, identified by email address. Set Active to false to revoke access without deleting the user. |
| Set Offer State By UID | `setOfferStateByUid` | Activates or deactivates a user's access to a specific offer, identified by Memberspot user id. |
| Set Order State By Email | `setOrderState` | Activates or deactivates every offer a user received under a specific order id, identified by email address. Use this to revoke access when an order is refunded or charged back. |
| Set Order State By Order ID | `setOrderStateByOrderId` | Activates or deactivates every offer carrying the given order id across all users in the school, without needing to know which user holds it. |
| Set Order State By UID | `setOrderStateByUid` | Activates or deactivates every offer a user received under a specific order id, identified by Memberspot user id. |
| Set Single Custom Property By Email | `setCustomProperty` | Sets one custom user property for the user with the given email address. When Value is omitted the property is set to an empty string. |
| Set Single Custom Property By UID | `setCustomPropertyByUid` | Sets one custom user property for the user with the given Memberspot user id. When Value is omitted the property is set to an empty string. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Course Completed | `course.completed` | Fires when a member finishes every lesson of a course. SETUP (required, per school): sign in to Memberspot as an admin, open Einstellungen (Settings) &gt; Integrationen &gt; Webhooks, choose Webhook erstellen, paste this trigger URL as the target, and select the course-completed event. Memberspot sends no event-type discriminator of its own, so add a literal payload field named 'event' with the value 'course.completed'. The payload must also carry 'schoolId'. Payload schema below is modelled from Memberspot's published event categories, not captured from a live delivery. |
| Course Progress Updated | `course.progress` | Fires when a member's learning progress in a course changes, such as completing a lesson or a chapter. SETUP (required, per school): sign in to Memberspot as an admin, open Einstellungen (Settings) &gt; Integrationen &gt; Webhooks, choose Webhook erstellen, paste this trigger URL as the target, and select the learning-progress event. Memberspot sends no event-type discriminator of its own, so add a literal payload field named 'event' with the value 'course.progress'. The payload must also carry 'schoolId'. Payload schema below is modelled from Memberspot's published event categories, not captured from a live delivery. |
| Exam Completed | `exam.completed` | Fires when a member submits an exam run, carrying whether the run was a pass. SETUP (required, per school): sign in to Memberspot as an admin, open Einstellungen (Settings) &gt; Integrationen &gt; Webhooks, choose Webhook erstellen, paste this trigger URL as the target, and select the exam event. Memberspot sends no event-type discriminator of its own, so add a literal payload field named 'event' with the value 'exam.completed'. The payload must also carry 'schoolId'. Payload schema below is modelled from Memberspot's published event categories, not captured from a live delivery. |
| Member Registered | `user.registered` | Fires when a new member completes registration in the school. SETUP (required, per school): sign in to Memberspot as an admin, open Einstellungen (Settings) &gt; Integrationen &gt; Webhooks, choose Webhook erstellen, paste this trigger URL as the target, and select the registration event. Memberspot sends no event-type discriminator of its own, so in the same dialog add a literal payload field named 'event' with the value 'user.registered' - without it this event cannot be routed and will be silently dropped. The payload must also carry 'schoolId' so the event can be matched to this connection. Payload schema below is modelled from Memberspot's published event categories, not captured from a live delivery. |
| Offer Access Granted | `offer.granted` | Fires when a member is granted access to an offer, typically after a purchase is confirmed by Stripe, Digistore24, CopeCart or Ablefy. SETUP (required, per school): sign in to Memberspot as an admin, open Einstellungen (Settings) &gt; Integrationen &gt; Webhooks, choose Webhook erstellen, paste this trigger URL as the target, and select the purchase or access-granted event. Memberspot sends no event-type discriminator of its own, so add a literal payload field named 'event' with the value 'offer.granted'. The payload must also carry 'schoolId'. Payload schema below is modelled from Memberspot's published event categories, not captured from a live delivery. |
| Offer Access Revoked | `offer.revoked` | Fires when a member's access to an offer is deactivated, for example on a refund or chargeback. SETUP (required, per school): sign in to Memberspot as an admin, open Einstellungen (Settings) &gt; Integrationen &gt; Webhooks, choose Webhook erstellen, paste this trigger URL as the target, and select the access-revoked event. Memberspot sends no event-type discriminator of its own, so add a literal payload field named 'event' with the value 'offer.revoked'. The payload must also carry 'schoolId'. Payload schema below is modelled from Memberspot's published event categories, not captured from a live delivery. |
