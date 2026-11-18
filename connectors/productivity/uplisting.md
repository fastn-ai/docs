---
description: "Uplisting is a vacation-rental and short-term-let property management platform."
---

# Uplisting

Uplisting is a vacation-rental and short-term-let property management platform. This connector covers the full public Uplisting API: account verification, properties, availability search, bookings, calendar rates and restrictions, calendar updates, webhook registration, and the partner-only v2 endpoints for creating bookings and managing custom booking attributes.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [uplisting.io](https://uplisting.io) |
| **Authentication** | Credentials you enter |
| **Actions** | 15 |
| **Events** | 6 |
| **Slug** | `uplisting` |

## Use it

Add Uplisting from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.uplisting.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Booking | `createBooking` | Creates a confirmed booking on a property for the given stay dates. A guest email is needed for any scheduled guest messages to be delivered, and the guest count is used for price calculation. Requires a partner client ID to be set on the connection. |
| Create Custom Booking Attribute | `createCustomBookingAttribute` | Creates a custom booking attribute that can then hold extra metadata on individual bookings and be referenced in the host's automated message templates. Names must be snake_case and prefixed with the partner namespace, and a partner may define at most fifteen attributes per account. Requires a partner client ID with a configured attribute prefix. |
| Create Webhook | `createWebhook` | Registers a webhook so that Uplisting posts a payload to your target URL whenever the chosen booking or property event occurs. Returns the new webhook identifier and the signing secret Uplisting uses for that hook. |
| Delete Webhook | `deleteWebhook` | Removes a registered webhook by its identifier so Uplisting stops posting that event to the target URL. |
| Get Calendar | `getCalendar` | Retrieves the day-by-day calendar for one property, including nightly rate, availability, minimum length of stay and arrival and departure restrictions. The response covers at most twelve months; with no date range it returns a year from today. |
| Get Property | `getProperty` | Retrieves a single property by its Uplisting identifier. Uplisting serves this endpoint as application/vnd.api+json, which fastn returns as a file reference whose data field is the Base64-encoded JSON:API document; decode it to get the property resource plus its address, photos, multi-unit, fees, taxes, suitabilities, channel commissions and amenities in the included array. |
| List Bookings | `listBookings` | Retrieves the bookings for one property. With no date range it returns a year from today; with a from date only it returns twelve months from that date. Results are paginated at a maximum of 50 bookings per page and the meta section reports the total bookings and total pages. |
| List Custom Booking Attributes | `listCustomBookingAttributes` | Lists the custom booking attributes available on the account, which are the attributes that Update Booking Attributes can set on an individual booking and that hosts can reference in automated message templates. Requires a partner client ID to be set on the connection. |
| List Properties | `listProperties` | Retrieves every property on the connected Uplisting account. Uplisting serves this endpoint as application/vnd.api+json, which fastn returns as a file reference whose data field is the Base64-encoded JSON:API document; decode it to get an object with a data array of properties and an included array carrying each property's address, photos, multi-units, fees, taxes, discounts, suitabilities, policies, channel commissions and amenities. |
| List Webhooks | `listWebhooks` | Retrieves every webhook registered on the connected Uplisting account in JSON:API format, showing the target URL and event type each one is subscribed to. |
| Ping API | `pingApi` | Checks that the Uplisting API is reachable, returning the literal text 'pong'. This is a liveness probe only and does not validate credentials, so use Verify API Key to confirm a connection is authenticated. |
| Search Availability | `searchAvailability` | Searches the connected Uplisting account for properties available under the supplied criteria. Every criterion is optional and they combine with AND. Uplisting serves this endpoint as application/vnd.api+json, which fastn returns as a file reference whose data field is the Base64-encoded JSON:API document; decode it to get the matching properties plus their addresses, photos and amenities in the included array. |
| Update Booking Attributes | `updateBookingAttributes` | Sets values for custom booking attributes on one booking. Only attributes returned by List Custom Booking Attributes can be set, and values are stored as strings for use in the host's automated message tags. Requires a partner client ID to be set on the connection. |
| Update Calendar | `updateCalendar` | Updates nightly rates, availability and minimum length of stay for a property across a date range, and broadcasts the change to every channel the property is connected to. Uplisting schedules the payload and applies it asynchronously, usually within a minute, returning a request identifier immediately; supply a notification URL to be told whether the update succeeded. |
| Verify API Key | `verifyApiKey` | Verifies that the configured Uplisting API key is valid and returns the name and unique identifier of the Uplisting account it belongs to. Use this to confirm a connection before running any other action. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Booking Created | `booking_created` | Fires for each new booking imported from a booking site or created directly in Uplisting. |
| Booking Removed | `booking_removed` | Fires when a booking is cancelled or removed. |
| Booking Updated | `booking_updated` | Fires whenever any change is made to an existing booking. |
| Property Created | `property_created` | Fires when a property is added to the Uplisting account. |
| Property Removed | `property_removed` | Fires when a property is removed from the Uplisting account. |
| Property Updated | `property_updated` | Fires when an existing property is changed. |
