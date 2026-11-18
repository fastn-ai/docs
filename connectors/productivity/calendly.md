---
description: "Calendly v2 REST API — users, event types, scheduled events, invitees, organization memberships/invitations, scheduling links, availability (schedules/busy…"
hidden: true
---

# Calendly

<img src="../../.gitbook/assets/connectors/calendly.jpg" alt="Calendly logo" width="64">

Calendly v2 REST API — users, event types, scheduled events, invitees, organization memberships/invitations, scheduling links, availability (schedules/busy times/available times), routing forms, groups, invitee no-shows, data compliance, activity log, and webhook subscriptions. Base https://api.calendly.com. Auth: Bearer personal access token or OAuth 2.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [calendly.com](https://calendly.com) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Slug** | `calendly` |

## Use it

Add Calendly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.calendly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Scheduled Event | `cancelScheduledEvent` | Cancel a scheduled event (POST /scheduled_events/{uuid}/cancellation). |
| Create Event Invitee | `createEventInvitee` | Books a meeting on a Calendly event type for an invitee, the same as the invitee booking through the Calendly page. start_time must be an open slot from List Event Type Available Times. Calendly sends its usual confirmation emails and adds the event to the host's calendar. Returns the invitee with the scheduled event URI, cancel URL and reschedule URL. Calendly allows this only on paid plans (Standard and above). |
| Create Invitee No Show | `createInviteeNoShow` | Mark an invitee as a no-show (POST /invitee_no_shows). |
| Create Organization Invitation | `createOrganizationInvitation` | Invite a user to an organization (POST /organizations/{org_uuid}/invitations). |
| Create Scheduling Link | `createSchedulingLink` | Create a single-use scheduling link for an event type (POST /scheduling_links). |
| Create Webhook Subscription | `createWebhookSubscription` | Create a webhook subscription (POST /webhook_subscriptions). Used by the webhook config subscription code. |
| Delete Invitee Data | `deleteInviteeData` | Request deletion of invitee PII for compliance (POST /data_compliance/deletion/invitees). Returns 202. |
| Delete Invitee No Show | `deleteInviteeNoShow` | Undo an invitee no-show (DELETE /invitee_no_shows/{uuid}). Returns 204. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | Delete a webhook subscription (DELETE /webhook_subscriptions/{uuid}). Returns 204. |
| Get Current User | `getCurrentUser` | Get the current authenticated user (GET /users/me). |

<details>

<summary>See 26 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Event Invitee | `getEventInvitee` | Get a single invitee of a scheduled event (GET /scheduled_events/{event_uuid}/invitees/{invitee_uuid}). |
| Get Event Type | `getEventType` | Get an event type by UUID (GET /event_types/{uuid}). |
| Get Invitee No Show | `getInviteeNoShow` | Get an invitee no-show by UUID (GET /invitee_no_shows/{uuid}). |
| Get Organization Invitation | `getOrganizationInvitation` | Get an organization invitation (GET /organizations/{org_uuid}/invitations/{uuid}). |
| Get Organization Membership | `getOrganizationMembership` | Get an organization membership by UUID (GET /organization_memberships/{uuid}). |
| Get Routing Form | `getRoutingForm` | Get a routing form by UUID (GET /routing_forms/{uuid}). |
| Get Routing Form Submission | `getRoutingFormSubmission` | Get a routing form submission by UUID (GET /routing_form_submissions/{uuid}). |
| Get Scheduled Event | `getScheduledEvent` | Get a scheduled event by UUID (GET /scheduled_events/{uuid}). |
| Get User | `getUser` | Get a user by UUID (GET /users/{uuid}). |
| Get User Availability Schedule | `getUserAvailabilitySchedule` | Get a user availability schedule by UUID (GET /user_availability_schedules/{uuid}). |
| Get Webhook Subscription | `getWebhookSubscription` | Get a webhook subscription by UUID (GET /webhook_subscriptions/{uuid}). |
| List Activity Log Entries | `listActivityLogEntries` | List organization activity log entries (GET /activity_log_entries). |
| List Event Invitees | `listEventInvitees` | List invitees of a scheduled event (GET /scheduled_events/{uuid}/invitees). |
| List Event Type Available Times | `listEventTypeAvailableTimes` | List available start times for an event type within a window (GET /event_type_available_times). |
| List Event Types | `listEventTypes` | List event types for a user or organization (GET /event_types). |
| List My Scheduled Events | `listMyScheduledEvents` | Lists the scheduled events (bookings) of the connected Calendly user, without needing the user URI. Filter by invitee email, status or a start-time window. Returns events with their URI, name, start and end time, status and location, plus a page token. |
| List Organization Invitations | `listOrganizationInvitations` | List invitations for an organization (GET /organizations/{org_uuid}/invitations). |
| List Organization Memberships | `listOrganizationMemberships` | List organization memberships (GET /organization_memberships). |
| List Routing Form Submissions | `listRoutingFormSubmissions` | List submissions for a routing form (GET /routing_form_submissions). |
| List Routing Forms | `listRoutingForms` | List routing forms for an organization (GET /routing_forms). |
| List Scheduled Events | `listScheduledEvents` | List scheduled events for a user or organization (GET /scheduled_events). |
| List User Availability Schedules | `listUserAvailabilitySchedules` | List a user's availability schedules (GET /user_availability_schedules). |
| List User Busy Times | `listUserBusyTimes` | List a user's busy times in a window (GET /user_busy_times). |
| List Webhook Subscriptions | `listWebhookSubscriptions` | List webhook subscriptions (GET /webhook_subscriptions). |
| Remove Organization Membership | `removeOrganizationMembership` | Remove a user from an organization (DELETE /organization_memberships/{uuid}). Returns 204. |
| Revoke Organization Invitation | `revokeOrganizationInvitation` | Revoke an organization invitation (DELETE /organizations/{org_uuid}/invitations/{uuid}). Returns 204. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Invitee Canceled | `invitee.canceled` | An invitee canceled a scheduled event. |
| Invitee Created | `invitee.created` | An invitee scheduled an event. |
| Invitee No-Show Created | `invitee_no_show.created` | An invitee was marked as a no-show. |
| Invitee No-Show Deleted | `invitee_no_show.deleted` | An invitee no-show was undone. |
| Routing Form Submission Created | `routing_form_submission.created` | A routing form was submitted. |
