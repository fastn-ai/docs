---
description: "Planyo online booking / reservation system."
hidden: true
---

# Planyo Online Booking

<img src="../../.gitbook/assets/connectors/lg/planyo-online-booking.png" alt="Planyo Online Booking logo">

Planyo online booking / reservation system. Single-URL RPC REST API at https://www.planyo.com/rest/ where every operation is ?method=&lt;name&gt;&api_key=&lt;key&gt;. HTTP status is always 200; success is indicated by response_code:0 in the body.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [planyo.com](https://planyo.com) |
| **Authentication** | API key |
| **Slug** | `planyoOnlineBooking` |

## Use it

Add Planyo Online Booking from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.planyoOnlineBooking.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Additional Product | `addAdditionalProduct` | [Additional products] RPC add_additional_product. Adds a new additional product to your Planyo site. Docs: https://www.planyo.com/api.php?topic=add_additional_product |
| Add Agent | `addAgent` | [Users] RPC add_agent. Adds a new agent to a site. Docs: https://www.planyo.com/api.php?topic=add_agent |
| Add Coupon Type | `addCouponType` | [Coupons and vouchers] RPC add_coupon_type. Adds a new coupon type (coupon definition). Docs: https://www.planyo.com/api.php?topic=add_coupon_type |
| Add Custom Product | `addCustomProduct` | [Additional products] RPC add_custom_product. Adds a new custom product to a reservation. Docs: https://www.planyo.com/api.php?topic=add_custom_product |
| Add Custom Property Definition | `addCustomPropertyDefinition` | [Sites/Users/Resources] RPC add_custom_property_definition. Adds a new custom property definition to your site or metasite. Docs: https://www.planyo.com/api.php?topic=add_custom_property_definition |
| Add Notification Callback | `addNotificationCallback` | [Notifications] RPC add_notification_callback. Registers a webhook URL for a Planyo notification event (same as Site settings / Notifications). Append &ppp_payload=json to callback_url for JSON instead of POST form fields. An empty callback_url removes ALL webhooks for that event. 30 accepted notification_name values (verified live): new_verified_reservation, reservation_confirmed, reservation_admin_canceled, reservation_user_canceled, reservation_admin_modified, reservation_user_modified, reservation_auto_canceled, reservation_removed, reservation_price_updated, reservation_payment_received, reservation_payment_removed, reservation_products_user_modified, new_price_quotation, confirmed_cleared, checked_in, checked_out, noshow, added_to_waitlist, vacation_modified, resource_settings_changed, resource_removed, user_updated, coupon_payment_received, hourly, before_or_after_event_1..6. Docs: https://www.planyo.com/faq.php?q=222 |
| Add Notification Message | `addNotificationMessage` | [Notifications] RPC add_notification_message. Adds a site notification email message template. Docs: https://www.planyo.com/api.php?topic=add_notification_message |
| Add Pricing Manager Rule | `addPricingManagerRule` | [Prices] RPC add_pricing_manager_rule. Adds a new rule to Pricing Manager. Docs: https://www.planyo.com/api.php?topic=add_pricing_manager_rule |
| Add Product Image | `addProductImage` | [Additional products] RPC add_product_image. Adds an image to an additional product. Docs: https://www.planyo.com/api.php?topic=add_product_image |
| Add Recurring Vacation | `addRecurringVacation` | [Availability] RPC add_recurring_vacation. Adds a recurring vacation (blocked period) for a resource or the whole site. Docs: https://www.planyo.com/api.php?topic=add_recurring_vacation |

<details>

<summary>See 126 more actions</summary>

