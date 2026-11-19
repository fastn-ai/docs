---
description: "Calendly is a scheduling platform. Read and cancel scheduled events, create scheduling links and manage webhooks."
hidden: true
---

# Calendly

<img src="../../.gitbook/assets/connectors/lg/calendly.png" alt="Calendly logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [calendly.com](https://calendly.com) |
| **Authentication** | Access token, OAuth 2.0 |
| **Slug** | `calendly` |

## Setup

Your customers sign in to Calendly through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Calendly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.calendly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel Scheduled Event</td><td><code>cancelScheduledEvent</code></td><td>Cancel a scheduled event</td></tr><tr><td>Create Event Invitee</td><td><code>createEventInvitee</code></td><td>Books a meeting on a Calendly event type for an invitee, the same as the invitee booking through the Calendly page. start_time must be an open slot from List Event Type Available Times. Calendly sends its usual confirmation emails and adds the event to the host's calendar. Returns the invitee with the scheduled event URI, cancel URL and reschedule URL. Calendly allows this only on paid plans (Standard and above).</td></tr><tr><td>Create Invitee No Show</td><td><code>createInviteeNoShow</code></td><td>Mark an invitee as a no-show</td></tr><tr><td>Create Organization Invitation</td><td><code>createOrganizationInvitation</code></td><td>Invite a user to an organization</td></tr><tr><td>Create Scheduling Link</td><td><code>createSchedulingLink</code></td><td>Create a single-use scheduling link for an event type</td></tr><tr><td>Create Webhook Subscription</td><td><code>createWebhookSubscription</code></td><td>Create a webhook subscription Used by the webhook config subscription code.</td></tr><tr><td>Delete Invitee Data</td><td><code>deleteInviteeData</code></td><td>Request deletion of invitee PII for compliance</td></tr><tr><td>Delete Invitee No Show</td><td><code>deleteInviteeNoShow</code></td><td>Undo an invitee no-show</td></tr><tr><td>Delete Webhook Subscription</td><td><code>deleteWebhookSubscription</code></td><td>Delete a webhook subscription</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Get the current authenticated user</td></tr></tbody></table>

<details>

<summary>View 26 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Event Invitee</td><td><code>getEventInvitee</code></td><td>Get a single invitee of a scheduled event</td></tr><tr><td>Get Event Type</td><td><code>getEventType</code></td><td>Get an event type by UUID</td></tr><tr><td>Get Invitee No Show</td><td><code>getInviteeNoShow</code></td><td>Get an invitee no-show by UUID</td></tr><tr><td>Get Organization Invitation</td><td><code>getOrganizationInvitation</code></td><td>Get an organization invitation</td></tr><tr><td>Get Organization Membership</td><td><code>getOrganizationMembership</code></td><td>Get an organization membership by UUID</td></tr><tr><td>Get Routing Form</td><td><code>getRoutingForm</code></td><td>Get a routing form by UUID</td></tr><tr><td>Get Routing Form Submission</td><td><code>getRoutingFormSubmission</code></td><td>Get a routing form submission by UUID</td></tr><tr><td>Get Scheduled Event</td><td><code>getScheduledEvent</code></td><td>Get a scheduled event by UUID</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Get a user by UUID</td></tr><tr><td>Get User Availability Schedule</td><td><code>getUserAvailabilitySchedule</code></td><td>Get a user availability schedule by UUID</td></tr><tr><td>Get Webhook Subscription</td><td><code>getWebhookSubscription</code></td><td>Get a webhook subscription by UUID</td></tr><tr><td>List Activity Log Entries</td><td><code>listActivityLogEntries</code></td><td>List organization activity log entries</td></tr><tr><td>List Event Invitees</td><td><code>listEventInvitees</code></td><td>List invitees of a scheduled event</td></tr><tr><td>List Event Type Available Times</td><td><code>listEventTypeAvailableTimes</code></td><td>List available start times for an event type within a window</td></tr><tr><td>List Event Types</td><td><code>listEventTypes</code></td><td>List event types for a user or organization</td></tr><tr><td>List My Scheduled Events</td><td><code>listMyScheduledEvents</code></td><td>Lists the scheduled events (bookings) of the connected Calendly user, without needing the user URI. Filter by invitee email, status or a start-time window. Returns events with their URI, name, start and end time, status and location, plus a page token.</td></tr><tr><td>List Organization Invitations</td><td><code>listOrganizationInvitations</code></td><td>List invitations for an organization</td></tr><tr><td>List Organization Memberships</td><td><code>listOrganizationMemberships</code></td><td>List organization memberships</td></tr><tr><td>List Routing Form Submissions</td><td><code>listRoutingFormSubmissions</code></td><td>List submissions for a routing form</td></tr><tr><td>List Routing Forms</td><td><code>listRoutingForms</code></td><td>List routing forms for an organization</td></tr><tr><td>List Scheduled Events</td><td><code>listScheduledEvents</code></td><td>List scheduled events for a user or organization</td></tr><tr><td>List User Availability Schedules</td><td><code>listUserAvailabilitySchedules</code></td><td>List a user's availability schedules</td></tr><tr><td>List User Busy Times</td><td><code>listUserBusyTimes</code></td><td>List a user's busy times in a window</td></tr><tr><td>List Webhook Subscriptions</td><td><code>listWebhookSubscriptions</code></td><td>List webhook subscriptions</td></tr><tr><td>Remove Organization Membership</td><td><code>removeOrganizationMembership</code></td><td>Remove a user from an organization</td></tr><tr><td>Revoke Organization Invitation</td><td><code>revokeOrganizationInvitation</code></td><td>Revoke an organization invitation</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Invitee Canceled</td><td><code>invitee.canceled</code></td><td>An invitee canceled a scheduled event.</td></tr><tr><td>Invitee Created</td><td><code>invitee.created</code></td><td>An invitee scheduled an event.</td></tr><tr><td>Invitee No-Show Created</td><td><code>invitee_no_show.created</code></td><td>An invitee was marked as a no-show.</td></tr><tr><td>Invitee No-Show Deleted</td><td><code>invitee_no_show.deleted</code></td><td>An invitee no-show was undone.</td></tr><tr><td>Routing Form Submission Created</td><td><code>routing_form_submission.created</code></td><td>A routing form was submitted.</td></tr></tbody></table>
