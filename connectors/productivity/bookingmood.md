---
description: "Bookingmood vacation-rental and booking management API (PostgREST v11.1 at https://api.bookingmood.com/v1)."
hidden: true
---

# Bookingmood

<img src="../../.gitbook/assets/connectors/lg/bookingmood.png" alt="Bookingmood logo">

Bookingmood vacation-rental and booking management API (PostgREST v11.1 at https://api.bookingmood.com/v1). Manage products, bookings, calendar events, guests/contacts, coupons, rates, availability, invoices, payments, tasks, sites, widgets and webhooks.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [bookingmood.com](https://bookingmood.com) |
| **Authentication** | Bearer token |
| **Slug** | `bookingmood` |

## Use it

Add Bookingmood from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bookingmood.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Book | `book` | Perform a booking by providing the product, interval, occupancy and form values (POST /v1/book). Returns booking_id, reference and secret; if payment_url is set the guest must be redirected there to finish. Creates a real booking. |
| Cart Checkout | `cartCheckout` | Book one or more cart items in one go (POST /v1/cart-checkout). Same rules as Book, but with an items array. Creates real bookings; redirect the guest to payment_url when set. |
| Create Contact | `createContact` | Create one contact (guest or company). organization_id and creator_id are both required: the API rejects a contact with no valid creator (409, customers_creator_fkey). Use the user_id of a member from List Members as creator_id. Any other documented contact column may also be supplied. |
| Create Coupon | `createCoupon` | Create a discount coupon code. organization_id is required by row-level security, and definition holds the PriceExpression describing the discount. |
| Create Product | `createProduct` | Create one rental product (accommodation or bookable unit). organization_id is required by row-level security. Any other documented product column may also be supplied. Returns the full created row. |
| Create Webhook | `createWebhook` | Register a webhook endpoint so Bookingmood pushes event notifications to a publicly reachable HTTPS URL. organization_id is required by row-level security. Returns the created webhook including its signing_secret. |
| Delete Contact | `deleteContact` | Permanently delete one contact, selected by its id. The id filter is mandatory so an unfiltered DELETE can never wipe the contacts table. Returns the deleted row. |
| Delete Coupon | `deleteCoupon` | Permanently delete one coupon, selected by its id. The id filter is mandatory so an unfiltered DELETE can never wipe the coupons table. |
| Delete Product | `deleteProduct` | Permanently delete one product, selected by its id. The id filter is mandatory so an unfiltered DELETE can never wipe the table. Returns the deleted row. |
| Delete Webhook | `deleteWebhook` | Unregister one webhook endpoint, selected by its id, so Bookingmood stops delivering events to it. The id filter is mandatory so an unfiltered DELETE can never remove every webhook. |

<details>

<summary>See 72 more actions</summary>

* **List Attribute options** `listAttributeOptions`: Possible options per attribute. Lists attribute options rows visible to the API key (GET /v1/attribute_options); every column can be filtered with PostgREST operators.
* **List Attributes** `listAttributes`: Attributes to segment and filter units by. Lists attributes rows visible to the API key (GET /v1/attributes); every column can be filtered with PostgREST operators.
* **List Booking details** `listBookingDetails`: Booking details as filled in by guests in the booking form. Lists booking details rows visible to the API key (GET /v1/booking_details); every column can be filtered with PostgREST operators.
* **List Booking updates** `listBookingUpdates`: Logs of each time a booking is updated. Lists booking updates rows visible to the API key (GET /v1/booking_updates); every column can be filtered with PostgREST operators.
* **List Calendar event notes** `listCalendarEventNotes`: Private notes send around some calendar event. Lists calendar event notes rows visible to the API key (GET /v1/calendar_event_notes); every column can be filtered with PostgREST operators.
* **List Calendar event updates** `listCalendarEventUpdates`: Snapshots of each time a calendar event is updated. Lists calendar event updates rows visible to the API key (GET /v1/calendar_event_updates); every column can be filtered with PostgREST operators.
* **List Calendar events** `listCalendarEvents`: Events as visible on your timeline. Can be bookings, blocked periods or notes.. Lists calendar events rows visible to the API key (GET /v1/calendar_events); every column can be filtered with PostgREST operators.
* **List Capacities** `listCapacities`: Occupancy limits per unit per occupancy group. Lists capacities rows visible to the API key (GET /v1/capacities); every column can be filtered with PostgREST operators.
* **List Capacity groups** `listCapacityGroups`: Distinct groups that can occupy units. Useful for configuring separate prices & limits for adult / children / pets.. Lists capacity groups rows visible to the API key (GET /v1/capacity_groups); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listApiRequests`: Api requests. Lists cart checkout rows visible to the API key (GET /v1/api_requests); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listBookings`: Bookings. Lists cart checkout rows visible to the API key (GET /v1/bookings); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listContacts`: Contacts. Lists cart checkout rows visible to the API key (GET /v1/contacts); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listOrganizationCalendarLogs`: Organization calendar logs. Lists cart checkout rows visible to the API key (GET /v1/organization_calendar_logs); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listOrganizations`: Organizations. Lists cart checkout rows visible to the API key (GET /v1/organizations); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listPaddlePlans`: Paddle plans. Lists cart checkout rows visible to the API key (GET /v1/paddle_plans); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listPaddleSubscriptions`: Paddle subscriptions. Lists cart checkout rows visible to the API key (GET /v1/paddle_subscriptions); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listPricelabsPricing`: Pricelabs pricing. Lists cart checkout rows visible to the API key (GET /v1/pricelabs_pricing); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listPricingWidgets`: Pricing widgets. Lists cart checkout rows visible to the API key (GET /v1/pricing_widgets); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listRefunds`: Refunds. Lists cart checkout rows visible to the API key (GET /v1/refunds); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listReviewProducts`: Review products. Lists cart checkout rows visible to the API key (GET /v1/review_products); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listReviewWidgetListings`: Review widget listings. Lists cart checkout rows visible to the API key (GET /v1/review_widget_listings); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listReviewWidgets`: Review widgets. Lists cart checkout rows visible to the API key (GET /v1/review_widgets); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listReviews`: Reviews. Lists cart checkout rows visible to the API key (GET /v1/reviews); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listTaskAssignees`: Task assignees. Lists cart checkout rows visible to the API key (GET /v1/task_assignees); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listTaskTemplateAssignees`: Task template assignees. Lists cart checkout rows visible to the API key (GET /v1/task_template_assignees); every column can be filtered with PostgREST operators.
* **List Cart checkout** `listWidgetAnalytics`: Widget analytics. Lists cart checkout rows visible to the API key (GET /v1/widget_analytics); every column can be filtered with PostgREST operators.
* **List Contact bookings** `listContactBookings`: Link between contacts and bookings. Lists contact bookings rows visible to the API key (GET /v1/contact_bookings); every column can be filtered with PostgREST operators.
* **List Coupon uses** `listCouponUses`: Coupon usage in bookings. Lists coupon uses rows visible to the API key (GET /v1/coupon_uses); every column can be filtered with PostgREST operators.
* **List Coupons** `listCoupons`: Codes guests can enter for additional discounts. Lists coupons rows visible to the API key (GET /v1/coupons); every column can be filtered with PostgREST operators.
* **List element_id** `listCapacityGroupDependencies`: .. Lists element_id rows visible to the API key (GET /v1/capacity_group_dependencies); every column can be filtered with PostgREST operators.
* **List External calendars** `listExternalCalendars`: Calendars which are being imported. Useful for syncing bookings with services like Airbnb or booking.com.. Lists external calendars rows visible to the API key (GET /v1/external_calendars); every column can be filtered with PostgREST operators.
* **List For more information on the webhook mechanics, see** `listWebhooks`: our documentation. Lists for more information on the webhook mechanics, see rows visible to the API key (GET /v1/webhooks); every column can be filtered with PostgREST operators.
* **List Invoices** `listInvoices`: Invoices for bookings. Lists invoices rows visible to the API key (GET /v1/invoices); every column can be filtered with PostgREST operators.
* **List Line item taxes** `listLineItemTaxes`: Taxes applying on line items. Lists line item taxes rows visible to the API key (GET /v1/line_item_taxes); every column can be filtered with PostgREST operators.
* **List Line items** `listLineItems`: Invoice lines for booking invoices. Lists line items rows visible to the API key (GET /v1/line_items); every column can be filtered with PostgREST operators.
* **List Members** `listMembers`: Organization members.. Lists members rows visible to the API key (GET /v1/members); every column can be filtered with PostgREST operators.
* **List Message events** `listMessageEvents`: Bounce, delivery and open events for emails. Lists message events rows visible to the API key (GET /v1/message_events); every column can be filtered with PostgREST operators.
* **List Message templates** `listMessageTemplates`: Re-usable email templates. Lists message templates rows visible to the API key (GET /v1/message_templates); every column can be filtered with PostgREST operators.
* **List Messages** `listMessages`: Emails scheduled or sent to guests. Lists messages rows visible to the API key (GET /v1/messages); every column can be filtered with PostgREST operators.
* **List Payments** `listPayments`: Booking payments. Both planned, partially paid and paid.. Lists payments rows visible to the API key (GET /v1/payments); every column can be filtered with PostgREST operators.
* **List Price calendar entries** `listPriceCalendarEntries`: Rate and availability configurations. Applied per unit on multiple intervals. Lists price calendar entries rows visible to the API key (GET /v1/price_calendar_entries); every column can be filtered with PostgREST operators.
* **List product** `listCouponProducts`: .. Lists product rows visible to the API key (GET /v1/coupon_products); every column can be filtered with PostgREST operators.
* **List Product attribute options** `listProductAttributeOptions`: Attribute options assigned to each unit. Lists product attribute options rows visible to the API key (GET /v1/product_attribute_options); every column can be filtered with PostgREST operators.
* **List Product calendar logs** `listProductCalendarLogs`: Logs for each time the ical feed of a unit is read by an external platform. Lists product calendar logs rows visible to the API key (GET /v1/product_calendar_logs); every column can be filtered with PostgREST operators.
* **List Product message templates** `listProductMessageTemplates`: Automated emails active per unit. Lists product message templates rows visible to the API key (GET /v1/product_message_templates); every column can be filtered with PostgREST operators.
* **List Product reply to addresses** `listProductReplyToAddresses`: Reply-to addresses per unit. Lists product reply to addresses rows visible to the API key (GET /v1/product_reply_to_addresses); every column can be filtered with PostgREST operators.
* **List Product services** `listProductServices`: Services included in the booking form of a unit. Lists product services rows visible to the API key (GET /v1/product_services); every column can be filtered with PostgREST operators.
* **List Products** `listProducts`: Units that can be booked individually. Lists products rows visible to the API key (GET /v1/products); every column can be filtered with PostgREST operators.
* **List Reply to addresses** `listReplyToAddresses`: Reply-to email addresses. Lists reply to addresses rows visible to the API key (GET /v1/reply_to_addresses); every column can be filtered with PostgREST operators.
* **List Seasons** `listSeasons`: Season definitions. Useful for making re-usable pricing definitions. Lists seasons rows visible to the API key (GET /v1/seasons); every column can be filtered with PostgREST operators.
* **List service** `listCouponServices`: .. Lists service rows visible to the API key (GET /v1/coupon_services); every column can be filtered with PostgREST operators.
* **List Services** `listServices`: Re-usable elements that can be included in the booking forms of units. Lists services rows visible to the API key (GET /v1/services); every column can be filtered with PostgREST operators.
* **List Site listings** `listSiteListings`: Listed units on a site. Lists site listings rows visible to the API key (GET /v1/site_listings); every column can be filtered with PostgREST operators.
* **List Site nav items** `listSiteNavItems`: Items in the navigation bar of a site. Lists site nav items rows visible to the API key (GET /v1/site_nav_items); every column can be filtered with PostgREST operators.
* **List Site pages** `listSitePages`: Additional pages on a site. Lists site pages rows visible to the API key (GET /v1/site_pages); every column can be filtered with PostgREST operators.
* **List Site views** `listSiteViews`: Logs of each pageview for a site. Lists site views rows visible to the API key (GET /v1/site_views); every column can be filtered with PostgREST operators.
* **List Sites** `listSites`: Websites, either single-unit or catalog sites.. Lists sites rows visible to the API key (GET /v1/sites); every column can be filtered with PostgREST operators.
* **List Task templates** `listTaskTemplates`: Tasks required for all bookings for a unit. Lists task templates rows visible to the API key (GET /v1/task_templates); every column can be filtered with PostgREST operators.
* **List Tasks** `listTasks`: Tasks defined per event.. Lists tasks rows visible to the API key (GET /v1/tasks); every column can be filtered with PostgREST operators.
* **List Taxes** `listTaxes`: Re-usable tax definitions. Lists taxes rows visible to the API key (GET /v1/taxes); every column can be filtered with PostgREST operators.
* **List user** `listPermissions`: role per unit.. Lists user rows visible to the API key (GET /v1/permissions); every column can be filtered with PostgREST operators.
* **List User profiles** `listUserProfiles`: User profiles. Lists user profiles rows visible to the API key (GET /v1/user_profiles); every column can be filtered with PostgREST operators.
* **List Webhook notifications** `listWebhookNotifications`: Notifications sent and scheduled per webhook. Lists webhook notifications rows visible to the API key (GET /v1/webhook_notifications); every column can be filtered with PostgREST operators.
* **List Widget listings** `listWidgetListings`: Units listed in a widget. Lists widget listings rows visible to the API key (GET /v1/widget_listings); every column can be filtered with PostgREST operators.
* **List Widgets** `listWidgets`: Embeddable widgets. Lists widgets rows visible to the API key (GET /v1/widgets); every column can be filtered with PostgREST operators.
* **Query Availability** `queryAvailability`: Fetch the availability of one or more products over a long period, as contiguous intervals with a status each. Use this to render a calendar. Returns an array of { product_id, intervals[] }.
* **Search Availability** `searchAvailability`: Find which products are available for a given date range, optionally filtered by occupancy and attribute options. Returns one result per product with match flags, availability status and a price range.
* **Update Contact** `updateContact`: Update one contact, selected by its id. The id filter is mandatory so an unfiltered PATCH is impossible. Any other documented contact column may also be supplied.
* **Update Coupon** `updateCoupon`: Update one coupon, selected by its id. The id filter is mandatory so an unfiltered PATCH is impossible. Set deleted_at to soft-delete a coupon that has already been used.
* **Update Product** `updateProduct`: Update one product, selected by its id. The id filter is mandatory so an unfiltered PATCH can never touch every product. Any other documented product column may also be supplied in the body. Returns the updated row.
* **Update Webhook** `updateWebhook`: Update one registered webhook, selected by its id - for example to change its delivery URL or its event subscription list. The id filter is mandatory so an unfiltered PATCH is impossible.
* **Validate Cart** `validateCart`: Validate a cart of items by checking availability and occupancy of each item, before booking with Cart Checkout (POST /v1/cart-validate).

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Booking Created | `bookings.created` | A booking was created. |
| Booking Updated | `bookings.updated` | A booking was updated. |
| Calendar Event Cancelled | `calendar_events.cancelled` | A calendar event was cancelled. |
| Calendar Event Confirmed | `calendar_events.confirmed` | A calendar event was confirmed. Bookingmood also emits calendar_events.updated for the same change. |
| Calendar Event Created | `calendar_events.created` | A calendar event (a stay, request or blocked period) was created. |
| Calendar Event Task Completed | `calendar_event_tasks.completed` | A task attached to a calendar event was completed. |
| Calendar Event Task Created | `calendar_event_tasks.created` | A task attached to a calendar event was created. |
| Calendar Event Task Updated | `calendar_event_tasks.updated` | A task attached to a calendar event was updated. |
| Calendar Event Updated | `calendar_events.updated` | A calendar event was updated. |
| Contact Created | `contacts.created` | A contact (guest) was created. Payload schema below was CAPTURED from a real Bookingmood delivery. |

<details>

<summary>See 14 more events</summary>

* **Contact Updated** `contacts.updated`: A contact was updated. Payload carries both the new and the old row.
* **Invoice Created** `invoices.created`: An invoice was created.
* **Invoice Updated** `invoices.updated`: An invoice was updated.
* **Member Created** `members.created`: An organization member was created.
* **Member Updated** `members.updated`: An organization member was updated.
* **Payment Created** `payments.created`: A payment was created.
* **Payment Paid** `payments.paid`: A payment was paid.
* **Payment Updated** `payments.updated`: A payment was updated. Bookingmood does not guarantee ordering against payments.paid.
* **Product Created** `products.created`: A rental product was created.
* **Product Updated** `products.updated`: A rental product was updated.
* **Site Created** `sites.created`: A booking site was created.
* **Site Updated** `sites.updated`: A booking site was updated.
* **Widget Created** `widgets.created`: A booking widget was created.
* **Widget Updated** `widgets.updated`: A booking widget was updated.

</details>
