---
description: "Microsoft Bookings appointment scheduling via the Microsoft Graph v1.0 API (https://graph.microsoft.com/v1.0/solutions/bookingBusinesses)."
hidden: true
---

# Microsoft Bookings

<img src="../../.gitbook/assets/connectors/microsoft-bookings.png" alt="Microsoft Bookings logo" width="64">

Microsoft Bookings appointment scheduling via the Microsoft Graph v1.0 API (https://graph.microsoft.com/v1.0/solutions/bookingBusinesses). Manage booking businesses (create, read, update, delete, publish and unpublish the self-service booking page), services, staff members, customers, custom questions and appointments, cancel an appointment with a message, read the calendar view for a date range, look up staff availability, and list the supported booking currencies. Connect with a Microsoft work or school account using Entra ID OAuth 2.0. All four delegated Bookings permissions are user-consentable and need no tenant administrator approval, but the tenant must have Microsoft Bookings enabled and the signed-in user must hold a licence that includes it (Microsoft 365 Business Standard or Premium, or A3/A5/E3/E5).

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [graph.microsoft.com](https://graph.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `microsoftBookings` |

## Use it

Add Microsoft Bookings from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.microsoftBookings.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Booking Appointment | `cancelBookingAppointment` | Cancels an appointment of a Microsoft Bookings business and emails the customer the cancellation message. The appointment record itself is kept; use Delete Booking Appointment to remove it. |
| Create Booking Appointment | `createBookingAppointment` | Books an appointment for a service of a Microsoft Bookings business. When the service allows more than one attendee, each entry in Customers must carry a valid customerId created with Create Booking Customer. |
| Create Booking Business | `createBookingBusiness` | Creates a new Microsoft Bookings business. Display Name is the only required property; everything else can be set later with Update Booking Business. Requires the Bookings.Manage.All delegated permission. |
| Create Booking Custom Question | `createBookingCustomQuestion` | Creates a custom question for a Microsoft Bookings business. Attach the question to a service through the Custom Questions input of Create or Update Booking Service. |
| Create Booking Customer | `createBookingCustomer` | Registers a customer with a Microsoft Bookings business. A customer must exist before it can be referenced by ID on an appointment whose service allows more than one attendee. |
| Create Booking Service | `createBookingService` | Creates a bookable service in a Microsoft Bookings business, defining its duration, price, assigned staff, buffers and reminders. |
| Create Booking Staff Member | `createBookingStaffMember` | Adds a staff member to a Microsoft Bookings business. Display Name, Email Address and Role are required by the API. The staff member's email may be inside or outside the tenant. |
| Delete Booking Appointment | `deleteBookingAppointment` | Permanently deletes an appointment from a Microsoft Bookings business without notifying the customer. Use Cancel Booking Appointment when the customer should be told. |
| Delete Booking Business | `deleteBookingBusiness` | Permanently deletes a Microsoft Bookings business together with its services, staff, customers and appointments. Requires the Bookings.Manage.All delegated permission and cannot be undone. |
| Delete Booking Custom Question | `deleteBookingCustomQuestion` | Permanently deletes a custom question from a Microsoft Bookings business. Services that still reference the question should be updated afterwards. |

<details>

<summary>See 27 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Booking Customer | `deleteBookingCustomer` | Permanently deletes a customer from a Microsoft Bookings business. Existing appointments that reference the customer are not removed. |
| Delete Booking Service | `deleteBookingService` | Permanently deletes a bookable service from a Microsoft Bookings business. Existing appointments for the service are not removed. |
| Delete Booking Staff Member | `deleteBookingStaffMember` | Removes a staff member from a Microsoft Bookings business. Services that reference the staff member keep the entry in staffMemberIds until updated. |
| Get Booking Appointment | `getBookingAppointment` | Retrieves a single appointment of a Microsoft Bookings business. Reading an appointment by ID is the only way to see its customer notes, service notes and reminders. |
| Get Booking Business | `getBookingBusiness` | Retrieves a single Microsoft Bookings business, including its address, business hours, scheduling policy, booking page settings and public scheduling page URL. |
| Get Booking Currency | `getBookingCurrency` | Retrieves a single currency supported by Microsoft Bookings, by its ISO 4217 code. |
| Get Booking Custom Question | `getBookingCustomQuestion` | Retrieves a single custom question of a Microsoft Bookings business, including its answer type and any preset answer options. |
| Get Booking Customer | `getBookingCustomer` | Retrieves a single customer of a Microsoft Bookings business, including their phone numbers and addresses. |
| Get Booking Service | `getBookingService` | Retrieves a single bookable service of a Microsoft Bookings business, including its default reminders, custom questions and scheduling policy. |
| Get Booking Staff Member | `getBookingStaffMember` | Retrieves a single staff member of a Microsoft Bookings business, including their working hours for each day of the week. |
| Get Staff Availability | `getStaffAvailability` | Returns the availability of the specified Bookings staff members over a date range. Note that Microsoft Graph serves this endpoint for application (app-only) tokens only: a delegated user token is rejected with 403 Forbidden, "Api Business.GetStaffAvailability does not support the token type: User". Use a client-credentials connection for this action. |
| List Booking Appointments | `listBookingAppointments` | Lists all appointments of a Microsoft Bookings business. To retrieve appointments within a date range use List Booking Calendar View instead, which is the supported way to filter by date. |
| List Booking Businesses | `listBookingBusinesses` | Lists the Microsoft Bookings businesses in the tenant that the signed-in user can access. Supply Search Query to limit the results to businesses whose name matches a string. |
| List Booking Calendar View | `listBookingCalendarView` | Lists the appointments of a Microsoft Bookings business that fall inside a date range. Start and End are required query parameters and must be ISO 8601 timestamps. |
| List Booking Currencies | `listBookingCurrencies` | Lists the currencies Microsoft Bookings supports, which are the valid values for a business's default currency. The endpoint always returns the complete set: Microsoft Graph ignores paging, filtering and property selection on this collection, so narrow the results in your own code. |
| List Booking Custom Questions | `listBookingCustomQuestions` | Lists the custom questions defined for a Microsoft Bookings business, which services can attach to their booking form. |
| List Booking Customers | `listBookingCustomers` | Lists the customers registered with a Microsoft Bookings business. |
| List Booking Services | `listBookingServices` | Lists the bookable services offered by a Microsoft Bookings business, with their durations, prices and assigned staff. |
| List Booking Staff Members | `listBookingStaffMembers` | Lists the staff members of a Microsoft Bookings business, with their roles, working hours and membership status. |
| Publish Booking Business | `publishBookingBusiness` | Makes the self-service scheduling page of a Microsoft Bookings business available to external customers, setting isPublished to true and populating publicUrl. Requires the Bookings.Manage.All delegated permission. |
| Unpublish Booking Business | `unpublishBookingBusiness` | Withdraws the self-service scheduling page of a Microsoft Bookings business from external customers, setting isPublished to false. Requires the Bookings.Manage.All delegated permission. |
| Update Booking Appointment | `updateBookingAppointment` | Updates an appointment of a Microsoft Bookings business, for example to reschedule it or change its staff. Only the properties you supply are sent. |
| Update Booking Business | `updateBookingBusiness` | Updates a Microsoft Bookings business. Only the properties you supply are sent, so untouched settings keep their values. The isPublished and publicUrl properties are read-only; use Publish and Unpublish instead. |
| Update Booking Custom Question | `updateBookingCustomQuestion` | Updates a custom question of a Microsoft Bookings business. Only the properties you supply are sent. |
| Update Booking Customer | `updateBookingCustomer` | Updates a customer of a Microsoft Bookings business. Only the properties you supply are sent, so untouched details keep their values. Verified live: supplying Phones or Addresses merges the entries into the existing list rather than replacing it, so read the customer first if you need to remove an entry. |
| Update Booking Service | `updateBookingService` | Updates a bookable service of a Microsoft Bookings business. Only the properties you supply are sent, so untouched settings keep their values. |
| Update Booking Staff Member | `updateBookingStaffMember` | Updates a staff member of a Microsoft Bookings business, for example their role, time zone or working hours. Only the properties you supply are sent. |

</details>