* **Add Reservation Payment** `addReservationPayment`: [Reservations] RPC add_reservation_payment. Adds a payment record for a reservation. Never pass credit card numbers. Docs: https://www.planyo.com/api.php?topic=add_reservation_payment
* **Add Resource** `addResource`: [Resources] RPC add_resource. Adds a new resource by copying an existing base resource. Docs: https://www.planyo.com/api.php?topic=add_resource
* **Add Resource Image** `addResourceImage`: [Resources] RPC add_resource_image. Adds an image to a resource. Docs: https://www.planyo.com/api.php?topic=add_resource_image
* **Add Resource Season** `addResourceSeason`: [Seasons] RPC add_resource_season. Adds a new season for a resource or the entire Planyo site. Docs: https://www.planyo.com/api.php?topic=add_resource_season
* **Add Site** `addSite`: [Sites] RPC add_site. Adds a new site to your metasite by copying a base site. METASITE API KEYS ONLY. Planyo has no remove_site method, so a created site cannot be deleted through the API. Docs: https://www.planyo.com/api.php?topic=add_site
* **Add Site Image** `addSiteImage`: [Sites] RPC add_site_image. Adds an image to your site. Docs: https://www.planyo.com/api.php?topic=add_site_image
* **Add Site Moderator** `addSiteModerator`: [Users/Sites] RPC add_site_moderator. Adds a new moderator to a site. Docs: https://www.planyo.com/api.php?topic=add_site_moderator
* **Add Url To Admin Favorites** `addUrlToAdminFavorites`: [Sites] RPC add_url_to_admin_favorites. Adds a favorite backend page for site moderators/admins. Docs: https://www.planyo.com/api.php?topic=add_url_to_admin_favorites
* **Add User** `addUser`: [Users] RPC add_user. Inserts a new user associated with your Planyo site. Docs: https://www.planyo.com/api.php?topic=add_user
* **Add Vacation** `addVacation`: [Availability] RPC add_vacation. Adds a one-time vacation (blocked period) for a resource or the whole site. Docs: https://www.planyo.com/api.php?topic=add_vacation
* **Api Test** `apiTest`: [Diagnostics] RPC api_test. Connectivity/credential check; returns "API Test Response" with response_code 0. Undocumented in the method index but live and referenced in the Planyo API authentication section.
* **Apply Coupon** `applyCoupon`: [Coupons and vouchers] RPC apply_coupon. Applies a coupon to an existing reservation. Docs: https://www.planyo.com/api.php?topic=apply_coupon
* **Apply Voucher** `applyVoucher`: [Coupons and vouchers] RPC apply_voucher. Applies a voucher to an existing reservation. Docs: https://www.planyo.com/api.php?topic=apply_voucher
* **Can Make Reservation** `canMakeReservation`: [Availability/Reservations] RPC can_make_reservation. Returns whether a reservation can be made for the given resource and period. Docs: https://www.planyo.com/api.php?topic=can_make_reservation
* **Create Cart** `createCart`: [Shopping cart] RPC create_cart. Creates a new shopping cart. Docs: https://www.planyo.com/api.php?topic=create_cart
* **Create Voucher** `createVoucher`: [Coupons and vouchers] RPC create_voucher. Creates a new voucher (discount code). Docs: https://www.planyo.com/api.php?topic=create_voucher
* **Delete Cart** `deleteCart`: [Shopping cart] RPC delete_cart. Deletes an (empty) shopping cart. Docs: https://www.planyo.com/api.php?topic=delete_cart
* **Delete Custom Property** `deleteCustomProperty`: [Custom properties] RPC delete_custom_property. Deletes a custom property by name for a site, resource, user or reservation. Docs: https://www.planyo.com/api.php?topic=delete_custom_property
* **Delete Reservation** `deleteReservation`: [Reservations] RPC delete_reservation. Permanently deletes a reservation (cannot be undone). To only cancel, use do_reservation_action. Docs: https://www.planyo.com/api.php?topic=delete_reservation
* **Delete Unit Property** `deleteUnitProperty`: [Resource units] RPC delete_unit_property. Deletes a custom unit property previously set for a date/time. Docs: https://www.planyo.com/api.php?topic=delete_unit_property
* **Do Reservation Action** `doReservationAction`: [Reservations] RPC do_reservation_action. Performs an administrative action on a reservation (confirm, cancel, etc). Use is_quiet=true to suppress customer notification emails. Docs: https://www.planyo.com/api.php?topic=do_reservation_action
* **Generate Coupon** `generateCoupon`: [Coupons and vouchers] RPC generate_coupon. Adds a new coupon to your site from an existing coupon type. Docs: https://www.planyo.com/api.php?topic=generate_coupon
* **Generate Coupon Payment Request** `generateCouponPaymentRequest`: [Coupons and vouchers] RPC generate_coupon_payment_request. Adds a new coupon and returns a payment request URL for it. Docs: https://www.planyo.com/api.php?topic=generate_coupon_payment_request
* **Generate Invoice** `generateInvoice`: [Invoices] RPC generate_invoice. Generates a new invoice for a reservation if one does not exist. Docs: https://www.planyo.com/api.php?topic=generate_invoice
* **Get Bundle Contents** `getBundleContents`: [Resources] RPC get_bundle_contents. Returns the resources and coupons included in a bundle resource. Docs: https://www.planyo.com/api.php?topic=get_bundle_contents
* **Get Cart Items** `getCartItems`: [Shopping cart] RPC get_cart_items. Lists reservations included in a shopping cart. Docs: https://www.planyo.com/api.php?topic=get_cart_items
* **Get Custom Property** `getCustomProperty`: [Custom properties] RPC get_custom_property. Returns the value of a custom property for a site, resource, user or reservation. Docs: https://www.planyo.com/api.php?topic=get_custom_property
* **Get Custom Property Definition** `getCustomPropertyDefinition`: [Custom properties] RPC get_custom_property_definition. Retrieves details of a custom property definition. Docs: https://www.planyo.com/api.php?topic=get_custom_property_definition
* **Get Event Times** `getEventTimes`: [Resources] RPC get_event_times. Lists all event times of an event-type resource. Docs: https://www.planyo.com/api.php?topic=get_event_times
* **Get Form Items** `getFormItems`: [Sites/Resources] RPC get_form_items. Returns reservation form items for a resource or the whole site. Docs: https://www.planyo.com/api.php?topic=get_form_items
* **Get Ical Feed Url** `getIcalFeedUrl`: [Sites/Resources] RPC get_ical_feed_url. Returns the URL of an iCal feed for a metasite, site, resource or unit. Docs: https://www.planyo.com/api.php?topic=get_ical_feed_url
* **Get Invoice Items** `getInvoiceItems`: [Invoices] RPC get_invoice_items. Returns all invoice items (products) for a reservation. Docs: https://www.planyo.com/api.php?topic=get_invoice_items
* **Get Package Contents** `getPackageContents`: [Resources] RPC get_package_contents. Returns detailed information about a package resource. Docs: https://www.planyo.com/api.php?topic=get_package_contents
* **Get Pricing Manager Rules** `getPricingManagerRules`: [Prices] RPC get_pricing_manager_rules. Lists Pricing Manager rules. Docs: https://www.planyo.com/api.php?topic=get_pricing_manager_rules
* **Get Promotable Reservations** `getPromotableReservations`: [Reservations] RPC get_promotable_reservations. Lists waiting-list requests that can be promoted to a valid reservation. Docs: https://www.planyo.com/api.php?topic=get_promotable_reservations
* **Get Rental Price** `getRentalPrice`: [Prices] RPC get_rental_price. Returns the price of a rental for a resource and start/end times. Docs: https://www.planyo.com/api.php?topic=get_rental_price
* **Get Reservation Actions** `getReservationActions`: [Reservations] RPC get_reservation_actions. Lists reservation actions (events) such as modifications and status changes. Docs: https://www.planyo.com/api.php?topic=get_reservation_actions
* **Get Reservation Data** `getReservationData`: [Reservations] RPC get_reservation_data. Returns details of a reservation. Docs: https://www.planyo.com/api.php?topic=get_reservation_data
* **Get Reservation Payment Amount** `getReservationPaymentAmount`: [Reservations] RPC get_reservation_payment_amount. Returns payment information (total amount paid) for a reservation. Docs: https://www.planyo.com/api.php?topic=get_reservation_payment_amount
* **Get Reservation Products** `getReservationProducts`: [Additional products] RPC get_reservation_products. Returns the additional products attached to a reservation. Docs: https://www.planyo.com/api.php?topic=get_reservation_products
* **Get Resource Info** `getResourceInfo`: [Resources] RPC get_resource_info. Returns information for a resource, including photos and resource-specific properties. Docs: https://www.planyo.com/api.php?topic=get_resource_info
* **Get Resource Pricing** `getResourcePricing`: [Prices/Resources] RPC get_resource_pricing. Returns complete pricing information for resources of a site. Docs: https://www.planyo.com/api.php?topic=get_resource_pricing
* **Get Resource Seasons** `getResourceSeasons`: [Seasons] RPC get_resource_seasons. Returns seasonal settings for a resource (pass 0 for site-wide seasons). Docs: https://www.planyo.com/api.php?topic=get_resource_seasons
* **Get Resource Usage** `getResourceUsage`: [Availability] RPC get_resource_usage. Returns usage/availability information of a resource over a period. Docs: https://www.planyo.com/api.php?topic=get_resource_usage
* **Get Resource Usage For Month** `getResourceUsageForMonth`: [Availability] RPC get_resource_usage_for_month. Returns usage/availability information of a resource for a given month. Docs: https://www.planyo.com/api.php?topic=get_resource_usage_for_month
* **Get Simplified Daily Pricing** `getSimplifiedDailyPricing`: [Prices] RPC get_simplified_daily_pricing. Returns daily prices for day-based resources over a period. Docs: https://www.planyo.com/api.php?topic=get_simplified_daily_pricing
* **Get Simplified Daily Restrictions** `getSimplifiedDailyRestrictions`: [Resources] RPC get_simplified_daily_restrictions. Returns daily restrictions for day-based resources over a period. Docs: https://www.planyo.com/api.php?topic=get_simplified_daily_restrictions
* **Get Site Info** `getSiteInfo`: Returns information for the Planyo site, including photos and site-specific properties. RPC method get_site_info. Success = response_code 0.
* **Get Unit Property** `getUnitProperty`: [Resource units] RPC get_unit_property. Returns the value of a custom unit property. Docs: https://www.planyo.com/api.php?topic=get_unit_property
* **Get User Data** `getUserData`: [Users] RPC get_user_data. Returns details of a user by user_id or email. Docs: https://www.planyo.com/api.php?topic=get_user_data
* **Get Weekly Schedule** `getWeeklySchedule`: [Availability] RPC get_weekly_schedule. Lists all weekly vacations (or available times) of a resource. Docs: https://www.planyo.com/api.php?topic=get_weekly_schedule
* **Is Resource Available** `isResourceAvailable`: [Availability] RPC is_resource_available. Returns resource availability for a given time period. Docs: https://www.planyo.com/api.php?topic=is_resource_available
* **List Additional Products** `listAdditionalProducts`: [Additional products] RPC list_additional_products. Returns additional products defined in a Planyo site. Docs: https://www.planyo.com/api.php?topic=list_additional_products
* **List Cart Payments** `listCartPayments`: [Shopping cart] RPC list_cart_payments. Lists payments made for all reservations of a shopping cart. Docs: https://www.planyo.com/api.php?topic=list_cart_payments
* **List Carts** `listCarts`: [Shopping cart] RPC list_carts. Lists shopping carts for a site or metasite. Docs: https://www.planyo.com/api.php?topic=list_carts
* **List Coupon Payments** `listCouponPayments`: [Coupons and vouchers] RPC list_coupon_payments. Lists coupon payments. Docs: https://www.planyo.com/api.php?topic=list_coupon_payments
* **List Coupon Types** `listCouponTypes`: [Coupons and vouchers] RPC list_coupon_types. Lists coupon definitions that can be purchased. Docs: https://www.planyo.com/api.php?topic=list_coupon_types
* **List Coupons** `listCoupons`: [Coupons and vouchers] RPC list_coupons. Lists purchased coupons, optionally filtered. Docs: https://www.planyo.com/api.php?topic=list_coupons
* **List Custom User Properties** `listCustomUserProperties`: [Users] RPC list_custom_user_properties. Returns custom user property definitions for a site. Docs: https://www.planyo.com/api.php?topic=list_custom_user_properties
* **List Invoices** `listInvoices`: [Invoices] RPC list_invoices. Lists invoices for a reservation or generated in a given period. Docs: https://www.planyo.com/api.php?topic=list_invoices
* **List Payments** `listPayments`: [Reservations] RPC list_payments. Lists payments made for your reservations in a date range. Docs: https://www.planyo.com/api.php?topic=list_payments
* **List Reservation Payments** `listReservationPayments`: [Reservations] RPC list_reservation_payments. Lists payments made for a reservation, including coupon usage. Docs: https://www.planyo.com/api.php?topic=list_reservation_payments
* **List Reservations** `listReservations`: [Reservations] RPC list_reservations. Lists reservations starting within a time period (or created in it). Docs: https://www.planyo.com/api.php?topic=list_reservations
* **List Resources** `listResources`: [Resources] RPC list_resources. Returns resources defined in a Planyo site or metasite. Docs: https://www.planyo.com/api.php?topic=list_resources
* **List Reviews** `listReviews`: [Sites] RPC list_reviews. Lists the reviews added by clients. Docs: https://www.planyo.com/api.php?topic=list_reviews
* **List Site Moderators** `listSiteModerators`: [Users] RPC list_site_moderators. Returns all moderators of a Planyo site. Docs: https://www.planyo.com/api.php?topic=list_site_moderators
* **List Sites** `listSites`: [Sites] RPC list_sites. Returns sites defined in a Planyo metasite. Docs: https://www.planyo.com/api.php?topic=list_sites
* **List Translations** `listTranslations`: [Translations] RPC list_translations. Lists user-defined translations for a metasite, site or resource. Docs: https://www.planyo.com/api.php?topic=list_translations
* **List Users** `listUsers`: [Users] RPC list_users. Returns users with at least one reservation (or admin-created users). Docs: https://www.planyo.com/api.php?topic=list_users
* **List Vacations** `listVacations`: [Availability] RPC list_vacations. Lists all vacations within a time range. Docs: https://www.planyo.com/api.php?topic=list_vacations
* **List Vouchers** `listVouchers`: [Coupons and vouchers] RPC list_vouchers. Lists vouchers, optionally filtered. Docs: https://www.planyo.com/api.php?topic=list_vouchers
* **Make Reservation** `makeReservation`: [Reservations] RPC make_reservation. Enters a new reservation; returns reservation_id. IMPORTANT: send_notifications defaults to TRUE and emails the customer - pass send_notifications=false to suppress. Docs: https://www.planyo.com/api.php?topic=make_reservation
* **Modify Additional Product** `modifyAdditionalProduct`: [Additional products] RPC modify_additional_product. Modifies an existing additional product. Docs: https://www.planyo.com/api.php?topic=modify_additional_product
* **Modify Coupon** `modifyCoupon`: [Coupons and vouchers] RPC modify_coupon. Modifies an existing coupon. Docs: https://www.planyo.com/api.php?topic=modify_coupon
* **Modify Reservation** `modifyReservation`: [Reservations] RPC modify_reservation. Modifies an existing reservation. Pass send_notifications=false to suppress customer emails. Docs: https://www.planyo.com/api.php?topic=modify_reservation
* **Modify Reservation Payment** `modifyReservationPayment`: [Reservations] RPC modify_reservation_payment. Changes the status of a reservation payment. Docs: https://www.planyo.com/api.php?topic=modify_reservation_payment
* **Modify Resource** `modifyResource`: [Resources] RPC modify_resource. Modifies an existing resource; only the fields you pass are changed. Docs: https://www.planyo.com/api.php?topic=modify_resource
* **Modify Resource Season** `modifyResourceSeason`: [Seasons] RPC modify_resource_season. Modifies an existing season. Docs: https://www.planyo.com/api.php?topic=modify_resource_season
* **Modify Site** `modifySite`: [Sites] RPC modify_site. Modifies an existing site; only the fields you pass are changed. Docs: https://www.planyo.com/api.php?topic=modify_site
* **Modify User** `modifyUser`: [Users] RPC modify_user. Modifies an existing user's data; identify by user_id, email or user_login. Docs: https://www.planyo.com/api.php?topic=modify_user
* **Modify Voucher** `modifyVoucher`: [Coupons and vouchers] RPC modify_voucher. Modifies an existing voucher. Docs: https://www.planyo.com/api.php?topic=modify_voucher
* **Move Reservations To Cart** `moveReservationsToCart`: [Shopping cart] RPC move_reservations_to_cart. Moves reservations into a new or existing shopping cart. Docs: https://www.planyo.com/api.php?topic=move_reservations_to_cart
* **Process Template** `processTemplate`: [Templates] RPC process_template. Processes a Planyo template in the context of a reservation, resource or site. Docs: https://www.planyo.com/api.php?topic=process_template
* **Recalculate Price** `recalculatePrice`: [Prices] RPC recalculate_price. Recalculates the price of an existing reservation. Docs: https://www.planyo.com/api.php?topic=recalculate_price
* **Remove Additional Product** `removeAdditionalProduct`: [Additional products] RPC remove_additional_product. Removes an existing additional product. Docs: https://www.planyo.com/api.php?topic=remove_additional_product
* **Remove Coupon** `removeCoupon`: [Coupons and vouchers] RPC remove_coupon. Removes a coupon. Docs: https://www.planyo.com/api.php?topic=remove_coupon
* **Remove Coupon Type** `removeCouponType`: [Coupons and vouchers] RPC remove_coupon_type. Removes a coupon type. Docs: https://www.planyo.com/api.php?topic=remove_coupon_type
* **Remove Custom Product** `removeCustomProduct`: [Additional products] RPC remove_custom_product. Removes an existing custom product from a reservation. Docs: https://www.planyo.com/api.php?topic=remove_custom_product
* **Remove Custom Property Definition** `removeCustomPropertyDefinition`: [Custom properties] RPC remove_custom_property_definition. Removes a custom resource, user or site property definition. Docs: https://www.planyo.com/api.php?topic=remove_custom_property_definition
* **Remove Notification Callback** `removeNotificationCallback`: [Notifications] RPC remove_notification_callback. Removes an existing webhook (HTTP notification callback). Pass the same notification_name and the exact callback_url used when registering; omitting callback_url removes ALL webhooks for that event. Accepted notification_name values are the same 30 listed on Add Notification Callback. Docs: https://www.planyo.com/api.php?topic=remove_notification_callback
* **Remove Pricing Manager Rule** `removePricingManagerRule`: [Prices] RPC remove_pricing_manager_rule. Deletes a Pricing Manager rule. Docs: https://www.planyo.com/api.php?topic=remove_pricing_manager_rule
* **Remove Product Image** `removeProductImage`: [Additional products] RPC remove_product_image. Removes an additional-product image by photo ID. Docs: https://www.planyo.com/api.php?topic=remove_product_image
* **Remove Reservation Payment** `removeReservationPayment`: [Reservations] RPC remove_reservation_payment. Deletes a payment from a reservation. Docs: https://www.planyo.com/api.php?topic=remove_reservation_payment
* **Remove Resource** `removeResource`: [Resources] RPC remove_resource. Removes an existing resource. WARNING: all existing reservations for the resource are removed too and this cannot be undone. Docs: https://www.planyo.com/api.php?topic=remove_resource
* **Remove Resource Image** `removeResourceImage`: [Resources] RPC remove_resource_image. Removes a resource image by photo ID. Docs: https://www.planyo.com/api.php?topic=remove_resource_image
* **Remove Resource Season** `removeResourceSeason`: [Seasons] RPC remove_resource_season. Removes a season by ID. Docs: https://www.planyo.com/api.php?topic=remove_resource_season
* **Remove Site Image** `removeSiteImage`: [Sites] RPC remove_site_image. Removes a site image by photo ID. Docs: https://www.planyo.com/api.php?topic=remove_site_image
* **Remove Site Moderator** `removeSiteModerator`: [Users] RPC remove_site_moderator. Removes the moderator role from a user. Docs: https://www.planyo.com/api.php?topic=remove_site_moderator
* **Remove Url From Admin Favorites** `removeUrlFromAdminFavorites`: [Sites] RPC remove_url_from_admin_favorites. Removes a URL from the backend favorites list. Docs: https://www.planyo.com/api.php?topic=remove_url_from_admin_favorites
* **Remove User** `removeUser`: [Users] RPC remove_user. Deletes an existing user (only possible when the user has no reservations). Docs: https://www.planyo.com/api.php?topic=remove_user
* **Remove Vacation** `removeVacation`: [Availability] RPC remove_vacation. Removes an existing vacation by ID. Docs: https://www.planyo.com/api.php?topic=remove_vacation
* **Remove Voucher** `removeVoucher`: [Coupons and vouchers] RPC remove_voucher. Removes a voucher. Docs: https://www.planyo.com/api.php?topic=remove_voucher
* **Reservation Search** `reservationSearch`: [Reservations] RPC reservation_search. Finds reservations containing the given search text. Docs: https://www.planyo.com/api.php?topic=reservation_search
* **Resource Search** `resourceSearch`: [Availability] RPC resource_search. Searches for available resources for a given time period. Docs: https://www.planyo.com/api.php?topic=resource_search
* **Search Reservations By Form Item** `searchReservationsByFormItem`: [Reservations] RPC search_reservations_by_form_item. Finds reservations whose form item has the given value. Docs: https://www.planyo.com/api.php?topic=search_reservations_by_form_item
* **Search Users By Custom Property** `searchUsersByCustomProperty`: [Users] RPC search_users_by_custom_property. Finds users whose custom user property has the given value. Docs: https://www.planyo.com/api.php?topic=search_users_by_custom_property
* **Send Email To Customer** `sendEmailToCustomer`: [Notifications] RPC send_email_to_customer. Sends an email message to the customer of a reservation. WARNING: this sends a real email to the reservation's customer address. Docs: https://www.planyo.com/api.php?topic=send_email_to_customer
* **Set Custom Properties** `setCustomProperties`: [Custom properties] RPC set_custom_properties. Sets values for up to 50 properties at once. Pass the value of each name as its own query parameter. Docs: https://www.planyo.com/api.php?topic=set_custom_properties
* **Set Custom Property** `setCustomProperty`: [Custom properties] RPC set_custom_property. Sets a new value for a custom property. Docs: https://www.planyo.com/api.php?topic=set_custom_property
* **Set Event Times** `setEventTimes`: [Resources] RPC set_event_times. Sets new times for an event-type resource. Docs: https://www.planyo.com/api.php?topic=set_event_times
* **Set Form Items From Csv** `setFormItemsFromCsv`: [Resources] RPC set_form_items_from_csv. Imports the reservation form for a resource from CSV. Docs: https://www.planyo.com/api.php?topic=set_form_items_from_csv
* **Set Package Contents** `setPackageContents`: [Resources] RPC set_package_contents. Makes a resource into a package and sets its package type and contents. Extra quantity_used_XXX / quantity_blocked_XXX / category_XXX params are documented at the docs URL. Docs: https://www.planyo.com/api.php?topic=set_package_contents
* **Set Payment Gateway** `setPaymentGateway`: [Sites] RPC set_payment_gateway. Sets the payment gateway used by a site or metasite. Docs: https://www.planyo.com/api.php?topic=set_payment_gateway
* **Set Product Usage For Reservation** `setProductUsageForReservation`: [Additional products] RPC set_product_usage_for_reservation. Adds or removes an additional product on a reservation (quantity 0 removes). Docs: https://www.planyo.com/api.php?topic=set_product_usage_for_reservation
* **Set Reservation Color** `setReservationColor`: [Reservations] RPC set_reservation_color. Sets a new colour for a reservation. Docs: https://www.planyo.com/api.php?topic=set_reservation_color
* **Set Reservation Notes** `setReservationNotes`: [Reservations] RPC set_reservation_notes. Sets new user and/or admin notes for a reservation. Docs: https://www.planyo.com/api.php?topic=set_reservation_notes
* **Set Reservation Price** `setReservationPrice`: [Prices] RPC set_reservation_price. Sets a custom price for a reservation. Docs: https://www.planyo.com/api.php?topic=set_reservation_price
* **Set Reservation Products** `setReservationProducts`: [Additional products] RPC set_reservation_products. Sets/resets the usage of all additional products on a reservation. Per-product params product_XXX / product_XXX_extra_field are documented at the docs URL. Docs: https://www.planyo.com/api.php?topic=set_reservation_products
* **Set Resource Admin** `setResourceAdmin`: [Users/Resources] RPC set_resource_admin. Sets a new resource administrator. Docs: https://www.planyo.com/api.php?topic=set_resource_admin
* **Set Resource Availability** `setResourceAvailability`: [Availability] RPC set_resource_availability. Sets availability in bulk for a number of dates. Per-date params are named timeYYYY-MM-DD (see docs). Docs: https://www.planyo.com/api.php?topic=set_resource_availability
* **Set Resource Daily Pricing** `setResourceDailyPricing`: [Prices] RPC set_resource_daily_pricing. Sets daily pricing values for a resource. Per-date price params are documented at the docs URL. Docs: https://www.planyo.com/api.php?topic=set_resource_daily_pricing
* **Set Resource Pricing** `setResourcePricing`: [Prices] RPC set_resource_pricing. Sets pricing rules for a resource. Per-rule params rule_price_type_XXX / rule_price_value_XXX are documented at the docs URL. Docs: https://www.planyo.com/api.php?topic=set_resource_pricing
* **Set Translation** `setTranslation`: [Translations] RPC set_translation. Adds or updates a text translation for a site, metasite or resource. Docs: https://www.planyo.com/api.php?topic=set_translation
* **Set Unit Names** `setUnitNames`: [Resource units] RPC set_unit_names. Sets the unit names of a resource; count must equal the resource quantity. Docs: https://www.planyo.com/api.php?topic=set_unit_names
* **Set Unit Property** `setUnitProperty`: [Resource units] RPC set_unit_property. Sets a custom unit property, optionally for a specific date/time. Docs: https://www.planyo.com/api.php?topic=set_unit_property
* **Set Weekly Schedule** `setWeeklySchedule`: [Availability] RPC set_weekly_schedule. Specifies the regular working / unavailable hours for a resource. Per-slot params are documented at the docs URL. Docs: https://www.planyo.com/api.php?topic=set_weekly_schedule

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Added to waiting list | `added_to_waitlist` | A reservation request was added to the waiting list. |
| Before/after event #1 | `before_or_after_event_1` | Custom 'before or after event' notification #1, configured in Settings / Email SMS notifications. |
| Before/after event #2 | `before_or_after_event_2` | Custom 'before or after event' notification #2, configured in Settings / Email SMS notifications. |
| Before/after event #3 | `before_or_after_event_3` | Custom 'before or after event' notification #3, configured in Settings / Email SMS notifications. |
| Before/after event #4 | `before_or_after_event_4` | Custom 'before or after event' notification #4, configured in Settings / Email SMS notifications. |
| Before/after event #5 | `before_or_after_event_5` | Custom 'before or after event' notification #5, configured in Settings / Email SMS notifications. |
| Before/after event #6 | `before_or_after_event_6` | Custom 'before or after event' notification #6, configured in Settings / Email SMS notifications. |
| Checked in | `checked_in` | A reservation status changed to checked-in. |
| Checked out | `checked_out` | A reservation status changed to checked-out. |
| Confirmed status cleared | `confirmed_cleared` | The 'confirmed' status of a reservation was cleared. |

