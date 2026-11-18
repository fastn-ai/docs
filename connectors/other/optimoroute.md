---
description: "OptimoRoute Web Service API connector for route planning and delivery/field-service management: create/update/get/delete orders, plan and stop routing, get…"
hidden: true
---

# OptimoRoute

<img src="../../.gitbook/assets/connectors/lg/optimoroute.png" alt="OptimoRoute logo">

OptimoRoute Web Service API connector for route planning and delivery/field-service management: create/update/get/delete orders, plan and stop routing, get routes and scheduling info, completion details, mobile events, and driver parameter/position updates. Auth via API key passed as the `key` query parameter.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [optimoroute.com](https://optimoroute.com) |
| **Authentication** | API key |
| **Slug** | `optimoroute` |

## Use it

Add OptimoRoute from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.optimoroute.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create or Update Orders (Bulk) | `createOrUpdateOrders` | Create or Update Orders (POST /v1/create_or_update_orders). Creates, updates or replaces up to 500 orders in one call. Each order uses the Create Order fields plus operation (CREATE, UPDATE, SYNC, MERGE) and acceptDuplicateOrderNo. Unlike Create Order, the bulk call does not look up addresses: give location latitude and longitude (or an existing locationNo), and do not send acceptPartialMatch/acceptMultipleResults. Returns success (true if at least one worked) and a result per order. |
| Create Order | `createOrder` | Create Order (POST /v1/create_order). Creates, updates or replaces one order. operation: CREATE (new order, error if orderNo exists), UPDATE (change only the fields sent; needs orderNo or id), SYNC (create or replace), MERGE (create or update only the fields sent). For CREATE/SYNC/MERGE, date, type, location and orderNo or id are required. Location is either an address to geocode or latitude/longitude, or an existing locationNo. Returns success, the order id, the stored location and geocoding results. |
| Delete All Orders | `deleteAllOrders` | Delete All Orders (POST /v1/delete_all_orders). Deletes all orders and routes for one date. Careful: if date is left out, ALL orders in the account are deleted. Returns success, or code/message, and planningId if an optimization is running. |
| Delete Order | `deleteOrder` | Delete Order (POST /v1/delete_order). Deletes one order by its orderNo. forceDelete true ignores the usual limits on deleting orders that are on live routes. Returns success, or code/message on error, and planningId if an optimization is running for that order. |
| Delete Orders (Bulk) | `deleteOrders` | Delete Orders (POST /v1/delete_orders). Deletes up to 500 orders, each named by orderNo or id. deleteMultiple true deletes every order matching one orderNo (otherwise that is an error); forceDelete true ignores the limits on orders on live routes. Returns success (true if at least one was deleted) and a result per order. |
| Get Completion Details | `getCompletionDetails` | Get Order Completion (POST /v1/get_completion_details). Returns completion details for up to 500 orders, each named by orderNo or id: status (unscheduled, scheduled, on_route, servicing, success, failed, rejected, cancelled), start/end time and position, the Proof of Delivery form (notes, signature, photos, barcodes) and the tracking URL. Each order has its own success flag; a missing order comes back with success false and code ERR_ORD_NOT_FOUND. |
| Get Dispatch Status | `getDispatchStatus` | Get Dispatch Status (GET /v1/get_dispatch_status). Tells whether a date's routes and customer notifications were sent to drivers (not_sent, scheduled, sent), and whether they are the live routes. Without date it reports the live routes (date null if none). includeRouteChanges adds counts of routes added, changed or removed since sending. Needs no input, so it also works as a connection check. |
| Get Events | `getEvents` | Get Events (GET /v1/get_events). Returns driver app events for the live routes, oldest first, up to 500 per call: on_duty, off_duty, start_service, success, failed, rejected, start_route, end_route, start_time_changed. Pass the returned tag as after_tag to get only newer events. If no routes were sent to drivers, OptimoRoute answers success false with ERR_JOB_NO_ACTIVE_PLAN. |
| Get Orders | `getOrders` | Retrieve one or more orders by orderNo or id (max 500). POST /v1/get_orders. |
| Get Planning Status | `getPlanningStatus` | Get the status of a planning run. GET /v1/get_planning_status. status is N/R/C/F/E. |
| Get Routes | `getRoutes` | Get planned routes for a date, including drivers, stops and optional polyline. GET /v1/get_routes. |
| Get Scheduling Info | `getSchedulingInfo` | Get scheduling information (assigned driver, ETA, live estimate) for one order. GET /v1/get_scheduling_info. |
| Search Orders | `searchOrders` | Search Orders (POST /v1/search_orders). Find orders by a date range (at most 35 days) and/or a list of orders (orderNo or id, max 500), optionally filtered by status. Give at least one of dateRange or orders. Returns up to 500 orders per call; when after_tag comes back, call again with the same inputs plus that after_tag to get the next page. Set includeOrderData for full order data and includeScheduleInformation for driver/ETA info. |
| Send Routes | `sendRoutes` | Send Routes (POST /v1/send_routes). Sends a date's planned routes to the drivers' mobile app, making them the live routes. sendNotifications (default true) also sends the account's customer notifications; set it to false to send routes only. Returns success and the date, or code/message on error. |
| Start Planning | `startPlanning` | Start Planning (POST /v1/start_planning). Starts route optimization for a date (or a dateRange for weekly planning, then date is ignored). Options: balancing, starting from current routes with a lock type, depot trips, clustering, and limiting to some drivers or orders. Returns planningId to poll with Get Planning Status, or an error code with missingOrders / missingDrivers / ordersWithInvalidLocation. |
| Stop Planning | `stopPlanning` | Stop an in-progress planning run. POST /v1/stop_planning. |
| Update Driver Parameters | `updateDriverParameters` | Update Driver Parameters (POST /v1/update_driver_parameters). Changes one driver's settings for one date, found by the driver's external id: enabled, work time, assigned vehicle, vehicle capacities, start and end location. Fields left out stay unchanged. Start/end coordinates are used for all future optimizations. |
| Update Drivers Parameters (Bulk) | `updateDriversParameters` | Update Drivers Parameters (POST /v1/update_drivers_parameters). Changes settings for up to 500 driver-date pairs in one call. Each update names a driver by serial or externalId and a date, plus any of: enabled, workTime {from,to}, assignedVehicle, vehicle capacities, startLocation, endLocation. Fields left out stay unchanged. Returns success and a result per update. |
| Update Drivers Positions (Bulk) | `updateDriversPositions` | Update Drivers Positions (POST /v1/update_drivers_positions). Sends GPS positions for one or more drivers. Each update names a driver by serial or externalId and lists up to 100 positions (timestamp, latitude, longitude required; accuracy, speed, heading optional). One update per driver. Returns success and a result per driver. |
| Update Order Completion | `updateOrderCompletion` | Update Order Completion (POST /v1/update_completion_details). Sets the completion status of up to 500 orders, each named by orderNo or id, with optional start and end time. Status values: unscheduled, scheduled, on_route, servicing, success, failed, rejected, cancelled. The order must be on routes that were sent to drivers, otherwise OptimoRoute answers "order not part of any dispatch plan". Returns success and a result per order. |
