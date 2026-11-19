---
description: "SuperSaaS is an online appointment scheduling platform. Create and delete bookings, slots and users, manage promotions, and read user agendas."
hidden: true
---

# SuperSaaS

<img src="../../.gitbook/assets/connectors/lg/supersaas.png" alt="SuperSaaS logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [supersaas.com](https://supersaas.com) |
| **Authentication** | Username and password |
| **Slug** | `supersaas` |

## Setup

Your customers enter their username and password for SuperSaaS when they connect. Nothing else needs setting up.

## Use it

Add SuperSaaS from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.supersaas.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Booking</td><td><code>createBooking</code></td><td>Create an appointment in a resource or capacity schedule Not for service schedules. Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>Create or Update User by Your Key</td><td><code>createUserWithKey</code></td><td>Create a user under your own key (format like 9999fk); if the key exists the call updates it unless duplicate=raise Docs: https://www.supersaas.com/info/dev/user_api</td></tr><tr><td>Create Slot</td><td><code>createSlot</code></td><td>Create a slot in a capacity schedule Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>Create User</td><td><code>createUser</code></td><td>Create a user; SuperSaaS assigns the ID Docs: https://www.supersaas.com/info/dev/user_api</td></tr><tr><td>Delete Booking</td><td><code>deleteBooking</code></td><td>Delete an appointment Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>Delete Promotion</td><td><code>deletePromotion</code></td><td>Delete a promotion code; existing bookings keep their discounts Docs: https://www.supersaas.com/info/dev/promotion_api</td></tr><tr><td>Delete Slot</td><td><code>deleteSlot</code></td><td>Delete a slot and ALL its bookings, without notification or undo Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>Delete User</td><td><code>deleteUser</code></td><td>Delete a user Docs: https://www.supersaas.com/info/dev/user_api</td></tr><tr><td>Duplicate Promotion</td><td><code>duplicatePromotion</code></td><td>Create a new promotion code copied from an existing template code Docs: https://www.supersaas.com/info/dev/promotion_api</td></tr><tr><td>Get Availability</td><td><code>getAvailability</code></td><td>List free time (resource type) or free slots (capacity type) after a time Not for service schedules. Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr></tbody></table>

<details>

<summary>View 22 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Booking</td><td><code>getBooking</code></td><td>Read one appointment Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>Get Field List</td><td><code>getFieldList</code></td><td>Get the list of fields on bookings of a schedule, or on User objects when schedule_id is omitted Docs: https://www.supersaas.com/info/dev/information_api</td></tr><tr><td>Get Form</td><td><code>getForm</code></td><td>Read one filled-in form by ID Docs: https://www.supersaas.com/info/dev/form_api</td></tr><tr><td>Get Promotion</td><td><code>getPromotion</code></td><td>Read one promotion code Docs: https://www.supersaas.com/info/dev/promotion_api</td></tr><tr><td>Get Recent Changes</td><td><code>getRecentChanges</code></td><td>List bookings changed in a schedule in a time window Without from, returns the 10 most recent changes. Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>Get Slot</td><td><code>getSlot</code></td><td>Read one slot of a capacity schedule Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>Get User</td><td><code>getUser</code></td><td>Read one user by SuperSaaS ID (numeric) or your foreign key Docs: https://www.supersaas.com/info/dev/user_api</td></tr><tr><td>Get User Agenda</td><td><code>getAgenda</code></td><td>List a user's upcoming appointments in one schedule Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>Get User Agenda (All Schedules)</td><td><code>getAgendaAllSchedules</code></td><td>List a user's upcoming appointments across all schedules The account name is taken from the connection username. Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>List Appointments in Range</td><td><code>listAppointmentsInRange</code></td><td>List appointments (or slots for capacity schedules) in a time range Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>List Bookings</td><td><code>listBookings</code></td><td>List appointments of a schedule Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>List Form Definitions</td><td><code>listSuperForms</code></td><td>List the account's form definitions (super forms) with their internal IDs Docs: https://www.supersaas.com/info/dev/information_api</td></tr><tr><td>List Forms</td><td><code>listForms</code></td><td>List filled-in forms of one form definition Docs: https://www.supersaas.com/info/dev/form_api</td></tr><tr><td>List Groups</td><td><code>listGroups</code></td><td>List user groups as [id, name] pairs Docs: https://www.supersaas.com/info/dev/information_api</td></tr><tr><td>List Promotions</td><td><code>listPromotions</code></td><td>List promotion (coupon) codes Docs: https://www.supersaas.com/info/dev/promotion_api</td></tr><tr><td>List Resources or Services</td><td><code>listResources</code></td><td>List the resources or services of a schedule as [id, name] pairs Not available for capacity schedules. Docs: https://www.supersaas.com/info/dev/information_api</td></tr><tr><td>List Schedules</td><td><code>listSchedules</code></td><td>List all schedules in the account as [id, name] pairs Docs: https://www.supersaas.com/info/dev/information_api</td></tr><tr><td>List Slots</td><td><code>listSlots</code></td><td>List slots of a capacity schedule ordered by start Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>List Users</td><td><code>listUsers</code></td><td>List all users with paging Docs: https://www.supersaas.com/info/dev/user_api</td></tr><tr><td>Update Booking</td><td><code>updateBooking</code></td><td>Update an appointment Only sent fields change. Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>Update Slot</td><td><code>updateSlot</code></td><td>Update a slot Only sent fields change. Docs: https://www.supersaas.com/info/dev/appointment_api</td></tr><tr><td>Update User</td><td><code>updateUser</code></td><td>Update a user Without notfound a missing user is created. Docs: https://www.supersaas.com/info/dev/user_api</td></tr></tbody></table>

</details>

## Events

SuperSaaS has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
