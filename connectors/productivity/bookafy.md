---
description: "Bookafy is an online appointment scheduling platform for booking meetings, consultations, classes and group events."
hidden: true
---

# Bookafy

Bookafy is an online appointment scheduling platform for booking meetings, consultations, classes and group events. This connector covers the complete Bookafy REST API v3: appointments (list, create, reschedule, cancel), customers (list, create, update, soft/hard delete, retrieve soft-deleted), services and appointment types with booking-page links, classes and their sessions and attendees, staff members, real-time staff availability lookup, the authenticated account, API key retrieval, and webhook subscription management for appointment and customer events.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [bookafy.com](https://bookafy.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 22 |
| **Events** | 6 |
| **Slug** | `bookafy` |

## Use it

Add Bookafy from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bookafy.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Appointment | `deleteAppointment` | Cancel and delete an existing appointment. Bookafy sends the configured cancellation notifications to the customer and the staff member. |
| Create Appointment | `createAppointment` | Book a new appointment for a customer with a staff member. Bookafy matches or creates the customer from the supplied booking-form details, sends the configured confirmation notifications, and composes the appointment title as 'Customer Name \| Service Name'. Use Get Available Time Slots first to pick a free start time. |
| Create Customer | `createCustomer` | Create a customer record in Bookafy without booking an appointment. The customer can then be booked later, or imported into your own system. |
| Create Staff Member | `createStaffMember` | Invite a new staff member to the account and return the generated password for their login. Staff seats are limited by your Bookafy plan, and Bookafy has no API to delete a staff member again - remove them from Settings &gt; Staff in the Bookafy web app. |
| Create Webhook Subscription | `createWebhookSubscription` | Register a callback URL to receive a POST from Bookafy whenever the chosen appointment or customer event occurs. Register one subscription per event type. |
| Delete Customer | `deleteCustomer` | Delete a customer. Send softDelete 'true' to hide the customer while keeping the record retrievable via Get Customer, or 'false' to remove the customer permanently along with their appointments. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | Remove a webhook subscription so Bookafy stops sending that event to its callback URL. |
| Get Account Email | `getAccountEmail` | Retrieve the email address of the Bookafy admin account that owns the API key. Useful as a connection health check and to obtain the staff email required by List Appointments. |
| Get API Key | `getApiKey` | Exchange a Bookafy admin email and password for that account's API key. Bookafy issues a long-lived key that does not expire, so this is normally only needed once when setting up an integration; the same key is also shown in Bookafy under Settings &gt; Integrations &gt; API. |
| Get Available Time Slots | `getAvailableTimeSlots` | Fetch the bookable start times for a staff member and service on a given date, expressed in the requested time zone. Use a returned slot as the appointment_start_time for Create Appointment. This endpoint is served only from your own booking-page host, which is why the connection asks for that URL. |
| Get Class | `getClass` | Retrieve one class or one-off group event by id, with every session and the attendees booked into each session. The optional filters narrow which sessions are returned. Returns 'Class not found' when the id does not belong to the account. |
| Get Customer | `getCustomer` | Retrieve a single customer by id, including soft-deleted customers. Pass softDelete 'true' to include customers that have been soft deleted; the soft_delete field on the returned record tells you which state it is in. |
| List Appointment Types | `listAppointmentTypes` | List the account's appointment-type categories and the services inside each one, together with the public booking-page link for every category and service. Use this to surface bookable links to customers. |
| List Appointments | `listAppointments` | List the appointments booked with a specific staff member, optionally restricted to a date range. Results are paginated and sorted by creation date descending. The staff member's email is required - an unfiltered call returns no appointments. |
| List Classes | `listClasses` | List every class and one-off group event configured on the account, with each class's scheduled sessions, seat counts and public booking link. Returns an empty list when the account has no classes. |
| List Customers | `listCustomers` | List every customer record in the authenticated Bookafy account, including their booking-form answers. Soft-deleted customers are included - check the soft_delete flag on each record to tell them apart. |
| List Services | `listServices` | List every service (appointment type) offered by the account, with its full configuration: duration, price, buffers, scheduling mode, online-meeting settings and booking-page slug. |
| List Session Attendees | `listSessionAttendees` | Retrieve the attendees booked into a single class session. The session id comes from List Classes or Get Class - an id that does not exist returns a server error rather than an empty list. |
| List Staff Members | `listStaffMembers` | List every staff member in the account with their id, name, email and personal booking-page URL. The id is what Create Appointment and Get Available Time Slots expect as user_id. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | List every webhook subscription registered on the account, with the callback URL and event type each one listens for. |
| Update Appointment | `updateAppointment` | Reschedule or edit an existing appointment. Bookafy replaces the appointment with the values supplied, so send the full staff member, service and time details even when only one of them changes, and re-send the customer's booking-form details. |
| Update Customer | `updateCustomer` | Update an existing customer's booking-form details. Bookafy replaces the stored details with the values supplied, so send every field you want to keep. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Appointment Cancelled | `appointment_destroyed` | Fires when an appointment is cancelled or deleted. Bookafy publishes no specification for the body it POSTs to a callback URL, and no delivery was observed during certification: all six event types were subscribed against a verified-reachable HTTPS endpoint and neither API-originated nor admin-UI-originated changes produced a callback within ten minutes. The schema below is therefore a recommended field set modelled on the appointment object the Bookafy REST API itself returns, not a vendor contract - confirm it against your first live delivery. Bookafy also documents no event-type discriminator inside the payload; routing is safe regardless because Bookafy registers one callback URL per event type, so this event has its own dedicated trigger URL. |
| Appointment Created | `appointment_created` | Fires when an appointment is booked in Bookafy. Bookafy publishes no specification for the body it POSTs to a callback URL, and no delivery was observed during certification: all six event types were subscribed against a verified-reachable HTTPS endpoint and neither API-originated nor admin-UI-originated changes produced a callback within ten minutes. The schema below is therefore a recommended field set modelled on the appointment object the Bookafy REST API itself returns, not a vendor contract - confirm it against your first live delivery. Bookafy also documents no event-type discriminator inside the payload; routing is safe regardless because Bookafy registers one callback URL per event type, so this event has its own dedicated trigger URL. |
| Appointment Updated | `appointment_updated` | Fires when an existing appointment is rescheduled or edited. Bookafy publishes no specification for the body it POSTs to a callback URL, and no delivery was observed during certification: all six event types were subscribed against a verified-reachable HTTPS endpoint and neither API-originated nor admin-UI-originated changes produced a callback within ten minutes. The schema below is therefore a recommended field set modelled on the appointment object the Bookafy REST API itself returns, not a vendor contract - confirm it against your first live delivery. Bookafy also documents no event-type discriminator inside the payload; routing is safe regardless because Bookafy registers one callback URL per event type, so this event has its own dedicated trigger URL. |
| Customer Created | `customer_created` | Fires when a customer record is created in Bookafy. Bookafy publishes no specification for the body it POSTs to a callback URL, and no delivery was observed during certification: all six event types were subscribed against a verified-reachable HTTPS endpoint and neither API-originated nor admin-UI-originated changes produced a callback within ten minutes. The schema below is therefore a recommended field set modelled on the customer object the Bookafy REST API itself returns, not a vendor contract - confirm it against your first live delivery. Bookafy also documents no event-type discriminator inside the payload; routing is safe regardless because Bookafy registers one callback URL per event type, so this event has its own dedicated trigger URL. |
| Customer Deleted | `customer_destroyed` | Fires when a customer record is deleted. Bookafy publishes no specification for the body it POSTs to a callback URL, and no delivery was observed during certification: all six event types were subscribed against a verified-reachable HTTPS endpoint and neither API-originated nor admin-UI-originated changes produced a callback within ten minutes. The schema below is therefore a recommended field set modelled on the customer object the Bookafy REST API itself returns, not a vendor contract - confirm it against your first live delivery. Bookafy also documents no event-type discriminator inside the payload; routing is safe regardless because Bookafy registers one callback URL per event type, so this event has its own dedicated trigger URL. |
| Customer Updated | `customer_updated` | Fires when a customer's details are updated. Bookafy publishes no specification for the body it POSTs to a callback URL, and no delivery was observed during certification: all six event types were subscribed against a verified-reachable HTTPS endpoint and neither API-originated nor admin-UI-originated changes produced a callback within ten minutes. The schema below is therefore a recommended field set modelled on the customer object the Bookafy REST API itself returns, not a vendor contract - confirm it against your first live delivery. Bookafy also documents no event-type discriminator inside the payload; routing is safe regardless because Bookafy registers one callback URL per event type, so this event has its own dedicated trigger URL. |
