---
description: "Ticket Tailor is a low-fee event ticketing and box office platform."
---

# Ticket Tailor

Ticket Tailor is a low-fee event ticketing and box office platform. This connector covers the Ticket Tailor API v1: event series and their event occurrences, ticket types, ticket groups, bundles and overrides, events, orders and offline payment confirmation, issued tickets and voiding, check-ins, discount codes, vouchers and voucher codes, memberships (types, issued memberships and redemptions), products and stores, checkout forms, waitlist signups, and the box office overview.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [tickettailor.com](https://tickettailor.com) |
| **Authentication** | Basic auth |
| **Actions** | 80 |
| **Events** | 8 |
| **Slug** | `ticketTailor` |

## Use it

Add Ticket Tailor from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ticketTailor.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Change Event Series Status | `changeEventSeriesStatus` | Publish an event series, return it to draft, or close its sales. |
| Confirm Order Payment Received | `confirmOrderPaymentReceived` | Mark an offline payment for an order as received, which completes the order and releases its tickets. Use this for bank transfer, cash or other payments taken outside Ticket Tailor. |
| Create Bundle | `createEventSeriesBundle` | Create a bundle on an event series: a fixed set of tickets sold together for one price. Each call adds one ticket type and its quantity to the bundle. |
| Create Check-In | `createCheckIn` | Check an issued ticket in or out at the door. Send quantity 1 to check in and -1 to check out. Supply a Local Unique ID to make retries safe so the same scan is not recorded twice. |
| Create Discount | `createDiscountCode` | Create a discount code buyers can apply at checkout, as either a fixed amount off or a percentage. Restrict it to a ticket type or product, cap how many times it can be redeemed, and give it an expiry date. |
| Create Event Occurrence | `createEventSeriesEvent` | Add an event occurrence (one date) to an event series. Dates are YYYY-MM-DD and times are HH:MM in the series timezone. |
| Create Event Series | `createEventSeries` | Create an event series, the container that holds one or more event occurrences along with their ticket types, groups and bundles. New series start as a draft; publish them with Change Event Series Status. |
| Create Event Series Override | `createEventSeriesOverride` | Create an override on an event series so one ticket type, ticket group or bundle is sold at a different price, quantity or status than its default. Each call sets one override line; create additional overrides for additional lines. |
| Create Hold | `createHold` | Hold back tickets of one ticket type on an event occurrence so they are removed from public sale and can be issued later. Each call holds one ticket type; create additional holds for additional ticket types. |
| Create Issued Membership | `createIssuedMembership` | Issue a membership to a named member from an existing membership type. Validity dates and redemption limits default to the membership type's settings unless you override them. Member photos must be uploaded in the Ticket Tailor dashboard. |
| Create Issued Membership Redemption | `createIssuedMembershipRedemption` | Redeem a membership at an event, recording that the member used it for entry. The redemption counts towards the membership's redemption limit. |
| Create Issued Ticket | `createIssuedTicket` | Issue a ticket directly from an event's inventory or from a hold, without going through checkout. Supply event_id and ticket_type_id to issue from ticket type inventory, or hold_id to issue from a hold. Ticket Tailor charges one credit per ticket issued through the API, even when the ticket is free. |
| Create Membership Type | `createMembershipType` | Create a membership type: the template that issued memberships are created from, defining how long they last, how many times they can be redeemed and what benefits they carry. |
| Create Product | `createProduct` | Create a product sold alongside tickets, such as merchandise, a membership or a gift card. Link it to an event series or to every series, and optionally have it fulfil a membership type or gift card voucher. Product images must be uploaded in the Ticket Tailor dashboard. |
| Create Ticket Group | `createTicketGroupForEventSeries` | Create a ticket group on an event series so several ticket types and bundles are sold together under one heading with shared order limits. One ticket type and one bundle can be attached per call; add further members with Update Ticket Group. |
| Create Ticket Type | `createTicketTypeForEventSeries` | Create a ticket type on an event series. Prices and booking fees are in the smallest currency unit, so 1000 is 10.00. Set price to 0 for a free ticket. |
| Create Voucher | `createVoucher` | Create a promotional voucher or gift card, optionally with its first redeemable code. Promotional vouchers use codes you supply; gift cards expire a fixed number of days after they are issued. |
| Delete Bundle | `deleteEventSeriesBundle` | Permanently delete a bundle from an event series. This cannot be undone. The ticket types and products the bundle contained are not themselves deleted. |
| Delete Discount | `deleteDiscountById` | Permanently delete a discount code so it can no longer be redeemed at checkout. This cannot be undone. |
| Delete Event Occurrence | `deleteEventOccurrenceById` | Permanently delete an event occurrence. Only possible when the occurrence has no orders against it; otherwise hide it with Update Event Occurrence instead. |
| Delete Event Series | `deleteEventSeriesById` | Permanently delete an event series and every event occurrence in it. This cannot be undone. |
| Delete Hold | `deleteHoldById` | Permanently delete a ticket hold, returning the held tickets to general sale. This cannot be undone. |
| Delete Membership Type | `deleteMembershipTypeById` | Permanently delete a membership type. Only possible when it has no issued memberships and no products linked to it. |
| Delete Product | `deleteProductById` | Permanently delete a product so it can no longer be sold. This cannot be undone. |
| Delete Ticket Group | `deleteTicketGroupById` | Permanently delete a ticket group. Ticket types and bundles inside it are removed from the group but are not themselves deleted. |
| Delete Ticket Type | `deleteTicketTypeById` | Permanently delete a ticket type from an event series. This cannot be undone. |
| Delete Voucher | `deleteVoucherById` | Permanently delete a voucher and every code that belongs to it. This cannot be undone. |
| Delete Waiting List Sign-Up | `deleteEventSeriesWaitlistSignup` | Permanently remove one sign-up from an event series waiting list. This cannot be undone. |
| List Check-Ins | `getCheckInList` | List the check-in and check-out records recorded on the door. Filter by event, event series, issued ticket, check-in time or creation time. Results are cursor paginated. |
| List Checkout Form Elements | `getCheckoutFormElements` | List the questions and terms elements that make up one checkout form, including their type, answer options and whether each is asked once per order or once per ticket. |
| List Checkout Forms | `getCheckoutFormList` | List the checkout forms configured on the box office, with the event series each one is attached to and the identifiers of its form elements. |
| List Discounts | `getDiscountList` | List the discount codes set up in the box office, optionally narrowed to a single code. Results are cursor paginated. |
| List Event Occurrences | `getAllEventOccurrences` | List the event occurrences (individual dates) inside one event series, filtered by start or end time. |
| List Event Series | `getAllEventSeries` | List the event series in the box office. Filter by status, name, venue or creation time. Results are cursor paginated. |
| List Event Series Overrides | `getEventSeriesOverrideList` | List the overrides defined on an event series. Filter by the ticket type or ticket group an override references, by reference type, by status or by creation time. Results are cursor paginated. |
| List Events | `getAllEvents` | List every event occurrence in the box office across all series. Filter by status, name, venue or start and end time. |
| List Holds | `getHoldList` | List the ticket holds in the box office. Filter by event occurrence, creation time or last update time. Results are cursor paginated. |
| List Issued Memberships | `getAllIssuedMemberships` | List the memberships issued by the box office. Filter by member name, email, membership code, validity status, issue date or validity window, and order the results by member name. Results are cursor paginated. |
| List Issued Tickets | `getAllIssuedTickets` | List the tickets issued by the box office. Filter by event, event series, order, barcode, attendee name or email, external reference, status or creation time. Results are cursor paginated. |
| List Membership Types | `getAllMembershipTypes` | List the membership types set up in the box office, with their validity rules, redemption limits and benefits. Results are cursor paginated. |
| List Orders | `getAllOrders` | List the orders placed with the box office. Filter by buyer name or email, transaction id, ticket barcode, event, event series, store, referral tag, status or creation time. Results are cursor paginated. |
| List Products | `getProductList` | List the products sold by the box office. Filter by event series, creation time or last update time. Results are cursor paginated. |
| List Stores | `getStoreList` | List the stores configured on the box office, with the currency, payment methods and products each one sells. |
| List Voucher Codes | `getVoucherCodeList` | List the individual redeemable codes belonging to a voucher, with their value and whether they have been used. Filter by expiry or creation time. Results are cursor paginated. |
| List Vouchers | `getVoucherList` | List the vouchers and gift cards in the box office. Filter by expiry date or creation time. Results are cursor paginated. |
| List Waiting List Sign-Ups | `getEventSeriesWaitlistList` | List the waiting list sign-ups recorded against an event series. Filter by email, by the events they signed up for, by whether they have been notified, or by sign-up time. Results are cursor paginated. |
| Ping | `ping` | Check that the Ticket Tailor API is reachable and that the connected API key is valid. Returns the API version. |
| Retrieve Box Office Overview | `getOverview` | Retrieve headline statistics for the connected box office: revenue, orders received, tickets issued, waiting list sign-ups, draft and published event counts, credit balance and climate contribution. |
| Retrieve Checkout Form Element | `getCheckoutFormElementById` | Retrieve a single question or terms element from a checkout form, including its type, answer options and whether it is required. |
| Retrieve Discount | `getDiscountById` | Retrieve a single discount by its identifier, including its code, value, expiry, redemption count and the ticket types or products it is restricted to. |
| Retrieve Event | `getEventById` | Retrieve a single event occurrence in the box office by its identifier, including its ticket types and sales totals. |
| Retrieve Event Occurrence | `getEventOccurrenceById` | Retrieve a single event occurrence inside an event series. |
| Retrieve Event Series | `getEventSeriesById` | Retrieve a single event series by its identifier, including its default ticket types, ticket groups, bundles and sales totals. |
| Retrieve Hold | `getHoldById` | Retrieve a single ticket hold by its identifier, including the event it applies to and the held quantity for each ticket type. |
| Retrieve Issued Membership | `getIssuedMembershipById` | Retrieve a single issued membership by its identifier, including the member's details, validity window, benefits and the redemptions recorded against it. |
| Retrieve Issued Ticket | `getIssuedTicketById` | Retrieve a single issued ticket by its identifier, including its barcode, attendee details, check-in state and the order it belongs to. |
| Retrieve Membership Photo Link | `getMembershipPhotoShare` | Get a temporary signed URL for a member's photo so it can be shown on a door-scanning screen. The link expires after a short period. |
| Retrieve Membership Type | `getMembershipTypeById` | Retrieve a single membership type by its identifier, including its validity rules, redemption limit, benefits and whether a member photo is required. |
| Retrieve Order | `getOrderById` | Retrieve a single order belonging to the box office, including buyer details, issued tickets, sold products, line items and payment information. |
| Retrieve Product | `getProductById` | Retrieve a single product by its identifier, including its price, availability, sales status and any membership type or gift card it fulfils. |
| Retrieve Store | `getStoreById` | Retrieve a single store's configuration, including its name, currency, payment methods and the products it sells. |
| Retrieve Voucher | `getVoucherById` | Retrieve a single voucher or gift card by its identifier, including its value, expiry, redemption rules and how many of its codes remain unused. |
| Update Bundle | `updateEventSeriesBundle` | Update a bundle's name, description, price, booking fee, access code or sales status. Only the fields you supply are changed. The ticket types and products inside a bundle are set when it is created and cannot be changed by this action; recreate the bundle to change its contents. |
| Update Checkout Form Element | `updateCheckoutFormElementById` | Update a question or terms element on a checkout form: its wording, type, answer option, whether it is required and whether it is asked once per order or once per ticket. Only the fields you supply are changed. |
| Update Discount | `updateDiscountById` | Update a discount's name, code, value, expiry or redemption limit. Only the fields you supply are changed. The ticket types and products a discount is restricted to are set when it is created and cannot be changed by this action. |
| Update Event Occurrence | `updateEventOccurrenceById` | Change the dates, visibility or availability of an event occurrence. Only the fields you supply are changed. |
| Update Event Series | `updateEventSeriesById` | Update an existing event series. Only the fields you supply are changed. Voucher associations are sent as a map of voucher id to \"1\" to attach or \"0\" to detach. |
| Update Event Series Override | `updateEventSeriesOverride` | Replace an override's name, ticket cap and override line. All fields are sent on every call, so supply the current values for anything you do not want to change. |
| Update Hold | `updateHold` | Replace the note and held quantity on an existing hold. Both values are sent on every call, so supply the current note if you only want to change the quantity. |
| Update Issued Membership | `updateIssuedMembershipById` | Update the member details, validity dates or redemption limit on an issued membership. Only the fields you supply are changed, and only fixed validity dates may be set here. Member photos must be uploaded in the Ticket Tailor dashboard. |
| Update Membership Type | `updateMembershipTypeById` | Update a membership type's name, validity rules, redemption limit, benefits or photo requirement. Only the fields you supply are changed. |
| Update Order | `updateOrderById` | Update the buyer contact and address details recorded against an order. Only the fields you supply are changed; the tickets and payment on the order are not affected. |
| Update Product | `updateProductById` | Update a product's name, price, description, availability or sales status. Only the fields you supply are changed. Use Modify Quantity to add or remove stock relative to the current level. The event series a product is linked to are set when it is created and cannot be changed by this action, and product images must be uploaded in the Ticket Tailor dashboard. |
| Update Store | `updateStoreById` | Update a store's name, currency or the products it sells. Only the fields you supply are changed. Sending a Product ID replaces the store's product list with that product; send Clear Products as an empty value to remove every product from the store. |
| Update Ticket Group | `updateTicketGroupById` | Update a ticket group's name, membership or order limits. Only the fields you supply are changed. One ticket type and one bundle can be set per call, and a group that contains a bundle cannot also carry order limits. |
| Update Ticket Type | `updateTicketTypeById` | Update a ticket type on an event series. Only the fields you supply are changed. Discount associations are sent as a map of discount id to \"1\" to attach or \"0\" to detach. |
| Update Voucher | `updateVoucherById` | Update a voucher's name, value, expiry or redemption rules, and optionally add a new redeemable code to it. Only the fields you supply are changed. The event series a voucher is tied to are set when it is created and cannot be changed by this action. |
| Void Issued Membership | `voidIssuedMembershipById` | Void an issued membership so it can no longer be redeemed. This cannot be undone. |
| Void Issued Ticket | `voidIssuedTicketById` | Mark an issued ticket as voided so it is no longer valid for entry. This is irreversible, and it does not cancel the rest of the order or issue a refund. Set Void To Hold to convert the voided ticket into a hold instead of releasing it. |
| Void Voucher Code | `voidVoucherCodeById` | Mark a single voucher code as voided so it can no longer be redeemed. This is irreversible and does not affect the other codes on the same voucher. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Event Created | `EVENT.CREATED` | Fires when a new event occurrence is created in the box office. Register it in Ticket Tailor: Settings &gt; Webhooks &gt; Add webhook, paste the fastn trigger URL, tick Event created, then Save. Payload schema modelled from Ticket Tailor's published webhook sample, not from a captured delivery. |
| Event Deleted | `EVENT.DELETED` | Fires when an event occurrence is deleted. Register it in Ticket Tailor: Settings &gt; Webhooks &gt; Add webhook, paste the fastn trigger URL, tick Event deleted, then Save. Payload schema modelled from Ticket Tailor's published webhook sample, not from a captured delivery. |
| Event Updated | `EVENT.UPDATED` | Fires when an existing event occurrence is changed. Register it in Ticket Tailor: Settings &gt; Webhooks &gt; Add webhook, paste the fastn trigger URL, tick Event updated, then Save. Payload schema modelled from Ticket Tailor's published webhook sample, not from a captured delivery. |
| Issued Ticket Created | `ISSUED_TICKET.CREATED` | Fires when a ticket is issued, whether through checkout or the API. Register it in Ticket Tailor: Settings &gt; Webhooks &gt; Add webhook, paste the fastn trigger URL, tick Issued ticket created, then Save. Payload schema modelled from Ticket Tailor's published webhook sample, not from a captured delivery. |
| Issued Ticket Updated | `ISSUED_TICKET.UPDATED` | Fires when an issued ticket changes, for example when it is checked in or voided. Register it in Ticket Tailor: Settings &gt; Webhooks &gt; Add webhook, paste the fastn trigger URL, tick Issued ticket updated, then Save. Payload schema modelled from Ticket Tailor's published webhook sample, not from a captured delivery. |
| Order Created | `ORDER.CREATED` | Fires when a buyer completes a new order. Register it in Ticket Tailor: Settings &gt; Webhooks &gt; Add webhook, paste the fastn trigger URL, tick Order created, then Save. Payload schema modelled from Ticket Tailor's published webhook sample, not from a captured delivery. |
| Order Updated | `ORDER.UPDATED` | Fires when an existing order changes, for example a refund or a buyer detail edit. Register it in Ticket Tailor: Settings &gt; Webhooks &gt; Add webhook, paste the fastn trigger URL, tick Order updated, then Save. Payload schema modelled from Ticket Tailor's published webhook sample, not from a captured delivery. |
| Waiting List Sign-Up Created | `WAITLIST_SIGNUP.CREATED` | Fires when someone joins the waiting list for an event. Register it in Ticket Tailor: Settings &gt; Webhooks &gt; Add webhook, paste the fastn trigger URL, tick Waitlist signup created, then Save. Payload schema modelled from Ticket Tailor's published webhook sample, not from a captured delivery. |
