---
description: "SuperSaaS is an online appointment scheduling and booking platform."
hidden: true
---

# SuperSaaS

SuperSaaS is an online appointment scheduling and booking platform. This connector wraps the SuperSaaS REST API at https://www.supersaas.com/api: the user database (create, read, update and delete users, with groups and the account field list), schedules and form definitions, submitted form data, promotional coupon codes, resources and services, appointments (bookings, recent changes, date-range listing, per-user agenda and availability), and the REST-hooks webhook subscriptions that drive SuperSaaS event notifications.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [supersaas.com](https://supersaas.com) |
| **Authentication** | Basic auth |
| **Actions** | 32 |
| **Events** | 0 |
| **Slug** | `supersaas` |

## Use it

Add SuperSaaS from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.supersaas.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Booking | `createBooking` | Create an appointment in a resource or capacity schedule (POST /api/bookings.json). Returns 201 with the new ID in the Location header. Not for service schedules. Docs: https://www.supersaas.com/info/dev/appointment_api |
| Create or Update User by Your Key | `createUserWithKey` | Create a user under your own key (format like 9999fk); if the key exists the call updates it unless duplicate=raise (POST /api/users/{id}.json). Docs: https://www.supersaas.com/info/dev/user_api |
| Create Slot | `createSlot` | Create a slot in a capacity schedule (POST /api/slots.json). Returns 201 with the slot ID in the Location header. Docs: https://www.supersaas.com/info/dev/appointment_api |
| Create User | `createUser` | Create a user; SuperSaaS assigns the ID (POST /api/users.json). Returns 201 with the new user's URL in the Location header. Docs: https://www.supersaas.com/info/dev/user_api |
| Delete Booking | `deleteBooking` | Delete an appointment (DELETE /api/bookings/{id}.json). Docs: https://www.supersaas.com/info/dev/appointment_api |
| Delete Promotion | `deletePromotion` | Delete a promotion code; existing bookings keep their discounts (DELETE /api/promotions.json?id=). Docs: https://www.supersaas.com/info/dev/promotion_api |
| Delete Slot | `deleteSlot` | Delete a slot and ALL its bookings, without notification or undo (DELETE /api/slots/{id}.json). Docs: https://www.supersaas.com/info/dev/appointment_api |
| Delete User | `deleteUser` | Delete a user (DELETE /api/users/{id}.json). Docs: https://www.supersaas.com/info/dev/user_api |
| Duplicate Promotion | `duplicatePromotion` | Create a new promotion code copied from an existing template code (POST /api/promotions.json). Docs: https://www.supersaas.com/info/dev/promotion_api |
| Get Availability | `getAvailability` | List free time (resource type) or free slots (capacity type) after a time (GET /api/free/{schedule_id}.json). Not for service schedules. Docs: https://www.supersaas.com/info/dev/appointment_api |
| Get Booking | `getBooking` | Read one appointment (GET /api/bookings/{id}.json). Docs: https://www.supersaas.com/info/dev/appointment_api |
| Get Field List | `getFieldList` | Get the list of fields on bookings of a schedule, or on User objects when schedule_id is omitted (GET /api/field_list.json). Docs: https://www.supersaas.com/info/dev/information_api |
| Get Form | `getForm` | Read one filled-in form by ID (GET /api/forms.json?id=). Docs: https://www.supersaas.com/info/dev/form_api |
| Get Promotion | `getPromotion` | Read one promotion code (GET /api/promotions.json?id=). Docs: https://www.supersaas.com/info/dev/promotion_api |
| Get Recent Changes | `getRecentChanges` | List bookings changed in a schedule in a time window (GET /api/changes/{schedule_id}.json). Without from, returns the 10 most recent changes. Docs: https://www.supersaas.com/info/dev/appointment_api |
| Get Slot | `getSlot` | Read one slot of a capacity schedule (GET /api/slots/{id}.json). Docs: https://www.supersaas.com/info/dev/appointment_api |
| Get User | `getUser` | Read one user by SuperSaaS ID (numeric) or your foreign key (GET /api/users/{id}.json). Docs: https://www.supersaas.com/info/dev/user_api |
| Get User Agenda | `getAgenda` | List a user's upcoming appointments in one schedule (GET /api/agenda/{schedule_id}.json). Docs: https://www.supersaas.com/info/dev/appointment_api |
| Get User Agenda (All Schedules) | `getAgendaAllSchedules` | List a user's upcoming appointments across all schedules (GET /api/agenda.json). The account name is taken from the connection username. Docs: https://www.supersaas.com/info/dev/appointment_api |
| List Appointments in Range | `listAppointmentsInRange` | List appointments (or slots for capacity schedules) in a time range (GET /api/range/{schedule_id}.json). Docs: https://www.supersaas.com/info/dev/appointment_api |
| List Bookings | `listBookings` | List appointments of a schedule (GET /api/bookings.json). Docs: https://www.supersaas.com/info/dev/appointment_api |
| List Form Definitions | `listSuperForms` | List the account's form definitions (super forms) with their internal IDs (GET /api/super_forms.json). Docs: https://www.supersaas.com/info/dev/information_api |
| List Forms | `listForms` | List filled-in forms of one form definition (GET /api/forms.json?form_id=). Docs: https://www.supersaas.com/info/dev/form_api |
| List Groups | `listGroups` | List user groups as [id, name] pairs (GET /api/groups.json). Docs: https://www.supersaas.com/info/dev/information_api |
| List Promotions | `listPromotions` | List promotion (coupon) codes (GET /api/promotions.json). Docs: https://www.supersaas.com/info/dev/promotion_api |
| List Resources or Services | `listResources` | List the resources or services of a schedule as [id, name] pairs (GET /api/resources.json). Not available for capacity schedules. Docs: https://www.supersaas.com/info/dev/information_api |
| List Schedules | `listSchedules` | List all schedules in the account as [id, name] pairs (GET /api/schedules.json). Docs: https://www.supersaas.com/info/dev/information_api |
| List Slots | `listSlots` | List slots of a capacity schedule ordered by start (GET /api/slots.json). Docs: https://www.supersaas.com/info/dev/appointment_api |
| List Users | `listUsers` | List all users with paging (GET /api/users.json). Docs: https://www.supersaas.com/info/dev/user_api |
| Update Booking | `updateBooking` | Update an appointment (PUT /api/bookings/{id}.json). Only sent fields change. Docs: https://www.supersaas.com/info/dev/appointment_api |
| Update Slot | `updateSlot` | Update a slot (PUT /api/slots/{id}.json). Only sent fields change. Docs: https://www.supersaas.com/info/dev/appointment_api |
| Update User | `updateUser` | Update a user (PUT /api/users/{id}.json). Without notfound a missing user is created. Docs: https://www.supersaas.com/info/dev/user_api |