<details>

<summary>See 20 more events</summary>

* **Coupon payment received** `coupon_payment_received`: An online payment for a coupon was received.
* **Hourly notification** `hourly`: Planyo's hourly notification tick.
* **New price quotation** `new_price_quotation`: A new price quotation was created.
* **New verified reservation** `new_verified_reservation`: A new reservation was entered and its email address was verified.
* **No show** `noshow`: A reservation status changed to no-show.
* **Reservation automatically cancelled** `reservation_auto_canceled`: Planyo auto-cancelled a reservation (e.g. unpaid past the deadline). Carries prev_status.
* **Reservation cancelled by admin** `reservation_admin_canceled`: A reservation was cancelled by an administrator. Carries prev_status.
* **Reservation cancelled by customer** `reservation_user_canceled`: A reservation was cancelled by the customer. Carries prev_status.
* **Reservation confirmed** `reservation_confirmed`: A reservation was confirmed by an administrator.
* **Reservation modified by admin** `reservation_admin_modified`: A reservation was modified by an administrator.
* **Reservation modified by customer** `reservation_user_modified`: A reservation was modified by the customer.
* **Reservation payment received** `reservation_payment_received`: An online payment for a reservation was received. Carries payment_amount, payment_mode, payment_time.
* **Reservation payment removed** `reservation_payment_removed`: An administrator removed a payment from a reservation.
* **Reservation price updated** `reservation_price_updated`: The price of an existing reservation changed.
* **Reservation products modified by customer** `reservation_products_user_modified`: The customer changed the additional products on a reservation.
* **Reservation removed** `reservation_removed`: A reservation was permanently deleted.
* **Resource removed** `resource_removed`: A resource was removed.
* **Resource settings changed** `resource_settings_changed`: Settings of a resource changed.
* **User added or updated** `user_updated`: A user was added or their settings were updated. Carries is_new_user.
* **Vacation added, removed or modified** `vacation_modified`: A vacation (blocked period) was added, removed or modified.

</details>
