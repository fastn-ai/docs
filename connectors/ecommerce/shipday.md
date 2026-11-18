---
description: "Shipday delivery management API — delivery orders, takeout/pickup orders, drivers (carriers), order assignment and status, on-demand 3rd-party delivery, order…"
hidden: true
---

# Shipday

Shipday delivery management API — delivery orders, takeout/pickup orders, drivers (carriers), order assignment and status, on-demand 3rd-party delivery, order tracking progress, and partner/member endpoints.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [shipday.com](https://shipday.com) |
| **Authentication** | API key |
| **Actions** | 27 |
| **Events** | 14 |
| **Slug** | `shipday` |

## Use it

Add Shipday from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.shipday.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add a Carrier | `addCarrier` | Add a carrier (driver) to the Shipday account. WARNING: Shipday emails the address given an invitation to the driver app — only use addresses you control. Returns the created carrier including its carrierId. |
| Assign Order to Driver | `assignOrderToDriver` | Assign a delivery order to one of your own carriers (drivers). WARNING: this notifies the assigned driver in the Shipday driver app. Takes the numeric orderId and the carrierId. |
| Delete a Carrier | `deleteCarrier` | Remove a carrier (driver) from the Shipday account by numeric carrierId. |
| Delete Order | `deleteOrder` | Delete a delivery order by its numeric orderId. Returns a success envelope. |
| Delete Pickup Order | `deletePickupOrder` | Delete a takeout / pickup order by numeric orderId. |
| Edit Order | `editOrder` | Edit an existing delivery order by its numeric orderId. Requires the full order payload (orderNo, customer and restaurant fields). Returns the updated order. |
| Edit Pickup Order | `editPickupOrder` | Update a takeout / pickup order by numeric orderId. Requires the full payload (orderNumber, restaurant, customer); status may be IN_PROGRESS, READY, DONE or CANCEL. |
| Insert Order | `insertOrder` | Create a new delivery order in Shipday. Requires orderNumber, customer name/address/phone and restaurant (pickup) name/address. Returns success, a message and the new numeric orderId. |
| Insert Pickup Order | `insertPickupOrder` | Create a takeout / pickup order (customer collects in person, no driver). Requires orderNumber plus restaurant {name,address,phone} and customer {name,phone,email}. |
| On-Demand Assign | `onDemandAssign` | Dispatch an existing order to a named third-party delivery provider, usually after an estimate. WARNING: this books a real paid courier. Requires the 3rd-party delivery add-on. |
| On-Demand Availability | `onDemandAvailability` | Check which third-party on-demand delivery providers can serve a pickup/delivery address pair, with quotes. Requires the 3rd-party delivery add-on. |
| On-Demand Cancel | `onDemandCancel` | Cancel a third-party on-demand delivery previously assigned to an order. Requires the 3rd-party delivery add-on. |
| On-Demand Details | `onDemandDetails` | Get the third-party on-demand delivery details (provider, courier, fee, tracking) for an order. Requires the 3rd-party delivery add-on. |
| On-Demand Estimate | `onDemandEstimate` | Get third-party on-demand delivery quotes (fee and ETA per provider) for an existing Shipday order. Requires the 3rd-party delivery add-on. |
| On-Demand Services | `onDemandServices` | List the third-party on-demand delivery services (DoorDash Drive, Uber Direct, Roadie, ...) enabled for this Shipday account. Requires the 3rd-party delivery add-on. |
| Order Delivery Progress | `orderDeliveryProgress` | Public real-time delivery progress and ETA for an order, keyed by its trackingId (the token in the order's trackingLink). Requires the BUSINESS ADVANCED plan; rate limited to 3 requests/minute per trackingId. |
| Order Ready to Pickup | `orderReadyToPickup` | Flag an order as ready (or not ready) to be picked up, by numeric orderId. Sets the readyToPickup meta flag. |
| Order Status Update | `orderStatusUpdate` | Update the delivery state of an order by numeric orderId. status is one of ACTIVE, NOT_ACCEPTED, NOT_STARTED_YET, STARTED, PICKED_UP, ALREADY_DELIVERED, FAILED_DELIVERY, INCOMPLETE. |
| Orders Query | `ordersQuery` | Search delivery orders by time window, status and cursor. startTime/endTime must be local ISO date-time without a zone, e.g. 2026-09-01T00:00:00. Returns an array of order objects. |
| Partner Orders Query | `partnerOrdersQuery` | Partner API: search orders across a member company by time window, status, carrier or pickup location. Requires the Shipday Partner API Key auth method (PARTNER-API-KEY header). |
| Retrieve Active Orders | `retrieveActiveOrders` | List all currently active (not yet completed) delivery orders in the Shipday account. Returns an array of delivery order objects. |
| Retrieve Carriers | `retrieveCarriers` | List all carriers (drivers) in the Shipday account, with their id, name, email, phone and current status. |
| Retrieve Member Completed Orders (Partner) | `retrieveMemberOrders` | Partner API: list completed orders for one member company. Requires the Shipday Partner API Key auth method (PARTNER-API-KEY header). |
| Retrieve Members (Partner) | `retrieveMembers` | Partner API: list the member companies linked to a Shipday platform partner. Requires the Shipday Partner API Key auth method (PARTNER-API-KEY header), not an ordinary company API key. |
| Retrieve Order Details | `retrieveOrderDetails` | Get the full details of a delivery order by its order number. Returns an array containing the matching delivery order object(s). |
| Retrieve Pickup Order Details | `retrievePickupOrderDetails` | Get a takeout / pickup order by its numeric orderId. |
| Unassign Order from Driver | `unassignOrderFromDriver` | Remove the currently assigned carrier (driver) from a delivery order, by numeric orderId. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Driver Location Update (Beta) | `LOCATION_UPDATE` | Real-time driver latitude/longitude. BETA and NOT self-serve: Shipday staff must enable and configure this webhook for your account — contact Shipday support with the endpoint URL and an optional validation token (max 32 chars). It is not registrable from the dashboard. |
| Order Accepted and Started | `ORDER_ACCEPTED_AND_STARTED` | The driver accepted the order and started the delivery. Manual one-time setup: register the fastn webhook URL at https://dispatch.shipday.com/dashboard#accountInfo (Account Info, password-unlocked API section). |
| Order Assigned | `ORDER_ASSIGNED` | The order was assigned to a carrier (driver). Manual one-time setup: see Order Inserted — register the fastn webhook URL at https://dispatch.shipday.com/dashboard#accountInfo (Account Info, password-unlocked API section). |
| Order Completed | `ORDER_COMPLETED` | The order was delivered successfully. Manual one-time setup: register the fastn webhook URL at https://dispatch.shipday.com/dashboard#accountInfo (Account Info, password-unlocked API section). |
| Order Deleted | `ORDER_DELETE` | The order was deleted. Manual one-time setup: register the fastn webhook URL at https://dispatch.shipday.com/dashboard#accountInfo (Account Info, password-unlocked API section). |
| Order Failed | `ORDER_FAILED` | The delivery failed. Manual one-time setup: register the fastn webhook URL at https://dispatch.shipday.com/dashboard#accountInfo (Account Info, password-unlocked API section). |
| Order Incomplete | `ORDER_INCOMPLETE` | The order was marked incomplete. Manual one-time setup: register the fastn webhook URL at https://dispatch.shipday.com/dashboard#accountInfo (Account Info, password-unlocked API section). |
| Order Inserted | `ORDER_INSERTED` | A new delivery order was created. SETUP (manual, one-time): Shipday has no public webhook-registration API — sign in at https://dispatch.shipday.com/dashboard#accountInfo (Account Info), re-enter your account password to unlock the API section, paste the fastn webhook URL into the Webhook / callback URL field and save. All order events are then delivered to that single URL. |
| Order On The Way | `ORDER_ONTHEWAY` | The driver is en route to the customer. Manual one-time setup: register the fastn webhook URL at https://dispatch.shipday.com/dashboard#accountInfo (Account Info, password-unlocked API section). |
| Order On The Way Removed | `ORDER_ONTHEWAY_REMOVED` | The on-the-way state was reverted. Manual one-time setup: register the fastn webhook URL at https://dispatch.shipday.com/dashboard#accountInfo (Account Info, password-unlocked API section). |
| Order Picked Up | `ORDER_PIKEDUP` | The driver picked the order up (Shipday spells the event ORDER_PIKEDUP). Manual one-time setup: register the fastn webhook URL at https://dispatch.shipday.com/dashboard#accountInfo (Account Info, password-unlocked API section). |
| Order Picked Up Removed | `ORDER_PIKEDUP_REMOVED` | The picked-up state was reverted. Manual one-time setup: register the fastn webhook URL at https://dispatch.shipday.com/dashboard#accountInfo (Account Info, password-unlocked API section). |
| Order Unassigned | `ORDER_UNASSIGNED` | The carrier was removed from the order. Manual one-time setup: register the fastn webhook URL at https://dispatch.shipday.com/dashboard#accountInfo (Account Info, password-unlocked API section). |
| Proof of Delivery Uploaded | `ORDER_POD_UPLOAD` | A proof-of-delivery photo or signature was uploaded; see order.podUrls. Manual one-time setup: register the fastn webhook URL at https://dispatch.shipday.com/dashboard#accountInfo (Account Info, password-unlocked API section). |
