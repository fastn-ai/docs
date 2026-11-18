---
description: "Acuity Scheduling (a Squarespace company) is an online appointment scheduling platform."
hidden: true
---

# Acuity Scheduling

<img src="../../.gitbook/assets/connectors/acuity-scheduling.png" alt="Acuity Scheduling logo" width="64">

Acuity Scheduling (a Squarespace company) is an online appointment scheduling platform. Manage appointments, appointment types, availability, calendars, clients, intake forms, labels, orders, products, package and coupon certificates, blocked time, and webhook subscriptions through the Acuity Scheduling API v1.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [acuityscheduling.com](https://acuityscheduling.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `acuityScheduling` |

## Use it

Add Acuity Scheduling from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.acuityScheduling.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Appointment | `cancelAppointment` | Cancels an existing appointment. Canceling as an admin bypasses the account's client cancellation rules and allows marking the appointment as a no show. An appointment cannot be un-canceled. |
| Check Available Time | `checkAvailableTime` | Validates that a specific date and time is bookable for an appointment type before creating the appointment. |
| Check Certificate | `checkCertificate` | Validates that a certificate code may be redeemed against a given appointment type, and returns the certificate's remaining balance. |
| Create Appointment | `createAppointment` | Books a new appointment for a client on the authenticated Acuity account. Availability is validated as a client booking unless Book as Admin is set to true, in which case a calendar ID is required. |
| Create Blocked Time | `createBlock` | Blocks off a period of time on a calendar so no appointments can be booked into it. |
| Create Certificate | `createCertificate` | Issues a package or coupon certificate code. Supply either a package Product ID or a Coupon ID; Acuity generates the code when one is not supplied. |
| Create Client | `createClient` | Creates a new client record on the authenticated Acuity account. Acuity returns 400 client_aready_exists when a client with the same name and phone number already exists. |
| Create Webhook | `createWebhook` | Creates a webhook subscription so Acuity notifies a target URL when the chosen event occurs. The target must be reachable on port 443 or 80, and an account may hold at most 25 webhooks. |
| Delete Blocked Time | `deleteBlockedTime` | Removes a blocked off period from a calendar, making the time bookable again. |
| Delete Certificate | `deleteCertificate` | Deletes a package or coupon certificate code so it can no longer be redeemed. |

<details>

<summary>See 26 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Client | `deleteClient` | Deletes a client record, located by first name, last name and optionally phone number. Acuity returns 400 client_not_found when no client matches. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook subscription so Acuity stops sending notifications to its target URL. |
| Get Account | `getAccount` | Returns the profile of the authenticated Acuity account, including its timezone, currency, plan and scheduling page URL. |
| Get Appointment | `getAppointment` | Returns a single appointment on the authenticated Acuity account by its numeric appointment ID. |
| Get Blocked Time | `getBlockedTime` | Returns a single blocked off period by its numeric block ID. |
| Get Order | `getOrder` | Returns a single online store order by its numeric order ID. |
| Get Service Metadata | `getMetadata` | Returns metadata about the Acuity service, including the IPv4 and IPv6 CIDR ranges that webhook deliveries originate from. |
| List Appointment Addons | `listAppointmentAddons` | Returns every appointment addon configured on the authenticated Acuity account, including its duration and price. |
| List Appointment Payments | `listAppointmentPayments` | Returns the payment transactions recorded against a single appointment. |
| List Appointment Types | `listAppointmentTypes` | Returns every appointment type, class and series configured on the authenticated Acuity account. |
| List Appointments | `listAppointments` | Returns the appointments scheduled on the authenticated Acuity account, newest first, with optional date, calendar, appointment type and client filters. Canceled appointments are excluded unless Canceled Only or Show All is "true". Note: Acuity's dynamic intake-form filter (?field:&lt;id&gt;=&lt;value&gt;) is not exposed because its key is dynamic; filter the returned list by the forms data instead. |
| List Available Classes | `listAvailableClasses` | Returns the scheduled class and series occurrences for a month, including how many seats remain in each. |
| List Available Dates | `listAvailableDates` | Returns the dates in a given month that have availability for an appointment type. Both Month and Appointment Type ID are required; the call returns 400 required_month or 400 required_appointment_type_id without them. |
| List Available Times | `listAvailableTimes` | Returns the bookable start times on a given date for an appointment type. Both Date and Appointment Type ID are required; the call returns 400 required_date or 400 required_appointment_type_id without them. |
| List Blocked Times | `listBlocks` | Returns the blocked off periods on the authenticated Acuity account's calendars. |
| List Calendars | `listCalendars` | Returns every calendar the authenticated Acuity user has access to. |
| List Certificates | `listCertificates` | Returns package and coupon certificates issued on the authenticated Acuity account. Combine Email with Appointment Type ID to suggest valid certificates to a client. |
| List Clients | `listClients` | Returns the clients stored on the authenticated Acuity account, optionally filtered by a search term matched against first name, last name and phone number. |
| List Intake Forms | `listForms` | Returns every intake form on the authenticated Acuity account together with its fields, which supplies the field IDs needed when booking or updating an appointment. |
| List Labels | `listLabels` | Returns the appointment labels configured on the authenticated Acuity account, which supplies the label IDs used when creating or updating an appointment. |
| List Orders | `listOrders` | Returns orders placed through the Acuity online store, most recent first. Orders cover packages, gift certificates and subscriptions. |
| List Products | `listProducts` | Returns the products, packages and gift certificates sold through the Acuity online store. |
| List Webhooks | `listWebhooks` | Returns the active webhook subscriptions created through the Acuity Webhooks API for the authenticated account. |
| Reschedule Appointment | `rescheduleAppointment` | Moves an existing appointment to a new date and time, and optionally to a different calendar. |
| Update Appointment | `updateAppointment` | Updates the client details, intake form answers, notes or label on an existing appointment. Use Reschedule Appointment to change its time. |
| Update Client | `updateClient` | Updates an existing client record. The client is located by the Current First Name, Current Last Name and Current Phone inputs, and the remaining inputs supply the new values. Acuity returns 400 client_not_found when no client matches. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Appointment Canceled | `canceled` | Fires when an appointment is canceled. Registered with Acuity as the appointment.canceled subscription; the delivered payload's action field is 'canceled'. |
| Appointment Changed | `changed` | Catch-all that fires whenever an appointment changes in any way, including when it is scheduled, rescheduled, canceled, or has its client details or intake form answers edited. Acuity warns that subscribing to this alongside the scheduled, rescheduled or canceled events produces duplicate deliveries. Registered with Acuity as the appointment.changed subscription; the delivered payload's action field is 'changed'. |
| Appointment Rescheduled | `rescheduled` | Fires when an appointment is moved to a new time. Registered with Acuity as the appointment.rescheduled subscription; the delivered payload's action field is 'rescheduled'. |
| Appointment Scheduled | `scheduled` | Fires once when an appointment is initially booked. Registered with Acuity as the appointment.scheduled subscription; the delivered payload's action field is 'scheduled'. |
| Order Completed | `order.completed` | Fires when an online store order for a package, gift certificate or subscription is completed. Registered with Acuity as the order.completed subscription; the delivered payload's action field is 'order.completed'. |
